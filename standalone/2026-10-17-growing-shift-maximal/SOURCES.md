# Sources and reading boundaries

## Main external premise

Kaisa Matomaki, Maksym Radziwill, Terence Tao,
*An averaged form of Chowla's conjecture*, Algebra & Number Theory 9 (2015),
2167--2196; arXiv:1503.05121v3, 1 March 2022.

- https://arxiv.org/abs/1503.05121v3
- https://arxiv.org/pdf/1503.05121
- https://doi.org/10.2140/ant.2015.9.2167

The current v3 PDF was freshly read with screenshots of printed pages 3,5,6
(zero-based pages 2,4,5). Load-bearing items: Theorem 1.7 (the general bounded
short-exponential estimate); equation (1.12) and its stated small-modulus range;
Lemma 1.4 (the finite Fourier identity, whose mixed form is derived explicitly).
The source's frequency supremum is outside the integral. Its 1/700 exponent
is retained; no stronger short-frequency maximal theorem is substituted.
The v3 metadata records a correction to Proposition A.3. This pass uses v3,
not a claim that an older appendix was freshly rebuilt.

MRT is a genuine deep imported theorem. Only its application, the quantitative
prime-distance perturbation, endpoint treatment, powerful-source approximation,
sparse-dilation estimates, mixed Fourier identity and maximal partition are
proved here. Finite checks do not reconstruct MRT's proof.

## Repository source identities

- #956: 943d7714f81b97a75652ebc6e19990a88c917d4d. Recovered affine packet,
  standalone/2026-10-17-affine-cancellation-lift/THEOREMS.md.
  Its definitions, unique supports and Lemma 3.1 tail count are reused and
  reconstructed; the prior fixed-affine logarithmic theorem is not needed
  as a premise for the new ordinary growing-shift theorem.
- #956's mesoscopic packet is preserved at tree
  13d3f1121d05f547e2067fe25103d4051e4b20cf. Positive selected covariance is not
  a lower bound on total energy. No mesoscopic asymptotic is used here.
- #952: 3b7d2948840446c752bbf284f6f90f6592395a29. Its exact Gaussian kernel
  is used only for the explicit shell corollary. This kernel is also present
  in the delivered #953 and mesoscopic proofs. Its full-energy criterion is
  not declared proved by the shell bound.
- #959: 7b845294207d96b883c1fa95028663082267804f. Live PROOF.md and SOURCES.md
  inspected for the stated family mean and remaining positive-estimate ceiling.
  No independent review or improvement of its proposed 11/12 theorem is claimed.
  Direct fresh requests for CT v2 and DF failed in this session; the older
  author's successful reading is not relabeled as this pass's primary audit.

The 13-file mesoscopic ZIP and 11-file affine ZIP are the user's delivered
archives. Their exact Git trees were reconstructed before running scripts and
matched the existing recovery tree IDs. RECOVERY.json records the actual reruns.

## Other outside work checked but NOT used

OpenAI, *Ordinary two-point correlations of multiplicative functions*,
September 24 2026 release. The official scope and primary source text surfaced
in the fresh web search. The full proof and Lean dependencies were NOT rebuilt.
The present theorem does not need that ordinary fixed-affine assertion: the
older established MRT theorem already has the growing-shift averaging needed
here. This is a mathematical choice of the applicable theorem, not refusal to
use outside work. All external results retain their actual quantifiers.

No claim of global literature novelty is made. In particular, averaged Chowla,
short-interval cancellation, Fourier/Parseval, the coefficient-support tail,
and basic maximal partitioning are credited rather than renamed as new fields.
