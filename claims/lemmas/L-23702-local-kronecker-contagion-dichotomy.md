# L-23702 — Local Kronecker contagion dichotomy for the actual balanced packet

Claim ID: `L-23702`  
Title: Proposed bounded-rank local Kronecker contagion for balanced packets  
Status: **REFUTED BY `R-23702`**  
Authoring agent: `gpt56-pro-22`  
Created: 2026-08-07  
Corrected: 2026-08-07  
Issue: #237

## Disposition

The original version proposed that every fully recombined balanced packet could
be partitioned into:

1. exact product collisions;
2. Euler-eligible complete free-lattice faces;
3. strict lower-scale packets; or
4. same-scale resonance faces of rank at most one absolute constant `C_0`,
   independent of the packet order `K`.

`R-23702` constructs, inside the exact fixed-logarithm Möbius slice of
`L-15159`, balanced squarefree product cubes of arbitrary affine Bohr rank
`K`.  Their products all lie in one fixed-ratio `2/3` shell, their grouped
coefficients are the nonzero common value `(-1)^K`, and none of the first three
outcomes applies.

There is an unavoidable representation dichotomy:

```text
retain the K short prime coordinates:
    exact face rank is K;

collapse them to the product n:
    one coordinate ranges over exp(J-o(J)) values,
    not exp(J/K+o(J)).
```

Thus the enumeration loss `exp(C_0 J/K)` does not follow from product-collision
recombination or local Kronecker geometry.

## What survives

The exact Bohr lift in `L-23701` remains valid and useful.  It identifies the
balanced obstruction as restriction of the actual Möbius polynomial to the
prime Kronecker orbit.  What fails is the proposed order-independent rank
compression.

A valid completion must prove cancellation between high-rank, opposite-parity
Möbius families.  That is a source-specific signed Type-II theorem, carry
minorant, reflected packet identity, or another genuinely arithmetic result;
it cannot be replaced by face counting.

## Exact finite regression

`X-23702` freezes a rank-eight squarefree product cube:

```text
products                         256
distinct products                256
affine Bohr rank                   8
all products in one 2/3 shell     yes
common Möbius sign                 +1
scaled common-overlap energy    65536
proof-object SHA-256
d786fd9608ecba0f3cd6d816699ef250b45cb20c05169085187f62e06b2e080f
```

The all-order construction in `R-23702` uses the prime number theorem in fixed
relative intervals.

## Proof boundary

```text
exact Bohr lift                         retained
absolute bounded-rank contagion         refuted
C_0/K balanced contraction from rank    unavailable
balanced Möbius shell estimate          open / RH-bearing
Riemann Hypothesis                       unproved
```
