---
permalink: /gold-notes/gold-pips-points/
title: "Gold Pips, Points, and Dollars"
description: "Why XAUUSD traders disagree about pip counts, how to state a gold move clearly, and how tick size and tick value affect risk."
page_type: article
note_number: "02"
content_id: RL-NOTE-02
topic: Risk mechanics
query: "Beginner question · How are pips calculated on gold?"
dek: "Gold traders often use the same word for different price increments. The safest language is entry, stop, price distance, and planned dollar risk."
reading_time: 8
published: "2026-08-30"
updated: "2026-09-25"
lesson_url: /learn/start-here/
lesson_title: "Use the Foundations risk calculator"
---

<div class="direct-answer">
  <small>The direct answer</small>
  <p>There is no single pip convention used consistently by every gold trader. Some call a `0.01` XAUUSD move one pip; others call `0.10` one pip. Write the actual price distance and check your broker's tick size and tick value.</p>
</div>

If gold moves from `4500.00` to `4501.00`, the unambiguous statement is: **price moved one US dollar per quoted ounce**. Calling that 100 pips or 10 pips depends on the convention being used. The price move itself does not change.

<div class="note-lab">
  <div class="note-lab-head"><div><small>Interactive distance lab</small><strong>See how the convention changes the count</strong></div><span>Not a lot-size calculator</span></div>
  <div class="pip-calc">
    <label>Start price<input id="noteStart" type="number" step="0.01" value="4500"></label>
    <label>End price<input id="noteEnd" type="number" step="0.01" value="4502"></label>
    <label>Pip convention<select id="notePip"><option value="0.01">0.01 per pip</option><option value="0.10">0.10 per pip</option></select></label>
  </div>
  <p id="pipStatus" class="calc-status" role="status" aria-live="polite">Enter both prices to compare the move.</p>
  <div class="pip-output" aria-live="polite">
    <div><small>Price distance</small><strong id="noteDistance">2.00 USD</strong></div>
    <div><small>Stated count</small><strong id="notePipCount">200 pips</strong></div>
    <div><small>Direction</small><strong id="noteDirection">Up</strong></div>
  </div>
  <p class="lab-result">Change only the convention. The market move stays the same while the pip count changes. That is why entry and stop prices are better public communication.</p>
</div>

## Point, tick, and pip are not the same thing

On MT5, the useful platform terms are defined by the symbol:

- **Point** is tied to the symbol's displayed precision.
- **Tick size** is the minimum allowed price change.
- **Tick value** is the money value of a tick for the stated position volume.
- **Pip** is trader vocabulary and may be used differently between communities.

MetaQuotes exposes tick size, tick value, digits, contract size, minimum volume, and volume step separately. Your EA should use those broker properties instead of assuming every XAUUSD product has identical economics.

## Why lot size alone does not tell you the risk

A `0.10` lot position is exposure. Risk also needs a stop distance.

If the broker's one-lot tick value is `$1` for a `0.01` tick, then a `$10.00` price distance contains 1,000 ticks. At one full lot, that illustrative distance would represent `$1,000`; at `0.10` lot, approximately `$100`, before spread, slippage, or product-specific differences.

Change the stop to `$20.00` without changing the lot and the planned money risk roughly doubles. This is the exact reason the MMM EA now treats `0.10` as a ceiling, not as the default size for every setup.

<div class="honesty-note">
  <strong>What the example does not guarantee</strong>
  <p>Your broker may use different tick values, contract size, profit/loss tick values, currency conversion, or lot steps. Read the live symbol specification and the platform's projected loss before submitting an order.</p>
</div>

## A clearer way to publish a trade plan

Instead of writing only “100-pip stop,” publish:

- Instrument: `XAUUSD` on the stated broker/feed.
- Entry or entry zone: the actual price.
- Invalidation/SL: the actual price.
- Price distance: for example `$8.50`.
- Planned risk: for example “maximum `$100` on the research account.”
- Target logic: preferably in both price and `R` multiples.

That wording remains understandable even when two readers use different pip conventions.

## Risk-to-reward still needs realistic execution

A plan with a `$5` stop and `$20` target is nominally `1:4`. It is not automatically a good trade. The stop still needs a structural reason, and spread or slippage can change the realized result. A narrow stop chosen only to manufacture a large ratio is not risk control.

Refined Liquidity uses the ratio as an audit field: what was planned, what was actually risked, and what was realized. It is evidence after a rule-based setup, not a substitute for one.

## What to remember

- State the actual XAUUSD price distance before using pip language.
- Get tick size and tick value from the broker specification.
- Calculate position size from money risk and stop distance together.
- Treat maximum lot as a ceiling, not a required size.
- Judge risk-to-reward alongside structure and execution quality.

## Sources and further reading

<ul class="source-list">
  <li><a href="https://www.mql5.com/en/docs/constants/environment_state/marketinfoconstants">MetaQuotes · Symbol properties</a> — official definitions for point, tick size, tick value, contract size, and volume steps.</li>
  <li><a href="https://www.mql5.com/en/book/automation/symbols/symbols_margin">MQL5 Programming for Traders · Margin and symbol inputs</a> — the platform variables used in position and margin calculations.</li>
</ul>
