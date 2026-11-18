# Independent skeptical review: bounded auxiliary spectral states

Reviewer: li_advocate. Date:2026-11-17. The parent's proof was not read; only the proposed statement and suggested cutoff route were supplied. Result: the3M inequality is valid under the stated bounded-coupling assumptions, including when A is unbounded in both directions, and the factor3 is sharp. This is elementary operator-theoretic negative knowledge, not a novelty claim.

## Exact statement

Let A be self-adjoint with compact resolvent on a Hilbert space H. Let D be Hermitian on C^M and B:C^M→H bounded. The block operator

T=[[A,B],[B*,D]]

is self-adjoint with compact resolvent on domain D(A)⊕C^M. For K>0 define

Δ_T(K)=N_T((0,4K])−3N_T((0,2K])+2N_T((0,K]).

Then

|Δ_T(K)−Δ_A(K)|≤3M.

All counts are finite because they concern bounded intervals and compact resolvent. No count of all eigenvalues below a threshold is used for the limiting infinite operator.

## Zero and negative-spectrum checks

The statistic is exactly

Δ_T(K)=N_T((2K,4K])−2N_T((K,2K]).

Eigenvalues in(0,K] cancel, as do any chosen common lower-reference counts. Thus0 is not a spectral endpoint that needs a gap or a perturbation convention. Negative eigenvalues cause no direct term. This identity is especially useful when A has infinitely many negative eigenvalues, for which an unrenormalized cumulative count below x would be infinite.

## Finite-dimensional interlacing

Let A_R be the restriction of A to P_R H, where P_R=1_[−R,R](A) and R→∞. This is a finite-rank spectral projection. Form

T_R=[[A_R,P_RB],[B*P_R,D]]

on P_RH⊕C^M. The matrix A_R is a principal compression of T_R of codimensionM. Cauchy interlacing implies for every real x

ξ_R(x):=F_(T_R)(x)−F_(A_R)(x), 0≤ξ_R(x)≤M,

where F_T(x) counts eigenvalues at most x, including multiplicity.

The lower-reference count cancels because1−3+2=0, so

Δ_(T_R)−Δ_(A_R)=ξ_R(4K)−3ξ_R(2K)+2ξ_R(K).

The positive weights sum to3 and the negative weights sum to−3. Since every ξ lies in[0,M], the absolute value is at most3M. It would be incorrect to assume ξ is monotone; the argument does not require it.

## Convergence without spectral pollution

Extend T_R to H⊕C^M by the unchanged A on (1−P_R)H. Call this extension T^(R). Since P_R commutes with A, this is an exact direct sum, and

T^(R)=[[A,P_RB],[B*P_R,D]].

The image of the unit ball of C^M under B is relatively compact (indeed finite-dimensional), so strong convergence P_R→I implies ||(1−P_R)B||→0. Consequently

||T^(R)−T||=||(1−P_R)B||→0,

where the difference is a bounded operator on their common unbounded domain. Self-adjointness follows from bounded perturbation of A⊕D. Compactness of the resolvent is preserved by the same bounded perturbation. The resolvent identity gives norm-resolvent convergence.

For K,2K,4K outside σ(T), the finite spectral projections onto(K,2K] and(2K,4K] converge in operator norm. One can obtain this by a finite contour around the respective isolated finite spectral sets; norm-resolvent convergence supplies convergence of the Riesz projections. Projections at norm distance<1 have equal rank, so both window counts are eventually exact. This excludes spectral pollution in these windows.

For R>4K, the untouched A tail has no spectrum in(K,4K], so Δ_(T^(R))=Δ_(T_R) and Δ_(A_R)=Δ_A. Passing to the limit in the finite inequality gives the desired bound. No assertion that the individual ξ_R converge is needed: they might carry a cutoff-dependent reference shift, but that shift is eliminated by the three coefficients.

If an endpoint lies in σ(T) or σ(A), choose K_j>K with K_j↓K so that all three multiples avoid both discrete spectra. Such a sequence exists because the excluded set is countable and locally finite around each of the three positive endpoints. The half-open/right-closed window counts are right-continuous under this common scaling, hence Δ(K_j)→Δ(K). This gives the bound with exactly the requested endpoint convention, even at eigenvalues. Again0 is irrelevant.

## Sharp exact witnesses

At K=1,M=1, choose A=[3/2],D=[3/2],B=[1]. Then T has eigenvalues1/2 and5/2. The A eigenvalue lies in(1,2], so Δ_A=−2. The T eigenvalue1/2 cancels and5/2 contributes1, so Δ_T=1. Therefore Δ_T−Δ_A=3.

For the opposite sign choose A=[3],D=[3],B=[3/2]. The T eigenvalues are3/2 and9/2; hence Δ_T=−2 while Δ_A=1, giving−3. Direct sums of M identical blocks give±3M. Appending an uncoupled diagonal tail with eigenvalues±(10+n), n≥1, to A produces an infinite-dimensional compact-resolvent operator unbounded in both directions, and leaves all these counts unchanged. Thus neither two-sided unboundedness nor infinite dimension allows an improved universal coefficient.

`experiments/code/auxiliary_sharp_exact.py` checks these witnesses using Fraction arithmetic for M=1,2,5,10; results are saved in `experiments/results/auxiliary_sharp_exact.json`. The infinite tail conclusion is analytic and requires no truncation experiment.

## Consequence and scope

If a separately established base estimate gives |Δ_A(K)|<3E, the triangle inequality yields |Δ_T(K)|<3(E+M). This is a conditional transfer of that base estimate; this review does not independently establish the graph's original E bound.

The bounded map B is material to this proof. Finite-dimensional endpoint or boundary couplings that change an unbounded operator's domain are not automatically represented by this bounded block matrix and are not covered. One-sided truncations are also not justified by this proof: the chosen projections are full two-sided spectral cutoffs, commute with A, exhaust H, and converge uniformly on B's finite-dimensional image. No statement about arbitrary Galerkin approximations is made.

Classification: independently checked with no issue in the inspected bounded-coupling theorem. The constant is sharp; the zero-endpoint and two-sided-count concerns are resolved by the window identity and full-cutoff argument.
