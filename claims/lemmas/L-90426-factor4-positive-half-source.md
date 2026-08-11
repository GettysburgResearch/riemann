# L-90426 — The phase-locked quartic is the critical adjoint square of a factor-four positive source

Claim ID: `L-90426`  
Title: The unique factor-16 phase-locked filter splits into a minimal factor-four annular half-source and its critical adjoint; the half-source already has positive inverse, nonnegative generalized primes, zero bare field, and a directly RH-equivalent current  
Status: **PROPOSED COMPLETE EXACT SOURCE/FRAME THEOREM — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-11  
Dependencies: `L-90423`--`L-90425`  
Scope: the factor-four half-source and critical adjoint factorization; no arithmetic current estimate

## 1. Minimal annular half-filter

Put

\[
D(y)=(1-y)(2-y)=2-3y+y^2.
\tag{L-90426.1}
\]

Define

\[
\boxed{
\mathcal G(X)
 =\mathcal H(X)-\frac32\mathcal H(X/2)
  +\frac12\mathcal H(X/4).
}
\tag{L-90426.2}
\]

Since `D(1)=D(2)=0`, this is exactly supported on `[X/4,X]`:

\[
\boxed{
\mathcal G(X)
 =\sum_{X/4<n\le X}\Lambda(n)V(n/X),
}
\tag{L-90426.3}
\]

where

\[
V(u)=
\begin{cases}
\frac12-4u,&1/4<u\le1/2,\\
2u-1,&1/2<u\le1,\\
0,&\text{otherwise}.
\end{cases}
\tag{L-90426.4}
\]

Its Mellin transform is

\[
\boxed{
\int_1^\infty \mathcal G(X)X^{-z-1}\,dX
 =\frac{D(2^{-z})}{2}
  \frac{z-1}{z(z+1)}
  \left(-\frac{\zeta'}{\zeta}(z)\right).
}
\tag{L-90426.5}
\]

The roots of `D(2^-z)` lie on `Re z=0,-1`, so no open-strip zeta zero is cancelled. Therefore

\[
\boxed{
\mathrm{RH}
\Longleftrightarrow
\mathcal G(X)=O_\epsilon(X^{1/2+\epsilon})
\quad\text{for every }\epsilon>0.
}
\tag{L-90426.6}
\]

Thus the smallest scalar in the phase-locked route is already a factor-four annular RH criterion.

## 2. Positive inverse half-source

Define

\[
\boxed{
B_D(s)=\frac{D(2^{-s})}{2\zeta(s)},
\qquad
A_D(s)=\frac{2\zeta(s)}{D(2^{-s})}.
}
\tag{L-90426.7}
\]

At two,

\[
\boxed{
A_{D,2}(y)
 =\frac1{(1-y)^2(1-y/2)}.
}
\tag{L-90426.8}
\]

Hence every inverse coefficient is positive. Its generalized primes are ordinary at odd primes and

\[
\boxed{
\Lambda_D(2^k)
 =\log2\,(2+2^{-k})>0.
}
\tag{L-90426.9}
\]

The shifted Jordan ratios `A_D(s-tau)/A_D(s)` have nonnegative formal Dirichlet coefficients for every `tau>=0`.

If `b_D` is the coefficient sequence of `B_D`, then

\[
\boxed{
\mathbf1*b_D
 =\delta_1-\frac32\delta_2+\frac12\delta_4.
}
\tag{L-90426.10}
\]

Its prefix is exactly zero above four. Thus the half-source is already zero-bare on every deep row.

## 3. Own current and finite gauge

Let

\[
q_D=-b_D\log=b_D*\Lambda_D.
\tag{L-90426.11}
\]

Then

\[
\zeta B_D'
 =\frac12\left[D'(2^{-s})
  +D(2^{-s})\left(-\frac{\zeta'}{\zeta}(s)\right)\right].
\tag{L-90426.12}
\]

Therefore the ordinary factor-four current of (L-90426.5) is the own current prefix minus one gauge supported at two and four. After factoring out `log2`, its coefficients are

\[
\boxed{\left(\frac32,-1\right).}
\tag{L-90426.13}
\]

No infinite dyadic tower and no moving derivative gauge remains.

## 4. Critical adjoint and the full phase-locked filter

On `Re z=1/2`, with `y=2^-z`, define

\[
D^\#(y)=(1-2y)(1-4y).
\tag{L-90426.14}
\]

Since `1/(2y)=conj(y)`, one has exactly

\[
\boxed{
D^\#(y)=4y^2\overline{D(y)}.
}
\tag{L-90426.15}
\]

Consequently

\[
\boxed{
Q_*(y)=D(y)D^\#(y)=4y^2|D(y)|^2
\qquad(|y|=2^{-1/2}).
}
\tag{L-90426.16}
\]

Thus the phase-locked factor-16 source is not an arbitrary quartic. It is the critical adjoint square of the factor-four positive source.

After square-root normalization,

\[
\frac{D(2^{-1/2}z)}2
 =1-\frac{3}{2\sqrt2}z+\frac14z^2,
\tag{L-90426.17}
\]

which is precisely the half-filter `p` in `L-90425`.

## 5. Strategic reduction

The complete route may therefore be organized around one minimal source:

```text
factor-four half-source B_D:
    positive inverse;
    nonnegative generalized primes;
    positive Jordan deformation;
    zero bare field;
    two-atom gauge;
    direct RH-equivalent current G;

critical adjoint D#:
    no new arithmetic source;
    forms the uniformly coercive factor-16 normal operator.
```

Any arithmetic current estimate may be proved at factor four and then transported through the exact coercive frame of `L-90425`. There is no reason to work with a larger dyadic state unless it creates genuinely new arithmetic positivity.

This reduction does not prove the factor-four current estimate. That estimate remains RH-bearing.

## 6. Proof boundary

Closed exactly here:

1. factor-four annular kernel;
2. direct RH equivalence;
3. positive inverse source;
4. nonnegative generalized primes and Jordan path;
5. exact zero-bare collapse;
6. two-atom current gauge;
7. critical-adjoint factorization;
8. identification with the coercive half-filter.

Open:

1. critical growth of `G`;
2. a prime-side positive product-gram upper bound;
3. RH.