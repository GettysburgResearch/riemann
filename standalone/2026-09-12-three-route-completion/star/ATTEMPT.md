# Attempt to cross the new star's sixteenth-moment target

Status: **ordinary numerical exploration; no new root certificate**.
Scope: the 96-spin model of PR867, first with structured couplings and then
with all nineteen grouped weights/biases free. These are finite attempts,
not an infeasibility theorem or an all-order argument.

PR867 appeared during this research pass. Its frozen head
`4c7898432546814812b2be8c72fc199e294354d1` supplies a proposed exact degree-14
star with standardized degree-16 excess about -0.11438319548843916. The
degree-14 model of PR863 has the opposite sign. Their mixture is not assumed
to be a ferromagnet, and no continuous lower-moment-fiber connection is known.

The code uses the actual finite-star identity

    X=epsilon (b+sum_i a_i tau_i),
    E tau_i=m_i,  m_i=tanh(J_i),  J_i>=0,

with conditional signs independent and epsilon fair. Every graph state is
encoded by the exact polynomial cumulant/moment recurrence; no configuration
tail is dropped. Floating evaluation and optimization are a separate issue:
all the searches below are **non-directed**.

The starting rational weights and group counts are read from PR867's
parameters.json. Scouting targets are midpoints of the standardized cumulant
ratio intervals in PR863 at `0640c9c59be0bf20c18258460a7517fb09728e82`,
`standalone/2026-09-12-astra-interacting-cluster-realization/result.json`.
The initial lower-moment residual and degree-16 error reproduce the expected
cross-source normalization. This is not a fresh primitive theta integration.

## What was actually attempted

* Keep the seven designated active weights and vary the rule m_i=k a_i.
  Decreasing k from .01 to zero changes the degree-16 excess from about
  -.1143832 to -.1119262. Increasing k to .015 makes it about -.1156070;
  the selected-coordinate solver then stalls at .02. No crossing occurs
  in the computed points. See scout-down.json and scout-up.json.
* Independently release the bias of one leaf group, m_j=k a_j+tau. Of nine
  initial compensated derivatives, group7 (24 leaves) has the favorable
  sign: about +.47847264. At tau=.002 the excess is still -.1134365;
  the fixed-seven-coordinate search stalls at .005. See bias-directions.json
  and bias-path-7.json. These signs are scouting values, separate from the
  rigorously certified dimer-graft signs in ../ferromagnetic/.
* Release all ten weights on that same group-bias path. The computed excess
  is -.1105474 at tau=.001, reverses to -.1114103 at .002, and the search
  stalls at .005. See bias-path-7-all.json. A failed chosen continuation
  is not a proof that the fiber ends there.
* Release all ten observable weights and all nine independent group biases.
  A bounded nineteen-variable SciPy search, using 65-decimal mpmath forward
  derivatives, ran its complete 600-evaluation budget. The maximum relative
  residual among eight normalized cumulant equations remained about
  4.3660e-7. See full-scout-result.json. These approximate values do not keep
  all lower moments exactly equal, so they are not a new realization.
* Starting at that point, two 65-decimal minimum-norm Newton searches each
  ran fifty iterations, with unit and relative parameter scaling. The last
  recorded maximum residuals are about 4.3660e-7 and 4.0917e-7. Neither
  reached the requested numerical tolerance; neither is certified.
  See refine-result.json. The record retains every iteration residual.

All weights must stay positive and all biases in [0,1); these constraints
were included in the searches. No negative coupling or unphysical signed
mixture is counted as progress. Numerical solver failure supplies no lower
bound on the best attainable residual and no global conclusion about stars.

## Reproduction

The optional scouts require mpmath; full_scout.py also requires NumPy and
SciPy. They do not enter the accepting standard-library checks. This run used
Python 3.12, mpmath 1.3.0, NumPy 2.5.1 and SciPy 1.18.0; the saved results
remain ordinary numerical data, regardless of decimal precision.

The scripts read the frozen Git objects. If absent in a fresh checkout,
fetch the PRs and check that the objects above exist; later PR heads may
differ from these frozen versions. Run from this directory:

    python -B scout.py --direction down
    python -B scout.py --direction up
    python -B bias_scout.py
    python -B bias_scout.py --owner 7
    python -B bias_scout.py --owner 7 --release-all
    python -B full_scout.py
    python -B refine.py

An exact next-moment root and a target-containing continuation remain open.
These attempts are retained so the same failed coordinates and local search
are not mistaken for an untried completion step.
