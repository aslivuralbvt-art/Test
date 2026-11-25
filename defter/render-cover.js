const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 794, height: 1123 } });
  for (const n of ['kapak', 'kapak-fotografli']) {
    await p.goto('file://' + path.join(__dirname, n + '.html'));
    await p.evaluate(() => document.fonts.ready);
    await p.pdf({ path: path.join(__dirname, n + '.pdf'), printBackground: true, preferCSSPageSize: true });
    await p.screenshot({ path: path.join(__dirname, n + '.png') });
  }
  await b.close();
})();
