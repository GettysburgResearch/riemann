# T-98910 — Disposition of the fractional Julia–Tao–Hermite candidate

Claim ID: `T-98910`  
Status: **UNCONDITIONAL REFUTATION + CORRECTED OPEN FRONTIER**  
Created: 2026-08-18  
Frozen target: PR #613 at `f28aa51a6d6740067202611d8ebda4be2ef0a1c9`  
RH status: **unproved**

The exact fractional positive-chaos identity of `L-98700` and the atomwise Tao
source labels of `L-98701` survive this audit. The proposed conclusion does
not.

`L-98910` proves that the uncentered fractional packet has deterministic heat
energy

\[
 \asymp_\theta T^{-2\theta-1}e^{T/2}
\]

at center zero. Hence `R-98910` refutes the uniform `96 theta` heat rate in
`L-98703`. `R-98911` independently refutes the claimed Weyl invariance of the
parity matrix coefficient.

Therefore the chain

\[
 L\text{-}98703\Longrightarrow L\text{-}98704\Longrightarrow T\text{-}98700
\]

cannot be used, and PR #613 does not prove RH.

A corrected continuation is now typed explicitly. `L-98912` tensors the parity
source with the positive continuum carrier `(s/(s-1))^theta`, removing the pole
branch while preserving every nontrivial-zero branch. The remaining mixed
discrete-continuous estimate is `PCFHE`. Conditional on a source-faithful proof
of `PCFHE` and a renewed pole-growth audit for that same observable, the
tunable-theta contradiction may be reconsidered.

```text
fractional positive chaos                 RETAINED EXACT
atomwise Tao local Gram                   RETAINED EXACT
uncentered uniform theta-rate             REFUTED
Weyl/parity invariance                    REFUTED
positive continuum pole carrier          PROVED EXACT
pole-centered heat estimate PCFHE         OPEN / RH-BEARING
T-98700 RH conclusion                     UNPROVEN
Riemann Hypothesis                        UNPROVEN
```
