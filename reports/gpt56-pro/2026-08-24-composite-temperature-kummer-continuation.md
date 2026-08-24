# Composite-conductor and temperature–Kummer continuation

Date: 2026-08-24  
Execution PR: #751  
Programme issues: #743, #736, #737  
Parent audited: PR #719 at `ae61d988568fdc3e7d790a42b5c340c29a6ea3e5`  
RH status: **unproved**

## 1. Publication audit

The remote branch was checked before continuation. The previously reported
composite-conductor packet had not landed. In particular, the claimed scalar
leverage

\[
(1-\varphi(q)/q)4^{\omega(q)}
\]

was not present in the tree and is not retained as mathematics. `R-106040`
withdraws it and replaces it by the exact tensor-local normalization.

## 2. Correct composite frame

For odd squarefree `q`, the source uses the tensor of nonzero local square
phases. On one local quadratic-class sector,

\[
\|F_0\|^2
\le
\prod_{p\mid q}\frac{p-1}{p+1}
\sum_{h_p\ne0}\|F_{\mathbf h}\|^2.
\]

The reciprocal principal-root-fibre weight is

\[
\prod_{p\mid q}\frac{p+1}{p-1}.
\]

There are `2^omega(q)` local source classes. Their recombination cost is a
sector cost, not amplifier leverage. Composite principal Euler completion is
coefficient-exact when performed on the full source.

## 3. Temperature and Kummer fibres

For every unramified character,

\[
\sigma_{t,\chi}*\sigma_{1-t,\chi}
=E_\chi*S_{\chi^2}.
\]

Thus the owner-conductor square map `chi -> chi^2` is built directly into the
flat complementary-temperature connection of PR #719.

The roots `chi` and `chi*kappa` have the same squared completion. Their
symmetric and antisymmetric combinations are exactly the two source projectors

\[
(1\pm\kappa)/2.
\]

On `P a^2`, these projectors see only `kappa(P)`. The quadratic root fibre is
therefore the pair of owner-squareclass Kummer charts.

The midpoint remains the unique energy-minimizing temperature in every unitary
character channel. A nonprincipal square-lattice inverse is not positive: its
coefficient at `n^2` is `eta(n)/n`. Positive inversion is available only in the
principal channel; the Kummer family frame must be formed first.

## 4. Tangent current

At the midpoint,

\[
\dot\Gamma_{1/2,\chi}
=2E_\chi*S_{\chi^2}*\Lambda_\chi.
\]

The Hadamard combinations of one quadratic root fibre split this tangent into
the two quadratic source classes. After the principal positive inverse, their
first-chaos pieces are

\[
2P_+(\beta*\Pi_1),
\qquad
2P_-(\beta*\Pi_1),
\]

and their sum is the complete native prime owner/transfer current. Hence the
parent temperature-zero route and the L-family owner-dispersion route act on
one generator.

## 5. Two phases are genuinely conjunctive

For one collision-line packet over `F_Q`, one linear phase has energy

\[
QD-\|S\|^2
\]

and can lose `Q-1`.

With two same-occurrence nonzero phases,

\[
\sum_{\alpha,\beta\ne0}\|F_{\alpha,\beta}\|^2
=Q(Q-2)D+\|S\|^2,
\]

and

\[
\left\|\sum_{\alpha,\beta\ne0}F_{\alpha,\beta}\right\|^2
\le
\frac{Q-1}{Q^2-Q-1}
\sum_{\alpha,\beta\ne0}\|F_{\alpha,\beta}\|^2.
\]

This is a sharp `1/Q`-scale contraction. After the character collision
`c=+/-tau d`, it reduces the remaining line problem to aggregation within one
root residue.

## 6. Current open gates

```text
CCSOCM106040:
  composite owner-conductor coherent assembly;

TKCA106050:
  collective midpoint temperature/Kummer assembly;

CROP106060:
  same-root-residue occupancy after the two-phase line frame.
```

Each is sufficient for an existing conclusion route when proved on its exact
source functor. None is proved.

## 7. Exact replays added

```text
PASS_X_106040_COMPOSITE_KUMMER_TENSOR_FRAME
checks=4015
sha256=5c5dfbf952abdb3f790bbea95ea9a036c7d45b74caee5e9d38292e4717ab95cb

PASS_X_106050_TEMPERATURE_KUMMER_FIBRE
checks=852
sha256=c82c642f9b91805471219edad01a58a5c34d9fceaa8d2e7cf56f7211926857bb

PASS_X_106052_TEMPERATURE_TANGENT_KUMMER_CHARTS
checks=36912
sha256=04ae5cfd6495a62bf899618f0ccdae99041f1467c717fb7a974974e533df50e2

PASS_X_106060_TWO_PHASE_COLLISION_LINE_FRAME
checks=6378
sha256=9bf57d9245f9a445a77b77d973255a183a65b425e940ccca206e1657158cd1de
```

They authenticate finite exact algebra only.

```text
new exact checks in this continuation: 48157
Riemann Hypothesis:                     UNPROVED
```
