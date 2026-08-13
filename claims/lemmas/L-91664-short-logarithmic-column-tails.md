# L-91664 — Short logarithmic column-defect tails are nonpositive

Claim ID: `L-91664`  
Status: **PROVED EXACT POSITIVE-SOURCE TAIL THEOREM**  
Created: 2026-08-13  
Depends on: `L-90015`, `L-90016`  
RH status: **unproved**

For an integer cutoff `Q>=2`, put

\[
\lambda_Q(q)=\mathbf1_{q\ge Q}.
\]

At endpoint `X>=Q`, let

\[
F_Q(X)=\sum_{q=Q}^{\lfloor X\rfloor}r_X(q),
\]

where `r_X(q)=v_q(b_X)-w_X(q)` is the exact parabolic column residual.

`L-90016` gives, for `t=log X`,

\[
-F_Q(e^t)
=\int_0^t
\left(1-\frac{t-u}{2}\right)
\mathcal Q_Q(u)\,du,
\tag{L-91664.1}
\]

where

\[
\mathcal Q_Q(u)
=e^{-u/2}\sum_{Q\le q\le e^u}\Delta_q(e^u)\ge0.
\tag{L-91664.2}
\]

The source vanishes before `u=log Q`. Assume

\[
Q\ge Xe^{-2}.
\tag{L-91664.3}
\]

Every source point in (L-91664.1) then satisfies

\[
t-u\le\log(X/Q)\le2.
\]

Therefore

\[
1-\frac{t-u}{2}\ge0
\]

throughout the support. Since the source is nonnegative,

\[
\boxed{
\sum_{q=Q}^{\lfloor X\rfloor}r_X(q)\le0
\qquad(Q\ge Xe^{-2}).
}
\tag{L-91664.4}
\]

The inequality is strict when `Q<X`. For integer `X`, it applies to every
integer cutoff `Q>=ceil(Xe^-2)`.

`L-91663` proves the terminal-half subrange independently by direct telescoping
and supplies an explicit algebraic reserve. The present theorem extends the
exact ordered sector down to logarithmic width two. Below that cutoff, genuinely
old source mass reaches the negative lobe of the Green kernel, so a mean-age or
renewal estimate is necessary.

```text
positive aggregate tail source                IMPORTED EXACT
source starts no earlier than log Q            EXACT
log(X/Q)<=2 keeps Green factor nonnegative     EXACT
short logarithmic tails nonpositive           EXACT
long-tail mean-age control                     OPEN
Riemann Hypothesis                             UNPROVED
```
