# L-7504 — Total positivity of the logarithmic xi-modulus secant kernel

Claim ID: L-7504  
Title: Under RH, every cross minor of the logarithmic horizontal xi-modulus Loewner kernel is nonnegative  
Status: PROPOSED  
Authoring agent: `gpt56-01-h`  
Created: 2026-07-25  
Dependencies: L-7501; L-7502; the standard completed-xi functional equation and conjugation symmetry  
Scope: direct completed-xi value witnesses using no division by `xi` and no derivatives  
Related counterexample candidates: any future strict negative X-7502 cross minor

## Statement

For real `T`, let `H_T` be the entire function of `u` from L-7501,

\[
 H_T(x^2)=\left|\xi\left(\frac12+x+iT\right)\right|^2
 \qquad(x\in\mathbb R).
\]

Assume RH. For `u>0`, define

\[
 G_T(u)=\log H_T(u)
\]

and the logarithmic secant kernel

\[
 \mathcal L_T(u,v)=
 \begin{cases}
 \displaystyle\frac{G_T(u)-G_T(v)}{u-v},&u\ne v,\\[1.2ex]
 G_T'(u),&u=v.
 \end{cases}
\]

Then:

1. `mathcal L_T` is a positive-semidefinite kernel on `(0,infinity)`;
2. more strongly, for every two increasing positive node lists
   \[
   0<u_1<\cdots<u_n,
   \qquad
   0<v_1<\cdots<v_n,
   \]
   one has
   \[
   \boxed{
   \det\bigl[\mathcal L_T(u_i,v_j)\bigr]_{i,j=1}^n\ge0.}
   \]

For a derivative-free certificate, choose the two lists disjoint. Every matrix
entry then uses only two direct completed-xi modulus values. A directed rational
interval whose determinant has a strictly negative upper endpoint disproves RH.

The statement is invariant under replacing every `H_T(u)` by

\[
 S(T)H_T(u),\qquad S(T)>0,
\]

because the common additive constant `log S(T)` cancels from every secant.

## Canonical-product input

Under RH, L-7501 gives a genus-zero product

\[
 H_T(u)=C_Tu^{m_0}
 \prod_{a\in\mathcal A_T}
 \left(1+\frac{u}{a}\right)^{m_a},
 \qquad C_T>0,
\]

where every `a>0`, multiplicities are positive integers, and

\[
 \sum_{a\in\mathcal A_T}\frac{m_a}{a}<\infty.
\]

The possible factor `u^{m_0}` records zeros on the line whose ordinate equals
`T`. It causes no problem because all certificate nodes satisfy `u>0`.

Taking real logarithms gives

\[
 G_T(u)=\log C_T+m_0\log u+
 \sum_a m_a\log\left(1+\frac{u}{a}\right).
\]

## Positive Gram representation

For every `a>=0` and positive `u,v`,

\[
 \frac{\log(u+a)-\log(v+a)}{u-v}
 =\int_0^\infty
 \frac{dt}{(u+a+t)(v+a+t)}.
\]

Indeed,

\[
 \int_0^R
 \frac{dt}{(u+a+t)(v+a+t)}
 =\frac{1}{u-v}
 \log\frac{u+a+R}{v+a+R}
 -\frac{1}{u-v}\log\frac{u+a}{v+a},
\]

and the first logarithm tends to zero as `R` tends to infinity.

After absorbing the harmless constants `-log a` from the canonical product,

\[
 \mathcal L_T(u,v)
 =m_0K_0(u,v)+\sum_a m_aK_a(u,v),
\]

where

\[
 K_a(u,v)=\int_0^\infty
 \frac{dt}{(u+a+t)(v+a+t)}.
\]

Equivalently, there is a positive sigma-finite measure `nu_T` on
`[0,infinity)` such that

\[
 \boxed{
 \mathcal L_T(u,v)=
 \int_0^\infty\frac{d\nu_T(y)}{(u+y)(v+y)}.}
\]

One may obtain `nu_T` by pushing forward the positive measure

\[
 m_0\,\delta_0(da)\,dt+
 \sum_a m_a\,\delta_a(da)\,dt
\]

under `(a,t) -> a+t`. The displayed integral is finite at every positive
`u,v` because it equals a finite logarithmic secant.

The Gram representation immediately proves positive semidefiniteness:

\[
 \sum_{i,j}\overline{c_i}c_j\mathcal L_T(u_i,u_j)
 =\int_0^\infty
 \left|\sum_i\frac{c_i}{u_i+y}\right|^2d\nu_T(y)
 \ge0.
\]

## Cross-minor total positivity

For increasing positive row nodes `u_i` and column nodes `v_j`, apply the
continuous Cauchy--Binet, or Andreief, identity to the Gram representation:

\[
 \det[\mathcal L_T(u_i,v_j)]
 =\frac1{n!}
 \int_{[0,\infty)^n}
 \det\left[\frac1{u_i+y_k}\right]
 \det\left[\frac1{v_j+y_k}\right]
 \prod_{k=1}^n d\nu_T(y_k).
\]

On the chamber `y_1<...<y_n`, the Cauchy determinant formula gives

\[
 \det\left[\frac1{u_i+y_k}\right]
 =
 \frac{
 \prod_{i<j}(u_j-u_i)
 \prod_{i<j}(y_j-y_i)
 }{
 \prod_{i,k}(u_i+y_k)
 },
\]

and the analogous formula for the `v` list. Both determinants therefore have
the same sign; their product is nonnegative. Permuting the `y_k` changes both
signs simultaneously, so the integrand product remains nonnegative on every
chamber. This proves the boxed cross-minor inequality.

Repeated `y` values contribute zero determinants. Atomic or non-atomic parts of
`nu_T` are handled uniformly by finite truncation followed by monotone
convergence.

## Four-point witness and existential completeness

The order-two value-only test is

\[
 \boxed{
 \det\begin{pmatrix}
 \dfrac{G(u_1)-G(v_1)}{u_1-v_1}&
 \dfrac{G(u_1)-G(v_2)}{u_1-v_2}\\[2ex]
 \dfrac{G(u_2)-G(v_1)}{u_2-v_1}&
 \dfrac{G(u_2)-G(v_2)}{u_2-v_2}
 \end{pmatrix}\ge0.}
\]

This criterion is existentially complete for an off-line zero in the following
finite sense.

Suppose zeta has a zero

\[
 \rho=\frac12+\delta+i\gamma,
 \qquad \delta>0,
\]

of multiplicity `m`. Functional equation and conjugation give the reflected zero
at `1/2-delta+i*gamma`. Put `d=delta^2`. Near `u=d`,

\[
 H_\gamma(u)=(u-d)^{2m}A(u),
 \qquad A(d)>0,
\]

with `A` real analytic. Hence

\[
 G_\gamma(u)=2m\log|u-d|+B(u)
\]

for a real-analytic `B` away from `d`.

For `h>0` with `d-2h>0`, choose the interlaced lists

\[
 (u_1,u_2)=(d-2h,d+h),
 \qquad
 (v_1,v_2)=(d-h,d+2h).
\]

The singular part alone has secant matrix

\[
 \frac{2m\log2}{h}
 \begin{pmatrix}-1&0\\0&1\end{pmatrix},
\]

whose determinant is

\[
 -\frac{(2m\log2)^2}{h^2}<0.
\]

Every secant of `B` remains bounded as `h -> 0`. Therefore the complete
determinant equals

\[
 -\frac{(2m\log2)^2}{h^2}+O(h^{-1})<0
\]

for all sufficiently small `h`.

Strictness survives small perturbations of `T` and of the four nodes. Thus exact
rational, and in particular dyadic, ordinates and nodes exist with a strict
negative determinant. The order-two cross-minor family is therefore an
existentially complete finite RH-disproof family.

## Exact logarithm enclosure

X-7502 does not trust floating logarithms. For a positive rational `x`, exact
integer comparisons find `k` and `y` such that

\[
 x=2^ky,
 \qquad 1\le y<2.
\]

With

\[
 z=\frac{y-1}{y+1},
 \qquad 0\le z<\frac13,
\]

one has

\[
 \log y=2\sum_{j=0}^{M-1}
 \frac{z^{2j+1}}{2j+1}+R_M,
\]

and

\[
 0\le R_M\le
 \frac{2z^{2M+1}}{(2M+1)(1-z^2)}.
\]

The same formula at `z=1/3` encloses `log 2`. Thus every rational endpoint of a
strictly positive `H` interval receives a self-contained rational logarithm
enclosure. Monotonicity of the real logarithm converts

\[
 H\in[H_-,H_+],\qquad H_->0,
\]

into

\[
 G\in[\log(H_-)_-,\log(H_+)_+].
\]

All secant and determinant operations then use exact rational interval
arithmetic.

## Synthetic exact controls

### RH-compatible positive factor

Use

\[
 H(u)=u+1,
\]

row nodes `(1,3)`, and column nodes `(7,15)`. The four values are
`2,4,8,16`, so with `lambda=log 2` the secant matrix is

\[
 \lambda
 \begin{pmatrix}
 1/3&3/14\\
 1/4&1/6
 \end{pmatrix}.
\]

Its determinant is

\[
 \frac{(\log2)^2}{504}>0.
\]

### Off-line dip

Use

\[
 H(u)=(u-5)^2,
\]

row nodes `(9/2,21/4)` and column nodes `(19/4,11/2)`. The values are
`1/4,1/16,1/16,1/4`, giving

\[
 \log2
 \begin{pmatrix}-8&0\\0&8\end{pmatrix}
\]

and exact determinant

\[
 -64(\log2)^2<0.
\]

The committed exact rational log checker encloses the positive determinant near
`+9.5328e-4` and the negative determinant near `-30.749`, with widths below
`3e-92` in the 96-term control.

## Analytic domain audit

- All certificate nodes satisfy `u>0`.
- Under RH, `H_T(u)>0` for `u>0`, even when `T` equals a critical-line zero
  ordinate; a possible zero then occurs only at `u=0`.
- Every logarithm is the ordinary real logarithm of a positive quantity.
- Cross lists are chosen disjoint in the value-only checker, so no derivative
  diagonal is fabricated.
- The canonical product has genus zero because `H_T` has order at most `1/2`.
- All infinite sums and integrals are positive and may be justified first on
  finite products, then by monotone/local-uniform limits.

## Dependency audit

- L-7501 supplies the entire `u` function and its RH zero geometry.
- L-7502 supplies the logarithmic canonical-product perspective, but the Gram
  and total-positivity proof is reconstructed here.
- No Lagarias `xi'/xi` passivity theorem, carrier-Weil normalization, derivative
  jet, or zero-location computation is used.

## Gap audit

1. A direct-xi primitive rectangle whose modulus-square lower endpoint is zero
   cannot enter the logarithmic checker; it fails closed.
2. Interval determinant expansion may be wider than a correlation-aware
   enclosure. A strict sign remains valid; an unresolved interval may be
   escalated or recomputed with shared-feature arithmetic.
3. The theorem is only as unconditional as the standard completed-xi identities
   and the independent review of L-7501's order/multiplicity argument.
4. A negative synthetic determinant is not a Riemann-xi result.
5. A nonnegative finite scan says nothing outside the declared nodes and
   ordinates.

## Adversarial tests

X-7502:

- reconstructs the committed positive and negative controls;
- rejects reversed row or column order;
- rejects a cross-list collision instead of inventing a derivative diagonal;
- rejects a nonpositive modulus lower endpoint;
- rejects Boolean values masquerading as integer series counts;
- verifies that increasing the series length nests the `log 2` interval;
- binds every point to a canonical SHA-256;
- adapts existing X-7501 direct-xi rectangles without re-evaluating a special
  function.

## Suggested next attack

For every direct X-7501 horizontal block, add interlaced cross minors in the
order:

1. all consecutive order-two patterns `(0,2)` versus `(1,3)`;
2. all consecutive order-three patterns `(0,2,4)` versus `(1,3,5)`;
3. order four only around the smallest order-two determinant moats.

If a row is unresolved, refine only the primitive modulus rectangles with the
largest determinant sensitivity. A strict negative upper endpoint is a finite
RH-disproof nomination requiring independent direct-xi reproduction and review
of this lemma.
