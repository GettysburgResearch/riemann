# Post-review repository-wide salvage of the positive RH programme

Agent: `gpt56-pro-09-v`  
Date: 2026-08-14  
Live main inspected: `9c7538559d7f56c2914b39aed5a1fb3fbf7ce131`  
PR #202 head at start of review: `6de0ecba3c0bb0fb4eafd15e0369ff8ae0e4ca69`  
Scientific status: **independent review + PROPOSED corrected full architecture; RH is not claimed proved**

## Executive verdict

The independent review of the historical prolate proposal is accurate.  The old
`T-19807` is not a proof of RH and cannot be restored by merely strengthening
its constants:

1. the support translation cancels exactly in the polarized zero-side form, and
   the large-sieve theorem required a scaled support derivative that the proof
   did not provide;
2. the complete signed finite CCM space has a `d_6`-scale complement direction,
   so the asserted complete `d_8` gap is false;
3. independently, a hypothetical off-line Xi-cardinal quartet gives a fixed
   negative finite-Hardy direction, showing that complete finite ground
   selection of the Xi-like line is already RH-bearing.

The finite Hardy--prolate implication `T-14301` and its residual/coercivity
certificates survive.  They should be used as an independent Galerkin audit, not
as the primary conclusion mechanism.

After sweeping the live graph through PR #470, the strongest corrected full
proposal is a synthesis of two later fronts:

```text
source-owned native thinning / one-use capacity          PRs #468--#470
completed additive Clark/Jordan radial source             PRs #421, #425, #427
radial diffuse-versus-pure-point exclusion                PRs #430, #435
finite Hardy--prolate generator/zero audit                surviving PR #202 stack
```

The combined missing theorem is `SORKMD`: construct one source-owned
native-to-radial feature dictionary whose coefficientwise slack gives
intervalwise Loewner domination of the complete model kernel by the diffuse
arithmetic source.  If this is proved for one sequence `a_j->0`, the exact
radial spectral-type argument yields RH.  `T-19817` records the full conditional
composition.

## 1. Independent verdict on the review of `T-19807`

### 1.1 Support translation cancellation — review correct

The rejected argument used

\[
 \widehat T_{j,R}(s)
 =\sqrt{d_j(R)/R}\,
 e^{-isx_R}\Phi_{j,R}(s/R).
\]

The polarized Weil matrix contains

\[
 \overline{\widehat T_{j,R}(\overline s)}
 \widehat T_{k,R}(s).
\]

The factors `exp(+-isx_R)` cancel identically.  Therefore the quarter-power
bound on the isolated translation factor cannot be used as either a cost or a
reserve in the quadratic form.

More importantly, the parent support large sieve assumes

\[
 \|A_\gamma(R)\|+T\|\partial_RA_\gamma(R)\|\le B_T
 \qquad(T\le R\le2T).
\]

The old lemma supplied only an unscaled derivative estimate.  With the real
support oscillation left in the amplitude, the missing factor `T` destroys the
claimed vanishing mean square.  A valid repair would require a branchwise
holomorphic WKB/Airy expansion with every real phase extracted and
`R partial_R` control on the remaining amplitudes.  No such theorem was proved
in `T-19807`.

This is a fatal load-bearing error in hypothesis C and therefore in the support
selection step.

### 1.2 Complete `d_8` gap — review correct

The complete finite CCM space contains both Fourier-sign sectors:

```text
+ sector: modes 0,4,8,...
- sector: modes 2,6,10,...
```

Exact point and integral repairs combine `(0,4)` with `(2,6)` to produce a
source-admissible target at scale `d_4`.  A second exact repaired vector built
from `(2,6)` and `(4,8)` is asymptotically orthogonal to the target and has
first-alias energy `O(d_6)`.  Projecting it to the target complement preserves
that scale.

Thus the complete target-complement generalized eigenvalue is at most
`C d_6`, while `d_6/d_8->0`.  A fixed positive lower bound at scale `d_8`
cannot hold on the complete signed space.

The positive-sector `d_4/d_8` calculation is not refuted; the error was its
promotion to the complete signed space.

### 1.3 Off-line cardinal obstruction — accurate with stated dependencies

`R-19846` gives a stronger conceptual obstruction.  Under false RH, an off-line
quartet has an even cardinal combination with exact negative Weil value.  Fixed
Hardy-strip finite projections preserve a negative Rayleigh moat, whereas an
Xi-like global radical target has finite Weil value tending to zero.  Hence any
cofinal affine theorem forcing that target to be the complete finite ground
line already excludes the off-line cardinal.

The argument depends on the Xi-cardinal form-core and Hardy-form continuity
interfaces cited in `R-19846`; at that declared scope the logic is correct.  It
shows why better high-ordinate estimates alone cannot recover the historical
ground-selection theorem.

### 1.4 Correct lifecycle

```text
T-19807 as an RH proof                         REJECTED
L-19821 quarter-power support argument         REJECTED
complete d8 complement floor                   FALSE
T-14301 Hardy-prolate implication              RETAINED CONDITIONAL
L-14302/L-14303 finite residual certificates   RETAINED
L-19867/L-19868/L-19873 finite audit tools      RETAINED
complete Xi-line ground selection              RH-BEARING, not a producer lemma
```

## 2. Live route sweep

### 2.1 Prolate/CCM

The route still has exceptional value as a finite spectral laboratory:

- finite simple-even real-zero transfer and Hurwitz convergence;
- exact weighted residual, sector-gap and reciprocal-Hardy bounds;
- moving-Hardy target control including aliases and endpoints;
- source-generator intertwining controlling finite vertical zero defect.

It no longer has a valid unconditional complete-ground conclusion.  A generic
non-ground eigenline need not have a real-zero transform, and optimizing a
positive symmetrizer after seeing a finite matrix is tautological.

**Disposition:** validation layer, not the main RH consumer.

### 2.2 Completed arithmetic Julia / radial source-model route

The later source stack has closed much of the construction that was vague in
the August 12 salvage report.

- PR #400: safe Jordan first-chaos curvature and canonical model-space tangent
  reserve; amplitude embedding imported from Suzuki.
- PR #404: exact ordinary-prime tail-Hankel Julia dilation, gamma/pole covariant
  connection, completed Fisher/model-space colligation and compressed-delay
  semigroup.
- PR #421: logarithmic Clark coordinates linearize the safe prime cascade.
- PR #425: the prime source is an exact dyadic martingale of positive radial
  innovations.
- PR #427: eta, bridge and gamma factors form one coefficient-one positive
  arithmetic Julia cascade.
- PR #430: arithmetic radial source is diffuse; crossed-zero depth measure is
  pure point; interval-natural domination kills the latter.
- PR #435: local Kolmogorov systems glue automatically.  The former global
  `W_a` construction is reduced to one intervalwise Loewner inequality, `RKMD`.

This is presently the cleanest conclusion mechanism because it avoids finite
ground selection and uses a structural invariant—radial spectral type—that an
off-line zero cannot hide.

**Open theorem:** intervalwise completed arithmetic/model kernel domination.

### 2.3 Native-root / CFFP arithmetic route

PRs #468--#470 have sharply corrected the native arithmetic producer.

Surviving exact work includes:

```text
native-root normalization and rough-reservoir decompilation;
Euler shell and terminal stopped-leaf row/response algebra;
subcritical recursive coefficient mass <1/8;
exact leftmost Lorenz basis for the stopped-leaf LP;
large Y4-zero score-free triangular repair cone.
```

The raw current is not feasible.  PR #470 supplies an exact one-column Farkas
separator at `(X,p,q)=(136,67,2)` and an unbounded family of separators.  Adding
more nonnegative raw-current generators cannot repair the separated column.
The current must be thinned or replaced source-by-source.

The surviving theorem is `SONTR`: one atomwise source partition, one-use native
ordinary/detail/port capacity, a source-owned recursive packet of mass below
`1/8`, nonnegative reconstructed current, and controlled `Y4` slack.

**Disposition:** most concrete finite arithmetic producer; source ownership is
its central new lesson.

### 2.4 Complete-Bernstein / fractional-string route

PR #461 identifies the universal high-safe-axis fractional-string limit and an
exact beta-Hankel determinant.  Fixed and proposed growing orders become
positive far from the negative cut.  Exact delayed-witness examples prove that
arbitrarily many finite orders can pass before a weak off-line pair is detected.
The near-cut boundary layer remains `NCFSC`, open and RH-equivalent.

**Disposition:** powerful asymptotic diagnostic; no current near-cut closure.

### 2.5 Scalar/carry/Type-II routes

Weighted shell-tail stability, carry-resolvent stability, balanced Type-II
packing, prime-polygon/Haar and related scalar criteria have exact finite
algebra and useful refutations.  Their remaining cofinal estimates are already
shown to be RH-equivalent or to contain the complete pointwise arithmetic
burden.

**Disposition:** important arithmetic tests and possible producer technology,
but not presently a smaller conclusion theorem than `RKMD` or `SONTR`.

### 2.6 Brownian/theta and generic positive-operator routes

The positive theta supersymmetric bulk, Brownian two-copy identities, Gaussian
Fredholm criteria and various Hankel/Volterra factorizations are valuable exact
structures.  Repeated firewalls show that amplitude unitarity, reversible
Markov positivity, finite-order Hankel positivity, or one scalar Green
stationarity does not control the off-line inner factor.

**Disposition:** reserve/environment components for a source colligation, not a
standalone conclusion.

## 3. New synthesis: source ownership is the missing provenance for `RKMD`

The radial route and native-root route had been treated as separate endgames.
They solve complementary halves of one problem.

The radial route supplies:

```text
positive completed arithmetic source;
exact radial interval decomposition;
diffuse source spectral type;
critical/stable/hyperbolic model ledger;
local gluing and the zero-exclusion consumer.
```

The native route supplies:

```text
atomwise source ownership;
one-use ordinary/detail/shared-port capacity;
subcritical recursive mass;
finite correction ownership;
exact dual separators when an allocation is impossible.
```

The exact separator of PR #470 explains why a global positive arithmetic kernel
can coexist with an invalid physical/source allocation: total positivity does
not identify which source atom pays which model column.  This is the same
provenance issue exposed abstractly by the rotation countermodels on PRs #425
and #427.

Therefore the vague global source map `W_a` should be replaced by a
**source-owned common-column certificate**.

For every radial interval and finite polarized packet, use one common family of
feature columns and prove

\[
 \mathsf A_a(I)-\mathsf M_a(I)
 =\sum_\alpha s_{a,I,\alpha}v_{a,I,\alpha}v_{a,I,\alpha}^*,
 \qquad s_{a,I,\alpha}\ge0.
\]

The arithmetic coefficients must come from one `SONTR`-compatible source
partition; the model coefficients must retain critical, stable, hyperbolic and
auxiliary ownership.  Compatibility under interval refinement gives `RKMD`,
and PR #435 then constructs the module isometry automatically.

This is `SORKMD`, formalized in `T-19817`.

## 4. Corrected full proposal

The proposed full spine is:

```text
completed additive Clark/Jordan arithmetic source
+ eta/bridge/gamma coefficient-one Julia cascade
+ compressed delays and both Hardy orientations
+ SONTR atomwise thinning / one-use native capacity

-> construct common native-to-radial feature dictionary
-> prove coefficientwise nonnegative source/model slack on every rational interval
-> SORKMD / complete intervalwise Loewner domination
-> local Kolmogorov gluing gives L-infinity(dr)-module isometry
-> diffuse arithmetic source dominates pure-point hyperbolic depth measure
-> hyperbolic measure vanishes
-> Re(s)>1/2+a zero-free
-> repeat for a_j down to 0
-> RH.
```

This proposal has one mathematical conclusion theorem, not three competing
ones.  `SONTR` is its finite/source realization requirement; `RKMD` is its
operator form.

## 5. Prolate audit of the same source object

The source-owned radial map should also satisfy the generator covariance

\[
 A_aW_a-W_a\Lambda_a
 =|g_a\rangle\langle\eta_a|+R_a.
\]

A relative Hilbert--Schmidt estimate for `R_a` feeds `L-19873`, while
`L-19868` supplies the complete moving-Hardy target rate.  This gives a finite
CCM/prolate audit:

```text
source map correctly normalized
-> finite vertical defect tends to zero
-> finite transforms approach Xi in the Hardy strip.
```

It does not select the Xi target as the complete ground state and therefore is
immune to the `d_8` and off-line-cardinal refutations.

## 6. Exact missing packet

The smallest honest remaining package is:

1. **Native-to-radial source lock.**  Map every source-owned native atom to the
   corresponding additive Clark/Jordan radial innovation with coefficient one,
   including eta, bridge, gamma, orientation and delay channels.
2. **Coefficientwise model allocation.**  Express the complete model measure in
   the same columns and prove every source-minus-model coefficient is
   nonnegative.
3. **Refinement consistency.**  Prove countable additivity and compatibility for
   every rational radial interval and finite polarized packet.
4. **Finite producer.**  Establish `SONTR` on every arithmetic activation cell,
   including full triangular repair tails, provenance and `Y4` slack.
5. **Independent audit.**  Prove source-generator covariance with the relative
   error required by `L-19873`.

Items 1--3 are the mathematical `SORKMD` theorem.  Item 4 is the most concrete
proof-producing campaign suggested by the current arithmetic branch.  Item 5
is a validation layer and not logically required for the radial conclusion.

## SERIOUS RESOLUTION PATH

**YES — a serious corrected full proposal is present.  RH is not proved.**

The old prolate full proposal is rejected, but its best finite components can be
salvaged inside a stronger architecture.  The source-model route supplies the
clean conclusion, the native-root route supplies source ownership and exact
finite separators, and the prolate route supplies an independent spectral
audit.

The one decisive theorem is `SORKMD`: a source-owned intervalwise common-column
domination of the complete model kernel by the diffuse completed arithmetic
source.  Proving it for one explicit sequence `a_j->0` would complete RH.

No current PR proves that theorem, and this report does not claim otherwise.
