# L-105031 — The maximal transport license: exact reduction, removal of the 87.36 cap, equivalence with the signed rows, and the log-cost of score debt

Claim ID: `L-105031`
Status: **PROVED EXACT REDUCTION + MAXIMALITY + FINITE-RANGE FEASIBILITY (x ≤ 10⁶) + FROZEN-BLOCK BALANCE CLOSED FOR ALL x; the arithmetic core is OPEN and stated as such**
Created: 2026-08-21
Agent: claude (external reviewer lane)
Depends on: `L-99020` (system + downstream contract) @
`review/gpt56-pro/99600-three-interface-hostile-audit`; `L-99240` (kernel
`κ_j`) @ `review/gpt56-pro/99440-half-order-subsidy-audit`; `L-105001 §1`
(derivative engine), `L-105021` (nested cap), `L-105022` (quarantine),
`T-105030` (escape pricing). Replay:
`experiments/X-105030-maximal-license-and-circ13/lane_repair/`.
RH status: **unproved, not addressed**

## 1. The aggregate license (the repair proposal)

Adjudicated downstream contract of `L-99020` (§§2–3, re-audited): only the
per-`(x,j)` aggregates `B_{x,j} ≥ 0`, the score inequality `L-99020.7`,
and `u ≥ 0` are consumed; the per-edge nonnegativity of `L-99020.6` was
the nested proof device (its word "coefficientwise" must be restated; the
sort discipline, the `x = 2` firewall, and `R-99020` @
`review/gpt56-pro/99820-native-box-normalization-audit` are preserved
verbatim — full audit in the deposit report). The **aggregate license**
admits flows on all pairs subject to demand equality, capacity, and three
aggregates: `B_{x,2} ≥ 0`, `B_{x,3} ≥ 0`, score edge term `≤ 0`. Honest
new label: *score-constrained transport, score-free row sort*.

## 2. Theorem R (exact reduction; proved unconditionally)

The system sees a flow only through its column sums `c(e) = Σ_o t(o,e)`:
any admissible column profile is realized by the product flow
`t(o,e) = T(o)c(e)/D`; the aggregates are affine in `c`; and since
`ρ_2, ρ_3` are nonincreasing in `k` (reproved from the integral
representation via the `L-105001 §1` derivative — Lemma 1 of the deposit)
while `s(k) = 5/4 + (3/4)/(4√(x/k) − 3)` is increasing (Lemma 2), the
**greedy prefix fill `c*`** simultaneously weakly maximizes both row
aggregates and weakly minimizes the score aggregate. Hence:

```
aggregate-licensed feasibility at fibre x
   <=>   TB(x) >= 0  and  c* passes the three aggregate tests,
```

decidable in `O(x)` exact arithmetic — no LP. Closed forms (Corollary R.1,
all machine-verified):
* `TB(x) = 4√x·A_x − 3B_x` (balance);
* row margins `M_j(x) = G_j(x)` **exactly** for all `x ≥ 47` (`j = 2,3`),
  where `G_j(x) = Σ_{k≤x} μ(k)Q_{x/k}(j)k^{-1/2}` **is the signed compact
  row**; with the exact regrouping `G_j(x) = C_j log x +
  Σ_{q≤j+1} δ_j(q)q^{-1/2}W(x/q)`, `W(y) = Σ_{m≤y}μ(m)log(y/m)m^{-1/2}`,
  effective slopes `1.1117` (j=2), `0.4065` (j=3);
* score margin `M_sc(x) = (3/4)[−B_x + Σ_e(1−θ*(e))e^{-1/2}]` exactly,
  with proved floor `−(3/4)B_x` whenever `TB(x) ≥ 0`.

## 3. Results

**(a) The `L-105021` cap is removed.** At cuts
`C ∈ {89, 101, 149, 211, 401, 1009, 4001, 10007}` and at every integer
fibre `x ≤ 10⁶`: **zero infeasible fibres** (nested-infeasible counts at
the same cuts: 2, 14, 62, 124, 314, 922, 3914, 9920). Margins: rows grow
like `c_j log x`; score and balance stabilize (`≈ 2.0`, `≈ 2.05`, bounded
oscillation; the score aggregate binds at 9972 of 10005 fibres). Greedy
criterion cross-checked against full pair-variable LPs (≤ 94,000
variables) to `8.3·10⁻¹³`.

**(b) Crossing law (exact).** The anti-monotone mass crossing threshold
`t` equals `(−H_t(x))₊` — the nested deficit *is* the anti-monotone
traffic, threshold by threshold; at `x = 10007⁻` the crossings are
concentrated exactly on the `L-105022` quarantine set (then the rough
negatives, first family `t = 114`), all spans `e/o ≤ 1.429`, total
anti-monotone mass `188.755 = 16.47%` of demand.

**(c) Debt is log-cheap (proved increment lemma).** Profile increments
obey `0 ≤ ρ_j(Y) − ρ_j(Y') ≤ 3κ̄_j log Y'[1/T(Y') − 1/T(Y)] +
2κ̄_j[Y'^{-1/2} − Y^{-1/2}]` with `κ̄_2 = 3/√2`, `κ̄_3 = 2/√3` (proved
sup of the kernel); hence total row debt of the quarantine-adjacent
anti-monotone traffic is `O(log x)` — measured `0.6927`/`0.2580` (rows
2/3) vs nested bonuses `10.867`/`3.939` at `x = 10007⁻`. **Sharpening of
`T-105030(iii)`: the escape must carry `Θ(√X)` mass, but its ledger cost
is only `Θ(log x)`.**

**(d) Honest correction (recorded).** The design hope "finance with
`Θ(√x)` nested row bonus from long edges" is **false**: `A_x → 0` starves
`e = 1`'s spare capacity; the maximal attainable row bonus is exactly
`G_j(x) = Θ(log x)`. The theorem survives because the debt is also
`O(log x)` with a smaller constant — but the margin is `c_j log x`, not
`c√x`.

**(e) The circularity finding (the sharpest self-attack, stated
plainly).** By Theorem R, aggregate feasibility is *equivalent* to
`{TB(x) ≥ 0, G_2(x) ≥ 0, G_3(x) ≥ 0, M_sc(x) ≥ 0}` — and `G_j` **is**
the signed compact row. The maximal license does not derive row
positivity; it re-expresses it. **Theorem D (maximality):** these
conditions are necessary for **any** license keeping demand equality,
capacity, and the downstream contract — no transport license can do
better, so this is the true boundary of the entire transport technology,
priced exactly. The value of the repair: (i) the `87.36` cap is proved to
be a license artifact; (ii) the LP-feasibility family collapses to four
explicit arithmetic inequalities with proved closed forms and measured
margins; (iii) any future failure would be a failure of the consumer
contract itself, not of transport.

**(f) The frozen 61-smooth block: balance closed for ALL x
(unconditional).** Complete `2^{18}`-cell enumeration proves
`TB_s(x) = 4√x A^s_x − 3B^s_x ≥ 1.676601032…` for **every real
`x ∈ [2, P_61]`** (infimum at `x → 33⁻`), growing like `0.5263√x` beyond —
`L-105022`'s quarantine doing exactly the work it was deposited for. The
frozen rows/score margins grow (`m_2 = 106.2`, `m_3 = 39.4`,
`m_sc = 10.7` at `x = 10⁶`); their all-`x` statement is again a finite
lattice computation, flagged as completable and not executed.

## 4. Honest boundary

Uniform-in-`x` feasibility of the full-support system is **equivalent**
(Theorem R + D) to the four arithmetic inequalities; those are
sign-uniformity statements about weighted Mertens-type sums with `O(1)` or
`O(log x)` margins against oscillations of comparable eventual size — the
open core, not provable with current technology, and **not claimed**. No
step of Theorems R, D, the identities, the crossing law, or the increment
lemma is numerics-dependent; Theorem F (the `x ≤ 10⁶` range) and the
`x ≥ 47` sliver crossover are finite verifications. Nothing here bears on
RH.
