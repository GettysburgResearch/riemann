# Sylvester division-boundary -> native Möbius cutoff-boundary research packet

Status: **research continuation / proposed mathematics**. RH is not claimed proved.

This packet continues PR #848 at head `617cfaca6130addd2d16bbce6af117a55aef761b` and records a focused transfer principle suggested by Burungale--Tian, *A proof of Sylvester's conjecture*, arXiv:2609.14893v2 (15 Sep 2026).

The paper's decisive mechanism is not imported as a theorem about zeta. Its value here is architectural:

1. a natural trace vanishes;
2. one performs an arithmetic division before tracing;
3. the resulting boundary survives in a finite kernel and is proved nonzero from source-specific Frobenius/Kummer data;
4. an integral norm--projector identity forces the desired character component to survive;
5. analytic machinery then converts that nonvanishing to the target L-function statement.

For the Newton/Möbius programme, the closest native analogue is the exact cutoff boundary in divisor inversion. For
[
R_Y(n)=sum_{substack{dmid n\dle Y}}mu(d),
]
and (n=ell^a m), ((ell,m)=1), pairing (d) with (ell d) gives
[
R_Y(n)=sum_{substack{dmid m\Y/ell<dle Y}}mu(d).
]
Thus every complete divisor pair cancels and the residual is supported exactly on pairs cut by the cutoff.

This packet develops that observation into an interaction object designed to feed the open distinct-product covariance in #848. The main point is to retain **which divisor pairs crossed the cutoff** before applying Cauchy/absolute values.

Read:
- `PROOF_NOTES.md`: exact identities and structural lemmas.
- `RESEARCH_TARGET.md`: the proposed all-scale inequality and falsification criteria.
- `LFAMILY_NOTE.md`: the separate, bounded relevance to issue #738.
- `SOURCE_NOTE.md`: paper mechanism and transfer firewall.

No result in this directory upgrades the current status of RH. The new exact identities are elementary and should be independently checked; the all-scale covariance estimate remains open.
