# Validation, self-audit, and publication status

## What was performed

The author derived the two mathematical notes, then wrote and ran the standard-
library diagnostic `checks/check_replica_model.py` in ordinary Python and
`python -O`. The resulting JSON files are byte-identical. A separate set of
three deliberately corrupted temporary scripts was rejected in both modes.
No independent reviewer was available or invoked. These are author checks,
not independent AI review or human peer review.

The exact diagnostic ran 44,979 explicit finite predicates per execution:

| Check | Count |
|---|---:|
| Eisenstein ideal counts by norm, through norm 512 | 512 |
| Finite Bernoulli basis orthogonality | 768 |
| Exact causal mean/inverse coefficients | 771 |
| Centered operator factorization on finite horizons | 12,336 |
| Exact coherent means | 24 |
| Exact orthogonal energies | 24 |
| Fourth-moment Jensen lower bounds | 24 |
| Exact annulus-divisibility count identities | 495 |
| Actual joint-moment expansions, orders 1 through 4 | 20 |
| Independent joint-moment expansions | 20 |
| Exact joint-moment discrepancies | 20 |
| Vanishing physical probabilities when radical exceeds Y | 29,956 |
| Probability normalization, nonempty panels, and mask controls | 9 |

Many predicates repeat algebra across different tuples; these are not 44,979
independent analytic cases. In particular the high-radical count is a repeated
finite guard. No finite result is promoted to an asymptotic bound.

The exact physical panels use ideal bases with Y=16,32,64,128,512 and column
horizon D=24. Their deterministic source is the sharp finite Mertens sum, an
example covered by the general locally bounded causal-function theorem. This
is NOT a numerical implementation of the source's infinite-convolution smooth
window, and no window-specific claim is tested by those panels.

The deeper finite-prime operator panels use four distinct prime ideals with
norms 4,7,7,13 and horizons through 256. They test repeated powers of the same
ideal, two distinct split-prime ideals of equal norm, and shared supports in
orthogonal decompositions. They are finite-prime identity checks, not empirical
samples from the complete asymptotic prime product.

## Deliberate false-substitution tests

The checks reject each of the following in ordinary and optimized Python:

1. Removing the Bernoulli centering in the orthogonal basis.
2. Adding an erroneous small bias to every physical divisibility probability.
3. Identifying the two split prime ideals that have the same rational norm.

The exact failure receipts are in `results/mutation_checks.json`. The original
checker is not modified by these tests. The `require` function raises an
exception explicitly; its predicates remain active under optimization.

## Mathematical self-audit

The following sensitive points were checked in the written derivations:

- A divisibility event for several dilations uses the radical of their union,
  not the product of their norms and not independent indicators for prime powers.
- The rough-annulus denominator is paid explicitly. Its required threshold is
  Y >= C R_Q^2. The growing-Q result proves this threshold is satisfied.
- Q(P) is held fixed on the full past horizon of each experiment. No moving-Q
  dilation operator is silently commuted through another operator.
- Critical source norms remain present in EVERY physical/model error bound.
  None is replaced by an RH-strength bound.
- The r-dependent local Taylor estimate requires P >= (4r)^2. The growing-order
  range satisfies this eventually, and all exponential r-costs are recorded.
- The finite source horizon justifies every product expansion, including the
  equal-norm split factors and the causal mean inverse.
- Independent orthogonality is applied only in the Bernoulli model. The physical
  nonorthogonality is an explicitly bounded discrepancy, with no assumed sign.
- The signed-witness corollary uses the fixed real universal test and the
  exact Taylor-Markov lemma of #932; it is not asserted for arbitrary rough
  causal functions.

## Inputs not independently re-proved or certified by computation

The ideal lattice count is restated with its standard fixed-field justification;
its primitive geometry and constants are not numerically certified here.
The rational-prime Chebyshev bound is a classical input, with a primary source
cited in the comparison note. Its prime-ideal adaptation is proved in the note.
The #932 ordinary-zeta bridge and zero-safe window implication retain their
source qualifications. The upstream quasi-Riemann theta theorem and #931's
model moment theorem are not needed for the new comparison/decomposition.

No Lean proof, directed interval enclosure, external literature priority check,
independent mathematical review, or proof of the missing Möbius bound was run.

## Integrity and publication

`MANIFEST.json` records the bytes and SHA-256 of each file in this packet other
than the manifest itself. `checks/verify_manifest.py` verifies those local
bytes. Hashes establish integrity, not truth of a proof.

The GitHub connector verified PR #932 is open/unmerged at
c63b5aaa5d53dd183abb20299cea4628f0ab57b7. Current PR metadata through #934 was
inspected for concurrent work; only the load-bearing sources named in
SOURCE_LOCK.json were read in the scope specified there. No full audit of every
adjacent branch is claimed.

The connector exposed no mutation action. Plugin discovery found no usable
additional GitHub write action. The local runtime also failed to resolve
raw.githubusercontent.com. No push, commit on GitHub, remote branch, or PR was
created in this pass. The additive patch contains only this new standalone
folder and has been applied and byte-checked in a clean temporary local tree.
It was NOT tested against a complete local checkout of the upstream base,
which was unavailable.
