# Lane P3 — [E1a-residue] The u-block <-> X-octave bookkeeping lemma (verified, with constants)

T-105059.5(ii) asserts the U-cell bookkeeping "closes trivially" via `log U = (1/3) log X`.
VERDICT AFTER VERIFICATION: the assertion is CORRECT, and in fact stronger than stated —
under the pinned continuous-u definition the change of variables is an EXACT IDENTITY,
not an asymptotic bookkeeping step; no off-by-cell issue exists. One definitional
ambiguity in T-105059.6's `W_u` was found and is PINNED here (Definition 1); it is the
reading P2.1 and P4 already use.

## Definition 1 (pinning W_u — the continuous-u reading)

For real `u >= 1` set `X := u^3`, `U := floor(u) = floor(X^{1/3})`, `N := floor(X/U)`
(for `u < 4`, i.e. `X < 64`, set `W_u := 0`; this head contributes a fixed finite
constant and is invisible to every limsup). Then

    W_u := Lambda(u^3) sqrt(log N) / u,
    V(X) := Lambda(X) sqrt(log N_X) X^{-1/6}     (so  u W_u^2 = V(u^3)^2 * u^{-... see L1).

Here `Lambda` is T-105059.5's tent sum. The DISCRETE alternative (u ranging over
integers, sums over unit cells) appears nowhere in the proof chain — T-105059.5's
consumption and P2.7's production are both integrals of the continuous field — so
Definition 1 is the honest formalization of T-105059.6's pinned lemma. (Within a cell
`u in [U, U+1)`, N sweeps ~3u integers and Lambda varies; no freezing claim is made or
needed.)

## Lemma 1 (exact change of variables — zero constants lost)

For all `T >= 1`, with `Y := T^3`:

    int_1^T u W_u^2 du/u  =  (1/3) int_1^Y V(X)^2 dX/X,
    (1/log T) int_1^T u W_u^2 du/u  =  (1/log Y) int_1^Y V(X)^2 dX/X    (T > 1),

hence  `limsup_T (1/log T) int_1^T u W_u^2 du/u = limsup_Y (1/log Y) int_1^Y V^2 dX/X`
EXACTLY. (= P2.1(a); re-derived and numerically confirmed here.)

Proof. `u W_u^2 du/u = W_u^2 du = (Lambda(u^3)^2 log N / u^2) du`. Substitute
`X = u^3`: `du = (1/3) X^{-2/3} dX`, `u^2 = X^{2/3}`, so the integrand is
`(1/3) Lambda(X)^2 log N_X X^{-4/3} dX = (1/3) V(X)^2 dX/X` since
`V^2 = Lambda^2 (log N_X) X^{-1/3}`. The floors ride along untouched: `U = floor(X^{1/3})`
is the same integer whether computed from u or from X (X = u^3 exactly), and N = floor(X/U)
likewise — this is the only place a cell-slip could enter, and there is none because the
substitution is a bijection of the parameters, not an approximation. The normalization:
`log Y = 3 log T` cancels the Jacobian 1/3. QED.

Cube-corner audit (the one potential off-by-one): at `X = d^3` (perfect cube),
`U = d` and the mollifier cutoff reads `d' > U = X^{1/3}`; for INTEGER d' this is
`d' > X^{1/3}` iff `d'^3 > X` — exact in both readings (P2.2's observation).
Numerically verified for all `X in [60, 3000] ∪ {k^3 : 4 <= k <= 59}` and all
`d' <= U+2`: 0 violations (laneP3/bookkeep.py).

## Lemma 2 (io u-blocks -> io heavy X-octaves -> E(L), with constants)

Assume the W-pinch lemma: `limsup_T (1/log T) int_1^T u W_u^2 du/u >= c_0' > 0`.
Then for every `eps in (0, c_0')`:

(a) [io heavy X-octaves] There are infinitely many L with
    `int_{2^L}^{2^{L+1}} V^2 dX/X >= (c_0' - eps) ln 2`.
    Proof: by Lemma 1 the limsup transfers to the X side. If only finitely many
    octaves were heavy, then for all J: `int_1^{2^J} V^2 dX/X <= C_eps + (c_0'-eps) J ln2`,
    so `limsup (1/log Y) int_1^Y V^2 <= c_0' - eps`, contradiction (L-105058.5 Cor 2
    argument verbatim).

(b) [octave consumption] For each heavy octave L (with 2^L >= 64):
    `E(L) >= 2 ln2 int_oct Lambda^2 dX/X = 2 ln2 int_oct V^2 (X^{1/3}/log N_X) dX/X
           >= 3 (c_0'-eps) ln2 * 2^{L/3}/(L+2)`,
    using T-105059.5 (exact, unconditional) and, pointwise on the octave,
    `X^{1/3} >= 2^{L/3}` and `log N_X <= log(X^{2/3} * X^{1/3}/U) <= (2/3) log(2X)
    < (2/3) ln 2 * (L+2)` since `N_X <= X/U <= (2X)^{2/3}` and `X < 2^{L+1}` on the
    octave. [CORRECTION, hostile review 2026-08-23: the previously claimed concrete
    form `log N_X <= (2/3) ln 2 * (L+1)` for `2^L >= 64` is FALSE near octave tops —
    e.g. L=8, X=511 (U=7, N=73): ln 73 = 4.290 > (2/3)(9) ln 2 = 4.159; 85 violations
    found for L in 6..39. The `(L+2)` form above is what the argument proves. The
    `(L+1)` denominator is recoverable for large L by absorbing the factor
    `(L+2)/(L+1) = 1 + O(1/L)` into eps; all asymptotics, and the refutation of
    GATE_theta for every theta < 1/3, are untouched.]
    So:  **E(L) >= 3 ln2 (c_0'-eps) 2^{L/3}/(L+2) for infinitely many L.**

(c) [u-block form, as T-105059.5(ii) states it] If instead the io input is given in
    u-octaves — infinitely many j with `int_{2^j}^{2^{j+1}} u W_u^2 du/u >= c` — then by
    Lemma 1 the triple of X-octaves {3j, 3j+1, 3j+2} carries `int V^2 dX/X >= 3c`, so at
    least one of the three has `int_oct V^2 >= c`, and (b) gives
    `E(L) >= 3 c * 2^{L/3}/(L+2)` for some `L in {3j, 3j+1, 3j+2}`. io j gives io L
    (each u-octave's triple is disjoint from every other's). This is T-105059.5(ii)'s
    "each u-octave maps onto 3 X-octaves" claim, now with the pigeonhole and the
    constants written. Note (a)+(b) is the cleaner route and is what T-105070 uses;
    (c) confirms the original phrasing is also correct.

## What was checked for off-by-cell issues (all clean)

1. Floor coherence: `U = floor(X^{1/3})`, `N = floor(X/U)` recomputed on the lane S grid
   (out_big.json, 9 rows, X up to 1e12): all match. `X^{1/3} |log N_X - (2/3) log X|
   <= 0.96` on the grid — the P2.2 rate `O(X^{-1/3})`, confirming the weight replacement
   `sqrt(log N) -> sqrt((2/3) log X)` costs only L2(dX/X)-summable error (consumed by
   P2.2, not needed by Lemmas 1-2, which keep the exact floors).
2. Cube corners: exact (above).
3. Head: `u in [1,4)` (X < 64): `W := 0` by Definition 1; T-105059.5 needs `X >= 64`;
   the omitted mass is a fixed constant, irrelevant to limsups. No hidden mass: for
   `u in [4, T]` everything is covered exactly.
4. Octave alignment: `[2^j, 2^{j+1})` in u maps to exactly `[2^{3j}, 2^{3j+3})` in X —
   octave boundaries in u land ON octave boundaries in X (2^{3j} is a power of 2);
   no partial-octave slivers exist. (This is why the factor is exactly 3.)

## Numerical verification (numeric duty; laneP3/bookkeep2.py)

Direct quadrature with the GENUINE arithmetic field (h_U = (mu 1_{>U})*eta computed by
sieve, tent weights, floors intact), u-octave [20, 40] (X in [8000, 64000]):
independent log-uniform grids, 6000 points in u vs 18000 points in X:

    I1 := int u W_u^2 du/u              = 0.0017534
    I2 := (1/3) int V^2 dX/X            = 0.0017560      rel. diff 0.0015

(pure quadrature noise on a piecewise-constant integrand; any factor slip or cell slip
would show at O(1) or at the 3x scale). Octave decomposition of the X side:
0.0013813 + 0.0022048 + 0.0016818 = 0.0052679 = 3*I2 exactly — the triple-octave
accounting closes with no sliver. Lane S grid checks in laneP3/bookkeep.py as above.

## Statement of record

The measure bookkeeping between the W-pinch lemma's u-normalized limsup and the
gate's X-octave energy is an EXACT identity (Lemma 1) plus a pigeonhole with explicit
constants (Lemma 2): W-pinch with constant c_0' implies
`E(L) >= 3 ln2 (c_0'-eps) 2^{L/3}/(L+2)` for infinitely many L, unconditionally,
with no RH and no unproved input beyond the W-pinch lemma itself. T-105059.5(ii)'s
"closes trivially" is VERIFIED (and the trivially is earned: the exactness is a
consequence of defining W_u on continuous u with X = u^3 — Definition 1, now pinned).
