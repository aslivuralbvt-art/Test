---
name: bedenine-video
description: Bedenine Yolculuk kanalı için gönderilen bir videoyu kanalın standart tarzında düzenler (1080x1920 görüntü iyileştirme, telifsiz orijinal arka plan müziği, konuşma altında müzik kısma, zamanlı ekran yazıları, dikey ve yatay kapak, açıklama metni). Kullanıcı Aslı / Bedenine Yolculuk için yeni bir video gönderdiğinde, "videoyu düzenle", "aynısını uygula", "kapak yap", "müzik ekle", "ekran yazısı ekle" dediğinde kullan.
---

# Bedenine Yolculuk video düzenleme

Tüm adımları `araclar/bedenine_video.py` yapar. Senin işin videoyu izleyip doğru **tarifi**
(JSON) yazmak, aracı çalıştırmak ve sonucu kontrol etmek.
Marka kuralları: `marka-profili.md`. Örnek tarif: `videolar/tarifler/asli-havuz-yoga.json`.

## Adımlar

1. **Kaynağı kopyala.** Gönderilen videoyu `videolar/kaynak/<ad>.mp4` olarak kopyala.
   `<ad>`: küçük harf, Türkçe karaktersiz, tireli (ör. `asli-boyun-esneme`).

2. **Videoyu incele.**
   - Önce kısa bir tarif yaz (sadece `ad`, `kaynak`, `cikti_klasoru`).
   - `python3 araclar/bedenine_video.py videolar/tarifler/<ad>.json --kareler` çalıştır.
   - Çıkan zaman damgalı kare çizelgesine bak: pozlar hangi saniyede değişiyor, karakter
     konuşuyor mu?
   - Sesi kontrol et: `ffmpeg -i <video> -lavfi showspectrumpic=s=1200x400:fscale=log:stop=8000 spec.png`.
     Konuşma, spektrogramda yatay harmonik çizgiler olarak görünür.
   - Konuşma varsa yazıya çevir ki ekran yazıları söylenenle eşleşsin. Gerekirse önce
     `pip install faster-whisper` ile kur. Sesi
     `ffmpeg -i <video> -ar 16000 -ac 1 speech.wav` ile çıkar, numpy dizisi olarak ver
     (dosya yolu verilirse `av` sürüm hatası çıkıyor):
     `WhisperModel('small', device='cpu', compute_type='int8').transcribe(dizi, word_timestamps=True)`.
     Kelime zamanlarını kart zamanlaması için kullan, metni tarifte `konusma` alanına yaz.

3. **Tarifi doldur** (`videolar/tarifler/<ad>.json`):
   - `muzik`:
     - `tohum`: her videoda farklı bir sayı ver (0–3 akor dizisini, arpej desenini değiştirir).
     - `konusma_var`: konuşma varsa `true`. Ses yoksa araç bunu kendisi algılar.
     - `seviye_db`: -4 (konuşmanın yaklaşık 11 dB altı).
     - `yok`: Kullanıcı müzik istemezse `true`. Bu durumda sadece orijinal ses temizlenir
       ve -14 LUFS'a getirilir, müzik dosyası üretilmez.
   - `yazi_y`: Kartların dikey konumu (varsayılan 230). Yüz üstteyse 1050–1180 arası kullan.
     Tek tek kartlar için `y` alanı verilebilir; liste gibi alt alta açılan kartlarda
     yaklaşık 128 px aralık bırak. `"no": ""` verilirse kart numarasız olur (bilgi kartı).
   - `hook`: En fazla 5 kelime, ilk 1.5–2 sn. İsteğe bağlı kısa bir `alt` satırı.
   - `adimlar`: Her poz için bir kart.
     - `baslik`: Poz adı, en fazla 3–4 kelime.
     - `altlar`: 1–2 kısa talimat.
     - `bas` / `bit`: Saniye. Kartlar arka arkaya gelir. Kartlar 0.25 sn'lik geçişle değişir;
       pozun gerçekten başladığı ana göre ayarla.
   - `efektler` (isteğe bağlı): Söylenen kelimeyi görselleştiren animasyonlar. Kelime
     zamanlarını transkriptten al. Örnek:
     `{"tur": "tik", "bas": 5.2, "sure": 1.3, "x": 800, "y": 1230, "boyut": 340}`.
     - Türler: `tik` (onay), `odul` (kupa + konfeti), `hedef` (tahta + ok), `kalp` (atan kalp),
       `gunes` (dönen ışınlı güneş), `su` (damla + halka), `ay` (hilal + yıldızlar), `yildiz` (parlayan yıldız), `hediye` (renkli ambalajlı kutu açılır, konfeti).
     - Her efektin kendi telifsiz ses efekti var. `"ses": false` ile kapatılır, `ses_db` ile
       seviyesi ayarlanır (varsayılan -12; tekrar eden efektlerde -16).
     - Efektleri yüzün ve kartların dışına yerleştir. Animasyonlar `araclar/efektler.py`.
   - `uzat` (isteğe bağlı): Sona son kareyi dondurarak N saniye ekler. Kapanış kartı için
     kullan (ör. "Yarın: …" + CTA), kartın `bas` değerini orijinal video süresine eşitle.
   - `cta`: Son 1.5–2 sn, ör. "Kaydet, yarın sabah dene". Poz kartının altında y=500'de çıkar.
   - `kapak`:
     - `kare`: Yüzün net ve gülümsediği saniye.
     - `etiket`: Kısa konu, BÜYÜK HARF.
     - `buyuk`: 1–2 kelime, BÜYÜK HARF, örneğin süre.
     - `alt`: Fayda cümlesi.
     - `yatay_ikinci_kare`: Hareketin en net göründüğü saniye.
   - `aciklama`: Hook satırı, kısa talimat, CTA, sağlık uyarısı (gerekirse), AI notu,
     en fazla 10 hashtag. AI notu her zaman şu olmalı:
     `🤖 Videodaki görüntüler yapay zekâ ile üretildi`.

4. **Çalıştır.** `python3 araclar/bedenine_video.py videolar/tarifler/<ad>.json` komutunu
   çalıştır (10 sn'lik video yaklaşık 1 dk sürer).

5. **Kontrol et:**
   - Yazılı videodan saniyede 1 kare alıp bak:
     `ffmpeg -i <ad>-1080p-yazili.mp4 -vf "fps=1,scale=216:-1,tile=10x1" -frames:v 1 kontrol.jpg`.
   - Yazılar yüzü kapatmamalı ve doğru pozla eşleşmeli.
   - Yazılar Shorts güvenli alanında kalmalı: üstte y≈230–650. Alt %25'i ve sağ kenarı boş bırak.
   - Kapaklara da bak.
   - Bir sorun varsa tarifi düzelt ve tekrar çalıştır.

6. **Shorts kapak seçenekleri (kullanıcı kapak isterse):**
   - Üç cesur kapak hazırla, hepsi 1080×1920:
     - **A:** Soru + yakın plan yüz
     - **B:** Bölünmüş görüntü (üstte yüz, altta hareket) + sarı şerit
     - **C:** Kısa komut (ör. "DUR. NEFES AL.")
   - Yazı stili: büyük beyaz ve sarı (#FFD640) harfler, koyu kontür, terrakota (#D6623C)
     süre etiketi, üstte küçük "BEDENİNE YOLCULUK" etiketi.
   - Yazıları yüzün üstüne koyma. Yüz üstteyse yazıları gövde hizasına indir ve altına
     sayfanın sonuna kadar uzanan yumuşak bir karartma koy (ani biten geçiş çizgi bırakır).
   - Kapak karesinde gözler açık olmalı; yüz kareleri ızgarasıyla kontrol et.
   - Akış önizlemesi yap (240 px genişlikte üç kapak yan yana) ve okunurluğu kontrol et.
   - Dosyaları `<ad>-shorts-kapak-A/B/C.jpg` olarak kaydet.
   - Kullanıcı seçince tarife şunu ekle ve aracı tekrar çalıştır:
     `"kapak_basa": {"dosya": "../<ad>-shorts-kapak-X.jpg", "sure": 0.5}`.
     Bu adım `<ad>-1080p-yazili-kapakli.mp4` dosyasını üretir: kapak ilk 0.5 sn görünür,
     0.15 sn geçişle videoya bağlanır, ses kesintisiz devam eder.

7. **Teslim et:**
   - Değişiklikleri commit edip push et.
   - Kullanıcıya şu dosyaları SendUserFile ile gönder: `<ad>-1080p-yazili.mp4`, iki kapak,
     ve `<ad>-aciklama.txt` içeriği.
   - YouTube'da "Değiştirilmiş veya sentetik içerik → Evet" seçmesini hatırlat.

## Çıktılar (`videolar/`)
- `<ad>-1080p-yazili-kapakli.mp4`: Kapak seçildiyse yüklenecek ana dosya.
- `<ad>-1080p-yazili.mp4`: Kapak seçilmediyse yüklenecek ana dosya.
- `<ad>-1080p.mp4`: Yazısız sürüm.
- `<ad>-kapak-dikey-1080x1920.jpg`: Shorts, Reels ve TikTok kapağı.
- `<ad>-kapak-yatay-1280x720.jpg`: Yatay YouTube kapağı.
- `<ad>-muzik.wav`: Bu videonun orijinal müziği.
- `<ad>-aciklama.txt`: Açıklama metni.

## Kurallar
- **Sağlık:** Kesin vaat verme ("ağrını geçirir" yazma). Ağrı, bel ya da boyun konularında
  "Ağrın varsa bir uzmana danış" ekle.
- **Müzik:** Hazır parça indirme. Sadece aracın ürettiği müziği kullan. Kullanıcı kendi
  müziğini isterse YouTube Ses Kütüphanesi'ni öner.
- **Görüntü kalitesi:** İyileştirme klasik yöntemle yapılıyor (ffmpeg), AI ile büyütme değil.
  Kullanıcıya böyle anlat; abartma.
- **Video yönü:** Video yatay ya da kare gelirse araç kırparak 9:16'ya getirir. Önemli bir
  kısım kesiliyorsa kullanıcıya söyle.
- **Kontrol:** Müziği dinleyemediğini, sadece seviye ve spektrumla kontrol ettiğini dürüstçe belirt.
