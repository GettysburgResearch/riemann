# From iterating zeta to one-sided arithmetic: complete conversation packet

**Status:** curated conversation reconstruction; imported classical mathematics,
proposed component proofs, explicit failed routes, finite evidence, and open
RH-bearing estimates. **No proof or disproof of RH, no new zero-free region,
no claim of mathematical priority or independent acceptance.**

**Scope:** the whole visible conversation, beginning with Gideon Freund's
question about composing zeta with itself, through inverse dynamics, a
one-sided logarithmic integral, fractional-part approximation, explicit
mollifiers, reflection/GCD ideas, and the support-rigidity packet first
published in PR #901. This is not merely a re-publication of the last result.

**Frozen predecessor:** PR #901, commit
`001fe76229324946a915d4db84282324f7ff9673`, based on main
`f99d9e3908dde4865377c75d9ca051c1f545bf4f`.
Its seven files under
[`../2026-09-18-vasyunin-support-leakage/`](../2026-09-18-vasyunin-support-leakage/README.md)
are preserved unchanged. This companion adds the missing history and mathematics.

**What was actually run:** see [validation](VALIDATION.md). Earlier execution
claims remain historical unless explicitly replayed here. The retained source
collection contains all supplied scripts, notes and result records; storing a
certificate is not the same as re-running or independently validating it.

**Smallest remaining gap:** a source-specific arithmetic upper bound, such as
subpolynomial growth of the prescribed mollifier norm or the weighted
best-linear-fit variance of psi. Matrix positivity, the exact finite identities,
and the numerical bound on the logarithmic integral do not supply it.

## Read the mathematical story

| Reading order | Contents |
|---|---|
| [Original questions](ORIGINAL_QUESTIONS.md) | All eight user turns, including the proposed relaxations, both pairs of attacks, and the request for this comprehensive publication. Connector markup is normalized; wording is preserved. |
| [Chronology and coverage](CHRONOLOGY.md) | Each user turn paired with the response, its significance, source artifacts, and later disposition. |
| [Notation](NOTATION.md) | Separates zeta iteration, logarithmic derivatives, projection limits, scalar divisor sums, and Gram corrections that reused letters in chat. |
| [01: Iteration and inverse trees](01_ITERATION.md) | Pole/exponential feedback, real fixed points, preimages, singularities, spirals, and the precise limits of the tetration heuristic. |
| [02: Dynamics to Li and BSY](02_DYNAMICS_TO_BSY.md) | Adapted inverse-value flows, multiplicity, monodromy, fixed-point multipliers, Li coefficients, and one-sided logarithmic contraction. |
| [03: The arithmetic upper bound](03_ARITHMETIC_BOUND.md) | Pole-canceling multipliers, Mellin/Poisson-Jensen proof, exact Gram sums, finite certificates, and the original scale-gain target. |
| [04: Residuals and tail control](04_RESIDUALS_AND_TAILS.md) | Weakened dyadic criterion, exact zero kernels, coefficient and conditioning bounds, large-sieve cutoff, and the no-geometric-decay restriction. |
| [05: Explicit mollifier](05_MOLLIFIER.md) | Spectral-synthesis question, logarithmic Mobius coefficients, exact divisor sums, N-squared cutoff, and the length-averaging growth lemma. |
| [06: Reflection and GCD geometry](06_REFLECTION_AND_GCD.md) | Dilation rigidity, unbounded reflected kernels, Ramanujan atoms, prime-power source, two-norm counterexample, and the correct Schur complement. |
| [07: Latest support results](07_SUPPORT_AND_CURRENT_FRONTIER.md) | Vasyunin coefficient duals, indispensable squarefree denominators, head/ramp/tail decomposition, trace bound, and the psi-variance target. |
| [Claim ledger](CLAIM_LEDGER.md) | Imported/proposed/finite/open/refuted distinctions, with proof and source locations. |
| [Corrections](CORRECTIONS.md) | Preserved correction history and tempting inferences that must not be revived. |
| [Next work and review](NEXT_STEPS.md) | Concrete proof obligations and review order, without presenting equivalent reformulations as progress on the missing upper estimate. |

The original compact notebooks and numerical evidence are retained byte-for-byte
as files under [retained sources](artifacts/retained).
[ARTIFACTS.md](ARTIFACTS.md) describes every stage, extraction, original ZIP
hashes, duplicate checks, and execution boundaries. No external paper text or
font is bundled. [SOURCES.md](SOURCES.md) supplies primary-source attribution.

## One-page result map

Literal backward zeta iteration motivated the investigation; it is not the same
map as the later xi-based flow. The chain then became

    zero displacement -> a local multiplier -> BSY logarithmic mass D
       <= -1/2 log(1-E_N)
       <- weighted fractional-part approximation.

Two further reorganizations survive:

    prescribed logarithmic Mobius error Q_N = N^{o(1)} -> RH;
    actual error = dual coefficient mismatch + linear mode + arithmetic tail.

The antecedent Q_N=N^{o(1)} is **not proved**. Likewise E_N->0 and the
source-specific Schur gain are unproved. The complete source-aware correction
has uniformly bounded trace, but its action on the growing signed source is
not shown to vanish. No step in this packet changes those boundaries.

This is a curated, mathematically qualified reconstruction, not a verbatim
export of every assistant response or a replacement of the source notebooks.
Original user proposals are attributed to the user. Public research content
only is included; private reasoning and unrelated project conversations are not.
