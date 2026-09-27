const { chromium } = require('playwright');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');

const base = process.env.SITE_URL || 'https://refined.automationssaas.com';
const output = path.join(__dirname, 'output/lesson-visuals');
const routes = [
  '/learn/tracks/read-structure/h1-bias-before-m15/',
  '/learn/tracks/hunt-liquidity/what-a-sweep-does-not-prove/',
  '/learn/tracks/hunt-liquidity/sweep-that-isnt/',
  '/learn/tracks/time-the-killzone/when-london-matters/',
  '/learn/tracks/master-the-mind/pre-trade-journal/'
];

(async () => {
  fs.mkdirSync(output, { recursive: true });
  const browser = await chromium.launch({
    ...(process.env.BROWSER_EXECUTABLE ? { executablePath: process.env.BROWSER_EXECUTABLE } : {}),
    headless: true
  });
  try {
    for (const width of [390, 1440]) {
      const page = await browser.newPage({ viewport: { width, height: 850 } });
      const errors = [];
      page.on('pageerror', error => errors.push(error.message));
      for (let i = 0; i < routes.length; i++) {
        const response = await page.goto(base + routes[i], { waitUntil: 'domcontentloaded' });
        assert.equal(response.status(), 200, routes[i]);
        const figure = page.locator('.lesson-visual');
        await figure.scrollIntoViewIfNeeded();
        await assert.doesNotReject(() => page.waitForFunction(() => {
          const image = document.querySelector('.lesson-visual__image');
          return image && image.complete && image.naturalWidth > 0;
        }));
        assert.equal(await figure.count(), 1, routes[i]);
        assert.match(await figure.locator('img').getAttribute('src'), /-step-4\.svg$/);
        assert.equal(await figure.locator('.lesson-visual__count').textContent(), 'Step 4 of 4');
        assert.ok(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth + 1), routes[i]);
        await figure.screenshot({ path: path.join(output, `${i + 1}-${width}.png`) });
        await figure.locator('[data-action="previous"]').click();
        assert.match(await figure.locator('img').getAttribute('src'), /-step-3\.svg$/);
        await figure.locator('[data-action="next"]').click();
        assert.match(await figure.locator('img').getAttribute('src'), /-step-4\.svg$/);
        await figure.locator('[data-action="replay"]').click();
        assert.match(await figure.locator('img').getAttribute('src'), /-step-1\.svg$/);
      }
      assert.deepEqual(errors, []);
      await page.close();
    }
    const page = await browser.newPage({ viewport: { width: 390, height: 850 } });
    await page.emulateMedia({ reducedMotion: 'reduce' });
    await page.goto(base + routes[0], { waitUntil: 'domcontentloaded' });
    await page.locator('.lesson-visual [data-action="replay"]').click();
    await page.waitForTimeout(1900);
    assert.match(await page.locator('.lesson-visual img').getAttribute('src'), /-step-1\.svg$/);
    await page.close();
    console.log('Five visual lessons passed at 390px and 1440px, including reduced motion.');
  } finally {
    await browser.close();
  }
})().catch(error => { console.error(error); process.exitCode = 1; });
