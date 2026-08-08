# M-26202 — Review protocol for the bottom-charge RH criterion

Claim ID: `M-26202`  
Title: Verify the compact source, formal carry inverse, and Landau transfer before considering bottom-charge positivity  
Status: **PROPOSED FAIL-CLOSED REVIEW PROTOCOL**  
Authoring agent: `gpt56-pro-source-specific`  
Created: 2026-08-08  
Dependencies: `L-26204`, `T-26202`, `X-26202-bottom-charge`

## 1. Freeze inputs

Record the exact head of PR #268 and the frozen heads used for:

- PR #269's two-contact/two-charge identities;
- PR #244's carry matrix and triangular inverse;
- the square-screw or Landau consumer used for comparison.

Do not import a later sign computation into the frozen theorem.

## 2. Exact finite replay

Run

```bash
python experiments/X-26202-bottom-charge/verify.py
```

and require

```text
EXACT_BOTTOM_TWO_CARRY_CHARGE_ALGEBRA_VERIFIED
```

The checker must verify:

1. `omega_2=b_2-(1/2)delta_2*b_2`;
2. the carry image `(-5/6,-1/2,0,...)`;
3. formal backward substitution for `B^T c=w`;
4. `5c(2)+3c(3)=-6 sum omega_2(q)w_q`;
5. sibling-deletion mutations fail.

This verifies algebra only.

## 3. Independent analytic reconstruction

Starting from

\[
\mathcal R_\omega(X)
=\sum_{n=2}^{X}\omega_2(n)n^{-1/2}\log(X/n),
\]

derive its Mellin transform without quoting the theorem file. Check the subtraction of the `n=1` term and the shift `s=z+1/2`.

State the precise eventually-one-signed Mellin version of Landau's theorem and verify that a finite initial interval changes the transform only by an entire function.

## 4. Numerator firewall

At a hypothetical zeta zero `rho` with `1/2<Re rho<1`, verify

```text
1-2^(-rho)       !=0
1-2^(-rho-1)     !=0
```

before concluding that the reciprocal-zeta pole survives.

## 5. Sign proof requirements

A claimed proof of BCP must establish

\[
5c_X(2)+3c_X(3)\ge0
\]

for every sufficiently large integer `X`. Acceptable forms include:

- exact symbolic inequalities;
- a recurrence with a strict lower scale and a summable boundary term;
- a source-specific reflected identity with every cross term displayed;
- a positive finite certificate whose consumer is exactly the bottom charge.

Reject:

- finite numerical verification;
- pointwise positivity of an unrelated kernel;
- generic bounded rank or automatic Brion-line cancellation;
- a global diagonal Selberg integral in place of a physical block;
- high-index carry transport with no bottom-charge telescope;
- a proof of only `c_X(2)` or `c_X(3)` after assuming the other sign.

## 6. Suggested source-specific attack

The preferred production order is

```text
complete omega_2 source
-> corrected two-frequency physical block
-> compact inner/outer carry dipole
-> binary-digit three-atom boundary
-> explicit contribution to rows 2 and 3
-> BCP.
```

PR #269's half-scale lift may be used only if the odd-column leakage and the bottom charges at `2,3` are emitted before absolute values.

## 7. Verdicts

Return one of:

```text
VERIFIED_BOTTOM_CHARGE_CRITERION
VERIFIED_WITH_LANDAU_NORMALIZATION_FIX
GAP_BOTTOM_CHARGE_SIGN
REJECTED_SOURCE_PAIRING
REJECTED_NUMERATOR_CANCELLATION
```

Successful finite replays do not change `GAP_BOTTOM_CHARGE_SIGN`.
