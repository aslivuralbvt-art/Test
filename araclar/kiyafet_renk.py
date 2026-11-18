#!/usr/bin/env python3
"""Videodaki kıyafetin rengini değiştirir (MediaPipe selfie_multiclass: sınıf 4 = kıyafet).

Kumaşın gölge ve kıvrımları korunur: her pikselin parlaklığı hedef renge oranlanır.
Ten, saç, yüz, arka plan değişmez. Maske kareler arasında yumuşatılır (titreme olmasın).

Kullanım:
  python3 araclar/kiyafet_renk.py GIRDI.mp4 CIKTI.mp4 --renk bordo [--model selfie_multiclass.tflite]
Renkler: bordo, mavi, toprak, yesil, ya da "R,G,B"
"""
import argparse, json, os, subprocess, sys
import numpy as np

RENKLER = {
    "bordo": (84, 20, 34),
    "mavi": (92, 128, 168),
    "toprak": (176, 92, 62),
    "yesil": (138, 154, 123),
}
MODEL_URL = ("https://storage.googleapis.com/mediapipe-models/image_segmenter/"
             "selfie_multiclass_256x256/float32/latest/selfie_multiclass_256x256.tflite")


def probe(p):
    r = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries",
                        "stream=width,height,r_frame_rate", "-of", "json", p], capture_output=True, text=True)
    s = json.loads(r.stdout)["streams"][0]
    n, d = s["r_frame_rate"].split("/")
    return s["width"], s["height"], float(n) / float(d)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("girdi")
    ap.add_argument("cikti")
    ap.add_argument("--renk", default="bordo")
    ap.add_argument("--model", default=os.path.expanduser("~/.cache/selfie_multiclass_256x256.tflite"))
    ap.add_argument("--yumusatma", type=float, default=0.6, help="maske zaman yumuşatma (0-1)")
    a = ap.parse_args()

    if not os.path.exists(a.model):
        os.makedirs(os.path.dirname(a.model), exist_ok=True)
        subprocess.run(["curl", "-sSfLo", a.model, MODEL_URL], check=True)

    import mediapipe as mp
    from mediapipe.tasks.python import vision, BaseOptions
    from PIL import Image, ImageFilter

    hedef = np.array(RENKLER.get(a.renk) or [int(x) for x in a.renk.split(",")], dtype=np.float32)
    w, h, fps = probe(a.girdi)
    seg = vision.ImageSegmenter.create_from_options(vision.ImageSegmenterOptions(
        base_options=BaseOptions(model_asset_path=a.model), output_confidence_masks=True))

    dec = subprocess.Popen(["ffmpeg", "-v", "error", "-i", a.girdi, "-f", "rawvideo", "-pix_fmt", "rgb24", "-"],
                           stdout=subprocess.PIPE)
    tmpv = a.cikti + ".video.mp4"
    enc = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{w}x{h}",
                            "-r", f"{fps}", "-i", "-", "-c:v", "libx264", "-crf", "15", "-preset", "slow",
                            "-pix_fmt", "yuv420p", tmpv], stdin=subprocess.PIPE)
    onceki = None
    ref_l = None
    n = 0
    while True:
        buf = dec.stdout.read(w * h * 3)
        if len(buf) < w * h * 3:
            break
        fr = np.frombuffer(buf, np.uint8).reshape(h, w, 3)
        res = seg.segment(mp.Image(image_format=mp.ImageFormat.SRGB, data=np.ascontiguousarray(fr)))
        def buyut(c, blur, kapat=0):
            x = np.squeeze(res.confidence_masks[c].numpy_view()).astype(np.float32)
            xi = Image.fromarray((np.clip(x, 0, 1) * 255).astype(np.uint8))
            if kapat:  # maskedeki delikleri kapat (dilate + erode)
                xi = xi.filter(ImageFilter.MaxFilter(kapat)).filter(ImageFilter.MinFilter(kapat))
            xi = xi.resize((w, h), Image.BILINEAR)
            return np.asarray(xi.filter(ImageFilter.GaussianBlur(blur))).astype(np.float32) / 255
        kiyafet = np.clip((buyut(4, 2.0, kapat=11) - 0.25) / 0.5, 0, 1)
        kisi = np.clip((1 - buyut(0, 6.0) - 0.15) / 0.3, 0, 1)  # kişi bölgesi
        # renk kapısı: adaçayı yeşili tonu (H 45-95°), ten/saç/yatak (H 20-40°) dışarıda kalır
        hsv = np.asarray(Image.fromarray(fr).convert("HSV")).astype(np.float32)
        H = hsv[..., 0] * (360 / 255)
        Sa = hsv[..., 1] / 255
        def bulanik(x, r):
            return np.asarray(Image.fromarray((np.clip(x, 0, 1) * 255).astype(np.uint8))
                              .filter(ImageFilter.GaussianBlur(r))).astype(np.float32) / 255
        V = hsv[..., 2] / 255
        ton_dar = np.clip((110 - H) / 10, 0, 1)
        notr = np.clip((0.14 - Sa) / 0.06, 0, 1)  # gri gölge/ışık: tonu güvenilmez, kıyafet içinde boya
        parlak_degil = np.clip((0.80 - V) / 0.08, 0, 1)  # beyaz çarşaf/perde dışarıda
        gevsek = bulanik(np.maximum(np.clip((H - 33) / 6, 0, 1) * ton_dar, notr) * parlak_degil, 3.0)  # kıyafet maskesi içinde: sadece ten/yatak tonunu at
        siki = bulanik(np.clip((H - 37) / 5, 0, 1) * ton_dar * np.clip((Sa - 0.05) / 0.05, 0, 1) * np.clip((0.90 - V) / 0.06, 0, 1), 2.0)  # maske dışı uzatma
        m = np.maximum(kiyafet * gevsek, kisi * siki)
        m = bulanik(m, 1.5)
        if onceki is not None:
            m = a.yumusatma * onceki + (1 - a.yumusatma) * m
        onceki = m
        f = fr.astype(np.float32)
        lum = 0.299 * f[..., 0] + 0.587 * f[..., 1] + 0.114 * f[..., 2]
        if ref_l is None:
            sel = m > 0.6
            ref_l = float(np.median(lum[sel])) if sel.any() else 140.0
        oran = (lum / max(ref_l, 1.0))[..., None]
        yeni = np.clip(hedef[None, None, :] * np.clip(oran, 0.12, 2.2), 0, 255)  # gölgeleri koru
        out = f * (1 - m[..., None]) + yeni * m[..., None]
        enc.stdin.write(out.astype(np.uint8).tobytes())
        n += 1
    enc.stdin.close()
    enc.wait()
    dec.wait()
    # orijinal sesi geri ekle
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", tmpv, "-i", a.girdi, "-map", "0:v", "-map", "1:a?",
                    "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-shortest", a.cikti], check=True)
    os.remove(tmpv)
    print(f"{a.cikti} · {n} kare · renk {tuple(int(x) for x in hedef)} · kumaş ref parlaklık {ref_l:.0f}")


if __name__ == "__main__":
    main()
