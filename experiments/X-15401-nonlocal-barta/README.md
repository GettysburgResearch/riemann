# X-15401 — Exact nonlocal Barta and polar-rank regression

Status: exact finite synthetic regression; continuum Suzuki producer pending  
Agent: `gpt56-05-l`  
Issue: #154  
Claims: L-15401, T-15401

## Purpose

The positive RH route needs lower bounds for the **complete** localized Weil
operator, not only positive finite Ritz matrices.  L-15401 rewrites Suzuki's
scaled form as

```text
positive Markov jump form
+ explicit local potential
+ positive cosh rank one
- negative sinh rank one.
```

T-15401 then gives two exact lower-floor gates:

1. a positive supersolution supplies an ambient Barta floor for the entire
   Markov base;
2. one Birman--Schwinger scalar controls the only dangerous polar channel.

X-15401 verifies the finite graph analogue using Python integers and
`fractions.Fraction` only.

## Synthetic model

The graph has three vertices, path jump weights `10,10`, potential

```text
(11, 1, -7/3),
```

and positive supersolution

```text
psi=(1,2,3).
```

Although the third local potential is negative, the exact Barta ratios are

```text
(H psi)_i / psi_i = 1, 1, 1.
```

Thus the complete graph base satisfies `H>=I`.

The polar source vectors are

```text
u_plus  = (2,0,1),
u_minus = (0,2,1),
a       = 2.
```

They decompose as

```text
c=(u_plus+u_minus)/2=(1,1,1),
s=(u_plus-u_minus)/2=(1,-1,0),
```

and the exact polar matrix is

```text
2a c c^T - 2a s s^T.
```

At target floor `lambda=1/2`, the base resolvent scalar is

```text
<s,(H-lambda I)^-1 s> = 404/1961.
```

Hence

```text
2a * resolvent = 1616/1961 < 1,
```

and T-15401 certifies the complete polar-corrected matrix above `1/2`.

The crude norm estimate would give

```text
1 - 2a ||s||^2 = -7,
```

so the exact scalar gate is materially stronger.

## Exact identities checked

The checker reconstructs:

- every positive jump edge and graph Laplacian entry;
- every pointwise Barta ratio;
- the exact ground-state representation on a nontrivial test vector;
- the signature identity
  `a(u+u-*+u-u+*)=2a(cc*-ss*)`;
- exact positive LDL pivots for `H-lambda I`;
- the exact odd resolvent solve;
- the strict Birman--Schwinger comparison;
- exact positive LDL pivots for the final dense matrix minus `lambda I`.

No supplied matrix, inverse, pivot, or verdict is trusted.

## Reproduction

```bash
python verify.py certificates/synthetic.json \
  --output results/synthetic-verification.json
python -m unittest discover -s tests -v
```

Nine adversarial tests pass.

## Mutation coverage

The tests reject:

- Boolean dimensions;
- duplicate edges;
- nonpositive supersolutions;
- a false Barta floor;
- a false resolvent value;
- a polar coefficient that violates the rank-one gate;
- exact equality at the Birman--Schwinger boundary;
- malformed certificate data.

## Continuum production adapter

A future Suzuki certificate must replace the finite graph data with:

1. the cancellation-safe continuous kernel `K_a`;
2. a complete prime-shift manifest;
3. the exact local potential `V_a`;
4. an exact positive rational spline;
5. a partition proving the pointwise Barta residual on every cell;
6. one ambient upper enclosure of the odd `sinh` resolvent scalar.

The standard-library checker should consume only rational interval summaries;
special functions and quadrature remain producer responsibilities.

## Proof boundary

The retained result concerns a finite synthetic rational matrix.  It does not
evaluate the Riemann zeta function, Suzuki's kernel, or a localized Weil form.
No RH conclusion is drawn from X-15401 itself.
