# Complete moments bootstrap a source zero-free central range

Status: proposed analytic theorem with a directed native degree-twelve guard
packet, pending independent source/math/code review.
Scope: actual `Xi(z)=xi(1/2+iz)`, its complete positive theta source, complete
classical strip and complete even product. The primitive packet proves
`Xi(z)!=0` throughout `|Re z|<=14`; the complete strip confines all zeros,
so this statement has no restriction on Im z. The resulting global acute
projection is valid through moment order 22. It does not establish a
complete census at larger height or RH.
Exact dependencies: [THEOREM.md](../../xi/outer-ray/THEOREM.md), the source
theta disk argument CF1–CF5 in
[COUNT_FREE_CENSUS_RECOVERY.md](../../xi/outer-ray/COUNT_FREE_CENSUS_RECOVERY.md),
and complete paired-product coefficient extraction. All primitive bounds
below are freshly evaluated from Gamma/zeta; no finite root list, strict
endpoint-sign receipt, zero-count routine or published verification is used.
What was run: native `acb_series` completed Xi through degree twelve at
224 bits, five exact rational source-exclusion guards, and exact angular
projection and arctangent guards. The checker uses no root enumeration.
Smallest remaining gap: independent frozen-source review and native replay.

## MB1. A complete-moment exclusion step with no root selection

Let F be even real entire, `F(0)>0`, of order below two, with its complete
constant-times-genus-zero product in `z^2`, and all zeros in `|Im rho|<=A`.
Suppose an already established source theorem gives `|Re rho|>R>0` for
every zero. For a positive integer k, assume

\[
 2k\arctan(A/R)<\pi/2,\qquad
 c_k(R,A)=\cos(2k\arctan(A/R))>0.
\tag{MB1}
\]

The complete unsubtracted coefficient is

\[
 C_k=-k[z^{2k}]\log(F(z)/F(0))
     =\sum_{\operatorname{Re}\rho>0}m_\rho\rho^{-2k}.
\tag{MB2}
\]

Complete conjugate grouping makes this real; absolute convergence follows
from the complete product's inverse-square sum. By the monotone acute
cosine projection,

\[
 C_k\ge c_k(R,A)\sum_{\operatorname{Re}\rho>0}
                      m_\rho|\rho|^{-2k}\ge0.
\tag{MB3}
\]

If a directed native enclosure gives `C_k<=U_k` and an H satisfies

\[
 \boxed{U_k(H^2+A^2)^k<c_k(R,A),}
\tag{MB4}
\]

there is no source zero with `|Re rho|<=H`. A zero there has a
positive-half-plane occurrence by the prior real-part exclusion; its
multiplicity is at least one and `|rho|^2<=H^2+A^2`. That occurrence alone
violates MB4, and every other source contribution is nonnegative.
Evenness supplies the reflected half. The argument also excludes a zero
at the proposed boundary. No selected root is subtracted in MB2.

For rational R,A, compute the exact projection as

\[
 c_k(R,A)=
 \frac{\sum_{j=0}^k(-1)^j{2k\choose2j}R^{2k-2j}A^{2j}}
      {(R^2+A^2)^k}.
\tag{MB5}
\]

The prior exclusion is essential: a complex quartet can have a negative
complete inverse-power moment when its doubled root angles leave the acute
sector. A native small coefficient alone is not an exclusion theorem.

## MB2. Five authenticated actual-Xi steps reach real part 14

The actual positive theta source and the native seed `Xi(0)>99/200` give
CF1–CF5: `Xi` has no zero in the closed disk of radius 11/2, because
`Xi(-11i/2)=2*pi^3/63<2*Xi(0)`. The complete classical strip `A=1/2`
then gives `|Re rho|>sqrt(30)>5`. This supplies the starting R=5.

The new checker directly evaluates

`s=1/2+i*z`,
`Xi(z)=s(s-1)/2*exp[-s*log(pi)/2]*Gamma(s/2)*zeta(s)`

through degree twelve at 224 bits. It verifies its strict constant seed,
nonzero divisor, and parity/reality enclosures, then forms the normalized
logarithmic jet. Each upper endpoint is outward rounded and converted to
an exact rational. No source root input appears in the calculation.

Apply MB4 successively with the following exact R, k and H:

| Prior R | Moment k | New exclusion H | Strict guard ratio, rounded for reading |
| --- | ---: | --- | ---: |
| 5 | 2 | 12 | 0.8393116834 |
| 12 | 3 | 13 | 0.7213935042 |
| 13 | 4 | 27/2 | 0.7717132954 |
| 27/2 | 5 | 139/10 | 0.9341613127 |
| 139/10 | 6 | 14 | 0.9985509140 |

Every acute-angle hypothesis is immediate from
`2k*atan(A/R)<2k*A/R=k/R<1<pi/2`. Every accepted exact rational ratio is
strictly below one. Each established H is the next step's prior R; no
later result is assumed in an earlier projection. In particular,

\[
 \boxed{|\operatorname{Re}\rho|>14
 \quad\text{for every actual Xi zero}.}
\tag{MB6}
\]

The last margin is about 0.001449086, but only the exact rational guard
in the receipt is an acceptance predicate. These central-range exclusions
are compatible with the known first real Xi zero above 14; no approximate
zero location or candidate root index is used in this proof.

## MB3. The complete remaining source now has 22 acute moment orders

With the proven `R=14,A=1/2`, for every `1<=k<=21`,

`2k*atan(1/28)<42/28=3/2<pi/2`.

The endpoint k=22 also remains acute. The exact identity

\[
 \arctan x=x-x^3/3+x^5/5
             -\int_0^x\frac{t^6}{1+t^2}\,dt
 <x-x^3/3+x^5/5\qquad(x>0)
\tag{MB7}
\]

gives

\[
 44\arctan(1/28)
 <44\left(1/28-1/(3\cdot28^3)+1/(5\cdot28^5)\right)
 <314159/200000<\pi/2.
\tag{MB8}
\]

The middle comparison is exact rational; the last uses the freshly directed
constant `pi>314159/100000`. Thus the exact positive projections MB5 are
valid for all `1<=k<=22`. Any collection of real root occurrences selected
from authenticated disjoint strict sign intervals leaves these same positive
projections valid for the complete residual. Its directed upper guard

`U_residual,k*(H^2+1/4)^k<c_k(14,1/2)`

therefore supplies the higher count-free complete simple census predicate
at that proposed H, with all unknown roots and extra multiplicities retained.
This is a conditional predicate; no new residual coefficient or census
height above the separate accepted packets is computed here.

The native zero-free proof itself only needs complete coefficients through
k=6. It does not compute degrees 14 through 44 or prove the displayed
residual guards at higher k. Root-interval widths and native coefficient
precision remain necessary for any future subtraction certificate.

## MB4. Reproduction and source boundaries

Run from the repository root without overwriting its accepted receipt:

```bash
source /workspace/.riemann-tools/activate.sh
python research/exploratory/2026-10-10-four-hour-wave/heights/final-review/check_complete_moment_bootstrap.py --output /tmp/complete-moment-bootstrap.json
```

Every predicate uses an explicit failure branch, so optimized Python retains
all checks. The receipt binds the primitive source formula, direct proof
sources, checker, exact guards and native extension/shared-library hashes.
It does not authenticate the infinite theta identity, strip, product theorem,
or classical Gamma/zeta continuation by finite checking. All runs use the
same directed native arithmetic backend. This is a finite primitive guard
packet supporting a complete-source analytic zero-free range, not a proof
that every actual zero is real or that a full kernel has all-order positivity.
