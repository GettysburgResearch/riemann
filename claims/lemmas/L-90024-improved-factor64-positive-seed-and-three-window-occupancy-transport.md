# L-90024 — The improved factor-64 filter has a positive compact seed and an exact three-window occupancy transport

Claim ID: `L-90024` (provisional range; branch-qualified)  
Title: The preferred seven-scale filter turns the parabolic seed into a nonnegative compact atom; its entire prime endpoint is one three-window comparison of the positive occupancy source with exact masses `4`, `4+2^{-1/2}`, `2^{-1/2}`  
Status: **PROPOSED COMPLETE EXACT POSITIVITY / TRANSPORT NORMAL FORM — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Date: 2026-08-10  
Depends on: the endpoint definitions of `L-90004`; the improved filter of `L-90022/L-90023`; the occupancy deficit identity of PR #353 `L-90015` (reproved below at the needed scope)  
Scope: exact finite reduction and positive source geometry; no proof of the final three-window inequality and no claim of RH

## 1. The preferred filter

Put

\[
q=2^{-1/2},\qquad h=\log 2,
\]

and let

\[
P_*(y)=(1-y)^2(1-qy)(1+y)\left(1+\frac34y+y^2\right)
       =\sum_{j=0}^{6}a_jy^j.
\tag{L-90024.1}
\]

The integer-friendly coefficients are

\[
c_j=4\sqrt2\,a_j,
\]

namely

\[
(c_0,\ldots,c_6)=
\bigl(
4\sqrt2,-(4+\sqrt2),1-3\sqrt2,3-3\sqrt2,
3-\sqrt2,1+4\sqrt2,-4
\bigr).
\tag{L-90024.2}
\]

For real `X>=1`, define the filtered parabolic seed

\[
\boxed{
\mathcal B_X(m)=\sum_{j=0}^{6}c_j b_{X/2^j}(m),
}
\tag{L-90024.3}
\]

where every scale seed is zero outside its natural support.

The corresponding endpoint scalar is exactly the preferred criterion

\[
\boxed{
\mathcal V_{64}(X)=\sum_{j=0}^{6}c_jA(X/2^j).
}
\tag{L-90024.4}
\]

At `X=64N`, this is the seven-term inequality displayed in `T-90015`.

## 2. Hidden positivity of the filtered seed

Fix `m>0`, put

\[
t=\log(X/m),
\]

and use the causal convention that every function below is zero for negative
arguments. Apart from the positive constant `2sqrt(m)`, the scale seed is

\[
 b(t)=2\sqrt m\,[t-2+2e^{-t/2}]\mathbf1_{t\ge0}.
\tag{L-90024.5}
\]

Let

\[
(\mathcal Sf)(t)=f(t-h).
\]

Factor the filter state by state:

\[
 C=(I-q\mathcal S)b,
 \qquad
 H=(I-\mathcal S)C,
 \qquad
 G=(I-\mathcal S^2)H.
\tag{L-90024.6}
\]

Then

\[
\boxed{
\mathcal B_X(m)=4\sqrt2\,
\left(I+\frac34\mathcal S+\mathcal S^2\right)G(t).
}
\tag{L-90024.7}
\]

The point is that every state in (L-90024.6) is nonnegative.

First, on `0<=t<h`, `C(t)=b(t)`. For `t>=h`, the critical exponential cancels exactly and

\[
\boxed{
 C(t)=2\sqrt m\,[(1-q)(t-2)+qh].
}
\tag{L-90024.8}
\]

The two formulas meet with the same first derivative at `t=h`. Moreover

\[
 C'(t)=
 \begin{cases}
 2\sqrt m(1-e^{-t/2}),&0<t<h,\\
 2\sqrt m(1-q),&t>h,
 \end{cases}
\tag{L-90024.9}
\]

so `C'` is nonnegative and nondecreasing. Also `C(h)>0`: the elementary bounds
`log 2>2/3` and `sqrt(2)>7/5` give

\[
h-2+\sqrt2>\frac1{15}>0.
\]

Thus `C` is nonnegative and increasing.

It follows immediately that

\[
H(t)=C(t)-C(t-h)\ge0,
\qquad
H'(t)=C'(t)-C'(t-h)\ge0.
\tag{L-90024.10}
\]

Because `C` is affine after `h`, `H` is constant after `2h`. Hence

\[
G(t)=H(t)-H(t-2h)\ge0
\tag{L-90024.11}
\]

and `G(t)=0` for `t>=4h`. The positive smoothing in (L-90024.7) finally gives

\[
\boxed{
 \mathcal B_X(m)\ge0\quad\text{for every }m,X,
 \qquad
 \mathcal B_X(m)=0\quad(m\le X/64\text{ or }m\ge X).
}
\tag{L-90024.12}
\]

In fact the inequalities are strict for `X/64<m<X`. Thus the apparently signed
seven-scale combination is one positive compact parabolic atom.

## 3. Curvature has the exact sign pattern `+ - +`

For `0<m<X` the unfiltered seed satisfies

\[
 b_X''(m)=m^{-3/2}\left(1-\frac12\log\frac Xm\right).
\tag{L-90024.13}
\]

Write

\[
 u=\log_2(X/m).
\]

Away from the six scale knots,

\[
\boxed{
 \mathcal B_X''(m)=m^{-3/2}K_*(u),
 \qquad
 K_*(u)=\sum_{0\le j\le u}c_j
 \left(1-\frac h2(u-j)\right).
}
\tag{L-90024.14}
\]

On each unit interval `K_*` is affine. Direct endpoint evaluation in
`Q(sqrt(2),log 2)` gives the rigorous corridors

\[
\begin{array}{c|c}
 u\text{-interval}&K_*(u)\\ \hline
(0,1)&(0,\infty)\\
(1,2)&(-\infty,0)\\
(2,3)&(-\infty,0)\\
(3,4)&(-\infty,0)\\
(4,5)&(-\infty,0)\\
(5,6)&(0,\infty).
\end{array}
\tag{L-90024.15}
\]

For example, after division by the positive factor `4sqrt(2)`, the six affine
pieces lie respectively in

\[
(13/20,1),\quad(-1/3,-3/10),\quad(-9/10,-7/10),
\quad(-1,-2/3),\quad(-2/5,-1/5),\quad(7/10,1),
\tag{L-90024.16}
\]

using only the rational enclosures

\[
0.6931<\log2<0.6932,
\qquad
1.4142<\sqrt2<1.4143.
\]

Consequently

\[
\boxed{
\begin{aligned}
 \mathcal B_X''(m)&>0,
 &&X/2<m<X,\\
 \mathcal B_X''(m)&<0,
 &&X/32<m<X/2,\\
 \mathcal B_X''(m)&>0,
 &&X/64<m<X/32.
\end{aligned}}
\tag{L-90024.17}
\]

The compact positive seed is therefore convex on the two boundary octaves and
concave on the four middle octaves.

## 4. Occupancy identity for an arbitrary compact seed

For an integer column `q>=2`, let

\[
\mathcal U_q=\bigcup_{k\ge1}[kq,kq+1],
\qquad
\Delta_q(x)=\frac xq-|\mathcal U_q\cap[q,x]|.
\tag{L-90024.18}
\]

Then `Delta_q(x)>0`; explicitly `1/q<=Delta_q<=1`. Let `B` be a compact `C^1`
seed with piecewise integrable second derivative, and put

\[
 v_q(B)=\sum_{k\ge1}[B(kq)-B(kq+1)].
\]

Since

\[
\mathbf1_{\mathcal U_q}=q^{-1}-\Delta_q'
\]

away from the harmless corners, two integrations by parts give

\[
\boxed{
 v_q(B)-\left(\frac{B(q)}q-B'(q)\right)
 =-\int_q^\infty\Delta_q(x)B''(x)\,dx.
}
\tag{L-90024.19}
\]

For every original scale seed,

\[
\frac{b_Y(q)}q-b_Y'(q)=q^{-1/2}\log(Y/q)\mathbf1_{q\le Y}.
\tag{L-90024.20}
\]

By linearity, (L-90024.19) applied to `mathcal B_X` is exactly the filtered
column residual.

## 5. The whole endpoint is one positive-source integral

Define the positive prime occupancy source in physical coordinates by

\[
\boxed{
 \mathcal D_{\mathbb P}(x)
 =\sum_{p\le x}(\log p)\Delta_p(x)>0,
 \qquad
 R_{\mathbb P}(x)=\frac{\mathcal D_{\mathbb P}(x)}x>0.
}
\tag{L-90024.21}
\]

Summing (L-90024.19) over primes and using finite Fubini yields

\[
\boxed{
 \mathcal V_{64}(X)
 =-\int_{X/64}^{X}
   \mathcal B_X''(x)\mathcal D_{\mathbb P}(x)\,dx.
}
\tag{L-90024.22}
\]

Thus the signed radical/ramp expression of `L-90023` is, equivalently, one
pairing of a positive arithmetic source with the explicit `+ - +` curvature in
(L-90024.17).

Put

\[
 W_*(u)=2^{-u/2}K_*(u).
\tag{L-90024.23}
\]

The change of variables `x=X2^{-u}` gives the exact normalized form

\[
\boxed{
 \mathcal V_{64}(X)
 =-(\log2)\sqrt X
  \int_0^6W_*(u)R_{\mathbb P}(X2^{-u})\,du.
}
\tag{L-90024.24}
\]

The source is the same positive occupancy state isolated independently on PR
#353; no Möbius coefficient or signed prime distribution remains inside it.

## 6. Exact lobe masses and the three-window criterion

The sign pattern is

\[
 W_*>0\text{ on }(0,1)\cup(5,6),
 \qquad
 W_*<0\text{ on }(1,5).
\]

Using the antiderivative

\[
\int(\alpha+\beta u)2^{-u/2}du
=-\frac2h2^{-u/2}
 \left(\alpha+\beta u+\frac{2\beta}{h}\right),
\tag{L-90024.25}
\]

direct endpoint substitution gives

\[
\boxed{
 \int_0^1W_*(u)du=4,
 \qquad
 -\int_1^5W_*(u)du=4+q,
 \qquad
 \int_5^6W_*(u)du=q.
}
\tag{L-90024.26}
\]

In particular the total mass is zero, as required by critical neutrality.
Define the three probability-weighted source averages

\[
\boxed{
 \begin{aligned}
 \overline R_0(X)&=\frac14
  \int_0^1W_*(u)R_{\mathbb P}(X2^{-u})du,\\
 \overline R_1(X)&=\frac1{4+q}
  \int_1^5[-W_*(u)]R_{\mathbb P}(X2^{-u})du,\\
 \overline R_2(X)&=\frac1q
  \int_5^6W_*(u)R_{\mathbb P}(X2^{-u})du.
 \end{aligned}}
\tag{L-90024.27}
\]

Then (L-90024.24) becomes

\[
\boxed{
 \mathcal V_{64}(X)
 =-(\log2)\sqrt X
 \left[
 4(\overline R_0-\overline R_1)
 -q(\overline R_1-\overline R_2)
 \right].
}
\tag{L-90024.28}
\]

Therefore the preferred RH-equivalent inequality has the exact positive-source
form

\[
\boxed{
 \mathcal V_{64}(X)<0
 \iff
 \overline R_0(X)-\overline R_1(X)
 >\frac1{4\sqrt2}
  [\overline R_1(X)-\overline R_2(X)].
}
\tag{L-90024.29}
\]

This is the new conclusion-producing target: the recent-octave gain of the
normalized occupancy source must exceed `1/(4sqrt(2))` of its four-octave to
oldest-octave loss.

## 7. Exact finite cell coordinates

For `N<x<N+1`, write

\[
 \ell(N)=\log\operatorname{rad}(N),
 \qquad
 P_1(N)=\sum_{p\le N}\frac{\log p}{p},
\]

\[
 S_1(N)=(N+1)\ell(N)-\sum_{m\le N}\ell(m).
\]

Direct occupancy summation gives

\[
\boxed{
 R_{\mathbb P}(x)
 =P_1(N)-\ell(N)+\frac{S_1(N)}x.
}
\tag{L-90024.30}
\]

Thus every average in (L-90024.27) is a finite sum of elementary integrals of
one constant plus one reciprocal term over the cells intersecting `[X/64,X]`.
The three-window target contains no inaccessible continuum object.

## 8. What this changes

The factor-64 route is no longer best viewed as seven unrelated endpoint values
or as a signed prime ramp. It is exactly

```text
one nonnegative compact parabolic seed;
one positive prime occupancy source;
three fixed age windows with masses 4, 4+1/sqrt(2), 1/sqrt(2);
one sharp slope-ratio inequality with threshold 1/(4sqrt(2)).
```

The equality case for a scale-stationary normalized source is automatic because
the three masses balance. The prime-square moat produces the favorable strict
bias. A proof must control the arithmetic evolution of the positive source
across these windows; it no longer needs to manipulate signed prime or Möbius
coefficients directly.

## 9. Proof boundary

Closed exactly, subject to independent review:

1. positivity and compact support of the preferred filtered seed;
2. its exact `+ - +` curvature pattern;
3. the general occupancy-residual identity;
4. the positive-source integral for the complete endpoint;
5. exact lobe masses;
6. the three-window slope-ratio criterion;
7. exact finite cell coordinates.

Still open:

1. the source inequality (L-90024.29);
2. the factor-64 endpoint sign;
3. RH.
