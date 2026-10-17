# Sources and exact dependency scopes

All research statements in this packet are proposed at their written
scope. Published source statements, our deductions, arithmetic fixtures,
and unresolved principal-member extraction are different obligations.
The proofs cite classical techniques without worldwide priority claims.

## Load-bearing new-paper input: the common Dirichlet strip

OpenAI, *The Quasi-Riemann Hypothesis: A Zero-Free Half-Plane Re(s)>7/8*,
30 September 2026, Theorem `thm:main` and its preceding uniform-exclusion
definition. Exact GitHub commit:
1581d4cbdd69a0faf34b2089614fe2a814316a6a.
TeX blob: 268c4e3206d460c617d3d2129742a72b831b3def.

https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex

The primary theorem explicitly asserts a common half-plane for ALL
Dirichlet L-functions, including the principal character, with a pole at
one allowed. Its scope is stronger than nonvanishing of one Dedekind
zeta function. The theorem statement and definitions were freshly read
in this pass; the entire underlying theta/moment proof and its Lean
dependency graph were not freshly rebuilt. The application of our
abstract ZF(theta) theorem to theta=7/8 is source-qualified on this
reported theorem. The angular-ray theorem does not assume it.

## Classical comparison and tools proved in the packet

R. C. Baker and G. Harman, *Exponential Sums Formed with the Mobius
Function*, J. London Math. Soc. s2-43 (1991), 193--198.
https://doi.org/10.1112/jlms/s2-43.2.193

The publisher bibliographic record was inspected; the original full PDF
was unavailable in this session. Its relevant statements are explicitly
reproduced in these primary research papers, both freshly inspected:

- Wei Zhang, *On an exponential sum related to the Mobius function*,
  arXiv:2204.04613v2, 16 October 2022, introduction and Lemma 2.2.
  https://arxiv.org/html/2204.04613v2
  This gives the exact linear major-arc estimate and classical exponent
  (1+theta)/2 for theta>=3/5. Its separate theta<=4/7 density improvement
  is not used.
- Xiaoguang He and Bingrong Huang, *Exponential sums involving the
  Mobius function*, author manuscript dated 10 April 2015, (1.3)--(1.4),
  Lemma 2 and the following analytic proof mechanism.
  https://bingronghuang.github.io/expsum2016he.pdf
  Its common-strip hypothesis and conductor-uniform reciprocal bound
  were read. Its Lemma 3 concerns nonlinear monomials of degree>=3;
  it is not substituted for a linear theorem.

STRIP_AND_MAJOR_ARCS.md proves the reciprocal-product analytic adapter
directly, including its sharp-cutoff Perron errors. DIRECT_FOURIER.md
proves its finite inverse identity, elementary geometric and bilinear
estimates, cutoff separation and grouping. The required Dirichlet
analytic continuation, Euler products, periodic character bound,
Borel--Caratheodory, three-circles, Perron, Plancherel and elementary
divisor estimates are classical. The common-strip input is not hidden
inside the elementary lemmas.

## Repo predecessors for source identification

- #962, b2032c663736ecd1e3872559d160ce069664ea06:
  https://github.com/GettysburgResearch/riemann/pull/962
  Base of this branch. Its actual Gaussian/source conventions and
  critical coefficient-kernel method are retained where cited.
- #963, c91fd9ddfb37668338d9aec22c0e29cfe741cf07:
  https://github.com/GettysburgResearch/riemann/blob/c91fd9ddfb37668338d9aec22c0e29cfe741cf07/standalone/2026-10-17-archimedean-ideal-resolution/PROOF.md
  Full main proof read. Supplies the comparison with earlier hybrid
  ideal resolution, not a missing arithmetic assumption for the new
  elementary ray proof.
- #964, 09ab9bc067bc66278fad8fcd883e8c8569b0cbc9:
  https://github.com/GettysburgResearch/riemann/blob/09ab9bc067bc66278fad8fcd883e8c8569b0cbc9/standalone/2026-10-17-native-local-uniformity/PROOF.md
  Full proof read. Exact norm aggregation, completion families, caps,
  asymmetric ideal exclusions and BV convention are retained. Their
  propagation is written again in the present packet, without assuming
  #964's logarithmic theorem is a power theorem.

NATIVE_ANGULAR_RAY_MOMENT.md uses only elementary arithmetic of
Z[omega], its six units, lattice ideal counting, squarefree inversion,
periodic chi_{-3} cancellation and the Gaussian Poisson formula. All
needed ray/cofactor and separation calculations are supplied there.
No angular Hecke zero-free theorem is imported.

## Recent work audited but not assumed in the new arithmetic proofs

- Cureton--Thorner, *The quasi-Riemann hypothesis for Dedekind zeta
  functions*, Hexagon 2610.00200v2. The cached primary TeX remained
  accessible by its retrieved source reference, although a new direct
  URL request failed earlier in this pass.
  https://hexagonmath.org/2610.00200v2
  https://hexagonmath.org/api/v1/works/2610.00200v2/source?path=DedekindZeta.tex
  Relevant reflection, source definition and principal/nonprincipal
  comparison sections were inspected. No full transitive theta or
  formal proof audit is asserted.
- Alexandre de Faveri, *Optimal large sieve for fixed order characters*,
  arXiv:2610.04045v1, 2 October 2026, (1.2), Theorem 1.1, Sections 2.3,
  2.5 and 9.
  https://arxiv.org/html/2610.04045v1
  Fresh primary full-flat-family, conductor, mask and detector checks
  support the interfaces discussed in MOMENT_INTERFACE_AUDIT.md.
- Valentin Blomer, Leo Goldmakher and Benoit Louvel, *L-functions with
  n-th order twists*, arXiv:1112.1650, Section 5, (5.1)--(5.5).
  https://arxiv.org/pdf/1112.1650
  The full pre-Cauchy detector and complete-column mean were inspected.
- Baiying Liu, *Slightly improved zero-free half-planes for the
  quasi-Riemann hypothesis*, arXiv:2610.12234v1.
  https://arxiv.org/html/2610.12234v1
  The abstract/introduction, parameter formula and relevant stated
  dependency account were inspected; no complete independent proof
  or Lean replay is claimed. Its numerical improvement is not used.

LATEST_REVIEW.md pins the seven concurrent PR heads, including the
one-file off-central numerator checkpoint #969. Their proposed global
Dedekind conclusions are not assumptions of either new proof here.
