# L-23825 — Finite shell profile and exact prime-sampling remainder

Claim ID: `L-23825`  
Title: The finite parabolic carry shell equals its continuum majorized profile plus an absolutely summable floor error; only one Chebyshev prime-sampling remainder remains  
Status: **PROPOSED COMPLETE REDUCTION — independent review requested**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-08  
Issue: #238  
Dependencies: `L-23823`; PR #248 parabolic seed and prime-only reduction  
Scope: exact finite-to-continuum reduction; no estimate of the prime-sampling remainder

## 1. Seed scaling

Let

\[
B(u)=2\sqrt u\left[
\log(1/u)-2(1-\sqrt u)
\right],
\qquad 0<u\le1,
\tag{L-23825.1}
\]

and put

\[
g(u)=-B'(u)=\frac{\log u+4}{\sqrt u}-4.
\tag{L-23825.2}
\]

For an integer endpoint `X`, the parabolic seed is

\[
b_X(m)=\sqrt X\,B(m/X),
\qquad 2\le m\le X,
\tag{L-23825.3}
\]

with zero extension above `X`.

For every integer `2<=q<=X`, its divisor-gradient response is

\[
v_q(b_X)
=\sum_{kq\le X}[b_X(kq)-b_X(kq+1)].
\tag{L-23825.4}
\]

If `kq<X`, the fundamental theorem of calculus gives

\[
b_X(kq)-b_X(kq+1)
=X^{-1/2}\int_0^1
 g\left(\frac{kq+t}{X}\right)dt.
\tag{L-23825.5}
\]

When `kq=X`, both the finite summand and the continuum value `g(1)` are zero.

## 2. Uniform floor approximation

The derivative is

\[
g'(u)=-\frac{\log u+2}{2u^{3/2}}.
\tag{L-23825.6}
\]

Consequently, for one absolute constant `C`,

\[
|g'(u)|
\le C u^{-3/2}[1+\log(1/u)]
\qquad(0<u\le1).
\tag{L-23825.7}
\]

Apply the mean-value estimate to (L-23825.5), sum over `k`, and use

\[
\sum_{k\ge1}k^{-3/2}<\infty.
\]

This gives

\[
\boxed{
\left|
 v_q(b_X)-X^{-1/2}F(q/X)
\right|
\le
Cq^{-3/2}\left[1+\log\frac Xq\right],}
\tag{L-23825.8}
\]

where

\[
F(\theta)=\sum_{k\le1/\theta}g(k\theta).
\tag{L-23825.9}
\]

Let

\[
h(\theta)=\theta^{-1/2}\log(1/\theta),
\qquad
E(\theta)=F(\theta)-h(\theta).
\tag{L-23825.10}
\]

The finite residual

\[
r_X(q)=v_q(b_X)-q^{-1/2}\log(X/q)
\tag{L-23825.11}
\]

therefore satisfies

\[
\boxed{
 r_X(q)
 =X^{-1/2}E(q/X)+\epsilon_X(q),}
\tag{L-23825.12}
\]

with

\[
\boxed{
|\epsilon_X(q)|
\le
Cq^{-3/2}\left[1+\log\frac Xq\right].}
\tag{L-23825.13}
\]

The estimate is uniform down to `q=2`; no fixed-ratio restriction is used.

## 3. Two-endpoint shell

Let `2<=Y<X` be integers and put

\[
c=Y/X.
\]

Define the finite shell residual

\[
s_{X,Y}(q)
=r_X(q)-\mathbf1_{q\le Y}r_Y(q).
\tag{L-23825.14}
\]

The continuum shell defect of `L-23823` is

\[
E_c(\theta)
=E(\theta)-c^{-1/2}E(\theta/c)\mathbf1_{\theta\le c}.
\tag{L-23825.15}
\]

Using (L-23825.12) at both endpoints gives

\[
\boxed{
s_{X,Y}(q)
=X^{-1/2}E_c(q/X)+\epsilon_{X,Y}(q),}
\tag{L-23825.16}
\]

where, after enlarging the absolute constant,

\[
\boxed{
|\epsilon_{X,Y}(q)|
\le
Cq^{-3/2}\left[1+\log\frac Xq\right].}
\tag{L-23825.17}
\]

Thus the finite carry-floor discrepancy is already absolutely summable in the
logarithmically weighted prime norm.

Indeed, for every `z>=2`,

\[
\boxed{
\sum_{z\le p\le X}
(\log p)|\epsilon_{X,Y}(p)|
\le
Cz^{-1/2}(1+\log z)(1+\log X).}
\tag{L-23825.18}
\]

The same bound follows by summing over all integers, so it uses no prime theorem.

## 4. Exact Chebyshev sampling identity

Let

\[
\vartheta(t)=\sum_{p\le t}\log p
\tag{L-23825.19}
\]

and let

\[
H_c(\theta)=\int_\theta^1E_c(u)du\le0
\tag{L-23825.20}
\]

be the shell tail from `L-23823`.

For every real `z` between `2` and `X`, Stieltjes summation gives the exact
identity

\[
\begin{aligned}
&X^{-1/2}
\sum_{z\le p\le X}(\log p)E_c(p/X)\\
&\qquad=
\sqrt X\,H_c(z/X)
+\mathcal E_{X,Y}(z),
\end{aligned}
\tag{L-23825.21}
\]

where the complete prime-sampling remainder is

\[
\boxed{
\mathcal E_{X,Y}(z)
=
X^{-1/2}
\int_{[z,X]}
E_c(t/X)\,d[\vartheta(t)-t].}
\tag{L-23825.22}
\]

Endpoint conventions may be fixed by taking right-continuous Stieltjes
integrals; changing the convention moves only the explicitly displayed endpoint
atom.

Combining (L-23825.16), (L-23825.18), and (L-23825.21),

\[
\begin{aligned}
\sum_{z\le p\le X}(\log p)s_{X,Y}(p)
={}&
\sqrt X\,H_c(z/X)\\
&+\mathcal E_{X,Y}(z)
+O\left(
 z^{-1/2}(1+\log z)(1+\log X)
\right).
\end{aligned}
\tag{L-23825.23}
\]

The first term is nonpositive, with the quantitative moat of `L-23823`. The
floor term is polylogarithmic once `z` is bounded below, and remains explicit at
small `z`.

Therefore the weighted shell-tail charge of `L-23824` is bounded by one precise
source-specific object:

\[
\boxed{
\mathcal B_{X,Y}
\le
\sup_{2\le z\le X}
(\mathcal E_{X,Y}(z))_+
+O((1+\log X)^2).}
\tag{L-23825.24}
\]

No source-rank, face-count, Schur-reserve, or Green-energy term remains.

## 5. Meaning of the remaining theorem

The classical prime number theorem controls `mathcal E_(X,Y)` only at a
sub-square-root scale. The RH proof requires the much sharper subpolynomial
upper envelope after the exact negative continuum moat has been retained.

The remaining estimate is therefore neither a generic PNT error nor an unsigned
operator norm. It is a one-sided, fixed-ratio, source-specific Chebyshev sampling
remainder:

\[
\boxed{
\sup_z(\mathcal E_{X,Y}(z))_+=X^{o(1)}.}
\tag{L-23825.25}
\]

The first `2/3` Mertens/Farey cell is an explicit mutation of this remainder.
Thus (L-23825.25) does not hide the RH-bearing scalar; it isolates it after the
continuum and floor geometry have been proved.

## 6. Proof boundary

Closed here:

1. uniform finite-to-continuum response approximation;
2. uniform fixed-ratio shell approximation;
3. absolute weighted summability of the carry-floor error;
4. exact Stieltjes decomposition into negative continuum moat plus one prime
   sampling remainder;
5. the scalar bound (L-23825.24).

Open:

1. the subpolynomial one-sided estimate (L-23825.25);
2. the sharp finite shell charge;
3. RH.
