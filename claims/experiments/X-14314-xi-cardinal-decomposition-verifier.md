# X-14314 — Exact Xi-cardinal spectral-decomposition regression

Claim ID: `X-14314`  
Title: Gaussian-rational verification that normalized quotient cardinal functions isolate selected real zeros and split an indefinite zero-sum form exactly  
Status: `EMPIRICAL`  
Authoring agent: `gpt56-pro-09-c`  
Created: 2026-07-31  
Dependencies: the finite algebra in `L-14321`  
Scope: synthetic exact regression; no Riemann-Xi evaluation

The checker uses a real polynomial analogue of `Xi` with two selected simple
real zeros and one nonreal conjugate pair.  It constructs

```text
ell_gamma(z)=P(z)/[(z-gamma)P'(gamma)]
```

by exact synthetic division, verifies the Kronecker values at every root, and
checks the exact zero-sum decomposition

```text
Q(h,h)=sum_selected |h(gamma)|^2+Q(Rh,Rh).
```

The retained polynomial is

```text
P(z)=(z-1)(z-3)(z^2+1).
```

For `h(z)=z`, the full synthetic Weil form is `8`; the selected positive block
is `10`, and the off-real residual is `-2`.  Thus the cardinal splitting is
exact even when the remainder is genuinely indefinite.
