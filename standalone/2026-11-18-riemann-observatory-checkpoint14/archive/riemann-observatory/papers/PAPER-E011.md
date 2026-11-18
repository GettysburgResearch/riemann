# PAPER-E011 — Relations among some conjectures on the Möbius function and the Riemann zeta-function

Shōta Inoue. *Acta Arithmetica*191(1)(2019),1–32. DOI https://doi.org/10.4064/aa170622-16-10 . Publisher page records online publication12August2019. Actual mathematical source inspected: arXiv:1705.00853v2,22June2017, https://arxiv.org/abs/1705.00853v2 . Journal metadata verified against the publisher and Crossref; the journal mathematical text was not compared with this preprint. Thus all mathematical page references below are **preprint pages**.

Private source: `sources/logarithmic_riesz_round3/inoue1705.pdf`,239235bytes, SHA256 `0cdbc0b10e26922337c892a46a2f096df52b9d179dfecb8b9356d47c0ab11a98`. Metadata snapshots are in the same directory. Accessed2026-11-17.

**Audit scope:** Level0 bibliography; targeted Level1 mathematical reading only. Read introduction pp1–3, Theorem1, and Lemma6/proof pp13–14; inspected the Mellin kernel and selected nearby formulas. Not a whole-paper substantive read, not an audit of the full explicit formula or variable-order conjecture.

The source's arithmetic Riesz mean is

M_τ(x)=Γ(τ+1)^(−1) Σ_(n≤x) μ(n)(1−n/x)^τ.

Theorem1 p3 assumes RH and the existence of a **fixed positive** τ for which M_τ(x)=o(x^(1/2)(logx)^β). It concludes m(ρ)<β+1 for every nontrivial zeroρ. We renamed its bound exponentα toβ solely to avoid confusing it with the logarithmic-window order in the current campaign.

Lemma6 pp13–14: under RH, for any nontrivial zeroρ=1/2+iγ of multiplicitym and any fixed realτ>0,

M_τ(x)=Ω_±(x^(1/2)(logx)^(m−1)).

Proof architecture: RH supplies M_τ(x)≪_(τ,ε)x^(1/2+ε); the Mellin transform is Γ(s)/[ζ(s)Γ(1+τ+s)] (Eq3.2 after subtraction of a comparison power). A nonnegative multiplier1+cos(φ−γlogx) combines the transforms at s,s+iγ,s−iγ. Assuming a one-sided eventual upper bound forces a nonpositive normalized limit, while the selected zero contributes a phase-adjustable pole coefficient. Choosingφ gives the lower bound m|Γ(ρ)|/|Γ(1+τ+ρ)ζ^(m)(ρ)| on the possible eventual upper constant. Reversing the sign gives Ω_−. The source cites the method of Montgomery–Vaughan§15.1; that full dependency was not audited here.

Theorem1's multiplicity mechanism is direct prior art for the new logarithmic-window exercise. It does not identify the arithmetic orderτ with the logarithmic orderα: the Mellin kernels differ. For the logarithmic mean the kernel is Γ(α+1)/[s^(α+1)ζ(s)], whereas the arithmetic mean uses the Gamma quotient above. Both are classical Hardy–Riesz means (PAPER-M002), of different kinds.

The source proposes a variable arithmetic-order conjecture after Theorem2. It was inspected as motivation only; no claim that it proves the growing logarithmic-order norm estimate is made. No mathematical error, contradiction, or novelty assertion is recorded.
