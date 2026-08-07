# X-23820 — Exact Green neutralization and signed balayage replay

This standard-library checker replays two exact finite interfaces:

1. `L-23820`: decomposition of a residual into its logarithmic Green mode and an orthogonal residual removed at zero objective cost;
2. `L-23821`: compression of an arbitrary signed cell residual to its two endpoint moments through exact zero-cost prime-incidence transport.

Run:

```bash
python verify.py
```

Retained classification:

```text
EXACT_GREEN_NEUTRALIZATION_AND_BALAYAGE_VERIFIED
```

Proof-object SHA-256:

```text
ef7ac6b1828f4215667a1c0549820ea454bb66337941497cff825d08bd5d79e0
```

The checker uses only integers and `fractions.Fraction`. Four deliberate mutations are rejected.

## Proof boundary

The replay certifies finite rational algebra only. It does not prove the signed quotient-layer barrier `SGQB(K)`, an asymptotic carry estimate, the prime-ramp bound, or RH.
