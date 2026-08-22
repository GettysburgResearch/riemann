# Research report — confluent residue ledger

Date: 2026-08-23

Branch: codex/105100-residue-second-moment

Checkpoint base: 0c1aedcafe7c6fe384695eee64435cc87b792aea

## Outcome

The paired boundary-flux route no longer needs simple zeros inside its
rectangle. L-105103 gives a finite local Taylor recurrence for both quotient
residues at arbitrary multiplicity and a unique union-support ledger that
prevents common \(F'/F''\) points from being counted twice.

The corrected simple-noncommon-stratum moments are

\[
\mathcal M_1^{\mathrm{snc}}
=-\Phi_1+C_1^s+\Lambda_1^{\mathrm{mrg}},
\qquad
\mathcal M_2^{\mathrm{snc}}
=B-C_2^s-D_2^s-\Lambda_2^{\mathrm{mrg}}.
\]

This closes the “separate confluent residue ledger” gap explicitly left by
L-105101 and L-105102.

## What changed scientifically

The new formulas distinguish three facts that the simple-zero ledger merged:

1. local pole order is determined by the valuation triple \((m,r,s)\);
2. the residue is a later Taylor coefficient and can vanish at a genuine
   higher-order pole;
3. real reverse--Rolle transfer cares about multiple/common critical events
   even when the contour residue is zero.

The merged second correction is not a positive moment. Exact examples give
\(-5/18\) and \(+1/4\), and the common-event fixture \(x^3\) has zero
residue despite nontrivial multiplicity.

## Exact verification

The focused replay authenticates checkpoint 3 and uses:

- full local principal parts;
- a unique-center event manifest with mutation rejection;
- independently reversed residue-at-infinity series;
- frozen \(V_2\) and \(V_2,V_4\) root ledgers;
- Gaussian-rational algebraic-square checks;
- shift/scale invariance.

Result:

    PASS_T105103_CONFLUENT_RESIDUE_LEDGER
    15/15 normal
    15/15 optimized
    e208cceb8b09c639f6587024e5bef334a37d650435453515f68b8f42512c53c2

No heavy computation was run.

## Remaining frontier

The next required input is not another formal contour rearrangement. It is an
Xi multiplicity/event manifest together with either:

- exclusion of real multiple/common \(\Xi^{(k)}\)-events on cofinal windows,
  or
- a genuinely new multiplicity-aware reverse--Rolle theorem.

Boundary-flux, merged-correction, endpoint, carrier-sign, and strict-margin
estimates also remain open. No RCMV104530 or RH conclusion is claimed.
