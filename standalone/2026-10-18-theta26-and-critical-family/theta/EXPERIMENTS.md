# Completed theta experiments and the change of construction

The numerical work in this note is **exploratory**. Only the separately
directed endpoint certificates establish exact finite moment matching.
Failure of a chosen chart or optimization is not a mathematical impossibility
result for its model class.

## 1. Broad interacting graph searches

The initial experiments retained the complete proposed earlier coupled-dimer
Ising model and opened all 46 effective old coordinates. Both signs of the
auxiliary dimer difference coordinate were allowed, with physical positivity
enforced by `A>|B|`. Several QR-selected square charts and full-coordinate
Newton directions were tried. None produced an order-22 root. Some directions
stalled; others approached a domain face. `graph_experiments.json` retains
their selected complete terminal parameter vectors, target residuals, and
original record hashes.

A new positive edge was then added between block roots 3 and 8. Its exact
configuration formula preserves the complete graph and its correlations; it
is not an independent factor approximation. Retuning all 46 old coordinates
while increasing the new edge correlation t from zero through 0.5 gave the
best observed order-22 residual near

\[
 t=0.08399952392578125,\qquad
 R_{22}\approx 8.91780745\,10^{-17},
\]

down from the starting `R_22≈1.50099659e-16`. It remained positive and later
increased. The residual is the standardized 22nd cumulant divided by the
22nd cumulant of a fair sign, minus the corresponding theta target.

A further 100-step predictor-corrector optimization held that edge fixed,
moved all old coordinates, and rebalanced the first 20 moments after every
predictor. Its final residual was

\[
 R_{22}\approx 3.56137325648\,10^{-17},
\]

with an ordinary-Decimal relative error of approximately `1.4071e-114` in the
first 20 normalized cumulant coordinates. This improved the starting mismatch
by about 76 percent but did not reach zero. The stopping rule was the stated
100 iterations. The complete final vector is preserved in
`graph_experiments.json`; `best_cycle22_seed.json` is the earlier seed for
replaying the fixed-edge optimization.

The complete evaluators are `search_full.py`, `continue_cycle.py`,
`optimize_cycle_manifold.py`, and `extension/explore_added_edge.py`. The
extension note also records independently checked vertex-splitting and
triangle formulas. These graph experiments motivated a structural change
instead of further reliance on small deformations of the same graph.

## 2. Direct Gaussian-polynomial models

The new class

\[
       e^{-az^2}\prod_j(1-b_jz^2)
\]

has explicit real zero locations and a simple entire bound when
`a>=0`, `b_j>0`, and `a+sum b_j=1/2`. Exact theta matching becomes a positive
power-sum system. It needs no inverse Fourier density positivity because the
zero-exclusion consumer concerns holomorphic functions.

The chosen direct fits use 64 factors at order 22 and 128 at orders 24 and 26.
All three searches settled, and their exact rational neighborhoods passed
the complete directed checker. Smaller tested node counts and rougher initial
guesses sometimes stalled; those outcomes do not give lower bounds on the
necessary factor count. Public numerical zero entries were useful optimizer
seeds, but neither the source construction nor the existence checker reads
or trusts them.

`gaussian_candidates.json` keeps the chosen three complete parameter vectors,
targets, and all their Newton/damping histories. The retained producer
reproduces those numerical records and their rational certification inputs.
Large optional inverse-density coefficient lists are omitted: their numerical
positivity diagnostics are not part of any theorem in this packet.

## 3. An incremental construction actually reaches the next two orders

The moving-root flow appends an integer cloud of equal new positive nodes,
retunes old nodes to preserve earlier powers, and has an exact formula for
the change of the next power. Small clouds initially approached anchor
collisions before reaching the target. At the 64-factor order-22 start,
one new root reduced the target deficit by about 11.4 percent and four new
roots by about 43.3 percent in the tested switching runs.

Larger clouds succeeded. A cloud of 20 new roots, with 35 changes of active
anchor set, reached an 84-factor order-24 candidate. Starting from that
numerical endpoint, another cloud of 20, with 20 anchor changes, reached a
104-factor order-26 candidate. Both endpoints then passed separate directed
full-cube certificates. At each certified endpoint the newest 20 nodes remain
identical and fixed, while only old nodes vary in the certificate cube.

The flow is an empirical two-step chain; the separate exact endpoint solutions
are not asserted to lie on the recorded numerical paths. The distinction
matters because an all-order construction would have to control every
intervening chart, collision, and target gap. The exact root-flow theorem
gives explicit local conditions and derivative identities, but those
conditions have not been proved cofinally for the theta target.

The curated candidate files in `extension/` retain the successful complete
endpoint vectors and the provenance of their preceding inputs. Larger-cloud
alternatives are numerical candidates only unless a directed certificate is
explicitly provided for them.

## 4. The analytic consumer became substantially less restrictive

The first compactness argument used a nonnegative Gaussian reserve. The
canonical-factor inequality removes that restriction for real positive
nodes: the fourth-order power sum alone supplies a uniform quartic entire
bound. Controlled complex-pair paths have a related continuous bound, proved
in the extension note.

The stronger weighted theorem removes unit multiplicity as well. Fractional
factors are holomorphic and nonzero on each open half-plane, and a direct
imaginary-axis remainder identifies the limit without assuming a common
Taylor disk. Thus a cofinal positive weighted moment construction would
suffice. The theorem does not supply the all-order positive moment measures.

These changes explain the current research emphasis: the finite solver now
has verified order-26 examples and a successful incremental mechanism, while
the infinite consumer asks for a weaker positive moment construction than
the original probability-model program required.
