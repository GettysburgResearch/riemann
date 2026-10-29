# Quadratic Hecke density: comparison with the fourth-witness exponent

**Status.** This is a targeted, nonexhaustive source comparison. It does not independently prove the proposed fixed-field detector or source-to-family matching, and it makes no novelty claim.

For `h=2(1−σ)`, the proposed fixed-field natural squarefree-label density exponent is

    3h/(2+h) = 3(1−σ)/(2−σ).                                  (1)

## Direct match for the rational family

[Corrigan–Zhao, *Zero density theorems for families of Dirichlet L-functions*, Theorem 1.4 and equation (1.2)](https://arxiv.org/pdf/2211.00260), published in *Bulletin of the Australian Mathematical Society* 108 (2023), pp. 224–235, prove for the full collection C₂(Q) of primitive quadratic Dirichlet characters of conductor at most Q, T≳1,

    Σ_{χ∈C₂(Q)} N(σ,T;χ)
      ≪_ε (QT)^ε min{(Q³T⁴)^[(1−σ)/(2−σ)],
                      (QT)^[3(1−σ)/σ]}.                        (2)

Thus its first term has *exactly* exponent (1) in Q at bounded height, and gives the explicit height factor `T^[4(1−σ)/(2−σ)]`. At T=Q^τ a comparison must include this factor as well as the proposed bound's small-height losses. The second branch is also available, and its conductor exponent is larger than (1) for 1/2<σ<1 but its height exponent may be useful. Their proof on pp. 6–7 combines a quadratic-family fourth moment with a zero detector, so the method is also closely related. This directly covers the fixed-field candidate when K=Q (up to its bounded local twists and excluding the principal pole as appropriate), and is ordered by conductor rather than one particular index presentation. This source makes no general-number-field assertion.

## General fixed number fields

[Goldmakher–Louvel, *A quadratic large sieve inequality over number fields*, arXiv:1112.1642v2, Definition 1 and Theorem 1.1](https://arxiv.org/pdf/1112.1642), gives for a quadratic Hecke family over any fixed number field K, and arbitrary coefficients supported on squarefree good ideals,

    Σ_{Na≤M}* |Σ_{Nb≤N}* λ_b χ_b(a)|²
        ≪_{K,S,ε} (MN)^ε(M+N) Σ_{Nb≤N}* |λ_b|².               (3)

Both stars restrict to squarefree ideals and the displayed source orientation is `χ_b(a)`. Its Definition 1 assumes primitive trivial-infinity-type characters, finite-group reciprocity, and a conductor-product property after fixing the finite reciprocity class. §2 explicitly constructs the Fisher–Friedberg/FHL family, using the narrow ray class group when K has real places. Passing to the opposite orientation needs those finite reciprocity sectors; fixed numerator/denominator zero masks and fixed twists must be preserved. Theorem 1.1 is a large sieve, **not** itself a printed assertion of (1). A detector replay with one common height/profile allowance, square-part extraction for ordinary fourth moments, and control of fixed twists is a separate proof obligation.

The family can potentially be extended to all primitive quadratic Hecke characters of K ordered by conductor. Outside the finite set S containing primes over 2, the conductor is squarefree. For each such character, use its good conductor as squarefree FHL label; dividing by the corresponding FHL quadratic character leaves a quadratic character unramified outside S. Only finitely many such characters exist by class field theory, including real-place signs and the finitely many dyadic local types. Hence a proof of (1) **uniform over this finite list of fixed twists**, with the original masks and conductor comparisons, would give the full primitive quadratic conductor family up to bounded multiplicity and constants. That extension is a deduction conditional on these matching and analytic steps, not a theorem stated in Goldmakher–Louvel.

The broader [Khale–O’Kuhn–Panidapu–Sun–Zhang, Lemma 3.3](https://arxiv.org/abs/2008.09677v3), covers primitive finite-order Hecke characters in a fixed Galois field and yields, at fixed height, the less specialized exponent `2 min{3/(2−σ),2/σ}(1−σ)` in the conductor bound. Its height factor and field restrictions remain relevant. This is not a complete literature survey; no directly comparable printed arbitrary-K theorem with (1) was identified in the targeted search. In particular, do not infer novelty from absence in this search.
