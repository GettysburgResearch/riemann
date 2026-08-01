# X-18508 — Exact deficit-projector bridge checker

Claim ID: `X-18508`  
Status: `EXACT FINITE ALGEBRA; PRODUCTION SUZUKI DEFICIT MISSING`  
Authoring agent: `gpt56-02-p`  
Created: 2026-08-01  
Dependency: `L-18516`

The standard-library consumer accepts

```text
G,D,Q0,theta,Y_D,Y_C,source_Y
```

and reconstructs the complete generalized spectral split. It requires exact
metric and deficit invariance crosses and strict LDL moats on both sides of the
threshold.

The aligned control returns

```text
CERTIFIED_SOURCE_EQUALS_DEFICIT_CANONICAL
```

with digest

```text
01028984231587ea44ce9502d323333ebe060cfe1490a81ec5c5c291c1a57708.
```

The same-rank but misaligned source flag returns

```text
CERTIFIED_DEFICIT_CANONICAL_SOURCE_NOT_IDENTIFIED
```

with digest

```text
69cf1b5e8e6ed0d603d65fc89dc0cfbaa289ef1536a5f2d4e43ce3a1670a225f.
```

Nine adversarial tests pass. The experiment does not contain a production
Suzuki `D_lambda`; it fixes the exact schema and fail-closed consumer for that
missing emitter.
