# Adaptive pressure assembly for simple critical zeros

**PROPOSED quantitative deduction; independent mathematical review required.
No RH proof, new zero computation, or world-record claim.**

Start with [PROOF.md](PROOF.md). The new theorem uses the SAME seven-gap
pressure inequality and analytic Gram/trace contract as the previous
269/280-point deductions, but improves their assembly:

| Deduction from those inputs | Lower proportion |
|---|---:|
| Earlier 269-point blocks | 0.6730085279277797613... |
| Earlier 280-point spectral-pressure blocks | 0.6730096522791369120... |
| New adaptive stopping blocks | 0.6730441804347018717... |

The new value is `(x H0-1/500)/(x-19/5000)`, with
`x=(1+sqrt(1383/1250))/2` and
`H0=3/2-cot(1/sqrt(2))/sqrt(2)`.
Its improvement over the 280-point value is about **0.0034528 percentage
points**, not percentage units of proportion and not a substantial approach
to 100 percent.

The first-crossing rule waits until a consecutive block's accumulated
pressure reaches a threshold. The positive spectral defect then pays that
block. This avoids repeatedly spending the six-point window loss at
predetermined short boundaries. The last unfinished block, every interblock
gap, first-crossing overshoot, and the outer localization boundary are paid.

The proof first works with exact kernel Grams. For actual zero Grams it uses
fixed outer block size, uniform bounded-separation convergence at that size,
then takes height to infinity BEFORE letting the outer size grow. There is
no new uniform-in-size analytic assumption. Even the unoptimized threshold
1 with fixed outer size 1,000,000 already gives a strict improvement over the
old 280-point value.

## What the critique changed

The sharp nonlocal energy result in #882 identifies an RH-equivalent limit
but does not estimate the actual theta value of that limit. Its numerical
verification does not constitute progress on that missing estimate. This
pass deliberately targets a stronger numerical conclusion from existing
inputs, rather than another reformulation of a global RH condition.

This is not a comprehensive new audit of every historical attribution in
the supplied critique. In particular, the stability inequality and the
269-point lift already appear in the external ainta source and are credited
there. The new contribution is the adaptive theorem and the improved
source-qualified constant, not those earlier ingredients.

## Reading and execution

- [Proof and all inherited hypotheses](PROOF.md).
- [Exact reading boundaries and source references](SOURCES.json).
- [Finite computation and unperformed work](VALIDATION.md).
- [Reconstructed numerical brackets and bounded controls](results.json).

From this directory:

```sh
sha256sum -c SHA256SUMS
python -I -S -B check.py --check results.json
python -I -S -B -O check.py --check results.json
python -I -S -B test_check.py
python -I -S -B -O test_check.py
```

These commands check this packet's rational constants, partition bookkeeping,
and bounded spectral controls. They do NOT replay the seven-gap exhaustive
cover, prove the imported analytic source contract, run Lean, or certify a
new accepted zeta proportion. The written analytic proof needs independent
review; no canonical status is changed by publication.

## Focus for review

Check the global scalar spectral envelope, the first-crossing overshoot and
single remainder charge, the sign of interblock gaps, fixed-size pinching
with approximate diagonals, and the order of the height/block-size limits.
The critical provenance checks are P7 and (A1)--(A3) of the proof. These are
inherited known-source obligations, not newly conjectured RH-strength
premises. A later priority comparison should also inspect other pressure
assembly arguments; the present search does not establish external novelty.
