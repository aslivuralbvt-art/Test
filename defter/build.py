#!/usr/bin/env python3
"""Kitap özeti defteri sayfaları: A4 yatay, kesilip yapıştırılacak 2 sayfa.

kitap-ozeti   : sol = kitap soruları, sağ = çizgili 'Kitabın Özeti' sayfası
bugunun-ozeti : iki adet çizgili 'Bugünün Özeti' sayfası
"""
from pathlib import Path
from sprites import SPRITE, FONT_CSS, INK

HERE = Path(__file__).parent

PURPLE, PINK, BLUE, GREEN, RED, ORANGE, TEAL = (
    "#7b4fa0", "#b0478a", "#2f6db5", "#2e8b57", "#c0392b", "#d35400", "#1f8a8a")


def use(sym, cls="", style=""):
    return f'<svg class="{cls}" style="{style}"><use href="#{sym}"/></svg>'


# ---- küçük yüzler (alttaki sıra) ----
def face(kind, i):
    eyes = f'<circle cx="23" cy="31" r="2.6" fill="{INK}"/><circle cx="37" cy="31" r="2.6" fill="{INK}"/>'
    smile = f'<path d="M25 40 Q30 46 35 40" fill="none" stroke="{INK}" stroke-width="2" stroke-linecap="round"/>'
    happy_eyes = (f'<path d="M20 32 Q23 28 26 32 M34 32 Q37 28 40 32" fill="none" stroke="{INK}" '
                  f'stroke-width="2" stroke-linecap="round"/>')
    if kind == "h":
        feat = (eyes + smile) if i % 2 else (happy_eyes + smile)
        return f'<svg viewBox="0 0 60 56" class="fc"><use href="#hhead"/>{feat}</svg>'
    ge = (f'<circle cx="22" cy="29" r="3" fill="{INK}"/><circle cx="42" cy="29" r="3" fill="{INK}"/>'
          f'<circle cx="23" cy="28" r="1" fill="#fff"/><circle cx="43" cy="28" r="1" fill="#fff"/>')
    if i % 3 == 0:
        ge = (f'<path d="M18 30 Q22 26 26 30 M38 30 Q42 26 46 30" fill="none" stroke="{INK}" '
              f'stroke-width="2" stroke-linecap="round"/>')
    return f'<svg viewBox="0 0 64 56" class="fc"><use href="#ghead"/>{ge}</svg>'


PALETTES = [  # (--h1 / --g1, --g2)
    "--h1:#f0a868", "--g1:#d89a62;--g2:#e9b27c", "--h1:#e9c08f", "--g1:#8a7a6e;--g2:#b39a86",
    "--h1:#f3b98a", "--g1:#3f3a36;--g2:#d89a62", "--h1:#dcc6a8", "--g1:#c97b4a;--g2:#f0d2a8",
]


def face_row(cls="faces"):
    items = []
    for i in range(8):
        kind = "h" if i % 2 == 0 else "g"
        items.append(f'<span style="{PALETTES[i]}">{face(kind, i)}</span>')
    return f'<div class="{cls}">{"".join(items)}</div>'


# ---- sol sayfa: sorular ----
def q(label, color, extra=0, cls="", inline=None):
    """Bir soru: etiket + noktalı satır, ardından 'extra' kadar boş satır."""
    style = f"--c:{color}"
    head = f'<div class="ln"><b>{label}</b><i></i></div>' if inline is None else inline
    more = "".join('<div class="ln"><i></i></div>' for _ in range(extra))
    return f'<div class="q {cls}" style="{style}">{head}{more}</div>'


def questions_page():
    dates = (f'<div class="ln dates">'
             f'<b style="color:{PINK}">Sayfa Sayısı:</b><i style="border-color:{PINK}"></i>'
             f'<b style="color:{BLUE}">Başlangıç Tarihi:</b><i style="border-color:{BLUE}"></i>'
             f'<b style="color:{GREEN}">Bitiş Tarihi:</b><i style="border-color:{GREEN}"></i></div>')
    reader = (
        '<div class="art art-reader">'
        + use("hamster", "a-ham")
        + use("book", "a-book", "--bf:#fff7d6")
        + '</div>')
    garden = (
        '<div class="art art-garden">'
        + use("leaf", "", "left:0;bottom:2mm;width:9mm;height:6mm;transform:rotate(-20deg)")
        + use("leaf", "", "right:0;bottom:3mm;width:9mm;height:6mm;transform:scaleX(-1) rotate(-20deg)")
        + use("flower", "", "left:2mm;top:2mm;width:6mm;height:6mm")
        + use("flower", "", "right:1mm;top:0;width:6.5mm;height:6.5mm;--ff:#c9b6f2")
        + use("guinea", "a-gp")
        + use("book", "a-book2", "--bf:#fff7d6")
        + use("carrot", "", "left:-1mm;bottom:-1mm;width:5mm;height:8mm;transform:rotate(-35deg)")
        + use("strawberry", "", "right:2mm;bottom:-1mm;width:5mm;height:6mm")
        + '</div>')
    return f"""
<section class="panel left">
 <div class="qs">
  <div class="grp top">
   {q("Kitabın Adı:", PURPLE)}
   {q("", PURPLE, inline=dates)}
   {q("Kitabın Yazarı:", PURPLE)}
   {reader}
  </div>
  {q("Kitabın Konusu:", RED, 3)}
  <div class="grp mid">
   {q("Kitabın Kahramanları:", PURPLE, 2, "short")}
   {q("Kitabın Anafikri:", BLUE, 1, "short")}
   {garden}
  </div>
  {q("En Çok Etkilendiğim Bölüm:", ORANGE, 2)}
  {q("En Sevdiğim Karakter:", PURPLE)}
  {q("Kitabı Tavsiye Eder Misin?", PINK)}
  {q("Kitabın Yazarı Sen Olsaydın Sonunu Nasıl Bitirirdin?", GREEN, 1)}
  {q("Kitabın Yazarı Sen Olsaydın Adını Ne Koyardın?", TEAL)}
  {q("Genel Olarak Kitapla Alakalı Düşüncem:", BLUE, 1)}
  {q("Sevdim. Çünkü:", PURPLE)}
  {q("Sevmedim. Çünkü:", PURPLE)}
 </div>
 {face_row()}
</section>"""


# ---- çizgili sayfa (özet) ----
def lined_page(title, sub=None, flip=False):
    left = ('<div class="hd-l">' + use("hamster", "h-ham") + use("pencil", "h-pen") + '</div>')
    right = ('<div class="hd-r">' + use("guinea", "h-gp") + use("book", "h-book", "--bf:#fff7d6") + '</div>')
    if flip:
        left, right = (('<div class="hd-l">' + use("guinea", "h-gp flipx") + use("pencil", "h-pen2") + '</div>'),
                       ('<div class="hd-r">' + use("hamster", "h-ham") + use("book", "h-book2", "--bf:#fff7d6") + '</div>'))
    sub_html = f'<div class="subrow">{sub}</div>' if sub else ""
    return f"""
<section class="panel right">
 <header class="hd">{left}<h2>{title}</h2>{right}</header>
 {sub_html}
 <div class="ruled"></div>
 {face_row("faces ghost")}
</section>"""


DAY_SUB = (f'<div class="ln" style="--c:{PURPLE}"><b>Tarih:</b><i></i></div>'
           f'<div class="ln" style="--c:{BLUE}"><b>Okuduğum Kitap:</b><i></i></div>'
           f'<div class="ln" style="--c:{GREEN}"><b>Okuduğum Sayfalar:</b><i></i>'
           f'<b style="color:{INK}">–</b><i></i></div>')


CSS = """
@page { size: A4 landscape; margin: 0; }
* { box-sizing: border-box; -webkit-print-color-adjust: exact; print-color-adjust: exact; }
html, body { margin: 0; padding: 0; background: #fff; }
body { font-family: 'Baloo 2', sans-serif; color: #5a3e2b; }
.sheet { width: 297mm; height: 210mm; display: flex; position: relative; overflow: hidden;
         break-after: page; }
.sheet:last-child { break-after: auto; }
.cut { position: absolute; left: 148.5mm; top: 0; bottom: 0; border-left: 0.5mm dashed #c8c8c8; }
.cut svg { position: absolute; left: -3.2mm; top: 2mm; width: 6mm; height: 6mm; background: #fff; transform: rotate(90deg); }
.panel { width: 148.5mm; height: 210mm; padding: 9mm 9mm 5mm 10mm; position: relative;
         display: flex; flex-direction: column; }
svg { display: block; overflow: visible; }

/* satırlar */
.ln { display: flex; align-items: flex-end; gap: 1.2mm; height: 6.55mm; }
.ln b { font-weight: 600; font-size: 11.5pt; line-height: 1; white-space: nowrap; color: var(--c); padding-bottom: .5mm; }
.ln i { flex: 1; min-width: 6mm; border-bottom: 0.45mm dotted var(--c); opacity: .85; }
.ln.dates { gap: 1mm; }
.ln.dates i { flex: 1; margin-right: 2mm; }

/* sol sayfa */
.qs { flex: 1; display: flex; flex-direction: column; justify-content: space-between; }
.grp { position: relative; }
.grp.top .q { padding-right: 23mm; }
.ln.dates b { font-size: 10.5pt; }
.grp.mid .q { padding-right: 30mm; }
.art { position: absolute; }
.art svg { position: absolute; }
.art-reader { right: -2mm; top: -6mm; width: 24mm; height: 24mm; }
.a-ham { width: 24mm; height: 22mm; left: 0; top: 0; }
.a-book { width: 15mm; height: 10mm; left: 4.5mm; top: 14mm; transform: rotate(-4deg); }
.art-garden { right: -2mm; top: 0; width: 30mm; height: 27mm; }
.a-gp { width: 26mm; height: 16.5mm; left: 2mm; top: 5mm; }
.a-book2 { width: 13mm; height: 9mm; left: 7.5mm; top: 16mm; transform: rotate(6deg); }

.faces { display: flex; justify-content: center; gap: 2mm; height: 13mm; margin-top: 2mm; }
.faces .fc { width: 13mm; height: 12mm; }
.faces.ghost { opacity: .22; }

/* sağ sayfa */
.hd { display: flex; align-items: center; justify-content: space-between; height: 25mm; }
.hd h2 { margin: 0; font-weight: 800; font-size: 24pt; line-height: 1; text-align: center; flex: 1; color: #c0392b; }
.hd-l, .hd-r { position: relative; width: 30mm; height: 25mm; flex: none; }
.hd-l svg, .hd-r svg { position: absolute; }
.h-ham { width: 25mm; height: 23mm; left: 2mm; top: 1mm; }
.h-pen { width: 3.5mm; height: 16mm; left: 21mm; top: 6mm; transform: rotate(25deg); }
.h-gp  { width: 30mm; height: 19mm; left: 0; top: 4mm; }
.h-gp.flipx { transform: scaleX(-1); }
.h-pen2 { width: 3.5mm; height: 16mm; left: 1mm; top: 6mm; transform: rotate(-25deg); }
.h-book { width: 13mm; height: 9mm; left: 1mm; top: 15mm; transform: rotate(-8deg); }
.h-book2 { width: 14mm; height: 9.5mm; left: 7.5mm; top: 14.5mm; transform: rotate(-4deg); }
.hd h2 { background: linear-gradient(transparent 62%, #ffe08a 62%, #ffe08a 88%, transparent 88%);
         display: inline; }
.hd .ttl { flex: 1; text-align: center; }

.subrow { display: flex; flex-direction: column; gap: .8mm; margin: 1mm 0 2mm; }
.ruled { flex: 1; margin-top: 1mm; background-position: 0 0;
         background-image: repeating-linear-gradient(to bottom, transparent 0, transparent 7.5mm, #eebcbc 7.5mm, #eebcbc 8mm); }
"""


def html(title, sheets):
    body = "".join(
        f'<div class="sheet">{a}{b}<div class="cut"><svg><use href="#scissors"/></svg></div></div>'
        for a, b in sheets)
    return (f'<!doctype html><html lang="tr"><head><meta charset="utf-8"><title>{title}</title>'
            f'<style>{FONT_CSS}{CSS}</style></head><body>{SPRITE}{body}</body></html>')


if __name__ == "__main__":
    book = (questions_page(), lined_page("Kitabın Özeti"))
    day = (lined_page("Bugünün Özeti", DAY_SUB), lined_page("Bugünün Özeti", DAY_SUB, flip=True))
    (HERE / "kitap-ozeti.html").write_text(html("Kitap Özeti", [book]))
    (HERE / "bugunun-ozeti.html").write_text(html("Bugünün Özeti", [day]))
    (HERE / "hepsi.html").write_text(html("Kitap Defteri Sayfaları", [book, day]))
    print("ok")
