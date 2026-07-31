# X-18502 — Exact full-complement frame replay

This experiment checks the finite algebra consumed by `L-18507/T-18502`.

A certificate supplies:

```text
G > 0,
U = R direct-sum_G W,
K >= 0,
W^*(K-tau G)W > 0,
R^*(epsilon G-K)R > 0,
0 <= epsilon < tau.
```

It follows that the generalized evaluation Gram has exactly `dim R` eigenvalues
below `tau`, and the low evaluation spectral space has squared angle at most
`epsilon/tau` from `R`.

The checker uses only integers and `fractions.Fraction`. It verifies:

- metric positivity;
- exact full rank of `R` and `W`;
- exact `G`-orthogonality;
- exact packet completeness `rank[R W]=dim U`;
- strict complement frame LDL pivots;
- strict radical evaluation-upper LDL pivots;
- exact count and angle arithmetic;
- typed rational/schema gates.

## Retained exact control

```text
ambient dimension       4
radical rank             2
full complement rank     2
threshold                1
radical endpoint         1/100
count lower/upper        2 / 2
angle squared upper      1/100
complement pivots        4, 23/4
radical pivots           1/100, 1/100
```

Proof-object SHA-256:

```text
a89de5b1155948aaa524dcb3eabeff62b9e7d5d074fdbd9b2ff2336361c25f68
```

Nine central/adversarial tests pass.

## Production contract

A Riemann packet certificate must additionally bind:

1. the exact harmonic lift and `G_C` metric;
2. the actual complete finite low packet;
3. the exact radical basis and its evaluation-tail upper bound;
4. proof-grade simple critical-line zero intervals;
5. directed evaluation rectangles and multiplicities;
6. the complete omitted-zero budget `B_T`;
7. the strict scalar moat `B_T+beta < sigma_Z^2`.

The exact checker verifies the finite consequence, not the Paley--Wiener or
Conrey inputs and not the cofinal moat.
