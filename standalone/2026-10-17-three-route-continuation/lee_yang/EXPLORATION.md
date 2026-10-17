# Exploratory search record and next experiment

Status: **nondirected numerical reconnaissance except for the two separately
certified theorems in PROOF.md.** A stalled optimizer is not a no-go theorem.

The target throughout was the original standardized theta law, with all
odd moments zero. Source moments through degree 18 were first regenerated
using the complete PR #886 primitive. The final certificates instead use
the tighter six-index full-source replay in `theta_source.py`; the
arithmetic backend is unchanged.

## Searches actually run

| Architecture and parameter freedom | Observed outcome | Permitted inference |
|---|---|---|
| The 96-spin heterogeneous star of PR #867, freeing all leaf biases as well as weights | Least-squares searches approached bias boundaries; no degree-18 root was obtained | Those runs did not produce a candidate |
| A 281-spin hidden-hub tree joining every D16 component, with common weight-adapted hub bias | Fixed-coordinate and full-coordinate searches did not reach degree 18 | No architecture obstruction follows |
| The same tree, with hub connections to the two largest dimers weighted more heavily; exact lower-16 projection in 75-digit Decimal arithmetic | The 18th-moment defect fell from about 0.169578 to about 0.090800, then progress became very small near colliding amplitude groups | A useful search direction was identified; this continuation itself was not directed or certified |
| Free the five internal dimer correlations, keeping the complete tree and all positive couplings | Lower-16 projection reached a candidate with next-moment defect about 0.0348337; further projection encountered another coalescence bottleneck | The selected candidate was subsequently certified as T16C; the continuation and bottleneck are numerical observations |
| Free additional individual hub biases | No degree-18 root was obtained in the subsequent local runs | No global nonexistence claim |
| Add a sixth independent dimer to the D16 power-sum model, initialize its squared amplitude at 0.005, 0.02, 0.05, 0.1, 0.15, and 0.25 | Six positive least-squares runs, each capped at 6000 evaluations, left maximum relative cumulant residuals between roughly 4.5e-9 and 1.4e-8; subsequent 85-digit corrections did not find a root | These are unfinished fits, not certified realizations and not proofs against adding components |

All optimization statements above used nondirected NumPy/SciPy or Decimal
arithmetic. Matching residuals were never substituted for theta moment
equalities. The publication packet retains the exact accepted centers,
the complete polynomial moment map, and a runnable edge-response experiment;
exploratory iteration histories are not load-bearing proof inputs.

## A reproducible next-moment experiment

`python3 certify_edge.py --check edge_certificate.json` reconstructs the
actual D16 source root and computes the compensated response of its 18th
moment to an edge joining two dimer roots. The derivative is strictly
between -0.785 and -0.784. The formula includes the weight compensation
needed to preserve all lower theta moments; it is not an uncompensated
Gibbs correlation derivative.

This experiment gives a source-specific design signal: correlations
between already interacting components can move the next moment downward.
The single connected tree in T16C demonstrates a finite positive-coupling
realization with a substantially smaller discrepancy. Neither result gives
a continuation interval reaching zero.

The next architecture experiment should add a genuinely new correlated
component or a new independent response direction before an amplitude
collision. Success means a complete degree-18 root whose positive graph
parameters have an outward-certified box. A full-rank numerical Jacobian
or smaller residual is insufficient. Failure should be recorded as a
failure of the stated search, unless a rigorous separating inequality is
actually proved.
