---
name: canliradyo-api
description: canliradyo.live editör paneli işlemlerini (radyo ekleme/düzenleme/silme, yayın linki, logo yükleme, yayın testi, kategoriler, yorumlar, iletişim mesajları, yönlendirmeler, panel özeti, önbellek temizleme) tarayıcı açmadan HTTP API ile yapar. Kullanıcı canliradyo, canliradyo.live, radyo paneli, editör paneli, radyo ekle/güncelle, yayın taraması, yorum onayı gibi bir şey istediğinde kullan.
---

# canliradyo.live editör paneli — API

canliradyo editör panelinde (www.canliradyo.live/editor) yapılabilen işlemler bu HTTP API ile yapılır.

## Bağlantı
- Adres: `POST https://www.canliradyo.live/editor/api/index.php`
- Kimlik başlığı: `Authorization: Bearer $CANLIRADYO_API_KEY`
- Gövde: JSON — `{"islem":"<işlem adı>", ...parametreler}`
- Yanıt: `{"ok":true,"api_surum":"...","veri":...}` ya da `{"ok":false,"hata":"..."}`

Anahtar **`CANLIRADYO_API_KEY` ortam değişkeninden** okunur; bu dosyaya, depoya ya da başka bir yere yazılmaz.
Değişken tanımlı değilse işlem yapma; kullanıcıya, anahtarı bulut ortamının ayarlarında
(oturum başlığındaki ortam menüsü → Edit → ortam değişkeni / secret) `CANLIRADYO_API_KEY` adıyla eklemesini
ve yeni oturum açmasını söyle. Anahtarı sohbete yapıştırmasını isteme.

Kolaylık için `scripts/cr.sh` kullan (anahtarı ortamdan alır):
```bash
S=.claude/skills/canliradyo-api/scripts/cr.sh
$S '{"islem":"yardim"}'                 # JSON metni
$S @istek.json                          # JSON dosyası (Türkçe karakterli yazma istekleri için)
$S -F islem=radyo.logo -F kanal_key=power-fm -F "dosya=@logo.jpg"   # multipart (logo/resim)
```

## Her oturumda
- canliradyo ile ilgili ilk işten önce `{"islem":"yardim"}` çağır. Katalog sunucuda üretilir ve **tek doğru kaynaktır**: tüm işlemler, parametreleri, tabloların güncel alanları, player kodları ve içerik kuralları oradadır. Bu dosyadaki örnekler yalnızca başlangıç içindir. Tek konu için: `{"islem":"yardim","konu":"radyo"}`.
- Her yanıtta `api_surum` gelir. Aşağıdaki bilinen sürümden farklıysa `{"islem":"degisiklikler"}` ile nelerin eklendiğini oku ve kullanıcıya kısaca bildir.
- Bilinen son sürüm: 2026-10-12.3

## Başlıca işlemler (ayrıntı: `yardim`)
- Kaynaklar (`liste`, `getir`, `ekle`, `guncelle`, `sil`): `radyo` (anahtar `kanal_key`), `kategori` (`kategori_key`), `yorum`, `mesaj`, `yonlendirme` (`source`), `tarama` (salt okunur).
- Özel: `ben`, `panel.ozet`, `radyo.logo`, `radyo.adlandir`, `radyo.tara`, `tarama.ozet`, `icerik.resim`, `kategori.gizle`, `yorum.onayla`, `mesaj.okundu`, `radyo.durum_sifirla`, `onbellek.temizle`.

## Örnekler
```bash
$S '{"islem":"radyo.liste","ara":"power","alanlar":["Id","kanal","kanal_key","kategori","player","link","onay","hit"],"limit":20}'
$S '{"islem":"radyo.getir","kanal_key":"power-fm"}'
$S '{"islem":"radyo.tara","kanal_key":"power-fm"}'
# istek.json: {"islem":"radyo.guncelle","kanal_key":"power-fm","alanlar":{"player":1,"link":"https://..."}}
# istek.json: {"islem":"radyo.ekle","alanlar":{"kanal":"Örnek FM","kanal_key":"ornek-fm","kategori":"pop","player":1,"link":"https://..."}}
# istek.json: {"islem":"yorum.onayla","ids":[101,102]}
```

## Kurallar
- İstek dosyalarını UTF-8 kaydet (geçici dosyaları depo dışına, ör. scratchpad'e yaz); radyo/kategori alanlarında emoji kullanma.
- Yazmadan önce ilgili kaydı `getir` ile oku; `guncelle` yalnız gönderilen alanları değiştirir.
- Yeni radyoyu önce `onay:0` ile ekle (varsayılan), logosunu yükle, `radyo.tara` ile yayını test et, sonra `onay:1` yap.
- Silme işlemleri, `radyo.durum_sifirla` ve `onbellek.temizle` geri alınamaz ya da tüm siteyi etkiler: kullanıcı açıkça istemedikçe çalıştırma, çalıştırmadan önce ne yapacağını söyle.
- Site canlıdır; toplu değişikliklerden önce etkilenecek kayıtları listeleyip kullanıcıya göster.
- Tek istek 100 saniyeyi geçemez (Cloudflare); büyük listeleri `limit`/`atla` ile parça parça al.
- Anahtarı hiçbir yere yazma, paylaşma, depoya ekleme. Tüm istekler sunucuda anahtar adına kaydedilir; anahtar site sahibi tarafından her an kapatılabilir (401 alırsan kullanıcıya bildir).
