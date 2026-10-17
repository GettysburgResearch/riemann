# Sources, reading scope, and qualifications

## Exact repository sources

- #965, d58e3282a9379b6ae165681bc2e21e4f9fd18c26:
  standalone/2026-10-17-subcritical-dedekind/PROOF.md,
  SOURCES.md, and verify.py. PROOF Sections 1--3.2 and 4--6 were read through
  the connected GitHub file interface; the detector parameters and formula
  were checked against the complete exact verifier. The source supplies the
  M<1 reflected reconstruction, full CT Poisson/correction contracts, fixed
  S-unit family adapter, density detector, and contour/tail organization.
  The new proof does NOT assume its zero-free conclusion. Its most important
  unresolved REVIEW obligation remains the full source-level reconstruction
  of the reflected bound, not a fourth-moment arithmetic hypothesis.
  Source proof Git blob: 02969ee622c407a3029d3745b9db7b67e9b36169.
  Source account Git blob: d65463e9a7255bcb254e5917be38e1a55276e97c.

- #959, 7b845294207d96b883c1fa95028663082267804f:
  standalone/2026-10-17-numerator-mean-refinement/PROOF.md and SOURCES.md.
  The complete available excerpt through the central comparison and the source
  account were inspected. Credit: using the numerator family rather than
  individual convexity, zero-selected subset Cauchy, and fixed reciprocal
  rectangles. Its proposed 11/12 conclusion is not an input.

- #961, 7bd275b44261fff93bb565a9342c44b7c66526f6:
  standalone/2026-10-17-review-imports-theta-escape/THETA_ESCAPE.md,
  read in full. Its M>1 ceiling and OPEN-L are not contradicted on that domain;
  #965 changes the physical scale regime. OPEN-L is not assumed or proved here.

- #963, c91fd9ddfb37668338d9aec22c0e29cfe741cf07:
  standalone/2026-10-17-archimedean-ideal-resolution/PROOF.md, read from the
  user-delivered ZIP. Its full radial/angular mean resolves geometric ideal
  collisions but does not bound a fixed principal member. That theorem is
  not an analytic input to the present detector composition.

The checker uses the elementary rational density parametrization from the
pinned #965 verifier, with new classes and independent implementation of the
polynomial/finite-phase checks. Same-author code/proof is not an independent
mathematical referee. No full historical priority audit was performed.

## Primary mathematical inputs, ADOPTED AT THE PINNED INTERFACE SCOPE

CT: Dean Cureton and Jesse Thorner, A quasi-Riemann hypothesis for Dedekind
zeta functions, Hexagon 2610.00200v2 (revision 14 October 2026).
https://hexagonmath.org/2610.00200v2
https://hexagonmath.org/api/v1/works/2610.00200v2/source?path=DedekindZeta.tex

DF: Alexandre de Faveri, Optimal large sieve for fixed order characters,
arXiv:2610.04045v1, Theorem 1.1, character construction and density detector.
https://arxiv.org/html/2610.04045v1

BGL: Valentin Blomer, Leo Goldmakher and Benoit Louvel, L-functions with n-th
order twists, arXiv:1112.1650; IMRN 2014(7), 1925--1955. Complete AFE and central
family framework, Section 5, as specified in #959/#965.
https://arxiv.org/abs/1112.1650

IMPORTANT: fresh web retrievals of CT's v2 landing/PDF/TeX and DF's v1
HTML/PDF failed in this pass (502/404 or unsafe-open errors). #965 reports a
successful primary-source inspection; this pass inherits those precise
interfaces and does not claim to repeat that inspection or verify its report.
No fresh BGL proof reconstruction, upstream Lean build, comparator, transitive
axiom audit, or independent analytic certification was performed.

NUMERATOR_MOMENTS explicitly states the full sixth-free sieve S6 and complete
AFE compatibility needed here. If the source supports only squarefree indices,
different fixed twists, or different uniformity, the new claim would fail.
The contour arithmetic checker does not decide those questions.

## Other attempted directions, not used as premises

An additive-Fourier consequence of a uniform Dirichlet half-plane was explored.
Cha and Kim, arXiv:2504.06726v1 HTML, was actually read; it recalls the classical
Hajela--Smith/Baker--Harman exponents and states the Type I/II bounds. The PDF
screenshot and original Baker--Harman PDF retrieval failed. No Fourier theorem,
new affine-correlation bound, or literature-priority claim from that exploration
is asserted in this packet. It was superseded by the direct numerator-moment
connection after #965 appeared during the live repository check.
