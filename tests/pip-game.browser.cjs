const { chromium } = require('playwright');
const assert = require('node:assert/strict');

const base = process.env.SITE_URL || 'http://127.0.0.1:4173';

(async () => {
  const browser = await chromium.launch({ headless: true, ...(process.env.BROWSER_EXECUTABLE ? { executablePath: process.env.BROWSER_EXECUTABLE } : {}) });
  try {
    for (const width of [390, 1440]) {
      const page = await browser.newPage({ viewport: { width, height: 900 } });
      const errors = [];
      page.on('pageerror', error => errors.push(error.message));
      await page.goto(`${base}/learn/start-here/`);
      assert.ok(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth + 1), `overflow at ${width}px`);
      if (width === 390 && process.env.SCREENSHOT_PATH) await page.locator('#pip-lab').screenshot({ path: process.env.SCREENSHOT_PATH });
      assert.ok(await page.evaluate(() => {
        const title = document.querySelector('article h1');
        const outline = document.getElementById('lessonOutline');
        return title && outline && title.compareDocumentPosition(outline) & Node.DOCUMENT_POSITION_FOLLOWING;
      }));
      assert.equal(await page.locator('#lessonOutline a').count(), 7);
      await page.getByRole('button', { name: '2.5 pips' }).click();
      assert.match(await page.locator('[data-game-feedback]').innerText(), /Not quite/);
      await page.getByRole('button', { name: 'Next round' }).click();
      await page.getByRole('button', { name: '50 pips down' }).click();
      assert.match(await page.locator('[data-game-feedback]').innerText(), /Correct/);
      await page.getByRole('button', { name: 'Next round' }).click();
      await page.getByRole('button', { name: '0.05 lots' }).click();
      assert.match(await page.locator('[data-game-feedback]').innerText(), /Correct/);
      await page.getByRole('button', { name: 'See result' }).click();
      assert.equal(await page.locator('[data-game-question]').innerText(), 'You got 2 of 3 right.');
      await page.getByRole('button', { name: 'Play again' }).click();
      assert.equal(await page.locator('[data-game-top]').innerText(), 'Round 1 of 3');
      assert.deepEqual(errors, []);
      await page.close();
    }
    console.log('PASS: pip game, restart, lesson outline and mobile width.');
  } finally {
    await browser.close();
  }
})().catch(error => { console.error(error); process.exitCode = 1; });
