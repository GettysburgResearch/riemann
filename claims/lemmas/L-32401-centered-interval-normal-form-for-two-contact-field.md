# L-32401 — Centered-interval normal form for the two-contact pole field

Claim ID: `L-32401`  
Title: The exact two-contact atomized pole field is a Brownian/min-kernel Gram of one paired odd-prime-power charge sequence  
Status: **PROPOSED COMPLETE EXACT FINITE/ANALYTIC LEMMA PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-08  
Base: PR #302 at `477b527fb489397eb9e58ed6631be04f5eae00d1`  
Dependencies: PR #302 `L-28005`, `L-28011`; elementary interval algebra  
Scope: exact normal form and energy diagonalization only; no cofinal estimate or RH claim

## 1. Oriented centered intervals

For `0<r<=1` and `0<theta<1`, define

\[
 J_r(\theta)
 =1-\mathbf 1_{\theta\ge r}-\mathbf 1_{1-\theta\ge r}.
\tag{L-32401.1}
\]

For `r>1` put `J_r=0`. Endpoint conventions on sets of measure zero are
irrelevant below. If

\[
 a(r)=\left|r-\frac12\right|,
 \qquad
 \epsilon(r)=\operatorname{sgn}\left(r-\frac12\right),
\]

then

\[
 \boxed{
 J_r(\theta)
 =\epsilon(r)\,
 \mathbf 1_{|\theta-1/2|<a(r)}
 }
\tag{L-32401.2}
\]

for `r!=1/2`, while `J_(1/2)=0` almost everywhere. Thus every `J_r` is one
oriented interval centered at the same point `1/2`.

## 2. The two-contact wavelet is one dyadic interval difference

Retain from PR #302

\[
 b_2=(\varepsilon-\delta_2)*\mu,
 \qquad
 \Lambda_2(n)=\Lambda(n)+(\log2)\mathbf1_{n=2^a}.
\]

For real `X>=1`, integer `m<=X`, and carry position `theta`, `L-28011` defines

\[
 Y_{X,m}(\theta)
 =\sum_{k\le X/m}b_2(k)
 C\!\left(\frac{X}{mk},\theta\right).
\]

Because

\[
 \mathbf1*b_2=\varepsilon-\delta_2,
\]

the floor sums collapse exactly. In the notation (L-32401.1),

\[
 \boxed{
 Y_{X,m}(\theta)
 =J_{m/X}(\theta)-J_{2m/X}(\theta).
 }
\tag{L-32401.3}
\]

This is the complete factor-five/two-contact wavelet. No quotient-cell
partition is required to state it.

## 3. Collapse of the generalized-prime source

The physical field is

\[
 \mathfrak P_{2,\theta}(\log X)
 ={1\over\sqrt X}
  \sum_{m\le X}\Lambda_2(m)Y_{X,m}(\theta).
\tag{L-32401.4}
\]

Insert (L-32401.3), then in the second sum set `n=2m`. This gives

\[
 \boxed{
 \sqrt X\,\mathfrak P_{2,\theta}(\log X)
 =\sum_{n\le X}c_2(n)J_{n/X}(\theta),
 }
\tag{L-32401.5}
\]

where

\[
 \boxed{
 c_2(n)=\Lambda_2(n)
 -\mathbf1_{2\mid n}\Lambda_2(n/2).
 }
\tag{L-32401.6}
\]

The sequence `c_2` has an especially sparse exact form:

\[
 \boxed{
 c_2(n)=
 \begin{cases}
 2\log2,&n=2,\\
 \log p,&n=p^a\text{ with }p\text{ odd},\\
 -\log p,&n=2p^a\text{ with }p\text{ odd},\\
 0,&\text{otherwise}.
 \end{cases}}
\tag{L-32401.7}
\]

Indeed every dyadic power `2^a`, `a>=2`, has the same coefficient `2 log 2`
in `Lambda_2` as its half and cancels. Every odd prime power occurs positively,
and its double occurs negatively. Thus the complete physical source contains no
other arithmetic fibers after this recombination.

## 4. Exact Brownian/min kernel

Since all intervals in (L-32401.2) are centered at `1/2`, for `0<r,s<=1`

\[
 \boxed{
 \int_0^1J_r(\theta)J_s(\theta)\,d\theta
 =2\epsilon(r)\epsilon(s)
 \min\{a(r),a(s)\}.
 }
\tag{L-32401.8}
\]

After conjugating by the signs `epsilon(r)`, this is exactly twice the Brownian
covariance kernel `min(u,v)` on `[0,1/2]`.

Consequently the dense finite carry Gram of `L-28011` has a one-dimensional
layer-cake diagonalization. Put

\[
 \boxed{
 S_X(u)=
 \sum_{\substack{n\le X\\|n/X-1/2|>u}}
 \epsilon(n/X)c_2(n),
 \qquad0\le u\le\frac12.
 }
\tag{L-32401.9}
\]

Then Tonelli's theorem applied to the finite sum gives

\[
 \boxed{
 \int_0^1
 |\mathfrak P_{2,\theta}(\log X)|^2d\theta
 ={2\over X}
 \int_0^{1/2}|S_X(u)|^2du.
 }
\tag{L-32401.10}
\]

No spectral diagonalization, floating eigenvector, or asymptotic argument enters
this identity.

## 5. Equivalent generalized-Chebyshev Jensen form

Let

\[
 C_2^{\rm Ch}(y)=\sum_{n\le y}c_2(n).
\tag{L-32401.11}
\]

Equation (L-32401.6) gives

\[
 \boxed{
 C_2^{\rm Ch}(y)
 =\Psi_2(y)-\Psi_2(y/2),
 }
\tag{L-32401.12}
\]

which is the `A_2^{Ch}` state of `L-28011`. If

\[
 y=\left(\frac12-u\right)X,
\]

then the two tails in (L-32401.9) give exactly

\[
 \boxed{
 S_X(u)
 =C_2^{\rm Ch}(X)
  -C_2^{\rm Ch}(y)
  -C_2^{\rm Ch}(X-y).
 }
\tag{L-32401.13}
\]

Hence (L-32401.10) is equivalently

\[
 \boxed{
 \int_0^1
 |\mathfrak P_{2,\theta}(\log X)|^2d\theta
 ={2\over X^2}
 \int_0^{X/2}
 |C_2^{\rm Ch}(X)-C_2^{\rm Ch}(y)-C_2^{\rm Ch}(X-y)|^2dy.
 }
\tag{L-32401.14}
\]

This supplies an exact bridge between the finite carry Gram, the atomized pole
field, a Brownian covariance, and one additive generalized-Chebyshev Jensen
defect.

## 6. Finite precision matrix

For a fixed endpoint, aggregate equal radii

\[
 0<a_1<a_2<\cdots<a_M\le\frac12
\]

and let `g_i` be the signed coefficient at radius `a_i`. Then

\[
 \boxed{
 \left\|\sum_i g_i\mathbf1_{|\theta-1/2|<a_i}\right\|_2^2
 =2\sum_{i=1}^{M}(a_i-a_{i-1})
   \left|\sum_{k=i}^{M}g_k\right|^2,
 \quad a_0=0.
 }
\tag{L-32401.15}
\]

Equivalently, the inverse of the unsigned covariance matrix
`[2 min(a_i,a_j)]` is tridiagonal. Apart from the overall factor `1/2`, its
entries are

\[
 Q_{ii}=
 \begin{cases}
 a_1^{-1}+(a_2-a_1)^{-1},&i=1<M,\\
 (a_i-a_{i-1})^{-1}+(a_{i+1}-a_i)^{-1},&1<i<M,\\
 (a_M-a_{M-1})^{-1},&i=M>1,
 \end{cases}
\]

and

\[
 Q_{i,i+1}=Q_{i+1,i}=-(a_{i+1}-a_i)^{-1}.
\tag{L-32401.16}
\]

Thus the complete atomized Gram has an exact adjacent-gap precision operator.

## 7. Diagonal budget and the true remaining term

The diagonal of (L-32401.8) is at most one. By (L-32401.7),

\[
 {1\over X}\sum_{n\le X}|c_2(n)|^2
 \ll 1+\log(2X)
\tag{L-32401.17}
\]

using the elementary Chebyshev bound
`sum_(p^a<=X) log p = O(X)` and `log p<=log X`. Therefore the entire diagonal
part of the physical theta-energy is polylogarithmic.

The RH-bearing content is exactly the signed interaction of the cumulative tail
charges in (L-32401.15), not the diagonal and not an unspecified physical-to-carry
map.

## 8. Proof boundary

Closed exactly here, subject to review:

- oriented-centered-interval form of every carry atom;
- dyadic wavelet factorization;
- collapse to odd prime powers and their doubles;
- Brownian/min covariance of the complete physical Gram;
- one-dimensional layer-cake energy identity;
- tridiagonal precision matrix;
- polylogarithmic diagonal budget.

Not proved here:

- the critical bound
  `int_0^(1/2)|S_X(u)|^2 du = X^(1+o(1))`;
- a coefficient-one lower-scale recurrence for those tail charges;
- RH.