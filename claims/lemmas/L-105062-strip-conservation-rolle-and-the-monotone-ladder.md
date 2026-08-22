# L-105062 — Strip, conservation, Rolle floor, and the monotone ladder for the ξ-derivative chain

Claim ID: `L-105062`
Status: **PROVED (four theorems, explicit constants; independent numeric falsification pass at T ≤ 100) — RH NOT ADDRESSED**
Created: 2026-08-22
Agent: claude (external reviewer lane; Program B lane B1, assembled by orchestrator)
Depends on: classical inputs only (Hadamard factorization, Gauss–Lucas, Hurwitz, Riemann–von Mangoldt, Hardy's theorem, Landau's lemma [Montgomery–Vaughan, Mult. Number Theory I, Lemma 6.4], Binet's formula) — all EXTERNAL-CLASSICAL, named at point of use. Zeta23 corollary additionally consumes the repo-official import row (see §6).
Replay: `experiments/X-105060-descent-ladder/` (laneB1_NOTES.md = full proofs; xi_ladder.py, ladder_census.py, results_B1.json).
RH status: **unproved, not addressed**

## 0. Objects

`xi(s) = (1/2) s(s-1) pi^{-s/2} Gamma(s/2) zeta(s)`; `Xi(t) := xi(1/2+it)` real
entire, EVEN, order 1; `Xi_k := (d/dt)^k Xi = i^k xi^{(k)}(1/2+it)`, real entire
of parity `(-1)^k`. Counts on `0 < Re t <= T` WITH multiplicity, `Re t = 0`
excluded: `N_k(T)` all zeros, `N_k^r(T)` real ones, `N_k^c = N_k - N_k^r`;
`D_k(T)` = DISTINCT real zeros in `(0, T]`.

## 1. Strip Lemma

**Theorem 1.** For every `k >= 0`, every zero of `Xi_k` lies in `|Im t| <= 1/2`
(equivalently every zero of `xi^{(k)}` lies in `0 <= Re s <= 1`).

Proof (induction on k). `Xi_k` real entire, order ≤ 1, parity `(-1)^k`, zeros in
the closed strip (base case: classical zero-free regions + functional equation).
Write `Xi_k(t) = c t^m E(t)`, `E` even, `E(0) != 0`; `G(t^2) := E(t)` is entire
of order ≤ 1/2 < 1, so by genus-0 Hadamard factorization [Titchmarsh, Theory of
Functions §8.24] `Xi_k(t) = c t^m prod_nu (1 - t^2/tau_nu^2)`, absolutely and
locally uniformly (`sum 1/|tau_nu|^2 < infinity` since the exponent of
convergence is ≤ order ≤ 1 < 2 [ToF §8.22]). Partial products are polynomials
with all zeros `(0, ±tau_nu)` in the closed convex strip; Gauss–Lucas [Marden,
Geometry of Polynomials, Thm 6.1 — no reality of coefficients needed] puts their
derivatives' zeros in the strip; `P_N' -> Xi_{k+1}` locally uniformly (Cauchy
integral formula); Hurwitz [Conway VII.2.5] excludes zeros of `Xi_{k+1}` off the
strip. Only the CLOSED strip is claimed. QED.

(Recorded failure: the alternative route via termwise Re-positivity of the
paired Hadamard sum of `xi'/xi` on `Re s > 1/2` is FALSE as stated — explicit
sign counterexample in the replay notes §6.4; it holds only for `Re s >= 1`.)

## 2. Conservation Lemma

**Theorem 2.** For every `k` there are explicit constants (admissible
`A_k = 70 + 6k`; `B_k, T_k` explicit but large — see honesty §5) with

```
|N_{k+1}(T) - N_k(T)| <= A_k log T + B_k    for all T >= T_k.
```

**Corollary 2.1 (Riemann–von Mangoldt on every rung).**
`N_k(T) = (T/2pi) log(T/2pi) - T/2pi + O_k(log T)` (telescoping from the
classical `N_0 = N`).

Proof route (full details in replay laneB1_NOTES.md §2): argument principle for
`G_k = Xi_{k+1}/Xi_k` on `[eta, T] x [-1, 1]`, boundary zero-free by Theorem 1 +
good-T selection. Key Sub-lemma A: on `sigma in [5/4 + eps_k, 5 - eps_k]`,
`x >= a_k`: `xi^{(k)}(s) = xi(s) ell(s)^k (1 + delta_k(s))`,
`ell(s) = (1/2) log(s/2pi)`, `|delta_k| <= min(C_k/ell_0(x), 1/8)`, built from
the exact identity `xi'/xi = 1/s + 1/(s-1) - (1/2)log pi + (1/2)psi(s/2) +
zeta'/zeta`, the Binet bound `|psi(z) - log z| <= 0.64/|z|` (`Re z >= 5/8`,
derived), and `|zeta'/zeta(sigma+ix)| <= -zeta'/zeta(5/4) = 3.4667...`
(`sigma >= 5/4`, Lambda-series). Orientation resolved: the `Im t = -1` edge is
`s = 3/2 + ix` (right of the strip); the `Im t = +1` edge needs no separate
estimate since `G_k(x+i) = conj(G_k(x-i))` by reality. On the far horizontal
edges `G_k = i ell (1 + theta)`, `|theta| <= 2/7`, values confined to an open
sector of opening `5pi/6 < pi` ⇒ bounded argument variation. Right vertical
edge: Landau's lemma + a Jensen disk count centered at `t = T - 4i` (where
Sub-lemma A gives the unconditional lower bound `log|Xi_k| >= -pi T/4 - 9`)
yields `|Delta arg Xi_j| <= 6.1 (17+j) log T`. QED.

(Recorded correction to the orchestrator brief: on the far edge `|E_k| =
|xi^{(k+1)}/xi^{(k)} - ell|` is BOUNDED, not `o(1)` — measured 0.09–0.65 for
`x in [20, 500]`, `k = 0,1,2`; boundedness is what the proof claims and needs.)

## 3. Rolle floor

**Theorem 3.** For all `k, T`: `N_{k+1}^r(T) >= N_k^r(T) - 1` (absolute
constant 1), with multiplicity: an m-fold real zero of `Xi_k` yields an
(m-1)-fold real zero of `Xi_{k+1}` at the same point, plus one Rolle zero per
open gap between the `M` distinct zeros in `(0, T]`:
`sum(m_i - 1) + (M - 1) = N_k^r - 1`, all produced zeros in `(0, t_M]`. For ODD
`k` the origin gives the sharper `N_{k+1}^r(T) >= N_k^r(T)` (`Xi_k` odd
vanishes at 0; Rolle on `[0, t_1]`).

**Theorem 3′ (distinct variant).** `D_{k+1}(T) >= D_k(T) - 1` (gap-produced
zeros lie in disjoint open intervals, hence are distinct).

## 4. Monotone Ladder

**Theorem 4.** `kappa_k(T) := N_k^r(T)/N_k(T)` satisfies, for `T >= T_k^*`:

```
kappa_{k+1}(T) >= kappa_k(T) - (A_k + 1) log T / N_k(T);
```

since `N_k(T) >> T log T` (Cor 2.1), `liminf_T kappa_{k+1} >= liminf_T kappa_k`.
The same holds for the distinct ratio `kappa~_k(T) := D_k(T)/N_k(T)`.
**The asymptotic on-line proportion is monotone non-decreasing along the
ξ-derivative ladder.**

Note: SIMPLICITY (as opposed to distinctness) does NOT transfer through Rolle
by this argument; the distinct-zero ladder is the honest strengthening.

## 5. Honesty on constants

`A_k = 70 + 6k` is explicit but lossy (observed truth ≤ 1 at `T <= 100`); the
additive constants `B_k, T_k` inherit Sub-lemma A's abscissae
`a_k ~ 2pi exp(16 C_k)`, `C_k ~ 2^{k+1}` — tower-large in `k`. Asymptotically
harmless (Theorem 4 is a `T -> infinity` statement at each fixed `k`);
finite-height use of Theorem 2 for `k >= 1` at small `T` is vacuous — the
certified census (`X-105061`) covers low height instead. The Landau-lemma
constant is cited [MV Lemma 6.4]; any absolute constant works.

## 6. Corollary: the imported Zeta23 baseline rides the ladder

Consuming the repo-official import row
[`Z23-UPSTREAM`, `integration/2026-08-11/CLAIM_LEDGER.tsv` line 50, branch
`main`, `677203992eb0168920365ee45ae9db76bfa97dcf` — status
IMPORTED_UNCONDITIONAL_THEOREM / IMPORTED_UPSTREAM_VERIFIED]: for the dyadic
windows `(T, 2T]`, `liminf N0star/N >= 0.67250...` with `N0star` = DISTINCT
points on the critical line and `N` counted with multiplicity [statement text:
`research/external/anthropic-zeta23/README.md` §1 @
`origin/research/gpt56-pro/import-anthropic-zeta23-and-extend`
`c13b8836f6c7f4e36f17ab1c4ebe41e4cf072f2e`; exact constant
`0.6725007036794117 = 3/2 - (1/sqrt2) cot(1/sqrt2)` per
`verification-results/constants.json` (same commit) and closed form L-90227.1 @
`origin/research/gpt56-pro/90102-liouville-bernstein-extremality`
`1a60df88aadac731ec32e48a87b74537662114dd`].

Dyadic-to-cumulative bridge: if `a_i/b_i >= c - eps` for all dyadic windows
`i >= i_0` (`a_i, b_i >= 0`, `b_i` the window totals, `sum b_i -> infinity`),
then `sum_{i<=I} a_i / sum_{i<=I} b_i >= c - eps - O(1/sum b) -> c - eps`. Hence
`kappa~_0 = liminf_T D_0(T)/N_0(T) >= 0.67250...`, and by Theorem 4:

```
FOR EVERY k >= 0:   liminf_T D_k(T)/N_k(T) >= 0.6725007036...
```

— at least 67.25% of the zeros of every derivative `xi^{(k)}` are distinct
points on the critical line, unconditionally MODULO the import row's own
status (upstream fixed-window Lean; repo-side exact-SHA review pending per
`RESULTS_INDEX_SNIPPET.md`; this corollary inherits exactly that status and
nothing stronger). For `k >= 1` this is weaker than Conrey's classical
proportions at large `k` but carries the import's distinct-points refinement at
every rung from `k = 0`.

## 7. Numeric falsification pass (replay results_B1.json; dps 40)

Real zeros by fine-grid sign changes + bisection; TOTAL zeros by winding of
`Xi_k` around `[2,T] x [-1,1]` (adaptive phase tracking; windings integer to
~1e-13): `T = 50`: real = total = (10, 9, 10, 9) for `k = 0..3`; `T = 100`:
real = total = (29, 29, 29, 29) — all zeros in these rectangles real and
simple; conservation `|N_{k+1} - N_k| <= 1` at `T = 50` (genuine edge
breathing), `= 0` at `T = 100`; Rolle floor observed SHARP (9 = 10 - 1).
Implementation validated against `mp.diff` to rel. 1e-39 and the functional
equation. First real zeros: `Xi_1`: 15.5857 (+ t = 0), `Xi_2`: 4.7502,
`Xi_3`: 8.2607. The deep census to `T = 500` is `X-105061`.

## 8. Falsifiers

A zero of any `Xi_k` off the closed strip; `|N_{k+1}(T) - N_k(T)|` exceeding
`A_k log T + B_k` beyond `T_k`; a gap of `Xi_k` with no `Xi_{k+1}` zero
(violates Rolle); `kappa~_k` measurably below `kappa~_0` at scale (violates
Theorem 4); withdrawal or downgrade of the Z23-UPSTREAM import row (kills §6
only — Theorems 1–4 are independent of it).
