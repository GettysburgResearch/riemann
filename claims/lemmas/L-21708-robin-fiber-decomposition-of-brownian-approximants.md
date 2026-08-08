# L-21708 — Exact Robin-fiber decomposition of finite Brownian approximants

Claim ID: `L-21708`  
Title: Every symmetrized finite Brownian Mellin transform is a positive mixture of explicit Robin characteristic determinants, with the off-line mechanism confined to negative logarithmic lengths  
Status: **PROPOSED COMPLETE EXACT THEOREM PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-08  
Dependencies: positive finite Brownian cutoff mixtures from `L-21705`--`L-21707`; elementary Sturm--Liouville theory  
Scope: exact finite zero-geometry decomposition; no all-mixture real-zero theorem or RH conclusion

## 1. One positive finite Brownian law

Let `S` be any positive finite Brownian cutoff mixture: conditionally on a finite index `K`,

\[
S=S_K=\sum_{j=1}^K\frac{\Gamma_{2,j}}{j^2},
\]

with arbitrary nonnegative mixing weights of total mass one. Let

\[
T(x)=\mathbb P(S>x),
\qquad
f(x)=-T'(x)
\]

be its tail and density, and put

\[
m(s)=\pi^{-s/2}\mathbb E[S^{s/2}].
\tag{L-21708.1}
\]

The functional-equation symmetrization is

\[
\mathcal X(s)=m(s)+m(1-s).
\tag{L-21708.2}
\]

This includes the raw, logarithmic Nörlund, and central-binomial Green producers.

## 2. Tail representation

For `0<Re(s)<1`, integration by parts gives

\[
\mathbb E[S^{s/2}]
=\frac s2\int_0^\infty T(x)x^{s/2-1}dx.
\tag{L-21708.3}
\]

Therefore

\[
\boxed{
\mathcal X(s)
=\frac12\int_0^\infty\frac{T(x)}x
\left[
 s\left(\frac x\pi\right)^{s/2}
 +(1-s)\left(\frac x\pi\right)^{(1-s)/2}
\right]dx.}
\tag{L-21708.4}
\]

Set

\[
s=\frac12+z,
\qquad
 a=\frac12\log\frac x\pi.
\tag{L-21708.5}
\]

Then `x=pi exp(2a)` and the bracket in (L-21708.4) is

\[
e^{a/2}
\left[
 \cosh(az)+2z\sinh(az)
\right].
\]

Hence

\[
\boxed{
\mathcal X\!\left(\frac12+z\right)
=\int_{-\infty}^{\infty}
 W(a)H_a(z)\,da,}
\tag{L-21708.6}
\]

where

\[
\boxed{
W(a)=e^{a/2}T(\pi e^{2a})>0,}
\tag{L-21708.7}
\]

and

\[
\boxed{
H_a(z)=\cosh(az)+2z\sinh(az).}
\tag{L-21708.8}
\]

Every finite symmetrized Brownian approximant is therefore a positive mixture of one explicit one-parameter family.

## 3. Density/cosh form

Since

\[
H_a(z)=\left(1+2\frac{\partial}{\partial a}\right)\cosh(az),
\tag{L-21708.9}
\]

integration by parts in (L-21708.6) gives

\[
\boxed{
\mathcal X\!\left(\frac12+z\right)
=\int_{-\infty}^{\infty}
 K(a)\cosh(az)\,da,}
\tag{L-21708.10}
\]

where

\[
\boxed{
K(a)=W(a)-2W'(a)
=4\pi e^{5a/2}f(\pi e^{2a})>0.}
\tag{L-21708.11}
\]

The boundary terms vanish uniformly on compact subsets of `|Re(z)|<1/2`: at negative infinity `W(a)=O(e^(a/2))`, while at positive infinity the finite phase-type tail decays superexponentially in `a`.

Because `cosh(az)` is even in `a`, only the positive even kernel

\[
K_{\rm ev}(a)=K(a)+K(-a),
\qquad a>0,
\tag{L-21708.12}
\]

matters. On the critical line `z=it`, (L-21708.10) is the ordinary cosine transform of `K_ev`.

This recovers the positive Brownian Fourier kernel without importing the limiting theta function.

## 4. The exact single-fiber Sturm theorem

Fix `a>0`. Consider

\[
-u''=\lambda u
\qquad(0<x<a)
\tag{L-21708.13}
\]

with the self-adjoint boundary conditions

\[
u'(0)=0,
\qquad
u'(a)+\frac12u(a)=0.
\tag{L-21708.14}
\]

For `lambda=-z^2`, the normalized solution is `u(x)=cosh(zx)`, and the second boundary condition is exactly

\[
\frac12H_a(z)=0.
\]

The quadratic form is

\[
\int_0^a|u'(x)|^2dx+\frac12|u(a)|^2\ge0.
\]

Thus every eigenvalue is nonnegative, and every zero of `H_a` lies on the imaginary `z` axis. Equivalently, every zero of

\[
H_a(s-1/2)
\]

lies on the critical line.

Therefore

\[
\boxed{
a>0\quad\Longrightarrow\quad H_a\text{ has only critical-line zeros}.}
\tag{L-21708.15}
\]

## 5. The negative-length obstruction is exact

Let `a=-b<0`, `b>0`. Then

\[
H_{-b}(z)=\cosh(bz)-2z\sinh(bz).
\tag{L-21708.16}
\]

For real `z>0`, its zeros satisfy

\[
2z\tanh(bz)=1.
\tag{L-21708.17}
\]

The left side is strictly increasing from zero to infinity. Hence there is exactly one positive real solution, together with its reflected negative solution. The corresponding Robin form

\[
\int_0^b|u'|^2dx-\frac12|u(b)|^2
\]

has exactly one negative eigenvalue; all remaining eigenvalues are nonnegative.

Consequently

\[
\boxed{
a<0\quad\Longrightarrow\quad H_a
\text{ has exactly one reflected off-line real pair}.}
\tag{L-21708.18}
\]

The transition `a=0`, or `x=pi`, is the exact boundary between favorable and unfavorable elementary fibers.

## 6. Equal-length pairing

For `a>0` and nonnegative weights `u,v`,

\[
u H_a(z)+vH_{-a}(z)
=(u+v)\cosh(az)+2(u-v)z\sinh(az).
\tag{L-21708.19}
\]

If `u>=v`, this is, after a positive scalar normalization, the characteristic determinant of a nonnegative Robin problem. Indeed, for `u>v`, put

\[
h=\frac{u+v}{2(u-v)}>0.
\]

Then its zeros satisfy

\[
z\sinh(az)+h\cosh(az)=0.
\]

The case `u=v` is simply `2u cosh(az)`. Therefore

\[
\boxed{
u\ge v\ge0
\quad\Longrightarrow\quad
u H_a+vH_{-a}
\text{ has only imaginary zeros}.}
\tag{L-21708.20}
\]

If `v>u`, the same equation has one real pair. Thus the orientation in (L-21708.20) is sharp for a single reflected length.

## 7. Direct proof target after the decomposition

The finite Brownian real-zero problem is now a source-specific **Robin mixture** problem:

\[
\int_{a>0}W(a)H_a(z)da
+
\int_{a>0}W(-a)H_{-a}(z)da.
\tag{L-21708.21}
\]

Every positive-length fiber is already closed. Every negative-length fiber contributes one unstable mode. A valid proof must transport or Schur-complement the complete negative-length sector against the positive-length sector before taking a modulus or total variation.

The equal-length theorem suggests, but does not prove, the pointwise comparison

\[
W(a)\ge W(-a).
\tag{L-21708.22}
\]

Even (L-21708.22) would not automatically prove the full continuous mixture has only imaginary zeros: positive sums of characteristic determinants at different interval lengths need not preserve real-rootedness without a common-interlacing, canonical-system, or total-positivity theorem.

The production theorem must therefore emit one of:

1. an explicit canonical system whose characteristic determinant is (L-21708.6);
2. a common-interlacing/Obreschkoff theorem for the complete transported fiber family;
3. an all-order Lee--Yang Wronskian certificate for the even density kernel (L-21708.12);
4. a positive Schur complement proving the Hermite--Biehler modulus inequality directly.

This is a genuinely finite theorem about the phase-type tail `T`, not a prime or zeta estimate.

## 8. Mandatory firewalls

This decomposition supplies three immediate rejection tests.

1. **Positivity-only shortcut.** `W>=0` and `K>=0` are automatic for every raw cutoff, yet raw cutoffs develop off-line zeros. Positivity alone cannot prove BLNRZ.
2. **Fiberwise shortcut.** The family contains negative `a` because every finite gamma sum has support arbitrarily near zero. A proof considering only `a>0` omits an actual source sector.
3. **Independent pairing shortcut.** Spending the same positive-length mass independently on many negative fibers is invalid; a continuous no-double-spend ledger or one global canonical system is required.

## 9. Proof boundary

Closed here, subject to review:

- exact tail and density representations;
- positive Robin-fiber mixture;
- the self-adjoint positive-length theorem;
- the unique negative-length off-line pair;
- the sharp equal-length pairing theorem.

Open:

- a global canonical-system or total-positivity closure of the complete mixture;
- BLNRZ or a corresponding theorem for the central-binomial producer;
- RH.
