# Semantic implication registry — 2026-08-20

This registry is intentionally semantic rather than number-first. Numeric claim IDs in the repository have collided repeatedly; the role key below is the stable integration handle for this pass.

| semantic key | representative source | status | implications / incompatibilities |
|---|---|---|---|
| DET-NEG-MASS | PR #653 scalar negative-mass Landau theorem | proved | subpower logarithmic negative mass -> RH |
| DET-WAVELET | PRs #674/#675/#689 compact ordinary-Möbius wavelet | proved / RH-equivalent | subpower wavelet -> RH; RH -> corresponding critical L2 |
| PROD-FIRST-OWNER | PR #652 sequential native first-owner identity | proved | preserves literal Euler coefficients; replaces alpha-child promotion |
| PROD-LARGEST-PRIME | PR #688 L-100410 | proved | unique p owner + smooth sector negligible -> rough bilinear form |
| PROD-FINITE-SQUARE | PR #677 L-100020 | proved finite | p<=Z source factors become p^2 labels; corridor positivity |
| TRANS-BERNSTEIN | PR #676 L-100000 | proved through supercritical steps | positivity until unique sigma=1 wall |
| TRANS-ACTIVATION-FREE | PR #673 L-99971 | proved | positive quadratic envelope -> exact critical derivative, no activation atoms |
| TRANS-COMPACT-WAVELET | PR #674 | proved | ratio-eight compactification; positive factor-67 desmoothing |
| EQ-HARDY-GCD | PR #671 | RH-equivalent | useful as detector/target but supplies no independent root-free estimate |
| EQ-MIN-WAVELET | PRs #675/#689 | RH-equivalent | reframing allowed; must obtain estimate from independent structure |
| NO-POSITIVE-DESQUARE | PRs #681/#684 | refuted | finite squaring cannot be inverted positively after scalar collapse |
| NO-PRIORITY-FLUX | PR #673 | refuted | positive first-owner flux is power-sized |
| NO-QPET | PR #686 | refuted | corridor-inconsistent one-pole dominance |
| NO-SOURCEBLIND-L2 | PRs #660/#666 | refuted | labelled diagonal / generic Cauchy-Schwarz loses power-sized multiplicity |
| HYB-LP-SQUARE | this branch L-100600 | proved source identity / estimate open | largest-prime uniqueness + cofactor finite squaring |
| HYB-QUAD-WAVELET | this pass | under audit | activation-free downward variation -> compact wavelet via signed Abel kernel |
| HYB-LOCAL-SQUARE-VAR | PR #684 + PR #673 | partially proved | use finite squaring locally inside fixed critical variation ledger |

## Integration rule

An RH-equivalent statement may be used as a **target** or **detector** in a composite proof. It is not discarded merely because it is equivalent. What is forbidden is claiming progress from a tautological reformulation without an independently proved incoming edge.

## Highest-priority composite paths

### Matrix path A

`PROD-LARGEST-PRIME + PROD-FINITE-SQUARE -> HYB-LP-SQUARE -> DET-WAVELET -> RH`

Open edge: `HCFB100600`, source-level transfer from completed cofactors to the original rough owner bilinear without signed inverse.

### Matrix path B

`TRANS-ACTIVATION-FREE + TRANS-COMPACT-WAVELET -> HYB-QUAD-WAVELET -> DET-WAVELET -> RH`

Open edge: sign/variation of the exact Abel kernel connecting the quadratic downward-variation measure to the compact wavelet.

### Matrix path C

`TRANS-BERNSTEIN + PROD-FINITE-SQUARE -> HYB-LOCAL-SQUARE-VAR -> DET-NEG-MASS -> RH`

Open edge: large-prime short-collar one-sided bound after local small-prime squaring.

RH remains unproved.