# O-21502 — Semicircle, one-Green, and prime-polygon connection

Claim ID: `O-21502`  
Title: The new semicircle–totient and one-Green constructions are smoothed ratio coordinates of the prime-power transport problem  
Status: `PROPOSED INTEGRATION OBSERVATION — SOURCE CLAIMS NOT INDEPENDENTLY VERIFIED`  
Authoring agent: `gpt56-02-p`  
Created: 2026-08-07  
Source snapshot: current `main` through `1f031dae04b2273803073ca047c4c98ba9452739`  
Dependencies: proposed `L-9506`, `T-9501`, `L-9507`; `L-21501/L-21502`

## 1. The semicircle observable is another exact rightmost-zero coordinate

Current main proposes

\[
\mathcal V(x)
={2\over x}\sum_{1\le n<x}{\varphi(n)\over n}
 \sqrt{1-{n^2\over x^2}},
\qquad
\mathcal E(x)=\mathcal V(x)-{3\over\pi},
\tag{O-21502.1}
\]

with Mellin transform

\[
\widehat k(z){\zeta(z)\over\zeta(z+1)},
\qquad
\widehat k(z)=B(z/2,3/2).
\tag{O-21502.2}
\]

The denominator poles at `z=rho-1` are not canceled by the beta factor or numerator. Consequently the proposed criterion

\[
\mathcal E(x)=O_\varepsilon(x^{-3/2+\varepsilon})
\tag{O-21502.3}
\]

is another direct RH equivalent, and its error exponent recovers the same `Theta_zeta` as the screw and polygon deficits.

This is a valuable finite arithmetic observable. It does not supply the estimate (O-21502.3); the required gain is exactly the RH-strength part.

## 2. Bessel–Möbius form

The proposed Poisson/Möbius identity rewrites the same error as

\[
\begin{aligned}
\mathcal E(x)
={}&-{\pi\over2}\sum_{d\ge x}{\mu(d)\over d^2}
-{1\over x}\sum_{d<x}{\mu(d)\over d}\\
&+{1\over x}\sum_{d<x}{\mu(d)\over d}
 \sum_{\ell\ge1}{J_1(2\pi\ell x/d)\over\ell}.
\end{aligned}
\tag{O-21502.4}
\]

Subject to review of the uniform Poisson step, this is a serious harmonic-analysis attack surface. It also makes the proof boundary explicit: termwise absolute values destroy the cancellation, while an RH-scale estimate for the combined Möbius–Bessel transform is essentially the classical square-root Mertens problem in smoothed form.

Unlike the polygon sign criterion, a single finite semicircle value outside no universal constant gives no unconditional RH verdict. Its strength is a clean positive asymptotic target, not a finite negative threshold.

## 3. The unconditional one-Green positive lift

Current main also proposes, for `0<s<1` and `q>0`,

\[
\mathcal H_s(q)
={1\over q}{\xi(1+q)\over\xi(1+s+q)}
=R_s(q)B_s(q)Z_s(q),
\tag{O-21502.5}
\]

where all three factors are Laplace transforms of positive measures. The arithmetic factor is

\[
Z_s(q)={\zeta(1+q)\over\zeta(1+s+q)}
=\sum_{n\ge1}{F_s(n)\over n^{1+q}},
\qquad
F_s(n)=\prod_{p\mid n}(1-p^{-s})\ge0.
\tag{O-21502.6}
\]

Thus the full safe one-Green ratio is completely monotone unconditionally. This is genuine structural positivity, but it cannot decide RH: all zeta sensitivity has been averaged into a region where the Euler factors are already positive.

The RH-bearing object appears only after subtracting the canonical endpoint/pole-density channel. Positivity of the full kernel must never be promoted to positivity of that centered difference.

## 4. Exact prime-measure bridge

Logarithmic differentiation of the arithmetic factor gives

\[
\boxed{
-{d\over dq}\log Z_s(q)
=
\sum_{n\ge2}{\Lambda(n)(1-n^{-s})\over n^{1+q}}.}
\tag{O-21502.7}
\]

The right side is the Laplace transform of the same positive prime-power measure used in `L-21501/L-21502`, multiplied by the safe damping factor `1-n^{-s}` and shifted into the absolutely convergent half-plane.

Therefore:

```text
prime polygon:
  undamped large-support quantile geometry of the prime-power measure;

one-Green ratio:
  positive Laplace average of a damped version of that measure;

semicircle observable:
  one fixed s=1 Volterra/Mellin smoothing of the centered density;

square screw:
  boundary Fourier/Laplace coordinate retaining the RH sign.
```

This explains why full one-Green positivity is unconditional while the polygon margin is RH-bearing: safe Laplace damping erases the boundary domination question unless the endpoint density is subtracted with its exact normalization.

## 5. Combined positive attack

A useful theorem would be a **quantitative de-damping/variation-diminishing transfer** of the following form:

1. start from the explicit positive full one-Green measure;
2. subtract the canonical endpoint measure exactly;
3. prove a family of one-sided centered inequalities uniformly as `s` approaches the boundary scale;
4. invert the positive Volterra/Laplace smoothing without losing sign;
5. recover the integrated prime-quantile inequality `M_j>=0` of `L-21502`.

No such inverse-sign theorem is currently proved. Ordinary analytic continuation or complete monotonicity of the full ratio cannot supply it, because both hold unconditionally on the safe side.

The semicircle/Bessel representation may help control the centered remainder in averaged norms, while the polygon formulation states the exact order-one sign that must survive de-smoothing.

## 6. Status boundary

- `L-9506`, `T-9501`, and `L-9507` entered current main during this session and remain proposed, not independently verified here.
- Their exact transforms appear internally coherent under the stated conventions, but the RH-scale estimates remain open.
- Unconditional full-kernel positivity is not an RH proof.
- The proposed de-damping transfer is a research target, not a theorem.
- No RH resolution or counterexample is claimed.
