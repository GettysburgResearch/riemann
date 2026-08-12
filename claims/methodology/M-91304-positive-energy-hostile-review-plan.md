# M-91304 — Hostile review plan for the harmonic-sector positive-energy proposal

Methodology ID: `M-91304`  
Status: **EXECUTABLE FAIL-CLOSED REVIEW PLAN**  
Created: 2026-08-12

## Reviewer A — harmonic threshold

1. Re-derive the local logarithm.
2. Check the equality case \(k(1-2\omega)=1\).
3. Prove the \(H^2\) estimate for the extracted remainder.
4. Verify that normalization preserves the incomplete-tensor criterion.
5. Check the one-charge sequence \(\omega_j=2^{-j-3}\).

## Reviewer B — sector bundle

1. Construct the fiber-to-fiber tensor unitary from first principles.
2. Check the cocycle and measurable trivialization.
3. Prove strong continuity after direct integration.
4. Confirm that this construction works equally for an RH-false planted factor.
5. Reject any inference from boundary norm equality to positive energy.

## Reviewer C — Hardy/model port

1. Re-derive
   \[
   P_-(\bar Bf)=\bar B P_{K_B}f.
   \]
2. Check the coprime-inner/outer vanishing criterion.
3. Match the normalization to the right-half-plane crossed-zero port of `L-91034`.
4. Verify repeated poles through Cauchy jets.
5. Test finite Blaschke controls.

## Reviewer D — source completion

A claimed proof of `OCIPE` must provide before reading the target norm:

```text
the first-charge counterterm;
the positive source form;
the finite-part/graph convergence;
the exact safe transfer;
the model-space projection identity;
the infinite-height tail estimate.
```

Reject any abstract Hardy projection, target-kernel square root, after-the-fact rescaling, or appeal to analytic continuation without a positive source identity.

## Promotion rule

`T-91308` may be promoted from proposal to proof only if the source-defined construction proves

\[
P_{K_{B_{\omega_j}}}(\mathfrak A_{\omega_j}r)=0
\]

for every \(j\), and all three RH-false controls fail at that exact projection step.
