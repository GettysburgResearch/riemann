# L-8402 — Certified critical-line zero counts may be deflated from fixed-vector Pick forms

Claim ID: L-8402  
Title: Zero-bin lower Gram contributions preserve every fixed-vector RH Pick inequality  
Status: PROPOSED  
Authoring agent: `gpt56-06-e`  
Reviewing agents: none  
Created: 2026-07-25  
Last updated: 2026-07-25  
Dependencies: D-3201, L-3202, L-4503/L-6602 for exact fixed-vector contraction  
Scope: arbitrary-height finite Pick certificates  
Related counterexample candidates: none

## Statement

Let

\[
 s_j=\frac12+z_j,
 \qquad \operatorname{Re}z_j>0,
 \qquad j=1,\ldots,n,
\]

be exact rational or Gaussian-rational points at which `xi` is nonzero. Let

\[
 K_{jk}=
 \frac{F(s_j)+\overline{F(s_k)}}{z_j+\overline{z_k}},
 \qquad F=\frac{\xi'}{\xi},
\]

and freeze an exact nonzero vector `v in C^n`. Define

\[
 \Phi_v(\gamma)=
 \sum_{j=1}^{n}
 \frac{\overline{v_j}}{z_j-i\gamma}.
 \tag{1}
\]

Let `I_r` be pairwise disjoint real intervals containing at least `m_r>=1`
critical-line zeros, counted with multiplicity. Suppose a finite exact checker
proves

\[
 0\le L_r\le
 \inf_{\gamma\in I_r}|\Phi_v(\gamma)|^2.
 \tag{2}
\]

If RH holds, then

\[
 \boxed{
 v^*Kv-\sum_r m_rL_r\ge0.
 }
 \tag{3}
\]

Thus exact sample points, an exact vector, directed primitive `F` rectangles,
certified zero bins, and a rigorous negative upper endpoint for the deflated
fixed-vector form give a finite RH-disproof witness.

## Exact contraction before enclosure

For proof production, define

\[
 c_j=2\overline{v_j}
 \sum_{k=1}^{n}
 \frac{v_k}{z_j+\overline{z_k}}.
\]

Then

\[
 v^*Kv=\operatorname{Re}\sum_j c_jF(s_j).
 \tag{4}
\]

Every primitive `F(s_j)` is therefore used once. The matrix is contracted before
its real and imaginary rectangles are widened.

For a zero bin `I=[a,b]`, exact rational complex-interval arithmetic applied to

\[
 \Phi_v(I)=
 \sum_j\frac{\overline{v_j}}{z_j-iI}
\]

produces a rectangle `R+iS` containing every `Phi_v(gamma)` for `gamma in I`.
If

\[
 d(R)=\operatorname{dist}(R,0),
 \qquad d(S)=\operatorname{dist}(S,0),
\]

then

\[
 L=d(R)^2+d(S)^2
\]

is a valid lower bound in (2). More sophisticated complex disks, affine forms,
or Taylor models may replace the rectangle if their containment proof is
checked exactly.

## Proof

Assume RH. L-3202 gives the Gram representation

\[
 K_{jk}=\sum_{\gamma}
 \frac1{z_j-i\gamma}
 \frac1{\overline{z_k}+i\gamma}.
\]

Hence

\[
 v^*Kv
 =\sum_{\gamma}
 \left|\sum_j\frac{\overline{v_j}}{z_j-i\gamma}\right|^2
 =\sum_{\gamma}|\Phi_v(\gamma)|^2.
 \tag{5}
\]

Each zero in `I_r` contributes at least `L_r`, and there are at least `m_r` of
them. Disjoint bins prevent double charging. Removing those guaranteed
contributions from (5) leaves a sum of nonnegative terms, proving (3). Equation
(4) follows by direct collection of the two halves of the Pick kernel. ∎

## Strict synthetic separation

Use one point with `z=x=1/20`, vector `v=1`, and the finite zero model of L-8401.
The ordinary Pick form is

\[
 v^*Kv=\frac{\operatorname{Re}F(s)}{x}=\frac{400}{3}>0.
\]

For the exact certified line zero at `gamma=0`,

\[
 |\Phi_v(0)|^2=\frac1{x^2}=400.
\]

The deflated Pick value is therefore

\[
 \frac{400}{3}-400=-\frac{800}{3}<0.
\]

The same finite sample is positive under ordinary Pick testing and strictly
negative after certified zero deflation.

## Certificate interface

A fixed-vector certificate should contain:

- exact sample points and exact Gaussian-rational vector;
- outward real and imaginary rectangles for every primitive `F(s_j)`;
- exact contracted coefficients in (4), reconstructed rather than trusted;
- disjoint zero bins and certified lower counts;
- a checked complex enclosure of `Phi_v(I_r)` for every bin;
- exact lower values `L_r` and the total subtracted contribution;
- one outward residual interval with negative upper endpoint;
- a complete logical-gate and primitive-feature manifest.

## Analytic domain audit

- Every point is strictly in the shifted right half-plane and must exclude a zero
  of `xi` before evaluating `F`.
- The Pick denominators have positive real part and cannot vanish.
- `Phi_v(gamma)` is rational in the exact points and the real variable `gamma`;
  its interval enclosure is finite algebra, not a zero-sum truncation.
- The proof uses the full Gram expansion only under RH.

## Dependency audit

- D-3201 fixes `F` and the completed-xi normalization.
- L-3202 supplies the RH-conditional Pick Gram representation.
- L-4503/L-6602 supply equivalent fixed-vector compression interfaces; the
  contraction is also rederived directly here.
- L-8404 can certify one-zero sign-change bins.

## Gap audit

- A lower bound on `|Phi|^2` must hold over the entire zero interval, not merely
  at its midpoint.
- A rectangle containing zero gives lower bound zero and cannot be sharpened by
  wishful correlation assumptions.
- Zero bins and primitive `F` rectangles are different proof objects and need
  independent provenance.
- A fitted pole, approximate zero ordinate, or floating eigenvector has no proof
  value.
- Exact vector scaling changes the raw score but not its sign; normalized repair
  moats should be reported for comparison.

## Adversarial tests

1. Reconstruct the one-point strict synthetic separation exactly.
2. Mutate the vector and require any claimed residual to fail replay.
3. Use a bin whose `Phi` rectangle crosses zero and require a zero subtraction.
4. Reverse the sign of the imaginary contraction coefficient and require a
   direct-matrix equality test to fail.
5. Overlap bins and require rejection.
6. Compare direct dense Pick contraction with (4) on random exact finite models.

## Remaining uncertainty

The theorem gives a larger finite witness family, but its strength depends on
finding vectors whose transfer function `Phi_v` is large on certified line-zero
bins and sensitive with the opposite sign to a hidden off-line component.

## Suggested next attack

Jointly optimize exact Pick vectors and zero-bin placement. Use an untrusted
solver to nominate a vector maximizing

\[
 \text{deflated midpoint}
 \;\text{relative to}\;
 \text{primitive and zero-bin uncertainty},
\]

then rationalize the vector and replay (3) exactly. Cross-height vectors are
especially promising because they retain both real and imaginary primitive
information.
