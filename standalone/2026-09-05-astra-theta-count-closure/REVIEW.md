# Independent review request and self-audit boundary

The author has reconstructed the proofs and run the retained code. This is
NOT an independent-agent, specialist, formal-kernel, or journal review.
The published PR's head SHA is the review target; a later repair gets a new
commit. The frozen scientific inputs are in SOURCE_LOCK.json.

## Highest-priority mathematical checks

1. Verify the upper-half-plane zero indexing and factors: K_parent=2S,
   q_parent=2h, X(0)=1/2, and Re a>=gamma^2, |Im a|<=gamma.
2. Reconstruct the Jensen bound (4), the Stieltjes Gaussian tail (5), and
   both time ranges of ASTRA-TC-03. Check that the finite verified prefix
   is not substituted for an infinite tail estimate.
3. Verify the eta-transform error and the directed Gamma implementation's
   numerical trust boundary. Replace the two endpoint signs with an
   independently sourced certificate if desired; no simplicity is needed.
4. Check differentiation at u=0, Levy integrability, and the distinction
   between h completely monotone and h Stieltjes.
5. Verify that the pure-Phi mixture and the predecessor's vacuum/forced-one
   mixture are different MARKINGS of the same PGF. The covariance argument
   works for both; neither licenses a statement about every scalar count.
6. Check the high-mode tail moment threshold, the finite-partition cumulant
   signs, and the factorials in the Laguerre identity and Rodrigues formula.
7. Reconstruct the Hausdorff-to-analytic-ODE zero-exclusion argument. This
   is a conditional implication with the WHOLE mixed family as premise.
8. Check every polynomial in the positive-source quartet insertion. In
   particular (7) is a GLOBAL polynomial lower bound, not a sampled ratio.
9. Check no-Poisson-escape compactness: bounded trace alone is insufficient;
   order below one is what removes the exp(a y) factor.

## Self-audit: attempts that did not close RH

- Integrating fiber determinants does not produce a determinant of the
  integrated operator. The actual marked source now has a strict obstruction.
- Discarding marks only on the high tail does not help: that tail's total
  count is overdispersed. The full unmarked count remains a different problem.
- All logarithmic power-trace signs follow from positive S, but do not force
  Hausdorff mixed differences. The exact polynomial witness demonstrates it.
- The heat lower bound cannot be inserted into an oscillatory Laguerre
  integral as a positive comparison. Integration by parts returns the
  genuinely missing signs of derivatives of S.
- Positive Fourier source, strip confinement, and finite zero verification
  still do not suffice: the explicit quartet counterfeit retains them all.
- Finite exterior feasibility would close the problem without consistency,
  but no source-built feasible contractions have been produced.

The corrected outcome is therefore a proved-component proposal and a
precise unsuccessful full-closure attempt, not an RH proof.

## Literature boundary

Primary source metadata/abstracts and relevant HTML were checked on
2026-09-05; this is not an exhaustive literature audit or a PDF proof audit.

- Platt--Trudgian, *The Riemann hypothesis is true up to 3*10^12*,
  Bull. LMS 53 (2021), 792--797, DOI 10.1112/blms.12460,
  https://arxiv.org/abs/2004.09765. Imported only through height 100.
- Schilling--Song--Vondracek, *Bernstein Functions: Theory and Applications*,
  second edition (2012), DOI 10.1515/9783110269338. Classical Bernstein,
  Stieltjes, and Levy vocabulary; not a source of an RH conclusion.
- Lyons, *Determinantal probability measures*, Publ. Math. IHES 98 (2003),
  167--212, https://arxiv.org/abs/math/0204325. The pair covariance identity
  is elementary and reproduced in the proof; no novelty is claimed for it.
- Liu--Pego, *On generating functions of Hausdorff moment sequences*,
  https://arxiv.org/abs/1401.8052. The classical moment representation is
  the imported general theorem in the one-scale conditional closure.
- Zhang, *On complete monotonicity of the Riemann zeta function*,
  J. Inequal. Appl. 2014:15, DOI 10.1186/1029-242X-2014-15. Its stated
  results assume RH for the relevant products. This packet uses a different
  invariant log-derivative and proves a weaker-than-Stieltjes property.
- DLMF chapters 5 and 25: classical Gamma and completed-zeta identities,
  https://dlmf.nist.gov/5 and https://dlmf.nist.gov/25.

Existing Riemann/Wald/Thorin and infinitely divisible zeta-distribution
literature deserves further specialist comparison. No unreviewed claimed
RH proof in that literature is imported. The compactness and mixed-moment
criteria are classical mechanisms specialized here, not priority claims.
