# X-19841 — Exact affine-hybrid regression

This standard-library-only verifier checks the finite algebra used by
`L-19861`, `L-19862`, and `T-19813`.

It reconstructs an exact residual Gram from rational residual vectors, verifies
that the codimension-one target complement has a positive floor, verifies the
affine shifted lower LMI

```text
Q - sigma I - c D >= 0,
```

checks the target-only upper bound, and checks strict target/gap separation.

Run:

```bash
python3 experiments/X-19841-affine-hybrid/verify.py \
  experiments/X-19841-affine-hybrid/certificates/synthetic.json

python3 -m unittest discover \
  -s experiments/X-19841-affine-hybrid/tests
```

Retained exact values:

```text
target residual energy        1/100
complete complement floor     1
affine lower coefficient      3
target excess                 3/100
strict separation margin      297/100
```

Proof-object digest:

```text
7b1a65e8b957aadb8ed2613bcb7a6e87d93c5a3afa9e4ea05bc625e02fd278f5
```

The control is deliberately non-diagonal: the target residual has nonzero cross
pairings with both complement residuals. The exact compression floor still
forces the second residual eigenvalue above the declared moat. Five adversarial
mutations fail closed.

This experiment verifies only the finite affine/interlacing algebra. It does not
verify the Riemann-specific profile LMIs of `L-19865` and does not prove RH.
