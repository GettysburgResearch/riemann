# Reviewer C repair response to PR #749

Binding review:

```text
PR #749
9da1e250b647575418290407c6e30054322bb581
```

Repair target:

```text
PR #735
formal/030-xi-operator-qa
base repaired from 4863c31dd497ffe69ea400fe29275decf4cb5d29
```

RH remains unproved.

## P0 disposition

| Finding | Disposition |
|---|---|
| Arbitrary proposition labels | Removed. Replaced by concrete external publication, source-lock, actual-Xi, grouped C2, orbit, multiplicity, residual and tail/allocation structures. |
| External theorem/source lock | Exact height and theorem shape stated. Bibliographic/artifact record and normalized SHA-256 are locked independently of local claim SHAs. |
| Repeated-node PSD assumed | Removed. Positive squared-node equality gives node equality; duplicate rows/columns reduce to order-two PSD for all three repetition patterns. |
| Generic one-orbit payment | Replaced by exact reflected-orbit defect and cross formulas, reviewed epsilon and `9m/b^2` bound. |
| Global reserve not one-use | Replaced by nonnegative shares/tails, every-orbit payment, finite-prefix total `<=1`, exact leftover and one-use identity. |
| Canonical semantic overmapping | Repaired. Canonical C.tsv rows are source-specific; generic lemmas moved to `C_API.tsv`. |
| Conditional comparator too weak | Replaced by one exact shared full-packet `ChallengeStatement`, including repeated nodes and concrete inputs. |
| Manual QA booleans | Removed from the QA schema. Evidence is generated from Lean declarations, exact comparator statements, canonical/source-lock joins and registry-generated axiom audits. |

## P1 disposition

The finite algebra and firewalls accepted by PR #749 are preserved. The
source-specific reserve layer is added without changing the accepted determinant,
LDL, PSD/PD, Hermite, Q4 or firewall mathematics.

The full grouped actual-Xi C2 theorem, exact reciprocal-square analytic tail,
source-faithful paid-prefix componentwise local C2 convergence, and source-specific scalar
curvature bridges remain explicit hypotheses. They are
not axioms and are not classified as unconditionally proved.

## Exact external propositions introduced

- `PublishedVerifiedHeightTheorem`
- `ExternalSourceLock` / `SourceLockExact`
- `CriticalOrbit`
- `ReflectedOffLineOrbit`
- `SelectedCriticalReserve`
- `GroupedActualXiC2Expansion`
- `CriticalMultiplicityResidual`
- `OneOrbitPaid`
- `ActualXiReserveAllocation`
- `RegroupedActualXiC2Approximation`
- `ActualXiOrderThreeInputs`

## Repeated-node status

```text
12 duplicate: PROVED BY CONGRUENCE -> ORDER TWO
13 duplicate: PROVED BY CONGRUENCE -> ORDER TWO
23 duplicate: PROVED BY CONGRUENCE -> ORDER TWO
wholesale IsPSD3 premise: REMOVED
```

## Reserve-allocation status

```text
source-specific cross formula: PROVED IN LEAN SOURCE
source-specific defect formula: PROVED IN LEAN SOURCE
reviewed epsilon: EXPLICIT
9m/b^2 bound: PROVED FROM EXPLICIT DOMAIN
finite-prefix one-use allocation: PROVED FROM EXPLICIT TAIL/BUDGET INPUTS
infinite analytic tail theorem: EXPLICIT UNPROVED INPUT
```

## Comparator status

```text
RiemannComparatorChallenge.XiPickOrderThreeConditional: exact shared headline through sizes one, two, and three; one placeholder
RiemannComparatorSolution.XiPickOrderThreeConditional: same shared type, sorry-free
PSD only: YES
repeated nodes: INCLUDED
order four: ABSENT
PD strengthening: ABSENT
```

## Build status

```text
local publication environment: Lean/Lake unavailable
static Python/shell checks: run in packet build
full exact-head Lean suite: PENDING INDEPENDENT LAPTOP CODEX
```

The exact command is `bash formal/scripts/run_c_repair_validation.sh`.

## Acceptance request

After the repaired branch is published and the exact-head suite passes, Reviewer
B is requested to append a short acceptance addendum to PR #749 covering the P0
repairs above.
