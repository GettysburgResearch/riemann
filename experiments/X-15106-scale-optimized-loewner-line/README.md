# X-15106 — Exact scale-optimized canonical-ray checker

Experiment ID: `X-15106`  
Associated theorem: `L-15120`  
Status: exact finite arithmetic and synthetic controls; no Riemann production data

## Purpose

The old nodewise proximity criterion compared the arithmetic target-pinned
matrix only with `Q_can`.  That is not scale invariant.  This checker verifies
the corrected certificate

```text
||T_p(c)-a Q_can||_infinity < a m_can,
a > 0,
```

where `m_can` is a certified lower moat of the canonical matrix on `p^perp`.
Every calculation uses Python integers and `fractions.Fraction`.

## Checked objects

The verifier reconstructs:

1. the canonical source directly from the target coefficients;
2. the canonical Loewner matrix and its exact target kernel;
3. a rational lower moat through complement `LDL^T`;
4. the arithmetic special matrix from its source values;
5. the exact target-pinned matrix at the declared boundary scalar;
6. the complete matrix difference from `a Q_can`;
7. the maximum absolute row-sum bound;
8. an independent exact `LDL^T` pass of the arithmetic matrix on `p^perp`.

It rejects a nonpositive scale, false moat, malformed rationals, zero target
coordinates, normalization drift, and certificates whose scaled difference
reaches the moat.

## Retained exact control

```text
nodes                  (-1,0,1)
p                      (1/3,1/3,1/3)
canonical source       (3,0,-3)
positive eigenvalues   9,9
certified moat          8
arithmetic source      (12,5,-2)
canonical scale         3
boundary scalar         2
T_p(2)                  3 Q_can exactly
scaled row error        0
scaled moat             24
arithmetic LDL pivots   54, 81/2
```

The same certificate has unscaled row difference `24 > 8`, so it is an exact
regression showing that the fixed-scale criterion can reject a perfect passing
completion.

Proof-object SHA-256:

```text
d13e9f4bf7178c356f87cba37bbea8569e531075d809aae17e2e146ed154c4ab
```

## Reproduction

```bash
cd experiments/X-15106-scale-optimized-loewner-line
python3 verify.py certificates/scaled-exact-pass.json
python3 -m unittest discover -s tests -v
```

## Proof boundary

The retained certificate is synthetic.  A Riemann production certificate must
supply directed smooth-window coefficients, a directed canonical moat, and the
actual arithmetic source of `L-15119` in the same normalization.