# X-91701 — Exact two-channel Cycle-Debt replay

Arithmetic class: `EXACT_RATIONAL`  
Claims exercised: `L-93010`, `L-93011`

Run:

```bash
python3 verify.py
sha256sum -c SHA256SUMS
```

The checker reconstructs random signed balanced flows as two nonnegative
size-biased Markov channels, checks the source and cost identities, cancels
overlapping channel mass, and verifies one nontrivial exact Bellman/complementary-
slackness certificate. Mutations alter a channel sign, an occupied upper
capacity, and a lower-tight support action; all are detected.

It does **not** evaluate the repository's irrational carry capacities, prove
that the synthetic source is the critical Möbius source, establish a cofinal
bound, or prove RH.
