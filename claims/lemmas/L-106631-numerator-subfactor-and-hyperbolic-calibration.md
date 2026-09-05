# L-106631 — Numerator subfactor monotonicity and one-pole hyperbolic calibration

Claim ID: `L-106631`  
Status: **PROVED EXACT FOR FINITE INNER FUNCTIONS**  
Created: 2026-08-26  
Depends on: `L-106630`  
RH status: **not assumed**

Let \(B_-,B_+\) be finite upper-half-plane inner functions and let
\(P_-,P_+\) be their model-space projections.

## 1. A selected numerator subfactor is sufficient

If \(A_+\) is an inner divisor of \(B_+\), then

\[
K_{A_+}\subseteq K_{B_+},
\qquad
P_{A_+}\preceq P_+.
\]

Therefore

\[
\boxed{
\operatorname{tr}\bigl(P_-(I-P_+)\bigr)
\le
\operatorname{tr}\bigl(P_-(I-P_{A_+})\bigr).
}
\tag{L-106631.1}
\]

One may therefore select a manageable, source-owned subset of numerator
companion factors. Extra favorable numerator directions can only improve the
conclusion.

Let \(E_-\) synthesize the complete denominator block and \(E_A\) the selected
numerator block. For every matrix \(X\),

\[
\boxed{
\operatorname{tr}\bigl(P_-(I-P_+)\bigr)
\le
\left\|
(E_- -E_AX)G_-^{-1/2}
\right\|_{\mathcal S_2}^2.
}
\tag{L-106631.2}
\]

This is a constructive sufficient certificate. It does not require solving
the optimal normal equations.

## 2. Exact one-pole cost

For \(b=a+iy\) and \(c=d+iv\), \(y,v>0\), use the normalized Fourier model
vectors

\[
e_b(\xi)=\sqrt{2y}\,e^{-(y+ia)\xi},
\qquad
e_c(\xi)=\sqrt{2v}\,e^{-(v+id)\xi}.
\]

Then

\[
\left|\langle e_b,e_c\rangle\right|^2
=
\frac{4yv}{(y+v)^2+(a-d)^2}.
\]

The optimal rank-one transport cost is

\[
\boxed{
\inf_{x\in\mathbb C}\|e_b-xe_c\|^2
=
\frac{(y-v)^2+(a-d)^2}
     {(y+v)^2+(a-d)^2}.
}
\tag{L-106631.3}
\]

This is the squared upper-half-plane pseudohyperbolic distance. It vanishes
exactly when the two factors coincide and tends to one when their horizontal
separation dominates their combined depth.

## 3. Scope

Equation (L-106631.3) is a calibration, not an additive many-pole theorem.
For a clustered divisor, raw pairwise errors must be inserted into the
basis-invariant generalized residual of `L-106630`. The whitening cannot be
discarded; `R-106630` gives an exact two-column counterexample.
