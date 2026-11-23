const { chromium } = require('playwright');
const fs = require('fs');
const heart = `<path d="M300 560 C 150 445, 28 345, 28 205 C 28 108, 100 40, 188 40 C 245 40, 282 72, 300 110 C 318 72, 355 40, 412 40 C 500 40, 572 108, 572 205 C 572 345, 450 445, 300 560 Z" fill="#fafafa" stroke="#d0d0d0" stroke-width="2" stroke-dasharray="10 8"/>`;
const rect = `<rect x="40" y="70" width="520" height="400" rx="6" fill="#fafafa" stroke="#d0d0d0" stroke-width="2" stroke-dasharray="10 8"/>`;
const extra = `<style>.card,.foot,.stats{display:none!important}.mirror{top:372px!important}</style>`;
(async () => {
  const b = await chromium.launch();
  let base = fs.readFileSync('tasarim.html','utf8')
    .replace('width="480" height="470" viewBox="0 0 480 470"','width="600" height="600" viewBox="0 0 600 600"')
    .replace('</head>', extra + '</head>');
  for (const [n, g] of [['kalp', heart], ['dikdortgen', rect]]) {
    fs.writeFileSync(`tmp_${n}.html`, base.replace('<!--GUIDE-->', g));
    const p = await b.newPage({ viewport:{width:794,height:1123}, deviceScaleFactor: 3.125 });
    await p.goto('file://'+process.cwd()+`/tmp_${n}.html`, {waitUntil:'networkidle'});
    await p.evaluate(() => document.fonts.ready);
    await p.screenshot({ path:`ogretmenler-gunu-sade-${n}.png` });
    await p.pdf({ path:`ogretmenler-gunu-sade-${n}.pdf`, format:'A4', printBackground:true, pageRanges:'1' });
    fs.unlinkSync(`tmp_${n}.html`);
  }
  await b.close();
})();
