# Post-merge delta-census addendum

**Correction census:** `2026-08-11T09:13:13Z`  
**Merged integration commit:** `0552d80078111ac677fa163995d8c1bfddc61f0d`  
**Scientific cutoff remains:** `2026-08-11T08:20:51Z`  
**PR #376 independent-review cutoff:** `2026-08-11T12:31:26Z`  
**RH status:** **unproved and undisproved**

## Why this addendum exists

A final repository census immediately after merging PR #374 surfaced two concurrently created draft PRs that were not returned by the earlier recent-PR query:

```text
#375 created 2026-08-11T08:55:34Z
#376 created 2026-08-11T09:04:04Z
```

Both timestamps are after the scientific cutoff but before the declared pre-merge validation cutoff `2026-08-11T09:05:27Z`. The earlier verification report therefore contains one stale census sentence: its statement that no later PR appeared before validation cutoff is superseded by this addendum.

This is an asynchronous discovery/indexing correction, not movement of the frozen review heads and not a change to the mathematics integrated at the `08:20:51Z` scientific cutoff.

## PR #375 — terminal Gaussian heat-residue extension

```text
PR:       #375
created:  2026-08-11T08:55:34Z
head:     a3662f62ac0f1a7ec21bca3498938fedcbeeddba
base:     2a725fb71794dfca11e76c1af2a49e6b3ea8bc9c
status:   POST_REVIEW_DELTA / UNREVIEWED / QUARANTINED
```

The branch proposes a Gaussian Mellin/Bromwich normal form, an exact `-2m` target residue, fusion with the terminal-pair threat exponent, and finite linear prime certificates under false RH. Its own declared terminal scalar sign and corrected-kernel floor remain open/RH-equivalent.

Required independent checks include:

- contour-shift domain and decay;
- sign and multiplicity conventions in the residue sum;
- critical-line boundary decomposition;
- terminal-pair nuisance suppression;
- finite-tail direction and directed strictness;
- consistency with the reviewed hyperbolic pole correction.

## PR #376 — Brownian Bohr-instability delta

### Original quarantine

```text
PR:       #376
created:  2026-08-11T09:04:04Z
initial quarantined head:
          2ef174866ba9ce3a1c4939797ca223680bb21734
base:     fed85f2969a5ab9f09890cd89bd6b57ff2115320
original status:
          POST_REVIEW_DELTA / UNREVIEWED / QUARANTINED
```

The original delta claimed that the raw Brownian numerator has high-frequency Bohr zeros in every strip `1/4 < Re z < 1/2` for all sufficiently large truncation indices, thereby refuting the reviewed route's proposed cofinal half-plane stability theorem while retaining its finite algebra and compact-height convergence.

The live PR subsequently moved materially by adding a general positive-mixture theorem and a functional-equation symmetrization transfer.

### Independent theorem-level review resolution

```text
reviewed live head:
  0ed0e7de3aa1b81bb832df53d861dd6f27f2db8b
review cutoff:
  2026-08-11T12:31:26Z
overall verdict:
  VERIFIED WITH FIXES
```

Durable review artifacts:

```text
reports/integration-wave/20260811-pr376-brownian-bohr-instability-review.md
audits/integration-wave/20260811-pr376-brownian-bohr-instability-status.tsv
```

The selected-prime coefficient bounds, disjoint composite-fiber decomposition, Steinhaus `L^2` residual estimate, diverging selected phase mass, polygon closure, simultaneous Kronecker approximation, local-uniform vertical limit and Hurwitz transfer were independently checked. No load-bearing gap was found.

The reviewed mathematical dispositions are:

```text
L-90601 raw selected-prime Bohr theorem          VERIFIED
R-90601 raw cofinal-stability refutation         VERIFIED
L-90603 positive-mixture theorem                 VERIFIED WITH FIXES
L-90604 symmetrized Stirling/Hurwitz transfer    VERIFIED
R-90602 current finite real-zero finishes        VERIFIED AS REFUTED
L-90602 fixed-compact 1/N asymptotic              VERIFIED WITH FIXES
X-90601 / X-90602                                 EMPIRICAL ONLY
```

Consequently:

```text
raw all-large-N half-plane stability             FALSE
raw stability on any unbounded cofinal sequence  FALSE
logarithmic Nörlund one-sided stability           FALSE
current Nörlund finite-real-zero finish           FALSE
current central-binomial Green/Robin finish       FALSE
Riemann Hypothesis                                UNPROVED
```

### Required fixes before canonical extraction

1. In `L-90603`, replace the general assertion `b_(N,n)>0` by `b_(N,n)>=0`; strict positivity is available on the selected-prime block under the top-half-mass hypothesis.
2. Qualify the phrase `positive finite cutoff averaging as cure FALSE`: the theorem covers the two repository mixtures and every positive mixture satisfying the displayed `c/log N` top-half-mass condition, not every conceivable weighting scheme.
3. Repair the stale sentence in `R-90601` saying that the symmetrized programme is unaffected. `L-90601` alone does not address it, but current `L-90603/L-90604/R-90602` do refute the exact current Nörlund and Green mixtures.
4. In `L-90602`, state the initial convergence domain `Re z<1/2` for the continuum integral before invoking the gamma-recurrence continuation.

These are scope/editorial fixes; they do not alter the route-level refutations.

## Updated effect on the merged integration

The original merge remains valid as a frozen status/provenance integration through `2026-08-11T08:20:51Z`. The independent delta review now changes the live scientific frontier as follows:

1. remove raw all-large/cofinal half-plane stability from the open-hinge list and mark its antecedent false;
2. remove the current logarithmic Nörlund and central-binomial Green/Robin finite-real-zero finishes from the live proof frontier;
3. preserve all reviewed finite Brownian probability, gamma, Dirichlet, Hermite, occupation, corrected one-fiber Robin and compact-height convergence infrastructure;
4. redirect Brownian research toward:
   - a height-dependent theorem with `N=N(T)`;
   - a structurally redesigned producer avoiding Bohr-torus zeros;
   - a direct infinite canonical system for the limiting object;
5. retain PR #375 as unreviewed and quarantined;
6. retain RH status as unproved and undisproved.

The exact Brownian conclusion is a no-go for the current global finite producers, not a result about the truth or falsity of RH.

This addendum is normative wherever it differs from the pre-merge verification report, the original delta quarantine, or the earlier route DAG.
