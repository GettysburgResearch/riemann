# X-98900 — Fractional pole carrier and phased Tao separator

This exact standard-library replay checks the two finite trust-boundary facts
used by `L/R-98900` and `L/R-98901`:

1. at `theta=1/384`, the unavoidable pole-carrier energy exponent `1/2`
   strictly exceeds the claimed exponent `96 theta=1/4`;
2. at `P={3}`, `x=3`, `tau=pi/log 3`, the unphased Tao diagonal is `8/9`,
   the phased off-diagonal is `4/3`, and the Schur determinant is `-80/81`.

The checker uses `fractions.Fraction` only after JSON parsing. It does not
machine-prove the Hankel-contour asymptotic in `L-98900`; that is an analytic
theorem.

## Replay

```bash
python3 experiments/X-98900-fractional-pole-carrier/verify.py \
  experiments/X-98900-fractional-pole-carrier/certificates/control.json \
  --output /tmp/x98900.json

cmp /tmp/x98900.json \
  experiments/X-98900-fractional-pole-carrier/results/verification.json

python3 -m unittest discover \
  -s experiments/X-98900-fractional-pole-carrier/tests -v
```

Expected verdict:

```text
PASS_X98900_FRACTIONAL_POLE_AND_PHASE_FIREWALLS
```

Proof object:

```text
7fd8db1695fa966316cf127b6a4958a1625d9fbcc334fbf512a6147ea79dbd37
```

RH is not established.
