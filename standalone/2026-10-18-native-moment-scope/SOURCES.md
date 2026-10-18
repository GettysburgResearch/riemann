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

The primary AxiomMath/DedekindZetaZeroFree repository was located at
`09afbb4ce6570c1615d58509dc197fc9f0956b7d`:
<https://github.com/AxiomMath/DedekindZetaZeroFree>

Its published Challenge and Solution statements were read. The existence
of an analytic continuation agreeing with Mathlib's Dedekind zeta on Re>1
is a genuine source lock, not an arbitrary identically-one replacement.
See the separately recorded build receipt for the outcome of any local
compilation attempt; a source inspection alone is not a successful build.

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

Hecke continuation, the functional equation, Euler convergence, polynomial
strip bounds, Borel–Carathéodory, three-lines, ideal counting and uniqueness
of Mellin continuation are classical. The two zero-free equivalences and
growth-abscissa proofs are elementary deductions from those stated
contracts. The mask identities and nonnegative divisor expansion are
classical Euler algebra, specialized here to the exact native source and
all its repeated rows. No worldwide priority claim is made.

The claimed contribution is a precise, reviewable source adapter and
target classification for the latest packet, a separately typed imported-
input native power bound, an actual primary-source transcription check,
and a reproducible directed experiment with complete finite ideal coverage.
No new signed theta-to-native projection, critical native bound, field RH,
ordinary RH, independent referee approval or integrated acceptance follows.
