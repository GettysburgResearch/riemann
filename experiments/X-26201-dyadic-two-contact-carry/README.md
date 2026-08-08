# X-26201 — Dyadic two-contact, factor-five dipole, and bottom-charge replay

This experiment package supports `L-26201`--`L-26205`, `L-26901`,
`R-26201`, `R-26901`, and the proposal `T-26201`.

It uses only the Python standard library. The exact scripts use integers and
`fractions.Fraction`; `recon.py` uses 60-digit `decimal.Decimal` arithmetic and
is explicitly discovery-only.

## Exact replay

Run:

```bash
python3 verify.py
python3 verify_bottom_charge.py
python3 verify_digital_lift.py
python3 verify_factor_five.py
```

`verify.py` checks:

1. the divisor convolution
   ```text
   1 * b_2 = epsilon - delta_2;
   ```
2. the pointwise carry collapse
   ```text
   sum_q b_2(q) chi_(n,q)(j)
     = -1_(j=1)-1_(j=n-1);
   ```
3. the averaged affine/rank-one carry row in 12,879 `(n,m)` cells;
4. Kummer's identity with a formal completely additive derivation;
5. the exact reflected cross term and carry-square norm;
6. the signed carry-residual pairing;
7. the dyadic valuation layers of `b_2`;
8. the full-divisor Green identity
   ```text
   Gbar_X b_2 = -3 e_2 + e_3,
   b_2^T Gbar_X b_2 = 5;
   ```
9. the exact closed formula for `Gbar_X^-1` through dimension 17;
10. the coefficient-space adjacent-flow potential and its `j^-2` envelope.

Retained proof-object SHA-256:

```text
dd6f66f1e026178c1277f2fa634671d8868219e0303db505d9f0547df5eb0715
```

`verify_bottom_charge.py` independently checks the divisor-gradient projection

```text
sum_q b_2(q) v_q(b) = -2 b(2)+b(3)
```

and the adjacent-flow identity

```text
sum_q b_2(q) Delta_F v_q = 3F_2-F_3.
```

It deliberately applies nonzero flows only at indices `j>=4` and verifies that
the dyadic source does not move.

Retained proof-object SHA-256:

```text
395a7a89ea2267cfa5a3b805ead2646fa46a1761408f6ff048fed7b2e218757f
```

`verify_digital_lift.py` checks the exact half-scale subsystem

```text
chi_(2n+1,2q)(2j+epsilon) = chi_(n,q)(j),
beta_(2n+1,2q) = beta_(n,q),
```

including 3,780 pointwise cells, 1,830 average cells, 60 exact Hermitian
isometries, and 72 lifted packing columns. The incorrect even-row mutation is
explicitly rejected.

Retained proof-object SHA-256:

```text
17e23d1e2ebc01cc7283d125c15c721d4743e69f906b17b715294f60b0e09b23
```

`verify_factor_five.py` checks the new source-specific localization:

```text
Y_(n,m)(j)
 =1_(m<=n<2m)-1_(m<=j<2m)-1_(m<=n-j<2m),

Z_(n,m)(j)
 =g_m(n)-g_m(j)-g_m(n-j),
g_m=1_[m,2m)-(1/2)1_[2m,4m).
```

It replays:

```text
scaled b_2 box cells                         386,270
pointwise omega_2 wavelet cells              386,270
pointwise inner/outer sign cells              71,610
exact factor-five Kummer product cases         2,505
far-field monotonicity products                2,940
odd-Mobius pointwise carry cells              13,040
```

The integer product comparison verifies that every negative logarithmic Kummer
row is confined to `2m<=n<5m`. It also records actual negative transition
examples, so a false claim of all-row positivity fails closed.

Retained proof-object SHA-256:

```text
b2ff53b948da65a81082fa9a14d7f990c227bb47a6bb592458655ccec7a03f95
```

## Finite reconnaissance

Run:

```bash
python3 recon.py
```

The script reconstructs the exact triangular carry inverse from the
Möbius-adjoint formula using 60 decimal digits. At endpoints

```text
100, 250, 500, 1000, 2000, 5000
```

all nonterminal coefficients were positive, and selected columns reconstructed
the target to approximately 57 decimal places.

Retained reconnaissance SHA-256:

```text
7a249c5a00cb1e5c6daa0434bcbdc40efef890f381f2ae1eb52091e8557f001e
```

This is not an interval certificate and is not promoted to Carry Saturation.

## Tests

```bash
pytest -q tests/test_verify.py
```

The test file contains four exact replay groups.

## Proof boundary

The package verifies exact finite algebra only. It does **not** prove:

- the factor-five transition normal-Gram contraction;
- Dyadic Signed Slack (`DSS`);
- Parity Blocker Descent (`PBD`);
- positivity of the carry inverse for every endpoint;
- a Green-to-physical-normal transference;
- the Riemann Hypothesis.

The original description of unsigned odd-column leakage as the sole obstruction
is corrected by `R-26901`: its signed load is automatically polylogarithmic,
while the odd target remains RH-bearing. The preferred next object is the
complete opposite-parity transition block `2m<=n<5m`.
