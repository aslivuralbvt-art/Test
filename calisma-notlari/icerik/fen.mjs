// 5. sınıf Fen Bilimleri – 1. dönem 1. ortak yazılı çalışma notları
// Kapsam: MEB 2026-2027 konu–soru dağılım tablosu (FB.5.1.2, FB.5.1.3, FB.5.1.4, FB.5.2.1)

const LIT = '#ffd23f';
const DARK = '#4b5066';

// Dünya'dan görünen Ay evresi. f: aydınlık oran (0..1), side: 'R' sağ / 'L' sol aydınlık
function phase(cx, cy, r, f, side = 'R') {
  let lit = '';
  if (f >= 0.999) lit = `<circle cx="${cx}" cy="${cy}" r="${r}" fill="${LIT}"/>`;
  else if (f > 0.001) {
    const rx = Math.abs(1 - 2 * f) * r;
    const sweep = f > 0.5 ? 1 : 0;
    const d = `M${cx} ${cy - r} A${r} ${r} 0 0 1 ${cx} ${cy + r} A${rx} ${r} 0 0 ${sweep} ${cx} ${cy - r}Z`;
    const tr = side === 'L' ? ` transform="translate(${2 * cx} 0) scale(-1 1)"` : '';
    lit = `<path d="${d}" fill="${LIT}"${tr}/>`;
  }
  return `<circle cx="${cx}" cy="${cy}" r="${r}" fill="${DARK}"/>${lit}<circle cx="${cx}" cy="${cy}" r="${r}" fill="none" stroke="#2b2f3d" stroke-width="1"/>`;
}

// Uzaydan bakınca Ay: Güneş'e bakan (sağ) yarısı aydınlık
function moonSpace(cx, cy, r) {
  return `<circle cx="${cx}" cy="${cy}" r="${r}" fill="${DARK}"/><path d="M${cx} ${cy - r} A${r} ${r} 0 0 1 ${cx} ${cy + r}Z" fill="${LIT}"/><circle cx="${cx}" cy="${cy}" r="${r}" fill="none" stroke="#2b2f3d" stroke-width="1"/>`;
}

const PHASES = [
  // açı (derece, sağ = 0, yukarı = 90), ad, aydınlık oran, taraf
  [0, 'Yeni Ay', 0, 'R'],
  [45, 'Hilal (büyüyen)', 0.2, 'R'],
  [90, 'İlk Dördün', 0.5, 'R'],
  [135, 'Şişkin Ay (büyüyen)', 0.8, 'R'],
  [180, 'Dolunay', 1, 'R'],
  [225, 'Şişkin Ay (küçülen)', 0.8, 'L'],
  [270, 'Son Dördün', 0.5, 'L'],
  [315, 'Hilal (küçülen)', 0.2, 'L'],
];

function phaseCycle() {
  const ex = 250, ey = 215, ri = 92, ro = 158;
  let s = `<svg width="640" height="430" viewBox="0 0 640 430" xmlns="http://www.w3.org/2000/svg" font-family="Nunito, sans-serif">`;
  // Güneş ışınları
  s += `<circle cx="640" cy="215" r="62" fill="#ffb627"/><text x="604" y="219" font-size="14" font-weight="800" fill="#7a3d00">GÜNEŞ</text>`;
  for (let y = 60; y <= 370; y += 44) s += `<path d="M570 ${y} H500" stroke="#f5a623" stroke-width="2" stroke-dasharray="6 5"/><path d="M506 ${y - 5} L498 ${y} L506 ${y + 5}" fill="none" stroke="#f5a623" stroke-width="2"/>`;
  s += `<text x="500" y="40" font-size="11" fill="#b06b00" font-weight="700">Güneş ışınları</text>`;
  // yörünge
  s += `<circle cx="${ex}" cy="${ey}" r="${ri}" fill="none" stroke="#9aa3b5" stroke-width="1.5" stroke-dasharray="5 4"/>`;
  s += `<path d="M${ex - 62} ${ey - 68} l-4 12 l12 -3" fill="none" stroke="#6b7280" stroke-width="2"/>`;
  s += `<text x="${ex - 120}" y="${ey - 80}" font-size="10.5" fill="#4b5563" font-weight="700">dolanma yönü</text>`;
  // Dünya (Güneş'e bakan yarısı gündüz)
  s += `<circle cx="${ex}" cy="${ey}" r="24" fill="#1d4f91"/><path d="M${ex} ${ey - 24} A24 24 0 0 1 ${ex} ${ey + 24}Z" fill="#4aa3df"/><circle cx="${ex}" cy="${ey}" r="24" fill="none" stroke="#123" stroke-width="1"/>`;
  s += `<text x="${ex}" y="${ey + 4}" font-size="10" text-anchor="middle" fill="#fff" font-weight="800">DÜNYA</text>`;
  for (const [a, name, f, side] of PHASES) {
    const rad = (a * Math.PI) / 180;
    const xi = ex + ri * Math.cos(rad), yi = ey - ri * Math.sin(rad);
    const xo = ex + ro * Math.cos(rad), yo = ey - ro * Math.sin(rad);
    s += `<line x1="${xi}" y1="${yi}" x2="${xo}" y2="${yo}" stroke="#c7cbd6" stroke-width="1" stroke-dasharray="2 3"/>`;
    s += moonSpace(xi, yi, 11);
    s += phase(xo, yo, 15, f, side);
    const ly = Math.sin(rad) > 0.1 ? yo - 21 : yo + 30;
    const lx = a === 180 ? xo - 4 : xo;
    s += `<text x="${lx}" y="${ly}" font-size="11.5" font-weight="800" text-anchor="middle" fill="#333">${name}</text>`;
  }
  s += `<text x="8" y="420" font-size="10.5" fill="#555">İç halka: Ay'ın uzaydan görünüşü (Güneş'e bakan yarısı hep aydınlık) · Dış halka: Ay'ın Dünya'dan (Kuzey Yarım Küre) görünüşü</text>`;
  return s + `</svg>`;
}

function sunEarthMoon() {
  return `<svg width="600" height="230" viewBox="0 0 600 230" xmlns="http://www.w3.org/2000/svg" font-family="Nunito, sans-serif">
  <ellipse cx="190" cy="115" rx="170" ry="90" fill="none" stroke="#9aa3b5" stroke-width="1.5" stroke-dasharray="6 4"/>
  <path d="M296 40 l12 3 l-9 8" fill="none" stroke="#6b7280" stroke-width="2"/>
  <circle cx="190" cy="115" r="38" fill="#ffb627"/><text x="190" y="119" text-anchor="middle" font-size="13" font-weight="800" fill="#7a3d00">GÜNEŞ</text>
  <circle cx="360" cy="115" r="40" fill="none" stroke="#9aa3b5" stroke-width="1.3" stroke-dasharray="4 3"/>
  <path d="M352 76 l-10 -2 l7 -7" fill="none" stroke="#6b7280" stroke-width="2"/>
  <circle cx="360" cy="115" r="15" fill="#3b82c4"/><text x="360" y="150" text-anchor="middle" font-size="11" font-weight="800" fill="#1d4f91">DÜNYA</text>
  <path d="M348 96 A20 20 0 0 1 375 100" fill="none" stroke="#e5533d" stroke-width="1.8"/><path d="M372 94 l4 6 l-7 1" fill="none" stroke="#e5533d" stroke-width="1.8"/>
  <circle cx="400" cy="115" r="6" fill="#9aa0ac"/><text x="414" y="119" font-size="11" font-weight="800" fill="#555">AY</text>
  <g font-size="11" fill="#333" font-weight="700">
    <text x="440" y="40">• Dünya kendi ekseni etrafında</text><text x="452" y="54">döner: ≈ 24 saat (1 gün)</text>
    <text x="440" y="80">• Dünya, Güneş etrafında</text><text x="452" y="94">dolanır: ≈ 365 gün 6 saat (1 yıl)</text>
    <text x="440" y="120">• Ay kendi ekseni etrafında döner</text><text x="452" y="134">ve Dünya etrafında dolanır:</text><text x="452" y="148">ikisi de ≈ 27,3 gün</text>
    <text x="440" y="174">• Ay, Dünya ile birlikte</text><text x="452" y="188">Güneş etrafında da dolanır.</text>
  </g>
  <text x="10" y="222" font-size="10" fill="#666" font-style="italic">Çizim ölçekli değildir. Kırmızı ok: Dünya'nın dönme hareketi; kesikli çizgiler: yörüngeler.</text>
</svg>`;
}

function sizes() {
  return `<svg width="600" height="170" viewBox="0 0 600 170" xmlns="http://www.w3.org/2000/svg" font-family="Nunito, sans-serif">
  <defs><clipPath id="cp"><rect x="0" y="0" width="600" height="150"/></clipPath></defs>
  <circle cx="-1010" cy="75" r="1090" fill="#ffb627" clip-path="url(#cp)"/>
  <text x="20" y="80" font-size="14" font-weight="800" fill="#7a3d00">GÜNEŞ</text>
  <text x="20" y="98" font-size="10" fill="#7a3d00">(çizime sığmadı; sadece kenarı)</text>
  <circle cx="260" cy="75" r="40" fill="#3b82c4"/><text x="260" y="79" text-anchor="middle" font-size="12" font-weight="800" fill="#fff">DÜNYA</text>
  <circle cx="340" cy="75" r="11" fill="#9aa0ac"/><text x="340" y="104" text-anchor="middle" font-size="11" font-weight="800" fill="#555">AY</text>
  <g font-size="11.5" fill="#333" font-weight="700">
    <text x="380" y="45">Güneş'in çapı ≈ 109 Dünya çapı</text>
    <text x="380" y="65">Güneş'in hacmi ≈ 1,3 milyon Dünya</text>
    <text x="380" y="90">Dünya'nın çapı ≈ 4 Ay çapı</text>
    <text x="380" y="110">Dünya'nın hacmi ≈ 50 Ay</text>
  </g>
  <text x="10" y="165" font-size="10" fill="#666" font-style="italic">Dünya ve Ay'ın çapları birbirine göre ölçekli çizildi (Dünya yaklaşık 3,7 kat büyük).</text>
</svg>`;
}

// Dinamometre. val: gösterilen değer (0..10 N), labels: parça adları gösterilsin mi
function dynamometer(val = 6, labels = true, w = 260) {
  const top = 50, step = 18; // 0 N çizgisi y = top + 20
  const y0 = top + 20, yv = y0 + val * step;
  let s = `<svg width="${w}" height="330" viewBox="0 0 ${labels ? 300 : 160} 330" xmlns="http://www.w3.org/2000/svg" font-family="Nunito, sans-serif">`;
  s += `<circle cx="70" cy="22" r="13" fill="none" stroke="#555" stroke-width="4"/><rect x="66" y="33" width="8" height="12" fill="#555"/>`;
  s += `<rect x="45" y="${top - 6}" width="50" height="${10 * step + 52}" rx="8" fill="#e8eef7" stroke="#557" stroke-width="2"/>`;
  for (let i = 0; i <= 10; i++) {
    const y = y0 + i * step;
    s += `<line x1="83" y1="${y}" x2="93" y2="${y}" stroke="#333" stroke-width="1.5"/>`;
    if (i % 2 === 0) s += `<text x="${i === 10 ? 98 : 102}" y="${y + 4}" font-size="10" font-weight="700" fill="#333">${i}</text>`;
  }
  s += `<text x="100" y="${y0 - 10}" font-size="10" font-weight="800" fill="#c0392b">N</text>`;
  // yay
  let zz = `M70 ${top} `;
  const n = 10, h = (yv - top - 6) / n;
  for (let i = 1; i <= n; i++) zz += `L${i % 2 ? 56 : 84} ${top + i * h} `;
  zz += `L70 ${yv - 2}`;
  s += `<path d="${zz}" fill="none" stroke="#7a7f8c" stroke-width="2"/>`;
  s += `<rect x="52" y="${yv - 3}" width="36" height="6" rx="2" fill="#e5533d"/>`;
  s += `<line x1="70" y1="${yv}" x2="70" y2="${y0 + 10 * step + 26}" stroke="#555" stroke-width="3"/>`;
  const hy = y0 + 10 * step + 26 + (labels ? 0 : 0);
  s += `<path d="M70 ${hy} v10 a8 8 0 1 1 -10 7" fill="none" stroke="#555" stroke-width="3"/>`;
  s += `<rect x="48" y="${hy + 22}" width="30" height="24" rx="3" fill="#8d6e63"/><text x="63" y="${hy + 38}" font-size="10" text-anchor="middle" fill="#fff" font-weight="800">cisim</text>`;
  if (labels) {
    const L = (y, ty, t) => `<line x1="95" y1="${y}" x2="185" y2="${ty}" stroke="#999" stroke-width="1"/><text x="190" y="${ty + 4}" font-size="11.5" font-weight="800" fill="#333">${t}</text>`;
    s += `<line x1="83" y1="22" x2="185" y2="22" stroke="#999"/><text x="190" y="26" font-size="11.5" font-weight="800" fill="#333">Tutma halkası</text>`;
    s += L(top + 40, 70, 'Esnek yay');
    s += L(yv, yv + 8, 'Gösterge (ibre)');
    s += L(y0 + 4 * step, 165, 'Ölçek (N)');
    s += `<line x1="72" y1="${hy + 10}" x2="185" y2="${hy + 6}" stroke="#999"/><text x="190" y="${hy + 10}" font-size="11.5" font-weight="800" fill="#333">Kanca</text>`;
  }
  return s + `</svg>`;
}

function phaseRow(items) {
  let s = `<svg width="440" height="90" viewBox="0 0 440 90" xmlns="http://www.w3.org/2000/svg" font-family="Nunito, sans-serif">`;
  items.forEach(([letter, f, side], i) => {
    const cx = 55 + i * 110;
    s += phase(cx, 38, 26, f, side);
    s += `<text x="${cx}" y="84" text-anchor="middle" font-size="14" font-weight="800" fill="#333">${letter}</text>`;
  });
  return s + `</svg>`;
}

function positionQ() {
  // I: Ay Güneş ile Dünya arasında; II: Dünya ortada
  const sun = (x, y) => `<circle cx="${x}" cy="${y}" r="16" fill="#ffb627"/><text x="${x}" y="${y + 30}" font-size="10" text-anchor="middle" font-weight="800">Güneş</text>`;
  const earth = (x, y) => `<circle cx="${x}" cy="${y}" r="10" fill="#3b82c4"/><text x="${x}" y="${y + 30}" font-size="10" text-anchor="middle" font-weight="800">Dünya</text>`;
  const moon = (x, y) => `<circle cx="${x}" cy="${y}" r="5" fill="#9aa0ac"/><text x="${x}" y="${y + 30}" font-size="10" text-anchor="middle" font-weight="800">Ay</text>`;
  return `<svg width="520" height="70" viewBox="0 0 520 70" xmlns="http://www.w3.org/2000/svg" font-family="Nunito, sans-serif">
  <text x="0" y="28" font-size="13" font-weight="800">I.</text>${sun(45, 24)}${moon(120, 24)}${earth(175, 24)}
  <text x="270" y="28" font-size="13" font-weight="800">II.</text>${sun(315, 24)}${earth(400, 24)}${moon(460, 24)}
</svg>`;
}

export default {
  ad: 'Fen Bilimleri',
  dosya: 'Fen-Bilimleri',
  kapsam: [
    { kod: 'FB.5.1.1', metin: '<i>Ön bilgi:</i> Güneş\'in yapısı ve dönme hareketi (tabloda 1. yazılıya soru ayrılmamış, ama konuları anlamak için gerekli).' },
    { kod: 'FB.5.1.2', metin: 'Ay\'ın özellikleri, dönme ve dolanma hareketleri ile ilgili bilimsel çıkarım yapabilme' },
    { kod: 'FB.5.1.3', metin: 'Ay\'ın evrelerini temsil eden bilimsel model oluşturabilme' },
    { kod: 'FB.5.1.4', metin: 'Güneş, Dünya ve Ay\'ın birbirlerine göre hareketlerini ve hacimsel büyüklüklerini temsil eden bilimsel model oluşturabilme' },
    { kod: 'FB.5.2.1', metin: 'Kuvveti büyüklüğü ile operasyonel tanımlayabilme (Kuvvet ve Kuvvetin Ölçülmesi)' },
  ],
  kapsamNot: 'MEB tablosunda 1. yazılı için 4 senaryo var; hangisinin uygulanacağını okulundaki fen zümresi seçer. Her çıktıdan senaryoya göre 1–3 soru gelebilir. En çok soru Ay\'ın özellikleri ve Ay\'ın evrelerinden çıkıyor. Kütle–ağırlık ve sürtünme kuvveti 2. yazılının konusudur.',
  icerik: [
    { h: 'Gökyüzündeki Komşumuz: Güneş (ön bilgi)', no: 1, kod: 'FB.5.1.1' },
    { ul: [
      'Güneş bir <b>yıldızdır</b>. Kendi ısısını ve ışığını üretir; Dünya\'mızın <b>ısı ve ışık kaynağıdır</b>.',
      'Katı değildir; çoğunlukla <b>hidrojen ve helyum gazlarından</b> oluşur. Katmanlı bir yapısı vardır.',
      'Güneş de <b>kendi ekseni etrafında döner</b> (ekvator bölgesinde yaklaşık 25 günde bir tur).',
      'Bize en yakın yıldızdır. Çok uzakta olduğu için gökyüzünde küçük görünür.',
    ] },
    { box: 'dikkat', html: '<p>Güneş\'e asla çıplak gözle, dürbünle veya teleskopla bakılmaz; gözlerimize kalıcı zarar verebilir.</p>' },

    { h: 'Gökyüzündeki Komşumuz: Ay', no: 2, kod: 'FB.5.1.2' },
    { p: 'Ay, Dünya\'nın <b>tek doğal uydusudur</b>. Uydu; bir gök cisminin etrafında dolanan gök cismidir.' },
    { cols: [
      [{ h2: 'Ay\'ın özellikleri' }, { ul: [
        'Kendi ışığı <b>yoktur</b>; Güneş\'ten aldığı ışığı <b>yansıttığı</b> için parlak görünür.',
        'Yüzeyi taşlık, tozlu ve engebelidir; dağlar, düzlükler ve <b>kraterler</b> (çukurlar) vardır.',
        '<b>Atmosferi yok</b> denecek kadar azdır.',
        'Yüzeyinde sıvı su ve canlı yoktur.',
        'Çapı Dünya\'nın çapının yaklaşık <b>4\'te 1\'i</b> kadardır.',
        'Ay\'daki çekim, Dünya\'dakinin yaklaşık <b>6\'da 1\'i</b> kadardır; bu yüzden astronotlar Ay\'da daha kolay zıplar.',
      ] }],
      [{ h2: 'Atmosfer olmadığı için…' }, { ul: [
        'Gündüz ile gece arasındaki sıcaklık farkı çok fazladır (gündüz ≈ 120 °C, gece ≈ –170 °C).',
        'Göktaşları yanmadan yüzeye çarpar → <b>kraterler</b> oluşur.',
        'Ses yayılamaz; astronotlar telsizle konuşur.',
        'Rüzgâr ve yağmur olmadığı için astronotların <b>ayak izleri</b> uzun yıllar bozulmadan kalır.',
        'Gökyüzü gündüz bile <b>siyah</b> görünür.',
      ] }],
    ] },
    { h2: 'Ay\'ın hareketleri' },
    { table: { head: ['Hareket', 'Ne demek?', 'Süresi'], rows: [
      ['<b>Dönme</b>', 'Ay\'ın kendi ekseni etrafında dönmesi', 'Yaklaşık 27,3 gün'],
      ['<b>Dolanma</b>', 'Ay\'ın Dünya etrafında dolanması', 'Yaklaşık 27,3 gün'],
      ['Güneş etrafında dolanma', 'Ay, Dünya ile birlikte Güneş etrafında da dolanır', '1 yıl'],
    ] } },
    { box: 'hatirla', html: '<p>Ay\'ın <b>dönme süresi ile dolanma süresi eşittir</b>. Bu yüzden Dünya\'dan Ay\'ın <b>hep aynı yüzünü</b> görürüz. Ay\'ın bize dönük olmayan yüzü de Güneş ışığı alır; yani "hep karanlık" değildir, sadece biz onu göremeyiz.</p>' },
    { box: 'dikkat', html: '<p>"Ay dönmediği için hep aynı yüzünü görüyoruz." cümlesi <b>yanlıştır</b>. Ay döner; dönme ve dolanma süreleri eşit olduğu için aynı yüzü görürüz.</p>' },

    { h: 'Ay\'ın Evreleri', no: 3, kod: 'FB.5.1.3' },
    { p: 'Ay, Dünya etrafında dolanırken gökyüzünde her gece farklı şekillerde görünür. Ay\'ın Dünya\'dan farklı şekillerde görünmesine <b>Ay\'ın evreleri</b> denir.' },
    { h2: 'Evreler nasıl oluşur?' },
    { ol: [
      'Ay\'ın <b>Güneş\'e bakan yarısı her zaman aydınlıktır</b>.',
      'Ay Dünya etrafında dolanırken Güneş, Dünya ve Ay\'ın <b>birbirine göre konumu</b> değişir.',
      'Bu yüzden Ay\'ın aydınlık yarısının <b>Dünya\'dan görebildiğimiz kısmı</b> değişir. İşte evreler bu yüzden oluşur.',
    ] },
    { svg: phaseCycle(), caption: 'Ay\'ın evreleri. Güneş sağda; Ay, Dünya etrafında saat yönünün tersine dolanır.' },
    { table: { head: ['Evre', 'Konum', 'Dünya\'dan görünüşü', 'Yaklaşık zaman'], rows: [
      ['<b>Yeni Ay</b>', 'Ay, Güneş ile Dünya\'nın arasında', 'Görünmez (karanlık yüz bize dönük)', '1. gün'],
      ['<b>İlk Dördün</b>', 'Ay, Dünya\'ya göre Güneş\'le dik açı yapar', 'Sağ yarısı aydınlık', '≈ 7. gün'],
      ['<b>Dolunay</b>', 'Dünya, Güneş ile Ay\'ın arasında', 'Tamamı aydınlık, yuvarlak', '≈ 15. gün'],
      ['<b>Son Dördün</b>', 'Ay, Dünya\'ya göre Güneş\'le dik açı yapar (öbür tarafta)', 'Sol yarısı aydınlık', '≈ 22. gün'],
    ] } },
    { p: 'Ana evrelerin arasında <b>hilal</b> (ince, kavisli) ve <b>şişkin ay</b> (yarıdan fazla aydınlık) görünümleri vardır. Evreler yaklaşık <b>29,5 günde</b> bir tamamlanır ve tekrar başlar. Bu süre 27,3 günden biraz uzundur, çünkü bu sırada Dünya da Güneş etrafında ilerler.' },
    { box: 'ipucu', html: '<p>Kuzey Yarım Küre\'de Ay <b>sağdan büyür, soldan küçülür</b>. Aydınlık kısım <b>sağdaysa</b> Ay büyüyordur (yeni aydan dolunaya); <b>soldaysa</b> küçülüyordur (dolunaydan yeni aya).</p>' },
    { h2: 'Model oluşturalım: Lamba – top etkinliği' },
    { cols: [
      [{ table: { head: ['Modelde', 'Neyi temsil eder?'], rows: [
        ['Lamba / el feneri', 'Güneş'],
        ['Top (strafor top)', 'Ay'],
        ['Öğrencinin başı (gözleri)', 'Dünya (gözlemci)'],
      ] } }],
      [{ ol: [
        'Oda karartılır, lamba sabit bir yere konur.',
        'Topu tutan kol uzatılır; öğrenci kendi etrafında yavaşça <b>saat yönünün tersine</b> döner.',
        'Topun aydınlık kısmının görünen bölümü gözlenir ve çizilir.',
      ] }],
    ] },
    { box: 'ornek', html: '<ul><li>Top, lamba ile baş arasındaysa → <b>yeni ay</b> (topun aydınlık yüzü görülmez).</li><li>Baş, lamba ile top arasındaysa (top başın gölgesine girmeden biraz yukarıda) → <b>dolunay</b>.</li><li>Top yanlarda iken → <b>ilk dördün</b> veya <b>son dördün</b>.</li></ul>' },
    { box: 'bilgi', html: '<p>Bilimsel modeller gerçeği basitleştirerek anlamamızı kolaylaştırır. Ama her modelin <b>sınırlılıkları</b> vardır: Bu etkinlikte lamba ile top arasındaki uzaklık ve büyüklükler gerçekteki oranlarda değildir.</p>' },

    { h: 'Güneş, Dünya ve Ay: Hareketler ve Büyüklükler', no: 4, kod: 'FB.5.1.4' },
    { svg: sunEarthMoon(), caption: 'Güneş, Dünya ve Ay\'ın birbirine göre hareketleri' },
    { table: { head: ['Gök cismi', 'Dönme (kendi etrafında)', 'Dolanma'], rows: [
      ['Güneş', 'Döner', '—'],
      ['Dünya', '≈ 24 saat → gece ve gündüz oluşur', 'Güneş etrafında ≈ 365 gün 6 saat'],
      ['Ay', '≈ 27,3 gün', 'Dünya etrafında ≈ 27,3 gün; Dünya ile birlikte Güneş etrafında 1 yıl'],
    ] } },
    { h2: 'Hacimsel büyüklükler' },
    { p: 'Büyükten küçüğe sıralama: <b>Güneş &gt; Dünya &gt; Ay</b>' },
    { svg: sizes() },
    { box: 'bilgi', html: '<p>Güneş, Ay\'dan yaklaşık 400 kat büyüktür ama Dünya\'ya yaklaşık 400 kat daha uzaktır. Bu yüzden gökyüzünde ikisi <b>neredeyse aynı büyüklükte</b> görünür. Yani bir cismin gökyüzünde küçük görünmesi, onun gerçekten küçük olduğu anlamına gelmez.</p>' },
    { h2: 'Ölçekli model örneği' },
    { table: { head: ['Gök cismi', 'Gerçek çap (yaklaşık)', 'Modelde (Dünya = 1 cm\'lik nohut)'], rows: [
      ['Güneş', '1 milyon 390 bin km', '≈ 109 cm (1 metrelik büyük bir pilates topu)'],
      ['Dünya', '12 750 km', '1 cm (nohut)'],
      ['Ay', '3 475 km', '≈ 3 mm (bir susam / hardal tanesi)'],
    ] } },
    { box: 'dikkat', html: '<p>"Güneş karpuz, Dünya portakal, Ay nohut" gibi modeller sadece <b>büyüklük sıralamasını</b> gösterir; oranları doğru değildir. Gerçekte Güneş, Dünya\'nın yanında çok daha büyüktür. Bir modelin doğru olup olmadığını <b>oranlara</b> bakarak değerlendir.</p>' },

    { h: 'Kuvvet ve Kuvvetin Ölçülmesi', no: 5, kod: 'FB.5.2.1' },
    { p: 'Bir cisme uygulanan <b>itme</b> veya <b>çekme</b> etkisine <b>kuvvet</b> denir. Kuvvet gözle görülmez; ama cisimler üzerindeki <b>etkileri</b> görülür.' },
    { cols: [
      [{ h2: 'Kuvvetin etkileri' }, { table: { head: ['Etki', 'Örnek'], rows: [
        ['Duran cismi <b>hareket ettirir</b>', 'Durmakta olan topa vurmak'],
        ['Hareketli cismi <b>hızlandırır / yavaşlatır</b>', 'Bisiklette pedala hızlı basmak, fren yapmak'],
        ['Hareketli cismi <b>durdurur</b>', 'Kalecinin topu tutması'],
        ['Cismin <b>yönünü</b> değiştirir', 'Gelen topa kafa vurmak'],
        ['Cismin <b>şeklini</b> değiştirir', 'Oyun hamurunu sıkmak, süngeri ezmek'],
      ] } }],
      [{ h2: 'Kuvvetin büyüklüğü' }, { ul: [
        'Kuvvetin bir <b>büyüklüğü</b> ve bir <b>yönü</b> vardır.',
        'Kuvvet <b>ok</b> ile gösterilir: okun yönü kuvvetin yönünü, okun uzunluğu kuvvetin büyüklüğünü gösterir.',
        'Kuvvetin birimi <b>newton</b>dur; <b>N</b> harfiyle gösterilir (bilim insanı Isaac Newton\'un adından).',
        'Kuvvet <b>dinamometre</b> ile ölçülür.',
      ] }],
    ] },
    { h2: 'Dinamometre' },
    { cols: [
      [{ svg: dynamometer(6, true, 280), caption: 'Bu dinamometre 6 N gösteriyor.' }],
      [{ ul: [
        'Dinamometrenin içinde <b>esnek bir yay</b> vardır.',
        'Kancaya asılan cismin uyguladığı kuvvet arttıkça <b>yay daha çok uzar</b>; gösterge ölçekte daha büyük bir değeri gösterir.',
        'Ölçüm bitince yay eski hâline döner (esneklik).',
        'Farklı dinamometrelerin <b>ölçüm aralıkları</b> farklıdır. Kalın/sert yaylı dinamometre büyük kuvvetleri, ince yaylı dinamometre küçük kuvvetleri ölçer.',
      ] }, { box: 'ipucu', title: 'DOĞRU ÖLÇÜM İÇİN', html: '<ul><li>Ölçümden önce göstergenin <b>0</b>\'da olduğunu kontrol et.</li><li>Dinamometreyi <b>dik</b> tut, ölçeği <b>göz hizasından</b> oku.</li><li>Ölçüm sınırını aşan kuvvet uygulama; yay bozulabilir.</li></ul>' }],
    ] },
  ],

  sorular: [
    { q: '<p>Ay\'da atmosfer olmamasının <b>üç</b> sonucunu yazınız.</p>', lines: 3 },
    { q: '<p>Ay\'ın kendi ışığı olmadığı hâlde gece parlak görünmesinin nedenini açıklayınız.</p>', lines: 2 },
    { q: '<p>Ece: "Ay kendi ekseni etrafında dönmediği için Dünya\'dan hep aynı yüzünü görüyoruz." diyor. Ece\'nin düşüncesi doğru mudur? Gerekçesiyle açıklayınız.</p>', lines: 3 },
    { q: '<p>Aşağıda Ay\'ın Dünya\'dan görünen dört evresi verilmiştir. Her evrenin adını yazınız ve yeni aydan başlayarak hangi sırayla görüleceklerini belirtiniz.</p>', svg: phaseRow([['A', 1, 'R'], ['B', 0.5, 'L'], ['C', 0.5, 'R'], ['D', 0.2, 'R']]), lines: 3 },
    { q: '<p>Aşağıda Güneş, Ay ve Dünya\'nın iki farklı konumu verilmiştir. I ve II numaralı konumlarda Dünya\'dan hangi evre görülür? Nedenini açıklayınız.</p>', svg: positionQ(), lines: 3 },
    { q: '<p>Bu akşam gökyüzünde <b>ilk dördün</b> evresi görülüyor. Yaklaşık kaç gün sonra <b>dolunay</b>, yaklaşık kaç gün sonra <b>son dördün</b> görülür?</p>', lines: 2 },
    { q: '<p>Gökyüzünde aydınlık kısmı <b>solda</b> olan ince bir hilal görüyorsunuz. Ay büyüyor mu, küçülüyor mu? Birkaç gün sonra hangi evre görülür?</p>', lines: 2 },
    { q: '<p>Ay\'ın evrelerini lamba ve top kullanarak modelleyeceksiniz. Lamba, top ve sizin başınız neyi temsil eder? <b>Yeni ay</b> evresini göstermek için topu nereye tutmalısınız?</p>', lines: 3 },
    { q: '<p>Ay\'ın evrelerinin tamamlanma süresi (≈ 29,5 gün), Ay\'ın Dünya etrafında dolanma süresinden (≈ 27,3 gün) neden biraz uzundur?</p>', lines: 2 },
    { q: '<p>Güneş, Dünya ve Ay\'ı hacimleri büyükten küçüğe olacak şekilde sıralayınız. Güneş bu kadar büyük olduğu hâlde gökyüzünde neden küçük görünür?</p>', lines: 3 },
    { q: '<p>Bir modelde Dünya 1 cm çapında bir nohut ile gösteriliyor. Bu modelde Güneş\'in çapı yaklaşık kaç cm olmalıdır? Ay için hangi nesneyi seçersiniz?</p>', lines: 2 },
    { q: '<p>Aşağıdaki olaylarda kuvvetin cisim üzerindeki etkisini yazınız.<br>a) Kalecinin gelen topu tutması: ..................<br>b) Oyun hamurunun sıkılması: ..................<br>c) Duran oyuncak arabanın itilmesi: ..................<br>d) Gelen topa kafa vurularak topun başka yöne gitmesi: ..................</p>', lines: 0 },
    { q: '<p>Yandaki dinamometre kaç N gösteriyor? "N" neyin kısaltmasıdır? Kancaya daha ağır bir cisim asılırsa yayda ne değişir?</p>', svg: dynamometer(7, false, 120), lines: 3 },
    { q: '<p>Ölçüm aralıkları 0–10 N ve 0–50 N olan iki dinamometreniz var. Yaklaşık 30 N\'luk bir kuvveti ölçmek için hangisini seçersiniz? Nedenini açıklayınız.</p>', lines: 2 },
  ],

  cevaplar: [
    'Gece ile gündüz arasındaki sıcaklık farkı çok fazladır; göktaşları yanmadan çarptığı için kraterler oluşur; ses yayılmaz; rüzgâr olmadığı için ayak izleri silinmez; gökyüzü siyah görünür. (Herhangi üçü)',
    'Ay, Güneş\'ten aldığı ışığı yansıtır. Yansıyan ışık gözümüze geldiği için Ay\'ı parlak görürüz.',
    'Doğru değildir. Ay kendi ekseni etrafında döner. Dönme süresi ile Dünya etrafındaki dolanma süresi eşit (≈ 27,3 gün) olduğu için hep aynı yüzünü görürüz.',
    'A: Dolunay, B: Son dördün (sol yarı aydınlık), C: İlk dördün (sağ yarı aydınlık), D: Hilal (büyüyen, sağda ince). Sıralama: D → C → A → B.',
    'I: Ay, Güneş ile Dünya\'nın arasında; Ay\'ın aydınlık yüzü Güneş\'e, karanlık yüzü Dünya\'ya dönük olduğu için <b>yeni ay</b> görülür (Ay görünmez). II: Dünya, Güneş ile Ay\'ın arasında; Ay\'ın aydınlık yüzünün tamamı Dünya\'ya dönük olduğu için <b>dolunay</b> görülür.',
    'Yaklaşık 7–8 gün sonra dolunay, yaklaşık 15 gün sonra son dördün görülür.',
    'Aydınlık kısım solda olduğu için Ay küçülüyordur (küçülen hilal). Birkaç gün sonra yeni ay evresi görülür (Ay görünmez).',
    'Lamba Güneş\'i, top Ay\'ı, baş (gözler) Dünya\'yı / Dünya\'daki gözlemciyi temsil eder. Yeni ay için top, lamba ile başın arasında, lambaya doğru tutulmalıdır.',
    'Çünkü Ay Dünya etrafında dolanırken Dünya da Güneş etrafında ilerler. Ay\'ın Güneş\'e göre aynı konuma gelmesi için yaklaşık 2 gün daha yol alması gerekir.',
    'Güneş &gt; Dünya &gt; Ay. Güneş, Dünya\'dan çok uzakta olduğu için küçük görünür.',
    'Yaklaşık 109 cm (yaklaşık 1 metre). Ay için yaklaşık 3 mm\'lik bir nesne (susam, hardal tanesi, küçük boncuk) seçilir.',
    'a) Hareketli cismi durdurma, b) Şekil değiştirme, c) Duran cismi harekete geçirme, d) Yön değiştirme.',
    '7 N. N, kuvvet birimi olan <b>newton</b>un kısaltmasıdır. Daha ağır cisim asılırsa yay daha çok uzar, gösterge daha büyük bir değer gösterir.',
    '0–50 N\'luk dinamometre seçilir. Çünkü 30 N, 0–10 N\'luk dinamometrenin ölçüm sınırını aşar; doğru ölçülemez ve yayı bozulabilir.',
  ],

  kontrol: [
    'Ay\'ın uydu olduğunu ve ışığını Güneş\'ten aldığını açıklayabiliyorum.',
    'Ay\'da atmosfer olmamasının sonuçlarını sayabiliyorum.',
    'Ay\'ın dönme ve dolanma sürelerini ve hep aynı yüzünü görmemizin nedenini söyleyebiliyorum.',
    'Ay\'ın evrelerinin neden oluştuğunu açıklayabiliyorum.',
    'Yeni ay, ilk dördün, dolunay ve son dördünü çizebiliyor, sıralayabiliyorum.',
    'Güneş–Dünya–Ay konumuna bakarak hangi evrenin görüleceğini bulabiliyorum.',
    'Lamba–top modeliyle Ay\'ın evrelerini gösterebiliyorum.',
    'Güneş, Dünya ve Ay\'ın hareketlerini ve büyüklüklerini karşılaştırabiliyorum.',
    'Kuvvetin etkilerini örneklerle açıklayabiliyorum.',
    'Dinamometre ile ölçüm yapıp sonucu newton (N) birimiyle yazabiliyorum.',
  ],
};
