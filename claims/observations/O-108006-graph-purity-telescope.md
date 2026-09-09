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
   breach is, is deposited as the campaign's open question.
   **n = 14 extension (census14.json)**: 471 Hamiltonian-cubic classes
   (spectral+invariant dedup; count may slightly undercount from
   cospectral merges — purity/side rows are unaffected), 31
   non-Ramanujan, and ALL 31 breach at the negative end (zero
   positive-end, zero both-end; separation guard clean). The law now
   covers all 37 non-Ramanujan graphs in scope through n = 14.
   **OPEN QUESTION ANSWERED (continuation run; gp24_certificate.json):
   positive-end-only breaches EXIST — first certified witness
   GP(24, 2) on 48 vertices**: exactly one untempered eigenvalue-square
   in (8, 9), separation guard clean, one eigenvalue in (283/100, 3)
   beyond the trivial 3 and ZERO in (-3, -283/100] — an
   expansion-side purity failure with NO near-bipartiteness (girth 5,
   diameter 8, non-bipartite: the negative-end breachers at n = 12
   were all girth 3, and the sides swap girth profiles exactly as the
   mechanism reading predicts), fully Sturm-certified on the exact
   degree-48 characteristic polynomial (22 s). Family reading (float + closed-form block reconnaissance,
   labelled): GP(n,2) has lambda_min >= -sqrt 5 > -2 sqrt 2 for ALL n
   (block minima), while lambda_2 crosses 2 sqrt 2 between n = 22 and
   n = 24 — so GP(n,2), n >= 24, appears to be an entire
   positive-end-only family; only the n = 24 member is certified here.
   The MINIMAL order question was then SETTLED within the
   Hamiltonian-cubic scope by the exhaustive n = 16 spectral census
   (census16.py + census16.json: 2,027,025 chord diagrams -> 65,346
   canonical -> 3,801 distinct spectra, verdicts exact per spectrum):
   3,495 Ramanujan spectra and 306 non-Ramanujan with the FINAL side
   tally — after the 18 guard-flagged spectra (untempered square
   inside (8, 8.0089]) were resolved by adaptive rational cuts
   (witness16.py + witness16.json: per-spectrum Sturm-isolated cut r
   with 8 < r^2 <= smallest square, exact) — of:
   302 negative-end-only, THREE POSITIVE-END-ONLY (idx 706, 708, 709;
   all girth 3, non-bipartite; 708/709 with adjacency matrices and
   charpolys deposited in witness16.json; 706's untempered square
   lies within 0.0089 of the threshold 8 — a barely-untempered
   graph), and ONE BOTH-END spectrum (idx 707) — the census's first.
   Since all Hamiltonian cubic n <= 14 are negative-only or Ramanujan
   and cubic orders are even, the minimal Hamiltonian-cubic
   positive-end-only order is EXACTLY 16. A correction this result
   forces on earlier text: the girth-profile-swap reading suggested
   by GP(24,2) (girth 5) is REFUTED — all three n = 16 positive-end
   witnesses have girth 3.
   **The witnesses DECODED (graphs/WITNESS16_STRUCTURE.md;
   adversarially verified, 20/21 exact claims confirmed, the 21st a
   naming ambiguity with members exactly re-certified):** both primary
   witnesses are CAPPED LADDERS — a diamond (K4 minus an edge) joined
   through a two-rail rung corridor to a far cap (a second diamond
   for 709, |Aut| = 16, lambda_min = -(1+sqrt 3); a one-triangle
   block for 708, |Aut| = 4) — differing by a single 2-switch and
   non-isomorphic. Their minimum cut is 2 but realized by 4-5
   PARALLEL corridor cross-sections, which is exactly why the
   single-neck dumbbell search missed them. Extending the families
   exactly: n = 14 members are Ramanujan, n = 16-20 members are
   positive-end-only (two non-isomorphic examples at n = 18), and
   n = 20-22 members breach BOTH ends — the positive-end-only
   property is a FINITE TRANSITIONAL WINDOW in near-bipartite
   corridor families, versus the positive-only regime of the
   lambda_min-bounded GP(n,2) family — which is now a THEOREM
   (T-108514, adversarially verified three-piece proof): GP(n,2) is
   positive-end-only for EVERY n >= 24, with exact threshold
   (GP(23,2) certified below) and lambda_min > -2 sqrt 2 for every
   n >= 5. Two distinct mechanisms, one exactly witnessed as a
   window, one proved as an infinite family. FINAL CLASSIFICATION:
   idx 706 decoded (same diamond head + 3-rung corridor, third cap
   variant: a two-triangle chain), so the three minimal positive-only
   spectra are precisely the three diamond-headed 3-rung capped
   ladders, one per cap variant (diamond / one-triangle block /
   two-triangle chain) — the expansion-side breach at minimal order
   has exactly one structural mechanism (WITNESS16_STRUCTURE.md). Earlier negative
   evidence inside the (14, 48] bracket, from before the census
   (both searches Sturm-exact, no floats — an earlier float screen
   was found unreliable and discarded): (i) all 774
   two-edge-bottleneck dumbbells from the five 8-vertex cubic
   classes, Petersen, and Mobius ladders M8/M10 (n = 16, 18, 20):
   zero positive-end-only — showing the n = 16 witnesses are NOT of
   dumbbell type; (ii) GP(n, k) for 13 <= n <= 20, k >= 2: zero
   positive-end-only, but FIVE new negative-end members certified —
   GP(17,3), GP(17,6), GP(18,8), GP(19,3), GP(19,6).
   (dp20_certificate.json records one dumbbell certified Ramanujan as
   the float screen's false positive.)
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
