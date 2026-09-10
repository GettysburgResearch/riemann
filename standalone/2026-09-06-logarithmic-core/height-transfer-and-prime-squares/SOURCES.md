# Sources, reading boundary, and attribution

## Repository freeze

Repository: GettysburgResearch/riemann.
PR #803 parent: 8d8750e5be8e0f2920db371bf31ea93c2d0a0caf.
Branch: research/astra/20260906-logarithmic-core-certification.

The live PR metadata and annular packet tree were read at this head.
AGENTS.md at that head was read. The previous supplied ZIP was extracted
locally and its consumed files authenticated against the live Git tree:

| Source path below standalone/2026-09-06-logarithmic-core/ | Git blob |
|---|---|
| annular-scalar-route/PROOF.md | 0f1b21227d064e61f4f532d9025c78106baa688e |
| annular-scalar-route/verify.py | a347fb454f3f1116b521cedb8dace3c23612657a |

The parent packet tree is f8d63205477e532e699ba2799890270c3b1a105a.
Its source W normalization, filtered identity, C0 formula, gamma remainder,
RH-side scalar bound, square interpolation and one-sided Landau theorem
are the mathematical dependencies. PROOF.md rederives the new unconditional
paired-zero formula and the sharper gamma remainder; it does not assume
a cosine-only spectrum beyond the verified height.

The parent verify.py provides 160-bit outward dyadic arithmetic, elementary
logarithm and Machin-pi bounds, harmonic-constant enclosure, and the C0
formula. Its complete 603-control result and delivery validator were rerun
locally before extension in ordinary and optimized Python. This is not an
independent referee acceptance or a rebuild of the older length-one package.

The 2026-09-06 logarithmic-core and length-one packets are preserved, but
neither their operator-domain theorem nor their computer-assisted full
length-one sign is a hypothesis of the new finite-height transfer.

## External finite-height input

D. Platt and T. Trudgian, *The Riemann hypothesis is true up to 3*10^12*,
Bulletin of the London Mathematical Society 53 (2021), 792--797.
DOI: 10.1112/blms.12460.
Exact preprint version read: arXiv:2004.09765v1.
https://arxiv.org/abs/2004.09765v1
https://arxiv.org/pdf/2004.09765v1

Theorem 1 on printed page 2 gives the endpoint 3,000,175,332,800.
The mathematical statement and the adjacent description of the
interval/Turing verification were checked in parsed text and a rendered
page. Only the weaker endpoint 3,000,000,000,000 is used. The publication's
simplicity information is unnecessary. Its code, primitive interval
artifacts, and large computation were NOT replayed. No PDF bytes are
redistributed or falsely assigned a content hash in this package.
The citation and consumed statement in SOURCE_LOCK.json are not a proof
term or a claim of artifact reproduction.

The same paper's Section 3.1 already explains how finite RH verification
can yield explicit prime estimates, citing Buthe. This packet is a
specialization to the parent's smooth compact-annulus scalar, not a claim
of a new general finite-RH transfer principle or an optimal range.

## Classical analytic inputs and quantitative replacements

* Hadamard factorization for the entire completed xi and its symmetries;
  classical argument-principle zero count and Laplace uniqueness.
  See Titchmarsh, *The Theory of the Riemann Zeta-Function*, 2nd ed.,
  Chapters II and IX. These general theorems are imported, not formalized.
* NIST DLMF 25.10: critical strip, zero symmetry, theta normalization.
  https://dlmf.nist.gov/25.10
* Euler--Maclaurin for zeta and log Gamma: DLMF 25.11 and 5.11.
  https://dlmf.nist.gov/25.11
  https://dlmf.nist.gov/5.11
  The specific integral remainders and all constants used in the counting
  estimate are written out and estimated in Section 3. No sharp bound for
  S(T), subconvexity constant, or zero-density estimate is imported.
* Classical PNT, theta(y)=y+o(y), used only in Section 6's asymptotics.
  https://dlmf.nist.gov/27.12
  Partial summation from pi(y)~y/log y yields the stated theta form.
  No effective PNT error bound is asserted by this application.
* Mangoldt/logarithmic-derivative identity, DLMF 27.4.12.
  https://dlmf.nist.gov/27.4.E12

These reference entries were accessed during this continuation. Their
current historical/record claims are not relied on. No external novelty,
record prime bound, new zero-free region, or statement that the sharp
unbounded inequality has been proved is made.

## Independence

This is a research continuation after the earlier A/C reviews, not a new
independent review of our own source files. The new paper arguments and
finite checker require an exact-head non-author review. Source hashes,
finite checks, and prior review roles do not discharge that requirement.
