# L-32408 — Exact real-endpoint carry cells and cofinal physical reserve absorption for Q=4

Claim ID: `L-32408`  
Title: The continuous Q=4 atomized pole field is an exact mixture of two neighboring integer carry rows plus one logarithmic divisor boundary, so the vanishing current/reserve ratio transfers to the actual balanced physical energy  
Status: **PROPOSED COMPLETE UNCONDITIONAL THEOREM — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-09  
Dependencies: `L-32407`; PR #297 `L-29001` atomized carry geometry  
Scope: physical/carry localization for the Q=4 inverse-source current; no global reflected recurrence or RH claim

## 1. Continuous atomized Q=4 current

Retain the Q=4 inverse-source current

\[
 q_4=b_4*\Lambda_4=-b_4\log
\]

from `L-32407`. For real `X>=2` and `0<=theta<=1`, define

\[
 \boxed{
 \mathcal V_4(X,\theta)
 =X^{-1/2}\sum_{d\le X}q_4(d)
 C(X/d,\theta),
 }
 \tag{L-32408.1}
\]

where

\[
 C(x,\theta)=\lfloor x\rfloor
 -\lfloor\theta x\rfloor
 -\lfloor(1-\theta)x\rfloor.
\]

The Mellin transform in `X=e^t` is the Q=4 pole field

\[
 E_4(s)L_4(s)N_\theta(s),
 \qquad s=z+1/2,
\]

up to the fixed critical normalization already used in `L-32406`. Thus every
nontrivial zeta zero remains visible.

Put

\[
 n=\lfloor X\rfloor,
 \qquad
 \delta=X-n\in[0,1).
\]

## 2. Exact unit-cell decomposition in the carry-position variable

For a fixed `theta`, write

\[
 \theta X=j+u,
 \qquad
 j=\lfloor\theta X\rfloor,
 \quad0\le u<1.
\]

For every integer `d>=1`, because `X<n+1`,

\[
 \left\lfloor\frac Xd\right\rfloor
 =\left\lfloor\frac nd\right\rfloor,
 \tag{L-32408.2}
\]

and because `0<=u<1`,

\[
 \left\lfloor\frac{\theta X}{d}\right\rfloor
 =\left\lfloor\frac jd\right\rfloor.
 \tag{L-32408.3}
\]

For the second child,

\[
 \lfloor(1-\theta)X\rfloor
 =\begin{cases}
 n-j,&0\le u\le\delta,\\
 n-j-1,&\delta<u<1.
 \end{cases}
 \tag{L-32408.4}
\]

Therefore, away from the measure-zero interfaces,

\[
 \boxed{
 C(X/d,\theta)
 =\begin{cases}
 \chi_{n,d}(j),&u<\delta,\\
 \chi_{n-1,d}(j)+\mathbf1_{d\mid n},&u>\delta.
 \end{cases}}
 \tag{L-32408.5}
\]

The second line uses

\[
 \left\lfloor\frac nd\right\rfloor
 -\left\lfloor\frac{n-1}{d}\right\rfloor
 =\mathbf1_{d\mid n}.
\]

Define the divisor boundary

\[
 \boxed{
 \gamma_4(n)=\sum_{d\mid n}q_4(d)=(\mathbf1*q_4)(n).
 }
 \tag{L-32408.6}
\]

Then the unnormalized current in (L-32408.1) is exactly

\[
 \boxed{
 \sum_{d\le X}q_4(d)C(X/d,\theta)
 =\begin{cases}
 Q_4(n,j),&u<\delta,\\
 Q_4(n-1,j)+\gamma_4(n),&u>\delta.
 \end{cases}}
 \tag{L-32408.7}
\]

where `Q_4` is the integer carry current of `L-32407`.

This is an exact continuous-to-discrete adapter. No Riemann-sum or sampling
argument is used.

## 3. The boundary coefficient is only logarithmic

By `L-32404`, `1*b_4=e_4` and hence

\[
 \gamma_4=e_4*\Lambda_4.
 \tag{L-32408.8}
\]

The coefficient is sparse. Explicitly:

- at an odd prime power `p^a`, `gamma_4=log p`;
- at `4^r p^a` with `p` odd and `r>=1`, `gamma_4=-3 log p`;
- at `4^r`,
  \[
  \gamma_4(4^r)=(3r+4)\log2;
  \]
- at `2*4^r`,
  \[
  \gamma_4(2\cdot4^r)=(1-3r)\log2;
  \]
- all remaining integers have coefficient zero.

The pure-dyadic formulas follow by substituting `Lambda_4(4^m)` from
`L-32404.8` and telescoping the threefold Q-adic predecessor sum.

In particular there is an absolute constant, for example

\[
 \boxed{
 |\gamma_4(n)|\le4\log(2n)
 \qquad(n\ge1).
 }
 \tag{L-32408.9}
\]

Thus the only error created by a noninteger endpoint is logarithmic, not an
RH-scale source.

## 4. Exact full-theta cell integral

For `j=0,...,n-1`, the cell

\[
 j\le\theta X<j+1
\]

has `theta`-length `1/X`; its first `delta` fraction uses the `n` row and the
remaining `1-delta` fraction uses the `n-1` row plus `gamma_4(n)`. The final
partial cell `j=n` has length `delta/X` and contributes zero because
`Q_4(n,n)=0`.

Consequently

\[
 \boxed{
 \begin{aligned}
 \int_0^1|\mathcal V_4(X,\theta)|^2d\theta
 ={1\over X^2}\sum_{j=0}^{n-1}
 \Big[
 &\delta |Q_4(n,j)|^2\\
 &+(1-\delta)|Q_4(n-1,j)+\gamma_4(n)|^2
 \Big].
 \end{aligned}}
 \tag{L-32408.10}
\]

This identity is useful beyond Q=4: it is the exact real-endpoint cell law for
any divisor current.

## 5. Balanced physical interval

Fix the pole-detecting carry-position interval

\[
 I=[1/3,2/3].
\]

PR #297 `L-29001` proves that every nontrivial zero has a nonzero residue vector
on any fixed balanced interval, so restricting to `I` loses no zeta-zero pole.

For all sufficiently large `n`, every complete `theta X` cell contained in `I`
corresponds in (L-32408.7) to a quarter-balanced row of both `n` and `n-1`.
Only `O(1)` edge cells are clipped by the endpoints of `I`; by (L-32408.9)
and the elementary Chebyshev bounds in `L-32405`, their total contribution is
polynomial-logarithmic after the critical normalization.

Let

\[
 \mathcal R_4(n)
 =\sum_{n/4\le j\le3n/4}R_4(n,j).
 \tag{L-32408.11}
\]

By `L-32407.14`, for every `epsilon>0` and all sufficiently large parents,

\[
 |Q_4(n,j)|^2\le\epsilon R_4(n,j)
\]

on every quarter-balanced row. Also

\[
 |a+b|^2\le(1+\epsilon)|a|^2+(1+\epsilon^{-1})|b|^2.
\]

Using (L-32408.9) for the boundary term in the second branch, one obtains the
cofinal physical estimate

\[
 \boxed{
 \int_{1/3}^{2/3}|\mathcal V_4(X,\theta)|^2d\theta
 \le
 {\varepsilon_X\over X^2}
 \big[\mathcal R_4(n)+\mathcal R_4(n-1)\big]
 +O\!\left({\log^2(2X)\over X}\right),
 }
 \tag{L-32408.12}
\]

where

\[
 \boxed{\varepsilon_X\longrightarrow0.}
 \tag{L-32408.13}
\]

The same statement holds with any fixed balanced interval strictly inside
`(1/4,3/4)`.

The `O(log^2 X/X)` term includes the divisor boundary and the finitely many
clipped carry-position cells; it is exponentially small in logarithmic scale.

## 6. Unit logarithmic blocks

Put `X=e^t`. Since `dt=dX/X`, integrating (L-32408.12) over a unit logarithmic
block gives

\[
 \boxed{
 \begin{aligned}
 \int_J^{J+1}\int_{1/3}^{2/3}
 |\mathcal V_4(e^t,\theta)|^2d\theta\,dt
 \le{}&
 \int_{e^J}^{e^{J+1}}
 {\varepsilon_X[\mathcal R_4(\lfloor X\rfloor)
 +\mathcal R_4(\lfloor X\rfloor-1)]\over X^3}\,dX\\
 &+O(J^2e^{-J}).
 \end{aligned}}
 \tag{L-32408.14}
\]

Thus the actual independent carry-position pole energy consumes a vanishing
fraction of the source-matched Q=4 reserve, with only a negligible real-endpoint
boundary forcing.

## 7. Proof boundary

Closed here, subject to independent review:

1. the exact real-endpoint carry-cell identity;
2. the exact neighboring-row plus divisor-boundary decomposition;
3. the sparse logarithmic classification of the divisor boundary;
4. the exact full-theta physical cell integral;
5. transfer of `L-32407` to a fixed pole-detecting balanced interval;
6. the cofinal physical reserve-absorption estimate with coefficient tending to
   zero;
7. its unit-logarithmic-block form.

Still open:

1. placing the Q=4 reserve with the correct sign in the complete
   source-convolved reflected Selberg identity;
2. the final neutral scattering recurrence;
3. RH.
