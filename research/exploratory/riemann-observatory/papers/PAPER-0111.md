# PAPER-0111 — The arithmetic site

*Original title:* Le site arithmétique

| Field | Value |
|---|---|
| Authors | Connes, Alain; Consani, Caterina |
| Year / stratum | 2014 / S5 |
| Venue | C. R., Math., Acad. Sci. Paris 352, No. 12, 971-975 (2014). |
| Identifiers | zbMATH [1315.11054](https://zbmath.org/?q=an:1315.11054) · DOI [10.1016/j.crma.2014.07.009](https://doi.org/10.1016/j.crma.2014.07.009) · arXiv [1405.4527](https://arxiv.org/abs/1405.4527) |
| MSC | 11G99, 11M26, 58B34, 18F10, 18B25 |
| Families | D, E |
| Work type | original_paper |
| Evidence level of this record | **L1** |
| Full text | fulltext_read — arXiv:1405.4527v1 |
| Selection | score 4.1941, in-pool citations 7, seed lists 2, triage relevance 4 |

## Mathematical content (Level 1: full text read)

**Research question.** Does the non-commutative geometric approach to the Riemann zeta function (adele class space, Hasse-Weil counting distribution) have an algebraic-geometric incarnation? Answer: the Arithmetic Site, the topos $\widehat{\mathbb N^\times}$ (presheaves on the multiplicative semigroup of positive integers) with structure sheaf the tropical semiring $\overline{\mathbb N}=(\mathbb N\cup\{\infty\},\inf,+)$, whose points over $[0,1]_{\max}\subset\mathbb R^{\max}_+$ recover the quotient $\mathbb Q^\times_+\backslash\mathbb A_{\mathbb Q}/\hat{\mathbb Z}^*$ of the adele class space and whose Frobenius-count gives the complete zeta function. It also constructs the square of the site and Frobenius correspondences $\Psi(\lambda)$ toward a Weil-style proof of RH in characteristic 1.

**Historical motivation.** Connes's 1999 trace-formula approach to RH on the adele class space, the Connes-Consani Hasse-Weil F_1 count (Compositio 2010), and Soule's F_1 varieties suggested a missing algebraic-geometric space. This note supplies it as a ringed topos in characteristic 1.

### Main results

- **THM-PAPER-0111-1** (Theorem 2.2, theorem, scope: global; Sec. 2.1, p. 2). (i) The category of points of the topos $\widehat{\mathbb N^\times}$ is equivalent to the category of totally ordered groups isomorphic to non-trivial subgroups of $(\mathbb Q,\mathbb Q_+)$ with injective order-preserving morphisms. (ii) The space of isomorphism classes of points is canonically $\mathbb Q^\times_+\backslash\mathbb A_f/\hat{\mathbb Z}^*$, with $\mathbb A_f$ the finite adeles of $\mathbb Q$ and $\mathbb Q^\times_+$ acting by multiplication.
- **THM-PAPER-0111-2** (Corollary 2.3, corollary, scope: global; Sec. 2.1, p. 2). The category of points of $\widehat{\mathbb N^\times}$ is equivalent to the category of algebraic extensions $F\subset K\subset\bar F=\mathbb Q_{\max}$ of the semifield $F=\mathbb Z_{\max}$ (fraction semifield of $\overline{\mathbb N}$), morphisms being injective semifield morphisms.
- **THM-PAPER-0111-3** (Theorem 2.4, theorem, scope: global; Sec. 2.2, p. 3). At the point of $\widehat{\mathbb N^\times}$ attached to an intermediate semifield $F\subset K\subset\bar F=\mathbb Q_{\max}$, the stalk of the structure sheaf $\mathcal O=\overline{\mathbb N}$ is the semiring $\mathcal O_K=\{r\in K: r\vee1=1\}$ ($\vee$ = semiring addition).
- **THM-PAPER-0111-4** (Theorem 2.6, theorem, scope: global; Sec. 2.3, p. 3). The points of the arithmetic site $(\widehat{\mathbb N^\times},\overline{\mathbb N})$ over the maximal compact subring $[0,1]_{\max}\subset\mathbb R^{\max}_+$ form the quotient $\mathbb Q^\times_+\backslash\mathbb A_{\mathbb Q}/\hat{\mathbb Z}^*$ of the adele class space of $\mathbb Q$ by $\hat{\mathbb Z}^*$ (the extracted text writes the quotient as $\mathbb Q^\times/\mathbb A_{\mathbb Q}/\hat{\mathbb Z}^*$ in the statement). The Frobenius action $\mathrm{Fr}_\lambda\in\mathrm{Aut}([0,1]_{\max})$ corresponds to the action of the idele class group mod $\hat{\mathbb Z}^*$. The quotient is the disjoint union of (i) $\mathbb Q^\times_+\backslash\mathbb A_f/\hat{\mathbb Z}^*$ (archimedean component 0; the points defined over $\mathbb B$) and (ii) $\mathbb Q^\times_+\backslash((\mathbb A_f/\hat{\mathbb Z}^*)\times\mathbb R^*_+)$, in bijection with rank-one subgroups of $\mathbb R$ via $(a,\lambda)\mapsto\lambda H_a$, $H_a=\{q\in\mathbb Q: qa\in\hat{\mathbb Z}\}$.
- **THM-PAPER-0111-5** (Theorem 2.7, theorem, scope: global; Sec. 2.4, pp. 3-4). Let $N(u)$, $u\in[1,\infty)$, be the counting distribution of the Frobenius action on the points of the arithmetic site over $[0,1]_{\max}$. The zeta function $\zeta_N$ defined by $\frac{\partial_s\zeta_N(s)}{\zeta_N(s)}=-\int_1^\infty N(u)u^{-s}d^*u$ is the complete Riemann zeta function $\zeta_{\mathbb Q}(s)=\pi^{-s/2}\Gamma(s/2)\zeta(s)$.
- **THM-PAPER-0111-6** (Proposition 3.1 and Proposition 3.6, proposition, scope: global; Sec. 3.1, 3.3, pp. 4-5). 3.1: $\mathbb N\otimes_{\mathbb B}\mathbb N\simeq\mathrm{Sub}_{\ge}(\mathbb N\times\mathbb N)$ (hereditary subsets for product order), with unique bilinear multiplication $(q^a\otimes q^b)(q^c\otimes q^d)=q^{a+c}\otimes q^{b+d}$ making it a semiring of characteristic 1 with an action $\mathrm{Fr}_{n,m}$ of $\mathbb N^\times\times\mathbb N^\times$. 3.6: $\mathrm{Conv}_{\ge}(\mathbb N\times\mathbb N)$ (closed convex $C\subset\mathbb R_+^2$ with $C+Q=C$, extreme points in $\mathbb N^2$; operations convex hull of union and Minkowski sum) is multiplicatively cancellative, the convex-hull map $\gamma$ coincides with the reduction $\iota$ to the image in the fraction semifield, and it is universal among homomorphisms $\rho$ to multiplicatively cancellative semirings with $\rho^{-1}(0)=\{0\}$.
- **THM-PAPER-0111-7** (Proposition 3.3 and Proposition 3.4, proposition, scope: global; Sec. 3.2, p. 4). 3.3: the range of $\mu\circ\mathrm{Fr}_{n,m}$ depends only on $r=n/m$; for coprime $n,m$ it contains the ideal $\{q^a: a\ge(n-1)(m-1)\}$; and it coincides with $m_r(\sum q^{n_i}\otimes q^{m_i})=q^{\alpha}$, $\alpha=\inf(rn_i+m_i)$. 3.4: for $\lambda\in\mathbb R^*_+$, $q\in(0,1)$, $F(\lambda,q)(\sum q^{n_i}\otimes q^{m_i})=q^{\alpha}$, $\alpha=\inf(\lambda n_i+m_i)$ is a homomorphism $\mathbb N\otimes_{\mathbb B}\mathbb N\to\mathbb R^{\max}_+$; its image $R(\lambda)$ is independent of $q$, and $R(\lambda)\cong R(\lambda')$ iff $\lambda'=\lambda$ or $\lambda'=1/\lambda$.
- **THM-PAPER-0111-8** (Theorem 4.3, theorem, scope: global; Sec. 4.2, p. 6). For $\lambda,\lambda'\in\mathbb R^*_+$ with $\lambda\lambda'\notin\mathbb Q$, the composition of Frobenius correspondences is $\Psi(\lambda)\circ\Psi(\lambda')=\Psi(\lambda\lambda')$; the same holds for $\lambda,\lambda'$ rational. When $\lambda,\lambda'$ are irrational and $\lambda\lambda'\in\mathbb Q$, $\Psi(\lambda)\circ\Psi(\lambda')=\Psi(\lambda\lambda')\circ\mathrm{Id}^\epsilon=\mathrm{Id}^\epsilon\circ\Psi(\lambda\lambda')$, where $\mathrm{Id}^\epsilon$ is the tangential deformation of the identity correspondence on the sub-semiring $\overline{\mathbb N}^\epsilon$ of germs at $0$ of continuous functions $\mathbb R\to\mathbb R^{\max}_+$ generated by $q$ and $q^{1+\epsilon}$.

### Key definitions

- Arithmetic site (N-hat^x, N-bar): the topos of presheaves on the one-object category N^x with structure sheaf the tropical semiring N-bar=(N union {inf}, inf, +) with N^x acting by multiplication (Def. 2.1)
- points of a topos (geometric morphisms from Sets)
- semifield Zmax and Qmax, tropical semirings of characteristic 1
- points of the site over a local semiring R (Def. 2.5): a point p of the topos with a local morphism of semirings O_p -> R
- B=({0,1},max,x), B-module N tensor_B N = Sub>=(NxN)
- Conv>=(NxN) (Def. 3.5)
- Frobenius correspondence Psi(lambda)=(R(lambda), l(lambda), r(lambda)) with l(lambda)(q^n)q^alpha=q^{alpha+n lambda}, r(lambda)(q^n)q^alpha=q^{alpha+n} (Sec. 4.1)
- reduced correspondence (Def. 4.1)
- tangential deformation of the identity (Def. 4.2)

### Principal lemmas

- **THM-PAPER-0111-L1** (Eq. (1) (trace formula); Sec. 2.4, p. 3). $\mathrm{Tr}_{\mathrm{distr}}(\int_G h(u)\vartheta_u d^*u)=\sum_{v\in\Sigma_{\mathbb Q}}\int_{\mathbb Q_v^*}\frac{h(u^{-1})}{|1-u|}d^*u$, $\vartheta_u\xi(x)=\xi(u^{-1}x)$ on $\mathbb A_{\mathbb Q}/\mathbb Q^*$, $G=GL_1(\mathbb A_{\mathbb Q})/GL_1(\mathbb Q)$. — *Role:* Imported (Connes 1999, Connes-Marcolli, Meyer 2005); used with $h(u)=g(|u|)$, supp g in (1,infinity), to obtain the counting distribution N(u) in Thm 2.7. The note only states it.
- **THM-PAPER-0111-L2** (Def. 3.5 / Prop. 3.6(iii); Sec. 3.3, p. 5). Universal property of $\mathrm{Conv}_{\ge}(\mathbb N\times\mathbb N)$ as the reduced (multiplicatively cancellative) quotient of $\mathbb N\otimes_{\mathbb B}\mathbb N$. — *Role:* Identifies the structure sheaf of the reduced square, on which Frobenius correspondences are built.
- **THM-PAPER-0111-L3** (Prop. 3.3(i); Sec. 3.2, p. 4). For coprime $n,m$, the range of $\mu\circ\mathrm{Fr}_{n,m}$ contains $\{q^a: a\ge(n-1)(m-1)\}$. — *Role:* Frobenius (coin) problem bound; shows rational Frobenius correspondences are genuinely curves in the square.

### Proof architecture

Announcement note without proofs. Chain: (1) Topos of presheaves on N^x with tropical semiring as structure sheaf (Def. 2.1); (2) points of the topos = ordered subgroups of Q (Thm 2.2) = algebraic extensions of Zmax (Cor 2.3); (3) stalks of N-bar (Thm 2.4); (4) points over [0,1]max = adele class space mod Z-hat* (Thm 2.6), with Frobenius = idele class action; (5) the trace formula (1) from Connes/Meyer applied to $\hat{\mathbb Z}^*$-invariant test functions with support in |u|>1 gives N(u), and [5,6] shows the resulting zeta is the complete Riemann zeta (Thm 2.7), the q->1 limit of Hasse-Weil for F_q; (6) the square over B, its reduced version Conv>=(NxN), Frobenius correspondences for rational lambda via Fr_{n,m} composed with product mu, extended to real lambda via m_r = inf formula (diophantine approximation), (7) composition law with correction for irrational lambda, lambda' with rational product. Imports: Connes trace formula and Meyer's representation theory, Connes-Consani Compositio 2010 and de Gruyter 2010, Castella on tropical polynomial algebras, Pareigis-Rohrl on semimodules.

Dependency edges: CAND-01453 → CAND-01453 (depends on external Connes 1999, Connes-Consani 2010 (not in this batch))

**Imported results.** Connes, Selecta Math. 5 (1999): trace formula in noncommutative geometry; Connes-Marcolli, Noncommutative Geometry, Quantum Fields and Motives (2008); Meyer, Duke Math. J. 127 (2005): idele class group representation; Connes-Consani, Compositio 146 (2010) and de Gruyter (2010): zeta from Hasse-Weil counting distribution; SGA4, Mac Lane-Moerdijk: topos theory; Castella, Ann. Math. Blaise Pascal 20 (2013); Pareigis-Rohrl, arXiv:1305.5531

**Techniques.** topos of presheaves on a monoid; tropical/characteristic-1 semirings; Connes-Meyer trace formula for adele class space; tensor product of B-semimodules, Newton polygons / convex hulls; diophantine approximation for real Frobenius correspondences

## Context and interpretation

**Importance and obstacle overcome.** Provides the first algebraic-geometric (topos plus semiring) object whose F_1-style point count is the complete Riemann zeta function, replacing the non-commutative adele class space; makes Frobenius correspondences real objects in a square, supplying the geometric setting for a Weil-type proof (which still needs Riemann-Roch and an intersection theory in char 1). Obstacle: identifying the correct 'curve' and the correct category of spaces over B; resolved via the topos of N^x and its points.

**Relation to prior work.** Builds on Connes 1999 (trace formula), Connes-Consani Compositio 2010 and de Gruyter 2010 (q->1 limit of Hasse-Weil, counting distribution), Meyer 2005 (idele class group representation), Soule 2004 (F_1), Castella 2013 (tropical polynomial algebras), Pareigis-Rohrl (semimodules).

**Limitations and open questions.** The note does not prove RH or reduce it to a stated finite statement; it says that transposing Weil's proof (as in Grothendieck [7]) would need a Riemann-Roch theorem in characteristic 1, which is not given. Theorem 2.7 is a re-interpretation of the earlier [5,6] result; the Hasse-Weil identity gives the zeta function but not the zero location. No intersection theory, positivity, or Castelnuovo-type inequality is established here.

## Research potential

- **Hypotheses that might be weakened.** Theorem 2.7 holds for the test-function class supp g in (1,infinity); extension to all test functions (needed for zeros) is not claimed. Thm 4.3 excludes nothing but gives a defect Id^epsilon for irrational pairs with rational product.
- **Generalizations.** Replace Q by number fields or function fields (function-field case gives a classical RH check); replace N^x by other monoids; Frobenius correspondences over the square for the arithmetic site with extension of scalars (later work of the authors, not read here).
- **Candidate connections.** A positivity/Lefschetz-type argument on the Frobenius correspondences Psi(lambda) in the square, as in Weil's proof via intersection numbers of the graph of Frobenius with the diagonal; the Conv>=(N x N) semiring of Newton polygons suggests a tropical intersection theory (degree of Psi(lambda) vs diagonal). The ideal {q^a: a>=(n-1)(m-1)} is the Frobenius coin problem, relating to the genus-like count for the rational correspondence.
- **Reusable lemmas.** Prop. 3.1 and 3.6 (description of N tensor_B N and its reduced form as Newton polygons) are self-contained algebra, reusable for any tropical-geometry model of the square. Prop. 3.4(iii) classifies the images R(lambda).
- **Possible experiments.** Compute the Newton-polygon degree of the intersection of Psi(lambda) with the diagonal in Conv>=(NxN) for rational lambda = n/m, in particular compare with the count (n-1)(m-1) and check against the expected Weil-style formula 'degree = 1 + lambda - (trace)'. Test whether the explicit-formula side of (1) can be recovered from such intersection numbers.
- **Risks / barriers.** The note does not give a Riemann-Roch theorem, positivity, or any bound on zeros: the argument toward RH is entirely programmatic. The semiring Conv>=(N x N) is multiplicatively cancellative but additive structure is idempotent (characteristic 1), so classical Hodge-index/positivity arguments do not transfer directly.

## Audit notes (Level 1 reader)

Extracted text of Theorem 2.6 shows the quotient as 'Q^x/A_Q/Z-hat*' (likely a lost plus subscript in extraction; later in the same section it is written Q^x_+). The constant 'q' is a fixed number in (0,1) throughout and independence of q is asserted in Prop 3.4(ii) without proof in the note. Proofs are all omitted (announcement note), so each result relies on the authors' longer papers; none noticed otherwise in inspected portion.

*These notes are a reader's observations, not verified findings; see `audits/` for adjudicated findings.*

## Provenance

- Candidate `CAND-01453`; harvest queries: kw_RH_any, kw_function_field_rh, msc_11M26.
- Triage decision: include — Arithmetic site, Connes-Consani geometric approach.
- Record generated by `tools/make_records.py`; search cutoff 2026-11-17.
