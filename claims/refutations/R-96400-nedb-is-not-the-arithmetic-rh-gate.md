# R-96400 — Endpoint-blocker localization is not the arithmetic RH gate

Claim ID: `R-96400`  
Status: **PROVED EXACT NORMALIZATION FIREWALL / NONIMPLICATION**  
Created: 2026-08-17  
Frozen comparison inputs: PR #530 at `6c818a35094b978863a08bde4227d1f4ad9b65d4`; PR #541 normalization review  
RH status: **unproved**

## 1. Three distinct quantities

For the endpoint-detail compiler, let

\[
s_X(q)=\Omega_X(q)-\Xi_{d_X}(q)\ge0
\]

and define its packing slack

\[
\mathfrak P_X=\langle Y_4,s_X\rangle
=P_\Lambda(X)-\mathcal H(d_X).
\]

The arithmetic discrepancy is

\[
F_\Lambda(X)=J_\Lambda(X)-P_\Lambda(X).
\]

The full signed score loss is therefore

\[
\boxed{
J_\Lambda(X)-\mathcal H(d_X)
=
F_\Lambda(X)+\mathfrak P_X.
}
\tag{R-96400.1}
\]

This is an identity. It is not an estimate and no positivity of `F_Lambda` is
asserted.

## 2. What `B_X` controls

Let

\[
B_X=\max\{q:s_X(q)>0\}.
\]

The endpoint compiler proves

\[
B_X\le B\le X/4
\Longrightarrow
\mathfrak P_X
<
32(\log 2)^2\sqrt B.
\tag{R-96400.2}
\]

Thus

\[
B_X=o(\log^4X)
\Longrightarrow
\mathfrak P_X=o(\log^2X).
\]

It gives no bound on `F_Lambda`.

## 3. Exact nonimplication

Fix any endpoint target `Omega_X`, any compiler row `d_X`, and therefore the
same `s_X`, `B_X`, and packing slack. Replace the arithmetic benchmark by

\[
J_\Lambda^{(G)}(X)=P_\Lambda(X)+G(X)
\]

for an arbitrary scalar function `G`. All packing data are unchanged, while

\[
J_\Lambda^{(G)}(X)-\mathcal H(d_X)
=
G(X)+\mathfrak P_X.
\]

Taking `G(X)=log^3 X`, for example, proves formally that no theorem whose
hypotheses mention only `B_X`, `Omega_X`, the detail matrix, and the greedy
coefficients can imply a subquadratic full arithmetic deficit.

This is a type-level nonimplication, not a statement that the actual arithmetic
`F_Lambda` equals an arbitrary function.

## 4. Disposition

The requested statement

\[
B_X=o(\log^4X)
\]

is not promoted in this successor. Finite reconnaissance also shows that
`B_X` is an unstable location statistic: a macroscopic last slack coordinate
can carry a tiny weighted mass. Those computations are retained only as
diagnostics.

The successor bypasses both `B_X` and `F_Lambda` by using fixed component rows
whose Mellin transforms carry the reciprocal-zeta poles directly.

```text
packing slack                         physical / nonnegative
F_Lambda                              separate arithmetic term
B_X                                  packing-support statistic
B_X alone -> RH                       false as a logical implication
fixed-row Mellin route                independent of this normalization
Riemann Hypothesis                    unproved pending review
```
