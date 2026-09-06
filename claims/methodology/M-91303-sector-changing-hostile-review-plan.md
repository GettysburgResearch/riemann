# M-91303 — Hostile review plan for the sector-changing pole-bridge completion

Methodology ID: `M-91303`  
Status: **EXECUTABLE REVIEW SPECIFICATION**  
Created: 2026-08-12

## Review 1 — product sectors

Re-derive the local inverse coefficients, exact H2 norm, Kakutani threshold, and translation-overlap formula. Check both the unphased and phase-adjusted incomplete-tensor criteria. Reject any proof that treats a cylinder distribution as a Hilbert vector.

## Review 2 — Mellin orientation

Re-derive

\[
 \mathcal J\mathcal T_a=\mathcal T_a\mathcal J,
 \qquad
 \mathcal T_{d_\omega}A_\omega=\mathcal JF_\omega.
\]

Verify the Mellin conventions and determine which port is forward and which is inverse. Reject any construction whose finite-prime action has the wrong orientation.

## Review 3 — pole bridge

Starting from Suzuki's explicit \(g_\omega\), independently derive \(C_{0,\omega}\), \(C_{1,\omega}\), the free Green threshold, and

\[
 \operatorname{Res}_{s=1-\omega}G_\omega=C_{0,\omega}.
\]

Check the coefficient-one zero of the forward Jordan factor and the finite-Euler amplification asymptotic.

## Review 4 — one-node normalization

Independently expand the arithmetic source scalar and model ledger at \(a=0\). Confirm that they scale as \(a^{-1}\) and \(a\), respectively. Locate every branch statement that implicitly identifies them.

## Review 5 — proposed optical theorem

A claimed `EPBOT_omega` proof must supply:

```text
an explicit rigged source topology;
a declared dense cylinder core;
a closable sector-changing map;
finite-prime Julia compatibility;
pre-norm pole-bridge cancellation;
safe-open completed Xi amplitude identity;
positive graph form;
cutoff-uniform tail estimate;
output translation covariance;
dyadic cocycle compatibility.
```

## Controls

Run both existing RH-false controls:

1. the PR #398 planted symmetric factor preserving the true zeta Jordan channel and one-Green positivity;
2. the historical self-dual bad theta mask.

The proposed map must fail at the completed entangled boundary identity, not earlier at the safe source algebra.

## Promotion rule

Do not promote to an RH proof unless `EPBOT_(omega_j)` is proved for every member of one fixed sequence tending to zero, all four exact reviews pass, both controls fail at the declared joint, and no abstract target-kernel square root or numerical assumption remains.
