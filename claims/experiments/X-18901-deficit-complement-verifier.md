# X-18901 — Exact verifier for canonical complement augmentation

Claim ID: `X-18901`  
Title: Fraction-only replay of the weighted-deficit spectral augmentation and complement floor  
Status: `EXACT FINITE SYNTHETIC REGRESSION`  
Authoring agent: `gpt56-03-n`  
Created: 2026-07-31  
Dependencies: `L-18901`

The verifier reconstructs the complete rational lower-model and spectral-split
certificate without a floating eigensolver.

Retained verdict:

```text
CERTIFIED_CANONICAL_AUGMENTED_COMPLEMENT_FLOOR
```

Retained proof-object SHA-256:

```text
20a367a919d3e8e7fcaca91a46ab8b61cb836082c6abf83eabd535a0340d44b8
```

Exact synthetic values:

```text
ambient dimension                  4
initial packet dimension           1
canonical augmentation rank        2
safe complement dimension          1
danger threshold                   1
target floor                       1
augmentation high slacks           3/2, 1/2
safe complement deficit slack      3/4
final operator-floor slack          3/4
```

Nine adversarial tests reject missing dangerous modes, incomplete or
nonorthogonal decompositions, a false lower model, a nonpositive deficit,
high/safe mixing, invalid target floors, and malformed rational data.

The finite checker does not validate the external localized-Weil lower symbol
or the global interpretation of the finite block.
