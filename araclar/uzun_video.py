#!/usr/bin/env python3
"""Bedenine Yolculuk uzun video montajı ("benimle birlikte yap" rutini, 1920x1080).

Her bölüm: konuşma kısmı (orijinal ses) + hareketin sessiz döngüsü (geri sayım sayacıyla) +
"Sıradaki" önizlemesi. Bölümler arasında dinlenme ekranı. Baştan sona handpan müziği
(konuşmada kısılır). YouTube bölüm listesi otomatik çıkar.

Kullanım:  python3 araclar/uzun_video.py videolar/uzun-video/tarif.json
"""
import json, os, shutil, subprocess, sys, tempfile, wave

import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import bedenine_video as bv  # noqa: E402

W, H, FPS = 1920, 1080, 24
FD = "/usr/share/fonts/opentype/inter/"
SAGE = (138, 154, 123, 255)
DARK = (28, 36, 28)
CREAM = (245, 239, 230, 255)
WHITE = (255, 255, 255, 255)
TERRA = (214, 98, 60, 255)
ENH = ("hqdn3d=1.2:1.2:2.5:2.5,scale=1920:1080:force_original_aspect_ratio=increase:flags=lanczos,"
       "crop=1920:1080,cas=0.4,eq=contrast=1.06:brightness=0.012:saturation=1.05,vibrance=intensity=0.1")
NUM = "①②③④⑤⑥⑦⑧⑨"


def F(n, s):
    return ImageFont.truetype(FD + n, s)


def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        sys.exit(f"ffmpeg hatası:\n{r.stderr[-2500:]}")


def sure(p):
    return float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of",
                                 "csv=p=0", p], capture_output=True, text=True).stdout.strip())


def kart(yol, baslik, alt=None, rozet=None, x=70, y=70, buyuk=60):
    im = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    fb, fa = F("InterDisplay-ExtraBold.otf", buyuk), F("Inter-SemiBold.otf", int(buyuk * 0.55))
    bb = d.textbbox((0, 0), baslik, font=fb)
    ab = d.textbbox((0, 0), alt, font=fa) if alt else (0, 0, 0, 0)
    rz = int(buyuk * 1.25) if rozet else 0
    w = max(bb[2] - bb[0], ab[2] - ab[0]) + rz + (30 if rozet else 0) + 80
    h = (bb[3] - bb[1]) + ((ab[3] - ab[1]) + 16 if alt else 0) + 56
    sh = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(sh).rounded_rectangle([x + 6, y + 10, x + w + 6, y + h + 10], radius=30, fill=(0, 0, 0, 90))
    im.alpha_composite(sh.filter(ImageFilter.GaussianBlur(14)))
    d = ImageDraw.Draw(im)
    d.rounded_rectangle([x, y, x + w, y + h], radius=30, fill=(28, 36, 28, 170))
    tx = x + 40
    if rozet:
        cy = y + h // 2
        d.ellipse([tx, cy - rz // 2, tx + rz, cy + rz // 2], fill=SAGE)
        d.text((tx + rz // 2, cy), rozet, font=F("Inter-Black.otf", int(buyuk * 0.75)), fill=WHITE, anchor="mm")
        tx += rz + 30
    d.text((tx - bb[0], y + 28 - bb[1]), baslik, font=fb, fill=WHITE)
    if alt:
        d.text((tx - ab[0], y + 28 + (bb[3] - bb[1]) + 16 - ab[1]), alt, font=fa, fill=CREAM)
    im.save(yol)


def sayac(klasor, n, x=1640, y=800, r=150, etiket="saniye"):
    yollar = []
    for k in range(n, 0, -1):
        im = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        sh = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        ImageDraw.Draw(sh).ellipse([x - r + 6, y - r + 10, x + r + 6, y + r + 10], fill=(0, 0, 0, 100))
        im.alpha_composite(sh.filter(ImageFilter.GaussianBlur(14)))
        d = ImageDraw.Draw(im)
        d.ellipse([x - r, y - r, x + r, y + r], fill=(28, 36, 28, 200))
        lw = 14
        d.arc([x - r + lw, y - r + lw, x + r - lw, y + r - lw], 0, 360, fill=(255, 255, 255, 60), width=lw)
        d.arc([x - r + lw, y - r + lw, x + r - lw, y + r - lw], -90, -90 + 360 * k / n, fill=SAGE, width=lw)
        d.text((x, y - 10), str(k), font=F("InterDisplay-Black.otf", int(r * 0.95)), fill=WHITE, anchor="mm")
        d.text((x, y + r * 0.55), etiket, font=F("Inter-Bold.otf", int(r * 0.2)), fill=CREAM, anchor="mm")
        p = os.path.join(klasor, f"s{k:03d}.png")
        im.save(p)
        yollar.append(p)
    return yollar


def overlay_chain(inputs_start, katmanlar):
    """katmanlar: [(png, bas, bit)] → filtre zinciri (girişler inputs_start'tan itibaren)."""
    zincir, son = [], "v0"
    for i, (_, b, e) in enumerate(katmanlar):
        idx = inputs_start + i
        zincir.append(f"[{idx}]format=rgba,fade=t=in:st={b:.2f}:d=0.2:alpha=1,"
                      f"fade=t=out:st={max(e - 0.2, b):.2f}:d=0.2:alpha=1[k{i}]")
        zincir.append(f"[{son}][k{i}]overlay=enable='between(t,{b:.2f},{e:.2f})'[v{i + 1}]")
        son = f"v{i + 1}"
    return zincir, son


def segment(cikti, video_fc, sure_s, katmanlar, ses_girdisi=None, ses_fc=None, girisler=()):
    """video_fc: [v0] üreten filtre; katmanlar: overlay pngleri."""
    inp = list(girisler)
    n_in = sum(1 for x in inp if x == "-i")
    for png, b, e in katmanlar:
        inp += ["-loop", "1", "-t", f"{sure_s + 0.1:.2f}", "-framerate", str(FPS), "-i", png]
    zincir, son = overlay_chain(n_in, katmanlar)
    fc = video_fc + (";" + ";".join(zincir) if zincir else "") + f";[{son}]format=yuv420p[vout]"
    if ses_fc:
        fc += ";" + ses_fc
    else:
        fc += f";anullsrc=r=48000:cl=stereo,atrim=0:{sure_s:.3f}[aout]"
    run(["ffmpeg", "-v", "error", "-y", *inp, "-filter_complex", fc, "-map", "[vout]", "-map", "[aout]",
         "-t", f"{sure_s:.3f}", "-r", str(FPS), "-c:v", "libx264", "-preset", "medium", "-crf", "18",
         "-c:a", "aac", "-b:a", "192k", "-ar", "48000", cikti])


def hareket_dongusu(parcalar, hedef, cikti, gecis=0.3):
    """parcalar: [(dosya, bas, bit)] — sırayla ve tekrar ederek hedef süreye kadar çapraz geçişle birleştir."""
    seq, toplam, i = [], 0.0, 0
    while toplam < hedef + gecis:
        f, b, e = parcalar[i % len(parcalar)]
        seq.append((f, b, e))
        toplam += (e - b) - (gecis if seq[:-1] else 0)
        i += 1
    inp, fc = [], []
    for j, (f, b, e) in enumerate(seq):
        inp += ["-i", f]
        fc.append(f"[{j}:v]trim={b}:{e},setpts=PTS-STARTPTS,fps={FPS},{ENH},format=yuv420p[p{j}]")
    son, uz = "p0", seq[0][2] - seq[0][1]
    for j in range(1, len(seq)):
        fc.append(f"[{son}][p{j}]xfade=transition=fade:duration={gecis}:offset={uz - gecis:.3f}[x{j}]")
        son = f"x{j}"
        uz += (seq[j][2] - seq[j][1]) - gecis
    run(["ffmpeg", "-v", "error", "-y", *inp, "-filter_complex", ";".join(fc), "-map", f"[{son}]",
         "-t", f"{hedef:.3f}", "-c:v", "libx264", "-preset", "medium", "-crf", "16", cikti])


def zaman(s):
    s = int(round(s))
    return f"{s // 60}:{s % 60:02d}"


def main():
    tarif = sys.argv[1]
    base = os.path.dirname(os.path.abspath(tarif))
    t = json.load(open(tarif, encoding="utf-8"))
    yol = lambda p: p if os.path.isabs(p) else os.path.join(base, p)
    tmp = tempfile.mkdtemp(prefix="uzun_")
    segler, bolumler, konusma_araliklari, saat = [], [], [], 0.0
    hedef = float(t.get("hareket_suresi", 45))
    dinlen = float(t.get("dinlenme", 8))
    try:
        # --- giriş
        g = t["giris"]
        gs = sure(yol(g["dosya"]))
        kart(os.path.join(tmp, "baslik.png"), t["baslik"], t.get("alt_baslik"), y=760, buyuk=78)
        p = os.path.join(tmp, "seg_giris.mp4")
        segment(p, f"[0:v]{ENH}[v0]", gs, [(os.path.join(tmp, "baslik.png"), g.get("baslik_bas", 0.3), gs)],
                ses_fc="[0:a]aformat=sample_rates=48000:channel_layouts=stereo[aout]",
                girisler=["-i", yol(g["dosya"])])
        segler.append(p)
        bolumler.append((saat, "Giriş"))
        konusma_araliklari.append((saat, saat + g.get("konusma_bit", gs)))
        saat += gs

        hareketler = t["hareketler"]
        for i, h in enumerate(hareketler):
            no = NUM[i]
            ad = h["ad"]
            # konuşma kısmı
            ks = float(h["konusma_bit"])
            kp = os.path.join(tmp, f"k{i}.png")
            kart(kp, ad, h.get("talimat"), rozet=str(i + 1), buyuk=56)
            p = os.path.join(tmp, f"seg_{i}_a.mp4")
            segment(p, f"[0:v]trim=0:{ks},setpts=PTS-STARTPTS,fps={FPS},{ENH}[v0]", ks, [(kp, 0.3, ks + 0.2)],
                    ses_fc=f"[0:a]atrim=0:{ks},asetpts=PTS-STARTPTS,aformat=sample_rates=48000:channel_layouts=stereo,"
                           f"afade=t=out:st={max(ks - 0.25, 0):.2f}:d=0.25[aout]",
                    girisler=["-i", yol(h["dosya"])])
            bolumler.append((saat, f"{i + 1}. {ad}"))
            konusma_araliklari.append((saat, saat + ks))
            segler.append(p)
            saat += ks
            # hareket döngüsü + sayaç
            parca = [(yol(x["dosya"]), float(x["bas"]), float(x["bit"])) for x in h["hareket"]]
            dp = os.path.join(tmp, f"loop{i}.mp4")
            hareket_dongusu(parca, hedef, dp)
            sk = os.path.join(tmp, f"sayac{i}")
            os.makedirs(sk)
            n = int(hedef)
            kats = [(kp, 0, hedef)]
            for j, sp in enumerate(sayac(sk, n)):
                kats.append((sp, j, j + 1.0))
            if i + 1 < len(hareketler):
                sp_ = os.path.join(tmp, f"sira{i}.png")
                kart(sp_, f"Sıradaki: {hareketler[i + 1]['ad']}", None, y=940, x=70, buyuk=40)
                kats.append((sp_, hedef - 6, hedef))
            p = os.path.join(tmp, f"seg_{i}_b.mp4")
            segment(p, "[0:v]null[v0]", hedef, kats, girisler=["-i", dp])
            segler.append(p)
            saat += hedef
            # dinlenme
            if i + 1 < len(hareketler):
                rp = os.path.join(tmp, f"dinlen{i}.png")
                kart(rp, "Dinlen, derin nefes al", f"Sıradaki: {NUM[i + 1]} {hareketler[i + 1]['ad']}",
                     x=W // 2 - 520, y=H // 2 - 110, buyuk=72)
                son_kare = os.path.join(tmp, f"son{i}.png")
                run(["ffmpeg", "-v", "error", "-y", "-sseof", "-0.1", "-i", dp, "-frames:v", "1", son_kare])
                rk = os.path.join(tmp, f"rs{i}")
                os.makedirs(rk)
                kats = [(rp, 0, dinlen)] + [(sp, j, j + 1.0) for j, sp in enumerate(sayac(rk, int(dinlen), r=110))]
                p = os.path.join(tmp, f"seg_{i}_r.mp4")
                segment(p, f"[0:v]scale={W}:{H},boxblur=18:2,eq=brightness=-0.08[v0]", dinlen, kats,
                        girisler=["-loop", "1", "-t", f"{dinlen + 0.1}", "-framerate", str(FPS), "-i", son_kare])
                segler.append(p)
                saat += dinlen

        # --- kapanış
        k = t.get("kapanis")
        if k:
            ks_ = sure(yol(k["dosya"]))
            kp = os.path.join(tmp, "kapanis.png")
            kart(kp, "Abone ol, yarın sabah yine buradayız", "Bedenine Yolculuk", y=780, buyuk=56)
            p = os.path.join(tmp, "seg_kapanis.mp4")
            segment(p, f"[0:v]{ENH}[v0]", ks_, [(kp, k.get("kart_bas", 2.0), ks_)],
                    ses_fc="[0:a]aformat=sample_rates=48000:channel_layouts=stereo[aout]",
                    girisler=["-i", yol(k["dosya"])])
            segler.append(p)
            bolumler.append((saat, "Kapanış"))
            konusma_araliklari.append((saat, saat + k.get("konusma_bit", ks_)))
            saat += ks_

        # --- birleştir
        lst = os.path.join(tmp, "liste.txt")
        with open(lst, "w") as f:
            f.writelines(f"file '{s}'\n" for s in segler)
        ham = os.path.join(tmp, "ham.mp4")
        run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", lst, "-c", "copy", ham])
        toplam = sure(ham)

        # --- müzik + ses
        muz = os.path.join(tmp, "muzik.wav")
        bv.make_handpan(muz, toplam + 1.5, seed=t.get("muzik_tohum", 6), bpm=t.get("muzik_bpm", 72))
        cik = yol(t["cikti"])
        fc = ("[0:a]highpass=f=80,acompressor=threshold=-22dB:ratio=2.5:attack=10:release=150:makeup=2,"
              "aformat=sample_rates=48000:channel_layouts=stereo,asplit=2[ses][sc];"
              f"[1:a]volume={t.get('muzik_db', -4)}dB,atrim=0:{toplam:.3f},afade=t=out:st={toplam - 3:.2f}:d=3[m];"
              "[m][sc]sidechaincompress=threshold=0.05:ratio=4:attack=40:release=600[md];"
              "[ses][md]amix=inputs=2:duration=first:normalize=0,loudnorm=I=-14:TP=-1.5:LRA=11[a]")
        run(["ffmpeg", "-v", "error", "-y", "-i", ham, "-i", muz, "-filter_complex", fc, "-map", "0:v",
             "-map", "[a]", "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", cik])
        bolum_txt = "\n".join(f"{zaman(s)} {ad}" for s, ad in bolumler)
        with open(os.path.splitext(cik)[0] + "-bolumler.txt", "w", encoding="utf-8") as f:
            f.write(bolum_txt + "\n")
        print(cik)
        print(f"Süre: {zaman(toplam)}")
        print(bolum_txt)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


if __name__ == "__main__":
    main()
