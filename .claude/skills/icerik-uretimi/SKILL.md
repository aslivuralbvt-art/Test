---
name: icerik-uretimi
description: Instagram, TikTok, YouTube Shorts ve LinkedIn için sosyal medya içeriği üretir; içerik fikri, Reels/kısa video senaryosu, hook, açıklama (caption), hashtag, haftalık içerik takvimi, karusel metni ve yapay zekâ görsel/video promptları (Midjourney, GPT Image, Seedance, Kling, Higgsfield vb.) hazırlar. Kullanıcı içerik, post, reels, video fikri, senaryo, caption, hashtag, içerik takvimi, AI influencer, görsel promptu ya da video promptu istediğinde kullan.
---

# İçerik Üretimi

Sosyal medya için uçtan uca içerik üretir: fikir → senaryo → metin → görsel/video promptu → yayın planı.
Varsayılan dil Türkçe; kullanıcı başka dil isterse o dilde yaz.

## 1. Önce bağlamı topla

Aşağıdakiler belli değilse **tek mesajda, kısa bir liste hâlinde** sor (hepsini zorunlu tutma; cevap yoksa makul varsayım yap ve varsayımı belirt):

- **Marka / hesap:** Kim, ne satıyor ya da ne anlatıyor? (Kişisel hesap, marka, AI influencer karakteri)
- **Hedef kitle:** Yaş, ilgi alanı, sorun/ihtiyaç
- **Platform ve format:** Reels, TikTok, Shorts, karusel, tek görsel, LinkedIn yazısı
- **Amaç:** Takipçi, etkileşim, satış, bilinirlik, DM/lead toplama
- **Ton:** Samimi, esprili, uzman, ilham verici, minimal
- **Kısıtlar:** Süre, yasaklı konular, marka renkleri, kullanılacak AI araçları

Kullanıcı daha önce bir **marka profili** verdiyse (aynı sohbette ya da çalışma dizininde `marka-profili.md`), onu kullan ve tekrar sorma.

## 2. Görev türüne göre çalış

### A. İçerik fikri
- En az 10 fikir üret; her birini şu sütunlarla tablo yap: **Fikir | Format | Hook (ilk cümle) | Neden işe yarar**
- Fikirleri karıştır: eğitici, eğlenceli, kamera arkası, trend uyarlaması, müşteri sorusu, mit/gerçek, önce-sonra, liste ("3 hata…").
- En güçlü 3 fikri işaretle.

### B. Kısa video senaryosu (Reels / TikTok / Shorts)
Şu yapıyı kullan:

| Saniye | Görüntü (ne görünüyor) | Ses / konuşma | Ekran yazısı |
|---|---|---|---|
| 0–3 | **Hook:** merak, şok, soru ya da vaat | … | … |
| 3–… | Değer: asıl içerik, hızlı kesmeler | … | … |
| Son 3 | **CTA:** yorum yaz, kaydet, takip et, DM | … | … |

Kurallar:
- Hook ilk 2 saniyede gelmeli; "Merhaba arkadaşlar" ile başlama.
- Varsayılan süre 15–30 sn; her sahne en fazla 3 sn.
- Senaryoya 3 alternatif hook ekle.
- Müzik/ses önerisi ver (trend ses adı uydurma; "enerjik lo-fi", "dramatik gerilim" gibi tarif et).

### C. Açıklama (caption) ve hashtag
- İlk satır tek başına okunduğunda "devamını gör"e tıklatmalı.
- Gövde: kısa paragraflar, gerekiyorsa 1–3 emoji, net bir CTA.
- "Yorumlara X yaz, sana gönderelim" tarzı CTA'yı ancak kullanıcı gerçekten bir şey gönderecekse öner.
- Hashtag: 3–5 niş + 2–3 orta + 1–2 geniş, toplam en fazla 10. Uydurma istatistik verme.
- 2 farklı uzunlukta (kısa / uzun) versiyon sun.

### D. Karusel
- 7–10 slayt: 1. slayt hook başlık, son slayt CTA.
- Her slayt için: **Başlık (en fazla 8 kelime) | Alt metin (en fazla 25 kelime) | Görsel önerisi**

### E. Yapay zekâ görsel / video promptu
Ayrıntılı şablonlar: `references/prompt-sablonlari.md` dosyasını oku.
- Promptları **İngilizce** yaz (modeller İngilizcede daha iyi sonuç verir), altına kısa Türkçe açıklama ekle.
- AI influencer / tekrar eden karakter için önce bir **karakter kartı** oluştur (yüz, saç, yaş, stil, ayırt edici detaylar) ve tüm promptlarda aynı tanımı kullan ki karakter tutarlı kalsın.
- Her prompt için 2 varyasyon ver (farklı açı/ışık/ortam).
- Kullanıcı hangi aracı kullandığını söylediyse o aracın söz dizimine uy (ör. Midjourney'de `--ar 9:16`).

### F. İçerik takvimi
- Varsayılan: 1 hafta, günde 1 paylaşım.
- Tablo: **Gün | Saat önerisi | Format | Konu | Hook | CTA | Durum**
- İçerik sütunlarını dengele: yaklaşık %40 eğitici, %30 eğlence/ilişki, %20 güven/kanıt, %10 satış.
- İstenirse tabloyu CSV olarak da ver.

## 3. Kalite kontrol (teslimden önce)

- [ ] Hook ilk 2 saniyede ya da ilk satırda mı?
- [ ] Hedef kitleye ve tona uygun mu?
- [ ] Tek ve net bir CTA var mı?
- [ ] Platformun format ve uzunluk sınırlarına uyuyor mu? (Instagram caption en fazla 2.200 karakter, hashtag en fazla 30)
- [ ] Uydurma veri, sahte yorum ya da gerçek dışı vaat yok mu?
- [ ] AI ile üretilen gerçekçi insan görüntüsü varsa, platform kuralına göre "AI ile üretildi" etiketi hatırlatıldı mı?

## 4. Sınırlar

- Gerçek bir kişinin (ünlü, rakip, özel kişi) yüzünü ya da kimliğini taklit eden görsel/video promptu yazma; kurgusal karakter öner.
- Telif hakkı olan karakter, logo ya da marka kullanımını önerme.
- Sağlık, finans ve hukuk içeriklerinde kesin vaat verme; "uzmana danışın" notu ekle.
- Sahte kullanıcı yorumu, sahte referans ya da uydurma rakam üretme.

## 5. Çıktı biçimi

- Başlıklar ve tablolarla düzenli yaz; kullanıcı doğrudan kopyalayabilsin diye caption ve promptları kod bloğu içinde ver.
- Sonunda en fazla 2 satırlık "Sonraki adım" önerisi ekle (ör. "Bu senaryonun görsel promptlarını da hazırlayayım mı?").
