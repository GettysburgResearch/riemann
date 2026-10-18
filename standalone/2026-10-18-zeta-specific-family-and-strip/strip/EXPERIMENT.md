# What the new field freedom did at the first unmatched order

Status: **EMPIRICAL, ordinary 90-digit Decimal continuation. No certified root
or order-22 moment theorem is claimed.** This experiment is separate from the
independently reviewed statements in PROOF.md and the directed finite example
in certificate.json.

The experiment retuned the ten active coordinates of the proposed T20D model
while changing only specified symmetric fields or a symmetric local graph
replacement. All 305 spins, or all 307 spins in the clone experiment, enter the
complete moment formula. It measured the first unmatched normalized cumulant,

\[
 \Delta_{22}=\kappa_{22}(Y)/\kappa_{22}(\varepsilon)
             -\kappa_{22}(T/\sqrt v)/\kappa_{22}(\varepsilon),
\]

where epsilon is a fair sign. The target ratio is approximately
`4.9692694891940005984e-7`. At the retuned zero-field starting point the residual
is approximately `+1.5009965854252348e-16`. A small residual does not imply exact
equality, feasibility, or an existence theorem.

## Results

| Perturbation | Largest completed parameter | Physical field/weight cap | Final Delta22 | Relative reduction in its positive initial residual |
|---|---:|---:|---:|---:|
| Opposite fields on two identical leaves | tanh(h)=0.0015 | 0.3293269718 | +1.5009965899971886e-16 | -0.0000003046%; moved away |
| Opposite proportional fields on two identical dimers | standardized lambda=0.0716 | 0.3330773516 | +1.5009719337859867e-16 | 0.0016423515% |
| Two replicas of the dominant dimer, opposite fields, finite cross-couplings | delta=0.00001, lambda=0.0716 | 0.3330773516 | +1.5009950881356499e-16 | 0.0000997530% |

All completed finite-coupling points stayed within the positive weight and
ferromagnetic parameter domain. Their computed physical zero-field reference
variances remained below 0.046211. At each completed point the first ten
cumulant-ratio equations settled to the ordinary numerical precision used by
the Newton iterations. Those residuals are retained in the JSON; they are not
directed root certificates.

No sign crossing occurred. For the clone continuation, the prescribed
ten-coordinate positive-domain line search failed at delta=0.0001. This is a
failure of this continuation chart and implementation; it does **not** prove
that no legal model exists there. The short stopping rule was four clone
parameters `0, 0.000001, 0.00001, 0.0001`, stopping on the first failure.

The result is a concrete limit on the easiest continuations of T20D. Fields on
its repeated small components have very little influence on the first
unmatched high cumulant after the lower ten equations are restored. The larger
clone changed the graph legitimately but did not close that equation in the
tested local chart. An all-order construction in Theorem S4 remains open.

## Complete model formulas

The inherited graph, multiplicities, parameters and active coordinates are
those of PR #994 at `c93ca65a510b6acaf167f929b9bf7e67d742b05a`. Let the hub sign
be H, and its original edge correlation be eta=10^-10.

### Two leaves

On two of the 256 equal-weight leaves set fields +h,-h and leave every other
field zero. Put r=tanh(h). Conditional on H=+1, their means become

\[
 m_+=\frac{\eta+r}{1+\eta r},\qquad
 m_-=\frac{\eta-r}{1-\eta r}.
\]

The product of their conditional normalization factors is
`(1+eta r)(1-eta r)=1-eta^2 r^2`, independent of the hub sign. The hub remains
fair. All other conditional blocks are unchanged. Summing conditional
cumulants and then averaging the hub sign gives the complete finite law.

### Two repeated dimers

Type 1 occurs ten times. On one copy put fields +lambda*w_i at its two
vertices, and on another put fields -lambda*w_i; all other fields are zero.
The permutation exchanging the two copies preserves the graph and weights.

Conditional on H=+1, an unperturbed dimer has support `A,B,-B,-A`, with masses
`p(1+eta)/2, (1-p)(1+eta)/2, (1-p)(1-eta)/2, p(1-eta)/2`. For sign choice
+lambda or -lambda, multiply each of these four masses by `exp(lambda*x)` and
normalize. The paired normalizers are again independent of the hub sign by
spin reversal and exchange of the two copies. No individual state or
cross-cumulant is discarded.

The physical cap equals `lambda/sqrt(v)`. This is why the standardized endpoint
0.0716 gives the original-xi cap 0.3330773516, below 1/3.

### Clones of the dominant dimer

Replace the unique type-2 dimer by two replicas, giving each replica half of
each original observable weight. The within-replica couplings and the hub
couplings are each half of the original coupling **in J**, not half of its
tanh. Join the two root replicas to one another, and the two partner replicas
to one another, with cross-couplings having

\[
 \tanh J_{\rm clone}=1-\delta.
\]

Give every observed vertex in one replica the field +lambda times its new
weight, and the matching vertex in the other replica the opposite field. The
replica exchange is the required symmetry involution. This makes a graph with
307 vertices, 306 observed spins, one zero-weight hub and 308 edges; every edge
is positive and finite when 0<delta<1.

Conditional on H=+1, all 16 configurations of these four spins are summed with
their complete Gibbs weights. At delta=0 only equal replicas survive, their
half-couplings recombine, the fields cancel, and the original dimer is recovered.
That starting point is a limiting locked model with infinite cross-couplings,
not itself a new finite-coupling example. At delta>0 all configurations are
retained and every cross-coupling is finite.

## Source arithmetic and numerical limits

`explore_field22.py` authenticates the two frozen primitive/source Git blobs,
the inherited `tree_core.py` and `parameters20.json`, and the SHA256 of the fresh
`theta_source_replay.json`. For the extra order-22 moment it reuses the same
320-bit integer interval primitive, the same 98 cells, and the same six theta
indices. It substitutes j=22 into the explicit remainder formulas in the
inherited PROOF20.md, including the Taylor remainder, all six time tails, and
the entire omitted-index tail. The Taylor estimate remains valid because it
only uses `t^j<=2^j` on the finite cells; the time-tail binomial formula and
omitted-index estimate apply to each nonnegative integer j. The enclosed raw
order-22 moment and normalized cumulant ratio are retained in the JSON.

The source midpoint is then used in ordinary Decimal Newton iterations with
analytic forward derivatives. Neither the Newton steps nor the graph parameter
boxes are directed. The experiment therefore remains empirical even though
its extra target is supplied by an outward primitive formula. It does not
extend the independent mathematical review of the theorem/checker files to a
new degree-22 certificate.

`explore_clone22.py` consumes the recorded order-22 target from the dimer run
and records that input JSON's SHA256. Its finite Gibbs sums and derivatives are
also ordinary Decimal calculations.

## Replay

From this directory in the stacked repository checkout:

```bash
python check_strip.py
python explore_field22.py --mode leaf
python explore_field22.py --mode dimer
python explore_clone22.py
```

Each command accepts `--source /path/to/exact/theta` when the inherited source
is in another location. Its default is the sibling packet
`../../2026-10-18-theta20-and-native-cancellation/theta/`.

The full retained outputs are `field22_leaf_exploration.json`,
`field22_dimer_exploration.json`, and `field22_clone_exploration.json`.
`experiment_summary.json` records concise endpoints, provenance hashes and the
failed clone step. No failed continuation is labeled an infeasibility theorem.
