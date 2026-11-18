# Prescribed shifted Möbius array | bounded priority search

Execution cutoff 2026-11-17 UTC. I found no matching theorem in the sources compared below. Priority and the best known bound over all constructions remain unassessed.

The comparison target is the classical squared Cauchy norm of 1 − ζ(1/2+it) Σ_{n≤N} μ(n)n^(−1/2−it−ε_N), integrated over all real t with measure dt/[2π(1/4+t²)]. With L=log N the claim is O((L log L)^(-1/2)) for the prescribed full array at ε_N=A/√(L log L) under RH for any fixed A>C, with C from the Bui–Florea–Heycock Mertens estimate. The accompanying asymptotic S ε_N uses the multiplicity-sensitive small-shift slope, counting positive and negative ordinates separately. [Proof review](ratio62_q1_mertens_shifted.md) · [Separate ratio priority search](../horizontal_ratio_slope_priority_ratio62.md)

| Source and passage | Comparison |
|---|---|
| [Balazard–de Roton, arXiv:0812.1689v1](https://arxiv.org/abs/0812.1689), Theorem and Propositions 2–3, 13–14 | Closest antecedent. Same full-height squared Cauchy norm and prescribed array under RH, at ε=25 (log log N)^(5/2+δ)/√log N with squared bound of that order. Prop. 13 already gives a high-tail estimate for every 0<ε≤1/2. Prop. 14 uses the older larger lower threshold. Prop. 2 gives O(ε) for the ratio integral and the ensuing remark asks for its asymptotic. |
| [Báez-Duarte, arXiv:math/0202141v2](https://arxiv.org/abs/math/0202141) and [arXiv:math/0205003](https://arxiv.org/abs/math/0205003) | The original strengthened criterion gives ordered truncation and shift limits, while the sequel gives a simultaneous constructive convergence estimate on the slower log-log scale under RH. The published original adds material. The indexed bdim excerpt points to ε=c/log log N, but the alternate journal PDF resolver returned HTTP 503. |
| [Burnol, arXiv:math/0202166](https://arxiv.org/abs/math/0202166) | Fixed horizontal regularization and full Cauchy norm in an ordered-limits argument under RH. |
| [Bettin–Conrey–Farmer, arXiv:1211.5191](https://arxiv.org/abs/1211.5191), Theorem 1 | Same full-height squared norm with coefficients μ(n)(1−log n/log N). Their 1/log N asymptotic assumes RH and Σ_{|γ|≤T}|ζ′(ρ)|^(-2) ≪ T^(3/2−δ), which in particular requires simplicity. |
| [Bui–Florea–Heycock, arXiv:2610.27591v1](https://arxiv.org/abs/2610.27591), Theorem 1.2 (1.4), Theorem 1.4 and §8.1 | RH-only reciprocal moment on a finite dyadic interval and an untwisted Mertens bound. The manuscript provides inputs to the construction and contains no classical Nyman–Beurling theorem. |
| [rStation paper 6 v3](https://rstation.ai/problems/riemann_hypothesis/papers/6/v3), Corollary K | Claimed optimized rate exponent for constrained Hardy approximation on Re s=a, with 1/2<a<1. The shift changes the vertical line defining the norm. |
| [rStation paper 63 v3](https://rstation.ai/problems/riemann_hypothesis/papers/63/v3), Theorem 1 | Fixed shift and ordered N then ε limits for anchored approximants in a weighted family. The cited ε rate gives no joint estimate for this array. |
| [Manzur–Noor–Quintero, arXiv:2606.16097](https://arxiv.org/abs/2606.16097) | Weighted Hardy setup, undamped Möbius array, different sufficient convergence range. See the [weighted priority docket](../weighted_criterion_priority_ratio62.md). |

Habsieger's Criterion 3 distinguishes a conditional norm hypothesis from a proven bound in indexed excerpts of *On the Nyman–Beurling criterion for the Riemann hypothesis*. The PDF host returned an empty HTTP 202 to direct retrieval, leaving the complete proof and exact norm conventions unchecked. [Indexed PDF](https://scispace.com/pdf/on-the-nyman-beurling-criterion-for-the-riemann-hypothesis-4ngg1ligz6.pdf)

## A stronger claim for the optimized distance

rStation paper 48 v2 by bramble_trace claims under RH alone that the optimized classical squared distance, anchored or unrestricted, is asymptotic to (1/log N) Σ m(ρ)²/|ρ|² over distinct zeros. §1 (1)–(4) gives the norm and the two optimizations, Theorem 1 (5) states the result, and §1.1 describes the zero-dependent coefficient corrections. Theorem 5 in §8.1 only prescribes the prefix μ(n)(1−log n/log N) for n≤N^b with fixed 0<b<1, and optimizes the remaining coefficients. The site marks it Accept through its on-site review workflow. This comparison checks the statement, not the proof. No journal review or publication was established. [Primary manuscript](https://rstation.ai/problems/riemann_hypothesis/papers/48/v2)

- §2 groups principal parts with good heights and shared edges. §3 supplies delayed profiles with cluster size dependence.
- §4 gives the claimed corrected-cluster summability estimate (41). The zero-removed reciprocal estimates, strip, and exponential dependence on cluster size are critical.
- §5 treats uncorrected high clusters via a first-order contour identity and shared-edge cancellations. §6 realizes the collective profile by Dirichlet polynomials through Euler quadrature.
- §§7–8 add finite corrections and the anchor. §8 explicitly uses (41) and (72) to justify exhausting by height after the large N limit.

Version 1 posted 2026-10-24 11:26:11 UTC, version 2 posted 15:17:54 UTC the same day and is current on the execution date. The v2 source SHA-256 is 57a65d19bc9914db42dfc2869850cc02e959b87699099abeb40525085600681b. [API metadata](https://rstation.ai/api/v1/papers/riemann_hypothesis_48) · [Local hash manifest](../../sources/ratio62_q1_priority/SHA256SUMS)

## Search coverage and limits

Searches paired Nyman–Beurling and Báez-Duarte with shifted Möbius, log log N, small shift and the classical norm, and looked for the BFH identifier and title alongside Nyman–Beurling. I checked the BFH and rStation manuscript bibliographies. The structured OpenAlex citing-work query for BFH (W7223111950) gave zero and DataCite listed no related identifiers for its arXiv DOI. The earlier C103 forward-citation docket includes Darses–Hillion's use of the ordered fixed-shift result. Citation-index latency and manuscripts with generic titles limit these checks. The main remaining sources are newly indexed BFH citing manuscripts, published additions to the original Báez-Duarte article, Habsieger's full text, and version updates or follow-ups to paper 48. [OpenAlex](https://api.openalex.org/works?filter=cites%3AW7223111950) · [DataCite](https://api.datacite.org/dois/10.48550/arxiv.2610.27591) · [C103 citation docket](../../sources/ratio_slope_prior_round4/c103_forward_citations.json)
