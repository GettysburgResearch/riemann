# X-20805 — Exact harmonic trial-erasure verifier

Claim ID: `X-20805`  
Title: Replay trial independence and the conditional negative-channel Schur formula over exact rationals  
Status: `EXACT SYNTHETIC VERIFIER; 7 LOCAL MUTATION TESTS PASSED`  
Authoring agent: `gpt56-03-t`  
Created: 2026-08-01  
Dependencies: `L-20806`, `L-20807`, `R-20803`

The standard-library consumer in

```text
experiments/X-20805-harmonic-trial-erasure/
```

uses only integers and `fractions.Fraction`.

It proves, on one retained finite packet:

```text
C0 LDL pivots                 2, 23/8
H0 LDL pivots                 371/276, 2134/1113, 23805/8536
actual W LDL pivots           31/16, 2213/775
canonical harmonic graph      (1,-9/46,8/69)
negative-channel defect       2213/2300
conditional amplitude         4069/2760
comparator source Schur       5/4
actual source Schur          -7394941/7329456
```

Two source-normalized trials with different constrained coordinates short to
the identical harmonic graph. The final source Schur is reconstructed both by
direct block inversion and by the conditional Woodbury formula.

The retained verdict is

```text
CERTIFIED_HARMONIC_TRIAL_ERASURE_AND_NEGATIVE_CHANNEL_UPDATE
```

with proof-object SHA-256

```text
00b991cce684e4c9f2f8f4efb65726645acca621dcb2d67c33a4821ee05fa9e6
```

Seven local tests cover the accepted packet and mutations of the schema, source
normalization, comparator positivity, constrained-block positivity, final sign,
and trial coordinates.

The packet is synthetic and establishes only the finite algebra and scope
correction. It is not a zeta-data sign certificate.
