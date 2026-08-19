# L-99703 — Critical tilt energy is logarithmic, but the squarefree owner martingale is degenerate

Claim ID: `L-99703`  
Status: **PROVED EXACT ENERGY THEOREM + BINDING FIREWALL**  
Created: 2026-08-20  
Depends on: `L-99702`; PR #570 `L-97102`  
RH status: **not assumed**

Let

\[
\mathcal E_\tau(X)
=
\sum_{2\le n\le X}
\frac{\beta(n)^2}{g(n)n^{1+2\tau}},
\qquad \tau\ge0.
\tag{L-99703.1}
\]

Writing `n=67^e m`, with `(m,67)=1`, the only nonzero local fibres are

\[
\begin{array}{c|ccc}
e&0&1&2\\ \hline
\beta(67^em)/\mu(m)&1&-2&1\\
g(67^em)&1&2&3.
\end{array}
\]

Consequently

\[
\boxed{\frac{\beta(n)^2}{g(n)}\le2.}
\tag{L-99703.2}
\]

Finite Tonelli gives

\[
\begin{aligned}
\int_0^\infty\mathcal E_\tau(X)\,d\tau
&=
\sum_{2\le n\le X}
\frac{\beta(n)^2}{2g(n)n\log n}\\
&\le
\sum_{2\le n\le X}\frac1{n\log n}.
\end{aligned}
\tag{L-99703.3}
\]

The decreasing-integrand comparison yields, for `X>=3`,

\[
\boxed{
\int_0^\infty\mathcal E_\tau(X)\,d\tau
\le 2+\log\log X.
}
\tag{L-99703.4}
\]

Thus the complete tilt direction has only logarithmic-square coefficient
energy.

## The binding degeneracy

Put `f(n)=beta(n)/g(n)`. The logarithmic-owner probabilities make
`(-1)^t f(N_t)` a bounded martingale. On every squarefree `n` coprime to 67,

\[
g(n)=1,
\qquad
f(n)=\mu(n)\in\{-1,1\}.
\]

Every admissible owner removes one prime, so

\[
f(n/p)=-f(n).
\]

Hence

\[
(-1)^{t+1}f(N_{t+1})=(-1)^tf(N_t)
\]

on the complete squarefree trajectory. Its martingale quadratic variation is
**zero** there. Standard Doob, Burkholder, or variance inequalities therefore
cannot create cancellation on the dominant parity sector.

This firewall explains why (L-99703.4) does not prove `TOCE67`. A successful
boundary estimate must use covariance **between source roots and multiplicative
scales** before the source index is collapsed. It may not cite within-chain
martingale variance as the missing parity cancellation.

```text
critical integrated tilt energy          O(log log X)
squarefree within-chain variance          exactly zero
ordinary Doob-to-sign inference           invalid
source-root / boundary Carleson estimate  still open
```
