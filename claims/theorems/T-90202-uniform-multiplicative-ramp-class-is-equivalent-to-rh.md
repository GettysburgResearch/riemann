# T-90202 — Uniform Form A on the full real multiplicative cube is equivalent to the Riemann Hypothesis

Claim ID: `T-90202`  
Status: **PROPOSED COMPLETE EQUIVALENCE — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-10  
Depends on: `L-90201`; the resident one-sided prime-ramp Landau consumer of `T-90001 §4`; the classical RH Chebyshev error  
Scope: exact reduction plus standard RH-side estimation; this is a criterion for RH, not a proof of RH

## 1. Real-cube Form A

For prime parameters

\[
 x_p\in[-1,1],
\]

let `f_x` be their completely multiplicative squarefree extension and define

\[
 \operatorname{Ramp}_x(X)
 =\sum_{d\le X/2\atop d\ {\rm squarefree}}
 f_x(d)
 \sum_{2\le m\le X/d}(\log m)
 (md)^{-1/2}\log\frac{X}{md}.
 \tag{T-90202.1}
\]

Call **real-cube Form A** the assertion that, for every `epsilon>0`, there is a constant `C_epsilon` such that

\[
 \boxed{
 \operatorname{Ramp}_x(X)
 \ge4\sqrt X-C_\varepsilon X^\varepsilon
 }
 \tag{T-90202.2}
\]

for every `X>=2` and every simultaneous choice of the real prime parameters.

The vertex restriction `x_p in {+-1}` is exactly Form A over the class `H` of `T-90008`.

## 2. Exact class collapse

By divisor switching and `L-90201`,

\[
 \operatorname{Ramp}_x(X)
 =\sum_{n\le X}w_X(n)\Lambda_x(n)
 \ge\sum_{n\le X}w_X(n)\Lambda(n)
 =:\operatorname{Ramp}_\lambda(X),
 \tag{T-90202.3}
\]

where

\[
 w_X(n)=n^{-1/2}\log\frac Xn\,\mathbf1_{n\le X}.
\]

Therefore

\[
 \boxed{
 \text{real-cube Form A}
 \Longleftrightarrow
 \text{Form A over }\mathcal H
 \Longleftrightarrow
 \operatorname{Ramp}_\lambda(X)
 \ge4\sqrt X-C_\varepsilon X^\varepsilon.
 }
 \tag{T-90202.4}
\]

The implication from either class statement to the Liouville slice is specialization. The reverse implications are the pointwise theorem.

Thus the complete multiplicative class creates no additional loss, even when enlarged from signs to the full real cube.

## 3. RH implies the uniform class criterion

Assume RH. The classical von Koch estimate gives

\[
 \psi(t)=t+E(t),
 \qquad
 E(t)=O\bigl(\sqrt t\log^2(2t)\bigr).
 \tag{T-90202.5}
\]

Write

\[
 P(X)=\operatorname{Ramp}_\lambda(X)
 =\int_{1^-}^{X}t^{-1/2}\log\frac Xt\,d\psi(t).
 \tag{T-90202.6}
\]

The continuous main term is exact:

\[
 \int_1^X t^{-1/2}\log\frac Xt\,dt
 =4\sqrt X-2\log X-4.
 \tag{T-90202.7}
\]

Since

\[
 -\frac d{dt}\left(t^{-1/2}\log\frac Xt\right)
 =t^{-3/2}\left(1+\frac12\log\frac Xt\right),
 \tag{T-90202.8}
\]

Stieltjes integration by parts and (T-90202.5) give

\[
 \begin{aligned}
 \int_{1^-}^{X}w_X(t)\,dE(t)
 &=O(\log X)
 +O\left(
 \int_1^X
 \frac{\log^2(2t)}{t}
 \left(1+\log\frac Xt\right)dt
 \right)\\
 &=O(\log^4(2X)).
 \end{aligned}
 \tag{T-90202.9}
\]

Consequently

\[
 \boxed{
 P(X)=4\sqrt X+O(\log^4(2X)).
 }
 \tag{T-90202.10}
\]

For every `epsilon>0`, the logarithmic error is bounded by `C_epsilon X^epsilon`. Equation (T-90202.3) then proves real-cube Form A uniformly in all prime parameters.

## 4. The uniform class criterion implies RH

Assume real-cube Form A. Specialize to the Liouville point `x_p=-1`. Then

\[
 \sum_{n\le X}\frac{\Lambda(n)}{\sqrt n}\log\frac Xn
 \ge4\sqrt X-C_\varepsilon X^\varepsilon.
 \tag{T-90202.11}
\]

This is exactly the one-sided complete prime-power ramp consumed by `T-90001 §4` (equivalently the `T-90008 §2` lambda-slice reduction). The resident radical bridge and Landau pole-exclusion argument exclude every zeta zero with real part greater than `1/2`; functional-equation symmetry gives RH.

No estimate for another member of the class is used in this direction.

## 5. Equivalence theorem

Combining Sections 2--4,

\[
 \boxed{
 \begin{aligned}
 \mathrm{RH}
 &\Longleftrightarrow
 \operatorname{Ramp}_\lambda(X)
 =4\sqrt X+O(\log^4(2X))\\
 &\Longrightarrow
 \text{real-cube Form A}\\
 &\Longleftrightarrow
 \text{Form A over }\mathcal H\\
 &\Longrightarrow
 \mathrm{RH}.
 \end{aligned}}
 \tag{T-90202.12}
\]

In particular,

\[
 \boxed{
 \mathrm{RH}
 \Longleftrightarrow
 \text{Form A uniformly over every completely multiplicative sign source}
 \Longleftrightarrow
 \text{Form A uniformly over the full real prime cube}.
 }
 \tag{T-90202.13}
\]

The class criterion is therefore exact and free: its worst point is always Liouville, and under RH the entire uncountable cube inherits the same polylogarithmic error.

## 6. Relation to the Stage-2 deficit

`T-90009` correctly shows that a particular engine using only pretentious distances and telescope structure cannot manufacture the required power-scale estimate at the Liouville point.

The present theorem sharpens the logical location of that deficit:

```text
uniformity over H or the real cube       no deficit; exact pointwise order;
RH-side class estimate                    inherited from lambda with O(log^4 X);
production of the lambda estimate         precisely the RH-equivalent step.
```

Thus the class bootstrap is completely solved. The remaining problem is not to make Halasz supply uniform in `f`; it is to prove the single Liouville ramp estimate without assuming RH.

## 7. Proof boundary

Proved here, subject to the named resident Landau consumer:

- exact collapse of the sign class and real cube to Liouville;
- RH implies the uniform real-cube criterion with `O(log^4 X)` error;
- uniform Form A implies RH;
- the equivalence (T-90202.13).

Not proved:

- the Liouville ramp estimate unconditionally;
- RH.
