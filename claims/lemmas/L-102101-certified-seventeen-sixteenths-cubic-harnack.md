# L-102101 — A certified \(17/16\) source-normalized Harnack bound for every cubic double-owner endpoint kernel

Claim ID: `L-102101`  
Status: **PROVED EXACT ANALYTIC THEOREM WITH RATIONAL BERNSTEIN CERTIFICATE**  
Created: 2026-08-21  
Depends on: PR #691 `L-100612` cubic endpoint positivity  
RH status: **not assumed**

Let

\[
\Psi(y)=64\begin{cases}3y-y^{3/2},&0<y\le1,\\3\sqrt y-1,&y\ge1,\end{cases}
\]

and, for primes `67<=p<q`, put `K_(p,q)=(I-U_p)(I-U_q)Psi`. Then, for every real `ell>=2` and every `y>0`,

\[
\boxed{\sqrt\ell\,K_{p,q}(y/\ell)\le {17\over16}K_{p,q}(y).}
\tag{L-102101.1}
\]

Equivalently,

\[
\boxed{\ell^{-1/2}K_{p,q}(y/\ell)\le {17\over16\ell}K_{p,q}(y).}
\tag{L-102101.2}
\]

## Logarithmic normalization

Put `x=sqrt(y)`, `a=p^(-1/2)`, `b=q^(-1/2)`, and

\[
\varphi(x)=\Psi(x^2)/64=\begin{cases}3x^2-x^3,&x\le1,\\3x-1,&x\ge1.\end{cases}
\]

Define

\[
h_{a,b}(x)={\varphi(x)-\varphi(ax)-\varphi(bx)+\varphi(abx)\over x}.
\]

Then `K_(p,q)(y)/(64 sqrt(y))=h_(a,b)(sqrt(y))`, and on the deep branch

\[
\boxed{h_\infty=3(1-a)(1-b).}
\tag{L-102101.3}
\]

Because `p,q>=67`, `0<b<=a<1/8`.

For `0<x<=1`,

\[
h(x)=3x(1-a^2)(1-b^2)-x^2(1-a^3)(1-b^3)
\]

is strictly increasing. For `1<=x<=1/a`, write `t=b/a` and `u=ax`. Then

\[
\begin{aligned}
h(x)={}&3-{a\over u}-3au(1+t^2-a^2t^2)\\
&+au^2(1+t^3-a^3t^3).
\end{aligned}
\tag{L-102101.4}
\]

The exact bound

\[
\boxed{h(x)\le {17\over16}h_\infty}
\tag{L-102101.5}
\]

on this region is certified below.

For `1/a<=x<=1/b`, putting `v=bx` gives

\[
h(x)-h_\infty=b[3(1-a)-3v(1-a^2)+v^2(1-a^3)],
\]

whose bracket decreases on `v<=1` and equals `(1-a)^3` at one. Hence `h>=h_infty`. For `1/b<=x<=1/(ab)`, with `w=abx`,

\[
\boxed{h(x)-h_\infty=ab{(1-w)^3\over w}\ge0.}
\tag{L-102101.6}
\]

Beyond this range equality holds.

On `1<=x<=1/a`, one has `h'(1)>0`,

\[
h'(1/a)=a^2t^2[-3+2t+3a^2-2a^3t]<0,
\]

and `h''(x)=-2x^(-3)+2(a^3+b^3-a^3b^3)` has at most one zero. Thus this branch has one maximum. Also

\[
h(1)\le3-(511/512)^2<147/64\le h_\infty.
\]

Consequently the set where `h<h_infty` is an initial increasing interval.

## Exact Bernstein certificate

Set `A=8a`, `T=t`, `U=u`. Exact expansion gives

\[
-16U\left(h-{17\over16}h_\infty\right)=R(A,T,U),
\]

where

\[
\begin{aligned}
R={}&{A^4T^3U^3\over256}-{3A^3T^2U^2\over32}+{51A^2TU\over64}\\
&-2AT^3U^3+6AT^2U^2-{51ATU\over8}\\
&-2AU^3+6AU^2-{51AU\over8}+2A+3U.
\end{aligned}
\tag{L-102101.7}
\]

Convert `R` exactly to the tensor Bernstein basis of degrees `(4,3,3)`. After restricting only `U` to

\[
[0,1/2], [1/2,17/32], [17/32,9/16], [9/16,5/8], [5/8,3/4], [3/4,1],
\]

all Bernstein coefficients are nonnegative. The smallest strictly positive retained coefficient is `1/32768`. The standard-library replay performs this exact rational check.

If `h(x)<h_infty`, then `x` lies on the initial increasing branch, so `h(x/sqrt(ell))<=h(x)`. Otherwise the global maximum is at most `(17/16)h_infty<=(17/16)h(x)`. This proves (L-102101.1).
