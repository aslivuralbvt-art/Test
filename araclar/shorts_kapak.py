#!/usr/bin/env python3
"""Bedenine Yolculuk: 3 Shorts kapak seçeneği (A soru, B bölünmüş, C komut) + akış önizlemesi.

Kullanım:  python3 araclar/shorts_kapak.py videolar/tarifler/<ad>.json

Tarifte "shorts_kapak" bölümü:
{
  "yazi_y": 1060,                       # yazı bloğunun üst kenarı (yüz üstteyse 1000-1150)
  "A": {"kare": 2.4, "satirlar": [["OMUZLARIN", "b"], ["ÖNE Mİ", "b"], ["DÜŞÜYOR?", "s"]],
        "etiket": "3 ADIM · SABAH RİTÜELİ"},
  "B": {"ust_kare": 8.5, "alt_kare": 5.5, "ust_kirp": 150, "alt_kirp": 600,
        "serit": "SABAH RİTÜELİ", "satirlar": [["GÖĞÜS AÇMA", "b"]], "etiket": "3 ADIM"},
  "C": {"kare": 9.75, "satirlar": [["DUR.", "b"], ["GÖĞSÜNÜ AÇ.", "s"]], "etiket": "EVDEN ÇIKMADAN ÖNCE"}
}
Satır rengi: "b" beyaz, "s" sarı (#FFD640). Kare kaynağı yazısız 1080p video.
Çıktı: videolar/<ad>-shorts-kapak-A/B/C.jpg ve <ad>-shorts-kapak-onizleme.jpg
"""
import json, os, subprocess, sys, tempfile
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance

FD = "/usr/share/fonts/opentype/inter/"
W, H = 1080, 1920
WHITE = (255, 255, 255); YEL = (255, 214, 64); TERRA = (214, 98, 60)
CREAM = (248, 242, 232); DARK = (34, 30, 28)


def font(n, s): return ImageFont.truetype(FD + n, s)


def frame(video, t, tmp):
    p = os.path.join(tmp, f"f{t:.2f}.png")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", str(t), "-i", video, "-frames:v", "1", p], check=True)
    im = Image.open(p).convert("RGB")
    im = ImageEnhance.Contrast(ImageEnhance.Color(im).enhance(1.08)).enhance(1.04)
    return im.convert("RGBA")


def soft_dark(im, y0, maxa=215):
    """y0'dan sayfa sonuna kadar yumuşak karartma (kesik çizgi bırakmaz)."""
    g = Image.new("L", (1, H), 0)
    for y in range(H):
        if y > y0:
            x = (y - y0) / (H - y0)
            g.putpixel((0, y), int(maxa * (x * x * (3 - 2 * x)) ** 0.8))
    layer = Image.new("RGBA", (W, H), (12, 8, 6, 255))
    layer.putalpha(g.resize((W, H)))
    im.alpha_composite(layer)


def fit(text, maxw, start=190, mn=110):
    s = start
    d = ImageDraw.Draw(Image.new("L", (1, 1)))
    while s > mn:
        f = font("InterDisplay-Black.otf", s)
        if d.textlength(text, font=f) <= maxw: return f
        s -= 6
    return font("InterDisplay-Black.otf", mn)


def big_line(im, y, text, col, size=None):
    f = fit(text, W - 90, start=size or 190)
    lay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(lay).text((W / 2, y + 10), text, font=f, fill=(0, 0, 0, 170), anchor="ma",
                             stroke_width=10, stroke_fill=(0, 0, 0, 170))
    im.alpha_composite(lay.filter(ImageFilter.GaussianBlur(12)))
    ImageDraw.Draw(im).text((W / 2, y), text, font=f, fill=col, anchor="ma",
                            stroke_width=9, stroke_fill=DARK)
    b = f.getbbox(text)
    return y + (b[3] - b[1]) + 34


def pill(im, cy, text, fill, tc, size=46, pad=(36, 16)):
    d = ImageDraw.Draw(im)
    f = font("Inter-ExtraBold.otf", size)
    b = d.textbbox((0, 0), text, font=f)
    w, h = b[2] - b[0] + pad[0] * 2, b[3] - b[1] + pad[1] * 2
    x0, y0 = (W - w) / 2, cy - h / 2
    sh = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(sh).rounded_rectangle([x0, y0 + 6, x0 + w, y0 + h + 6], h / 2, fill=(0, 0, 0, 110))
    im.alpha_composite(sh.filter(ImageFilter.GaussianBlur(8)))
    d.rounded_rectangle([x0, y0, x0 + w, y0 + h], h / 2, fill=fill)
    d.text((W / 2, cy), text, font=f, fill=tc, anchor="mm")
    return y0 + h


def brand(im, kanal):
    pill(im, 70, kanal, CREAM + (235,), DARK, size=30, pad=(26, 12))


def block(im, y, satirlar, etiket, size=None):
    for txt, c in satirlar:
        y = big_line(im, y, txt, YEL if c == "s" else WHITE, size)
    if etiket:
        pill(im, y + 30, etiket, TERRA, WHITE)


def main():
    tarif = sys.argv[1]
    base = os.path.dirname(os.path.abspath(tarif))
    spec = json.load(open(tarif, encoding="utf-8"))
    out = os.path.normpath(os.path.join(base, spec.get("cikti_klasoru", "..")))
    ad = spec["ad"]; sk = spec["shorts_kapak"]; kanal = spec.get("kanal", "BEDENİNE YOLCULUK")
    video = os.path.join(out, f"{ad}-1080p.mp4")
    yy = sk.get("yazi_y", 1060)
    res = []
    with tempfile.TemporaryDirectory() as tmp:
        # A: soru + yüz
        a = sk["A"]; im = frame(video, a["kare"], tmp)
        soft_dark(im, yy - 260); brand(im, kanal); block(im, yy, a["satirlar"], a.get("etiket"))
        res.append(("A", im))
        # B: bölünmüş görüntü + sarı şerit
        b = sk["B"]; top = frame(video, b["ust_kare"], tmp); bot = frame(video, b["alt_kare"], tmp)
        im = Image.new("RGBA", (W, H))
        uk = b.get("ust_kirp", 150); ak = b.get("alt_kirp", 600)
        im.paste(top.crop((0, uk, W, uk + 960)), (0, 0)); im.paste(bot.crop((0, ak, W, ak + 960)), (0, 960))
        soft_dark(im, 900, 230)
        d = ImageDraw.Draw(im); d.rectangle([0, 952, W, 968], fill=YEL)
        brand(im, kanal)
        pill(im, 960, b["serit"], YEL, DARK, size=54, pad=(44, 18))
        block(im, 1050, b["satirlar"], b.get("etiket"))
        res.append(("B", im))
        # C: kısa komut
        c = sk["C"]; im = frame(video, c["kare"], tmp)
        soft_dark(im, yy - 260); brand(im, kanal); block(im, yy, c["satirlar"], c.get("etiket"), 210)
        res.append(("C", im))
    thumbs = []
    for k, im in res:
        p = os.path.join(out, f"{ad}-shorts-kapak-{k}.jpg")
        im.convert("RGB").save(p, quality=93); print(p)
        thumbs.append(im.convert("RGB").resize((240, 427), Image.LANCZOS))
    prev = Image.new("RGB", (240 * 3 + 40, 427 + 20), (24, 24, 24))
    for i, t in enumerate(thumbs): prev.paste(t, (10 + i * 250, 10))
    p = os.path.join(out, f"{ad}-shorts-kapak-onizleme.jpg"); prev.save(p, quality=90); print(p)


if __name__ == "__main__":
    main()
