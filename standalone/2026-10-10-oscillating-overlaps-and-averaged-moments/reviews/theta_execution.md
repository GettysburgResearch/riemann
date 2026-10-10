# Exact arithmetic execution record for the factorwise theta note

This records the author's execution of the companion finite checker. It is not an independent replay of the theta automorphy theorem or of an infinite moment estimate.

## Frozen identities

| File | SHA256 |
|---|---|
| attack2_theta.md | f4854894c797f9b9f92b6d52a24b61caa941e3aff2b15c4c5a460db8fff469ff |
| attack2_theta_verify.py | aabf77a3f75f4a0ce7dc6af5784e2dda93804fa8089f02147d21344388d2c7f5 |
| attack2_theta_results.json | 3b0d17f7f6dd369668559c179e26babf6642a5b8b316cfc1a16ade2243edd619 |
| Canonical pinned October 5 paper2.tex | d9a8f15aa770cf883d0eabd2b775fad694ce20b44cba7928f5c0c9a6d8750d4d |

The paper is the source at OpenAI/math commit adc7f1241b42e322a6451854ab7e4b4c146bf78a named in the note.

The canonical imported source has 169,005 bytes and Git blob identity 2000faddbbebac5de0ecfe0b962534ea61a852d5. The scratch reading copy theta_paper2.tex had 169,006 bytes and SHA256 80c322411ede981efb250f2b5631622f43f8e896ed9542a33cd057d8a6c922d4. A direct byte comparison established exactly that the scratch copy equals the canonical bytes followed by one extra newline. The canonical hash above is the source identity for this record; the scratch hash is retained only to explain the reading-copy provenance. No mathematical content differs.

## Actual run

The command was:

    python -O /workspace/scratch/5b23d9b20a3a/attack2_theta_verify.py --output /workspace/scratch/5b23d9b20a3a/attack2_theta_results.json

The runtime reported Python 3.12.14. Execution exited with code zero and reported PASS for 2,122 explicit predicates. The checks use explicit exceptions and therefore remain active under Python's optimization flag. The JSON output records the checker source hash.

## What the primitive finite checks cover

The prime ideals have primary generators -2-3 omega and 1-3 omega, of norms 7 and 13. Their residue fields identify omega with 4 modulo 7 and 9 modulo 13. The physical sixth root is 1+omega, and the sextic residue character is computed by raising each residue to (q-1)/6 and identifying the resulting sixth root in that embedding.

For a primary denominator a+b omega of norm q, the source's additive character on an integer representative t is exactly exp(2 pi i (-b)t/q). Integer representatives form the complete residue system in both split prime fields and their coprime product of norm 91. This fixes the Gauss-sum normalization used by the checker rather than replacing it by an unspecified additive phase.

All Gauss sums are computed as integer coefficient vectors in Z[X]/Phi_(6q)(X). The three tested cyclotomic fields have orders 42, 78, and 546 and degrees 12, 24, and 144. There are no floating-point calculations. The unnormalized products G_2(a)G_4(a) are exactly 7, 13, and 91; division by the two square-root normalizers therefore gives gamma_2(a)gamma_4(a)=1 in each case.

The CRT check independently compares the direct norm-91 Gauss sum with the product of the two prime Gauss sums and the actual reciprocity cross phase. That cross phase is zeta_6^4, so a mutation omitting the phase is detected.

Further complete checks cover:

- All six local exponents, every nonzero denominator quotient, and every nonzero outer residue in both prime fields: 1,080 checks of the scalar character scaling in Lemma 2.1. The c-independent normalized Gauss factors cancel in this ratio; their relevant conjugate product is checked separately as above.
- Every row valuation from 1 through 18, including both active and inactive choices for positive multiples of six: 420 checks of the final quadratic charge with its nonunit zeros.
- Every pair of divisor and residual residues in both prime fields: 218 checks that removing a quadratic square factor retains its exact coprimality mask.
- Complete additive Ramanujan sums at every residue modulo the ideals of norms 7, 13, and 91: 111 comparisons with the independently assembled Mobius divisor formula. Their means are exactly zero, and their squared totals are respectively 42, 156, and 6,552, equal to N(a) phi_K(a).
- The local reciprocal-Euler correction through degree 12 for every sextic value, including the zero value: 260 coefficient checks.

Native ideal identities, Gauss products, energy equalities, and explicit rejection of dropped CRT phases, a spurious Mobius sign, and dropped sixth-power zero masks account for the remaining predicates.

## Acceptance and limitations

Acceptance requires every exact predicate to hold; any failed identity raises an exception and prevents the PASS JSON from being written. The output does not infer correctness from a pre-existing result file.

The finite arithmetic is useful evidence that the exact formulas preserve their normalizers and masks. It proves no infinite theorem by sampling. The analytic arguments in attack2_theta.md depend on the named source theta-reflection formula and quadratic large sieve, plus the proofs written in that note. No computation here checks the source's automorphy, archimedean contour shifts, cusp coefficient bounds, angular Hecke L-function zeros, or a coupled short-row mean square.
