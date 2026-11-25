#!/usr/bin/env python3
"""Akşam videoları için sakin kapak: sıcak koyu tonlar, italik serif merak cümlesi, ince altın detaylar.

Kullanım:
  python3 araclar/aksam_kapak.py VIDEO SANIYE CIKTI --etiket "AKŞAM · 10 SANİYE" \
      --satirlar "Bunu kendine" "en son ne zaman" "söyledin?" [--vurgu 2] [--ay]
--vurgu: altın renkte yazılacak satırın sırası (1'den başlar, 0 = yok)
"""
import argparse, subprocess
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

W, H = 1080, 1920
KREM = (246, 236, 222)
ALTIN = (214, 176, 122)
KOYU = (34, 21, 15)
SERIF_I = "/usr/share/fonts/truetype/crosextra/Caladea-Italic.ttf"
SERIF_BI = "/usr/share/fonts/truetype/crosextra/Caladea-BoldItalic.ttf"
SANS = "/usr/share/fonts/opentype/inter/Inter-Medium.otf"


def kare(video, t):
    r = subprocess.run(["ffmpeg", "-v", "error", "-ss", str(t), "-i", video, "-frames:v", "1",
                        "-vf", f"scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H}",
                        "-f", "rawvideo", "-pix_fmt", "rgb24", "-"], capture_output=True, check=True)
    return Image.frombytes("RGB", (W, H), r.stdout)


def aralikli(d, xy, metin, font, renk, aralik):
    x, y = xy
    for ch in metin:
        d.text((x, y), ch, font=font, fill=renk)
        x += d.textlength(ch, font=font) + aralik


def aralikli_gen(d, metin, font, aralik):
    return sum(d.textlength(c, font=font) for c in metin) + aralik * (len(metin) - 1)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("video"); ap.add_argument("saniye", type=float); ap.add_argument("cikti")
    ap.add_argument("--etiket", default="AKŞAM · 10 SANİYE")
    ap.add_argument("--satirlar", nargs="+", required=True)
    ap.add_argument("--vurgu", type=int, default=0)
    ap.add_argument("--ay", action="store_true", help="etiketin üstüne ince hilal")
    a = ap.parse_args()

    img = kare(a.video, a.saniye)
    f = np.asarray(img).astype(np.float32)
    # sıcak, hafif koyu ton
    f = f * np.array([1.03, 0.97, 0.90]) * 0.92
    # vinyet
    yy, xx = np.mgrid[0:H, 0:W]
    r = np.sqrt(((xx - W / 2) / (W * 0.75)) ** 2 + ((yy - H * 0.38) / (H * 0.62)) ** 2)
    f *= np.clip(1.15 - 0.55 * r ** 2, 0.45, 1.0)[..., None]
    # alttan koyu kahve geçiş
    g = np.clip((yy - H * 0.48) / (H * 0.34), 0, 1) ** 1.3
    f = f * (1 - 0.88 * g[..., None]) + np.array(KOYU) * (0.88 * g[..., None])
    img = Image.fromarray(np.clip(f, 0, 255).astype(np.uint8))
    d = ImageDraw.Draw(img)

    # üst marka
    fs = ImageFont.truetype(SANS, 26)
    m = "BEDENİNE YOLCULUK"
    aralikli(d, ((W - aralikli_gen(d, m, fs, 6)) / 2, 70), m, fs, KREM + (0,), 6)

    # başlık satırları (italik serif)
    boy = 118 if max(len(s) for s in a.satirlar) <= 15 else 100
    fi = ImageFont.truetype(SERIF_I, boy)
    fb = ImageFont.truetype(SERIF_BI, boy)
    satir_h = int(boy * 1.08)
    toplam = satir_h * len(a.satirlar)
    y = H - 230 - toplam
    # etiket + ince çizgiler
    fe = ImageFont.truetype(SANS, 30)
    ew = aralikli_gen(d, a.etiket, fe, 5)
    ey = y - 92
    aralikli(d, ((W - ew) / 2, ey), a.etiket, fe, ALTIN, 5)
    d.line([(W / 2 - ew / 2 - 90, ey + 19), (W / 2 - ew / 2 - 26, ey + 19)], fill=ALTIN, width=2)
    d.line([(W / 2 + ew / 2 + 26, ey + 19), (W / 2 + ew / 2 + 90, ey + 19)], fill=ALTIN, width=2)
    if a.ay:
        cx, cy, rr = W / 2, ey - 58, 22
        d.ellipse([cx - rr, cy - rr, cx + rr, cy + rr], fill=ALTIN)
        d.ellipse([cx - rr + 11, cy - rr - 6, cx + rr + 11, cy + rr - 6], fill=tuple(img.getpixel((int(cx + 30), int(cy - 30)))))
    # yazıya hafif gölge
    golge = Image.new("L", (W, H), 0)
    gd = ImageDraw.Draw(golge)
    for i, s in enumerate(a.satirlar):
        font = fb if a.vurgu == i + 1 else fi
        tw = d.textlength(s, font=font)
        gd.text(((W - tw) / 2, y + i * satir_h + 4), s, font=font, fill=170)
    golge = golge.filter(ImageFilter.GaussianBlur(10))
    img = Image.composite(Image.new("RGB", (W, H), (15, 8, 5)), img, golge)
    d = ImageDraw.Draw(img)
    for i, s in enumerate(a.satirlar):
        font = fb if a.vurgu == i + 1 else fi
        renk = ALTIN if a.vurgu == i + 1 else KREM
        tw = d.textlength(s, font=font)
        d.text(((W - tw) / 2, y + i * satir_h), s, font=font, fill=renk)
    # alt ince çizgi
    d.line([(W / 2 - 40, H - 150), (W / 2 + 40, H - 150)], fill=ALTIN, width=2)
    img.save(a.cikti, quality=93)
    print(a.cikti)


if __name__ == "__main__":
    main()
