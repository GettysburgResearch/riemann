# L-105671 — Any CTI counterexample is an intermediate stationary contact

**Claim ID:** `L-105671`  
**Status:** proved exact reduction  
**Date:** 2026-08-31  
**Depends on:** `L-105661`, `L-105670`  
**RH:** not assumed

For a finite Cauchy packet define

\[
F(H)=\mathcal O_H-\mathcal T_H,
\qquad H>0.
\]

The function is real analytic. `L-105661` proves `F(H)>0` for all sufficiently
small positive `H`; `L-105670` proves the same for all sufficiently large
`H`. Rank one and rank two are already known to satisfy CTI at every height.

Therefore any failure of general CTI must have all of the following
properties:

```text
packet rank at least three;
height bounded away from both zero and infinity;
a negative connected component of F;
an interior negative minimum H_*;
F(H_*)<0 and F'(H_*)=0;
at least two positive-height zeros of F surrounding that component.
```

This turns the remaining all-rank problem into an intermediate-scale contact
problem rather than an endpoint or conditioning problem.

## Exact contact ledger

Put

\[
M_s=\left[(\overline\lambda_i+\lambda_j+s)^{-2}\right]_{i,j},
\qquad G_s'= -M_s.
\]

Differentiation of

\[
\mathcal O_H=\operatorname{tr}
 (G_0^{-1}G_{2H}G_{4H}^{-1}G_{2H})
\]

gives

\[
\boxed{
\begin{aligned}
F'(H)={}&\operatorname{tr}(G_0^{-1}M_H)\\
&-4\Re\operatorname{tr}
 (G_0^{-1}M_{2H}G_{4H}^{-1}G_{2H})\\
&+4\operatorname{tr}
 (G_0^{-1}G_{2H}G_{4H}^{-1}
 M_{4H}G_{4H}^{-1}G_{2H}).
\end{aligned}}
\tag{L-105671.1}
\]

Thus an interior stationary contact obeys the two explicit scalar equations

\[
\boxed{
\operatorname{tr}
 (G_0^{-1}G_{2H}G_{4H}^{-1}G_{2H})
 =\operatorname{tr}(G_0^{-1}G_H),
}
\tag{L-105671.2}
\]

and

\[
\boxed{
\begin{aligned}
\operatorname{tr}(G_0^{-1}M_H)
&+4\operatorname{tr}
 (G_0^{-1}G_{2H}G_{4H}^{-1}
 M_{4H}G_{4H}^{-1}G_{2H})\\
&=4\Re\operatorname{tr}
 (G_0^{-1}M_{2H}G_{4H}^{-1}G_{2H}).
\end{aligned}}
\tag{L-105671.3}
\]

No matrix order is assumed.

## Symmetry reductions

For every `c>0`,

\[
F_{c\lambda}(cH)=F_\lambda(H),
\tag{L-105671.4}
\]

because every Cauchy Gram acquires the same scalar factor `c^{-1}`. A common
horizontal translation

\[
\lambda_j\mapsto\lambda_j+i\alpha
\]

also leaves all `G_s` unchanged. A hostile search or proof may therefore
normalize one positive scale and one horizontal origin before attacking
(L-105671.2)--(L-105671.3).

## Consequence

A proof that the contact system (L-105671.2)--(L-105671.3) has no solution
with `F<=0` would establish arbitrary-rank CTI. Conversely, a counterexample
must be a genuine finite intermediate-scale geometric obstruction; it cannot
escape through a confluent endpoint, large translation, global rescaling, or
common phase translation.

## Scope

The lemma does not rule out the stationary contact system. It supplies the
exact smallest surviving finite obstruction after the two endpoint theorems.