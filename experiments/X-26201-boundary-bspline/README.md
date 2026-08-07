# X-26201 — Exact boundary B-spline algebra

This standard-library replay verifies the finite algebra used by `L-26201` and
`L-26202`.

It checks:

- arithmetic in `Q(sqrt(2))`;
- the base source polynomial
  `R(x)=(1-2x)(1-sqrt(2)x)^2`;
- the finite forcing polynomial `D(x)=(1-2x)R(x)`;
- `epsilon*b=d` through 256 coefficient rows;
- positivity of the first 33 local inverse coefficients at the prime 2;
- 158 exact finite Euler-transform identities;
- a rational lower bound `eta(1/2)>1/2`, hence paired transport mass `<1`;
- five adversarial/unit controls.

Run:

```bash
python experiments/X-26201-boundary-bspline/verify.py
python -m unittest discover \
  -s experiments/X-26201-boundary-bspline/tests -v
```

The retained proof-object digest is

```text
cde8ac0d20702856c6fc0339d33861ec63aa819b237a1facbf4e49ff7353db69
```

## Scope

The checker certifies finite polynomial, convolution, inverse-coefficient, and
Euler identities only. It does not certify:

- the analytic convolution representation of the exponential B-spline;
- the source-specific reflected graph contraction `L-26203`;
- a cofinal block-energy bound;
- RH.
