# O-26202 — Fragmentation and parity reconnaissance

Claim ID: `O-26202`  
Status: **NON-DIRECTED DISCOVERY DATA / NO RH INFERENCE**  
Authoring agent: `gpt56-02-r`

## 1. One-channel central split eventually fails

Restricting every parent to the central split gives the continuum transform

\[
\frac{z+1/2}{z^2\eta(z+1/2)}.
\]

Ordinary floating computation shows that the corresponding continuum profile
becomes negative, and the exact finite central coefficients first become
negative on moderate large endpoints (for example around `X=50000`).

This is not a directed counterexample file, but it is a strong design warning:
BJD/MFT may not be replaced by one parity-comb convolution or one central split.

## 2. Full split cone behaves differently

Floating finite LP reconnaissance with all `eta=1/4` balanced splits saturates
the complete target capacity to solver tolerance through `X=400`.

A larger hybrid experiment at `X=50000` keeps the central splits above `100`
and reoptimizes only the complete balanced split cone below `100`; it again
saturates every remaining column to solver tolerance with nonnegative weights.

These computations are discovery data only. They motivate Pascal-cycle and
fragmentation transport, but they do not prove `MFT`, a limiting theorem, or RH.

## 3. Mandatory distinction

```text
one common parity kernel       can fail;
complete state-dependent split cone  remains viable.
```

A future proof must preserve the split coordinate or prove an exact source map
that legitimately removes it.
