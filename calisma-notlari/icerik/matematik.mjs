// 5. sınıf Matematik — 1. dönem 1. ortak yazılı (Geometrik Şekiller ünitesi)

const INK = '#555';
const RED = '#e5533d';
const BLUE = '#3c7fd9';
const GREEN = '#2f9e6b';
const F = `font-family="Nunito, sans-serif" font-weight="700"`;
const rad = d => (d * Math.PI) / 180;
const pt = (cx, cy, r, deg) => [+(cx + r * Math.cos(rad(deg))).toFixed(1), +(cy - r * Math.sin(rad(deg))).toFixed(1)];
const arrowDefs = `<defs><marker id="ok" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M0 0 L10 5 L0 10z" fill="${INK}"/></marker></defs>`;
const dot = (x, y, c = INK) => `<circle cx="${x}" cy="${y}" r="3.2" fill="${c}"/>`;
const txt = (x, y, s, c = INK, size = 13, anchor = 'middle') => `<text x="${x}" y="${y}" ${F} font-size="${size}" fill="${c}" text-anchor="${anchor}">${s}</text>`;
const line = (x1, y1, x2, y2, c = INK, w = 2.2, extra = '') => `<line x1="${x1}" y1="${y1}" x2="${x2}" y2="${y2}" stroke="${c}" stroke-width="${w}" stroke-linecap="round" ${extra}/>`;
// Açı yayı: köşe (cx,cy), yarıçap r, a1'den a2'ye (derece, saat yönünün tersine)
const arc = (cx, cy, r, a1, a2, c = RED) => {
  const [x1, y1] = pt(cx, cy, r, a1);
  const [x2, y2] = pt(cx, cy, r, a2);
  return `<path d="M${x1} ${y1} A${r} ${r} 0 ${a2 - a1 > 180 ? 1 : 0} 0 ${x2} ${y2}" fill="none" stroke="${c}" stroke-width="2"/>`;
};
const ray = (cx, cy, L, deg, c = INK) => {
  const [x, y] = pt(cx, cy, L, deg);
  return line(cx, cy, x, y, c);
};
const poly = (cx, cy, r, n, start = 90) => Array.from({ length: n }, (_, i) => pt(cx, cy, r, start + (360 / n) * i).join(',')).join(' ');

// --- Şekiller ---
const svgTemel = `<svg width="480" viewBox="0 0 480 120">${arrowDefs}
  ${dot(40, 55)}${txt(40, 40, 'A')}${txt(40, 100, 'Nokta: A', INK, 12)}
  ${line(100, 55, 200, 55, INK, 2.2, 'marker-start="url(#ok)" marker-end="url(#ok)"')}${dot(125, 55)}${dot(175, 55)}${txt(125, 40, 'B')}${txt(175, 40, 'C')}${txt(150, 100, 'Doğru: BC', INK, 12)}
  ${line(230, 55, 330, 55)}${dot(230, 55)}${dot(330, 55)}${txt(230, 40, 'D')}${txt(330, 40, 'E')}${txt(280, 100, 'Doğru parçası: [DE]', INK, 12)}
  ${line(370, 55, 465, 55, INK, 2.2, 'marker-end="url(#ok)"')}${dot(370, 55)}${dot(420, 55)}${txt(370, 40, 'K')}${txt(420, 40, 'L')}${txt(418, 100, 'Işın: [KL', INK, 12)}
</svg>`;

const svgDogrular = `<svg width="480" viewBox="0 0 480 140">${arrowDefs}
  ${line(20, 110, 140, 20, BLUE, 2.2, 'marker-start="url(#ok)" marker-end="url(#ok)"')}${line(20, 30, 140, 110, RED, 2.2, 'marker-start="url(#ok)" marker-end="url(#ok)"')}${txt(80, 134, 'Kesişen doğrular', INK, 12)}
  ${line(180, 45, 300, 45, BLUE, 2.2, 'marker-start="url(#ok)" marker-end="url(#ok)"')}${line(180, 95, 300, 95, RED, 2.2, 'marker-start="url(#ok)" marker-end="url(#ok)"')}${txt(240, 134, 'Paralel doğrular', INK, 12)}
  ${line(340, 70, 470, 70, BLUE, 2.2, 'marker-start="url(#ok)" marker-end="url(#ok)"')}${line(405, 10, 405, 120, RED, 2.2, 'marker-start="url(#ok)" marker-end="url(#ok)"')}
  <path d="M405 58 H417 V70" fill="none" stroke="${INK}" stroke-width="1.6"/>${txt(405, 134, 'Dik doğrular', INK, 12)}
</svg>`;

const svgAciElem = `<svg width="250" viewBox="0 0 300 170">
  ${ray(60, 140, 200, 0)}${ray(60, 140, 170, 50)}${arc(60, 140, 40, 0, 50)}
  ${dot(60, 140)}${txt(48, 158, 'O')}${dot(220, 140)}${txt(220, 160, 'B')}${dot(...pt(60, 140, 150, 50))}${txt(...pt(60, 140, 150, 50).map((v, i) => (i ? v - 8 : v - 14)), 'A')}
  ${txt(125, 128, 'kol', BLUE, 12)}${txt(95, 70, 'kol', BLUE, 12)}${txt(60, 108, 'köşe', RED, 11, 'end')}
  ${txt(150, 22, 'AÔB açısı (BÔA da denir)', INK, 12)}
</svg>`;

function iletki(angle) {
  const cx = 170, cy = 150, R = 120;
  let s = `<path d="M${cx - R} ${cy} A${R} ${R} 0 0 1 ${cx + R} ${cy} Z" fill="#fff8e6" stroke="#c9a640" stroke-width="2"/>`;
  for (let d = 0; d <= 180; d += 10) {
    const [x1, y1] = pt(cx, cy, R, d);
    const [x2, y2] = pt(cx, cy, d % 30 ? R - 7 : R - 13, d);
    s += line(x1, y1, x2, y2, '#c9a640', 1.4);
    if (d % 30 === 0) {
      const [lx, ly] = pt(cx, cy, R - 24, d);
      s += txt(lx, ly + 4, d, '#a07f1f', 10);
    }
  }
  s += ray(cx, cy, R + 25, 0, BLUE) + ray(cx, cy, R + 25, angle, RED) + arc(cx, cy, 30, 0, angle, RED) + dot(cx, cy);
  s += txt(cx, cy + 18, 'merkez noktası (köşe buraya)', INK, 11);
  return `<svg width="290" viewBox="0 0 340 175">${s}</svg>`;
}

function aciPanel(x, deg, name) {
  const cx = x + 20, cy = 95;
  const kol2 = deg === 180 ? ray(cx + 50, cy, 50, 180) + ray(cx + 50, cy, 50, 0) : ray(cx, cy, 90, 0) + ray(cx, cy, deg > 90 ? 60 : 80, deg);
  const vx = deg === 180 ? cx + 50 : cx;
  const ark = deg === 90 ? `<path d="M${cx + 14} ${cy} V${cy - 14} H${cx}" fill="none" stroke="${RED}" stroke-width="2"/>` : arc(vx, cy, 18, 0, deg);
  return kol2 + ark + dot(vx, cy) + txt(x + 55, 128, name, INK, 12) + txt(x + 55, 145, deg === 180 ? '180°' : deg === 90 ? '90°' : deg < 90 ? '0° ile 90° arası' : '90° ile 180° arası', RED, 10.5);
}
const svgAciTur = `<svg width="490" viewBox="0 0 490 150">${aciPanel(0, 45, 'Dar açı')}${aciPanel(125, 90, 'Dik açı')}${aciPanel(245, 130, 'Geniş açı')}${aciPanel(370, 180, 'Doğru açı')}</svg>`;

function kesisen(deg, labels, cx = 150, cy = 90, L = 125) {
  const [a, b] = [pt(cx, cy, L, 0), pt(cx, cy, L, 180)];
  const [c, d] = [pt(cx, cy, L, deg), pt(cx, cy, L, deg + 180)];
  let s = line(...a, ...b, BLUE) + line(...c, ...d, RED) + dot(cx, cy);
  const mids = [deg / 2, (deg + 180) / 2, 180 + deg / 2, (deg + 360 + 180) / 2 - 0];
  const angs = [deg / 2, deg + (180 - deg) / 2, 180 + deg / 2, 180 + deg + (180 - deg) / 2];
  angs.forEach((m, i) => { const [x, y] = pt(cx, cy, 38, m); s += txt(x, y + 5, labels[i], INK, 13); });
  void mids;
  return s;
}
const svgTers = `<svg width="260" viewBox="0 0 300 180">${kesisen(40, ['a', 'b', 'c', 'd'])}</svg>`;

const svgCokgen = `<svg width="490" viewBox="0 0 490 150">
  <g fill="#e8f1fc" stroke="${BLUE}" stroke-width="2.2">
    <polygon points="${poly(40, 50, 32, 3)}"/><polygon points="95,22 150,22 150,77 95,77"/><polygon points="${poly(205, 52, 32, 5)}"/><polygon points="${poly(270, 52, 32, 6)}"/>
  </g>
  ${txt(150, 105, '✔ Çokgen: kapalı, kenarları doğru parçası, kenarlar kesişmiyor', GREEN, 11)}
  <g fill="#fdecea" stroke="${RED}" stroke-width="2.2">
    <circle cx="350" cy="50" r="28"/><path d="M395 75 L410 25 L445 25 L460 75" fill="none"/>
  </g>
  ${txt(410, 105, '✘ Çokgen değil', RED, 11)}${txt(350, 135, 'eğri kenar', RED, 10)}${txt(428, 135, 'kapalı değil', RED, 10)}
</svg>`;

const svgCember = `<svg width="210" viewBox="0 0 240 160">
  <circle cx="110" cy="80" r="62" fill="#f3f8ff" stroke="${BLUE}" stroke-width="2.4"/>
  ${line(110, 80, 172, 80, RED)}${line(...pt(110, 80, 62, 130), ...pt(110, 80, 62, 310), GREEN, 2, 'stroke-dasharray="5 4"')}
  ${dot(110, 80)}${txt(100, 96, 'O', INK, 13)}${txt(142, 74, 'r', RED, 13)}${txt(205, 84, 'yarıçap', RED, 11)}${txt(48, 34, 'çap', GREEN, 11)}${txt(110, 156, 'O: merkez', INK, 11)}
</svg>`;

function insa(rA, rB, d, x0 = 70, y0 = 135, label) {
  const A = [x0, y0], B = [x0 + d, y0];
  const ax = (rA * rA - rB * rB + d * d) / (2 * d);
  const h = Math.sqrt(rA * rA - ax * ax);
  const C = [+(x0 + ax).toFixed(1), +(y0 - h).toFixed(1)];
  return `<circle cx="${A[0]}" cy="${A[1]}" r="${rA}" fill="none" stroke="${BLUE}" stroke-width="1.4" stroke-dasharray="4 3"/>
    <circle cx="${B[0]}" cy="${B[1]}" r="${rB}" fill="none" stroke="${GREEN}" stroke-width="1.4" stroke-dasharray="4 3"/>
    <polygon points="${A.join(',')} ${B.join(',')} ${C.join(',')}" fill="rgba(229,83,61,.08)" stroke="${RED}" stroke-width="2.4"/>
    ${dot(...A)}${dot(...B)}${dot(...C, RED)}${txt(A[0] - 8, A[1] + 16, 'A')}${txt(B[0] + 8, B[1] + 16, 'B')}${txt(C[0], C[1] - 8, 'C', RED)}
    ${txt(x0 + d / 2, y0 + 102, label, INK, 12)}`;
}
const svgInsa = `<svg width="400" viewBox="0 0 520 240">
  <g transform="translate(10,10)">${insa(80, 80, 80, 80, 120, 'Yarıçaplar = |AB| → eşkenar üçgen')}</g>
  <g transform="translate(260,10)">${insa(85, 60, 100, 80, 120, 'Yarıçaplar farklı → çeşitkenar')}</g>
</svg>`;

// --- Soru şekilleri ---
const svgSoruAci = `<svg width="180" viewBox="0 0 240 150">${ray(30, 130, 190, 0)}${ray(30, 130, 150, 65)}${arc(30, 130, 28, 0, 65)}${dot(30, 130)}${txt(20, 146, 'K')}${txt(215, 146, 'L')}${txt(...pt(30, 130, 150, 65).map((v, i) => (i ? v + 4 : v - 12)), 'M')}</svg>`;
const svgSoruTers = `<svg width="220" viewBox="0 0 300 180">${kesisen(35, ['35°', 'x', 'y', 'z'])}</svg>`;
const svgSoruUc = (() => {
  const cx = 160, cy = 120;
  let s = line(30, cy, 290, cy, BLUE) + ray(cx, cy, 110, 50, RED) + ray(cx, cy, 110, 120, GREEN) + dot(cx, cy);
  s += arc(cx, cy, 30, 0, 50) + arc(cx, cy, 38, 50, 120, GREEN) + arc(cx, cy, 30, 120, 180, BLUE);
  s += txt(...pt(cx, cy, 52, 25), '50°', RED, 12) + txt(...pt(cx, cy, 58, 85), '70°', GREEN, 12) + txt(...pt(cx, cy, 52, 150), 'x', BLUE, 14);
  return `<svg width="240" viewBox="0 0 320 140">${s}</svg>`;
})();
const svgSoruSekil = `<svg width="380" viewBox="0 0 460 110">
  <g fill="none" stroke="${INK}" stroke-width="2.2">
    <polygon points="${poly(45, 50, 34, 5)}"/>
    <path d="M100 85 L130 20 L160 85"/>
    <path d="M190 85 L190 25 L250 25 L250 85 Z"/>
    <path d="M280 85 Q300 15 330 40 L340 85 Z"/>
    <polygon points="${poly(405, 50, 34, 3, 90)}"/>
  </g>
  ${txt(45, 104, '1')}${txt(130, 104, '2')}${txt(220, 104, '3')}${txt(310, 104, '4')}${txt(405, 104, '5')}
</svg>`;

export default {
  ad: 'Matematik',
  dosya: 'Matematik',
  kapsam: [
    { kod: 'MAT.5.3.1', metin: 'Temel geometrik çizimler için matematiksel araç ve teknolojiden (cetvel, gönye, pergel, dijital araçlar) yararlanabilme' },
    { kod: 'MAT.5.3.2', metin: 'Temel geometrik çizimlere dayalı deneyimlerini yansıtabilme' },
    { kod: 'MAT.5.3.3', metin: 'Açıları ölçmek için matematiksel araç ve teknolojiden (iletki) yararlanabilme' },
    { kod: 'MAT.5.3.4', metin: 'Düzlemde iki veya üç doğrunun birbirine göre durumuna bağlı olarak oluşabilecek açılara dair çıkarım yapabilme' },
    { kod: 'MAT.5.3.5', metin: 'Çokgenleri düzlemde ardışık olarak kesişen doğruların oluşturduğu kapalı şekiller olarak yorumlayabilme' },
    { kod: 'MAT.5.3.6', metin: 'Çokgenlerin özellikleri ile ilgili edindiği deneyimleri yansıtabilme' },
    { kod: 'MAT.5.3.7', metin: 'Düzlemde iki noktada kesişen çember çiftinin merkezleri ve kesişim noktalarından biri ile inşa edilen üçgenlerin kenar özelliklerine yönelik çıkarım yapabilme' },
  ],
  kapsamNot: 'Ünite: Geometrik Şekiller. MEB bu yazılı için 5 farklı senaryo yayımladı; okulunuzdaki matematik zümresi bunlardan birini seçer. Sınav genellikle 7 civarında açık uçlu sorudan oluşur. Hangi senaryonun seçildiğini öğretmeninize sorabilirsiniz.',
  icerik: [
    { h: 'Temel Geometrik Kavramlar', no: 1, kod: 'MAT.5.3.1 · 5.3.2' },
    { p: 'Geometrinin “yapı taşları” nokta, doğru, doğru parçası, ışın ve düzlemdir. Etrafımızdaki her şekil bunlardan oluşur.' },
    { svg: svgTemel, caption: 'Nokta, doğru, doğru parçası ve ışın' },
    { table: { head: ['Kavram', 'Ne demek?', 'Gösterimi / Günlük hayattan örnek'], rows: [
      ['<b>Nokta</b>', 'Boyutu olmayan, yer belirten iz. Büyük harfle adlandırılır.', 'A noktası · haritada bir şehrin yeri'],
      ['<b>Doğru</b>', 'İki yönde sonsuza kadar uzanır; başı ve sonu yoktur.', 'AB doğrusu · (iki ucu oklu çizilir)'],
      ['<b>Doğru parçası</b>', 'Bir doğrunun iki nokta arasındaki kısmı; başı ve sonu vardır, uzunluğu ölçülebilir.', '[AB] · cetvelin kenarı, kalem'],
      ['<b>Işın</b>', 'Bir noktada başlar, tek yönde sonsuza uzanır.', '[AB · el fenerinden çıkan ışık'],
      ['<b>Düzlem</b>', 'Her yöne sonsuza uzanan düz yüzey.', 'masa yüzeyi, sakin göl yüzeyi (modeli)'],
    ] } },
    { box: 'dikkat', html: '<p>Doğru ve ışının uzunluğu <b>ölçülemez</b> çünkü sonsuza uzanırlar. Yalnızca <b>doğru parçasının</b> uzunluğu ölçülebilir.</p>' },
    { h2: 'Doğruların birbirine göre durumları' },
    { svg: svgDogrular },
    { ul: [
      '<b>Kesişen doğrular:</b> Düzlemde bir noktada kesişir (ortak noktaları 1 tanedir). Örnek: makasın iki kolu.',
      '<b>Paralel doğrular:</b> Aralarındaki uzaklık her yerde aynıdır, ne kadar uzatılsa da hiç kesişmezler. Gösterimi: d ∥ k. Örnek: tren rayları, defter çizgileri.',
      '<b>Dik doğrular:</b> Kesişen doğruların özel hâlidir; kesiştiklerinde <b>90°</b> (dik açı) oluştururlar. Gösterimi: d ⊥ k. Örnek: pencere çerçevesinin köşesi.',
    ] },
    { h2: 'Cetvel, gönye ve pergelle çizim' },
    { cols: [[
      { p: '<b>Dik doğru çizme (gönye ile)</b>' },
      { ol: ['Cetvelle bir d doğrusu çiz.', 'Gönyenin dik kenarlarından birini d doğrusunun üzerine yerleştir.', 'Gönyenin diğer dik kenarı boyunca çizgi çek.', 'Kesişim noktasına dik açı işaretini (küçük kare) koy.'] },
    ], [
      { p: '<b>Paralel doğru çizme (cetvel + gönye)</b>' },
      { ol: ['Gönyenin bir kenarını d doğrusuna yerleştir, cetveli gönyenin diğer dik kenarına daya.', 'Cetveli sabit tut, gönyeyi cetvel boyunca kaydır.', 'Gönyenin d’ye dayalı olan kenarı boyunca yeni doğruyu çiz.'] },
    ]] },
    { box: 'ipucu', html: '<p><b>Pergel</b> çember çizmek ve bir uzunluğu başka bir yere aynen taşımak için kullanılır. Pergelin açıklığı = çemberin yarıçapı. Dijital geometri yazılımlarında da aynı çizimler “dik doğru”, “paralel doğru”, “çember” araçlarıyla yapılır.</p>' },

    { h: 'Açı ve Açı Ölçme', no: 2, kod: 'MAT.5.3.3' },
    { p: 'Başlangıç noktaları aynı olan iki ışının oluşturduğu şekle <b>açı</b> denir. Işınlara açının <b>kolları</b>, ortak başlangıç noktasına <b>köşe</b> denir. Açılar köşedeki harf ortada olacak şekilde okunur.' },
    { svg: svgAciElem },
    { p: 'Açının ölçüsü <b>derece (°)</b> ile ifade edilir ve <b>iletki</b> (açıölçer) ile ölçülür. Açının ölçüsü kolların uzunluğuna değil, kolların arasındaki <b>açıklığa</b> bağlıdır.' },
    { cols: [[
      { svg: iletki(50), caption: 'Bu açı 50°' },
    ], [
      { p: '<b>İletki ile açı ölçme adımları</b>' },
      { ol: [
        'İletkinin <b>merkez noktasını</b> açının köşesine yerleştir.',
        'İletkinin <b>0 çizgisini</b> açının bir kolu ile çakıştır.',
        'Diğer kolun iletki üzerinde kestiği sayıyı oku.',
        'Kolun 0’dan başladığı ölçeği (iç ya da dış) kullan!',
      ] },
    ]] },
    { box: 'dikkat', html: '<p>İletkide iç içe iki ölçek vardır. Açının bir kolu hangi ölçekte <b>0</b>’ı gösteriyorsa o ölçekten okunur. Yanlış ölçekten okursan dar açıyı geniş açı sanabilirsin (ör. 50° yerine 130°). Önce açının dar mı geniş mi olduğunu gözle tahmin et!</p>' },
    { h2: 'Açı çeşitleri' },
    { svg: svgAciTur },
    { table: { head: ['Açı', 'Ölçüsü', 'Günlük hayattan örnek'], rows: [
      ['Dar açı', '0° ile 90° arasında', 'Saat 1:00’de akrep ve yelkovan'],
      ['Dik açı', 'Tam 90°', 'Kitabın köşesi, kapı ile duvar'],
      ['Geniş açı', '90° ile 180° arasında', 'Saat 4:00’te akrep ve yelkovan, açık dizüstü bilgisayar'],
      ['Doğru açı', 'Tam 180°', 'Saat 6:00’da akrep ve yelkovan'],
    ] } },
    { box: 'ipucu', html: '<p>Bir açının dar, dik ya da geniş olduğunu anlamak için defterinin köşesini (dik açı) karşılaştırma aracı olarak kullanabilirsin.</p>' },

    { h: 'Kesişen Doğruların Oluşturduğu Açılar', no: 3, kod: 'MAT.5.3.4' },
    { p: 'Düzlemde kesişen iki doğru, kesişim noktası etrafında <b>4 açı</b> oluşturur.' },
    { cols: [[
      { svg: svgTers, caption: 'a = 40° ise c = 40°, b = d = 140°' },
    ], [
      { ul: [
        '<b>Komşu açılar:</b> Köşeleri ve birer kolları ortak olan açılar (a ile b gibi). Bir doğru üzerindeki komşu açıların toplamı <b>180°</b>’dir: a + b = 180°.',
        '<b>Ters açılar:</b> Kesişim noktasına göre karşı karşıya duran açılar (a ile c, b ile d). Ters açıların ölçüleri <b>eşittir</b>.',
        'Bir nokta etrafındaki tüm açıların toplamı <b>360°</b>’dir: a + b + c + d = 360°.',
      ] },
    ]] },
    { box: 'hatirla', html: '<p><b>Neden ters açılar eşit?</b> a + b = 180° ve b + c = 180° (ikisi de doğru açı). İkisinde de b ortak olduğuna göre a ile c eşit olmak zorundadır.</p>' },
    { box: 'ornek', html: '<p>Kesişen iki doğrudan biri ile diğeri arasındaki açılardan biri 65° ise:<br>Ters açısı = <b>65°</b>; komşu açısı = 180° − 65° = <b>115°</b>; diğer açı (115°’nin ters açısı) = <b>115°</b>. Kontrol: 65 + 115 + 65 + 115 = 360 ✔</p>' },
    { p: '<b>Dik kesişen doğrular:</b> Doğrular dik kesişirse oluşan 4 açının hepsi 90°’dir.' },
    { p: '<b>Üç doğru bir noktada kesişirse</b> 6 açı oluşur. Yine karşılıklı açılar ters açıdır ve eşittir. Bir doğrunun bir tarafında kalan açıların toplamı 180°’dir.' },

    { h: 'Çokgenler', no: 4, kod: 'MAT.5.3.5 · 5.3.6' },
    { p: 'Düzlemde <b>ardışık olarak kesişen doğru parçalarının</b> oluşturduğu, kenarları birbirini kesmeyen <b>kapalı</b> şekillere <b>çokgen</b> denir. Doğru parçalarına <b>kenar</b>, kenarların birleştiği noktalara <b>köşe</b>, iki kenar arasındaki açılara <b>iç açı</b> denir.' },
    { svg: svgCokgen },
    { table: { head: ['Çokgen', 'Kenar', 'Köşe', 'İç açı', 'Bir köşeden çizilen köşegen'], rows: [
      ['Üçgen', '3', '3', '3', '0'],
      ['Dörtgen', '4', '4', '4', '1'],
      ['Beşgen', '5', '5', '5', '2'],
      ['Altıgen', '6', '6', '6', '3'],
    ] } },
    { box: 'hatirla', html: '<ul><li>Bir çokgende <b>kenar sayısı = köşe sayısı = iç açı sayısı</b>dır.</li><li>En az kenarlı çokgen <b>üçgendir</b> (2 doğru parçası kapalı şekil oluşturamaz).</li><li><b>Köşegen:</b> Komşu olmayan iki köşeyi birleştiren doğru parçasıdır. Üçgenin köşegeni yoktur.</li></ul>' },
    { p: '<b>Düzgün çokgen:</b> Bütün kenar uzunlukları <b>ve</b> bütün iç açılarının ölçüleri eşit olan çokgendir. Örnek: eşkenar üçgen, kare, arı peteğindeki düzgün altıgen. Dikdörtgenin açıları eşittir ama kenarları eşit olmadığı için düzgün çokgen değildir.' },
    { box: 'bilgi', html: '<p>Arılar peteklerini düzgün altıgen şeklinde yapar. Düzgün altıgenler aralarında boşluk kalmadan yan yana dizilebilir; böylece en az balmumuyla en çok bal depolanır.</p>' },

    { h: 'Çember ve Çemberle Üçgen İnşası', no: 5, kod: 'MAT.5.3.7' },
    { cols: [[
      { svg: svgCember },
    ], [
      { ul: [
        '<b>Çember:</b> Düzlemde sabit bir noktaya eşit uzaklıktaki noktaların oluşturduğu kapalı eğri. Pergelle çizilir.',
        '<b>Merkez (O):</b> Çemberin tam ortasındaki sabit nokta.',
        '<b>Yarıçap (r):</b> Merkezi çember üzerindeki bir noktaya birleştiren doğru parçası. Bir çemberin bütün yarıçapları eşittir.',
        '<b>Çap:</b> Merkezden geçen ve çemberin iki noktasını birleştiren doğru parçası; çap = 2 × yarıçap.',
      ] },
      { box: 'dikkat', html: '<p>Çember bir çokgen <b>değildir</b>; kenarları doğru parçası değil, eğridir.</p>' },
    ]] },
    { h2: 'İki çember yardımıyla üçgen inşası' },
    { ol: [
      'Bir [AB] doğru parçası çiz.',
      'Pergelin sivri ucunu A’ya koy ve bir çember çiz.',
      'Pergelin sivri ucunu B’ye koy ve ilk çemberi iki noktada kesecek bir çember çiz.',
      'Kesişim noktalarından birine C de ve A, B, C noktalarını cetvelle birleştir. ABC üçgeni oluştu!',
    ] },
    { svg: svgInsa, caption: 'Kesik çizgiler pergelle çizilen çemberleri gösterir.' },
    { box: 'hatirla', title: 'ÇIKARIM', html: '<p>C noktası <b>A merkezli</b> çemberin üzerinde olduğu için |AC| = A merkezli çemberin yarıçapıdır. C aynı zamanda <b>B merkezli</b> çemberin üzerinde olduğu için |BC| = B merkezli çemberin yarıçapıdır.</p><ul><li>İki yarıçap da |AB|’ye eşitse → üç kenar eşit → <b>eşkenar üçgen</b>.</li><li>İki yarıçap birbirine eşit ama |AB|’den farklıysa → iki kenar eşit → <b>ikizkenar üçgen</b>.</li><li>Yarıçaplar birbirinden ve |AB|’den farklıysa → kenarların hepsi farklı → <b>çeşitkenar üçgen</b>.</li></ul>' },
    { box: 'dikkat', html: '<p>Çemberlerin kesişebilmesi için iki yarıçapın toplamı |AB|’den büyük olmalıdır. Yarıçaplar çok küçük seçilirse çemberler kesişmez ve üçgen oluşmaz.</p>' },
  ],
  sorular: [
    { q: '<p>Aşağıdaki şekillerden hangileri çokgendir? Çokgen olmayanların neden çokgen olmadığını açıklayınız.</p>', svg: svgSoruSekil, lines: 3 },
    { q: '<p>Doğru, ışın ve doğru parçası arasındaki farkları birer günlük hayat örneği vererek açıklayınız. Hangisinin uzunluğu ölçülebilir? Neden?</p>', lines: 3 },
    { q: '<p>Sınıfınızdaki nesnelerden <b>paralel</b>, <b>dik</b> ve <b>kesişen</b> doğrulara birer örnek yazınız.</p>', lines: 2 },
    { q: '<p>Gönye ve cetvel kullanarak bir d doğrusuna paralel bir k doğrusunu nasıl çizeceğinizi adım adım yazınız.</p>', lines: 3 },
    { q: '<p>Aşağıdaki açıyı iletkinizle ölçünüz. Açıyı üç harf kullanarak adlandırınız ve türünü yazınız.</p>', svg: svgSoruAci, lines: 2 },
    { q: '<p>Ece, iletkiyle ölçtüğü bir açının 130° olduğunu söyledi. Oysa açı gözle bakıldığında dar açıdır. Ece nerede hata yapmış olabilir? Açının gerçek ölçüsü kaç derecedir?</p>', lines: 3 },
    { q: '<p>Saat 3:00, 5:00 ve 6:00’da akrep ile yelkovan arasındaki (küçük) açının türlerini yazınız.</p>', lines: 2 },
    { q: '<p>Şekilde kesişen iki doğru verilmiştir. x, y ve z açılarının ölçülerini bulunuz. Ters açılarla ilgili hangi bilgiyi kullandığınızı açıklayınız.</p>', svg: svgSoruTers, lines: 3 },
    { q: '<p>Şekilde üç doğru bir noktada kesişmektedir. Mavi doğru bir doğru olduğuna göre x kaç derecedir? Nasıl bulduğunuzu açıklayınız.</p>', svg: svgSoruUc, lines: 3 },
    { q: '<p>Bir çokgenin 5 köşesi vardır. Bu çokgenin kenar ve iç açı sayısı kaçtır? Bir köşesinden kaç köşegen çizilebilir? Çizerek gösteriniz.</p>', lines: 3 },
    { q: '<p>“Bütün dikdörtgenler düzgün çokgendir.” ifadesine katılıyor musunuz? Nedenini açıklayınız.</p>', lines: 3 },
    { q: '<p>|AB| = 6 cm olan bir doğru parçasının uçlarını merkez kabul eden, yarıçapları 6 cm olan iki çember çiziliyor. Çemberlerin kesişim noktalarından biri C olmak üzere ABC üçgeninin kenar uzunluklarını ve türünü yazınız. Neden böyle olduğunu açıklayınız.</p>', lines: 3 },
  ],
  cevaplar: [
    '1, 3 ve 5 çokgendir (beşgen, dörtgen, üçgen). 2 kapalı değildir (açık şekil). 4’ün bir kenarı eğridir; çokgenin bütün kenarları doğru parçası olmalıdır.',
    'Doğru iki yönde sonsuza uzanır (ör. iki ucu sonsuza giden düz yol modeli); ışın bir noktadan başlayıp tek yönde uzanır (ör. el fenerinin ışığı); doğru parçasının iki ucu vardır (ör. kalem, cetvel kenarı). Yalnızca doğru parçasının uzunluğu ölçülebilir; çünkü başı ve sonu vardır.',
    'Örnek: Paralel: defter çizgileri, tahtanın alt ve üst kenarı. Dik: kapı ile eşik, sıranın köşesindeki iki kenar. Kesişen: makas kolları, X şeklindeki sandalye ayakları. (Uygun her örnek doğrudur.)',
    '1) Gönyenin bir kenarını d doğrusuna yerleştir. 2) Cetveli gönyenin diğer kenarına daya. 3) Cetveli sabit tutup gönyeyi cetvel boyunca kaydır. 4) Gönyenin d’ye dayalı kenarı boyunca k doğrusunu çiz. k ∥ d olur.',
    'Köşe K olduğu için açı <b>LKM</b> (ya da MKL) açısıdır; köşe harfi ortada yazılır. Ölçüsü <b>65°</b>, türü <b>dar açı</b>.',
    'Ece açıyı yanlış ölçekten okumuştur. Açının kolunun 0’dan başladığı ölçeği kullanması gerekirdi. Gerçek ölçü 180° − 130° = <b>50°</b>’dir.',
    '3:00 → 90° dik açı; 5:00 → 150° geniş açı; 6:00 → 180° doğru açı.',
    'x, 35° ile komşu (aynı doğru üzerinde): x = 180° − 35° = <b>145°</b>. y, 35°’nin ters açısıdır: y = <b>35°</b>. z, x’in ters açısıdır: z = <b>145°</b>. Ters açıların ölçüleri eşittir.',
    'Mavi doğru üzerindeki açıların toplamı 180°’dir: 50° + 70° + x = 180° → x = <b>60°</b>.',
    '5 köşeli çokgen beşgendir: 5 kenar, 5 iç açı. Bir köşesinden komşu olmayan 2 köşeye <b>2 köşegen</b> çizilir.',
    'Katılmıyorum. Düzgün çokgenin hem bütün kenarları hem bütün açıları eşit olmalıdır. Dikdörtgenin açıları eşit (90°) ama kenarları genellikle eşit değildir. Yalnızca kare (özel dikdörtgen) düzgündür.',
    '|AC| = 6 cm (A merkezli çemberin yarıçapı), |BC| = 6 cm (B merkezli çemberin yarıçapı), |AB| = 6 cm. Üç kenar eşit olduğu için ABC bir <b>eşkenar üçgendir</b>.',
  ],
  kontrol: [
    'Nokta, doğru, doğru parçası, ışın ve düzlemi açıklayıp gösterebiliyorum.',
    'Paralel, dik ve kesişen doğrulara günlük hayattan örnek verebiliyorum.',
    'Cetvel ve gönye ile dik ve paralel doğru çizebiliyorum.',
    'İletkiyi doğru yerleştirip açıyı doğru ölçekten okuyabiliyorum.',
    'Açıları dar, dik, geniş ve doğru açı olarak sınıflandırabiliyorum.',
    'Kesişen doğrularda ters açıların eşit, komşu açıların toplamının 180° olduğunu kullanabiliyorum.',
    'Bir şeklin çokgen olup olmadığını nedeniyle açıklayabiliyorum.',
    'Çokgenlerin kenar, köşe, açı ve köşegenlerini gösterebiliyorum; düzgün çokgeni tanıyorum.',
    'Çemberin merkezini, yarıçapını ve çapını gösterebiliyorum.',
    'İki çemberle üçgen çizip kenarlarının neden eşit olduğunu açıklayabiliyorum.',
  ],
};
