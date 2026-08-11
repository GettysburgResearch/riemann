# L-91027 — The final arithmetic Green removal is positive at every terminal scale

Claim ID: `L-91027`  
Status: **PROPOSED COMPLETE UNCONDITIONAL TERMINAL-SCALE THEOREM**  
Created: 2026-08-12  
Depends on: `L-91026`  
RH status: **unproved**

## Statement

For every

\[
 a\ge\frac12
 \qquad\text{and}\qquad
 t\ge0,
\]

the exact Green-removal density of `L-91026` satisfies

\[
 \boxed{
 \mathcal B_{2a,a}(t)
 =-c_{2a}
 +\sqrt{\frac{275}{14}}\,aE_{2a,0}(t)
 +4a^2E_{2a,1}(t)
 >0.
 }
 \tag{L-91027.1}
\]

Consequently, for `a>=1/2`,

\[
 \boxed{
 q\left(q+\sqrt\alpha a\right)
  \left(q+\sqrt\beta a\right)
 \frac{Z_{2a}(q)-c_{2a}/q}{q^3}
 }
 \tag{L-91027.2}
\]

is completely monotone, where

\[
 \alpha+\beta=\frac{163}{14},
 \qquad
 \alpha\beta=16.
\]

After convolution with the positive rational and beta/Gamma channels of `L-9506`, the corresponding completed safe-side Cauchy numerator also has a positive Laplace measure.

## Proof

Write

\[
 \kappa=\sqrt{275/14},
 \qquad
 L=\log2,
 \qquad
 \delta=1-L.
\]

For `0<=t<=L`, positivity is `L-91026.7`.

For `t>=L`, `L-91026.8` gives

\[
 \mathcal B_{2a,a}(t)
 >c_{2a}
 \left[
 -1+\kappa a\delta
 +4a^2\delta t
 +2a^2L^2
 \right].
\]

The bracket is increasing in both `a` and `t`. Its minimum on

\[
 a\ge1/2,
 \qquad
 t\ge L
\]

is therefore attained at `a=1/2,t=L`, where it equals

\[
 -1+\frac\kappa2(1-L)+L-\frac{L^2}{2}.
\]

This number is strictly positive. For example, the elementary enclosures

\[
 \kappa>4.43,
 \qquad
 0.693<L<0.694
\]

give a lower bound greater than `0.13`. Hence (L-91027.1) holds on the entire terminal region.

Equation (L-91026.2) then expresses (L-91027.2) as the Laplace transform of:

1. one positive contact at zero;
2. positive arithmetic atoms at `log n`, `n>=2`;
3. the positive continuous density `B_(2a,a)`.

Complete monotonicity follows. Convolution with the positive completed factors preserves it.

## Significance

The Green-removal obstruction is now confined to

\[
 \boxed{0<a<\frac12.}
\]

This is exactly the horizontally RH-sensitive range. The terminal scale needed by the coefficient-one recurrence is no longer conditional or asymptotic.

What remains is a cofinal proof on the open interval `(0,1/2)`, together with the exact critical-boundary intertwiner. No RH conclusion is claimed here.