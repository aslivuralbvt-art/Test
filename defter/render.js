const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1123, height: 794 }, deviceScaleFactor: 1 });
  for (const name of ['kitap-ozeti', 'bugunun-ozeti', 'hepsi']) {
    await page.goto('file://' + path.join(__dirname, name + '.html'));
    await page.evaluate(() => document.fonts.ready);
    await page.pdf({ path: path.join(__dirname, name + '.pdf'), format: 'A4', landscape: true, printBackground: true, preferCSSPageSize: true });
    if (name !== 'hepsi') await page.screenshot({ path: path.join(__dirname, name + '.png'), clip: { x: 0, y: 0, width: 1123, height: 794 } });
  }
  await browser.close();
})();
