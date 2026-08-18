# X-97701 - BLPTE67 / C4MBI67 critical-core replay

The replay checks exact finite algebra only:

- the sparse `5:3` coefficient dictionary;
- scale-four annularization;
- the exact four-band coefficient vector in `Q(sqrt(2))`;
- logarithmic prime ownership on every squarefree integer through a finite
  exhaustive limit using arbitrary additive prime weights;
- the Bellman / annular / C4MBI equivalence;
- the source-blind unsigned mutation countermodel;
- hostile constant and sign mutations.

It does not prove the all-scale C4MBI67 sign or RH.

```bash
./build_and_replay.sh
```
