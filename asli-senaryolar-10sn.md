# Bedenine Yolculuk: 10 saniyelik video senaryoları

Bu senaryolar Gemini'de (Veo) üretilecek 10 saniyelik, konuşmalı videolar için yazıldı.
Her senaryoda şunlar var:
- Aslı'nın söyleyeceği Türkçe metin (en fazla 22 kelime; 10 saniyeye sığıyor)
- Gemini'ye yapıştırılacak İngilizce prompt
- Ekran yazısı planı
- Kapak fikri
- Açıklama metni

Video geldikten sonra düzenleme, ekran yazıları ve kapak her zamanki gibi
`araclar/bedenine_video.py` ile yapılır.

---

## Tıklanma, izlenme ve abone getiren 6 kural (bütün senaryolarda uygulandı)

1. **İlk 2 saniyede hook.** Videoya "Merhaba" ile değil, bir soru, şaşırtıcı bir bilgi ya da
   doğrudan "sen" diye hitap ederek başla.
2. **Seri formatı.** "Mutluluk Hormonları 2/4" gibi numaralı seriler bir sonraki bölüm için
   takip etme sebebi yaratır. Abone kazandıran en güçlü araç bu.
3. **Tek fikir, tek eylem.** Her video tek bir şey öğretir ve izleyici bunu hemen deneyebilir.
4. **Yarın kancası.** Serinin son kartında "Yarın: Serotonin → takip et" yazar.
5. **Yorum sorusu.** Açıklamada ve gerektiğinde konuşmada tek bir basit soru sor
   ("Sen hangisini yapıyorsun?"). Yorumlar videonun daha çok kişiye gösterilmesine yardım eder.
6. **Döngü (loop).** Son cümle ilk sahneye doğal bağlansın; video baştan oynadığında kopukluk
   hissedilmesin. Tekrar izlenme, izlenme süresini artırır.

**Sağlık dili:** Hormonlar ve beden hakkında kesin vaat yok. "İyileştirir" ya da "geçirir"
yerine "destekler", "ilişkilidir", "iyi gelebilir" gibi ifadeler kullanıldı.

---

## Gemini (Veo) için ortak prompt kalıbı

Her senaryonun promptu bu kalıpla yazıldı. Önceki videolardaki Aslı'ya benzesin diye
**referans fotoğrafınızı da yükleyin.**

```
Vertical 9:16 video, 10 seconds, photorealistic, natural UGC style.
CHARACTER: Aslı, a woman in her late 30s, soft oval face, grey-green eyes,
platinum ash-blonde hair swept to one side in a loose low bun with loose strands,
thin round dark metal-frame glasses, berry-red lipstick, small gold hoop earrings,
warm friendly smile.
[SAHNE / KIYAFET / EYLEM]
She looks into the camera and speaks in Turkish, clearly and warmly: "[METİN]"
Camera: [kamera]. Lighting: [ışık].
No subtitles, no on-screen text, no background music, no logo.
```

> "No background music" satırı bilerek eklendi. Müziğe biz karar veriyoruz
> (ekliyoruz ya da hiç koymuyoruz).

---

# SERİ 1: Mutluluk Hormonları (4 bölüm)
*1/4 Oksitosin yayında. Aşağıdakiler 2/4, 3/4 ve 4/4.*

Serinin her videosu aynı sahne yapısını kullanır. Seri, aynı formatı görünce tanınsın.
Kapakta küçük "MUTLULUK HORMONLARI 2/4" etiketi olur.

## 1. Dopamin (Mutluluk Hormonları 2/4)

**Konuşma (18 kelime):**
> "Dopamin, motivasyon ve ödül demek. Küçük bir hedef koy, bitirince tik at. Her tik, beynine minik bir ödül."

**Prompt:**
```
Vertical 9:16 video, 10 seconds, photorealistic, natural UGC style.
CHARACTER: Aslı, a woman in her late 30s, soft oval face, grey-green eyes,
platinum ash-blonde hair swept to one side in a loose low bun with loose strands,
thin round dark metal-frame glasses, berry-red lipstick, small gold hoop earrings,
warm friendly smile.
She sits at a bright wooden kitchen table with a cup of coffee and an open paper
notebook, wearing a cream knit sweater. Halfway through, she ticks a box in the
notebook with a pen and smiles proudly at the camera.
She looks into the camera and speaks in Turkish, clearly and warmly:
"Dopamin, motivasyon ve ödül demek. Küçük bir hedef koy, bitirince tik at. Her tik, beynine minik bir ödül."
Camera: static, medium close-up, eye level, slow subtle push-in.
Lighting: soft morning window light.
No subtitles, no on-screen text, no background music, no logo.
```

**Ekran yazıları:**
- 0–2.5 sn: **Dopamin nedir?** · *Motivasyon ve ödül*
- 2.5 sn sonrası: **① Küçük bir hedef koy** → **② Bitirince tik at ✓**
- Son 1.5 sn: **Yarın: Serotonin → takip et**

**Kapak:** "MOTİVASYONUN YOK MU?", alt satırda "Dopamin · 2/4"

**Açıklama:**
```
Motivasyonun yok mu? Belki dopaminin bir ödüle ihtiyacı var ✓
Bugün tek küçük hedef koy, bitirince tik at.

Bugünkü küçük hedefin ne? Yorumlara yaz 👇
Mutluluk Hormonları serisi 2/4 · Yarın: Serotonin

🤖 Videodaki görüntüler yapay zekâ ile üretildi
#bedenineyolculuk #dopamin #motivasyon #mutlulukhormonları #küçükadımlar #shorts
```

**Neden işe yarar:** "Motivasyonum yok" çok aranan bir derdi hedefliyor. Çözüm hemen
uygulanabilir. Yorum sorusu kolay cevaplanıyor.

---

## 2. Serotonin (Mutluluk Hormonları 3/4)

**Konuşma (17 kelime):**
> "Serotonin, huzur ve denge demek. Sabah gün ışığına çık, on dakika yürü. Ruh hâlin bunu fark edecek."

**Prompt:**
```
Vertical 9:16 video, 10 seconds, photorealistic, natural UGC style.
CHARACTER: Aslı, a woman in her late 30s, soft oval face, grey-green eyes,
platinum ash-blonde hair swept to one side in a loose low bun with loose strands,
thin round dark metal-frame glasses, berry-red lipstick, small gold hoop earrings,
warm friendly smile.
She walks slowly along a sunny tree-lined park path in the early morning, wearing a
sage green light jacket over a white t-shirt, holding the phone at arm's length like
a selfie vlog, sunlight flickering through leaves on her face.
She looks into the camera and speaks in Turkish, clearly and warmly:
"Serotonin, huzur ve denge demek. Sabah gün ışığına çık, on dakika yürü. Ruh hâlin bunu fark edecek."
Camera: handheld selfie angle, gentle walking motion.
Lighting: golden morning sunlight, soft lens flare.
No subtitles, no on-screen text, no background music, no logo.
```

**Ekran yazıları:**
- 0–2.5 sn: **Serotonin nedir?** · *Huzur ve denge*
- Sonra: **☀️ Sabah gün ışığı** → **🚶 10 dakika yürüyüş**
- Son 1.5 sn: **Yarın: Endorfin → takip et**

**Kapak:** "SABAH 10 DAKİKA", alt satırda "Serotonin · 3/4"

**Açıklama:**
```
Huzur için sabah 10 dakika ☀️
Gün ışığı ve kısa bir yürüyüş, serotoninle ilişkilendirilen iki basit alışkanlık.

Sabahları dışarı çıkabiliyor musun? 👇
Mutluluk Hormonları serisi 3/4 · Yarın: Endorfin

🤖 Videodaki görüntüler yapay zekâ ile üretildi
#bedenineyolculuk #serotonin #sabahrutini #yürüyüş #mutlulukhormonları #shorts
```

---

## 3. Endorfin (Mutluluk Hormonları 4/4, final)

**Konuşma (15 kelime):**
> "Endorfin, bedeninin doğal iyi hissetme kimyasalı. Hareket et, dans et, kahkaha at. Bugün hangisini yapacaksın?"

**Prompt:**
```
Vertical 9:16 video, 10 seconds, photorealistic, natural UGC style.
CHARACTER: Aslı, a woman in her late 30s, soft oval face, grey-green eyes,
platinum ash-blonde hair swept to one side in a loose low bun with loose strands,
thin round dark metal-frame glasses, berry-red lipstick, small gold hoop earrings,
warm friendly smile.
She is in a bright cozy living room with plants, wearing a terracotta athleisure set.
She starts speaking to the camera, then does a few playful dance moves and bursts
into genuine laughter, then looks back at the camera with a big smile.
She speaks in Turkish, clearly and joyfully:
"Endorfin, bedeninin doğal iyi hissetme kimyasalı. Hareket et, dans et, kahkaha at. Bugün hangisini yapacaksın?"
Camera: static, full-body to medium shot, eye level.
Lighting: bright natural daylight.
No subtitles, no on-screen text, no background music, no logo.
```

**Ekran yazıları:**
- 0–2.5 sn: **Endorfin nedir?** · *Doğal iyi hissetme kimyasalı*
- Sonra: **① Hareket et** → **② Dans et** → **③ Kahkaha at**
- Son 1.5 sn: **Serinin tamamı profilde 💚**

**Kapak:** "DANS ET, GÜL, İYİ HİSSET", alt satırda "Endorfin · 4/4"

**Açıklama:**
```
Endorfin: bedeninin doğal iyi hissetme kimyasalı 💃
Hareket et, dans et, kahkaha at.

Bugün hangisini yapacaksın? 1, 2 ya da 3 yaz 👇
Mutluluk Hormonları serisi 4/4 · Serinin tamamı profilde

🤖 Videodaki görüntüler yapay zekâ ile üretildi
#bedenineyolculuk #endorfin #dans #mutlulukhormonları #iyihisset #shorts
```

**Seri ipucu:** 4 video yayınlanınca YouTube'da **"Mutluluk Hormonları" oynatma listesi**
oluşturun. Shorts'ta videonun altında görünür ve izleyiciyi seriyi bitirmeye yönlendirir.

---

# SERİ 2: 10 Saniyede Rahatla (pratik)

## 4. Masa başı boyun

**Konuşma (17 kelime):**
> "Ekrana bakarken çenen öne mi kaçıyor? Çeneni düz geriye çek, beş saniye tut, bırak. Üç kez tekrarla."

**Prompt:**
```
Vertical 9:16 video, 10 seconds, photorealistic, natural UGC style.
CHARACTER: Aslı, a woman in her late 30s, soft oval face, grey-green eyes,
platinum ash-blonde hair swept to one side in a loose low bun with loose strands,
thin round dark metal-frame glasses, berry-red lipstick, small gold hoop earrings,
warm friendly smile.
She sits at a home office desk with a laptop, wearing an oversized cream cardigan.
First she leans her head forward toward the screen with a tired face, then sits up
straight and slowly draws her chin straight back, holds, and releases with a smile.
She speaks in Turkish, clearly and warmly:
"Ekrana bakarken çenen öne mi kaçıyor? Çeneni düz geriye çek, beş saniye tut, bırak. Üç kez tekrarla."
Camera: static, side three-quarter angle, chest-up framing.
Lighting: soft daylight from a window.
No subtitles, no on-screen text, no background music, no logo.
```

**Ekran yazıları:**
- 0–2.5 sn: **Çenen öne mi kaçıyor? 😬**
- Sonra: **Çeneni geri çek** · *5 sn tut · 3 tekrar*
- Son: **Masa başı arkadaşına gönder 📩**

**Kapak:** "BU HATAYI YAPIYOR MUSUN?"

**Açıklama:**
```
Ekrana bakarken çenen öne mi kaçıyor? 😬
Çeneni düz geriye çek, 5 sn tut, bırak. 3 tekrar.

Ağrın varsa bir uzmana danış.
Masa başında çalışan arkadaşına gönder 📩

🤖 Videodaki görüntüler yapay zekâ ile üretildi
#bedenineyolculuk #masabaşı #boyunegzersizi #duruş #ofisegzersizi #shorts
```

**Neden işe yarar:** "Bu hatayı yapıyor musun?" merak uyandırır. "Arkadaşına gönder"
paylaşımı artırır, paylaşım da yeni izleyici getirir.

---

## 5. Uyumadan önce kutu nefesi

**Konuşma (18 kelime):**
> "Uyuyamıyor musun? Dört saniye al, dört tut, dört ver, dört bekle. Buna kutu nefesi denir. Üç tur dene."

**Prompt:**
```
Vertical 9:16 video, 10 seconds, photorealistic, cozy calm style.
CHARACTER: Aslı, a woman in her late 30s, soft oval face, grey-green eyes,
platinum ash-blonde hair swept to one side in a loose low bun with loose strands,
thin round dark metal-frame glasses, berry-red lipstick, small gold hoop earrings,
warm friendly smile.
She sits in bed against soft pillows at night, wearing a light linen pajama shirt,
a warm bedside lamp glowing. She speaks softly and slowly, breathing calmly,
tracing a small square in the air with her finger as she counts.
She speaks in Turkish, softly and calmly:
"Uyuyamıyor musun? Dört saniye al, dört tut, dört ver, dört bekle. Buna kutu nefesi denir. Üç tur dene."
Camera: static, medium close-up, eye level.
Lighting: warm dim bedside lamp, cozy night atmosphere.
No subtitles, no on-screen text, no background music, no logo.
```

**Ekran yazıları:**
- 0–2.5 sn: **Uyuyamıyor musun? 🌙**
- Sonra: **4 al → 4 tut → 4 ver → 4 bekle** (sırayla dört kart)
- Son: **Bu gece dene, kaydet 🔖**

**Kapak:** "UYUYAMIYOR MUSUN?", alt satırda "Kutu nefesi"

**Açıklama:**
```
Uyuyamıyor musun? 🌙 Kutu nefesini dene:
4 sn al · 4 sn tut · 4 sn ver · 4 sn bekle. 3 tur.

Baş dönmesi hissedersen normal nefesine dön.
Bu gece dene ve kaydet 🔖

🤖 Videodaki görüntüler yapay zekâ ile üretildi
#bedenineyolculuk #uyku #kutunefesi #nefesegzersizi #rahatla #shorts
```

**Paylaşım saati:** Akşam 22:00 civarı. Konu, izleyicinin o anki durumuyla örtüşür.

---

## 6. Önce su, sonra kahve

**Konuşma (17 kelime):**
> "Güne kahveyle mi başlıyorsun? Gece boyunca hiç su içmedin. Önce bir bardak su, sonra kahve. Anlaştık mı?"

**Prompt:**
```
Vertical 9:16 video, 10 seconds, photorealistic, natural UGC style.
CHARACTER: Aslı, a woman in her late 30s, soft oval face, grey-green eyes,
platinum ash-blonde hair swept to one side in a loose low bun with loose strands,
thin round dark metal-frame glasses, berry-red lipstick, small gold hoop earrings,
warm friendly smile.
In a bright kitchen in the morning, wearing a white linen shirt, she reaches for a
coffee cup, playfully stops herself, puts it down and instead picks up a glass of
water, raising it to the camera with a wink.
She speaks in Turkish, warmly and playfully:
"Güne kahveyle mi başlıyorsun? Gece boyunca hiç su içmedin. Önce bir bardak su, sonra kahve. Anlaştık mı?"
Camera: static, medium shot, eye level.
Lighting: bright morning sunlight through a window.
No subtitles, no on-screen text, no background music, no logo.
```

**Ekran yazıları:**
- 0–2.5 sn: **Güne kahveyle mi başlıyorsun? ☕**
- Sonra: **① Önce bir bardak su 💧** → **② Sonra kahve ☕**
- Son: **Yarın sabah dene**

**Kapak:** "KAHVEDEN ÖNCE BUNU YAP"

**Açıklama:**
```
Kahveden önce bunu yap 💧
Gece boyunca su içmedin. Önce bir bardak su, sonra kahve.

Sen sabah ilk ne içiyorsun? ☕ mi 💧 mu? 👇

🤖 Videodaki görüntüler yapay zekâ ile üretildi
#bedenineyolculuk #sabahrutini #su #sağlıklıalışkanlık #kahve #shorts
```

**Neden işe yarar:** Kahve çok geniş bir kitleye hitap ediyor. "☕ mi 💧 mu?" sorusu
tek emojiyle cevaplanabildiği için çok yorum alır.

---

# SERİ 3: Mit mi, Gerçek mi? (yorum ve tartışma getirir)

## 7. 10 bin adım şart mı?

**Konuşma (20 kelime):**
> "Günde on bin adım şart mı? Aslında bilimsel bir kural değil. Her ek adım sayılır. Bugün dünden biraz fazla yürü."

**Prompt:**
```
Vertical 9:16 video, 10 seconds, photorealistic, natural UGC style.
CHARACTER: Aslı, a woman in her late 30s, soft oval face, grey-green eyes,
platinum ash-blonde hair swept to one side in a loose low bun with loose strands,
thin round dark metal-frame glasses, berry-red lipstick, small gold hoop earrings,
warm friendly smile.
She walks in a green park wearing a sage green zip jacket, then stops, glances at
her smartwatch, raises an eyebrow at the camera, and shakes her head with a smile.
She speaks in Turkish, confidently and warmly:
"Günde on bin adım şart mı? Aslında bilimsel bir kural değil. Her ek adım sayılır. Bugün dünden biraz fazla yürü."
Camera: handheld, medium shot, slight walking motion then still.
Lighting: soft afternoon daylight.
No subtitles, no on-screen text, no background music, no logo.
```

**Ekran yazıları:**
- 0–2.5 sn: **10.000 adım şart mı? 🤔**
- Sonra: **❌ Bilimsel bir kural değil** → **✅ Her ek adım sayılır**
- Son: **Bugün kaç adım attın? 👇**

**Kapak:** "10.000 ADIM ŞART MI?", "MİT" etiketiyle

**Açıklama:**
```
10.000 adım şart mı? 🤔
Bu sayı bilimsel bir kural değil. Her ek adım önemlidir.
Bugün dünden biraz fazla yürü.

Bugün kaç adım attın? Yorumlara yaz 👇

🤖 Videodaki görüntüler yapay zekâ ile üretildi
#bedenineyolculuk #10binadım #yürüyüş #mitvegerçek #sağlıklıyaşam #shorts
```

**Neden işe yarar:** Herkesin bildiği bir "kuralı" sorgulamak merak uyandırır.
"Kaç adım attın?" sorusu sayıyla cevaplandığı için yorum yazmak kolay.

---

## 8. Esneme sabah mı akşam mı?

**Konuşma (19 kelime):**
> "Esneme sabah mı yapılır, akşam mı? Cevap: ikisi de olur. Önemli olan her gün yapmak. Sen ne zaman esniyorsun?"

**Prompt:**
```
Vertical 9:16 video, 10 seconds, photorealistic, natural UGC style.
CHARACTER: Aslı, a woman in her late 30s, soft oval face, grey-green eyes,
platinum ash-blonde hair swept to one side in a loose low bun with loose strands,
thin round dark metal-frame glasses, berry-red lipstick, small gold hoop earrings,
warm friendly smile.
She sits on a yoga mat in a bright living room with plants, wearing a sage green
sports top. She speaks to the camera, then reaches both arms up in a gentle
overhead stretch, and ends with a curious questioning smile at the camera.
She speaks in Turkish, clearly and warmly:
"Esneme sabah mı yapılır, akşam mı? Cevap: ikisi de olur. Önemli olan her gün yapmak. Sen ne zaman esniyorsun?"
Camera: static, medium-wide shot, eye level.
Lighting: soft natural daylight.
No subtitles, no on-screen text, no background music, no logo.
```

**Ekran yazıları:**
- 0–2.5 sn: **Sabah mı, akşam mı? ☀️🌙**
- Sonra: **✅ İkisi de olur** · *Önemli olan her gün*
- Son: **Sen ne zaman? ☀️ / 🌙 yaz**

**Kapak:** "SABAH MI AKŞAM MI?"

**Açıklama:**
```
Esneme sabah mı, akşam mı? ☀️🌙
Cevap: ikisi de olur. Önemli olan her gün yapmak.

Sen ne zaman esniyorsun? ☀️ ya da 🌙 yaz 👇

🤖 Videodaki görüntüler yapay zekâ ile üretildi
#bedenineyolculuk #esneme #mitvegerçek #yoga #evdehareket #shorts
```

---

# SERİ 4: Kanalın kalbi (abone getirir)

## 9. Tanışma ve kanal vaadi

**Konuşma (17 kelime):**
> "Ben Aslı. Bu kanalda her gün sadece on saniye ayırıyoruz. Küçük adımlar, büyük bir yolculuk. Benimle misin?"

**Prompt:**
```
Vertical 9:16 video, 10 seconds, photorealistic, warm personal vlog style.
CHARACTER: Aslı, a woman in her late 30s, soft oval face, grey-green eyes,
platinum ash-blonde hair swept to one side in a loose low bun with loose strands,
thin round dark metal-frame glasses, berry-red lipstick, small gold hoop earrings,
warm friendly smile.
She sits on a sunny garden bench surrounded by greenery, wearing a white linen shirt.
She speaks warmly to the camera, places her hand on her heart on "yolculuk", and
ends with an inviting open-hand gesture toward the camera.
She speaks in Turkish, warmly and sincerely:
"Ben Aslı. Bu kanalda her gün sadece on saniye ayırıyoruz. Küçük adımlar, büyük bir yolculuk. Benimle misin?"
Camera: static, medium close-up, slow push-in.
Lighting: soft golden hour sunlight, green bokeh background.
No subtitles, no on-screen text, no background music, no logo.
```

**Ekran yazıları:**
- 0–2.5 sn: **Ben Aslı 👋**
- Sonra: **Her gün 10 saniye** → **Küçük adımlar, büyük yolculuk**
- Son: **Benimle misin? → Takip et 💚**

**Kapak:** "HER GÜN 10 SANİYE"

**Kullanım:** Kanalın **fragmanı** olarak ayarlayın: YouTube Studio → Özelleştirme →
Düzen → "Abone olmayanlar için kanal fragmanı". Ayrıca yorumlara sabitleyin.

---

## 10. 7 günlük meydan okuma (abone ve takip)

**Konuşma (18 kelime):**
> "Yedi gün, günde on saniye. Her gün yeni bir küçük alışkanlık. Yarın birinci gün başlıyor. Takip et, kaçırma."

**Prompt:**
```
Vertical 9:16 video, 10 seconds, photorealistic, energetic natural UGC style.
CHARACTER: Aslı, a woman in her late 30s, soft oval face, grey-green eyes,
platinum ash-blonde hair swept to one side in a loose low bun with loose strands,
thin round dark metal-frame glasses, berry-red lipstick, small gold hoop earrings,
warm friendly smile.
She stands in a bright living room with plants, wearing a sage green sports top,
holding a small paper calendar. She points at it, counts on her fingers with
excitement, then points directly at the camera with a confident smile.
She speaks in Turkish, energetically and warmly:
"Yedi gün, günde on saniye. Her gün yeni bir küçük alışkanlık. Yarın birinci gün başlıyor. Takip et, kaçırma."
Camera: static, medium shot, eye level, slight push-in at the end.
Lighting: bright natural daylight.
No subtitles, no on-screen text, no background music, no logo.
```

**Ekran yazıları:**
- 0–2.5 sn: **7 GÜN · 10 SANİYE 🔥**
- Sonra: **Her gün 1 yeni alışkanlık**
- Son: **Yarın 1. gün → Takip et 🔔**

**Kapak:** "7 GÜNLÜK MEYDAN OKUMA"

**Önemli:** Bu videoyu sadece sonraki 7 günün videoları hazırsa yayınlayın; söz verip
tutmamak güveni zedeler. 7 gün için 4–8 numaralı senaryolar ve iki yeni senaryo
kullanılabilir.

---

## Önerilen yayın sırası

| Gün | Video | Neden bu sıra |
|---|---|---|
| 1 | 9. Tanışma | Yeni gelenler kanalı tanısın; fragman olarak da kullanılır |
| 2 | 1. Dopamin (2/4) | Oksitosin (1/4) yayında, seri devam ediyor |
| 3 | 2. Serotonin (3/4) | Seri devam |
| 4 | 3. Endorfin (4/4) | Seri tamamlanıyor, oynatma listesi kurulur |
| 5 | 6. Önce su | Geniş kitleye hitap eder |
| 6 | 7. 10 bin adım | Tartışma ve yorum getirir |
| 7 | 4. Masa başı boyun | Paylaşım getirir |
| 8 | 5. Kutu nefesi | 22:00'de yayınla |
| 9 | 8. Sabah mı akşam mı | Yorum getirir |
| 10 | 10. 7 günlük meydan okuma | Ancak sonraki 7 video hazırsa |

## Üretim notları
- Gemini bazen Türkçe kelimeleri yanlış telaffuz edebilir. Videoyu dinleyin, sorunlu
  bir kelime varsa promptta o kelimeyi değiştirip yeniden üretin.
- Konuşma 10 saniyeyi aşarsa video sonunda kesilir. Kelime sayıları buna göre ayarlandı;
  cümle eklemeyin.
- Videolar geldiğinde: "Bedenine Yolculuk tarzında düzenle" deyin. Müzik isteyip
  istemediğinizi de söyleyin. Konuşmalı videolarda müziksiz versiyon daha temiz duyulabilir.

---

# EK: Endorfin (yeni sürüm, kullanıcının senaryosu) · Mutluluk Hormonları 3. Aşama

**Konuşma (asıl, 26 kelime):**
> "Egzersiz yaptığında kendini iyi hissediyor musun? İşte bu, egzersiz sonrası salgılanan mutluluk ve ağrı kesici hormonumuz endorfin. Peki sen en çok hangi egzersizle bedenine yolculuk yapıyorsun?"

**Kısa yedek (20 kelime):**
> "Egzersizden sonra kendini iyi hissediyor musun? İşte bu, endorfin: doğal mutluluk ve ağrı kesici hormonun. Sen hangi egzersizle bedenine yolculuk yapıyorsun?"

**Prompt:**
```
Vertical 9:16 video, 10 seconds, photorealistic, cinematic natural style.
CHARACTER: Aslı, a woman in her late 30s, soft oval face, grey-green eyes,
platinum ash-blonde hair swept to one side in a loose low bun with loose strands,
thin round dark metal-frame glasses, berry-red lipstick, small gold hoop earrings,
warm friendly smile.
SETTING: The terrace of a luxurious villa in nature. A light stone deck with an
infinity pool behind her; beyond the pool's edge the calm blue sea stretches to
the horizon, framed by olive trees and green hills. Golden morning sunlight.
She wears a matching sage green athletic set: a sports bra top and high-waisted
leggings. She sits cross-legged on a grey yoga mat on the deck, as if she has
just finished a workout: relaxed shoulders, a light healthy glow on her skin,
calm deep breath, a small towel and a glass water bottle beside the mat.
She takes one relaxed breath, smiles, looks into the camera and speaks in
Turkish, clearly and warmly, at a natural pace:
"Egzersiz yaptığında kendini iyi hissediyor musun? İşte bu, egzersiz sonrası salgılanan mutluluk ve ağrı kesici hormonumuz endorfin. Peki sen en çok hangi egzersizle bedenine yolculuk yapıyorsun?"
On the final question she tilts her head slightly with a curious, inviting smile.
Camera: static, eye level, medium shot (head to knees), very slow push-in.
The pool and sea are clearly visible behind her, softly in focus.
Lighting: warm golden sunlight, soft sea breeze moving her loose hair strands.
No subtitles, no on-screen text, no background music, no logo.
```

**Ekran yazıları ve efektler:** Hook "Egzersizden sonra iyi mi hissediyorsun?" · "mutluluk" → yıldız ·
"ağrı kesici" → kalp · son soru kartı · kapanış kartı "Yorumlara yaz 👇 · 3. Aşama"

**Kapak:** "EGZERSİZDEN SONRA NEDEN İYİ HİSSEDİYORSUN?" + "3. AŞAMA · ENDORFİN"

**Başlık:** `Egzersizden Sonra Neden İyi Hissediyorsun? 🧘‍♀️ #endorfin #mutlulukhormonları`

## 💌 Serotonin: "Bugün senin gününü kim güzelleştirdi?" (18 Kasım 2026)
Kıyafet: askılı beyaz basic body + siyah tayt. A = sessiz sahne (stres → mesaj → yumuşama), B = A'yı uzat, kameraya konuşma.
Mesaj metni telefonda okunmaz; düzenlemede bildirim kartı olarak eklenir: "İyi ki varsın, seni çok seviyorum".

## 🧴 Güneş kremi: "Ama bir şeyi unuttun!" (19 Kasım 2026)
Kıyafet: deep blue tayt takım + butter yellow yağmurluk, kulaküstü kulaklık. Kamera = ayna (yansıma yok).
A = hazırlanma (fermuar, telefon, anahtar) → durup komodinden güneş kremini alır: "Ama bir şeyi unuttun!"
B = A'yı uzat: kremi sürerken "Yaz kış fark etmez, en önemli adım güneş kremi. Cildini UV ışınlarından korur, leke ve yaşlanmayı geciktirir."
Düzenleme: A'nın hazır anında flu ekran + tikli liste (kulaklık, telefon, su veya kahven, anahtarlar) ~3,5 sn · "Ama 1 şeyi unuttun" kartı + güneş · kapanış "Dışarı çıkmasan da sür, cildini koru" · açıklamada "Cildine uygun ürün için dermatoloğuna danış".

## 🔄 10 saniyede reset (21 Kasım 2026)
Kıyafet: buz mavisi kot pantolon + beyaz dar tişört + omuz/kol çantası. Kamera = ayna.
Konuşma (kısaltılmış): "10 saniyede kendine reset at: su iç, derin bir nefes al, seni mutlu edecek bir şey düşün. Sen değerlisin, unutma, sadece gülümse!"
Düzenleme: su / nefes / mutluluk kartları (tikli), "Sen değerlisin" kapanış kartı, kalp efekti.

## 🙆‍♀️ 10 saniyede omuzlarını indir (22 Kasım 2026)
Kıyafet: bebek mavisi tayt takım. Masa başı. Tek 10 sn klip, ≤15 sn final (kısa format testi).
Konuşma: "Omuzların kulağına mı yapıştı? Nefes al, omuzlarını kaldır... ve nefes verirken bırak. İşte bu kadar!"
Düzenleme: reset formatı · 10 sn sayaç · "Nefes al ↑ / Nefes ver ↓" kartları · tik · kapanış "Gün içinde 3 kez tekrarla".

## 📱 Telefona bakmadan önce 10 saniye (24 Kasım 2026)
Kıyafet: lavanta saten pijama takımı. Yatak, sabah. İlk kare: kameraya dönük yüz (yeni kural).
Konuşma: "Uyanınca ilk iş telefona mı uzanıyorsun? Dur. Önce 10 saniye kendine: gerin, derin bir nefes al ve güne gülümse."
Düzenleme: 10 sn sayaç · ✓ Gerin / ✓ Derin nefes / ✓ Gülümse · kapanış "Telefon bekleyebilir. Sen önce gel" · kalp.
