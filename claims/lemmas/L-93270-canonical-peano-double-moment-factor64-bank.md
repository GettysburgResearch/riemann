# L-93270 - Canonical Peano double-moment kernel and a positive factor-64 bank

Claim ID: `L-93270`
Status: **PROPOSED COMPLETE EXACT TRANSFORM THEOREM - INDEPENDENT REVIEW REQUIRED**
Created: 2026-08-16
Depends on: PR #531 at exact head `e1b3b03d97d47c5046aa84f31e51c925d92baabd` only for route context; the proof below is elementary
Scope: compact scale kernels and Mellin transforms; no prime estimate and no RH conclusion by itself

## 1. The canonical Peano potential

Put

\[
\Phi_P(x)=x(1-x)^2\mathbf 1_{[0,1]}(x),
\qquad
D=x\frac{d}{dx}.
\tag{L-93270.1}
\]

Define its scale curvature by

\[
W_P(x)=\frac{D^2\Phi_P(x)}x.
\tag{L-93270.2}
\]

On `0<x<1`,

\[
\boxed{W_P(x)=1-8x+9x^2.}
\tag{L-93270.3}
\]

The Mellin transform is

\[
\boxed{
\widehat W_P(s)
=\int_0^1W_P(x)x^{s-1}\,dx
=\frac{2(s-1)^2}{s(s+1)(s+2)}.
}
\tag{L-93270.4}
\]

Thus

\[
\int_0^1W_P(x)\,dx=0,
\qquad
\int_0^1W_P(x)\log x\,dx=0,
\tag{L-93270.5}
\]

and the zero at `s=1` is exactly double.

The quadratic `1-8x+9x^2` has two distinct roots in `(0,1)`, so it has the minimum two sign changes compatible with two independent vanished scale moments. A nonzero one-switch real kernel cannot have both moments zero: if it is nonnegative before its unique switch and nonpositive afterward, then `log x` is strictly increasing and the two signed centroids cannot agree unless the kernel vanishes.

## 2. A positive factor-64 scale bank

Let

\[
(Tf)(x)=f(4x),
\tag{L-93270.6}
\]

where every compact kernel is extended by zero outside `[0,1]`. Define

\[
\boxed{
\Phi_{64}
=(64-T)(16-T)(4-T)\Phi_P.
}
\tag{L-93270.7}
\]

Expanding the scale polynomial gives

\[
\Phi_{64}(x)
=4096\Phi_P(x)-1344\Phi_P(4x)+84\Phi_P(16x)-\Phi_P(64x).
\tag{L-93270.8}
\]

The exact physical pieces are

\[
\boxed{
\Phi_{64}(x)=
\begin{cases}
0,&0\le x\le 1/64,\\[1mm]
64x(1-64x)^2,&1/64\le x\le1/16,\\[1mm]
256x(-5+136x-320x^2),&1/16\le x\le1/4,\\[1mm]
4096x(1-x)^2,&1/4\le x\le1,\\[1mm]
0,&x\ge1.
\end{cases}
}
\tag{L-93270.9}
\]

Every piece is nonnegative. On the middle interval, the concave quadratic

\[
-5+136x-320x^2
\tag{L-93270.10}
\]

is positive at both endpoints and hence throughout the interval.

## 3. Positive causal factorization

Put

\[
L=\log4,
\qquad
b_j(v)=e^{-jv}\mathbf 1_{[0,L]}(v),
\quad j=1,2,3.
\tag{L-93270.11}
\]

In logarithmic coordinates `x=e^{-v}`, Mellin transforms become one-sided Laplace transforms. Since

\[
\int_0^L e^{-(s+j)v}\,dv
=\frac{1-4^{-(s+j)}}{s+j},
\tag{L-93270.12}
\]

and

\[
\widehat\Phi_P(s)=\frac{2}{(s+1)(s+2)(s+3)},
\tag{L-93270.13}
\]

we obtain the exact positive convolution factorization

\[
\boxed{
\Phi_{64}(e^{-v})
=8192\,(b_1*b_2*b_3)(v).
}
\tag{L-93270.14}
\]

Thus the bank is a three-stage positive causal transport, not a numerical sign observation.

## 4. Curvature multiplier and zero safety

Because `D` commutes with `T` and

\[
\frac{D^2(Tf)(x)}x=4\,T\left(\frac{D^2f}x\right)(x),
\tag{L-93270.15}
\]

its curvature kernel is

\[
W_{64}
=(64-4T)(16-4T)(4-4T)W_P.
\tag{L-93270.16}
\]

Hence

\[
\boxed{
\widehat W_{64}(s)
=
\frac{2(s-1)^2
(4-4^{1-s})(16-4^{1-s})(64-4^{1-s})}
{s(s+1)(s+2)}.
}
\tag{L-93270.17}
\]

The added zero lines are `Re s=0,-1,-2`. They do not meet the open critical strip. Every nontrivial zeta-zero pole is therefore retained by this factor-64 kernel.

## 5. Boundary

Established exactly:

1. the double-moment Peano kernel;
2. the nonnegative factor-64 physical bank;
3. its positive three-stage causal factorization;
4. the exact zero-safe Mellin multiplier.

Not established:

1. square-root cancellation for the associated prime observable;
2. an implication from positivity of `Phi_64` to positivity of its curvature;
3. RH.
