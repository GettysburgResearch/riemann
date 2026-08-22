# L-90018 — Annular filters are compact splines, and critical cancellation forces a sign change

Claim ID: `L-90018` (provisional range; branch-qualified)  
Title: Every finite scale filter with two neutral moments has an exact compact hinge-spline kernel; canceling the critical square-root mode is equivalent to one positive exponential moment being zero, so no nontrivial conclusion-producing kernel can be one-signed  
Status: **PROPOSED COMPLETE EXACT NORMAL-FORM/FIREWALL LEMMA — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Date: 2026-08-10  
Depends on: `L-90009`, elementary finite differences  
Scope: exact scale-filter normal form and sign obstruction; no RH claim

## 1. General finite scale filter

Fix `R>1` and real coefficients

\[
 a_0,\ldots,a_d.
\]

Put

\[
 P(y)=\sum_{j=0}^d a_jy^j
\tag{L-90018.1}
\]

and assume the two neutral moments

\[
\boxed{
 P(1)=\sum_ja_j=0,
 \qquad
 P'(1)=\sum_jja_j=0.
}
\tag{L-90018.2}
\]

Define the compact hinge spline

\[
\boxed{
 \Phi_P(u)=\sum_{j=0}^da_j(u-j)_+.
}
\tag{L-90018.3}
\]

For `u<0`, `Phi_P(u)=0`. For `u>d`, equations (L-90018.2) give

\[
 \Phi_P(u)=u\sum_ja_j-\sum_jja_j=0.
\]

Thus

\[
\boxed{
 \operatorname{supp}\Phi_P\subset[0,d].
}
\tag{L-90018.4}
\]

It is continuous, piecewise linear, and its distributional second derivative is

\[
 \Phi_P''=\sum_{j=0}^da_j\delta_j.
\tag{L-90018.5}
\]

## 2. Exact Laplace identity

For every complex `s!=0`, compact support and two integrations by parts give

\[
\boxed{
 s^2\int_0^d\Phi_P(u)e^{su}\,du
 =\sum_{j=0}^da_je^{sj}
 =P(e^s).
}
\tag{L-90018.6}
\]

There are no boundary terms because both `Phi_P` and its exterior slopes vanish outside `[0,d]`.

In particular, the critical square-root cancellation

\[
\boxed{P(\sqrt R)=0}
\tag{L-90018.7}
\]

is equivalent to

\[
\boxed{
 \int_0^d
 \Phi_P(u)R^{u/2}\,du=0.
}
\tag{L-90018.8}
\]

## 3. Sign-change firewall

The weight `R^(u/2)` is strictly positive. Therefore a nonzero compact spline satisfying (L-90018.8) cannot be nonnegative everywhere and cannot be nonpositive everywhere.

Hence

\[
\boxed{
 P(1)=P'(1)=P(\sqrt R)=0,
 \quad P\not\equiv0
 \Longrightarrow
 \Phi_P\text{ changes sign on }(0,d).
}
\tag{L-90018.9}
\]

This is an exact obstruction, not an empirical warning. Any scale filter which simultaneously

```text
localizes the ramp;
kills its constant density;
kills the critical square-root seed mode
```

must compare two oppositely signed annular arithmetic masses. A proof cannot come from coefficientwise positivity of the filtered ramp kernel.

## 4. Complete-prime-power normal form

Retain the complete-prime-power deficit

\[
 \Delta_\Lambda(X)
 =4\sqrt X-\sum_{n\le X}{\Lambda(n)\over\sqrt n}
 \log{X\over n}
\]

from `L-90009`. Apply the scale filter

\[
 \mathcal F_P f(X)=\sum_{j=0}^da_j f(X/R^j).
\]

If `P(sqrt R)=0`, the `4sqrt(X)` term cancels. Put

\[
 u_n=\log_R(X/n).
\]

Finite switching gives the exact identity

\[
\boxed{
 \mathcal F_P\Delta_\Lambda(X)
 =-(\log R)
 \sum_{X/R^d<n\le X}
 {\Lambda(n)\over\sqrt n}
 \Phi_P(u_n).
}
\tag{L-90018.10}
\]

Thus for the prime endpoint

\[
 A(X)=\Delta_\Lambda(X)+\mathfrak M(X),
\]

every annular filter has the exact decomposition

\[
\boxed{
 \mathcal F_PA(X)
 =-(\log R)
 \sum_{X/R^d<n\le X}
 {\Lambda(n)\over\sqrt n}
 \Phi_P(\log_R(X/n))
 +\mathcal F_P\mathfrak M(X).
}
\tag{L-90018.11}
\]

The first term is the complete zero-sensitive coordinate; the second is the explicit zero-insensitive moat.

## 5. The factor-81 spline explicitly

For

\[
 P_3(y)=(1-y)^2(1-y/\sqrt3)(1+y),
 \qquad q=1/\sqrt3,
\]

the spline is

\[
\boxed{
\Phi_3(u)=
\begin{cases}
 u,&0\le u\le1,\\
 1+q-qu,&1\le u\le2,\\
 3-q-u,&2\le u\le3,\\
 q(u-4),&3\le u\le4,\\
 0,&\text{otherwise}.
\end{cases}}
\tag{L-90018.12}
\]

It has one interior sign change at

\[
\boxed{u_*=3-1/\sqrt3.}
\tag{L-90018.13}
\]

Hence

\[
 \Phi_3(u)>0\quad(0<u<u_*),
 \qquad
 \Phi_3(u)<0\quad(u_*<u<4).
\]

In arithmetic coordinates the positive and negative sectors are

\[
 X/3^{u_*}<n<X
\]

and

\[
 X/81<n<X/3^{u_*},
\]

respectively. Equation (L-90018.8) becomes

\[
 \int_0^4\Phi_3(u)3^{u/2}\,du=0.
\tag{L-90018.14}
\]

The remaining factor-81 theorem is therefore exactly a source-specific comparison between these two fixed annular sectors, plus the known negative moat. No tail maximum, floor geometry, or unspecified source remains.

## 6. Consequence for future attacks

A valid completion may exploit correlations of `Lambda` across the two sectors, a source-matched Hermitian identity, or another arithmetic mechanism. It cannot prove the filtered complete-prime-power term nonpositive merely by observing a one-signed kernel: such a kernel is ruled out by (L-90018.9).

The factor-64 numerical false lead described in the optimization report fails a different mandatory condition—zero safety in the unit disk. Together the two firewalls are:

```text
critical cancellation forces spline sign change;
off-line-pole preservation forbids filter zeros in |y|<1.
```

## 7. Proof boundary

Closed exactly:

1. compact spline representation;
2. Laplace/filter identity;
3. sign-change necessity;
4. complete-prime-power annular normal form;
5. explicit factor-81 spline and its unique sign change.

Still open:

1. the arithmetic comparison of the two factor-81 sectors;
2. the annular endpoint sign;
3. RH.
