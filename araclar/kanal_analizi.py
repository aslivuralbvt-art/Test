#!/usr/bin/env python3
"""Bedenine Yolculuk kanal analizi.

YouTube Studio'nun "Gelişmiş mod" tablosunun dışa aktarımını (CSV) okur, her videoyu
özellikleriyle (konu, açılış, müzik, kapak) eşleştirir, grupları karşılaştırır, bir önceki
analizle kıyaslar ve Markdown rapor yazar.

Kullanım:
  python3 araclar/kanal_analizi.py analizler/veri/2026-11-23.csv
  python3 araclar/kanal_analizi.py analizler/veri/2026-11-23.csv --onceki analizler/veri/2026-11-16.csv

Sütun adları Türkçe ya da İngilizce olabilir; anahtar kelimelerle eşleştirilir.
Video özellikleri: analizler/video-etiketleri.csv (başlıktaki bir anahtar ifadeyle eşleşir).
"""
import argparse, csv, os, re, sys
from datetime import date

KOK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ETIKET = os.path.join(KOK, "analizler", "video-etiketleri.csv")

# sütun -> olası başlık parçaları (küçük harf)
SUTUNLAR = {
    "baslik": ["video başlığı", "video title", "başlık", "title"],
    "icerik": ["içerik", "content"],
    "tarih": ["yayınlanma", "publish"],
    "sure": ["süre", "duration"],
    "goruntuleme": ["görüntüleme", "views"],
    "izlenme_saat": ["izlenme süresi", "watch time"],
    "abone": ["abone", "subscribers"],
    "gosterim": ["gösterimler", "impressions"],
    "tiklama": ["tıklama oranı", "click-through"],
    "ort_sure": ["ortalama görüntüleme süresi", "average view duration"],
    "ort_yuzde": ["ortalama görüntülenme yüzdesi", "ortalama izlenme yüzdesi", "average percentage viewed"],
    "devam": ["izlemeye devam", "stayed to watch", "viewed vs"],
    "begeni": ["beğeni", "likes"],
}


def kucuk(t):
    """Türkçe uyumlu küçük harf (İ→i, I→ı)."""
    return str(t).replace("İ", "i").replace("I", "ı").lower()


def sayi(v):
    if v is None:
        return None
    s = str(v).strip().replace("%", "").replace(" ", "").replace(" ", "")
    if not s or s in ("-", "—"):
        return None
    if re.fullmatch(r"\d+:\d{2}(:\d{2})?", s):  # 0:04 ya da 1:02:03 → saniye
        p = [int(x) for x in s.split(":")]
        return sum(x * 60 ** i for i, x in enumerate(reversed(p)))
    if re.fullmatch(r"\d{1,3}(\.\d{3})+", s):        # 1.312 → binlik ayraç (Türkçe)
        s = s.replace(".", "")
    elif re.fullmatch(r"\d{1,3}(,\d{3})+", s):       # 1,312 → binlik ayraç (İngilizce)
        s = s.replace(",", "")
    elif "," in s and "." in s:
        if s.rfind(",") > s.rfind("."):                  # 1.234,5
            s = s.replace(".", "").replace(",", ".")
        else:                                            # 1,234.5
            s = s.replace(",", "")
    elif "," in s:
        s = s.replace(",", ".")
    try:
        return float(s)
    except ValueError:
        return None


def sutun_bul(basliklar):
    harita = {}
    alt = [kucuk(h).strip() for h in basliklar]
    # uzun eşleşmeler önce (ör. "ortalama görüntüleme süresi" "görüntüleme"den önce)
    adaylar = sorted(((k, p) for k, ps in SUTUNLAR.items() for p in ps), key=lambda x: -len(x[1]))
    for k, p in adaylar:
        if k in harita:
            continue
        for i, h in enumerate(alt):
            if p in h and i not in harita.values():
                if k == "goruntuleme" and ("süre" in h or "yüzde" in h or "duration" in h or "percentage" in h):
                    continue
                harita[k] = i
                break
    return harita


def oku(yol):
    with open(yol, encoding="utf-8-sig") as f:
        satirlar = list(csv.reader(f))
    bas = satirlar[0]
    h = sutun_bul(bas)
    veriler = []
    for r in satirlar[1:]:
        if not r or all(not c.strip() for c in r):
            continue
        d = {k: (r[i] if i < len(r) else "") for k, i in h.items()}
        b = (d.get("baslik") or d.get("icerik") or "").strip()
        if kucuk(b) in ("toplam", "total", ""):
            continue
        d["baslik"] = b
        for k in ("goruntuleme", "izlenme_saat", "abone", "gosterim", "tiklama", "ort_sure", "ort_yuzde", "devam",
                  "begeni", "sure"):
            if k in d:
                d[k] = sayi(d[k])
        veriler.append(d)
    return veriler, h


def etiketler():
    if not os.path.exists(ETIKET):
        return []
    with open(ETIKET, encoding="utf-8") as f:
        return list(csv.DictReader(f))


def etiketle(v, et):
    b = kucuk(v["baslik"])
    for e in et:
        if kucuk(e["anahtar"]) in b:
            return e
    return {}


def fmt(x, n=0, yuzde=False):
    if x is None:
        return "—"
    s = f"{x:,.{n}f}".replace(",", "X").replace(".", ",").replace("X", ".")
    return f"%{s}" if yuzde else s


def ozet(vs):
    g = sum(v.get("goruntuleme") or 0 for v in vs)
    a = sum(v.get("abone") or 0 for v in vs)
    sa = sum(v.get("izlenme_saat") or 0 for v in vs)
    yz = [v["ort_yuzde"] for v in vs if v.get("ort_yuzde") is not None]
    dv = [v["devam"] for v in vs if v.get("devam") is not None]
    return {"n": len(vs), "goruntuleme": g, "abone": a, "saat": sa,
            "abone_1000": (a / g * 1000) if g else None,
            "ort_yuzde": sum(yz) / len(yz) if yz else None,
            "devam": sum(dv) / len(dv) if dv else None}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("veri")
    ap.add_argument("--onceki")
    ap.add_argument("--cikti")
    a = ap.parse_args()

    vs, h = oku(a.veri)
    et = etiketler()
    for v in vs:
        v["et"] = etiketle(v, et)
    vs.sort(key=lambda v: -(v.get("goruntuleme") or 0))
    toplam = ozet(vs)

    onceki = {}
    if a.onceki and os.path.exists(a.onceki):
        for v in oku(a.onceki)[0]:
            onceki[v["baslik"]] = v

    L = []
    L.append(f"# Kanal analizi · {os.path.splitext(os.path.basename(a.veri))[0]}\n")
    L.append(f"Bulunan sütunlar: {', '.join(sorted(h))}\n")
    L.append("## Toplam\n")
    L.append("| Video | Görüntüleme | İzlenme (saat) | Abone | 1.000 görüntülemede abone | Ort. izlenme yüzdesi |")
    L.append("|---|---|---|---|---|---|")
    L.append(f"| {toplam['n']} | {fmt(toplam['goruntuleme'])} | {fmt(toplam['saat'], 1)} | {fmt(toplam['abone'])} | "
             f"{fmt(toplam['abone_1000'], 1)} | {fmt(toplam['ort_yuzde'], 1, True)} |\n")

    L.append("## Videolar\n")
    L.append("| Video | Görüntüleme | Δ önceki | Abone | Ort. izlenme % | Konu | Açılış | Müzik |")
    L.append("|---|---|---|---|---|---|---|---|")
    for v in vs:
        o = onceki.get(v["baslik"])
        delta = None
        if o and o.get("goruntuleme") is not None and v.get("goruntuleme") is not None:
            delta = v["goruntuleme"] - o["goruntuleme"]
        e = v["et"]
        L.append(f"| {v['baslik'][:60]} | {fmt(v.get('goruntuleme'))} | "
                 f"{('+' if (delta or 0) >= 0 else '') + fmt(delta) if delta is not None else '—'} | "
                 f"{fmt(v.get('abone'))} | {fmt(v.get('ort_yuzde'), 1, True)} | {e.get('konu', '?')} | "
                 f"{e.get('acilis', '?')} | {e.get('muzik', '?')} |")
    L.append("")

    for alan, ad in (("konu", "Konuya göre"), ("acilis", "Açılış tarzına göre"), ("muzik", "Müziğe göre")):
        gruplar = {}
        for v in vs:
            gruplar.setdefault(v["et"].get(alan, "etiketsiz") or "etiketsiz", []).append(v)
        if len(gruplar) < 2:
            continue
        L.append(f"## {ad}\n")
        L.append("| Grup | Video | Ort. görüntüleme | 1.000 görüntülemede abone | Ort. izlenme % |")
        L.append("|---|---|---|---|---|")
        for gad, gv in sorted(gruplar.items(), key=lambda x: -ozet(x[1])["goruntuleme"] / max(1, len(x[1]))):
            oz = ozet(gv)
            L.append(f"| {gad} | {oz['n']} | {fmt(oz['goruntuleme'] / max(1, oz['n']))} | "
                     f"{fmt(oz['abone_1000'], 1)} | {fmt(oz['ort_yuzde'], 1, True)} |")
        L.append("")

    etiketsiz = [v["baslik"] for v in vs if not v["et"]]
    if etiketsiz:
        L.append("## Etiketlenmemiş videolar\n")
        L.append("`analizler/video-etiketleri.csv` dosyasına eklenmeli:\n")
        L += [f"- {b}" for b in etiketsiz]
        L.append("")

    rapor = "\n".join(L)
    cikti = a.cikti or os.path.join(KOK, "analizler", f"rapor-{date.today().isoformat()}.md")
    os.makedirs(os.path.dirname(cikti), exist_ok=True)
    with open(cikti, "w", encoding="utf-8") as f:
        f.write(rapor)
    print(rapor)
    print(f"\n[rapor] {cikti}", file=sys.stderr)


if __name__ == "__main__":
    main()
