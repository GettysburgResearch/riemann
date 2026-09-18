# Primary sources, attribution, and reading boundaries

This bibliography distinguishes imported mathematics from this conversation's
proposed deductions. Links identify sources, not copies bundled into the repo.
No third-party paper text is reproduced in the retained artifact set. There is
no exhaustive novelty or current-open-status audit.

## Dynamics and the first motivation

- **W98:** S. C. Woon, *Fractals of the Julia and Mandelbrot sets of the Riemann
  Zeta Function*, arXiv:chao-dyn/9812031 (1998).
  https://arxiv.org/abs/chao-dyn/9812031
  Numerical dynamical context; no RH theorem is imported.
- **BR17:** Barry Brent, *Experiments with the dynamics of the Riemann zeta
  function*, arXiv:1703.08779v2 (2017).
  https://arxiv.org/html/1703.08779v2
  Experimental inverse spirals and the acknowledged difficulty of constructing
  zero-location bands independently. Not a proved spiral-based RH criterion.
- **KOENIGS:** Local Koenigs linearization; a readable primary exposition is
  Terence Tao, *Newton iteration and the Siegel linearisation theorem* (2015).
  https://terrytao.wordpress.com/2015/04/14/newton-iteration-and-the-siegel-linearisation-theorem/
  Only the local attracting/repelling linearization is used here.
- **K16:** Tomoki Kawahira, *The Riemann hypothesis and holomorphic index in
  complex dynamics*, arXiv:1602.06843; Experimental Mathematics 27 (2018), 37–46.
  https://arxiv.org/abs/1602.06843
  Established dynamical characterization involving RH and simplicity for its
  map. The conversation's multiplicity-normalized variant is separately derived.
- **XI:** NIST DLMF, sections 25.2 and 25.4, zeta definition and reflection.
  https://dlmf.nist.gov/25.2 and https://dlmf.nist.gov/25.4
  Normalization of xi, zeta's Laurent expansion, and functional equation.
- **LI:** Xian-Jin Li, *The positivity of a sequence of numbers and the Riemann
  hypothesis*, J. Number Theory 65 (1997), 325–333; Enrico Bombieri and Jeffrey
  C. Lagarias, *Complements to Li's criterion for the Riemann hypothesis*,
  J. Number Theory 77 (1999), 274–287.
  https://www.nokia.com/bell-labs/publications-and-media/publications/complements-to-lis-criterion-for-the-riemann-hypothesis/
  Classical positivity criterion and symmetric zero-sum interpretation.
- **APS22:** Athanasios Sourmelidis, Jörn Steuding, Ade Irma Suriajaya,
  *The a-points of the Riemann zeta-function and the functional equation*,
  arXiv:2204.13887 (2022).
  https://arxiv.org/abs/2204.13887
  Fixed-a theorem and value-distribution background. Moving-target uniformity
  is not imported, and no a-point estimate is used to prove the later bounds.

## One-sided integral and arithmetic approximation

- **BSY13:** H. M. Bui, S. J. Lester, M. B. Milinovich, *On Balazard, Saias,
  and Yor's equivalence to the Riemann Hypothesis*, arXiv:1306.0856 (2013).
  https://arxiv.org/abs/1306.0856
  Restates the BSY identity and supplies the unconditional truncated identity
  in Theorem 1.2. RH-assuming finer asymptotics in the paper are not used as
  unconditional input. The original BSY identity is credited through this paper.
- **BD02:** Luis Báez-Duarte, *A strengthening of the Nyman–Beurling criterion
  for the Riemann hypothesis*, arXiv:math/0202141.
  https://arxiv.org/abs/math/0202141
- **B18:** Michel Balazard, *An arithmetical function related to Báez-Duarte's
  criterion for the Riemann hypothesis*, arXiv:1812.04309v1 (2018).
  https://arxiv.org/abs/1812.04309
  Weighted sequence realization, Section 2's biorthogonal construction and
  coefficient functionals, and the divisibility/approximation Question 2.
  The original Vasyunin source is *On a biorthogonal system associated with the
  Riemann hypothesis*, St. Petersburg Math. J. 7 (1996), 405–419. It was not
  independently read for this compilation; the attribution is via Balazard.
- **G06:** Bhaskar Bagchi, *On Nyman, Beurling and Baez-Duarte's Hilbert space
  reformulation of the Riemann hypothesis*, arXiv:math/0607733 (2006).
  https://arxiv.org/abs/math/0607733
  Theorem 1 supplies the sequence criterion. Remark 4 supplies squarefree-only
  sufficiency under RH. This conditional direction is not reproved here.
- **H22:** F. Calderaro, J. Manzur, W. Noor, C. Santos, *Orthogonality questions
  in the Hardy space related to zeta-zeros*, arXiv:2203.05030.
  https://arxiv.org/abs/2203.05030
  Related zero-kernel orthogonality; no full discrete synthesis is imported.
- **B01:** Jean-François Burnol, *A lower bound in an approximation problem
  involving the zeros of the Riemann zeta function*, arXiv:math/0103058v2;
  Advances in Mathematics 170 (2002), 56–70.
  https://arxiv.org/abs/math/0103058
  Positive 1/log N lower scale and multiplicity-sensitive refinement.
- **BCF12:** Sandro Bettin, J. Brian Conrey, David W. Farmer, *An optimal choice
  of Dirichlet polynomials for the Nyman–Beurling criterion*, arXiv:1211.5191.
  https://arxiv.org/abs/1211.5191
  Its sharp asymptotic assumes RH and an additional reciprocal-derivative bound.
  Neither assumption is discharged by this conversation.
- **B02:** Jean-François Burnol, *On an analytic estimate in the theory of the Riemann Zeta function
  and a Theorem of Baez-Duarte*, arXiv:math/0202166.
  https://arxiv.org/abs/math/0202166
  Shifted-Mobius/Hardy-space context. Its uniform zeta-ratio estimate assumes
  RH; it is not imported here as an unconditional upper bound.
- **GY01:** D. A. Goldston, C. Y. Yıldırım, *Higher correlations of divisor sums
  related to primes I: Triple correlations*, arXiv:math/0111212.
  https://arxiv.org/abs/math/0111212
  Truncated von Mangoldt sums. No required all-shift cumulative variance estimate
  is claimed as a consequence without additional argument.

## Finite evaluation, GCD spectra and operator context

- **DH20:** Sébastien Darses, Erwan Hillion, *An exponentially averaged Vasyunin
  formula*, arXiv:2004.10086.
  https://arxiv.org/abs/2004.10086
  Ordinary Vasyunin cotangent identity and reciprocity context. The implemented
  algorithm is paired cubic construction, not a continued-fraction logarithmic
  implementation.
- **LS:** J.-H. Evertse, MasterMath Analytic Number Theory, Chapter 11,
  *The large sieve*; additive large sieve with the Q^2+4*pi*x constant.
  https://pub.math.leidenuniv.nl/~evertsejh/Chapter%2011.pdf
  Imported exactly for the finite rational-frequency bound in the tail proof.
- **DLMF5:** NIST DLMF 5.11, equation 5.11.2 and positive-real remainder bound.
  https://dlmf.nist.gov/5.11
  Digamma expansion underlying the N=20 interval enclosure.
- **GCD14:** C. Aistleitner, I. Berkes, K. Seip, M. Weber, *Convergence of
  series of dilated functions and spectral norms of GCD matrices*,
  arXiv:1407.5403. Background cited in the original rigidity response. https://arxiv.org/abs/1407.5403
  The finite covariance and its Mobius diagonalization are proved directly;
  no external GCD spectral asymptotic is a load-bearing input.
- **RAM23:** N. E. Thomas, K. V. Namboothiri, *On near orthogonality of certain
  k-vectors involving generalized Ramanujan sums*, arXiv:2312.07098. Background
  cited in the original response. https://arxiv.org/abs/2312.07098
  The precise finite identities used here have elementary proofs and exact checks.
- **SC00:** Jean-François Burnol, *An adelic causality problem related to
  abelian L-functions*,
  arXiv:math/0001013. https://arxiv.org/abs/math/0001013
  Relevant operator precedent, not a bounded reflection theorem supplied here.

## Repository and conversation provenance

The last packet is pinned at PR #901 head
`001fe76229324946a915d4db84282324f7ff9673`; its original main base is
`f99d9e3908dde4865377c75d9ca051c1f545bf4f`. The original sources/validation pages
record the earlier reading boundary. PR #892's reciprocal hierarchies and
#898/#900's Observatory are context only; they are not asserted proof dependencies.

This consolidation read the current PR metadata, its scope and repository agent
instructions, all supplied source notes, and the retained scripts/results.
Primary arXiv metadata was refreshed for W98, K16, APS22, BSY13, G06, B01, BCF12,
DH20, B02, GY01, GCD14, RAM23, SC00 and B18; BR17's HTML was available. The direct B18 HTML request failed in this
session, so earlier source-note reading receipts are not represented as a fresh
full reading. No original third-party paper is copied into the repo, and no
abstract-only read is claimed as an independent proof audit.
