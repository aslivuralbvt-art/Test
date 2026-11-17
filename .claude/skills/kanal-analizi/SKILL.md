---
name: kanal-analizi
description: Bedenine Yolculuk YouTube kanalının performansını analiz eder (YouTube Studio dışa aktarımı Google E-Tablolar/Drive'dan, CSV'den ya da Studio ekran görüntülerinden). Videoları konu, açılış tarzı, müzik ve kapağa göre karşılaştırır, önceki analizle kıyaslar, geçmişe kaydeder ve sonraki hafta için içerik önerileri çıkarır. Kullanıcı "kanal analizini yap", "YouTube verilerimi aktardım", "videolarım nasıl gidiyor", "istatistiklerime bak", "hangi video tuttu" dediğinde ya da Studio ekran görüntüsü gönderdiğinde kullan.
---

# Bedenine Yolculuk kanal analizi

Amaç: Hangi içeriğin (konu, açılış, müzik, kapak) izlenme, izlemeye devam oranı ve abone
getirdiğini bulmak ve bunu bir sonraki videolara uygulamak.

Dosyalar:
- `araclar/kanal_analizi.py`: CSV'yi okur, gruplar, önceki analizle kıyaslar, rapor yazar.
- `analizler/video-etiketleri.csv`: Her videonun özellikleri. Başlıktaki bir **anahtar** ifadeyle
  eşleşir; sütunlar: konu, açılış, müzik, kapak, notlar.
- `analizler/veri/YYYY-MM-DD.csv`: Ham veri arşivi.
- `analizler/rapor-YYYY-MM-DD.md`: Analiz raporları.
- `analizler/gecmis.md`: Her analizin kısa özeti ve alınan kararlar (en yeni en üstte).

## 1. Veriyi al

**A) Google E-Tablolar (tercih edilen).** Kullanıcı Studio'dan dışa aktarmışsa:
1. Google Drive arama aracını yükle (ToolSearch: "Google Drive search files") ve en son
   oluşturulan YouTube Analytics tablosunu bul. Başlıkta genelde "Tablo verileri", "Table data",
   "Analytics" ya da kanal adı geçer; emin değilsen kullanıcıya hangisi olduğunu sor.
2. Google E-Tablolar `get_values` aracıyla tüm aralığı oku.
3. Değerleri olduğu gibi `analizler/veri/<bugünün tarihi>.csv` dosyasına yaz (ilk satır başlıklar).

**B) CSV dosyası.** Kullanıcı CSV gönderdiyse `analizler/veri/<tarih>.csv` olarak kopyala.

**C) Ekran görüntüleri.** Görüntülerdeki sayıları oku ve aynı sütun adlarıyla elle bir CSV oluştur
(Video başlığı, Görüntüleme, Abone, İzlemeye devam edenler %, Ortalama görüntülenme yüzdesi %).
Okunamayan değeri boş bırak, tahmin etme.

**İzlemeye devam edenler oranı** (Shorts akışında kaydırmayanlar) dışa aktarımda çoğunlukla yoktur;
Studio → Analytics → İçerik → Shorts → "İzleyici etkileşimi" ekranının görüntüsünden alınır.
Varsa CSV'ye "İzlemeye devam (%)" sütunu olarak ekle; yoksa kullanıcıdan bu ekranın görüntüsünü iste.

Kullanıcıya dışa aktarma adımları (gerekirse anlat): bilgisayardan studio.youtube.com → Analytics →
sağ üstte "Gelişmiş mod" → tarih aralığı (ör. son 28 gün ya da son 7 gün) → sağ üstteki dışa aktar
simgesi → "Google E-Tablolar". Telefondaki Studio uygulamasında bu özellik yok.

## 2. Videoları etiketle
- Raporun "Etiketlenmemiş videolar" bölümündeki her video için `analizler/video-etiketleri.csv`
  dosyasına bir satır ekle.
- Bilgiyi `videolar/tarifler/*.json` dosyalarından al:
  - müzik: `muzik.stil` / `muzik.yok`
  - açılış: `kapak_basa` varsa "sabit kapak başta", `kirp_bas` varsa "temiz (kırpılmış)",
    hareketle başlıyorsa "hareket", konuşmayla başlıyorsa "temiz (konuşma)"
  - konu: hareket-esneme / nefes-rahatlama / bilgi-hormon / alışkanlık / beslenme
  - notlarda kullanılan efektleri yaz
- Anahtar, başlıkta birebir geçen kısa bir ifade olmalı.
- Kullanıcının kendi yaptığı videoları bilmiyorsan "?" bırak ve kullanıcıya sor.

## 3. Aracı çalıştır
```
python3 araclar/kanal_analizi.py analizler/veri/<tarih>.csv --onceki analizler/veri/<önceki tarih>.csv
```
Önceki dosya yoksa `--onceki` verme. Etiket ekledikten sonra bir kez daha çalıştır.

## 4. Yorumla
Raporu ve `analizler/gecmis.md` dosyasını birlikte oku. Şunlara bak:
1. **İzlemeye devam oranı** (en önemli Shorts metriği): kanal ortalaması ve önceki analiz
   (16 Kasım: ort. %22; en iyi %44,7) ile kıyasla. Açılış tarzına göre grupla: yeni formül
   (temiz açılış, kapak başta yok) eski formülden (sabit kapak başta) iyi mi?
2. **1.000 görüntülemede abone**: hangi konu abone getiriyor? (16 Kasım: nefes-rahatlama öndeydi)
3. **Ortalama izlenme yüzdesi**: video sonuna kadar izleniyor mu? Düşükse hook ya da süre sorunu.
4. **Konu karşılaştırması**: hareket, nefes, bilgi-hormon, alışkanlık, beslenme.
5. **Müzik**: handpan, diğer üretilmiş müzik ya da müziksiz.
6. **Uzun videolar** (varsa): izlenme saati katkısı. 4.000 saat hedefine ne kadar kaldı?

Dürüst ol:
- Az veriyle (tek video, birkaç yüz görüntüleme) kesin sonuç çıkarma; "eğilim" de.
- Videoların yayın süreleri farklıysa (2 gün ve 2 hafta) toplam görüntülemeyi doğrudan karşılaştırma;
  oranlara (devam %, abone/1.000, izlenme %) bak.
- Nedensellik iddia etme; "birlikte görülüyor" de.

## 5. Kaydet ve öner
1. `analizler/gecmis.md` dosyasının **en üstüne** kısa bir özet ekle: tarih, toplamlar,
   en iyi ve en kötü video, test sonuçları, alınan kararlar.
2. Bulgular video üretim kurallarını değiştiriyorsa `.claude/skills/bedenine-video/SKILL.md`
   içindeki "YouTube verilerinden öğrenilenler" bölümünü güncelle.
3. Kullanıcıya Türkçe, kısa bir rapor ver:
   - 3–5 madde ana bulgu (sayılarla)
   - Ne işe yaradı, ne yaramadı
   - Önümüzdeki hafta için 3 somut öneri
   - 2–3 yeni video fikri (en iyi çalışan konu ve formüle göre; istenirse
     `asli-senaryolar-10sn.md` tarzında Gemini promptuyla)
4. Değişiklikleri commit edip push et.

## Kurallar
- Kullanıcının verisini ve kanal bilgilerini dış servislere gönderme.
- Sayıları uydurma. Ekran görüntüsünde okunamayan değeri boş bırak.
- Sağlık içeriği önerilerinde kesin vaat yok ("iyileştirir" değil, "destekler", "yardımcı olabilir").
