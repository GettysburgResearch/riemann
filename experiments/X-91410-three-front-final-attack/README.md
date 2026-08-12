# X-91410 — Three-front final-attack replay

Run:

```bash
python3 verify.py --json /tmp/verification.json
cmp /tmp/verification.json results/verification.json
```

Retained verdict:

```text
PASS_X_91410_THREE_FRONT_FINAL_ATTACK
```

The replay checks:

- beta-binomial normalization and detailed balance;
- the exact Hahn polynomial diagonal and unit spectral gap;
- the score eigenfunction and product score-edge covariance identity;
- exact Green-density free-flight energy conservation;
- exact nonnegative arithmetic kick increments;
- the scalar algebra used in the `a>=1/4` Green-density theorem.

It does not prove the complete factor-54 margin, the arbitrary-phase Theta–DtN identity, the Green-density sign for every `0<a<1/4`, or RH.
