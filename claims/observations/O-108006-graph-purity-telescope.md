# O-108006 — Graph purity telescope: exact atlas, certified rewiring bifurcations, and the negative-end breach law at small order

```text
Claim ID: O-108006
Status:   OBSERVATION over PROVED-per-instance certificates (every
          purity/breach statement below is Sturm-certified exact for the
          named finite graph; the "laws" are patterns over the stated
          finite scope, not theorems)
Created:  2026-08-31 (pass 3, campaigns C5-C7)
Programme: #763 (mechanism discovery; the graph world of the corpus)
Machine:  research/exploratory/2026-08-30-two-programme-pass/graphs/
          telescope.py + telescope.json (atlas + walks),
          spectroscopy.py + spectroscopy.json (breach analysis),
          census14.py + census14.json (n = 14 extension)
Scope:    Hamiltonian connected cubic graphs, exhaustive n <= 10 with
          brute isomorphism, n = 12 (and 14) with spectral+invariant
          dedup (cospectral-mate merges cannot corrupt purity rows —
          purity and breach side are spectral invariants — but could
          undercount classes); plus Petersen and the GP(n,k) family
          n <= 12. NOT exhaustive over all connected cubic graphs
          (bridged non-Hamiltonian examples exist from n = 10).
RH status: unproved; unaddressed.
```

## What was measured (all exact)

1. **Atlas**: 134 graphs (classes n = 4..12 + Petersen + GP family),
   each with girth, diameter, bipartiteness, and a Sturm-certified
   Ramanujan verdict (eigenvalue-squares counted in (8, 9] with exact
   endpoint subtraction). Class counts 1, 2, 5, 17, 80 for
   n = 4, 6, 8, 10, 12 match the published census of Hamiltonian
   connected cubic graphs (total connected cubic 1, 2, 5, 19, 85 minus
   non-Hamiltonian 0, 0, 0, 2, 5 — OEIS A002851-adjacent;
   CITATION-NEEDED for the exact reference) — an external validation
   that the n = 12 spectral dedup lost nothing.
2. **Within scope, the smallest non-Ramanujan order is 12**: all
   classes with n <= 10 (including Petersen) are Ramanujan; at n = 12
   exactly 4 of 80 classes are not (each with ONE untempered
   eigenvalue-square; all girth 3, diameter 4, non-bipartite). In the
   GP family the odd prisms GP(9,1), GP(11,1) are non-Ramanujan while
   GP(7,1) is Ramanujan (margin |−2.802| < 2 sqrt 2 ≈ 2.828), and even
   prisms stay Ramanujan through GP(12,1).
3. **Negative-end breach law (spectroscopy)**: for ALL six
   non-Ramanujan atlas graphs the breach is at the NEGATIVE spectral
   end — lambda_min < -2 sqrt 2, certified by exact Sturm counts in
   (-3, -283/100] vs (283/100, 3) with a (8, 8.0089] separation guard —
   and NEVER at the positive end. At small order, purity dies by
   NEAR-BIPARTITENESS (odd-cycle frustration pushing lambda_min toward
   the bipartite value -3), not by expansion failure (lambda_2 > 2
   sqrt 2). The two failure directions of the same mechanism have
   different size thresholds; how large the smallest positive-end
   breach is, is deposited as the campaign's open question (n = 14
   census extension: census14.json).
4. **Fields where purity breaks**: the breach eigenvalue's minimal
   polynomial per graph — GP(9,1): x^3 + 3x^2 - 1, i.e. the breach
   value is 2 cos(8 pi/9) - 1 in the real cyclotomic field
   Q(cos 2pi/9) (exact shift of the classical minimal polynomial of
   2 cos 2pi/9); GP(11,1): a quintic (Q(cos 2pi/11)); the four n = 12
   graphs: two cubics and two quartics. None rational, none quadratic.
5. **Certified rewiring bifurcations (the discrete Epstein mirror)**:
   deterministic UNBIASED 2-swap walks (first valid swap chosen without
   looking at the spectrum; one Sturm certificate per step) from the
   Ramanujan seeds GP(12,1) and GP(12,5):
   walk(GP(12,1)): departure at step 1, reentry at 8, departure 11,
   reentry 14, departure 15, reentry 16 (25 steps);
   walk(GP(12,5)): departure 1, reentry 2. Every event is an exact
   theorem about a specific pair of adjacent cubic graphs — the
   fully-provable analogue of the Epstein moduli departures/reentries
   of O-108503, with the bound's SUPPLIER swapped per the L-108005
   transfer dictionary.

## Reading (conjecture-generating only)

The graph world now mirrors the Epstein lab event-for-event: a moduli
walk (rewiring), certified departures and reentries of the critical
property, and a stratified locus (here: the negative-end law + girth-3
clustering of the first breaches). The structural contrast deposited
for the matrix: in the lattice world the first breaches were
HEIGHT-STRATIFIED and ANISOTROPIC (O-108503 E4); in the graph world at
small order they are SIGN-STRATIFIED (all at the bipartite-frustration
end) — both are statements that the critical property fails first along
a preferred direction of the mechanism, not isotropically.
```
