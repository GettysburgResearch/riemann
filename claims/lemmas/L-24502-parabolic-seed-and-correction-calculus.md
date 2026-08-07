# L-24502 — Parabolic seed and exact correction calculus

Claim ID: `L-24502`  
Status: `PROPOSED COMPLETE IDENTITIES; former Divisibility Cover rejected by R-24501`  
Scope: elementary carry minorant construction  
Issue: #245

## 1. Explicit parabolic seed

For `2<=m<=X`, define

\[
\boxed{
b_X^{(0)}(m)=2\sqrt m\left[\log\frac Xm-2\left(1-\sqrt{\frac mX}\right)\right].}
\tag{L-24502.1}
\]

With `r=sqrt(m/X)`, the bracket is `-2 log r-2(1-r)>=0`, so

\[
b_X^{(0)}(m)\ge0.
\]

Define

\[
f_X(x)=\frac{b_X^{(0)}(x)}x
=2x^{-1/2}\log\frac Xx-4x^{-1/2}+4X^{-1/2}.
\]

Then

\[
\boxed{f_X'(x)=-x^{-3/2}\log\frac Xx\le0.}
\tag{L-24502.2}
\]

## 2. Sharp objective mass

Since `log(m/(m-1))>=1/m`,

\[
J_X(b_X^{(0)})\ge\sum_{m=2}^X f_X(m).
\]

Using monotonicity from (L-24502.2) and elementary integral comparison gives

\[
\boxed{J_X(b_X^{(0)})\ge4\sqrt X-6\log X+4-8X^{-1/2}.}
\tag{L-24502.3}
\]

Thus the complete critical `4 sqrt(X)` main term is present before arithmetic repair.

## 3. Adjacent-flow correction

Let `F_1=F_X=0` and define

\[
b_F(m)=b_X^{(0)}(m)+F_{m-1}-F_m.
\tag{L-24502.4}
\]

Then for every integer `q>=2`,

\[
\boxed{
v_q(b_F)-v_q(b_X^{(0)})
=\sum_{j=2}^{X-1}F_j\left(\mathbf1_{q\mid j+1}-2\mathbf1_{q\mid j}+\mathbf1_{q\mid j-1}\right).}
\tag{L-24502.5}
\]

The objective change telescopes exactly:

\[
\boxed{
J_X(b_X^{(0)})-J_X(b_F)
=\sum_{j=2}^{X-1}F_j\log\frac{j^2}{j^2-1}.}
\tag{L-24502.6}
\]

Since

\[
\log\frac{j^2}{j^2-1}=j^{-2}+O(j^{-4}),
\]

signed transport far to the right is asymptotically cheap in the exact objective metric.

The endpoint-projected extension of this calculus is `L-24509`.

## 4. Monotone tail subtraction identity

Choose `alpha_m>=0`, put

\[
B_m=\sum_{t=m}^X\alpha_t,
\qquad
\widetilde b_m=b_X^{(0)}(m)-B_m.
\tag{L-24502.7}
\]

Then

\[
\boxed{
v_q(\widetilde b)=v_q(b_X^{(0)})-\sum_{kq\le X}\alpha_{kq}.}
\tag{L-24502.8}
\]

and

\[
\boxed{
J_X(b_X^{(0)})-J_X(\widetilde b)=\sum_{m=2}^X\alpha_m\log m.}
\tag{L-24502.9}
\]

These are valid exact identities.

## 5. Former Divisibility Cover — rejected

The first version proposed nonnegative atoms satisfying

\[
\sum_{kq\le X}\alpha_{kq}\ge e_X(q),
\qquad
\sum_{t=m}^X\alpha_t\le b_X^{(0)}(m),
\qquad
\sum_m\alpha_m\log m=O(\log^2X).
\]

`R-24501` proves that the first and third conditions are already incompatible. On the fixed prime band

\[
X/40\le p\le X/32,
\]

the seed has excess at least `1/(20 sqrt(X))`, while the multiple sets of distinct band primes are disjoint below `X`. The prime number theorem then forces every nonnegative cover to cost

\[
\gg\sqrt X.
\]

Therefore the monotone Divisibility Cover is **REJECTED**. The finite LP behavior in `O-24501` was pre-asymptotic.

The refutation does not affect signed adjacent transport: its weight is `j^-2+O(j^-4)` rather than `log j`, and negative slack may be retained before the final objective pairing.

## Status boundary

The seed, its objective lower bound, and both correction identities are retained. The monotone positive cover is not a surviving closure. Current full-proposal routes are the endpoint-projected Green energy of `T-24503` and, separately, a genuinely signed primitive-neighbor estimate.
