# X-9307 — Exact simplicial portfolio-basis checker

X-9307 is the finite standard-library checker for L-9309.

For exact positive nodes

```text
u_1 < ... < u_n
```

and exact intervals for one linear residual feature at each node, it constructs
the `n-1` basis portfolios corresponding to

```text
P_beta(y) = 1, y, ..., y^(n-2).
```

The coefficients are

```text
beta_i^(k) = -(-u_i)^k / product_{j != i}(u_j-u_i).
```

The checker recomputes exactly:

- `sum_i beta_i^(k) = 0`;
- the polynomial identity `P_beta(y)=y^k`;
- the directed interval of every basis row;
- SHA-256 bindings for the frozen feature table when supplied.

By L-9309 these `n-1` rows decide the entire normalized monomial-positive L-9308
cone, including every such portfolio supported on any subset of the same nodes.

## Verdicts

```text
CERTIFIED_NEGATIVE_BASIS_WITNESS
CERTIFIED_NONNEGATIVE_ENTIRE_CONE
UNRESOLVED_CONE
```

A Riemann-xi negative remains pending independent primitive/count reproduction
and analytic review of L-9308/L-9309. A nonnegative result closes only the stated
finite node table and the monomial-positive response cone.

## Synthetic controls

Two exact controls are retained:

1. `synthetic-negative.json`: one basis row is strictly negative while another is
   positive, proving that the checker identifies an extreme-ray witness.
2. `synthetic-positive.json`: every basis row is positive, proving exact closure
   of every normalized portfolio in the full cone.

## Reproduction

```bash
python verify.py certificates/synthetic-negative.json \
  --output results/synthetic-negative-verification.json
python verify.py certificates/synthetic-positive.json \
  --output results/synthetic-positive-verification.json
python -m unittest discover -s tests -v
```

The checker uses only Python integers and `fractions.Fraction`.
