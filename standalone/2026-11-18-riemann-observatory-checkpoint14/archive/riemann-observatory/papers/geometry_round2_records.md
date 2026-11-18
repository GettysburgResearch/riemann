# Geometry round-two source records

Reading metrics: one full substantive reading (Weil1949); two targeted primary-text readings (DeligneI/II); no whole-paper L2 or L3 audit. See `frontiers/geometry_round2.md` for derived lemmas, countermodels and precise continuation.


# PAPER-G001: Numbers of solutions of equations in finite fields

André Weil. Bulletin of the American Mathematical Society 55 (5), 497–508 (1949). DOI: 10.1090/S0002-9904-1949-09219-4. [Primary source](https://math.ucr.edu/~res/math205B-2021/app2number-theory/weil-conjectures1949.pdf).

**Audit status:** L1; full substantive reading = True. All twelve printed pages 497–508 read. Independently reconstructed the finite Gauss-sum norm argument in equation (4); character/Jacobi/Davenport–Hasse architecture traced. Not a full L2 audit of every lifting argument or antecedent.

**Source identity:** Original 1949 journal paper, university-hosted scan; SHA-256 `55cb48abcb191cb344c01587afed7c9fea809b31826c5803c5dbd3092d1dd468`. Corrections: Not systematically searched; no assertion that all corrections or later versions were located.

## Main mathematical results

- **Equation (4), pp. 500–501:** For a nontrivial multiplicative character χ and nontrivial additive character ψ of Fq, the Gauss sum has squared absolute value q.
- **Formula (3), p. 500; estimate p. 502:** For ai∈Fq* and positive ni, the number N of affine solutions of Σ(i=0..r) ai xi^ni=0 satisfies |N−q^r|≤M(q−1)q^((r−1)/2), with M the number of rational tuples 0<αi<1, ni αi∈Z, Σαi∈Z. The actual character sum is restricted by di=gcd(ni,q−1); the stated M is a q-independent upper bound.
- **Equation (5), pp. 503–505:** For degree-v finite-field extension, lifted characters χ′=χ∘Norm and ψ′=ψ∘Trace satisfy −G(χ′,ψ′)=(−G(χ,ψ))^v.
- **pp. 505–507, equation (8):** Diagonal projective examples yield rational generating functions with eigenvalue magnitudes matching their expected weights. The general higher-dimensional statements on p. 507 are explicitly conjectural in this paper.

## Definitions and notation

- Multiplicative and additive characters; gcd di=gcd(ni,q−1).
- Source Jacobi sum j(α), defined for nonzero character exponents summing to zero modulo 1.
- Extension-field norm/trace; generating series of point counts; conjectural Betti factors.

## Proof architecture

- Express power-preimage counts by multiplicative character orthogonality.
- Reduce nonzero character contributions to Jacobi sums.
- Evaluate Gauss-sum norms and express Jacobi sums as products divided by q.
- Use norm/trace lift and a formal Euler product of monic polynomials to compare extensions.
- Pass from homogeneous affine counts to projective counts; infer diagonal zeta weights; formulate general conjectures.

## Limitations

- The general Weil-conjecture package is conjectural here, not proved.
- Smooth proper/projective hypotheses must be explicit in modern restatement; open A1/Gm refute unrestricted proper-curve factorization.
- Square-root Gauss cancellation does not constitute a general cohomological purity proof.
- No implication to classical RH is established.

## Concrete research questions

- Formalize the small Gauss-norm proof with both nontriviality hypotheses.
- Track exactly which diagonal equations give pure cohomological factors versus degenerations when characteristic divides the exponent.
- Compare formal Euler-product positivity with the genuinely geometric pole-control hypotheses.

## Context and reuse

The source belongs to the finite-field/geometry program. The campaign’s reusable outputs are a precise purity statement, a hypothesis-deletion countermodel, and a quantified tensor-amplification requirement. None constitutes a result about classical ζ zeros. Later uses/corrections were not systematically mapped in this round. Preserve original notation in the source; this record uses F for geometric Frobenius and q for the finite-field cardinality.


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
