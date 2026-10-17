# Sources, versions and dependencies

Read on 17 October 2026. A repository title or a statement in a preprint is
not an independent certification of its theorem. The newly derived operator,
memory, calibration and transfer statements do not use the proposed quasi-RH
bounds as premises. The sources below fix their mathematical context.

## 1. Repository state

Repository: [GettysburgResearch/riemann](https://github.com/GettysburgResearch/riemann).
The opening research inventory and the base of this packet identified
[#959](https://github.com/GettysburgResearch/riemann/pull/959), still draft/open.
Its exact head was `7b845294207d96b883c1fa95028663082267804f` on
`research/dedekind-numerator-mean-20261017`; root tree
`b93445b2021ecadd032ef8a48214f8bcdcf8fe05`. It proposes the all-field strict
`Re(s)>11/12` boundary, with finite-order Hecke descent. It does not claim
RH or a theorem for the infinite-order angular character.

The final scan after our initial publication also found concurrent #960 at
`c127f4f22d08585b699ccd59faa4eedd9bb001ae` and #961 at
`7bd275b44261fff93bb565a9342c44b7c66526f6`. Their compatibility read and the
additional FSW/BV primary-source checks are in CONCURRENT_UPDATES.md. They are
separate proposed branches, not silently inherited analytic premises.

| Earlier work | Frozen source | Relevance |
|---|---|---|
| #959, numerator-family mean | `7b845294207d96b883c1fa95028663082267804f` | Full proof and source map read; mean adapter, density classes and binding theta ceiling. |
| #958, recovered native packets and density strata | `e6dfa07d07ed7a5d049039d7255919a992cadc77` | Inherited branch parent and proposed `25/27` precursor. |
| #956, affine and growing-shift work | `943d7714f81b97a75652ebc6e19990a88c917d4d` | Fixed-affine transfer and exact coefficient families; this separate branch is cited rather than silently treated as inherited. |
| #955, long-twist moments | `6d3d69c7896e3a5d61d1f67e4627125257398ec7` | Native worst-center obstruction; every new asymptotic here keeps its twist separately fixed. |
| #954, norm collision energies | `3241178607671c4dd979cefdad0670fd426194da` | Distinct ideals and their full norm-fiber blocks must be retained. |
| #953, divisibility covariance | `a93d382951f8fac7b0c28783061a7ddb99fcf0a4` | Existing native signed-covariance direction. |
| #952, critical Gaussian energy | `3b7d2948840446c752bbf284f6f90f6592395a29` | Literal Gaussian, critical energy and already-open subpower target. |
| #950, critical geometric lift | `5a6418b021a35c95bbc2c80775353ee33506faee` | Existing Euler stripping, coefficient lift and critical convolution comparison. |
| #948, Dedekind import | `05b6f2172c686356ccd9900d33ffc5f526c5e98b` | Original imported CT setting and Euler stripping. |

The relevant source files are identified in the individual notes. No claim of
reading every historical branch or every file in the repository is made.

## 2. Current OpenAI source snapshot

The current main commit found was
[`1581d4cbdd69a0faf34b2089614fe2a814316a6a`](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a),
dated 12 October 2026. Its complete
[CONTENTS](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/CONTENTS.md)
listed 719 manuscripts in 372 result families. The scan found no further
later Dirichlet result beyond the relevant entries below. This inventory is
not a claim to have read those hundreds of manuscripts.

### Result 003 and its companion

* [September 30 paper](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/paper.pdf),
  PDF blob `8132b77eeb270a70b25df8d6609f008e83e65d91`.
  [TeX](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex),
  blob `268c4e3206d460c617d3d2129742a72b831b3def`.
  It asserts nonvanishing in `Re(s)>7/8` for Dirichlet L-functions and
  finite-order Hecke L-functions over `Q(sqrt(-3))`.
* [October 5 companion](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-Quasi-Riemann-Hypothesis-October-5-2026/paper2.pdf),
  blob `3ea94d87ffdee8db02c6ef1e563e6d166021ad2f`.
  It asserts the `11/12` boundary through a sextic-twist second-mean argument.

The TeX sources were fetched and the theorem/reduction architecture inspected.
Neither complete proof nor transitive Lean dependencies were rebuilt.

### Result 007: ordinary correlations

[Primary paper](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Ordinary-two-point-correlations-of-multiplicative-functions-September-24-2026/final.pdf),
blob `a1fa025a59ecbfc5176d16cfdc6e0afd418cc82e`;
[introduction](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Ordinary-two-point-correlations-of-multiplicative-functions-September-24-2026/build/introduction.tex),
blob `da38786f2b27248f49985c1e7f3d8a95fd152f81`.

The quantitative Liouville theorem uses fixed nonproportional affine forms
and explicitly disclaims growing-coefficient uniformity. The general
corrected Elliott assertion is qualitative. Introduction, quantitative setup
and spectral-transfer interfaces were read. The new Fourier theorem in this
packet instead imports the older established uniform additive-phase results.

### Exact local Poisson formula

[Primary TeX section](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Primitive-roots-for-every-admissible-integer-base-October-4-2026/build/sections/05-poisson.tex),
blob `c8526f74b281d37fda034c17195c4bb5afd5f79b`.

Equation `eq:Euler-good-exact` is the primitive local input to the new
two-variable calculation. The section was read in full. Its physical powers
of X and Z, fixed angular character, nonunit conventions, and weights
subsection are retained. The profile argument uses its local Tate identity
for `0<s<1`, citing Tate's Theorem 2.4.1.

## 3. Dedekind and higher-order mean sources

* Cureton--Thorner,
  [A quasi-Riemann hypothesis for Dedekind zeta functions, v2](https://hexagonmath.org/2610.00200v2),
  [version-specific TeX](https://hexagonmath.org/api/v1/works/2610.00200v2/source?path=DedekindZeta.tex).
  The version history records v2 on October 14; the overview also displays
  the original October 12 date. The asserted boundary is `31/32` for all
  fields, with finite-order Hecke corollary. The source index displayed hash
  prefix `f54808ad0f967b54`; no full source-archive hash is asserted.
* Blomer--Goldmakher--Louvel,
  [L-functions with n-th-order twists](https://arxiv.org/pdf/1112.1650),
  Section 5 and its complete-column second mean.
* De Faveri,
  [Optimal large sieve for fixed order characters, v1](https://arxiv.org/html/2610.04045v1),
  Theorem 1.1 and the full-family zero detector in the proof of Corollary 1.5.

The actual CT PDF and TeX were accessible after following the version-specific
source links. Its generators, character, reflected estimate, profile range,
principal correction and noncancellation interfaces were inspected. A minor
lemma-number discrepancy in #959 is recorded in AUDIT_SCOPE.md; no fatal
analytic error was found in the interfaces checked. This is not a complete
independent audit of #959 or its automorphic foundations.

## 4. Established analytic inputs and prior art

* Green--Tao,
  [Quadratic uniformity of the Möbius function, v2](https://arxiv.org/pdf/math/0606087v2).
  Uniform Davenport cancellation appears in Example 3, (1.3), with a proof
  in Section 5; quadratic cancellation is (1.7), proved in Section 7.
  These are the imported quantitative inputs for the Fourier appendix.
* Hu--Kaneko--Martin--Schildkraut,
  [Order of Zeros of Dedekind Zeta Functions](https://arxiv.org/html/2107.03269v2),
  Proc. Amer. Math. Soc. 150 (2022), 5111--5120, Theorems 1.1--1.2.
  The unconditional multiple-zero theorem supplies the actual all-field
  obstruction to overly strong native energy targets.
* The same authors,
  [On a Mertens-type conjecture for number fields](https://www.cambridge.org/core/journals/mathematical-proceedings-of-the-cambridge-philosophical-society/article/on-a-mertenstype-conjecture-for-number-fields/B01C7628DF4D57CAE8410901FD6A9321).
  Its weak-Mertens, multiplicity and nonabelian discussion is directly
  relevant prior art. The present notes do not claim the basic obstruction,
  explicit formula, or log-derivative RH criterion as globally new.

Classical Hecke continuation and functional equations, Hadamard products,
Hardy-space projection, unique ideal factorization, and Gaussian inversion
are explicitly used as standard inputs. The source-specific normalization,
local factorizations, finite Gram argument, memory tail calculation, and
convolution estimates are proved in the companion notes. Global literature
priority is not asserted.
