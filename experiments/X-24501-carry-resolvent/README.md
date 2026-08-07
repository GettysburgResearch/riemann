# X-24501 — Exact carry-resolvent algebra regression

Status: **finite exact algebra only**

Run:

```bash
python3 verify.py
```

The checker uses only the Python standard library and `fractions.Fraction`.
It verifies:

```text
carry-count rows                         8,128
beta/continuum comparison rows           8,128
finite transform telescopes                256
rational partial-fraction rows              30
greedy rational levels                      39
greedy feasibility constraints              780
critical Abel mass                            8
mutations                                  8/8 PASS
```

Retained verdict:

```text
PASS_EXACT_L24501_L24502_CARRY_RESOLVENT_ALGEBRA
```

Proof-object SHA-256:

```text
5638de49fc82948f1d411b20d85894ca04d6d7625f7627511173ed35cb47c916
```

## What it checks

1. the floor-sum and closed forms for `beta_(nq)`;
2. the exact positive error `b(n/q)-beta_(nq)`;
3. the bound `0<=b-beta<=2/q`;
4. finite telescoping behind the continuum carry transform;
5. the rational partial fraction producing the Möbius state;
6. the removable critical mass `G(1/2)=8` at the rational-prefactor level;
7. deterministic greedy feasibility for rational synthetic targets.

## What it does not check

- evaluation or continuation of zeta;
- positivity of the continuum inverse;
- the actual logarithmic/square-root target by directed arithmetic;
- Discrete Carry-Resolvent Stability;
- the prime-ramp asymptotic;
- the square-screw normalization;
- RH.

The synthetic greedy targets test only algorithmic residual orientation. A
production DCRS artifact must use the actual target

```text
w_X(q)=q^(-1/2) log(X/q)
```

with directed enclosures and an unbounded symbolic theorem.
