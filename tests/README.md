# Calculator checks

Run `node --test tests/calculators.test.cjs` for calculation and input-boundary tests.

With Playwright installed and the site served locally, run `node tests/browser.cjs`. Set SITE_URL to your preview origin (default http://127.0.0.1:4173). Optionally set BROWSER_EXECUTABLE to an installed Chromium path. Browser screenshots go to tests/output/playwright.

The browser check covers blank inputs and recovery, directional stops, minimum size, account-currency labels, fractional pips, mobile overflow, calendar filters and fallback, and the first learning step. It stubs the daily FX-rate response so the result does not depend on API uptime. Verify the live TradingView calendar and its timezone manually after deployment; event names change and should not be hard-coded into a regression test. Run `node tests/navigation.browser.cjs` to check the beginner entry route and both mobile menus after scrolling.

The preview renderer used in local development is not a native Jekyll build. Confirm the GitHub Pages build after deployment.
