#!/usr/bin/env python3
"""Kitap özeti defteri sayfalarını (A4 yatay, 2 sayfa) üretir."""
from pathlib import Path

HERE = Path(__file__).parent
FONT_CSS = (HERE / "fonts" / "fonts.css").read_text()

INK = "#5a3e2b"

SPRITE = f"""
<svg width="0" height="0" style="position:absolute">
 <defs>
  <clipPath id="gpClip"><path d="M30 40 C 32 20 60 12 90 14 C 125 16 145 38 143 60 C 141 80 120 86 90 86 L 45 86 C 22 86 10 74 10 60 C 10 50 20 42 30 40 Z"/></clipPath>

  <!-- Hamster (önden, oturan) -->
  <symbol id="hamster" viewBox="0 0 100 92">
   <g stroke="{INK}" stroke-width="2.4" stroke-linejoin="round" stroke-linecap="round">
    <circle cx="26" cy="22" r="11" fill="var(--h1,#f0a868)"/>
    <circle cx="74" cy="22" r="11" fill="var(--h1,#f0a868)"/>
    <circle cx="26" cy="22" r="5.5" fill="#f9c6c0" stroke="none"/>
    <circle cx="74" cy="22" r="5.5" fill="#f9c6c0" stroke="none"/>
    <path d="M50 18 C 80 18 92 40 92 60 C 92 80 74 88 50 88 C 26 88 8 80 8 60 C 8 40 20 18 50 18 Z" fill="var(--h1,#f0a868)"/>
    <path d="M50 40 C 68 40 79 54 79 66 C 79 80 66 86.5 50 86.5 C 34 86.5 21 80 21 66 C 21 54 32 40 50 40Z" fill="#fff6e8" stroke="none"/>
    <ellipse cx="28" cy="62" rx="6" ry="4" fill="#f59a9a" stroke="none" opacity=".65"/>
    <ellipse cx="72" cy="62" rx="6" ry="4" fill="#f59a9a" stroke="none" opacity=".65"/>
    <circle cx="37" cy="50" r="4.2" fill="{INK}" stroke="none"/>
    <circle cx="63" cy="50" r="4.2" fill="{INK}" stroke="none"/>
    <circle cx="38.4" cy="48.5" r="1.4" fill="#fff" stroke="none"/>
    <circle cx="64.4" cy="48.5" r="1.4" fill="#fff" stroke="none"/>
    <path d="M47 56.5 L53 56.5 L50 59.5 Z" fill="#e57f7f" stroke-width="1.4"/>
    <path d="M50 59.5 V62 M50 62 Q47 65 45 62.5 M50 62 Q53 65 55 62.5" fill="none" stroke-width="1.8"/>
    <ellipse cx="50" cy="76" rx="4.5" ry="6.5" fill="#7a6553" stroke-width="1.6"/>
    <path d="M50 70.5 V81.5" stroke="#f2e6d6" stroke-width="1.4"/>
    <ellipse cx="42" cy="77" rx="5" ry="4" fill="#f9c6c0"/>
    <ellipse cx="58" cy="77" rx="5" ry="4" fill="#f9c6c0"/>
   </g>
  </symbol>

  <!-- Hamster kafası (ruh hâli için) -->
  <symbol id="hhead" viewBox="0 0 60 56">
   <g stroke="{INK}" stroke-width="2.2" stroke-linejoin="round">
    <circle cx="14" cy="14" r="8" fill="var(--h1,#f0a868)"/>
    <circle cx="46" cy="14" r="8" fill="var(--h1,#f0a868)"/>
    <circle cx="14" cy="14" r="4" fill="#f9c6c0" stroke="none"/>
    <circle cx="46" cy="14" r="4" fill="#f9c6c0" stroke="none"/>
    <ellipse cx="30" cy="32" rx="25" ry="21" fill="var(--h1,#f0a868)"/>
    <ellipse cx="30" cy="39" rx="16" ry="13" fill="#fff6e8" stroke="none"/>
    <ellipse cx="14" cy="38" rx="4.5" ry="3" fill="#f59a9a" stroke="none" opacity=".65"/>
    <ellipse cx="46" cy="38" rx="4.5" ry="3" fill="#f59a9a" stroke="none" opacity=".65"/>
   </g>
  </symbol>

  <!-- Ginepig (yandan) -->
  <symbol id="guinea" viewBox="0 0 150 95">
   <g stroke="{INK}" stroke-width="2.4" stroke-linejoin="round" stroke-linecap="round">
    <ellipse cx="42" cy="86" rx="8" ry="4.5" fill="#f2b8b0"/>
    <ellipse cx="112" cy="86" rx="9" ry="4.5" fill="#f2b8b0"/>
    <path d="M30 40 C 32 20 60 12 90 14 C 125 16 145 38 143 60 C 141 80 120 86 90 86 L 45 86 C 22 86 10 74 10 60 C 10 50 20 42 30 40 Z" fill="#fffaf2" stroke="none"/>
    <g clip-path="url(#gpClip)" stroke="none">
     <ellipse cx="112" cy="40" rx="42" ry="36" fill="var(--g1,#d89a62)"/>
     <ellipse cx="36" cy="44" rx="27" ry="23" fill="var(--g2,#e9b27c)"/>
     <ellipse cx="22" cy="58" rx="9" ry="16" fill="#fffaf2"/>
    </g>
    <path d="M30 40 C 32 20 60 12 90 14 C 125 16 145 38 143 60 C 141 80 120 86 90 86 L 45 86 C 22 86 10 74 10 60 C 10 50 20 42 30 40 Z" fill="none"/>
    <path d="M44 32 C 40 20 56 15 62 26 C 61 33 52 37 44 32 Z" fill="#f2b8b0"/>
    <circle cx="35" cy="50" r="4.6" fill="{INK}" stroke="none"/>
    <circle cx="36.4" cy="48.6" r="1.5" fill="#fff" stroke="none"/>
    <ellipse cx="13" cy="60" rx="3.2" ry="2.4" fill="#e57f7f" stroke-width="1.3"/>
    <path d="M14 64 Q17 68 21 65.5" fill="none" stroke-width="1.8"/>
    <ellipse cx="29" cy="64" rx="6" ry="3.8" fill="#f59a9a" stroke="none" opacity=".6"/>
    <path d="M6 57 L-1 55 M6 61 L-1 62" stroke-width="1.2" opacity=".7"/>
   </g>
  </symbol>

  <symbol id="carrot" viewBox="0 0 40 60">
   <g stroke="{INK}" stroke-width="2.2" stroke-linejoin="round" stroke-linecap="round">
    <path d="M20 16 C 10 6 8 2 12 1 C 16 2 18 8 20 14 C 22 6 26 0 30 2 C 32 6 26 12 20 16 Z" fill="#8cc58f"/>
    <path d="M10 18 C 16 13 26 13 30 18 C 32 26 24 48 20 58 C 15 48 7 26 10 18 Z" fill="#f6a04d"/>
    <path d="M14 26 L19 27 M17 36 L22 37 M15 45 L19 45" fill="none" stroke-width="1.6"/>
   </g>
  </symbol>

  <symbol id="seed" viewBox="0 0 20 30">
   <path d="M10 1 C 18 6 19 22 10 29 C 1 22 2 6 10 1 Z" fill="#6f5c4c" stroke="{INK}" stroke-width="1.6"/>
   <path d="M10 5 V25 M6 9 C5 15 5 19 7 24 M14 9 C15 15 15 19 13 24" stroke="#f2e6d6" stroke-width="1.2" fill="none"/>
  </symbol>

  <symbol id="heart" viewBox="0 0 30 28">
   <path d="M15 26 C 4 18 1 12 2 8 C 3 3 10 1 15 7 C 20 1 27 3 28 8 C 29 12 26 18 15 26 Z" fill="var(--hf,#fff)" stroke="{INK}" stroke-width="2" stroke-linejoin="round"/>
  </symbol>

  <symbol id="paw" viewBox="0 0 30 30">
   <g fill="var(--pf,{INK})">
    <ellipse cx="15" cy="20" rx="7.5" ry="6.5"/>
    <ellipse cx="6" cy="11" rx="3" ry="4"/><ellipse cx="12" cy="6" rx="3" ry="4"/>
    <ellipse cx="18" cy="6" rx="3" ry="4"/><ellipse cx="24" cy="11" rx="3" ry="4"/>
   </g>
  </symbol>

  <symbol id="star" viewBox="0 0 30 30">
   <path d="M15 2 L18.6 10.6 L28 11.4 L20.8 17.5 L23 26.6 L15 21.7 L7 26.6 L9.2 17.5 L2 11.4 L11.4 10.6 Z" fill="var(--sf,#fff)" stroke="{INK}" stroke-width="2" stroke-linejoin="round"/>
  </symbol>

  <symbol id="strawberry" viewBox="0 0 34 40">
   <g stroke="{INK}" stroke-width="2" stroke-linejoin="round">
    <path d="M17 10 C 30 8 34 18 28 28 C 24 34 20 38 17 39 C 14 38 10 34 6 28 C 0 18 4 8 17 10 Z" fill="#f47b7b"/>
    <path d="M8 10 L13 6 L17 2 L21 6 L26 10 L20 12 L17 9 L14 12 Z" fill="#8cc58f"/>
   </g>
   <g fill="#fff3c4"><circle cx="11" cy="18" r="1.2"/><circle cx="17" cy="16" r="1.2"/><circle cx="23" cy="18" r="1.2"/><circle cx="14" cy="24" r="1.2"/><circle cx="20" cy="24" r="1.2"/><circle cx="17" cy="31" r="1.2"/><circle cx="25" cy="25" r="1.2"/><circle cx="9" cy="25" r="1.2"/></g>
  </symbol>

  <symbol id="book" viewBox="0 0 50 34">
   <g stroke="{INK}" stroke-width="2" stroke-linejoin="round">
    <path d="M25 6 C 18 1 8 1 2 4 V31 C 8 28 18 28 25 32 C 32 28 42 28 48 31 V4 C 42 1 32 1 25 6 Z" fill="var(--bf,#fff)"/>
    <path d="M25 6 V32" fill="none"/>
    <path d="M7 10 C 12 8 17 8 21 10 M7 15 C 12 13 17 13 21 15 M29 10 C 33 8 38 8 43 10 M29 15 C 33 13 38 13 43 15" fill="none" stroke-width="1.3" opacity=".6"/>
   </g>
  </symbol>

  <symbol id="sun" viewBox="0 0 40 40">
   <g stroke="{INK}" stroke-width="2" stroke-linecap="round">
    <path d="M20 2 V7 M20 33 V38 M2 20 H7 M33 20 H38 M7 7 L10.5 10.5 M29.5 29.5 L33 33 M7 33 L10.5 29.5 M29.5 10.5 L33 7"/>
    <circle cx="20" cy="20" r="9" fill="#ffd66b"/>
   </g>
  </symbol>
  <symbol id="cloud" viewBox="0 0 40 40">
   <path d="M10 30 C 3 30 3 21 10 20 C 10 12 22 10 24 17 C 30 13 37 18 34 24 C 39 26 37 31 32 30 Z" fill="#fff" stroke="{INK}" stroke-width="2" stroke-linejoin="round"/>
  </symbol>
  <symbol id="rain" viewBox="0 0 40 40">
   <path d="M10 24 C 3 24 3 15 10 14 C 10 6 22 4 24 11 C 30 7 37 12 34 18 C 39 20 37 25 32 24 Z" fill="#dce9f5" stroke="{INK}" stroke-width="2" stroke-linejoin="round"/>
   <path d="M12 29 L10 35 M20 29 L18 35 M28 29 L26 35" stroke="#6aa6d6" stroke-width="2.2" stroke-linecap="round"/>
  </symbol>
  <symbol id="snow" viewBox="0 0 40 40">
   <g stroke="{INK}" stroke-width="2" stroke-linecap="round" fill="none">
    <path d="M20 4 V36 M6 12 L34 28 M6 28 L34 12"/>
    <path d="M16 6 L20 10 L24 6 M16 34 L20 30 L24 34"/>
   </g>
  </symbol>

  <symbol id="scissors" viewBox="0 0 30 30">
   <g stroke="#999" stroke-width="1.8" fill="none" stroke-linecap="round">
    <circle cx="7" cy="7" r="4.5"/><circle cx="7" cy="23" r="4.5"/>
    <path d="M10.5 9.5 L28 22 M10.5 20.5 L28 8"/>
   </g>
  </symbol>
 </defs>
</svg>
"""

# Ruh hâli yüzleri: (etiket, gözler+ağız SVG parçası)
def mood_face(kind):
    eyes_open = f'<circle cx="23" cy="31" r="2.6" fill="{INK}"/><circle cx="37" cy="31" r="2.6" fill="{INK}"/>'
    if kind == "mutlu":
        feat = eyes_open + f'<path d="M24 40 Q30 47 36 40" fill="none" stroke="{INK}" stroke-width="2" stroke-linecap="round"/>'
    elif kind == "heyecanlı":
        feat = (f'<path d="M20 32 L23 28 L26 32 M34 32 L37 28 L40 32" fill="none" stroke="{INK}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>'
                f'<path d="M24 39 Q30 49 36 39 Z" fill="#e57f7f" stroke="{INK}" stroke-width="1.8" stroke-linejoin="round"/>')
    elif kind == "sakin":
        feat = (f'<path d="M20 31 Q23 34 26 31 M34 31 Q37 34 40 31" fill="none" stroke="{INK}" stroke-width="2" stroke-linecap="round"/>'
                f'<path d="M26 42 Q30 44 34 42" fill="none" stroke="{INK}" stroke-width="2" stroke-linecap="round"/>')
    elif kind == "üzgün":
        feat = eyes_open + f'<path d="M24 45 Q30 39 36 45" fill="none" stroke="{INK}" stroke-width="2" stroke-linecap="round"/><path d="M38 35 Q39.5 38 38 39.5 Q36.5 38 38 35Z" fill="#7cb7e6"/>'
    else:  # uykulu
        feat = (f'<path d="M20 32 H26 M34 32 H40" stroke="{INK}" stroke-width="2" stroke-linecap="round"/>'
                f'<ellipse cx="30" cy="43" rx="3" ry="3.4" fill="none" stroke="{INK}" stroke-width="1.8"/>'
                f'<text x="45" y="12" font-family="Baloo 2" font-weight="800" font-size="11" fill="{INK}">z</text>')
    return (f'<div class="mood"><svg viewBox="0 0 60 56"><use href="#hhead"/>{feat}</svg>'
            f'<span>{kind}</span></div>')


def icon(name, cls="", style=""):
    return f'<svg class="ic {cls}" style="{style}"><use href="#{name}"/></svg>'


THEMES = {
    "peach": dict(bg="#fff4e6", dot="#ffe1c2", accent="#ffc98b", accent2="#ffd3d3",
                  line="#e6c6a6", h1="#f0a868", g1="#d89a62", g2="#e9b27c"),
    "mint":  dict(bg="#eef7ef", dot="#d7ecd9", accent="#b5dfc0", accent2="#ffe1ad",
                  line="#bad6c0", h1="#e9c08f", g1="#8a7a6e", g2="#b39a86"),
}


def theme_style(t):
    th = THEMES[t]
    return (f"--bg:{th['bg']};--dot:{th['dot']};--accent:{th['accent']};--accent2:{th['accent2']};"
            f"--line:{th['line']};--h1:{th['h1']};--g1:{th['g1']};--g2:{th['g2']};")


def field(label, cls=""):
    return f'<div class="field {cls}"><label>{label}</label><span class="blank"></span></div>'


def book_panel(theme, mascot):
    hearts = "".join(icon("heart", "rate") for _ in range(5))
    if mascot == "hamster":
        hero = icon("hamster", "hero hero-ham")
        foot = icon("guinea", "foot-gp")
        extras = (icon("carrot", "deco", "left:6mm;bottom:3mm;width:8mm;height:12mm;transform:rotate(-25deg)")
                  + icon("seed", "deco", "left:16mm;bottom:3mm;width:4mm;height:6mm;transform:rotate(20deg)"))
    else:
        hero = icon("guinea", "hero hero-gp")
        foot = icon("hamster", "foot-ham")
        extras = (icon("strawberry", "deco", "left:6mm;bottom:3mm;width:8mm;height:10mm;transform:rotate(-15deg)")
                  + icon("seed", "deco", "left:16mm;bottom:3.5mm;width:4mm;height:6mm;transform:rotate(-20deg)"))
    return f"""
<section class="panel" style="{theme_style(theme)}">
 <div class="card">
  <header class="banner">
   {icon("book", "bk")}
   <div>
    <h1>Kitap Özeti</h1>
    <div class="sub">{icon("paw", "pw")} okudum, düşündüm, yazdım! {icon("paw", "pw")}</div>
   </div>
   {hero}
  </header>

  <div class="box info">
   <span class="tag">Kitap Kimliği</span>
   {field("Kitabın Adı:")}
   {field("Yazarı:")}
   <div class="row2">{field("Türü:")}{field("Sayfa Sayısı:")}</div>
   <div class="row2">{field("Başladım:", "date")}{field("Bitirdim:", "date")}</div>
  </div>

  <div class="rating">
   <span class="lbl">Puanım:</span><span class="hearts">{hearts}</span>
   <span class="hint">(boya!)</span>
  </div>

  <div class="row2 gap">
   <div class="box lines small"><span class="tag">Ana Karakterler</span></div>
   <div class="box lines small"><span class="tag t2">Yer &amp; Zaman</span></div>
  </div>

  <div class="box lines grow"><span class="tag">Kitabın Konusu</span></div>

  <div class="box quote"><span class="tag t2">En Sevdiğim Cümle</span>
   <span class="q ql">“</span><span class="q qr">”</span>
  </div>

  <div class="box lines think"><span class="tag">Bu Kitaptan Ne Öğrendim?</span></div>

  {foot}
  {extras}
 </div>
</section>"""


def day_panel(theme, mascot):
    days = "".join(f"<span>{d}</span>" for d in ["Pzt", "Sal", "Çar", "Per", "Cum", "Cmt", "Paz"])
    weather = "".join(icon(w, "wx") for w in ["sun", "cloud", "rain", "snow"])
    moods = "".join(mood_face(k) for k in ["mutlu", "heyecanlı", "sakin", "üzgün", "uykulu"])
    stars = "".join(icon("star", "st") for _ in range(5))
    words = "".join(
        '<div class="word"><span class="blank"></span><span class="arrow">→</span><span class="blank"></span></div>'
        for _ in range(3))
    if mascot == "guinea":
        hero = icon("guinea", "hero hero-gp")
        foot = icon("hamster", "foot-ham")
        extras = icon("carrot", "deco", "left:6mm;bottom:3mm;width:8mm;height:12mm;transform:rotate(-25deg)")
    else:
        hero = icon("hamster", "hero hero-ham")
        foot = icon("guinea", "foot-gp")
        extras = icon("strawberry", "deco", "left:6mm;bottom:3mm;width:8mm;height:10mm;transform:rotate(-15deg)")
    return f"""
<section class="panel" style="{theme_style(theme)}">
 <div class="card">
  <header class="banner">
   {icon("sun", "bk")}
   <div>
    <h1>Bugünün Özeti</h1>
    <div class="sub">{icon("paw", "pw")} bugün neler okudum? {icon("paw", "pw")}</div>
   </div>
   {hero}
  </header>

  <div class="dayrow">
   <div class="field date"><label>Tarih:</label><span class="blank"></span></div>
   <div class="days">{days}</div>
  </div>

  <div class="row2 gap feel">
   <div class="box mini"><span class="tag t2">Hava</span><div class="wxs">{weather}</div></div>
   <div class="box mini moodbox"><span class="tag">Ruh Hâlim</span><div class="moods">{moods}</div></div>
  </div>

  <div class="box info">
   <span class="tag">Bugün Okuduğum</span>
   {field("Kitap:")}
   <div class="row3">{field("Sayfa:", "pg")}<span class="dash">–</span>{field("", "pg2")}{field("Süre:", "min")}<span class="unit">dk</span></div>
  </div>

  <div class="box lines grow"><span class="tag t2">Bugün Okuduklarımın Özeti</span></div>

  <div class="box words"><span class="tag">Yeni Kelimeler</span>
   <div class="wordhead"><span>kelime</span><span>anlamı</span></div>
   {words}
  </div>

  <div class="box quote short"><span class="tag t2">Günün Cümlesi</span>
   <span class="q ql">“</span><span class="q qr">”</span>
  </div>

  <div class="rating stars">
   <span class="lbl">Bugün kendime:</span><span class="hearts">{stars}</span>
  </div>

  {foot}
  {extras}
 </div>
</section>"""


CSS = """
@page { size: A4 landscape; margin: 0; }
* { box-sizing: border-box; -webkit-print-color-adjust: exact; print-color-adjust: exact; }
html, body { margin: 0; padding: 0; background: #fff; }
body { font-family: 'Patrick Hand', 'Baloo 2', sans-serif; color: #5a3e2b; }
.sheet { width: 297mm; height: 210mm; display: flex; position: relative; overflow: hidden;
         page-break-after: always; break-after: page; }
.sheet:last-child { page-break-after: auto; break-after: auto; }
.cut { position: absolute; left: 148.5mm; top: 0; bottom: 0; border-left: 0.6mm dashed #bbb; }
.cut svg { position: absolute; left: -3.2mm; top: 2mm; width: 6mm; height: 6mm; background: #fff; transform: rotate(90deg); }
.panel { width: 148.5mm; height: 210mm; padding: 6mm 6.5mm; }
.card { position: relative; height: 100%; border: 0.7mm solid #5a3e2b; border-radius: 6mm;
        background-color: var(--bg);
        background-image: radial-gradient(var(--dot) 0.9mm, transparent 1mm);
        background-size: 7mm 7mm; background-position: 1.5mm 1.5mm;
        padding: 4mm 5mm 9mm; display: flex; flex-direction: column; gap: 3.6mm; }
.ic { display: block; }
.deco { position: absolute; }

/* başlık */
.banner { display: flex; align-items: center; gap: 3mm; background: var(--accent);
          border: 0.55mm solid #5a3e2b; border-radius: 5mm; padding: 1.5mm 4mm; position: relative;
          height: 21mm; margin-top: 2mm; }
.banner h1 { font-family: 'Baloo 2'; font-weight: 800; font-size: 25pt; line-height: 1; margin: 0; letter-spacing: .3px; }
.banner .sub { font-size: 12pt; display: flex; align-items: center; gap: 1.5mm; margin-top: .6mm; }
.banner .bk { width: 13mm; height: 11mm; flex: none; --bf: #fff; }
.banner .pw { width: 3.6mm; height: 3.6mm; opacity: .55; }
.hero { position: absolute; }
.hero-ham { width: 30mm; height: 28mm; right: 1mm; top: -8.5mm; }
.hero-gp  { width: 37mm; height: 24mm; right: -1mm; top: -6.5mm; }
.foot-gp  { position: absolute; width: 24mm; height: 15.5mm; right: 4mm; bottom: -1.2mm; }
.foot-ham { position: absolute; width: 17mm; height: 16mm; right: 5mm; bottom: -1.2mm; }

/* kutular */
.box { position: relative; background: #fff; border: 0.45mm solid #5a3e2b; border-radius: 3.5mm;
       padding: 4mm 3.5mm 2mm; }
.tag { position: absolute; top: -3.4mm; left: 3.5mm; background: var(--accent);
       border: 0.45mm solid #5a3e2b; border-radius: 3mm; padding: 0 2.6mm; height: 6.2mm;
       font-family: 'Baloo 2'; font-weight: 800; font-size: 10pt; line-height: 6mm; white-space: nowrap; }
.tag.t2 { background: var(--accent2); }

.field { display: flex; align-items: flex-end; gap: 1.5mm; height: 7.4mm; flex: 1; min-width: 0; }
.field label { font-size: 13pt; white-space: nowrap; line-height: 1; padding-bottom: .4mm; }
.field .blank { flex: 1; border-bottom: 0.4mm dotted #5a3e2b; height: 1px; }
.field.date .blank { background: none; }
.info { display: flex; flex-direction: column; gap: 1.6mm; padding-top: 3mm; }
.row2 { display: flex; gap: 5mm; }
.row2.gap > * { flex: 1; }
.row3 { display: flex; align-items: flex-end; gap: 2mm; }
.row3 .pg, .row3 .pg2 { flex: 0.9; }
.row3 .min { flex: 1.2; margin-left: 3mm; }
.row3 .dash, .row3 .unit { font-size: 13pt; padding-bottom: .3mm; }

.lines { background-image: repeating-linear-gradient(to bottom, transparent 0, transparent 6.6mm, var(--line) 6.6mm, var(--line) 7mm);
         background-origin: content-box; background-clip: content-box; }
.lines.small { height: 26mm; }
.lines.grow { flex: 1; min-height: 20mm; }
.lines.think { height: 26mm; }

.rating { display: flex; align-items: center; gap: 2.5mm; padding: 0 2mm; height: 8mm; }
.rating .lbl { font-family: 'Baloo 2'; font-weight: 800; font-size: 13pt; }
.rating .hearts { display: flex; gap: 2mm; }
.rating .rate { width: 8mm; height: 7.4mm; --hf: #fff; }
.rating .st { width: 8mm; height: 8mm; --sf: #fff; }
.rating.stars { padding-left: 15mm; }
.rating .hint { font-size: 11pt; opacity: .7; }

.quote { height: 19mm; }
.quote.short { height: 17mm; }
.quote .q { position: absolute; font-family: 'Baloo 2'; font-weight: 800; font-size: 30pt; color: var(--line); line-height: 1; }
.quote .ql { left: 2mm; top: 2.5mm; }
.quote .qr { right: 2.5mm; bottom: -4mm; }

/* günlük sayfa */
.dayrow { display: flex; align-items: flex-end; gap: 3mm; padding: 0 1mm; }
.dayrow .field { flex: 1; }
.days { display: flex; gap: 1mm; }
.days span { width: 8.4mm; height: 8.4mm; border: 0.4mm solid #5a3e2b; border-radius: 50%; background: #fff;
             font-size: 10pt; display: flex; align-items: center; justify-content: center; }
.feel { gap: 3.5mm; }
.feel > .box:first-child { flex: 0 0 36mm; }
.mini { padding: 4mm 2mm 1.5mm; }
.wxs { display: flex; justify-content: space-around; align-items: center; height: 14mm; }
.wx { width: 8mm; height: 8mm; }
.moods { display: flex; justify-content: space-between; }
.mood { display: flex; flex-direction: column; align-items: center; width: 13mm; }
.mood svg { width: 10.5mm; height: 9.8mm; }
.mood span { font-size: 9pt; line-height: 1; margin-top: .4mm; }

.words { padding-top: 4mm; padding-bottom: 1mm; }
.wordhead { display: flex; justify-content: space-around; font-size: 10pt; opacity: .6; margin: -.5mm 0 -1.5mm; }
.word { display: flex; align-items: flex-end; gap: 2mm; height: 7mm; }
.word .blank { flex: 1; border-bottom: 0.4mm dotted #5a3e2b; }
.word .arrow { font-size: 13pt; line-height: 1; }
.word .blank:last-child { flex: 1.6; }
"""


def page(title, sheets):
    body = "".join(
        f'<div class="sheet">{a}{b}<div class="cut"><svg><use href="#scissors"/></svg></div></div>'
        for a, b in sheets)
    return f"""<!doctype html>
<html lang="tr"><head><meta charset="utf-8"><title>{title}</title>
<style>{FONT_CSS}{CSS}</style></head>
<body>{SPRITE}{body}</body></html>"""


if __name__ == "__main__":
    book = (book_panel("peach", "hamster"), book_panel("mint", "guinea"))
    day = (day_panel("mint", "guinea"), day_panel("peach", "hamster"))
    (HERE / "kitap-ozeti.html").write_text(page("Kitap Özeti", [book]))
    (HERE / "bugunun-ozeti.html").write_text(page("Bugünün Özeti", [day]))
    (HERE / "hepsi.html").write_text(page("Kitap Defteri Sayfaları", [book, day]))
    print("ok")
