# Source and novelty boundary

## Frozen repository inputs

- PR790: https://github.com/gfreund123/riemann/pull/790
- Exact head: bc3c35d8f434949748a2185783bf831d3afd9126.
- Root: standalone/2026-09-05-astra-theta-count-closure/.
- HEAT_BERNSTEIN.md: normalization, genus-zero product, N(T)<=T^2,
  S>0, and the V100/Z14/15 inputs. All claims remain subject to the parent's
  review boundary; this pass reran its executable checks, not an independent
  referee process.
- THETA_COUNT.md: the mixed differences, Laguerre/integration-by-parts
  formulas, and exact Hausdorff implication to RH.
- COUNTERFEITS.md: positive Bernstein logarithm does not imply Stieltjes
  or all mixed signs. The finite polynomial witness is replayed here.
- Parent PR785 at 9a965c26fd3e0310736829689db1734bcb5c3ec4:
  the matching-scale Widder geometry. Its finite-rank positivity results
  are NOT inputs to this continuation.

## External analytic inputs

1. D. Platt and T. Trudgian, *The Riemann hypothesis is true up to
   3*10^12*, Bulletin of the London Mathematical Society 53 (2021),
   792--797; DOI 10.1112/blms.12460; arXiv:2004.09765.
   https://arxiv.org/abs/2004.09765
   Exact imported statement: every nontrivial zero beta+i gamma with
   0<gamma<=3*10^12 has beta=1/2. No simplicity is used. Its abstract and
   publication metadata were checked online in this pass. The proof code,
   interval computation and full zero census were NOT rerun.
   The 27-layer and all-order small-time proofs use only its restriction
   to gamma<=100. The 10^15-depth corollary uses its full stated height.
2. NIST Digital Library of Mathematical Functions, 25.2(iii), especially
   25.2.8--25.2.10: Euler--Maclaurin continuation for zeta.
   https://dlmf.nist.gov/25.2
   The B2 formula actually needed here is displayed and bounded in the
   manuscript, obtained by one integration by parts; it is not copied as
   a purported literal transcription of the site's B3 formula.
3. NIST DLMF 5.11: Stirling expansion and remainder theory.
   https://dlmf.nist.gov/5.11
   The needed periodic-B2 remainder and its elementary absolute bound are
   explicitly stated in the manuscript, including the 1/(12z) term.
4. Classical completed-xi argument principle and Riemann--von Mangoldt
   identity with the continuous horizontal-path argument, as in
   E. C. Titchmarsh, *The Theory of the Riemann Zeta-function*, 2nd edition,
   revised by D. R. Heath-Brown (Oxford, 1986), Chapter 9.
   General primary reference and conventions: https://dlmf.nist.gov/25.10
   The exact identity is imported; the deliberately coarse bound on its
   remainder is proved here. No recent optimized S(T) estimate is imported.

Jensen, finite Bernstein degree elevation, the Vandermonde determinant,
Parseval and elementary Gamma integrals are classical general tools.

## Novelty and verification

The author claims a reviewable deduction with explicit constants and scope,
not external priority. A specialist literature assessment could identify
prior versions or stronger known statements. No recent proof claim, conjectural
GGC representation, assumed RH factorization, or unreviewed zero table is
used to close a gap. References are not substitutes for the displayed
parameter and tail estimates.

Web checks were performed on September 5, 2026 in the user's Asia/Jerusalem
calendar date. Only the specified source contents are relied upon.
