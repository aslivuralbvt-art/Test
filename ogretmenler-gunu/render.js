const { chromium } = require('playwright');
const fs = require('fs');
const heart = `<path d="M240 440 C 120 350, 22 270, 22 160 C 22 85, 80 30, 150 30 C 195 30, 225 55, 240 85 C 255 55, 285 30, 330 30 C 400 30, 458 85, 458 160 C 458 270, 360 350, 240 440 Z" fill="#fafafa" stroke="#c9c9c9" stroke-width="2" stroke-dasharray="10 8"/>
<text x="240" y="225" text-anchor="middle" font-family="Roboto" font-size="15" fill="#b0b0b0">ayna / fotoğraf alanı</text>`;
const rect = `<rect x="30" y="60" width="420" height="330" rx="6" fill="#fafafa" stroke="#c9c9c9" stroke-width="2" stroke-dasharray="10 8"/>
<text x="240" y="232" text-anchor="middle" font-family="Roboto" font-size="15" fill="#b0b0b0">ayna / fotoğraf alanı</text>`;
(async () => {
  const b = await chromium.launch();
  const base = fs.readFileSync('tasarim.html','utf8');
  for (const [n, g] of [['kalp', heart], ['dikdortgen', rect]]) {
    const html = base.replace('<!--GUIDE-->', g);
    fs.writeFileSync(`tmp_${n}.html`, html);
    const p = await b.newPage({ viewport:{width:794,height:1123}, deviceScaleFactor: 3.125 });
    await p.goto('file://'+process.cwd()+`/tmp_${n}.html`, {waitUntil:'networkidle'});
    await p.evaluate(() => document.fonts.ready);
    await p.screenshot({ path:`ogretmenler-gunu-${n}.png` });
    await p.pdf({ path:`ogretmenler-gunu-${n}.pdf`, format:'A4', printBackground:true, pageRanges:'1' });
    console.log(n, await p.evaluate(()=>[...document.fonts].filter(f=>f.status==='loaded').map(f=>f.family).join(',')));
  }
  await b.close();
})();
