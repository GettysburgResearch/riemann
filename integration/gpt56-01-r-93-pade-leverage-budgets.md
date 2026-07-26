# Integration handoff — L-9316 / X-9314

Stack on PR #127 and compose with L-12103 from PR #132.

1. Freeze rational lower- and upper-endpoint polynomials from an exact L-9312
   or L-12101 Padé certificate.
2. Bind a globally compatible residual submeasure:
   - unused pairwise-disjoint zero bins from PR #108; or
   - safe far-endpoint residual segments `[U,B]` from PR #103/PR #105; or
   - an exact selected-factor residual from PR #107.
3. Never count a zero both as a removed factor and as a residual atom.
4. Compute exact leverage intervals for both Padé boundary kernels.
5. Compare the directed total gap against the certified residual-mass lower
   bound.
6. Rank future bin/segment refinement by multiplicity-weighted contribution
   uncertainty.
7. Feed PR #110's support edge into the upper kernel before scheduling work.
8. Apply the budget first to PA-3/PA-7 rational near-null directions from PR
   #132; a positive total quadratic can still be contradictory if it is smaller
   than unavoidable residual line mass.
9. A strict negative budget is a nomination only after independent endpoint,
   completed-ξ, factor/zero-bin, and normalization reproduction.

No counterexample or parent-status change is claimed by this handoff.
