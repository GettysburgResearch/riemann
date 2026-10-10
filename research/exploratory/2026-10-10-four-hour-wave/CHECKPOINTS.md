# Publication and review checkpoints

Status: ongoing four-hour wave, 11:59:27–15:59:27 UTC on 10 October 2026.

The root coordinator owns publication. No accepted registry entry is changed.
Scoped mathematical review below does not authenticate inherited source
theorems, formalize the analysis, or claim RH.

## Checkpoint 1: directed anchors and continuum positive sector

Prepared around 12:20 UTC. Included work:

- `certificates/`: sixteen disjoint critical-pair existence intervals, using
  Arb at 256 bits and an optimized-Python replay at 128 bits. The first nine
  received independent branch/IVT review; the root verified the appended
  seven by the identical exact-rational procedure.
- `operators/CODIMENSION_18_COERCIVITY.md`: exact L=1 source-tail reduction,
  globally covered multiplier inequality, codimension-18 primitive coercivity,
  and the inherited residual enclosure for the new 18-dimensional matrix.
  An independent reviewer checked the Fourier-domain hypotheses, sine transfer,
  rational compact coverage and unbounded tail. Normal and optimized replay
  preserve every explicit acceptance predicate. Matrix positivity remains open.
- `arithmetic/NEGATIVE_MASS.md`: the root checked the Mellin normalization,
  noncancellation, nonnegative-transform Landau implication, conditional Mertens
  upper rate, explicit rightmost-pole lower constant, and signed BV firewall.
  This checkpoint keeps the Mertens estimate as an explicit hypothesis.

Other workstreams remain under active analysis and are omitted from this first
publication snapshot until their proofs and execution receipts are ready.

Publication receipt: commit `e742f14` pushed to the research branch. Draft PR
<https://github.com/GettysburgResearch/riemann/pull/911> was created and attached.

## Checkpoint 2: reviewed adapters and stronger uniform bounds

Prepared around 12:55 UTC. Included work:

- Exact critical negative-mass exponent equality, a fully written
  zero-free-to-Mertens adapter, and all-real SHARP positivity for m>=1.737.
- Negative-only quartet completions with H^-5 and H^-7 tails, a native
  complete zero count, 48 directed critical anchors and compact positivity
  through 96 points on 0<x<=1.
- Native codimension-14 continuum coercivity and a convex full-continuum
  window of length 3/20, with explicit positive lower constants.
- Source-qualified derivative, theta-tail and modularly normalized quartet
  obstruction models, plus fifteen compiled Lean capacity inequalities.
- A conditional new half-plane B=0.87495703 from the enlarged plain-moment
  adapter, assuming the frozen source analytic inputs.
- Exact correlation transfer, square-divisor transport and a bounded
  multiplicative log-saving example with no summatory power saving.

The review record is `SCOPED_REVIEWS.md`. Root replayed the completed
component checks. The continuation imports, compact height restriction,
modified-source restriction and continuum residual gap remain explicit.
New two-label, mixed-node and all-order outer-ray work continues separately.
