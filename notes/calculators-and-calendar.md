# Calculator and calendar release

25 September 2026

The mechanics guide and pip lab use assets/calculators.js. Pure functions are covered by `node --test tests/calculators.test.cjs`. Browser checks must cover clearing and restoring every input, buy/sell stop direction, broker minimum/maximum, fractional steps, mobile widths and external calendar failures.

Inputs are broker-specific estimates. No quote or conversion API is connected. Currency selection labels the user's values. Commission, swap, slippage and margin are outside this calculator. MetaTrader OrderCalcProfit is the broker-specific follow-up.

The TradingView economic-calendar embed uses supported currencyFilter and importanceFilter settings. Filters recreate the embed. A source link is always available if the embed is blocked. The calendar reports scheduled releases and must never be labelled a complete news feed or a signal generator.

The beginner journey begins with the available mechanics guide. The planned Foundations series remains distinct from the five available method previews.

Deployment checks: clean diff, calculator tests, local route checks, real-browser desktop/mobile checks, GitHub Pages build and production smoke test. Roll back this release with a normal revert if empty fields produce a numeric estimate or the primary beginner route fails. If only TradingView is unavailable, keep the source link and explain the dependency; do not publish fabricated event data.
