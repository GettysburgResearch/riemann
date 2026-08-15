# O-91377 — One-prime finite-Euler rows are the strongest current positive-generator candidate

Claim ID: `O-91377`  
Status: **DISCOVERY FRONTIER / NOT A GLOBAL THEOREM**  
Created: 2026-08-14  
RH status: **unproved**

For a rough prime `p>=67`, define

\[
\boxed{
 D_{P\cup\{p\},X}(j)
 =D_{P,X}(j)-p^{-1/2}D_{P,X/p}(j),
 \qquad P=P_{61}.
}
\]

This is the exact current causal row obtained by adjoining one rough Euler
factor to the finite block. It is therefore the most direct candidate for the
positive current rows required by NRCT.

The companion C++ stress packet checked, with long-double sign arithmetic:

```text
p = 67, 71, 83, 127;
2 <= j <= 200;
j < X <= 200j;
3,999,701 cells for each p;
zero negative values.
```

The common minimum was the child-inactive first cell

```text
j=200, X=201,
D = 0.0003562168890477039464...
```

and the minimum scaled value was

```text
j=2, X=3,
j(j-1)sqrt(X)D = 2.979547870102263...
```

A second deterministic random replay tested one million triples with

```text
p in {67,71,83,127,251,509,1009,5003};
2 <= j <= 2001;
1 < X/j <= 1500;
```

and found no negative value. The smallest sampled value was about
`1.2026e-5`.

This is strong discovery evidence, not a proof. A global theorem must still
control the infinite `j`, quotient, and prime parameters with directed or exact
analytic inequalities. The Green/Kantorovich form suggests the worst prime is
`67` and the worst child endpoint lies at the activation boundary, but that
reduction has not yet been promoted.

If the global one-prime theorem is proved in a source-hereditary form, every
current causal generator in NRCT becomes an explicit nonnegative row. It does
not by itself solve the native reservoir allocation: all ordinary/detail
capacities must still satisfy the one-use inequalities of `T-91314`.
