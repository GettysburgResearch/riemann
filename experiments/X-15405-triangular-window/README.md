# X-15405 — Exact triangular pole-free window regression

Status: exact finite synthetic regression  
Agent: `gpt56-05-l`  
Issue: #154  
Claims: `L-15409`, `T-15406`

## Purpose

The prior universal prime-window construction uses a smooth infinite
convolution. `L-15409` shows that a single normalized box convolved with itself
already suffices. After scaling by `h=log 4`, its pole-free two-shift window has
three linear pieces and transform

```text
((1-exp(-h z))/(h z))^2 * (1-2 exp(-h z)).
```

The first factor has zeros only on `Re z=0`; the second cancels the shifted zeta
pole at `z=1/2` and has its other zeros on `Re z=1/2`. No possible shifted
off-line zeta zero in `0<Re z<1/2` is canceled.

X-15405 checks the finite rational algebra after normalizing `h=1` and retaining
`q=2` symbolically through rational coefficients.

## Exact identities

The checker reconstructs

```text
(1-r)^2(1-2r)=1-4r+5r^2-2r^3.
```

It verifies:

- zero constant moment;
- zero linear moment;
- exact pole root at `r=1/2`;
- normalized piecewise-linear window
  ```text
  t,       0<=t<=1
  4-3t,   1<=t<=2
  2t-6,   2<=t<=3;
  ```
- exact normalized energy
  ```text
  integral G(t)^2 dt = 8/3;
  ```
- a nontrivial direct window contraction against three positive rational events;
- equality with the four-value cumulative-hinge replay.

The retained synthetic evaluation is

```text
direct value              1/15
finite-difference value   1/15.
```

## Reproduction

```bash
python verify.py certificates/synthetic.json \
  --output results/synthetic-verification.json
python -m unittest discover -s tests -v
```

Eight adversarial tests pass locally.

## Production adapter

For real prime powers, a directed producer needs only:

1. exact `h=log 4` enclosure;
2. the complete annulus `exp(x-3h)<=n<=exp(x)`;
3. directed comparisons locating every `x-log n` in one of three pieces;
4. affine outward evaluation and directed accumulation;
5. an independent replay from the cumulative hinge sum `K` at
   `x,x-h,x-2h,x-3h`;
6. exact piecewise integration of the square for mean-square blocks.

## Proof boundary

This checker verifies finite rational window algebra only. It does not evaluate
zeta, prime powers, a Laplace transform, or an RH-valid mean-square bound.
