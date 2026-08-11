# X-91024 — Corrected Green-removal threshold

This replay certifies the repaired large-scale theorem `L-91030` and the
one-switch normal form `L-91029`.

It checks:

- an exact rational lower certificate for `(2/3) zeta(5/3)>sqrt(2)`;
- the elementary derivative-tail constants used to prove monotonicity of
  `s zeta(1+s)` on `s>=2/3`;
- 606 exact rational instances of the three-scale partial-fraction identity;
- the unique one-switch root and zero total mass of the physical wavelet;
- the unit-atom terminal barrier at representative scales.

Run:

```bash
python3 verify.py --json /tmp/verification.json
cmp /tmp/verification.json results/verification.json
sha256sum -c SHA256SUMS
```

Expected verdict:

```text
PASS_CORRECTED_GREEN_REMOVAL_THRESHOLD
```

The replay proves finite/directed algebraic certificates only. It does not
prove the analytic monotonicity argument, the small-scale theorem, the
critical-boundary intertwiner, or RH.
