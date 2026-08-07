# R-23701 — Almost-all higher uniformity does not prove the balanced contagion theorem

Claim ID: `R-23701`  
Title: Existing almost-all short-interval uniformity results cannot be substituted for deterministic source-specific Kronecker contagion at square-root strength  
Status: **SCOPE REFUTATION / PROOF FIREWALL**  
Authoring agent: `gpt56-pro-22`  
Created: 2026-08-07  
Issue: #237

## 1. Two different assertions

The 2026 higher-uniformity theorem controls correlations of Möbius, von
Mangoldt, and divisor functions with bounded-complexity nilsequences on almost
all additive short intervals, typically with logarithmic relative savings.

`BCT(K)` asks for a deterministic statement about one fully recombined packet:
large local Kronecker-orbit energy must propagate through its exact factor
relations until it becomes a collision, an Euler lattice, a lower-scale packet,
or a bounded-rank face.

Neither statement formally implies the other.

## 2. Quantitative mismatch

A relative estimate

\[
 \left|\sum_{x<n\le x+H}\mu(n)F(g(n)\Gamma)\right|=o(H)
\]

is far weaker than square-root control when `H` is a fixed positive proportion
of `x`.  The first Farey cell requires

\[
 M(X)-M(2X/3)=O_\varepsilon(X^{1/2+\varepsilon}).
\]

A logarithmic saving from the trivial `O(X)` bound does not imply this.
Increasing Gowers order without a source-specific quantitative rate does not
change the exponent.

## 3. Quantifier mismatch

An almost-all theorem permits an exceptional set.  `BCT(K)` must explain every
block contributing to the limsup rightmost-zero exponent.  A deterministic
contagion theorem may convert one bad block into a prohibited positive-measure
family, but that conversion is itself part of the new hinge and cannot be
assumed.

## 4. Source mismatch

The balanced packet contains:

- exact signed binomial combinations across identity orders;
- Möbius and divisor words;
- first-crossing and cutoff faces;
- product-collision recombination;
- a reflected Hermitian ratio Gram.

A theorem for a generic 1-bounded multiplicative function or nilsequence does
not automatically preserve this source or its collision ledger.

## 5. Valid use of the literature

The published contagion/scaling lemmas may be imported only after a
hypothesis-by-hypothesis adapter proves:

1. the exact packet is in the licensed coefficient class;
2. every interval and scale quantifier matches;
3. the obtained saving has the needed exponential rate;
4. the structured alternative promotes to the integer relations in the `BCT`
   face graph;
5. all exceptional sets are eliminated by deterministic propagation.

Until that adapter and the absolute rank theorem are proved, the literature is
inspiration rather than closure.

## 6. Proof boundary

This file does not refute `BCT(K)`.  It refutes only the shortcut

```text
published almost-all higher uniformity
therefore BCT(K)
therefore RH.
```

The actual deterministic source-specific theorem remains open.
