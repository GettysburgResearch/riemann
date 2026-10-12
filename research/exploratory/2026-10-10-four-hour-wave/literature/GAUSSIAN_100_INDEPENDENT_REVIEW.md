# Independent audit: native Taylor-bound Gaussian100 packet

Reviewer: kappa_proof_audit, read-only checkout/Git. Date: 2026-10-10.
Verdict: scoped PASS for the displayed finite-domain theorem, subject to
its explicitly imported analytic, complete-count and directed-backend
contracts. No substantive proof, source-binding or coverage gap found.

Claim audited: for actual Xi(z)=xi(1/2+i z), r=0, lambda=10, the entire
closed rectangle z=T-i y, |T|<=100, 0<=y<=1/2 has nonzero companion and
companion derivative and Re(i E/E')>1/200000. This is a fixed compact claim.

## Exact finite far-product adapter

1. FINITE_PRODUCT_JET.md lines 8–49: for all retained real far roots
   gamma>D>B, the two logarithmic derivatives have the displayed
   geometric expansions. With S_k=sum gamma^(-2k), the coefficient
   inequality S_(j+1)<=S_1 D^(-2j) gives FJ3 and FJ4, including the
   (2K+1)/(1-q)+2q/(1-q)^2 derivative factor. The error is a complex
   disk; enclosing both components by the full epsilon radius is safe.
   No retained finite root is removed by this expansion.

2. Checker lines 121–142: the lower bracket endpoints give an exact
   disjoint cutoff partition at 256. Every root with lower endpoint
   greater than 256 is strictly outside that disk. All 7,938 such roots
   contribute to all 16 finite coefficient balls. The 111 remaining
   paired factors are handled individually. The B=101 disk contains
   the whole compact rectangle and is strictly below the far cutoff.
   Both finite remainder radii are directed upper rational bounds.

3. Checker lines 158–163: Horner indexes and factors (2k+1) agree with
   FJ2; the Gaussian contributions -2a z and -2a are subsequently added
   at lines 185–190. The finite-far remainder is included in the base
   ball before any sector margin is extracted.

4. FINITE_PRODUCT_JET.md lines 53–86 and checker lines 164–195:
   every selected local pair is multiplied by the full second-order
   product rule. Python's simultaneous tuple assignment uses all old
   product values. The formulas are exactly FJ6 and FJ7. The local
   factor is never divided by, so its genuine real zero is harmless.
   Every remaining low-factor denominator is explicitly guarded.
   Far factors are nonvanishing by their strict disk separation, and
   the Gaussian multiplier is never zero. The companion derivative
   divided by this nonvanishing bulk is also explicitly guarded.
   Strict positive real part of the enclosed quotient then guards the
   companion numerator as well.

## Native coefficient and complete-source binding

5. Checker lines 37–92 retain the source normalization, exact dyadic
   endpoints, 8,049 disjoint positive sign-crossing brackets below 8192,
   the nonzero endpoint, and the separately imported complete count.
   The Hardy reality is supplied by the actual completed functional
   equation; an imaginary ball containing zero is a consistency check,
   not a substitute for that analytic identity. Strict opposite real
   signs prove roots by continuity. Complete analytic multiplicity
   count equality makes every root simple and excludes any omitted
   nonreal root below the endpoint, within the library contract.

6. The complete count is precisely the qualified FLINT3.6.0 contract
   in NATIVE_SLAB_CERTIFICATE.md lines 81–102. Its historical finite
   Gram/Rosser input is imported, not independently rederived. This
   qualification is explicit in both the manuscript and receipt.

7. Checker lines 103–119 evaluate the actual native degree-two Taylor
   series via directed Gamma/zeta, guarding c0 and using its actual
   even-real normalization. Series coefficient [2] is c2, with no
   missing factor two. TB3 therefore binds a1=-c2/c0-sum gamma^-2.
   Subtracting the complete directed finite census encloses the full
   unknown tail coefficient, including possible nonreal tail blocks.
   Its real positive interval is enclosed in its entirety, rather than
   replaced by a fitted central value. Correlation with the root balls
   is conservatively forgotten; that only enlarges the family.

8. Checker lines 93–102 and GAUSSIAN_TAIL_TRANSPORT.md G1–G7 retain
   the complete unseen infinite tail. The coarse actual count and
   negative endpoint -8049/R^2 bound S. The exact quadratic coefficient
   is absorbed in exp(-a1 z^2), leaving the stated J1 and J2 bounds for
   the degree-four-and-higher residual. Nonreal tail zeros in the
   classical strip remain permitted. The finite geometric remainder
   and this infinite residual are separate, both retained budgets.

9. Checker lines 184–210 encloses all a in the full native real ball.
   For each box the extracted a=Re W lower and M=|W| upper give a/M as
   a valid uniform sector ratio. With alpha=10 J1 and
   beta=M[2J1+10(J1^2+J2)], the G14 and GS3 guards are exactly the
   order-zero complete multiplier transport predicates. The base's
   H/E disk bound extends to the real boundary by continuity. No
   higher-order Leibniz transport is claimed by this r=0 certificate.

## Exact adaptive coverage and receipt

10. Checker lines 224–252 starts with precisely the 400 by 4 closed
    coarse boxes, covering [0,100] by [0,1/2]. Every failure is replaced
    by all four exact children and returns only after all children
    have completed. Depth exhaustion raises an unconditional SystemExit;
    it remains active under python -O. Accepted boxes retain their
    whole parameter interval. GS2 is the exact even-real companion
    reflection identity and supplies the negative-T half.

11. The leaf-count identity by itself would not prove coverage for an
    arbitrary imported receipt. The independent oracle reconstructs
    every dyadic path from exact rational coordinates and rejects
    duplicates, accepted ancestors, missing coarse roots and missing
    child quadrants. It verified all 1,600 coarse roots, 9,303 internal
    nodes with exactly four children, 29,509 accepted leaves and depth5.
    It also verifies local-factor selection counts against the exact
    root brackets on every leaf. Attempted parameter count 38,812 is
    exactly leaves+splits; every accepted leaf encloses one whole
    native coefficient interval.

12. Independently recomputing each beta, G14 and GS3 from the stored
    rational family margins and the stored upper J1,J2 bounds gives
    strictly positive guards on all 29,509 leaves. Every reconstructed
    actual sector lower bound exceeds 1/200000. The minimum is about
    7.526221534807278e-6 and the minimum reconstructed acceptance about
    7.978116312022333e-6. Exact rational minima are saved in the oracle
    receipt. The recorded minima and all recorded per-leaf positivity
    bounds were independently checked as well.

13. Gzip is storage only: decompression yields canonical, sorted JSON
    containing every exact box margin, with no omitted leaves. Gzip
    mtime is zero. Every displayed direct-source hash in the receipt
    matches the current file, and loaded backend binary hashes match.
    The source list is a direct list; it is not a recursive hash of
    every analytic theorem referenced by those sources.

## Independent controls and precise replay scope

Scripts and outputs are under /tmp only; owner artifacts were preserved.

* `/tmp/review_bound_gaussian_receipt.py` and
  `/tmp/review-bound-gaussian-receipt.json`: complete exact tree,
  parameter/local-factor counts, direct source hashes and exact rational
  transport guards for every retained leaf.
* `/tmp/review_bound_gaussian_controls.py`: native Taylor interval and
  both finite remainder radii reproduce the retained exact rationals;
  14 difficult/real-zero/endpoint leaf enclosures reproduce the complete
  frozen leaf records exactly. Symbolic checks reconstruct the complete
  geometric remainders for K=1..4 and the full local polynomial derivative
  and companion quotient at a genuine exact real zero.
* Six independent direct rational-function sums retain all 7,938 far
  factors, with exact dyadic midpoint roots and separately recomputed
  integer-power coefficients. Their errors fit the full geometric
  remainder budgets. These are arithmetic controls on concrete finite
  products; the native uncertain roots remain fully enclosed in the
  actual frozen leaf replays.
* Direct actual-source spot controls replay all 29 primitive Hardy
  brackets below 100 plus six representative later brackets, including
  the far-cutoff boundary and the final bracket. All 35 strict sign
  crossings passed. Five independent local Taylor evaluations of actual
  Gamma/zeta Xi and its first two derivatives give the expected guarded
  positive companion sector, including T=100 and y=1/2.
* `/tmp/review_bound_gaussian_structure.py` extracts the actual frozen
  cover_box function. Normal and optimized synthetic tests at depths
  0,1,3 verify exact area, four-child counts and disjoint interiors;
  forced failure verifies the depth8 limit fails closed.

The complete owner normal/-O native runs are retained. This audit does
not repeat every one of the 8,049 primitive sign brackets or all 29,509
directed enclosures. The explicit complete-count historical input,
infinite product/count theorems and backend correctness contract remain
dependencies. A fixed successful rectangle does not certify an unbounded
sector, an additional complete census or RH.

The expanded independent Taylor/leaf/35-primitive/5-native-point/full-far
controls also passed normal and optimized modes with identical output:
`/tmp/review-bound-gaussian-controls.log` and
`/tmp/review-bound-gaussian-controls-optimized.log`. Thus all independent
implementation controls, as well as the actual adaptive recursion
controls, remain active and agree under -O.

## Frozen hashes

Compressed receipt:
`de55ef2163a3c875133066a0ee6337970fc146bfad1cf0439881fd5b32e91875`.
Uncompressed canonical receipt:
`ec3be8c7739335c0160b4b59e429e1a9c0089f9ec8b9e94bb581e89260a8d07e`.
Checker:
`e6df586352f78f2cbac9c96ade4aca8fd8ef1acdb079ad6161e43784b0dccdae`.
FINITE_PRODUCT_JET.md:
`d56d119770fb0aaa6b210ab40ca36e9ead55a4b60a66fa1b8cce3e90668f04a4`.
BOUND_GAUSSIAN_SLAB_CERTIFICATE.md:
`5e2de8ec02baa4cd283083898c3e332302bc03528f4effdf5a5b588ba1ac4a12`.
Candidate census:
`bbb7fe9adce4fa9581cbb23fb558c62abafec4e568cb69c4d9f0324443ad8c20`.
Producer:
`4cd87390db736ee4a745942a988da4566412909b51b7cdca029171f2a67aa3f2`.
