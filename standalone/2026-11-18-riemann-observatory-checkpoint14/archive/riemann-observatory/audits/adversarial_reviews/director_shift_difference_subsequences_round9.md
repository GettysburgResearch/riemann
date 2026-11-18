# Director adjudication: a superseded clause and the precise subsequence theorem

17 November 2026. I inspected Sklyar–Marchenko's arXiv1405.2731v2 Proposition6 and its lead-in. I read the independent source audit sklyar_marchenko63_prop6_skeptic.md, the exact version comparison finite_moment63_manzur_noor_operator_antecedents.md, and the independent full proof sklyar_runlength63_independent.md. The latest preprint v4 removes the universal clause. The journal text was inaccessible; this is not a journal-error allegation. The general group construction and resolvent results remain separately valid and credited.

The old v1–v3 assertion says every indexed subsequence of φ_n=(I−T)^k e_n fails to be a basis sequence. Even after v3 restricts to infinite index sets, a canonical orthonormal starting basis and indices spaced k+1 apart give disjoint binomial blocks. Those vectors are orthogonal with equal nonzero norm and form an orthogonal basis of their closed span. For k=1 the even indices already suffice. Ambient biorthogonals grow, but their orthogonal projections onto this subsequence span have bounded norms; inheriting ambient norms is invalid. Latest v4 omits the assertion entirely.

The following exact replacement is accepted. Let e_n be any Riesz basis with squared bounds a_0,b_0>0, T its associated right shift, k≥1 fixed, and A a set of positive integers. Then

    {(I−T)^k e_n:n∈A} is a Riesz sequence
    iff consecutive runs in A have uniformly bounded length.

If the lengths are unbounded, no ordering is a Schauder basis of its closed span. If their maximum length is r≥1, valid squared Riesz bounds are

    a_0[2−2cos(π/(r+1))]^k and b_0 4^k.

Here the shift must be the one associated to the stated basis. An arbitrary unrelated bounded operator is not covered. Empty and finite sets have the usual trivial or finite-dimensional interpretation.

For the proof conjugate by the Riesz coordinate isomorphism. A finite coefficient sequence c supported on A has first-difference energy decomposing over its consecutive runs. Each run of length≤r is a Dirichlet tridiagonal block with smallest eigenvalue at least λ_r=2−2cos(π/(r+1)). Parseval and Jensen for the nonnegative multiplier |1−e^(it)|² give

    ‖(I−S)^k c‖²≥[‖(I−S)c‖²/‖c‖²]^k ‖c‖²
                 ≥λ_r^k ‖c‖².

The upper bound is4^k. The Riesz isomorphism supplies the stated constants.

For unbounded runs there is an exact polynomial witness. Set S_m(z)=1+…+z^(m−1) and C_m=S_m^(k+1)/M_m, where M_m is its maximum coefficient. Shift its support inside a run of length at least(k+1)(m−1)+1. One coefficient is1, while

    (1−z)^k C_m=(1−z^m)^k S_m/M_m,
    ‖(1−z)^k C_m‖²=m binom(2k,k)/M_m²,
    M_m≥m^k/(k+1).

The image norm tends to zero, although the chosen individual term has norm bounded below. Any Schauder ordering would make all individual coefficient projections uniformly bounded, a contradiction. This proves the stronger no-ordering statement without assuming that a non-Riesz sequence automatically fails to be Schauder.

This replacement is an independently checked difference-energy result with a bounded source-priority search, not a claim of literature novelty. It identifies exactly when the sparse-subsequence counterexample can be used and when the original full-family obstruction survives. The versioned correction trail prevents applying an obsolete universal assertion to the modern RH operator.
