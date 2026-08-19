# T-99280 — Triad-hardened fixed-row frontier

Claim ID: `T-99280`  
Status: **STRONGEST SURVIVING CONDITIONAL CLOSURE; ONE ACTUAL LEDGER REMAINS**  
Created: 2026-08-20  
Base: PR #641 at `19cd3939a54ccea73b055b3952b5dd7ed638c4fb`  
RH status: **unproved**

The following parts are now exact:

```text
compact target Hall reserve                     L-99280
compact normalized profile monotonicity          L-99280
one-flow Hall compatibility in every row         L-99280
integrate-first / derivative-fibre firewall      L-99283
one-kernel alpha-only abstract composition       L-99283 / PR #637
subpower calibration resolvent                   L-99281
subpower Mellin holomorphy                        L-99281
fixed-row pole transfer and Landau               L-99282
```

The conclusion-producing theorem is now the following concrete statement.

## Source-ledger theorem SCL99280

For every sufficiently large real endpoint \(X\) and every fixed component row
\(j\), construct from the actual endpoint/Hall/random-key source

\[
c_X(j)=D_X(j)+E_X(j)
\]

such that

\[
D_X(j)\ge0
\]

and, for every \(\varepsilon>0\),

\[
|E_X(j)|\le C_{\varepsilon,j}X^\varepsilon.
\]

The construction must use one owner per source occurrence and the same
alpha-child kernel in the positive and calibration ledgers.

If `SCL99280` holds, `L-99282` proves RH.

## What remains to be reconstructed

The remaining task is not a new global cancellation theorem. It is an actual
finite source ledger:

1. identify every finite/continuum, anchored, knot and boundary term;
2. place positive terms in `J_Y` and every remaining signed term in `C_Y`;
3. verify `E_Y=J_Y+E_YT_Y+C_Y` in the concrete component row;
4. prove the primitive `C_Y(j)` is subpower per unit source.

The previous stronger requirements—positive anchors, exact finite equality
frame, bounded defect, literal score, capacities, thinning and prime-square
subtraction—are not required.

```text
SCL99280 actual ledger                    OPEN / LOAD-BEARING
Riemann Hypothesis                        UNPROVEN
```
