# Calculator checks

Run `node --test tests/calculators.test.cjs` for calculation and input-boundary tests.

With Playwright installed and the site served locally, run `node tests/browser.cjs`. Set SITE_URL to your preview origin (default http://127.0.0.1:4173). Optionally set BROWSER_EXECUTABLE to an installed Chromium path. Browser screenshots go to tests/output/playwright.

The browser check covers blank inputs and recovery, directional stops, minimum size, account-currency labels, fractional pips, mobile overflow, calendar filters, blocked calendar scripts and the first learning step. Live calendar tests require network access and reference the test date's release names; update those selectors when the event window changes. Timezone probes compare the same scheduled release in UTC and Europe/Warsaw.

The preview renderer used in local development is not a native Jekyll build. Confirm the GitHub Pages build after deployment.
