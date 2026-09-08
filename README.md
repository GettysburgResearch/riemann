# Riemann Hypothesis — Agentic Polymath Project

We are developing and testing approaches to the **Riemann Hypothesis (RH)**: every nontrivial zero of the Riemann zeta function has real part $1/2$.

$$
\zeta(s)=\sum_{n=1}^{\infty}\frac{1}{n^s}, \qquad \Re(s)>1.
$$

Its analytic continuation connects the distribution of primes with complex analysis, harmonic analysis and spectral theory. This repository is part of the [Agentic Polymath Project](https://github.com/gfreund123/agentic-polymath-project).

**RH remains unproved here. There is no accepted proof or disproof, and no certified off-critical zeta zero.** The project has produced useful theorems, exact reductions, finite certificates and counterexamples to proposed mechanisms. These are a research foundation, not a completed solution.

## Contribute

**Working from your phone?** See the [phone tutorial](docs/PHONE.md).

Our ambition is to resolve this together. Existing programmes are starting points, not a fixed agenda: new directions and unfinished exploratory PRs are welcome. Leave useful findings and failed attempts in the repository so others can build on them.

| Stage | How it works |
|---|---|
| Explore | Open a branch or exploratory PR for proofs, computations, mechanisms, counterexamples or new directions. No preliminary permission needed. |
| Review | Review one another's work at an exact commit, checking specific claims, dependencies and evidence. |
| Integrate | Trusted integrators bring useful work into main with its status, proof, dependencies and remaining gaps attached; another core member reviews the integration PR. |
| Consolidate | Periodically update the cumulative results and open problems, preserving useful failed attempts and superseded arguments. |

Merging preserves and shares work; mathematical acceptance requires substantive review. Exploratory work can be merged while remaining clearly labeled **PROPOSED**, **EMPIRICAL** or **OPEN**.

This way of working is itself experimental: we'll learn together and adapt it as the project grows. Suggestions and improvements are welcome.

Read [CONTRIBUTING](CONTRIBUTING.md), explore your own question or choose a [suggested task](OPEN_CUTS.md#bounded-contributions), and check the existing issue or PR before starting. Exploration, independent review and useful counterexamples are welcome. Agents should also read [AGENTS](AGENTS.md).

[Integration and audit records](integration/README.md), [history](HISTORY.md), the [machine-readable current record](canonical/CURRENT.json), and [publication readiness](RELEASE_READINESS.md) supply provenance and operational detail; they are not prerequisites for understanding the mathematics.

## Read the project

| Question | Start here |
|---|---|
| What is established, and with what qualifications? | [Scientific status](STATUS.md) and [results with significance and scope](RESULTS.md) |
| What do the current statements actually say? | [Current statements and proof routes](research/integrated/CURRENT_RESULTS.md) |
| How do the approaches connect? | [Approaches](PROGRAMMES.md) and [implication map](PROOF_GRAPH.md) |
| What should be tried next, and what has already failed? | [Open problems and concrete tasks](OPEN_CUTS.md) and [useful failed approaches](REFUTATIONS.md) |
| Where are the proofs, evidence and ongoing experiments? | [Research navigation](research/RESULTS_INDEX.md) and [computational evidence](COMPUTATIONS.md) |

Ask your agent to review work since the last integration, run exploratory computations to discover mechanisms, develop proofs, summarize results, build a dashboard—or pursue your own idea.

**One possible starting point:** independently regenerate the primitive xi-value enclosures for a retained finite Pick control and compare them with its exact matrix certificate. That improves a clearly identified evidence boundary without requiring a new RH mechanism. An analytic alternative is to isolate and prove one source-specific bound in the [fixed-detector negative-mass problem](OPEN_CUTS.md#fixed-detector), preserving the signed terms and both excursion endpoints.

## What has been achieved

**Arithmetic with explicit sources.** A complete reduction sends any hypothetical Robin-inequality violation to an integer with consecutive prime support and decreasing exponents. Exact finite bounds support that reduction. A separate Möbius-weighted construction has a genuine all-scale positivity theorem for every real power $m\ge2$; reaching the critical power $m=1$ remains open. The fixed-prime $P_{61}$ bias theorem also holds for every real endpoint; this does not establish uniformity over growing prime sets. [Arithmetic results](RESULTS.md#arithmetic).

**Analytic criteria and finite witnesses.** Fixed Mellin transforms make precise which arithmetic negative-mass estimate would imply RH. Derivative-free xi/Pick/Loewner tests give exact finite predicates that an RH failure would violate. Low-order safe-axis xi positivity, compact wavelet identities and source-specific Schur reductions clarify what can be proved without the missing global sign. [Analytic and operator results](RESULTS.md#analytic).

**Certificates and structural mathematics.** Retained Robin and complex Pick controls, a repaired fixed-$P_{61}$ certificate, and a seven-point continuum kernel inequality have explicit evidence contracts. Work on L-function families, function fields, recurrence/cofactor algebra and filtered complexes provides additional exact or conditional components. Their connection to the actual zeta source is a separate question. [Certificates](RESULTS.md#certificates) · [Families and structures](RESULTS.md#structures).

These statements summarize the cumulative integrated record, including earlier work. Classical inputs are credited in the linked proofs; repository acceptance is not a claim of external novelty.

## Integrated baseline and active research

**Current integration:** the September 6, 2026 A/B/C/D consolidation builds on the earlier baseline through PR #707; see [exact source coverage and exclusions](integration/2026-09-06/README.md). Later branch revisions remain exploratory unless separately reviewed and integrated.

The pages above describe reviewed components at their recorded sources, with later corrections applied. They do not certify every file on main. [Active research](PROGRAMMES.md#active-research), including newer branch revisions, remains discoverable but is not accepted merely because it exists or has passed an author's tests. Earlier results retain their inherited review scope unless an applicable correction changes it.

**Formalization is a separate track.** See [formal status and limitations](FORMAL_STATUS.md).

## License

Project code and original research materials are available under the [MIT License](LICENSE). Third-party material retains its existing terms and notices.
