# A Hermite–Pick inertia formulation of low-order Levinson descent

## Abstract

The high-derivative Xi tail can be made asymptotically monochromatic, but the
Levinson difficulty lies at derivative order one. We introduce a finite,
coefficient-computable trace form that captures that low-order step exactly.
For a real squarefree polynomial `p` with squarefree derivative, the trace form
on `R[x]/(p')` weighted by `-p/p''`, augmented by one positive dimension, has
signature equal to the number of real roots of `p`. Wrong real extrema and
nonreal critical-point pairs occupy the negative index on one common ledger.
Polynomial multiplication gives a sign-blind congruence preconditioner. A
rank–trace ratio above `0.83625` would beat the certified `0.67250` zeta
critical-line record, while an exact sign-resolvent integral supplies a route
beyond the two-moment ceiling. We also compute the exact threshold by which the
published `0.86864` Xi-prime theorem would yield `0.694912`. No asymptotic Xi
matrix estimate or RH proof is claimed.

## 1. The critical algebra

Let `p` be real monic of degree `n`, with `p` and `p'` squarefree. Since `p'`
is squarefree, `p''` is invertible in

\[
A=\mathbb R[x]/(p').
\]

Put

\[
q=-p(p'')^{-1}\pmod {p'}
\]

and

\[
B(u,v)=\operatorname{Tr}_{A/\mathbb R}(quv).
\]

At a real critical point `c`, the local factor is the scalar

\[
q(c)=-\frac{p(c)}{p''(c)}.
\]

At a nonreal conjugate pair, the real two-dimensional factor has determinant
negative. Hence

\[
\operatorname{inertia}(B)=(G+C,E+C),
\]

with `G` good real extrema, `E` wrong real extrema and `C` nonreal critical
pairs.

## 2. Pick congruence and the root count

For `R=p/p'` and `L=p'/p`,

\[
K_R(z,w)=-\frac{K_L(z,w)}{L(z)\overline{L(w)}}.
\]

The root partial fractions of `L` give one negative direction for every real
root of `p` and one positive/one negative direction for every nonreal root
pair. The congruence reverses signs. The critical partial fractions of `R`
give one extra positive linear direction plus the form `B`. Thus

\[
\operatorname{sig}(\langle1\rangle\oplus B)=N_\mathbb R(p).
\]

In particular,

\[
N_\mathbb R(p)=1+G-E.
\]

This is reverse Rolle as an exact inertia identity rather than a scalar
moment estimate.

## 3. Coefficient matrix

Let `X` be multiplication by `x` on `A` in the monomial basis and let `Q=q(X)`.
Then

\[
B_{ij}=\operatorname{tr}(QX^{i+j}).
\]

The construction requires only Euclidean polynomial arithmetic and traces.
No critical point is factored.

## 4. Preconditioning and rank–trace

If `w` is coprime to `p'`, then

\[
B_w(u,v)=\operatorname{Tr}(qw^2uv)=B(wu,wv),
\]

so `B_w` is congruent to `B`. Put `H_w=<1> direct-sum B_w`. If `P` is its
positive index, then

\[
(\operatorname{tr}H_w)_+^2\le P\operatorname{tr}(H_w^2).
\]

Since `N_R(p)=2P-n`,

\[
\frac{N_R(p)}n\ge
2\frac{(\operatorname{tr}H_w)_+^2}{n\operatorname{tr}(H_w^2)}-1.
\]

Therefore a Xi window ratio greater than `0.83625` beats `0.67250`.

## 5. Beyond two moments

For nonsingular `H`,

\[
\operatorname{sgn}H=\frac2\pi\int_0^\infty H(H^2+t^2I)^{-1}dt.
\]

Taking traces recovers the exact signature. Rational lower approximants to the
sign function give finite, rigorous certificates using resolvent or higher
trace moments. This adds information absent from the tight first-two-moment
configuration of the existing record theorem.

## 6. Direct entire-window localization

For a regular conjugation-invariant rectangle and `M` simple critical points
of a real entire `F`, define

\[
B_{ij}=-\frac1{2\pi i}\int_{\partial\Omega}
\frac{F(z)}{F'(z)}z^{i+j}\,dz,\qquad 0\le i,j<M.
\]

Residues give the critical trace form directly. The evaluation Vandermonde is
an isomorphism, so

\[
\operatorname{inertia}B=(G+C,E+C),\qquad\operatorname{sig}B=G-E.
\]

The real reverse--Rolle identity is therefore

\[
N_{\mathbb R}(F;I)=1+\operatorname{sig}B-\epsilon_a-\epsilon_b.
\]

For any fixed source-owned analytic test family, the corresponding contour
compression `C` satisfies

\[
N_{\mathbb R}(F;I)\ge
2\frac{(\operatorname{tr}C)_+^2}{\operatorname{tr}(C^2)}
-M+1-\epsilon_a-\epsilon_b.
\]

This is already a true Xi-window object; canonical-product exhaustion is not
needed for the identity. The remaining task is the explicit-formula estimate
of its two traces or a higher sign-resolvent minorant.

## 7. External Xi-prime bridge

The frozen public formalization proves the quartic-window bound

\[
N_{0,\mathrm{simple}}(\xi')\ge0.86864N_{\xi'}.
\]

If the full real critical set of Xi has good fraction `g`, exact reverse Rolle
gives the lower bound `0.86864(2g-1)` after the zero-count comparison. Beating
`0.67250` requires

\[
g>77057/86864=0.8870993737\ldots .
\]

The clean target `g>=9/10` yields `0.694912`.

## 8. Scalar-coherence firewall

For `p=x^3-3x+3/2`, every root is real and both critical residues are negative,
but their unweighted coherence is `16/25`. A magnitude-variance quotient can
therefore fail badly even when the sign theorem is perfect. The trace-form
inertia is the correct object.

## 9. Open analytic boundary

The trace form is already localized exactly to a regular Xi rectangle. What remains is to estimate the contour compression from a fixed source, while retaining endpoint/winding terms, multiplicities and common-zero branches. No such estimate is claimed here.

```text
record beaten: false
RH established: false
```
