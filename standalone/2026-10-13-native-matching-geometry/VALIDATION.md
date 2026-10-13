# Validation and limits

Status: same-author validation of proposed written proofs and exact finite
identities. No independent mathematical review, integration verdict, external
peer review, proof-assistant build, full-repository validator or remote CI.

## Executed

1. `python -I -S -B verify.py` and `python -I -S -B -O verify.py` both completed.
   Their JSON reports are byte-identical to `results.json`.
2. `python -I -S -B calibrate.py` and its optimized counterpart both completed.
   Their JSON reports are byte-identical to `calibration.json`.
3. The copied arithmetic helper matches the exact #942 Git blob and size.
4. The payload inventory is bound by MANIFEST.json. Package/patch round-trip
   results are recorded in the separately generated DELIVERY.json; that file
   authenticates publication artifacts, not theorem truth.

## Checker scope

165,577 explicit predicates including setup and simple domain checks:
- 1,099 graphs on at most five vertices: rational matrix rank versus a separate
  bipartite-component calculation; representative graph dimensions through k=8.
- Dyadic fibers and energy identities on four small graph families, plus exact
  K_(2,2), K_4, and K_(3,3) equal-margin counts.
- 17,846 local principal occurrence patterns through k=8: deterministic
  cross-match/six-slot decoding, reconstruction, total norm cost and parity.
- Higher incidence summability guards; these dominate the raw predicate count
  and are not independent asymptotic theorems.
- Rational positive-density local factors and the exact 926-versus-922
  order-twelve phase example, which prevents discarding negative alias terms.
- All good squarefree columns in the stated hard windows D=16,32,64, and all
  nonzero rows with norm at most H for H=1,7,13,31,64. Fifteen complete cases
  compare tuple and product formulations and literal divisor masks.
- Four deliberately false formulas have explicit counterexamples. These are
  algebraic negative controls, not a claim to have run four mutated CLI copies.

These checks do not prove Lemma 4.1's infinite positive density, the all-scale
graph bounds, the Schwartz Poisson estimate, or the moment theorem. Those rely
on the written arguments. Hashing the proof is not independent review.

## Calibration scope

Every good squarefree ideal column in D/2<Nn<=D is retained at D=64,128,256,
512,1024,2048. There are 294 columns and 42,299 pair products at the largest
scale. Both split prime ideals and the inert primes are included.

Each independent principal reference is enclosed using 96-bit dyadic rational
endpoints. Every summand is floored/ceiled by integer division; the final width
is at most the number of product ideals times 2^(-96). At the first three
scales the interval is checked against a separate full Fraction sum. Exact
sharp physical principal sums at H=D and H=ceil(D^(21/20)) are compared using
two different product-label implementations from the prior helper. The root
and all rounding tests use integer arithmetic.

This is a principal calibration only. It does not measure the full physical
moment, the signed remainder, any numerical zero, or a new asymptotic rate.
The hard diagnostic window is not evidence for a smooth-test theorem.

## Same-author reconstruction of the analytic steps

The author checked these load-bearing points explicitly:
- unsigned, not oriented, graph rank; odd-cycle and isolated-vertex cases;
- the geometric deficit sum with unequal vertex caps;
- uniformity of the F_theta ideal mean and of the six-slot sums as theta -> 0;
- an injective local decoder with shared primes retained;
- all sixth-power aliases at k>=6, and why general unitary phases prevent
  termwise positivity across aliases;
- the high-product, squarefree, alias-isolated charge blocks in the lower bound;
- the finite-prime approximation and both uniform large-prime error sums in
  the positive-density lemma;
- zero-row subtraction and uniform rotated-lattice bounds at every Y>0;
- choosing theta=min(1/2,1/log(2H)) without setting theta=0.

This list is not an independent referee report. Recommended review priority:
PROOF Sections 3, 4 and 5, then the distinction between the absolute graph
sector in Section 6 and the still-open signed singleton sum in Section 7.

## Publishing limitation encountered

Live GitHub reads succeeded. Discovery of `create` and `push` actions returned
none in the current tool surface. Plugin discovery found the already-installed
GitHub integration, not an additional connected write provider. The container
has no `gh` executable. A noninteractive `git ls-remote` attempt failed because
`github.com` could not be resolved. No branch, commit, PR, comment or repository
file was written by this session. An add-only patch is supplied instead.
