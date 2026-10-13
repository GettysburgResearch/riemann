# Native signed moments: exact principal reference and a complete census

**PROPOSED component theorem and exact FINITE computation. No improved full
moment exponent, zero-free boundary, or RH proof. Independent review remains
outstanding.**

This continuation of #939 returns to the actual arithmetic rather than enlarging
the coefficient classification again. Read [PROOF.md](PROOF.md), the complete
raw [results.json](results.json), then [VALIDATION.md](VALIDATION.md).

## Mathematical result

For each fixed order 2k and coefficients on all ideals Nn<=X, including the
native Mobius or Liouville source, let P be the COMPLETE principal part of the
physical moment. It includes all sixth-power aliases and every nonunit zero.
Let B be the corresponding independent local-density moment. The proof gives

    P(Phi,H) = c_Phi H B + O(X^(k+epsilon))

for every fixed Schwartz row profile Phi, uniformly for H>=1. For a hard norm
ball the error is instead O(sqrt(H) X^(k+epsilon)). These are absolute errors;
no relative estimate is asserted for a small B. Row-independent coefficients,
fixed k and the stated profile uniformity are essential.

This specializes standard Poisson, inclusion-exclusion and squarefull counting.
It is not a new general large sieve or a bound for the nonprincipal remainder.
The references are exactly invariant under primewise sixth-root phases; hence
Mobius and unsigned-squarefree coefficients have the same principal reference.
Their different physical moments live entirely in the nonprincipal part.

## What the complete arithmetic census finds

Every good ideal in the listed hard column window is included, not a semigroup
on a few selected primes. Every nonzero element in the row ball is included.
Results contain exact 2nd, 4th, 6th and 8th moments for Mobius, Liouville, and
unsigned-squarefree coefficients. Full principal references are calculated for
the fourth moments, not for every large-scale higher moment.

At D=8192 and H=ceil(D^(21/20))=12855 there are 46,608 rows, 1,145 squarefree
columns and 1,231 unrestricted Liouville columns in the window. The Mobius
fourth moment is 114923460372, its exact principal reference is 114879621108,
and the signed remainder is +43839264 (about +0.03816 percent of the reference).
At H=D=8192 the remainder is instead -1192770378 (about -1.62883 percent).
These are finite values, not evidence of a certified decay exponent.

Two calibration failures are resolved explicitly:

- At D=H=4096 an unmasked reference makes the fourth moment look about 13.03
  percent too small. The actual zero-preserving reference gives only -1.35323
  percent. Ignoring nonunit zeros fabricates most of that apparent cancellation.
- Liouville's nonsquarefree columns already have unequal-product sixth aliases
  in the fourth moment at D=512. They add 2748 to the exact H=512 reference.
  Product equality alone is sufficient for squarefree columns only through
  order ten. The code preserves the support even when the sixth charge is zero.

All 15 recorded Mobius fourth cases are below. No case is discarded for sign.
The column test is a HARD annulus, not a smooth-test theorem or fitted model.

| D | H | Native fourth moment | Exact principal part | Signed remainder |
|---:|---:|---:|---:|---:|
| 16 | 16 | 336 | 300 | 36 |
| 32 | 32 | 5136 | 4890 | 246 |
| 64 | 64 | 20976 | 19290 | 1686 |
| 128 | 128 | 280044 | 295296 | -15252 |
| 256 | 256 | 2400654 | 2268108 | 132546 |
| 512 | 512 | 17233824 | 18564120 | -1330296 |
| 512 | 700 | 24073938 | 25257168 | -1183230 |
| 1024 | 1024 | 129675360 | 130607694 | -932334 |
| 1024 | 1449 | 181593786 | 185268672 | -3674886 |
| 2048 | 2048 | 1186401918 | 1187985282 | -1583364 |
| 2048 | 2999 | 1770129186 | 1737230958 | 32898228 |
| 4096 | 4096 | 9310647792 | 9438370176 | -127722384 |
| 4096 | 6209 | 14353730886 | 14293795482 | 59935404 |
| 8192 | 8192 | 72035687874 | 73228458252 | -1192770378 |
| 8192 | 12855 | 114923460372 | 114879621108 | 43839264 |

## Exact remaining target

    M_(2k)=P_(2k)+R_(2k),
    OPEN: R_(2k)(D,H) <= C H D^(k+epsilon)

with the original near-linear heights and test/twist uniformity. Only the
one-sided upper bound is needed. The census rejects assigning R a universal
sign; it does not prove an asymptotic bound for it. All-order principal control
cannot distinguish the special Mobius signs from arbitrary sixth-root prime
rotations, so another estimate on R is still indispensable.

## Reproduction

Python 3 with NumPy is needed for vectorized row sums. No floating point enters
accepting arithmetic; high moments use Python's unbounded integers.

    python -B verify.py
    python -B -O verify.py
    python -B census.py --D 8192 --H 12855 --output replay.json
    python -B -O census.py --D 8192 --near-linear --output replay.optimized.json

The two example census files must match each other and the corresponding case
of results.json after JSON decoding. Every recorded case was separately replayed
under optimized Python and reproduced exactly. See VALIDATION.md for bounds and
what the checker does not establish.

## Attribution and exact source scope

Parent #939: `751eff5d759f82ae8316f141613f2214c97b7553`. Its determinant theorem
is not an analytic input to this packet. #935 at
`a7a7fad2c5fa1929c7e04570cde4188e3191b071` supplies the original Liouville
conventions and unchanged prime coefficients; the provided packet and its local
arithmetic code were consulted. Euclidean residue checks adapt that same-author
small-field method, not an independent outside implementation.

#936 at `eb8d23decc003d36ded287dc98868308192cc889`, PROOF.md, already has the
mask-preserving independent-phase projection, its exact rough-charge blocks,
and the warning about order-twelve aliases. #940 at
`59d5a8ebcd390ff898d63b2fc5ed7290995ae58b`, MATHEMATICS.md Sections 1--7,
already supplies squarefull/singleton counting with explicit growing-order
bounds. Those principles are credited, not rediscovered here. The quantitative
physical-density comparison and complete nonsquarefree census are the present
specialization. No historical priority claim is made.

Recent #938/#941 freezing obstructions were checked at PR-description scope;
they are not imported theorems here. Earlier #914/#928 principal-diagonal and
cube-kernel calculations are credited at the supplied summary scope, not claimed
to be independently replayed. Classical Poisson summation, ideal factorization,
lattice counts and residue-field arithmetic are the named standard inputs.
No quasi-RH, Hecke subconvexity, new fixed-order sieve, or unproved native moment
is assumed. Proof/code authorship is shared; finite replay is not peer review.
