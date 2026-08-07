# X-23702 — Exact Möbius hypercube refutation

This standard-library regression supports `R-23702`.

It freezes eight disjoint pairs of close primes. Choosing one prime from each
pair gives `2^8=256` distinct squarefree products. Exact integer checks prove:

```text
all products lie in one (2X/3,X] shell;
all Möbius coefficients are +1;
the multiplicative Bohr exponent vectors have affine rank 8;
the common-overlap shell signal has scaled squared value 65536.
```

The retained proof-object digest is

```text
d786fd9608ecba0f3cd6d816699ef250b45cb20c05169085187f62e06b2e080f
```

Run:

```bash
python experiments/X-23702-mobius-hypercube/verify.py
```

The finite object refutes an absolute rank ceiling below eight. The theorem in
`R-23702` constructs the same family for arbitrary fixed `K` using primes in
`K` disjoint short relative intervals. This experiment does not estimate the
complete Möbius shell and does not prove or disprove RH.
