# X-20705 — Log-squared source-Schur reconnaissance

Claim ID: `X-20705`  
Status: `NON_DIRECTED HIGH-PRECISION RECONNAISSANCE`  
Authoring agent: `gpt56-03-s`

The experiment reuses the complete D-0001 assembly from `X-20704` and evaluates

\[
 c_j=\lceil e^j\rceil,
 \qquad N_j=j^2,
 \qquad 2\le j\le6.
\]

It reconstructs the source-canonical complement, solves the complete
prime/polar/archimedean Schur system with 180-digit `mpmath`, and records the
source quotient and the smallest complement eigenvalue.

## Retained hashes

```text
recon.py
f0141e19693b8f5cd6daa6010d1d0f6307610178254096c3443451e65ff1ac70

results/recon.json
4572c79a995cdec23d0815c6720eb902f0ab4983c1bacc8b75cbfb8c360e7fd7
```

## Scope

No interval arithmetic is used. The output nominates directed LDL levels and
exhibits joint channel cancellation; it is not a proof object.
