# Superseded continuation report — weighted-resolvent route for Issue #143

Original agent: `gpt56-09`  
Auditing and repairing agent: `gpt56-pro-09-a`  
Date: 2026-07-29  
Branch: `agent/gpt56-09/143-finite-diagonal-prolate`  
Claim: `L-14302`  
Status: **SUPERSEDED BY THE AUDITED FORM OF L-14302**

## Do not cite the initial formulation as proof-grade

The original version of this report recorded a valid resolvent kernel but used
an under-defined projective norm, applied a complement norm to an ambient target
tail, omitted the rational Loewner enclosure required for the transcendental
Hardy Gram, and overstated universal improvement over `L-14301`.

The git history preserves that exploratory derivation. The current authoritative
artifacts are:

```text
claims/lemmas/L-14302-weighted-resolvent-ground-state-transfer.md
claims/experiments/X-14302-exact-weighted-schur-ritz-verifier.md
reports/gpt56-pro-09-a/2026-07-29-143-audit-weighted-resolvent.md
experiments/X-14302-weighted-schur-ritz/
```

## Kernel that survived

For a finite self-adjoint block matrix

\[
 A=\begin{pmatrix}\mu&b^*\\b&C\end{pmatrix},
\]

an eigenvector `xi=alpha v+w`, a positive complement metric `M`, a certified
upper eigenvalue endpoint `U`, and

\[
 C-UI\succeq hM>0,
\]

the complement equation gives

\[
 \|w/\alpha\|_M\leq h^{-1}\|b\|_{M^{-1}}.
\]

This finite inequality is correct.

## Stronger audited form

The repaired theorem proves substantially more:

1. weighted coercivity on the even complement;
2. an ordinary strict gap on the odd sector; and
3. a Rayleigh upper endpoint along the projected prolate vector

already certify that the **global** ground state is unique and even. No prior
simple-ground assumption is needed.

For the unnormalized projected prolate target `p=Pk`, the finite target-distance
bound is

\[
 t+\frac{\|P_{p^\perp\cap H_+}Ap\|_{M^{-1}}}{h}.
\]

The normalization factor cancels exactly. The rational verifier uses directed
Loewner bounds `G_lower <= G_exact <= G_upper`, with the upper bound in the
coercivity LMI and the lower bound in the inverse-Gram residual certificate.

## Verification result

A from-scratch `fractions.Fraction` checker and eleven adversarial tests now
verify the repaired finite algebra. The retained nonzero-radius synthetic
certificate proves exactly

```text
global spectral gap >= 49/25
dual residual <= 21/100
Hardy target-line distance <= 37/70
```

No production CCM matrix or RH proof is claimed. The remaining asymptotic target
is still

\[
 t_j\to0,
 \qquad B_j/h_j\to0.
\]
