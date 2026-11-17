#!/usr/bin/env python3
"""Bedenine Yolculuk kanal kimliği: YouTube banner (2560x1440) ve profil fotoğrafı (800x800).

Kullanım:
  python3 araclar/kanal_kimlik.py KISI_KESIM.png DOGA_KARESI.png CIKTI_KLASORU

KISI_KESIM.png : arka planı ayrılmış kişi (araclar/kisi_ayir.py ile), dikey video karesinden
DOGA_KARESI.png: arka plan yeşilliği için bahçe/ağaç içeren bir video karesi
"""
import math, os, random, sys
from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import efektler  # noqa: E402

FD = "/usr/share/fonts/opentype/inter/"
DARK = (38, 52, 38)
SAGE_D = (96, 118, 86)
CREAM = (247, 242, 232)
TERRA = (160, 72, 42)


def F(n, s):
    return ImageFont.truetype(FD + n, s)


def doga(w, h, kaynak, seed=3):
    src = Image.open(kaynak).convert("RGB")
    sw, sh = src.size
    agac = src.crop((0, 0, sw, int(sh * 0.20)))  # üst kısım: ağaçlar
    bg = agac.resize((w, h), Image.LANCZOS).filter(ImageFilter.GaussianBlur(max(w, h) / 75))
    bg = ImageEnhance.Brightness(ImageEnhance.Color(bg).enhance(1.25)).enhance(1.05).convert("RGBA")
    glow = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    ImageDraw.Draw(glow).ellipse([-w * 0.2, -h * 0.5, w * 0.6, h * 0.5], fill=(255, 240, 200, 120))
    bg.alpha_composite(glow.filter(ImageFilter.GaussianBlur(max(w, h) / 13)))
    rnd = random.Random(seed)
    bk = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    bd = ImageDraw.Draw(bk)
    for _ in range(int(w * h / 50000)):
        x, y = rnd.randrange(w), rnd.randrange(h)
        r = rnd.randrange(int(w / 180) + 4, int(w / 45) + 6)
        bd.ellipse([x - r, y - r, x + r, y + r], fill=(255, 250, 225, rnd.randrange(25, 70)))
    bg.alpha_composite(bk.filter(ImageFilter.GaussianBlur(6)))
    return bg


def kisi(kesim, ust_oran=0.0, alt_oran=0.42, sol=0.0, sag=1.0):
    p = Image.open(kesim).convert("RGBA")
    w, h = p.size
    p = p.crop((int(w * sol), int(h * ust_oran), int(w * sag), int(h * alt_oran)))
    rgb = p.convert("RGB").filter(ImageFilter.UnsharpMask(radius=2.2, percent=90, threshold=2))
    rgb = ImageEnhance.Contrast(rgb).enhance(1.05)
    rgb.putalpha(p.split()[3])
    return rgb


def yumusat_kenar(p, alt=0.30, yan=0.08):
    import numpy as np
    a = np.asarray(p.split()[3]).astype("float32") / 255
    hh, ww = a.shape
    yy = np.linspace(0, 1, hh)[:, None]
    xx = np.linspace(0, 1, ww)[None, :]
    a = a * np.clip((1 - yy) / alt, 0, 1) * np.clip(np.minimum(xx, 1 - xx) / yan, 0, 1)
    p = p.copy()
    p.putalpha(Image.fromarray((a * 255).astype("uint8")))
    return p


def golge_yapistir(img, p, xy, blur=20, alpha=90):
    sh = Image.new("RGBA", img.size, (0, 0, 0, 0))
    sh.paste((10, 20, 10, alpha), (xy[0] + 14, xy[1] + 16), p.split()[3])
    img.alpha_composite(sh.filter(ImageFilter.GaussianBlur(blur)))
    img.alpha_composite(p, xy)


def hale(img, cx, cy, r, renk=(255, 248, 228, 200), blur=70):
    h = Image.new("RGBA", img.size, (0, 0, 0, 0))
    ImageDraw.Draw(h).ellipse([cx - r, cy - r, cx + r, cy + r], fill=renk)
    img.alpha_composite(h.filter(ImageFilter.GaussianBlur(blur)))


def cip(img, x, y, ikon, metin, f):
    d = ImageDraw.Draw(img)
    b = d.textbbox((0, 0), metin, font=f)
    tw, th = b[2] - b[0], b[3] - b[1]
    H = th + 34
    isz = H + 18
    W = isz + tw + 40
    sh = Image.new("RGBA", img.size, (0, 0, 0, 0))
    ImageDraw.Draw(sh).rounded_rectangle([x + 4, y + 8, x + W + 4, y + H + 8], radius=H // 2, fill=(0, 0, 0, 60))
    img.alpha_composite(sh.filter(ImageFilter.GaussianBlur(8)))
    d = ImageDraw.Draw(img)
    d.rounded_rectangle([x, y, x + W, y + H], radius=H // 2, fill=CREAM + (235,))
    ic = efektler.FRAMES[ikon](0.9 if ikon != "tik" else 1.0, 1.9, isz)
    img.alpha_composite(ic, (x - 4, y + H // 2 - isz // 2))
    d.text((x + isz + 6 - b[0], y + (H - th) // 2 - b[1]), metin, font=f, fill=DARK)
    return W


def banner(kesim, doga_kare, cikti):
    W, H = 2560, 1440
    SX0, SY0 = (W - 1546) // 2, (H - 423) // 2
    SX1, SY1 = SX0 + 1546, SY0 + 423
    img = doga(W, H, doga_kare)
    # yazı arkası krem aydınlık
    m = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(m).rounded_rectangle([SX0 - 60, SY0 - 10, SX0 + 960, SY1 + 10], radius=220, fill=CREAM + (185,))
    img.alpha_composite(m.filter(ImageFilter.GaussianBlur(85)))
    # kişi (baş-omuz), güvenli alanın sağında
    p = yumusat_kenar(kisi(kesim, 0.04, 0.33, 0.10, 0.90), alt=0.42, yan=0.14)
    ph = 400
    p = p.resize((int(p.width * ph / p.height), ph), Image.LANCZOS)
    cx = SX1 - 290
    hale(img, cx, SY0 + 180, 230, renk=(255, 248, 228, 140))
    golge_yapistir(img, p, (cx - p.width // 2, SY0 + 12), alpha=50)
    d = ImageDraw.Draw(img)
    tx = SX0 + 40
    d.text((tx, SY0 + 22), "Ben Aslı  ·  Her gün yeni Shorts", font=F("Inter-ExtraBold.otf", 36), fill=TERRA)
    d.text((tx - 4, SY0 + 66), "Bedenine Yolculuk", font=F("InterDisplay-Black.otf", 112), fill=DARK)
    d.text((tx, SY0 + 196), "Mükemmel değil, sürdürülebilir.", font=F("Inter-SemiBold.otf", 40), fill=SAGE_D)
    f = F("Inter-Bold.otf", 30)
    x = tx
    for ikon, metin in (("gunes", "Sabah rutinleri"), ("kalp", "Mutluluk hormonları"), ("tik", "10 saniyede rahatla")):
        x += cip(img, x, SY0 + 290, ikon, metin, f) + 18
    img.convert("RGB").save(cikti, quality=92)
    img.convert("RGB").crop((SX0, SY0, SX1, SY1)).save(cikti.replace(".jpg", "-telefon.jpg"), quality=90)
    return img


def profil(kesim, doga_kare, cikti):
    S = 800
    img = doga(S, S, doga_kare, seed=7)
    p = kisi(kesim, 0.035, 0.33, 0.12, 0.88)
    ph = 760
    p = p.resize((int(p.width * ph / p.height), ph), Image.LANCZOS)
    p = yumusat_kenar(p, alt=0.12, yan=0.04)
    hale(img, S // 2, int(S * 0.40), int(S * 0.30), renk=(255, 248, 228, 110), blur=70)
    golge_yapistir(img, p, (S // 2 - p.width // 2, S - ph + 70), blur=14, alpha=70)
    img.convert("RGB").save(cikti, quality=95)
    # daire önizleme
    m = Image.new("L", (S, S), 0)
    ImageDraw.Draw(m).ellipse([0, 0, S - 1, S - 1], fill=255)
    o = Image.new("RGBA", (S, S), (24, 24, 24, 255))
    o.paste(img.convert("RGB"), (0, 0), m)
    o.convert("RGB").save(cikti.replace(".jpg", "-daire-onizleme.jpg"), quality=90)


if __name__ == "__main__":
    kes, dog, out = sys.argv[1:4]
    os.makedirs(out, exist_ok=True)
    banner(kes, dog, os.path.join(out, "kanal-banner-2560x1440.jpg"))
    profil(kes, dog, os.path.join(out, "profil-fotografi-800x800.jpg"))
    print(out)
