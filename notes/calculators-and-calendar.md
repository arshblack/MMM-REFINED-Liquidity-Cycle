# Calculator and calendar release

25 September 2026

The mechanics guide and pip lab use assets/calculators.js. Pure functions are covered by `node --test tests/calculators.test.cjs`. Browser checks must cover clearing and restoring every input, buy/sell stop direction, broker minimum/maximum, fractional steps, mobile widths and external calendar failures.

The beginner position estimator uses assets/position-calculator.js with gold, seven major FX pairs and GBPJPY/EURGBP/GBPNZD presets. It converts account size and risk percentage to a money budget. Standard contract sizes and broker-volume assumptions are disclosed; an advanced section accepts broker-specific loss tick values.

Quote/account currency matches need no conversion. If the account currency is the pair's base, conversion uses the proposed stop price. Other combinations use a dated Frankfurter daily reference rate. Rates older than seven days, malformed responses and failed requests block the standard estimate; the user can supply a broker tick value. Switching symbol or account resets overrides; switching symbol clears prices. Requests send only currency codes, not account size or trade inputs. Commission, swap, slippage and margin are outside this estimate. MetaTrader OrderCalcProfit is the broker-specific follow-up.

The TradingView economic-calendar embed uses supported currencyFilter and importanceFilter settings. Filters recreate the embed. A source link is always available if the embed is blocked. The calendar reports scheduled releases and must never be labelled a complete news feed or a signal generator.

The beginner journey begins with the available mechanics guide. The planned Foundations series remains distinct from the five available method previews.

Deployment checks: clean diff, calculator tests, local route checks, real-browser desktop/mobile checks, GitHub Pages build and production smoke test. Roll back this release with a normal revert if empty fields produce a numeric estimate or the primary beginner route fails. If only TradingView is unavailable, keep the source link and explain the dependency; do not publish fabricated event data.
