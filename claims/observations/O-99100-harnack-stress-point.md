# O-99100 — The Harnack defect exposes a sharper finite stress point

Claim ID: `O-99100`  
Status: **EXACT COMPUTATIONAL OBSERVATION**

The original primitive prefix `C` has its retained lower minimum through
`10^9` at `48,433`, with value greater than `1.115`.  The renormalized defect

\[
 H_{67}(t)=C(t)-67^{-1/2}C(t/67)
\]

is substantially tighter.  Through `2*10^9` its exact lower enclosure is
minimized at

```text
61,848,971
```

with lower numerator

```text
57,262,723,035 / 2^40 = 0.052080143209423113...
```

The integer factors as `19 * 3,255,209`; no conclusion is drawn from that
factorization.

On the new tail `10^9<t<=2*10^9`, the smallest block-combined lower enclosure
occurs at `1,408,925,742` and is

```text
1,836,182,423,142 / 2^40 = 1.669998185336226...
```

Thus the global stress point remains well inside the original finite range,
while the newly scanned tail has considerably more margin.  This is evidence
for the renormalized target, not a proof of its infinite tail.
