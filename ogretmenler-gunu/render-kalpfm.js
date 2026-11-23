const { chromium } = require('playwright');
const fs = require('fs');
(async () => {
  const b = await chromium.launch();
  fs.writeFileSync('tmp.html', fs.readFileSync('tasarim.html','utf8'));
  const p = await b.newPage({ viewport:{width:794,height:1123}, deviceScaleFactor: 3.125 });
  await p.goto('file://'+process.cwd()+'/tmp.html', {waitUntil:'networkidle'});
  await p.evaluate(() => document.fonts.ready);
  await p.screenshot({ path:'ogretmenler-gunu-kalp-fm.png' });
  await p.pdf({ path:'ogretmenler-gunu-kalp-fm.pdf', format:'A4', printBackground:true, pageRanges:'1' });
  fs.unlinkSync('tmp.html'); await b.close();
})();
