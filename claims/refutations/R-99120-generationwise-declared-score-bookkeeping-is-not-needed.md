# R-99120 — Generationwise declared-score bookkeeping is not the proof object

Claim ID: `R-99120`  
Status: **PROVED TYPE AND COMPOSITION FIREWALL**  
Created: 2026-08-19

The Hall row bonus is a nonnegative physical row but is intentionally
`target-free` and `declared-score-free`. Assigning it an artificial source score
revives the exact type error already exposed at the compact endpoint `x=2`.

The correct object is the complete physical row. If

\[
E=J+ET
\]

holds in every component row, then the literal score is obtained only after
resolving the finite tree:

\[
\mathcal H(E s)
=\mathcal H(J(I-T)^{-1}s).
\]

A generationwise score telescope is therefore neither necessary nor canonical.
It may be used as a redundant lower bound only after it has been derived from
the same physical-row identity.

Three operations must occur in this order:

```text
1. resolve the labelled source tree exactly;
2. form the one physical row and every q/4q response;
3. apply common omission, thinning and optional exact cubature.
```

Moving cubature, thinning or a score proxy inside the recursion can duplicate
labels, charge a row bonus as source, or break the common ordinary/detail row.
The exact nilpotent resolvent is the fail-closed replacement.
