# Organizational Proposals

## M-0001 — Separate discovery, enclosure, and exact checking

The finite-witness route should use three deliberately independent layers:

1. **Discovery:** fast ordinary high-precision search, allowed to be heuristic.
2. **Enclosure:** directed-rounding analytic generation of matrix-entry balls.
3. **Checking:** a small exact rational verifier consuming only a compact
   certificate.

A candidate should not be promoted merely because one large program reports a
negative eigenvalue.  Separation makes shared bugs less likely and permits
reviewers to verify the decisive inequality without rerunning the search.

Trial implementation: X-0001 includes layers 1 and 3.  Q-0001 is layer 2.

Success criterion: two independent enclosure generators produce certificates
accepted by the same tiny exact checker, with all normalization dependencies
audited.
