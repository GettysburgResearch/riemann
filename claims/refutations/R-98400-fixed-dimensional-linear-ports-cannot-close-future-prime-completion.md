# R-98400 — Fixed-dimensional linear completion ports cannot be exact

Claim ID: `R-98400`  
Status: **PROVED STRUCTURAL NO-GO**  
Created: 2026-08-18  
Depends on: `L-98400`  
RH status: **the arithmetic boundary remains open**

The exact future-prime transition orbit of the root output contains at least

\[
\#\{q\le\sqrt N:q\text{ odd squarefree}\}
\]

linearly independent quotient evaluations.  Consequently an exact all-word
linear realization has dimension \(\Omega(\sqrt N)\).

This rules out the following as complete future-prime states:

```text
boundary alone;
boundary plus one child;
any fixed number of moments;
any fixed-size Schur/Julia matrix;
PSD + parity + logarithmic energy;
any fixed-dimensional passive port.
```

The theorem does not say those quantities are useless estimates.  It says they
cannot be an exact Markov replacement for the quotient profile.  Any closure
using a bounded state must be nonlinear and source-specific, or must prove a
new compression identity that violates none of the orbit-separation tests.
