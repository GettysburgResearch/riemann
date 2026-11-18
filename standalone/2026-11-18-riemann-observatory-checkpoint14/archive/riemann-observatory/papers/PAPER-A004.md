# PAPER-A004 — Alpöge–Furman: rank, trace, and off-line inertia

Levent Alpöge and Ralph Furman, [*More than two thirds of the zeta zeros are simple and on the critical line*, arXiv:2608.13637v2](https://arxiv.org/abs/2608.13637v2), first 13 August 2026, revised 19 August 2026. Preprint. The PDF credits discovery/writing to Claude and verification/responsibility to the named authors. Attribution does not substitute for an independent audit. Accessed 17 November 2026.

**Initial checkpoint scope (superseded by the dated Round2 reading update below):** §§1–6 inspected; §7 and appendices not fully read. Bibliographic L0 complete, whole-work L1 not claimed. Lemma3.2 reconstructed and no issue found in inspected algebra; main analytic second-moment theorem and Lean code not independently verified.

TheoremA gives (2/3−o(1)) simple critical zeros and (5/6−o(1)) distinct zeros on (T,2T], improved by the Montgomery–Taylor window to 0.67250… and 0.83625… . TheoremB states the same for any **fixed primitive** Dirichlet character χ; no uniform statement in a growing conductor was checked. The theorem for ζ is not a proof of GRH.

Lemma3.2, p5: if P,Q Hermitian, P≥0, rankP≤r, n_+(Q)≤b, then r≥2trP+4trQ−4b−||P+Q||²_HS. Proof splits Q into positive and negative parts, uses von Neumann's trace inequality and scalar square inequalities. Sharpness example P=Π1,Q=2Π2 for orthogonal projections of ranks r,b. No universal improvement can follow from those matrix statistics alone.

Off-line pairing {ρ,1−conjugateρ} produces 2m(aaᵀ−bbᵀ), which has at most one positive and one negative direction. Pullback cannot increase positive index (Lemma3.1). Simple on-line zeros give positive rank-one contributions. This is the precise role of the functional-equation symmetry; treating every complex zero evaluation as positive is invalid.

The difficult bridge is Theorem5.7: a prime-side evaluation of the Hilbert–Schmidt square for a growing matrix and a smoothed compact window. Lemma2.1 Poisson sampling, boundary zero buffers, trace-norm tails and the finite-grid truncation are material hypotheses. The algebraic lemma alone establishes no proportion theorem. Lamzouri supplies an alternate finite-multiset Hilbert-space route (PAPER-A003); its derivative deweighting avoids this growing matrix but retains the analytic pair-correlation dependency.

Next: independently audit §§5.2–5.7 with explicit constants and compare normalizations to upstream pair correlation. Inspect the precise statement generated in Lean before treating its compilation as a proof of the prose theorem. No error allegation is made.

A scoped independent check of §5 found that the indicator lower bound(5.2) must be restricted to ψ0, while the MT leading term is supplied by Thm5.7 rescaling. It also found the displayed E2 bound only yields O(NlogL/L), not the sharper Prop5.2/Thm5.7 displayed rates at L=log(T/(2π)); both are o(N), preserving the limiting argument. See audits/adversarial_reviews/analytic_window_scope.md. A subsequent independent frame-operator estimate repairs the stronger quantitative claim; this reviewer reconstructed ||H||≪BL and J≪BLlogL, giving E2≪B²L²logL. The initially weaker printed estimate is preserved as proof-bookkeeping history, not a finding that the theorem is false.

Title provenance: the arXiv landing citation_title and embedded PDF Title metadata use the shorter title above; the visible v2 PDF title page reads *More than two thirds of the zeros of the Riemann zeta function are simple and on the critical line*. Both source variants are preserved in the structured record.


Round2 reading update,17November2026: all21 pages ofv2 have now been substantively read, including§7, both appendices and references. This supports whole-workLevel1, with the exact audit in audits/AF_full_reading_round2.md. No completeLevel2/3 paper audit or main Lean build is claimed. The omitted family-average extension, conditional higher-moment proposals, external numerical ceiling enclosures and author-reported review history retain their separate limitations.

Current formal update,17November2026: the pinned main Multiplicity target and all12 type/axiom queries have now completed. See experiments/results/formal_multiplicity_summary.json and audits/adversarial_reviews/AF_formal_query_semantics_rt62.md. Earlier build-pending paragraphs are historical; whole-paper Level2/3 remains unclaimed.
