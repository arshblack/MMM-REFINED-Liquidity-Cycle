const { chromium } = require('playwright');
const assert = require('node:assert/strict');

const base = process.env.SITE_URL || 'http://127.0.0.1:4173';

(async () => {
  const browser = await chromium.launch({ headless: true, ...(process.env.BROWSER_EXECUTABLE ? { executablePath: process.env.BROWSER_EXECUTABLE } : {}) });
  try {
    const page = await browser.newPage({ viewport: { width: 390, height: 844 } });
    await page.goto(base + '/');
    assert.ok(await page.evaluate(() => document.querySelector('#start-title').getBoundingClientRect().top < innerHeight), 'beginner section should be visible below hero');
    await page.locator('.hcta a').first().click();
    assert.match(page.url(), /\/learn\/start-here\//);
    await page.goto(base + '/start/');
    await page.waitForURL('**/learn/start-here/');

    for (const route of ['/learn/start-here/', '/gold-notes/gold-pips-points/']) {
      await page.goto(base + route);
      await page.evaluate(() => scrollTo(0, document.body.scrollHeight / 2));
      const toggle = page.locator('[data-menu-toggle]');
      assert.equal(await toggle.evaluate(el => getComputedStyle(el).flexDirection), 'column');
      await toggle.click();
      assert.equal(await toggle.getAttribute('aria-expanded'), 'true');
      const panel = page.locator('.mobile-nav:not([hidden])');
      const box = await panel.boundingBox();
      assert.ok(box && box.y >= 60 && box.y < 100 && box.height > 100, `${route}: menu should open below sticky header`);
      await page.keyboard.press('Escape');
      assert.equal(await toggle.getAttribute('aria-expanded'), 'false');
      assert.ok(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth + 1), `${route}: horizontal overflow`);
    }
    await page.close();
    console.log('PASS: beginner entry, legacy redirect and deep-scroll mobile menus.');
  } finally {
    await browser.close();
  }
})().catch(error => { console.error(error); process.exitCode = 1; });
