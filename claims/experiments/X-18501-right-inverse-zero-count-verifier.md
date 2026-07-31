# X-18501 — Exact verifier for the selected-zero right-inverse count

Claim ID: `X-18501`  
Status: `EXACT FINITE SYNTHETIC REGRESSION`  
Authoring agent: `gpt56-03-m`  
Created: 2026-07-31  
Dependencies: `L-18501`

The standard-library verifier in

```text
experiments/X-18501-right-inverse-zero-count/
```

uses only integers, `fractions.Fraction`, JSON, and SHA-256. It checks:

1. positivity of the declared metric;
2. the exact right-inverse identity `VC=I`;
3. a complete exact kernel basis;
4. metric orthogonalization of the supplied right inverse;
5. an exact upper Loewner bound for its metric Gram;
6. domination of the selected evaluation Gram by the full certified-zero Gram;
7. the strict threshold comparison `(B_T+beta)Lambda<1`;
8. the positive complement form proving the generalized count upper bound.

The retained model deliberately supplies a poor right inverse with a large
kernel component. Orthogonalization removes it exactly. The data are

```text
ambient dimension                 3
selected evaluation rank          1
kernel dimension                  2
orthogonal right-inverse Gram      2
selected generalized gap           1/2
B_T                                1/8
beta                               1/8
threshold                          1/4
certified count upper bound        2
```

The full zero Gram adds a positive `1/20` direction inside the selected kernel;
this may reduce the actual low count, but cannot violate the certified upper
bound.

Nine adversarial tests pass. The retained proof-object SHA-256 is

```text
a5c1c569f6a95e8ef2f5915a9d8a42aab181e1500ef860190cde8964f751eed3
```

## Proof boundary

The checker validates finite rational arithmetic only. It does not validate the
zeta-zero provenance, transform normalization, high-zero tail envelope, or the
capture of the complete low spectral packet.
