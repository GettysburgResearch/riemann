# T-99930 — Critical Taylor renormalization of the native scalar

This packet continues the exact native-coefficient line from PR #664. It does
not claim the Riemann Hypothesis.

The new idea is to replace the SHARP activation by the zero-at-activation
carrier

```text
S(y)=4(sqrt(y)-1)_+
```

and expand its positive supercritical powers by an exact Euler–Taylor ladder.
Every Taylor remainder whose effective prime exponent is strictly larger than
one is proved positive for the complete labelled Euler source. This removes all
absolutely convergent layers and leaves one explicit critical remainder.

The critical remainder has a positive scalar kernel and a zero-safe
reciprocal-zeta Mellin transform. Eventual positivity, or merely subpower
logarithmic negative mass, would imply RH. Its sign is not proved here.

```text
activation-zero powers m>=2                 proved positive
Euler–Taylor remainders k<=m-2              proved positive
critical remainder k=m-1                    exact / RH-bearing
all positive-real Mellin carriers           explicitly subtracted
contracted-alpha/native-source shortcut      forbidden
Riemann Hypothesis                           unproved
```

Replay:

```bash
python3 experiments/X-99930-critical-taylor/verify.py \
  --output experiments/X-99930-critical-taylor/results/verification.json
```
