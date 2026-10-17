# Sources, exact pins, and what was actually inspected

This is a source-qualified proposed research packet, not a claim to have rebuilt
all upstream analytic theory. The new contribution is the selected-cardinality
block/moment estimate, its self-restricted density use, and a complete new
finite contour composition. AFE, Holder, large-values, Mellin zero detection,
convexity and class-field descent are classical and credited. No global
literature-priority or independent-referee claim is made.

## Primary external sources

1. Alexandre de Faveri, Optimal large sieve for fixed order characters,
   arXiv:2610.04045v1, https://arxiv.org/html/2610.04045v1 .
   Fresh primary HTML was accessible. Theorem 1.1, the definitions of Xi_n and
   Theta_n preceding it, and Section 9's complete zero-density calculation were
   read. Theta_n has BOTH indices n-th-power-free; at n=6 its four terms are
   precisely U+V+U^(5/6)V^(1/3)+U^(1/3)V^(5/6). The full index norm, not conductor
   or radical ordering, is retained. The character construction and fixed-data
   convention are in Sections 2.3--2.5. No reconstruction of the recursive sieve
   proof, root-number coupling or all its dependencies was performed here.

2. Valentin Blomer, Leo Goldmakher and Benoit Louvel, L-functions with n-th order
   twists, arXiv:1112.1650, https://arxiv.org/pdf/1112.1650 .
   The primary PDF was accessible, and PDF pages 18--19 (zero-based 17--18)
   were rendered and read. Section 5 supplies the classical AFE/Mellin and
   zero-detector framework. Its printed detector uses the central line; the
   shifted rowwise form in DENSITY.md is reconstructed explicitly and overlaps
   the later repository #971. No unprinted shifted formula is ascribed to BGL.

3. Dean Cureton and Jesse Thorner, A quasi-Riemann hypothesis for Dedekind zeta
   functions, Hexagon 2610.00200v2, revision 14 October 2026.
   Intended primary URLs:
   https://hexagonmath.org/2610.00200v2
   https://hexagonmath.org/pdf/2610.00200v2
   https://hexagonmath.org/api/v1/works/2610.00200v2/source?path=DedekindZeta.tex
   FRESH BODY RETRIEVAL FAILED in this execution through these reader requests.
   We do not describe earlier agents' successful reads as this pass's reads.
   The full physical/Poisson interfaces are adopted from the exact pinned
   repository proofs below. The formal repository pin is
   AxiomMath/DedekindZetaZeroFree@09afbb4ce6570c1615d58509dc197fc9f0956b7d;
   no Lean build, comparator or transitive axiom audit was run. The new domain
   and subcritical scale use are proposed repository reconstructions, not
   silently asserted to be already formalized upstream.

Classical fixed-field Hecke analytic continuation, AFE for fixed powers,
functional equations, ideal counting, divisor bounds, subharmonic disk means,
Sobolev and binary maximal decompositions are used with their ordinary fixed-data
quantifiers. No new conductor/discriminant-uniform assertion is imported.

## Exact repository dependencies and overlap

- #965, d58e3282a9379b6ae165681bc2e21e4f9fd18c26,
  standalone/2026-10-17-subcritical-dedekind/PROOF.md.
  The actual proof and full twenty-two-class continuation were previously read
  in this live thread. It supplies the adopted unrestricted reflection
  reconstruction N+N^2/Z, complete auxiliary sums, actual Poisson source,
  character adapter, correction and joint-height normalization. Its proposed
  91/100 conclusion is NOT used as a black box or fed back into the proof.

- #966, 8d94494698ee447711a53dec922986586418e398,
  standalone/2026-10-17-selected-fourth-density/PROOF.md.
  Full text read live. Central fourth moments and retaining a count factor in
  Holder are already present; 43/60 at three quarters and the proposed 109/120
  global region are credited, not rediscovered. The new density retains the
  count inside BOTH norms rather than estimating those norms on all rows.

- #968, 14f544fb4293ffb59942ff8d345ab9d6da67025c,
  standalone/2026-10-17-fourth-numerator-dedekind/NUMERATOR_MOMENTS.md.
  Full text read live. Complete sixth-power column removal, fixed-order full
  numerator moments, dual conductor separation and the distinction from native
  inverse moments are inherited. Our moment bound changes the actual family
  norm, not merely the subsequent Holder exponent.

- #969, initial 2eaa5b5221c1f2b8998fa32ebf9023471e5b7a18, final
  6542781188469e8a23dadf9d419b3d5cf4d11de7,
  standalone/2026-10-18-offcentral-numerator/OFFCENTER_MOMENT.md.
  The complete unchanged component was read at its initial pin. Actual-conductor
  off-central moments at 7/12 and 5/12 and their physical Y-weight advantage are
  credited. The later proposed 49/54 composition was read at PR-description
  scope, not independently replayed. The present selected moments are stronger
  for some sparse families and do not claim off-central AFE as a new method.

- #970, 026f70fc91f221296b4a4ad874dc2235c5ba07ac,
  standalone/2026-10-18-local-support-recovery/.
  THIS PASS published all nineteen original files of the previously unpushed
  68/75 packet, byte-preserved in the authenticated archive. Its LOCAL_DOMAIN.md,
  MOMENTS_AND_DENSITY.md and PROOF.md were read from the supplied original bytes.
  The enlarged local domain is an essential adopted proposal, not re-proved or
  independently certified by the new finite checker. The old normal/optimized
  checker, manifest and nine mutations were freshly replayed before recovery.
  The archive's SHA-256 is
  48e7398a17d57ba2e1f07a1bf39caaa318817ab931b6d246c857efea2df7f490.
  This new packet is stacked on that recovery; no historical bytes are changed.

- #971, 3f1d2a07631eb6cca1f2716be01f64e874667639,
  standalone/2026-10-18-ramified-shifted-detector/SHIFTED_DETECTOR.md.
  FULL TEXT read live. It already reconstructs a shifted Mellin zero detector,
  including prefix/height maxima, and gives 395/552 at three quarters. Those
  methods are credited. The new 5/7 deduction is different because its two
  moments themselves retain R. The ramified-factor companion was seen at
  metadata/description scope, not imported as a silently reviewed alternative
  to #970's LOCAL_DOMAIN. This head does not announce a new global boundary.

- #974, 89c37b6707cb77fc5a86143ea98d8756759fdcbc, and #975,
  edbc27b61208ccc7ee1fa99fa3f4e861f5a03452, were found in the late refresh at
  PR-DESCRIPTION scope only. They overlap the earlier local-domain and
  off-central work and develop a separate transverse prime detector. They are
  not premises of this packet; their finite checkers were not rerun here.
  No claim that the recovered local-domain argument is globally unique is made.

Earlier distinct 91/100 recovery #967 and #961's source/import packet were
already published. No unseen work from unavailable conversations is claimed
recovered, and publication order is not mathematical priority.

## What could invalidate the proposed global consequence

A failure of the complete-column sieve/AFE adapter or the same-subset moment
estimate would invalidate the new hereditary bounds. A failure of the rowwise
shifted detector/maximal step would invalidate its density improvement. A
failure of the adopted short-support reflection, enlarged correction domain,
actual character identification or full Mellin comparison would invalidate
633/700 even if the two new component theorems survive. Rational tests and
Git hashes address none of these infinite analytic obligations by themselves.
