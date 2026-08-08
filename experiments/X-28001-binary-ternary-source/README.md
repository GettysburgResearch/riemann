# X-28001 — Binary–ternary source exact replay

Run

```bash
python experiments/X-28001-binary-ternary-source/verify.py
```

The checker uses only Python's standard library and exact integer/Fraction
arithmetic.

It verifies:

```text
third-Abel witness                     -91/256 at (Q,n)=(520,15)
fourth-Abel witness                    -84,999,795/2048 at (3559,15)
b_2 pointwise two-contact rows         5,148
bottom-charge synthetic target checks  20
omega_(2,3) floor identities           201
omega_(2,3) scaled wavelet identities  111,055
positive inverse identities            200
generalized-prime formal identities    200
```

It also reconstructs the complete bottom source tables in `L-28001/L-28002`.

Retained result digest, computed before inserting the digest field:

```text
c044d774fd7e60a71653064e419c6c3ca6d8825ab1a99e679a90c02307abe393
```

## Assurance boundary

The experiment proves finite algebra and the two exact negative Abel witnesses.
It does not prove:

```text
BTEBC;
the dyadic or binary–ternary bottom-charge sign;
physical-normal-to-carry transference;
any cofinal source recurrence;
the Riemann Hypothesis.
```
