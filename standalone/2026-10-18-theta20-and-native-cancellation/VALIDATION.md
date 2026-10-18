# Executed verification and its exact scope

The complete packet is authenticated by `MANIFEST.json`. It records every
payload's relative path, byte length, SHA-256 and Git blob identity; the
manifest itself is included in the final publication inventory. No generated
Python cache is part of the payload. The component authors' original
accepting receipts are included and reproduced by the final assembled replay.

## Complete replay

Run `python verify_packet.py --replay` from the packet directory. Python 3.12
and its standard library are sufficient. All runtime predicates raise explicit
exceptions and remain active in optimized Python. The runner checks the
complete inventory before and after execution and rejects any payload change.

| Component | What is actually reconstructed | Ordinary/optimized comparison | Executed optimized corruptions |
|---|---|---|---:|
| Native | 27 complete prefixes, every reciprocal crossing through 63, all old products and denominators, and all 30,602 strict square-step cells; exact rational/formal-log low/paid-core/rough-core reconstruction | Reports byte-identical; 917,056 explicit guards including repeated setup checks | 9 |
| Critical | Full coefficient/inverse convolution through 256, complete local prime-power and fixed primitive-ratio fixtures, a directed 512-term sign calculation with the whole tail; separately labelled finite binary64 Gaussian QA | Reports byte-identical; 2,573 explicit predicates including repeated primitive guards | 3 |
| Theta | Original infinite source moments through 20, six explicit indices, 98 degree-120 cells and all three tails; exact ten-coordinate center inverse on both sides; whole-box contraction and all graph inequalities; complete finite assemblies | Both accepting scripts reproduce identical receipts and stdout in both modes | 4 |
| Independent theta map | Direct formal generating product, logarithm, product differentiation and reciprocal for all 305 vertices; 21 raw moments, ten cumulants and 100 Jacobian entries at the rational center | Exact Fraction reports byte-identical | 2 |
| Independent divisibility constant | All ratios 2--4096, exact beta coefficients, rational convex quadrature logarithms, positive-series exponentials and the complete infinite tail | Directed 100-bit reports byte-identical | 0 |

There are **18 separately executed optimized corrupted subprocesses** in
the assembled replay. Every corruption must return nonzero at its declared
mathematical or coverage gate; a stored Boolean list does not replace those
executions. The large native predicate count measures repeated exact guards
over complete finite data, not a count of independent analytic theorems.

Component runners own disjoint directories and may run concurrently. Their
dependent ordinary, optimized and negative-control stages remain sequential.
The top-level runner awaits and checks every component and verifies that all
manifested bytes still agree afterwards.

## Exact finite certificate identities

- Theta full-source certificate:
  `0cf3307c9493dc6b6c813e2aa0b18a6e1a637ab89ce6f3ffaf5719f161ddcc0c`.
- Native complete finite report:
  `0da354dbc2a4ddf5a30169c0619584698f9c7b87e614ae2486b843c271a616fc`.
- Critical finite report:
  `8a314267209f9fe2b62dd6035ef2ff2dbb7ebad92bdf257fceda6dfa0e30628c`.
- Independently implemented theta map/Jacobian report:
  `a1f1204686adccd12ace4ed93b0f73d202eb775d810280999c85226de12dd93d`.
- Independently implemented infinite divisibility-constant report:
  `d5514c2c9a094f8b6517bc176427a7b4c7b1c314c7f853a14ddee0c63581c83a`.

The independent constant enclosure proves -9/5<L_div<-17/10. Its decimal
display is approximately (-1.7715054494689935,-1.7430583147069783); only exact
integer/rational endpoints decide acceptance. Its different transcendental
primitives provide a second implementation of this constant, not a second
implementation of the theta source backend.

The author's optional Decimal center producer also reconstructed its source
afresh and reproduced the exact parameter file byte for byte. Its separate
producer receipt is retained. The final accepting root proof does not depend
on rerunning or trusting this nondirected producer, its seed, or its search
history; the assembled replay therefore does not require that optional step.

## Mathematical review versus executable coverage

The separately authored reviews in `reviews/` reconstruct the analytic
arguments and bind them to exact proof identities. They check the genuine
infinite points: full-source bounds, summable tails, norm domains, all-prefix
growth, the sparse sequence consumer, uniformity in the masks, and legal
limit exchanges. Their precise scope appears in [REVIEW.md](REVIEW.md).

The native finite checker does not prove its infinite frequency estimate,
PNT balance limit, arbitrary-mask norm inequality, Landau cofinality or the
#848 growth theorem. The critical checker does not prove Tao's theorem,
fixed-field contour bounds, or the infinite arithmetic asymptotics. Those
claims are supported by their written proofs and identified classical
inputs. The finite binary64 Gaussian integrations are normalization QA,
with finite integration windows; they are not directed integral certificates.

The theta computation does prove a finite root assertion when combined with
the written interval/tail/Banach proof. It does not identify the complete
theta characteristic function with the constructed spin law. No order above
20, cofinal construction, critical upper estimate or RH proof is claimed.

The reviews are separate work within one AI session. No independent human
referee, Lean build, transitive formal axiom audit, repository-wide validation,
actual zeta zero computation, remote CI, or integrated mathematical approval
is represented as completed by this packet.
