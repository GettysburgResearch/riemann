# Sources, exact scopes, and credit

## Primary sources inspected in this pass

**CT.** Dean Cureton and Jesse Thorner, *A quasi-Riemann hypothesis for
Dedekind zeta functions*, Hexagon 2610.00200v2, October 14 revision.
Primary TeX:
https://hexagonmath.org/api/v1/works/2610.00200v2/source?path=DedekindZeta.tex

The actual v2 source was freshly opened. Inspected interfaces: the local
finite Poisson factor, the complete frequency series and character ratio,
the correction-region inequalities and their ramified shell argument in
Section 11.1, and principal specialization/nonvanishing in Section 11.2.
The source explicitly attributes the finite common-prime calculation to
OpenAI's primitive-root paper. We do not claim a full metaplectic rebuild,
a transitive formal-source audit, or a Lean/comparator run. No local full
TeX/PDF byte hash is claimed from browser text. The existing normalizations,
not a newly invented theta average, identify the object in RAMIFIED_FACTORS.
CT's zero-free theorem is NOT a premise of either new component.

**OpenAI local source.** Repository `openai/math`, frozen commit
`1581d4cbdd69a0faf34b2089614fe2a814316a6a`, file
`preprints/Primitive-roots-for-every-admissible-integer-base-October-4-2026/build/sections/05-poisson.tex`.
Git blob: `c8526f74b281d37fda034c17195c4bb5afd5f79b`.

Read via the connected GitHub file reader, especially lines 470--795:
CRT unit factors, exact local-series coefficients, the C_(t,k)(J) table,
unramified rational factor, and crude ramified bound. Source labels:
`eq:C-local-definition`, `eq:C-local-values`, `eq:exact-Euler-factor`,
`eq:Euler-good-exact`, `eq:Euler-bad-exponents`.
The C table and UNRAMIFIED factor are prior work, expressly credited. The
new item is the complete five-case ramified rational sum and its stronger
domain/weighted estimates. The preceding Poisson-definition/multiplier
passages were also inspected; the entire primitive-root theorem was not.
CT's passage to a general field imports this same local calculation.
The proofs here reconstruct its local identity rather than importing a
stronger zero-free theorem for the target eta.

**DF.** Alexandre de Faveri, *Optimal large sieve for fixed order characters*,
arXiv:2610.04045v1 (October 2, 2026).
https://arxiv.org/html/2610.04045v1

Primary HTML freshly inspected: Theorem 1.1 and the distinction between
starred squarefree and flat sixth-free indices; the character-family
construction/scope; the full Section 9 detector monomials. Both indices in
(1) of SHIFTED_DETECTOR are flat. Our complete-column proof retains c*d^6
and its mask, without falsely imposing (c,d)=1. DF's sieve is a substantive
import, not certified by our finite calculations or independently reproved.
The shifted detector is NOT quoted as a literal printed DF theorem.

**BGL.** Valentin Blomer, Leo Goldmakher and Benoit Louvel, *L-functions with
n-th order twists*, arXiv:1112.1650; IMRN 2014(7), 1925--1955.
https://arxiv.org/pdf/1112.1650

Primary PDF freshly opened; printed pages 17--19 rendered and inspected.
The relevant parts are (5.1), the complete AFE support, and (5.3)--(5.5).
Their printed detector uses line 1/2. Our line 6/11 and the one-zero-per-index
maximal argument are reconstructed in SHIFTED_DETECTOR Section 3. The
classical Mellin/Gamma detector, Holder, dyadic prefix and height arguments
are credited, not claimed invented. No conditional result is used.

## Frozen repository work and overlap

- #966, `8d94494698ee447711a53dec922986586418e398`, is the base.
  Its PROOF.md blob `08195836816c1e3718c04e0b966bf89a0b5dad01` was read live
  and checked against the delivered expanded source. Its CONTOURS.md blob
  `acc546e69be4f6f1baa5f68ded051033c528108d` and verifier blob
  `adaab699c619033318eb9cdaad09674698965193` match local bytes. The original
  normal/optimized verifier reports and manifest were freshly reproduced.
  Its central fourth moment, retained R^(1/4) and 43/60 count are prior work.
  We do not call the new proofs independently reviewed because a parent
  checker passed. No claim to improve its proposed global 109/120 boundary.
- #968, `14f544fb4293ffb59942ff8d345ab9d6da67025c`, inspected at detailed
  live PR-description scope. It overlaps the central fourth moment and
  records higher fixed numerator moments. Its 10/11 global proposal is
  weaker than #966's 109/120; it is not reported as new progress here.
- #959 source map was read live at
  `7b845294207d96b883c1fa95028663082267804f`. Its source-location correction
  remains: CT principal nonvanishing is Lemma 11.1/label
  `lem:principal-nonzero`, not an invented Lemma 11.2.
- #961--#965 and the archived recovery records were inspected in the
  supplied context or live PR descriptions at their stated scopes. Their
  full independent reviews, proofs and tests are not all newly replayed.
  In particular the short-support theorem is NOT a premise of our two
  new components, so its all-field analytic adapter is not implicitly
  certified here.

Methods used: exact local Fourier/Gauss orthogonality, geometric series,
normal Euler products, fixed-field ideal counting, approximate functional
equations, Mellin separation, subharmonic mean values, binary prefix bounds,
Sobolev height control and Holder. Those are classical. Only the stated
source-specific conclusions are proposed as additions to the inspected
corpus. There was no exhaustive literature priority search, separate
commissioned agent, external referee, or proof-assistant verification.
