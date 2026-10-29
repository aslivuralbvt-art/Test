// Kullanım: node olustur.js [kullaniciadi]
// Her şablonu 1080x1350 PNG olarak png/ klasörüne kaydeder ve bir grid önizlemesi üretir.
const { chromium } = require("playwright");
const path = require("path");
const fs = require("fs");

(async () => {
  const user = process.argv[2] || "kullaniciadi";
  const out = path.join(__dirname, "png");
  fs.mkdirSync(out, { recursive: true });

  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1200, height: 1500 } });
  const url = "file://" + path.join(__dirname, "sablonlar.html") + "?u=" + encodeURIComponent(user);
  await page.goto(url, { waitUntil: "networkidle" });
  await page.evaluate(() => document.fonts.ready);

  const ids = await page.$$eval(".post", els => els.map(e => e.id));
  for (const id of ids) {
    await page.locator(`[id="${id}"]`).screenshot({ path: path.join(out, id + ".png") });
    console.log("✓", id);
  }

  // Profil grid önizlemesi (3x3, Instagram 4:5 görünümü)
  const imgs = ids.map(id => "data:image/png;base64," + fs.readFileSync(path.join(out, id + ".png")).toString("base64"));
  await page.setViewportSize({ width: 1086, height: 1356 });
  await page.setContent(`<body style="margin:0;background:#fff;display:grid;grid-template-columns:repeat(3,360px);gap:3px">
    ${imgs.map(s => `<img src="${s}" style="width:360px;height:450px;display:block">`).join("")}</body>`);
  await page.screenshot({ path: path.join(out, "00-grid-onizleme.png"), fullPage: true });
  console.log("✓ grid önizleme");

  await browser.close();
})();
