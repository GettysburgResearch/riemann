# Cancellation-aware multiband complement reduction

Agent: `gpt56-pro-09-b`  
Date: 2026-07-30  
Issue: #143  
PR: #152

## Result

`L-14311` strengthens the prolate complement theorem by replacing the absolute
prime-coefficient sum with a directed cover of the **actual low-symbol frequency
set**.

The theorem is exact.  A Riemann-Weil production result still requires the
symbol cover, generalized-prolate packet, and low-block Schur certificate.
RH is not proved.

## Multiband concentration theorem

For any finite-measure frequency set `B`, the time-limited concentration
operator on `[-1,1]` has trace

```text
|B|/pi.
```

Thus, outside at most

```text
ceil(|B|/(pi eta))
```

generalized-prolate modes, no time-limited vector can place more than an `eta`
fraction of its Fourier energy in `B`.

If a bounded-below symbol has global lower bound `m` and lower bound `G` outside
`B`, the complete complement has floor

```text
(1-eta) G + eta m.
```

For the Suzuki form, the negative logarithm on `|xi|<1` adds the explicit charge
`-2/pi`.

## Exact arithmetic symbol

Suzuki (4.5) becomes, after zero extension, a Fourier symbol composed of:

```text
log_+ |xi|
+ scalar archimedean terms
- 2 sum Lambda(n)/sqrt(n) cos(xi log(n)/a)
- smooth remainder multiplier.
```

A production calculation need not bound the cosine polynomial by the sum of its
absolute coefficients.  It may instead partition frequency space, evaluate the
complete symbol with directed balls, and retain only cells whose lower endpoint
fails the chosen good floor.

The total length of those cells controls the number of low modes.

## Why high-frequency phase alignment is harmless

The finitely many prime phases may nearly re-align at arbitrarily large
frequencies.  A pointwise supremum therefore does not improve the absolute
coefficient bound.  `L-14311` does not use a pointwise supremum.  It charges the
**measure** of neighborhoods where the complete symbol is low.  Isolated
re-alignments are inexpensive unless they occupy substantial frequency measure.

## New candidate scheduler

For each support `a`, define a proof-grade bad-symbol measure at a fixed floor.
Supports should be ranked by:

```text
bad-set measure / floor moat,
```

not only by the smallest Ritz value.  A small bad set yields a smaller exact
low packet and a stronger path to the block Schur floor.

This scheduler can reuse the existing complete prime manifests and directed
phase infrastructure from the counterexample program.

## Exact verifier

`X-14306` checks the multiband trace cap and complement floor with exact rational
arithmetic.  The synthetic packet proves

```text
bad-set measure upper   10
required rank cap        7
complement floor         5/6
```

with proof digest

```text
4fcd9ceb05a3002675ce704bef43f3a4ad398ba29974ee11b8b8a7898d97ae66
```

Seven tests pass.

## Immediate implementation

1. Fix one retained CCM/Suzuki support.
2. Build the exact complete symbol from the prime manifest.
3. Use adaptive interval cells, preserving every ambiguous cell.
4. Prove a tail threshold from logarithmic growth.
5. Export the exact union length and run `X-14306`.
6. Construct an overcomplete low packet of dimension at least the certified cap.
7. Run `X-14304` on the resulting block.

The most useful first comparison is between:

- `L-14310`'s one-band rank cap;
- `L-14311`'s exact low-symbol measure cap.

Their ratio directly quantifies how much prime cancellation can be converted
into proof-level dimensional savings.
