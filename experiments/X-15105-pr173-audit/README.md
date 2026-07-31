# X-15105 — Exact controls for the PR #173 theorem audit

Experiment ID: `X-15105`  
Status: exact finite arithmetic; no Riemann-`Xi` primitive evaluation  
Author: `gpt56-04-f`  
Date: 2026-07-31

## Purpose

This experiment verifies three small exact objects used in the audit of PR #173:

1. a gap-parity converse counterexample;
2. a simple-real-root target for which arbitrary special completion exists but the one-scalar target-pinned family fails;
3. the distinction between a valid corank-one leading-minor certificate and the invalid nonnegative-leading-minor test.

It deliberately does **not** rerun PR #173's large sampled-`Xi` census.

## Exact retained objects

### Gap-parity converse

```text
nodes = (-1,0,1)
p     = (-1,3,-1)
P(s)  = s^2-3
```

There are zero same-sign adjacent pairs and two real roots. The canonical Loewner matrix is

```text
[[2,1,1],
 [1,2/3,1],
 [1,1,2]],
```

with kernel `Rp` and all principal minors nonnegative.

### Scalar-gate separation

```text
nodes = (0,1,2,3)
p     = (5,-9,35,33)/64
P(s)  = -(s-1/4)(s-3/4)(s-5/2)
Q     = 0
```

The polynomial is simple and real-rooted. But the target-pinned family is `T_p(c)=cB_p`, and the exact vectors

```text
x_plus  = (-5,-3,-1,1)
x_minus = (-3,5,-3,5)
```

are both orthogonal to `p`, with

```text
x_plus^T B_p x_plus   = 226112/1155 > 0
x_minus^T B_p x_minus = -47248/3465 < 0.
```

Hence strict completion would require both `c>0` and `c<0`.

### Leading-minor boundary

The canonical `3 x 3` matrix has leading minors

```text
2, 1/3, 0
```

and is PSD of corank one. Conversely `diag(1,0,-1)` has nonnegative leading minors

```text
1,0,0
```

but is indefinite.

## Reproduction

```bash
python3 experiments/X-15105-pr173-audit/verify.py
```

The verifier uses only the Python standard library and `fractions.Fraction`.

Retained proof-object SHA-256:

```text
c363504fb71e8666413e682f094fb5ac975bc7fce2898f196fdf3918bde82b2b
```

## Proof boundary

The exact objects refute general implications and audit certificate logic. They make no claim about the sign or roots of any production Riemann target.