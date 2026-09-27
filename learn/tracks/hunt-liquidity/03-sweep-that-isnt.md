---
permalink: /learn/tracks/hunt-liquidity/sweep-that-isnt/
title: "The Sweep That Isn't: Wick, Close, Follow-Through"
content_id: RL-LIQ-03
track: hunt-liquidity
position: 3
level: Intermediate
reading_time: 9
last_reviewed: 2026-08-16
status: public
prerequisites: []
previous_title: "What a Sweep Does Not Prove"
previous_url: "/learn/tracks/hunt-liquidity/what-a-sweep-does-not-prove/"
next_title: "When the London Window Matters"
next_url: "/learn/tracks/time-the-killzone/when-london-matters/"
---
# The Sweep That Isn't: Wick, Close, Follow-Through

**Learning objective.** By the end of this lesson you will be able to apply a three-part qualitative test to any candidate liquidity sweep on XAUUSD, and — more importantly — say which specific part failed when one fails.

**Prerequisite.** Hunt Liquidity lessons 1 and 2, plus structure labelling from Read Structure. The recap below covers the minimum.

---
<section class="learning-lab" id="animSweep">
  <div class="lab-h">
    <p class="kick">Diagram · Animation <span class="src">motion that teaches</span></p>
    <h2>A sweep, forming</h2>
    <p>The shape builds in three beats: price reaches beyond the level, closes back below, then something follows. Press replay to watch it again.</p>
  </div>
  <div class="lab-body">
    <div class="stage"><svg id="SWsvg" viewBox="0 0 520 240" role="img" aria-label="Animated candle reaching above EQH1 then closing back below, with follow-through"><line opacity="0.9" stroke-dasharray="6 5" stroke-width="1.4" stroke="#E9C97A" y2="82.16000000000001" x2="504" y1="82.16000000000001" x1="30" /><text font-size="12" font-family="IBM Plex Mono,monospace" fill="#F4E3B0" text-anchor="end" y="76.16000000000001" x="504">EQH1</text><line stroke-width="1.6" stroke="#C9CCD4" y2="161.12" x2="180" y1="44.56" x1="180" /><rect stroke-width="1.6" stroke="#C9CCD4" fill="#12151E" rx="1.5" height="1.5" width="26" y="149.84" x="167" /><line stroke-linecap="round" stroke-width="3.4" stroke="#E9C97A" y2="44.56" x2="180" y1="82.16000000000001" x1="180" /><circle fill="#F4E3B0" r="3.4" cy="44.56" cx="180" /><line stroke-width="2.4" stroke="#3FE0C5" y2="149.84" x2="198" y1="149.84" x1="162" /><g opacity="1"><line stroke-width="1.4" stroke="#878D9C" y2="187.44" x2="252" y1="149.84" x1="252" /><rect stroke="#878D9C" fill="#878D9C" rx="1.5" height="22.560000000000002" width="22" y="157.36" x="241" /></g><g opacity="1"><line stroke-width="1.4" stroke="#878D9C" y2="210" x2="314" y1="176.16" x1="314" /><rect stroke="#878D9C" fill="#878D9C" rx="1.5" height="22.559999999999974" width="22" y="179.92000000000002" x="303" /></g><line opacity="0.85" stroke-dasharray="2 4" stroke-width="2" stroke="#3FE0C5" y2="202.48" x2="322" y1="149.84" x1="198" /></svg></div>
    <div class="playrow"><button type="button" class="btn" id="SWplay">▶ Replay</button><span class="caption" id="SWcap">reached beyond · closed back below · followed through</span></div>
  </div>
<details class="static-readings"><summary>Read the observations and failure states</summary><p>The still frame shows a completed shape. A wick that never reaches beyond EQH1 is not a sweep; a close above it is a breakout; no follow-through means setup expiry. Explore all four cases in the sweep lab below.</p></details></section>

<section class="learning-lab" id="labA">
  <div class="lab-h">
    <p class="kick">Lab A · Liquidity sweep <span class="src">RL-LIQ-03</span></p>
    <h2>Wick, close, follow-through</h2>
    <p>Step through the three parts. Then switch candidate — three of the four <em>fail</em> a different part, and the failures are the lesson.</p>
  </div>
  <div class="lab-body">
    <div class="controls">
      <span class="clabel">Candidate</span>
      <div class="seg" id="Acand" role="group" aria-label="Candidate">
        <button type="button" data-c="A" aria-pressed="true">A · passes</button>
        <button type="button" data-c="B" aria-pressed="false">B · fails wick</button>
        <button type="button" data-c="C" aria-pressed="false">C · fails close</button>
        <button type="button" data-c="D" aria-pressed="false">D · fails follow</button>
      </div>
    </div>
    <div class="stage"><svg id="Asvg" viewBox="0 0 660 320" role="img" aria-label="Schematic candles testing a sweep of level EQH1"><line opacity="0.9" stroke-dasharray="6 5" stroke-width="1.4" stroke="#E9C97A" y2="119" x2="644" y1="119" x1="40" /><text font-size="12" font-family="IBM Plex Mono,monospace" fill="#F4E3B0" text-anchor="end" y="113" x="644">EQH1</text><line stroke-width="1.4" stroke="#C9CCD4" y2="233" x2="73.55555555555556" y1="185.5" x1="73.55555555555556" /><rect stroke-width="1.4" stroke="#C9CCD4" fill="#C9CCD4" rx="1.5" height="9.5" width="26" y="214" x="60.55555555555556" /><line stroke-width="1.4" stroke="#C9CCD4" y2="237.75" x2="140.66666666666669" y1="199.75" x1="140.66666666666669" /><rect stroke-width="1.4" stroke="#C9CCD4" fill="#12151E" rx="1.5" height="19" width="26" y="204.5" x="127.66666666666669" /><line stroke-width="1.4" stroke="#C9CCD4" y2="214" x2="207.77777777777777" y1="176" x1="207.77777777777777" /><rect stroke-width="1.4" stroke="#C9CCD4" fill="#C9CCD4" rx="1.5" height="4.75" width="26" y="204.5" x="194.77777777777777" /><line stroke-width="1.4" stroke="#C9CCD4" y2="218.75" x2="274.8888888888889" y1="161.75" x1="274.8888888888889" /><rect stroke-width="1.4" stroke="#C9CCD4" fill="#12151E" rx="1.5" height="23.75" width="26" y="185.5" x="261.8888888888889" /><line stroke-width="1.4" stroke="#C9CCD4" y2="195" x2="342" y1="152.25" x1="342" /><rect stroke-width="1.4" stroke="#C9CCD4" fill="#12151E" rx="1.5" height="14.25" width="26" y="171.25" x="329" /><line stroke-width="1.4" stroke="#C9CCD4" y2="180.75" x2="409.11111111111114" y1="81" x1="409.11111111111114" /><rect stroke-width="1.4" stroke="#C9CCD4" fill="#12151E" rx="1.5" height="14.25" width="26" y="157" x="396.11111111111114" /><line stroke-linecap="round" stroke-width="3.4" stroke="#E9C97A" y2="81" x2="409.11111111111114" y1="119" x1="409.11111111111114" /><circle fill="#F4E3B0" r="3.4" cy="81" cx="409.11111111111114" /><line stroke-width="2.2" stroke="#3FE0C5" y2="157" x2="426.11111111111114" y1="157" x1="392.11111111111114" /><line stroke-width="1.4" stroke="#878D9C" y2="195" x2="476.22222222222223" y1="152.25" x1="476.22222222222223" /><rect stroke-width="1.4" stroke="#878D9C" fill="#878D9C" rx="1.5" height="33.25" width="26" y="157" x="463.22222222222223" /><line stroke-width="1.4" stroke="#878D9C" y2="233" x2="543.3333333333334" y1="185.5" x1="543.3333333333334" /><rect stroke-width="1.4" stroke="#878D9C" fill="#878D9C" rx="1.5" height="38" width="26" y="190.25" x="530.3333333333334" /><line stroke-width="1.4" stroke="#878D9C" y2="266.25" x2="610.4444444444445" y1="223.5" x1="610.4444444444445" /><rect stroke-width="1.4" stroke="#878D9C" fill="#878D9C" rx="1.5" height="28.5" width="26" y="228.25" x="597.4444444444445" /><line opacity="0.85" stroke-dasharray="2 4" stroke-width="2" stroke="#3FE0C5" y2="256.75" x2="610.4444444444445" y1="157" x1="476.22222222222223" /></svg></div>
    <div class="controls">
      <span class="clabel">Reveal</span>
      <div class="seg aq" id="Astep" role="group" aria-label="Step">
        <button type="button" data-s="1" aria-pressed="false">1 · wick</button>
        <button type="button" data-s="2" aria-pressed="false">2 · close</button>
        <button type="button" data-s="3" aria-pressed="true">3 · follow-through</button>
      </div>
    </div>
    <div class="verdict">
      <div class="parts" id="Aparts">
        <span class="part" data-p="wick" data-s="pass"><b>Wick</b> <em id="Awv">reached beyond</em></span>
        <span class="part" data-p="close" data-s="pass"><b>Close</b> <em id="Acv">closed back below</em></span>
        <span class="part" data-p="follow" data-s="pass"><b>Follow-through</b> <em id="Afv">moved away</em></span>
      </div>
      <p aria-live="polite" role="status" class="vtext" id="Averdict"><span class="tag pass">Passes all three</span>Wick beyond <span class="mono">EQH1</span>, close back below, and price moved down and away. A complete three-part observation — which is not the same as a guarantee.</p>
    </div>
    <p class="honest"><b>No entry rule here.</b> The test is qualitative on purpose — no candle counts, no timing constants. What transfers is the reasoning behind each part, not a number that would be wrong on your feed anyway.</p>
  </div>
<details class="static-readings"><summary>Read the observations and failure states</summary><h3>Candidate A</h3><svg viewBox="0 0 660 320" role="img" aria-label="Schematic candles testing a sweep of level EQH1"><line opacity="0.9" stroke-dasharray="6 5" stroke-width="1.4" stroke="#E9C97A" y2="119" x2="644" y1="119" x1="40" /><text font-size="12" font-family="IBM Plex Mono,monospace" fill="#F4E3B0" text-anchor="end" y="113" x="644">EQH1</text><line stroke-width="1.4" stroke="#C9CCD4" y2="233" x2="73.55555555555556" y1="185.5" x1="73.55555555555556" /><rect stroke-width="1.4" stroke="#C9CCD4" fill="#C9CCD4" rx="1.5" height="9.5" width="26" y="214" x="60.55555555555556" /><line stroke-width="1.4" stroke="#C9CCD4" y2="237.75" x2="140.66666666666669" y1="199.75" x1="140.66666666666669" /><rect stroke-width="1.4" stroke="#C9CCD4" fill="#12151E" rx="1.5" height="19" width="26" y="204.5" x="127.66666666666669" /><line stroke-width="1.4" stroke="#C9CCD4" y2="214" x2="207.77777777777777" y1="176" x1="207.77777777777777" /><rect stroke-width="1.4" stroke="#C9CCD4" fill="#C9CCD4" rx="1.5" height="4.75" width="26" y="204.5" x="194.77777777777777" /><line stroke-width="1.4" stroke="#C9CCD4" y2="218.75" x2="274.8888888888889" y1="161.75" x1="274.8888888888889" /><rect stroke-width="1.4" stroke="#C9CCD4" fill="#12151E" rx="1.5" height="23.75" width="26" y="185.5" x="261.8888888888889" /><line stroke-width="1.4" stroke="#C9CCD4" y2="195" x2="342" y1="152.25" x1="342" /><rect stroke-width="1.4" stroke="#C9CCD4" fill="#12151E" rx="1.5" height="14.25" width="26" y="171.25" x="329" /><line stroke-width="1.4" stroke="#C9CCD4" y2="180.75" x2="409.11111111111114" y1="81" x1="409.11111111111114" /><rect stroke-width="1.4" stroke="#C9CCD4" fill="#12151E" rx="1.5" height="14.25" width="26" y="157" x="396.11111111111114" /><line stroke-linecap="round" stroke-width="3.4" stroke="#E9C97A" y2="81" x2="409.11111111111114" y1="119" x1="409.11111111111114" /><circle fill="#F4E3B0" r="3.4" cy="81" cx="409.11111111111114" /><line stroke-width="2.2" stroke="#3FE0C5" y2="157" x2="426.11111111111114" y1="157" x1="392.11111111111114" /><line stroke-width="1.4" stroke="#878D9C" y2="195" x2="476.22222222222223" y1="152.25" x1="476.22222222222223" /><rect stroke-width="1.4" stroke="#878D9C" fill="#878D9C" rx="1.5" height="33.25" width="26" y="157" x="463.22222222222223" /><line stroke-width="1.4" stroke="#878D9C" y2="233" x2="543.3333333333334" y1="185.5" x1="543.3333333333334" /><rect stroke-width="1.4" stroke="#878D9C" fill="#878D9C" rx="1.5" height="38" width="26" y="190.25" x="530.3333333333334" /><line stroke-width="1.4" stroke="#878D9C" y2="266.25" x2="610.4444444444445" y1="223.5" x1="610.4444444444445" /><rect stroke-width="1.4" stroke="#878D9C" fill="#878D9C" rx="1.5" height="28.5" width="26" y="228.25" x="597.4444444444445" /><line opacity="0.85" stroke-dasharray="2 4" stroke-width="2" stroke="#3FE0C5" y2="256.75" x2="610.4444444444445" y1="157" x1="476.22222222222223" /></svg><p><span class="tag pass">Passes all three</span>Wick beyond <span class="mono">EQH1</span>, close back below, and price moved down and away. A complete three-part observation — which is not the same as a guarantee.</p><h3>Candidate B</h3><svg viewBox="0 0 660 320" role="img" aria-label="Schematic candles testing a sweep of level EQH1"><line opacity="0.9" stroke-dasharray="6 5" stroke-width="1.4" stroke="#E9C97A" y2="119" x2="644" y1="119" x1="40" /><text font-size="12" font-family="IBM Plex Mono,monospace" fill="#F4E3B0" text-anchor="end" y="113" x="644">EQH1</text><line stroke-width="1.4" stroke="#C9CCD4" y2="233" x2="73.55555555555556" y1="185.5" x1="73.55555555555556" /><rect stroke-width="1.4" stroke="#C9CCD4" fill="#C9CCD4" rx="1.5" height="9.5" width="26" y="214" x="60.55555555555556" /><line stroke-width="1.4" stroke="#C9CCD4" y2="237.75" x2="140.66666666666669" y1="199.75" x1="140.66666666666669" /><rect stroke-width="1.4" stroke="#C9CCD4" fill="#12151E" rx="1.5" height="19" width="26" y="204.5" x="127.66666666666669" /><line stroke-width="1.4" stroke="#C9CCD4" y2="214" x2="207.77777777777777" y1="176" x1="207.77777777777777" /><rect stroke-width="1.4" stroke="#C9CCD4" fill="#C9CCD4" rx="1.5" height="4.75" width="26" y="204.5" x="194.77777777777777" /><line stroke-width="1.4" stroke="#C9CCD4" y2="218.75" x2="274.8888888888889" y1="161.75" x1="274.8888888888889" /><rect stroke-width="1.4" stroke="#C9CCD4" fill="#12151E" rx="1.5" height="23.75" width="26" y="185.5" x="261.8888888888889" /><line stroke-width="1.4" stroke="#C9CCD4" y2="195" x2="342" y1="152.25" x1="342" /><rect stroke-width="1.4" stroke="#C9CCD4" fill="#12151E" rx="1.5" height="14.25" width="26" y="171.25" x="329" /><line stroke-width="1.4" stroke="#C9CCD4" y2="180.75" x2="409.11111111111114" y1="128.5" x1="409.11111111111114" /><rect stroke-width="1.4" stroke="#C9CCD4" fill="#12151E" rx="1.5" height="14.25" width="26" y="157" x="396.11111111111114" /><line stroke-width="2.2" stroke="#3FE0C5" y2="157" x2="426.11111111111114" y1="157" x1="392.11111111111114" /><line stroke-width="1.4" stroke="#878D9C" y2="195" x2="476.22222222222223" y1="152.25" x1="476.22222222222223" /><rect stroke-width="1.4" stroke="#878D9C" fill="#878D9C" rx="1.5" height="33.25" width="26" y="157" x="463.22222222222223" /><line stroke-width="1.4" stroke="#878D9C" y2="233" x2="543.3333333333334" y1="185.5" x1="543.3333333333334" /><rect stroke-width="1.4" stroke="#878D9C" fill="#878D9C" rx="1.5" height="38" width="26" y="190.25" x="530.3333333333334" /><line stroke-width="1.4" stroke="#878D9C" y2="266.25" x2="610.4444444444445" y1="223.5" x1="610.4444444444445" /><rect stroke-width="1.4" stroke="#878D9C" fill="#878D9C" rx="1.5" height="28.5" width="26" y="228.25" x="597.4444444444445" /></svg><p><span class="tag fail">Fails part 1 — the wick</span>The rejection looks <em>better</em> than A’s — and price never touched the orders above <span class="mono">EQH1</span>. The most seductive failure of the four: the prettiest candle is the one that isn’t a sweep at all.</p><h3>Candidate C</h3><svg viewBox="0 0 660 320" role="img" aria-label="Schematic candles testing a sweep of level EQH1"><line opacity="0.9" stroke-dasharray="6 5" stroke-width="1.4" stroke="#E9C97A" y2="119" x2="644" y1="119" x1="40" /><text font-size="12" font-family="IBM Plex Mono,monospace" fill="#F4E3B0" text-anchor="end" y="113" x="644">EQH1</text><line stroke-width="1.4" stroke="#C9CCD4" y2="233" x2="73.55555555555556" y1="185.5" x1="73.55555555555556" /><rect stroke-width="1.4" stroke="#C9CCD4" fill="#C9CCD4" rx="1.5" height="9.5" width="26" y="214" x="60.55555555555556" /><line stroke-width="1.4" stroke="#C9CCD4" y2="237.75" x2="140.66666666666669" y1="199.75" x1="140.66666666666669" /><rect stroke-width="1.4" stroke="#C9CCD4" fill="#12151E" rx="1.5" height="19" width="26" y="204.5" x="127.66666666666669" /><line stroke-width="1.4" stroke="#C9CCD4" y2="214" x2="207.77777777777777" y1="176" x1="207.77777777777777" /><rect stroke-width="1.4" stroke="#C9CCD4" fill="#C9CCD4" rx="1.5" height="4.75" width="26" y="204.5" x="194.77777777777777" /><line stroke-width="1.4" stroke="#C9CCD4" y2="218.75" x2="274.8888888888889" y1="161.75" x1="274.8888888888889" /><rect stroke-width="1.4" stroke="#C9CCD4" fill="#12151E" rx="1.5" height="23.75" width="26" y="185.5" x="261.8888888888889" /><line stroke-width="1.4" stroke="#C9CCD4" y2="195" x2="342" y1="152.25" x1="342" /><rect stroke-width="1.4" stroke="#C9CCD4" fill="#12151E" rx="1.5" height="14.25" width="26" y="171.25" x="329" /><line stroke-width="1.4" stroke="#C9CCD4" y2="176" x2="409.11111111111114" y1="71.5" x1="409.11111111111114" /><rect stroke-width="1.4" stroke="#C9CCD4" fill="#12151E" rx="1.5" height="76" width="26" y="95.25" x="396.11111111111114" /><line stroke-linecap="round" stroke-width="3.4" stroke="#E9C97A" y2="71.5" x2="409.11111111111114" y1="119" x1="409.11111111111114" /><circle fill="#F4E3B0" r="3.4" cy="71.5" cx="409.11111111111114" /><line stroke-width="2.2" stroke="#E0683F" y2="95.25" x2="426.11111111111114" y1="95.25" x1="392.11111111111114" /><line stroke-width="1.4" stroke="#878D9C" y2="100" x2="476.22222222222223" y1="62" x1="476.22222222222223" /><rect stroke-width="1.4" stroke="#878D9C" fill="#12151E" rx="1.5" height="23.75" width="26" y="71.5" x="463.22222222222223" /><line stroke-width="1.4" stroke="#878D9C" y2="81" x2="543.3333333333334" y1="47.75" x1="543.3333333333334" /><rect stroke-width="1.4" stroke="#878D9C" fill="#12151E" rx="1.5" height="14.25" width="26" y="57.25" x="530.3333333333334" /><line stroke-width="1.4" stroke="#878D9C" y2="71.5" x2="610.4444444444445" y1="43" x1="610.4444444444445" /><rect stroke-width="1.4" stroke="#878D9C" fill="#12151E" rx="1.5" height="4.75" width="26" y="52.5" x="597.4444444444445" /><line opacity="0.85" stroke-dasharray="2 4" stroke-width="2" stroke="#E0683F" y2="52.5" x2="610.4444444444445" y1="95.25" x1="476.22222222222223" /></svg><p><span class="tag fail">Fails part 2 — the close</span>Price closed <em>above</em> the level. Read forwards, at the time, this is a breakout — a different event. Calling it a failed sweep later, once it came back, is the backwards reasoning the test exists to prevent.</p><h3>Candidate D</h3><svg viewBox="0 0 660 320" role="img" aria-label="Schematic candles testing a sweep of level EQH1"><line opacity="0.9" stroke-dasharray="6 5" stroke-width="1.4" stroke="#E9C97A" y2="119" x2="644" y1="119" x1="40" /><text font-size="12" font-family="IBM Plex Mono,monospace" fill="#F4E3B0" text-anchor="end" y="113" x="644">EQH1</text><line stroke-width="1.4" stroke="#C9CCD4" y2="233" x2="73.55555555555556" y1="185.5" x1="73.55555555555556" /><rect stroke-width="1.4" stroke="#C9CCD4" fill="#C9CCD4" rx="1.5" height="9.5" width="26" y="214" x="60.55555555555556" /><line stroke-width="1.4" stroke="#C9CCD4" y2="237.75" x2="140.66666666666669" y1="199.75" x1="140.66666666666669" /><rect stroke-width="1.4" stroke="#C9CCD4" fill="#12151E" rx="1.5" height="19" width="26" y="204.5" x="127.66666666666669" /><line stroke-width="1.4" stroke="#C9CCD4" y2="214" x2="207.77777777777777" y1="176" x1="207.77777777777777" /><rect stroke-width="1.4" stroke="#C9CCD4" fill="#C9CCD4" rx="1.5" height="4.75" width="26" y="204.5" x="194.77777777777777" /><line stroke-width="1.4" stroke="#C9CCD4" y2="218.75" x2="274.8888888888889" y1="161.75" x1="274.8888888888889" /><rect stroke-width="1.4" stroke="#C9CCD4" fill="#12151E" rx="1.5" height="23.75" width="26" y="185.5" x="261.8888888888889" /><line stroke-width="1.4" stroke="#C9CCD4" y2="195" x2="342" y1="152.25" x1="342" /><rect stroke-width="1.4" stroke="#C9CCD4" fill="#12151E" rx="1.5" height="14.25" width="26" y="171.25" x="329" /><line stroke-width="1.4" stroke="#C9CCD4" y2="180.75" x2="409.11111111111114" y1="81" x1="409.11111111111114" /><rect stroke-width="1.4" stroke="#C9CCD4" fill="#12151E" rx="1.5" height="14.25" width="26" y="157" x="396.11111111111114" /><line stroke-linecap="round" stroke-width="3.4" stroke="#E9C97A" y2="81" x2="409.11111111111114" y1="119" x1="409.11111111111114" /><circle fill="#F4E3B0" r="3.4" cy="81" cx="409.11111111111114" /><line stroke-width="2.2" stroke="#3FE0C5" y2="157" x2="426.11111111111114" y1="157" x1="392.11111111111114" /><line stroke-width="1.4" stroke="#878D9C" y2="171.25" x2="476.22222222222223" y1="142.75" x1="476.22222222222223" /><rect stroke-width="1.4" stroke="#878D9C" fill="#878D9C" rx="1.5" height="4.75" width="26" y="157" x="463.22222222222223" /><line stroke-width="1.4" stroke="#878D9C" y2="176" x2="543.3333333333334" y1="147.5" x1="543.3333333333334" /><rect stroke-width="1.4" stroke="#878D9C" fill="#878D9C" rx="1.5" height="4.75" width="26" y="161.75" x="530.3333333333334" /><line stroke-width="1.4" stroke="#878D9C" y2="176" x2="610.4444444444445" y1="152.25" x1="610.4444444444445" /><rect stroke-width="1.4" stroke="#878D9C" fill="#12151E" rx="1.5" height="9.5" width="26" y="157" x="597.4444444444445" /><line opacity="0.85" stroke-dasharray="2 4" stroke-width="2" stroke="#878D9C" y2="157" x2="610.4444444444445" y1="157" x1="476.22222222222223" /></svg><p><span class="tag expire">Fails part 3 — follow-through</span>Textbook shape — then hours of chop inside the range. The setup <b>expired</b>. Not a loss, not a missed trade, not evidence the test failed. A test that returns “nothing here” is doing its job.</p></details></section>

<section class="learning-lab" id="dtree-sec">
  <div class="lab-h">
    <p class="kick">Diagram · Decision flow <span class="src">the honest version</span></p>
    <h2>Before you act: the tree that can’t say “buy”</h2>
    <p>The popular flowchart ends in <em>BUY</em> or <em>SELL</em>. This one can’t — a chart doesn’t prove that much. Most branches end in <em>wait</em>, and that is the entire point.</p>
  </div>
  <div class="lab-body">
    <div class="dtree">
      <div class="drow">
        <div class="q">Did price trade <b>beyond</b> the level — not just near it?<span class="qk">the wick · EQH1</span></div>
        <div class="no say"><span class="rk">No</span><b>Not a sweep.</b> The orders above were never reached. Whatever happened next, this wasn’t it.</div>
      </div>
      <div class="yes">↓ yes</div>
      <div class="drow">
        <div class="q">Did the candle <b>close back below</b> it?<span class="qk">the close</span></div>
        <div class="no amber"><span class="rk">No — it closed above</span><b>A breakout.</b> A different event, read forwards. Calling it a failed sweep later is backwards reasoning.</div>
      </div>
      <div class="yes">↓ yes</div>
      <div class="drow">
        <div class="q">Did <b>anything follow</b> — movement away from the level?<span class="qk">follow-through</span></div>
        <div class="no say"><span class="rk">No — it drifted</span><b>Setup expired.</b> Not a loss, not a missed trade. A test that returns “nothing here” is doing its job.</div>
      </div>
      <div class="yes">↓ yes</div>
      <div class="endp"><b>A research setup.</b> Size for uncertainty, write the invalidation before entry, and check the session and calendar.<span class="neg">Still not a signal to buy — only a read worth acting on with care.</span></div>
    </div>
  </div>
</section>

---
## Recap: what you need from lessons 1 and 2

A **liquidity pool** is a price area where resting orders plausibly cluster. You do not need special data to locate one. Ask where you would put a stop if you were long, and you have found where most people put theirs: just beyond an obvious high or low that many traders can see.

**Equal highs** (`EQH`) form when price reaches roughly the same level twice or more and turns away each time. Equal lows (`EQL`) are the mirror. The tighter and more obvious the level, the more visible it is — and visibility is the point. A level nobody can see holds nobody's stops.

That is the entire setup for this lesson: an obvious level, with orders plausibly resting beyond it.

---
## The thing this lesson is actually about

Price reaches beyond an obvious level and comes back. Every day, on every timeframe, on every instrument.

Most of the time it means nothing.

The version taught almost everywhere goes: price sweeps liquidity, then reverses, so enter on the reversal. Stated that way it is unfalsifiable — any reach beyond a level followed by any return can be called a sweep after the fact, and any reach that keeps going gets quietly excluded as "not a real sweep." A rule that can only be applied backwards is not a rule.

So this lesson is built the other way round. Instead of asking *was that a sweep*, it asks three separate questions with three separate answers, and treats a no on any one of them as information rather than as an inconvenience.

---
## The three-part test

### Part 1 — The wick: did price actually reach beyond the level?

Not near it. Beyond it. If your level is `EQH1`, price must trade above `EQH1`.

This sounds trivial and is the most commonly fudged part of the whole test. A candle that stops two or three dollars short of an equal high on gold has not reached the orders resting above it. Nothing has been triggered. Whatever happens next is not a sweep, whatever it looks like.

There is a real complication here and it is worth stating rather than hiding: **your chart's high is not everyone's high.** The wick that just cleared `EQH1` on your MT5 broker's feed may not have cleared it on a TradingView OANDA feed, because spot gold has no central exchange and every feed is its own aggregation. Feeds can and do disagree at the extremes of a fast move, and the disagreement is largest exactly where it matters — at the wick that decides whether a level was cleared. I have not measured the typical size of that gap and will not quote one until I have. What follows regardless: if a sweep is only a sweep on one feed, treat it as marginal. That is not pedantry — it is the honest state of an instrument with no central exchange.

### Part 2 — The close: where did the candle finish?

This is what separates a sweep from a breakout, and it is the part the two share nothing but geometry.

If price reaches above `EQH1` and the candle closes back below it, the move beyond the level was not sustained. If price reaches above `EQH1` and closes above it, that is a breakout — a different event, with different implications, and calling it a failed sweep because it later came back is exactly the backwards reasoning this test exists to prevent.

Two candles can have identical highs. One closes above the level, one closes below. They are not the same event and should not produce the same reading.

**The honest part.** Which timeframe's close counts is a decision you make in advance and apply consistently. There is no universally correct answer, and any source that gives you one without telling you what it depends on is guessing. Pick a timeframe, write it in your rules, and stop re-deciding it per chart. The research system's answer to this question is not published — but the reasoning above is the whole of what makes the choice matter, and that reasoning is yours to use.

### Part 3 — The follow-through: did anything happen after?

Price cleared the level, closed back inside, and then… drifted sideways for four hours.

Nothing has been confirmed. The first two parts describe a shape. Follow-through is the only part that carries any information about whether the shape mattered — and it is the part most often skipped, because by the time you can assess it, the entry that felt obvious has already gone.

That is the trade-off, stated plainly: waiting for follow-through costs you the best price and buys you the difference between a pattern and an observation. Which side of that trade-off you sit on is a decision about your own tolerance, not a fact about markets. This lesson's only claim is that you should know which one you are choosing.

**What follow-through is not.** It is not a target, a pip count, or a promise. It is the presence of directional movement away from the level, on the timeframe you are working. Its absence is a complete answer.

{% include lesson-visual.html key="the-sweep-that-isnt" %}

---
## Worked example — XAUUSD, London session

*Schematic. Structural labels, not prices.*

**Setup.** Over the Asian session, gold prints two highs at effectively the same level. Label it `EQH1`. Price drifts below it into the London open. Structure on H1 is a sequence of lower highs — the bias is down, and `EQH1` sits above as an obvious pool.

**Candidate A — passes all three.** An M15 candle in the first London hour trades clearly above `EQH1`, then closes back below it. The following two candles move down and away, taking out the small swing low that formed before the reach. Wick: yes. Close: yes. Follow-through: yes.

**Candidate B — fails part 1.** A candle rallies to within a hair of `EQH1` and rejects hard. The rejection looks better on the chart than Candidate A's did. But the orders above `EQH1` were never reached, so the mechanism the whole idea depends on did not occur. This is the most seductive failure of the three, because the candle is more attractive than the one that passes.

**Candidate C — fails part 2.** A candle trades above `EQH1` and closes above it. Then it comes back below an hour later. Read forwards, this was a breakout that failed. Read backwards, it looks like a slow sweep. Only the forwards reading was available at the time, which is the reading that counts.

**Candidate D — fails part 3.** Wick above, close back below, textbook shape — and then six hours of chop inside the prior range. The shape was there. Nothing followed. This is not a loss if you waited; it is a setup that expired.

**Session context matters.** The same four candidates during a thin Asian session are weaker observations than during London. That is developed in Time the Killzone. Here it is enough that *when* is part of *what*.

---
## Exercise — no trade required

Take one week of XAUUSD M15 with H1 open beside it.

1. Mark every equal-high and equal-low formation you can find. Grade each one — clean or marginal.
2. Find every instance where price traded beyond a marked level.
3. For each, score the three parts as pass or fail, before looking at what happened next.
4. Then look. Record what followed.

You are counting how often each part fails, not whether you would have made money. Most people find part 3 fails far more often than they expected, and that number — your number, from your chart — is worth more than any claim in this lesson.

---
## Common failure mode

**Reclassifying after the fact.** A level is reached, you call it a sweep, price keeps going, and it becomes "a breakout, not a real sweep." The chart did not change. Your label did, after the outcome was known, which means it can never be wrong and never teach you anything.

The defence is scoring all three parts *before* the next candles arrive, and writing the score down. A record of your part-3 failures is the single most useful thing this lesson can leave you with.

**Second failure mode: marking levels to find sweeps.** If you are hunting for a setup, you will find equal highs where there are only two adjacent candles. Mark levels first, on their own merits, before you have any interest in what happens at them.

**Invalidation condition.** A candidate sweep is invalidated when price closes beyond the level in the direction of the reach, on your chosen timeframe, and holds there. At that point it is not a sweep that failed — it is a different event, and the sweep reading should be dropped rather than defended.

---
## Observation checklist

Before calling anything a sweep:

1. The level was marked before price approached it, not after.
2. Price traded *beyond* the level, not near it — checked against the feed I actually trade.
3. I know which timeframe's close I am using, and it is the same one I used last time.
4. I have scored all three parts, in writing, before the next candle closed.
5. I have noted the session, and whether scheduled news sits inside the window.

---
## Knowledge check

**1. Price rejects violently one dollar below `EQH1` and drops fifty. Was that a sweep?**

No. Part 1 failed — price never reached beyond the level, so the resting orders that give a sweep its meaning were never involved. The move may have been profitable; that is a separate question from whether it was this pattern. Conflating "it worked" with "it was the setup" is how a rule set quietly dissolves.

**2. Your feed shows the wick clearing `EQH1` by twenty cents. A friend's feed shows it stopping just short. Who is right?**

Both, and neither. Spot gold has no central exchange; each feed is its own aggregation, and they can disagree at the extremes of fast moves. Treat a sweep that exists on one feed and not another as marginal, and size accordingly. Trade the feed you execute on, and hold the level a little more loosely than the line on your chart suggests.

**3. Wick above the level, close back below, and then four hours of sideways. What is your reading?**

Parts 1 and 2 passed, part 3 did not. The correct reading is that the setup expired. It is not a loss, it is not a missed trade, and it is not evidence the test failed — a test that returns "nothing here" is doing its job. Recording it as an expiry rather than deleting it from memory is what makes the sample honest.

---
## Risk note

This lesson is educational and is not financial advice. Nothing here predicts price, and no level on any chart is under any obligation to produce a reaction.

The three-part test is deliberately qualitative in public. It contains no candle-count windows, no timing constants, and no scoring thresholds — what is taught is the reasoning behind each part, which is the portion that transfers to your chart, your broker, and your feed. A constant copied without its reasoning is worth very little anyway, and would be wrong on your feed in any case.

Gold is traded with leverage and a position can lose more than you intended to risk. Verify contract size and tick value in your own MT5 symbol specification.

A setup identified through this test is **research**. It becomes part of the public record only when the MT5 Expert Advisor confirms execution. Manual trades stay outside that record.

---

