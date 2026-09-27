"""Assembles the self-contained review prototype from the generated SVGs."""
from html import escape

CSS = r"""
:root{
  /* Map onto the site's existing tokens; hex values are fallbacks only. */
  --rl-ground: var(--bg, #08090D);
  --rl-panel: var(--surf, #12151E);
  --rl-line: #303744;
  --rl-text: var(--ink, #F3F2EC);
  --rl-muted: #AEB4BF;
  --rl-gold: var(--gold, #E9C97A);
  --rl-aqua: var(--aqua, #3FE0C5);
  --rl-rust: #E0683F;
  --rl-rust-text: #F09978;
  --rl-candle-up: #8E958F; --rl-candle-dn: #8E958F;
}
*{box-sizing:border-box}
html{background:var(--rl-ground);color-scheme:dark}
body{margin:0;background:var(--rl-ground);color:var(--rl-text);
  font:15px/1.55 ui-sans-serif,system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;-webkit-text-size-adjust:100%}
.wrap{max-width:720px;margin:0 auto;padding:28px 16px 64px}
header.top h1{font-size:22px;line-height:1.25;margin:0 0 6px;font-weight:650;letter-spacing:-.01em}
header.top p{margin:0 0 14px;color:var(--rl-muted)}
.grammar{display:grid;grid-template-columns:1fr 1fr;gap:6px 14px;padding:12px 14px;border:1px solid var(--rl-line);
  border-radius:8px;background:var(--rl-panel);font-size:13px;margin:0 0 8px}
.grammar span{display:flex;align-items:center;gap:8px}
.sw{width:18px;height:0;border-top:2px solid;flex:none}
.sw.g{border-color:var(--rl-gold)} .sw.a{border-color:var(--rl-aqua)} .sw.r{border-color:var(--rl-rust)}
.sw.d{border-color:var(--rl-muted);border-top-style:dashed}
nav.toc{font-size:13px;margin:14px 0 8px;display:flex;flex-wrap:wrap;gap:6px}
nav.toc a{color:var(--rl-text);text-decoration:none;border:1px solid var(--rl-line);border-radius:999px;padding:3px 10px}
nav.toc a:hover,nav.toc a:focus-visible{border-color:var(--rl-gold)}
section.lesson{margin-top:44px;scroll-margin-top:16px}
.eyebrow{font:600 11.5px/1 ui-monospace,Menlo,Consolas,monospace;letter-spacing:.08em;color:var(--rl-gold);text-transform:uppercase}
section h2{font-size:19px;line-height:1.3;margin:6px 0 12px;font-weight:650}
section h2 a{color:inherit;text-decoration-color:var(--rl-line);text-underline-offset:3px}
figure.rlv{margin:0;border:1px solid var(--rl-line);border-radius:10px;overflow:hidden;background:var(--rl-ground)}
.stage{max-width:520px;margin:0 auto}
.stage svg{display:block;width:100%;height:auto}
.rlv-svg .st{transition:opacity .45s ease}
.rlv-svg .st.off{opacity:0}
.rlv-svg .st.past{opacity:.42}
.controls{display:flex;align-items:center;gap:8px;flex-wrap:wrap;padding:10px 12px;border-top:1px solid var(--rl-line);background:var(--rl-panel)}
.controls button{font:600 13px/1 inherit;font-family:inherit;color:var(--rl-text);background:transparent;border:1px solid var(--rl-line);
  border-radius:6px;padding:9px 12px;min-height:40px;cursor:pointer}
.controls button:hover,.controls button:focus-visible{border-color:var(--rl-gold);outline:none}
.controls button[aria-pressed="true"]{border-color:var(--rl-gold)}
.controls .count{font:12px ui-monospace,Menlo,monospace;color:var(--rl-muted);margin-left:auto}
ol.steps{margin:0;padding:12px 14px 14px 34px;background:var(--rl-panel);border-top:1px solid var(--rl-line);font-size:14px}
ol.steps li{margin:3px 0;color:var(--rl-muted)}
ol.steps li.now{color:var(--rl-text)}
ol.steps li.now::marker{color:var(--rl-gold)}
.why{margin:14px 0 0;font-size:14px;color:var(--rl-muted)}
.why b{color:var(--rl-text);font-weight:600}
footer{margin-top:52px;font-size:13px;color:var(--rl-muted);border-top:1px solid var(--rl-line);padding-top:14px}
@media (prefers-reduced-motion: reduce){ .rlv-svg .st{transition:none} }
@media (max-width:420px){ .grammar{grid-template-columns:1fr} }
"""

JS = r"""
(function(){
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  document.querySelectorAll('figure.rlv').forEach(function(fig){
    var svg = fig.querySelector('svg'); var n = +svg.getAttribute('data-steps');
    var groups = svg.querySelectorAll('.st'); var items = fig.querySelectorAll('ol.steps li');
    var cur = n, timer = null;
    var bar = document.createElement('div'); bar.className = 'controls';
    bar.innerHTML = '<button type="button" data-a="play"></button>' +
      '<button type="button" data-a="prev" aria-label="Previous step">‹ Prev</button>' +
      '<button type="button" data-a="next" aria-label="Next step">Next ›</button>' +
      '<span class="count" aria-live="polite"></span>';
    fig.insertBefore(bar, fig.querySelector('ol.steps'));
    var play = bar.querySelector('[data-a=play]'), count = bar.querySelector('.count');
    play.textContent = reduce ? 'Step through' : 'Replay (6s)';
    function set(k){
      cur = Math.max(1, Math.min(n, k));
      groups.forEach(function(g){
        var s = +g.getAttribute('data-s');
        g.classList.toggle('off', s > cur);
        g.classList.toggle('past', cur < n && s < cur);
      });
      items.forEach(function(li,i){ li.classList.toggle('now', i+1 === cur); });
      count.textContent = cur === n ? 'Final frame · ' + n + '/' + n : 'Step ' + cur + '/' + n + ': ' + items[cur-1].textContent;
    }
    function stop(){ if(timer){ clearInterval(timer); timer = null; } }
    play.addEventListener('click', function(){
      stop(); set(1);
      if (reduce) return;                     // reduced motion: manual stepping only, no transitions
      timer = setInterval(function(){ if (cur >= n) { stop(); return; } set(cur + 1); }, 1600);
    });
    bar.querySelector('[data-a=prev]').addEventListener('click', function(){ stop(); set(cur - 1); });
    bar.querySelector('[data-a=next]').addEventListener('click', function(){ stop(); set(cur + 1); });
    set(n);                                   // always start on the finished static frame
  });
})();
"""

def build(diagrams, out):
    toc = "".join(f'<a href="#{k}">{lid}</a>' for k, lid, *_ in diagrams)
    secs = []
    for key, lid, title, url, svg, caps, why in diagrams:
        svg_inline = svg.replace('<svg xmlns="http://www.w3.org/2000/svg" ', '<svg ')
        lis = "".join(f"<li>{escape(c)}</li>" for c in caps)
        secs.append(f"""
<section class="lesson" id="{key}" aria-labelledby="{key}-h">
  <div class="eyebrow">{lid} · published lesson</div>
  <h2 id="{key}-h"><a href="https://refined.automationssaas.com{url}">{escape(title)}</a></h2>
  <figure class="rlv">
    <div class="stage">{svg_inline}</div>
    <ol class="steps">{lis}</ol>
  </figure>
  <p class="why"><b>Teaching rationale (for review, not learner copy).</b> {escape(why)}</p>
</section>""")
    html = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Refined Lesson Visuals</title>
<meta name="description" content="Five glance-first diagrams for the Refined Liquidity published lessons. Review prototype for Codex.">
<style>{CSS}</style></head>
<body><div class="wrap">
<header class="top">
  <h1>Beginner visual sequences — five published lessons</h1>
  <p>Review prototype for Codex. Each diagram opens on its finished static frame; Replay runs a 6-second build that stops on the same frame. All charts are synthetic teaching schematics — structural labels, no prices, no calls.</p>
  <div class="grammar" role="list" aria-label="Visual grammar">
    <span role="listitem"><i class="sw g"></i>Gold — reference / context</span>
    <span role="listitem"><i class="sw a"></i>Aqua — confirmed observation</span>
    <span role="listitem"><i class="sw r"></i>Rust — invalidation / risk</span>
    <span role="listitem"><i class="sw d"></i>Dashed grey — possible, not observed</span>
  </div>
  <nav class="toc" aria-label="Lessons">{toc}</nav>
</header>
{''.join(secs)}
<footer>Educational schematics only. Not financial advice. A setup is research until the MT5 EA confirms execution. Session and daylight-saving dates are for 2026 and must be regenerated annually.</footer>
</div><script>{JS}</script></body></html>"""
    (out / "refined-lesson-visuals.html").write_text(html, encoding="utf-8")
