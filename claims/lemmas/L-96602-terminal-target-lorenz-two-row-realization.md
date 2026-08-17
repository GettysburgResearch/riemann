# L-96602 — Directed Target-Lorenz terminal leaves realize rows two and three

For `p>=67`, `1<=y<67`, and squarefree `d|P61`, the terminal row is

```text
mu(d)/sqrt(d) [Q_(py/d)(j)-p^(-1/2)Q_(y/d)(j)].
```

The Hall flow identity writes the signed row as a positive residual-source row plus a nonnegative Hall bonus whenever the target-normalized profile is no-upward ordered.

The compact certificate owns `py<166000`. The MPFR-directed tail owns `py>=166000`, with 256-bit outward arithmetic and 51,118,080 event records. Frozen objects:

```text
compact blob:
2c16327c6653009667fa06ddbb24628ff583c0fe

tail proof object:
ba6b137b64819a9d01e706ffffdf100b091e49034895e6eeb280b56f514c99c5
```

The theorem is stable under passive source histories and positive scalar weights. It yields nonnegative terminal rows for `j=2,3`.
