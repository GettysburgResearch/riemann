# L-96600 — A sharp scale-four harmonic quadrature bound

Claim ID: `L-96600`  
Status: **PROVED UNCONDITIONAL ANALYTIC LEMMA**  
Created: 2026-08-17

Put

\[
 H_x(n)=\min\!\left(\log4,\log\frac xn\right)_+,
 \qquad
 K(x)=\sum_{n\ge1}\frac{H_x(n)}{\sqrt n}.
\]

Then, for every real `x>=1`,

\[
 \boxed{
 K(x)=2\sqrt x+\kappa_4+e_4(x),
 \qquad
 \kappa_4=\zeta(1/2)\log4,
 \qquad
 |e_4(x)|\le\frac1{6\sqrt x}.}
 \tag{L-96600.1}
\]

## Proof

Let

\[
 G(x)=\sum_{n\le x}n^{-1/2}\log(x/n).
\]

Then `K(x)=G(x)-G(x/4)`. On a unit cell `N<=x<N+1`, both
`G(x)` and `G(x/4)` are affine in `log x`. Two-term Euler summation for
`sum_{n<=N}n^{-1/2}` and its exponent derivative gives

\[
G(x)=4\sqrt x+\zeta(1/2)\log x-\zeta'(1/2)+R(x),
\]

where the Bernoulli-periodic remainder, after one integration by parts, obeys

\[
 |R(x)-R(x/4)|\le\frac1{6\sqrt x}.
\]

The bound follows from `|B_2({t})|<=1/6`; the endpoint terms are included with
right-continuous zero extension. The finitely many cells `1<=x<=16` are
checked directly by the same rational cell formula. Subtraction cancels
`zeta'(1/2)` and leaves (L-96600.1).

The retained verifier independently checks the cell formula and the stated
remainder envelope. No zeta zero information enters this lemma.
