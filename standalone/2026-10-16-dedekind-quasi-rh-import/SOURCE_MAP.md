# Source map, versions, and formal-statement fidelity

Status: inspected-source account, not a fresh Lean certification or a full manuscript review. Retrieval date: 16 October 2026.

## 1. Bibliography and version boundaries

The user supplied [Hexagon 2610.00200v1](https://hexagonmath.org/2610.00200v1), with contributors Dean Cureton and Jesse Thorner. The indexed landing record identifies v1 as 12 October 2026, CC BY 4.0, and describes AxiomProver-generated proofs and Lean formalization under the investigators' direction. It reports 31/32 for Dedekind zeta functions over every number field and the corresponding finite-order Hecke corollary. Its bibliography explicitly includes the OpenAI 7/8 and 11/12 manuscripts and the primitive-roots manuscript; it is not an unrelated approach accidentally resembling that programme.

The same indexed record advertises v2 dated 14 October 2026. Direct landing-page, manuscript, and source-download requests failed. Therefore:

1. The landing metadata is not treated as the manuscript body.
2. No v1/v2 mathematical diff or PDF hash is supplied.
3. No claim of reading all fifteen manuscript sections is made.
4. The linked formal repository is pinned independently, not labeled a v2 formalization.

An older indexed [short-link record](https://t.co/scVWfWc4f4) encountered during discovery reported 1-1/6000. That cached record is not used as a theorem source. Whether this reflects stale indexing or an earlier statement cannot be resolved without the manuscript/version files. Both the accessible canonical metadata and the pinned formal theorem inspected here use **31/32**. This discrepancy is preserved rather than silently reconciled.

## 2. Author-maintained formal source

Repository: [AxiomMath/DedekindZetaZeroFree](https://github.com/AxiomMath/DedekindZetaZeroFree).

- Commit: `09afbb4ce6570c1615d58509dc197fc9f0956b7d`.
- Tree: `1bf2926b595f39b95fbdc331421a0dc8118ad973`.
- Commit date: 13 October 2026; message: `add Hecke zero-free corollary`.
- License: Apache-2.0, copied unchanged under `upstream/LICENSE`.
- Lean: `leanprover/lean4:v4.35.0-rc3`.
- Mathlib: `0493595ecd5da8ef14742febab99728f98e948e8` in the copied lakefile.
- Tau Ceti: `c197d7bdbae257e85d23443c89aa7cd34c13410b` in the copied lakefile.
- A vendored class-field-theory project is a path dependency. The upstream [formalization.yaml](https://github.com/AxiomMath/DedekindZetaZeroFree/blob/09afbb4ce6570c1615d58509dc197fc9f0956b7d/formalization.yaml) reports 1,658 retained modules from `58370e628052f54159c1eac913de908e360059d6`, with compatibility changes. That transitive library is not copied into this packet.

Upstream reports a complete build and only `propext`, `Quot.sound`, and `Classical.choice` in the final theorem footprint. This is an **upstream report**, not our independently reproduced result. Its metadata itself distinguishes agent review from a line-by-line manuscript/formal-proof correspondence.

## 3. What the formal statements actually say

[Challenge](upstream/Challenge/DedekindZetaChallenge.lean) and [Solution](upstream/Solution/DedekindZetaSolution.lean) have matching visible mathematical targets. For every number field K, they quantify a function holomorphic away from one, equal to **Mathlib's Dedekind zeta** in Re(s)>1, and nonzero when Re(s)>31/32 and s is not one. Agreement on a nonempty open set ties the continuation to the arithmetic function; this is not merely a named auxiliary function asserted nonzero.

The Hecke statement uses ray class characters as ideal-valued multiplicative data with exact zero conditions, and equality to the ideal Dirichlet series on Re(s)>1. It is entire for a nonprincipal character and includes s=1 in that case. The principal pole is not misrepresented as a zero or as a finite function value.

The Challenge intentionally contains two `sorry` placeholders. The Solution supplies the two proofs by invoking the library results. Copying the Challenge for statement comparison does **not** claim its placeholders are acceptable proof dependencies. A real audit must compile the Solution and examine its transitive proof terms, using the copied comparator configuration in the complete upstream checkout.

This theorem concerns **finite-order** Hecke characters. It is not a theorem for the infinite-order angular characters alpha^r used in some earlier Eisenstein packets. It also asserts a common zero-free exponent, not a numerical bound for every discriminant/conductor-dependent constant in every auxiliary estimate.

## 4. Inspected formal path

All paths in this table are relative to the pinned author repository. Full-file reads were used except where the coverage column says otherwise. Only the thirteen files listed in UPSTREAM_LOCK.json are physically copied; the rest remain immutable source references.

| Path | What it supplies | Coverage / Git blob |
|---|---|---|
| `DedekindZetaZeroFree/Main.lean` | Dedekind theorem entrypoint | Copied; `c6889afaa224757d712d8d97594628cbfb860c2e` |
| `DedekindZetaZeroFree/HeckeCorollary.lean` | Principal/nonprincipal Hecke split | Copied; `0e90a98fc52f305cfdcd5ed9086d8b1b12c0c148` |
| `Nonvanishing/Mellin/Quantitative/DedekindZetaNonvanishing.lean` | Lift to K(zeta_12), then abelian descent | Copied below `DedekindZetaZeroFree/`; `c82ebe140e8fdf9ddfc5cfe8944d798ebd9aa22d` |
| `Nonvanishing/Mellin/Quantitative/TwelfthRootNonvanishing.lean` | Totally complex, mu_12-containing case; principal source and continuation comparison | Read; `d94fabe45503e3883e196d38032bc7db080ec2f0` |
| `Nonvanishing/Mellin/Quantitative/PrincipalNonvanishing.lean` | Construct actual source; restore finite excluded factors | Read; `7605e5240ce5f71e2dea97969e63d4df207008c0` |
| `Theta/Unfolding/AbsolutelyConvergentExpansion.lean` | Actual source-existence entrypoint | Read; `cf3be65e9b987e1c05d3d355d299f741e7135d93` |
| `Moments/Reflected/RankOneExpansion.lean` | Source construction through residue, profile, and signed-unfolding steps | Read; `f589625e27a83e04a4d0a7ccff59680af1e38add` |
| `Moments/Reflected/GeneralSupportMoment.lean` | Fixed compact-shape row second moment at every row exponent m>1 | Read; `f57f0705f3839b9e24c9b768898eaa104ec50a57` |
| `Moments/Reflected/FixedProbeBound.lean` | Additive square energy and Cauchy assembly for the probe | Beginning through the general-bound derivation; output truncated. Not a whole-file audit. |
| `Moments/Principal/EulerCorrectionAlgebra.lean` | Literal local rational correction and its convex-combination nonzero proof | Copied; `bd11d01dcc9ae22c07b65bc5d3641d26dea781c3` |
| `Nonvanishing/Mellin/NormalizedProbeArithmeticData.lean` | Actual substitution r=1/q, D=target*q^-s, E=theta^6*q^(3-6s) | Copied; `b89b6fdcbf16c7d142c18aacc14c71fde9bc41cf` |
| `Moments/Probes/Poisson/Scales.lean` | Exact parameters | Copied; `a9ad776773d51c85bc77bf0662f8270217220968` |
| `Nonvanishing/Mellin/Quantitative/Growth.lean` | Comparison error, reflected bound, and final exponent | Copied; `50a7f57dd028ad5c98b8702bf40f5cbfa8b94890` |
| `Nonvanishing/Mellin/Quantitative/Holomorphy.lean` | Mellin convergence/holomorphy from growth and flatness | Read; `6bcdbfb0517c41c668a2ff6f2a07f8e2d8227e4a` |
| `Nonvanishing/Mellin/Quantitative/AxisIdentity.lean` | Exact identity on Re(s)=2 | Read; `b7c038d2ed3ca5cf956e9798f88ce813794f63a6` |
| `Nonvanishing/Mellin/Quantitative/ZeroExclusion.lean` | Analytic uniqueness plus a nonzero numerator | Read; `fea64c77e6518fdbded00521b723606f78b56afd` |
| `Nonvanishing/Mellin/Quantitative/SpectralRegularity.lean` | Numerator scope and recipe comparison | Read through its end; `32b7ca6150aa3741cc8c6ec77bef9a76d30b7d2f` |
| `Nonvanishing/Mellin/PrincipalProductSpectralProperties.lean` | Euler majorant and holomorphic/nonzero numerator on Re(s)>2/3 | Beginning through these theorems, not the later full file. |

Except for Main, HeckeCorollary, and the Challenge/Solution paths, the source paths above are under `DedekindZetaZeroFree/`. The map is a scoped call-graph reading, not an independent reconstruction of thousands of imports.

The upstream metadata names Kazhdan--Patterson's *Metaplectic forms* and its 1985 correction, plus Bernstein--Krotz's smooth globalization results. These are the relevant deep foundations to inspect when transporting the argument. Their proofs and the entire formal transitive closure were not replayed here.

## 5. Relationship to this repository

The new import branches from main at `f99d9e3908dde4865377c75d9ca051c1f545bf4f`, rather than merging the many research drafts. The assessment cites the following live PR descriptions and pinned results; it does not certify or integrate their proofs:

| PR | Pinned head | Interface used for comparison |
|---|---|---|
| #940 | `59d5a8ebcd390ff898d63b2fc5ed7290995ae58b` | Smooth-singleton sector and exact rooted signed remainder |
| #941 | `f106e31f12b8a10f2d57b336c983a25fb8dd6adc` | Native prime-freezing obstruction |
| #942 | `377f548cab8759399aca80ed3188c495667d562a` | Exact band-limited low-radical pruning and principal-density reference |
| #944 | `18290b5cdc646022ed0693519aa54c20e3296b5a` | Active-conductor / neutral-divisor window |
| #945 | `90d0a737789821092fec27c04c6d96099a0a1b35` | Invertible compensated Euler phases, unchanged native constant mode |
| #946 | `c90818b3a671bb3d124019f3be93a439697deab1` | Signed injection minus positive compensation |
| #947 | `0ef2eeb731f5528df04a14685b35dc887fcfee36` | Coherent physical-row separation and its logarithmic/power distinction |

The earlier 7/8 and 11/12 comparisons use their already imported settings and the new paper's explicit reference list. No fresh verification of those full manuscripts is claimed.
