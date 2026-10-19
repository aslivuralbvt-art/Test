// Haftalık Ödev Planı şablonu (kız / erkek temaları) -> PDF
// Çalıştırma: node build.mjs   (playwright gerekir)
import { chromium } from 'playwright';
import { writeFileSync } from 'node:fs';

const DAYS = [
  { name: 'PAZARTESİ', lessons: ['İngilizce', 'Türkçe', 'Matematik', 'Sosyal Bilgiler', 'Din Kültürü'] },
  { name: 'SALI', lessons: ['Türkçe', 'Matematik', 'İngilizce', 'Müzik'] },
  { name: 'ÇARŞAMBA', lessons: ['Spor', 'İngilizce', 'Fen Bilimleri', 'Görsel Sanatlar'] },
  { name: 'PERŞEMBE', lessons: ['İngilizce', 'Fen Bilimleri', 'Rehberlik', 'Matematik', 'Almanca'] },
  { name: 'CUMA', lessons: ['Türkçe', 'Fen Bilimleri', 'Bilgisayar', 'Beden Eğitimi', 'İngilizce'] },
];

const THEMES = {
  kiz: {
    file: 'Haftalik-Odev-Plani-KIZ.pdf',
    title: 'Haftalık Ödev Planım',
    c1: '#e84f8a', c2: '#9b6bd3', c3: '#ffc2d9', c4: '#efe3ff', c5: '#fff4f8',
    ink: '#5a2a4a', line: '#e7b6cc', arrow: '#c76aa0',
    days: ['#ff8fb8', '#b48ef0', '#ffa98a', '#7fc8e8', '#f6a6d6'],
    motifs: ['flower', 'heart', 'butterfly', 'flower', 'heart', 'star'],
  },
  erkek: {
    file: 'Haftalik-Odev-Plani-ERKEK.pdf',
    title: 'Haftalık Görev Planım',
    c1: '#1f6fd1', c2: '#16a39a', c3: '#bfe0ff', c4: '#dff6f2', c5: '#f3f9ff',
    ink: '#183457', line: '#b5cde8', arrow: '#3f86d8',
    days: ['#3b8ef0', '#20b3a5', '#ff9a3c', '#7b6cf0', '#3fbf62'],
    motifs: ['rocket', 'star', 'planet', 'bolt', 'star', 'planet'],
  },
};

// ---------- SVG motifler ----------
const svg = {
  flower: (c, s) => `<svg width="${s}" height="${s}" viewBox="0 0 40 40">${[0,72,144,216,288].map(a=>`<ellipse cx="20" cy="10" rx="6.5" ry="9" fill="${c}" opacity=".85" transform="rotate(${a} 20 20)"/>`).join('')}<circle cx="20" cy="20" r="5.5" fill="#ffd34d"/></svg>`,
  heart: (c, s) => `<svg width="${s}" height="${s}" viewBox="0 0 40 40"><path d="M20 35 C6 25 2 17 6 10 C10 4 18 5 20 12 C22 5 30 4 34 10 C38 17 34 25 20 35Z" fill="${c}"/></svg>`,
  butterfly: (c, s) => `<svg width="${s}" height="${s}" viewBox="0 0 40 40"><ellipse cx="12" cy="14" rx="9" ry="8" fill="${c}"/><ellipse cx="28" cy="14" rx="9" ry="8" fill="${c}"/><ellipse cx="13" cy="27" rx="6" ry="6" fill="${c}" opacity=".7"/><ellipse cx="27" cy="27" rx="6" ry="6" fill="${c}" opacity=".7"/><rect x="18.5" y="9" width="3" height="24" rx="1.5" fill="#6b3b5c"/><path d="M19 9 Q15 3 13 4 M21 9 Q25 3 27 4" stroke="#6b3b5c" stroke-width="1.3" fill="none"/></svg>`,
  star: (c, s) => `<svg width="${s}" height="${s}" viewBox="0 0 40 40"><polygon points="20,3 25,15 38,15.5 27.5,23.5 31.5,36.5 20,29 8.5,36.5 12.5,23.5 2,15.5 15,15" fill="${c}" stroke-linejoin="round"/></svg>`,
  rocket: (c, s) => `<svg width="${s}" height="${s}" viewBox="0 0 40 40"><g transform="rotate(35 20 20)"><path d="M20 2 C27 9 27 22 25 29 H15 C13 22 13 9 20 2Z" fill="${c}"/><circle cx="20" cy="14" r="3.5" fill="#fff"/><path d="M15 22 L9 30 L15 29Z M25 22 L31 30 L25 29Z" fill="#ff9a3c"/><path d="M16 30 Q20 39 24 30Z" fill="#ffcf3d"/></g></svg>`,
  planet: (c, s) => `<svg width="${s}" height="${s}" viewBox="0 0 40 40"><circle cx="20" cy="20" r="10" fill="${c}"/><ellipse cx="20" cy="20" rx="18" ry="5" fill="none" stroke="#ff9a3c" stroke-width="2.4" transform="rotate(-20 20 20)"/></svg>`,
  bolt: (c, s) => `<svg width="${s}" height="${s}" viewBox="0 0 40 40"><path d="M23 2 L8 23 H18 L15 38 L32 15 H22Z" fill="${c}"/></svg>`,
  arrow: (c) => `<svg width="22" height="12" viewBox="0 0 22 12"><path d="M1 6 H17" stroke="${c}" stroke-width="2.2" stroke-linecap="round" stroke-dasharray="3 2.5"/><path d="M14 1.5 L20.5 6 L14 10.5" stroke="${c}" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg>`,
};

function motifColor(t, i) { return [t.c1, t.c2, t.days[2], t.days[3], t.days[4]][i % 5]; }

// Kenar süslemeleri: sayfa çerçevesinin iki yanına dağılmış motifler
function borderDeco(t, seed) {
  let out = '';
  const ys = [6, 18, 30, 42, 54, 66, 78, 88];
  ys.forEach((y, i) => {
    const m = t.motifs[(i + seed) % t.motifs.length];
    out += `<div class="deco" style="left:1.2mm;top:${y}%">${svg[m](motifColor(t, i + seed), 24)}</div>`;
    const m2 = t.motifs[(i + seed + 3) % t.motifs.length];
    out += `<div class="deco" style="right:1.2mm;top:${y + 6}%">${svg[m2](motifColor(t, i + seed + 2), 24)}</div>`;
  });
  return out;
}

function dayBlock(t, d, idx) {
  const col = t.days[idx];
  const rows = d.lessons.map(l => `
    <tr>
      <td class="les"><span class="chip" style="border-color:${col}">${l}</span></td>
      <td class="arr">${svg.arrow(t.arrow)}</td>
      <td class="hw"><div class="wline"></div></td>
      <td class="arr">${svg.arrow(t.arrow)}</td>
      <td class="due"><div class="wline"></div></td>
    </tr>`).join('');
  return `
  <section class="day">
    <div class="dayhead">
      <span class="dayname" style="background:${col}">${svg[t.motifs[idx]]('#fff', 15)} ${d.name}</span>
      <span class="daydate">Tarih: <i></i></span>
      <span class="colh hwh">ÖDEV</span>
      <span class="colh dueh">TESLİM TARİHİ</span>
    </div>
    <table>${rows}</table>
    <div class="after" style="border-color:${col}">
      <div class="aftlabel" style="background:${col}">OKULDAN SONRA</div>
      <div class="aftlines">
        <div class="aline"><b class="box"></b><div class="wline"></div></div>
        <div class="aline"><b class="box"></b><div class="wline"></div></div>
      </div>
    </div>
  </section>`;
}

function header(t) {
  return `
  <header>
    <div class="tag">Türkiye Yüzyılı Maarif Modeli · Ortaokul</div>
    <h1>${svg[t.motifs[0]](t.c1, 30)} ${t.title} ${svg[t.motifs[1]](t.c2, 30)}</h1>
    <div class="meta">
      <span>Adım Soyadım: <i style="width:36mm"></i></span>
      <span>Sınıfım: <i style="width:10mm"></i></span>
      <span>Hafta: <i style="width:14mm"></i> – <i style="width:14mm"></i></span>
      <span>Okuma kitabım: <i style="width:34mm"></i></span>
    </div>
  </header>`;
}

function page(t, content, seed) {
  return `<div class="page">
    <div class="frame"></div>
    ${borderDeco(t, seed)}
    <div class="inner">${content}</div>
  </div>`;
}

function html(t) {
  const body = header(t) + DAYS.map((d, i) => dayBlock(t, d, i)).join('');
  return `<!doctype html><html lang="tr"><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Baloo+2:wght@600;700;800&family=Nunito:wght@600;700;800&display=swap" rel="stylesheet">
<style>
@page { size: A4; margin: 0; }
* { box-sizing: border-box; margin: 0; padding: 0; }
body { font-family: 'Nunito', sans-serif; color: ${t.ink}; -webkit-print-color-adjust: exact; print-color-adjust: exact; }
.page { width: 210mm; height: 297mm; position: relative; overflow: hidden; page-break-after: always; background: ${t.c5}; }
.frame { position: absolute; inset: 5mm 9mm; border: 1.6mm solid ${t.c3}; border-radius: 7mm;
  box-shadow: inset 0 0 0 0.6mm #fff, inset 0 0 0 1.2mm ${t.c4}; background: #fff; }
.deco { position: absolute; width: 24px; height: 24px; }
.inner { position: absolute; inset: 8.5mm 14mm 8.5mm 14mm; display: flex; flex-direction: column; justify-content: space-between; }
.pno { position: absolute; bottom: 7.5mm; right: 50%; transform: translateX(50%); font-size: 8pt; color: ${t.c2}; background:#fff; padding: 0 2mm; }
header { text-align: center; }
.tag { display: inline-block; font-size: 7.5pt; font-weight: 800; letter-spacing: .5px; color: #fff; background: linear-gradient(90deg, ${t.c1}, ${t.c2}); padding: .6mm 3.5mm; border-radius: 9mm; }
h1 { font-family: 'Baloo 2', cursive; font-size: 18pt; font-weight: 800; line-height: 1.1; margin-top: .8mm;
  color: ${t.c1}; display: flex; align-items: center; justify-content: center; gap: 3mm; }
.meta { display: flex; justify-content: center; gap: 3.5mm; font-size: 8pt; font-weight: 700; margin-top: .6mm; white-space: nowrap; }
i { display: inline-block; border-bottom: 1.4px dotted ${t.ink}; height: 4mm; vertical-align: bottom; font-style: normal; }
.day { }
.dayhead { display: grid; grid-template-columns: 40mm 1fr 62mm 36mm; align-items: end; gap: 0 2mm; margin-bottom: .2mm; }
.dayname { font-family: 'Baloo 2', cursive; font-weight: 800; font-size: 10.5pt; color: #fff; padding: 0 3mm; border-radius: 3mm 3mm 3mm 0;
  display: inline-flex; align-items: center; gap: 1.5mm; width: max-content; line-height: 1.5; }
.daydate { font-size: 9pt; font-weight: 700; }
.daydate i { width: 26mm; }
.colh { font-family: 'Baloo 2', cursive; font-size: 8.5pt; font-weight: 800; color: ${t.c2}; letter-spacing: .6px; text-align: center; }
table { width: 100%; border-collapse: separate; border-spacing: 0; }
td { height: 6.1mm; vertical-align: bottom; padding-bottom: .5mm; line-height: 1.25; }
td.les { width: 33mm; }
.chip { display: inline-block; font-weight: 800; font-size: 8.5pt; padding: 0 2.2mm; border: 1.3px solid; border-radius: 4mm; background: ${t.c5}; white-space: nowrap; }
td.arr { width: 7mm; text-align: center; padding-bottom: .5mm; line-height: 0; }
td.hw { }
td.due { width: 36mm; }
.wline { border-bottom: 1.5px dashed ${t.line}; height: 3.6mm; }
tr + tr td { border-top: 0; }
.after { border: 1.4px solid; border-radius: 3mm; position: relative; margin-top: 1.8mm; padding: 2mm 3mm 1mm; background: ${t.c5}; }
.aftlabel { position: absolute; top: -2.4mm; left: 4mm; color: #fff; font-size: 7.5pt; font-weight: 800; letter-spacing: .6px; padding: 0 2.5mm; border-radius: 2mm; line-height: 4.4mm; }
.aline { display: flex; align-items: end; gap: 2mm; height: 5.2mm; }
.aline .wline { flex: 1; height: auto; }
.box { width: 3.6mm; height: 3.6mm; border: 1.4px solid ${t.c2}; border-radius: 1mm; flex: none; background:#fff; }
</style></head><body>
${page(t, body, 0)}
</body></html>`;
}

const browser = await chromium.launch();
const pg = await browser.newPage();
for (const [key, t] of Object.entries(THEMES)) {
  const h = html(t);
  writeFileSync(`sablon-${key}.html`, h);
  await pg.setContent(h, { waitUntil: 'networkidle' });
  await pg.evaluate(() => document.fonts.ready);
  await pg.pdf({ path: t.file, format: 'A4', printBackground: true, preferCSSPageSize: true });
  await pg.screenshot({ path: `onizleme-${key}.png`, fullPage: true });
  console.log('OK', t.file);
}
await browser.close();
