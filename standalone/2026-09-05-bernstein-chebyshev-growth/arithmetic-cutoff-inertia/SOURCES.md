# Sources and boundaries

## Exact repository source

- Repository: GettysburgResearch/riemann, stable GitHub ID 1309150028.
- Parent: PR #792, commit `39c13367f4b3956631ea1e00fac6c3005fc32057`.
- File: `standalone/2026-09-05-bernstein-chebyshev-growth/cross-route-hardy-laguerre/BRIDGE.md`.
- Git blob: `81d7d5db7a25f5875a08c10235fdb514d67cc744`.
- Used: the actual arithmetic kernel A1, its normalization, and arithmetic
  trace-class convergence. The gamma multiplier is reconstructed in the new proof.
- Not assumed: positivity, RH, any positive finite section beyond its stated scope,
  or a source-specific cancellation theorem.

The current #792 metadata and comments were read. The #790 cross-programme comment
and current #793 metadata still identify an open full-source matrix sign. No new
claim from those updates is an analytic input to AC-1 through AC-3.

## Classical primary references consulted

NIST Digital Library of Mathematical Functions, accessed 2026-09-05:

- Equation 5.7.6, digamma partial fractions: https://dlmf.nist.gov/5.7.E6
- Equations 5.5.4 and 5.5.8, digamma reflection and duplication:
  https://dlmf.nist.gov/5.5.E4 and https://dlmf.nist.gov/5.5.E8
- Equation 5.11.2, digamma large-argument asymptotics:
  https://dlmf.nist.gov/5.11.E2

The proof derives its elementary global digamma bound from those identities.
Fourier/Plancherel and the compact self-adjoint min-max principle are classical
background. All test functions, endpoint cancellations and kernel summations
are specified explicitly. No arithmetic zero-density or PNT theorem is imported.

For context, Suzuki, *Aspects of the screw function corresponding to the Riemann
zeta function*, arXiv:2206.03682, belongs to the established Weil/screw positivity
framework. Its abstract/publication record was consulted; no unquoted theorem
from it is required here. This packet makes no external novelty or priority claim.

## Boundaries

The cutoff theorem is a refutation of a proposed proof mechanism, not RH and not
a new counterexample to RH. It uses the literal positive von Mangoldt weights
only in finite sums. The full infinite signed interaction is not estimated.
The averaged-tail repair is a changed source and is separately labelled.
