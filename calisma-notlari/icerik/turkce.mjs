// 5. sınıf Türkçe — 1. dönem 1. ortak yazılı çalışma notları
const afisKitap = `<svg width="330" height="200" viewBox="0 0 330 200" font-family="Nunito, sans-serif">
  <rect x="2" y="2" width="326" height="196" rx="14" fill="#fff8e6" stroke="#f2a516" stroke-width="3"/>
  <text x="165" y="38" text-anchor="middle" font-size="24" font-weight="800" fill="#d9480f">KİTAP OKUMA ŞENLİĞİ</text>
  <g transform="translate(28 60)">
    <path d="M0 10 Q30 0 55 10 V70 Q30 60 0 70Z" fill="#4dabf7"/>
    <path d="M110 10 Q80 0 55 10 V70 Q80 60 110 70Z" fill="#74c0fc"/>
    <path d="M55 10 V70" stroke="#1c7ed6" stroke-width="2"/>
  </g>
  <text x="155" y="78" font-size="14" font-weight="700" fill="#333">Tarih: 15 Kasım Cumartesi</text>
  <text x="155" y="100" font-size="14" font-weight="700" fill="#333">Saat: 14.00</text>
  <text x="155" y="122" font-size="14" font-weight="700" fill="#333">Yer: Okul Kütüphanesi</text>
  <text x="165" y="165" text-anchor="middle" font-size="16" font-weight="800" fill="#2b8a3e">Herkes davetlidir. Kitabını al, gel!</text>
</svg>`;

const afisSu = `<svg width="300" height="190" viewBox="0 0 300 190" font-family="Nunito, sans-serif">
  <rect x="2" y="2" width="296" height="186" rx="14" fill="#e7f5ff" stroke="#1c7ed6" stroke-width="3"/>
  <text x="150" y="34" text-anchor="middle" font-size="20" font-weight="800" fill="#1864ab">BİR DAMLA SU, BİR HAYAT!</text>
  <rect x="40" y="58" width="70" height="16" rx="4" fill="#868e96"/>
  <rect x="96" y="58" width="14" height="34" rx="3" fill="#868e96"/>
  <rect x="62" y="48" width="24" height="10" rx="3" fill="#495057"/>
  <path d="M103 104 C97 114 97 120 103 122 C109 120 109 114 103 104Z" fill="#339af0"/>
  <path d="M103 134 C97 144 97 150 103 152 C109 150 109 144 103 134Z" fill="#74c0fc"/>
  <text x="140" y="90" font-size="14" font-weight="700" fill="#333">Musluğu açık</text>
  <text x="140" y="108" font-size="14" font-weight="700" fill="#333">bırakma!</text>
  <text x="140" y="138" font-size="12" font-weight="700" fill="#495057">Dişlerini fırçalarken</text>
  <text x="140" y="154" font-size="12" font-weight="700" fill="#495057">suyu kapat.</text>
  <text x="150" y="178" text-anchor="middle" font-size="11" font-weight="800" fill="#1864ab">Su Tasarrufu Kulübü</text>
</svg>`;

const metin = `<div class="box" style="--bc:#8a5cd1"><b class="boxl">OKUMA METNİ</b>
<p style="text-align:center"><b style="color:#8a5cd1">Kütüphanedeki Mektup</b></p>
<p>Kasım ayının yağmurlu bir pazartesisiydi. Elif, okul çıkışı her zamanki gibi mahalledeki küçük kütüphaneye uğradı. Raflar arasında dolaşırken eski, kalın kapaklı bir kitabın arasından <u>sararmış</u> bir kâğıt düştü. Kâğıdı merakla açtı. Bu, yıllar önce bir öğrencinin kütüphaneciye yazdığı bir teşekkür mektubuydu. Öğrenci, kitaplar sayesinde hayallerinin genişlediğini, bir gün kendisinin de bir kütüphane açacağını yazmıştı.</p>
<p>Elif, mektubu kütüphaneci Nermin Hanım’a götürdü. Nermin Hanım mektubu okuyunca gözleri doldu: “Bu mektubu yazan çocuk, şimdi şehrimizin en büyük kütüphanesinin müdürü.” dedi.</p>
<p>O gün Elif, eve dönerken çantasındaki kitaba daha bir sevgiyle baktı. Kitapların, insanları birbirine bağlayan <u>görünmez köprüler</u> olduğunu anladı. Akşam, defterinin ilk sayfasına kocaman harflerle şunu yazdı: “Ben de bir gün birine <u>ilham</u> olacağım!”</p>
</div>`;

export default {
  ad: 'Türkçe',
  dosya: 'Turkce',
  kapsam: [
    { kod: 'T.O.5.5', metin: 'Metinde geçen anlamını bilmediği söz varlığı unsurlarının anlamını tahmin edebilme' },
    { kod: 'T.O.5.6', metin: 'Metnin yüzey anlamını belirleyebilme' },
    { kod: 'T.O.5.7', metin: 'Görselle iletilen anlamı belirleyebilme' },
    { kod: 'T.O.5.15', metin: 'Metnin anahtar kelimelerini belirlemeye yönelik çözümleme yapabilme' },
    { kod: 'T.O.5.20', metin: 'Metinden hareketle söz varlığını geliştirmeye yönelik çözümleme yapabilme' },
    { kod: 'T.Y.5.3', metin: 'Yazısında içerik ve yapıya yönelik seçimlerini yönetebilme' },
    { kod: 'T.Y.5.13', metin: 'Yazısını zenginleştirecek biçimde söz varlığını kullanabilme' },
    { kod: 'T.Y.5.16', metin: 'Yazım ve noktalama işaretleriyle ilgili kuralları uygulayabilme' },
  ],
  kapsamNot: 'MEB, bu yazılı için birkaç senaryo yayımladı; okulundaki Türkçe öğretmenleri bunlardan birini seçer. Yazım ve noktalama kuralları bütün senaryolarda var. Sorular çoğunlukla bir okuma metnine ve görsele dayalı açık uçlu sorulardır.',
  icerik: [
    { h: 'Bilmediğim Kelimenin Anlamını Tahmin Ediyorum', no: 1, kod: 'T.O.5.5' },
    { p: 'Okurken anlamını bilmediğin bir kelimeyle karşılaşınca hemen sözlüğe koşmana gerek yok. Önce <b>bağlamdan</b>, yani kelimenin içinde geçtiği cümleden ve metinden yararlanarak anlamını tahmin edebilirsin.' },
    { ol: [
      '<b>Cümlenin bütününü oku.</b> Kelimeden önce ve sonra gelen sözler sana ipucu verir.',
      '<b>Eş ya da zıt anlamlı ipucu ara.</b> Yazar bazen aynı şeyi başka bir kelimeyle tekrar söyler.',
      '<b>Kelimenin kökünü ve eklerini incele.</b> “Kitaplık” kelimesinde “kitap” kökü vardır.',
      '<b>Varsa görsele bak.</b> Resim, afiş ya da fotoğraf anlamı destekler.',
      '<b>Tahminini cümlede dene.</b> Kelimenin yerine tahminini koy; cümle anlamlı oluyorsa doğru yoldasın. Sonra sözlükten kontrol et.',
    ] },
    { box: 'ornek', html: `<p><i>“Dedem çok <u>cömert</u> biriydi; elindekini hep komşularıyla paylaşırdı.”</i></p>
<p>İpucu: “elindekini hep paylaşırdı” → <b>Cömert:</b> eli açık, sahip olduğunu başkalarıyla paylaşmayı seven.</p>
<p><i>“Uzun yoldan gelen yorgun yolcular, köydeki <u>hana</u> sığınıp dinlendiler.”</i> → <b>Han:</b> yolcuların konakladığı, dinlendiği yapı.</p>` },

    { h: 'Metnin Yüzey Anlamı: 5N1K', no: 2, kod: 'T.O.5.6' },
    { p: 'Bir metnin <b>yüzey anlamı</b>, metinde <b>açıkça yazılan</b> bilgilerdir. Bunları bulmak için 5N1K sorularını sorarız. Cevaplar metnin içinde hazır durur; yorum yapmana gerek yoktur.' },
    { table: { head: ['Soru', 'Neyi bulur?', 'Örnek cevap (Okuma metni)'], rows: [
      ['<b>Kim?</b>', 'Olaydaki kişi ya da varlık', 'Elif, Nermin Hanım'],
      ['<b>Ne?</b>', 'Olan olay, yapılan iş', 'Kitabın arasından eski bir mektup düştü.'],
      ['<b>Nerede?</b>', 'Olayın geçtiği yer', 'Mahalledeki küçük kütüphanede'],
      ['<b>Ne zaman?</b>', 'Olayın zamanı', 'Kasım ayında, yağmurlu bir pazartesi'],
      ['<b>Nasıl?</b>', 'Olayın oluş biçimi', 'Raflar arasında dolaşırken, merakla'],
      ['<b>Neden?</b>', 'Olayın sebebi', 'Nermin Hanım’ın gözleri doldu, çünkü mektubu yazan çocuk kütüphane müdürü olmuştu.'],
    ] } },
    { box: 'ipucu', html: '<p>5N1K sorusunu cevaplarken metindeki cümleyi bul ve cevabını <b>tam cümleyle</b> yaz. Örneğin “Nerede?” sorusuna yalnızca “kütüphane” yerine “Olay mahalledeki küçük kütüphanede geçer.” yazmak daha iyidir.</p>' },

    { h: 'Görselle İletilen Anlam', no: 3, kod: 'T.O.5.7' },
    { p: 'Afiş, broşür, karikatür, fotoğraf ve tablolar da bize bir şey anlatır. Bir görseli “okurken” şunlara dikkat et:' },
    { cols: [[
      { ul: [
        '<b>Başlık ve büyük yazılar:</b> Ana mesaj genellikle en büyük yazıdadır.',
        '<b>Simge ve resimler:</b> Kitap, damla, saat gibi çizimler konuyu gösterir.',
        '<b>Renkler:</b> Kırmızı uyarıyı, yeşil doğayı ya da onayı çağrıştırabilir.',
        '<b>Tarih, saat, yer bilgisi:</b> Duyuru ve davet afişlerinde mutlaka bulunur.',
        '<b>Kime seslendiği:</b> “Herkes davetlidir” gibi ifadeler hedef kitleyi gösterir.',
      ] },
    ], [
      { svg: afisKitap, caption: 'Örnek afiş: Ne duyuruluyor? Ne zaman, nerede?' },
    ]] },
    { box: 'ornek', html: '<p>Yukarıdaki afiş bir <b>kitap okuma şenliğini</b> duyurmaktadır. Etkinlik <b>15 Kasım Cumartesi, saat 14.00’te, okul kütüphanesinde</b> yapılacaktır. Afiş herkesi davet etmektedir. Kitap çizimi, etkinliğin konusunu destekler.</p>' },

    { h: 'Anahtar Kelimeleri Buluyorum', no: 4, kod: 'T.O.5.15' },
    { p: '<b>Anahtar kelimeler</b>, metnin konusunu taşıyan, metinde sık geçen ve çıkarıldığında metnin anlamı eksik kalan önemli kelimelerdir. Anahtar kelimeleri bulmak; metnin <b>konusunu</b>, <b>ana fikrini</b> ve uygun bir <b>başlığı</b> bulmamızı kolaylaştırır.' },
    { box: 'ornek', html: `<p><i>“Arılar, çiçekten çiçeğe konarak polen taşır. Bu sayede bitkiler meyve verir. Arılar topladıkları nektardan da bal yapar. Arılar olmasaydı sofralarımızdaki pek çok meyve ve sebze olmazdı.”</i></p>
<p><b>Anahtar kelimeler:</b> arı, çiçek, polen, bal &nbsp;→&nbsp; <b>Başlık önerisi:</b> “Doğanın Çalışkan Dostları: Arılar”</p>` },
    { box: 'ipucu', html: '<p>Kendine sor: “Bu metin <b>en çok neyi</b> anlatıyor?” Metinde tekrar eden ya da aynı anlamı taşıyan kelimeleri işaretle. “ve, ile, bir, çok” gibi kelimeler anahtar kelime değildir.</p>' },

    { h: 'Söz Varlığımı Geliştiriyorum', no: 5, kod: 'T.O.5.20' },
    { cols: [[
      { h2: 'Eş Anlamlı Kelimeler' },
      { p: 'Yazılışları farklı, anlamları aynı ya da çok yakın kelimelerdir.' },
      { table: { head: ['Kelime', 'Eş anlamlısı'], rows: [['cevap', 'yanıt'], ['yıl', 'sene'], ['kelime', 'sözcük'], ['öğrenci', 'talebe'], ['hediye', 'armağan'], ['siyah', 'kara']] } },
    ], [
      { h2: 'Zıt Anlamlı Kelimeler' },
      { p: 'Anlamca birbirinin karşıtı olan kelimelerdir.' },
      { table: { head: ['Kelime', 'Zıt anlamlısı'], rows: [['eski', 'yeni'], ['büyük', 'küçük'], ['cömert', 'cimri'], ['erken', 'geç'], ['kolay', 'zor'], ['gelmek', 'gitmek']] } },
    ]] },
    { h2: 'Sesteş (Eş Sesli) Kelimeler' },
    { p: 'Yazılışları ve okunuşları aynı, anlamları farklı kelimelerdir. Anlamını <b>cümle</b> belirler.' },
    { ul: [
      '<b>yüz:</b> Sabah <u>yüzümü</u> yıkadım. (surat) / Kitap <u>yüz</u> sayfadır. (sayı) / Denizde <u>yüzdük</u>. (yüzmek)',
      '<b>gül:</b> Bahçedeki <u>gül</u> açtı. (çiçek) / Biraz <u>gül</u>, mutlu ol. (gülmek)',
      '<b>dolu:</b> Bardak <u>dolu</u>. (boş değil) / Gökten <u>dolu</u> yağdı. (buz taneleri)',
    ] },
    { h2: 'Deyimler ve Atasözleri' },
    { cols: [[
      { p: '<b>Deyim:</b> Genellikle gerçek anlamından farklı bir anlam taşıyan, kalıplaşmış söz grubudur.' },
      { ul: ['<b>göz atmak:</b> kısaca bakmak', '<b>kulak vermek:</b> dikkatle dinlemek', '<b>eli açık:</b> cömert', '<b>gözleri dolmak:</b> ağlayacak duruma gelmek'] },
    ], [
      { p: '<b>Atasözü:</b> Atalarımızın deneyimlerine dayanan, öğüt veren, kalıplaşmış sözlerdir.' },
      { ul: ['<b>Damlaya damlaya göl olur.</b> Küçük birikimler zamanla büyür.', '<b>Bilgi, servetten üstündür.</b>', '<b>Sakla samanı, gelir zamanı.</b> Gereksiz görünen şey bir gün işe yarar.'] },
    ]] },
    { h2: 'Kelime Türetme' },
    { p: 'Bir kelimeye yapım eki getirerek yeni anlamlı kelimeler türetebiliriz: <b>göz</b> → gözlük, gözcü · <b>kitap</b> → kitaplık, kitapçı · <b>bil-</b> → bilgi, bilgin · <b>yaz-</b> → yazar, yazı.' },

    { h: 'Yazımda İçerik ve Yapı', no: 6, kod: 'T.Y.5.3' },
    { p: 'Yazmaya başlamadan önce <b>konunu</b> belirle, ne anlatacağını kısaca <b>planla</b> ve yazına uygun bir <b>başlık</b> koy. İyi bir yazı üç bölümden oluşur:' },
    { table: { head: ['Bölüm', 'Ne yaparız?', 'Örnek (Konu: En sevdiğim mevsim)'], rows: [
      ['<b>Giriş</b>', 'Konuyu tanıtır, okuru yazıya hazırlarız.', 'En sevdiğim mevsim sonbahardır.'],
      ['<b>Gelişme</b>', 'Konuyu ayrıntılarla, örneklerle açıklarız. En uzun bölümdür.', 'Ağaçların yaprakları sarıya, kırmızıya döner; yağmurun kokusu her yere yayılır…'],
      ['<b>Sonuç</b>', 'Yazıyı toparlar, duygu ya da düşüncemizi kısaca belirtiriz.', 'Bu yüzden sonbaharı her yıl sabırsızlıkla beklerim.'],
    ] } },
    { box: 'hatirla', html: '<p>Her yeni paragrafa <b>satır başından biraz içeriden</b> başlanır. Bir paragrafta tek bir ana düşünce anlatılır. Başlıktaki her kelimenin ilk harfi büyük yazılır.</p>' },

    { h: 'Yazımı Zenginleştiriyorum', no: 7, kod: 'T.Y.5.13' },
    { p: 'Aynı kelimeleri tekrar tekrar kullanmak yazıyı sıkıcı yapar. Yazını zenginleştirmek için:' },
    { ul: [
      'Tekrar eden kelimeler yerine <b>eş anlamlılarını</b> kullan.',
      'Varlıkları anlatırken renk, şekil, ses, koku bildiren <b>betimleyici kelimeler</b> ekle (masmavi gökyüzü, mis kokulu çiçekler).',
      'Uygun yerlerde <b>deyim, atasözü ve benzetme</b> kullan (pamuk gibi bulutlar).',
      'Cümleleri “ve, ama, çünkü, bu yüzden, sonra” gibi <b>bağlayıcı ifadelerle</b> birleştir.',
    ] },
    { box: 'ornek', html: `<p><b>Önce:</b> Hava güzeldi. Parka gittik. Parkta oynadık. Çok güzeldi.</p>
<p><b>Sonra:</b> Güneşli bir pazar sabahı, ailemle birlikte yemyeşil parka gittik. Rengârenk salıncaklarda sallandık, kahkahalarla koşturduk. Günün sonunda yorgun ama mutluyduk.</p>` },

    { h: 'Yazım Kuralları', no: 8, kod: 'T.Y.5.16' },
    { h2: 'Büyük Harflerin Kullanımı' },
    { ul: [
      'Cümleler büyük harfle başlar: <i>Bugün hava çok güzel.</i>',
      'Kişi adları ve soyadları: <i>Elif Yılmaz, Atatürk</i>',
      'Unvan ve saygı sözleri: <i>Nermin Hanım, Ali Bey, Doktor Ayşe</i>',
      'Ülke, şehir, ilçe, köy, dağ, deniz adları: <i>Türkiye, Ankara, Ağrı Dağı, Karadeniz</i>',
      'Kurum ve kuruluş adları: <i>Türk Dil Kurumu, Atatürk Ortaokulu</i>',
      'Belirli bir tarih bildiren gün ve ay adları: <i>29 Ekim 1923, 15 Kasım Cumartesi</i>',
      'Kitap, dergi, gazete adları ile yazı başlıklarındaki kelimeler: <i>Kütüphanedeki Mektup</i>',
    ] },
    { box: 'dikkat', html: '<p>Belirli bir tarih bildirmeyen gün ve ay adları küçük harfle yazılır: <i>Her <u>pazartesi</u> kütüphaneye giderim. Okullar <u>eylülde</u> açılır.</i></p>' },
    { h2: 'Sayıların Yazımı' },
    { ul: [
      'Yazıyla yazılan sayılar <b>ayrı</b> yazılır: <i>on beş, yüz yirmi üç, iki bin yirmi altı</i>',
      'Rakamla yazılan sayılara gelen ekler <b>kesme işaretiyle</b> ayrılır: <i>1923’te, 5’inci, 3’e</i>',
      'Sıra bildiren sayılar rakamla yazılırken sonuna <b>nokta</b> konur: <i>5. sınıf, 2. kat</i>',
      'Saat ve dakikalar arasına <b>nokta</b> konur: <i>14.00, 08.30</i>',
    ] },
    { h2: '“de / da” Bağlacı ile “-de / -da” Eki' },
    { table: { head: ['', 'Bağlaç “de, da”', 'Ek “-de, -da, -te, -ta”'], rows: [
      ['Yazılışı', '<b>Ayrı</b> yazılır.', '<b>Bitişik</b> yazılır.'],
      ['Görevi', '“dahi, bile, de” anlamı katar.', 'Yer, zaman bildirir (bulunma hâli).'],
      ['Örnek', '<i>Ben <u>de</u> geleceğim. Kardeşim <u>de</u> kitap okur.</i>', '<i>Ev<u>de</u> kaldım. Okul<u>da</u> oynadık. Sınıf<u>ta</u> bekledik.</i>'],
      ['Test', 'Çıkarınca cümle anlamlı kalır, sadece anlamı biraz değişir.', 'Çıkarınca cümle bozulur.'],
    ] } },
    { box: 'dikkat', html: '<p>Bağlaç olan “de” hiçbir zaman “<b>te</b>” olmaz: <i>Ahmet <u>de</u> geldi</i> (✔) — <i>Ahmet <u>te</u> geldi</i> (✘). Bağlaç, kendinden önceki kelimenin son ünlüsüne uyar: <i>sen de, ben de, okul da, kitap da</i>.</p>' },
    { h2: '“ki” Bağlacı ile “-ki” Eki' },
    { ul: [
      '<b>Bağlaç olan “ki” ayrı yazılır:</b> <i>Duydum <u>ki</u> yarın kar yağacakmış. Öyle yorgunum <u>ki</u>…</i>',
      '<b>“-ki” eki bitişik yazılır:</b> <i>evde<u>ki</u> kitap, yarın<u>ki</u> gezi, benim<u>ki</u>, seninki</i>',
      '<b>Kalıplaşmış olanlar bitişik yazılır:</b> <i>belki, çünkü, sanki, oysaki, mademki, hâlbuki</i>',
    ] },
    { h2: 'Soru Eki “mi”' },
    { p: 'Soru eki <b>mı, mi, mu, mü</b> her zaman <b>ayrı</b> yazılır, kendinden önceki kelimenin ünlüsüne uyar. Kendinden sonra gelen ekler soru ekine <b>bitişik</b> yazılır: <i>Geldi <u>mi</u>? Güzel <u>mi</u>? Okudun <u>mu</u>? Geliyor <u>musun</u>? Hazır <u>mıyız</u>?</i>' },
    { h2: 'Kısaltmalar' },
    { ul: [
      'Kurum adlarının kısaltması büyük harfle ve noktasız yazılır: <i>TDK, MEB, TBMM</i>',
      'Kısaltmalara gelen ekler <b>kesme işaretiyle</b> ayrılır ve ek, kısaltmanın <b>okunuşuna</b> uyar: <i>TDK’ye (tedeke), MEB’e (meb), TBMM’ye</i>',
      'Ölçü birimleri noktasız yazılır: <i>cm, kg, km, m</i> → <i>5 km’lik yol</i>',
    ] },
    { h2: 'Birleşik Kelimeler' },
    { p: 'Anlam değişmesiyle oluşan birleşik kelimeler <b>bitişik</b> yazılır: <i>hanımeli, aslanağzı, kuşburnu</i>. “Etmek, olmak” ile kurulan birleşik fiillerde ses düşmesi ya da türemesi olursa kelime <b>bitişik</b>, olmazsa <b>ayrı</b> yazılır: <i>kaybetmek, affetmek, hissetmek</i> — <i>yardım etmek, teşekkür etmek, kayıt olmak</i>.' },

    { h: 'Noktalama İşaretleri', no: 9, kod: 'T.Y.5.16' },
    { table: { head: ['İşaret', 'Nerede kullanılır?', 'Örnek'], rows: [
      ['<b>Nokta&nbsp;(&nbsp;.&nbsp;)</b>', 'Tamamlanmış cümlenin sonunda; sıra sayılarında; kısaltmalarda; tarih ve saatlerde', '<i>Kitap okudum. · 5. sınıf · Dr. · 29.10.1923 · 14.30</i>'],
      ['<b>Virgül&nbsp;(&nbsp;,&nbsp;)</b>', 'Eş görevli kelimeler arasında; hitaplardan sonra; sıralı cümleler arasında', '<i>Kalem, silgi ve defter aldım. · Arkadaşlar, sessiz olalım.</i>'],
      ['<b>Soru&nbsp;işareti&nbsp;(&nbsp;?&nbsp;)</b>', 'Soru bildiren cümlelerin sonunda', '<i>Ödevini bitirdin mi?</i>'],
      ['<b>Ünlem&nbsp;(&nbsp;!&nbsp;)</b>', 'Sevinç, korku, şaşırma, acıma, seslenme ve uyarı bildiren cümlelerin sonunda', '<i>Eyvah! Otobüsü kaçırdık. · Dikkat, yol kaygan!</i>'],
      ['<b>İki&nbsp;nokta&nbsp;(&nbsp;:&nbsp;)</b>', 'Kendisinden sonra açıklama, örnek ya da alıntı yapılacak cümlenin sonunda', '<i>Çantama şunları koydum: kalem, silgi, defter.</i>'],
      ['<b>Kesme&nbsp;(&nbsp;’&nbsp;)</b>', 'Özel adlara, rakamlara ve kısaltmalara gelen ekleri ayırmak için', '<i>Ankara’ya, Elif’in, 2026’da, TDK’ye</i>'],
      ['<b>Tırnak&nbsp;(&nbsp;“&nbsp;”&nbsp;)</b>', 'Başkasının sözünü aynen aktarırken; eser adlarında; vurgulanmak istenen sözlerde', '<i>Annem “Ödevini bitirdin mi?” diye sordu.</i>'],
      ['<b>Üç&nbsp;nokta&nbsp;(&nbsp;…&nbsp;)</b>', 'Tamamlanmamış cümlelerin sonunda; sayılabilecek örneklerin devam ettiğini göstermek için', '<i>Bahçede gül, lale, papatya… vardı.</i>'],
    ] } },
    { box: 'dikkat', html: '<p>Kurum ve kuruluş adlarına gelen ekler kesme işaretiyle <b>ayrılmaz</b>: <i>Türk Dil Kurumuna, Atatürk Ortaokuluna</i>. Ama kısaltmalarına gelen ekler ayrılır: <i>TDK’ye</i>.</p>' },
  ],

  sorular: [
    { q: `<p>Aşağıdaki metni okuyunuz ve 1–5. soruları metne göre cevaplayınız.</p>${metin}<p><b>Altı çizili “sararmış” ve “ilham” kelimelerinin anlamını tahmin ediniz. Tahmin ederken metindeki hangi ipuçlarından yararlandığınızı yazınız.</b></p>`, lines: 4 },
    { q: `<p><b>Metne göre aşağıdaki soruları cevaplayınız.</b></p>
<p>a) Olay nerede geçmektedir? &nbsp; b) Olay ne zaman yaşanmıştır? &nbsp; c) Elif kitabın arasında ne buldu? &nbsp; d) Nermin Hanım’ın gözleri neden doldu?</p>`, lines: 4 },
    { q: '<p><b>Metnin anahtar kelimelerinden dördünü yazınız. Bu kelimelerden yararlanarak metne yeni bir başlık öneriniz.</b></p>', lines: 3 },
    { q: '<p><b>“Kitapların, insanları birbirine bağlayan görünmez köprüler olduğunu anladı.” cümlesinde “görünmez köprüler” ifadesiyle ne anlatılmak istenmektedir? Açıklayınız.</b></p>', lines: 3 },
    { q: '<p><b>Metinde geçen “gözleri dolmak” deyiminin anlamını yazınız. Bu deyimi kendi kuracağınız bir cümlede kullanınız.</b></p>', lines: 2 },
    { q: '<p><b>Aşağıdaki afişi inceleyiniz.</b> a) Afişte verilmek istenen mesaj nedir? b) Afişi kim hazırlamıştır? c) Afişteki hangi görsel unsurlar mesajı desteklemektedir?</p>', svg: afisSu, lines: 3 },
    { q: `<p><b>Aşağıdaki kelimelerin eş anlamlısını ya da zıt anlamlısını yazınız.</b></p>
<table class="tbl"><thead><tr><th>Kelime</th><th>Eş anlamlısı</th><th>Kelime</th><th>Zıt anlamlısı</th></tr></thead><tbody>
<tr><td>yanıt</td><td></td><td>eski</td><td></td></tr>
<tr><td>sene</td><td></td><td>cömert</td><td></td></tr>
<tr><td>armağan</td><td></td><td>erken</td><td></td></tr></tbody></table>`, lines: 0 },
    { q: '<p><b>“yüz” kelimesini iki farklı anlamda kullanarak iki cümle kurunuz.</b></p>', lines: 2 },
    { q: `<p><b>Aşağıdaki cümlelerdeki yazım yanlışlarını bulup cümleleri doğru biçimde yeniden yazınız.</b></p>
<p>a) kardeşim de okula gidiyormu?<br>b) Yaz tatilinde izmir’e gittik, oradaki deniz çok güzeldi.<br>c) Bu kitabı üç günde bitirdim, sende okumalısın.<br>d) Cumhuriyet, 29 ekim 1923’te ilan edildi.<br>e) Bu kelimenin yazılışını TDK’ya sordum.</p>`, lines: 3 },
    { q: `<p><b>Aşağıdaki cümlelerde ayraç içine uygun noktalama işaretlerini koyunuz.</b></p>
<p>a) Çantama kalem( ) silgi( ) cetvel ve defter koydum( )<br>b) Eyvah( ) Otobüsü kaçırdık( )<br>c) Öğretmenimiz şöyle dedi( ) ( )Yarın müzeye gideceğiz.( )<br>d) Bugün kütüphaneye gidecek misin( )<br>e) Ankara( )ya 2026( )da taşındık.</p>`, lines: 0 },
    { q: `<p><b>Aşağıdaki paragrafı eş anlamlı ve betimleyici kelimeler kullanarak zenginleştirip yeniden yazınız.</b></p>
<p><i>“Bahçe güzeldi. Bahçede çiçekler vardı. Çiçekler güzeldi. Bahçede kuşlar da vardı.”</i></p>`, lines: 3 },
    { q: '<p><b>“Okulumda En Sevdiğim Yer” konulu, giriş-gelişme-sonuç bölümlerinden oluşan kısa bir yazı yazınız.</b> Yazınıza bir başlık koyunuz; en az bir deyim ve bir benzetme kullanınız; yazım ve noktalama kurallarına dikkat ediniz.</p>', lines: 9 },
  ],

  cevaplar: [
    '<b>Sararmış:</b> eskidiği için rengi solup sarıya dönmüş. İpucu: kâğıt “eski” bir kitabın arasından çıkmış ve “yıllar önce” yazılmış. <b>İlham:</b> birine bir iş yapma isteği, fikri ve cesareti vermek; örnek olmak. İpucu: mektubu yazan çocuk kitaplardan etkilenip kütüphane müdürü olmuş, Elif de onun gibi başkalarına örnek olmak istiyor.',
    'a) Mahalledeki küçük kütüphanede. b) Kasım ayının yağmurlu bir pazartesi günü, okul çıkışında. c) Yıllar önce bir öğrencinin kütüphaneciye yazdığı sararmış bir teşekkür mektubu buldu. d) Çünkü mektubu yazan çocuk, artık şehrin en büyük kütüphanesinin müdürü olmuştu; bu durum onu duygulandırdı.',
    '<b>Anahtar kelimeler:</b> kütüphane, kitap, mektup, ilham (hayal de kabul edilir). <b>Başlık önerisi:</b> “Kitaplardan Gelen Mektup”, “Bir Mektubun İzinde”, “Görünmez Köprüler” gibi konuya uygun başlıklar doğrudur.',
    'Kitaplar, farklı zamanlarda yaşayan insanları birbirine bağlar: Yıllar önce okuyan bir öğrenci ile bugünkü Elif aynı kitaplar sayesinde birbirine “dokunmuştur”. Köprü gerçek bir köprü değildir; kitapların insanlar arasında kurduğu bağ anlatılmaktadır.',
    '<b>Gözleri dolmak:</b> duygulanıp ağlayacak duruma gelmek. Örnek cümle: <i>Dedemin anlattığı anıyı dinlerken gözlerim doldu.</i>',
    'a) Suyu boşa harcamamalıyız; su çok değerlidir, her damla bir canlıya hayat verir. b) Su Tasarrufu Kulübü. c) Açık musluk ve damlayan su damlası çizimi, mavi renkler, büyük harflerle yazılmış “BİR DAMLA SU, BİR HAYAT!” başlığı ve “Musluğu açık bırakma!” uyarısı mesajı destekler.',
    '<b>Eş anlamlı:</b> yanıt → cevap, sene → yıl, armağan → hediye. <b>Zıt anlamlı:</b> eski → yeni, cömert → cimri, erken → geç.',
    'Örnek: <i>Sabah kalkınca yüzümü yıkadım.</i> (surat) — <i>Okulumuzda yüz öğrenci var.</i> (sayı) — <i>Yazın denizde yüzmeyi severim.</i> (yüzmek) gibi cümleler doğrudur.',
    'a) <i>Kardeşim de okula gidiyor mu?</i> (cümle başı büyük harf; soru eki ayrı) b) <i>Yaz tatilinde İzmir’e gittik, oradaki deniz çok güzeldi.</i> (şehir adı büyük harf) c) <i>Bu kitabı üç günde bitirdim, sen de okumalısın.</i> (bağlaç “de” ayrı) d) <i>Cumhuriyet, 29 Ekim 1923’te ilan edildi.</i> (belirli tarih bildiren ay adı büyük) e) <i>Bu kelimenin yazılışını TDK’ye sordum.</i> (ek, okunuşa uyar: “tedeke”ye)',
    'a) <i>Çantama kalem, silgi, cetvel ve defter koydum.</i> b) <i>Eyvah! Otobüsü kaçırdık.</i> c) <i>Öğretmenimiz şöyle dedi: “Yarın müzeye gideceğiz.”</i> d) <i>Bugün kütüphaneye gidecek misin?</i> e) <i>Ankara’ya 2026’da taşındık.</i>',
    'Örnek: <i>Evimizin arkasındaki bahçe, bahar gelince adeta bir masal diyarına dönüşürdü. Rengârenk laleler, mis kokulu güller ve bembeyaz papatyalar yan yana dizilirdi. Ağaçların dallarında cıvıl cıvıl öten serçeler, bu güzelliğe neşeli bir şarkıyla eşlik ederdi.</i> Tekrarlardan kaçınan, betimleyici kelimeler kullanan her yazı doğrudur.',
    'Değerlendirmede şunlara bakılır: konuya uygun bir başlık; giriş, gelişme ve sonuç paragrafları; paragraf başlarında içeriden başlama; en az bir deyim (ör. “gözüm gibi bakmak”) ve bir benzetme (ör. “kütüphane bir hazine sandığı gibidir”); büyük harf, “de/da”, “mi” ve noktalama kurallarına uygunluk.',
  ],

  kontrol: [
    'Bilmediğim bir kelimenin anlamını cümledeki ipuçlarından tahmin edebiliyorum.',
    'Bir metinde Kim? Ne? Nerede? Ne zaman? Nasıl? Neden? sorularının cevaplarını bulabiliyorum.',
    'Bir afişin ya da görselin vermek istediği mesajı açıklayabiliyorum.',
    'Bir metnin anahtar kelimelerini bulup metne uygun bir başlık önerebiliyorum.',
    'Eş anlamlı, zıt anlamlı ve sesteş kelimelere örnek verebiliyorum.',
    'Deyim ve atasözlerinin anlamını açıklayıp cümlede kullanabiliyorum.',
    'Giriş, gelişme ve sonuç bölümlerinden oluşan bir yazı yazabiliyorum.',
    'Büyük harflerin, sayıların, “de/da”, “ki” ve “mi”nin yazımını doğru yapabiliyorum.',
    'Nokta, virgül, soru, ünlem, iki nokta, kesme, tırnak ve üç nokta işaretlerini yerinde kullanabiliyorum.',
  ],
};
