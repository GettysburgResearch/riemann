# Source identity, attribution and reading scope

No exhaustive literature-priority claim is made. This packet does not newly
prove Cauchy, the BGL mean, the DF sieve/detector, or CT's automorphic source.
The proposed new composition is their stated source-compatible use giving
11/12, with explicit positive-slack parameters and complete contour costs.

## Primary external sources freshly read in this pass

1. Dean Cureton and Jesse Thorner, *A quasi-Riemann hypothesis for Dedekind
   zeta functions*, Hexagon 2610.00200v2, revision 14 October 2026.
   Landing: https://hexagonmath.org/2610.00200v2
   PDF: https://hexagonmath.org/pdf/2610.00200v2
   TeX: https://hexagonmath.org/api/v1/works/2610.00200v2/source?path=DedekindZeta.tex
   Source index: https://hexagonmath.org/src/2610.00200v2/files
   These URLs were successfully opened through the web reader after following
   the landing-page links. Initial direct retrieval failures and a failed
   container download are not claimed successful. The browser source index
   displays DedekindZeta.tex and hash prefix f54808ad0f967b54; no full source-file
   hash or local PDF download is claimed. The landing page states CC BY 4.0.

   Inspected in the actual v2 text: Section 7 (allowed generators, unit classes,
   zero-extension and Kummer conductors); Section 9 (Proposition 9.1 and its
   explicit arbitrary-fixed-M>1 support-exponent paragraph); Section 10 (the
   complete additive normalization); Section 11 (triple Mellin identity,
   Lemma 11.1 correction domain/height bound, Lemma 11.2 principal H); Section
   13 (contours, joint xi+z height decay, principal residues and large U); and
   the final abelian/finite-order Hecke descent. The browser's TeX line windows
   are approximately 645--728, 970--1040, 1084--1202, 1317--1423. Section numbers,
   labels and formula content are the primary identifiers, not mutable reader
   line numbers. We read the remaining foundational discussion only where needed
   to locate these interfaces. No complete independent KP/theta reconstruction,
   Lean build, comparator or transitive axiom audit was performed.

   In particular this pass resolves the fresh-v2-access limitation recorded by
   #958 for these interfaces; it does not retrospectively claim that #958's
   author fetched the primary file or certify the whole CT proof.

2. Valentin Blomer, Leo Goldmakher and Benoit Louvel, *L-functions with n-th
   order twists*, arXiv:1112.1650, published IMRN 2014(7), 1925--1955.
   https://arxiv.org/pdf/1112.1650
   The 21-page arXiv PDF was read, with screenshots of PDF pages 17--19
   (zero-based 16--18). Load-bearing scope: Theorem 1.3 and Section 5,
   especially (5.1), its complete-column AFE/powerful decomposition, and
   (5.3)--(5.5). Equation (5.1) is already a weighted all-index statement;
   setting the sixth-power part to one retains EVERY sixth-free row.
   The fixed S-ray twists are adapted in PROOF Section 3, not assumed absent.
   BGL's sharper multiple-Dirichlet-series theorems and nonvanishing results
   are not inputs. No conjectural estimate is extracted from the paper.

3. Alexandre de Faveri, *Optimal large sieve for fixed order characters*,
   arXiv:2610.04045v1.
   https://arxiv.org/html/2610.04045v1
   Inspected: Theorem 1.1, Corollary 1.5, Section 2.3.1--2.3.4's choice-dependent
   generators and deep ray modulus, Section 2.5's conductors/multiplicativity,
   and the complete Corollary 1.5 calculation in Section 9. BOTH indices of
   its enlarged sieve are sixth-power-free; the index norm is the full norm.
   The three rational substitutions here use its displayed detector inequality.
   The source's own piecewise parameter formulas are reproduced by the checker.
   Its norm-order versus radical/conductor-order distinction is retained.
   The cubic conductor-ordered and multiple-series results are not used.

Classical analytic facts used alongside these papers: finite-dimensional ray
class/Kummer theory, ideal counting, ordinary Hecke analytic continuation and
convexity, Cauchy/Minkowski, Borel--Caratheodory, Hadamard three circles, Mellin
inversion and abelian class-field factorization. The papers provide their
required fixed-field implementations. No claim that all those classical
foundations were rebuilt in this execution environment is made.

## Exact internal sources and inherited work

- Parent #958, e6dfa07d07ed7a5d049039d7255919a992cadc77,
  standalone/2026-10-17-stratified-dedekind-density/CONTRACTS.md
  (blob 3ab34cd2a464617dc240b47f0ff0460ba6b816f2) and PROOF.md:
  finite zero strata, fixed exceptional sets, reciprocal disks, full-frequency
  split and the proposed 25/27 bound. The contracts and relevant proof through
  the central/tail comparison were read live. Their scalar-convexity ceiling
  is a restriction of that estimate, not a prohibition on the numerator mean.
- #957, ec54cb6b0029aedd8a99e6016a42a1426a0223a2: the earlier 23/24 adapter
  and its family identification are credited from its detailed live PR and
  #958's quoted proof. Its full nine-file packet was NOT independently replayed.
- #955, 6d3d69c7896e3a5d61d1f67e4627125257398ec7: the complete long-twist
  moments and fixed-center warning are respected. No bounded native source
  is inferred from that worst-center discussion.
- The two pending local packets are already recovered on #958 with unchanged
  trees. RECOVERY_AUDIT.md records this execution's actual read-back/hash/replay
  scope. They are NOT analytic premises of the proposed 11/12 theorem.

Neither #957's 23/24 nor #958's 25/27 conclusion is used as a black box. This
packet recomposes their stated unconditional source inputs at new scales.
A mismatch in CT's source or the fixed-twist BGL/DF family adapter would
invalidate the new global consequence even if every finite predicate passed.
