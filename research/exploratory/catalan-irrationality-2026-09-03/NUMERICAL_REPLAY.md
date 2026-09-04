# Independent numerical and finite replay

```text
Status: NON_PROOF_DIAGNOSTIC
Script: diagnostics/catalan_audit_replay.py
Frozen output: diagnostics/replay.json
```

## Purpose

The paper says that AI produced numerical data needed by the proof, but no
program or cell table accompanies the attached v1 PDF. This replay
independently implements several displayed formulas to test consistency.

It is deliberately not called a certificate:

- SciPy quadrature is not directed interval arithmetic;
- the finite search is bounded;
- the exact 178-cell and 235-cell partitions are not reconstructed;
- Proposition 9.5's full ledger is not implemented.

## Exact final-margin arithmetic

The script uses the paper's rigorous-facing endpoints:

```text
c_odd <
0.006276744728100982604597600317605549

Lambda_mid >
0.17635583792

Delta_large = 83/2400
raw          = 39/200
```

It obtains

```text
-LHS correction + gains - raw
=
0.0096624265252323507287357330157277843...
```

which is strictly above

```text
0.00966242652523235.
```

Using the exact middle-prime fraction gives

```text
0.0096624265338806464283987760258952475...
```

with the same upper endpoint for `c_odd`.

## Odd-small-prime replay

The script implements equations (6.2)–(6.21):

- the floor functions and transformed residue coordinate;
- the finitely many constant pieces of `h_v(y)`;
- the marginal ladders `h_v(y)+2r`;
- the lowest-`1+v` mass functional `K_v(1+v)`;
- `Q_0(v)`;
- the Hurwitz-zeta integral.

The exact breakpoint union (6.24) gives:

```text
239 breakpoints
238 raw cells
```

matching the paper. Numerical integration cell by cell gives:

```text
I_odd  = -0.006276744728100986
c_odd  =  0.006276744728100986

displayed decimal:
          0.006276744728100982604597600317605548503...
absolute floating difference:
          3.47e-18
```

This is strong consistency evidence, not validation of the claimed
Euler-Maclaurin interval enclosure.

## Middle-prime replay

The script implements equations (7.7)–(7.13) directly:

- floor parameters `a`, `k`, `b`;
- six residue-coordinate boundaries;
- all marginal levels in (7.11)–(7.12);
- selection of the lowest `rho` measure;
- the row-factorial density `C_rho(t)`.

Adaptive integration over the primary floor-break intervals gives:

```text
numerical reconstruction:
0.17635583794457388

exact displayed fraction:
33042423784278900654572890582560690565493664595111
/
187362234062518051579626183549876762148305272280000

exact decimal:
0.17635583792864828...

absolute difference:
1.59e-11

summed quadrature error report:
6.28e-10
```

The result is consistent with the source. It is much weaker than exact
integration over the claimed 235 affine cells.

## Finite check of the saturation reduction

The script checks the left side minus the right side of (5.21) for:

```text
20 <= B <= 300
1 <= S <= floor(B/20)
all odd Q <= 2B+S+3
```

It checks all odd `Q`, not only prime powers:

```text
437661 cases
status: PASS
minimum observed difference: 29
at B=20, S=1, Q=31.
```

This supports the paper's inequality in the intended regime but is not an
all-`B` proof.

## Cutoff diagnostic

For the denominator layer in the full-row and ideal-row models:

```text
B = 100
S = 5
Q = 503

5B = 500
ideal upper row  = 204
actual upper row = 207

ideal layer  = 108
actual layer = 114
difference   = 6.
```

Thus a literal `5B` support cutoff is unsafe for the difference discussed in
Lemma 5.5. A safe `O(B)` cutoff, for example `7B` in the final regime, leaves
the asymptotic order unchanged.

## Reproduction

```bash
python3 diagnostics/catalan_audit_replay.py \
  --pdf /path/to/2609.04176.pdf \
  --max-b 300
```

The frozen run used:

```text
Python 3.13.5
SciPy 1.17.0
```
