# Scoped final-manuscript audit of the stratified two-scalar raw and full-A2 theorem

**Verdict: PASS for the stated source-qualified component theorems.**

**Reviewed file:** `STRATIFIED_TWO_SCALAR_A2.md`, 22,168 bytes.

**Exact reviewed SHA256:**
`9b540fe779b6e0f3c64baba04deed6ee380f1d9746035afc3cf9c7fdb0cf3ad5`.

**Reviewer:** `signed_auxiliary_attack`. The reviewer supplied the proposed
tau cutoff calculation before the root agent authored this manuscript, then
read and reconstructed the complete final manuscript and its load-bearing
source statements. This is an independent final-manuscript audit, with that
prior mathematical contribution disclosed. It is not a claim of independence
from every underlying idea, human peer review, proof-assistant verification,
or fresh verification of the imported analytic foundations.

No required correction was found in the frozen target. This verdict applies
only to these exact bytes and the explicitly retained source premises.

## 1. Sources read and the scope actually certified

The audit read the complete new manuscript, the frozen
`HYBRID_CUBE_INVERSE.md`, `MOVING_COLUMN_MASKS.md`, and
`A2_MOVING_MEAN_SQUARE.md` identified in its Section 1. It independently
fetched and read the following PR #924 files from commit
`725b2d25ab47e57500049d93985560098c7ef3fa`:

- `SIXTH_POWER_STRATIFIED_INVERSE.md`, Git blob
  `004dd4a8de2237661235a9da460b3caab432ef53`;
- `ANISOTROPIC_A2_NORM_TRANSFER.md`, Git blob
  `1e4e8a9b70fb15ee42bc41abbcdc3b217e07f215`;
- `MIXED_LABEL_COMPLETION.md`, Git blob
  `6f59a15b41cc87c64188a8037cfc3516bf962ea3`.

The new proof continues to require the actual uniform angular scalar
estimate for each of the two Möbius variables, its finite smooth seminorm
loss, the theta and cusp factorizations, and the named classical sieves.
The beta=11/12 notation retains the positive-margin convention of its source.
The beta=1 specialization uses counting in the scalar step and does not
claim a strict improvement over the adjacent counting theorem.

The results under review are positive row energies of a specifically
normalized two-axis Gauss polynomial and its full arithmetic A2 correction.
They are not a native inverse fourth moment. The proof makes no deduction
of a cofinal hierarchy, a new zero-free boundary, 17/24, or RH.

## 2. Exact family, exclusions, and normalization

The raw product an is squarefree, so its two physical factors are squarefree
and coprime. The original q0 exclusion acts on both physical axes. The
fourth-power f symbol retains its zero whenever a column meets f. Therefore
q0/(q0,f) is the exact effective exclusion, including inherited overlaps.
The costs

\[
J=FQ,\qquad K=F^{2/3}Q^{1/3}\le J^{2/3}
\]

are precisely those of the moving-mask factorization. The proof does not
replace them by a label-independent norm contraction. Rows may share primes
with q0 or f; the literal zeros, rather than an extra row coprimality
condition, handle those cases.

The A2 support has the actual five disjoint labels
n1=a c d^2 e^2, n2=b c^2 d e^2. Its normalized correction weight is exactly

\[
\sqrt{N(cde)}\sqrt{A_tB_t/D^2}=1/(xyz^{3/2}),
\]

where x=Nc, y=Nd, z=Ne. The exterior source phase has modulus at most one
only after its row zeros have been retained. The child labels q_t=q0cde and
f_t=fe give J_t=Jxyz and K_t=K(xy)^(1/3)z^(2/3); the e overlap is removed
once as an exclusion and remains in the fourth-power auxiliary.

Nonempty child scales below one have a fixed positive support bound. The
fixed rescaling to unit size preserves the normalization and finitely many
test seminorms. The proof does not apply an estimate to arbitrarily small
nonempty physical scales.

## 3. Sixth-power-free sieve and physical row stratification

The reduction to the sixth-power-free row sieve is correct. With logarithmic
valuation parameters, the three inequalities

\[
P_0\le U,\qquad P_0^2/M\le U,
\qquad P_0/M^{1/3}\le U^{2/3}
\]

follow from the weighted physical norm constraint: the possible positive
excess from the first valuation label is absorbed by log(M). Hence
min(P0L/M,P0^2) is at most (UL)^(2/3), yielding the stated
U+L+(UL)^(2/3) envelope from the two source alternatives. This is the
classical arbitrary-coefficient step, where fixed masks and twists may
legitimately remain in the coefficient vector. No corresponding extension
of a structured theta estimate is asserted.

The row decomposition k=epsilon v^6 k0 uses quotient and remainder of every
prime valuation on division by six. It is unique in the stated generator
convention and permits (v,k0)>1. Units and bad-prime remainder patterns are
retained. For fixed v, the new physical zero mask is rad(v), including on
the cube index and the inverse coefficient. It enlarges Q by at most Nv,
while the actual row height is divided by (Nv)^6. The proof never averages
at the artificial height obtained from the mask's sixth-power encoding.

The original physical strata are disjoint, so their energies add. Only the
short part is enlarged from sixth-power-free k0 rows to all rows, and that
enlargement occurs in a positive norm with the fixed v exclusion retained.
The long part uses the sixth-power-free sieve itself.

## 4. Smooth short/long identity, doubled cap, and oriented raw bound

The proof deliberately dilates the old smooth cutoff: omega is one through
1/2 and zero from one onward. Thus r<=1 gives an exactly empty short part.
If the physical inverse support is at most C B^(1/3), the long part becomes
exactly empty at r=2C B^(1/3). The doubled cap is required by this chosen
profile and appears explicitly in every row stratum and A2 child.

The regrouped coefficient is the actual finite sum

\[
c_r(d)=\sum_{h\mid d}\mu(h)[1-\omega(Nh/r)].
\]

It vanishes for Nd<=r/2. The ideal d may have powers, the factors h and the
physical cube b may overlap, and the inner squarefree raw factor may meet d.
Only the actual outer mask (a,d)=1 is introduced. These are the exact
physical inverse identities; forbidding any of those permitted overlaps
would change the arithmetic.

On every nonempty short dyad the normalized support ratio Z/r is bounded.
The common-divisor shifts preserve that ratio, so the scalar test seminorms
do not acquire powers of the moving cutoff. This justifies using the second
Möbius cancellation with a smooth, including subunit, cutoff.

The oriented raw bound is reconstructed directly from the actual middle
block monomial

\[
\frac{J U^2 A}{BF_1^2}G^{2\beta-1}Z^{2\beta+1},
\qquad G^2Z^3\ll B.
\]

Using the support bound for G yields J U^2 A B^(beta-3/2) Z^(5/2-beta)
without requiring A<=B. If that bound for G exceeds the outer support, it
remains a valid upper bound. The other two monomials give UA and
K U^(4/3) A^(4/3) B^(-2/3) Z^(2beta). The common-divisor weights for the
two scalar estimates have convergent sums at beta>1/2, and the remaining
positive factor retains its allowed overlap with the shared divisor.

For each long raw child, grouping the squarefree physical product gives
normalized squared coefficient mass D^epsilon. The outer mask, f twist and
all other fixed factors are allowed coefficients of the classical sieve.
Minkowski with 1/Nd yields the two ideal tails of powers -5/2 and -2. Their
bounds by r^(-3/2) and r^(-1) remain valid for every positive r; the first
harmonic sum is physically finite. Capped strata have no long part and are
not charged a spurious positive tail.

After the choice r_v=min(2C B^(1/3),R Nv), the six stratum powers are

\[
-6,\quad -17/2-\beta,\quad -23/3+2\beta,
\qquad -6,\quad -3,\quad -6.
\]

All are strictly less than -1 for the entire stated beta range. The
associated ideal sums therefore converge after preliminary small-power
losses are chosen sufficiently small. This proves Theorem 3.1 with exactly
its six monomials and no all-row H^(1/6) factor in the ABR^(-3) tail.

## 5. Full A2 transfer with the new child cutoff

The cutoff

\[
\tau=(3-2\beta)/(5-2\beta),\qquad
R_t=R(B_t/D)^\tau
\]

has 1/3<=tau<1/2 and p tau=(3-2beta)/2. The proof applies the oriented
raw theorem to the actual A_t,B_t, with no hidden size ordering. Each child
then uses its own doubled physical cap and its own sixth-power strata.

I independently substituted the child A,B,J,K,R exponents into all six
raw energy monomials, took square roots, and applied the exterior
1/(xyz^(3/2)) weight. The resulting table agrees entry by entry with the
manuscript. The critical middle row is exactly (-1,-3/2,-2), because its
three child energy exponents before the exterior factor are (0,-1,-1).

For the third row, 2 beta tau>1/3 already places its x exponent below -1.
For the two long rows, tau<1/2 gives strict convergence, including the
most restrictive x exponents. The only harmonic entries are the middle
row's x sum and the base-H row's x and y sums. Every correction ideal is
polynomially bounded on nonempty support, so these cost fixed powers of
log(D), absorbed in D^epsilon. The pairwise-coprimality restrictions are
dropped only in these positive upper sums after the exact projection.

At beta=11/12, tau=7/19, the nonconstant rows evaluate to

| Row | x | y | z |
|---|---:|---:|---:|
| Third short term | -86/57 | -165/76 | -143/57 |
| ABR^(-3) | -53/38 | -37/19 | -91/38 |
| Mixed long term | -24/19 | -31/19 | -239/114 |

These checks certify the coordinatewise norm summation actually used here.
The old cube-root choice gives x exponent -17/18 in the new middle row;
this rejects the naive independent coordinatewise summation with that
choice. It does not reject an ordered or coupled summation of correction
scales, as the final manuscript correctly states.

## 6. Optimization, labels, and quantitative improvement

The balancing cutoffs R2 and R3 in (5.2) are correct. Under JH^2<=D^p,
R2>=1. The inequality K<=J^(2/3) also gives R3>=1. R3 is individually at
most D^(1/3), so min(R2,R3) lies in the admissible parent interval. The
proof correctly avoids requiring that R2 itself lie below D^(1/3).

At the minimum, both increasing terms are at most E*=D^2R^(-3), the larger
of the two closed-form optimized monomials. Since H<=D, its R3 branch is
at least HD. The mixed long term divided by E* is bounded by
(H/D)^(2/3-4/[3(2beta+3)]) K^(-1/(2beta+3)), which is at most one.
The remaining base-H term is smaller. This proves the complete general
optimization, including the moving-label condition and the D^2 range.

At beta=11/12, H=D^(1/2), J=K=1, and R=D^(7/55), the six exponents are

\[
3/2,\quad 89/55,\quad 47/30,\quad
1/2,\quad 89/55,\quad 233/165.
\]

Their maximum is 89/55. Both the raw family and the entire A2 correction
therefore have the claimed energy bound under the stated source inputs.
The adjacent improvement is exactly 31/19-89/55=14/1045. The improvement
over the earlier unstratified raw value is 19/660. The beta=1 powers reduce
to the existing counting theorem and support no strict counting gain.

The sufficient unit-label physical row-height range remains 19/24. With
moving labels the stated condition is H<=D^(19/24) J^(-1/2), H>=1. These
are bounds for positive normalized Gauss/A2 energies, not zeta boundaries.

## 7. General tests, row profiles, and the retained signed boundary

The extension from product tests to a fixed smooth two-variable profile
uses Mellin separation with enough integrable polynomial moments to absorb
the finite seminorm losses. The cutoff depends on fixed physical scales,
so it does not introduce an arbitrary arithmetic coefficient.

The proof handles the row-independent long monomial correctly. Inward
annuli give a logarithmic, not geometric, count for this term; the other
row powers are positive. On outward Schwartz annuli, the original physical
axes, parent cutoff, arithmetic children and their exclusions stay fixed.
Only the reference parameter is enlarged. The largest row power is two,
so fixed Schwartz decay absorbs that growth and preliminary subpower loss.
The proof uses the unoptimized envelope there and does not reapply the
feasibility condition after the row height has grown.

The final scope paragraph accurately preserves the remaining signed
comparison: its coupled row kernel, independently corrected columns,
reconstructed product-column equality subtraction, and adverse original
dual height are not estimated by the new positive theorem. The earlier
small-w audit has a separate addendum explaining how positive child cutoffs
below one affect its method comparison. None of these positive-energy
results closes the native balanced fourth-moment core.

## 8. Executable exact diagnostic and replay

The independently written diagnostic is
`pass3_check_stratified_two_scalar.py`, 14,441 bytes, SHA256
`8514752259495996202e0c771093d181b8d754bc9b353686af7cd8f3b2a6a5a8`.

The deterministic report is `pass3_stratified_two_scalar_checks.json`,
1,805 bytes, SHA256
`423752137129baa502a5f633f59189282a90f059960b3fc9dd7bc578d9fb5c16`.

The program verifies the target proof's exact hash and byte count before
running its gates. It was executed normally and with python -O. Both runs
passed, and their complete stdout and saved reports agree byte for byte.
The optimized-run report has the same hash. Every gate uses an exception;
there are no assert-based acceptance conditions.

Its exact finite coverage is:

- 4,096 mask cases, including original q/f redundancy and permitted A2
  child overlap identities;
- 5,832 row-valuation decompositions, retaining 5,320 patterns with overlap
  between v and k0;
- 7,168 valuation/column-exponent tests of the sixth-power-free sieve
  reduction;
- 270 exact smooth divisor identities and 2,800 cap/support checks;
- 2,952 A2 norm entries and 984 stratum powers across 164 rational beta
  values, including values close to one half;
- 4,158 exact feasible optimization cases, covering interior and boundary
  moving-label costs, plus the explicit 89/55 fractions and savings.

Negative controls reject a false (h,b)=1 restriction, an undoubled cap,
clamping a small child cutoff while claiming the same norm table, the
naive independent old-cutoff summation, and a separate upper bound on R2
that the theorem does not need.

The finite cutoff diagnostic uses a rational piecewise-linear value
profile with the same endpoint and support conventions solely to verify
finite identities and empty-support claims. It does not use that profile
to certify smooth derivative estimates. Those are checked in the written
proof. Likewise the program does not evaluate genuine Gauss sums or prove
analytic estimates by enumeration. It supplements the full algebraic and
source-qualified mathematical reconstruction above.

## Final acceptance scope

**PASS:** Theorems 3.1 and 4.1, their general optimized bound, the moving-label
condition, and the source-qualified raw/full-A2 exponent 89/55 are supported
by the stated premises and the displayed proof. The first place this
conclusion would fail if its inputs failed is the two-scalar structured
block estimate with its exact moving exclusions and uniform finite
seminorms. That input has not been silently replaced by an arbitrary
coefficient or enlarged-domain theorem. No further native moment or RH
claim is accepted by this review.
