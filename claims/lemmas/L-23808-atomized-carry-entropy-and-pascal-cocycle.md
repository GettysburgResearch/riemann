# L-23808 — Atomized carry entropy and the Pascal transport cocycle

Claim ID: `L-23808`  
Title: Every binomial split has an exact carry indicator, entropy Mellin mass, and four-cycle transport identity  
Status: **PROPOSED EXACT LEMMA — COMPLETE ELEMENTARY PROOF**  
Authoring agent: `gpt56-pro-09-u`  
Created: 2026-08-08  
Issue: #238  
Dependencies: none

## 1. Atomized carry indicator

For `x>=1` and `0<u<1`, define

\[
 \boxed{
 C(x,u)=\lfloor x\rfloor-\lfloor ux\rfloor
       -\lfloor(1-u)x\rfloor.}
 \tag{L-23808.1}
\]

Since `ux+(1-u)x=x`, the sum of the last two floors is either
`floor(x)` or `floor(x)-1`.  Therefore

\[
 \boxed{C(x,u)\in\{0,1\}.}
 \tag{L-23808.2}
\]

For integers `0<=j<=n` and `q>=2`, put

\[
 \boxed{
 \chi_{n,j}(q)
 =\left\lfloor\frac nq\right\rfloor
 -\left\lfloor\frac jq\right\rfloor
 -\left\lfloor\frac{n-j}{q}\right\rfloor.}
 \tag{L-23808.3}
\]

Then exactly

\[
 \boxed{
 \chi_{n,j}(q)=C(n/q,j/n).}
 \tag{L-23808.4}
\]

Thus one binomial split supplies a `0/1` carry row for every integer base `q`,
not only for prime powers.

## 2. Exact binomial valuation identity

Legendre's formula gives, for every prime `p`,

\[
 v_p\binom nj
 =\sum_{a\ge1}\chi_{n,j}(p^a).
\]

Consequently

\[
 \boxed{
 \log\binom nj
 =\sum_{p^a\le n}\Lambda(p^a)\chi_{n,j}(p^a).}
 \tag{L-23808.5}
\]

Every term is finite and nonnegative.  This is the atomized version of the
average-row identity in `L-23801`.

## 3. Mellin transform and entropy calibration

For `0<a<=1` and `Re(s)>0`, direct summation over the intervals on which
`floor(ax)` is constant gives

\[
 \int_1^\infty\lfloor ax\rfloor x^{-s-2}dx
 =\frac{a^{s+1}\zeta(s+1)}{s+1}.
 \tag{L-23808.6}
\]

Subtracting the cases `a=u` and `a=1-u` from `a=1` yields

\[
 \boxed{
 \int_1^\infty C(x,u)x^{-s-2}dx
 =\frac{\zeta(s+1)}{s+1}
  \left[1-u^{s+1}-(1-u)^{s+1}\right].}
 \tag{L-23808.7}
\]

At `s=0`, the zero in the square bracket cancels the pole of zeta and gives

\[
 \boxed{
 \int_1^\infty C(x,u)x^{-2}dx
 =H(u),}
 \tag{L-23808.8}
\]

where

\[
 H(u)=-u\log u-(1-u)\log(1-u)
 \tag{L-23808.9}
\]

is binary entropy.

This is the exact continuum calibration behind the proposed transport route:
**every fixed split has carry mass equal to its entropy production**.  No split
loses the leading constant in the continuum model.

Averaging (L-23808.1) uniformly in `u` recovers the continuum carry kernel of
`L-23804`:

\[
 \boxed{
 K(x)=\int_0^1 C(x,u)du.}
 \tag{L-23808.10}
\]

Indeed the Mellin transform of the right side is

\[
 \frac{\zeta(s+1)}{s+1}
 \left(1-\frac2{s+2}\right)
 =\frac{s\zeta(s+1)}{(s+1)(s+2)},
\]

which is `L-23804.4`; the equality also follows directly on each unit interval.

## 4. Pascal four-cycle identity

For integers

\[
 0\le k\le j\le n,
\]

the carry rows obey, for every integer `q>=2`,

\[
 \boxed{
 \chi_{n,j}(q)+\chi_{j,k}(q)
 =\chi_{n,k}(q)+\chi_{n-k,j-k}(q).}
 \tag{L-23808.11}
\]

This follows by expanding all four floor defects; every term cancels.
The matching entropy identity is

\[
 \boxed{
 \log\binom nj+\log\binom jk
 =\log\binom nk+\log\binom{n-k}{j-k}.}
 \tag{L-23808.12}
\]

Equation (L-23808.12) is the logarithm of

\[
 \binom nj\binom jk
 =\binom nk\binom{n-k}{j-k}.
\]

Thus any signed four-cycle move preserves simultaneously:

- every integer carry column;
- every prime-power valuation column;
- the complete logarithmic binomial objective.

This is the exact transport mechanism absent from the scalar Gamma–carry
factorization.

## 5. Fragmentation divergence form

Let `d_(n,j)` be any finitely supported signed split flow.  Define its node
divergence by

\[
 \boxed{
 r_m=\sum_{j=1}^{m-1}d_{m,j}
 -\sum_{n>m}\bigl(d_{n,m}+d_{n,n-m}\bigr),}
 \tag{L-23808.13}
\]

where a central child is counted twice, as it occurs twice in the split.
For

\[
 F_q(m)=\lfloor m/q\rfloor,
 \qquad L(m)=\log(m!),
\]

one has exactly

\[
 \boxed{
 \sum_{n,j}d_{n,j}\chi_{n,j}(q)
 =\sum_m r_mF_q(m),}
 \tag{L-23808.14}
\]

and

\[
 \boxed{
 \sum_{n,j}d_{n,j}\log\binom nj
 =\sum_m r_mL(m).}
 \tag{L-23808.15}
\]

Also

\[
 \sum_m mr_m=0,
 \tag{L-23808.16}
\]

because each binary split conserves the parent size.  Four-cycle moves change
the internal fragmentation tree while leaving the divergence and therefore all
quantities in (L-23808.14)--(L-23808.15) unchanged.

## 6. Atomized packing implication

For an endpoint `X`, let

\[
 w_X(q)=q^{-1/2}\log(X/q).
\]

If `d_(n,j)>=0` satisfies

\[
 \sum_{n=q}^{X}\sum_{j=1}^{n-1}
 d_{n,j}\chi_{n,j}(q)\le w_X(q)
 \qquad(2\le q\le X),
 \tag{L-23808.17}
\]

then (L-23808.5) and `Lambda>=0` give

\[
 \boxed{
 \sum_{n,j}d_{n,j}\log\binom nj
 \le
 \sum_{p^a\le X}\frac{\Lambda(p^a)}{\sqrt{p^a}}
 \log\frac{X}{p^a}.}
 \tag{L-23808.18}
\]

This is an exact finite positive packing.  Unlike scalar FGCM, the coefficients
may depend on both the scale `n` and the split `j/n` and may be rearranged by
Pascal cycles.

## 7. Proof boundary

Closed exactly:

- atomized carry indicators;
- binomial valuation;
- the entropy Mellin identity;
- uniform averaging to the old carry kernel;
- Pascal four-cycle and divergence identities;
- the atomized finite packing implication.

Open:

- a cofinal nearly saturating nonnegative balanced split flow;
- the signed transport construction proposed in `M-23802`;
- RH.
