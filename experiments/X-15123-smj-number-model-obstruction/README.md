# X-15123 — Exact number-model obstruction to universal `SM(J)`

This standard-library checker replays the finite model from `R-15112`.

For

```text
A = N
K = A(A-I) = N(N-I)
d = (I-S)c = e_j
j = floor(J/2)
```

it computes exactly

```text
||d||^2 = 1
4^(-j)||Kd||^2 = 4^(-j) j^2 (j-1)^2
```

so any universal block-normalized inverse needs a constant at least

```text
4^j / [j^2 (j-1)^2],
```

which grows exponentially.

Run:

```bash
python3 experiments/X-15123-smj-number-model-obstruction/verify.py
```

The retained result has proof digest

```text
e0fb622c741d330bb4d46d819c383f338b47a82e13ec7f5c6a12e6acd1db5a00
```

This is an exact finite regression. It refutes the universal statement `(M-15110.12)` but makes no claim about a source-specific arithmetic estimate.