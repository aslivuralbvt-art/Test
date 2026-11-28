#!/usr/bin/env python3
"""Regl Ağrısı Follow-Along videosu: 10 klibi kurgu planına göre birleştirir.

Kullanım: python3 build.py <klip_klasoru> <cikti_klasoru>
Klasörde sahne sırasıyla eşleşen dosyalar (SCENES listesindeki önekler) bulunmalı.
"""
import glob, os, subprocess, sys

SRC, OUT = sys.argv[1], sys.argv[2]
TMP = os.path.join(OUT, "_seg")
os.makedirs(TMP, exist_ok=True)

SCENES = ["b67c6c94", "47820dad", "63483d0c", "ca9c8a41", "d2d94676",
          "3d7114f5", "94a47314", "a19bfb10", "cd35b31f", "076c1a8c"]
CLIP = {i + 1: glob.glob(os.path.join(SRC, p + "-*.mp4"))[0] for i, p in enumerate(SCENES)}

FONT_L = "/usr/share/fonts/opentype/inter/Inter-Light.otf"
FONT_M = "/usr/share/fonts/opentype/inter/Inter-Medium.otf"
CREAM = "0xFFF8EE"
# Tüm sahnelere aynı hafif sıcak filtre (~%15)
WARM = "colortemperature=temperature=5200:mix=0.15,eq=saturation=1.04"
NORM = "scale=1280:720,fps=24,format=yuv420p"
ENC = ["-c:v", "libx264", "-preset", "medium", "-crf", "18", "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-ac", "2"]


def run(args):
    subprocess.run(["ffmpeg", "-v", "error", "-y"] + args, check=True)


def esc(s):
    return s.replace("\\", "\\\\").replace(":", "\\:").replace("'", "’").replace("%", "\\%")


def fade_alpha(t0, t1, f=0.6):
    return f"if(lt(t,{t0}),0,if(lt(t,{t0}+{f}),(t-{t0})/{f},if(lt(t,{t1}-{f}),1,if(lt(t,{t1}),({t1}-t)/{f},0))))"


def step_label(text, t0=0.8, t1=9.4):
    """Sağ alt köşe, ince font, yumuşak giriş/çıkış."""
    return (f"drawtext=fontfile={FONT_L}:text='{esc(text)}':fontsize=34:fontcolor={CREAM}"
            f":x=w-tw-56:y=h-th-52:shadowcolor=black@0.35:shadowx=0:shadowy=2"
            f":alpha='{fade_alpha(t0, t1)}'")


def seg(n, vf, af="anull", extra_in=None, dur=None):
    out = os.path.join(TMP, f"s{n:02d}.mp4")
    args = extra_in or ["-i", CLIP[n]]
    fc = f"[0:v]{vf},{WARM},{NORM}[v];[0:a]{af},aresample=48000[a]"
    a = args + ["-filter_complex", fc, "-map", "[v]", "-map", "[a]"]
    if dur:
        a += ["-t", str(dur)]
    run(a + ENC + [out])
    return out


segs = {}
# 1: Yatak açılış — 2 sn fade in
segs[1] = seg(1, "fade=t=in:st=0:d=2", "afade=t=in:st=0:d=2")
# 2: Banyo & çay
segs[2] = seg(2, "null")
# 3: Sessiz çay demleme — 0.8x
segs[3] = seg(3, "setpts=PTS/0.8", "atempo=0.8")
# 4: Sıcak su torbası
segs[4] = seg(4, step_label("1. Adım: Sıcak Terapi"))
# 5: Diz çekme & sallanma
segs[5] = seg(5, step_label("2. Adım: Vagus Siniri & Endorfin"))

# 6: Sessiz esneme — 3 kez (ileri/geri/ileri, atlamasız döngü) + 30 sn geri sayım
c6 = CLIP[6]
out6 = os.path.join(TMP, "s06.mp4")
title = esc("Birlikte Nefes Alalım")
fc6 = (
    "[0:v]split=3[a][b][c];[b]reverse[br];[a][br][c]concat=n=3:v=1:a=0,"
    + f"drawtext=fontfile={FONT_L}:text='{title}':fontsize=30:fontcolor={CREAM}:x=w-tw-56:y=48"
      ":shadowcolor=black@0.35:shadowy=2,"
    + f"drawtext=fontfile={FONT_M}:text='%{{eif\\:ceil(30-t)\\:d}} sn':fontsize=64:fontcolor={CREAM}"
      ":x=w-tw-56:y=92:shadowcolor=black@0.35:shadowy=2,"
    # ince ilerleme çubuğu
    + "drawbox=x=iw-376:y=176:w=320:h=3:color=0xFFF8EE@0.25:t=fill,"
    + "drawbox=x=iw-376:y=176:w='320*min(t/30,1)':h=3:color=0xFFF8EE@0.9:t=fill,"
    + f"{WARM},{NORM}[v];"
    "[0:a]asplit=3[x][y][z];[y]areverse[yr];[x][yr][z]concat=n=3:v=0:a=1,aresample=48000[au]"
)
run(["-i", c6, "-filter_complex", fc6, "-map", "[v]", "-map", "[au]", "-t", "30"] + ENC + [out6])
segs[6] = out6

# 7: Diyafram nefesi — 10 sn orijinal + son 5 sn geri/ileri döngü (10 sn) ve nefes sayacı
c7 = CLIP[7]
out7 = os.path.join(TMP, "s07.mp4")
inhale, exhale = esc("Burnundan derin nefes al"), esc("Ağzından yavaşça ver")
cnt = "%{eif\\:ceil(5-mod(t-10\\,5))\\:d}"
fc7 = (
    "[0:v]split=3[full][t1][t2];"
    "[t1]trim=5:10,setpts=PTS-STARTPTS,reverse[tr];"
    "[t2]trim=5:10,setpts=PTS-STARTPTS[tf];"
    "[full][tr][tf]concat=n=3:v=1:a=0,"
    + f"drawtext=fontfile={FONT_L}:text='{inhale}':fontsize=34:fontcolor={CREAM}:x=w-tw-56:y=48"
      f":shadowcolor=black@0.35:shadowy=2:enable='between(t,10,15)',"
    + f"drawtext=fontfile={FONT_L}:text='{exhale}':fontsize=34:fontcolor={CREAM}:x=w-tw-56:y=48"
      f":shadowcolor=black@0.35:shadowy=2:enable='between(t,15,20)',"
    + f"drawtext=fontfile={FONT_M}:text='{cnt}':fontsize=72:fontcolor={CREAM}:x=w-tw-56:y=96"
      f":shadowcolor=black@0.35:shadowy=2:enable='between(t,10,20)',"
    + f"{WARM},{NORM}[v];"
    # konuşma 10. sn'de yumuşakça biter, uzatılan kısım sessiz oda tonu
    "[0:a]afade=t=out:st=9.4:d=0.6,apad=whole_dur=20,aresample=48000[au]"
)
run(["-i", c7, "-filter_complex", fc7, "-map", "[v]", "-map", "[au]", "-t", "20"] + ENC + [out7])
segs[7] = out7

# 8: Salon & dopamin
segs[8] = seg(8, step_label("3. Adım: Dopamin Dengeleme"))
# 9: Sessiz telefon & çikolata — 0.8x
segs[9] = seg(9, "setpts=PTS/0.8", "atempo=0.8")
# 10: Şefkatli kapanış
segs[10] = seg(10, "null")

# Bitiş ekranı kartı: son kare bulanık, YouTube end-screen öğeleri için alt yarı boş
end = os.path.join(TMP, "s11.mp4")
thanks = esc("İzlediğin için teşekkürler")
fce = (
    "[0:v]trim=start_frame=239:end_frame=240,setpts=PTS-STARTPTS,loop=loop=-1:size=1,"
    "gblur=sigma=28,eq=brightness=-0.08,"
    + f"drawtext=fontfile={FONT_L}:text='{thanks}':fontsize=46:fontcolor={CREAM}:x=(w-tw)/2:y=130"
      f":alpha='{fade_alpha(0.8, 20)}',"
    + f"drawtext=fontfile={FONT_L}:text='{esc('Kendine nazik davran')}':fontsize=28:fontcolor={CREAM}@0.85"
      f":x=(w-tw)/2:y=196:alpha='{fade_alpha(1.4, 20)}',"
    + f"{WARM},{NORM}[v]"
)
run(["-i", CLIP[10], "-f", "lavfi", "-i", "anullsrc=r=48000:cl=stereo", "-filter_complex", fce,
     "-map", "[v]", "-map", "1:a", "-t", "12"] + ENC + [end])
segs[11] = end


def dur(p):
    return float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                                          "-of", "csv=p=0", p]).decode())


# Birleştirme: geçiş süresi (0 = düz kesme). Geçiş i → i+1 arasında
XF = {1: 0.5, 7: 0.5, 10: 1.0}
order = list(range(1, 12))
inputs, fc, starts = [], [], {}
for i in order:
    inputs += ["-i", segs[i]]
for k in range(len(order)):  # zaman tabanlarını eşitle (xfade şartı)
    fc.append(f"[{k}:v]setpts=PTS-STARTPTS,fps=24,settb=AVTB[iv{k}]")
    fc.append(f"[{k}:a]asetpts=PTS-STARTPTS[ia{k}]")
vprev, aprev, t = "[iv0]", "[ia0]", dur(segs[1])
starts[1] = 0.0
for k, i in enumerate(order[1:], start=1):
    prev = order[k - 1]
    d = XF.get(prev, 0)
    vo, ao = f"[v{k}]", f"[a{k}]"
    if d:
        off = t - d
        fc.append(f"{vprev}[iv{k}]xfade=transition=fade:duration={d}:offset={off:.3f}{vo}")
        fc.append(f"{aprev}[ia{k}]acrossfade=d={d}{ao}")
        starts[i] = off
        t = off + dur(segs[i])
    else:
        fc.append(f"{vprev}{aprev}[iv{k}][ia{k}]concat=n=2:v=1:a=1{vo}{ao}")
        starts[i] = t
        t += dur(segs[i])
    vprev, aprev = vo, ao
# Final: 2 sn fade out
# YouTube 1080p yüklemelerde daha yüksek bit hızı verir: lanczos ile 1080p'ye büyüt
fc.append(f"{vprev}fade=t=out:st={t-2:.3f}:d=2,scale=1920:1080:flags=lanczos,format=yuv420p[vf]")
fc.append(f"{aprev}afade=t=out:st={t-2:.3f}:d=2,loudnorm=I=-16:TP=-1.5:LRA=11[af]")
final = os.path.join(OUT, "regl_agrisi_follow_along_1080p.mp4")
run(inputs + ["-filter_complex", ";".join(fc), "-map", "[vf]", "-map", "[af]",
              "-movflags", "+faststart",
              "-c:v", "libx264", "-preset", "slow", "-crf", "20", "-profile:v", "high",
              "-c:a", "aac", "-b:a", "192k", "-ar", "48000", final])

def ts(s):
    s = int(s + 0.5)
    return f"{s//60:02d}:{s%60:02d}"

print(f"TOPLAM: {ts(t)} ({t:.2f} sn)")
for i in order:
    print(f"Sahne {i}: {ts(starts[i])}")
