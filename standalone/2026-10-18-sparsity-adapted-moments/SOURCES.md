# Sources, comparison scope, and dependencies

## Primary analytical inputs actually inspected

1. Alexandre de Faveri, *Optimal large sieve for fixed order characters*, arXiv:2610.04045v1 (2 October 2026). Primary parsed full text: https://arxiv.org/abs/2610.04045 . Relevant locations: Section 1.1, definitions of Theta_n and flat sums, Theorem 1.1, Section 2 character conventions, and the Corollary 1.5 zero detector. Both indices of Theta_n are n-th-power-free, not merely squarefree. The four-term bracket is displayed in equation (1.8) and the upper theorem is stated for the stronger kernel. Some isolated display equations are missing in the text parser; the exact bracket is also pinned in the repository source contracts. The input is adopted as the source's unconditional theorem, not independently rebuilt. An initial direct URL fetch failed; opening the already indexed primary record succeeded and its body was inspected. No PDF/source bytes or unverifiable manuscript hashes are vendored.

2. Valentin Blomer, Leo Goldmakher and Benoit Louvel, *L-functions with n-th-order twists*, arXiv:1112.1650, https://arxiv.org/pdf/1112.1650 . The primary PDF was read, with printed pages 18-19 rendered as images. Section 5 supplies the classical AFE/Mellin separation and the zero-detection mechanism (5.3). Its printed detector is at real part 1/2 and originally uses squarefree rows. Our changed line, complete power-free column adapter, selected row count, maxima and small-height multiplicity extension are proved in this packet; they are not falsely quoted as BGL's literal theorem.

3. Standard Hecke functional equations, the complete approximate functional equation for a fixed power L(s)^r, fixed-field ideal counting, divisor bounds, polynomial conductor/height bounds, and Jensen's theorem. Their uses and normalizations are written in the proofs. No statement about the location of nontrivial zeros is assumed. Fixed Euler omissions lie on Re s=0 and remain outside the domains used here.

No CT theta estimate, proposed quasi-RH result, unproved native moment, inverse-L moment, scattering projection, or signed covariance hypothesis enters the proofs. An error in the imported sieve or the AFE/family adapter would invalidate the deductions regardless of finite checks.

## Repository comparisons and overlapping work

- #968, 14f544fb4293ffb59942ff8d345ab9d6da67025c: central fixed-order numerator moments and the complete sixth-power/mask adapter. These are credited, not rediscovered.
- #969, 6542781188469e8a23dadf9d419b3d5cf4d11de7: off-central fourth moment at 7/12 and the actual conductor split. Its sextic full-family U bound is used as a cross-check, with a direct general-order argument supplied here.
- #971, 3f1d2a07631eb6cca1f2716be01f64e874667639: SHIFTED_DETECTOR.md was read in full, including its 395/552 bound and all-row mollifier norm. Our strict change is selected-cardinality control of that norm. We do not import the ramified correction or a CT composition.
- #975, edbc27b61208ccc7ee1fa99fa3f4e861f5a03452: publication base only. Its resonant factorization supplies no estimate used here. #974 independently overlaps that resonance; no uniqueness of the old result is claimed.
- Concurrent #976, bf845aa1d9d06b0ce62440edc5726de997a888db: NUMERATOR_HIERARCHY.md was freshly read. Its full-strip sextic hierarchy, eighth-moment anchor, finite-generation observation and actual-conductor AFE overlap the nu=1 specialization. Our sparse numerical example is explicitly not advertised as beating its eighth-moment consequence. Its theta theorem and native target were inspected at PR-description scope only and are not inputs.
- #977's reflected-ratio checkpoint and #978's recovered 19/21 proposal were seen at PR-description scope. They are different source operations, not claimed inputs or independently reviewed compositions.

The comparisons are to these exact inspected statements. GitHub text search is not an exhaustive bibliography. No worldwide literature-priority or optimality claim is made. Classical trivial/sieve interpolation, Holder, Mellin zero detection and AFE methods are credited.
