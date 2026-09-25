---
permalink: /learn/start-here/
title: "Gold Trading Mechanics: A Short Guide"
description: "A plain-language starting point for XAUUSD, pips, lot size, stop loss, take profit, and MT5 risk checks."
content_id: RL-FND-START
track: gold-foundations
level: Beginner
reading_time: 12
status: public
previous_url: /learn/
previous_title: Learn hub
next_url: /learn/tracks/read-structure/h1-bias-before-m15/
next_title: H1 Bias Before M15 Execution
last_reviewed: 2026-09-25
---

# Start with the mechanics

**New to gold or MetaTrader 5? Begin here. You do not need to understand liquidity, BOS, CHoCH, or killzones yet.**

This page gives you the minimum foundation needed to read an XAUUSD trade plan without guessing. Work from top to bottom on a demo account. The goal is not to place a trade today. The goal is to understand exactly what a trade would risk before you press a button.

<div class="foundation-lab" aria-label="Visual entry stop and target lab">
  <header>
    <div><small>Visual lab 01</small><strong>Entry, invalidation, and target</strong></div>
    <span>Long setup example</span>
  </header>
  <div class="trade-plan-visual" role="img" aria-label="Candlestick chart showing a long entry after a pullback, invalidation below structure, a partial objective at one R, and a final target at two R">
    <svg viewBox="0 0 760 330" aria-hidden="true">
      <defs>
        <linearGradient id="rewardZone" x1="0" y1="1" x2="0" y2="0"><stop offset="0" stop-color="#3FE0C5" stop-opacity=".04"/><stop offset="1" stop-color="#3FE0C5" stop-opacity=".18"/></linearGradient>
        <linearGradient id="riskZone" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#E0683F" stop-opacity=".04"/><stop offset="1" stop-color="#E0683F" stop-opacity=".18"/></linearGradient>
        <marker id="planArrow" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 Z" fill="#E9C97A"/></marker>
      </defs>
      <g class="plan-grid"><path d="M70 42H700M70 96H700M70 150H700M70 204H700M70 258H700M70 312H700"/><path d="M112 28V312M196 28V312M280 28V312M364 28V312M448 28V312M532 28V312M616 28V312"/></g>
      <rect class="reward-zone" x="70" y="48" width="630" height="132" rx="2"/><rect class="risk-zone" x="70" y="180" width="630" height="66" rx="2"/>
      <g class="plan-level target-level"><path d="M70 48H700"/><text x="82" y="40">FINAL TARGET · +2R</text><text x="686" y="40" text-anchor="end">TAKE PROFIT</text></g>
      <g class="plan-level partial-level"><path d="M70 114H700"/><text x="82" y="106">FIRST OBJECTIVE · +1R</text><text x="686" y="106" text-anchor="end">PARTIAL / PROTECT</text></g>
      <g class="plan-level entry-level"><path d="M70 180H700"/><text x="82" y="171">ENTRY · 0R</text><text x="686" y="171" text-anchor="end">RISK BEGINS HERE</text></g>
      <g class="plan-level stop-level"><path d="M70 246H700"/><text x="82" y="266">INVALIDATION · -1R</text><text x="686" y="266" text-anchor="end">STOP LOSS</text></g>
      <g class="candles">
        <g class="candle up"><path d="M116 242V207"/><rect x="109" y="218" width="14" height="17"/></g><g class="candle up"><path d="M152 230V188"/><rect x="145" y="202" width="14" height="22"/></g><g class="candle down"><path d="M188 198V242"/><rect x="181" y="204" width="14" height="25"/></g><g class="candle up"><path d="M224 226V172"/><rect x="217" y="184" width="14" height="34"/></g><g class="candle up"><path d="M260 192V142"/><rect x="253" y="154" width="14" height="29"/></g><g class="candle down"><path d="M296 145V194"/><rect x="289" y="156" width="14" height="27"/></g><g class="candle down"><path d="M332 166V216"/><rect x="325" y="174" width="14" height="29"/></g><g class="candle up entry-candle"><path d="M368 214V166"/><rect x="361" y="178" width="14" height="27"/></g><g class="candle up"><path d="M404 186V134"/><rect x="397" y="145" width="14" height="34"/></g><g class="candle down"><path d="M440 136V170"/><rect x="433" y="142" width="14" height="19"/></g><g class="candle up"><path d="M476 158V106"/><rect x="469" y="116" width="14" height="34"/></g><g class="candle up"><path d="M512 122V78"/><rect x="505" y="88" width="14" height="28"/></g><g class="candle down"><path d="M548 72V112"/><rect x="541" y="82" width="14" height="21"/></g><g class="candle up"><path d="M584 96V48"/><rect x="577" y="58" width="14" height="31"/></g>
      </g>
      <path class="projected-path" d="M368 180 C430 150 486 104 584 48" marker-end="url(#planArrow)"/><circle class="entry-marker" cx="368" cy="180" r="7"/><text class="entry-callout" x="383" y="199">confirmation closes above entry</text>
      <path class="risk-bracket" d="M718 180h14M725 180v66M718 246h14"/><text class="risk-copy" x="742" y="213" transform="rotate(90 742 213)">1R PLANNED RISK</text>
    </svg>
  </div>
  <div class="trade-plan-legend"><div><i class="legend-swatch reward"></i><span><b>Reward zone</b> begins only after entry.</span></div><div><i class="legend-swatch risk"></i><span><b>Risk zone</b> ends where the idea is invalid.</span></div><div><i class="legend-swatch path"></i><span>The path is a <b>scenario</b>, never a promise.</span></div></div>
</div>

## 1. What XAUUSD means

`XAU` is gold. `USD` is the US dollar. An XAUUSD quote tells you how many US dollars the feed is quoting for one troy ounce of gold.

Your broker may show `XAUUSD`, `XAUUSD.`, `GOLD`, or another suffix. Those names can describe similar markets while still having different contract sizes, tick values, spreads, and trading hours. **Always open MT5 → Market Watch → Specification before calculating risk.**

## 2. Point, pip, and price move

Gold traders use the word *pip* inconsistently. One person may call a `0.01` move one pip; another may call a `0.10` move one pip. The platform itself gives you safer numbers:

- **Digits** — how many decimals the symbol displays.
- **Point** — the smallest displayed price increment.
- **Tick size** — the minimum tradable price change.
- **Tick value** — the money gained or lost for one tick at a stated lot size.

When somebody says “100 pips,” ask what price distance they mean. A written entry and stop price are clearer than pip slang.

## 3. Lot size is exposure, not risk

A lot controls how much the position gains or loses as price moves. It does **not** tell you the risk by itself. Risk depends on both lot size and the distance from entry to stop loss.

The same `0.10` lot can be a small risk with a tight stop and a much larger risk with a wide structural stop. Calculate the money at risk before choosing the volume.

Choose gold or a currency pair, then enter your account size, risk percentage and planned prices. **Risk percentage is the part of your account you plan to risk on this one trade.** For example, 0.5% of 10,000 is 50. The example is educational, not a recommended risk level.

<div class="foundation-lab" id="position-calculator" aria-label="Gold and forex position risk calculator">
  <header>
    <div><small>Position size calculator</small><strong>How much would this trade risk?</strong></div>
    <span>Gold + major currency pairs</span>
  </header>
  <p class="calculator-intro">Choose a market. Set your risk. See the estimated lot size.</p>
  <div class="calc-grid">
    <label>What are you trading?<select id="instrument"><optgroup label="Gold"><option value="XAUUSD">XAUUSD - Gold</option></optgroup><optgroup label="Major currency pairs"><option>EURUSD</option><option>GBPUSD</option><option>USDJPY</option><option>USDCHF</option><option>USDCAD</option><option>AUDUSD</option><option>NZDUSD</option></optgroup><optgroup label="Currency crosses"><option>GBPJPY</option><option>EURGBP</option><option>GBPNZD</option></optgroup></select></label>
    <label>Account currency<select id="accountCurrency"><option>USD</option><option>EUR</option><option>GBP</option><option>PLN</option><option>JPY</option><option>AUD</option><option>CAD</option><option>CHF</option><option>NZD</option></select></label>
    <label>Account size (<span data-account-unit>USD</span>)<input id="accountSize" type="number" min="0" step="any" value="10000" aria-describedby="riskStatus"></label>
    <label>Risk per trade (%)<input id="riskPercent" type="number" min="0" max="100" step="any" value="0.5" aria-describedby="riskStatus"></label>
    <label>Direction<select id="direction"><option value="buy">Buy / long</option><option value="sell">Sell / short</option></select></label>
    <label>Entry price<input id="entryPrice" type="number" min="0" step="any" value="4500" aria-describedby="riskStatus"></label>
    <label>Stop price<input id="stopPrice" type="number" min="0" step="any" value="4490" aria-describedby="riskStatus"></label>
  </div>
  <div class="calc-example"><button type="button" id="loadExample">Load example</button><span>Example prices only. Replace them with your own plan.</span></div>
  <p id="riskStatus" class="calc-status" role="status" aria-live="polite">Complete the fields to estimate size.</p>
  <div class="calc-output" aria-live="polite">
    <div><small>Estimated lot</small><strong id="estimatedLot">—</strong></div>
    <div><small>Estimated loss at stop</small><strong id="estimatedRisk">—</strong></div>
    <div><small>Your risk budget</small><strong id="riskBudget">—</strong></div>
    <div><small>Entry-to-stop distance</small><strong id="stopDistance">—</strong></div>
  </div>
  <p id="assumptions" class="calc-detail"></p>
  <p id="conversionNote" class="calc-detail" aria-live="polite"></p>
  <button type="button" id="retryRate" hidden>Retry conversion rate</button>
  <details class="broker-details"><summary>Broker details / advanced</summary>
    <p>Standard forex lots assume 100,000 units; gold assumes 100 troy ounces. If your broker differs, use its tick size and loss tick value for one lot in your account currency. Switching market or account currency resets this override.</p>
    <label class="broker-toggle"><input type="checkbox" id="brokerOverride"> Use my broker's tick value</label>
    <div class="calc-grid">
      <label>Tick size<input id="tickSize" type="number" min="0" step="any" value="0.01" disabled aria-describedby="riskStatus"></label>
      <label>Loss tick value at 1 lot (<span data-account-unit>USD</span>)<input id="tickValue" type="number" min="0" step="any" value="" disabled aria-describedby="riskStatus"></label>
      <label>Broker lot step<input id="lotStep" type="number" min="0" step="any" value="0.01" aria-describedby="riskStatus"></label>
      <label>Broker minimum lot<input id="minLot" type="number" min="0" step="any" value="0.01" aria-describedby="riskStatus"></label>
      <label>Broker maximum lot<input id="maxLot" type="number" min="0" step="any" value="100" aria-describedby="riskStatus"></label>
    </div>
  </details>
  <p class="notice">Estimate before commission, swap and slippage. Reference conversions are daily, not live broker rates. Confirm the projected loss and volume limits in MT5. This does not check margin or funded-account rules. <a href="https://frankfurter.dev/">Reference rate source: Frankfurter</a>.</p>
  <noscript><p>Enable JavaScript to use the calculator. No estimate has been calculated.</p></noscript>
</div>

## 4. Entry, stop loss, and take profit

- **Entry** is the price where the position opens.
- **Stop loss (SL)** is the broker-side exit intended to cap the loss if the idea is wrong.
- **Take profit (TP)** is a broker-side exit at a planned favorable price.
- **Invalidation** is the market condition that makes the setup thesis no longer valid. It should be written before entry.
- **R** is the original planned risk. A `2R` target is twice the entry-to-stop distance.

A stop is not guaranteed to fill at its exact price during gaps or extreme volatility. Slippage is possible. That is another reason to learn on demo before using real or evaluation capital.

## 5. Your first MT5 demo checklist

<ul class="micro-check">
  <li>Confirm you are logged into a demo account.</li>
  <li>Open the exact gold symbol's Specification window.</li>
  <li>Write entry, stop, target, and maximum dollar loss.</li>
  <li>Check lot size against tick value and stop distance.</li>
  <li>Confirm the order has a visible broker-side SL.</li>
  <li>After closing, find the trade in the History tab.</li>
</ul>

## Where to go next

You now know the order mechanics. The next layer is **context**: what the H1 chart is doing before an M15 setup appears. Continue to [H1 Bias Before M15 Execution]({{ '/learn/tracks/read-structure/h1-bias-before-m15/' | relative_url }}).

If a term still feels unclear, do not trade around it. Write it down and ask in the community. Understanding the risk comes before trying to earn the reward.

## Using the same mechanics for currencies

For a pair such as GBPUSD, the quote is US dollars per pound. For GBPJPY, it is yen per pound. A commonly used pip is `0.0001` for GBPUSD and `0.01` for GBPJPY; the broker's point and tick size may be smaller. Never carry gold's tick value across to a currency pair.

Check scheduled events for **both currencies**, and write down the session and timezone. Several trades sharing GBP can rise or fall together, so count their combined exposure before adding another position.

[Check the Gold & FX Event Calendar]({{ '/#event-calendar' | relative_url }}) before planning a session. Then use the [pre-trade journal]({{ '/learn/tracks/master-the-mind/pre-trade-journal/' | relative_url }}) to record the idea, its invalidation, and the result, including skipped trades.

Sources: [MetaQuotes symbol properties](https://www.mql5.com/en/docs/constants/environment_state/marketinfoconstants) and [OrderCalcProfit](https://www.mql5.com/en/docs/trading/ordercalcprofit).
