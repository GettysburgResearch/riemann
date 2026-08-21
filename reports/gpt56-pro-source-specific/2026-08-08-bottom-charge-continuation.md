# Bottom-charge continuation of the dyadic parity-dipole proposal

Agent: `gpt56-pro-source-specific`  
Date: 2026-08-08  
Status: **NEW EXACT REDUCTION; NO UNCONDITIONAL RH PROOF CLAIM**

## Result

A fresh pass through PRs #265, #268, #269, and #271 found a sharper consumer for the source already introduced on PR #268.

The compact opposite-parity source

\[
\omega_2
=
\mu-\frac32\delta_2*\mu+\frac12\delta_4*\mu
\]

does not merely have bounded carry complexity. Its exact carry image is

\[
(-5/6,-1/2,0,0,\ldots).
\]

Consequently, if `c_X` is the exact triangular inverse of the logarithmic carry target, then

\[
\sum_{q=2}^{X}\frac{\omega_2(q)}{\sqrt q}\log(X/q)
=
-\frac56c_X(2)-\frac12c_X(3).
\]

The whole RH-bearing source has collapsed to one fixed linear combination of the first two carry coefficients.

## New finite hinge

The proposed theorem is simply

\[
5c_X(2)+3c_X(3)\ge0
\]

for every sufficiently large `X`.

This is strictly weaker than full Carry Saturation and weaker than positivity of either coefficient separately. It permits every coefficient from row four upward to be signed.

The inequality makes the compact Riesz mean eventually nonpositive. Its Mellin transform is

\[
\frac{(1-2^{-z-1/2})(1-2^{-z-3/2})/\zeta(z+1/2)-1}{z^2}.
\]

Landau's theorem then moves the convergence boundary to `Re z<=0`. Because the Euler numerator cannot cancel a zero in the critical strip, every hypothetical zero with real part greater than `1/2` is excluded. The functional equation gives RH.

## Why this is progress but not completion

The exact source, carry compression, formal triangular identity, and conditional Landau chain are now written and replayed.

The sign itself remains open. It contains the RH burden: a finite sign ladder, the high-precision positivity of the first carry coefficients through the current reconnaissance range, or positivity of a generic convolution kernel does not prove it.

The preferred attack is source specific:

```text
opposite-parity omega_2 family
-> two-frequency physical normal block
-> compact carry dipole
-> binary-digit boundary atoms
-> rows 2 and 3
-> bottom-charge sign.
```

This continuation replaces the broad Reflected Dyadic Hall theorem by one smaller necessary consumer. RDH would imply the sign, but reviewers no longer need to verify a Hall inequality for every dual witness merely to decide the RH chain.

## Artifacts

```text
L-26204  exact compact-source/bottom-charge identity
T-26202  bottom-charge one-sign criterion for RH
M-26202  fail-closed review protocol
X-26202  exact formal regression
```

Exact regression verdict:

```text
EXACT_BOTTOM_TWO_CARRY_CHARGE_ALGEBRA_VERIFIED
```

The regression proves no sign and no RH theorem.
