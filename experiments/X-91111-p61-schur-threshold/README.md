# X-91111 — P61 Boolean forcing and the strict rough Schur threshold

Companion replay for `L-91320`.

```bash
python3 experiments/X-91111-p61-schur-threshold/verify.py
sha256sum -c experiments/X-91111-p61-schur-threshold/SHA256SUMS
```

Expected verdict:

```text
PASS_FACTOR54_P61_BOOLEAN_AND_SCHUR_THRESHOLD
```

The standard-library checker uses exact integer and `Fraction` arithmetic with
directed rational square-root enclosures. It certifies:

- global positivity of both equality and reserve Boolean forcings after
  absorbing every prime through `61`;
- all `262,144` activation cells;
- the exact rough renewal beginning at prime `67`;
- the finite endpoint-port mass bound below `14/3`;
- the sharp reserve gate
  `p^(-1/2)(1-p^(-1/2)) < 1/9` for every `p>=67`.

The replay proves finite gates and algebra only. It does not perform the final
colored-to-physical column projection or prove RH.
