# X-103120 — QPTI Euler–Beta reduction replay

Run:

```bash
python experiments/X-103120-qpti-euler-beta/verify.py
python -O experiments/X-103120-qpti-euler-beta/verify.py
```

Expected verdict:

```text
PASS_T103120_QPTI_EULER_BETA_REDUCTION
1be3d2b1484aef51e8661fe49ac95fb062249d1238b003d6c8ad1991075bb4e5
```

The checker verifies finite Boolean Vaughan algebra, canonical equal-pair
shares, the Euler–Beta transform, and a nonzero two-prime-core owner mode.  It
explicitly records that neither QPTI nor RH is proved.
