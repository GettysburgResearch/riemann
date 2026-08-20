# T-100400 — Corrected two-route endgame after the live graph audit

Claim ID: `T-100400`  
Status: **UNCONDITIONAL STRUCTURAL ADVANCE; TWO FINAL PRODUCERS OPEN**  
Created: 2026-08-20  
Base: PR #685 at `4f69b7656f42dcb5ff250d13adc9f88e8d18f315`  
RH status: **unproved**

The live graph eliminates several tempting endpoints:

```text
HTOC/DGOC complete positive squares      RH-equivalent
minimal compact wavelet L2 bound         RH-equivalent
positive priority flux UPBF67            false
PR #685 normalized cell coarea           wrong Landau normalization
```

Two routes retain nontrivial arithmetic leverage.

## Route A — activation-zero upper envelope

`L-100400` replaces the discontinuous unshifted envelope by the activation-zero
quadratic member.  Its envelope is a global `C1` quadratic spline in
`sqrt(X)`, has no activation atoms, and has the correct reciprocal-zeta Mellin
consumer.

`L-100401` proves every actual native block through four labels positive.
The remaining theorem is the all-order actual-prime activation gate
`FAEG100401`, equivalently the subpower unnormalized deficit estimate
`ACAD100400`.

\[
\boxed{
\mathrm{FAEG100401}\Longrightarrow
\mathcal E_-(X)\ge0\Longrightarrow RH.
}
\]

## Route B — phase-Hasse physical collapse

`L-100410` rewrites the symmetric phase-Hasse boundary as an exact
two-parameter divergence and removes the degree-zero and degree-one sectors.
`L-100411` proves a polylogarithmic bound for the entire free labelled phase
packet.

The only remaining theorem is `PHPC100410`, a subpower norm bound for the
literal half-order physical collapse on the root-free phase range.

\[
\boxed{
\mathrm{PHPC100410}\Longrightarrow RH
}
\]

on the frozen zero-safe box/Mellin consumer.

## Exact boundary

```text
activation-zero envelope and pole audit       PROVED EXACT
correct unnormalized cell coarea               PROVED EXACT
actual one-to-four-label blocks                PROVED EXACT
FAEG100401 / ACAD100400                        OPEN / CONCLUSION-BEARING

phase-Hasse two-parameter divergence           PROVED EXACT
free labelled phase packing                    PROVED POLYLOG
PHPC100410 physical half-order collapse        OPEN / CONCLUSION-BEARING

Riemann Hypothesis                             UNPROVED
```
