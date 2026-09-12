# Collective theta ferromagnets

**Proposed components; independent review required. The all-order construction
and RH remain unproved.** This is a continuation of #842, not a new canonical
acceptance or an end-to-end RH proof with an omitted construction.

Read [PROOF.md](PROOF.md), then [REVIEW.md](REVIEW.md) and
[VALIDATION.md](VALIDATION.md). Exact dependencies are in SOURCES.json.

## Positive construction results

**CT1.** The actual six-moment seed can be made CONNECTED: turn on a prescribed
path through the 4096 bath spins and one connecting edge to the K8 block, all
at a sufficiently small positive coupling. Adjust the block coupling and the
two positive field scales. An explicit derivative and uniform implicit-function
argument preserve variance, fourth moment and sixth moment exactly. This uses
the parent's strict native certificate. No numerical connecting strength or
higher-order match is supplied.

**CT2.** Every finite weighted zero-field pair ferromagnet can be approximated
in all fixed moments and entire MGFs by CONNECTED, common-field ferromagnets of
maximum degree three. Replace each spin by a strongly coupled path; every
misalignment and rounding error has an explicit finite bound. The resulting
all-order source-realization target is equivalent to the parent's one. Graph
size and coupling strengths may grow; it is not a construction of the unknown
theta limit.

## Arithmetic restrictions on a successful all-order sequence

**CT3--CT4.** The actual theta law has no nonzero Gaussian convolution factor
and no nondegenerate finite-lattice Lee--Yang convolution factor. The second
claim uses the published unconditional Li--Radziwill theorem: a whole vertical
arithmetic progression cannot consist of critical-line zeta zeros.

Consequently, in any successful sequence whose connected components each have
one common field weight, the total variance in components with at most B spins
tends to ZERO, for every fixed B. Independent bounded-size blocks cannot extend
the seed to all orders. Adding bridges whose TOTAL coupling tends to zero does
not repair this. General growing connected models remain possible; there is no
refutation of RH or of the full Ising programme.

**CT5.** The exact theta moments satisfy
(E|X|^p)^(1/p)~log(p)/(2sigma). If a growing independent unbiased-spin bath has
L_r>=r(r-1) spins while the full model matches through moment 2r, its variance
must be at most [e/(8sigma^2)+o(1)]log^2(2r)/r. A fixed positive bath variance
cannot persist.

Section 7 gives the exact random-cluster equations for the remaining interacting
construction, including all variance/covariance terms. Section 8 supplies the
complete conditional ending via Lee--Yang and Hurwitz, but does not prove its
all-order graph-existence premise.

## Executable scope

```
python -I -S -B check.py --check result.json
python -I -S -B -O check.py --check result.json
python -I -S -B test_check.py --part 1
python -I -S -B test_check.py --part 2
python -I -S -B test_check.py --optimized --part 1
python -I -S -B test_check.py --optimized --part 2
```

The new checks use exact rational spin and random-cluster sums, full small clone
graphs, independent-bath combinatorics and formal jet algebra. They do not
compute a theta integral, a zeta zero, an infinite-volume spin limit, or a new
moment-realization certificate. Prior source evidence is inherited, not rerun.
