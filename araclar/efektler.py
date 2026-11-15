#!/usr/bin/env python3
"""Bedenine Yolculuk animasyonlu efektleri.

Söylenen kelimeyi görselleştiren kısa animasyonlar üretir (şeffaf PNG kare dizisi, 24 fps).
Türler:
  tik   : adaçayı yeşili daire büyüyerek gelir, beyaz onay işareti çizilir, kıvılcımlar saçılır
  odul  : altın kupa zıplayarak gelir, arkasında dönen ışık hüzmeleri ve konfeti
  hedef : hedef tahtası belirir, ok saplanır
Her efekt: giriş animasyonu + bekleme + çıkış (sure saniye toplam).

Kullanım (bedenine_video.py içinden çağrılır):
  render_effect(tur, klasor, boyut=360, sure=1.6, fps=24)
"""
import math, os, random
from PIL import Image, ImageDraw, ImageFilter, ImageFont

SAGE = (122, 150, 108)
SAGE_D = (92, 118, 82)
GOLD = (245, 190, 60)
GOLD_L = (255, 226, 120)
GOLD_D = (196, 136, 30)
TERRA = (214, 98, 60)
WHITE = (255, 255, 255)
FONT = "/usr/share/fonts/opentype/inter/InterDisplay-Black.otf"


def ease_out_back(t, s=1.70158):
    t = max(0.0, min(1.0, t)) - 1
    return t * t * ((s + 1) * t + s) + 1


def ease_out(t):
    t = max(0.0, min(1.0, t))
    return 1 - (1 - t) ** 3


def _alpha_env(t, total, fade_in=0.12, fade_out=0.25):
    if t < fade_in:
        return t / fade_in
    if t > total - fade_out:
        return max(0.0, (total - t) / fade_out)
    return 1.0


def _shadow(img, blur=14, off=(6, 10), alpha=110):
    a = img.split()[3].point(lambda v: v * alpha // 255)
    sh = Image.new("RGBA", img.size, (0, 0, 0, 0))
    sh.putalpha(a)
    sh = sh.filter(ImageFilter.GaussianBlur(blur))
    out = Image.new("RGBA", img.size, (0, 0, 0, 0))
    out.alpha_composite(sh, off)
    out.alpha_composite(img)
    return out


def _sparkles(d, cx, cy, r0, progress, n, seed, color, size=10):
    rnd = random.Random(seed)
    for i in range(n):
        ang = 2 * math.pi * i / n + rnd.uniform(-0.2, 0.2)
        dist = r0 + progress * rnd.uniform(60, 120)
        s = size * (1 - progress) * rnd.uniform(0.7, 1.3)
        if s <= 0.5:
            continue
        x, y = cx + math.cos(ang) * dist, cy + math.sin(ang) * dist
        d.ellipse([x - s, y - s, x + s, y + s], fill=color + (int(255 * (1 - progress)),))


def frame_tik(t, total, S):
    img = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    c = S / 2
    R = S * 0.30
    sc = ease_out_back(t / 0.30)
    r = R * sc
    if r > 1:
        d.ellipse([c - r, c - r, c + r, c + r], fill=SAGE + (255,))
        d.ellipse([c - r * 0.86, c - r * 0.86, c + r * 0.86, c + r * 0.86], outline=WHITE + (90,), width=max(2, int(S * 0.008)))
    # check stroke drawing between 0.15s and 0.5s
    p = ease_out((t - 0.15) / 0.35)
    pts = [(c - R * 0.48, c + R * 0.02), (c - R * 0.12, c + R * 0.38), (c + R * 0.52, c - R * 0.34)]
    seg1 = math.dist(pts[0], pts[1])
    seg2 = math.dist(pts[1], pts[2])
    L = (seg1 + seg2) * p
    w = int(S * 0.055)
    if L > 0:
        if L <= seg1:
            f = L / seg1
            end = (pts[0][0] + (pts[1][0] - pts[0][0]) * f, pts[0][1] + (pts[1][1] - pts[0][1]) * f)
            line = [pts[0], end]
        else:
            f = (L - seg1) / seg2
            end = (pts[1][0] + (pts[2][0] - pts[1][0]) * f, pts[1][1] + (pts[2][1] - pts[1][1]) * f)
            line = [pts[0], pts[1], end]
        d.line(line, fill=WHITE + (255,), width=w, joint="curve")
        for q in (line[0], line[-1]):
            d.ellipse([q[0] - w / 2, q[1] - w / 2, q[0] + w / 2, q[1] + w / 2], fill=WHITE + (255,))
    sp = (t - 0.45) / 0.5
    if 0 <= sp <= 1:
        _sparkles(d, c, c, R * 1.05, ease_out(sp), 10, 1, GOLD_L, size=S * 0.022)
    img = _shadow(img)
    a = _alpha_env(t, total)
    if a < 1:
        img.putalpha(img.split()[3].point(lambda v: int(v * a)))
    return img


def _trophy(S):
    """Altın kupa (S x S şeffaf)."""
    img = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    c = S / 2
    w = S * 0.40
    top = S * 0.24
    cup_h = S * 0.30
    # handles
    hw = int(S * 0.035)
    d.arc([c - w / 2 - S * 0.12, top + S * 0.02, c - w / 2 + S * 0.06, top + cup_h * 0.8], 90, 270, fill=GOLD_D + (255,), width=hw)
    d.arc([c + w / 2 - S * 0.06, top + S * 0.02, c + w / 2 + S * 0.12, top + cup_h * 0.8], 270, 90, fill=GOLD_D + (255,), width=hw)
    # cup body
    d.pieslice([c - w / 2, top - cup_h, c + w / 2, top + cup_h], 0, 180, fill=GOLD + (255,))
    d.rectangle([c - w / 2, top - 2, c + w / 2, top + S * 0.01], fill=GOLD + (255,))
    d.ellipse([c - w / 2, top - S * 0.035, c + w / 2, top + S * 0.035], fill=GOLD_L + (255,))
    # highlight
    d.pieslice([c - w * 0.36, top - cup_h * 0.75, c - w * 0.08, top + cup_h * 0.75], 100, 170, fill=(255, 245, 200, 170))
    # stem + base
    d.rectangle([c - S * 0.03, top + cup_h - S * 0.01, c + S * 0.03, top + cup_h + S * 0.10], fill=GOLD_D + (255,))
    d.rounded_rectangle([c - S * 0.14, top + cup_h + S * 0.09, c + S * 0.14, top + cup_h + S * 0.15], radius=int(S * 0.02), fill=GOLD + (255,))
    d.rounded_rectangle([c - S * 0.18, top + cup_h + S * 0.14, c + S * 0.18, top + cup_h + S * 0.20], radius=int(S * 0.02), fill=GOLD_D + (255,))
    # star on cup
    sr = S * 0.065
    scx, scy = c, top + cup_h * 0.42
    pts = []
    for i in range(10):
        rr = sr if i % 2 == 0 else sr * 0.45
        a = -math.pi / 2 + i * math.pi / 5
        pts.append((scx + rr * math.cos(a), scy + rr * math.sin(a)))
    d.polygon(pts, fill=WHITE + (235,))
    return img


_TROPHY_CACHE = {}


def frame_odul(t, total, S):
    img = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    c = S / 2
    # rotating rays
    rp = ease_out(t / 0.4)
    if rp > 0:
        rays = Image.new("RGBA", (S, S), (0, 0, 0, 0))
        rd = ImageDraw.Draw(rays)
        n = 12
        rot = t * 0.9
        Rr = S * 0.48 * rp
        for i in range(n):
            a0 = rot + 2 * math.pi * i / n
            a1 = a0 + math.pi / n * 0.6
            rd.polygon([(c, c), (c + Rr * math.cos(a0), c + Rr * math.sin(a0)), (c + Rr * math.cos(a1), c + Rr * math.sin(a1))], fill=GOLD_L + (110,))
        rays = rays.filter(ImageFilter.GaussianBlur(3))
        glow = Image.new("RGBA", (S, S), (0, 0, 0, 0))
        ImageDraw.Draw(glow).ellipse([c - S * 0.26, c - S * 0.26, c + S * 0.26, c + S * 0.26], fill=(255, 240, 180, 150))
        img.alpha_composite(glow.filter(ImageFilter.GaussianBlur(S * 0.06)))
        img.alpha_composite(rays)
    if S not in _TROPHY_CACHE:
        _TROPHY_CACHE[S] = _shadow(_trophy(S), blur=10, off=(4, 8), alpha=120)
    tr = _TROPHY_CACHE[S]
    sc = ease_out_back(t / 0.35, s=2.2)
    if sc > 0.02:
        tw = max(1, int(S * sc))
        trs = tr.resize((tw, tw), Image.LANCZOS)
        bob = math.sin(max(0, t - 0.35) * 5) * S * 0.01
        img.alpha_composite(trs, (int(c - tw / 2), int(c - tw / 2 + bob)))
    # confetti
    cp = (t - 0.2) / 1.0
    if 0 <= cp <= 1:
        rnd = random.Random(7)
        cols = [GOLD, TERRA, SAGE, (255, 255, 255)]
        for i in range(22):
            ang = rnd.uniform(-math.pi, 0)
            sp = rnd.uniform(0.5, 1.0) * S * 0.55
            x = c + math.cos(ang) * sp * ease_out(cp)
            y = c + math.sin(ang) * sp * ease_out(cp) + (cp ** 2) * S * 0.35
            s = S * 0.016
            col = rnd.choice(cols)
            rot = rnd.uniform(0, math.pi) + cp * 6
            pts = [(x + s * math.cos(rot + k * math.pi / 2) * (1.8 if k % 2 == 0 else 0.8),
                    y + s * math.sin(rot + k * math.pi / 2) * (1.8 if k % 2 == 0 else 0.8)) for k in range(4)]
            d.polygon(pts, fill=col + (int(255 * (1 - cp * 0.7)),))
    a = _alpha_env(t, total)
    if a < 1:
        img.putalpha(img.split()[3].point(lambda v: int(v * a)))
    return img


def frame_hedef(t, total, S):
    img = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    c = S / 2
    R = S * 0.30
    sc = ease_out_back(t / 0.30)
    cols = [TERRA, WHITE, TERRA, WHITE, TERRA]
    for i, col in enumerate(cols):
        rr = R * sc * (1 - i * 0.19)
        if rr > 1:
            d.ellipse([c - rr, c - rr, c + rr, c + rr], fill=col + (255,))
    # arrow flies in from upper right 0.3-0.55s
    p = ease_out((t - 0.30) / 0.25)
    if p > 0:
        ang = math.radians(-35)
        tip = (c + R * 0.02, c - R * 0.02)
        L = S * 0.30
        start_off = (1 - p) * S * 0.6
        tx = tip[0] + math.cos(ang) * start_off
        ty = tip[1] + math.sin(ang) * start_off
        tail = (tx + math.cos(ang) * L, ty + math.sin(ang) * L)
        d.line([(tx, ty), tail], fill=(60, 50, 40, 255), width=int(S * 0.022))
        # fletching
        for k in (-1, 1):
            fa = ang + k * 0.5
            d.line([tail, (tail[0] - math.cos(fa) * S * 0.06 + math.cos(ang) * S * 0.0, tail[1] - math.sin(fa) * S * 0.06)],
                   fill=SAGE_D + (255,), width=int(S * 0.02))
        # head
        hl = S * 0.05
        d.polygon([(tx - math.cos(ang) * hl * 0.3, ty - math.sin(ang) * hl * 0.3),
                   (tx + math.cos(ang + 0.45) * hl, ty + math.sin(ang + 0.45) * hl),
                   (tx + math.cos(ang - 0.45) * hl, ty + math.sin(ang - 0.45) * hl)], fill=(60, 50, 40, 255))
    sp = (t - 0.55) / 0.45
    if 0 <= sp <= 1:
        _sparkles(d, c, c, R * 0.4, ease_out(sp), 8, 3, GOLD_L, size=S * 0.02)
    img = _shadow(img)
    a = _alpha_env(t, total)
    if a < 1:
        img.putalpha(img.split()[3].point(lambda v: int(v * a)))
    return img


FRAMES = {"tik": frame_tik, "odul": frame_odul, "hedef": frame_hedef}


def render_effect(tur, klasor, boyut=360, sure=1.6, fps=24):
    os.makedirs(klasor, exist_ok=True)
    fn = FRAMES[tur]
    n = int(round(sure * fps))
    for i in range(n):
        fn(i / fps, sure, boyut).save(os.path.join(klasor, f"f{i:04d}.png"))
    return os.path.join(klasor, "f%04d.png"), n


if __name__ == "__main__":
    import sys
    out = sys.argv[1] if len(sys.argv) > 1 else "efekt_onizleme"
    for k in FRAMES:
        render_effect(k, os.path.join(out, k))
    print(out)
