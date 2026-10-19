// 5. sınıf 1. dönem 1. ortak yazılı çalışma notları -> PDF (kız / erkek temaları)
// Çalıştırma: node render.mjs [ders-id ...]   (örn. node render.mjs matematik)
import { chromium } from 'playwright';
import { mkdirSync, readdirSync, writeFileSync } from 'node:fs';

const THEMES = {
  kiz: {
    c1: '#e84f8a', c2: '#9b6bd3', c3: '#ffc2d9', c4: '#efe3ff', c5: '#fff4f8',
    ink: '#4a2340', line: '#e7b6cc', motifs: ['flower', 'heart', 'butterfly', 'star'],
  },
  erkek: {
    c1: '#1f6fd1', c2: '#16a39a', c3: '#bfe0ff', c4: '#dff6f2', c5: '#f3f9ff',
    ink: '#183457', line: '#b5cde8', motifs: ['rocket', 'star', 'planet', 'bolt'],
  },
};

const svg = {
  flower: (c, s) => `<svg width="${s}" height="${s}" viewBox="0 0 40 40">${[0,72,144,216,288].map(a=>`<ellipse cx="20" cy="10" rx="6.5" ry="9" fill="${c}" opacity=".85" transform="rotate(${a} 20 20)"/>`).join('')}<circle cx="20" cy="20" r="5.5" fill="#ffd34d"/></svg>`,
  heart: (c, s) => `<svg width="${s}" height="${s}" viewBox="0 0 40 40"><path d="M20 35 C6 25 2 17 6 10 C10 4 18 5 20 12 C22 5 30 4 34 10 C38 17 34 25 20 35Z" fill="${c}"/></svg>`,
  butterfly: (c, s) => `<svg width="${s}" height="${s}" viewBox="0 0 40 40"><ellipse cx="12" cy="14" rx="9" ry="8" fill="${c}"/><ellipse cx="28" cy="14" rx="9" ry="8" fill="${c}"/><ellipse cx="13" cy="27" rx="6" ry="6" fill="${c}" opacity=".7"/><ellipse cx="27" cy="27" rx="6" ry="6" fill="${c}" opacity=".7"/><rect x="18.5" y="9" width="3" height="24" rx="1.5" fill="#6b3b5c"/></svg>`,
  star: (c, s) => `<svg width="${s}" height="${s}" viewBox="0 0 40 40"><polygon points="20,3 25,15 38,15.5 27.5,23.5 31.5,36.5 20,29 8.5,36.5 12.5,23.5 2,15.5 15,15" fill="${c}"/></svg>`,
  rocket: (c, s) => `<svg width="${s}" height="${s}" viewBox="0 0 40 40"><g transform="rotate(35 20 20)"><path d="M20 2 C27 9 27 22 25 29 H15 C13 22 13 9 20 2Z" fill="${c}"/><circle cx="20" cy="14" r="3.5" fill="#fff"/><path d="M15 22 L9 30 L15 29Z M25 22 L31 30 L25 29Z" fill="#ff9a3c"/><path d="M16 30 Q20 39 24 30Z" fill="#ffcf3d"/></g></svg>`,
  planet: (c, s) => `<svg width="${s}" height="${s}" viewBox="0 0 40 40"><circle cx="20" cy="20" r="10" fill="${c}"/><ellipse cx="20" cy="20" rx="18" ry="5" fill="none" stroke="#ff9a3c" stroke-width="2.4" transform="rotate(-20 20 20)"/></svg>`,
  bolt: (c, s) => `<svg width="${s}" height="${s}" viewBox="0 0 40 40"><path d="M23 2 L8 23 H18 L15 38 L32 15 H22Z" fill="${c}"/></svg>`,
};

const BOX = {
  dikkat: { label: 'DİKKAT!', color: '#e5533d' },
  ipucu: { label: 'İPUCU', color: '#f2a516' },
  hatirla: { label: 'HATIRLA', color: '#2f9e6b' },
  ornek: { label: 'ÖRNEK', color: '#3c7fd9' },
  bilgi: { label: 'BİLİYOR MUSUN?', color: '#8a5cd1' },
};

function block(b, t) {
  if (b.h) return `<h2 class="sec"><span class="secno">${b.no ?? ''}</span>${b.h}${b.kod ? `<small>${b.kod}</small>` : ''}</h2>`;
  if (b.h2) return `<h3>${b.h2}</h3>`;
  if (b.p) return `<p>${b.p}</p>`;
  if (b.ul) return `<ul>${b.ul.map(i => `<li>${i}</li>`).join('')}</ul>`;
  if (b.ol) return `<ol>${b.ol.map(i => `<li>${i}</li>`).join('')}</ol>`;
  if (b.box) {
    const k = BOX[b.box];
    return `<div class="box" style="--bc:${k.color}"><b class="boxl">${b.title ?? k.label}</b>${b.html}</div>`;
  }
  if (b.table) return `<table class="tbl"><thead><tr>${b.table.head.map(h => `<th>${h}</th>`).join('')}</tr></thead><tbody>${b.table.rows.map(r => `<tr>${r.map(c => `<td>${c}</td>`).join('')}</tr>`).join('')}</tbody></table>`;
  if (b.svg) return `<figure>${b.svg}${b.caption ? `<figcaption>${b.caption}</figcaption>` : ''}</figure>`;
  if (b.cols) return `<div class="cols">${b.cols.map(c => `<div>${c.map(x => block(x, t)).join('')}</div>`).join('')}</div>`;
  if (b.kelime) return `<div class="vocab">${b.kelime.map(([a, c]) => `<div><b>${a}</b><span>${c}</span></div>`).join('')}</div>`;
  if (b.pagebreak) return `<div class="pb"></div>`;
  throw new Error('Bilinmeyen blok: ' + JSON.stringify(b).slice(0, 80));
}

function html(d, t) {
  const kapsam = d.kapsam.map(k => `<tr><td class="kod">${k.kod}</td><td>${k.metin}</td></tr>`).join('');
  const sorular = d.sorular.map((s, i) => `
    <div class="q"><div class="qn">${i + 1}</div><div class="qb">${s.q}${s.svg ? `<figure>${s.svg}</figure>` : ''}
      ${'<div class="wl"></div>'.repeat(s.lines ?? 3)}</div></div>`).join('');
  const cevaplar = d.cevaplar.map((c, i) => `<li><b>${i + 1}.</b> ${c}</li>`).join('');
  const kontrol = d.kontrol.map(k => `<li><span class="cb"></span>${k}</li>`).join('');
  return `<!doctype html><html lang="tr"><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Baloo+2:wght@600;700;800&family=Nunito:ital,wght@0,500;0,600;0,700;0,800;1,600&display=swap" rel="stylesheet">
<style>
@page { size: A4; margin: 0; }
* { box-sizing: border-box; }
body { margin: 0; padding: 0 17mm; font-family: 'Nunito', sans-serif; font-size: 10.5pt; line-height: 1.45; color: ${t.ink};
  -webkit-print-color-adjust: exact; print-color-adjust: exact; }
.frame { position: fixed; top: 6mm; bottom: 7mm; left: 6mm; right: 6mm; border: 1.3mm solid ${t.c3}; border-radius: 6mm; z-index: -1; }
.deco { position: fixed; z-index: -1; }
.foot { position: fixed; bottom: 5.4mm; left: 0; right: 0; text-align: center; font-size: 7.5pt; font-weight: 700; color: ${t.c2}; }
.foot span { background: #fff; padding: 0 2mm; }
.top { text-align: center; padding: 1mm 0 3mm; }
.tag { display: inline-block; font-size: 8pt; font-weight: 800; color: #fff; background: linear-gradient(90deg, ${t.c1}, ${t.c2}); padding: .5mm 4mm; border-radius: 9mm; letter-spacing: .4px; }
h1 { font-family: 'Baloo 2', cursive; font-size: 26pt; line-height: 1.05; margin: 1.5mm 0 0; color: ${t.c1}; display: flex; justify-content: center; align-items: center; gap: 3mm; }
.sub { font-weight: 800; color: ${t.c2}; font-size: 11pt; }
.name { margin-top: 2mm; font-size: 9.5pt; font-weight: 700; }
.name i { display: inline-block; width: 55mm; border-bottom: 1.4px dotted ${t.ink}; }
.panel { background: ${t.c5}; border: 1.3px solid ${t.c3}; border-radius: 4mm; padding: 3mm 4mm; margin: 3mm 0 4mm; break-inside: avoid; }
.panel h4 { font-family: 'Baloo 2', cursive; margin: 0 0 1.5mm; color: ${t.c2}; font-size: 12pt; display: flex; align-items: center; gap: 2mm; }
.kt { width: 100%; border-collapse: collapse; font-size: 9pt; }
.kt td { padding: .8mm 1.5mm; border-bottom: 1px dashed ${t.line}; vertical-align: top; }
.kt td.kod { font-weight: 800; color: ${t.c1}; white-space: nowrap; width: 22mm; }
.note { font-size: 8.5pt; margin: 1.5mm 0 0; font-style: italic; }
h2.sec { font-family: 'Baloo 2', cursive; font-size: 15pt; color: ${t.c1}; margin: 5mm 0 2mm; padding-bottom: 1mm; border-bottom: 2px solid ${t.c3};
  display: flex; align-items: center; gap: 2.5mm; break-after: avoid; }
h2.sec small { margin-left: auto; font-family: 'Nunito'; font-size: 8pt; font-weight: 800; color: #fff; background: ${t.c2}; border-radius: 3mm; padding: .3mm 2.5mm; }
.secno { display: inline-grid; place-items: center; min-width: 8mm; height: 8mm; border-radius: 50%; background: ${t.c1}; color: #fff; font-size: 11pt; }
.secno:empty { display: none; }
h3 { font-family: 'Baloo 2', cursive; font-size: 12pt; color: ${t.c2}; margin: 3mm 0 1mm; break-after: avoid; }
p { margin: 1mm 0 2mm; }
ul, ol { margin: 1mm 0 2mm; padding-left: 6mm; }
li { margin: .6mm 0; }
ul li::marker { color: ${t.c1}; }
b, strong { color: ${t.c1}; }
.box b, .tbl b { color: inherit; }
.box { position: relative; border: 1.5px solid var(--bc); border-left-width: 2.2mm; border-radius: 3mm; padding: 4mm 3.5mm 2mm; margin: 4mm 0 3mm; background: #fff; break-inside: avoid; }
.box .boxl { position: absolute; top: -2.6mm; left: 3mm; background: var(--bc); color: #fff; font-size: 8pt; letter-spacing: .5px; padding: 0 2.5mm; border-radius: 2mm; line-height: 5mm; }
.box p:last-child, .box ul:last-child { margin-bottom: 0; }
.tbl { width: 100%; border-collapse: separate; border-spacing: 0; margin: 2mm 0 3mm; font-size: 9.5pt; break-inside: avoid; border: 1.3px solid ${t.c3}; border-radius: 3mm; overflow: hidden; }
.tbl th { background: ${t.c2}; color: #fff; padding: 1.2mm 2mm; text-align: left; font-weight: 800; }
.tbl td { padding: 1.2mm 2mm; border-top: 1px solid ${t.c3}; vertical-align: top; }
.tbl tr:nth-child(even) td { background: ${t.c5}; }
figure { margin: 2mm 0 3mm; text-align: center; break-inside: avoid; }
figure svg { max-width: 100%; height: auto; }
figcaption { font-size: 8.5pt; font-style: italic; margin-top: 1mm; }
.cols { display: grid; grid-template-columns: 1fr 1fr; gap: 5mm; }
.vocab { display: grid; grid-template-columns: repeat(3, 1fr); gap: 1.5mm; margin: 2mm 0 3mm; }
.vocab div { border: 1.2px solid ${t.c3}; border-radius: 2.5mm; padding: 1mm 2mm; background: ${t.c5}; font-size: 9pt; break-inside: avoid; }
.vocab b { display: block; }
.pb { break-after: page; }
.wrap { width: 100%; border-collapse: collapse; }
.wrap > tbody > tr > td, .wrap > thead > tr > td, .wrap > tfoot > tr > td { padding: 0; }
.chk { list-style: none; padding: 0; columns: 1; }
.chk li { display: flex; gap: 2.5mm; align-items: flex-start; margin: 1.4mm 0; break-inside: avoid; }
.cb { flex: none; width: 4mm; height: 4mm; border: 1.5px solid ${t.c2}; border-radius: 1mm; margin-top: .6mm; background: #fff; }
.q { display: flex; gap: 3mm; margin: 0 0 4mm; break-inside: avoid; }
.qn { flex: none; width: 7.5mm; height: 7.5mm; border-radius: 50%; background: ${t.c2}; color: #fff; font-weight: 800; display: grid; place-items: center; font-size: 10pt; }
.qb { flex: 1; }
.qb p { margin: 0 0 1mm; }
.wl { border-bottom: 1.4px dashed ${t.line}; height: 7.5mm; }
.ans { columns: 1; padding-left: 0; list-style: none; font-size: 9.5pt; }
.ans li { margin: 0 0 2mm; break-inside: avoid; }
.hd { font-family: 'Baloo 2', cursive; font-size: 17pt; color: ${t.c1}; margin: 0 0 3mm; text-align: center; display: flex; justify-content: center; align-items: center; gap: 2mm; }
.score { text-align: center; margin: 4mm 0 0; font-weight: 800; color: ${t.c2}; }
</style></head><body>
<div class="frame"></div>
${[8, 30, 52, 74, 92].map((y, i) => `<div class="deco" style="left:1mm;top:${y}%">${svg[t.motifs[i % 4]]([t.c1, t.c2][i % 2], 20)}</div><div class="deco" style="right:1mm;top:${y - 4}%">${svg[t.motifs[(i + 2) % 4]]([t.c2, t.c1][i % 2], 20)}</div>`).join('')}
<div class="foot"><span>5. Sınıf ${d.ad} · 1. Dönem 1. Ortak Yazılı Çalışma Notları</span></div>

<table class="wrap"><thead><tr><td><div style="height:12mm"></div></td></tr></thead>
<tfoot><tr><td><div style="height:13mm"></div></td></tr></tfoot><tbody><tr><td>
<div class="top">
  <div class="tag">Türkiye Yüzyılı Maarif Modeli · 5. Sınıf · 1. Dönem 1. Ortak Yazılı</div>
  <h1>${svg[t.motifs[0]](t.c1, 30)} ${d.ad} ${svg[t.motifs[1]](t.c2, 30)}</h1>
  <div class="sub">Yazılıya Hazırlık Çalışma Notları</div>
  <div class="name">Adım Soyadım: <i></i> &nbsp; Sınav tarihi: <i style="width:28mm"></i></div>
</div>

<div class="panel">
  <h4>${svg[t.motifs[3]](t.c2, 16)} Bu yazılıda neler var? (MEB konu–soru dağılım tablosu)</h4>
  <table class="kt">${kapsam}</table>
  <p class="note">${d.kapsamNot}</p>
</div>

${d.icerik.map(b => block(b, t)).join('\n')}

<div class="pb"></div>
<div class="hd">${svg[t.motifs[2]](t.c1, 22)} Yazılıya Hazırlık Soruları ${svg[t.motifs[3]](t.c2, 22)}</div>
${sorular}

<div class="panel">
  <h4>${svg[t.motifs[0]](t.c2, 16)} Kendimi Değerlendiriyorum</h4>
  <ul class="chk">${kontrol}</ul>
</div>

<div class="pb"></div>
<div class="hd">${svg[t.motifs[1]](t.c1, 22)} Cevap Anahtarı ${svg[t.motifs[0]](t.c2, 22)}</div>
<p class="note" style="text-align:center;margin-bottom:4mm">Önce soruları kendin çöz, sonra buradan kontrol et. Açık uçlu sorularda kendi cümlelerinle yazdığın doğru cevaplar da kabul edilir.</p>
<ol class="ans">${cevaplar}</ol>
</td></tr></tbody></table>
</body></html>`;
}

const want = process.argv.slice(2);
const files = readdirSync('icerik').filter(f => f.endsWith('.mjs')).map(f => f.replace('.mjs', ''))
  .filter(id => !want.length || want.includes(id));
mkdirSync('pdf', { recursive: true });
const browser = await chromium.launch();
const page = await browser.newPage();
for (const id of files) {
  const d = (await import(`./icerik/${id}.mjs?${Date.now()}`)).default;
  for (const [key, t] of Object.entries(THEMES)) {
    const h = html(d, t);
    writeFileSync(`pdf/.${id}-${key}.html`, h);
    await page.setContent(h, { waitUntil: 'networkidle' });
    await page.evaluate(() => document.fonts.ready);
    const out = `pdf/5-Sinif-${d.dosya}-1-Yazili-${key === 'kiz' ? 'KIZ' : 'ERKEK'}.pdf`;
    await page.pdf({ path: out, format: 'A4', printBackground: true, preferCSSPageSize: true });
    console.log('OK', out);
  }
}
await browser.close();
