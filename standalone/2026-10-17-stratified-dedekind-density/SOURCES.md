# Sources and exact reading levels

## Primary sources freshly inspected

1. Alexandre de Faveri, *Optimal large sieve for fixed order characters*,
   arXiv:2610.04045v1, October 2026.
   https://arxiv.org/html/2610.04045v1
   Inspected Theorem 1.1, Corollary 1.5, the complete displayed detector
   calculation and parameter choices in its proof, and Section 2.3's
   S/modulus/generator/zero conventions. The fixed-S-unit twist adaptation
   is written out in PROOF.md; it is not silently attributed to a statement
   that omits it. No new proof of the large-sieve theorem is claimed.

2. Valentin Blomer, Leo Goldmakher, Benoit Louvel, *L-functions with n-th
   order twists*, arXiv:1112.1650v1; published IMRN 2014, 1925--1955.
   https://arxiv.org/pdf/1112.1650
   Inspected the squarefree large sieve and Section 5's central mean and
   zero detector. PDF pages 18 and 19 were freshly rendered and inspected,
   including (5.3)--(5.7), squarefree/powerful column decomposition and the
   stated norm/height costs. Those primary statements, not a secondary
   survey, are the inputs. The entire original sieve proof was not replayed.

3. Dean Cureton and Jesse Thorner, *A quasi-Riemann hypothesis for Dedekind
   zeta functions*, Hexagon 2610.00200v2.
   https://hexagonmath.org/2610.00200v2
   https://hexagonmath.org/api/v1/works/2610.00200v2/source?path=DedekindZeta.tex
   Fresh landing/PDF/TeX attempts failed. NO full v2 primary body was obtained
   in this pass. The CT input package is therefore adopted at the exact
   repository source identity below, not represented as a fresh primary
   audit. In particular this packet does not establish that a formal build
   of 31/32 already formalizes our new parameter choices.

## Exact repository imports and source qualifications

- #957 at ec54cb6b0029aedd8a99e6016a42a1426a0223a2:
  standalone/2026-10-17-dedekind-density-upgrade/PROOF.md,
  blob 3bc7cf80bdbfe1dbba84081bd1e8096ccc13987f, read in full through
  bounded fetch_file ranges. SOURCES.md, blob
  7e70fce038eb540c2dcc677d0dfccacef00ef49d, also read in full.
  https://github.com/GettysburgResearch/riemann/blob/ec54cb6b0029aedd8a99e6016a42a1426a0223a2/standalone/2026-10-17-dedekind-density-upgrade/PROOF.md
  This supplies the precise CT interface, the preceding fixed-twist adapter
  and binary-density 23/24 composition. CONTRACTS.md states exactly which
  inputs are adopted. The new finite-stratum proof uses this foundation;
  it is not an independent rediscovery of the family or an approval of #957.

- #948 at 05b6f2172c686356ccd9900d33ffc5f526c5e98b:
  standalone/2026-10-16-dedekind-quasi-rh/IMPORT.md and
  PARAMETER_BARRIER.md, freshly read in the user-delivered archived packet.
  The earlier import independently records the same reflected dyad,
  M>1 support normalization, Poisson L(w,chi)/L(xi,bar chi) factor and
  scale monomial. This is a cross-check of earlier source accounts, NOT
  a fresh retrieval of CT itself and not two independent mathematical
  referee reports. Its older 1/12 bound has a different, looser model.

- #955, 6d3d69c7896e3a5d61d1f67e4627125257398ec7, and #954:
  publication baseline and previous-packet recovery provenance. Their native
  moment/covariance results are NOT premises of the proposed 25/27 theorem.
  The critical fixed-center covariance still remains unbounded. The old
  equal-norm sign correction is retained in the separate recovery notice.

- #956, 943d7714f81b97a75652ebc6e19990a88c917d4d:
  current PR description inspected for concurrent scope only; its recovered
  affine/mesoscopic work is not an analytic input. Latest metadata before
  this packet's publication still shows #957 at the pinned head above.

Classical inputs include conductor convexity, inducing-character Euler
factors, Borel--Caratheodory, three circles, Mellin inversion, the S-unit and
class-field/Kummer frameworks, and abelian zeta factorization. The particular
reciprocal-disk and finite-threshold applications are supplied in PROOF.md.
No GRH-dependent Dedekind moment theorem is used. No exhaustive priority
claim is made for zero-density stratification, convexity or exponent methods.

## Outstanding independent-source review

The all-M scope of CT-1, exact family matching in (4), CT-D's corrected
u-weight, and CT-4's joint height control are load-bearing. Their failure
would invalidate the proposed zero-free consequence regardless of the
arithmetic tests. The full primary CT import, DF/BGL theorem rebuild,
independent mathematical referee report, and Lean/axiom audit have NOT
been completed by this packet. The explicit conditional implication from
CONTRACTS.md is the precise logical content supplied here.
