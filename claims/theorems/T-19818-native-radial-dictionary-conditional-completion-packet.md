# T-19818 — Conditional completion from the native-radial dictionary and a decomposable model allocation

Claim ID: `T-19818`  
Status: **PROPOSED CONDITIONAL COMPLETION PACKET — NOT AN UNCONDITIONAL RH PROPOSAL**  
Authoring agent: `gpt56-pro-09-w`  
Created: 2026-08-14  
Dependencies: `L-19880`; PRs #404, #427, #430, #435, #470; `T-19817` only for comparison, not as an imported conclusion  
Scope: exact reduction after the native-to-radial source lock; no RH claim

## 1. What `L-19880` removes

The former `SORKMD` formulation required one common source-owned native/radial
feature dictionary. `L-19880` constructs that dictionary for the prime channel
and appends the already-positive eta, bridge, gamma/pole, orientation and delay
channels by direct sum.

Consequently the source side is no longer an unspecified common-column
certificate. Given a source-owned native family `d_X`, its radial arithmetic
feature map is explicit.

## 2. Source field

Fix a safe offset `a>0`, and let `sigma_a` denote the safe Euler line used by
the completed arithmetic source. Let

\[
 \mathcal V_{a,r}:\mathcal H_{\rm carrier}
 \longrightarrow\mathcal K_{a,r}^{\rm src}
 \tag{T-19818.1}
\]

be the completed source feature map whose prime summands are

\[
 \sqrt{c_\alpha(\sigma_a,r;q)}
 \bigl(1-e^{-it\log q}\bigr),
 \tag{T-19818.2}
\]

with coefficients from `L-19880`, and whose remaining summands are the exact
coefficient-one source channels of PRs #404, #427 and #430.

For a radial interval `I`, put

\[
 \mathsf U_a(I)
 =\int_I\mathcal V_{a,r}^*\mathcal V_{a,r}\,dr.
 \tag{T-19818.3}
\]

The full arithmetic source satisfies

\[
 \mathsf U_a(I)\preceq\mathsf A_a(I)
 \tag{T-19818.4}
\]

with explicit positive prime slack from `L-19880`.

## 3. The sole model-allocation theorem

The remaining conclusion-producing theorem is **Native-Radial Model Allocation
(`NRMA_a`)**:

For almost every radial depth `r`, construct a contraction

\[
 W_{a,r}:\mathcal K_{a,r}^{\rm src}
 \longrightarrow\mathcal K_{a,r}^{\rm model}
 \tag{T-19818.5}
\]

such that:

```text
W_(a,r) is decomposable and measurable in r;
it preserves carriers, both Hardy orientations, the bridge and compressed delays;
it respects the source-owner labels before their orthogonal sum;
its visible Gram is the complete critical + stable + hyperbolic + auxiliary
model density at depth r;
no post hoc unitary rotation among output ports is permitted.
```

Equivalently, for every finite polarized packet `F`,

\[
 [\mathsf M_a(dr)]_F
 =\mathcal V_{a,r}^*W_{a,r}^*W_{a,r}
  \mathcal V_{a,r}\,dr.
 \tag{T-19818.6}
\]

Then

\[
 \mathsf M_a(I)
 \preceq\mathsf U_a(I)
 \preceq\mathsf A_a(I)
 \tag{T-19818.7}
\]

for every rational interval `I`.

`NRMA_a` is not proved here. It is stronger than amplitude unitarity and weaker
than guessing a global source-to-model unitary: it asks only for one
source-ordered contraction at almost every radial depth.

## 4. Conditional zero exclusion

Assume:

1. a source-owned native family satisfying `SONTR` and the hypotheses of
   `L-19880`;
2. `NRMA_a`;
3. the positive radial model ledger and local Kolmogorov gluing of PRs #430 and
   #435.

Then (T-19818.7) gives intervalwise model domination by a diffuse arithmetic
source. The hyperbolic crossed-zero measure is positive and pure point, while

\[
 0\preceq\mathsf H_a(I)
 \preceq\mathsf M_a(I)
 \preceq\mathsf A_a(I).
 \tag{T-19818.8}
\]

For every singleton depth `x>0`, diffuseness gives

\[
 \mathsf A_a(\{x\})=0,
 \tag{T-19818.9}
\]

so `mathsf H_a({x})=0`. Therefore `mathsf H_a=0`, and the radial Krein--Langer
ledger gives

\[
 \xi(s)\ne0
 \qquad(\Re s>1/2+a).
 \tag{T-19818.10}
\]

If the assumptions hold for one explicit sequence `a_j downarrow0`, functional
equation symmetry gives RH.

## 5. Corrected frontier

The exact new status is:

```text
common native/radial arithmetic columns        CLOSED BY L-19880, PENDING REVIEW
coefficientwise prime radial slack              CLOSED BY L-19880, PENDING REVIEW
completed positive arithmetic source            AVAILABLE BY DIRECT SUM
SONTR native producer                            OPEN
NRMA source-ordered model allocation             OPEN / RH-BEARING
NRMA + radial spectral-type consumer -> RH       CONDITIONAL DEDUCTION
Riemann Hypothesis                               UNPROVED
```

This packet is deliberately not called a full proposal: two substantive
unconditional inputs, `SONTR` and `NRMA`, remain open.
