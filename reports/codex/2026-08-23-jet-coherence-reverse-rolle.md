# Research report — multiplicity-aware jet-coherence transfer

Date: 2026-08-23

Branch: codex/105100-residue-second-moment

Checkpoint base: eafd6d86055179e5b2fa9b3747ea740b8609ba64

## Outcome

The real reverse--Rolle step now has an exact arbitrary-multiplicity branch.
The proof separates:

- common critical zeros, whose derivative-order mass transfers directly;
- odd-order noncommon turns, whose orientation is measured by a leading jet;
- even-order stationary events and excess flat multiplicity, retained in an
  explicit defect.

The resulting inequality is

\[
N_{\mathbb R}^{\mathrm{mult}}(f)
\ge
\mathfrak m_{\mathrm{com}}
+(2\mathfrak C_{\mathrm{jet}}-1)R_{\mathrm{jet}}-1.
\]

It recovers draft L-104522.4 exactly when every real critical event is simple
and noncommon.

## Why the jet is necessary

For an odd-order event,

\[
\rho_c^{\mathrm{jet}}
=r!f(c)/f^{(r+1)}(c)
\]

is the leading principal coefficient of \(f/f'\), not its residue when
\(r>1\). The paired quotient supplies its square in the leading coefficient,
again not the residue.

The sextics \(x^6\pm1/64\) make the distinction binding. All ordinary
\(P,Q\) residue sums vanish and their event orders coincide, but the plus
polynomial has no real zero while the minus polynomial has two. Their jet
carriers have opposite signs.

## Exact verification

The replay authenticates checkpoint 4 and checks:

- 141 bounded nonadjacent-wrong-turn patterns;
- primitive distinct and multiplicity zero counts;
- common-mass, active-component, and multiplicity-defect mutations;
- simple, flat, common, and stationary exact fixtures;
- full leading principal coefficients and residue-at-infinity no-go oracles.

Result:

    PASS_T105104_JET_COHERENCE_REVERSE_ROLLE
    15/15 normal
    15/15 optimized
    bcd3ac0f644c49e47be6b2e019a57b2e7d2b8b6df14dfec97da854cb44b3bed6

No heavy computation was run.

## Remaining frontier

The theorem changes the analytic target. A multiplicity-tolerant Xi descent
now needs an eligible-turn proportion, common-mass census, control of
\(\Delta_{\mathrm{mult}}\), and first/second leading-jet estimates. The
ordinary boundary charges developed in checkpoints 2--4 do not reconstruct
those high-pole coefficients.

No RCMV104530 or RH conclusion is claimed.
