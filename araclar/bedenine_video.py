#!/usr/bin/env python3
"""Bedenine Yolculuk video düzenleyici.

Bir AI videosunu kanalın standart tarzına göre düzenler:
  1. Görüntü: 1080x1920'ye büyütme, hafif gürültü azaltma, keskinlik, ışık/renk
  2. Müzik: her video için sıfırdan üretilen, telifsiz, yumuşak arka plan müziği
  3. Ses: konuşma varsa müzik konuşmanın altında kısılır (ducking), -14 LUFS
  4. Ekran yazıları: hook, numaralı poz kartları, CTA (zamanlı, yumuşak geçişli)
  5. Kapaklar: dikey 1080x1920 ve yatay 1280x720
  6. Açıklama metni (tarifte verildiyse)

Kullanım:
  python3 araclar/bedenine_video.py videolar/tarifler/ornek.json
  python3 araclar/bedenine_video.py TARIF.json --kareler   # sadece zaman çizelgesi kareleri

Tarif (JSON) alanları için videolar/tarifler/asli-havuz-yoga.json örneğine bakın.
Gerekenler: ffmpeg, numpy, Pillow.
"""
import argparse, json, os, shutil, subprocess, sys, tempfile, wave

import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageEnhance, ImageFont

W, H = 1080, 1920
FONT_DIR = "/usr/share/fonts/opentype/inter/"
SAGE = (138, 154, 123, 255)
DARK = (47, 58, 47, 255)
CREAM = (245, 239, 230, 255)
WHITE = (255, 255, 255, 255)
CARD = (28, 36, 28, 165)

# Görüntü iyileştirme zinciri (havuz yoga videosunda test edildi)
ENHANCE = (
    "hqdn3d=1.2:1.2:2.5:2.5,"
    "scale=1080:1920:force_original_aspect_ratio=increase:flags=lanczos,crop=1080:1920,"
    "cas=0.45,"
    "eq=contrast=1.07:brightness=0.015:saturation=1.06:gamma=1.02,"
    "vibrance=intensity=0.12,"
    "curves=master='0/0 0.25/0.23 0.75/0.78 1/1'"
)


def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        sys.exit(f"Komut başarısız: {' '.join(cmd[:6])}...\n{r.stderr[-2000:]}")
    return r


def font(name, size):
    return ImageFont.truetype(FONT_DIR + name, size)


def probe(path):
    r = run(["ffprobe", "-v", "error", "-show_entries", "format=duration:stream=codec_type",
             "-of", "json", path])
    info = json.loads(r.stdout)
    dur = float(info["format"]["duration"])
    has_audio = any(s["codec_type"] == "audio" for s in info["streams"])
    return dur, has_audio


# ---------------------------------------------------------------- müzik
PROGRESSIONS = [
    [[53, 57, 60, 64], [52, 55, 59, 64], [45, 57, 60, 64], [43, 55, 59, 62]],  # Fmaj7 C/E Am7 G6
    [[48, 55, 59, 64], [45, 55, 60, 64], [41, 57, 60, 65], [43, 55, 59, 62]],  # Cmaj7 Am7 Fmaj7 G
    [[50, 57, 60, 65], [43, 55, 59, 62], [48, 55, 60, 64], [45, 57, 60, 64]],  # Dm7 G C Am7
    [[45, 55, 60, 64], [41, 57, 60, 64], [48, 55, 59, 64], [43, 55, 59, 62]],  # Am7 Fmaj7 Cmaj7 G
]


def make_music(path, dur, seed=0, bpm=96):
    """Yumuşak pad + elektrikli piyano arpeji + bas. Tamamen kodla üretilir (telifsiz)."""
    sr = 48000
    n = int(sr * dur)
    out = np.zeros((n, 2))
    rng = np.random.default_rng(seed)
    prog = PROGRESSIONS[seed % len(PROGRESSIONS)]
    seg = 2.5
    nseg = int(np.ceil(dur / seg)) + 1
    chords = [prog[i % len(prog)] for i in range(nseg)]

    def midi(m):
        return 440 * 2 ** ((m - 69) / 12)

    def env(length, a, r):
        e = np.ones(length)
        ai = min(int(a * sr), length // 2)
        ri = min(int(r * sr), length // 2)
        e[:ai] = np.linspace(0, 1, ai) ** 2
        e[length - ri:] *= np.linspace(1, 0, ri) ** 2
        return e

    for i, ch in enumerate(chords):  # pad
        s = int(i * seg * sr)
        L = min(int((seg + 1.2) * sr), n - s)
        if L <= 0:
            continue
        tt = np.arange(L) / sr
        e = env(L, 0.9, 1.1)
        for k, m in enumerate(ch):
            f = midi(m + 12)
            for det, pan in ((-0.12, 0.3), (0.12, 0.7)):
                ff = f * 2 ** (det / 120)
                w = (np.sin(2 * np.pi * ff * tt) + 0.25 * np.sin(4 * np.pi * ff * tt)
                     + 0.08 * np.sin(6 * np.pi * ff * tt))
                w *= e * 0.045 * (1 + 0.1 * np.sin(2 * np.pi * 0.3 * tt + k))
                out[s:s + L, 0] += w * (1 - pan)
                out[s:s + L, 1] += w * pan

    step = 60 / bpm / 2  # arpej
    pattern = [[0, 1, 2, 3, 2, 1], [0, 2, 1, 3, 2, 1], [3, 2, 1, 2, 0, 1]][seed % 3]
    idx, tpos = 0, 0.0
    while tpos < dur - 1.2:
        ch = chords[min(int(tpos // seg), len(chords) - 1)]
        f = midi(ch[pattern[idx % len(pattern)]] + 24)
        s = int(tpos * sr)
        L = min(int(1.6 * sr), n - s)
        tt = np.arange(L) / sr
        dec = np.exp(-tt * 3.2) * (1 - np.exp(-tt * 400))
        w = (np.sin(2 * np.pi * f * tt) + 0.3 * np.sin(4 * np.pi * f * tt) * np.exp(-tt * 6)
             + 0.1 * np.sin(6 * np.pi * f * tt) * np.exp(-tt * 9)) * dec
        vel = 0.05 * (0.85 + 0.3 * rng.random())
        pan = 0.35 + 0.3 * ((idx % 4) / 3)
        out[s:s + L, 0] += w * vel * (1 - pan)
        out[s:s + L, 1] += w * vel * pan
        idx += 1
        tpos += step

    for i, ch in enumerate(chords):  # bas
        s = int(i * seg * sr)
        L = min(int((seg + 0.3) * sr), n - s)
        if L <= 0:
            continue
        tt = np.arange(L) / sr
        root = ch[0] - 12 if ch[0] > 48 else ch[0]
        out[s:s + L] += (np.sin(2 * np.pi * midi(root) * tt) * env(L, 0.15, 0.6) * 0.06)[:, None]

    fi, fo = int(0.8 * sr), int(2.0 * sr)
    out[:fi] *= np.linspace(0, 1, fi)[:, None]
    out[-fo:] *= np.linspace(1, 0, fo)[:, None]
    out /= np.max(np.abs(out)) * 1.12
    dry = path + ".dry.wav"
    with wave.open(dry, "wb") as w:
        w.setnchannels(2)
        w.setsampwidth(2)
        w.setframerate(sr)
        w.writeframes((out * 32767).astype("<i2").tobytes())
    run(["ffmpeg", "-v", "error", "-y", "-i", dry, "-af",
         "aecho=0.8:0.6:60|120|240:0.35|0.25|0.15,lowpass=f=9000,highpass=f=50,"
         "loudnorm=I=-18:TP=-2:LRA=7", "-ar", "48000", path])
    os.remove(dry)


def make_handpan(path, dur, seed=0, bpm=84):
    """Handpan tarzı müzik (D Kurd dizisi): yumuşak metalik vuruşlar, uzun rezonans. Telifsiz, kodla üretilir."""
    sr = 48000
    n = int(sr * dur)
    out = np.zeros((n, 2))
    rng = np.random.default_rng(seed)
    scale = [50, 57, 58, 60, 62, 64, 65, 67, 69]  # D3 A3 Bb3 C4 D4 E4 F4 G4 A4

    def midi(m):
        return 440 * 2 ** ((m - 69) / 12)

    def hit(t0, m, vel, pan):
        s = int(t0 * sr)
        L = min(int(3.2 * sr), n - s)
        if L <= 0:
            return
        tt = np.arange(L) / sr
        f = midi(m)
        att = 1 - np.exp(-tt * 250)
        w = (np.sin(2 * np.pi * f * tt) * np.exp(-tt * 1.3)
             + 0.45 * np.sin(2 * np.pi * 2 * f * tt + 0.3) * np.exp(-tt * 2.2)
             + 0.22 * np.sin(2 * np.pi * 3.01 * f * tt) * np.exp(-tt * 3.5)
             + 0.10 * np.sin(2 * np.pi * f * 1.003 * tt) * np.exp(-tt * 1.1))  # hafif dalgalanma
        w *= att * vel
        w[: int(0.012 * sr)] += rng.standard_normal(int(0.012 * sr))[: L] * 0.02 * vel  # el vuruşu dokusu
        out[s:s + L, 0] += w * (1 - pan)
        out[s:s + L, 1] += w * pan

    beat = 60 / bpm
    patterns = [
        [0, 4, 6, 5, 0, 7, 6, 4], [0, 5, 4, 6, 0, 8, 7, 5], [0, 6, 5, 4, 0, 4, 7, 6], [0, 3, 5, 4, 0, 6, 5, 7]]
    pat = patterns[seed % len(patterns)]
    t = 0.15
    i = 0
    while t < dur - 1.5:
        idx = pat[i % len(pat)]
        m = scale[idx]
        vel = 0.9 if idx == 0 else 0.55 + 0.25 * rng.random()
        pan = 0.5 if idx == 0 else 0.3 + 0.4 * rng.random()
        hit(t, m, vel, pan)
        if i % 4 == 3 and rng.random() < 0.6:  # ara süs vuruşu
            hit(t + beat / 2, scale[rng.integers(4, 9)], 0.3, 0.3 + 0.4 * rng.random())
        t += beat
        i += 1
    fi, fo = int(0.3 * sr), int(1.8 * sr)
    out[:fi] *= np.linspace(0, 1, fi)[:, None]
    out[-fo:] *= np.linspace(1, 0, fo)[:, None]
    out /= np.max(np.abs(out)) * 1.12
    dry = path + ".dry.wav"
    with wave.open(dry, "wb") as w:
        w.setnchannels(2)
        w.setsampwidth(2)
        w.setframerate(sr)
        w.writeframes((out * 32767).astype("<i2").tobytes())
    run(["ffmpeg", "-v", "error", "-y", "-i", dry, "-af",
         "aecho=0.8:0.7:90|180|320:0.35|0.25|0.18,lowpass=f=10000,highpass=f=60,"
         "loudnorm=I=-18:TP=-2:LRA=7", "-ar", "48000", path])
    os.remove(dry)


# ---------------------------------------------------------------- ses efektleri
def make_sfx(path, tur):
    """Kısa, telifsiz efekt sesleri: tik (ding), odul (yükselen zil), hedef (tok)."""
    sr = 48000
    def tone(f, dur, decay, amp=1.0, start=0.0, total=None):
        n = int(sr * (total or dur))
        out = np.zeros(n)
        s = int(sr * start)
        tt = np.arange(int(sr * dur)) / sr
        w = (np.sin(2 * np.pi * f * tt) + 0.35 * np.sin(4 * np.pi * f * tt) * np.exp(-tt * decay * 1.5)) \
            * np.exp(-tt * decay) * (1 - np.exp(-tt * 600)) * amp
        e = min(n, s + len(w))
        out[s:e] += w[:e - s]
        return out
    if tur == "tik":
        x = tone(1318.5, 0.6, 9, 1.0, total=0.7) + tone(1975.5, 0.5, 11, 0.6, start=0.06, total=0.7)
    elif tur == "odul":
        x = sum(tone(f, 0.9, 5, 0.8, start=i * 0.08, total=1.3)
                for i, f in enumerate([1046.5, 1318.5, 1568.0, 2093.0]))
    elif tur == "kalp":  # küt-küt kalp atışı + yumuşak tını
        n = int(sr * 0.9)
        tt = np.arange(n) / sr
        x = np.zeros(n)
        for st, amp in ((0.0, 1.0), (0.22, 0.8)):
            k = int(sr * st)
            u = tt[:n - k]
            x[k:] += np.sin(2 * np.pi * 70 * u) * np.exp(-u * 18) * amp
        x += tone(880, 0.8, 5, 0.25, start=0.05, total=0.9)
    elif tur == "hediye":  # sallanma tıkırtısı + açılma "pop"u + yükselen zil
        n = int(sr * 1.8)
        x = np.zeros(n)
        rnd = np.random.default_rng(4)
        for st in (0.38, 0.47, 0.56, 0.64):
            k = int(sr * st)
            m = int(sr * 0.04)
            x[k:k + m] += rnd.standard_normal(m) * np.exp(-np.arange(m) / sr * 90) * 0.35
        k = int(sr * 0.75)
        u = np.arange(int(sr * 0.12)) / sr
        x[k:k + len(u)] += np.sin(2 * np.pi * (260 + 900 * u / 0.12) * u) * np.exp(-u * 30) * 0.9
        x += sum(tone(f, 0.9, 5, 0.6, start=0.8 + i * 0.07, total=1.8)
                 for i, f in enumerate([1046.5, 1318.5, 1568.0, 2093.0]))
    elif tur == "kapanis":  # kapanış kartı için yumuşak tını (müziksiz videolarda sessizliği önler)
        n = int(sr * 1.7)
        tt = np.arange(n) / sr
        pad = sum(np.sin(2 * np.pi * f * tt) for f in (261.63, 329.63, 392.0)) / 3
        env = np.minimum(1, tt / 0.25) * np.exp(-np.maximum(0, tt - 0.4) * 2.2)
        x = pad * env * 0.45
        x += sum(tone(f, 1.2, 3.2, 0.55, start=0.05 + i * 0.16, total=1.7)
                 for i, f in enumerate([523.25, 659.25, 783.99]))
        fo = int(sr * 0.5)
        x[-fo:] *= np.linspace(1, 0, fo)
    elif tur == "gunes":
        x = sum(tone(f, 1.0, 4, 0.5, start=i * 0.05, total=1.3) for i, f in enumerate([784, 988, 1175, 1568, 1976]))
    elif tur == "su":
        n = int(sr * 0.4)
        tt = np.arange(n) / sr
        x = np.sin(2 * np.pi * (500 + 1400 * tt / 0.4) * tt) * np.exp(-tt * 16)
    elif tur == "ay":
        x = tone(659.3, 1.2, 3, 0.8, total=1.4) + tone(987.8, 1.0, 3.5, 0.5, start=0.15, total=1.4)
    elif tur == "yildiz":
        x = sum(tone(f, 0.5, 9, 0.5, start=i * 0.04, total=0.8) for i, f in enumerate([2637, 3136, 3520, 4186]))
    else:  # hedef
        n = int(sr * 0.5)
        tt = np.arange(n) / sr
        sweep = np.sin(2 * np.pi * (300 + 900 * np.exp(-tt * 18)) * tt) * np.exp(-tt * 14) * 0.5
        thud = np.sin(2 * np.pi * 140 * tt) * np.exp(-tt * 22)
        x = np.zeros(n)
        k = int(sr * 0.12)
        x[:n] += sweep
        x[k:] += thud[:n - k]
    x = x / (np.max(np.abs(x)) + 1e-9) * 0.9
    st = np.stack([x, x], axis=1)
    with wave.open(path, "wb") as w:
        w.setnchannels(2)
        w.setsampwidth(2)
        w.setframerate(sr)
        w.writeframes((st * 32767).astype("<i2").tobytes())


# ---------------------------------------------------------------- ekran yazıları
def _tsize(d, t, f):
    b = d.textbbox((0, 0), t, font=f)
    return b[2] - b[0], b[3] - b[1], b


def card_png(path, lines, y, badge=None, center=False):
    im = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    padx, pady, gap = 40, 30, 14
    bw = 0
    if badge:
        bf = font("Inter-Black.otf", 58)
        bww, bhh, _ = _tsize(d, badge, bf)
        bw = max(bww, bhh) + 44 + 24
    # yazı karta sığmıyorsa yazı tipini küçült (kenardan taşmayı önler)
    maxw = W - 60 - bw - 2 * padx
    fitted = []
    for t, f, c in lines:
        while _tsize(d, t, f)[0] > maxw and f.size > 24:
            f = ImageFont.truetype(f.path, f.size - 2)
        fitted.append((t, f, c))
    lines = fitted
    sizes = [_tsize(d, t, f) for t, f, c in lines]
    cw = min(max(s[0] for s in sizes) + bw + 2 * padx, W - 60)
    ch = sum(s[1] for s in sizes) + gap * (len(lines) - 1) + 2 * pady
    x = (W - cw) // 2 if center else 60
    sh = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(sh).rounded_rectangle([x + 6, y + 10, x + cw + 6, y + ch + 10], radius=34,
                                         fill=(0, 0, 0, 90))
    im.alpha_composite(sh.filter(ImageFilter.GaussianBlur(14)))
    d = ImageDraw.Draw(im)
    d.rounded_rectangle([x, y, x + cw, y + ch], radius=34, fill=CARD)
    cx = x + padx
    if badge:
        r = (max(bww, bhh) + 44) // 2
        cy = y + ch // 2
        d.ellipse([cx, cy - r, cx + 2 * r, cy + r], fill=SAGE)
        d.text((cx + r, cy), badge, font=bf, fill=WHITE, anchor="mm")
        cx += bw
    ty = y + pady
    for (t, f, c), (tw, th, b) in zip(lines, sizes):
        tx = (x + (cw - tw) // 2) if center else cx
        d.text((tx - b[0], ty - b[1]), t, font=f, fill=c)
        ty += th + gap
    im.save(path)


def cta_png(path, text, y=500):
    im = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    f = font("Inter-ExtraBold.otf", 52)
    tw, th, b = _tsize(d, text, f)
    x = (W - tw - 90) // 2
    sh = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(sh).rounded_rectangle([x + 5, y + 8, x + tw + 95, y + th + 60], radius=60,
                                         fill=(0, 0, 0, 100))
    im.alpha_composite(sh.filter(ImageFilter.GaussianBlur(12)))
    d = ImageDraw.Draw(im)
    d.rounded_rectangle([x, y, x + tw + 90, y + th + 52], radius=60, fill=SAGE)
    d.text((x + 45 - b[0], y + 26 - b[1]), text, font=f, fill=WHITE)
    im.save(path)


def build_overlays(spec, tmp, dur):
    """[(png, start, end)] listesi döndürür."""
    title = font("InterDisplay-Black.otf", 78)
    step_t = font("InterDisplay-ExtraBold.otf", 72)
    sub = font("Inter-SemiBold.otf", 40)
    small = font("Inter-SemiBold.otf", 38)
    items = []
    y = spec.get("yazi_y", 230)
    h = spec.get("hook")
    if h:
        p = os.path.join(tmp, "hook.png")
        tf = font("InterDisplay-Black.otf", int(h.get("boyut", 78)))
        sf = font("Inter-SemiBold.otf", max(30, int(h.get("boyut", 78) * 0.52)))
        lines = [(h["metin"], tf, WHITE)] + ([(h["alt"], sf, CREAM)] if h.get("alt") else [])
        card_png(p, lines, h.get("y", y), center=True)
        items.append((p, h.get("bas", 0.0), h["bit"]))
    for i, s in enumerate(spec.get("adimlar", [])):
        p = os.path.join(tmp, f"adim{i}.png")
        lines = [(s["baslik"], step_t, WHITE)] + [(a, small, CREAM) for a in s.get("altlar", [])]
        card_png(p, lines, s.get("y", y), badge=str(s.get("no", i + 1)))
        items.append((p, s["bas"], s.get("bit", dur + 0.2)))
    c = spec.get("cta")
    if c:
        p = os.path.join(tmp, "cta.png")
        cta_png(p, c["metin"], c.get("y", 500))
        items.append((p, c["bas"], c.get("bit", dur + 0.2)))
    return items


# ---------------------------------------------------------------- kapaklar
def _pill(d, xy, text, f, fill, tc, pad=(28, 14)):
    x, y = xy
    b = d.textbbox((0, 0), text, font=f)
    w, h = b[2] - b[0], b[3] - b[1]
    d.rounded_rectangle([x, y, x + w + 2 * pad[0], y + h + 2 * pad[1]], radius=(h + 2 * pad[1]) // 2,
                        fill=fill)
    d.text((x + pad[0] - b[0], y + pad[1] - b[1]), text, font=f, fill=tc)


def _shadow_text(img, xy, text, f, fill, blur=10, off=4, alpha=150):
    sh = Image.new("RGBA", img.size, (0, 0, 0, 0))
    ImageDraw.Draw(sh).text((xy[0] + off, xy[1] + off), text, font=f, fill=(0, 0, 0, alpha))
    img.alpha_composite(sh.filter(ImageFilter.GaussianBlur(blur)))
    ImageDraw.Draw(img).text(xy, text, font=f, fill=fill)


def _grad(img, y0, y1, maxa):
    g = Image.new("RGBA", img.size, (0, 0, 0, 0))
    gd = ImageDraw.Draw(g)
    for y in range(y0, y1):
        gd.line([(0, y), (img.size[0], y)], fill=(25, 32, 25, int(maxa * ((y - y0) / (y1 - y0)) ** 1.4)))
    img.alpha_composite(g)


def grab_frame(video, t, path):
    run(["ffmpeg", "-v", "error", "-y", "-ss", str(t), "-i", video, "-frames:v", "1", path])


def make_thumbnails(spec, video, out_prefix, tmp):
    k = spec["kapak"]
    f1 = os.path.join(tmp, "k1.png")
    grab_frame(video, k.get("kare", 0.04), f1)
    kanal = spec.get("kanal", "BEDENİNE YOLCULUK")

    im = ImageEnhance.Brightness(Image.open(f1).convert("RGB")).enhance(1.03).convert("RGBA")
    _grad(im, 1080, 1920, 235)
    d = ImageDraw.Draw(im)
    _pill(d, (70, 90), kanal, font("Inter-Bold.otf", 34), CREAM[:3] + (235,), DARK)
    y = 1290
    _pill(d, (70, y), k["etiket"], font("Inter-Bold.otf", 46), SAGE, WHITE)
    _shadow_text(im, (62, y + 110), k["buyuk"], font("InterDisplay-Black.otf", 190), WHITE)
    _shadow_text(im, (72, y + 340), k["alt"], font("Inter-SemiBold.otf", 58), CREAM)
    im.convert("RGB").save(out_prefix + "-kapak-dikey-1080x1920.jpg", quality=94)

    bg = Image.new("RGBA", (1280, 720), CREAM)
    crop1 = k.get("yatay_kirpma_1", [0, 240, 1080, 1440])
    bg.paste(Image.open(f1).convert("RGB").crop(crop1).resize((640, 720), Image.LANCZOS), (0, 0))
    if "yatay_ikinci_kare" in k:
        f2 = os.path.join(tmp, "k2.png")
        grab_frame(video, k["yatay_ikinci_kare"], f2)
        crop2 = k.get("yatay_kirpma_2", [0, 700, 1080, 1900])
        bg.paste(Image.open(f2).convert("RGB").crop(crop2).resize((640, 720), Image.LANCZOS), (640, 0))
    else:
        bg.paste(Image.open(f1).convert("RGB").crop([0, 700, 1080, 1900]).resize((640, 720),
                 Image.LANCZOS), (640, 0))
    _grad(bg, 330, 720, 240)
    d = ImageDraw.Draw(bg)
    d.line([(640, 0), (640, 720)], fill=CREAM, width=5)
    _pill(d, (40, 34), kanal, font("Inter-Bold.otf", 26), CREAM[:3] + (235,), DARK, pad=(20, 10))
    _pill(d, (40, 438), k["etiket"], font("Inter-Bold.otf", 34), SAGE, WHITE, pad=(22, 11))
    _shadow_text(bg, (34, 515), k["buyuk"], font("InterDisplay-Black.otf", 118), WHITE)
    _shadow_text(bg, (42, 652), k["alt"], font("Inter-SemiBold.otf", 38), CREAM)
    bg.convert("RGB").save(out_prefix + "-kapak-yatay-1280x720.jpg", quality=94)


# ---------------------------------------------------------------- ana akış
def audio_graph(has_audio, konusma, muzik_db, dur, music_idx, muziksiz=False):
    if muziksiz:
        end = f"afade=t=out:st={max(dur - 0.28, 0):.2f}:d=0.28,loudnorm=I=-14:TP=-1.5:LRA=9[a]"
        if not has_audio:
            return f"anullsrc=r=48000:cl=stereo,atrim=0:{dur:.3f}[a]"
        return ("[0:a]highpass=f=80,acompressor=threshold=-22dB:ratio=2.5:attack=10:release=150:makeup=2,"
                f"aformat=sample_rates=48000:channel_layouts=stereo,{end}")
    fo = max(dur - 1.2, 0)
    mus = f"[{music_idx}:a]highpass=f=140,volume={muzik_db}dB,atrim=0:{dur:.3f},afade=t=out:st={fo:.2f}:d=1.2"
    end = f"afade=t=out:st={max(dur - 0.28, 0):.2f}:d=0.28,loudnorm=I=-14:TP=-1.5:LRA=9[a]"
    if not has_audio:
        return f"{mus},volume=6dB,{end}"
    voice = ("[0:a]highpass=f=80,acompressor=threshold=-22dB:ratio=2.5:attack=10:release=150:makeup=2,"
             "aformat=sample_rates=48000:channel_layouts=stereo")
    if konusma:
        return (f"{voice},asplit=2[voice][sc];{mus}[mus];"
                "[mus][sc]sidechaincompress=threshold=0.08:ratio=2.5:attack=40:release=500[ducked];"
                f"[voice][ducked]amix=inputs=2:duration=first:normalize=0,{end}")
    return (f"{voice},volume=-4dB[amb];{mus},volume=4dB[mus];"
            f"[amb][mus]amix=inputs=2:duration=first:normalize=0,{end}")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("tarif", help="JSON tarif dosyası")
    ap.add_argument("--kareler", action="store_true",
                    help="Sadece zaman damgalı kare çizelgesi üret (yazı zamanlarını belirlemek için)")
    a = ap.parse_args()
    base = os.path.dirname(os.path.abspath(a.tarif))
    spec = json.load(open(a.tarif, encoding="utf-8"))
    src = spec["kaynak"] if os.path.isabs(spec["kaynak"]) else os.path.join(base, spec["kaynak"])
    out_dir = spec.get("cikti_klasoru", "..")
    out_dir = out_dir if os.path.isabs(out_dir) else os.path.normpath(os.path.join(base, out_dir))
    os.makedirs(out_dir, exist_ok=True)
    prefix = os.path.join(out_dir, spec["ad"])
    dur, has_audio = probe(src)
    kirp = float(spec.get("kirp_bas", 0))  # baştaki boşluğu (sessizlik/hareketsizlik) kes
    dur -= kirp
    SS = ["-ss", f"{kirp:.3f}"] if kirp else []
    uzat = float(spec.get("uzat", 0))  # sona donmuş kare ile kapanış kartı süresi (sn)
    dur += uzat
    VENH = (f"tpad=stop_mode=clone:stop_duration={uzat}," if uzat else "") + ENHANCE

    if a.kareler:
        sheet = prefix + "-zaman-cizelgesi.jpg"
        run(["ffmpeg", "-v", "error", "-y", *SS, "-i", src, "-vf",
             "fps=2,scale=180:-1,drawtext=fontfile=/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf:"
             "text='%{pts\\:flt}':x=5:y=5:fontsize=24:fontcolor=yellow:box=1:boxcolor=black,"
             f"tile=10x{int(np.ceil(dur * 2 / 10))}", "-frames:v", "1", sheet])
        print(sheet)
        return

    tmp = tempfile.mkdtemp(prefix="bedenine_")
    try:
        m = spec.get("muzik", {})
        muziksiz = bool(m.get("yok"))
        music_in = []
        if not muziksiz:
            music = os.path.join(tmp, "muzik.wav")
            if m.get("stil") == "handpan":
                make_handpan(music, dur + 1.0, seed=m.get("tohum", 0), bpm=m.get("bpm", 84))
            else:
                make_music(music, dur + 1.0, seed=m.get("tohum", 0), bpm=m.get("bpm", 96))
            shutil.copy(music, prefix + "-muzik.wav")
            music_in = ["-i", music]
        agraph = audio_graph(has_audio, m.get("konusma_var", has_audio), m.get("seviye_db", -4), dur, 1,
                             muziksiz=muziksiz)
        if uzat and has_audio:
            agraph = agraph.replace("[0:a]", f"[0:a]apad=pad_dur={uzat},", 1)
        first_ov = 1 if muziksiz else 2
        enc = ["-c:v", "libx264", "-preset", "slow", "-crf", "17", "-profile:v", "high", "-r", "24",
               "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-movflags", "+faststart"]

        plain = prefix + "-1080p.mp4"
        run(["ffmpeg", "-v", "error", "-y", *SS, "-i", src, *music_in, "-filter_complex",
             f"[0:v]{VENH},format=yuv420p[v];{agraph}", "-map", "[v]", "-map", "[a]", "-t", f"{dur:.3f}", *enc, plain])

        items = build_overlays(spec, tmp, dur)
        inputs, chain, last = [], [], "base"
        for i, (png, st, en) in enumerate(items):
            inputs += ["-loop", "1", "-t", f"{dur + 0.2:.2f}", "-framerate", "24", "-i", png]
            idx = i + first_ov
            chain.append(f"[{idx}]format=rgba,fade=t=in:st={st}:d=0.25:alpha=1,"
                         f"fade=t=out:st={max(en - 0.25, st)}:d=0.25:alpha=1[o{i}]")
            chain.append(f"[{last}][o{i}]overlay=enable='between(t,{st},{en})'[x{i}]")
            last = f"x{i}"
        # animasyonlu efektler (söyleneni görselleştirir) + ses efektleri
        efx = spec.get("efektler", [])
        sfx_inputs, sfx_labels = [], []
        if efx:
            sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
            import efektler
            next_idx = first_ov + len(items)
            for j, e in enumerate(efx):
                boy = int(e.get("boyut", 360))
                sure_e = float(e.get("sure", 1.6))
                pat, _ = efektler.render_effect(e["tur"], os.path.join(tmp, f"efx{j}"), boyut=boy, sure=sure_e)
                inputs += ["-framerate", "24", "-i", pat]
                x = int(e.get("x", W // 2)) - boy // 2
                y = int(e.get("y", 900)) - boy // 2
                chain.append(f"[{next_idx}]format=rgba,setpts=PTS+{e['bas']}/TB[e{j}]")
                chain.append(f"[{last}][e{j}]overlay={x}:{y}:eof_action=pass[ex{j}]")
                last = f"ex{j}"
                next_idx += 1
                if e.get("ses", True):
                    wav = os.path.join(tmp, f"sfx{j}.wav")
                    make_sfx(wav, e["tur"])
                    sfx_inputs += ["-i", wav]
                    sfx_labels.append([None, int(float(e["bas"]) * 1000), e.get("ses_db", -12)])
            # ses girişleri tüm efekt görsellerinden sonra gelir
            for k, lab in enumerate(sfx_labels):
                lab[0] = first_ov + len(items) + len(efx) + k
        kapanis = spec.get("kapanis_sesi", bool(uzat) and muziksiz)
        if uzat and kapanis:
            wav = os.path.join(tmp, "sfx_kapanis.wav")
            make_sfx(wav, "kapanis")
            sfx_inputs += ["-i", wav]
            sfx_labels.append([first_ov + len(items) + len(efx) + len(sfx_labels),
                               int((dur - uzat) * 1000), -8])
        if sfx_labels:
            # ses dengelemeyi (loudnorm) yalnızca en sonda bir kez yap: art arda iki loudnorm
            # gecikme biriktirir ve video bittiğinde son saniyelerin sesi kaybolur
            ag = agraph[:-3].replace(",loudnorm=I=-14:TP=-1.5:LRA=9", "") + "[a0]"
            mix = "".join(f"[{i}:a]adelay={ms}|{ms},volume={db}dB[s{k}];" for k, (i, ms, db) in enumerate(sfx_labels))
            ins = "[a0]" + "".join(f"[s{k}]" for k in range(len(sfx_labels)))
            agraph = (f"{ag};{mix}{ins}amix=inputs={len(sfx_labels) + 1}:duration=first:normalize=0,"
                      "loudnorm=I=-14:TP=-1.5:LRA=9[a]")
        inputs += sfx_inputs
        fc = f"[0:v]{VENH}[base];" + ";".join(chain) + f";[{last}]format=yuv420p[v];{agraph}"
        if not items and not efx:
            fc = f"[0:v]{VENH},format=yuv420p[v];{agraph}"
        yazili = prefix + "-1080p-yazili.mp4"
        run(["ffmpeg", "-v", "error", "-y", *SS, "-i", src, *music_in, *inputs, "-filter_complex", fc,
             "-map", "[v]", "-map", "[a]", "-t", f"{dur:.3f}", *enc, yazili])

        kb = spec.get("kapak_basa")
        if kb:  # seçilen kapağı videonun ilk anına yerleştir (ses kesintisiz devam eder)
            img = kb["dosya"] if os.path.isabs(kb["dosya"]) else os.path.normpath(os.path.join(base, kb["dosya"]))
            sure = float(kb.get("sure", 0.5))
            gecis = 0.15
            run(["ffmpeg", "-v", "error", "-y", "-i", yazili, "-loop", "1", "-t", f"{sure + gecis:.2f}",
                 "-framerate", "24", "-i", img, "-filter_complex",
                 f"[1]scale={W}:{H},format=rgba,fade=t=out:st={sure:.2f}:d={gecis}:alpha=1[k];"
                 f"[0:v][k]overlay=eof_action=pass,format=yuv420p[v]",
                 "-map", "[v]", "-map", "0:a", "-c:v", "libx264", "-preset", "slow", "-crf", "17",
                 "-profile:v", "high", "-r", "24", "-c:a", "copy", "-movflags", "+faststart",
                 prefix + "-1080p-yazili-kapakli.mp4"])

        if spec.get("kapak"):
            make_thumbnails(spec, plain, prefix, tmp)
        if spec.get("aciklama"):
            with open(prefix + "-aciklama.txt", "w", encoding="utf-8") as f:
                f.write(spec["aciklama"].strip() + "\n")
        for f in sorted(os.listdir(out_dir)):
            if f.startswith(spec["ad"] + "-"):
                print(os.path.join(out_dir, f))
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


if __name__ == "__main__":
    main()
