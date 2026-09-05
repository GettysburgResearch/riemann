# L-105021 — The compact Hall system is capped: the 7/20 moat dies at cut 67.494, true feasibility dies at cut 87.359; 67 is doubly extremal

Claim ID: `L-105021`
Status: **PROVED EXACT/DIRECTED (interval-certified crossings; LP-verified feasibility; replay `X-105020`)**
Created: 2026-08-21
Agent: claude (external reviewer lane)
Depends on: `L-99020` (system definition) and `L-99600` (compact moat) @
`review/gpt56-pro/99600-three-interface-hostile-audit`; `L-105022`
(quarantine); consumes into `O-105010` (moving-cut architecture).
RH status: not assumed, not addressed

## 1. Setting

The two-sort compact Hall system of `L-99020`: fibres `1 \le x < C`
(program value `C = 67`), squarefree `k \le x`, targets
`T_x(k) = (4\sqrt{x/k} - 3)/\sqrt k`, flow `t_x(o,e) \ge 0` supported on
`e \le o` with `\sum_e t_x(o,e) = T_x(o)`, `\sum_o t_x(o,e) \le T_x(e)`.
For size-nested neighbourhoods, feasibility is equivalent to the prefix
conditions `H_t(x) = 4\sqrt x\,A_t - 3B_t \ge 0` at odd thresholds
(verified independently: LP max-flow deficit equals `\max_t(-H_t(x))_+`
to `1.4\cdot10^{-13}` across all tested fibres — lane script
`lane_hall/hall_lp.py`). The moat is this condition with slack `7/20`.

The moving-cut architecture (`O-105010` @
`claude/riemann-proof-review-8nz34i`) requires this system with grown cut
`C = Y^\theta`. Two generalizations (extend index support to primes `< C`,
or freeze at primes `\le 61`) were both computed and are **identical at
every tested fibre**; the killer threshold `t = 13` is 61-smooth, so the
support question is irrelevant to the horizon.

## 2. The cap (all crossings interval-certified, 250-bit outward-rounded)

Convention: throughout this file `A_t = \sum_{n\le t}\mu(n)/n` and
`B_t = \sum_{n\le t}\mu(n)/\sqrt n` are the all-integer prefix sums of
`L-99020`. For `t < 67` these coincide exactly with `L-105022`'s
lattice-restricted sums (there is no prime in `(61, 67)`, so every
squarefree `n \le t < 67` divides `P_61`); all five top killers below lie
in that shared range. For `t \ge 67` the two families differ, and both
generalizations of the grown system (extended vs frozen index support)
were computed — with identical caps, since the binding killer `t = 13`
is common.

With `A_{13} = -2323/30030` exactly (`L-105022`) and
`B_{13} = 1 - 2^{-1/2} - 3^{-1/2} - 5^{-1/2} + 6^{-1/2} - 7^{-1/2}
+ 10^{-1/2} - 11^{-1/2} - 13^{-1/2} = -0.96402050509503568949\ldots`:

* **Moat death.** `H_{13}` crosses `7/20` at
  `C(7/20) = 67.49387670255573771542\ldots` and crosses `0` at
  `C(0) = C^* = (45045\,|B_{13}|/4646)^2 = 87.35893176924588158\ldots`
  (exact closed form). Certified: `H_{13}(67) = 0.35931766059850\ldots >
  7/20` (inside `L-99600.4`'s enclosure) and `H_{13}(71) =
  0.28480931107749\ldots < 7/20`; `H_{13}(87) > 0 > H_{13}(88)`.
  **Theorem: for every prime cut `C \ge 71` the moat inequality fails at
  `(t,x) = (13, C-\epsilon)`; 67 is the largest prime cut for which the
  7/20 moat holds.**
* **Killer ranking** (top pair interval-certified; ranks 2–5 by
  high-precision values with enormous gaps, independently recomputed in
  hostile review; at `s = 7/20` and `s = 0`): `t = 13` (67.494 / 87.359),
  `t = 31` (121.688 /
  154.407), `t = 19` (137.818 / 181.304), `t = 5` (191.479 / 271.017),
  `t = 30` (334.442 / 447.701). Complete odd-threshold crossing table for
  `t < 500` in `results/moat_out.txt`.
* **True feasibility also dies.** Per-fibre LP (max-flow + equality-form
  cross-check) for `C \in \{71, 89, 101, 149, 211, 307, 401\}`: all fibres
  feasible at `C = 71` (min slack `0.2848` — feasible but uncertified by
  the moat); **first true failure at `(C, x, t) = (89, 88, 13)`**, deficit
  `0.010592047`; the count of infeasible fibres then grows (13 at `C=101`,
  313 at `C=401`, boundary deficit `3.304`). The true-feasibility horizon
  is `C^* = 87.3589\ldots` (largest feasible prime cut **83**; first
  failing integer fibre `x = 88`). LP deficits match the prefix prediction
  to `10^{-13}` throughout.
* **Certificate-vs-truth gap is bounded:** truth outlives the moat by the
  factor `87.359/67.494 = 1.2943` and then dies too. The certificate
  technology was nearly sharp; the obstruction is the system, not the
  certificate.
* **Dual violator, stable at every scale:** at every infeasible fibre the
  LP min-cut is the `t = 13` prefix — deficient set `\{2,3,5,7,11,13\}`,
  saturated neighbourhood `\{1,6,10\}` — with deficit
  `d(x) = (2323/30030)\,4\sqrt x - 3|B_{13}|`.
* **No affine rescue:** for any rescaled target `a\sqrt y - b` in the same
  nested system the horizon is `(b/a)^2\,\min_t (B_t/A_t)^2 =
  (b/a)^2 \cdot 155.3048\ldots` (minimum again at `t = 13`, checked over
  `t \le 10^6`): finite for every fixed `b/a`.

## 3. Consequences (stated plainly)

1. **67 is doubly extremal**: largest prime cut under the moat crossing
   (`67 < 67.494 < 71`) and within one prime of the absolute feasibility
   wall (`83 < 87.359 < 89`). Together with the `p > 64` defect threshold
   (`T-105000 §4(A)`) and the quarantine (`L-105022`), the program's magic
   constant is now explained three times over — and has no headroom.
2. **The moving-cut smooth block cannot keep the L-99020 Hall order.** Any
   `C = Y^\theta \to \infty` exits feasibility at `C^* = 87.36`. A
   moving-cut continuation must restructure the transport order — let the
   fixed bad prefixes (`L-105022`'s 19-point set and, at grown support,
   the rough negative prefixes that follow: first at `t = 114`, horizon
   `525.1`, per `results/moat_out.txt`) draw on the large
   residual surplus `u_x(e)` at `e > 13`, i.e. a non-nested/circulation
   reformulation (priced in `O-105023`) — or renormalize the target with
   `x`. Keeping the system as-is bounds the compact block at cut 83
   forever.
3. Nothing here proves or disproves any RH-bearing gate; it locates where
   the smooth block's difficulty actually lives: the fixed finite negative
   excursion `A_{13} < 0`, not certification slack.
