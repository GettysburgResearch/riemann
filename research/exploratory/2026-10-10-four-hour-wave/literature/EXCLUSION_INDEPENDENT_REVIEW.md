# Independent exclusion-pair and marked-moment audit

Read-only review by `kappa_proof_audit`, 2026-10-10. Base:
`/workspace/riemann/research/exploratory/2026-10-10-four-hour-wave/arithmetic`.
No Git or checkout mutation. All new outputs are in `/tmp`.

## Analytic and implementation finding

Scoped PASS for E1–E10 and S-E1–S-E2, subject to their stated finite
guards and the already independently reviewed larger-power input A-WM1.
The resulting sufficient threshold is every real m>=13/10 and every
real x>=1. The exact beta projection and SHARP kernel are preserved.
No critical-power or RH conclusion is justified. No gap found.

1. Literal marked source: E1/E2 sum over label indices. Two copies of 67
   give projected coefficients mu(l), -2mu(l), mu(l), 0 at powers
   67^0,67^1,67^2,67^j (j>=3), exactly the native beta. A subset containing
   both 67 labels marks their weight twice. V=P(a)+67^-a is the complete
   convergent static source because a=(m+1)/2>1.

2. Excluded-label removal: the active kernel ratio T(y/q)/T(y) is at
   most q^-1/2, including its activation boundary. For an inactive parent
   every superset is inactive. E3 follows after the positive m-th power
   and q^-1/2 coefficient. Counting the k+1 removals of every extension
   and retaining the exact unused-label sum gives

       (k+1) S_(k+1) <= V S_k - D_k.

   This handles all duplicate labels and empty levels. There are no
   conditional-series rearrangements. When V<3, every even/odd pair
   beginning at k>=2 is nonnegative with lower bound
   (1-V/(k+1)) S_k + D_k/(k+1). Selecting the positive pairs at 2,4,6
   and discarding the other nonnegative pairs proves E6. Any selected
   positive subset masses give valid further lower bounds.

3. Exact marked prefix engine: `exclusion_moments.py` 25–34 imports the
   independently audited ordinary source unchanged and builds the marked
   final-label prefix at q^(-2a+j/2). Lines 36–74 enumerate levels 2,4,6
   by increasing label indices and exact integer quotient floors. At the
   final label, lines 51–57 use exactly

       n^(-a+j/2) [used_sum * sum q^(-a+j/2)
                                + sum q^(-2a+j/2)].

   The used_sum is updated by q^-a, so it marks every chosen index
   exactly once, including equal-valued 67 indices. Minimum-consecutive-
   product pruning removes no active branch. Every constituent of a
   selected product at a level>=2 is at most N/2. Ordinary and marked
   vector metadata agree and are bound to the normalization exponent,
   level and active cutoff.

4. Uniform bounds: the marked static sum is positive and decreases with
   m; the normalized kernel term decreases with m and increases with x,
   including its positive activation jump. Thus both ordinary and marked
   selected masses have E9's directions. The fixed-power positive
   binomial enclosures apply to the marked moments termwise. A global
   directed V upper bound at m0 gives positive coefficients throughout
   the slab; the even and marked lower masses at (m1,L) then bound the
   whole real rectangle.

5. Whole-tail substitutions: `exclusion_tail.py` 9–46 binds the common
   selected caps and marked metadata, requires V<3, a positive omitted
   one-label mass and c0>0, and applies the previously audited exact
   rational activation-polynomial positivity guards. In the first bound,
   replace the negative odd denominator by its positive LOWER polynomial
   d_l and the positive even denominator by its UPPER polynomial d_h^+.
   The collected positive selected polynomial is nonnegative on the
   actual domain. After multiplying by d_l d_h^+, replace only the
   positive constant term c0 d_l d_h^+ by c0 d_l d_h. This gives exactly
   E10 with the correct lower direction. No infinite three/five-label
   negative majorant is assumed or omitted from an unproved formula.

6. Exact tail cover: `exclusion_tail.py` 49–81 rounds the directed upper
   coordinate cap outward onto a 40-bit dyadic grid, so every midpoint
   through the allowed depth fourteen is exact at 192 bits. Every
   accepted leaf requires every entire Bernstein coefficient ball to be
   strictly positive; unresolved leaves either split into both exact
   halves or fail explicitly. This certifies the continuous domain,
   including z=0 and hence the infinite endpoint limit. Positivity of the
   collected polynomial on the slightly enlarged cap needs no analytic
   kernel inequality beyond the actual required domain.

7. Complete bounded comparison: `verify_exclusion_stitch.py` 33–63
   computes the complete finite one/triple upper levels and even/marked
   lower levels. The one-label omission after B is paid by its full Euler
   remainder. The triples are complete through each bounded endpoint;
   there is no omitted negative triple at those endpoints. Lines 66–98
   form both the valid exclusion bound and the previously audited F1
   bound. Selecting either valid lower-bound ball is safe even when an
   interval comparison is inconclusive; the selected entire ball must be
   strictly positive. O1<=V<3 ensures its F1 coefficient is positive.

8. Real coverage and modes: lines 101–134 explicitly check the closed
   ordered chains. Ten slabs and 21 endpoint intervals give 210 bounded
   rectangles; ten E10 tails cover all x>=N. Together with the closed
   overlap at m=1.32 from A-WM1, every real m>=1.3 and x>=1 is covered.
   The reconnaissance-only switch has a separate status and no global
   threshold; the independent runs here use the complete default mode.
   Acceptance uses require/strict directed comparisons, with no Python
   assert or floating acceptance condition removed by optimization.

## Finite independent controls and receipts

All four supplied control groups passed in normal and optimized Python,
with no failures, errors or skips. They include direct marked/ordinary
subset sums through 40000, nonempty level six, the exact finite
used-label identity, duplicate-67 controls, kernel removal, actual dyadic
subdivision and explicit rejection guards. Outputs:

- `/tmp/review-exclusion-tests-normal.txt`
- `/tmp/review-exclusion-tests-optimized.txt`

The independent Horner/degree-elevation Bernstein oracle checks the
retained coefficient balls without using the production shift/binomial
conversion to establish positivity. All 130 coefficient balls over the
ten whole-tail intervals are positive; exact dyadic endpoint checks prove
each tail's complete contiguous cover. It also confirms all 210 retained
bounded margins are strictly positive. Output:
`/tmp/review-exclusion-bernstein.json`; script:
`/tmp/review_exclusion_bernstein.py`.

Both complete independent normal and optimized replays passed all ten
slabs, matching each other and the retained normal receipt byte-for-byte,
SHA256
`fbe84f776aef421655f2b4575391357ab89fbe107b4d3aa6b2705df6386a90b1`.
Outputs: `/tmp/review-exclusion-stitch-normal.json` and
`/tmp/review-exclusion-stitch-optimized.json`.

The independent smallest-prime-factor census through N=10000000
classifies every integer separately from the prefix recursion. Ordinary
prime factors must have exponent one; 67 can have exponent one with
label multiplicity two or exponent two with multiplicity one. It finds
complete labelled counts 1917661, 1133924 and 33975 for levels 2,4,6,
exactly matching the engine. At exponent zero the marked census also
equals k times the ordinary count, exactly.

Direct factorization gives independent ordinary and marked weighted sums
at exponents 1.15 and 1.16, all seven orders, through 100000 for levels
2,4 and through 1000000 for level 6: all 84 directed comparisons pass.
Every tested level includes a 67-square source term; the level-six
example is 942690=67^2*2*3*5*7 and its mark includes both 67 weights.
Output: `/tmp/review-exclusion-oracle.json`; script:
`/tmp/review_exclusion_oracle.py`.

Final scoped conclusion: PASS for the complete all-real sufficient-power
theorem m>=13/10 with the stated imported A-WM1 larger-power input.
Finite execution and the analytic argument were independently reviewed.

## Frozen implementation reviewed

    EXCLUSION_PAIRS.md c445e969d6998ce7bf0667f52ebfbdf20c693cfa7c54e5798824af483d8f398a
    EXCLUSION_STITCH.md cd4de9aeeea185a2a74927360fb8396e6113e164cdb7ebe541c4c6a68acfd20b
    exclusion_moments.py 8ac22c96b7ac1edf03defc9e099fdefe2c17907f21f3c24f3fbd180a2824dc1c
    exclusion_tail.py 79c8a5667fe2156fa593725ba012eda3e6635ec49898e80b82d8d7732442635c
    verify_exclusion_stitch.py 393adee89aa073024f7093b4f0dc415abdd8c4cdb5e7e7d761a9e3646ac04b79
    test_exclusion_moments.py 735784552db0fe56e9fbfcbf3e7abb708ce72403b9c15aed34ead104358156d0

The reviewed stitch manuscript was updated to record complete normal/
optimized execution during the audit; the earlier pending-status hash
was 7573ba67a679b35f6277fd493eb736e6e7236c227e8417179714659c2a42883d.
The mathematical coverage and all implementation files remained frozen.
