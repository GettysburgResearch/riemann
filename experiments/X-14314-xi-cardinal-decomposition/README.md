# X-14314 — Exact Xi-cardinal decomposition regression

This checker verifies the finite algebra behind `L-14321` with exact rational
and Gaussian-rational arithmetic.

It uses

```text
P(z)=(z-1)(z-3)(z^2+1)
```

as a synthetic completed-Xi analogue.  For each selected simple real root it
constructs

```text
ell_gamma(z)=P(z)/[(z-gamma)P'(gamma)]
```

and verifies that it is one at the selected root and zero at every other real
or nonreal root.

For `h(z)=z`, the synthetic zero-sum form has

```text
global form              8
selected positive block  10
nonreal residual         -2
```

and the decomposition is exact.  This demonstrates that the selected cardinal
block remains positive and orthogonal even when the unselected residual is
indefinite.

Production classification is rejected without a typed gate binding the actual
Riemann-Xi kernel, simple-zero enclosures, Weil zero-sum normalization, and
localization tails.
