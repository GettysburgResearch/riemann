# PAPER-0086 — Geometry of the arithmetic site

| Field | Value |
|---|---|
| Authors | Connes, Alain; Consani, Caterina |
| Year / stratum | 2016 / S6 |
| Venue | Adv. Math. 291, 274-329 (2016). |
| Identifiers | zbMATH [1368.14038](https://zbmath.org/?q=an:1368.14038) · DOI [10.1016/j.aim.2015.11.045](https://doi.org/10.1016/j.aim.2015.11.045) · arXiv [1502.05580](https://arxiv.org/abs/1502.05580) |
| MSC | 14G99, 11S40, 12K10, 14G10, 58B34, 46L85 |
| Families | D, E |
| Work type | original_paper |
| Evidence level of this record | **L1** |
| Full text | fulltext_read — arxiv.org/abs/1502.05580 |
| Selection | score 4.3687, in-pool citations 6, seed lists 2, triage relevance 4 |

## Mathematical content (Level 1: full text read)

**Research question.** Define the arithmetic site as a semi-ringed topos whose set of points over the tropical semifield R^max_+ is the quotient X_Q=Q^x\A_Q/Z^x of the adele class space of Q, so that Frobenius automorphisms correspond to the idele class group action, giving a geometric space on which the Hasse-Weil formula yields the complete zeta function, and study its square and Frobenius correspondences.

**Historical motivation.** Soule/Manin/Deninger programs for Spec Z as a curve over F_1; Connes' noncommutative approach (1999); Connes-Consani hyperring/F_1 work of 2009-2010; request for a geometric space over which the q->1 limit of Hasse-Weil holds.

### Main results

- **THM-PAPER-0086-1** (Thm 1.1 = Thm 3.8, theorem, scope: global; Intro; Sec 3.2, Thm 3.8). The set of points of the arithmetic site $(\widehat{\mathbb N^\times},\mathbb Z_{max})$ over $\mathbb R^{max}_+$ coincides with the quotient $\mathbb Q^\times\backslash\mathbb A_{\mathbb Q}/\hat{\mathbb Z}^\times$; the Frobenius automorphisms $Fr_\lambda(x)=x^\lambda$ of $\mathbb R^{max}_+$ act on these points as the idele class group action.
- **THM-PAPER-0086-2** (Thm 2.1, theorem, scope: global; Sec 2.2-2.3). The category of points of the topos $\widehat{\mathbb N^\times}$ is canonically equivalent to the category of totally ordered groups isomorphic to non-trivial subgroups of $(\mathbb Q,\mathbb Q_+)$ with injective ordered-group morphisms (Thm 2.4: for $\widehat{\mathbb N^\times_0}$, to subgroups of Q including zero, with all morphisms).
- **THM-PAPER-0086-3** (Thm 3.2, theorem, scope: global; Sec 3.1). The stalk of the structure sheaf O=Z_max at the point of $\widehat{\mathbb N^\times}$ associated to an ordered group $H\subset\mathbb Q$ is canonically isomorphic to the semiring $H_{max}=(H\cup\{-\infty\},\max,+)$.
- **THM-PAPER-0086-4** (Thm 4.2, theorem (combined with [7,8]), scope: global; Sec 4.3). The zeta function attached through $\partial_s\zeta_N/\zeta_N=-\int_1^\infty N(u)u^{-s}d^*u$ to the counting distribution of the Frobenius action on points over $\mathbb R^{max}_+$ is the complete Riemann zeta $\zeta_{\mathbb Q}(s)=\pi^{-s/2}\Gamma(s/2)\zeta(s)$; moreover $N(u)=u-\frac{d}{du}\big(\sum_{\rho}\mathrm{order}(\rho)\frac{u^{\rho+1}}{\rho+1}\big)+1$ in the distribution sense.
- **THM-PAPER-0086-5** (Thm 5.3 + Prop 5.4, theorem, scope: global; Sec 5.1-5.2). The functor $F:\mathbb N^\times_0\to Sh(\mathrm{Spec}\,\mathbb Z)$ sending * to the sheaf S is filtering and defines a geometric morphism $\Theta:\mathrm{Spec}\,\mathbb Z\to\widehat{\mathbb N^\times_0}$, sending the point p to the point attached to H(p)⊂Q; the stalk of $\Theta^*(\mathcal O)$ at p is $H(p)_{max}$ and equals B at the generic point.
- **THM-PAPER-0086-6** (Thm 1.2 = Thm 7.7, theorem, scope: global; Sec 7.4). For $\lambda,\lambda'\in\mathbb R^*_+$ with $\lambda\lambda'\notin\mathbb Q$, $\Psi(\lambda)\circ\Psi(\lambda')=\Psi(\lambda\lambda')$; the same holds for rational lambda, lambda'; if lambda, lambda' irrational and $\lambda\lambda'\in\mathbb Q$ then $\Psi(\lambda)\circ\Psi(\lambda')=\mathrm{Id}_\epsilon\circ\Psi(\lambda\lambda')$ with Id_epsilon the tangential deformation of the identity correspondence.
- **THM-PAPER-0086-7** (Prop 6.11, proposition, scope: global; Sec 6.2). The points of the unreduced square $(\widehat{\mathbb N^{\times2}},\mathbb Z_{min}\otimes_{\mathbb B}\mathbb Z_{min})$ over $\mathbb R^{max}_+$ coincide with the product of the points of the arithmetic site over $\mathbb R^{max}_+$.
- **THM-PAPER-0086-8** (Thm 8.1, theorem, scope: global; Sec 8). The semigroup End(K) of non-degenerate endomorphisms of the C*-algebra K of compact operators on l^2(Z) is an extension of the group Int(K) of inner automorphisms by the semigroup N^x via the modulus homomorphism Mod: End(K) -> N^x (action on K_0(K)=Z), with kernel Int(K); links the arithmetic site to the structure of the point in NCG and Dixmier's classification of matroids.

### Key definitions

- arithmetic site (N^x^, Z_max) (Def 3.1)
- points over R^max_+ (Def 3.6)
- Frobenius correspondence Psi(lambda)
- reduced square (N^x2^, Conv_>=(Z x Z)) (Def 6.22)
- tangential deformation of identity (Def 7.6)

### Principal lemmas

- **THM-PAPER-0086-L1** (Lemma 2.2/2.3; Sec 2.2). A flat functor F: N^x -> Sets determines a totally ordered group (H,H_+) by symmetrization of the filtered monoid (X,+). — *Role:* Classification of points of the topos
- **THM-PAPER-0086-L2** (Prop 2.5; Sec 2.3). Any non-trivial subgroup of Q is uniquely of the form H=(ordered) given by supernatural-number-type data. — *Role:* Parametrize points of the topos
- **THM-PAPER-0086-L3** (Lemma 3.7; Sec 3.2). Map Phi: (A_f/Z^x) x R_+^x -> subgroups of R defined by adelic data yields the identification of points over R^max_+ with the adelic quotient. — *Role:* Core of the adelic interpretation (Thm 3.8)
- **THM-PAPER-0086-L4** (Lemma 4.1; Sec 4.2-4.3). For Re(s) large, $\lim_{q\to1}F(q,s)=\int_1^\infty N(u)u^{-s}d^*u$ and $\partial_s\zeta_N/\zeta_N=-\int N(u)u^{-s}d^*u$. — *Role:* Hasse-Weil limit q->1
- **THM-PAPER-0086-L5** (Prop 6.7 / 6.19 / 6.21; Sec 6.2-6.4). Zmin tensor_B Zmin carries a unique bilinear multiplication; the reduced semiring Conv_>=(Z x Z) of closed convex subsets is multiplicatively cancellative; congruences F(lambda,q) separate distinct lambda. — *Role:* Construction of reduced square and Frobenius correspondences
- **THM-PAPER-0086-L6** (Prop 7.3 / 7.4; Sec 7.2-7.4). Reduction of R(lambda) tensor R(lambda') is R(lambda lambda', lambda') when lambda lambda' not in Q lambda' + Q, with explicit left/right actions; analogous formula when lambda lambda' in Q lambda'+Q for irrational lambda,lambda'. — *Role:* Composition law proof

### Proof architecture

Sec 2 classifies points of the presheaf topos N^x^ as ordered subgroups of Q via flat functors and ordered groups. Sec 3 defines O=Z_max and computes stalks H_max; Thm 3.8 identifies points over R^max_+ with Q^x\A_Q/Z^x using Lemma 3.7. Sec 4 combines this with the earlier counting function N(u) ([7,8]) to get the Hasse-Weil interpretation of the complete zeta. Sec 5 relates Spec Z with the site by the geometric morphism Theta and Cartier divisor interpretation (Prop 5.7). Secs 6-7 build the square via the semiring Z_min tensor_B Z_min, pass to Newton-polygon (convex) reduction, define Frobenius correspondences Psi(lambda) as congruences and compute their composition (Thm 7.7). Sec 8 relates the absolute point in NCG.

Dependency edges: CAND-01928 → CAND-01310 (uses counting distribution N(u) and F_1 framework); CAND-01928 → CAND-01561 (geometrizes adele class space); CAND-01785 → CAND-01928 (survey of)

**Imported results.** Connes-Consani counting distribution N(u) and complete zeta [7,8] (Lemma 4.1, Thm 4.2); Weil/Connes explicit formula (N(u) in terms of zeros); topos theory of presheaf topoi and flat functors (SGA4 / Mac Lane-Moerdijk); Dixmier's classification of matroids (Sec 8)

**Techniques.** Grothendieck topos of N^x-sets; points as flat functors; characteristic one semirings (Z_max, R^max_+, Boolean semifield B); tensor products of B-modules, Sub_>=(J) lattices of upsets; Newton polygons and convex hull semiring; congruences as ideals of semirings; adele class space quotients and Hasse-Weil limit q->1

## Context and interpretation

**Importance and obstacle overcome.** Provides the missing 'classical-type' geometric space (a topos with tropical structure sheaf) whose geometric points are the (quotiented) adele class space, so that the geometric proof of Weil can be attempted; overcomes countable-vs-continuous mismatch by showing a countable combinatorial site has real-parameter Frobenius correspondences.

**Relation to prior work.** Builds directly on Connes-Consani [7,8] (counting distribution N(u) yields complete zeta) and Connes 1999 trace formula; precedes scaling site [40] and 'Spec Z-bar' / Riemann-Roch on periodic orbits; also reinterprets Connes-Consani-Marcolli (CAND-01561) adele class dictionary.

**Limitations and open questions.** The paper does not prove RH or obtain Riemann-Roch / intersection theory on the square; it only produces the geometric space and Frobenius correspondences, leaving open the intersection pairing and positivity (the Weil step). Frobenius correspondences compose with a defect (Id_epsilon) in the irrational-product-rational case, which obstructs a clean semigroup law.

## Research potential

- **Hypotheses that might be weakened.** Thm 7.7 exceptional case lambda*lambda' in Q with lambda, lambda' irrational produces the defect Id_epsilon; classifying the composition law in this case or finding a modification of the square for which it is a strict semigroup is a bounded task.
- **Generalizations.** Replace N^x by multiplicative monoid of ideals of O_K for a number field K and Z_max by an analogous tropical semiring; Thm 3.2/Prop 5.4 suggests analogues using subgroups H(p) at primes above p.
- **Candidate connections.** Scaling site and Riemann-Roch on periodic orbits (CAND-01785 Thm 4.3); Weil positivity (17) in CAND-01785; hyperring structure of CAND-01310.
- **Reusable lemmas.** Thm 2.1 classification of points of N^x^; Thm 3.2 stalk formula; Props 6.7/6.19/6.21 (cancellative reduction via convex sets).
- **Possible experiments.** Computational verification of Psi(lambda) composition: compute Newton-polygon congruence classes of Z_min tensor Z_min for rational approximations n/d of lambda and test the defect cases lambda*lambda' rational (finite-level checks only).
- **Risks / barriers.** Intersection theory and Riemann-Roch on the square, positivity, and Frobenius-eigenspace cohomology are all missing, so no RH implication is obtained; the countable site is combinatorial and may not encode zeros except through the adelic quotient identification.

## Audit notes (Level 1 reader)

none noticed in inspected portion (Secs 6-7 proof details were not verified line by line).

*These notes are a reader's observations, not verified findings; see `audits/` for adjudicated findings.*

## Provenance

- Candidate `CAND-01928`; harvest queries: kw_RH_any, arxiv_rh_abs.
- Triage decision: include — Foundational Connes-Consani arithmetic site toward noncommutative geometry approach.
- Record generated by `tools/make_records.py`; search cutoff 2026-11-17.
