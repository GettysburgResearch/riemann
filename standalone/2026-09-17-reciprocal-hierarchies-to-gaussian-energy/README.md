# Reciprocal hierarchies, prime counting, and native Möbius energies

**RHG26 — comprehensive research-conversation packet, 17 September 2026**

**Status: exploratory synthesis and proposed component proofs. Independent mathematical review required. RH is not proved here.** The native signed-covariance / sparse subpolynomial-energy upper bound remains OPEN. Neither finite experiments nor a new equivalent criterion are presented as that estimate.

This packet preserves the mathematical development initiated by Gideon J. Freund's questions about natural families with reciprocal sums growing like successive logarithms, their reverse exponential hierarchy, altered Euler products, and possible connections to the Riemann Hypothesis. It follows the discussion through fractional multiplicative families, Li and R, power-free densities, Möbius transforms, source-exact energies, crossing cutoffs, moment-cancellation packets, and the final fixed-Gaussian criterion. It also preserves failed approaches and corrections.

This is a **curated, comprehensive reconstruction**, not a verbatim transcript or a claim to have recovered unavailable earlier conversations. The supplied handoff and all subsequent mathematical turns visible in this conversation are the source. The two supplied finite-computation files are preserved byte-for-byte. Model-attribution speculation and unrelated personal context are intentionally excluded.

## Scope and provenance

- Repository: `GettysburgResearch/riemann` (the older `gfreund123/riemann` URL redirects).
- Frozen publication base: `f99d9e3908dde4865377c75d9ca051c1f545bf4f`.
- Add-only directory: this packet. No changes to main, other research packets, canonical claims, Lean, workflows, or scientific-status ledgers.
- Original questions and research direction: Gideon J. Freund; mathematical exposition and exploratory deductions: the assistant conversation. This is not external authorship or priority verification.
- Local reconstruction and finite checks are distinguished from inherited chat-reported computations in [VALIDATION](VALIDATION.md).
- Historical PR heads are not silently replaced by later revisions. Read [repository connections](10-repository-connections.md).

## What is most worth retaining?

1. **Three different operations must not be conflated.** Logarithmic-scale selection produces the digit hierarchy; recursive residue sieving produces Golomb-type families; multiplicative generation produces Euler products. Equal harmonic growth does not imply equal analytic continuation.
2. **A real algebraic bridge to prime counting.** The family \(d_\alpha*d_\beta=d_{\alpha+\beta}\), with transform \(\zeta^\alpha\), has prime powers as its tangent at zero and Möbius inversion at \(\alpha=-1\). A continuous comparison law produces a regularized logarithmic integral; primitive extraction gives Riemann's \(R\).
3. **Power-free densities encode both R and reciprocal zeta.** The numbers \(\delta_k=1/\zeta(k)\) occur in the entire exponential-coordinate series for \(R\), and their finite differences give generalized Báez-Duarte coefficients. Their required decay is still RH-strength cancellation.
4. **One literal source, several exact norms.** The rational, hyperbolic-secant, Mellin, exponential-kernel and logarithmic-Gaussian energies below all keep the actual finite Möbius prefix. Their transforms, normalizations, endpoints and restoration costs are explicit.
5. **A fixed Gaussian suffices.** For each fixed \(\omega>0\), a proposed complete proof shows that a subpolynomial bound along any unbounded sequence for
   \[
   \int_{\mathbb R}\left|\sum_{n\le N}\frac{\mu(n)}{\sqrt n}
       e^{-\omega(u-\log n)^2}\right|^2du
   \]
   implies RH. The proof pays noncausal leakage and uses an every-prefix zero witness. This is a criterion, not a bound.
6. **Failed shortcuts have exact diagnoses.** Integer-kernel entrywise comparison is not positive-operator ordering; Fourier normalization carries \(H^2\); crossings only cancel an endpoint; fixed-pattern cancellation need not control the remainder; fractional inverse factors have large main terms; generic bilinear bounds fail for coherent positive coefficients.

## Reading paths

| Purpose | Read |
|---|---|
| Understand why the project started | [01 Motivation and history](01-motivation-and-history.md) |
| Natural, fractional and reverse reciprocal families | [02 Hierarchies](02-reciprocal-hierarchies.md) |
| Euler products, prime-zeta zeros, Golomb/digit continuation | [03 Analytic objects](03-zeta-products-and-continuation.md) |
| Exact connections to Li, R and power-free integers | [04 Fractional families and R](04-fractional-families-li-and-R.md) |
| Möbius transforms, rational energies and localization | [05 Energies](05-mobius-energies.md) |
| Every-prefix growth, critical multiplicity and sparse cutoffs | [06 Zero witnesses](06-zero-witnesses-and-sparse-cutoffs.md) |
| Crossings, native-source adapters and unconditional bounds | [07 Source transfer](07-source-transfer-and-covariance.md) |
| Actual finite cancellations and their unrecovered remainders | [08 Moment packets](08-moment-cancellation-packets.md) |
| Correct Gaussian identities, mixture law and fixed criterion | [09 Gaussians and variance](09-gaussian-mixtures-and-variance.md) |
| How this relates to existing repository work | [10 Repository map](10-repository-connections.md) |
| What is proved, proposed, corrected or still open | [11 Claim/correction ledger](11-corrections-and-claim-ledger.md) |
| Concrete review and research tasks | [12 Research agenda](12-research-agenda.md) |
| Bibliography and source-reading boundary | [SOURCES](SOURCES.md) |
| Actual executions and evidence limits | [VALIDATION](VALIDATION.md) |

## The unresolved completion, in three coordinates

Let \(j_N=\lceil(\log N)^4\rceil\), and let \(B_j\) denote the off-diagonal part of \(\mathcal Q_j\) as defined in Chapter 05. The conversation's label **(27)** refers to a native upper bound
\[
B_{j_{N_r}}(N_r)\le N_r^{o(1)}
\]
along some proved unbounded sequence. The labels changed between turns; this packet uses descriptive identifiers instead of reusing ambiguous equation numbers.

Equivalent or sufficient normalized formulations are:

- \(\mathcal Q_{j_{N_r}}(N_r)\le N_r^{o(1)}\), since the diagonal is logarithmic;
- for fixed \(\omega>0\), \(\mathcal G_\omega(N_r)\le N_r^{o(1)}\);
- a source-exact decomposition whose COMPLETE residual and cross-interaction costs yield either estimate.

The proposed every-prefix witnesses imply that an off-critical zero would make all sufficiently large cutoffs expensive. They do not construct inexpensive cutoffs. This logical direction is the main boundary to preserve.

## Status language

**CLASSICAL** means a stated imported mathematical input, not a newly discovered theorem. **DERIVED/PROPOSED** means an explicit argument reconstructed in this packet, pending independent review. **FINITE-EXACT** means a bounded exact-arithmetic calculation that was actually rerun. **HEURISTIC/OPEN** means not proved. **HISTORICAL-UNREPLAYED** preserves a chat report without upgrading it to evidence. No item is labeled formally verified.
