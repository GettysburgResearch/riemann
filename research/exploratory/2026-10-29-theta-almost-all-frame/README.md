# Almost all Gauss-frame directions past the square-root cutoff

**Status.** A source-qualified spectral deduction from the [uniform Wu/Hecke pair bound](../2026-10-29-gauss-profile-low-rank/moving-twist-overlap.md) and the [angular theta row mean](../2026-10-29-theta-row-mean-frame/README.md). It controls an almost-full subspace of the profile span, not every profile or the orthogonal complement in the ambient source space. The cited analytic inputs are not independently proved here; no zero-free region follows. Independent review is requested.

Use the individually normalized inverse-oriented profiles indexed by all distinct good sixth-free ideals h with full norm Nh≤H, as in the full-Gram note. Let N≈H and let G be their N-by-N Gram matrix. Its diagonal is exactly 1. Wu's pairwise bound, with the existing fixed ray sector and deleted masks, gives for h≠k

    |G_hk| ≪_ε P^(−1/2+ε) H^(103/256+ε).                       (1)

It follows that

    ||G−I||_HS² ≪_ε P^(−1+ε) H^(2+103/128+ε).                   (2)

Eigenvalues outside [1/2,3/2] contribute at least 1/4 apiece to the Hilbert–Schmidt square. Thus their fraction is

    ≪_ε P^(−1+ε) H^(231/128+ε).                                (3)

For any fixed δ>0 and H≤P^(128/231−δ), after choosing losses sufficiently small this is o(1). The image V_mid of the corresponding Gram eigenspace with eigenvalues in [1/2,3/2] therefore has dimension `(1−o(1))N`; the other o(N) eigenvectors are not controlled by this argument.

The unlabelled ℓ=−1 theta row mean gives the squared overlaps with all these normalized columns as `≪P^(−1)H(PH)^ε(1+|t|)^A`. Since every singular value on the retained eigenspace is at least 1/√2,

    ||Proj_(V_mid)m_P||² ≪ P^(−1)H(PH)^ε(1+|t|)^A.                (4)

At P=Y^(6/5) and H=P^a with a<128/231 fixed, the full-row sextic operator bound `||T_(Y,P)||²≪Y^(41/30+ε)` yields

    ||T_(Y,P)Proj_(V_mid)m_P||²
       ≪ Y^(1/6+(6/5)a+ε)(1+|t|)^A.                              (5)

This is below Y throughout the stated range after choosing ε and the common height budget sufficiently small. If a>1/2, then intersecting V_mid with the orthogonal complement of any earlier full-norm conditioned span of dimension O(P^(1/2+ε)) still retains `(1−o(1))N` directions. These are abstract linear combinations; (3) does not say that a particular named profile is retained.

This improves the proportion of well-conditioned directions over the larger [trace-only partial frame](../2026-10-29-theta-row-mean-large-frame/README.md), which reaches a longer norm cutoff but controls a smaller proportion. The exact whole-span conditioning in [full-gram](../2026-10-29-theta-partial-frame/full-gram.md) is stronger below the square-root cutoff. No statement here locates the large-eigenvalue directions of the physical row operator, removes the remaining Gram directions, or proves its complementary norm is O(Y).

**Independent review.** Families and Amplified_opt checked the Wu pair exponent, Hilbert–Schmidt exceptional fraction, singular-value projection and energy arithmetic. Their reviews retain the cited analytic assumptions and the partial-subspace and complement limitations.

Other_families independently confirmed the same Hilbert–Schmidt exponent and projection/intersection calculation under the stated source inputs.
