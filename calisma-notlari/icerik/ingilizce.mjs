// 5. sınıf İngilizce — 1. Dönem 1. Ortak Yazılı (Unit 1: SCHOOL LIFE)
export default {
  ad: 'İngilizce',
  dosya: 'Ingilizce',
  kapsam: [
    { kod: 'ENG.5.1.R2', metin: 'School Life metinlerine ve görsellerine hızlıca göz atarak (skimming) bilgi bulma' },
    { kod: 'ENG.5.1.R3', metin: 'School Life metinlerini dikkatle okuyup anlamını çıkarma' },
    { kod: 'ENG.5.1.V1', metin: 'Okul, kişiler, mekânlar, kurallar, kulüpler, ülkeler ve millî günlerle ilgili kelimeleri doğru kullanma' },
    { kod: 'ENG.5.1.G1', metin: 'Ünitenin dil yapılarını (am/is/are, Where are you from?, There is/are, emir cümleleri) doğru kullanma' },
    { kod: 'ENG.5.1.W3', metin: 'Verilen örneğe (model) bakarak kısa bir yazı düzenleme' },
    { kod: 'ENG.5.1.W4', metin: 'Konuyla ilgili kendi kısa yazısını oluşturma' },
  ],
  kapsamNot: 'Sınavın kapsamı yalnızca 1. ünite (School Life) ile sınırlıdır. Öğretmenin seçtiği senaryoya göre soru sayıları değişebilir; okuma, kelime, dil yapısı ve kısa yazma sorularına mutlaka hazırlan.',
  icerik: [
    // 1. Tanışma
    { h: 'Hello! Tanışma ve Selamlaşma', no: 1, kod: 'ENG.5.1.V1 · G1' },
    { p: 'Okulun ilk günlerinde yeni arkadaşlarla tanışırız. Kendimizi tanıtırken <b>adımızı</b>, <b>yaşımızı</b>, <b>nereli olduğumuzu</b> ve <b>sınıfımızı</b> söyleriz.' },
    {
      table: {
        head: ['Soru', 'Cevap', 'Türkçesi'],
        rows: [
          ['What\'s your name?', 'My name is Elif. / I\'m Elif.', 'Adın ne? / Benim adım Elif.'],
          ['How old are you?', 'I\'m eleven (years old).', 'Kaç yaşındasın? / On bir yaşındayım.'],
          ['Where are you from?', 'I\'m from Türkiye.', 'Nerelisin? / Türkiye\'denim.'],
          ['What class are you in?', 'I\'m in 5-A.', 'Hangi sınıftasın? / 5-A\'dayım.'],
          ['How are you?', 'I\'m fine, thanks. And you?', 'Nasılsın? / İyiyim, teşekkürler. Ya sen?'],
        ],
      },
    },
    { kelime: [['Hello / Hi', 'Merhaba'], ['Good morning', 'Günaydın'], ['Good afternoon', 'Tünaydın / İyi günler'], ['Nice to meet you.', 'Tanıştığımıza memnun oldum.'], ['Nice to meet you, too.', 'Ben de memnun oldum.'], ['Goodbye / Bye', 'Hoşça kal'], ['See you later.', 'Sonra görüşürüz.'], ['Welcome!', 'Hoş geldin!'], ['This is my friend, Can.', 'Bu benim arkadaşım Can.']] },
    { box: 'ornek', html: '<p><i>Ali:</i> Hi! I\'m Ali. What\'s your name?<br><i>Mia:</i> Hello, Ali. I\'m Mia. Nice to meet you.<br><i>Ali:</i> Nice to meet you, too. Where are you from, Mia?<br><i>Mia:</i> I\'m from England. I\'m English.</p>' },

    // 2. to be
    { h: 'Verb "to be": am / is / are', no: 2, kod: 'ENG.5.1.G1' },
    { p: '<b>am / is / are</b> Türkçedeki "-im, -sin, -dir" eklerinin görevini yapar. Kişiye göre değişir.' },
    {
      cols: [
        [{
          table: {
            head: ['Kişi', 'Olumlu (+)', 'Kısa hâli'],
            rows: [
              ['I', 'I am a student.', 'I\'m'],
              ['You', 'You are my friend.', 'You\'re'],
              ['He / She / It', 'She is a teacher.', 'She\'s'],
              ['We', 'We are in 5-B.', 'We\'re'],
              ['They', 'They are from Spain.', 'They\'re'],
            ],
          },
        }],
        [
          { h2: 'Olumsuz (−)' },
          { p: 'am/is/are + <b>not</b><br>I\'m <b>not</b> late.<br>He <b>isn\'t</b> (is not) in the gym.<br>They <b>aren\'t</b> (are not) Italian.' },
          { h2: 'Soru (?)' },
          { p: '<b>Is</b> she your teacher? — Yes, she <b>is</b>. / No, she <b>isn\'t</b>.<br><b>Are</b> you from Japan? — Yes, I <b>am</b>. / No, I\'m <b>not</b>.' },
        ],
      ],
    },
    { box: 'dikkat', html: '<p>Kısa cevapta <b>olumlu</b> kısaltma yapılmaz: "Yes, I am." doğru, <s>"Yes, I\'m."</s> yanlıştır.</p>' },

    // 3. People
    { h: 'People at School: Okuldaki Kişiler', no: 3, kod: 'ENG.5.1.V1' },
    { kelime: [['teacher', 'öğretmen'], ['student', 'öğrenci'], ['classmate', 'sınıf arkadaşı'], ['principal', 'okul müdürü'], ['vice principal', 'müdür yardımcısı'], ['school nurse', 'okul hemşiresi'], ['school counselor', 'rehber öğretmen'], ['janitor / caretaker', 'okul görevlisi'], ['cook', 'aşçı'], ['librarian', 'kütüphane görevlisi'], ['bus driver', 'servis şoförü'], ['security guard', 'güvenlik görevlisi']] },
    { box: 'ornek', html: '<p>Mr. Demir is our English teacher. Ms. Kaya is the principal. The school nurse is in the nurse\'s room.</p><p><b>Mr.</b> = Bay (erkek), <b>Ms./Mrs.</b> = Bayan (kadın). Unvandan sonra <b>soyadı</b> gelir.</p>' },

    // 4. Places
    { h: 'Places at School: Okuldaki Yerler', no: 4, kod: 'ENG.5.1.V1 · G1' },
    { kelime: [['classroom', 'sınıf'], ['library', 'kütüphane'], ['canteen', 'kantin'], ['dining hall', 'yemekhane'], ['gym', 'spor salonu'], ['science lab', 'fen laboratuvarı'], ['computer lab', 'bilgisayar sınıfı'], ['art room', 'resim atölyesi'], ['music room', 'müzik sınıfı'], ['schoolyard', 'okul bahçesi'], ['teachers\' room', 'öğretmenler odası'], ['principal\'s office', 'müdür odası'], ['nurse\'s room', 'revir'], ['corridor', 'koridor'], ['toilet / restroom', 'tuvalet']] },
    { h2: 'Ne yaparız? Nerede yaparız?' },
    {
      table: {
        head: ['Place', 'What do we do there?'],
        rows: [
          ['library', 'We read books.'],
          ['gym', 'We do sports. / We play basketball.'],
          ['canteen', 'We buy snacks and drinks.'],
          ['science lab', 'We do experiments.'],
          ['art room', 'We draw and paint pictures.'],
          ['music room', 'We sing songs and play instruments.'],
          ['schoolyard', 'We play games in the break.'],
        ],
      },
    },
    { h2: 'There is / There are (… var)' },
    { p: 'Okulda bir yerin olduğunu söylerken kullanırız.<br><b>There is</b> + tekil: There <b>is</b> a library in my school.<br><b>There are</b> + çoğul: There <b>are</b> twenty classrooms in my school.<br>Olumsuz: There <b>isn\'t</b> a swimming pool. / There <b>aren\'t</b> any computers.<br>Soru: <b>Is there</b> a gym? — Yes, there is. / No, there isn\'t.' },

    // 5. Rules
    { h: 'School Rules: Okul Kuralları', no: 5, kod: 'ENG.5.1.V1 · G1' },
    { p: 'Kuralları söylerken <b>emir cümlesi (imperative)</b> kullanırız. Cümle doğrudan <b>fiille</b> başlar, özne yazılmaz.' },
    {
      cols: [
        [
          { h2: '✔ Yapılması gerekenler' },
          { ul: ['<b>Raise</b> your hand. (Parmak kaldır.)', '<b>Listen</b> to your teacher. (Öğretmenini dinle.)', '<b>Be</b> on time. (Zamanında gel.)', '<b>Be</b> quiet in the library. (Kütüphanede sessiz ol.)', '<b>Keep</b> your classroom clean. (Sınıfını temiz tut.)', '<b>Wear</b> your school uniform. (Okul formanı giy.)', '<b>Respect</b> your friends. (Arkadaşlarına saygı göster.)'] },
        ],
        [
          { h2: '✘ Yapılmaması gerekenler' },
          { ul: ['<b>Don\'t run</b> in the corridors. (Koridorlarda koşma.)', '<b>Don\'t eat</b> in the classroom. (Sınıfta yemek yeme.)', '<b>Don\'t be</b> late. (Geç kalma.)', '<b>Don\'t shout</b>. (Bağırma.)', '<b>Don\'t use</b> your phone in class. (Derste telefon kullanma.)', '<b>Don\'t throw</b> rubbish on the floor. (Yere çöp atma.)', '<b>Don\'t write</b> on the desks. (Sıralara yazı yazma.)'] },
        ],
      ],
    },
    { box: 'ipucu', html: '<p>Kibar olmak için <b>please</b> ekle: "Please be quiet." / "Close the door, please." Olumsuz kural = <b>Don\'t</b> (Do not) + fiil.</p>' },

    // 6. Clubs
    { h: 'School Clubs: Okul Kulüpleri', no: 6, kod: 'ENG.5.1.V1 · G1' },
    { kelime: [['chess club', 'satranç kulübü'], ['drama club', 'tiyatro (drama) kulübü'], ['robotics club', 'robotik kulübü'], ['sports club', 'spor kulübü'], ['art club', 'resim kulübü'], ['music club', 'müzik kulübü'], ['science club', 'bilim kulübü'], ['nature club', 'doğa kulübü'], ['reading club', 'kitap okuma kulübü']] },
    {
      table: {
        head: ['Kalıp', 'Örnek'],
        rows: [
          ['I\'m in the … club.', 'I\'m in the chess club.'],
          ['I like / love + fiil-ing', 'I love acting. / I like playing chess.'],
          ['I don\'t like + fiil-ing', 'I don\'t like painting.'],
          ['I can …', 'I can play the guitar. / I can\'t swim.'],
          ['Which club are you in?', 'I\'m in the robotics club.'],
          ['What\'s your favourite club?', 'My favourite club is the drama club.'],
        ],
      },
    },
    { box: 'hatirla', html: '<p>Kulüp ↔ Etkinlik eşleştir: chess → playing chess · drama → acting · robotics → building robots, coding · music → singing, playing instruments · art → drawing, painting · sports → playing football, running.</p>' },

    // 7. Countries
    { h: 'Countries and Nationalities: Ülkeler ve Milliyetler', no: 7, kod: 'ENG.5.1.V1' },
    {
      table: {
        head: ['Country (Ülke)', 'Nationality (Milliyet)', 'Country (Ülke)', 'Nationality (Milliyet)'],
        rows: [
          ['Türkiye', 'Turkish', 'Japan', 'Japanese'],
          ['England', 'English', 'China', 'Chinese'],
          ['Germany', 'German', 'the USA', 'American'],
          ['Italy', 'Italian', 'Russia', 'Russian'],
          ['Spain', 'Spanish', 'Azerbaijan', 'Azerbaijani'],
          ['France', 'French', 'Greece', 'Greek'],
        ],
      },
    },
    { box: 'ornek', html: '<p><b>Where</b> are you <b>from</b>? — I\'m from Italy. I\'m Italian.<br><b>Where</b> is Hans <b>from</b>? — He\'s from Germany. He\'s German.<br><b>Where</b> are they from? — They\'re from Japan. They\'re Japanese.</p>' },
    { box: 'dikkat', html: '<p>Ülke ve milliyet isimleri her zaman <b>büyük harfle</b> başlar: <s>germany</s> → Germany, <s>turkish</s> → Turkish.</p>' },

    // 8. Dates and national days
    { h: 'National Days and Celebrations: Millî Günler', no: 8, kod: 'ENG.5.1.V1 · R3' },
    { h2: 'Months (Aylar)' },
    { kelime: [['January', 'Ocak'], ['February', 'Şubat'], ['March', 'Mart'], ['April', 'Nisan'], ['May', 'Mayıs'], ['June', 'Haziran'], ['July', 'Temmuz'], ['August', 'Ağustos'], ['September', 'Eylül'], ['October', 'Ekim'], ['November', 'Kasım'], ['December', 'Aralık']] },
    { h2: 'Ordinal numbers (Sıra sayıları)' },
    { p: '1st first · 2nd second · 3rd third · 4th fourth · 5th fifth · 10th tenth · 15th fifteenth · 19th nineteenth · 20th twentieth · 21st twenty-first · 23rd twenty-third · 29th twenty-ninth · 30th thirtieth' },
    {
      table: {
        head: ['Date', 'National Day', 'Millî Gün'],
        rows: [
          ['23rd April', 'National Sovereignty and Children\'s Day', 'Ulusal Egemenlik ve Çocuk Bayramı'],
          ['19th May', 'Commemoration of Atatürk, Youth and Sports Day', 'Atatürk\'ü Anma, Gençlik ve Spor Bayramı'],
          ['15th July', 'Democracy and National Unity Day', 'Demokrasi ve Millî Birlik Günü'],
          ['30th August', 'Victory Day', 'Zafer Bayramı'],
          ['29th October', 'Republic Day', 'Cumhuriyet Bayramı'],
        ],
      },
    },
    { box: 'ornek', html: '<p><b>When</b> is Republic Day? — It\'s <b>on</b> 29th October. (It\'s on the twenty-ninth of October.)<br><b>What</b> do you do on Children\'s Day? — We sing songs, dance and wear our costumes. We watch a show at school.</p>' },
    { kelime: [['flag', 'bayrak'], ['celebrate', 'kutlamak'], ['ceremony', 'tören'], ['parade', 'geçit töreni'], ['poem', 'şiir'], ['national anthem', 'İstiklal Marşı'], ['costume', 'kostüm'], ['fireworks', 'havai fişek'], ['festival', 'şenlik']] },
    { box: 'ipucu', html: '<p>Tarihten önce <b>on</b> kullanılır: on 23rd April. Sadece aydan önce <b>in</b> kullanılır: in April.</p>' },

    // 9. Reading
    { h: 'Reading: Okuma Stratejileri', no: 9, kod: 'ENG.5.1.R2 · R3' },
    {
      cols: [
        [{ box: 'ipucu', title: 'SKIMMING (Göz gezdirme)', html: '<p>Metne hızlıca bak. Başlığa, resimlere ve ilk cümlelere odaklan. Amaç: "Metin <b>genel olarak</b> ne hakkında?" sorusunu cevaplamak.</p>' }],
        [{ box: 'ipucu', title: 'SCANNING / CAREFUL READING', html: '<p>Bir bilgiyi (isim, ülke, tarih, kulüp) aramak için metni tara. Sonra soruyu dikkatle oku ve cevabı metinde <b>altını çizerek</b> bul.</p>' }],
      ],
    },
    { h2: 'Örnek metin: Welcome to My School!' },
    { box: 'bilgi', title: 'READING TEXT', html: '<p>Hi! My name is Defne. I\'m eleven years old and I\'m from Türkiye. I\'m in 5-C at Atatürk Secondary School. My school is big and nice. There are twenty-four classrooms, a library, a science lab and a big gym. There isn\'t a swimming pool.</p><p>Our English teacher is Ms. Yıldız. She is very kind. Our principal is Mr. Arslan. My best friend is Lucas. He is from France, so he is French. He is in the robotics club. I am in the drama club because I love acting.</p><p>Our school rules are simple: Be on time. Listen to your teacher. Don\'t run in the corridors. Don\'t eat in the library.</p><p>My favourite day at school is 29th October. It\'s Republic Day. We sing the national anthem, read poems and wave our flags.</p>' },
    {
      table: {
        head: ['Soru', 'Cevap (metinden)'],
        rows: [
          ['Where is Defne from?', 'She is from Türkiye.'],
          ['Is there a swimming pool?', 'No, there isn\'t.'],
          ['Who is Lucas?', 'Defne\'s best friend. He is French.'],
          ['Which club is Defne in? Why?', 'The drama club, because she loves acting.'],
        ],
      },
    },

    // 10. Writing
    { h: 'Writing: Kısa Yazı Yazma', no: 10, kod: 'ENG.5.1.W3 · W4' },
    { p: 'Yazılıda genellikle bir <b>model metin</b> verilir ve senden benzerini <b>kendi bilgilerinle</b> yazman istenir. Şu sırayı izle:' },
    { ol: ['<b>Kendini tanıt:</b> ad, yaş, ülke, sınıf.', '<b>Okulunu anlat:</b> okulun adı, There is / There are ile yerler.', '<b>Kişiler:</b> öğretmenin, müdürün, arkadaşın.', '<b>Kulübün:</b> I\'m in the … club. I like …ing.', '<b>Kurallar:</b> 2 olumlu, 1–2 olumsuz kural.', '<b>Bitiriş:</b> I love my school!'] },
    { box: 'ornek', title: 'MODEL PARAGRAPH: MY SCHOOL', html: '<p>Hello! I\'m Kerem. I\'m ten years old. I\'m from Türkiye. I\'m in 5-A at Cumhuriyet Secondary School. There are eighteen classrooms in my school. There is a computer lab and a big schoolyard. My Maths teacher is Mr. Aydın. He is funny. I\'m in the chess club because I like playing chess. Our rules are: Raise your hand. Don\'t shout in the classroom. I love my school!</p>' },
    { box: 'dikkat', html: '<ul><li>Cümleye <b>büyük harfle</b> başla, <b>nokta</b> ile bitir.</li><li>"I" her zaman büyük yazılır.</li><li>am / is / are\'yi doğru kişiyle kullan: I <b>am</b>, he <b>is</b>, they <b>are</b>.</li><li>Kısa ama tam cümleler yaz; 5–7 cümle yeterlidir.</li></ul>' },
  ],

  sorular: [
    { q: '<p><b>Read the text in section 9 (Welcome to My School!) quickly.</b> What is the text about? Choose and circle.<br>a) A holiday in France &nbsp; b) Defne\'s school &nbsp; c) A football match</p>', lines: 1 },
    { q: '<p><b>Read the text again and answer the questions.</b></p><p>a) How old is Defne?<br>b) What is the name of her English teacher?<br>c) Which club is Lucas in?<br>d) When is Republic Day?</p>', lines: 4 },
    { q: '<p><b>Read and write True (T) or False (F).</b></p><p>a) There are twenty-four classrooms in Defne\'s school. ( &nbsp; )<br>b) There is a swimming pool. ( &nbsp; )<br>c) Lucas is from Germany. ( &nbsp; )<br>d) Defne loves acting. ( &nbsp; )</p>', lines: 0 },
    { q: '<p><b>Match the places with the activities.</b></p><p>1. library &nbsp;&nbsp; 2. gym &nbsp;&nbsp; 3. science lab &nbsp;&nbsp; 4. canteen &nbsp;&nbsp; 5. art room</p><p>a) We do experiments. &nbsp; b) We buy snacks. &nbsp; c) We read books.<br>d) We paint pictures. &nbsp; e) We play basketball.</p>', lines: 1 },
    { q: '<p><b>Complete the table.</b></p><p>Germany – ………… &nbsp;&nbsp; ………… – Japanese &nbsp;&nbsp; Spain – ………… &nbsp;&nbsp; the USA – ………… &nbsp;&nbsp; ………… – Italian &nbsp;&nbsp; Azerbaijan – …………</p>', lines: 1 },
    { q: '<p><b>Fill in the blanks with am, is or are.</b></p><p>a) I ……… in the music club.<br>b) Mr. Demir ……… our principal.<br>c) Emma and Jack ……… from England.<br>d) ……… you a new student?<br>e) The library ……… very quiet.</p>', lines: 0 },
    { q: '<p><b>Put the words in order to make sentences or questions.</b></p><p>a) from / are / where / you / ?<br>b) a / there / gym / is / in my school<br>c) club / I\'m / the / in / robotics</p>', lines: 3 },
    { q: '<p><b>Write the school rules.</b> ✔ = do it, ✘ = don\'t do it. (Use imperatives: Don\'t … / Be … / Raise …)</p><p>a) run – corridors (✘) &nbsp;&nbsp; b) quiet – library (✔) &nbsp;&nbsp; c) raise – hand (✔) &nbsp;&nbsp; d) eat – classroom (✘)</p>', lines: 4 },
    { q: '<p><b>Write the dates of these national days in English.</b></p><p>a) Republic Day: ………………………<br>b) National Sovereignty and Children\'s Day: ………………………<br>c) Victory Day: ………………………</p>', lines: 0 },
    { q: '<p><b>Complete the dialogue.</b></p><p>Aylin: Hi! I\'m Aylin. What\'s your name?<br>Tom: ………………………………………… .<br>Aylin: Nice to meet you, Tom. ………………………………………… ?<br>Tom: I\'m from England. I\'m English.<br>Aylin: Which club are you in?<br>Tom: ………………………………………… . I love playing football.</p>', lines: 0 },
    { q: '<p><b>Write about your favourite school club.</b> Use: <i>I\'m in the … club. I like / love …ing. I can …</i> (3–4 sentences)</p>', lines: 4 },
    { q: '<p><b>Writing: My School.</b> Look at the model paragraph in section 10. Write 5–7 sentences about <u>you and your school</u>. Write your name, age, country, class, places at your school, your club and two school rules.</p>', lines: 8 },
  ],

  cevaplar: [
    'b) Defne\'s school.',
    'a) She is eleven (years old). b) Ms. Yıldız. c) He is in the robotics club. d) It\'s on 29th October.',
    'a) T &nbsp; b) F (There isn\'t a swimming pool.) &nbsp; c) F (He is from France.) &nbsp; d) T',
    '1-c, 2-e, 3-a, 4-b, 5-d',
    'German · Japan · Spanish · American · Italy · Azerbaijani',
    'a) am &nbsp; b) is &nbsp; c) are &nbsp; d) Are &nbsp; e) is',
    'a) Where are you from? &nbsp; b) There is a gym in my school. &nbsp; c) I\'m in the robotics club.',
    'a) Don\'t run in the corridor(s). b) Be quiet in the library. c) Raise your hand (before you speak). d) Don\'t eat in the classroom.',
    'a) 29th October (the twenty-ninth of October) b) 23rd April c) 30th August',
    'Örnek: "My name is Tom. / I\'m Tom." — "Where are you from?" — "I\'m in the sports club."',
    'Örnek: I\'m in the music club. I love singing. I can play the guitar. I like my music teacher. (Kendi kulübünü yazabilirsin; am/is/are ve -ing kullanımına dikkat et.)',
    'Model paragraftaki sırayı izleyen her doğru yazı kabul edilir. Kontrol et: ad–yaş–ülke–sınıf ✔, There is/are ✔, kulüp ✔, 2 kural ✔, büyük harf ve nokta ✔.',
  ],

  kontrol: [
    'Kendimi İngilizce tanıtabilirim (ad, yaş, ülke, sınıf).',
    'am / is / are\'yi doğru kişiyle kullanabilirim; olumsuz ve soru yapabilirim.',
    'Okuldaki kişilerin ve yerlerin İngilizcesini bilirim.',
    'There is / There are ile okulumu anlatabilirim.',
    'Emir cümleleriyle okul kurallarını (Be… / Don\'t…) yazabilirim.',
    'Okul kulüplerini ve sevdiğim etkinlikleri (I like …ing) söyleyebilirim.',
    'Ülkeleri ve milliyetleri eşleştirip doğru yazabilirim.',
    'Ayları, sıra sayılarını ve millî günlerin tarihlerini söyleyebilirim.',
    'Bir metne göz gezdirip konusunu, dikkatle okuyup ayrıntıları bulabilirim.',
    'Model bir metne bakarak kendi kısa paragrafımı yazabilirim.',
  ],
};
