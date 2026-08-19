# R-99301 — Cumulative compact Hall does not imply the differential Hall gate

Claim ID: `R-99301`  
Status: **PROVED EXACT REFUTATION OF THE L-99301 APPLICATION**  
Created: 2026-08-20  
Frozen target: PR #644 at `7462edcd1f6bb27b00d86853319f2c2ad71401a2`  
RH status: unproved

## 1. The inherited cumulative Hall prefix

For an active odd threshold `t`, the compact factor-67 Hall packet uses

\[
H_t(x)=4\sqrt{x}\,A_t-3B_t,
\qquad
A_t=\sum_{n\le t}\frac{\mu(n)}n,
\qquad
B_t=\sum_{n\le t}\frac{\mu(n)}{\sqrt n}.
\]

The frozen compact theorem certifies `H_t(x)>0` on the relevant cumulative
fibres. This is a statement about the cumulative target packets.

`L-99301` replaces it by a pointwise density statement: after differentiating
in the endpoint parameter, every Hall prefix must remain nonnegative. That
replacement is not valid.

## 2. Exact negative infinitesimal prefix

On every activation-free interval with `x>t`,

\[
H_t'(x)=\frac{2A_t}{\sqrt x}.
\]

At `t=13`, exact Fraction arithmetic gives

\[
\boxed{
A_{13}=\sum_{n\le13}\frac{\mu(n)}n
=-\frac{2323}{30030}<0.
}
\]

Consequently

\[
\boxed{
H_{13}'(x)
=-\frac{2323}{15015\sqrt x}<0
\qquad(13<x<67).
}
\]

Thus the signed infinitesimal target density has a negative Hall prefix on the
whole interval `(13,67)`. No Hall flow can match the endpoint densities
pointwise there while retaining the frozen no-upward neighbourhoods.

The cumulative prefix may remain positive because previously accumulated
activation atoms and mass compensate the negative density. Cumulative Hall and
differential Hall are therefore genuinely different assertions.

## 3. Disposition

```text
compact cumulative Hall inequalities       not refuted
cumulative finite Hall flow                 not refuted
pointwise endpoint-density Hall premise     false for t=13
L-99301 application to the native packet    rejected
PR #644 differential-Hall composition       blocked as written
Riemann Hypothesis                          unproved
```

This refutation does not attack the fixed-row Mellin consumer. The successor
repair projects to one fixed component row first and performs a scalar Bellman
resolution using cumulative Hall independently at each finite state; it needs
no pointwise density Hall flow and no endpoint-nested common parent.
