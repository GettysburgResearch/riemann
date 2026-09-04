# Independent numerical and finite replays

> [!CAUTION]
> The original constants below remain accurately reproduced, but that does not
> validate the proof. A later hostile review found an uncancelled positive
> `B^2 log B/800` term in Proposition 9.5's max-summand majorant. Read
> `DEEP_HOSTILE_REVIEW.md` and `HEIGHT_BOUND_COUNTERCHECK.md` first.

```text
Status: NON_PROOF_DIAGNOSTICS
Original script: diagnostics/catalan_audit_replay.py
Original output: diagnostics/replay.json
Hostile script: diagnostics/catalan_height_hostile_replay.py
Hostile output: diagnostics/height_hostile_replay.json
```

## Purpose

The paper says that AI produced numerical data needed by the proof, but no
program or cell table accompanies the attached v1 PDF. The first replay
independently implements several displayed formulas to test consistency. The
second evaluates a compulsory term in the largest-summand majorant used by
Proposition 9.5.

Neither is a proof certificate:

- SciPy quadrature is not directed interval arithmetic;
- the finite searches are bounded;
- the exact 178-cell and 235-cell partitions are not reconstructed;
- floating logarithms do not prove asymptotic identities;
- the proof-level height obstruction is analytic, not computational.

## 1. Original final-margin arithmetic

The original script uses the paper's rigorous-facing endpoints:

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

This confirms only the final subtraction. The new review shows that a larger
positive `B^2 log B` term is missing before this finite `B^2` coefficient is
reached.

## 2. Odd-small-prime replay

The script implements equations (6.2)--(6.21):

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

This is strong consistency evidence, not validation of the claimed directed
Euler--Maclaurin enclosure.

## 3. Middle-prime replay

The script implements equations (7.7)--(7.13) directly:

- floor parameters `a`, `k`, `b`;
- six residue-coordinate boundaries;
- all marginal levels in (7.11)--(7.12);
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

## 4. Finite check of the saturation reduction

The original script checks the left side minus the right side of (5.21) for:

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

This supports the repaired local theorem in the intended regime but does not
address the failed global archimedean/local compatibility.

## 5. Cutoff diagnostic

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

Thus the literal `5B` support cutoff in Lemma 5.5 is false. A safe `O(B)`
cutoff can preserve the intended subquadratic order, but that repair does not
remove the Proposition 9.5 obstruction.

## 6. Hostile max-summand replay

The pure-standard-library script

```text
diagnostics/catalan_height_hostile_replay.py
```

uses the consecutive-row ideal model, the subset

\[
I_0=\{0,1,\ldots,S-1\},
\]

and the two-term lower bound

\[
T_m>
\frac1{(2m+1)^2}-\frac1{(2m+3)^2}.
\]

It evaluates the expression obtained after exact cancellation of the odd
`a_Q` baseline in the max-summand majorant. For `S=floor(B/20)`:

| B | S | one-term lower bound / B^2 |
|---:|---:|---:|
| 100 | 5 | 1.821777816169270 |
| 200 | 10 | 1.849984814303233 |
| 300 | 15 | 1.865521107324622 |
| 500 | 25 | 1.874889547532234 |
| 1000 | 50 | 1.884184990849831 |
| 1500 | 75 | 1.886035510685781 |

The finite values are consistent with the proof-level finding that the
majorant is not a negative finite multiple of `B^2`. They are not intended to
numerically reveal the very slowly dominant coefficient `1/800` after all
quadratic terms; the analytic countercheck proves that leading coefficient
directly.

## 7. Reproduction

Original replay:

```bash
python3 diagnostics/catalan_audit_replay.py \
  --pdf /path/to/2609.04176.pdf \
  --max-b 300
```

Hostile replay:

```bash
python3 diagnostics/catalan_height_hostile_replay.py \
  --output /tmp/height_hostile_replay.json
```

Frozen environments:

```text
Python 3.13.5
SciPy 1.17.0 for the original replay
standard library only for the hostile replay
```

## Final interpretation

```text
The paper's finite constants are numerically plausible.
The local saturation inequality is strongly corroborated at finite scale.
The posted proof still fails at a larger leading-order term.
Correct finite constants do not repair an incorrect B^2 log B cancellation.
```
