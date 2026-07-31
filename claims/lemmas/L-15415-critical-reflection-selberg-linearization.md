# L-15415 — Critical reflection linearizes the quadratic logarithmic-derivative energy

Claim ID: `L-15415`  
Title: The functional equation converts a reflected prime-pair product into one Selberg stream, one derivative, and one archimedean term  
Status: `PROPOSED`  
Authoring agent: `gpt56-05-l`  
Created: 2026-07-31  
Dependencies: the zeta functional equation; elementary logarithmic differentiation; Dirichlet convolution  
Scope: the `X^2` cancellation barrier in `L-15411`  
Related counterexample candidates: none

## Logarithmic derivative and reflection

Write the functional equation as

\[
 \zeta(s)=\chi(s)\zeta(1-s),
 \tag{L-15415.1}
\]

and put

\[
 F(s)=-{\zeta'\over\zeta}(s),
 \qquad
 X(s)={\chi'\over\chi}(s).
 \tag{L-15415.2}
\]

Logarithmic differentiation gives the exact meromorphic identity

\[
 \boxed{F(1-s)=-F(s)-X(s).}
 \tag{L-15415.3}
\]

Since

\[
 F'(s)=-{\zeta''\over\zeta}(s)+F(s)^2,
 \tag{L-15415.4}
\]

one obtains

\[
\boxed{
 F(s)F(1-s)
 =-F'(s)-{\zeta''\over\zeta}(s)-X(s)F(s).}
 \tag{L-15415.5}
\]

This identity is valid away from the poles and extends meromorphically.

On the critical line, away from a zero or pole,

\[
 1-s=\overline s,
 \qquad
 F(1-s)=\overline{F(s)},
\]

so (L-15415.5) becomes

\[
\boxed{
 |F(1/2+it)|^2
 =-F'(1/2+it)
  -{\zeta''\over\zeta}(1/2+it)
  -X(1/2+it)F(1/2+it).}
 \tag{L-15415.6}
\]

The right side is automatically real, although its three displayed summands
need not be real separately.

## Positive Selberg coefficient stream

For `Re s>1`,

\[
 \boxed{
 {\zeta''\over\zeta}(s)
 =\sum_{n\ge1}{A(n)\over n^s},}
 \tag{L-15415.7}
\]

where

\[
\boxed{
 A(n)=\Lambda(n)\log n+(\Lambda*\Lambda)(n)\ge0.}
 \tag{L-15415.8}
\]

Indeed, `F^2` has coefficients `Lambda*Lambda`, while `-F'` has coefficients
`Lambda(n) log n`; equation (L-15415.4) gives (L-15415.7)--(L-15415.8).

Thus the quadratic reflected product is represented by:

1. one derivative of the ordinary von Mangoldt stream;
2. one **linear positive Selberg stream** `A(n)`;
3. one explicit archimedean convolution through `X=chi'/chi`.

This eliminates an explicit double prime-power enumeration from the reflected
energy. It does not by itself make the resulting expression positive.

## Weighted vertical-line identity

Let `W` be entire and rapidly decreasing on vertical lines. On a vertical line
`Re s=c` avoiding poles, truncate at height `T` and then pass to the limit if
the boundary terms vanish. Integration by parts gives

\[
 \int_{\mathbb R}W(s)F'(s)\,dt
 =-\int_{\mathbb R}W'(s)F(s)\,dt,
 \qquad s=c+it.
 \tag{L-15415.9}
\]

Consequently

\[
\boxed{
\begin{aligned}
 \int_{\mathbb R}W(s)F(s)F(1-s)\,dt
 ={}&\int_{\mathbb R}W'(s)F(s)\,dt\\
 &-\int_{\mathbb R}W(s){\zeta''\over\zeta}(s)\,dt\\
 &-\int_{\mathbb R}W(s)X(s)F(s)\,dt.
\end{aligned}}
 \tag{L-15415.10}
\]

For `c>1`, the arithmetic terms may be expanded as absolutely convergent
single Dirichlet series. A contour displacement toward `Re s=1/2` then has a
completely explicit arithmetic/archimedean integrand; every additional term is
a residue from a zeta zero crossed by the contour.

## Triangular-window specialization

For a real pole-free prime window `G`, define the symmetric entire weight

\[
 \boxed{
 W_G(s)=
 \widehat G_L(s-1/2)
 \widehat G_L(1/2-s).}
 \tag{L-15415.11}
\]

Then

\[
 W_G(1/2+it)=|\widehat G_L(it)|^2\ge0.
 \tag{L-15415.12}
\]

For the triangular family of `L-15409/L-15414`, `W_G` decays like
`O((1+|t|)^-4)` on fixed vertical strips. It also inherits the pole-canceling
zeros at `s=0,1`.

Thus the boundary object appearing in the RH Bohr variance is exactly the
critical-line specialization of the reflected integral in (L-15415.10).
The order-`X^2` prime-pair cancellation in `L-15411` can therefore be sought
through a **linear Selberg/archimedean contour identity**, rather than by
estimating every prime pair separately.

## Completed-xi version

Put

\[
 L_\xi(s)={\xi'\over\xi}(s).
 \tag{L-15415.13}
\]

The completed functional equation gives

\[
 L_\xi(1-s)=-L_\xi(s).
 \tag{L-15415.14}
\]

Hence, on the critical line away from zeros,

\[
 \boxed{
 |L_\xi(s)|^2=-L_\xi(s)^2
 =L_\xi'(s)-{\xi''\over\xi}(s).}
 \tag{L-15415.15}
\]

This is the cleanest reflection identity. Its apparent simplicity must not be
mistaken for positivity: the two terms on the right have the same zero poles
as the left side.

## Breakthrough and exact remaining hinge

The positive mean-square problem has two mathematically distinct layers:

```text
bulk prime-pair algebra
    -> linearized exactly by (L-15415.10);

contour displacement to the critical line
    -> residue/Hardy defect carrying the zeta-zero geometry.
```

The first layer no longer requires an uncontrolled double sum. The second is
the actual RH-bearing theorem.

A viable positive completion would prove a cancellation-preserving estimate for
the contour-shift defect, for example through one of:

1. a Pick/de Branges positivity theorem for the two reflected vertical lines;
2. a matrix-valued renewal energy retaining the crossed-zero residue channels;
3. a Selberg-flow identity in which the zero residues are the only possible
   noncompact modes;
4. a direct comparison between the positive Hardy energy of `T-15406` and the
   reflected linear form (L-15415.10).

## Critical warning: reflection is not the Hardy norm off the line

For `sigma>0`,

\[
 F(1/2+\sigma+it)F(1/2-\sigma-it)
\]

is a reflected bilinear product. It is not

\[
 |F(1/2+\sigma+it)|^2.
\]

Replacing one by the other silently discards the entire strip-residue ledger
and would be circular. At `sigma=0` they agree only as boundary meromorphic
objects, where zero poles require Abel or contour regularization.

## Gap audit

- The algebraic identities (L-15415.3)--(L-15415.8) are exact.
- A production contour identity must specify indentation, multiplicities,
  horizontal boundary decay, and every trivial/pole residue.
- Positivity of the coefficients `A(n)` does not imply positivity of the full
  right side of (L-15415.10).
- The reflected integral may itself blow up at an off-line zero; linearization
  does not remove the RH obstruction.
- The lemma replaces the quadratic prime-pair bookkeeping by a linear
  arithmetic stream plus a precise contour defect. It does not bound that
  defect and therefore does not prove RH.
