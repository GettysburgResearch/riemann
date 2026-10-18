# Source snapshot and dependency boundaries

This is a standalone continuation of [PR #974](https://github.com/GettysburgResearch/riemann/pull/974),
not an update to the integrated mathematics. The parent is exactly
`89c37b6707cb77fc5a86143ea98d8756759fdcbc`, whose root tree is
`9070d4cf2c7485687773040c34a58507ef54b9a4`. The proposed branch is
`research/native-amplitude-and-theta18-20261018`, based on
`research/three-route-continuation-20261017`. The final publication commit
and PR are recorded in the GitHub publication record, avoiding a
self-referential commit identifier inside its own payload.

The repository snapshot and concurrent-work cutoff is **2026-10-17 23:56 UTC**.
The main ref observed at that cutoff is
`f99d9e3908dde4865377c75d9ca051c1f545bf4f`. Main and the earlier standalone
packet are not modified by this contribution. This pass continues the
earlier repository survey; it does not claim a new exhaustive line-by-line
audit or execution of every historical PR.

## Inputs to the new results

| Result | Source used | Dependency and review boundary |
| --- | --- | --- |
| Newton amplitude theorem | [#905 at `0f82df3`](https://github.com/GettysburgResearch/riemann/tree/0f82df3bf1d0bc669a1bbca09f8404b77c6fecde/standalone/2026-09-21-native-covariance-compression) | Literal truncated Möbius convolution and the strict finite inverse identity. The new proof rederives that identity, the harmonic remainder, all Fourier estimates and the full output-range summation. |
| Newton projection consequence | [#974 at `89c37b6`](https://github.com/GettysburgResearch/riemann/tree/89c37b6707cb77fc5a86143ea98d8756759fdcbc/standalone/2026-10-17-three-route-continuation) | The earlier complete block partition supplies a useful projection. The new amplitude estimate requires no short-interval analytic import from #974. |
| Theta source primitive | [#886 at `d998605`](https://github.com/GettysburgResearch/riemann/blob/d998605c0718e332ac503baf078704b862f8250e/standalone/2026-09-13-astra-theta-degree-sixteen/primitive.py) | Inherited directed transcendental implementation; freshly authenticated against the upstream Git blob. The local copy has exactly one additional trailing newline, as detailed below. |
| Theta integration and exact cumulants | [#974 Lee–Yang packet](https://github.com/GettysburgResearch/riemann/tree/89c37b6707cb77fc5a86143ea98d8756759fdcbc/standalone/2026-10-17-three-route-continuation/lee_yang) | The six-index, 98-cell source implementation is extended through moment 20. The new proof supplies all Taylor, time and omitted-index remainder bounds for those orders. The new model is a connected chain and leaf tree. |
| Finite real-zero theorem | [Newman–Wu, arXiv:1901.06596v2, Section 2.5](https://arxiv.org/html/1901.06596v2#S2.SS5) | Finite zero-field ferromagnetic Ising with nonnegative real observable weights. The zero-weight hub also has an explicit positive-weight approximation and Hurwitz argument. This theorem is imported. |
| Full-strip character moments | [de Faveri, arXiv:2610.04045v1](https://arxiv.org/html/2610.04045v1) and [Blomer–Goldmakher–Louvel, arXiv:1112.1650](https://arxiv.org/pdf/1112.1650) | The complete sixth-power-free row and column large sieve and the classical Hecke functional equation/AFE are analytic imports. The all-order deduction retains actual conductors, both AFE pieces, finite twists, nonunit zeros and complete tails. |
| Retained Type-II detector | [#971 at `3f1d2a0`](https://github.com/GettysburgResearch/riemann/tree/3f1d2a07631eb6cca1f2716be01f64e874667639/standalone/2026-10-18-ramified-shifted-detector) | The shifted detector and ramified-factor contracts were read; the literal Type-II coefficients and all retained endpoints are displayed in the new proof. The full detector also agrees with de Faveri Section 9. |
| Physical application of the budget theorem | [#965 at `d58e328`](https://github.com/GettysburgResearch/riemann/tree/d58e3282a9379b6ae165681bc2e21e4f9fd18c26), #971 and #974 | The exact Mellin monomial and the two-term physical norm are declared contracts of the architecture. The reflected estimate is the #965 deduction, not the older numerical `probe-low` bound. This pass does not reconstruct the full CT foundation. |

The pinned CT source inspected for its Mellin monomial is
`OpenAI/math` at `1581d4cbdd69a0faf34b2089614fe2a814316a6a`,
`preprints/Primitive-roots-for-every-admissible-integer-base-October-4-2026/build/sections/05-poisson.tex`,
Git blob `c8526f74b281d37fda034c17195c4bb5afd5f79b`.
The arithmetic all-order theorem does not use CT. Its physical method
floor explicitly depends on the stated physical interface.

Detailed source reads, conductor qualifications and neighboring PRs are
recorded in [critical/SOURCES_AND_VALIDATION.md](critical/SOURCES_AND_VALIDATION.md),
[newton/SOURCES.md](newton/SOURCES.md) and
[lee_yang/SOURCES.json](lee_yang/SOURCES.json).

## Concurrent work inspected at the cutoff

The following table records exact heads, not moving branch labels. No
concurrent global zero-free conclusion is adopted as a premise.

| PR | Exact inspected head | Mathematical read and effect on this packet |
| --- | --- | --- |
| [#975](https://github.com/GettysburgResearch/riemann/pull/975) | `edbc27b61208ccc7ee1fa99fa3f4e861f5a03452` | The transverse normalization proof was read for overlap. It is not a signed physical estimate and is not an input here. |
| [#976](https://github.com/GettysburgResearch/riemann/pull/976) | `bf845aa1d9d06b0ce62440edc5726de997a888db` | The full numerator hierarchy was read and overlaps the full-strip moment envelope and finite anchors here. The new theta all-moment statement and source interface were inspected; no full independent audit or replay is claimed. The optimistic critical-target model was read and grants stronger hypothetical inputs. |
| [#977](https://github.com/GettysburgResearch/riemann/pull/977) | `f3727b60dcb769b9f2b06c0466a8199b872dc6c0` | The full reflection lemma was read. It uses numerator and reciprocal bounds from the same zero-free selection, outside the separate global-moment numerator architecture constrained here. |
| [#978](https://github.com/GettysburgResearch/riemann/pull/978) | `a33d4a9167943d289a4a3ac332a42331d2753e05` | The full ratio lemma and proposed 37-class `19/21` composition were read for scope and overlap, including both height truncations. That composition was not freshly certified or replayed and is not an input. |

In #976 the hierarchy file has Git blob
`eb1084b257712bd8792dad81ce971678ae132d94`.
The #977 reflection lemma has blob `feadcbc4298b0c4911b9139481bb51c71ac75094`.
The #978 ratio and composition files have blobs
`24951948e662e23012d616a4ba1a1ac8ab10177a` and
`6c3e2557c269fb8e69dc6e2988997c6520a98011`.
The earlier authenticated recovery of #976 and its precise extraction/read
scope remain documented in the critical component's source note.

There is no exclusive novelty claim for the concurrent numerator hierarchy.
The `100/111` theorem concerns the declared retained-Type-II/separate-moment
budget and does not rule out the coupled estimates in #977–#978.

## Exact inherited primitive qualification

The coordinator independently compared a fresh upstream fetch with the
local primitive. Upstream has 6,533 bytes, SHA-256
`c1b49fa5837546ab7521426b1dc7c1a1ab970c76863797880e3b3987118fb923`,
and Git blob `712bb0f0114cbba85e8082c3130ebf09b53e8936`.
The local copy has 6,534 bytes and SHA-256
`2eba75b7fc82617342c20f6a06270462b6d82f1e7162f66847c029e7e5a9fa55`.
Removing exactly its final newline reproduces the upstream bytes.
The implementation is unchanged; the two files are not byte-identical.
This corrects the provenance wording for the new packet without rewriting
the frozen historical #974 files.

## Status

All three results are proposed standalone mathematical components.
The written proofs, exact computations and separately authored reviews
have distinct scopes. Neither publication nor local replay makes them
accepted integrated theorems, proves every imported analytic contract,
or supplies a proof of RH.
