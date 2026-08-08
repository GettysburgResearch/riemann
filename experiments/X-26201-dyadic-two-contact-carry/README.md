# X-26201 — Consolidated dyadic two-contact and factor-five source replay

This standard-library package supports:

```text
L-26201--L-26205
R-26201
L-26901--L-26904
R-26901
T-26902
M-26901/M-26902
```

The exact scripts use integers and `fractions.Fraction`. `recon.py` uses
60-digit `decimal.Decimal` arithmetic and is explicitly discovery-only.

## Run the exact consumers

```bash
python3 verify.py
python3 verify_bottom_charge.py
python3 verify_digital_lift.py
python3 verify_factor_five.py
python3 verify_schur_structure.py
python3 verify_positive_synthesis.py
python3 verify_moment_tower.py
```

The unit-test front door is

```bash
pytest -q tests/test_verify.py
```

## 1. Core two-contact / Green replay

`verify.py` checks:

1. `1*b_2=epsilon-delta_2`;
2. the pointwise two-contact identity;
3. the averaged affine/rank-one carry row in 12,879 cells;
4. formal Kummer identities;
5. the reflected cross term and carry-square norm;
6. signed carry-residual pairing;
7. the dyadic valuation layers;
8. `Gbar_X b_2=-3e_2+e_3` and energy five;
9. the exact inverse formula through dimension 17;
10. the adjacent-flow potential.

Retained digest:

```text
dd6f66f1e026178c1277f2fa634671d8868219e0303db505d9f0547df5eb0715
```

## 2. Bottom-charge and flow-invisibility replay

`verify_bottom_charge.py` checks

```text
sum_q b_2(q)v_q(b)=-2b(2)+b(3)
```

and

```text
sum_q b_2(q)Delta_Fv_q=3F_2-F_3.
```

Arbitrary nonzero flows supported at indices `j>=4` are verified to be invisible
to the dyadic source.

Retained digest:

```text
395a7a89ea2267cfa5a3b805ead2646fa46a1761408f6ff048fed7b2e218757f
```

## 3. Exact digital half-scale lift

`verify_digital_lift.py` checks

```text
chi_(2n+1,2q)(2j+epsilon)=chi_(n,q)(j)
beta_(2n+1,2q)=beta_(n,q)
```

in 3,780 pointwise cells, 1,830 averaged cells, 60 Hermitian isometries, and
72 lifted packing columns. The incorrect even-row mutation is rejected.

Retained digest:

```text
17e23d1e2ebc01cc7283d125c15c721d4743e69f906b17b715294f60b0e09b23
```

## 4. Factor-five pointwise wavelet

`verify_factor_five.py` checks

```text
Y_(n,m)(j)
 =1_(m<=n<2m)-1_(m<=j<2m)-1_(m<=n-j<2m)
```

and

```text
Z_(n,m)(j)=g_m(n)-g_m(j)-g_m(n-j)
g_m=1_[m,2m)-(1/2)1_[2m,4m).
```

It replays:

```text
scaled b_2 box cells                         386,270
pointwise omega_2 wavelet cells              386,270
pointwise inner/outer sign cells              71,610
factor-five Kummer product cases               2,505
far-field monotonicity products                2,940
odd-Mobius pointwise carry cells              13,040
```

Actual negative transition examples are retained. The script verifies that every
negative ordinary-log Kummer row lies in `2m<=n<5m`.

Retained digest:

```text
b2ff53b948da65a81082fa9a14d7f990c227bb47a6bb592458655ccec7a03f95
```

## 5. Uniform carry Schur structure

`verify_schur_structure.py` checks the finite combinatorial inputs to
`L-26902` through 113,515 rows:

```text
n range                              210..520
maximum source breaks               <=6
long constant-source run            present
required reserve denominator        <=60,000,000
```

Retained digest:

```text
fe8287748e6c2e7320ca24e8db827044d77511dc2a72e401afb91a90e11365f0
```

The elementary proof in `L-26902`, not finite enumeration, supplies the all-row
theorem.

## 6. Positive inverse and generalized-prime synthesis

`verify_positive_synthesis.py` checks:

```text
a_omega*omega_2=epsilon
Lambda_omega=omega_2*(a_omega log)
positive generalized-prime coefficients
P_n=sum_m a_omega(m)log(m)Z_(n,m)
digital correction to ordinary Kummer
```

with every synthesis cross term retained.

Retained digest:

```text
11e5e76a49b49ab2f838d7a829936b4e46bed5482c0d0a717fb4161f6b99eeda
```

## 7. Selberg–carry moment tower and boundary firewall

`verify_moment_tower.py` uses a formal positive completely additive logarithm and
checks exactly:

```text
omega_2*a_omega=epsilon
omega_2*(a_omega log)=Lambda_omega>=0
omega_2*(a_omega log^2)
 =Lambda_omega log+Lambda_omega*Lambda_omega>=0
```

and, in 2,698 pointwise carry cells,

```text
sum_m a_omega(m)Z_(n,m)(j)=0
sum_m a_omega(m)log(m)Z_(n,m)(j)>=0
sum_m a_omega(m)log(m)^2Z_(n,m)(j)>=0.
```

It also finds 411 cells with a nonzero `m=1` source contribution and verifies
that deleting that boundary destroys the zeroth-moment identity. A dyadic source
coefficient mutation is rejected.

Retained digest:

```text
eaaed5595e09e6b7d0f9fd990f42bea3e99d4c4e180fd04d78b7d2fa8434c2af
```

## 8. Discovery-only carry-inverse reconnaissance

Run:

```bash
python3 recon.py
```

At endpoints

```text
100, 250, 500, 1000, 2000, 5000
```

the 60-digit reconnaissance found every nonterminal inverse coefficient
positive and reconstructed selected columns to about 57 decimal places.

Retained discovery digest:

```text
7a249c5a00cb1e5c6daa0434bcbdc40efef890f381f2ae1eb52091e8557f001e
```

This is not an interval certificate and is not promoted to Carry Saturation,
Bottom-Charge Positivity, or RH.

## Proof boundary

The package certifies exact finite/filter algebra only. It does **not** certify:

- the independent-frequency physical quotient-cell matrices;
- the physical-to-carry transference map;
- preservation of the carry Schur reserve in physical space;
- the finite `n<210` production boundary;
- `F5TC`;
- Bottom-Charge Positivity;
- Dyadic Signed Slack;
- a shell-energy recurrence;
- the Riemann Hypothesis.

The consolidated mathematical and review front doors are `T-26902` and
`M-26902`.
