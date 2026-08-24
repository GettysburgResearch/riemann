# R-105450 — Positive rectangle energy is not the controlling signed trace

Claim ID: `R-105450`

Status: **PROVED TYPE/COMPOSITION FIREWALL**

`T-105440` introduced `F1RECT105443` as a positive block-energy estimate for
source-complete Plücker rectangles. The exact factorization remains useful,
but that positive energy is not the conclusion-facing theorem.

## 1. Fixed packets do not sum source-blindly

Even if every scalar packet obeys

\[
|\mathcal C_\alpha|\le1,
\]

one may have \(N\) packets with the same phase and

\[
\left|\sum_{\alpha=1}^N\mathcal C_\alpha\right|=N.
\]

Thus modulus-free fixed-quadruple estimates do not bound the coherent identity
point.

## 2. Torus energy is not physical restriction

The augmentation characters are orthogonal on the full owner-phase torus.
Physical observation is their coherent value at the source-prescribed
identity point. The repository already contains explicit clustered-frequency
countermodels to a source-blind torus-to-physical contraction.

## 3. Signed trace may be small while positive energy is large

For vectors \(v_1=h\), \(v_2=-h\),

\[
\|v_1+v_2\|=0,
\qquad
\|v_1\|^2+\|v_2\|^2=2\|h\|^2.
\]

Carrier and homotopy cancellations in the native-minus-completion source have
exactly this structural form. Therefore a positive Plücker energy can be
power-sized while the signed conclusion current is small.

## Correct disposition

```text
Plücker factorization and local-system lift   retain;
fixed-quadruple phase normalization           retain;
positive rectangle energy as final gate       supersede;
coherent signed balanced Plücker trace         controlling.
```

No claim is made that `F1RECT105443` is false for the literal source. It is
simply stronger than, and not supplied by, the source-faithful signed phase
method.
