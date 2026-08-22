# L-105061 — The dipole interface: partial-fraction layer and threshold PROVED; the per-gap count cap OPEN

Claim ID: `L-105061`
Status: **INTERFACE — sub-lemmas [I-PF] and [THRESHOLD] PROVED here; the COUNT CAP is OPEN (pinned statement below; empirical sharp constant 2, pinned A′ = 4 held in every experiment) — RH NOT ADDRESSED**
Created: 2026-08-22
Agent: claude (external reviewer lane; Program B — orchestrator + lane B3; two dedicated proof lanes on the count cap died mid-derivation, incident recorded in §5)
Depends on: `L-105062` §1 (square-variable genus-0 Hadamard product).
Replay: `experiments/X-105060-descent-ladder/` (stress_tests.py, exact_check.py, results_B3.json — 250 exact-arithmetic random ladders + 10 adversarial families, 0 violations).
RH status: **unproved, not addressed**

## 1. Pinned interface statement (the count cap — OPEN)

Let `F = Xi_k`. Real zeros `{t_n}` (multiplicities `m_n`), non-real conjugate
pairs `{x_j ± i y_j}` (`0 < y_j <= 1/2` by the strip lemma; both signs of `x_j`
occur as distinct pairs; multiplicity counted). Gap `G = (a, b)`: a bounded
component of `R \ {real zeros}` (ALL components are bounded — L-105062 §3 +
Hardy + parity), `g = |G|`. Overhang: pair `j` overhangs `G` iff
`x_j - y_j < b` and `x_j + y_j > a`.

**[I-DIPOLE] (OPEN).** There is an absolute constant `A' >= 1` (pinned target
`A' = 4`; empirical sharp value 2) such that for every `k >= 0` and every gap
`G` of `Xi_k`:

```
n'(G) := #{real zeros of Xi_{k+1} in G, with multiplicity}
       <= 1 + A' * Sum_{pairs j overhanging G} min(1, g^2/(4 y_j^2)).
```

Any absolute constant, and any per-(pair,gap) weight shape dominating this one
(e.g. fattened overhang intervals), is accepted verbatim by the downstream
assembly `T-105060` (its summation layer is weight-shape-agnostic).

## 2. [I-PF] Partial-fraction layer — PROVED

**Lemma 2.1.** For real `t` not a real zero of `F`:

```
(F'/F)'(t) = -m_0/t^2 - Sum_n m_n/(t-t_n)^2 + Sum_j m_j phi'_j(t),
phi'_j(t) = 2 (y_j^2 - (t-x_j)^2) / ((t-x_j)^2 + y_j^2)^2,
```

with absolute, locally uniform convergence on `R \ {real zeros}` (`m_0` = the
multiplicity at the origin; pairs with `x_j = 0` — purely imaginary zeros —
appear ONCE, see the proof's final remark).

Proof. By L-105062 §1, `F(t) = c t^{m_0} prod_nu (1 - t^2/tau_nu^2)` with
absolute locally-uniform convergence, `{±tau_nu}` enumerating the nonzero zeros
with multiplicity, one `tau` per `±`-pair, and `sum |tau_nu|^{-2} < infinity`.
On any compact `K` avoiding the real zeros, log-differentiate the partial
products and pass to the limit (Weierstrass: locally uniform convergence of
holomorphic functions gives convergence of derivatives):

```
(F'/F)(t) = m_0/t + Sum_nu 2t/(t^2 - tau_nu^2),
```

the tail dominated by `Sum_{|tau_nu| > 2 max|K|} 4 |t| / |tau_nu|^2 < infinity`.
Differentiate termwise — legitimate since the differentiated series converges
absolutely locally uniformly: `d/dt [2t/(t^2-tau^2)] = -[(t-tau)^{-2} +
(t+tau)^{-2}]`, and for `|tau| >= 2|t| + 1` this is `<= 8/|tau|^2`, summable.
Hence

```
(F'/F)'(t) = -m_0/t^2 - Sum_nu [ (t-tau_nu)^{-2} + (t+tau_nu)^{-2} ].
```

Regroup the absolutely convergent sum by conjugation (the zero multiset is
closed under conjugation since `F` is real on `R`): a real `tau_nu = t_n > 0`
contributes `-(t-t_n)^{-2} - (t+t_n)^{-2}` — the real-zero sum over both signs,
matching the index convention (real zeros indexed over all of `R`). A non-real
`tau_nu = z = x + iy` (`x != 0`) is accompanied in the multiset by
`tau_{nu'} = z-bar`; grouping the four terms of `nu, nu'`:

```
-[(t-z)^{-2} + (t-z-bar)^{-2}] - [(t+z)^{-2} + (t+z-bar)^{-2}]
  = phi'_{(x,y)}(t) + phi'_{(-x,y)}(t),
```

using `-(t-z)^{-2} - (t-z-bar)^{-2} = -2 Re (t-z)^{-2} =
-2[(t-x)^2 - y^2]/((t-x)^2+y^2)^2 = phi'_{(x,y)}(t)`. So the pair sum runs over
pairs at both `±x` — exactly the deposit convention. For a purely imaginary
zero `z = iy`: `±tau` already exhausts `{iy, -iy}`, contributing
`phi'_{(0,y)}` once. Rearrangement is legitimate by absolute convergence. QED.

(For polynomials the identity is exact algebra; verified numerically to rel.
err ≤ 4e-10 across the replay's synthetic configurations.)

## 3. [THRESHOLD] — PROVED

On a gap `G = (a,b)`, `t in G`, write `B(t) = Sum m_n (t-t_n)^{-2} (+ m_0/t^2)`
and `Phi'(t) = Sum_j m_j phi'_j(t)`.

**Lemma 3.1 (background repulsion).** `B(t) >= 1/(t-a)^2 + 1/(b-t)^2 >= 8/g^2`
on `G` (keep the endpoint terms; minimize at the midpoint).

**Lemma 3.2 (support).** `phi'_j > 0` exactly on `int I_j`,
`I_j = [x_j - y_j, x_j + y_j]`; `max phi'_j = phi'_j(x_j) = 2/y_j^2`;
`min phi'_j = phi'_j(x_j ± sqrt3 y_j) = -1/(4 y_j^2)`. (Elementary calculus.)

**Lemma 3.3 (threshold).** If `(F'/F)'` has a zero at `t* in G`, then
`Sum_{j overhanging G} min(1, g^2/(4 y_j^2)) >= 1`.
Proof: at `t*`, `Phi'(t*) = B(t*) >= 8/g^2`; only `j` with `t* in int I_j`
contribute positively, each at most `2/y_j^2`; so
`Sum_{those j} g^2/(4 y_j^2) >= 1`, and `Sum min(1, c_j) >= min(1, Sum c_j)`.
Those `j` overhang `G`. QED.

**Corollary 3.4 (qualitative dipole).** If `n'(G) >= 2` then the gap weight is
`>= 1`. Proof: real zeros of `Xi_{k+1}` in `G` are zeros of `F'/F` there (same
multiplicities; `F != 0` on `G`); `z >= 2` zeros force a zero of `(F'/F)'` in
`G` (multiplicity drop + Rolle between distinct zeros); apply Lemma 3.3. QED.

Consequence: the count cap needs proving only on gaps of weight `>= 1`, so ANY
bound of the additive form `extra(G) <= A' * weight + A''` upgrades to the
multiplicative form with constant `A' + A''`. This is the safety net a
successor should use.

## 4. Numerical state of the count cap (exact arithmetic; replay)

- 10 deterministic adversarial configs (pair overhanging six gaps; pair
  annihilation ×4; double/triple real zeros; double pair; deep pair `y = g`;
  tiny pair) + 250 exact-rational random ladders (60-dps root classification):
  **zero violations** of `A' = 4`; per-gap parity (`n'(G)` odd) always holds.
- Extremal family: stacked near-real pairs give `extra = 2m` from `m` pairs of
  weight 1 each — ratio exactly **2**. Cooperation of `m = 3..10` pairs at the
  strip cap `y = 1/2` over `g = 0.6` SATURATES at `extra = 2` (one merged dip),
  ratio ≤ 1.85 decreasing in `m`. Working conjecture: sharp `A' = 2`.
- float64 root classification produced 6 spurious "violations" (one
  parity-impossible); all vanished in exact arithmetic — exact/high-precision
  classification is mandatory (replay discipline).

## 5. Obstruction ledger for the count cap (recorded for successors)

(i) **Monotone-run counting is false in general**: "solutions of `f = g` with
`g` strictly increasing ≤ 1 + increasing runs of `f`" fails — `f` and `g` can
both increase and cross many times; any proof must control derivative
crossings, not runs. (ii) **Second-Rolle regress does not terminate**: bounding
zeros of `(F'/F)'` by zeros of `(F'/F)''` recurses; the sign-structure of
`Re(t-z)^{-m}` localizes to bands only at even `m`, and band widths grow
linearly in the level, so the regress escapes the gap's neighborhood for
high-multiplicity degeneracies. (iii) **Jensen/disk counting** (poles-plus-
winding on `D(c, 2|C|)` around an excited component `C`) yields a cap with the
weight shape `log(2 + g/y_j)` and disk-fattened pair sets — every pair in the
disk has capped weight `>= 1/16`, but a single tiny-`y` pair is over-charged
`log(g/y)` against its true `extra <= 2`; route sketched, not completed, and
NOT deposited. (iv) Two dedicated proof lanes on this lemma terminated by
exceeding the per-response output ceiling mid-derivation (process incident,
2026-08-22, recorded per failure-ledger discipline): the problem reliably
provokes unbounded single-pass derivations; successors should decompose
(single-pair case; bounded-cooperation case; assembly) before attempting.

## 6. Falsifiers

A gap with `extra(G) >= 1` and total overhanging weight `< 1` (refutes Lemma
3.3, hence [I-PF] or the strip lemma — checked never in 260+ exact configs); a
per-gap ratio `extra/weight > 4` (refutes the pinned constant; the assembly
re-runs with any valid `A'`); failure of the partial-fraction identity on a
synthetic polynomial configuration (it is exact algebra there).
