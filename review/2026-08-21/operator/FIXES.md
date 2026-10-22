# Reviewer B fixes and non-minor dispositions

Review freeze: `gfreund123/riemann@677203992eb0168920365ee45ae9db76bfa97dcf`  
Branch: `review/2026-08-21/operator-heat-q4`  
Scientific status: **RH remains unproved.**

This file distinguishes local repairs that preserve a mathematical object from
changes that alter the source, quantifiers, half-plane, matrix order, or
conclusion-facing theorem.

## Local repairs accepted as `VERIFIED_WITH_FIXES`

### F-B-001 — PR #446 retained replay is syntactically corrupt

At exact head `880d14cb4bcbf542ec199137d60c58d9a8fd723d`, the Git blob

```text
experiments/X-92100-critical-reserve-allocation/verify.py
5020ebd96949d3942866471b27eadbc618c55b4d
```

contains malformed expressions, including a corrupted `qpp` line and `U+*4`.
It cannot authenticate the advertised PASS verdict.

The theorem is not rejected for this artifact defect. The review replay
independently reconstructs, with exact rational arithmetic:

* the three-node determinant factorization;
* reciprocal-concavity closure under positive sums;
* the one-orbit cross-curvature identity;
* nonnegativity after the declared reserve share;
* the global numerical budget bound
  `1.7836772651...e-10 < 1.8e-10`.

**Required repair:** replace the corrupt script with a clean deterministic
replay and retain a fresh result/hash. Do not claim the old PASS was rerun.

### F-B-002 — PR #446/#460 external verified-height source lock

The finite-height zero verification is a legal frozen external input, not a
local computation and not a proof of RH. The canonical source lock must identify
the correct publication metadata, distinguish “on the critical line” from
“simple,” and state exactly which tail/local-count estimates are imported.

**Required repair:** correct the bibliographic record and make every use of
height, simplicity, multiplicity, and local zero count explicit. The heavy
zero-verification campaign was not rerun.

### F-B-003 — PR #408 strict Julia absorption margin

The displayed arithmetic

```text
1 - (85/196)^2 - 1/4 = 19751/38416
```

is false. Exact arithmetic gives

```text
1 - (85/196)^2 - 1/4 = 21587/38416.
```

The correction strengthens the margin and preserves the operator theorem.

**Verdict:** `VERIFIED_WITH_FIXES`.

### F-B-004 — PR #438 order-two actual-Xi theorem

The orbitwise monotonicity argument survives, but the canonical statement
should explicitly record:

* centered Hadamard grouping;
* locally uniform differentiated convergence on the safe real axis;
* multiplicity conventions;
* the exact external input used only to keep all ordinates away from the small
  rational obstruction.

**Verdict:** `VERIFIED_WITH_FIXES`; no finite numerical Xi sample is evidence.

### F-B-005 — PR #445/#446 order-three assembly

The determinant and curvature allocation are valid after the following
clarifications:

* use one fixed verified critical orbit with its full multiplicity convention;
* allocate only a total fraction strictly below one;
* group conjugate/off-line orbits before differentiation;
* justify locally `C^2` passage by a uniform reciprocal-square zero tail;
* state the safe domain `t>1/4`, equivalently `x>1/2`.

**Verdict:** `VERIFIED_WITH_FIXES`.

### F-B-006 — PR #460 low-order Xi impedance results

The pairwise squared-pole identities and reciprocal Loewner–Hankel congruence
are exact. The zeta-specific anchor domination must cite the frozen external
height/local-count theorem and expose constants rather than inheriting the PR
summary.

The order-two Loewner conclusion survives. The enormous adjacent-Hankel tower
is retained only at the exact quantified order and exact source lock.

**Verdict:** `VERIFIED_WITH_FIXES`.

### F-B-007 — PR #461 fixed-order fractional-string result

The sectorial scaling and beta-Hankel limit survive for every prescribed fixed
order after stating compact subsets away from the negative cut, derivative
uniformity, and the normalization of `alpha_x`.

**Verdict:** `VERIFIED_WITH_FIXES`.

The growing-order theorem is addressed separately below and is not a local fix.

### F-B-008 — PR #400/#404/#429 Suzuki–Hardy normalization

Canonical extraction must:

* distinguish the imported amplitude isometry from the unproved curvature
  domination;
* use the corrected delayed form core rather than the scalar mother;
* retain resident, leakage, orientation, and bridge cross terms;
* separate the positive prime Poisson source from the completed Fisher source;
* apply `C-91333` as the controlling supersession map.

These are normalization and provenance fixes for the surviving local theorems.
They do not construct the missing common-source map.

### F-B-009 — PR #404 Fisher/Poisson source lock

The canonical refutation should pin the primary quasi-infinite-divisibility
theorem and show the parameter translation from the completed Xi law.
The conclusion that the two positive sources cannot simply be identified
survives.

**Verdict:** the mechanism is refuted; source-lock metadata require repair.

### F-B-010 — PR #379/#384/#385 First-Hermite family

Canonical statements should separate:

* the exact RH criterion from unconditional positivity regions;
* existence of effective thresholds from a deposited numerical threshold;
* absolute convergence of the prime formula from the open sign;
* the phase-blind constant-four firewall from a counterexample to the desired
  signed inequality.

The broad-kernel, fixed-resolution exterior, and
`q <= (4-epsilon) log log |x|` wedge theorems survive with these clarifications.

### F-B-011 — PR #580 Q4 annular packet

The factor-1024 support, scale-filter inverse, and pole-safe multiplier are
exact. Canonical extraction must retain the distinction:

```text
compact support in logarithmic coordinate
!= compact Fourier support.
```

The ten-band certificate is retained; the review replay checks representative
exact identities rather than regenerating the entire packet.

### F-B-012 — PR #606 Q4 filter exhaustion

State the exact normalization of UOSACF and the class of
subpower-invertible filters. The valid conclusion is that these filters
preserve an RH-equivalent criterion, not that UOSACF has been proved.

### F-B-013 — PR #368 corrected pole convention

Do not extract the obsolete positive-diagonal pole model or the corrupted
legacy `T-90502`. Use the hyperbolic cross block, corrected index shift,
Darboux pole-null completion, and rank-one positive completion from the
controlling corrected lineage.

### F-B-014 — numeric claim-ID collisions

Historical numeric IDs are not stable identities. In particular, the minimal
wavelet packet's old `T-100200` namespace collides with unrelated live work and
was migrated to `T-100500`.

**Required repair:** use semantic aliases plus
`PR/head/path/internal-ID`; do not rename historical files.

## Non-minor defects: no downstream verification

### N-B-001 — PR #641 moving fixed row

PR #641 fixes a row in the premise but later selects a sufficiently large row
after a hypothetical zero is introduced. That changes a fixed detector into a
zero-dependent detector.

This is a quantifier gap, not a local typo.

**Disposition:** `GAP_BLOCKED`, superseded by the fixed rows `2,3` theorem in
PR #652.

### N-B-002 — PR #461 growing-order high-axis passivity

The proposed moving Fekete-frame theorem does not supply enough quantified
control of:

* the moving-band Vandermonde lower bound;
* constants uniform in order and height;
* the full conjugate-pair perturbation;
* the transition from sectorial compact-set asymptotics to the stated growing
  order.

**Disposition:** `GAP_BLOCKED`. Fixed-order eventual passivity remains valid.

### N-B-003 — conclusion-facing common-source identifications

The following are not minor omissions:

* Suzuki completed-source first-chaos domination;
* theta/Brownian DtN identification;
* prime-Poisson to Fisher-Hankel renormalized source map;
* finite drift/gamma/pole/bridge source lock;
* Q4 SACF/UOSACF cancellation;
* First-Hermite constant-four signed prime theorem;
* fixed-center or pole-centered fractional signed heat estimate;
* Weil corrected arithmetic floor;
* all-order Fredholm prime-side positivity.

Each requires a new theorem and remains open or RH-equivalent.

## Artifact-only corrections

A checker or retained JSON may be regenerated only when the theorem, source
type, quantifiers, and normalization are unchanged. The fresh reviewer replay
has its own `SHA256SUMS`; it does not overwrite or retroactively authenticate
historical artifacts.
