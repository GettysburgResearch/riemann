# Research digest: repaired P61 bias and factor-67 source-interface hardening

## Freeze

```text
cutoff UTC:        2026-08-17T22:01:08Z
PR #565:           339e3367660f40c74795802a6f8170b15e19b13a
PR #566:           2407b4ffe5024a2e3898922cf0b722d5cf69e496
binding parity:    PR #561 @ db9bdc63c855c6ddf664b763d748f8155a6a2c67
source tree:       PR #556 @ a4feca0457d310c72054f274040f93b0503f658b
annular consumer:  PR #547 @ d60f93b0e207a83a283fb229eb988aa4c404765d
Euler-ramp input:  PR #497 @ bd2a3c32ab50d8a8cec39c4b51ccd63349b23a74
latest downgrade:  PR #575 @ 265c481ebd02807ab7d9a95cb0cf905a22c1876f
```

## Why this was the highest-leverage task

PRs #565 and #566 are the two newest candidate-complete attempts to defeat the
odd-history obstruction while retaining the unusually clean `5:3` scalar
Mellin consumer. Both place almost all closure pressure on one finite P61
source interface. A rigorous repair there would immediately feed Landau; a
precise failure prevents another integration cycle from accepting a scalar
identity as a source theorem.

## New mathematics

1. The claimed lower bias `F>=M/40` is exactly false at `x=184`.
2. The repaired global theorem
   \[
   M/42\le F\le M/8\quad(x\ge67)
   \]
   is proved for every real endpoint by a 256-bit finite-plus-analytic
   certificate.
3. The repaired `1/42` constant is exactly sufficient for a genuine `<1/8`
   parity contraction and gives an explicit factor-67 margin `>M/2730`.
4. Every one-prime high-scale canonical scalar difference is strictly positive.
5. PR #565 changes the same-channel positive restriction into a parity-swapped
   subtraction while continuing to use the canonical P61 marginals. Those are
   incompatible parent types.
6. PR #566 proves that child source fits inside a reserve, then consumes an
   inequality for the disjoint Hall complement. An exact finite countermodel
   separates the two scalars.

## Portfolio effect

The finite P61 arithmetic is stronger than the published packet claimed in one
sense and weaker in another:

```text
published 1/40 lower constant       false
repaired 1/42 lower constant        true globally
contraction arithmetic              survives with 1/42
source-complete rough recursion      not supplied
```

The cleanest surviving conclusion mechanism remains the single annular scalar
Mellin transform. The sharpest open obligation is not another local Hall
margin. It is a one-use parity-covariant root identity whose positive current
and `<1/8` children are both literal subobjects of the actual Möbius source.
This is the common content of `CPSL67`, `GPHT*`, `GABPT`, `TFPE`, and `ACBI`.

## RH status

```text
Riemann Hypothesis: UNPROVED
```
