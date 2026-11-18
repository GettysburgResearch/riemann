# PAPER-G002: La conjecture de Weil : I

Pierre Deligne. Publications Mathématiques de l’IHÉS 43, 273–307 (1974). DOI: 10.1007/BF02684373. [Primary source](https://www.numdam.org/item/PMIHES_1974__43__273_0.pdf).

**Audit status:** L0; full substantive reading = False. Targeted primary-text reading of §§1–3 (pp.273–287), statements/context (5.10), (6.1)–(6.3), and §7 (pp.298–301). Independently checked coefficient positivity in (3.3)–(3.6) and the elementary power amplification in (7.3). SGA, Lefschetz and rationality dependencies not fully audited; whole paper does not qualify for completed L1.

**Source identity:** Original French journal paper, Numdam scan; SHA-256 `8392b345d4854e6dc55fb42cfc0b616d941935983723627237239a87348f42e5`. Corrections: Not systematically searched; no assertion that all corrections or later versions were located.

## Main mathematical results

- **Theorem (1.6), p. 276:** For X0 smooth projective over Fq and ℓ≠char Fq, det(tI−F | H^i_et(X0×Fq Fqbar,Qℓ)) has integer coefficients independent of ℓ, and all complex conjugates of its roots have magnitude q^(i/2). F is geometric Frobenius, identified with pullback of the geometric Frobenius morphism by (1.15).
- **Theorem (3.2), pp. 283–285:** For a lisse Qℓ-sheaf F0 on U0=P1/Fq minus finitely many points: a perfect alternating pairing F0⊗F0→Qℓ(−β), β∈Z; open geometric monodromy image in the corresponding Sp; and rational local characteristic polynomials at every closed point imply pointwise purity of weight β.
- **Lemma (7.1), pp. 298–300; (7.3), p. 301:** A middle-degree bound q^(d/2−1/2)≤|α|≤q^(d/2+1/2) for smooth projective absolutely irreducible even-dimensional varieties is amplified on even cartesian powers, using Künneth, to exact magnitude q^(d/2).

## Definitions and notation

- Geometric Frobenius versus inverse arithmetic Frobenius, (1.15).
- Z(X0,t), Pi(t)=det(1−tF | Hc^i), trace formula, (1.5).
- Weight β at closed x means all conjugates have magnitude |k(x)|^(β/2).
- Vanishing-cycle quotient E/(E∩Eperp), not an assumed nondegenerate E.

## Proof architecture

- Grothendieck compact-support trace/determinant formula and Poincaré duality.
- Even tensor powers have positive rational local Euler coefficients; monodromy invariant theory restricts global poles.
- Lefschetz pencils supply vanishing cycles and open symplectic monodromy, (5.10).
- Rationality (6.2) on the nondegenerate quotient verifies the third hypothesis of (3.2).
- Leray filtration yields the weak middle-degree bound (7.1).
- Künneth and powers (7.3) remove a uniform ±1/2 exponent loss.
- Weak Lefschetz and duality reduce arbitrary degrees to the middle degree; weight separation yields integrality and ℓ-independence.

## Limitations

- No proof for Spec Z/classical ζ is given.
- The main theorem here is projective smooth; proper smooth is the later WeilII(3.3.9).
- Bilinear self-duality and positive Euler coefficients alone do not imply purity.
- The entire main proof and all external SGA dependencies were not audited here.

## Concrete research questions

- Replace open-Sp by a precisely sufficient even-tensor coinvariant pole bound and independently verify the derivation.
- Compute tensor invariants in one actual rank-two family and test local/global pole compatibility.
- Specify what sublinear tensor-degree localization error could mean in an actual number-field spectral model.

## Context and reuse

The source belongs to the finite-field/geometry program. The campaign’s reusable outputs are a precise purity statement, a hypothesis-deletion countermodel, and a quantified tensor-amplification requirement. None constitutes a result about classical ζ zeros. Later uses/corrections were not systematically mapped in this round. Preserve original notation in the source; this record uses F for geometric Frobenius and q for the finite-field cardinality.
