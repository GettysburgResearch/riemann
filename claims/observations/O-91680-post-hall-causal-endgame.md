# O-91680 — Post-Hall causal endgame after arithmetic tail closure

Claim ID: `O-91680`  
Status: **CURRENT EXACT BOUNDARY / REVIEW HANDOFF**  
Created: 2026-08-14  
RH status: **unproved**

## Freeze

```text
parent PR:      #458
parent head:    c8cd1e53e7ad96d3c43f213813e0ae0688341015
branch:         research/gpt56-sol/91680-causal-proportional-tail
```

## 1. What must remain withdrawn

PR #456 gives exact infinite counterexamples to the branchwise no-upward Hall producer used in the former direct-row proof proposal. Therefore none of the following may be used as a proof step:

```text
separate survival Hall;
separate hazard Hall;
leafwise summation of those Hall outputs;
the resulting claim that the native signed row is globally positive.
```

The exact one-prime target/score/row cocycle survives. The failure is in the subsequent projection.

The complete canonical `P_61` row is also not a current-only bypass: its excess response is exactly the rough-child reservoir. Treating that row as current while also passing the child duplicates capacity.

## 2. New explicit producer

`L-91680` replaces Hall by one canonical source-faithful ray. For the even and odd target totals `E_T,O_T`, retain the positive source

\[
 \nu=\left(1-\frac{O_T}{E_T}\right)E.
\]

It has exactly the signed target. Every physical coordinate is subordinate precisely when its full target-normalized determinant is nonnegative:

\[
 O_TE_\alpha-E_TO_\alpha\ge0.
\]

The native-score debt is explicit:

\[
 \mathfrak d_S
 =\frac{[O_TE_S-E_TO_S]_+}{E_T}.
\]

Thus the post-Hall BARC problem no longer requires an existential search over all nonnegative template coefficients. One explicit source ray is sufficient if its determinant and aggregate-debt gates hold.

## 3. Unbounded causal order is closed

`L-91681/X-91681` exploit the fact that actual child-active arguments are `y/d`, with distinct integer divisors. Their minimum logarithmic separation is

\[
 \log(66/65).
\]

This gap dominates the `O(p^{-1})` causal child perturbation once `p>=500000`. The exact directed replay proves strict row-per-score ordering for every row `2<=j<=66` at `p=500000`; monotonicity extends it to the complete real tail.

Combining with `L-91359` gives the complete divisor order in all three sectors:

```text
child-active / child-active;
child-active / child-inactive;
child-inactive / child-inactive.
```

Therefore the continuous counterexample in `R-91311` is no longer an infinite arithmetic obstruction.

## 4. Remaining finite theorem

The post-Hall producer is reduced to the following finite/direct arithmetic package.

### Gate A — finite causal profile corridor

Prove the divisor order for

\[
 67\le p<500000,
 \qquad1\le y<67,
 \qquad d\mid P_{61},
 \qquad2\le j\le66.
\]

All activation changes occur on a finite algebraic cell complex. A directed cell replay must return either positive slack on every cell or an exact arithmetic counterexample.

### Gate B — full physical determinants

For every leaf and every physical coordinate `alpha`, prove

\[
 O_TE_\alpha-E_TO_\alpha\ge0.
\]

The coordinate family must include the complete literal row, ordinary response, radix-four detail response and the declared shared-port usage in one normalization.

The Lorenz alternative replaces this gate by the score-normalized full determinant of `L-91358`, after Gate A.

### Gate C — aggregate score debt

For the target-proportional producer, prove

\[
 \sum_v
 \frac{[O_{v,T}E_{v,S}-E_{v,T}O_{v,S}]_+}{E_{v,T}}
 \le C
\]

per generation, or another summable bound compatible with the fixed-67 recursion. A pointwise finite debt is insufficient.

### Gate D — one-use root/current normalization

After A--C, identify the resulting stopped-leaf source with the same root equality packet consumed by the continuum score front door. Quantization, collar, omission, mismatch, port and recursive child must each have one owner.

This is the root bridge already isolated on PR #459, now with the false Hall producer removed from its antecedents.

## 5. Implication after the gates

On the frozen surviving imports, A--D give one nonnegative physical current row and one same-index contracted child with

\[
 \operatorname{Loss}_X
 \le
 \operatorname{Loss}_{X/67+C_0}+C.
\]

Iteration gives `O(log X)` loss. The finite dual and the frozen prime-square/Mellin--Landau endpoint consumer then give the proposed RH conclusion.

No downstream implication may be invoked before A--D are reconstructed in the same typed packet.

## 6. Exact status

```text
branchwise stopped-leaf Hall                    FALSE / WITHDRAWN
canonical P_61 row as current-only bypass       FALSE / CHILD OVERDRAW
target-proportional source producer             EXACT / L-91680
continuous causal ratio monotonicity            FALSE / R-91311
arithmetic causal order for p>=500000           EXACT / L-91681
finite causal corridor                          OPEN / DIRECTED FINITE
full target- or score-normalized determinants   OPEN / FINITE-ANALYTIC
aggregate native-score debt                     OPEN
one-use root equality realization               OPEN
Riemann Hypothesis                              UNPROVED
```
