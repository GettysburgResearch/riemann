# T-19701 — The complete Schur-corrected selected-real-zero-kernel floor is equivalent to RH

Claim ID: `T-19701`  
Title: Vanishing negativity on a complete selected-real-zero kernel holds exactly when every zeta zero is critical  
Status: `PROPOSED — COMPLETE EQUIVALENCE WITH EXPLICIT CAPTURE HYPOTHESIS`  
Authoring agent: `gpt56-03-o`  
Created: 2026-07-31  
Dependencies: `L-19701`; `T-14307`; positive ambient complement from `T-18901`; form-core completeness  
Scope: the final boxed estimate in Issue #197

## 1. Complete kernel hierarchy

At level `j`, let the exact localized Weil form have a decomposition

\[
 \mathcal H_j=
 \begin{pmatrix}
 B_{{\rm ker},j}&Z_{{\rm ker},j}^*\\
 Z_{{\rm ker},j}&C_j
 \end{pmatrix},
 \qquad C_j\succ0,
 \tag{T-19701.1}
\]

where the finite kernel packet lies in the selected-real-zero kernel and
contains:

1. the repaired exact-radical packet;
2. every direction added by the canonical ambient-deficit capture that is
   invisible at the selected real zeros.

Put

\[
 S_{{\rm ker},j}
 =B_{{\rm ker},j}
 -Z_{{\rm ker},j}^*C_j^{-1}Z_{{\rm ker},j}.
 \tag{T-19701.2}
\]

Assume the hierarchy is complete in the following precise sense: every
supported off-line Xi-cardinal difference constructed in `L-19701` is captured
in the form/metric topology by the finite kernel packets.

## 2. Equivalence

Under the exact Weil/Xi normalization and the complete-kernel capture
hypothesis,

\[
 \boxed{
 \mathrm{RH}
 \quad\Longleftrightarrow\quad
 \exists\varepsilon_j\downarrow0:\
 S_{{\rm ker},j}
 \succeq-\varepsilon_jG_{{\rm ker},j}.}
 \tag{T-19701.3}
\]

Equivalently,

\[
 \boxed{
 \lambda_{\min}
 \left(
 B_{{\rm ker},j}
 -Z_{{\rm ker},j}^*C_j^{-1}Z_{{\rm ker},j},
 G_{{\rm ker},j}
 \right)
 \ge-\varepsilon_j,
 \qquad\varepsilon_j\to0.}
 \tag{T-19701.4}
\]

### Forward implication

Under RH the complete Weil form is nonnegative. Every finite compression is
nonnegative, and a positive-complement Schur complement is nonnegative. Take
`epsilon_j=0`.

### Reverse implication

If RH is false, choose an off-line centered zero `rho` of multiplicity `m`.
`L-19701` supplies kernel vectors whose corrected generalized Rayleigh quotient
has limsup at most

\[
 -2m/\|h_\rho\|_{G_\infty}^2<0.
\]

This contradicts every floor with `epsilon_j->0`. QED.

## 3. Strong false-RH alternative

The reverse implication is quantitative. Under false RH there is a constant
`delta_rho>0` such that

\[
 \boxed{
 \lambda_{\min}(S_{{\rm ker},j},G_{{\rm ker},j})
 \le-\delta_\rho}
 \tag{T-19701.5}
\]

cofinally. Therefore the two alternatives are separated by a fixed gap:

\[
 \begin{array}{ll}
 \mathrm{RH}:&S_{{\rm ker},j}\succeq0,\\[1mm]
 \neg\mathrm{RH}:&\limsup\lambda_{\min}
                  (S_{{\rm ker},j},G_{{\rm ker},j})<0.
 \end{array}
 \tag{T-19701.6}
\]

## 4. Composition with the existing positive stack

`T-18901` closes the infinite-dimensional complement after canonical finite
augmentation. `L-18501` closes the evaluation-visible quotient of the resulting
finite packet. `L-15306` performs the exact triangular Schur elimination.

The only unresolved part after those steps is precisely `S_(ker,j)`. Hence a
proof of either

\[
 S_{{\rm ker},j}\succeq-o(1)G_{{\rm ker},j}
 \tag{T-19701.7}
\]

or the complete radical-synthesis estimate (L-19701.32) composes with the
existing cofinal lower-envelope theorem and proves RH.

There is no additional hidden ambient or finite-dimensional algebraic gate.

## 5. Exact remaining proof-producing statement

A noncircular sufficient theorem is:

> Construct exact global radical synthesis maps for the complete enlarged
> selected-real-zero kernels and prove, uniformly in every coefficient
> direction,
> \[
> |Q_W(E_ja,E_ja)|
> +\|C_j^{-1/2}Z_{{\rm ker},j}J_ja\|^2
> \le\eta_j\|J_ja\|_{G_j}^2,
> \qquad\eta_j\to0.
> \]

This is stronger than `L2` density and weaker than identifying each finite
kernel vector with an exact radical. It is exactly the form/metric synthesis
needed by the Schur floor.

## 6. Proof boundary

- The theorem does not claim RH.
- It identifies the requested estimate as an equivalent formulation of RH once
  complete selected-zero-kernel capture is in place.
- Any future proof must establish the complete synthesis estimate or another
  argument that explicitly excludes every off-line-cardinal difference;
  renaming that step as a tail lemma does not weaken it.
