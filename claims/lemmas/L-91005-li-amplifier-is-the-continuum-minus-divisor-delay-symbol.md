# L-91005 — The Li amplifier is the continuum-minus-divisor-delay symbol

Claim ID: `L-91005`  
Title: The fractional-part Li amplifier and the phase-locked Brun renewal are two functional calculi of the same divisor-delay symbol: one measures its Euler continuum defect, the other polynomially preconditions its singular inverse  
Status: **PROPOSED COMPLETE EXACT SYNTHESIS LEMMA — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-12  
Dependencies: `L-91001`, `L-91003`; Euler summation  
Scope: exact conceptual/algebraic unification; no positivity theorem or RH conclusion

## 1. The common symbol

Put

\[
\boxed{h(s)=\zeta(s)-1.}
\tag{L-91005.1}
\]

On the arithmetic side, `h` is the Dirichlet series of the strict divisor-delay source

\[
h(n)=\mathbf1_{n\ge2}.
\tag{L-91005.2}
\]

The Möbius inverse is

\[
\boxed{
\frac1{1+h(s)}=\frac1{\zeta(s)}.
}
\tag{L-91005.3}
\]

Thus the renewal equation `(I+K)D=G` of `L-91003` is the physical/Mellin realization of multiplication by `1+h(s)`.

## 2. The continuum analogue

The continuum density of integers has Mellin symbol

\[
\boxed{u(s)=\int_1^\infty x^{-s}\,dx=\frac1{s-1}.}
\tag{L-91005.4}
\]

The fractional-part amplifier satisfies

\[
\begin{aligned}
A(s)
&=\frac{s}{s-1}-\zeta(s)\\
&=\frac1{s-1}-[\zeta(s)-1].
\end{aligned}
\]

Therefore

\[
\boxed{A(s)=u(s)-h(s).}
\tag{L-91005.5}
\]

Equation (L-91001.3) says precisely that this continuum-minus-discrete discrepancy is the positive Euler remainder

\[
A(s)=s\int_1^\infty\{x\}x^{-s-1}\,dx.
\tag{L-91005.6}
\]

So the positive fractional-part kernel and the multiplicative renewal are not unrelated routes. They are the error and inverse calculi of the same symbol `h`.

## 3. Zero geometry

At a nontrivial zeta zero,

\[
1+h(\rho)=0,
\qquad h(\rho)=-1.
\tag{L-91005.7}
\]

Substituting in (L-91005.5),

\[
A(\rho)=1+\frac1{\rho-1}
=\frac\rho{\rho-1}.
\tag{L-91005.8}
\]

Thus the two conclusion mechanisms see the identical obstruction:

```text
Brun coordinate:
    the inverse 1/(1+h) becomes singular at h=-1;

Li coordinate:
    the Euler defect u-h leaves the unit circle exactly when Re rho != 1/2.
```

The relation is quantitative. If `rho=beta+i gamma`,

\[
|u(\rho)-h(\rho)|^2-1
=\frac{2\beta-1}{|\rho-1|^2}.
\tag{L-91005.9}
\]

## 4. Polynomial and positive-kernel calculi

The Brun projector uses polynomials

\[
Q(z)=\frac{1-R(z)}{1+z},
\qquad R(z)=\sum_{r\ {m even}}\omega_r z^r,
\tag{L-91005.10}
\]

with nonnegative probability weights. Evaluated at `h`, it replaces the singular inverse `(1+h)^-1` by a finite Möbius-free polynomial and a positive first-crossing remainder.

The Li amplifier uses powers

\[
[u(s)-h(s)]^r=A(s)^r,
\tag{L-91005.11}
\]

which, by `L-91002`, are Laplace transforms of positive fractional-part convolutions.

Hence a radical closure may seek a single two-variable functional calculus

\[
\boxed{\mathcal P_r(h,u)}
\tag{L-91005.12}
\]

with the following simultaneous properties:

1. at `h=-1`, it retains or amplifies the zero obstruction;
2. in the arithmetic convolution algebra, it has a finite nonnegative or sum-of-squares representation;
3. on the scale diagonal, its remainder is covered by `L-91004`;
4. its continuum-error factors occur only through the positive kernel `u-h=A`.

This is not an empty reformulation: the available building blocks already satisfy properties 1, 3 and 4 separately. The missing theorem is a positive factorisation joining them.

## 5. Concrete fusion target

For an even-depth probability polynomial `R`, put

\[
Q(h)=\frac{1-R(h)}{1+h}.
\tag{L-91005.13}
\]

The proposed **Fractional-Part Brun Factorisation** is an identity or inequality of the form

\[
\boxed{
Q(h)(\mathbf1-\ell)
=\sum_\nu \mathcal T_\nu(A)^*\mathcal T_\nu(A)
+\mathcal E_r,
}
\tag{L-91005.14}
\]

in the declared half-power Riesz/physical cone, where:

- each `T_nu(A)` is built from positive fractional-part convolution powers;
- the error `E_r` is supported on the near-minimal factorisation diagonal and is bounded by `L-91004`;
- the equality retains all phase-locked dyadic siblings.

A factorisation with nonnegative left evaluation on the diagonal would prove DBP and hence RH by `L-91003`.

Equation (L-91005.14) is a sharply specified research target, not a theorem claimed here.

## 6. Proof boundary

Closed exactly here:

1. the common divisor-delay symbol;
2. the continuum symbol;
3. `A=u-h`;
4. common zero geometry;
5. identification of the two exact functional calculi;
6. formulation of the source-complete fusion target.

Open:

1. Fractional-Part Brun Factorisation;
2. DBP or the Li moment bound;
3. RH.