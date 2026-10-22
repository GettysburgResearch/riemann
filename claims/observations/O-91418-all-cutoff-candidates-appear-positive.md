# O-91418 — All-cutoff strengthening

Status: **RECONNAISSANCE / PROPOSED**. RH remains unproved.

A stronger producer would prove the prefix determinant from `L-91415` for every positive `P_61` divisor
\[
y<c<2000,
\]
not only for the selected Lorenz cutoff. This removes all cutoff-transition logic.

A floating scan of `2,834,260` tuples with

```text
p in {67,101,509,5003}; y=1,...,67;
j=2,...,66; all admissible c<2000
```

found no negative value. The smallest observed value was about `4.658402e-4` at `p=67,y=30,j=66,c=1995`, with inactive cutoff row. The smallest active-cutoff value was about `5.189479e-2` at `p=509,y=17,j=66,c=129`.

This is discovery data, not a proof object.
