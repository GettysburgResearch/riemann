# Riemann research repository

This is an open research repository for rigorous work around the Riemann Hypothesis (RH).

> **RH remains unsolved. Nothing currently integrated here proves or disproves it.**

The repository contains reviewed finite mathematics, exact and directed finite computations, conditional RH criteria, refutations, exploratory programs, and complete provenance records. Those categories are deliberately kept separate.

## The two-minute map

Start with:

1. **[START_HERE.md](START_HERE.md)** — how to read the repository and interpret status.
2. **[RESEARCH_MAP.md](RESEARCH_MAP.md)** — the four main programs and how they connect.
3. **[FRONTIERS.md](FRONTIERS.md)** — the smallest load-bearing problems that remain.
4. **[research/integrated/](research/integrated/README.md)** — readable proof-bearing packets extracted from exact reviewed commits.

A research agent should also read **[AGENTS.md](AGENTS.md)** before opening or continuing a branch.

## What physically lives on `main`

`main` now has three layers.

### Front stage

The root pages above give a current human-readable view. They are intentionally short and do not require reading a 127-row pull-request ledger.

### Research stage

- [`research/integrated/`](research/integrated/README.md) contains curated proof-bearing packets. Each packet states the mathematics, proof boundary, exact source commit, review evidence, dependencies, and next missing step.
- [`research/exploratory/`](research/exploratory/README.md) explains where speculative or unconventional work belongs.
- Existing `claims/`, `experiments/`, `literature/`, `reports/`, and `audits/` paths remain source and research records where present. An integrated packet does not erase its source.

### Backstage

[`internal/`](internal/README.md) indexes machine registries, archival tools, and the first timestamped integration snapshot. Those records preserve exact provenance and review-wave detail, but they are not the project’s front door.

## Four principal programs

| Program | Core idea | Strongest narrow reviewed material represented here | Exact unresolved burden |
|---|---|---|---|
| **Robin/Nicolas arithmetic** | Replace RH by inequalities for divisor sums, primorials, or related arithmetic sequences. | An independently reviewed finite Robin barrier, a complete reduction to consecutive-prime nonincreasing exponent vectors, and an exact shared-budget tail envelope. | Prove the inequality for the entire infinite canonical class, find one certified violation, or obtain a new asymptotic theorem that closes the unbounded tail. |
| **Weil, screw, and terminal-prime methods** | Use RH-equivalent positivity or boundedness of explicit-formula test objects; a strict finite negative witness could disprove RH. | Reviewed finite algebra and finite positive controls exist in the source record; correction packets identify coverage and locality requirements. | Close the common source/admissibility/normalization interfaces, then produce either a strict fully authenticated negative object or a cofinal/global sign theorem. |
| **Completed-\(\xi\), Pick, Loewner, and Stieltjes methods** | Under RH, horizontal \(\xi'/\xi\) responses have positive-real, Stieltjes, divided-difference, and total-positivity structure. | Reviewed derivative-free secant, divided-difference, barycentric, two-channel, matched-pole, and cross-Loewner theorems; two exact finite \(8\times8\) Pick boxes were certified positive. | Produce one strict directed negative finite predicate with all normalizations and primitive values authenticated, or prove a genuinely global positivity theorem. |
| **Kernel/operator synthesis** | Approximate localized Weil forms by finite packets, split dangerous subspaces, and control Schur complements and cofinal lower floors. | A large reviewed finite algebraic stack is indexed in the archive, but it is not yet imported as a first-class proof packet because source and cofinal dependencies remain entangled. | Establish a complete capturing hierarchy and a cofinal corrected-kernel lower bound; finite packet positivity or finite Schur algebra is not enough. |

See [RESEARCH_MAP.md](RESEARCH_MAP.md) for the logical relationships and incompatibilities among these programs.

## Strong narrow results on `main`

The initial integrated spine includes:

- the exact finite Robin barrier through \(5582\), including the adjacent threshold at \(5583\);
- the canonical Hardy–Ramanujan reduction for every hypothetical Robin counterexample;
- an exact powered dynamic-program envelope for bounded canonical Robin tails;
- derivative-free \(\xi'/\xi\) secant, divided-difference, barycentric, two-channel, matched-pole, and cross-Loewner mathematics;
- two distinct exact finite complex Pick-matrix positive-definiteness certificates;
- reviewed corrections for saturated Hardy-\(Z\) sign chains, Hermite-matrix inertia, local-versus-global inference, targeted complex-center Li coefficients, and terminal-cell coverage.

These are meaningful results. They are also narrow. A finite positive matrix does not support RH globally; a finite Robin range does not settle all integers; and a conditional implication does not prove its hypothesis.

## What must never be overclaimed

Do not infer any of the following:

- “one finite object is positive” \(\Rightarrow\) “RH is probably true”;
- “a large finite search found no witness” \(\Rightarrow\) “the route is closed globally”;
- “all zeros in one slab are on the line” \(\Rightarrow\) “a nearby global Pick, Weil, screw, or direct-\(\xi\) functional is refuted”;
- “a checker accepts internally consistent JSON” \(\Rightarrow\) “the primitive data and normalization are authenticated”;
- “a cofinal theorem is stated conditionally” \(\Rightarrow\) “its cofinal hypothesis has been proved”;
- “a later repair works” \(\Rightarrow\) “the flawed frozen claim was retrospectively verified.”

A decisive finite negative could disprove RH only if a reviewed theorem makes that predicate RH-necessary and every source, domain, normalization, coverage, and strict interval gate is satisfied.

## Contributing

Exploration is intentionally lightweight. A speculative branch may be free-form, broad, or unconventional. It should still say:

- what is proved, proposed, empirical, imported, refuted, or unknown;
- whether the conclusion is finite, local, conditional, cofinal, or global;
- which exact source or artifact it relies on;
- what was actually run;
- what the smallest missing step is.

Promotion into [`research/integrated/`](research/integrated/README.md) requires exact-SHA review and a readable proof-residency packet. See [CONTRIBUTING.md](CONTRIBUTING.md).

## Historical and machine records

The first broad integration snapshot, complete PR ledger, registry, aliases, and archival utilities remain available through [`internal/`](internal/README.md). They are evidence and infrastructure, not the recommended first reading.
