# Independent review of paired collision bounds, the wider tube, and incidence pricing

Status: ACCEPTED at the scopes specified below. The complementary short-trace
contract remains OPEN. No generalized moment, signed-remainder estimate,
zero-free boundary, or RH theorem has been established by this review.

Reviewer: `/root/final_height_review/collision_review`, 2026-10-10, during
the authorized two-hour continuation. No Git operation or prior-file edit.

What was actually run: local source and checker reads and SHA-256 binding.
Neither finite checker was executed by this reviewer. No independent
directed replay, numerical Euler experiment, or moment computation is claimed.

## Frozen source identities

All paths in this table are relative to
`research/exploratory/2026-10-10-two-hour-continuation/literature/`.

| File | SHA-256 |
| --- | --- |
| `PAIRED_HIGHER_MOMENT_COLLISION.md` | `04c3a1ec1d82d977f6a7d9a0c86486fc87161f1d41d35ba389ab5e2ce94f35f6` |
| `WIDE_SUBCRITICAL_TUBE.md` | `53568631060432784811d8474e8d774257664826e8fb9fa59c0ba47959745f02` |
| `COMPLEMENTARY_SHORT_TRACE_CONTRACT.md` | `968a2bee6d47f0a92fded0ab32c23963d31332f649dc0046604b7b568d48640c` |
| `PRIME_SLOT_CANCELLATION.md` | `d37ad696b46c7dda15a7faf314c46cda2d7d67e25ac8d3288c7f138aac373c13` |
| `PAIRED_FREQUENCY_COLLISION.md` | `d057fd4138a4f9c7fcb5455c51e8eabe04b707b8817d4a6ae3359cdfdb85df9a` |
| `PRIME_SLOT_SUBCRITICAL_TUBE.md` | `5aca641b5c58e8d2efaf643c660d98cb5970235478bd9e0622e1d6014c4a1c28` |
| `SUBCRITICAL_RAPID_COLLISION_DECAY.md` | `a41b84b54f0e4052e6700887bad5cd82552ab452744f29c1b5f70e68cbf0735e` |
| `SHORT_POLYNOMIAL_COLLISION_TRANSPORT.md` | `c538719277b1e7de70a7e3f872fb2720668bd43ca57c9cffff6ff29b6766d5ac` |
| `check_paired_higher_collision.py` | `aad48e729419b89fc63bc11c4c35c7a2836cc37721c052b6fc62ed77e5138b33` |
| `check_wide_subcritical_tube.py` | `ec0a7a1f53362f72702bae4d735942491ba89c60857179646eb75cec18d788f8` |

The original source file `/workspace/.riemann-research/sources/qrh11-12.tex`
has SHA-256
`d9a8f15aa770cf883d0eabd2b775fad694ce20b44cba7928f5c0c9a6d8750d4d`.
The imported PR914 `CONDUCTOR_SECTORS.md` at
`/workspace/.riemann-research/moment-sources/914/standalone/2026-10-10-sextic-moment-conductor-core/`
has SHA-256
`c160bbb1b1d7c6bcc5514d496ad41f15fd17ea3d36206b0d05cfa0d7d6503983`.
I checked its source/mask definitions and the full-moment/controlled-sector
interface. Its controlled-sector estimates remain named imported inputs;
this is not a new independent review of that entire upstream packet.

## PH1–PH4: paired-frequency factorization and paid logarithms

ACCEPTED for every fixed integer `k>=2`, the specified k-dimensional
paired plane, every source ray phase, and all literal moving exclusions.

At each eligible prime, pair the right slot indexed j with the conjugate
of left slot j. The k self-cross factors are exactly `1-x`. Left/right
same-side factors occur in conjugate pairs, and the two cross factors
associated with distinct indices i,j also occur in conjugate pairs.
This yields precisely the modulus identity PH1, with k self-cross factors,
`binom(k,2)` squared same-side factors, and `binom(k,2)` squared
cross-frequency factors. Their total degree is
`k+2*binom(k,2)+2*binom(k,2)=k(2k-1)`: all pairs are present.

Bounding each same-side modulus by `1+x` yields

    (1-x)^k (1+x)^(k(k-1))
      = (1-x)^(k(2-k)) (1-x^2)^(k(k-1)).

The cross-frequency factors retain their actual phases. This verifies the
sign of the potentially growing exponent and PH2. Multiplication over
eligible primes and the uniform degree-three remainder bound in P4 give
PH3. At equal frequencies the cross product adds the exponent k(k-1),
leaving exponent k; at k=2 the positive zeta exponent vanishes.

The completed-zeta comparison in PF3 compares logarithms of moduli by
absolute first-power bounds and a summable higher-power remainder.
Its first-power finite change costs
`delta*sum_(Np<=Y) log(Np)/Np=O(1)`; its omitted first powers cost
`integral_Y^infinity dx/(x^(1+delta) log x)=O(1)` for
`delta=1/logY`. These are uniform in every real frequency difference.
The complete zeta is evaluated at real part strictly greater than one.
Its pole gives `Z_full(1)<<logY` and the reciprocal near-pole bound.

Because `k(k-2)>=0`, deleting primes decreases the positive factor.
For each reciprocal frequency factor the moving deletions cost at most
`prod_(p|uQ)(1-1/Np)^(-1)`. The elementary small/large-prime split in
P5 gives the displayed `1+loglog(3N(uQ))` bound. There are
`2*binom(k,2)=k(k-1)` reciprocal frequency powers. Thus PH4 has the
correct log and loglog exponents, retains every moving mask, and remains
valid with its explicit norm weight for the complete Schwartz row range.

When all pair differences are at most `b/logY`, the reciprocal pole bound
contributes `(logY)^(-k(k-1))`, hence the total log exponent is
`k(k-2)-k(k-1)=-k`, as in PH5. Extending this to all paired frequencies
by PH6 uses exactly the explicitly imported CLASSICAL-PF6 reciprocal
zeta estimate. Its zero-free proof is not reconstructed in these sources
or in this review.

The source set contains only a paired plane. None of these estimates
controls the full independent 2k-frequency trace, the individual source
reciprocals at real part 1/2, or the source moment. In particular the
local determinant `-|A(x)-A(y)|^2` in PF8 prevents the proposed automatic
positive-kernel Cauchy extension.

## WT1–WT3: quadratic phase floor and complete short-tube transfer

ACCEPTED for every fixed k, `1/3<sigma<1/2`, and fixed strict width
`0<kappa<arcsin(1/sqrt(2k))`. Constants are not uniform at the critical
width or as k grows.

There are exactly k^2 cross pairs. Their normalized phases are
`exp(-i(delta_i+epsilon_j) logq)` because the central source phase and
its conjugate cancel. Their arguments have magnitude at most `2kappa`.
The width restriction implies `2kappa<pi/2`, so each real part is at least
`cos(2kappa)`. The two same-side collections together have k(k-1)
pairs, each with real part at least -1. No conjugacy between their
independently perturbed phases was assumed. Consequently their full real
sum has the floor

    k^2*cos(2kappa)-k(k-1)
      = k*(1-2k*sin(kappa)^2) = lambda_quad > 0.

For `x=q^(-2sigma)`, the logarithmic remainder per pair is bounded by
`x^2/[2(1-x)]`. Its prime sum is finite, since `4sigma>1` and elementary
ideal counting bounds the larger all-ideal sum. The difference between
`log(1-x)` and `-x` has the same summable bound. Thus the complete pair
product is bounded by a uniform constant times the eligible positive
Euler product raised to `lambda_quad`. The degree-three remainder has
its separate summable majorant because `3sigma>1`.

RD1–RD4 genuinely provide any prescribed fixed polynomial decay: raising
the positive complete norm sum to an arbitrarily large fixed integer
power, and paying the complete ordered-divisor multiplicity, gives that
claim without a prime-ideal asymptotic. Moving deletions have cost at most
`C*(Nu*NQ)^epsilon_0` after decreasing the preliminary exponent. The
power requested in RD4 can be increased to absorb
`Y^((h+k)*epsilon_0)`, using `NQ<=Y^k` and `H` comparable to `Y^h`.
The remaining factor `(1+Nu/H)^epsilon_0` is integrable against the
actual Schwartz spatial majorant. This verifies WT4–WT5 for every row;
no spatial row tail has been discarded.

SC3 has only nonnegative coordinate exponents. A deleted term of an
individual finite Euler polynomial with column norm above Y cannot alter
a final coefficient of column norm at most Y. The literal norm weights
force that final range. Hence SC4 is an exact complete norm-filtered
Mellin identity. The finite cutoff and absolute collision-series
convergence on positive-real-part contours justify inversion; no infinite
reciprocal-L contour shift is used.

The literal short factors satisfy `|T_i,Y|<<Y^(1-sigma)` uniformly in
the frequencies and moving exclusions. Their product, the norm scale
factors, the full Schwartz row sum, and the complete incidence count have
only fixed polynomial costs. Requesting a larger fixed power in WT5
pays all those costs. Thus the total enlarged-tube component of the
short representation is indeed `O_M(HY^(-M))` for every fixed M.
This assertion concerns that short representation; complete filtered
integrals agree, but partial tube integrals in the original and short
representations need not agree.

The explicit choice `kappa=1/(2sqrt(k))` is strictly inside the permitted
interval. Since `sin(kappa)<kappa`, it gives
`lambda_quad>k*(1-2k*kappa^2)=k/2`, and is larger than the prior
half-floor width `1/[4(2k-1)]`. Its physical frequency width still
shrinks as `1/logY`.

## CT3–CT4: exact incidence price and conditional implication

ACCEPTED as a proved positive incidence sum and a conditional deduction.
CT1 is an explicitly OPEN hypothesis, not an accepted estimate.

For each actual squarefree allocation, the q_I are pairwise coprime and
the subset labels retain every same-side and cross incidence. Norm
multiplicativity gives the exact identity

    product_i Nc_i = product_I (Nq_I)^|I| >= (NQ)^2.

All subsets have cardinality at least two and sigma is positive. Therefore
`product_i(Nc_i)^(-sigma)<= (NQ)^(-2sigma)`, and `Nc_i<=Y` in each
of the 2k columns implies `NQ<=Y^k`. Both directions and their signs
are correct.

For a given squarefree Q, each prime is assigned exactly once to one
of `m=2^(2k)-1-2k` allowed subset labels. Dropping the column support
restrictions yields at most `m^omega(Q)=d_m(Q)` assignments, rather than
discarding composite Q or collapsing labels. For every fixed delta>0,
the elementary ideal divisor bound gives `d_m(Q)<=C_delta*(NQ)^delta`.
Enlarging the positive sum to all ideals of norm at most `X=Y^k` and
using the fixed-field count `A_K(X)<<X` gives

    sum_(NQ<=X) (NQ)^(-2sigma+delta)
       << X^(1-2sigma+delta).

Here `1-2sigma>0`, so partial summation applies with the stated positive
power. Choosing `k*delta<epsilon` proves CT3. Larger incidences only
decrease the original positive weight; all moving masks and exterior
source multipliers still have modulus at most one.

If CT1 holds for the complement with constants uniform in allocations,
the independently paid WT tube bound extends it to all frequencies.
For a fixed allocation, SC4 and the polynomial-frequency integrability
of the fixed smooth Mellin transforms then bound the row-weighted full
integral by

    C H D^(2k*sigma+epsilon_1)
        * product_i(Nc_i)^(-sigma).

The scales `(D/Nc_i)^it_i` have modulus one, so varying short column
lengths introduce no unpriced frequency weight. The cutoff of each
literal T_i remains the common Y; it is not replaced by the eventual
short column length. Summing CT3 with a separate preliminary loss
epsilon_2, and using `Y=bD`, gives exponent
`2k*sigma+k*(1-2sigma)=k`. Choosing
`epsilon_1+epsilon_2<epsilon` proves the conditional CT5.

The actual nonnegative smooth full moment majorizes the sharp moment.
Subtracting the named PR914 controlled-sector contribution then gives
the conditional absolute signed-remainder bound. This uses the exact
full-moment decomposition, never positivity of a selected signed sector.
PR914 states a compact smooth spatial majorant; its completion argument
uses rapid Fourier decay and its trivial row bound uses rapid spatial
decay, so these interfaces also apply to the actual Schwartz majorant.
The original theta source explicitly chooses a nonnegative Schwartz
spatial weight with compact Fourier support. No compact spatial support
or uniform finite row support follows from that Fourier support.

CT1 retains the exterior omega_q, its principal nonunit masks, one common
full row range, the literal source short coefficients, and all independent
left/right frequencies. A paired-plane estimate or a collision-factor
bound alone does not establish this target. This review does not audit
or promote a new zero-free extraction theorem from CT5; CT5 itself is
conditional, and the downstream CT6 extraction in the manuscript's
CT5 section is explicitly imported.

## Checker reading and remaining gate

The paired checker uses exact Eisenstein rational arithmetic and reconstructs
all labeled pairs before comparing with the separated formula. The wider
tube checker reconstructs every pair at its sampled endpoint allocations
with directed Arb/Acb arithmetic. It uses explicit exceptions rather than
assertion-only acceptance. I read their implementation and scope flags.
They sample finite phases and corners; arbitrary ray phases and the
continuum estimates are supplied by the analytic proofs above. Neither
checker proves a source moment or the open complement target, and no
execution of either checker is claimed by this reviewer.

The smallest unpaid statement needed for the conditional full moment is
the literal CT1 complementary short-row trace, uniformly in every exact
incidence allocation and all independent frequencies. The accepted
factorization, larger shrinking tube, complete row-tail payment and
incidence cost do not supply it.
