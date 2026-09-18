# Corrections, supersessions, and rejected shortcuts

This ledger preserves the evolution rather than silently rewriting earlier
claims. Archived source notes keep their original bytes. The current chapters
carry qualifications beside the relevant assertions. Entries C01 and C02 also
clarify wording from the very first response during this editorial compilation.

| ID | Earlier idea / possible reading | Current disposition |
|---|---|---|
| C01 | Pairwise zeta composition is asymptotic to 2^s, so every repeated tower is a relative asymptotic. | Pairwise asymptotic is valid. Exponentiation amplifies its additive error. The displayed tetration chain is schematic; already the fourth iterate divided by 2^{2^x} tends to zero on the positive axis. |
| C02 | All iterates are ordinary meromorphic functions on C with a uniform singularity-tree type. | The second iterate has an isolated essential singularity at 1 and poles at regular 1-points. Higher iterations can have non-isolated singular behavior. Use only the domain where a composition is defined. |
| C03 | Nearly logarithmic inverse spirals are specific to zeta zeros. | Generic Koenigs linearization produces them for arbitrary seeds. The seed constant is not constrained to one real degree of freedom. |
| C04 | The inverse tree should stay on the critical line under RH. | RH concerns the original zeros only; inverse descendants may lie outside the strip. |
| C05 | The adapted xi flow is literal zeta inverse iteration. | It is deliberately a different inverse-value construction with a critical-line weight. Preserve the distinction. |
| C06 | Local conserved imaginary time proves a global first integral. | Nonreal residues create imaginary monodromy. Reflected zeros can cancel in symmetric contours without either disappearing. |
| C07 | The normalized flow or discrete map has only zero-associated equilibria. | Extra equilibria/singularities must be treated. The multiplier identities are local at xi zeros; the simpler V has the clean no-finite-sink formulation. |
| C08 | A unit-modulus discrete multiplier implies a local flow center. | The center statement belongs to the continuous holomorphic vector field after linearization. Indifferent discrete fixed-point dynamics is a different question. |
| C09 | Li multiplier sums involve all fixed points or all periodic orbits of M. | They run over zeta zeros with original multiplicities and symmetric height truncation only. |
| C10 | Averaging several fixed inverse targets removes the prime error. | The a-point formula has the same psi term for every fixed target. Canceling that term also cancels the intended prime information. No moving-target uniformity is supplied. |
| C11 | Symmetry plus all checked low zeros should exclude a distant quartet. | Multiplying xi by Q_delta,T preserves the relevant symmetries and compact agreement while adding such a quartet. Its failure to retain the Euler product is the needed arithmetic distinction. |
| C12 | A subsequence of small truncated integrals is itself a cancellation technique. | The integral already has a fixed limit. A proved upper estimate on that subsequence is still required. |
| C13 | Jensen requires the pole-canceling multiplier to be zero-free. | It does not; the Poisson--Jensen inequality has the needed direction with zeros. Pole cancellation and the nonzero derivative at 1 still matter. |
| C14 | D<0.00834 forces off-line zeros to be few, high and close to the line. | It bounds a weighted total displacement. High zeros can have tiny weight even at substantial horizontal displacement. |
| C15 | The source component resembles k^{rho-1}, so its block correlations cannot all vanish. | In these coordinates the exact kernel behaves as conj(rho) k^{1-conj(rho)} and annihilates every b_n exactly. Truncating the asymptotic loses that cancellation. |
| C16 | A persistent residual's total norm forces new Schur gain. | New vectors see only the transient residual. The persistent component is orthogonal to the entire family. |
| C17 | Any infinite set of good dyadic scales suffices. | The retained reciprocal weights must have divergent sum. Sparse good lengths suffice for some optimized-error arguments, not automatically for the mollifier length integral. |
| C18 | Full spectral synthesis follows from holomorphic division by zeta. | The converse is an unproved discrete approximation statement here; closure and derivative kernels at multiple zeros are required. |
| C19 | The l1 optimizer bound must be O(N^{1+epsilon}) to obtain a near-quadratic cutoff. | The large-sieve mean-square argument achieves that cutoff with the weaker proved bounds. It controls the tail, not the interior. |
| C20 | The implemented Gram construction is O(log) per entry and reaches 10^5. | Those were user-proposed goals. The retained code is O(N^3) construction, O(N^2) memory; 1024 was interval-certified and 2048 was floating only. |
| C21 | E_N log N has a proved limit 2+gamma-log(4*pi) for this exact class. | It is a benchmark, not a proved limit here. The sharp mollifier theorem is conditional and multiplicities matter in the lower bound. Finite undershoots are not contradictions. |
| C22 | Fixed exponential contraction of inverse branches should give geometric decay of E_N. | A fixed-factor dyadic error contraction contradicts the classical positive 1/log N lower scale. |
| C23 | The prescribed Q_N equals the optimized E_N or is monotone. | Only E_N<=Q_N is automatic. Their asymptotic roles differ. |
| C24 | Subpolynomial Q_N on a sparse unbounded subsequence suffices for the proved averaging lemma. | That proof needs all sufficiently large lengths to form the H-valued integral. |
| C25 | A hypothetical zero gives the same power lower bound at every large N. | The note gives eventual logarithmic growth and separately a limsup polynomial exponent. Do not conflate them. |
| C26 | Centered truncated-prime increments can be treated as independent. | This inserts unproved signed-correlation cancellation. Fixed-shift theorems do not automatically control the cumulative weighted kernel. |
| C27 | Functional-equation reflection supplies a bounded paired zero kernel. | The reflected kernel's H-norm diverges; a bounded defect-space duality is the missing theorem, not a consequence of the formula alone. |
| C28 | Periodic GCD positivity can replace the full weighted Gram while preserving the source. | The N=3 construction produces a negative supposed squared distance. The periodic optimizer even has actual weighted error tending to one. |
| C29 | Zero direct Ramanujan source on composites means those directions can be deleted. | They alter the Schur complement. Deleting them gives a prime-power-only family with a permanent 1/92 error floor. |
| C30 | Entrywise positivity follows from positive semidefiniteness. | The weighted Fourier kernel has W_H(1/2)<0 and exact cancellations encoding Lambda(d). |
| C31 | Every squarefree Ramanujan atom is individually indispensable. | The full support classification is for b-indices; higher multiples can satisfy the same s-coordinate constraint. Bounded prime-interaction order is nevertheless insufficient for either family. |
| C32 | The finite-support duals are new in this chat. | They are Vasyunin's classical construction, credited through Balazard. Local support consequences are separated from imported construction. |
| C33 | Completeness and rapid approximation of the dual family prove primal completeness. | Biorthogonality is not that implication. F_N and G_N differ by explicit ramp/tail terms. |
| C34 | The integer dual Gram contains only the common-divisor term. | Adjacent-divisor correlations change signs already at (2,3) and are required. |
| C35 | Exact Mobius coefficient matching completes the approximation. | It leaves the linear residual k m_N and the genuine tail. Pointwise coefficient convergence is not norm convergence. |
| C36 | Uniform trace R<11 makes the correction negligible for RH. | The inverse inequality points the other way, and a bounded trace may act strongly on a small eigenvalue or growing signed source. |
| C37 | Small tails, successful finite tests or a lower gain consumer prove the remaining upper estimate. | None provides source-specific subpolynomial cancellation. The first component already contains a classical-strength psi variance. |
| C38 | Uploaded certificates, an author's PROVED label, or a PR merge are independent mathematical verification. | They are provenance and workflow facts. Each primitive, proof, arithmetic contract and quantifier needs review at an exact source. |

No numerical result has been retroactively called a proof-assistant certificate.
The new replay ledger distinguishes EXACT_RATIONAL, DIRECTED_INTERVAL,
NON_DIRECTED_HIGH_PRECISION and FLOATING_RECONNAISSANCE explicitly.
