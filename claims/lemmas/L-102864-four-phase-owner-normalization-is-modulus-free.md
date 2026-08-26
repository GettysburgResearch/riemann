# L-102864 — Four owner phases remove every explicit owner-weight loss

Claim ID: `L-102864`  
Status: **PROVED UNCONDITIONAL FIXED-QUADRUPLE ESTIMATE**  
Created: 2026-08-24  
Depends on: `L-102839`, `L-102862--L-102863`  
RH status: **not assumed**

Retain the clean four-owner sector

\[
N=pq\,a^2,
\qquad
M=rs\,b^2,
\]

with `p>q`, `r>s`, four distinct owners, and no owner in the opposite square
core. Put

\[
A\le a<2A,
\qquad
B\le b<2B.
\]

Use the two nonzero owner phases modulo `r` and `s` on the `N` field, and the
two nonzero owner phases modulo `p` and `q` on the `M` field. Since each prime
Ramanujan sum equals `-1`, their product is `+1`. Hence the original cross term
has an exact four-phase representation.

Let

\[
F_{k_1,k_2}^{(N)}
\]

be the `N`-side field with phases modulo `r,s`, including the coefficient
`(pq)^(-1/2)`, and let

\[
F_{h_1,h_2}^{(M)}
\]

be the `M`-side field with phases modulo `p,q`, including `(rs)^(-1/2)`.

## 1. Product-modulus energies

By `L-102839`,

\[
\boxed{
\sum_{k_1,k_2}
\|F_{k_1,k_2}^{(N)}\|_2^2
\ll_\phi
{1\over pq}\left(1+{rs\over A}\right),
}
\tag{L-102864.1}

and

\[
\boxed{
\sum_{h_1,h_2}
\|F_{h_1,h_2}^{(M)}\|_2^2
\ll_\phi
{1\over rs}\left(1+{pq\over B}\right).
}
\tag{L-102864.2}

The sums may be restricted to nonzero coordinates without increasing them.

## 2. Exact four-owner cancellation

Cauchy over the four phase coordinates gives

\[
\begin{aligned}
|\mathcal C_{P,Q}|
&\le
\left(rs\sum_{k_1,k_2}
\|F_{k_1,k_2}^{(N)}\|_2^2\right)^{1/2}\\
&\qquad\times
\left(pq\sum_{h_1,h_2}
\|F_{h_1,h_2}^{(M)}\|_2^2\right)^{1/2}.
\end{aligned}
\]

Substituting (L-102864.1)--(L-102864.2), all four literal owner weights cancel
all four phase-cardinality factors:

\[
\boxed{
|\mathcal C_{P,Q}|
\ll_\phi
\left(1+{rs\over A}\right)^{1/2}
\left(1+{pq\over B}\right)^{1/2}.
}
\tag{L-102864.3}

Thus the fixed-quadruple long-core packet is completely modulus-free. In the
regime

\[
A\ge rs,
\qquad
B\ge pq,
\]

one has simply

\[
\boxed{|\mathcal C_{P,Q}|\ll_\phi1.}
\tag{L-102864.4}

## Scope

The theorem removes every explicit owner-size loss for one clean quadruple.
It does not sum the normalized packets coherently over all semiprime
squareclasses. `R-102840` shows why that last operation is not source-blind;
`T-102870` isolates the exact arithmetic sum.