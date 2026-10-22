# Three-route attack on the live row-provenance theorem

Date: 2026-08-13  
Branch: `review/gpt56-pro/91304-direct-row-score-audit`  
PR: `#436`  
Status: **RH UNPROVEN; THREE INDEPENDENT FINITE/EFFECTIVE FRONTS**

## New exact results

`L-91410` proves an inner/outer secant barrier: every child-active row/score ratio is at least every frontier ratio.

`L-91411` reduces literal Lorenz row provenance to one actual-cutoff determinant

\[
\Delta_{j,c}=R_{sig}^{(j)}S_c-S_{sig}R_c^{(j)}.
\]

`L-91412` proves that its centered source kernel has one sign change at the cutoff.

`L-91413` proves causal-ratio monotonicity before the child row activates.  The genuinely active-child discrete ordering family is confined to rows `2,...,33` and finitely many small divisors.

`L-91415` proves the exact transport identity

\[
R_{sig}-R_{res}=\sum_{o,e}t_{o,e}(q_e-q_o).
\]

`X-91411` supplies a new proof-grade finite certificate for the reciprocal limiting score measures:

```text
262144 source states;
minimum radius-eight prefix margin >1/100;
131203 exact greedy-flow pieces;
maximum upward displacement 8;
square-root transport moment >18.
```

The retained moment is approximately `18.538552495926712`.

## Route A — actual-cutoff determinant

The proposed fixed-row asymptotic is

\[
\Delta_{j,c}(p,y)
=5(-\lambda_j)\sqrt y(A/\sqrt c-B/c)
 \sqrt p\log p+O(\sqrt p),
\]

with strictly positive coefficient.  Remaining work:

1. an explicit uniform remainder and transition height;
2. a directed compact-cell replay.

## Route B — discrete Monge/full determinant

The cross-interface and inactive-child orderings are exact.  Every fixed arithmetic pair has proposed positive asymptotic gap

\[
\frac{(-\lambda_j)\log p}{5\sqrt{py}}(\sqrt o-\sqrt e).
\]

The stronger full determinant also has a positive proposed `sqrt(p) log(p)` coefficient.  Remaining work:

1. effective pairwise remainder;
2. finite active-child ordering replay;
3. compact full-determinant replay.

## Route C — canonical shifted-eight flow

The exact reciprocal-limit moment yields the proposed tail law

\[
R_{sig}^{(j)}-R_{res}^{(j)}
=(-\lambda_j)M_\infty\log p+O_j(1),
\qquad M_\infty>18.
\]

Remaining work:

1. explicit perturbation stability from finite causal scores to reciprocal scores;
2. an effective transition height;
3. a compact greedy-flow cell replay.

## Empirical cross-check

`X-91410` is explicitly non-proof binary64 reconnaissance on 120 sparse-grid cases. It found positive values for the actual cutoff determinant, full determinant, literal Lorenz row gap, inner discrete-order gap and shifted-eight greedy gain.

## Boundary

```text
new analytic reductions and exact limit certificate  PUSHED
three positive unbounded-tail mechanisms              PROPOSED / PARTLY CERTIFIED
one effective all-parameter certificate                OPEN
literal row provenance                                 OPEN
factor-54 composition                                  CONDITIONAL
Riemann Hypothesis                                     UNPROVEN
```
