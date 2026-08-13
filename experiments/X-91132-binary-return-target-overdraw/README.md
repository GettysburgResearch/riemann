# X-91132 — Binary-return target overdraw counterexample

Companion replay for `R-91310`.

```bash
python3 experiments/X-91132-binary-return-target-overdraw/verify.py
```

Expected verdict:

```text
PASS_BINARY_RETURN_TARGET_OVERDRAW_COUNTEREXAMPLE
```

The checker uses exact `Fraction` arithmetic to verify

```text
(1,2)(C_r+H_r)=(1+3r-3r^2,2)
```

and the witness `r=1/9`, where the branch target is `35/27>1` on the pure equality ray. It does not construct a corrected return matrix or prove RH.
