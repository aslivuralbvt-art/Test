---
name: bedenine-video
description: Bedenine Yolculuk kanalı için gönderilen bir videoyu kanalın standart tarzında düzenler (1080x1920 görüntü iyileştirme, telifsiz orijinal arka plan müziği, konuşma altında müzik kısma, zamanlı ekran yazıları, dikey ve yatay kapak, açıklama metni). Kullanıcı Aslı / Bedenine Yolculuk için yeni bir video gönderdiğinde, "videoyu düzenle", "aynısını uygula", "kapak yap", "müzik ekle", "ekran yazısı ekle" dediğinde kullan.
---

# Bedenine Yolculuk video düzenleme

Tüm adımları `araclar/bedenine_video.py` yapar. Senin işin videoyu izleyip doğru **tarifi**
(JSON) yazmak, aracı çalıştırmak ve sonucu kontrol etmek.
Marka kuralları: `marka-profili.md`. Örnek tarif: `videolar/tarifler/asli-havuz-yoga.json`.

## YouTube verilerinden öğrenilenler (16 Kasım 2026)
Kanalın "izlemeye devam edenler" oranı: hareket ve müzikle başlayan videolar %22–45,
sabit kapakla ya da konuşma ve büyük yazıyla başlayan videolar %8–16. Bu yüzden varsayılanlar:
- **Başa kapak EKLEME** (`kapak_basa` kullanma). Kapağı `araclar/shorts_kapak.py` ile ayrı
  üret; kullanıcı YouTube'da kapak olarak seçer.
- **İlk kare temiz olsun:** hook kartı `bas` ≥ 0.3 ile başlasın, `boyut` 54–62 (küçük).
- **Baştaki sessizliği kes:** konuşma 0.5 sn'den geç başlıyorsa `kirp_bas` ile kırp
  (konuşma ~0.2 sn'de başlayacak şekilde).
- **Müzik:** varsayılan `"stil": "handpan"` (kanalın en iyi videosu handpan müzikli),
  `seviye_db` -6. Kullanıcı müzik istemezse `"yok": true`.
- **Kapak aracı:**
  `python3 araclar/shorts_kapak.py VIDEO SANIYE CIKTI --etiket ... --satir1 ... --satir2 ... --y ... --ikon ...`.
  Başlığı yüzün altına koy. Kare seçimi: gözler tam açık ve kameraya bakıyor, doğal ve rahat bir
  gülümseme (konuşurken yakalanmış yarım ağız ifadesi değil). 0.1–0.2 sn aralıklarla yüz ızgarası çıkar,
  2–3 adayı büyük boyutta karşılaştır, en doğal gülümsemeyi seç.

## Konu ve ilk kare (24 Kasım 2026)
- **İlk kare: kameraya dönük, gülümseyen yüz.** Profilden ya da eğik başlayan omuz videosu vasat kaldı;
  kameraya gülümseyerek açılan reset hızlı başladı. Promptlarda ACTION ilk cümlesi yüzü kameraya çevirsin.
- **Konu herkese hitap etsin:** uyku, enerji, stres, mutluluk, sabah rutini. Bölgesel ağrı (boyun, omuz)
  konuları zayıf kaldı (eğilim, kesin değil).
- **Süre:** ≤15 sn kısa format (10 sn sayaçlı) test ediliyor.

## Akşam videoları (25 Kasım 2026)
- Sayaç ve tik YOK (görev hissi veriyor). Kartlar sade, `no: ""`. Müzik yavaş handpan (bpm ~60, seviye -8), efekt sesi -20.
- Kapak: `python3 araclar/aksam_kapak.py VIDEO SANIYE CIKTI --etiket "AKŞAM · 10 SANİYE" --satirlar "..." "..." --vurgu N --ay`
  (sıcak koyu ton, italik serif, altın detay). Başlık bir merak sorusu olsun ("Bunu kendine en son ne zaman söyledin?").
- Prompt: konuşma ilk saniyede başlasın, cümleler arasına "..." duraklama koy (yutma ve hızlı geçişi önler).

## Konuşma kontrolü (Gemini telaffuz hataları)
- Her konuşmalı klibi `faster-whisper` **medium** modeliyle yazıya çevir; small model hataları kaçırabiliyor.
- Uzun, çok heceli kelimelere özellikle dikkat et ("esnemesine", "ödüllendirdin" gibi): Gemini hece
  tekrarlayabiliyor ("esnesnemesine") ya da kelime atlayabiliyor.
- **Hece tekrarı varsa kurtarılabilir:** Kelimenin içinde 0.12–0.20 sn'lik pencereleri dene (sesi numpy'de 30 ms
  çapraz geçişle kes), her denemeyi medium modelle yazıya çevir, doğru kelimeyi veren pencereyi seç (çevresindeki
  pencereler de doğruysa sonuç sağlamdır). Aynı aralığı görüntüden `trim` + `concat` ile kes.
  `apad` kullanırken mutlaka `whole_dur` ver; sonsuz apad + concat ffmpeg'de yanıltıcı
  "No space left on device" hatası verir.
- **Kelime atlanmışsa** kurtarılamaz: yeniden üretim öner (cümleyi kısalt, "pronounce every word" ekle).

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
       `gunes` (dönen ışınlı güneş), `su` (damla + halka), `ay` (hilal + yıldızlar), `yildiz` (parlayan yıldız), `hediye` (renkli ambalajlı kutu açılır, konfeti), `sihir` (spiral parıltılar; büyük boyut, kişinin etrafına).
     - Her efektin kendi telifsiz ses efekti var. `"ses": false` ile kapatılır, `ses_db` ile
       seviyesi ayarlanır (varsayılan -12; tekrar eden efektlerde -16).
     - Efektleri yüzün ve kartların dışına yerleştir. Animasyonlar `araclar/efektler.py`.
   - `uzat` (isteğe bağlı): Sona son kareyi dondurarak N saniye ekler. Kapanış kartı için
     kullan (ör. "Yarın: …" + CTA), kartın `bas` değerini orijinal video süresine eşitle.
     Müziksiz videolarda kapanış kartına otomatik yumuşak bir tını eklenir (`kapanis_sesi`),
     böylece video sessiz bitmez.
   - Kontrol: `ffprobe -show_entries stream=duration` ile ses ve görüntü sürelerinin eşit
     olduğunu doğrula (ses kesilmesi hatasını yakalar).
   - `dongu` (isteğe bağlı): `{"bas": 16.4, "bit": 19.95, "tekrar": 5, "gecis": 0.15}`. Bir hareket
     bölümünü çapraz geçişle tekrarlayarak uzatır (döngü kısmında orijinal ses yok, müzik sürer).
     Gemini "uzat" ile gelen 20 sn'lik videolarda hareket genelde son 3–4 sn'dir.
   - `geri_sayim` (isteğe bağlı): `{"bas": 16.5, "sure": 15, "x": 860, "y": 560, "boyut": 300}`.
     Büyük sayaç (halka ilerlemeli), her saniye tık sesi, sonda zil. Sayaç kartları `items`'a eklenir.
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
