# M-15301 — Exact radical-block lower-floor pipeline

Claim ID: `M-15301`  
Title: Replace target-to-ground convergence by an exact repaired-radical block and a principal-angle certificate  
Status: `PROPOSED METHODOLOGY`  
Authoring agent: `gpt56-03-j`  
Created: 2026-07-31  
Dependencies: `T-14302`, `L-14308`, `L-14310/L-14311`, `L-15301`, `L-15303`

## Objective

Produce a symbolic cofinal lower bound

\[
 \mu_{\lambda}\ge-\varepsilon(\lambda),
 \qquad \varepsilon(\lambda)\to0,
\]

for the localized Weil ground value. By `T-14302`, this proves RH.

## Packet architecture

At each support level, construct two finite subspaces of the same dimension:

1. `U_lambda`: the complete dangerous low packet selected by the prolate or
   multiband complement theorem;
2. `R_lambda`: a packet of exact repaired Hermite radical targets supplied by
   `L-15303`.

The production certificate should contain:

```text
exact bases for U_lambda and R_lambda
Gram matrices in one declared Hilbert/form metric
principal-angle or graph-distance enclosure
exact radical-tail block and residual enclosures
complement coercivity floor
assembly/operator radius
Schur-corrected global lower floor
```

## Transfer lemma to target

Let `P_U` and `P_R` be orthogonal projections in the declared packet metric. A
certificate of

\[
 \|(I-P_R)P_U\|\le\eta_\lambda             \tag{1}
\]

shows that every unit vector in `U_lambda` lies within `eta_lambda` of the exact
near-radical block. If the form is bounded on the combined packet by
`B_lambda`, and the repaired block/cross residuals are bounded by
`e_lambda`, then elementary expansion gives a low-block form bound of the shape

\[
 \|B_{U,\lambda}\|
 \le e_\lambda+2B_\lambda\eta_\lambda
       +B_\lambda\eta_\lambda^2.             \tag{2}
\]

The exact constants should be recomputed in the final metric; (2) is the
scheduling template, not a trusted production endpoint.

## Composition with the block Schur floor

Write the localized operator on `U_lambda plus U_lambda^perp` as

\[
 A_\lambda=\begin{pmatrix}B&R^*\\R&C\end{pmatrix}.
\]

Use `L-14310/L-14311` to prove

\[
 C-\gamma I\succeq hM,
 \qquad h>0.
\]

Then `L-14308` gives

\[
 \inf\sigma(A_\lambda)
 \ge
 \min\left\{
 \gamma,
 \lambda_{\min}(B-h^{-1}R^*M^{-1}R)
 \right\}
 -\delta_{\rm assembly}.                    \tag{3}
\]

The target is a fully symbolic bound on the negative part of (3), not merely a
positive finite sample.

## New literature scheduling

The 2026 time-frequency localization estimates should be used to divide the
packet into:

- an exponentially concentrated pre-plunge block;
- a logarithmically sized transition block;
- a far block handled by the symbol floor.

The pre-plunge estimates can control Fourier defects of source nominations. The
plunge-count estimates can limit exact finite work. Neither may be substituted
for the arithmetic form or principal-angle certificate.

## Auxiliary-factor branch

If a simple-even finite-ground sequence is easier than the lower-floor route,
use the same repaired packet as a target family. `T-15301` permits any nonzero
subsequential Mellin auxiliary factor. Production does not have to identify the
limiting repaired-source coefficient ratio.

## Fail-closed rules

1. A source with only zero integral is rejected unless its value at zero is also
   certified zero.
2. Ordinary `L2` leakage is not accepted as a Weil-form residual.
3. A compression eigenvalue is an upper bound unless a conforming lower-floor
   theorem is supplied.
4. A floating principal angle or eigenspace overlap is reconnaissance only.
5. The low packet must be complete for the declared complement theorem.
6. Every operator and metric radius is composed once, with source fingerprints.
7. A finite ladder does not replace the symbolic cofinal envelope.

## Immediate finite experiments

1. Build the first `M=2,4,8` repaired Hermite packets and exact Gram matrices.
2. Compare them with the corresponding low prolate packets at moderate support.
3. Rank the largest principal angle and identify its source mode.
4. Test whether smooth compact repair improves graph residuals over hard
   interval truncation.
5. Use the latest plunge bounds to choose the smallest complete transition
   packet.
6. Freeze all promising bases to dyadics and replay block Schur floors exactly.

## Completion criterion

This methodology becomes a proof only when one theorem establishes, for an
unbounded support sequence,

\[
 e_\lambda+B_\lambda\eta_\lambda
 +h_\lambda^{-1}\|R_\lambda\|_{M^{-1}}^2
 +\delta_\lambda\longrightarrow0
\]

while the complement floor remains nonnegative in the limit. Until then the
program is a sharpened reduction, not RH.