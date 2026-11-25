#!/usr/bin/env python3
"""'Nisan'ın Okuma Defteri' kapağı (A4 dikey).

kapak.html            : çizimli kapak (fotoğrafsız)
kapak-fotografli.html : ortada fotoğraf çerçevesi olan kapak (foto/nisan.jpg, git'e eklenmez)
"""
import math
from pathlib import Path
from sprites import SPRITE, FONT_CSS, INK

HERE = Path(__file__).parent
PACIFICO = (HERE / "fonts" / "pacifico.css").read_text()


def fluffy_outline(cx=80, cy=56, rx=62, ry=34, n=34):
    """Uzun tüylü ginepig gövdesi: püsküllü kenarlı elips (sola bakan)."""
    pts = []
    for i in range(n + 1):
        a = 2 * math.pi * i / n
        pts.append((a, cx + rx * math.cos(a), cy + ry * math.sin(a)))
    d = f"M{pts[0][1]:.1f} {pts[0][2]:.1f}"
    for (a0, x0, y0), (a1, x1, y1) in zip(pts, pts[1:]):
        am = (a0 + a1) / 2
        deg = math.degrees(am) % 360
        tuft = 9
        if 140 < deg < 220:      # yüz tarafı daha düzgün
            tuft = 3
        elif 50 < deg < 130:     # alt taraf: uzun tüy eteği
            tuft = 13
        cxp = cx + (rx + tuft) * math.cos(am)
        cyp = cy + (ry + tuft) * math.sin(am)
        d += f" Q{cxp:.1f} {cyp:.1f} {x1:.1f} {y1:.1f}"
    return d + " Z"


BODY = fluffy_outline()

FLUFFY = f"""
<svg width="0" height="0" style="position:absolute"><defs>
 <clipPath id="flClip"><path d="{BODY}"/></clipPath>
 <symbol id="fluffy" viewBox="0 0 160 110">
  <g stroke="{INK}" stroke-width="2.4" stroke-linejoin="round" stroke-linecap="round">
   <ellipse cx="45" cy="100" rx="8" ry="4" fill="#f2b8b0"/>
   <ellipse cx="112" cy="100" rx="9" ry="4" fill="#f2b8b0"/>
   <path d="{BODY}" fill="#fffaf2" stroke="none"/>
   <g clip-path="url(#flClip)" stroke="none">
    <path d="M70 0 C 100 10 130 15 160 30 V 70 C 140 60 120 66 100 56 C 88 44 72 30 70 0 Z" fill="#d9894a"/>
    <ellipse cx="38" cy="46" rx="24" ry="22" fill="#d9894a"/>
    <ellipse cx="20" cy="60" rx="9" ry="20" fill="#fffaf2"/>
    <path d="M30 28 C 34 20 40 18 46 22 C 44 30 38 34 30 28 Z" fill="#fffaf2"/>
   </g>
   <path d="{BODY}" fill="none"/>
   <g fill="none" stroke-width="1.4" opacity=".55">
    <path d="M90 40 Q100 52 96 66 M110 34 Q122 50 116 70 M130 44 Q140 58 134 76 M74 62 Q80 74 76 86"/>
   </g>
   <path d="M47 34 C 44 22 58 18 63 28 C 62 35 54 38 47 34 Z" fill="#f2b8b0"/>
   <circle cx="34" cy="50" r="4.8" fill="{INK}" stroke="none"/>
   <circle cx="35.6" cy="48.4" r="1.6" fill="#fff" stroke="none"/>
   <ellipse cx="16" cy="62" rx="3.2" ry="2.4" fill="#e57f7f" stroke-width="1.3"/>
   <path d="M17 66 Q20 70 24 67.5" fill="none" stroke-width="1.8"/>
   <ellipse cx="29" cy="66" rx="6" ry="3.8" fill="#f59a9a" stroke="none" opacity=".6"/>
   <path d="M9 59 L1 57 M9 63 L1 64" stroke-width="1.2" opacity=".7"/>
  </g>
 </symbol>
</defs></svg>"""


def use(sym, style, extra_cls=""):
    return f'<svg class="u {extra_cls}" style="{style}"><use href="#{sym}"/></svg>'


SPRINKLES = "".join([
    use("star", "left:14mm;top:16mm;width:7mm;height:7mm;--sf:#ffe08a;transform:rotate(-12deg)"),
    use("heart", "left:26mm;top:12mm;width:5mm;height:4.6mm;--hf:#f7a8b8"),
    use("star", "right:15mm;top:14mm;width:6mm;height:6mm;--sf:#c9b6f2;transform:rotate(10deg)"),
    use("heart", "right:27mm;top:19mm;width:6mm;height:5.5mm;--hf:#ffc98b;transform:rotate(12deg)"),
    use("paw", "left:17mm;top:62mm;width:5mm;height:5mm;--pf:#c7dccb;transform:rotate(-20deg)"),
    use("paw", "left:24mm;top:68mm;width:5mm;height:5mm;--pf:#c7dccb;transform:rotate(-10deg)"),
    use("paw", "right:18mm;top:64mm;width:5mm;height:5mm;--pf:#c7dccb;transform:rotate(20deg)"),
    use("seed", "right:26mm;top:70mm;width:3.5mm;height:5.5mm;transform:rotate(30deg)"),
])


def tracker():
    cols = ["#fff"] * 20
    books = "".join(
        f'<div class="spine"><span>{i + 1}</span></div>' for i in range(20))
    return f"""
<div class="track">
 <div class="track-h">Bitirdiğim kitaplar <small>(her kitap bitince bir tanesini boya!)</small></div>
 <div class="shelf">{books}</div>
</div>"""


def info():
    return """
<div class="info">
 <div class="ln"><b>Sınıfım:</b><i></i><b>Okulum:</b><i class="w2"></i></div>
 <div class="ln"><b>Başladığım tarih:</b><i></i><b>Öğretmenim:</b><i class="w2"></i></div>
</div>"""


def center_photo():
    return f"""
<div class="stage">
 <div class="polaroid">
  <img src="foto/nisan.jpg" alt="">
  <div class="cap">Ben ve ginepigim</div>
  <span class="tape t1"></span><span class="tape t2"></span>
 </div>
 {use("fluffy", "left:4mm;bottom:-3mm;width:56mm;height:38.5mm")}
 {use("hamster", "right:10mm;top:-6mm;width:28mm;height:26mm")}
 {use("book", "right:16mm;top:15.5mm;width:16mm;height:11mm;--bf:#fff7d6;transform:rotate(-6deg)")}
 {use("flower", "right:8mm;bottom:8mm;width:12mm;height:12mm")}
 {use("flower", "right:20mm;bottom:2mm;width:9mm;height:9mm;--ff:#c9b6f2")}
 {use("leaf", "right:3mm;bottom:1mm;width:12mm;height:8mm;transform:scaleX(-1)")}
 {use("carrot", "left:58mm;bottom:0;width:8mm;height:12mm;transform:rotate(-30deg)")}
</div>"""


def center_art():
    stack = "".join(
        f'<div class="bk" style="background:{c};width:{w}mm;margin-left:{m}mm"></div>'
        for c, w, m in [("#f7b6c8", 92, 6), ("#b5dfc0", 98, 0), ("#ffd98a", 88, 9), ("#c9d7f2", 96, 2)])
    return f"""
<div class="stage art">
 <div class="sunburst"></div>
 <div class="pile">
  {use("fluffy", "left:2mm;top:-60mm;width:92mm;height:63mm")}
  {use("book", "left:22mm;top:-23mm;width:32mm;height:22mm;--bf:#fff7d6;transform:rotate(-5deg)")}
  <div class="books">{stack}</div>
 </div>
 {use("hamster", "right:16mm;bottom:20mm;width:34mm;height:31mm")}
 {use("book", "right:23mm;bottom:20.5mm;width:20mm;height:13.5mm;--bf:#fff;transform:rotate(4deg)")}
 {use("strawberry", "right:9mm;bottom:19mm;width:8mm;height:9.5mm")}
 {use("carrot", "left:12mm;bottom:20mm;width:9mm;height:13mm;transform:rotate(-25deg)")}
 {use("flower", "left:14mm;top:10mm;width:14mm;height:14mm")}
 {use("flower", "right:14mm;top:22mm;width:11mm;height:11mm;--ff:#c9b6f2")}
 {use("heart", "right:30mm;top:6mm;width:8mm;height:7.4mm;--hf:#f7a8b8;transform:rotate(10deg)")}
 {use("star", "left:34mm;top:4mm;width:8mm;height:8mm;--sf:#ffe08a")}
</div>"""


CSS = """
@page { size: A4 portrait; margin: 0; }
* { box-sizing: border-box; -webkit-print-color-adjust: exact; print-color-adjust: exact; }
html, body { margin: 0; padding: 0; background: #fff; }
body { font-family: 'Baloo 2', sans-serif; color: #5a3e2b; }
svg { display: block; overflow: visible; }
.u { position: absolute; }
.page { width: 210mm; height: 297mm; padding: 8mm; }
.card { position: relative; width: 100%; height: 100%; border: 0.9mm solid #5a3e2b; border-radius: 9mm;
        background-color: #eef7ef;
        background-image: radial-gradient(#d3e9d6 1.1mm, transparent 1.2mm);
        background-size: 9mm 9mm; background-position: 2mm 2mm;
        display: flex; flex-direction: column; align-items: center; padding: 14mm 12mm 9mm; overflow: hidden; }
.title { text-align: center; position: relative; z-index: 2; }
.title .name { font-family: 'Pacifico', cursive; font-size: 50pt; line-height: 1.15; color: #e0607e;
               text-shadow: 0.7mm 0.7mm 0 #fff, -0.7mm -0.7mm 0 #fff, 0.7mm -0.7mm 0 #fff, -0.7mm 0.7mm 0 #fff; }
.title .sub { font-weight: 800; font-size: 40pt; line-height: 1; margin-top: -1mm;
              display: inline-block; padding: 0 4mm;
              background: linear-gradient(transparent 58%, #ffe08a 58%, #ffe08a 90%, transparent 90%); }
.motto { font-family: 'Patrick Hand'; font-size: 15pt; margin-top: 2mm; display: flex; align-items: center; gap: 2mm; }
.motto svg { width: 5mm; height: 5mm; --pf: #e0607e; }

.stage { position: relative; width: 100%; flex: 1; margin: 5mm 0 4mm; }
.polaroid { position: absolute; left: 50%; top: 3mm; width: 92mm; padding: 4mm 4mm 0; background: #fff;
            border: 0.6mm solid #5a3e2b; border-radius: 2mm; transform: translateX(-50%) rotate(-2.5deg);
            box-shadow: 1.5mm 2mm 0 rgba(90,62,43,.15); }
.polaroid img { width: 100%; height: 105mm; object-fit: cover; object-position: 50% 42%; display: block;
                border-radius: 1mm; border: 0.4mm solid #5a3e2b; }
.polaroid .cap { font-family: 'Patrick Hand'; font-size: 16pt; text-align: center; height: 12mm; line-height: 12mm; }
.tape { position: absolute; width: 22mm; height: 7mm; background: rgba(247,182,200,.75); border: 0.3mm solid rgba(90,62,43,.25); }
.tape.t1 { left: -7mm; top: 3mm; transform: rotate(-35deg); }
.tape.t2 { right: -7mm; top: 3mm; transform: rotate(35deg); background: rgba(255,224,138,.8); }

.stage.art .sunburst { position: absolute; left: 50%; top: 50%; width: 150mm; height: 150mm; transform: translate(-50%, -52%);
   border-radius: 50%; background: radial-gradient(circle, #fff 0 38%, #fff7e6 38% 52%, transparent 52%); }
.pile { position: absolute; left: 22mm; bottom: 18mm; width: 100mm; }
.books { display: flex; flex-direction: column-reverse; }
.bk { height: 9mm; border: 0.6mm solid #5a3e2b; border-radius: 1.6mm; margin-top: -0.6mm; position: relative; }
.bk::after { content: ""; position: absolute; left: 6mm; right: 6mm; top: 3.5mm; height: 1mm; background: rgba(255,255,255,.7); border-radius: 1mm; }

.track { width: 100%; background: #fff; border: 0.5mm solid #5a3e2b; border-radius: 4mm; padding: 2mm 4mm 3mm; position: relative; z-index: 2; }
.track-h { font-weight: 800; font-size: 12.5pt; }
.track-h small { font-family: 'Patrick Hand'; font-weight: 400; font-size: 11pt; opacity: .75; }
.shelf { display: grid; grid-template-columns: repeat(20, 1fr); gap: 1.2mm; margin-top: 1mm;
         border-bottom: 1.2mm solid #d9a77a; padding-bottom: 0; }
.spine { height: 15mm; border: 0.45mm solid #5a3e2b; border-bottom: none; border-radius: 1.2mm 1.2mm 0 0;
         display: flex; align-items: flex-end; justify-content: center; font-family: 'Patrick Hand'; font-size: 8.5pt; padding-bottom: .6mm; }
.spine:nth-child(3n) { height: 13mm; align-self: end; }
.spine:nth-child(4n+1) { height: 14mm; align-self: end; }
.info { width: 100%; margin-top: 3mm; display: flex; flex-direction: column; gap: 1mm; position: relative; z-index: 2;
        background: rgba(255,255,255,.85); border-radius: 3mm; padding: 1mm 4mm 2mm; border: 0.5mm solid #5a3e2b; }
.ln { display: flex; align-items: flex-end; gap: 1.5mm; height: 8mm; }
.ln b { font-weight: 600; font-size: 12pt; white-space: nowrap; line-height: 1; padding-bottom: .6mm; color: #7b4fa0; }
.ln i { flex: 1; border-bottom: 0.45mm dotted #7b4fa0; margin-right: 3mm; }
.ln i.w2 { flex: 1.4; margin-right: 0; }
"""


def html(center):
    motto = ('<div class="motto"><svg><use href="#paw"/></svg> Okudukça büyüyorum, büyüdükçe okuyorum! '
             '<svg><use href="#paw"/></svg></div>')
    return f"""<!doctype html><html lang="tr"><head><meta charset="utf-8"><title>Okuma Defteri Kapağı</title>
<style>{FONT_CSS}{PACIFICO}{CSS}</style></head><body>{SPRITE}{FLUFFY}
<div class="page"><div class="card">
 {SPRINKLES}
 <div class="title"><div class="name">Nisan'ın</div><div class="sub">Okuma Defteri</div>{motto}</div>
 {center}
 {tracker()}
 {info()}
</div></div></body></html>"""


if __name__ == "__main__":
    (HERE / "kapak.html").write_text(html(center_art()))
    (HERE / "kapak-fotografli.html").write_text(html(center_photo()))
    print("ok")
