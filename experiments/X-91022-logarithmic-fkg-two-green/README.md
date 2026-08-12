# X-91022 — Logarithmic-integer FKG and centered two-Green reserve

This exact replay checks:

- the finite logarithmic Jordan domination
  \[
  A_s(N)/H_N\ge\prod_{p\le N}(1-p^{-1-s})
  \]
  for integer `s=1,2,3,4` and `N<=500`;
- strict nontrivial gap controls;
- the divisor expansion
  \[
  F_s(n)=\sum_{d\mid n}\mu(d)d^{-s}.
  \]

Run:

```bash
python3 verify.py --json /tmp/verification.json
cmp /tmp/verification.json results/verification.json
sha256sum -c SHA256SUMS
```

Expected verdict:

```text
PASS_LOGARITHMIC_INTEGER_FKG_TWO_GREEN
```

The replay verifies finite exact arithmetic only. The Harris–FKG conditioning
argument and Bernstein/Laplace transfer are written proofs. The experiment does
not remove the final Green division and does not prove RH.
