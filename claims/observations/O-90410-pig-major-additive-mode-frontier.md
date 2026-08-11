# O-90410 — The PIG frontier is a major-additive-mode theorem

Claim ID: `O-90410`  
Status: **RESEARCH FRONTIER / PROPOSED SYNTHESIS**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-11  
Dependencies: `L-90410`--`L-90413`; PRs #352, #360, #362, #371  
RH status: unproved

The new exact decomposition changes the preferred PIG attack.

## What is now unconditional

For the actual compact innovation prefix:

```text
all additive residue classes with distance >= sqrt(N) from 0 mod N
    contribute O(N log N) to the complete carry-position energy;

after PIG normalization
    this is O(log N).
```

For the randomized Euler source:

```text
the entire innovation Gram has expected normalized energy O(log^2 N).
```

## What remains

The deterministic arithmetic problem is concentrated in

```text
mean mode a=0
+ O(sqrt(N)) residues with min(a,N-a)<sqrt(N).
```

The mean mode already has the reciprocal-zeta Mellin transform of `L-90413`,
so it is individually RH-bearing.

## Proposed major-mode gate

A sufficient endpoint theorem is

\[
|\widehat Q_{\circ,N}(0)|^2
+
\frac1{N^2}
\sum_{0<d_N(a)<\sqrt N}
\frac{|S_a|^2}{\sin^2(\pi a/N)}
\ll N\log^B(2N).
\tag{O-90410.1}
\]

Together with `L-90412`, this gives the full continuous-position PIG
bound. A source/measure adapter is still required before importing it into the
global Q4 recurrence, as emphasized by PR #371.

## Two concrete research interfaces

1. **Endpoint/annular interface.**  
   `L-90413` turns the mean into a zero-safe prime-ramp scalar. The factor-64
   annular machinery of PR #352 can be applied to this scalar, but its
   unconditional eventual sign remains a new theorem.

2. **Growing alias/compression interface.**  
   PR #360 proves that fixed or subpolynomial prime-resonant alias banks are
   lower order. The present theorem shows why: the required bank is genuinely
   macroscopic, of order at least \(N^{1/2}\), if it is to resolve every
   remaining low residue. A valid continuation must retain all cross-alias
   terms and cannot use the no-alias scalar collapse.

## Rejected shortcuts

```text
generic l2/wavelet bound                         too large (PR #362);
random-sign expectation -> deterministic Mobius invalid;
prime-by-prime monotonicity                      false in general;
negative inertia -> positive current             false (PR #357);
finite/subpolynomial alias bank                  lower order (PR #360).
```

The clean remaining target is therefore a deterministic major-mode theorem,
not another complete-Gram estimate.
