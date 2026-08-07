# X-26201 — Dyadic two-contact carry and bottom-charge replay

This experiment package supports `L-26201`--`L-26204` and the proposal
`T-26201`.

It uses only the Python standard library. The exact scripts use integers and
`fractions.Fraction`; `recon.py` uses 60-digit `decimal.Decimal` arithmetic and
is explicitly discovery-only.

## Exact replay

Run:

```bash
python3 verify.py
python3 verify_bottom_charge.py
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

## Proof boundary

The package verifies exact finite algebra only. It does **not** prove:

- Dyadic Signed Slack (`DSS`);
- Parity Blocker Descent (`PBD`);
- positivity of the carry inverse for every endpoint;
- a Green-to-physical-normal transference;
- the Riemann Hypothesis.

The load-bearing open scalar is

```text
Pi_2^gr(X) = sum_q b_2(q) s_X^gr(q)
           = -3 T_X(2)+T_X(3).
```
