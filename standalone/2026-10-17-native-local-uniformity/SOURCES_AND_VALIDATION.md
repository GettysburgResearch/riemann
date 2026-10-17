# Sources, exact scope, and validation

## Imported cancellation theorem

K. Matomaki, M. Radziwill, X. Shao, T. Tao, J. Teravainen, *Higher uniformity of arithmetic functions in short intervals II. Almost all intervals*, Inventiones mathematicae 244 (2026), 967--1091. Published 26 January 2026.

- DOI: https://doi.org/10.1007/s00222-026-01408-6
- Publisher HTML: https://link.springer.com/article/10.1007/s00222-026-01408-6
- Published PDF: https://link.springer.com/content/pdf/10.1007/s00222-026-01408-6.pdf
- Author version: https://arxiv.org/abs/2411.05770v2

The load-bearing input is **Theorem 1.1(i)** and the definition (1.4) of the starred sum. The publisher's rendered PDF page 970 and the corresponding HTML were inspected. The input allows the supremum over polynomial nilsequences and all finite arithmetic progressions INSIDE the exceptional-set statement. We specialize to circle polynomial phases with fixed degree/complexity and derive the integrated square estimate using the boundedness of mu. Fixed Dirichlet twists are handled by residue splitting. Corollary 1.2 alone would not supply the full progression maximum used here.

The theorem requires H>=X^(1/3+epsilon) and H<=X^(1-epsilon). We do not use the qualitative shorter-H alternative to claim arbitrary logarithmic savings there. The nilsequence proof was not reconstructed, and no claim of formal verification or an upstream build is made. The result is imported as a published unconditional theorem, not as an RH hypothesis.

## Repository provenance and limits

- #960, `c127f4f22d08585b699ccd59faa4eedd9bb001ae`, `standalone/2026-10-17-growing-shift-maximal/THEOREMS.md`: rational-integer source, exact convolution/tail methods, mixed Fourier identity, and heavy/light endpoint partition. The full delivered proof was read. Its explicit failure to cover unbounded Eisenstein norm-prime values is the arithmetic interface addressed here. Its smaller-H quantitative theorem is not superseded in every range.
- #951, `aba76e1df38dc438b9f5c5f20b698fb26fb1716e`: the same algebraic local completions and shorter-scale warnings, already resident in the conversation's source extracts. The local kernel bounds needed here are proved anew in PROOF.md; no inherited theorem is silently strengthened.
- #952, `3b7d2948840446c752bbf284f6f90f6592395a29`: literal Gaussian pair kernel and energy normalization. The kernel is explicitly written in Section 6. Only its elementary smoothness on a fixed shell is used for the new correlation corollary.
- #961, `7bd275b44261fff93bb565a9342c44b7c66526f6`: THETA_ESCAPE.md was fetched and read live. The proposed low-powerful-row theta inequality OPEN-L is NOT an input or conclusion here. #959's proposed all-field 11/12 theorem is not re-certified by this packet.

Classical quadratic-field splitting, Dirichlet convolution, hyperbola grouping, divisor bounds, Euler majorants, Minkowski, and Fourier orthogonality are credited as methods. The contribution claimed is the displayed source-specific capped-tensor and completion adapter, not global literature priority for these techniques. No exhaustive literature priority review has been performed.

## What was actually run

The standard-library checker uses integers and Fraction arithmetic. Normal and optimized Python reproduce RESULTS.json byte-for-byte.

1. Twenty-four complete supported-ideal censuses through norm 4096 cover four families, m=2,3,6, and two phase/exclusion profiles. Two additional censuses, native and coupled m=6, cover every allowed ideal through norm 131072. The larger coupled census has 37001 supported ideals; both conjugates at norm 7^6=117649 remain.
2. The independent aggregation mechanisms are a rational-prime Euler recurrence and increasing-prime-ideal enumeration with separately written local coefficient formulas. They share the elementary rational-prime sieve, splitting rule, and declared profiles. This is NOT independent mathematical review or two independent number-field libraries.
3. The full unmasked native norm coefficient agrees with `mu*(mu chi_-3)` at every integer norm through 20000, including ramified and inert factors. A single split ideal may be excluded in the other fixtures; its conjugate is not erased with it.
4. There are 108 exact local series identities through degree 36, 858 progression-preimage cases, twelve capped-tensor ownership configurations, 128 exact endpoint-exponent identities, and 800 dilation-overlap identities. The 38084 integer-fixture guards are repeated arithmetic setup, not independent analytic cases.
5. Odd-m ideal fixtures use b_p attenuated by q^(-1/2) so their coefficients are rational. Local critical-mass tests at square/fourth-power q are algebra fixtures, not assertions that those q enumerate prime ideals. Complex arbitrary-profile validity rests on the written absolute-majorant proof, not the rational fixtures alone.
6. Six actual separate `python -O check.py --mutate NAME` processes were executed and rejected: omit a conjugate, wrong powerful weight, erase an exclusion, duplicate largest-factor ownership, lose the congruence gcd, and use the wrong dilation Jacobian. MUTATIONS.json records their intended rejection predicates.

A fresh ZIP extraction is replayed before delivery. No numerical scan of cancellation, actual polynomial-phase supremum computation, interval certificate, full-repository validator, remote CI result, Lean build, or independent referee report is claimed.

## Review priorities

First check MRSTT's exact starred-supremum scope and (12)--(14), including the 1/a root weight and unique tie-breaking. Next check the complete norm-fiber identity with asymmetric exclusions, the uniform (18)--(24) kernel split, and the left-continuous BV endpoint convention. Finally check (28)--(30), including the light-bin and heavy-atom contributions. No constant is uniform in growing k, polynomial degree, logarithmic-saving exponent, conductor, or exclusion set. The polynomial lower bound on H is essential.
