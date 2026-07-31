# X-14306 — Exact multiband symbol-sublevel floor

This experiment checks the finite scalar interface of `L-14311`.  It consumes a
directed upper bound for the measure of the complete low-symbol frequency set
and exact lower bounds for the symbol.  It performs no zeta, prime, cosine,
Fourier, or generalized-prolate evaluation.

## Input semantics

A production packet must prove:

```text
|B_a| <= bad_measure_upper,
s_a^+(xi) >= global_symbol_lower       for all xi,
s_a^+(xi) >= good_symbol_lower         outside B_a,
pi >= pi_lower,
0 < eta < 1.
```

Then the generalized-prolate packet dimension is at most

```text
ceil(bad_measure_upper/(pi_lower eta)),
```

and the full complement floor is

```text
-2/pi_lower
+ (1-eta) good_symbol_lower
+ eta global_symbol_lower.
```

The `-2/pi_lower` term safely charges the negative logarithm on `|xi|<1`.

Production is rejected without a
`CERTIFIED_COMPLETE_SYMBOL_SUBLEVEL_COVER` gate.  That gate must bind the exact
support, prime manifest, interval cover, infinite-frequency tail proof, smooth
remainder, and normalization.

## Synthetic control

The retained exact packet uses

```text
bad-set measure upper       10
eta                          1/2
pi lower                     3
global symbol lower         -1
good-region symbol lower     4
```

and proves

```text
required rank cap            7
complete complement floor    5/6
```

with proof-object SHA-256

```text
4fcd9ceb05a3002675ce704bef43f3a4ad398ba29974ee11b8b8a7898d97ae66
```

## Reproduction

```bash
python experiments/X-14306-multiband-symbol-floor/verify.py \
  experiments/X-14306-multiband-symbol-floor/certificates/synthetic.json \
  --output /tmp/x14306-result.json

python -m unittest discover \
  -s experiments/X-14306-multiband-symbol-floor/tests -v
```

Expected result: seven tests passing.

## Production workflow

1. Partition a finite frequency window into rational cells.
2. Evaluate the complete Suzuki symbol with directed phase and smooth-remainder
   balls on every cell.
3. Mark a cell bad unless its lower endpoint is above the selected good floor.
4. Prove an analytic tail threshold outside the finite window.
5. Merge bad cells and sum their exact lengths.
6. Run this checker.
7. Construct or overcapture the corresponding multiband concentration packet.
8. Pass that finite packet to `X-14304`.

This checker certifies the rank and complement floor only.  It does not certify
the finite generalized-prolate low block.
