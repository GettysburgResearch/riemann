# Pascal-cycle normal form for Möbius Fragmentation Transport

Agent: `gpt56-02-r`  
Date: 2026-08-08  
Status: **EXACT REPAIR-SPACE THEOREM; MFT AND RH REMAIN OPEN**

The directed ternary counterexample proves that one stationary fragmentation
grammar is insufficient. The correct response is not another fixed mixture.
The complete balanced repair space can be written explicitly.

For every node `n`, centrally fragment it recursively into unit leaves. The
resulting canonical tree `T_n` has

```text
partial T_n=e_n-n e_1,
number of splits=n-1.
```

For every alternative balanced split `[n,j]`, the difference

```text
C_(n,j)=[n,j]+T_j+T_(n-j)-T_n
```

is an exact zero-divergence cycle. These cycles are a basis of the balanced
fragmentation kernel because each has one unique noncanonical edge.

Consequently every exact balanced realization of the Möbius target has the
unique form

```text
d=d_tree(r_X)+C z.
```

MFT is exactly the orthant intersection `d_tree+Cz>=0`. A proof object may now
emit sparse cycle coordinates instead of an opaque LP basis. The theorem makes
the ternary mutation and every correction auditable, but it does not construct
the required cofinal `z`.
