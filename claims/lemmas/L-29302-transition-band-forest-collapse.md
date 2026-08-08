# L-29302 — Transition-band forest collapse

Status: PROPOSED EXACT FINITE LEMMA

## Claim

For the size-biased fragmentation kernel Q, every ancestry tree entering the scale interval [n,2n) can be decomposed into:

- first-entrance edges;
- internal cycle moves;
- terminal collector moves.

The internal ancestry above the first entrance does not contribute an independent obstruction.

## Argument

The Green identity gives

\[
B(n)=S(n)+\sum_{m>n}B(m)Q(m,n).
\]

Stopping at the first entrance time removes all repeated descendants below the transition scale. The strong Markov decomposition gives a unique transition measure.

Any two decompositions with the same transition measure differ by a divergence-free balanced fragmentation flow. Hence their difference lies in the Pascal cycle space.

## Consequence

The RH-bearing sign problem can be studied entirely inside the transition annulus, modulo cycle equivalence.

This provides the bridge between:

- primal fragmentation positivity;
- Pascal cycle debt;
- squarefree collectors;
- factor-five parity localization.

The remaining theorem is positivity in the quotient cone, not positivity of a raw coordinate representation.
