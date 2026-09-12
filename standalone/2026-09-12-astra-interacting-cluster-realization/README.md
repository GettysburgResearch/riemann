# ICR26: finite genuine interaction, and a constraint on the full theta limit

**Proposed component proofs. RH and arbitrary-order moment realization remain
unproved. Independent mathematical and implementation review required.**

This successor to #854 supplies:

1. An exact 272-spin theta realization through moments 2,4,6,8,10,12,14,
   with one fixed positive edge J=log(3/2)/2 and pair correlation 1/5. The
   interacting dimer supplies about 9.27% of the variance. The actual full
   theta source, a seven-variable root box, and all infinite tails are included.
   Its standardized sixteenth-moment error lies in (0.20,0.21), not zero.
2. A global necessary theorem: in an all-order realizing sequence, the variance
   carried by components of bounded size and bounded integer weight complexity
   must tend to zero. In particular, indefinitely adding independent equal-
   weight dimers cannot finish. The proof imports weighted Lee--Yang and the
   unconditional Li--Radziwill arithmetic-progression nonvanishing theorem.
3. A weak-bridge consequence: homogeneous bounded-size blocks connected by a
   vanishing TOTAL coupling cannot supply the full theta limit either.

Read PROOF.md, then CLUSTER_LIMIT.md. The new root is not claimed connected by
a verified path to the old degree-twelve model. No all-order graph enlargement,
new zero-free region, or numerical spectral/entropy estimate is asserted.

The exact model is defined by parameters.json and its unique root, NOT rounded
physical weights. result.json stores outward integer endpoints at scale 2^320.
The code reconstructs the defining source rather than trusting a moment table.
The interval backend is adapted from #847, not an independent implementation.

## Reproduce

From this directory, with standard-library Python:

```
python -I -S -B check.py --check result.json
python -I -S -B -O check.py --check result.json
python -I -S -B test_rejections.py --part 1
python -I -S -B test_rejections.py --part 2
python -I -S -B -O test_rejections.py --part 1
python -I -S -B -O test_rejections.py --part 2
```

`--emit` is an unauthenticated producer mode, not acceptance. SHA256SUMS and the
exact regular-file inventory are checked by accepting runs. The manifest is a
file-integrity contract, not a substitute for mathematical review.

SOURCES.json fixes the inspected repository sources and imported literature.
VALIDATION.md states the executed scope and exclusions. Main and predecessor
files are unchanged. This is a research submission, not integration approval.
