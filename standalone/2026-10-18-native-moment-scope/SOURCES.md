# Sources and dependency boundaries

## Pinned repository source

PR #976, head `bf845aa1d9d06b0ce62440edc5726de997a888db`:

* `standalone/2026-10-18-full-moment-audit/CRITICAL_TARGET.md`, read in full:
  actual native Gaussian, same-height S6 moment, all sixth-power copies,
  cofinal-order target and the theta/native distinction.
* `THETA_ALL_MOMENTS.md` and `NUMERATOR_HIERARCHY.md`, read in full:
  their source contracts and positive-moment scope are preserved.
* `SOURCES.md`, `README.md`, checker and manifest: inspected and the
  original 12,040-predicate checker and sealed payloads replayed.

The source bytes in that packet are unchanged. On this Windows host the
initial default Git CRLF checkout broke its raw-byte manifest. Reading the
canonical Git blob bytes restored the exact sealed payloads; no historical
manifest or hash was rewritten to accept changed line endings. The new
directory's own `.gitattributes` enforces LF for all its text payloads.

The earlier reciprocal proof in
`research/integrated/2026-09-06/proof-extracts/D2.md`, R15 §1, was read in
full. Its Borel–Carathéodory and Gaussian three-lines argument is the
credited starting point for ANALYTIC_ADAPTER.md. We add the uniform
conductor dependence and every imprimitive Euler deletion needed here.

## Fresh primary analytic reads

Alexandre de Faveri, *Optimal large sieve for fixed order characters*,
arXiv:2610.04045v1:

<https://arxiv.org/html/2610.04045v1>

Freshly read Theorem 1.1, the two index conventions and §2.5.1–2.5.3.
The order-dividing-six family, complete zero extension, inducing conductor
shape and fixed field/S/infinity type are retained. This packet does not
reconstruct the large-sieve proof. The S6 high-order envelope compared in
PROOF.md §8 is the separately pinned #976 deduction, not a newly printed
theorem attributed to de Faveri.

Dean Cureton and Jesse Thorner, *A quasi-Riemann hypothesis for Dedekind
zeta functions*, Hexagon 2610.00200v2:

<https://hexagonmath.org/2610.00200v2>

Exact primary TeX endpoint:
<https://hexagonmath.org/api/v1/works/2610.00200v2/source?path=DedekindZeta.tex>

An ordinary direct HTTP GET obtained the actual 142,663-byte TeX source;
SHA-256 is `f54808ad0f967b5429c7ac30d7b27ff25671e02d7fb43cf753b2b826c9d35df4`.
The main theorem and Hecke corollary, family definition, relevant global
normalization/construction discussion, reflection, separated local beta
formulas, quadratic-family check and localized Fourier proof were read.
CT_INTERFACE_REVIEW.md gives the exact limited verdict. PROOF.md §§1–7
do not use CT's zero-free conclusion. Its §8 explicitly imports the printed
31/32 finite-order Hecke theorem and proves the displayed native consequence.
Neither CT's complete deep proof nor the cited upstream local theory was
independently reconstructed for that deduction.

The modern Cai–Fan–She reference was also freshly read at
<https://arxiv.org/html/2507.15279v2>, §2 and Proposition 2.2. The checked
scope and the distinct tame-recursion restriction are recorded in the
source-interface review.

Kazhdan--Patterson's published correction was freshly rendered from the
primary Numdam PDF:
<https://www.numdam.org/item/PMIHES_1985__62__203_0.pdf>.
Its full one-page body and the CT citation were compared at the limited
scope and exact PDF hash recorded in CT_INTERFACE_REVIEW.md.

The directly cited primitive-root manuscript was then obtained at a
fixed OpenAI mathematics commit:
<https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Primitive-roots-for-every-admissible-integer-base-October-4-2026/primitive-roots-all-integer-bases.pdf>.
Appendix A.1--A.2 was rendered and read for its global normalization and
explicit treatment of the correction. The exact PDF hash and limited
finding are in CT_INTERFACE_REVIEW.md; the whole upstream proof was not
rebuilt from this partial read.

The primary AxiomMath/DedekindZetaZeroFree repository was located at
`09afbb4ce6570c1615d58509dc197fc9f0956b7d`:
<https://github.com/AxiomMath/DedekindZetaZeroFree>

Its published Challenge and Solution statements were read. The existence
of an analytic continuation agreeing with Mathlib's Dedekind zeta on Re>1
is a genuine source lock, not an arbitrary identically-one replacement.
See the separately recorded build receipt for the outcome of any local
compilation attempt; a source inspection alone is not a successful build.
Its formalization metadata explicitly targets version 1 (12 October 2026),
Theorem 1.1 and Corollary 1.2. The fresh reflection/interface read above
concerns the separately pinned version-2 TeX. These are distinct source
objects; a formal check of the exported 31/32 statements is not a claim
that every version-2 lemma or this new packet has been formalized.

## Related reciprocal-moment proposal: scope comparison only

PR #984, *Research: actual reciprocal-moment asymptotics via a signed
mollified approximation*, was read at the fixed commit
`b6a29037a2be358294401d71d7305b0f402c2eea`:
<https://github.com/GettysburgResearch/riemann/blob/b6a29037a2be358294401d71d7305b0f402c2eea/standalone/2026-10-18-reciprocal-moment-law/RECIPROCAL_MOMENTS.md>.
The complete raw Markdown source was obtained and read; its SHA-256 is
`b693fa123ce6b5e509d84db3785f9a95638f35d0026be87923b04458665aa238`.
Its fixed-s good-family inverse-L law, common exceptional set, complete-
family capped law, and final stated limitations were compared with the
native target. No correctness verdict on its analytic proof is given and
none of its analytic results is an input here. PROOF.md §§9–9b supply a
separate elementary count of the lifted exceptional rows and a sufficient
vertical reciprocal-moment adapter from the literal Mellin integral and
Jensen's inequality, with the contour hypothesis still supplied. They
preserve the distinct core and unrestricted-mask probability spaces.
The sparse-full-row criterion reuses the native prime-replica bootstrap,
with the number of surviving primes explicitly retained.

## Numerical arithmetic contract

FLINT/Arb, accessed via python-flint 0.9.0, FLINT 3.6.0:

* <https://python-flint.readthedocs.io/en/stable/arb.html>
* <https://python-flint.readthedocs.io/en/latest/general.html>
* <https://flintlib.org/doc/using.html>

The directed-ball contract, exact rational inputs, erfc/log/exp operations,
and decimal roundtrip behavior were checked in the primary documentation
and the installed method documentation. No ordinary float is used as a
certified transcendental input. Software implementation correctness remains
an assumption; this is not a second implementation of Arb.

## Classical inputs and novelty

For the prime-replica bootstrap and sharp mask-order refinement, the classical NATURAL prime ideal
count pi_F(x)~x/log x was checked in Lagarias--Odlyzko, *Effective versions
of the Chebotarev density theorem* (1977), §1, equation (1.1) and the
following trivial-extension paragraph. The accessible copy is a modern
retypesetting of that primary paper:
<https://aareyanmanzoor.github.io/assets/articles/lagarias-odlyzko.pdf>.
The downloaded 594,676-byte PDF has SHA-256
`9e04f95d089e1c132408b7c3fc7e91520d620b2502fb193d39c25e8575d470d6`.
Its unconditional Theorem 1.3 was also read; the conditional Theorem 1.1 is
not used. For a fixed field any possible fixed exceptional zero is strictly
below one, so its term is lower order. No explicit uniform field error from
that theorem is needed. MASK_ASYMPTOTICS.md supplies all subsequent local,
small-prime, and infinite-tail estimates, rather than attributing its new
Euler-product asymptotic to the reference. Classical ideal counting gives
the exact fixed-order mean by dominated convergence.

Hecke continuation, the functional equation, Euler convergence, polynomial
strip bounds, Borel–Carathéodory, three-lines, ideal counting and uniqueness
of Mellin continuation are classical. The two zero-free equivalences and
growth-abscissa proofs are elementary deductions from those stated
contracts. The mask identities and nonnegative divisor expansion are
classical Euler algebra, specialized here to the exact native source and
all its repeated rows. No worldwide priority claim is made.

The claimed contribution is a precise, reviewable source adapter,
fixed-order principal criterion, sharp mask-order/tail deductions and
target classification for the latest packet, a separately typed imported-
input native power bound, an actual primary-source transcription check,
and a reproducible directed experiment with complete finite ideal coverage.
No new signed theta-to-native projection, critical native bound, field RH,
ordinary RH, independent referee approval or integrated acceptance follows.
