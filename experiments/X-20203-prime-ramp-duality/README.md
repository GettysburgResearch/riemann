# X-20203 — Exact prime-ramp/autocorrelation replay

This experiment is the finite exact consumer for `L-20208` and `L-20209`.

It starts from a rational Fejer factor `Q`, constructs

```text
A(z)=(1-z)Q(z),
P(x)=|A(exp(ix))|^2=sum_k lambda_k(1-cos(kx)),
L_P(s)=sum_k lambda_k(k-s)_+,
```

and verifies, with integers and `fractions.Fraction` only:

- the factor autocorrelation and `lambda` coefficients;
- `L_P(m)=2 d_m` at every integer knot;
- linear interpolation of the ramp between knots;
- `L_P(0)=2 ||q||^2`;
- `L_P(1/2)=1/2 sum |q_j+q_(j-1)|^2>0`;
- the declared exact sample values and half-knot ratio.

The retained synthetic factor is

```text
Q(z)=1-2z+z^2,
A(z)=(1-z)^3,
lambda=(30,-12,2),
d=(6,-4,1,0),
L_P(1/2)/L_P(0)=1/6.
```

Local replay commands:

```bash
python3 verify.py certificates/synthetic.json
python3 -m unittest discover -s tests -v
```

Seven central/mutation tests pass. This is synthetic exact algebra only; no zeta
prime stream, cofinal sign, or RH conclusion is certified.
