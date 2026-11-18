# Marka Profili: Aslı

## Hesap
- **YouTube kanalı:** Bedenine Yolculuk (sunucu: Aslı)
- **Tür:** Gerçek kişi (Aslı, kanalın yüzü) + videolarda yapay zekâ ile üretilmiş dijital hâli
- **Profil fotoğrafı:** Aslı'nın gerçek fotoğrafı (arka planı flu yeşillik)
- **Niş:** Vakti az olanlar için kısa hareket, esneme ve sağlıklı küçük alışkanlıklar
- **Motto:** Mükemmel değil, sürdürülebilir.
- **Hedef kitle:** 22–40 yaş, masa başı çalışan, spora başlamak isteyen ama vakti olmayanlar
- **Ana platform:** YouTube (Shorts + uzun video)
- **Büyüme platformları:** Instagram Reels, TikTok (aynı videolar)
- **Ton:** Pozitif, sakin, yargılamayan, cesaretlendirici
- **Gelir hedefleri (sırayla):** Marka iş birlikleri → affiliate linkler → kendi dijital programı → YouTube reklam geliri

## Karakter kartı (her promptta aynen kullan)

```
CHARACTER: Aslı, woman in her 30s, soft oval face, grey-green eyes, platinum
ash-blonde hair swept to one side and tied in a loose low bun with a few loose
strands, fair skin, thin round dark metal-frame glasses, berry-red lipstick,
small earrings, warm friendly closed-mouth smile, slim athletic build,
signature outfit: sage green sports crop top, high-waisted charcoal black leggings,
black smartwatch, barefoot on a grey-taupe yoga mat,
vibe: positive, grounded, encouraging
```

Referans görsel: Aslı'nın kendi fotoğrafı (`asli-referans`). AI videolarda yüz
gerçek Aslı'ya benzesin diye her üretimde bu fotoğraf yüklenir.
Mevcut iki park videosu da kullanılır.

## Görsel dünya
- **Mekânlar:** Sabah ışığında yeşil park, sade ve aydınlık bir oturma odası, bitkiler
- **Renk paleti:** Adaçayı yeşili, toprak/terrakota, kum, krem
- **Işık:** Yumuşak sabah ya da altın saat ışığı
- **Format:** 9:16 dikey, en az 1080×1920

## Kurallar
- Her paylaşımda "🤖 Videodaki görüntüler yapay zekâ ile üretildi" notu + platform AI etiketi
  (YouTube: "Değiştirilmiş veya sentetik içerik" → Evet)
- Gerçek fotoğraf ya da gerçek video kullanıldığında bunu AI içerikten ayırarak belirt
- Sağlık konusunda kesin vaat yok ("ağrını bitirir" değil, "rahatlatmaya yardımcı olabilir")
- Ağrı ve sakatlık içeriklerinde: "Ağrın devam ediyorsa bir uzmana danış."
- Sahte yorum, sahte öğrenci hikâyesi ya da uydurma rakam kullanma
- Her video gerçek bir şey öğretmeli: hareketin adı, tekrar sayısı, kime uygun olduğu

## YouTube kanal açıklaması (uzun versiyon)

```
Vakti olmayanlar için günde birkaç dakikalık hareket, esneme ve küçük sağlıklı alışkanlıklar. 🌿

Ben Aslı. Bedenine Yolculuk'ta seni kusursuz bir spor programına değil, her gün atabileceğin küçük adımlara davet ediyorum. Mottomuz: Mükemmel değil, sürdürülebilir.

Bu kanalda neler var?
☀️ Sabah uyanış ve esneme rutinleri
🪑 Masa başı çalışanlar için boyun, bel ve omuz hareketleri
⏱️ Ekipmansız 5–10 dakikalık evde egzersizler
🌙 Uyku öncesi rahatlama hareketleri
🧘 Yeni başlayanlar için yoga ve mobilite

📅 Her gün yeni bir Shorts, her hafta bir uzun rutin.

Kendi temponda ilerle. Bir sağlık sorunun ya da devam eden bir ağrın varsa egzersize başlamadan önce doktoruna veya fizyoterapistine danış.

🤖 Ben gerçek Aslı'yım; vaktim az olduğu için videolardaki görüntülerimi yapay zekâ ile üretiyorum. Hareketleri ve anlatımı ben seçiyorum.

Yolculuğa katılmak için abone ol, hangi bölge için rutin istediğini yorumlara yaz. 💚
```

## Video düzenleme standardı
Her yeni video aynı tarzda düzenlenir: `araclar/bedenine_video.py` + `.claude/skills/bedenine-video/`.
- Görüntü: 1080×1920, hafif gürültü azaltma, keskinlik, sıcak ve canlı renk
- Müzik: Her video için kodla üretilen orijinal, telifsiz, yumuşak müzik (konuşmanın ~11 dB altında, konuşurken kısılır)
- Ses: -14 LUFS (YouTube standardı)
- Ekran yazıları: Üstte hook kartı → numaralı poz kartları (adaçayı rozet) → yeşil CTA etiketi
- Kapak: Dikey 1080×1920 + yatay 1280×720, "BEDENİNE YOLCULUK" etiketi, büyük beyaz başlık

## Kıyafet rotasyonu (18 Kasım 2026)
Aslı (yüz, saç, gözlük) hep aynı; kıyafet videodan videoya değişir ki akışta tekrar hissi olmasın.
- Adaçayı yeşili: `matching sage green athletic set`
- Bordo: `matching burgundy (deep wine red) athletic set`
- Mavi: `matching dusty blue athletic set`
- Toprak: `matching terracotta athletic set`
- Siyah: `matching black athletic set`
Kural: Aynı videonun parçaları (A ve uzatma B) aynı kıyafette olmalı.
