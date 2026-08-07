# X-15407 — Exact eta-window and reflection algebra

Status: exact finite algebraic regression; no zeta evaluation  
Agent: `gpt56-05-l`  
Claims: `L-15414`, `L-15415`

## Purpose

This checker verifies two new positive-route reductions without trusting
floating arithmetic.

1. At `h=log 2`, the pole-annihilating triangular hinge polynomial is

   ```text
   (1-r)^2(1-sqrt(2) r).
   ```

   The checker works in the exact quadratic field `Q(sqrt(2))`, verifies the
   constant and linear moments, the pole root `r=1/sqrt(2)`, and

   ```text
   h ||G_h||_2^2 = 2-sqrt(2)/3.
   ```

2. The functional-equation reflection identity

   ```text
   F(1-s)=-F(s)-X(s),
   F(s)F(1-s)=-F'(s)-zeta''(s)/zeta(s)-X(s)F(s)
   ```

   is replayed on exact rational synthetic data. A finite synthetic Selberg
   stream checks the coefficient formula

   ```text
   A(n)=Lambda(n) log(n)+(Lambda*Lambda)(n)>=0.
   ```

## Retained result

The exact hinge coefficients are

```text
1,
-2-sqrt(2),
1+2sqrt(2),
-sqrt(2).
```

The retained reflection control has

```text
F=2,
X=3,
F'=7,
zeta''/zeta=-3,
F(1-s)=-5,
reflected product=-10.
```

The synthetic Selberg coefficients are

```text
0,1,4,3,9,4,0,2.
```

## Reproduction

```bash
python verify.py certificates/synthetic.json \
  --output results/synthetic-verification.json
python -m unittest discover -s tests -v
```

The connector environment did not expose a repository checkout or `gh`, so the
committed test module was not run directly in that environment. An independent
in-session `Fraction`/quadratic-field reconstruction replayed the retained
certificate and all six rejecting mutations successfully. The two remaining
unit cases are positive identity checks of the same replay.

## Proof boundary

X-15407 verifies finite algebra only. It does not evaluate `zeta`, prove the
critical Hardy bound, justify a contour displacement, or prove RH. In
particular, the eta/parity interpretation is a probability statement only for
real `s>1`; continuation of its contraction to the critical boundary remains
the RH-strength step.
