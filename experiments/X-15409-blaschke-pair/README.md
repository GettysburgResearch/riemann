# X-15409 — Exact Blaschke-pair Hankel pressure

Status: exact finite rational regression  
Agent: `gpt56-05-l`  
Issue: #180  
Claims: `L-15420`, `T-15408`, `R-15403`

## Purpose

For upper-half-plane points with the same real part,

```text
p=x+i(delta-omega),
q=x+i(delta+omega),
0<omega<delta,
```

the isolated unimodular symbol

```text
conj(b_p) b_q
```

has exact rank-one Hankel pressure

```text
||H|| = omega/delta
```

and exact Toeplitz coercivity floor

```text
inf ||Tf||^2/||f||^2 = 1-(omega/delta)^2.
```

X-15409 verifies these identities with Python integers and
`fractions.Fraction` only.

## Retained controls

### Interior pair

```text
delta             3/10
omega             1/10
y_minus           1/5
y_plus            2/5
Hankel norm        1/3
Hankel norm^2      1/9
Toeplitz floor     8/9
```

### Near-crossing pair

```text
delta             3/10
omega             29/100
y_minus           1/100
y_plus            59/100
Hankel norm        29/30
Hankel norm^2      841/900
Toeplitz floor     59/900
```

The second case displays the exact collapse as `omega` approaches `delta`.

## Reproduction

```bash
python verify.py certificates/synthetic.json \
  --output results/synthetic-verification.json
python -m unittest discover -s tests -v
```

## Proof boundary

This experiment checks the isolated finite Hardy-space factor only. It does not
locate a Riemann zero and does not prove or disprove the existence of the full
uniform Hankel moat. The transition from one isolated factor to Suzuki's full
scattering symbol uses the same-ordinate grouping and reproducing-kernel
localization in `L-15419/L-15420`.
