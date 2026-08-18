# R-98060 — The native `p=67` future-state ratio is not cellwise monotone

Claim ID: `R-98060`  
Status: **PROVED DIRECTED FINITE COUNTEREXAMPLE TO A MECHANISM**  
Created: 2026-08-18  
Depends on: `L-98060`; the exact `P_61` annular coefficient dictionary  
Replay: `X-98060-curvature-coboundary`  
RH status: **unproved**

Let `b=F_61` be the repaired annular base and put

\[
h(Y)={b(Y)\over\sqrt Y}.
\]

Let the complete future state after omitting the prime `67` be

\[
V(Y)=
\sum_{\substack{m\ {m squarefree}\\P^-(m)\ge71}}
{\mu(m)\over m}h(Y/m).
\tag{R-98060.1}
\]

The profile ratio proposed in `M-98050` at the first root edge is

\[
Q(Y)={V(Y/67)\over V(Y)}.
\tag{R-98060.2}
\]

On every open activation cell, write `D=d/d log Y` and define

\[
W(Y)=(DV)(Y/67)V(Y)-V(Y/67)(DV)(Y).
\tag{R-98060.3}
\]

Where `V(Y)>0`,

\[
{d\over d\log Y}Q(Y)={W(Y)\over V(Y)^2}.
\tag{R-98060.4}
\]

The exact coefficient generator is finite on each of the following cells.
Outward interval evaluation at 80 decimal digits gives

\[
\begin{array}{c|c}
Y & W(Y)\\ \hline
869/2 &
[0.0430062368642329344555,\ 0.0430062368642329344556]\\
871/2 &
[-0.0245469464584303259107,\ -0.0245469464584303259106]\\
875/2 &
[0.0426715647933337576189,\ 0.0426715647933337576190].
\end{array}
\tag{R-98060.5}
\]

At the negative fixture `Y=871/2`, the same directed computation gives

\[
\begin{aligned}
0.5213&<V(Y)<0.5214,\\
4.8953&<V(Y/67)<4.8954,\\
9.3894&<Q(Y)<9.3896<67.
\end{aligned}
\tag{R-98060.6}
\]

Thus the denominator is strictly positive and the derivative sign is genuine.
The ratio increases, then decreases, then increases again across three nearby
activation cells.  Consequently each of the following proposed shortcuts is
false at its literal native-source scope:

```text
Q(Y,67) is cellwise nondecreasing;
Q(Y,67) is cellwise nonincreasing;
Q(Y,67) has one global derivative sign;
a one-crossing derivative argument proves PRMP67.
```

The counterexample does **not** violate the desired Bellman bound.  Indeed its
ratio is far below `67`.  It refutes only the scalar monotonicity mechanism and
forces the future-prime curvature of `L-98060` into the state.

## Reconnaissance boundary

A separate double-precision scan of every real activation cell through
`Y=2,000,000` found no denominator zero and found

\[
\max Q(Y)=10.1543234467\ldots
\]

at `Y=584`.  This scan is nonprobative and is retained only to guide the next
barrier search.  The proved content of this file is the directed sign pattern
(R-98060.5).

```text
cellwise ratio monotonicity            REFUTED EXACTLY
one-crossing PRMP67                     REFUTED AS A MECHANISM
Q(Y,67)<=67 at all scales               OPEN
native Bellman margin / GPC67           OPEN / RH-BEARING
Riemann Hypothesis                      UNPROVEN
```