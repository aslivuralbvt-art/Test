#!/usr/bin/env python3
"""Bedenine Yolculuk Shorts kapağı (1080x1920).

Videodan bir kare alır (görüntü iyileştirmesiyle), üstüne cesur başlık, etiket ve isteğe bağlı
efekt ikonu ekler. Kapak videonun başına EKLENMEZ; YouTube'da kapak olarak seçmek içindir.

Kullanım:
  python3 araclar/shorts_kapak.py VIDEO SANIYE CIKTI.jpg --etiket "3. AŞAMA · ENDORFİN" \
      --satir1 "NEDEN İYİ" --satir2 "HİSSEDİYORSUN?" --y 980 [--ikon kalp] [--ikon-x 880 --ikon-y 420]
"""
import argparse, os, subprocess, sys, tempfile
from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import bedenine_video as bv  # noqa: E402
import efektler  # noqa: E402

W, H = 1080, 1920
FD = "/usr/share/fonts/opentype/inter/"
YEL = (255, 214, 64)
WHITE = (255, 255, 255)
TERRA = (214, 98, 60)
DARK = (20, 26, 20)
CREAM = (245, 239, 230)


def F(n, s):
    return ImageFont.truetype(FD + n, s)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("video")
    ap.add_argument("saniye", type=float)
    ap.add_argument("cikti")
    ap.add_argument("--etiket", default="")
    ap.add_argument("--satir1", required=True)
    ap.add_argument("--satir2", default="")
    ap.add_argument("--y", type=int, default=980, help="başlığın dikey merkezi")
    ap.add_argument("--ikon", default="")
    ap.add_argument("--ikon-x", type=int, default=880)
    ap.add_argument("--ikon-y", type=int, default=420)
    ap.add_argument("--ikon-boyut", type=int, default=260)
    a = ap.parse_args()

    tmp = tempfile.mkdtemp()
    src = os.path.join(tmp, "f.png")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", str(a.saniye), "-i", a.video, "-vf",
                    f"{bv.ENHANCE}", "-frames:v", "1", src], check=True)
    im = Image.open(src).convert("RGB")
    im = ImageEnhance.Contrast(ImageEnhance.Color(im).enhance(1.1)).enhance(1.06).convert("RGBA")

    y = a.y
    band = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(band).rectangle([0, y - 260, W, y + 260], fill=(25, 18, 12, 120))
    im.alpha_composite(band.filter(ImageFilter.GaussianBlur(70)))

    def big(xy, t, f, fill, stroke=10):
        sh = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        ImageDraw.Draw(sh).text((xy[0] + 8, xy[1] + 12), t, font=f, fill=(0, 0, 0, 170), anchor="mm",
                                stroke_width=stroke, stroke_fill=(0, 0, 0, 170))
        im.alpha_composite(sh.filter(ImageFilter.GaussianBlur(10)))
        ImageDraw.Draw(im).text(xy, t, font=f, fill=fill, anchor="mm", stroke_width=stroke, stroke_fill=DARK)

    def fit(t, maxw, start, name="InterDisplay-Black.otf"):
        d = ImageDraw.Draw(Image.new("RGB", (9, 9)))
        s = start
        while True:
            f = F(name, s)
            b = d.textbbox((0, 0), t, font=f, stroke_width=10)
            if b[2] - b[0] <= maxw or s < 40:
                return f
            s -= 4

    def pill(cx, py, t, f, bg, fg, pad=(40, 18)):
        d = ImageDraw.Draw(im)
        b = d.textbbox((0, 0), t, font=f)
        w, h = b[2] - b[0], b[3] - b[1]
        x = cx - (w + 2 * pad[0]) // 2
        sh = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        ImageDraw.Draw(sh).rounded_rectangle([x + 6, py + 10, x + w + 2 * pad[0] + 6, py + h + 2 * pad[1] + 10],
                                             radius=(h + 2 * pad[1]) // 2, fill=(0, 0, 0, 120))
        im.alpha_composite(sh.filter(ImageFilter.GaussianBlur(10)))
        d = ImageDraw.Draw(im)
        d.rounded_rectangle([x, py, x + w + 2 * pad[0], py + h + 2 * pad[1]], radius=(h + 2 * pad[1]) // 2, fill=bg)
        d.text((x + pad[0] - b[0], py + pad[1] - b[1]), t, font=f, fill=fg)

    pill(W // 2, 50, "BEDENİNE YOLCULUK", F("Inter-Bold.otf", 30), CREAM + (230,), DARK, pad=(26, 12))
    if a.etiket:
        pill(W // 2, y - 210, a.etiket, F("Inter-ExtraBold.otf", 48), TERRA, WHITE)
    if a.satir2:
        big((W // 2, y - 20), a.satir1, fit(a.satir1, 1000, 170), WHITE)
        big((W // 2, y + 160), a.satir2, fit(a.satir2, 1000, 190), YEL)
    else:
        big((W // 2, y + 60), a.satir1, fit(a.satir1, 1000, 190), YEL)
    if a.ikon:
        fn = efektler.FRAMES[a.ikon]
        ic = fn(1.05 if a.ikon == "hediye" else 0.9, 1.9, a.ikon_boyut)
        im.alpha_composite(ic, (a.ikon_x - a.ikon_boyut // 2, a.ikon_y - a.ikon_boyut // 2))
    im.convert("RGB").save(a.cikti, quality=94)
    print(a.cikti)


if __name__ == "__main__":
    main()
