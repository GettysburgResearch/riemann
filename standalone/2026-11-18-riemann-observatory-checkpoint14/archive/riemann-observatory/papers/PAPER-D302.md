# PAPER-D302: Trapped modes in linear quantum stochastic networks with delays

Gil Tabak, Hideo Mabuchi. EPJ Quantum Technology 3, article3 (2016). DOI10.1140/epjqt/s40507-016-0041-9. [Inspected primary version](https://arxiv.org/pdf/1510.08942v2).

**Reading/audit:** whole-paperL0, completed substantive reading=False. Targeted primary reading of preliminaries/passivity context, §5 equations15–20 and half-plane factorization discussion,pp6–7; §9 equations39–43,p18, passive single-factor realization and cascade interpretation. Numerical simulations, infinite factor convergence and all appendices not audited; not a completed whole-paperL1.

**Version/provenance:** v2, 2016-03-02; SHA256 `f41a089bae35601b5be4e295a2b4dcd740d27ee470dd10ca68d811aa83dbb646`. Primary arXiv history v1 2015-10-29,v2 2016-03-02 inspected; no exhaustive later correction search. PDF internal compilation date2022 is not treated as a new arXiv revision.

## Main source content

- §5,equations15–20,pp6–7: Half-plane passive inner transfer functions are discussed via Blaschke–Potapov factors and a separate singular/delay factor; finite factor phase constants can be absorbed in a unitary prefactor.
- §9,equations39–43,p18: A rank-one factor is realized in passive state-space form with A=−C_out* C_out/2−iΩ, B=−C_out*D, and unitary D; successive factors are interpreted as a cascade.

## Limitations

- Passive open-system input/output realization is not itself the closed compact-resolvent Hilbert-space proof; that proof is supplied separately in the campaign.
- Delay/singular inner factors and infinite products are outside a finite rational-degree budget unless explicitly accounted for.
- Full26-page mathematical/numerical audit was not completed.

## Concrete next steps

- Verify closed feedback boundary domains and dark-state accounting before importing open-system transfer identities into spectral counting.
- Preserve the Laplace-to-wave-number change s=−ik and the lower-half-plane pole convention.

## Campaign connection

`proposals/independent_campaigns/factored_inner_round2.md` reconstructs the prescribed positive-phase factor class, a closed self-adjoint realization, and its stronger generalization to arbitrary finite Hermitian Ω,G with dark states charged. These are original archive analyses grounded in established realization theory; no literature novelty or RH claim is made.
