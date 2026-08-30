# R-108420 — Positive Hellinger gluing cannot be applied before signed-current recombination

Claim ID: `R-108420`  
Status: **PROVED EXACT SCOPE FIREWALL**  
Created: 2026-08-31

The mixture and pushforward contractions of `L-108420` require nonnegative
measures. They cannot be applied componentwise to a signed principal-minus-
Kummer current before the exact signed recombination.

The smallest counterexample is a one-cell signed source with two labelled
pieces

\[
\sigma_1=+\delta_x,
\qquad
\sigma_2=-\delta_x.
\]

Their signed sum is exactly zero. Any procedure which first replaces them by
the positive measures

\[
|\sigma_1|=\delta_x,
\qquad
|\sigma_2|=\delta_x
\]

and then pays a positive distance or trace sees two units of mass rather than
zero. The cancellation is destroyed before the physical map is applied.

A two-cell version shows the same failure for nontrivial comparators. Let

\[
\sigma_1=(1,-1),
\qquad
\sigma_2=(-1,1).
\]

The combined current vanishes, while every componentwise absolute-value
occupancy equals `(1,1)` and carries positive total mass.

Therefore the valid ordering is

```text
literal signed source
  -> source-authorized history/principal/Kummer recombination
  -> nonnegative occupancy or positive spectral part
  -> Hellinger mixture and physical pushforward.
```

The invalid ordering is

```text
literal signed source
  -> componentwise absolute values
  -> positive Hellinger gluing
  -> attempted recovery of the signed principal current.
```

This firewall does not obstruct the positive quotient theorem. It requires
that the signed current enter that theorem only after the exact cancellation
ledger has been applied.
