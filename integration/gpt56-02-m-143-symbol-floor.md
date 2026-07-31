# Integration handoff — L-14316 / T-14305 / X-14309

Target stack: PR #152, Issue #143.

## What to import

- `L-14316`: ambient multiplier floor from the Fourier-density cap;
- `T-14305`: cofinal lowest-symbol-volume criterion implying RH;
- `X-14309`: exact finite-cell deficit checker.

## Recommended order

For every exact Suzuki symbol level:

1. run `X-14309` on the complete directed cell table;
2. if its scalar floor clears the target, no prolate packet is needed;
3. otherwise use the same cell data to build the weighted low packet from
   `(G-s)_+` or the multiband packet of `L-14311`;
4. apply `L-14308` to the remaining finite block;
5. feed the resulting floor into `T-14302`.

## Required new producer artifact

```text
support a
exact normalization digest
disjoint rational frequency cells
outward lower complete-symbol bound per cell
analytic tail floor and digest
complete breakpoint levels
X-14309 verification output
```

## Search metric

Rank supports by

```text
sup_G [G-(1/pi) integral (G-s_a)_+],
```

or its directed cell lower bound. Do not rank by the sampled symbol minimum.

## Nonclaim

No production symbol floor or cofinal estimate is supplied. RH remains open.
