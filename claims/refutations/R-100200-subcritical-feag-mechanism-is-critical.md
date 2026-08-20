# R-100200 — Summable \(p^{-3/2}\) label mass is not a closure mechanism for FEAG99980

Claim ID: `R-100200`  
Status: **REFUTATION OF A PROOF MECHANISM; FEAG99980 ITSELF REMAINS OPEN**  
Created: 2026-08-20  
Depends on: `L-100200`

The quadratic envelope of PR #672 is written with coefficients
\(p^{-3/2}\). It is tempting to combine

\[
\sum_p p^{-3/2}<\infty
\]

with one-prime or pairwise positivity and infer an all-prime contraction.

This inference is invalid at the conclusion-facing normalization. The exact
identity

\[
\prod_p(I-p^{-3/2}U_p)f(y)
=
y^{-1/2}\prod_p(I-p^{-1}U_p)\widetilde f(y)
\]

converts the source to the divergent prime-harmonic scale. Moreover

\[
\widetilde f=G-\mathbf1_{[1,\infty)}
\]

with \(G\) globally increasing, and the step contributes exactly

\[
A_\beta(y)=\sum_{n\le y}\frac{\beta(n)}n.
\]

Consequently:

```text
one-prime positivity                  survives;
two-prime positivity                  survives;
fully coactive explicit formulas      survive;
summable-label all-prime contraction  does not follow;
FEAG99980                              remains open.
```

Any successful proof of FEAG must control the critical activation prefix or
supply phase-sensitive cancellation before the half-order collapse. Pairwise
positivity and \(\sum p^{-3/2}<\infty\) do not do so.
