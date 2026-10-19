// 5. sınıf Sosyal Bilgiler · 1. dönem 1. ortak yazılı (MEB KSDT 2026-2027)

const grupSvg = `<svg width="520" height="210" viewBox="0 0 520 210" font-family="Nunito, sans-serif" font-size="12" font-weight="700">
  <circle cx="260" cy="105" r="44" fill="#ffd34d"/>
  <text x="260" y="101" text-anchor="middle" fill="#4a3a00" font-size="14" font-weight="800">BEN</text>
  <text x="260" y="118" text-anchor="middle" fill="#4a3a00" font-size="10">(Elif, 10 yaş)</text>
  <g stroke="#9aa5b1" stroke-width="2" stroke-dasharray="4 3">
    <line x1="220" y1="85" x2="120" y2="45"/><line x1="300" y1="85" x2="400" y2="45"/>
    <line x1="216" y1="110" x2="110" y2="110"/><line x1="304" y1="110" x2="410" y2="110"/>
    <line x1="225" y1="132" x2="125" y2="175"/><line x1="295" y1="132" x2="395" y2="175"/>
  </g>
  <g>
    <rect x="20" y="22" width="150" height="44" rx="12" fill="#ff8fb8"/>
    <text x="95" y="40" text-anchor="middle" fill="#fff">AİLE</text><text x="95" y="56" text-anchor="middle" fill="#fff" font-size="10.5">rolü: evlat, abla</text>
    <rect x="350" y="22" width="150" height="44" rx="12" fill="#3b8ef0"/>
    <text x="425" y="40" text-anchor="middle" fill="#fff">SINIF</text><text x="425" y="56" text-anchor="middle" fill="#fff" font-size="10.5">rolü: öğrenci, sınıf başkanı</text>
    <rect x="10" y="88" width="150" height="44" rx="12" fill="#20b3a5"/>
    <text x="85" y="106" text-anchor="middle" fill="#fff">VOLEYBOL TAKIMI</text><text x="85" y="122" text-anchor="middle" fill="#fff" font-size="10.5">rolü: oyuncu, kaptan</text>
    <rect x="360" y="88" width="150" height="44" rx="12" fill="#b48ef0"/>
    <text x="435" y="106" text-anchor="middle" fill="#fff">OKUL KULÜBÜ</text><text x="435" y="122" text-anchor="middle" fill="#fff" font-size="10.5">rolü: kulüp üyesi</text>
    <rect x="20" y="154" width="150" height="44" rx="12" fill="#ff9a3c"/>
    <text x="95" y="172" text-anchor="middle" fill="#fff">ARKADAŞ GRUBU</text><text x="95" y="188" text-anchor="middle" fill="#fff" font-size="10.5">rolü: arkadaş</text>
    <rect x="350" y="154" width="150" height="44" rx="12" fill="#3fbf62"/>
    <text x="425" y="172" text-anchor="middle" fill="#fff">MAHALLE</text><text x="425" y="188" text-anchor="middle" fill="#fff" font-size="10.5">rolü: komşu</text>
  </g>
</svg>`;

const ankaraSvg = `<svg width="390" height="225" viewBox="0 0 520 300" font-family="Nunito, sans-serif" font-size="12.5" font-weight="800">
  <g stroke="#fff" stroke-width="3">
    <polygon points="150,20 260,20 250,80 175,95 120,70" fill="#9fd3c7"/>
    <polygon points="260,20 380,30 375,95 300,100 250,80" fill="#ffcf8a"/>
    <polygon points="375,95 470,110 455,170 360,165 330,130" fill="#c9b6f2"/>
    <polygon points="360,165 455,170 430,240 340,230" fill="#ffb3c7"/>
    <polygon points="250,215 340,230 330,285 230,285" fill="#a9d0f5"/>
    <polygon points="100,190 250,215 230,285 80,280" fill="#f6e08a"/>
    <polygon points="40,75 120,70 175,95 160,185 100,190 30,170" fill="#b9e3a6"/>
    <polygon points="175,95 250,80 300,100 330,130 360,165 340,230 250,215 160,185" fill="#e84f8a"/>
  </g>
  <text x="190" y="52" text-anchor="middle" fill="#234">BOLU</text>
  <text x="315" y="62" text-anchor="middle" fill="#234">ÇANKIRI</text>
  <text x="405" y="138" text-anchor="middle" fill="#234">KIRIKKALE</text>
  <text x="395" y="205" text-anchor="middle" fill="#234">KIRŞEHİR</text>
  <text x="283" y="262" text-anchor="middle" fill="#234">AKSARAY</text>
  <text x="160" y="250" text-anchor="middle" fill="#234">KONYA</text>
  <text x="95" y="135" text-anchor="middle" fill="#234">ESKİŞEHİR</text>
  <text x="258" y="160" text-anchor="middle" fill="#fff" font-size="16">ANKARA</text>
  <g transform="translate(480,40)" font-size="11">
    <line x1="0" y1="18" x2="0" y2="-14" stroke="#234" stroke-width="2"/>
    <polygon points="0,-20 -6,-8 6,-8" fill="#234"/>
    <text x="0" y="32" text-anchor="middle" fill="#234">K</text>
  </g>
</svg>`;

const konumSvg = `<svg width="440" height="102" viewBox="0 0 520 120" font-family="Nunito, sans-serif" font-size="12" font-weight="700">
  <rect x="10" y="10" width="240" height="100" rx="14" fill="#e8f3ff" stroke="#3b8ef0" stroke-width="2"/>
  <text x="130" y="34" text-anchor="middle" fill="#1f6fd1" font-size="14" font-weight="800">GÖRECELİ KONUM</text>
  <text x="130" y="56" text-anchor="middle" fill="#183457">Bir yerin başka yerlere göre</text>
  <text x="130" y="72" text-anchor="middle" fill="#183457">anlatılan konumu</text>
  <text x="130" y="96" text-anchor="middle" fill="#183457" font-style="italic" font-size="11">"Okulum parkın karşısında."</text>
  <rect x="270" y="10" width="240" height="100" rx="14" fill="#fff4e6" stroke="#ff9a3c" stroke-width="2"/>
  <text x="390" y="34" text-anchor="middle" fill="#d9740f" font-size="14" font-weight="800">MUTLAK (KESİN) KONUM</text>
  <text x="390" y="56" text-anchor="middle" fill="#183457">Paralel ve meridyenlerle</text>
  <text x="390" y="72" text-anchor="middle" fill="#183457">belirlenen, değişmeyen konum</text>
  <text x="390" y="96" text-anchor="middle" fill="#183457" font-style="italic" font-size="11">(Üst sınıflarda öğreneceksin.)</text>
</svg>`;

export default {
  ad: 'Sosyal Bilgiler',
  dosya: 'Sosyal-Bilgiler',
  kapsam: [
    { kod: 'SB.5.1.1', metin: 'Dâhil olduğu gruplar ve bu gruplardaki rolleri arasındaki ilişkileri çözümleyebilme' },
    { kod: 'SB.5.1.2', metin: 'Kültürel özelliklere saygı duymanın birlikte yaşamaya etkisini yorumlayabilme' },
    { kod: 'SB.5.1.3', metin: 'Toplumsal birliği sürdürmeye yönelik yardımlaşma ve dayanışma faaliyetlerine katkı sağlayabilme' },
    { kod: 'SB.5.2.1', metin: 'Yaşadığı ilin göreceli konum özelliklerini algılayabilme' },
  ],
  kapsamNot: '1. Ünite "Birlikte Yaşamak" tamamı + 2. Ünite "Evimiz Dünya" ilk konusu. Soru sayısı okulun seçtiği senaryoya göre değişir; en çok soru genellikle yardımlaşma–dayanışma konusundan gelir.',
  icerik: [
    // ---------------- 1 ----------------
    { h: 'Gruplar ve Roller', no: 1, kod: 'SB.5.1.1' },
    { p: '<b>Grup</b>; ortak bir amaç, ilgi ya da bağ etrafında bir araya gelen ve birbiriyle etkileşim içinde olan insan topluluğudur. Her insan aynı anda <b>birden fazla grubun</b> üyesidir.' },
    { svg: grupSvg, caption: 'Bir öğrencinin dâhil olduğu gruplar ve bu gruplardaki rolleri' },
    { h2: 'Rol ve Sorumluluk' },
    { p: '<b>Rol</b>, bir kişinin içinde bulunduğu grupta üstlendiği görev ve bu göreve uygun davranışlardır. Her rol, beraberinde <b>sorumluluklar</b> (yapılması gereken görevler) ve <b>haklar</b> getirir.' },
    { table: {
      head: ['Grup', 'Rol', 'Sorumluluk örneği'],
      rows: [
        ['Aile', 'Evlat, kardeş', 'Ev işlerine yardım etmek, büyüklerine saygı göstermek'],
        ['Sınıf', 'Öğrenci', 'Ödevlerini zamanında yapmak, sınıf kurallarına uymak'],
        ['Sınıf', 'Sınıf başkanı', 'Arkadaşlarının isteklerini öğretmene iletmek, örnek olmak'],
        ['Spor takımı', 'Oyuncu / kaptan', 'Antrenmanlara düzenli gelmek, takım arkadaşlarını desteklemek'],
        ['Okul kulübü', 'Kulüp üyesi', 'Kulüp etkinliklerine katılmak, görevini üstlenmek'],
        ['Mahalle', 'Komşu', 'Çevreyi temiz tutmak, gürültü yapmamak, komşulara yardım etmek'],
      ],
    } },
    { box: 'hatirla', html: '<ul><li>Gruplara <b>doğuştan</b> (aile, akrabalar) ya da <b>sonradan, kendi isteğimizle</b> (kulüp, takım, arkadaş grubu) katılırız.</li><li>Bir kişinin rolü gruba göre değişir: Evde <b>abla</b> olan Elif, okulda <b>öğrenci</b>, takımda <b>kaptan</b>dır.</li><li>Rollerimizi yerine getirmek grubun düzenini ve uyumunu sağlar.</li></ul>' },
    { h2: 'Roller Arasındaki İlişki ve Rol Çatışması' },
    { p: 'Rollerimiz birbirini etkiler. Bazen iki rolün sorumlulukları <b>aynı anda</b> yerine getirilemez. Buna <b>rol çatışması</b> denir.' },
    { box: 'ornek', html: '<p>Can, cumartesi günü takımının maçına gitmek zorundadır (<b>oyuncu</b> rolü). Aynı saatte babaannesinin doğum günü kutlaması vardır (<b>torun</b> rolü). Can, antrenörüyle ve ailesiyle konuşur; maçtan sonra kutlamaya katılarak iki rolünü de dengeler.</p>' },
    { ul: [
      'Rol çatışmasını çözmek için <b>öncelik</b> belirlenir, <b>planlama</b> yapılır.',
      'İlgili kişilerle <b>iletişim</b> kurulur, <b>uzlaşma</b> (ortak noktada buluşma) aranır.',
      'Verilen sözlere ve sorumluluklara sadık kalmak, gruptaki <b>güveni</b> artırır.',
    ] },

    // ---------------- 2 ----------------
    { h: 'Kültürel Özelliklere Saygı ve Birlikte Yaşama', no: 2, kod: 'SB.5.1.2' },
    { p: '<b>Kültür</b>, bir toplumun yüzyıllar boyunca oluşturduğu ve nesilden nesile aktardığı maddi ve manevi değerlerin tamamıdır.' },
    { cols: [
      [{ h2: 'Maddi kültür ögeleri' }, { ul: ['Yemekler (mantı, keşkek, baklava)', 'Kıyafetler, yöresel giysiler', 'El sanatları (halı, kilim, çini, bakırcılık)', 'Mimari yapılar, evler'] }],
      [{ h2: 'Manevi kültür ögeleri' }, { ul: ['Dil, şive (ağız), atasözleri', 'Gelenek ve görenekler, örf ve âdetler', 'Bayramlar, düğün ve kına gecesi', 'Türküler, halk oyunları, masallar'] }],
    ] },
    { table: {
      head: ['Kavram', 'Anlamı'],
      rows: [
        ['<b>Gelenek</b>', 'Eskiden beri süregelen, kuşaktan kuşağa aktarılan alışkanlıklar (bayramda büyükleri ziyaret etmek).'],
        ['<b>Görenek</b>', 'Toplumda görerek öğrenilen ve uygulanan davranışlar (misafire ikram etmek).'],
        ['<b>Örf ve âdet</b>', 'Toplumun benimsediği, uyulması beklenen yazısız kurallar (asker uğurlama, kız isteme).'],
        ['<b>Şive (ağız)</b>', 'Aynı dilin farklı yörelerde farklı söylenişi.'],
      ],
    } },
    { h2: 'Farklılıklar Zenginliktir' },
    { p: 'Ülkemizin farklı bölgelerinde yaşayan insanların yemekleri, giysileri, düğünleri ve konuşmaları farklılık gösterebilir. Bu farklılıklar bizi ayırmaz; tam tersine <b>ortak kültürümüzü zenginleştirir.</b>' },
    { ul: [
      '<b>Saygı:</b> Farklı kültürel özellikleri alay konusu yapmamak, onları değerli görmek.',
      '<b>Empati:</b> Kendini başkasının yerine koyarak onun duygu ve düşüncelerini anlamaya çalışmak.',
      '<b>Hoşgörü:</b> Farklı düşünce ve alışkanlıkları anlayışla karşılamak.',
    ] },
    { box: 'ornek', html: '<p>Sınıfa Erzurum’dan yeni gelen Ayşe’nin konuşması bazı arkadaşlarına farklı gelir. Öğretmen, “Kültür Haftası” düzenler; her öğrenci kendi ailesinin yöresine ait bir yemek, türkü ya da oyun tanıtır. Öğrenciler birbirlerini daha iyi tanır, sınıfta <b>dostluk ve birlik</b> artar.</p>' },
    { box: 'dikkat', html: '<p>Kültürel farklılıklara saygı gösterildiğinde toplumda <b>huzur, güven, dostluk ve barış</b> artar. Saygı gösterilmediğinde ise <b>kırgınlık, ön yargı ve anlaşmazlıklar</b> ortaya çıkar; birlikte yaşamak zorlaşır.</p>' },

    // ---------------- 3 ----------------
    { h: 'Yardımlaşma ve Dayanışma', no: 3, kod: 'SB.5.1.3' },
    { p: '<b>Yardımlaşma</b>, insanların birbirlerine maddi ve manevi destek olmasıdır. <b>Dayanışma</b> ise bir toplumun üyelerinin ortak amaçlar ve zor zamanlar için birlik içinde hareket etmesidir.' },
    { h2: 'Kültürümüzde Yardımlaşma Gelenekleri' },
    { table: {
      head: ['Gelenek / Kurum', 'Açıklama'],
      rows: [
        ['<b>İmece</b>', 'Köyde, mahallede bir işin herkesin katılımıyla birlikte yapılması (ev yapımı, hasat, salça yapımı).'],
        ['<b>Ahilik</b>', 'Esnaf ve sanatkârları dürüstlük, cömertlik ve yardımlaşma ilkeleri etrafında birleştiren teşkilat. Ahi Evran tarafından kurulmuştur.'],
        ['<b>Vakıflar</b>', 'Bir malın, toplum yararına (çeşme, okul, aşevi, hastane) sürekli kullanılmak üzere bağışlanmasıyla oluşan kurumlar.'],
        ['<b>Askıda ekmek</b>', 'Fırından fazladan ekmek alıp ihtiyacı olanlar için askıya bırakmak.'],
        ['<b>Bayram paylaşımları</b>', 'Ramazan Bayramı’nda fitre ve zekât, Kurban Bayramı’nda kurban etinin paylaşılması.'],
      ],
    } },
    { h2: 'Yardımlaşma ve Dayanışma Kurumları' },
    { table: {
      head: ['Kurum', 'Ne yapar?'],
      rows: [
        ['<b>Türk Kızılay</b>', 'Afet ve savaş bölgelerine yardım ulaştırır, kan bağışı toplar.'],
        ['<b>AFAD</b>', 'Afet ve acil durumlarda arama-kurtarma, barınma ve koordinasyon hizmeti verir.'],
        ['<b>TEMA Vakfı</b>', 'Erozyonla mücadele eder, ağaçlandırma ve doğa koruma çalışmaları yapar.'],
        ['<b>LÖSEV</b>', 'Lösemili çocuklara ve ailelerine destek olur.'],
        ['<b>Darüşşafaka</b>', 'Maddi imkânı kısıtlı çocukların eğitimine destek olur.'],
        ['<b>Türkiye Diyanet Vakfı</b>', 'Yurt içi ve dışında ihtiyaç sahiplerine yardım ulaştırır.'],
      ],
    } },
    { h2: 'Toplumsal Birliğe Etkisi' },
    { ul: [
      'İnsanlar arasında <b>sevgi, güven ve kardeşlik</b> duygularını güçlendirir.',
      'Zor zamanlarda (deprem, sel, yangın) yaraların <b>daha hızlı sarılmasını</b> sağlar.',
      'Toplumda <b>yalnızlık ve çaresizlik</b> duygusunu azaltır, “biz” bilincini artırır.',
      'Yardım edenlere de <b>mutluluk ve sorumluluk bilinci</b> kazandırır.',
    ] },
    { h2: 'Ben Nasıl Katkı Sağlayabilirim?' },
    { cols: [
      [{ ul: ['Okulda kitap, kırtasiye ya da kıyafet kampanyasına katılmak', 'Sınıfta ders anlamakta zorlanan arkadaşıma yardım etmek', 'Yaşlı komşularımın alışverişine yardım etmek'] }],
      [{ ul: ['Fidan dikimi, çevre temizliği etkinliklerine katılmak', 'Sokak hayvanları için mama ve su kabı koymak', 'Harçlığımdan bir kısmını yardım kampanyasına ayırmak'] }],
    ] },
    { box: 'bilgi', html: '<p>6 Şubat 2023 depremlerinden sonra ülkemizin dört bir yanından insanlar battaniye, yiyecek ve oyuncak topladı; gönüllüler bölgeye koştu. Bu, milletimizin <b>dayanışma</b> gücünün en güzel örneklerinden biridir.</p>' },

    // ---------------- 4 ----------------
    { h: 'Yaşadığım İlin Göreceli Konumu', no: 4, kod: 'SB.5.2.1' },
    { p: '<b>Konum</b>, bir yerin dünya üzerinde bulunduğu yerdir. 5. sınıfta <b>göreceli konum</b> üzerinde duruyoruz.' },
    { svg: konumSvg },
    { p: 'Göreceli konum anlatılırken şunlardan yararlanılır:' },
    { ul: [
      '<b>Yönler:</b> Kuzey, güney, doğu, batı ve ara yönler (kuzeydoğu, güneybatı…).',
      '<b>Komşu iller:</b> İlimizin sınır komşusu olan iller.',
      '<b>Denize yakınlık / uzaklık:</b> İlin denize kıyısı var mı, en yakın deniz hangisi?',
      '<b>Önemli yerlere uzaklık:</b> Başkent, büyük şehirler, dağlar, göller, akarsular.',
      '<b>Bulunduğu bölge:</b> İlin yer aldığı coğrafi bölge.',
    ] },
    { h2: 'Örnek: Ankara’nın Göreceli Konumu' },
    { cols: [
      [{ svg: ankaraSvg, caption: 'Basitleştirilmiş şema: Ankara ve komşu illeri (sınırlar gerçek ölçüde değildir)' }],
      [{ ul: [
      'Ankara, <b>İç Anadolu Bölgesi</b>’nde yer alır ve ülkemizin <b>başkentidir</b>.',
      'Komşuları: kuzeyde <b>Bolu</b> ve <b>Çankırı</b>, doğuda <b>Kırıkkale</b>, güneydoğuda <b>Kırşehir</b>, güneyde <b>Aksaray</b> ve <b>Konya</b>, batıda <b>Eskişehir</b>.',
      'Ankara’nın <b>denize kıyısı yoktur</b>; en yakın deniz kuzeydeki <b>Karadeniz</b>’dir.',
      'Türkiye’nin <b>orta kesiminde</b> yer aldığı için ülkenin pek çok yerine ulaşım kolaydır.',
    ] }],
    ] },
    { box: 'ipucu', html: '<p>Göreceli konumu anlatırken <b>“-in kuzeyinde, -e yakın, -den uzak, -in komşusu”</b> gibi ifadeler kullan. Örnek: “Bursa, Marmara Denizi’nin güneyinde, İstanbul’a yakın bir ildir.”</p>' },
  ],

  sorular: [
    { q: '<p>Dâhil olduğun üç grubu ve bu gruplardaki rollerini yaz. Her rol için bir sorumluluk örneği ver.</p>', lines: 3 },
    { q: '<p>Zeynep sınıf başkanıdır ve aynı zamanda okulun satranç kulübündedir. Kulüp toplantısı ile sınıf başkanları toplantısı aynı saate denk gelmiştir. Zeynep’in yaşadığı durumun adı nedir? Bu sorunu nasıl çözebilir?</p>', lines: 3 },
    { q: '<p>“Ailede baba, işyerinde öğretmen, futbol takımında kaleci.” Bu ifade, roller hakkında bize ne anlatmaktadır?</p>', lines: 3 },
    { q: '<p>Aşağıdaki kültür ögelerini <b>maddi</b> ve <b>manevi</b> olarak sınıflandır:<br><i>kilim – türkü – keşkek – bayramlaşma – çini – atasözü</i></p>', lines: 3 },
    { q: '<p>Sınıfa başka bir ilden gelen arkadaşının konuşmasıyla bazı öğrenciler alay ediyor. Bu davranış birlikte yaşamayı nasıl etkiler? Sen olsan ne yapardın?</p>', lines: 3 },
    { q: '<p>Kültürel farklılıklara saygı göstermenin toplum hayatına iki olumlu etkisini yaz.</p>', lines: 2 },
    { q: '<p><b>İmece</b> ve <b>ahilik</b> geleneklerini kısaca açıkla. Bu geleneklerin ortak özelliği nedir?</p>', lines: 3 },
    { q: '<p>Ülkemizde bir sel felaketi yaşandığını düşün. Bu durumda hangi kurumlar yardım eder? Bir öğrenci olarak sen nasıl katkı sağlayabilirsin?</p>', lines: 2 },
    { q: '<p>Yardımlaşma ve dayanışmanın toplumsal birliğe iki katkısını yaz.</p>', lines: 2 },
    { q: '<p>Okulunda bir yardımlaşma kampanyası düzenleyeceksin. Kampanyanın adını, amacını ve yapılacak iki etkinliği yaz.</p>', lines: 2 },
    { q: '<p>“Okulum, caminin arkasında ve parkın karşısındadır.” Bu cümlede hangi konum türü kullanılmıştır? Neden?</p>', lines: 2 },
    { q: '<p>Yukarıdaki Ankara şemasına göre Ankara’nın göreceli konumunu üç cümleyle anlat. (Komşu iller, yön ve denize uzaklık bilgilerini kullan.)</p>', lines: 2 },
    { q: '<p><b>Benim İlim:</b> Atlas ya da harita kullanarak kendi ilinin göreceli konumunu yaz: bulunduğu bölge, komşu illeri, denize kıyısı olup olmadığı (en yakın deniz) ve yakın olduğu önemli bir yer.</p>', lines: 2 },
  ],

  cevaplar: [
    'Örnek: <b>Aile</b> – evlat: odamı toplarım, büyüklerime saygı gösteririm. <b>Sınıf</b> – öğrenci: ödevlerimi zamanında yaparım. <b>Futbol takımı</b> – oyuncu: antrenmanlara düzenli giderim. (Kendi gruplarını yazman yeterlidir.)',
    'Durumun adı <b>rol çatışması</b>dır. Zeynep öncelik belirleyip öğretmeni ve kulüp sorumlusuyla konuşabilir; toplantılardan birine katılıp diğerinde alınan kararları arkadaşından öğrenebilir ya da yerine başka bir arkadaşının katılmasını isteyebilir.',
    'Bir kişi aynı anda <b>birden fazla grubun üyesidir</b> ve her grupta <b>farklı bir rolü</b> vardır. Kişinin rolü bulunduğu gruba göre değişir.',
    '<b>Maddi:</b> kilim, keşkek, çini. <b>Manevi:</b> türkü, bayramlaşma, atasözü.',
    'Bu davranış arkadaşın kırılmasına, sınıfta ön yargı ve anlaşmazlığa yol açar; birlikte yaşamayı zorlaştırır. Ben arkadaşlarımı uyarır, yeni arkadaşımla <b>empati</b> kurar, onun yöresini tanımaya çalışırım; farklılıkların zenginlik olduğunu anlatırım.',
    'Toplumda <b>huzur ve barış</b> artar; insanlar arasında <b>dostluk ve güven</b> gelişir; farklı kültürleri tanıyarak ortak kültürümüz zenginleşir.',
    '<b>İmece:</b> Bir köy ya da mahallede bir işin herkesin katılımıyla birlikte yapılmasıdır. <b>Ahilik:</b> Esnaf ve sanatkârları dürüstlük ve yardımlaşma ilkeleriyle birleştiren teşkilattır. <b>Ortak özellik:</b> İkisi de yardımlaşma ve dayanışmaya dayanır.',
    'Kurumlar: <b>AFAD</b>, <b>Türk Kızılay</b> (ayrıca belediyeler, vakıflar). Katkım: yardım kampanyasına giyecek, yiyecek, oyuncak bağışlamak; harçlığımdan bağış yapmak; ailemle birlikte gönüllü toplama çalışmalarına katılmak.',
    'İnsanlar arasında sevgi, güven ve kardeşliği artırır; zor zamanlarda yaraların hızla sarılmasını sağlar; “biz” bilincini güçlendirir.',
    'Örnek: <b>“Kitabım Senin Olsun”</b> kampanyası. Amaç: Kitaba ulaşmakta zorlanan okullardaki öğrencilere kitap göndermek. Etkinlikler: Sınıflarda kitap toplama kutusu kurmak; toplanan kitapları sınıflandırıp kolilemek.',
    '<b>Göreceli konum</b> kullanılmıştır; çünkü okulun yeri başka yerlere (cami, park) göre anlatılmıştır.',
    'Örnek: Ankara, İç Anadolu Bölgesi’nde yer alır. Kuzeyinde Bolu ve Çankırı, doğusunda Kırıkkale, güneyinde Aksaray ve Konya, batısında Eskişehir bulunur. Ankara’nın denize kıyısı yoktur; en yakın deniz kuzeydeki Karadeniz’dir.',
    'Kendi iline göre cevaplarsın. Örnek (İzmir): Ege Bölgesi’ndedir; komşuları Balıkesir, Manisa ve Aydın’dır; batısında Ege Denizi vardır, denize kıyısı vardır; Manisa’ya ve Gediz Nehri’ne yakındır.',
  ],

  kontrol: [
    'Grup kavramını açıklayabilir, dâhil olduğum grupları sayabilirim.',
    'Farklı gruplardaki rollerimi ve sorumluluklarımı örneklerle anlatabilirim.',
    'Rol çatışmasını tanır, çözüm yolları önerebilirim.',
    'Kültür ögelerini maddi–manevi diye ayırır; gelenek, görenek, örf-âdet kavramlarını açıklayabilirim.',
    'Kültürel farklılıklara saygının birlikte yaşamaya etkisini yorumlayabilirim.',
    'İmece, ahilik, vakıf geleneklerini ve Kızılay, AFAD, TEMA, LÖSEV gibi kurumların görevlerini bilirim.',
    'Yardımlaşma ve dayanışmaya nasıl katkı sağlayabileceğimi söyleyebilirim.',
    'Yaşadığım ilin göreceli konumunu komşu iller, yönler ve denize göre anlatabilirim.',
  ],
};
