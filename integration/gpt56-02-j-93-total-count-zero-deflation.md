# Integration patch — gpt56-02-j total-count zero deflation

Suggested registry additions after review:

```text
L-9303  PROPOSED  Total-zero-count deflation for direct-xi modulus witnesses
X-9302  PROPOSED  Exact total-count deflation checker and PR71 production stack
```

Dependency edges:

```text
L-7501 -> L-9303
L-7504 -> L-9303
L-9302 -> L-9303
L-9303 -> X-9302
```

The semantic distinction is mandatory:

```text
CERTIFIED_TOTAL_ZETA_ZERO_LOWER_BOUND
```

is an unconditional total count. It is converted into line mass only inside the
RH implication. It must not be silently relabeled as an unconditional
critical-line count.
