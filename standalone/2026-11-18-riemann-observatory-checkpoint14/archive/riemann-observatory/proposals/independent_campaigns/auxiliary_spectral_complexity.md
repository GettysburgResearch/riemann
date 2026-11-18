# Finite auxiliary levels do not remove a graph counting-cost barrier

Round2,2026-11-17. Self-contained elementary reconstruction. No novelty claim; general interlacing machinery is established background. Independent skeptical proof: audits/adversarial_reviews/auxiliary_skeptic_round2.md. Third reconstruction requested. This is not a result about the locations of zeta zeros.

## Exact proposition

Let A be a self-adjoint operator with compact resolvent on a Hilbert space H. Its spectrum may be unbounded in both directions. Let M be a nonnegative integer, D an M-by-M Hermitian matrix, and B:C^M→H a bounded operator. On D(A)⊕C^M define

T = [[A,B],[B*,D]].

Both A and T have only finitely many eigenvalues in any bounded interval. For K>0 let

Delta_A(K)=N_A((0,4K])−3N_A((0,2K])+2N_A((0,K]),

with multiplicities and the corresponding definition for T. Then

|Delta_T(K)−Delta_A(K)|≤3M.

The constant3 is sharp. No bound on ||B|| or ||D|| is needed; they must be finite for each individual operator. Endpoint zero is immaterial because

Delta_A(K)=N_A((2K,4K])−2N_A((K,2K]).

The assertion concerns bounded block coupling on the stated domain. It does not automatically cover unbounded boundary evaluation couplings, arbitrary unitary energy-dependent scattering matrices, essential spectrum or noncompact resolvent.

## Finite-dimensional interlacing, proved by subspaces

For an n-by-n Hermitian matrix A_n and its (n+M)-by-(n+M) Hermitian block enlargement T_n, set xi_n(x)=#spec(T_n)≤x−#spec(A_n)≤x. Then0≤xi_n(x)≤M for all realx.

For x away from eigenvalues, the negative eigenspace of A_n−xI embeds into a negative subspace of T_n−xI, giving the lower bound. Conversely a negative subspace of T_n−xI intersects the first n coordinates in dimension at least its dimension minusM; the restricted form is A_n−xI, giving the upper bound. Right limits supply the ≤ counting convention at eigenvalues. This argument is independent of signs or sizes of the diagonal blocks.

The three-height difference for T_n minus that for A_n is

xi_n(4K)−3xi_n(2K)+2xi_n(K),

which lies between−3M and3M because all three xi values lie in[0,M]. This uses cancellation of the same reference count; bounding the three interval discrepancies separately would lose a factor.

## Passing to compact-resolvent operators without assuming a lower bound

Let P_n be finite-rank spectral projections of A exhausting its eigenbasis, with cutoff radii tending to infinity. Such projections exist by the compact-resolvent spectral theorem. Put B_n=P_nB and

T_tilde_n=[[A,B_n],[B_n*,D]].

Since B has finite-dimensional domain, strong convergence P_n→I is uniform on its finite-dimensional range: ||B_n−B||→0. Hence T_tilde_n−T is a bounded self-adjoint perturbation tending to zero in operator norm, on the common domain D(A)⊕C^M. All these operators are self-adjoint and have compact resolvent by bounded perturbation of A⊕D.

The resolvent identity gives norm-resolvent convergence T_tilde_n→T. At endpoints outside spec(T) and spec(A), Riesz projections for a bounded spectral interval converge in norm; finite-rank projections within norm<1 have the same rank. Therefore the counts in(K,2K] and(2K,4K] stabilize. This is not an arbitrary Galerkin argument: on the orthogonal complement of ran(P_n) the operator is exactly the untouched spectral tail of A, while the off-diagonal coupling converges in norm.

The active finite-dimensional block of T_tilde_n is a Hermitian enlargement of A restricted to ran(P_n); the remaining A-tail has no eigenvalues in these fixed bounded windows for sufficiently largen. Finite-dimensional interlacing therefore gives the3M bound, which passes to the limit. No absolute count below a realx is used for the limiting two-sided operator.

If K,2K or4K is an eigenvalue, choose a sequence K_j>K decreasing toK with all three scaled endpoints avoiding the two discrete spectra. The half-open counts are eventually constant at their right-limit values because only finitely many eigenvalues occur locally. Apply the bound at K_j and pass to that limit. Eigenvalues at0 never enter these two windows.

## Sharpness, including a two-sided infinite example

For M=1 take A=[3/2],D=[3/2],B=[1] andK=1. T has eigenvalues1/2 and5/2. Thus Delta_A=−2,Delta_T=1, and their difference is3. Direct sums give3M for everyM. The negative witness A=D=[5/2],B=[1] has T eigenvalues3/2,7/2 and gives difference−3.

Appending to both A and T an uncoupled diagonal tail with eigenvalues±(10+j),j≥1, gives a self-adjoint compact-resolvent operator unbounded in both directions with the same local witness. This confirms the constant is sharp in the stated abstract class. No claim of joint sharpness for every underlying quantum-graph class follows.

## Consequence for the first-order graph family

The previously checked E-channel graph has |Delta_A(K)|<3E. Adding M boundedly coupled finite auxiliary levels gives

|Delta_T(K)|<3(E+M).

For a possibly different member at eachK, matching the classical Riemann zero counts atK,2K,4K with errors≤epsilon_K K implies

3(E_K+M_K) ≥ K log2/pi−6epsilon_K K−O(logK).

Thus epsilon_K→0 forces liminf(E_K+M_K)/K≥log2/(3pi). Arbitrarily large finite couplings do not evade the channel/auxiliary-dimension cost. The auxiliary system and graph must be the same during each three-height comparison; their parameters may change with the family indexK.

## Prior-work boundary and next step

A targeted search located Dancis–Davis, *An interlacing theorem for eigenvalues of self-adjoint operators*, Linear Algebra Appl.88/89(1987),117–122, DOI10.1016/0024-3795(87)90106-6. Only its publisher identity/abstract were located in this round; the original six-page proof has not been read and is not counted as audited. Its abstract describes infinite-dimensional codimension-one interlacing. The argument above is an independent finite-compression proof, not a claim to rediscover a new interlacing theorem.

The meaningful next interface is unbounded boundary coupling realized by one self-adjoint extension. State its common symmetric restriction, deficiency dimension and domains, then determine whether an extension-theoretic interlacing theorem yields the same finite counting cost. An arbitrary k-dependent unitary S(k) cannot simply be assumed to arise this way.
