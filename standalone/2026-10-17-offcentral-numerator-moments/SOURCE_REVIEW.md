# Source identity, live comparison, and review boundary

This packet imports stated unconditional analytic results and proves proposed
deductions from them. It does not claim a full independent reconstruction of
metaplectic theory, DF's large sieve, or BGL's analytic zero detector. Proof and
checker have the same author. No external referee or commissioned second agent,
Lean build, transitive axiom audit, actual L-value calculation, or repository-wide
validator was performed. Arithmetic tests cannot certify these interfaces.

## Primary sources inspected in this pass

1. Cureton--Thorner, A quasi-Riemann hypothesis for Dedekind zeta functions,
   Hexagon 2610.00200v2, revision 14 October 2026.
   https://hexagonmath.org/2610.00200v2
   https://hexagonmath.org/api/v1/works/2610.00200v2/source?path=DedekindZeta.tex
   Actual TeX read: allowed generators and Kummer rows in Section 7;
   Proposition 8.3 and the separated reflection (8.15), including the complete
   local beta weights and uniform finite profiles; Section 9's reflected dyad
   and explicitly supercritical simplification; Section 10's uncombined additive
   normalization; Section 11's exact scale factor, character ratio, correction
   domain and principal numerator; and Section 13's joint-height and tail
   arguments. Web-reader ranges were approximately 624--680, 875--1015,
   1065--1202, and 1318 onward. Labels/formulas, not reader line numbers, are
   the source identities. The principal nonvanishing lemma is labelled
   lem:principal-nonzero in Section 11.2 (Lemma 11.1), not Lemma 11.2.
   The source index reports hash prefix f54808ad0f967b54; no complete local
   PDF/TeX hash or fresh Lean checkout is claimed. Direct retrieval initially
   failed, then following the landing links succeeded in the web reader.

2. Alexandre de Faveri, Optimal large sieve for fixed order characters,
   arXiv:2610.04045v1.
   https://arxiv.org/html/2610.04045v1
   Read Theorem 1.1 and the definitions of both full-flat indices; the fixed
   generator/ray choices in Section 2.3; Section 2.5.1's conductor and nonunit
   convention; the AFE separation used in Section 8; Corollary 1.5 and its
   COMPLETE ten-term detector calculation in Section 9. We use the n=6 ideal-
   norm sieve, not the stronger cubic conductor-ordered result. Fixed S-ray
   twists multiply common columns. Every numerical density substitution is
   reconstructed from that displayed detector, not read off a fitted exponent.

3. Blomer--Goldmakher--Louvel, L-functions with n-th order twists,
   arXiv:1112.1650, IMRN 2014(7), 1925--1955.
   https://arxiv.org/pdf/1112.1650
   Section 5, especially (5.1) and (5.3)--(5.5), read in text and rendered
   screenshots of zero-based PDF pages 16 and 17. The second mean and full
   AFE/powerful-column and detector conventions were inspected. We do not
   attribute our new off-central fourth/eighth estimates to a stated BGL
   theorem. They are derived in MOMENTS.md from DF's full-flat sieve and the
   classical functional equation, preserving conductor and column support.

Classical tools used explicitly: primitive Hecke analytic continuation and
functional equation, smooth AFE for its fixed integer powers, ideal counting
and divisor bounds, Minkowski/Holder, Borel--Caratheodory and three circles,
Mellin inversion and abelian class-field factorization. The new proof exposes
where these enter rather than asserting a numerical check proves them.

## Repository sources actually read

- #965, d58e3282a9379b6ae165681bc2e21e4f9fd18c26:
  standalone/2026-10-17-subcritical-dedekind/PROOF.md,
  blob 02969ee622c407a3029d3745b9db7b67e9b36169. The full proof was read,
  including the short-support reconstruction and complete contour split.
  Its 91/100 theorem is not assumed. We use its reconstructed source estimate.
- #966, 8d94494698ee447711a53dec922986586418e398:
  standalone/2026-10-17-selected-fourth-density/PROOF.md,
  blob 08195836816c1e3718c04e0b966bf89a0b5dad01. This appeared concurrently;
  its full PROOF.md was read, not just the PR description. Its central fourth
  moment, selected-count density and 109/120 proposal are acknowledged.
  Its separate CONTOURS.md and whole checker were NOT replayed. Neither its
  new density nor its global conclusion is an analytic premise here.
- #968, 14f544fb4293ffb59942ff8d345ab9d6da67025c, appeared at the later
  pre-publication check. Its full NUMERATOR_MOMENTS.md was read, blob
  cab3ec0dd6680fe6e488d11f7f95f6f771c89ed1. It already records all fixed-order
  CENTRAL numerator bounds and proposes 10/11; we credit those overlaps.
  Its complete composition/checker were not replayed and are not inputs.
- #961/#959: their context and exact refinements are retained through #965.
  No claim is made to have re-reviewed their entire upstream foundations.
- #964 and other contemporaneous routes were seen at description scope only;
  they are not premises of this packet.

## Recovery completed before new mathematics

The user was correct that the 91/100 ROUTE was already on #965. Its ten-file
packet was not byte-identical to the earlier thirteen-file upload in this
conversation. That distinct historical source is now recovered in #967:

- head b7215948884cedb1b5062dd541bc79ec765e8e4c;
- branch research/subcritical-archive-recovery-20261017;
- root tree 976841345c0b0ea2f4bc95d7cc4822984869dcd5.

All original thirteen scientific files are compressed losslessly into four
binary transport parts, with a safe restore script and publication-only notice.
Fresh full normal/optimized checkers and all eight original mutation processes
reproduced their archived reports; manifest and byte comparisons passed.
All SIX remote recovery file hashes and sizes were read back and match the
local payload. No original mathematical qualification or NOT PUSHED label was
rewritten; the new notice supersedes only publication status.

#966 recovered a DIFFERENT archive, riemann-short-support-theta-20261017.zip,
source tree a80cb7e2404e0f6835c47017597b6acbeb9cb264, based on #959. Ours is the
riemann_subcritical_91_100.zip packet based on #961, scientific source tree
5ace9da6553854222a5ac7c4277088373277de96. Their filenames, hashes and bases were
checked; they are not conflated. No unseen work from other conversations is
claimed recovered. The new continuation is additive on #967, not a rewrite
or a duplicate announcement of either earlier 91/100 argument.

## Highest-priority adversarial checks

First challenge MOMENTS (2)--(8): complete-column q_c^-3 summability, original
nonunit masks, AFE of L^k off center, common-coefficient separation, and the
negative dual conductor power for SMALL conductors. Then check the inherited
physical reflection, generator transfer, the first threshold at 2/3 plus a
strict e buffer, all fifteen density classes and the changed small-z line.
Finally audit Mellin inversion and pointwise-e descent. A mismatch in any of
these analytic interfaces invalidates the global consequence despite the
finite checker or authenticated Git publication.
