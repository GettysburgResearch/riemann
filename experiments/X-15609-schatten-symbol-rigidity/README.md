# X-15609 — Exact Schatten symbol-rigidity regression

This standard-library-only experiment verifies the finite arithmetic behind
`L-15623`.

It checks the exact decomposition

```text
symbol moment excess
 = symbol-to-operator slack
 + packet flatness/Jensen slack
 + uncaptured Schatten tail,
```

and two strict synthetic cases.

## Passing case

```text
G=3, alpha=1, Gamma=2, t=3/2, r=2, d=2
D spectrum = 2, 2, 1/2, 1/4
A=G I-D   = 1, 1, 5/2, 11/4.
```

The proof object deliberately includes symbol/KSS slack `1/10`. It certifies

```text
symbol slack             1/10
packet flatness slack    0
uncaptured moment        5/16
total symbol excess      33/80
right side               1.
```

The exact low counts below both `t` and `Gamma` are two.

## Extra-low-mode case

Replace the third deficit eigenvalue by `8/5`. Then the third operator
eigenvalue is `7/5<t`. The exact Schatten excess is

```text
1049/400 > (G-t)^2 = 9/4 > (G-Gamma)^2 = 1.
```

Thus one additional low mode forces strict failure by more than a complete gap
quantum.

Run:

```bash
python experiments/X-15609-schatten-symbol-rigidity/verify.py
```

Expected verdict:

```text
PASS_EXACT_L15623_SCHATTEN_DEFECT_DECOMPOSITION
```

Proof-object SHA-256:

```text
d09e07eaf0ce0e185fe7ecaf45e820aa0aba43d60c6c9558d1ff413573a86d5c
```

This is an exact synthetic regression. It does not evaluate Suzuki's symbol,
prove the positive cofinal symbol inequality, or prove RH.
