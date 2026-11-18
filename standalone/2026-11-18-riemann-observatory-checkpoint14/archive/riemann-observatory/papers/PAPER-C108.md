# PAPER-C108 — On the Lagarias Inequality and Superabundant Numbers

Andrew MacArevey. [Primary source](https://arxiv.org/abs/2602.15905v2), v2,19February2026. Accessed2026-11-17.

**Audit level1; whole-work read: True.**

Complete seven-page preprint read, including all proof text and references. Elementary monotonicity inequalities reconstructed; the reported finite direct checks1≤n≤54 were not replayed from author code.

Proposition2.1 pp5–6 proves L′(x)>0 forx≥e^4, whereL(x)=[H(x)+exp(H(x))logH(x)]/x andH=digamma(x+1)+gamma. Corollary2.1 p6 states integer sequenceL(n) strictlyincreases foralln≥1, using finitechecksbelow55. Theorem3.1 p6 proves anyleast Lagarias counterexample must be superabundant.

Limits:

* No log-concavity claim appears in the actual source.
* Continuous monotonicity is provedonly forx≥e^4; fullinteger monotonicity uses reportedfinitechecks.
* The source first-derivativeN(x) is different from the compactcampaignsecond-derivative numeratorN(h).
* NoRH proof or prescribedinfiniteendpointverification.

See [source comparison](../audits/lagarias_source_comparison_round2.md). No priority claim is made for the independent concavity campaign.
