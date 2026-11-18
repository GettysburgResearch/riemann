# PAPER-G003: La conjecture de Weil : II

Pierre Deligne. Publications Mathématiques de l’IHÉS 52, 137–252 (1980). DOI: 10.1007/BF02684780. [Primary source](https://www.numdam.org/item/PMIHES_1980__52__137_0.pdf).

**Audit status:** L0; full substantive reading = False. Targeted reading: introduction pp.138–143; conventions(0.1)–(0.7); weight definitions(1.2.1)–(1.2.6), pp.153–154; §2 selected argument/Cor(2.2.10), pp.191,195–196; (3.2.3)–(3.2.5) and (3.2.15); (3.3.1)–(3.3.11), pp.204–207; (4.1.1)–(4.1.4), pp.217–218. The 116-page paper was not read in full; no completed L1 or full L2 audit.

**Source identity:** Original French journal paper, Numdam scan; SHA-256 `b06eea61bf9cb2b596c162f5befcf85d1be69828910a6107c8aa3a99c4afcc71`. Corrections: Not systematically searched; no assertion that all corrections or later versions were located.

## Main mathematical results

- **Theorem (3.3.1), p. 204; conventions (0.1), p.144:** For f:X→Y between separated noetherian algebraic spaces of finite type over Z on which fixed ℓ is invertible, and a constructible Qℓbar-sheaf F mixed of weights ≤n, R^i f! F is mixed of weights ≤n+i. The paper calls these algebraic spaces schemes by convention.
- **Corollaries (3.3.4)–(3.3.6), p. 206:** For finite-type X0/Fq and mixed F0 of weights ≤n, Hc^i(X,F) has weights ≤n+i. For X0 smooth and F0 lisse of weights ≥n, H^i has weights ≥n+i. If F0 is pure weight n and lisse, im(Hc^i→H^i) is pure weight n+i.
- **Corollary (3.3.9), p. 207:** For X0 smooth proper over Fq and ℓ≠char Fq, det(tI−F | H^i_et(X,Qℓ)) is integral and ℓ-independent, with all eigenvalue conjugates of magnitude q^(i/2). This extends I(1.6) from projective to proper.
- **Corollary (2.2.10), p. 196:** For X0/Fq a smooth curve and F0 lisse and iota-pure of weight β, each α on Hc^1(X,F) has wq(α)<β+2, where wq(α)=2log_q|iota(α)|.
- **Theorem (4.1.1), p. 217:** For X smooth projective pure dimension n over an algebraically closed field of characteristic ≠ℓ, and ample invertible sheaf L with η=c1(L), η^i:H^(n−i)(X,Qℓ)→H^(n+i)(X,Qℓ)(i) is an isomorphism for i≥0. The source chooses a Tate-twist trivialization in this section and suppresses twists.

## Definitions and notation

- Pure number of weight n relative q: algebraic and every complex conjugate has magnitude q^(n/2).
- Mixed sheaf: finite filtration with pointwise pure quotients; weights are those nonzero quotient weights.
- iota-purity for a chosen field isomorphism Qℓbar→C; real weights allowed.
- Compact versus ordinary cohomology; image of the natural map; weight shift and Tate twist.

## Proof architecture

- Local-monodromy weights and general purity criteria.
- Hadamard–de la Vallée-Poussin/Mertens method yields strict initial curve bound (2.2.10).
- Product-surface and vanishing-cycle iteration improves the bound by δ→δ/2, (3.2.4).
- Duality gives curve purity (3.2.3); dévissage and base change give (3.3.1).
- Opposite ordinary/compact weight inequalities give pure image and proper smooth purity.
- Geometric semisimplicity and nondegenerate invariants yield hard Lefschetz.

## Limitations

- General weights theorem concerns finite-field Frobenius at closed points; it does not establish classical RH.
- Purity of im(Hc→H) must not be inflated to purity of all ordinary or compact cohomology on open varieties.
- Theorem statement conventions include separatedness, noetherian hypotheses and invertible ℓ.
- Most local-monodromy and vanishing-cycle calculations remain unaudited in this campaign.

## Concrete research questions

- Fully reconstruct the strict-bound-to-contraction step for one concrete lisse sheaf family.
- Test whether proposed analytic transfers possess a real contraction mechanism, rather than merely coefficient positivity.
- Preserve properness and boundary-weight distinctions in future theorem chaining.

## Context and reuse

The source belongs to the finite-field/geometry program. The campaign’s reusable outputs are a precise purity statement, a hypothesis-deletion countermodel, and a quantified tensor-amplification requirement. None constitutes a result about classical ζ zeros. Later uses/corrections were not systematically mapped in this round. Preserve original notation in the source; this record uses F for geometric Frobenius and q for the finite-field cardinality.
