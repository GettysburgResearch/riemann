# X-9514 — Exact Volterra–virial totient regression

Claim ID: `X-9514`  
Title: Fraction-only verification of the total-minus-arithmetic virial identity over `Q[1/zeta(2)]`  
Status: `PROPOSED CERTIFIED FINITE ALGEBRA`  
Authoring agent: `gpt56-08`  
Created: 2026-08-07  
Dependencies: `L-9514`  
Scope: exact finite-cell algebra only  
Related counterexample candidates: none

## Result

The standard-library verifier under

```text
experiments/X-9514-volterra-virial/
```

represents the analytic totient part on every unit cell as a quadratic in `x`
with coefficients affine in the formal symbol

```text
C=1/zeta(2)=6/pi^2.
```

It verifies coefficient-by-coefficient that

\[
2\int_1^N|E^{\rm AN}(x)|^2dx
=
\int_1^N|E_\varphi(x)|^2dx
-
\int_1^Nx^2|f(x)|^2dx
+
[x|E^{\rm AN}(x)|^2]_1^N
\]

for every integer endpoint

```text
2 <= N <= 64.
```

The retained verdict is

```text
PASS_EXACT_L9514_VOLTERRA_VIRIAL_IDENTITY
```

and the proof-object SHA-256 is

```text
8c6a2dfa0425ff479c096519091babe922927bbd0637957d76e69e32422b58f5
```

## Classification

This independently checks the exact finite-cell algebra and endpoint flux. It
does not verify:

- the critical joint remainder bound;
- the Möbius-weighted near-resonance estimate;
- the local-to-Bohr transfer;
- RH.

Reviewers should mutate the endpoint sign, the coefficient `2` in front of the
analytic square, the `C*x^2/2` main term, and one totient value. Every mutation
must break an exact coefficient equality.
