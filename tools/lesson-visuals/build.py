#!/usr/bin/env python3
"""
Refined Liquidity — beginner visual lessons.
Generates five standalone SVG diagrams (the static final frame) and one
self-contained HTML prototype that inlines them with a replay/stepper.

Visual grammar (shared by every diagram):
  gold  (--rl-gold)  reference / context   (levels, sessions, plan fields)
  aqua  (--rl-aqua)  confirmed observation (what is on the chart / in the record)
  rust  (--rl-rust)  invalidation / risk
  grey dashed        possible, not yet observed / inferred
Every colour is paired with a text label; nothing relies on colour alone.

Run:  python3 build.py   ->  svg/*.svg  +  refined-lesson-visuals.html
"""
from pathlib import Path
from html import escape

OUT = Path(__file__).parent
(OUT / "svg").mkdir(exist_ok=True)

W = 360  # viewBox width. Designed ~1:1 at a 390px phone (16px gutters).

STYLE = """
.bg{fill:var(--rl-ground,#08090D)}
.panel{fill:var(--rl-panel,#12151E);stroke:var(--rl-line,#303744);stroke-width:1}
.grid{stroke:var(--rl-line,#303744);stroke-width:1}
.t{font-family:ui-sans-serif,system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;font-size:11px;fill:var(--rl-text,#F3F2EC)}
.m{font-family:ui-monospace,"SF Mono",Menlo,Consolas,monospace}
.h{font-size:12.5px;font-weight:650}
.k{font-size:10.5px;letter-spacing:.045em;text-transform:uppercase;font-weight:600}
.mut{fill:var(--rl-muted,#AEB4BF)}
.it{font-style:italic}
.b{font-weight:650}
.gold{fill:var(--rl-gold,#E9C97A)} .aqua{fill:var(--rl-aqua,#3FE0C5)} .rust{fill:var(--rl-rust-text,#F09978)}
.s-gold{stroke:var(--rl-gold,#E9C97A)} .s-aqua{stroke:var(--rl-aqua,#3FE0C5)} .s-rust{stroke:var(--rl-rust,#E0683F)}
.s-mut{stroke:var(--rl-muted,#AEB4BF)}
.lvl{stroke-width:1.5;fill:none}
.halo{paint-order:stroke;stroke:var(--rl-panel,#12151E);stroke-width:4px;stroke-linejoin:round}
.dash{stroke-dasharray:5 4}
.dot{stroke-dasharray:2 3}
.path{fill:none;stroke-width:1.75;stroke-linecap:round;stroke-linejoin:round}
.cu{fill:var(--rl-candle-up,#8E958F);stroke:var(--rl-candle-up,#8E958F)}
.cd{fill:var(--rl-ground,#08090D);stroke:var(--rl-candle-dn,#8E958F)}
.wk{stroke:var(--rl-candle-up,#8E958F);stroke-width:1}
.hl-aqua .cu,.hl-aqua .cd{stroke:var(--rl-aqua,#3FE0C5)} .hl-aqua .wk{stroke:var(--rl-aqua,#3FE0C5);stroke-width:1.5}
.hl-rust .cu,.hl-rust .cd{stroke:var(--rl-rust,#E0683F)} .hl-rust .wk{stroke:var(--rl-rust,#E0683F);stroke-width:1.5}
.chip-gold{fill:rgba(233,201,122,.12);stroke:var(--rl-gold,#E9C97A)}
.chip-aqua{fill:rgba(63,224,197,.10);stroke:var(--rl-aqua,#3FE0C5)}
.chip-rust{fill:rgba(224,104,63,.12);stroke:var(--rl-rust,#E0683F)}
.chip-mut{fill:rgba(174,180,191,.06);stroke:var(--rl-muted,#AEB4BF);stroke-dasharray:4 3}
.fillzone{fill:rgba(233,201,122,.07)}
.overlap{fill:url(#rl-hatch)}
"""

# ---------------------------------------------------------------- helpers
def T(x, y, s, cls="t", anchor="start", extra=""):
    """Text; s may be a list of lines (13.5px leading)."""
    lines = s if isinstance(s, list) else [s]
    a = f' text-anchor="{anchor}"' if anchor != "start" else ""
    if len(lines) == 1:
        return f'<text x="{x}" y="{y}" class="{cls}"{a}{extra}>{escape(lines[0])}</text>'
    sp = "".join(f'<tspan x="{x}" dy="{0 if i == 0 else 13.5}">{escape(ln)}</tspan>' for i, ln in enumerate(lines))
    return f'<text x="{x}" y="{y}" class="{cls}"{a}{extra}>{sp}</text>'

def L(x1, y1, x2, y2, cls):
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" class="{cls}"/>'

def R(x, y, w, h, cls, rx=4):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" class="{cls}"/>'

def P(d, cls):
    return f'<path d="{d}" class="{cls}"/>'

def G(step, body, cls=""):
    c = f"st {cls}".strip()
    return f'<g class="{c}" data-s="{step}">{body}</g>'

class Scale:
    def __init__(self, pmin, pmax, ytop, ybot):
        self.pmin, self.pmax, self.ytop, self.ybot = pmin, pmax, ytop, ybot
    def __call__(self, p):
        return round(self.ybot - (p - self.pmin) / (self.pmax - self.pmin) * (self.ybot - self.ytop), 1)

def candles(data, x0, dx, sc, w=8, hl=None):
    """data: list of (o,h,l,c). hl: {index: 'hl-aqua'|'hl-rust'}. returns svg, list of x centres."""
    out, xs = [], []
    hl = hl or {}
    for i, (o, h, l, c) in enumerate(data):
        x = round(x0 + i * dx, 1); xs.append(x)
        up = c >= o
        top, bot = sc(max(o, c)), sc(min(o, c))
        body = max(bot - top, 1.2)
        g = (f'<line x1="{x}" y1="{sc(h)}" x2="{x}" y2="{sc(l)}" class="wk"/>'
             f'<rect x="{x - w/2}" y="{top}" width="{w}" height="{body}" class="{"cu" if up else "cd"}" stroke-width="1"/>')
        out.append(f'<g class="{hl.get(i, "")}">{g}</g>' if i in hl else g)
    return "".join(out), xs

def header(title, lesson_id, h):
    return (R(0, 0, W, h, "bg", 0)
            + T(14, 22, lesson_id, "t k m gold")
            + T(W - 14, 22, "SYNTHETIC SCHEMATIC", "t k mut", "end")
            + T(14, 40, title, "t h"))

def svg(name, h, title, desc, body, steps):
    defs = ('<defs><pattern id="rl-hatch" width="6" height="6" patternUnits="userSpaceOnUse" '
            'patternTransform="rotate(45)"><rect width="6" height="6" fill="rgba(201,162,75,.10)"/>'
            '<line x1="0" y1="0" x2="0" y2="6" stroke="rgba(201,162,75,.45)" stroke-width="1.5"/></pattern></defs>')
    s = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {h}" role="img" '
         f'aria-labelledby="{name}-t {name}-d" class="rlv-svg" data-steps="{steps}">'
         f'<title id="{name}-t">{escape(title)}</title><desc id="{name}-d">{escape(desc)}</desc>'
         f'<style>{STYLE}</style>{defs}{body}</svg>')
    (OUT / "svg" / f"{name}.svg").write_text(s, encoding="utf-8")
    return s

DIAGRAMS = []

# ======================================================= 1. RL-STR-06 H1 bias
def d_h1():
    H = 560
    b = header("H1 decides whether. M15 only asks when.", "RL-STR-06", H)
    # --- H1 panel
    b += R(10, 54, 340, 200, "panel", 6)
    b += T(20, 72, "H1 · CONTEXT", "t k gold")
    sc = Scale(0, 100, 88, 236)
    h1 = [(60,64,50,52),(52,55,38,40),(40,42,22,25),(25,28,12,16),(16,34,14,32),(32,50,30,48),
          (48,66,45,63),(63,72,60,68),(68,70,52,54),(54,57,40,44),(44,60,42,58),(58,74,56,72),
          (72,88,70,84),(84,86,72,74),(74,77,64,66),(66,70,58,61)]
    s1_c, xs = candles(h1, 24, 13.5, sc, 7)
    # zoom box over last 3 candles
    zx0, zx1 = xs[13] - 7, xs[15] + 7
    swings = (T(xs[3], sc(12) + 13, "L", "t m aqua b", "middle")
              + T(xs[7], sc(72) - 5, "HH", "t m aqua b", "middle")
              + T(xs[9], sc(40) + 13, "HL1", "t m aqua b", "middle")
              + T(xs[12], sc(88) - 5, "HH1", "t m aqua b", "middle"))
    unk_x = xs[15] + 14
    unknown = (R(unk_x, 84, 340 - unk_x + 2, 80, "chip-mut", 4)
               + T((unk_x + 342) / 2, 104, ["Next H1 candles:", "not drawn.", "Bias is not", "a forecast."], "t mut it", "middle"))
    inv = (L(xs[9] - 4, sc(40), 342, sc(40), "lvl s-rust dash")
           + T(342, sc(40) + 15, ["Invalidation:", "an H1 close", "below HL1"], "t rust", "end"))
    b += G(1, s1_c + swings)
    b += G(2, inv + unknown)
    b += G(3, R(zx0, sc(88) - 2, zx1 - zx0, sc(56) - sc(88) + 6, "lvl s-gold", 2)
           + T((zx0 + zx1) / 2, sc(56) + 18, "zoomed ↓", "t gold halo", "middle"))
    # bias sentence
    bias = (R(10, 262, 340, 46, "chip-gold", 6)
            + T(20, 280, "WRITTEN BIAS", "t k gold")
            + T(20, 298, "“Upside is supported while H1 holds above HL1.”", "t b"))
    b += G(2, bias)
    # --- zoom connectors
    conn = ""
    # --- M15 panel
    m15p = R(10, 322, 340, 176, "panel", 6) + T(20, 340, "M15 · INSIDE THE GOLD BOX", "t k gold")
    sc2 = Scale(34, 90, 352, 476)
    m15 = [(85,87,81,82),(82,84,77,78),(78,82,76,81),(81,82,72,73),(73,75,68,69),(69,74,67,72),
           (72,73,62,63),(63,65,57,58),(58,64,56,62),(62,63,51,52),(52,54,46,47),(47,50,37.5,45),(45,49,43,48)]
    mc, mx = candles(m15, 24, 15, sc2, 8, {11: "hl-aqua"})
    lh = "".join(T(mx[i], sc2(m15[i][1]) - 5, "LH", "t m aqua b", "middle") for i in (2, 5, 8))
    m_inv = L(20, sc2(40), 340, sc2(40), "lvl s-rust dash") + T(20, sc2(40) + 14, "HL1 (from H1)", "t rust m")
    wick_note = (L(mx[11] + 6, sc2(37.5), 230, sc2(37.5) + 6, "lvl s-aqua") +
                 T(234, sc2(37.5) + 10, "Wick below HL1:", "t aqua") )
    read = (T(172, 360, ["Alone, M15 reads bearish:", "a run of lower highs."], "t mut")
            + T(172, 392, ["Inside H1 it is a pullback", "toward HL1 — nothing more."], "t"))
    b += G(3, conn + m15p + mc + lh + m_inv + read)
    wick_expl = T(234, sc2(37.5) + 23.5, "not an invalidation.", "t aqua")
    b += G(3, wick_note + wick_expl)
    # --- branches (step 4)
    ex = mx[-1] + 8
    br = (R(10, 506, 166, 46, "chip-aqua", 6) + T(18, 523, "H1 HOLDS ABOVE HL1", "t k aqua")
          + T(18, 540, "Bias still valid. Wait.", "t")
          + R(184, 506, 166, 46, "chip-rust", 6) + T(192, 523, "H1 CLOSES BELOW HL1", "t k rust")
          + T(192, 540, "Bias invalid → no bias yet.", "t"))
    b += G(4, br)
    return svg("h1-bias-before-m15", H,
               "H1 Bias Before M15 — synthetic schematic",
               "Top panel, H1: swing low L, higher high HH, higher low HL1, higher high HH1. A dashed rust line at HL1 "
               "marks the invalidation: an H1 close below HL1. The area after the last candle is left blank and labelled "
               "'not drawn — bias is not a forecast'. Written bias: upside is supported while H1 holds above HL1. "
               "Bottom panel, M15 zoom of the last H1 candles: a run of lower highs that alone reads bearish but inside H1 "
               "is a pullback toward HL1. One M15 wick dips below HL1 and closes above it — not an invalidation. "
               "Two outcomes are shown equally: H1 closes hold above HL1, bias still valid; an H1 candle closes below HL1, "
               "bias invalid and no bias yet.", b, 4)

# ================================================= 2. RL-LIQ-04 does not prove
def d_notprove():
    H = 534
    b = header("One wick. Two futures. Same four numbers.", "RL-LIQ-04", H)
    b += R(10, 54, 340, 250, "panel", 6)
    sc = Scale(20, 100, 96, 244)
    data = [(40,50,38,48),(48,62,46,60),(60,70,58,66),(66,68,52,54),(54,58,48,56),
            (56,69.8,55,65),(65,66,55,57),(57,63,54,62),(62,80,61,64)]
    c, xs = candles(data, 26, 13.5, sc, 8, {8: "hl-aqua"})
    lvl = (L(20, sc(70), 240, sc(70), "lvl s-gold") + T(20, sc(70) - 5, "EQH1", "t m gold b")
           + T(xs[2], sc(70) - 18, "1", "t m gold", "middle") + T(xs[5], sc(70) - 18, "2", "t m gold", "middle"))
    b += G(1, c.split('<g class="hl-aqua">')[0] + lvl)
    sweep = '<g class="hl-aqua">' + c.split('<g class="hl-aqua">')[1]
    x9 = xs[8]
    obs = (sweep
           + T(20, 76, "OBSERVED · traded above EQH1", "t k aqua") + L(x9, 80, x9, sc(80) - 3, "lvl s-aqua")
           + T(20, 270, "OBSERVED · closed back below", "t k aqua") + L(x9, sc(64) + 3, x9, 260, "lvl s-aqua"))
    b += G(2, obs)
    nx = x9 + 14
    y0 = sc(64)
    fut = (L(nx, 88, nx, 256, "lvl s-mut dot") + T(nx + 5, 102, "NOW", "t k mut halo")
           + P(f"M{nx} {y0} C {nx+30} {y0+10}, {nx+50} {sc(44)}, {nx+86} {sc(36)}", "path s-mut dash")
           + P(f"M{nx} {y0} C {nx+30} {y0-8}, {nx+46} {sc(78)}, {nx+86} {sc(84)}", "path s-mut dash")
           + L(nx + 40, sc(70), 338, sc(70), "lvl s-gold dot")
           + T(nx + 92, sc(95), ["Possible B:", "closes back", "above EQH1 →", "read invalid"], "t rust")
           + T(nx + 92, sc(40), ["Possible A:", "moves down", "and away"], "t mut")
           + T(342, 292, "Neither is on the chart yet.", "t mut it", "end"))
    b += G(3, fut)
    # ledger
    lg = (R(10, 314, 166, 108, "chip-aqua", 6) + T(20, 332, "ON THE CHART", "t k aqua")
          + T(20, 352, ["• Price traded above EQH1", "• The candle closed below", "• Open, high, low, close", "  + tick volume. That's all."], "t")
          + R(184, 314, 166, 108, "chip-mut", 6) + T(194, 332, "INFERRED — NOT IN IT", "t k mut")
          + T(194, 352, ["• Who traded", "• Why they traded", "• That it was “real”", "• Which future comes next"], "t mut it"))
    b += G(4, lg)
    risk = (R(10, 432, 340, 92, "chip-rust", 6) + T(20, 450, "WHERE IT SHOWS UP: RISK", "t k rust")
            + T(20, 470, ["A story about intent feels like certainty. Certainty", "sizes up, and holds past the invalidation level.", "The observed read keeps its exit condition:", "a close back above EQH1."], "t"))
    b += G(4, risk)
    return svg("what-a-sweep-does-not-prove", H,
               "What a Sweep Does Not Prove — synthetic schematic",
               "A gold level EQH1 made of two prior highs. A candle trades above EQH1 and closes back below it; both facts "
               "are labelled observed. After a 'now' line two dashed paths are drawn equally: possible A, price moves down "
               "and away; possible B, price closes back above EQH1 and the read is invalid. Neither is on the chart yet. "
               "A ledger separates what is on the chart (price traded above EQH1, candle closed below, OHLC plus tick "
               "volume) from what is inferred and not in it (who traded, why, that it was the real move, which future "
               "comes next). Risk note: a story about intent feels like certainty, which sizes up and holds past "
               "invalidation; the observed read keeps an invalidation — a close back above EQH1.", b, 4)

# ================================================ 3. RL-LIQ-03 sweep that isn't
def d_isnt():
    H = 590
    b = header("Three states that look alike — and aren't.", "RL-LIQ-03", H)
    b += T(14, 58, ["Score wick, close and follow-through separately,", "before the next candles arrive."], "t mut")
    panels = [
        ("STATE 1 · WICK-ONLY PROBE",
         [(46,54,44,52),(52,60,50,58),(58,64,56,62),(62,78,60,64)], None,
         [("Wick beyond", "PASS", "aqua"), ("Close back below", "PASS", "aqua"), ("Follow-through", "NOT YET", "mut")],
         ["A shape, not a signal.", "Unconfirmed until part 3."]),
        ("STATE 2 · CLOSE BEYOND THE LEVEL",
         [(46,54,44,52),(52,60,50,58),(58,64,56,62),(62,80,61,76),(76,80,72,77)], None,
         [("Wick beyond", "PASS", "aqua"), ("Close back below", "FAIL", "rust"), ("Follow-through", "N/A", "mut")],
         ["A breakout — different event.", "Drop the sweep label."]),
        ("STATE 3 · FAILED CONTINUATION",
         [(46,54,44,52),(52,60,50,58),(58,64,56,62),(62,78,60,64),(64,67,61,62),(62,66,60,65),(65,67,61,63),(63,66,61,64)], None,
         [("Wick beyond", "PASS", "aqua"), ("Close back below", "PASS", "aqua"), ("Follow-through", "FAIL", "rust")],
         ["Setup expired. Not a loss,", "not a missed trade — log it."]),
    ]
    y = 84
    for i, (title, data, _, score, verdict) in enumerate(panels):
        ph = 152
        body = R(10, y, 340, ph, "panel", 6) + T(20, y + 18, title, "t k " + ("gold"))
        sc = Scale(40, 86, y + 30, y + ph - 12)
        hl = {3: "hl-rust" if i == 1 else "hl-aqua"}
        c, xs = candles(data, 26, 14, sc, 8, hl)
        body += L(18, sc(70), 150, sc(70), "lvl s-gold") + T(20, sc(70) - 5, "EQH1", "t m gold")
        body += c
        if i == 2:
            body += R(xs[4] - 6, sc(68), xs[7] - xs[4] + 12, sc(59) - sc(68), "chip-mut", 2)
            body += T((xs[4] + xs[7]) / 2, sc(59) + 12, "chop", "t mut it", "middle")
        # scorecard
        sx = 164
        for j, (lab, res, col) in enumerate(score):
            yy = y + 36 + j * 22
            chip = {"aqua": "chip-aqua", "rust": "chip-rust", "mut": "chip-mut"}[col]
            body += T(sx, yy + 11, f"{j+1}. {lab}", "t")
            body += R(284, yy, 58, 16, chip, 3) + T(313, yy + 11.5, res, "t k " + col, "middle")
        body += T(sx, y + 114, verdict, "t b")
        b += G(i + 1, body)
        y += ph + 8
    b += G(4, T(W / 2, H - 12, "Part 3 is often skipped. Count your own cases.", "t it gold", "middle"))
    return svg("the-sweep-that-isnt", H,
               "The Sweep That Isn't — three distinct states, synthetic schematic",
               "Three panels, each with the level EQH1 and a three-part scorecard. State 1, wick-only probe: the wick "
               "reaches above EQH1 and the candle closes back below; wick pass, close pass, follow-through not yet — a "
               "shape, not a signal, unconfirmed until part 3. State 2, close beyond the level: the candle closes above "
               "EQH1 and the next holds; wick pass, close fail, follow-through not applicable — a breakout, a different "
               "event, drop the sweep label. State 3, failed continuation: wick above, close back below, then several "
               "overlapping candles of chop; wick pass, close pass, follow-through fail — setup expired, not a loss, not a "
               "missed trade, log it. Footer: part 3 is often skipped; count your own cases.", b, 4)

# ================================================ 4. RL-KZN-02 London matters
def d_london():
    H = 644
    b = header("Same shape, different hour, different context.", "RL-KZN-02", H)
    X0, X1, h0, h1 = 26, 344, 4, 22            # axis shows London local 04:00 → 22:00
    px = (X1 - X0) / (h1 - h0)
    X = lambda hr: round(X0 + (hr - h0) * px, 1)

    def timeline(y, title_lines, utc_off, ny, overlap, cpi, cls_note):
        s = R(10, y, 340, 214, "panel", 6)
        s += T(20, y + 18, title_lines[0], "t k gold") + T(20, y + 33, title_lines[1], "t mut")
        ay = y + 58
        # London-local ticks (top) and UTC ticks (bottom)
        s += T(X0 - 2, ay - 8, "LONDON", "t k mut")
        for hr in range(h0, h1 + 1, 2):
            s += L(X(hr), ay, X(hr), ay + 92, "grid")
        for hr in range(8, h1 + 1, 4):
            s += T(X(hr), ay - 8, f"{hr:02d}", "t m mut", "middle")
        s += L(X(cpi), ay - 2, X(cpi), ay + 94, "lvl s-rust dash")
        rows = [("Asia", 4, 9, "chip-mut"), ("London 08–16", 8, 16, "chip-gold"), (f"New York {ny[0]:02d}–{ny[1]:02d}", ny[0], ny[1], "chip-gold")]
        for k, (lab, a, z, chip) in enumerate(rows):
            ry = ay + 6 + k * 24
            s += R(X(a), ry, X(z) - X(a), 18, chip, 3)
            s += (T(X(a) + 5, ry + 12.5, "Asia (thin)", "t mut") if k == 0
                  else T(X(z) - 5, ry + 12.5, lab, "t halo", "end"))
        # overlap
        oy = ay + 78
        s += f'<rect x="{X(overlap[0])}" y="{oy}" width="{X(overlap[1]) - X(overlap[0])}" height="14" class="overlap"/>'
        s += T(X(overlap[1]) + 4, oy + 11, f"overlap {overlap[1]-overlap[0]}h", "t gold")
        # UTC axis
        uy = ay + 108
        s += T(X0 - 2, uy, "UTC", "t k mut")
        for hr in range(8, h1 + 1, 4):
            s += T(X(hr), uy, f"{(hr - utc_off) % 24:02d}", "t m mut", "middle")
        # CPI marker (US 08:30 New York) drawn beneath the bars above
        s += T(20, uy + 20, f"Rust line: US data 08:30 New York = {int(cpi):02d}:30 London", "t rust")
        s += T(20, uy + 36, cls_note, "t mut")
        return s

    y1 = 52
    base = timeline(y1, ("MOST OF THE YEAR · GAP 5H", "summer example: UK on BST (UTC+1), US on EDT"),
                    1, (13, 21), (13, 16), 13.5, "London = UTC+1 in summer (BST), = UTC in winter.")
    b += G(1, base)
    ay = y1 + 58
    # two identical setups, different context
    mk = (L(X(9 + 40/60), ay - 2, X(9 + 40/60), ay + 94, "lvl s-aqua")
          + f'<circle cx="{X(9+40/60)}" cy="{ay + 46}" r="4" class="aqua"/>'
          + f'<circle cx="{X(13+25/60)}" cy="{ay + 46}" r="4" class="rust"/>'
          + T(X(9 + 40/60) + 5, ay + 17, "09:40", "t m aqua halo")
          + T(X(13 + 25/60) + 5, ay + 17, "13:25", "t m rust halo"))
    b += G(2, mk)
    cmp_ = (R(10, 272, 166, 72, "chip-aqua", 6) + T(18, 289, "SETUP AT 09:40", "t k aqua")
            + T(18, 306, ["London active, no data due.", "Context: supports the read."], "t")
            + R(184, 272, 166, 72, "chip-rust", 6) + T(192, 289, "SAME SETUP, 13:25", "t k rust")
            + T(192, 306, ["5 min before US CPI.", "Context: weakens it —", "the release dominates."], "t"))
    b += G(2, cmp_)
    y2 = 352
    mis = timeline(y2, ("MISALIGNMENT WEEKS · GAP 4H", "2026: 8–29 Mar, 25 Oct–1 Nov (UK GMT, US EDT)"),
                   0, (12, 20), (12, 16), 12.5, "London local = UTC. The US release moves an hour earlier.")
    b += G(3, mis)
    foot = (R(10, 574, 340, 62, "chip-mut", 6)
            + T(18, 591, ["Third clock: your broker's server time. Derive the", "offset in MT5 — don't copy one. Windows are conventions,", "not exchange hours. Review these dates every year."], "t mut"))
    b += G(4, foot)
    return svg("when-london-matters", H,
               "When the London Window Matters — session clock with daylight-saving assumptions, schematic",
               "Two session timelines on a London-local axis from 04:00 to 22:00 with UTC underneath. Top, most of the "
               "year, gap 5 hours, shown with UK on BST (UTC+1) and US on EDT: Asia to 09:00 (thin), London 08–16, New "
               "York 13–21, overlap 3 hours 13–16; the 08:30 New York US data release lands at 13:30 London. Two "
               "identical setups: at 09:40 London, London active with no data due, context supports the read; at 13:25, "
               "five minutes before US CPI, context weakens it because the release dominates. Bottom, misalignment weeks, "
               "gap 4 hours — in 2026, 8–29 March and 25 October–1 November, UK on GMT and US on EDT: London 08–16 equals "
               "UTC, New York 12–20, overlap 4 hours 12–16, and the US release lands at 12:30 London. Footer: the third "
               "clock is your broker server time — derive its offset in MT5; session windows are conventions; review "
               "these dates yearly.", b, 4)

# ================================================ 5. RL-MND-06 pre-trade journal
def d_journal():
    H = 600
    b = header("Written before. Scored after — with no P&L.", "RL-MND-06", H)
    b += T(14, 58, "Illustrative entry, 09:38 London — not a recommendation.", "t mut")
    # PLAN
    b += G(1, T(14, 80, "1 · PLAN", "t k gold")
           + R(10, 88, 340, 52, "chip-gold", 6) + T(20, 105, "THESIS", "t k gold")
           + T(20, 122, ["H1 lower highs. M15 reached above EQH1,", "closed back below."], "t"))
    b += G(2, R(10, 148, 166, 60, "chip-rust", 6) + T(18, 165, "INVALIDATION", "t k rust")
           + T(18, 182, ["M15 close back above", "EQH1. A defined event."], "t")
           + R(184, 148, 166, 60, "chip-rust", 6) + T(192, 165, "RISK", "t k rust")
           + T(192, 182, ["0.5% (illustrative only).", "Lot from your MT5 spec."], "t")
           + R(10, 216, 340, 36, "chip-gold", 6) + T(18, 238, "STOP ME IF", "t k gold") + T(100, 238, "no follow-through within 2 candles.", "t")
           + T(14, 266, "+ why now, session & calendar — six fields in the lesson.", "t mut it"))
    # GATE + branches
    gate = (L(180, 274, 180, 288, "lvl s-mut")
            + P("M180 288 L 272 314 L 180 340 L 88 314 Z", "lvl s-gold") + T(180, 311, "Is invalidation a", "t", "middle")
            + T(180, 325, "number or event?", "t", "middle")
            + L(88, 314, 50, 314, "lvl s-mut") + L(50, 314, 50, 356, "lvl s-mut") + T(56, 309, "no", "t k mut", "end")
            + L(272, 314, 310, 314, "lvl s-mut") + L(310, 314, 310, 356, "lvl s-mut") + T(304, 309, "yes", "t k aqua", "start"))
    b += G(3, T(14, 286, "2 · DECIDE", "t k gold") + gate)
    skip = (R(10, 356, 166, 88, "chip-mut", 6) + T(18, 373, "SKIPPED / EXPIRED", "t k mut")
            + T(18, 390, ["No invalidation → not ready.", "Or the stop-me condition", "hit first. No order.", "Still logged."], "t"))
    take = (R(184, 356, 166, 88, "chip-aqua", 6) + T(192, 373, "ORDER PLACED", "t k aqua")
            + T(192, 390, ["Entry timestamped after", "the plan. Outcome is", "recorded — win, loss or", "manual exit."], "t"))
    b += G(3, skip + take)
    # REVIEW
    rv = (L(93, 444, 93, 470, "lvl s-mut") + L(267, 444, 267, 470, "lvl s-mut")
          + T(14, 466, "3 · REVIEW", "t k gold")
          + R(10, 474, 340, 118, "chip-aqua", 6) + T(20, 492, "SCORE EXECUTION, NOT PROFIT", "t k aqua")
          + T(20, 512, "Did I wait for what the thesis said?", "t") + T(340, 512, "Y / N", "t m", "end")
          + T(20, 530, "Did I honour the invalidation?", "t") + T(340, 530, "Y / N", "t m", "end")
          + T(20, 548, "Was risk what I wrote?", "t") + T(340, 548, "Y / N", "t m", "end")
          + T(20, 572, "Skipped entries count too — they keep the sample honest.", "t mut it"))
    b += G(4, rv)
    return svg("pre-trade-journal", H,
               "The Journal Entry You Write Before the Trade — plan-to-review board",
               "An illustrative entry at 09:38 London. Plan: thesis — H1 lower highs, M15 reached above EQH1 and closed "
               "back below; invalidation — an M15 close back above EQH1, a defined event; risk — 0.5 percent, "
               "illustrative only, lot size from your MT5 specification; what would stop me — no follow-through in two "
               "candles; two further fields in the lesson. Decide: a gate asks whether invalidation is a number or event. "
               "No leads to skipped or expired — not ready, or the stop-me condition hit first, no order, still logged. "
               "Yes leads to order placed, entry timestamped after the plan, outcome recorded. Review: score execution, "
               "not profit — did I wait for what the thesis said, did I honour the invalidation, was risk what I wrote. "
               "Skipped entries count too, they keep the sample honest.", b, 4)

LESSONS = [
    ("h1-bias-before-m15", "RL-STR-06", "H1 Bias Before M15 Execution", "/learn/tracks/read-structure/h1-bias-before-m15/", d_h1,
     ["H1: label the swings with one fixed rule — L, HH, HL1, HH1.",
      "Write the bias with its invalidation. What comes next is left blank on purpose.",
      "Drop to M15 inside the gold box: lower highs that are only a pullback. A wick below HL1 is not a close.",
      "Two outcomes, drawn equally. Only an H1 close below HL1 ends the bias."],
     "The lesson's failure mode is reading M15 first and back-filling an H1 story, so the diagram fixes H1 above M15 and physically links them with a zoom box: the reader sees the same lower highs twice — alarming alone, ordinary in context. The rust HL1 line runs through both panels so the invalidation is a single, visible price rather than a feeling, and the blank, labelled area to the right of H1 refuses to draw a direction. The final frame ends on two equal-weight outcome boxes, so the takeaway is the rule (H1 close below HL1 ends the bias; a wick does not), not a prediction."),
    ("what-a-sweep-does-not-prove", "RL-LIQ-04", "What a Sweep Does Not Prove", "/learn/tracks/hunt-liquidity/what-a-sweep-does-not-prove/", d_notprove,
     ["The level: two prior highs make EQH1. Reference only.",
      "The sweep: traded above, closed back below. Both are observed.",
      "After “now”, two possible futures are equally consistent with the same wick.",
      "The ledger: what's on the chart vs. what's inferred — and where the difference lands: risk."],
     "The argument of this lesson is that one set of four numbers supports more than one future, so the diagram literally forks at a “now” line and draws both branches in the same dashed, not-yet-observed style. Observation is anchored to the candle with aqua callouts; everything else moves into an explicit “inferred — not in it” column rather than being argued in prose. Ending on the rust risk panel turns epistemics into the practical point the lesson makes: the causal story is what makes traders size up and hold through invalidation, while the observed read keeps a defined exit condition."),
    ("the-sweep-that-isnt", "RL-LIQ-03", "The Sweep That Isn't: Wick, Close, Follow-Through", "/learn/tracks/hunt-liquidity/sweep-that-isnt/", d_isnt,
     ["State 1: a wick-only probe. Parts 1–2 pass; part 3 isn't known yet.",
      "State 2: the candle closes beyond the level — a breakout, a different event.",
      "State 3: wick and close pass, then chop. Follow-through fails; the setup expires.",
      "Part 3 is often skipped. Count your own cases."],
     "Three near-identical candles side by side are the fastest way to show that the sweep label depends on details beginners skip. Each state gets the same scorecard in the same order, so the eye learns the test itself — wick, close, follow-through — and sees that each part fails independently. Pass/fail are written words, not just colours. The probe state deliberately ends on “not yet” rather than a success, because the lesson's honest claim is that the first two parts describe a shape, and only the third says anything about whether it mattered."),
    ("when-london-matters", "RL-KZN-02", "When the London Window Matters, and When It Doesn't", "/learn/tracks/time-the-killzone/when-london-matters/", d_london,
     ["Most of the year: London and New York are 5h apart, with a 3h overlap. Two clocks on every axis.",
      "The same setup at 09:40 and at 13:25: one has context behind it, one sits five minutes before US CPI.",
      "Misalignment weeks: 4h apart. The overlap grows to 4h and the US release moves to 12:30 London.",
      "Your broker's clock is a third one. Derive it; review these dates every year."],
     "Beginners hear “London opens at 8” and never discover their chart is on another clock. The diagram puts London local and UTC on every axis and shows the normal-gap and misaligned-gap years as two stacked timelines, so the shift is seen rather than explained: the overlap grows from three to four hours and a fixed-clock US release moves an hour earlier in London terms. The two markers make the lesson's core point — identical pattern, different participation context — and the rust marker shows a scheduled release overriding the session label. Daylight-saving assumptions (which offsets apply, which 2026 dates) are printed on the diagram, and the broker server clock is named but deliberately not given a number."),
    ("pre-trade-journal", "RL-MND-06", "The Journal Entry You Write Before the Trade", "/learn/tracks/master-the-mind/pre-trade-journal/", d_journal,
     ["Plan: the thesis in plain words, written before any order.",
      "Invalidation and risk are the load-bearing fields — plus what would stop you.",
      "The gate: no defined invalidation means no order. Skipped and expired entries are still logged.",
      "Review scores execution — waiting, invalidation, risk. Profit is not a column."],
     "The lesson's claim is that a journal written before the trade does a different job from one written after, so the board reads top to bottom in time order: plan, decide, review. Invalidation and risk sit in rust as the two fields that carry money; the decision diamond makes “no invalidation → not ready” a visible branch rather than advice, and the skipped branch merges into review so the reader sees that non-trades belong in the sample. The review panel has three yes/no execution questions and no P&L field, which is the lesson's point made structurally. The 0.5% is labelled illustrative at the point of use, as the lesson's editorial note requires."),
]

if __name__ == "__main__":
    for key, lid, title, url, fn, caps, why in LESSONS:
        s = fn()
        DIAGRAMS.append((key, lid, title, url, s, caps, why))
    import assemble
    assemble.build(DIAGRAMS, OUT)
    print("ok", [d[0] for d in DIAGRAMS])
