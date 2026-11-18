# PAPER-S004 — Rodgers and Tao,2018/2020, corrected2021

**Identity.** Brad Rodgers and Terence Tao, *The De Bruijn–Newman constant is non-negative*. arXiv1801.05914, first2018-01-18; inspected v5 dated2021-07-03, https://arxiv.org/pdf/1801.05914v5 . Published in Forum of Mathematics,Pi8(2020),e6, DOI10.1017/fmp.2020.6. Publisher metadata: https://www.cambridge.org/core/journals/forum-of-mathematics-pi/article/de-bruijnnewman-constant-is-nonnegative/D4B85BA067E2D5A71D87E4FFB0D21E46 . The v5 cover retains placeholder journal metadata; do not derive publication year from it. Access2026-11-17.

**Audit scope (updated2026-11-17).** All61 pages of the actual arXivv5 preprint were substantively read sequentially, including allsections/proofs/references: whole-preprint **Level1**, not a complete Level2 audit. Scoped independent reconstruction covers the local Hamiltonian identity, a valid endpoint-cancellation estimate preserving Lemma16, and corrected Proposition27's averaging mechanism. Two literal printed auxiliary estimates have explicit independently corroborated scope witnesses; their downstream effect and a proposed signed-X4 repair are separate adjudication tasks. No claim that Theorem1 is false. The2020 journal version was not wholly read or compared.

[Full source audit and proof architecture](../audits/rodgerstao_full_source_advocate_round4.md). [Independent local/version review](../audits/adversarial_reviews/rodgerstao_local_semantic_round4.md). [Signed far-field reconstruction](../audits/adversarial_reviews/rodgerstao_far_field_advocate_round4.md).

## Precise framework

Let ξ(s)=s(s−1)π^(−s/2)Γ(s/2)ζ(s)/2 and H_0(z)=ξ(1/2+iz/2)/8, equations(1)–(2),p2. For real t set H_t(z)=∫_0^∞ exp(tu²)Φ(u)cos(zu)du, with Φ(u)=∑n≥1(2π²n⁴e^(9u)−3πn²e^(5u))exp(−πn²e^(4u)), equations(3)–(4). The superexponential decay permits the backward heat equation ∂_tH_t=−∂_z²H_t. In this normalization x_j(0) are twice the zeta-zero ordinates; missing this factor changes gap constants.

Newman's established threshold Λ is characterized by all zeros of H_t being real iff t≥Λ. Thus RH⇔Λ≤0. Theorem1,p3, proves Λ≥0 unconditionally. Hence RH becomes Λ=0, not a consequence of nonnegativity. Positive-t real-rootedness alone does not give real-rootedness at t=0.

## Inspected proof architecture

Assume Λ<0; this entails RH under the threshold characterization. On Λ<t≤0, zeros are simple and satisfy Theorem11,p27,

    ∂_t x_k(t)=2 PV∑_(j≠k) 1/(x_k(t)−x_j(t)).

The principal value is essential; a naive unrestricted rearrangement is invalid. Zero counting and gap bounds provide control for localized sums. An equilibrium comparison uses classical approximate locations ξ_j (this notation denotes locations, not the entire ξ-function) and the nonnegative convex remainder V(x)=|x|^(−2)−1+2(|x|−1). Theorem17,p40, gives ∫_(Λ/4)^0 Ẽ^[0.5TlogT,3TlogT](t)dt=o(Tlog³T). Proposition26,p55, upgrades this to Ẽ^[TlogT,2TlogT](0)=o(Tlog³T). This time-average to terminal-time step is nontrivial and must control boundary terms.

Section9,p59, derives normalized consecutive gaps=1+o(1) for a fraction1−o(1) of indices. A positive proportion of gaps<λ times the mean, for any λ>0.77, contradicts that. The paper uses its reference[7], Conrey–Ghosh–Goldston–Gonek–Heath-Brown(1985), rather than requiring the full GUE conjecture. That older result is an external dependency not read directly in this track. Using RH-conditionally obtained gap information inside a contradiction from Λ<0 is logically valid because Λ<0 already implies RH.

## Author-acknowledged version correction

The arXiv metadata explicitly states that v5 corrects Section8 boundary-energy treatment. Footnote16,p55, thanks Ofer Zeitouni for identifying an error in an earlier argument. The repaired route chooses a good interval(Proposition27) controlling integrated boundary energies, then propagates energy into a slightly shrunken interval(Proposition28) before concluding Proposition26. This is documented author correction, not a newly found current gap. We have not independently certified every repaired estimate. Any reuse should cite v5 with its date and inspect those boundary controls; citing the2020 journal title alone is not precise version provenance.

## Reuse and concrete question

The transferable structure is a nonnegative convex remainder plus localized dissipation plus boundary-controlled passage from integrated to terminal energy. It could be valuable for other zero dynamics, but neither polynomial truncation nor finite numerics substitutes for the tail estimate. State a target family F_t, prove simple real roots on a time interval, derive a legitimate principal-value root ODE, specify the approximate equilibrium and prove the relevant boundary flux bound. Only then transplant the relaxation argument.

A concrete project is to compare deformations whose zero-count scale changes: determine which assumptions on N_t(T), root rigidity and external forcing suffice to turn an integrated defect o(Tlog³T) into a terminal defect. Counterexamples with energy entering through moving boundaries should be constructed before any general theorem is asserted.
