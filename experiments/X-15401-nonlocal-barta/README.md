# X-15401 — Exact signed-edge Barta and polar-rank regression

Status: exact finite synthetic regression; continuum Suzuki producer pending  
Agent: `gpt56-05-l`  
Issue: #154  
Claims: L-15401, L-15402, T-15401

## Purpose

The positive RH route needs lower bounds for the **complete** localized Weil
operator, not only positive finite Ritz matrices. L-15401 rewrites Suzuki's
scaled form as

```text
positive continuous and prime jump form
+ explicit local potential
+ positive cosh rank one
- negative sinh rank one.
```

L-15402 shows that odd parity strengthens this to an exact positive
**signed-edge** representation: ordinary edges use `|f_i-f_j|^2`, while
cross-origin edges use `|f_i+f_j|^2`. The same positive supersolution controls
both signs because the sign remains in the nonnegative transformed edge square.

T-15401 supplies an alternative full-space route: a Barta floor for the Markov
base plus one Birman--Schwinger scalar for the negative polar channel.

X-15401 verifies both finite algebraic mechanisms using Python integers and
`fractions.Fraction` only.

## Synthetic model

The graph has three vertices, two edge weights `10,10`, and signs

```text
(+1,-1),
```

so the second edge contributes `10|f_1+f_2|^2`. The potential is

```text
(11, 1, -7/3),
```

and the positive supersolution is

```text
psi=(1,2,3).
```

Although the third local potential is negative, the exact signed-edge Barta
values are

```text
1, 1, 1.
```

The local values are sign-independent; the negative edge sign appears only in
the nonnegative transformed remainder. Thus the complete signed graph base is
bounded below by `1`.

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
The final exact shifted LDL pivots are

```text
41/2, 1665/82, 125/666.
```

The crude norm estimate would give

```text
1 - 2a ||s||^2 = -7,
```

so the exact scalar gate is materially stronger.

## Exact identities checked

The checker reconstructs:

- every positive edge weight and its sign;
- the signed dense matrix;
- every sign-independent local Barta value;
- the exact signed-edge ground-state identity on a nontrivial vector;
- the polar signature identity
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
python -m compileall -q verify.py tests
```

Ten adversarial tests pass.

## Mutation coverage

The tests reject:

- Boolean dimensions;
- duplicate edges;
- an invalid edge sign;
- nonpositive supersolutions;
- a false Barta floor;
- a false resolvent value;
- a polar coefficient that violates the rank-one gate;
- exact equality at the Birman--Schwinger boundary;
- malformed certificate data.

## Continuum production adapters

A future full-space Suzuki certificate must replace the graph data with:

1. the cancellation-safe continuous kernel `K_a`;
2. a complete prime-shift manifest;
3. the exact local potential `V_a`;
4. an exact positive rational spline;
5. a partition proving the pointwise Barta residual on every cell;
6. one ambient upper enclosure of the odd `sinh` resolvent scalar.

The stronger odd-only adapter instead uses the exact signed-edge channels of
L-15402 and requires no polar resolvent.

The standard-library checker should consume only rational interval summaries;
special functions and quadrature remain producer responsibilities.

## Proof boundary

The retained result concerns a finite synthetic rational matrix. It does not
evaluate the Riemann zeta function, Suzuki's kernel, or a localized Weil form.
No RH conclusion is drawn from X-15401 itself.
