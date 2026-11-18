# Third independent review: finite-defect self-adjoint extensions

Reviewer: li_advocate. Date:2026-11-17. The corpus proof and parent's proof were not read before reconstruction. Only the statement and suggested resolvent route were supplied. Result: the3d bound is valid without semiboundedness. A simpler anchor choice avoids the reciprocal branch seam, and an explicit nonsemibounded example shows sharpness. No novelty claim is made.

## Statement checked

Let S be a closed densely defined symmetric operator on a complex Hilbert space, with finite deficiency indices(d,d). Let A_0,A_1 be self-adjoint extensions of S on that same Hilbert space, both with compact resolvent. For K>0 define

Δ_A(K)=N_A((0,4K])−3N_A((0,2K])+2N_A((0,K]).

Then

|Δ_(A_1)(K)−Δ_(A_0)(K)|≤3d.

This is a statement about genuinely different self-adjoint extension domains; it is not restricted to bounded finite-dimensional auxiliary coupling. Compact resolvent ensures all bounded-window counts are finite, even with infinitely many negative eigenvalues.

## A common anchor below every cut

Choose a real a<K belonging to both resolvent sets. Such an anchor exists: the union of two compact-resolvent spectra is locally finite, so any bounded open interval below K contains points outside it. There is no requirement that a lie below the spectra themselves. In particular no semiboundedness is being introduced by this choice.

Put R_j=(A_j−a)^(−1). These are compact bounded self-adjoint operators. For every h∈H,

(S*−a)(R_1−R_0)h=h−h=0.

Thus V=R_1−R_0 is self-adjoint and has image in ker(S*−a).

The latter real defect space has dimension d. This requires justification; the deficiency indices at±i alone should not be quoted as if the equality at a real spectral point were automatic. Since a∈ρ(A_0), the maps

h↦h+(a−i)(A_0−a)^(−1)h,
g↦g+(i−a)(A_0−i)^(−1)g

are inverse isomorphisms between ker(S*−i) and ker(S*−a). Direct application of S* and the resolvent identity verifies this. Therefore rank V=r≤d. This argument also handles d=0, in which case the extensions coincide.

## Inertia gives a range of length r, rather than2r

Let V have p positive and m negative eigenvalues, counted with multiplicity, so p+m=r. For every positive t,

−m≤N_(R_1)([t,∞))−N_(R_0)([t,∞))≤p.                         (E1)

Here the closed tail is finite because R_j are compact and t>0. To verify(E1), write V=V_+−V_−. The order bounds R_0−V_−≤R_1≤R_0+V_+ combine with the usual finite-codimension variational argument: intersect a high-spectral subspace with ker V_+ or ker V_−, losing at most p or m dimensions. This works with the non-strict quadratic inequality≥t and hence with closed tails even if t is an eigenvalue. Strict-tail variants follow as well by endpoint limits.

For x≥K>a, reciprocal spectral mapping gives the exact identity

N_(A_j)((a,x])=N_(R_j)([1/(x−a),∞)).

Only the positive resolvent branch occurs. Define ξ(x) as the difference of these two finite counts. By(E1), ξ(x) always lies in the same interval[−m,p], of length r. There is no need to assume ξ is monotone.

Counts between0 and a contribute a constant independent of x, regardless of the sign of a, and the coefficients1−3+2 cancel that constant. Therefore

Δ_(A_1)−Δ_(A_0)=ξ(4K)−3ξ(2K)+2ξ(K).

The positive coefficients sum to3, and the negative coefficient to−3; since ξ has range contained in an interval of length r,

|ξ(4K)−3ξ(2K)+2ξ(K)|≤3r≤3d.

This proves the result with the original half-open/right-closed convention at every endpoint. No spectral-gap perturbation is required at K,2K,4K because(E1) was stated for closed resolvent tails. Zero eigenvalues cancel from Δ and require no separate argument.

## Review of the two-branch variant

A general real anchor could put cuts on both sides of a. The negative reciprocal branch then needs an oriented prefix and strict versus closed tail conventions chosen consistently; simply writing one cumulative count below a threshold is invalid when the original spectrum is unbounded below. With a right-continuous oriented prefix, the extra minus sign restores the same range[−m,p], so the suggested two-branch strategy can work. Choosing a<K avoids this bookkeeping entirely and is available under the actual hypotheses. This is a simplification, not a hidden semiboundedness assumption.

## Exact sharpness with a domain-changing extension

On L²(0,2π), let S=−i d/dx on H¹_0(0,2π). It is closed, dense and symmetric, with deficiency indices(1,1). For θ∈[0,1), its self-adjoint extension A_θ has domain

{f∈H¹(0,2π): f(2π)=exp(2πiθ)f(0)}

and spectrum {n+θ:n∈Z}, all simple. Its resolvent is compact by compact embedding of H¹ into L², and its spectrum is unbounded in both directions.

Take A_0=A_(9/10), A_1=A_(3/5), K=7/10. For A_(9/10), the counts at K,2K,4K are0,1,2, so Δ=−1. For A_(3/5), they are1,1,3, so Δ=2. The difference is exactly3. Swapping the extensions changes its sign. Direct sums of d copies attain±3d, proving that the coefficient3 is sharp in the full nonsemibounded extension class.

`experiments/code/extension_sharp_exact.py` checks these interval counts using exact Fraction arithmetic. The differential-operator domains, deficiency indices and compactness are verified analytically above, not inferred from finite matrix numerics.

Classification: independently checked with no issue found under the stated closed/dense/symmetric/common-extension/compact-resolvent hypotheses. This proof is separate from semibounded-only extension results such as the cited arXiv2311.06701 theorem; that source's assumptions are not being silently weakened by attribution. No claim about unbounded-defect restrictions, noncompact resolvents, or arbitrary singular perturbations follows.
