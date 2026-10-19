// 5. sınıf Din Kültürü ve Ahlak Bilgisi – 1. dönem 1. ortak yazılı çalışma notları
const suDongusu = `<svg width="520" height="200" viewBox="0 0 520 200" font-family="Nunito, sans-serif" font-size="12" font-weight="700">
  <defs><marker id="dk-ok" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto"><path d="M0 0 L8 4 L0 8Z" fill="#3c7fd9"/></marker></defs>
  <circle cx="60" cy="45" r="24" fill="#ffd34d"/><text x="60" y="88" text-anchor="middle" fill="#8a6a00">Güneş</text>
  <path d="M20 180 Q140 160 260 180 T500 180 V200 H20Z" fill="#7fc8e8"/><text x="120" y="194" fill="#fff">Deniz / göl</text>
  <ellipse cx="300" cy="40" rx="55" ry="20" fill="#dfe8f2"/><ellipse cx="340" cy="30" rx="40" ry="18" fill="#dfe8f2"/><text x="315" y="44" text-anchor="middle" fill="#456">Bulut</text>
  <path d="M420 170 L460 90 L500 170Z" fill="#9bc79b"/>
  <path d="M150 165 Q170 110 240 60" stroke="#3c7fd9" stroke-width="2.5" fill="none" stroke-dasharray="5 4" marker-end="url(#dk-ok)"/>
  <text x="110" y="120" fill="#3c7fd9">1. Buharlaşma</text>
  <path d="M370 55 Q420 60 440 95" stroke="#3c7fd9" stroke-width="2.5" fill="none" marker-end="url(#dk-ok)"/>
  <text x="395" y="52" fill="#3c7fd9">2. Yoğuşma</text>
  ${[0,1,2,3].map(i => `<line x1="${290+i*18}" y1="70" x2="${284+i*18}" y2="95" stroke="#3c7fd9" stroke-width="2"/>`).join('')}
  <text x="268" y="115" fill="#3c7fd9">3. Yağış</text>
  <path d="M430 170 Q380 178 330 176" stroke="#3c7fd9" stroke-width="2.5" fill="none" marker-end="url(#dk-ok)"/>
  <text x="345" y="166" fill="#3c7fd9">4. Akış</text>
</svg>`;

export default {
  ad: 'Din Kültürü ve Ahlak Bilgisi',
  dosya: 'Din-Kulturu',
  kapsam: [
    { kod: 'DKAB.5.1.1', metin: 'Evrendeki mükemmel düzene ilişkin akıl yürütebilme' },
    { kod: 'DKAB.5.1.2', metin: 'Evrendeki mükemmel düzenden hareketle Allah’ın (cc) varlığı ve birliğini müşahede edebilme (en çok soru buradan: 2–3 soru)' },
    { kod: 'DKAB.5.1.3', metin: 'Allah’ın (cc) güzel isimlerini bağlamına uygun kullanabilme' },
    { kod: 'DKAB.5.1.4', metin: 'İhlas suresini ve bu surenin anlamını okuyarak yorumlayabilme' },
    { kod: 'DKAB.5.2.1', metin: 'Namaz ibadetini özetleyebilme (yalnızca bazı senaryolarda)' },
  ],
  kapsamNot: '1. Ünite “Allah İnancı” konularının tamamı ve 2. Ünite “Namaz”ın ilk konusu. Hangi senaryonun uygulanacağını okulundaki zümre öğretmenleri seçer; namaz konusu bazı senaryolarda soruluyor, öğretmenine sor. Sorular açık uçlu olabilir: cevabını kendi cümlelerinle, gerekçesiyle yaz.',
  icerik: [
    { h: 'Evrendeki Mükemmel Düzen', no: 1, kod: 'DKAB.5.1.1' },
    { p: 'Etrafımıza baktığımızda her şeyin <b>belli bir ölçü, uyum ve amaç</b> içinde gerçekleştiğini görürüz. Hiçbir şey gelişigüzel değildir. Buna <b>evrendeki düzen</b> denir. Bu düzen sayesinde canlılar yaşamını sürdürebilir.' },
    { table: { head: ['Düzen örneği', 'Ne görüyoruz?', 'Düzen bozulsaydı ne olurdu?'], rows: [
      ['Gece ve gündüz', 'Dünya kendi ekseni etrafında döner; gece ve gündüz düzenli olarak birbirini izler.', 'Hep gündüz ya da hep gece olsaydı canlılar dinlenemez, bitkiler büyüyemezdi.'],
      ['Mevsimler', 'Dünya’nın Güneş etrafında dolanması ve eksen eğikliği ile mevsimler sırayla gelir.', 'Tarım yapılamaz, hayvanların göç ve üreme düzeni bozulurdu.'],
      ['Gezegenlerin yörüngeleri', 'Gezegenler kendi yörüngelerinde çarpışmadan döner.', 'Gök cisimleri birbirine çarpar, yaşam tehlikeye girerdi.'],
      ['İnsan vücudu', 'Kalp, akciğer, beyin gibi organlar uyum içinde, aralıksız çalışır.', 'Bir organ görevini yapmasa vücudun tamamı etkilenirdi.'],
      ['Su döngüsü', 'Su buharlaşır, bulut olur, yağmur/kar olarak yere döner.', 'Kuraklık olur, içecek su ve tarım için su bulunamazdı.'],
      ['Arıların peteği', 'Arılar altıgen petekler yapar; az malzemeyle en çok bal depolanır.', 'Bal ve tozlaşma azalır, bitkiler çoğalamazdı.'],
      ['Ekosistem dengesi', 'Bitkiler, otçullar ve etçiller arasında besin zinciri vardır.', 'Bir canlı türü yok olursa zincirin tamamı etkilenirdi.'],
    ] } },
    { svg: suDongusu, caption: 'Su döngüsü: Su sürekli dolaşır, hiçbir damla boşa gitmez. Bu da evrendeki düzenin bir örneğidir.' },
    { h2: 'Düzen hakkında akıl yürütme' },
    { p: '<b>Akıl yürütmek</b>, gördüklerimizden ve bildiklerimizden yola çıkarak bir sonuca ulaşmaktır. Örneğin bir saatin parçalarının uyum içinde çalıştığını görünce, onu bilgili bir ustanın yaptığını düşünürüz. Saatin parçaları kendi kendine bir araya gelip çalışmaz.' },
    { ol: [
      '<b>Gözlem:</b> Evrende her şey ölçülü ve uyumlu.',
      '<b>Soru:</b> Bu kadar mükemmel bir düzen kendiliğinden, tesadüfen oluşabilir mi?',
      '<b>Sonuç:</b> Düzen, onu kuran ve devam ettiren bir yaratıcının varlığını gösterir.',
    ] },
    { box: 'ornek', html: '<p>Bir kütüphanedeki kitaplar konularına göre sıralanmışsa bunu birinin düzenlediğini anlarız. Rüzgârın kitapları raflara tek tek dizmesini beklemeyiz. Evrendeki çok daha büyük düzen de onu düzenleyen bir yaratıcıyı akla getirir.</p>' },

    { h: 'Allah’ın Varlığı ve Birliği', no: 2, kod: 'DKAB.5.1.2' },
    { p: 'Evrendeki düzen, yüce bir yaratıcının, yani <b>Allah’ın (cc) varlığının</b> işaretidir. Düzenin bozulmadan sürmesi de evreni yaratan ve yöneten <b>tek bir</b> varlık olduğunu gösterir.' },
    { p: 'Allah’ın bir ve tek olduğuna, eşi, benzeri ve ortağı olmadığına inanmaya <b>tevhid</b> denir. Tevhid, İslam inancının temelidir. “Lâ ilâhe illallah” (Allah’tan başka ilah yoktur) cümlesi tevhidi ifade eder.' },
    { box: 'bilgi', title: 'KUR’AN’DAN', html: `<p>• “Eğer yerde ve gökte Allah’tan başka ilahlar olsaydı, ikisinin de düzeni bozulurdu.” <i>(Enbiyâ suresi, 22. ayet)</i></p>
      <p>• “O, yedi göğü birbiriyle uyumlu olarak yaratandır. Rahmân’ın yaratmasında hiçbir uyumsuzluk göremezsin. Gözünü çevir de bak, bir çatlak görebiliyor musun? Sonra gözünü tekrar tekrar çevir; göz (aradığı kusuru bulamayıp) yorgun ve bitkin olarak sana dönecektir.” <i>(Mülk suresi, 3–4. ayetler)</i></p>` },
    { box: 'hatirla', html: '<ul><li>Bir okulda iki müdür, bir sınıfta aynı anda iki farklı ders veren iki öğretmen olsa karışıklık çıkar. Evrende böyle bir karışıklık yoktur, çünkü evreni yöneten <b>tek</b> olan Allah’tır.</li><li>Allah hiçbir şeye benzemez. Doğmamış ve doğurmamıştır. Varlığının başlangıcı ve sonu yoktur.</li></ul>' },
    { h2: 'Müşahede ne demek?' },
    { p: '<b>Müşahede</b>, gözlemlemek, dikkatle bakıp görmek demektir. Gökyüzüne, bir çiçeğe, kendi vücudumuza dikkatle baktığımızda Allah’ın yarattıklarındaki ölçüyü, sanatı ve güzelliği fark ederiz. Böylece Allah’ın varlığını ve birliğini yaratılanlar üzerinden görürüz.' },

    { h: 'Allah’ın Güzel İsimleri (Esmâ-i Hüsnâ)', no: 3, kod: 'DKAB.5.1.3' },
    { p: 'Kur’an-ı Kerim’de ve Peygamberimizin (sav) sözlerinde Allah’ı tanıtan isimlere <b>Esmâ-i Hüsnâ</b> (en güzel isimler) denir. Bu isimler Allah’ın sıfatlarını, yani nasıl bir varlık olduğunu anlamamıza yardımcı olur.' },
    { box: 'bilgi', title: 'KUR’AN’DAN', html: '<p>“En güzel isimler Allah’ındır. O hâlde O’na o güzel isimlerle dua edin.” <i>(A‘râf suresi, 180. ayet)</i></p>' },
    { table: { head: ['İsim', 'Anlamı', 'Hayattan bir bağlam'], rows: [
      ['Hâlık', 'Yaratan, yoktan var eden', 'Bebeğin doğumu, tohumdan filiz çıkması'],
      ['Rahmân', 'Dünyada bütün canlılara merhamet eden', 'Güneşin, yağmurun herkese ulaşması'],
      ['Rahîm', 'Ahirette müminlere çok merhametli olan', 'İyiliklerin karşılığını fazlasıyla vermesi'],
      ['Rezzâk', 'Bütün canlıların rızkını veren', 'Kuşların, karıncaların yiyecek bulması'],
      ['Alîm', 'Her şeyi bilen', 'Kalbimizden geçenleri bile bilmesi'],
      ['Semî‘', 'Her şeyi işiten', 'Sessizce ettiğimiz duayı duyması'],
      ['Basîr', 'Her şeyi gören', 'Kimse görmese de yaptığımız iyiliği görmesi'],
      ['Vedûd', 'Kullarını çok seven, sevilmeye layık olan', 'İyilik yapanları sevmesi'],
      ['Gaffâr', 'Günahları çokça bağışlayan', 'Hatasından pişman olanı affetmesi'],
      ['Kerîm', 'Cömert, ikramı bol olan', 'Saymakla bitmeyecek nimetler vermesi'],
      ['Adl', 'Çok adaletli olan', 'Kimseye haksızlık etmemesi'],
      ['Hakîm', 'Her işi hikmetli, yerli yerinde olan', 'Evrendeki düzenin amaçlı ve ölçülü olması'],
      ['Melik', 'Mülkün gerçek sahibi, her şeyin hükümdarı', 'Bütün evrenin O’na ait olması'],
      ['Kuddûs', 'Her türlü eksiklikten uzak, tertemiz', 'Hiçbir kusurunun olmaması'],
    ] } },
    { h2: 'İsmi bağlamına uygun kullanmak' },
    { p: 'Bir olayı ya da durumu en iyi anlatan ismi seçebilmeliyiz. Kendine şunu sor: <i>“Bu durumda Allah’ın hangi özelliği öne çıkıyor?”</i>' },
    { box: 'ornek', html: `<ul>
      <li>Elif, kimsenin görmediği bir anda yerdeki çöpü aldı. Allah’ın <b>Basîr</b> ismini düşündü, çünkü Allah her şeyi görür.</li>
      <li>Kerem, arkadaşını kırdığı için pişman oldu ve tövbe etti. Allah’ın <b>Gaffâr</b> isminin bağışlamayı anlattığını hatırladı.</li>
      <li>Ayşe, kışın kuşlar için pencereye yem koydu. Bütün canlıların rızkını verenin Allah olduğunu, yani <b>Rezzâk</b> ismini düşündü.</li>
      <li>Ali, gökyüzündeki milyonlarca yıldızın düzenini izlerken Allah’ın <b>Hâlık</b> ve <b>Hakîm</b> isimlerini hatırladı.</li></ul>` },
    { box: 'ipucu', html: '<p>Bu isimler bize de örnek olur: Allah <b>Adl</b> olduğu için biz de adaletli olmaya çalışırız. <b>Rahmân</b> olduğu için biz de canlılara merhametli davranırız.</p>' },

    { h: 'Bir Sure Öğreniyorum: İhlas Suresi', no: 4, kod: 'DKAB.5.1.4' },
    { cols: [
      [ { h2: 'Okunuşu' }, { p: '<i>Bismillâhirrahmânirrahîm.</i>' }, { ol: [
        '<i>Kul hüvallâhü ehad.</i>',
        '<i>Allâhüssamed.</i>',
        '<i>Lem yelid ve lem yûled.</i>',
        '<i>Ve lem yekün lehû küfüven ehad.</i>',
      ] } ],
      [ { h2: 'Anlamı' }, { p: 'Rahmân ve Rahîm olan Allah’ın adıyla.' }, { ol: [
        'De ki: O, Allah’tır, bir tektir.',
        'Allah Samed’dir (her şey O’na muhtaçtır, O hiçbir şeye muhtaç değildir).',
        'O doğurmamış ve doğmamıştır.',
        'Hiçbir şey O’na denk ve benzer değildir.',
      ] } ],
    ] },
    { table: { head: ['Bilgi kartı', ''], rows: [
      ['İndiği yer', 'Mekke (Mekkî sure)'],
      ['Ayet sayısı', '4 ayet'],
      ['Mushaftaki sırası', 'Kur’an-ı Kerim’in 112. suresi'],
      ['Adının anlamı', '“İhlas”: samimiyet, içtenlik; inancı her türlü ortaktan arındırmak'],
      ['Ana konusu', 'Tevhid: Allah’ın birliği ve eşsizliği'],
    ] } },
    { h2: 'İhlas suresinin mesajları' },
    { ul: [
      'Allah <b>birdir</b>, tektir; O’nun ortağı yoktur (1. ayet).',
      'Her şey Allah’a muhtaçtır, Allah ise hiçbir şeye muhtaç değildir (2. ayet).',
      'Allah doğmamış ve doğurmamıştır; anne, baba ya da çocuk gibi bir yakını yoktur (3. ayet).',
      'Hiçbir varlık Allah’a benzemez ve O’na denk değildir (4. ayet).',
      'Bu yüzden yalnızca Allah’a ibadet edilir, yalnızca O’ndan yardım istenir. Sure, <b>tevhid</b> inancını en kısa ve açık biçimde anlatır.',
    ] },

    { h: 'Allah’ın Huzurunda Olmak: Namaz', no: 5, kod: 'DKAB.5.2.1' },
    { box: 'dikkat', title: 'SENARYOYA BAĞLI', html: '<p>Bu konu yalnızca bazı senaryolarda soruluyor. Öğretmenin hangi senaryoyu seçtiğini sor.</p>' },
    { p: '<b>Namaz</b>, belirli vakitlerde, belirli hareket ve okuyuşlarla Allah’a yapılan bir ibadettir. Namaz kılan kişi Allah’ın huzurunda olduğunu hisseder, O’na şükreder ve dua eder.' },
    { cols: [
      [ { h2: 'Bilmemiz gerekenler' }, { ul: [
        'Ergenlik çağına girmiş, aklı başında her Müslümana <b>farzdır</b> (Allah’ın kesin emri).',
        'İslam’ın beş şartından biridir.',
        'Günde <b>beş vakit</b>: <b>sabah, öğle, ikindi, akşam, yatsı</b>. Cuma günü öğlen <b>cuma namazı</b> kılınır.',
        'Önce abdest alınır; beden, elbise ve yer temiz olmalıdır.',
      ] } ],
      [ { h2: 'İnsana kazandırdıkları' }, { ul: [
        'Allah’a yakınlık ve kalp huzuru verir.',
        'Kişiyi kötülüklerden uzaklaştırır.',
        'Zamanı planlamayı ve düzenli olmayı öğretir.',
        'Temizlik alışkanlığı kazandırır.',
        'Cemaatle kılınınca birlik ve kardeşliği güçlendirir.',
      ] } ],
    ] },
    { box: 'bilgi', title: 'KUR’AN’DAN', html: '<p>“…Namaz, müminler üzerine vakitleri belirlenmiş bir farzdır.” <i>(Nisâ suresi, 103. ayet)</i></p>' },
  ],
  sorular: [
    { q: '<p>Gece ile gündüzün ve mevsimlerin düzenli olarak birbirini izlemesi evrendeki düzene örnektir. Bu düzen bozulsaydı canlıların hayatında neler olurdu? İki örnek yaz.</p>', lines: 3 },
    { q: '<p>Arıların altıgen petekler yapması ile su döngüsü arasında evrendeki düzen bakımından nasıl bir ortaklık vardır? Açıkla.</p>', lines: 3 },
    { q: '<p>Mert: “Bir saatin parçaları kendi kendine bir araya gelip çalışamaz.” dedi. Mert’in bu sözünden yola çıkarak evrendeki düzen ile Allah’ın varlığı arasında nasıl bir bağ kurabilirsin?</p>', lines: 3 },
    { q: '<p>“Eğer yerde ve gökte Allah’tan başka ilahlar olsaydı, ikisinin de düzeni bozulurdu.” (Enbiyâ suresi, 22. ayet) Bu ayet Allah’ın hangi özelliğini vurgulamaktadır? Günlük hayattan bir örnekle açıkla.</p>', lines: 3 },
    { q: '<p>“Tevhid” kavramını kendi cümlelerinle açıkla.</p>', lines: 3 },
    { q: '<p>Aşağıdaki durumlarda Allah’ın hangi güzel ismi öne çıkmaktadır? Yanlarına yaz.</p><p>a) Zeynep sessizce dua etti ve duasının duyulduğuna inandı. → ……………</p><p>b) Arda yaptığı hatadan pişman olup tövbe etti. → ……………</p><p>c) Çölde yaşayan küçük bir canlı bile yiyecek bulabiliyor. → ……………</p><p>ç) Hiçbir şey yokken her şey var edildi. → ……………</p>', lines: 0 },
    { q: '<p>Allah’ın <b>Adl</b> ve <b>Rahmân</b> isimlerini bilen bir öğrenci, arkadaşlarına ve çevresindeki canlılara nasıl davranmalıdır? Birer örnek yaz.</p>', lines: 3 },
    { q: '<p>Esmâ-i Hüsnâ ne demektir? Allah’ın güzel isimlerini öğrenmenin bize faydası nedir?</p>', lines: 3 },
    { q: '<p>İhlas suresinin indiği yeri, ayet sayısını ve Kur’an-ı Kerim’deki sırasını yaz.</p>', lines: 2 },
    { q: '<p>“O doğurmamış ve doğmamıştır. Hiçbir şey O’na denk ve benzer değildir.” İhlas suresinin bu ayetlerinden Allah hakkında hangi sonuçlara ulaşırız?</p>', lines: 3 },
    { q: '<p>İhlas suresi ile tevhid inancı arasındaki ilişkiyi açıkla.</p>', lines: 3 },
    { q: '<p><i>(Senaryoya bağlı)</i> Namaz nedir? Günlük beş vakit namazın adlarını yaz ve namazın insana kazandırdıklarından ikisini belirt.</p>', lines: 3 },
  ],
  cevaplar: [
    'Örnek cevap: Hep gündüz olsaydı canlılar dinlenemez, uyuyamazdı. Hep gece olsaydı bitkiler fotosentez yapamaz, büyüyemezdi. Mevsimler olmasaydı tarım yapılamaz, ürünler yetişmezdi.',
    'İkisinde de belli bir ölçü, uyum ve amaç vardır. Arılar az malzemeyle en çok bal depolanacak biçimde petek yapar, su döngüsünde ise su hiç bitmeden sürekli dolaşır. İkisi de gelişigüzel değildir, canlıların yaşamını sürdürmesine hizmet eder.',
    'Saatin düzenli çalışması onu bilgili bir ustanın yaptığını gösterir. Evren ise bir saatten çok daha büyük ve düzenlidir. Bu düzen kendiliğinden oluşamaz; onu yaratan ve yöneten güçlü, bilgili bir yaratıcının, yani Allah’ın varlığını gösterir.',
    'Allah’ın bir ve tek olduğunu (birliğini) vurgular. Örnek: Bir sınıfta aynı anda iki öğretmen farklı şeyler söylese karışıklık çıkar. Evrende böyle bir karışıklık yoktur, çünkü evreni tek olan Allah yönetir.',
    'Tevhid, Allah’ın bir ve tek olduğuna, eşi, benzeri ve ortağı olmadığına inanmaktır. İslam inancının temelidir.',
    'a) Semî‘ (her şeyi işiten). b) Gaffâr (çokça bağışlayan). c) Rezzâk (rızık veren). ç) Hâlık (yaratan).',
    'Adl ismini bilen öğrenci adil olur: Oyunda kurallara uyar, kimseye haksızlık yapmaz, arkadaşlarını ayırmaz. Rahmân ismini bilen öğrenci merhametli olur: Sokak hayvanlarına su ve mama verir, ihtiyacı olan arkadaşına yardım eder.',
    'Esmâ-i Hüsnâ, Allah’ın en güzel isimleri demektir. Bu isimler Allah’ı daha iyi tanımamızı sağlar, O’na bu isimlerle dua ederiz. Ayrıca güzel davranışlar için bize örnek olur (adaletli, merhametli, cömert olmak gibi).',
    'Mekke’de inmiştir, 4 ayettir, Kur’an-ı Kerim’in 112. suresidir.',
    'Allah’ın annesi, babası ya da çocuğu yoktur; başlangıcı yoktur. Hiçbir varlık O’na benzemez, O’nunla eşit değildir. Allah eşsiz ve benzersizdir.',
    'İhlas suresi Allah’ın bir tek olduğunu, hiçbir şeye muhtaç olmadığını, doğmadığını, doğurmadığını ve eşi benzeri olmadığını anlatır. Bunlar tevhid inancının ta kendisidir; bu yüzden İhlas suresi tevhidi en kısa ve açık şekilde anlatan suredir.',
    'Namaz, belirli vakitlerde belirli hareket ve okuyuşlarla Allah’a yapılan ibadettir. Vakitler: sabah, öğle, ikindi, akşam, yatsı. Kazandırdıkları (herhangi ikisi): kalp huzuru ve Allah’a yakınlık, kötülüklerden uzaklaşma, düzenli olma ve zamanı planlama, temizlik alışkanlığı, birlik ve beraberlik.',
  ],
  kontrol: [
    'Evrendeki düzene en az beş örnek verebilirim.',
    'Düzen bozulsaydı neler olacağını açıklayabilirim.',
    'Evrendeki düzenden Allah’ın varlığına nasıl akıl yürütüleceğini anlatabilirim.',
    'Tevhid kavramını açıklayabilir, Enbiyâ 22. ayetin anlamıyla ilişkilendirebilirim.',
    'Esmâ-i Hüsnâ’nın anlamını ve en az on ismin anlamını biliyorum.',
    'Verilen bir duruma uygun güzel ismi seçebilirim.',
    'İhlas suresini okuyabilir ve anlamını söyleyebilirim.',
    'İhlas suresinin indiği yeri, ayet sayısını, sırasını ve mesajlarını biliyorum.',
    'Namazın anlamını, beş vaktini ve kazandırdıklarını özetleyebilirim.',
  ],
};
