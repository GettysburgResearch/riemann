# L-15409 — A finite triangular window already has the universal pole-free transform

Claim ID: `L-15409`  
Title: Three compact linear pieces replace the infinite-convolution window without losing off-line-zero sensitivity  
Status: `PROPOSED`  
Authoring agent: `gpt56-05-l`  
Created: 2026-07-31  
Dependencies: elementary convolution and Laplace transforms; the logarithmic-prime distribution used in `T-15404`  
Scope: exact finite window for the positive prime-translation route  
Related counterexample candidates: none

## Window

Put

\[
 h=\log 4
 \tag{L-15409.1}
\]

and define the normalized box and its convolution square

\[
 b_h(u)=\frac1h\mathbf 1_{[0,h]}(u),
 \qquad
 F_h=b_h*b_h.
 \tag{L-15409.2}
\]

Thus

\[
 F_h(u)=\frac1{h^2}
 \begin{cases}
 u,&0\le u\le h,\\
 2h-u,&h\le u\le2h,\\
 0,&\text{otherwise}.
 \end{cases}
 \tag{L-15409.3}
\]

Define the signed pole-annihilating window

\[
 \boxed{G_h(u)=F_h(u)-2F_h(u-h).}
 \tag{L-15409.4}
\]

It is continuous, piecewise linear, and supported in `[0,3h]`. In normalized
coordinate `v=u/h`,

\[
 hG_h(hv)=
 \begin{cases}
 v,&0\le v\le1,\\
 4-3v,&1\le v\le2,\\
 2v-6,&2\le v\le3,\\
 0,&\text{otherwise}.
 \end{cases}
 \tag{L-15409.5}
\]

In particular,

\[
 \boxed{\|G_h\|_2^2=\frac8{3h}.}
 \tag{L-15409.6}
\]

## Transform and zero geometry

For complex `z`, with removable values at zero,

\[
 \widehat b_{h,L}(z)=\frac{1-e^{-hz}}{hz},
 \qquad
 \widehat F_{h,L}(z)=\left(\frac{1-e^{-hz}}{hz}\right)^2.
 \tag{L-15409.7}
\]

Therefore

\[
 \boxed{
 \widehat G_{h,L}(z)=
 \left(\frac{1-e^{-hz}}{hz}\right)^2
 (1-2e^{-hz}).}
 \tag{L-15409.8}
\]

The last factor vanishes at the shifted zeta pole:

\[
 \widehat G_{h,L}(1/2)=0,
 \tag{L-15409.9}
\]

because `e^{-h/2}=1/2`.

The box factors vanish only at

\[
 z=\frac{2\pi i k}{h},\qquad k\in\mathbb Z\setminus\{0\},
 \tag{L-15409.10}
\]

and the pole factor vanishes only at

\[
 z=\frac12-\frac{2\pi i k}{h},\qquad k\in\mathbb Z.
 \tag{L-15409.11}
\]

Hence

\[
 \boxed{
 \widehat G_{h,L}(z)\ne0
 \quad(0<\operatorname{Re}z<1/2).}
 \tag{L-15409.12}
\]

Moreover, on every fixed vertical strip,

\[
 \widehat G_{h,L}(\sigma+it)=O_h((1+|t|)^{-2}).
 \tag{L-15409.13}
\]

This decay is already sufficient for absolute summation over zeta zeros,
because the number of zeros in a unit ordinate interval is `O(log(2+|t|))`.
No `C^infinity` window is logically required.

## Raw prime statistic

Define

\[
 \boxed{
 Q_h(x)=\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
 G_h(x-\log n).}
 \tag{L-15409.14}
\]

For every fixed `x`, this is the finite prime-power annulus

\[
 e^{x-3h}\le n\le e^x.
 \tag{L-15409.15}
\]

Its unilateral Laplace transform, initially for `Re z>1/2`, is

\[
 \boxed{
 \mathcal LQ_h(z)=
 -\widehat G_{h,L}(z)
 \frac{\zeta'}{\zeta}\left(z+\frac12\right).}
 \tag{L-15409.16}
\]

The zero (L-15409.9) cancels the pole at `s=1`, while (L-15409.12) leaves every
possible shifted nontrivial zero in the open right half-plane visible.

## Finite-difference formula

Put

\[
 K(x)=\sum_{\log n\le x}
 \frac{\Lambda(n)}{\sqrt n}(x-\log n),
 \qquad K(x)=0\text{ below }\log2.
 \tag{L-15409.17}
\]

Since

\[
 F_h(u)=\frac1{h^2}
 \bigl[u_+-2(u-h)_++(u-2h)_+\bigr],
 \tag{L-15409.18}
\]

one obtains the exact four-value formula

\[
 \boxed{
 Q_h(x)=\frac1{h^2}
 \left[
 K(x)-4K(x-h)+5K(x-2h)-2K(x-3h)
 \right].}
 \tag{L-15409.19}
\]

The coefficient polynomial is

\[
 (1-r)^2(1-2r)=1-4r+5r^2-2r^3.
 \tag{L-15409.20}
\]

It has a double root at `r=1`, killing constants and linear functions, and a
root at `r=1/2`, killing the zeta-pole mode `e^{x/2}`.

## Exact RH equivalence

Subject to the standard smoothed explicit-formula and Laplace-transform
interfaces already declared in `T-15404`, the following are equivalent:

1. RH;
2. `Q_h` is bounded on a right half-line;
3. `Q_h` has uniformly bounded Cesaro mean square on a right half-line.

The converse follows from (L-15409.16): boundedness, or bounded Cesaro mean
square followed by Cauchy--Schwarz, makes the Laplace transform holomorphic in
`Re z>0`; no off-critical pole can be canceled by (L-15409.12).

Under RH, contour displacement gives an oscillatory zero expansion. The decay
(L-15409.13) makes the zero series absolutely and uniformly convergent, so
`Q_h` is bounded.

This criterion is recorded separately as `T-15406` so that the analytic review
can distinguish the elementary window algebra from the explicit-formula gate.

## Computational advantage

Compared with `L-15405`:

- there is no infinite product or spline-tail enclosure;
- every window value is one exact affine formula after two directed logarithm
  comparisons;
- the complete support ratio is exactly `e^(3h)=64`;
- the direct prime sum and the four cumulative values in (L-15409.19) provide
  independent producer paths;
- exact integration of `Q_h^2` reduces to a finite partition by prime-power
  deposition knots and linear-polynomial integration.

The infinite-convolution profile remains useful because of its much faster
transform decay and its notch conditioning. It is no longer needed for logical
universality.

## Gap audit

- Piecewise linearity is sufficient for the zero sum but requires explicit
  breakpoint conventions in a producer.
- Prime powers, not primes alone, must be included.
- Boundedness of finitely many values or finite mean-square blocks does not prove
  RH.
- The equivalence still inherits the distributional Laplace and explicit-formula
  audit of `T-15404`.
- This lemma simplifies the target; it does not prove the target bound.
