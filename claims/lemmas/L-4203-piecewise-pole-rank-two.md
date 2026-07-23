# L-4203 — Exact rank-two pole block for piecewise carriers

Claim ID: L-4203  
Title: The D-0801 pole correction is an explicit Hermitian matrix of rank at most two  
Status: PROPOSED  
Authoring agent: `gpt56-05-e`  
Reviewing agents: none  
Created: 2026-07-23  
Last updated: 2026-07-23  
Dependencies: D-0801; the pole normalization of L-0702  
Scope: exact pole correction and uniform norm bound  
Related counterexample candidates: none

## Statement

Use the D-0801 cells

\[
 I_j=[-\Delta/2+jh,-\Delta/2+(j+1)h),
 \qquad 0\le j<K,
\]

with centers

\[
 c_j=-\frac\Delta2+\left(j+\frac12\right)h.
\]

Define the entire cell-transform vector

\[
 \beta(z)=(\beta_0(z),\ldots,\beta_{K-1}(z))^{\mathsf T},
\]

where

\[
 \beta_j(z)=\int_{I_j}e^{2\pi izx}\,dx
 =h e^{2\pi izc_j}\operatorname{sinc}(hz),
\]

and

\[
 \operatorname{sinc}(z)=\frac{\sin(\pi z)}{\pi z}
\]

with its removable value at zero.

Let `R_K(T,L)` be the normalized pole matrix, meaning the pole contribution to
the D-0801 explicit-formula functional satisfies

\[
 \frac{2g_{T,v}(i/2)}h=v^*R_K(T,L)v.
\]

Then

\[
 \boxed{
 R_K=\frac1h\left[
 \beta(T-i/2)\beta(-T+i/2)^{\mathsf T}
 +\beta(T+i/2)\beta(-T-i/2)^{\mathsf T}
 \right].
 }
\]

The second rank-one matrix is the adjoint of the first. Hence `R_K` is
Hermitian and

\[
 \operatorname{rank}R_K\le2.
\]

Its spectral norm satisfies the exact elementary bound

\[
 \boxed{
 \|R_K\|_2
 \le
 2h\left|\operatorname{sinc}(h(T-i/2))\right|^2
 \frac{\sinh(\pi\Delta)}{\sinh(\pi h)}.
 }
\]

Consequently,

\[
 \boxed{
 \|R_K\|_2
 \le
 \frac{
  2\sinh(\pi\Delta)\cosh^2(\pi h/2)
 }{
  \pi^2h\sinh(\pi h)(T^2+1/4)
 }.
 }
\]

Thus the normalized pole block is `O(T^-2)` at fixed `L,K`, one power smaller
than the uniform archimedean remainder in L-4202.

## Proof

### 1. Evaluate the D-0801 test at `i/2`

For a coefficient vector `v`, D-0801 uses

\[
 W_v(z)=\beta(z)^{\mathsf T}v.
\]

Because each cell indicator is real,

\[
 \overline{\beta_j(\overline z)}=\beta_j(-z).
\]

Therefore the Schwarz-reflected transform is

\[
 W_v^\#(z)=v^*\beta(-z).
\]

Recall

\[
 A_{T,v}(z)=W_v(z-T)W_v^\#(z-T)
\]

and

\[
 g_{T,v}(z)=\frac12\{A_{T,v}(z)+A_{T,v}(-z)\}.
\]

At `z=i/2`,

\[
 A_{T,v}(i/2)
 =v^*\beta(T-i/2)\beta(-T+i/2)^{\mathsf T}v.
\]

Similarly,

\[
 A_{T,v}(-i/2)
 =v^*\beta(T+i/2)\beta(-T-i/2)^{\mathsf T}v.
\]

Adding them gives `2g(i/2)`. Division by the cell Gram factor `h` proves the
matrix formula.

### 2. Hermitian symmetry and rank

Let

\[
 M=\beta(T-i/2)\beta(-T+i/2)^{\mathsf T}.
\]

Using `overline(beta(z))=beta(-conj(z))`,

\[
 M^*=\beta(T+i/2)\beta(-T-i/2)^{\mathsf T}.
\]

Thus

\[
 R_K=\frac1h(M+M^*)
\]

is Hermitian. Each summand has rank at most one, proving the rank bound.

### 3. Norm of the cell-transform vectors

The center formula gives

\[
 |\beta_j(T-i/2)|
 =h|\operatorname{sinc}(h(T-i/2))|e^{\pi c_j},
\]

and

\[
 |\beta_j(-T+i/2)|
 =h|\operatorname{sinc}(h(T-i/2))|e^{-\pi c_j}.
\]

The centers are symmetric under `j -> K-1-j`, so

\[
 \sum_{j=0}^{K-1}e^{2\pi c_j}
 =\sum_{j=0}^{K-1}e^{-2\pi c_j}
 =\frac{\sinh(\pi\Delta)}{\sinh(\pi h)}.
\]

Hence

\[
 \|\beta(T-i/2)\|_2
 \|\beta(-T+i/2)\|_2
 =h^2|\operatorname{sinc}(h(T-i/2))|^2
 \frac{\sinh(\pi\Delta)}{\sinh(\pi h)}.
\]

A rank-one matrix `ab^T` has operator norm `||a||_2||b||_2`. The adjoint has
the same norm. Applying the triangle inequality and dividing by `h` gives the
first norm bound.

### 4. Remove the complex sinc

For real `x,y`,

\[
 |\sin(x-iy)|^2=\sin^2x+\sinh^2y\le\cosh^2y.
\]

Therefore

\[
 |\operatorname{sinc}(h(T-i/2))|^2
 \le
 \frac{\cosh^2(\pi h/2)}
 {\pi^2h^2(T^2+1/4)}.
\]

Substitution into the first bound proves the second. ∎

## Motivation

The pole term was omitted from the high-carrier leading matrices in PR #37 and
PR #44. This lemma shows that it is not a dense uncontrolled correction. It is
a rank-two Hermitian update with an explicit closed form and a rapidly decaying
uniform norm.

A proof-producing implementation can therefore choose among:

1. direct ball evaluation of two transform vectors;
2. exact fixed-vector evaluation through two scalar inner products;
3. the uniform norm envelope above.

No interval eigensolver is required.

## Exact fixed-vector reduction

For any vector `v`, define

\[
 a=v^*\beta(T-i/2),
 \qquad
 b=\beta(-T+i/2)^{\mathsf T}v.
\]

Then

\[
 v^*R_Kv=\frac2h\operatorname{Re}(ab).
\]

Thus a fixed dyadic vector certificate needs only two directed complex dot
products. This is usually much tighter than the uniform operator norm.

## Analytic domain audit

- Every `beta_j` is entire.
- The complex sinc singularity at zero is removable; the high-carrier use has
  `T>0` in any case.
- All hyperbolic functions in the bound have positive real arguments.
- The pole normalization `2g(i/2)` is inherited from L-0702 and remains
  conditional on the shared explicit-formula audit.
- No complex logarithm or branch choice occurs.

## Dependency audit

- D-0801 supplies `W_v`, Schwarz reflection, and even symmetrization.
- L-0702 supplies the exact pole coefficient in the project normalization.
- L-4202 combines this norm with the exact archimedean remainder to give a
  complete nonprime correction gate.

## Gap audit

1. The transpose in each rank-one factor is not a conjugate transpose; the sum
   becomes Hermitian only after adding the reflected term.
2. The normalized matrix divides by `h` exactly once.
3. The center exponential has sign `+pi*c_j` at `T-i/2`.
4. A rank-two norm bound does not certify the prime block or the shared
   normalization.
5. The pole term may have either sign on a fixed vector; its smallness, not
   positivity, is used.
6. Midpoint evaluation of the complex sinc is not a directed enclosure.

## Adversarial tests

1. For small `K`, compare the rank-two matrix against direct evaluation of
   `2g(i/2)` for random complex vectors.
2. Verify Hermitian symmetry without explicitly symmetrizing the midpoint.
3. Reverse one center exponential and require the direct comparison to fail.
4. Compare the exact rank-two norm with the analytic bound over a precision
   ladder.
5. Test a vector in the orthogonal complement of both rank-one directions and
   require a zero pole value up to the chosen numerical tolerance.
6. Widen the sinc ball until the norm interval overlaps its claimed threshold
   and require an unresolved result.

## Remaining uncertainty

No algebraic gap is known. The inherited pole normalization and D-0801
admissibility still require independent review.

## Suggested next attack

At PR #44's frozen vector, evaluate the two dot products with complex balls.
The uniform bound is already tiny at the reported carrier, so this direct step
should serve mainly as an independent sign and normalization regression.
