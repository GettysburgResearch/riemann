# A quantitative change of target: multiple off-critical zeros

**Proposed complete deduction; independent mathematical review required. RH is not proved.**

This replaces the bounded-smoothing / asymptotic-companion programme with a
specific zero-count improvement. The main result in `PROOF.md` is

    liminf N_{simple OR central}(T)/N(T)
       >= 0.888059653174364568859397107720... .

The compared Lamzouri-v2 constant is 0.887620008173354339866075859447... .
All counts use the paper's multiplicity conventions. This is NOT an 88.8%
critical-line theorem. It bounds the complementary mass of multiple off-line
zeros and says nothing that excludes simple off-line zeros or a sparse
exceptional set.

A second proposed conclusion improves the average of the simple-zero and
central-zero proportions to 0.8365229206385391165... . No assertion is made
that each proportion individually exceeds this number.

## What supplies the gain

Keep a free threshold h in the existing stability-enhanced rank argument,
retain the extra positive-index saving B/4 from multiple nonreal pairs,
and use the certified seven-point pressure to pay the resulting Gram defect.
The choice h=2+sqrt(255031/128000), block size 1536, cancels the unknown
central-zero count. The analytic passage uses Lamzouri's exact removal of
the pair weight and the published unconditional BGST theorem, with the
smooth-cutoff limit taken AFTER the height limit.

The seven-point continuum premise is imported from the already reviewed
main-branch supplement; it was NOT rerun. No new RH-strength upper estimate
is a hypothesis. The proof, however, is not independently reviewed or formalized.
An optional 0.888307171066... corollary additionally imports a newer external
nine-point/window certificate; it is NOT part of the independently reconstructed
input boundary used for the main numerical statement.

## Read and check

Read `PROOF.md`, especially (6), (9)-(10), (14), (17), and (20)-(24).
Exact source SHAs and the literature comparison are in its Section 8.

    python -I -S -B verify.py --check results.json
    python -I -S -B -O verify.py --check results.json

Both modes were executed successfully. They reconstruct the same 7,343 bounded
controls and exact outward constant enclosures. The scalar and matrix cases
are tests of the new finite algebra, not zeta computations or a machine proof
of the infinite argument. The arithmetic uses Fractions, integer square roots,
and alternating-series remainders. No floating-point value enters acceptance.

The current standard-library code is one implementation. A receipt with an
altered numerical bound and a receipt with an altered RH status were also
rejected by actual CLI reconstruction in both modes; duplicate-key input was
rejected. Clean ZIP extraction was replayed in both modes. These are delivery
checks, not independent analytic acceptance. No full-repository validation,
Lean build, new zero census, or fresh seven-/nine-point continuum search ran.

## Reassessment and attribution

The previous HBR30 work is at PR #883, head
`b0b64fd71f9dbefea4315a1fe145c70386ad7a1d`. Its finite-parameter positivity
and synthetic off-line countermodels do not supply a new exclusion theorem.
This packet neither modifies nor uses that proof.

The initial boundary-count refinement considered during this pass was found
already in tawanerguo-cn/trmdy work and was NOT counted as a discovery.
The existing external .673316977 simple-AND-central candidate is a different
statistic, not a smaller number beaten by the OR bound. No accepted world
record or exhaustive originality audit is claimed. The proposed contribution
is the explicit multiplicity-sensitive composition and its improved bounds.

Publication is add-only, on a separate branch from main
`f99d9e3908dde4865377c75d9ca051c1f545bf4f`. Existing research, reviews,
canonical claims, workflows and formal files are not modified.
