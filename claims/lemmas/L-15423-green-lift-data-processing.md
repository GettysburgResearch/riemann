# L-15423 — Minimal Green lifts turn pointwise multipliers into quotient contractions

Claim ID: `L-15423`  
Title: Exact data-processing theorem and physical-metric transfer gate for the Volterra branch map  
Status: `PROPOSED`  
Authoring agent: `gpt56-05-l`  
Created: 2026-08-01  
Dependencies: elementary Hilbert-space quotient theory; `L-15422`  
Scope: smallest operator gate behind endpoint branch domination  
Related counterexample candidates: none

## Abstract quotient theorem

Let `H,Y` be Hilbert spaces and let

\[
 C:\mathcal H\to\mathcal Y
 \tag{L-15423.1}
\]

be a bounded surjection. Equip the range with the quotient norm

\[
 \boxed{
 \|y\|_q
 =\inf\{\|h\|_\mathcal H:Ch=y\}.}
 \tag{L-15423.2}
\]

Let

\[
 E:\mathcal Y_q\to\mathcal H
 \tag{L-15423.3}
\]

be the minimum-norm right inverse. Then

\[
 CE=I,
 \qquad
 \|Ey\|_\mathcal H=\|y\|_q.
 \tag{L-15423.4}
\]

For every contraction `K` on `H`,

\[
 \boxed{
 \|CKE\|_{\mathcal Y_q\to\mathcal Y_q}\le1.}
 \tag{L-15423.5}
\]

### Proof

For every `y`, the vector `KEy` is one admissible lift of `CKEy`. Therefore

\[
 \|CKEy\|_q
 \le\|KEy\|_\mathcal H
 \le\|Ey\|_\mathcal H
 =\|y\|_q.
 \tag{L-15423.6}
\]

No compactness, spectral approximation, or Euler--Lagrange limit is needed.

## Exact defect identity in a prescribed physical metric

Suppose instead that `Y` carries a pre-existing physical inner product and `E` is a right inverse in that metric. Put

\[
 T=CKE.
 \tag{L-15423.7}
\]

Since `CE=I`,

\[
 \boxed{
 I-T^*T
 =E^*\left(C^*C-K^*C^*CK\right)E.}
 \tag{L-15423.8}
\]

Hence the desired endpoint domination is exactly

\[
 \boxed{
 E^*\left(C^*C-K^*C^*CK\right)E\succeq0.}
 \tag{L-15423.9}
\]

This compressed Green commutator is the complete defect. It retains all phase and cancellation information discarded by scalar pointwise estimates.

## Application to the Volterra multiplier

In the current lifted branch geometry,

\[
 \kappa(s,u)=\frac{1-s-u}{1+s+u},
 \qquad
 |\kappa(s,u)|\le1,
 \tag{L-15423.10}
\]

and `K` is multiplication by `kappa`. The quotient theorem proves the contraction automatically **in the quotient norm induced by Volterra integration `C`**.

Therefore the entire remaining transfer to the original Weyl/de Branges problem is the metric-identification statement

\[
 \boxed{
 \|y\|_{\mathrm{physical}}
 =\inf_{Ch=y}\|h\|_{\mathrm{lift}}
 \quad\text{on the complete branch range}.}
 \tag{L-15423.11}
\]

Equivalently, the physical branch Gram must equal the Green-minimal quotient Gram. A one-sided comparison with a strict reserve is also sufficient, but mere norm equivalence is not: a condition number larger than one can destroy the sharp contraction constant.

## Quantitative transfer with a strict lifted moat

Suppose two norms satisfy

\[
 a\|y\|_{\rm phys}^2
 \le\|y\|_q^2
 \le b\|y\|_{\rm phys}^2
 \tag{L-15423.12}
\]

and the lifted multiplier has a strict quotient contraction

\[
 \|CKE\|_q\le\kappa_q<1.
 \tag{L-15423.13}
\]

Then

\[
 \boxed{
 \|CKE\|_{\rm phys}^2
 \le {b\over a}\kappa_q^2.}
 \tag{L-15423.14}
\]

Thus a physical moat follows whenever

\[
 \boxed{b\kappa_q^2<a.}
 \tag{L-15423.15}
\]

For the raw multiplier (L-15423.10), the essential supremum is one, so a strict moat cannot come from `|kappa|<1` alone. It must come from either:

1. exact quotient isometry together with the endpoint index/innerness mechanism;
2. trace constraints that remove the `|kappa|=1` boundary channel;
3. a source-weighted strict contraction on the actual Green-lift range.

## Smallest concrete blocker

After `L-15421` and `L-15422`, the smallest unresolved positive statement is not the full Toeplitz LMI. It is the branch-range inequality

\[
 \boxed{
 E^*(C^*C-K^*C^*CK)E\succeq0
 }
 \tag{L-15423.16}
\]

in the physical/original Weyl metric, or the stronger exact metric identity (L-15423.11).

A finite normalized quotient certificate cannot be promoted without this metric binding. Conversely, once (L-15423.16) is established uniformly in the exact full-`Phi` model, `L-15422` and `L-15421` give `T_omega^*T_omega=I`.

## Gap audit

- A multiplier contraction before applying `C` does not in general imply contraction in an unrelated output norm.
- The quotient theorem is exact and elementary; the arithmetic content lies entirely in identifying the physical norm with the Green quotient.
- The identity (L-15423.8) requires adjoints in the declared physical and lifted metrics.
- A finite-dimensional near-isometry is reconnaissance unless the closure and metric-identification theorem are proved.
