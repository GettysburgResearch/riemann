# X-14307 — exact prolate source and radical-tail regression

This directory implements the finite rational algebra used by `L-14312` and
`L-14313`. It is a synthetic checker, not a prolate-function evaluator and not
a Riemann-hypothesis computation.

The checker uses only Python integers and `fractions.Fraction` after parsing.
It verifies two independent kernels.

## Three-mode source kernel

For exact mode data

```text
v_j   = p_j(0),
m_j   = chi_j v_j,
a     = v cross m,
```

it reconstructs `a`, checks

```text
sum a_j v_j = 0,
sum a_j m_j = 0,
```

and evaluates the normalized Fourier-leakage square

```text
2 sum a_j^2 (1-chi_j) / sum a_j^2.
```

The retained exact control gives

```text
a                              = (-3/5, 3/5, -1/5)
normalized leakage squared     = 6/19
first-excluded-mode bound       = 3/5
```

## Radical-tail quotient kernel

For a rational symmetric form with a declared radical vector `r=k+t`, the
checker verifies

```text
Q(k,g) = -Q(t,g),
Q(k,k) = Q(t,t),
```

on the localized coordinate basis. It then computes the weighted projective
residual in two exactly equivalent ways:

```text
inf_c ||A k-c k||_(W^-1)^2
```

and the weighted dual over the ordinary annihilator of `k`. The retained
control gives `4/11` by both routes.

## Reproduction

From this directory:

```bash
python3 -m py_compile verify.py tests/test_verify.py
python3 -m unittest discover -s tests -v
python3 verify.py certificates/synthetic-exact.json \
  --output results/synthetic-exact-verification.json
sha256sum -c SHA256SUMS
```

Eight adversarial tests cover eigenvalue-order drift, a vanishing cross product,
false leakage, a false radical, nonsymmetry, an indefinite weight, and Boolean
rational contamination.

## Proof boundary

The checker does not establish:

- that any supplied row is a genuine prolate mode;
- the CCM or Connes--Consani source normalization;
- smooth/Schwartz approximation of a compactly supported prolate packet;
- any special-function enclosure;
- any asymptotic lower spectral floor;
- RH.

Those are analytic and provenance gates outside this finite kernel.
