# Exact sources and import boundaries

All new results are proposed components. A source citation is not a claim
that the complete upstream theory was independently rebuilt.

## Repository snapshots

| Source | Frozen commit | Role in this packet |
|---|---|---|
| Integrated main snapshot | `f99d9e3908dde4865377c75d9ca051c1f545bf4f` | Reviewed starting state; not updated by this packet |
| [#965](https://github.com/GettysburgResearch/riemann/pull/965) | `d58e3282a9379b6ae165681bc2e21e4f9fd18c26` | Parent; all-scale reflected T+T^2/Z reconstruction and actual theta/Poisson interfaces |
| [#959](https://github.com/GettysburgResearch/riemann/pull/959) | `7b845294207d96b883c1fa95028663082267804f` | Inherited family adapter, central numerator mean, reciprocal disks and contour organization |
| [#961](https://github.com/GettysburgResearch/riemann/pull/961) | `7bd275b44261fff93bb565a9342c44b7c66526f6` | Inherited audit and prior scope warnings; its open native moment is not an assumption |
| [#962](https://github.com/GettysburgResearch/riemann/pull/962) | `b2032c663736ecd1e3872559d160ce069664ea06` | Free Mellin/principal-row source and critical-scattering context |
| [#966](https://github.com/GettysburgResearch/riemann/pull/966) | `8d94494698ee447711a53dec922986586418e398` | Theorem A, fourth numerator mean only; its new zero detector is not imported |
| [#905](https://github.com/GettysburgResearch/riemann/pull/905) | `0f82df3bf1d0bc669a1bbca09f8404b77c6fecde` | NRC32 finite native reciprocal energy and quadratic block coordinates |
| [#886](https://github.com/GettysburgResearch/riemann/pull/886) | `d998605c0718e332ac503baf078704b862f8250e` | Original D16 theta moment source and unmodified directed primitives |

Load-bearing source files are named in each proof. In particular:

- #965: `standalone/2026-10-17-subcritical-dedekind/PROOF.md`, Sections 2--4.
- #962: `standalone/2026-10-17-critical-scattering-reset/PRINCIPAL_TWO_VARIABLE_FACTOR.md`.
- #966: `standalone/2026-10-17-selected-fourth-density/PROOF.md`, Theorem A;
  Git blob `08195836816c1e3718c04e0b966bf89a0b5dad01`.
- #905: `standalone/2026-09-21-native-covariance-compression/PROOF.md`.
- #886: `standalone/2026-09-13-astra-theta-degree-sixteen/PROOF.md`,
  `primitive.py`, and `parameters.json`; exact copied-file hashes are in
  `lee_yang/SOURCES.json` and enforced by its checkers.

Concurrent [#963](https://github.com/GettysburgResearch/riemann/pull/963)
at `c91fd9ddfb37668338d9aec22c0e29cfe741cf07` and
[#964](https://github.com/GettysburgResearch/riemann/pull/964)
at `09ab9bc067bc66278fad8fcd883e8c8569b0cbc9` were read for overlap and
scope. Their archimedean ideal-resolution and native field-coefficient
uniformity claims are not assumptions of any result here.

The final publication refresh also identified two later concurrent PRs:
[#967](https://github.com/GettysburgResearch/riemann/pull/967), at
`b7215948884cedb1b5062dd541bc79ec765e8e4c`, preserves an unpublished
subcritical packet; and [#968](https://github.com/GettysburgResearch/riemann/pull/968),
at `14f544fb4293ffb59942ff8d345ab9d6da67025c`, also presents the
same 7/6 fourth numerator mean and a proposed 10/11 comparison. These
overlaps are credited, but neither is a new import into this packet.
The 49/54 proof was frozen with #966 Theorem A as its fourth-mean source;
it does not use #968's general fixed-order numerator formula. No global
priority claim is made. Main remained at the snapshot above on refresh.

The parent root tree is `b7a1737341c0f978b0d8386164417e3de762fe4e`.
The new contribution adds only this standalone directory. A later PR head
or an integrated summary does not silently change these frozen imports.

## Primary analytic inputs

### CT version 2

Dean Cureton and Jesse Thorner, *A quasi-Riemann hypothesis for Dedekind
zeta functions*, Hexagon 2610.00200v2, revised 14 October 2026.
[Primary PDF](https://hexagonmath.org/pdf/2610.00200v2).

Used through the exact interfaces of #965: original average and additive
second norm; Proposition 8.3's complete reflection and fixed profiles;
(8.15)--(8.16); the quadratic sieve (9.2) and localized Fourier bound (9.3);
Sections 10--11's literal Poisson identity, smoothing and principal
correction. The subcritical T+T^2/Z moment is reconstructed by #965 before
its long-support simplification. Neither CT's old zero-free conclusion nor
#965's proposed 91/100 conclusion is fed back into the new proof.

The primary PDF interfaces were read during this work. Failed source-index
or TeX retrieval attempts are not represented as a successful source
download. No full local CT source hash or formal metaplectic rebuild is
claimed.

### Exact local Poisson factors

OpenAI/math, commit `1581d4cbdd69a0faf34b2089614fe2a814316a6a`,
[05-poisson.tex](https://github.com/OpenAI/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Primitive-roots-for-every-admissible-integer-base-October-4-2026/build/sections/05-poisson.tex),
Git blob `c8526f74b281d37fda034c17195c4bb5afd5f79b`.

The exact file was fetched independently by the component author,
cross-reviewer and coordinating reviewer. The local-domain and diagonal
proofs use `eq:exact-Euler-factor`, `eq:C-local-values`,
`eq:Euler-good-exact`, and the immediately following definition of H.
The source target character is specialized to the principal character;
the distinct angular phase remains. CT v2 uses this finite local
calculation for its data. The new proofs do not authenticate the entire
global theta construction merely by checking these local formulas.

### BGL central mean

Valentin Blomer, Leo Goldmakher and Benoit Louvel, *L-functions with n-th
order twists*, [arXiv:1112.1650](https://arxiv.org/pdf/1112.1650),
Section 5, especially equation (5.1) and its complete AFE argument.

The complete actual-family mean, full norms, finite S-unit twists and
original nonunit zeros are imported through the explicit #959/#965
adapter. The new interpolation theorem is a finite-vector implication
from that mean, not a new reciprocal mean or a verification of the adapter.

### De Faveri sieve and original density

Alexandre de Faveri, *Optimal large sieve for fixed order characters*,
[arXiv:2610.04045v1](https://arxiv.org/html/2610.04045v1).

Theorem 1.1 at n=6, the full sixth-power-free/full-norm families and
conductor/zero-extension conventions in Sections 2.3--2.5, and the original
Corollary 1.5 detector are used. Every finite density substitution in the
new comparisons is rederived rationally. The fourth-mean deduction uses
the complete sieve columns after b=c d^6, with its exact ramification mask.
The new selected-character detector of #966 is outside this packet's
import and review scope.

### Mobius short intervals

Kaisa Matomaki, Maksym Radziwill, Xuancheng Shao, Terence Tao and Joni
Teravainen, *Higher uniformity of arithmetic functions in short intervals
II. Almost all intervals*,
[arXiv:2411.05770v2](https://arxiv.org/html/2411.05770v2), Theorem 3.1(i).

Only the ordinary Mobius function at T=0 is used, in intervals
H>=X^(1/3+epsilon). Its maximal arithmetic-progression estimate and
exceptional-set measure give the complete second moment over all integer
starts. The new Newton proof pays early annuli deterministically and
does not assume a Dedekind coefficient analogue, an effective numerical
threshold, or a pointwise bound at chosen block endpoints.

### Finite weighted Lee--Yang theorem

Charles M. Newman and Wei Wu, *Constants of de Bruijn--Newman type in
analytic number theory and statistical physics*,
[arXiv:1901.06596v2](https://arxiv.org/html/1901.06596v2#S2.SS5), Section 2.5,
equation (21) and following display.

The finite zero-field ferromagnetic theorem permits nonnegative real
observable weights. The new proof also gives a direct positive-hub-weight
limit using Hurwitz. It applies only to the constructed finite-spin
characteristic function. The standard theta Fourier normalization comes
from the exact #886 source and is restated in the new proof.

## Review and computation boundaries

The full new deductions are written in the component proofs. Imported
analytic theorems remain imported. Exact scalar identities, finite
partitions and directed root certificates cannot compensate for an
incorrect source-family identification or an omitted physical term.

The packet includes no new accepted integrated claim, formal proof build,
full-repository axiom audit, or remote CI assertion. It supplies a concrete
source-bound object for mathematical review and further research.
