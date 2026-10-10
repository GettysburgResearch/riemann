# Independent weighted-moment stitch audit

Read-only review, 2026-10-10, by `kappa_proof_audit`. Checkout base:
`/workspace/riemann/research/exploratory/2026-10-10-four-hour-wave/arithmetic`.
No Git or checkout mutation. All new outputs are in `/tmp`.

## Analytic conclusion

Scoped PASS for W1–W8 and S-W1–S-W3. Subject to the stated directed finite
guards and the separately reviewed A-FL1 input at m>=7/5, the packet proves
H_m(x)>0 for every real x>=1 and every real m>=33/25. It preserves the
literal beta source, the SHARP boundary kernel and two distinct labels at
67. It does not prove the critical power or RH. No mathematical gap found.

1. Exact source transport: from T(y)=(4 sqrt(y)-3) 1_{y>=1}, the active
   normalized term is

       r_n(m,x) = n^(-(m+1)/2)
                  (1-3 sqrt(n)/(4 sqrt(x)))^m
                  /(1-3/(4 sqrt(x)))^m.

   Thus the seven finite weighted moments have exactly the stated
   exponents. The positive activation jump at x=n is retained. The
   normalized term is nondecreasing in x and nonincreasing in m. The
   removal inequality and four-label remainder are the previously
   independently reviewed T2/F1, with coefficient 1-R/5>=0 whenever R<5.

2. Complete prefix sums: `weighted_moments.py` 38–61 sieves all ordinary
   primes through floor(N/2), adds the second 67 label, and forms directed
   prefixes at every moment order. Lines 63–94 use exact integer quotient
   floors and strictly increasing label indices. For any level>=2 product
   <=N, every constituent label is <=N/2. The one-label completeness cap
   is explicitly checked at line 66. The minimum-product pruning at
   82–90 cannot discard an admissible later choice. Duplicate-valued
   indices remain distinct.

3. Binomial enclosure: for 1<m<2, coefficients b_j, j>=2, are positive
   and decreasing; the recurrence at 97–106 is exact rational. The
   remainder after degree five is between zero and b6 v6/(1-v), hence
   between zero and 4 b6 v6 for 0<=v<=3/4. Differentiating the convergent
   tail shows that p_m is decreasing. The exact rational guard
   p_m(3/4)>0 in `polynomial_tail.py` 43–47 therefore proves positivity of
   every selected lower kernel and every denominator lower polynomial
   on its analytic domain. The finite normalization routine 109–127
   correctly binds exponent and active cutoff metadata and divides by
   the positive exact denominator.

4. Odd tails and all later levels: `verify_four_label.py` 62–77 uses the
   convergent prime-zeta Möbius series plus the full omitted tail P10 and
   the exact Newton e3 identity, with the extra 67 term in every power
   sum. These helpers have already passed an independent source audit.
   Every omitted odd product is bounded by n^(-(m0+1)/2); when the finite
   source is complete through the endpoint, omitted products are
   inactive. All omitted even products can be discarded in a lower
   bound. V bounds the actual removal mass for every later endpoint and
   power in the slab. The finite level pairing applies to the complete
   active source at each real endpoint.

5. Whole-tail numerator: `polynomial_tail.py` 57–90 sets exact directed
   upper tails, V<5, c0>0 and c4>0. The selected Q1+Q3 and P2+c4 P4 are
   positive on the actual tail domain. After multiplying by the positive
   exact denominators, substituting lower denominators into the positive
   terms and an upper denominator into the negative term has precisely
   the W7 direction. Arb coefficient collection encloses the exact
   collected polynomial, including all cancellations. Its degree is at
   most twelve. No separate unsigned defect bound replaces that
   collection.

6. Bernstein coverage: `polynomial_tail.py` 93–103 gives the correct
   affine power shift and power-to-Bernstein conversion. Lines 106–136
   construct an exact directed cap containing N^(-1/2), then certify all
   coefficient balls strictly positive on every leaf. Exact midpoint
   subdivision preserves both halves; the limits fail explicitly rather
   than accepting an unresolved leaf. Positivity on the slightly enlarged
   coordinate interval suffices, even though analytic kernel bounds are
   only needed on the original interval. For the current packet every
   tail is already certified on the unsubdivided cap, including z=0.

7. Bounded real rectangles: `verify_weighted_stitch.py` 49–82 correctly
   caps the finite one-label source at B and adds the positive complete
   Euler remainder when x>B; other selected levels are complete through
   N. Taking the smaller of two valid upper bounds and the maximum of a
   valid lower bound with zero is legitimate. Lines 85–114 use negative
   odd upper values at (m0,U), positive even lower values at (m1,L), and
   the positive coefficient 1-O1/5. Lines 117–132 explicitly check closed
   coverage and strict ordering. The 15 power slabs and 21 endpoint
   intervals cover all real m in [1.32,1.4] and x in [1,N], while W7/W8
   cover [N,infinity). A-FL1 supplies the closed overlap and all m>=1.4.

## Independent finite controls

The supplied four control groups passed normal and optimized Python,
with no failures, errors or skips. Outputs:

- `/tmp/review-weighted-tests-normal.txt`
- `/tmp/review-weighted-tests-optimized.txt`

An independent smallest-prime-factor census classifies every integer
n<=10^7 directly: all ordinary prime exponents must be one, except that
67 may have exponent two; one factor 67 has multiplicity two. It finds
and exactly matches the prefix engine's complete counts:

    level 1 through B: 348514
    level 2 through N: 1917661
    level 3 through N: 2120893
    level 4 through N: 1133924

The same integer factorization gives an independent direct moment sum
through 100000 (50000 for level one), at exponents 1.15, 1.16 and 1.2,
all seven orders and all four levels: 84 directed comparisons passed.
The 67-square products at levels two, three and four are included.
Output: `/tmp/review-weighted-oracle.json`; script:
`/tmp/review_weighted_oracle.py`.

An independent Bernstein oracle uses Horner multiplication by the
linear Bernstein polynomial [L,U] and exact degree elevation, rather
than the production power-shift/binomial conversion. All 195 coefficient
balls over the 15 current full tail intervals are positive and agree
with the production conversion. The original exact cap is reconstructed
at 192 bits; displayed JSON ball strings are not treated as exact
endpoints. Output: `/tmp/review-weighted-bernstein.json`; script:
`/tmp/review_weighted_bernstein.py`.

The retained certificate has 315 positive bounded margins and 15
positive whole-tail leaves. Approximate smallest margins (for display
only) are 0.0577659539000804 bounded and 0.000213463658318283 tail.

## Frozen implementation reviewed

    WEIGHTED_MOMENTS.md c23046fdf7379d392afb4b8d3d6bfa029af0cbaf67fac4f0d7ebc47a4457726d
    WEIGHTED_STITCH.md bacce63e9ca8ab47abba991585465d5d1c6ba274294ec3426dd8aef75f7a8240
    weighted_moments.py 715dae97b834735064aae0a9951c505750697ec003aacaafffa17c5975621677
    polynomial_tail.py ae8ec2f91e8f00d286a7e8176d1f47bbe56a5013f22357d6dab52fa8ffb5e295
    verify_weighted_stitch.py 14355093aed45e9a4378dc6a405ec251ea9c699c808cca4473983563776c85ab
    test_weighted_moments.py 371ce71e17961aeb6e86f85a19097e6cabe7c5d13bd5316452270142e1f91c5c

Independent complete normal and optimized Python replays both passed.
Their 315 bounded rectangle certificates and 15 whole-tail certificates
are byte-identical to each other and to both retained source receipts:

    SHA256 1f8172742b9af4999f358b647f52b30ca81560af93278ff087d28e2c2c74e9f5

Outputs:

- `/tmp/review-weighted-stitch-normal.json`
- `/tmp/review-weighted-stitch-optimized.json`

Final scoped conclusion: PASS for the stated all-real sufficient-power
theorem m>=33/25, with the explicitly imported A-FL1 larger-power input.
Finite execution is separate from the analytic source argument, both of
which were independently reviewed here. Critical positivity remains open.
