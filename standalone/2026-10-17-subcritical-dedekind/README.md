# A subcritical-scale route to a proposed 91/100 Dedekind boundary

**Proposed unconditional source composition; independent mathematical review required.** No accepted theorem, Lean verification, full RH proof, or critical native covariance bound is announced. The main new lemma and its full analytic composition are in PROOF.md.

The proposed conclusion is nonvanishing of every Dedekind zeta function for Re(s)>91/100, away from the pole at one, and the corresponding finite-order Hecke result. It improves #959's proposed 11/12 boundary by 1/150. The excluded width increases from 1/12 to 9/100, or 8%. It does not improve the earlier reported 7/8 special-setting bound.

## What actually changes

The previous positive 1/12 ceiling was proved in the support regime XY=Z^M with M>1. The original average and unrestricted reflected expression are defined more generally. Reconstructing the quadratic-sieve estimate before the supercritical simplification gives

    sum_physical |B_m(Z)|^2 << Z^eta (XY+(XY)^2/Z).

Both terms matter. In particular, using only (XY)^2/Z when XY<Z is wrong. The new proof retains the full cube variable, local powerful factors, all small-effective-length tails, fixed S-classes and original nonunit zeros.

Choose X=Y=Z^(23/50), so M=23/25<1. The COMPLETE theta/additive pairing is then O(Z^(23/100+eta)). Rebuild the Poisson comparison using twenty-two disjoint classes, applying BGL's mean to the good class and five middle classes, and convexity to the others. All principal, small-frequency, horizontal and large-frequency terms are included.

The principal xi line stays to the right of one. Unlike the old-scale escape in #961, no known global zero-free theorem is needed to shift it. The detector's true Mellin shift is 17/25. Hence growth 23/100+4e gives the strict proposed boundary 17/25+23/100=91/100, by choosing a fixed positive e for each point.

This BYPASSES #961's OPEN-L by changing the scales. It does not prove OPEN-L at the old scales. It is not just another conditional criterion or an extrapolation of the M>1 corollary into an inadmissible range.

## Read and reproduce

Read PROOF.md Sections 2 and 3 first, then the complete comparison in Sections 4--5. SOURCES.md distinguishes imported theorems from this derivation. VALIDATION.md records the finite/analytic boundary.

    python verify.py
    python -O verify.py
    python verify.py --details
    python run_mutations.py
    python verify_manifest.py

The checker uses exact rational arithmetic. It verifies 1,394 finite predicates, including all density monomials, every contour vertex and the complete e-interval budgets. Seven corrupted models fail. These facts do not certify the analytic theorem.

## Publication base and prior work

This is an additive continuation of #961 at 7bd275b44261fff93bb565a9342c44b7c66526f6. Its thirteen-file packet was reconstructed from the delivered archive, matched to the live Git tree 916580e58acc72b87df6931b4e688543501c95ab, and replayed in ordinary and optimized Python. It was already pushed; no duplicate recovery or historical-status rewrite is made.

No inherited file, main, or integrated scientific-status record is changed. The same author wrote the proof and checker. No external human referee, separately commissioned reviewer, new Lean build, upstream metaplectic reconstruction, full-repository validation or remote CI is claimed. No exhaustive literature-priority claim is made.
