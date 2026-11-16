#!/usr/bin/env python3
"""Bedenine Yolculuk animasyonlu efektleri.

Söylenen kelimeyi görselleştiren kısa animasyonlar üretir (şeffaf PNG kare dizisi, 24 fps).
Türler:
  tik   : adaçayı yeşili daire büyüyerek gelir, beyaz onay işareti çizilir, kıvılcımlar saçılır
  odul  : altın kupa zıplayarak gelir, arkasında dönen ışık hüzmeleri ve konfeti
  hedef : hedef tahtası belirir, ok saplanır
  kalp  : kalp atarak belirir, küçük kalpler yükselir
  gunes : dönen ışınlı güneş
  su    : su damlası düşer, halka yayılır
  ay    : hilal ve parıldayan yıldızlar (uyku/akşam)
  yildiz: parlayan yıldız ve kıvılcımlar
  sihir : spiral çizen parıltılar ve yıldızlar (sihirli değnek, peri tozu)
  hediye: renkli ambalajlı hediye kutusu zıplar, sallanır, kapağı açılır; ışık ve konfeti fışkırır
Her efekt: giriş animasyonu + bekleme + çıkış (sure saniye toplam).

Kullanım (bedenine_video.py içinden çağrılır):
  render_effect(tur, klasor, boyut=360, sure=1.6, fps=24)
"""
import math, os, random
from PIL import Image, ImageChops, ImageDraw, ImageFilter, ImageFont

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


HEART = (226, 84, 92)
HEART_L = (255, 150, 160)
SKY = (110, 180, 230)
NIGHT = (70, 80, 140)


def _heart_poly(cx, cy, r, n=80):
    pts = []
    for i in range(n):
        a = 2 * math.pi * i / n
        x = 16 * math.sin(a) ** 3
        y = -(13 * math.cos(a) - 5 * math.cos(2 * a) - 2 * math.cos(3 * a) - math.cos(4 * a))
        pts.append((cx + x * r / 17, cy + y * r / 17))
    return pts


def frame_kalp(t, total, S):
    img = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    c = S / 2
    R = S * 0.30
    sc = ease_out_back(t / 0.30, s=2.0)
    beat = 1 + 0.07 * max(0, math.sin((t - 0.35) * 2 * math.pi * 1.6)) if t > 0.35 else 1
    r = R * sc * beat
    if r > 1:
        glow = Image.new("RGBA", (S, S), (0, 0, 0, 0))
        ImageDraw.Draw(glow).polygon(_heart_poly(c, c + S * 0.02, r * 1.25), fill=HEART_L + (120,))
        img.alpha_composite(glow.filter(ImageFilter.GaussianBlur(S * 0.04)))
        d = ImageDraw.Draw(img)
        d.polygon(_heart_poly(c, c + S * 0.02, r), fill=HEART + (255,))
        d.ellipse([c - r * 0.55, c - r * 0.42, c - r * 0.25, c - r * 0.18], fill=(255, 220, 225, 170))
    # small hearts floating up
    fp = (t - 0.3) / 1.2
    if 0 <= fp <= 1:
        rnd = random.Random(11)
        for i in range(5):
            x = c + rnd.uniform(-S * 0.38, S * 0.38)
            y = c + S * 0.25 - fp * S * rnd.uniform(0.35, 0.55)
            rr = S * rnd.uniform(0.035, 0.06)
            d.polygon(_heart_poly(x, y, rr), fill=HEART_L + (int(230 * (1 - fp)),))
    img = _shadow(img)
    a = _alpha_env(t, total)
    if a < 1:
        img.putalpha(img.split()[3].point(lambda v: int(v * a)))
    return img


def frame_gunes(t, total, S):
    img = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    c = S / 2
    sc = ease_out_back(t / 0.35)
    R = S * 0.17 * sc
    if R > 1:
        glow = Image.new("RGBA", (S, S), (0, 0, 0, 0))
        ImageDraw.Draw(glow).ellipse([c - R * 2.1, c - R * 2.1, c + R * 2.1, c + R * 2.1], fill=(255, 220, 120, 120))
        img.alpha_composite(glow.filter(ImageFilter.GaussianBlur(S * 0.06)))
        d = ImageDraw.Draw(img)
        rot = t * 0.8
        for i in range(12):
            a = rot + 2 * math.pi * i / 12
            r1, r2 = R * 1.35, R * (1.95 if i % 2 == 0 else 1.7)
            w = R * 0.22
            p1 = (c + r1 * math.cos(a - 0.12), c + r1 * math.sin(a - 0.12))
            p2 = (c + r2 * math.cos(a), c + r2 * math.sin(a))
            p3 = (c + r1 * math.cos(a + 0.12), c + r1 * math.sin(a + 0.12))
            d.polygon([p1, p2, p3], fill=GOLD + (255,))
        d.ellipse([c - R, c - R, c + R, c + R], fill=GOLD_L + (255,))
        d.ellipse([c - R * 0.82, c - R * 0.82, c + R * 0.82, c + R * 0.82], fill=(255, 205, 80, 255))
    img = _shadow(img, alpha=70)
    a = _alpha_env(t, total)
    if a < 1:
        img.putalpha(img.split()[3].point(lambda v: int(v * a)))
    return img


def frame_su(t, total, S):
    img = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    c = S / 2
    fall = ease_out(t / 0.35)
    cy = c - S * 0.3 * (1 - fall)
    r = S * 0.17
    if t > 0.02:
        pts = []
        for i in range(60):
            a = 2 * math.pi * i / 60
            x = r * math.sin(a) * (1 - 0.5 * (1 + math.cos(a)) / 2 * 0)
            y = -r * math.cos(a)
            if math.cos(a) > 0:
                k = math.cos(a)
                x *= (1 - k) ** 0.9
                y = -r * (0.3 + 1.6 * k)
            pts.append((c + x, cy + y))
        d.polygon(pts, fill=SKY + (255,))
        d.ellipse([c - r * 0.45, cy - r * 0.35, c - r * 0.15, cy + r * 0.1], fill=(255, 255, 255, 170))
    rp = (t - 0.35) / 0.8
    if 0 <= rp <= 1:
        for k in range(2):
            q = max(0, rp - k * 0.25)
            rr = S * (0.2 + 0.25 * ease_out(q))
            d.ellipse([c - rr, cy + r * 0.95 - rr * 0.22, c + rr, cy + r * 0.95 + rr * 0.22],
                      outline=SKY + (int(220 * (1 - q)),), width=max(2, int(S * 0.012)))
    img = _shadow(img)
    a = _alpha_env(t, total)
    if a < 1:
        img.putalpha(img.split()[3].point(lambda v: int(v * a)))
    return img


def _star(d, cx, cy, r, col, inner=0.45):
    pts = []
    for i in range(10):
        rr = r if i % 2 == 0 else r * inner
        a = -math.pi / 2 + i * math.pi / 5
        pts.append((cx + rr * math.cos(a), cy + rr * math.sin(a)))
    d.polygon(pts, fill=col)


def frame_ay(t, total, S):
    img = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    c = S / 2
    sc = ease_out_back(t / 0.35)
    R = S * 0.25 * sc
    if R > 1:
        moon = Image.new("RGBA", (S, S), (0, 0, 0, 0))
        md = ImageDraw.Draw(moon)
        md.ellipse([c - R, c - R, c + R, c + R], fill=(255, 236, 170, 255))
        cut = Image.new("L", (S, S), 0)
        ImageDraw.Draw(cut).ellipse([c - R * 0.55, c - R * 1.15, c + R * 1.45, c + R * 0.85], fill=255)
        moon.putalpha(ImageChops.subtract(moon.split()[3], cut))
        img.alpha_composite(_shadow(moon, alpha=80))
    d = ImageDraw.Draw(img)
    for i, (dx, dy, rr, ph) in enumerate([(0.28, -0.22, 0.05, 0.0), (0.33, 0.12, 0.035, 0.7), (0.12, -0.36, 0.03, 1.3)]):
        tw = 0.6 + 0.4 * math.sin((t - 0.3) * 7 + ph)
        if t > 0.25 + i * 0.1:
            _star(d, c + dx * S, c + dy * S, rr * S * tw, (255, 245, 200, 255))
    a = _alpha_env(t, total)
    if a < 1:
        img.putalpha(img.split()[3].point(lambda v: int(v * a)))
    return img


def frame_yildiz(t, total, S):
    img = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    c = S / 2
    sc = ease_out_back(t / 0.3, s=2.2)
    r = S * 0.30 * sc
    if r > 1:
        glow = Image.new("RGBA", (S, S), (0, 0, 0, 0))
        _star(ImageDraw.Draw(glow), c, c, r * 1.25, GOLD_L + (130,))
        img.alpha_composite(glow.filter(ImageFilter.GaussianBlur(S * 0.04)))
        d = ImageDraw.Draw(img)
        _star(d, c, c, r, GOLD + (255,))
        _star(d, c - r * 0.08, c - r * 0.1, r * 0.45, GOLD_L + (200,))
    sp = (t - 0.3) / 0.6
    if 0 <= sp <= 1:
        _sparkles(d, c, c, S * 0.28, ease_out(sp), 12, 5, GOLD_L, size=S * 0.02)
    img = _shadow(img)
    a = _alpha_env(t, total)
    if a < 1:
        img.putalpha(img.split()[3].point(lambda v: int(v * a)))
    return img


GIFT_BODY = (226, 72, 96)
GIFT_STRIPE = (255, 140, 160)
GIFT_DOT = (255, 214, 64)
GIFT_TEAL = (64, 178, 170)
RIBBON = (255, 200, 50)
RIBBON_D = (214, 150, 20)


def _wrapped_rect(w, h, seed=0):
    """Renkli desenli ambalaj kâğıdı ile kaplı dikdörtgen."""
    im = Image.new("RGBA", (w, h), GIFT_BODY + (255,))
    d = ImageDraw.Draw(im)
    st = max(6, w // 9)
    for x in range(-h, w + h, st * 3):  # çapraz şeritler
        d.polygon([(x, 0), (x + st, 0), (x + st - h, h), (x - h, h)], fill=GIFT_STRIPE + (255,))
    rnd = random.Random(seed)
    r = max(3, w // 30)
    for _ in range(max(8, int(h / 9))):
        x, y = rnd.uniform(0, w), rnd.uniform(0, h)
        col = GIFT_DOT if rnd.random() < 0.6 else GIFT_TEAL
        d.ellipse([x - r, y - r, x + r, y + r], fill=col + (255,))
    m = Image.new("L", (w, h), 0)
    ImageDraw.Draw(m).rounded_rectangle([0, 0, w - 1, h - 1], radius=max(4, w // 22), fill=255)
    im.putalpha(m)
    return im


def frame_hediye(t, total, S):
    img = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    c = S / 2
    # açılış zamanı
    t_open = 0.75
    # ışık hüzmeleri (kapak açılınca)
    op = ease_out((t - t_open) / 0.35)
    if op > 0:
        rays = Image.new("RGBA", (S, S), (0, 0, 0, 0))
        rd = ImageDraw.Draw(rays)
        oy = c - S * 0.02
        Rr = S * 0.55 * op
        rot = t * 0.7
        for i in range(10):
            a0 = -math.pi / 2 + (i - 4.5) * 0.22 + math.sin(rot + i) * 0.03
            a1 = a0 + 0.1
            rd.polygon([(c, oy), (c + Rr * math.cos(a0), oy + Rr * math.sin(a0)),
                        (c + Rr * math.cos(a1), oy + Rr * math.sin(a1))], fill=GOLD_L + (120,))
        glow = Image.new("RGBA", (S, S), (0, 0, 0, 0))
        ImageDraw.Draw(glow).ellipse([c - S * 0.22, oy - S * 0.14, c + S * 0.22, oy + S * 0.10], fill=(255, 240, 180, 200))
        img.alpha_composite(glow.filter(ImageFilter.GaussianBlur(S * 0.05)))
        img.alpha_composite(rays.filter(ImageFilter.GaussianBlur(2)))

    # kutu: zıplayarak gelir, sallanır
    sc = ease_out_back(t / 0.35, s=2.0)
    if sc > 0.02:
        bw, bh = int(S * 0.46), int(S * 0.34)
        lw, lh = int(S * 0.52), int(S * 0.11)
        box = Image.new("RGBA", (S, S), (0, 0, 0, 0))
        bx, by = int(c - bw / 2), int(c + S * 0.02)
        body = _wrapped_rect(bw, bh, 1)
        bd = ImageDraw.Draw(body)
        rbw = max(6, int(bw * 0.15))
        bd.rectangle([bw // 2 - rbw // 2, 0, bw // 2 + rbw // 2, bh], fill=RIBBON + (255,))
        bd.rectangle([bw // 2 + rbw // 2 - 3, 0, bw // 2 + rbw // 2, bh], fill=RIBBON_D + (255,))
        bd.rectangle([0, 0, bw, int(bh * 0.06)], fill=(0, 0, 0, 45))
        box.alpha_composite(body, (bx, by))
        # kapak + fiyonk (açılınca yukarı kalkar ve döner)
        lift = ease_out((t - t_open) / 0.3)
        lid = Image.new("RGBA", (lw, lh + int(S * 0.16)), (0, 0, 0, 0))
        lp = _wrapped_rect(lw, lh, 2)
        ld = ImageDraw.Draw(lp)
        ld.rectangle([lw // 2 - rbw // 2, 0, lw // 2 + rbw // 2, lh], fill=RIBBON + (255,))
        lid.alpha_composite(lp, (0, int(S * 0.16)))
        fd = ImageDraw.Draw(lid)
        cx0, cy0 = lw / 2, S * 0.16
        L = S * 0.13
        for k in (-1, 1):  # fiyonk halkaları
            fd.ellipse([cx0 + (k * L * 1.05) - L * 0.62, cy0 - L * 0.95, cx0 + (k * L * 1.05) + L * 0.62, cy0 - L * 0.05],
                       fill=RIBBON + (255,))
            fd.ellipse([cx0 + (k * L * 1.05) - L * 0.32, cy0 - L * 0.7, cx0 + (k * L * 1.05) + L * 0.32, cy0 - L * 0.3],
                       fill=RIBBON_D + (255,))
            fd.polygon([(cx0, cy0), (cx0 + k * L * 0.6, cy0 + L * 0.9), (cx0 + k * L * 0.25, cy0 + L * 0.9)], fill=RIBBON_D + (255,))
        fd.ellipse([cx0 - L * 0.3, cy0 - L * 0.55, cx0 + L * 0.3, cy0 - L * 0.05], fill=RIBBON + (255,))
        if lift > 0:
            lid = lid.rotate(-22 * lift, resample=Image.BICUBIC, expand=True)
        lx = int(c - lid.width / 2 + lift * S * 0.14)
        ly = int(by - lh - S * 0.16 - lift * S * 0.20)
        box.alpha_composite(lid, (lx, max(0, ly)))
        # sallanma (açılmadan önce)
        wob = math.sin((t - 0.35) * 30) * 6 * max(0, 1 - abs(t - 0.55) / 0.2) if 0.35 < t < t_open else 0
        if wob:
            box = box.rotate(wob, resample=Image.BICUBIC, center=(c, by + bh))
        box = _shadow(box, blur=10, off=(4, 8), alpha=110)
        if sc != 1:
            tw = max(1, int(S * sc))
            box = box.resize((tw, tw), Image.LANCZOS)
            img.alpha_composite(box, (int(c - tw / 2), int(c - tw / 2)))
        else:
            img.alpha_composite(box)

    # içinden fışkıran konfeti ve yıldızlar
    cp = (t - t_open) / 1.0
    if 0 <= cp <= 1:
        d = ImageDraw.Draw(img)
        rnd = random.Random(9)
        cols = [GOLD, (226, 72, 96), GIFT_TEAL, (120, 170, 255), (255, 255, 255)]
        oy = c - S * 0.02
        for i in range(26):
            ang = -math.pi / 2 + rnd.uniform(-0.9, 0.9)
            sp = rnd.uniform(0.35, 0.6) * S
            x = c + math.cos(ang) * sp * ease_out(cp)
            y = oy + math.sin(ang) * sp * ease_out(cp) + (cp ** 2) * S * 0.30
            col = rnd.choice(cols)
            a = int(255 * (1 - cp ** 1.5))
            if i % 5 == 0:
                _star(d, x, y, S * 0.03, col + (a,))
            else:
                s_ = S * 0.014
                rot = rnd.uniform(0, math.pi) + cp * 8
                pts = [(x + s_ * math.cos(rot + k * math.pi / 2) * (1.8 if k % 2 == 0 else 0.8),
                        y + s_ * math.sin(rot + k * math.pi / 2) * (1.8 if k % 2 == 0 else 0.8)) for k in range(4)]
                d.polygon(pts, fill=col + (a,))
    a = _alpha_env(t, total)
    if a < 1:
        img.putalpha(img.split()[3].point(lambda v: int(v * a)))
    return img


def frame_sihir(t, total, S):
    """Sihirli değnek / peri tozu: merkez etrafında spiral çizen, parıldayan küçük yıldızlar."""
    img = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    c = S / 2
    rnd = random.Random(21)
    cols = [GOLD_L, (255, 255, 255), (255, 200, 230), (200, 225, 255)]
    n = 34
    for i in range(n):
        delay = i / n * 0.6
        lt = t - delay
        if lt <= 0:
            continue
        life = min(1.0, lt / 1.1)
        ang = i * 0.55 + lt * 2.2
        rad = S * (0.12 + 0.36 * (i / n)) * (0.7 + 0.3 * ease_out(life))
        x = c + math.cos(ang) * rad
        y = c + math.sin(ang) * rad * 0.8 - lt * S * 0.05
        tw = 0.5 + 0.5 * math.sin(lt * 14 + i)
        size = S * rnd.uniform(0.012, 0.03) * (0.6 + 0.6 * tw) * (1 - life * 0.5)
        a = int(255 * (1 - life ** 2) * (0.6 + 0.4 * tw))
        col = rnd.choice(cols)
        if a <= 0 or size < 1:
            continue
        if i % 3 == 0:
            _star(d, x, y, size * 1.8, col + (a,), inner=0.35)
        else:
            d.ellipse([x - size, y - size, x + size, y + size], fill=col + (a,))
    glow = img.filter(ImageFilter.GaussianBlur(S * 0.012))
    out = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    out.alpha_composite(glow)
    out.alpha_composite(glow)
    out.alpha_composite(img)
    a = _alpha_env(t, total, fade_in=0.05, fade_out=0.35)
    if a < 1:
        out.putalpha(out.split()[3].point(lambda v: int(v * a)))
    return out


FRAMES = {"tik": frame_tik, "odul": frame_odul, "hedef": frame_hedef,
          "kalp": frame_kalp, "gunes": frame_gunes, "su": frame_su, "ay": frame_ay, "yildiz": frame_yildiz, "hediye": frame_hediye, "sihir": frame_sihir}


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
