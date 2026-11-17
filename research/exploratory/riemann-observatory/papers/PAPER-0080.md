# PAPER-0080 — From monoids to hyperstructures: in search of an absolute arithmetic

| Field | Value |
|---|---|
| Authors | Connes, Alain; Consani, Caterina |
| Year / stratum | 2010 / S5 |
| Venue | van Dijk, Gerrit (ed.) et al., Casimir force, Casimir operators and Riemann hypothesis. Mathematics for innovation in industry and science. Proceedings of the conference, Fukuoka, Japan, November 9--13, 2009. Berlin: de Gruyter (ISBN 978-3-11-022612-6/hbk). 147-198 (2010). |
| Identifiers | zbMATH [1234.14002](https://zbmath.org/?q=an:1234.14002) · arXiv [1006.4810](https://arxiv.org/abs/1006.4810) |
| MSC | 14A15, 11M06, 20N20, 51J10 |
| Families | D, E |
| Work type | original_paper |
| Evidence level of this record | **L1** |
| Full text | fulltext_read — arxiv.org/abs/1006.4810 |
| Selection | score 4.4265, in-pool citations 13, seed lists 0, triage relevance 4 |

## Mathematical content (Level 1: full text read)

**Research question.** Express the counting function N(q) of the hypothetical curve C = Spec Z over F_1 (whose zeta is the complete Riemann zeta) as an intersection number via the scaling action on the adele class space, and develop the algebraic structure of A_K/K^* as a monoid and hyperring, including a hyperfield R^convex extending the hyperfield of signs and function theory over Spec K and Spec S.

**Historical motivation.** Tits/Soule F_1 program, Manin's analogy of Spec Z with a curve, Kurokawa and Deninger on absolute zeta functions; Krasner hyperrings (1956) coincidentally in same proceedings as Tits' 'corps de caracteristique un'.

### Main results

- **THM-PAPER-0080-1** (Lemma 2.1 (from [6]), lemma (imported), scope: global; Sec 2.1, (5)-(6)). Under suitable regularity of N(u), for Re(s) large, $\lim_{q\to1}F(q,s)=\int_1^\infty N(u)u^{-s}d^*u$ and $\frac{\partial_s\zeta_N(s)}{\zeta_N(s)}=-\int_1^\infty N(u)u^{-s}d^*u$, with $\zeta_N(s)=\lim_{q\to1}Z(q,q^{-s})(q-1)^{N(1)}$ (Soule).
- **THM-PAPER-0080-2** (Thm 2.2 (from [6, Thm 2.2]), theorem (recalled), scope: global; Sec 2.2, eq (16)). The tempered distribution N(u) solving $-\partial_s\zeta_{\mathbb Q}/\zeta_{\mathbb Q}=\int_1^\infty N(u)u^{-s}d^*u$ is positive on $(1,\infty)$ and on $[1,\infty)$ equals $N(u)=u-\frac{d}{du}\Big(\sum_{\rho}\mathrm{order}(\rho)\frac{u^{\rho+1}}{\rho+1}\Big)+1$ (derivative in distribution sense, rho over nontrivial zeros; value at u=1 via principal-value term omega).
- **THM-PAPER-0080-3** (Thm 3.3, theorem (recalled from [6]), scope: global; Sec 3.4, (53)). $H^0(\mathbb P^1_{\mathbb F_1},\Omega)=\{(f,F(f))\mid f\in\mathcal S(\mathbb A_K)_0/\{f-f_q\}\}\oplus\mathbb C^{2}\oplus(\mathbb C[1])^{2}$, i.e. the graph of the Fourier transform up to finite dimensions; the representation $\vartheta[-\tfrac12]$ of $C_K$ on $H^1(\mathbb P^1_{\mathbb F_1},\Omega)$ gives the spectral realization of zeros of L-functions and is invariant under chi(g) -> chi(g^{-1}).
- **THM-PAPER-0080-4** (Thm 4.2 + Cor 4.3 (from [8]), theorem/corollary, scope: global; Sec 4.2). For commutative ring R and proper subgroup G of R^x, the hyperring R/G contains the Krasner hyperfield K={0,1} as sub-hyperfield iff {0} U G is a subfield of R. Hence the adele class space H_K=A_K/K^x is a hyperring extension of K.
- **THM-PAPER-0080-5** (Thm 5.6, theorem, scope: global; Sec 5.2, eq (65)). On R there is a unique hyperfield structure $\mathbb R^{convex}=(\mathbb R,+_c,\cdot)$ with $x+_cy=\{\alpha x+\beta y\mid\alpha,\beta>0,\ \mathrm{sign}(\alpha x+\beta y)=\alpha\,\mathrm{sign}(x)+\beta\,\mathrm{sign}(y)\}$ and ordinary multiplication, characterized by $x+_cy=(x,y)$ for $y>x>0$ and containing the hyperfield of signs S as sub-hyperfield; $x+_c(-x)=\{-x,0,x\}$, $x+_cx=\{x\}$.
- **THM-PAPER-0080-6** (Prop 5.7, proposition, scope: global; Sec 5.2, (69)). $\mathrm{Aut}(\mathbb R^{convex})\cong\mathbb R^\times$ via $\lambda\mapsto\theta_\lambda$, $\theta_\lambda(x)=x^\lambda$ for x>0 and fixing S; Remark 5.8: no intermediate sub-hyperfield between S and R^convex.
- **THM-PAPER-0080-7** (Thm 8.12, theorem, scope: global; Sec 8.2). The finite functions $D_{finite}(S)\subset\mathrm{Hom}(\mathbb Z[T],S)$ form under hyperaddition $\star_{\Delta+}$ a canonical hypergroup isomorphic to $\mathbb R\times_{\bar{\mathbb Q}^c}S$; the subset with Re(phi) != 0 under hypermultiplication is isomorphic to $\mathbb R^\times\times_{\bar{\mathbb Q}^c}S$ (recovering R from function theory over Spec S).
- **THM-PAPER-0080-8** (Thm 9.1 / Thm 9.2 (from [8]), theorem, scope: global; Sec 9.2-9.3). (9.1) Principal prime ideals of H_K are p_w for a unique place w, C_K acts transitively on generators of p_w with isotropy K_w^x. (9.2) For K of characteristic p != 0 with curve X/F_q, the loop groupoid Pi_1^{ab}(X)' is canonically isomorphic, W-equivariantly, to the groupoid P(H_K) of prime elements of the hyperring H_K=A_K/K^x.

### Key definitions

- counting function N(q) / distribution N(u)
- Soule zeta zeta_N(s)
- Krasner hyperfield K={0,1}
- hyperfield of signs S
- R^convex
- hyperring H_K=A_K/K^x

### Principal lemmas

- **THM-PAPER-0080-L1** (Lemma 4.1; Sec 4.1, (54)). For commutative group G and subgroup K of Aut(G), the orbit set H={K(g)} carries the hypergroup law $K(g_1)\cdot K(g_2):=(Kg_1\cdot Kg_2)/K$. — *Role:* Source of hyperring structure on adele classes
- **THM-PAPER-0080-L2** (Thm 3.1; Sec 3 (from [7, Thm 3.34])). For a monoid scheme X, the geometric space |X| is characterized by $X(M)=\mathrm{Hom}(\mathrm{Spec}M,|X|)$, with underlying set X(F_1). — *Role:* Monoid-scheme framework for P^1 over F_1
- **THM-PAPER-0080-L3** (Thm 7.2; Sec 7.1). In the fiber over {0}, hyperaddition with generic point delta: delta*delta = whole fiber; delta*alpha = whole fiber for alpha algebraic irrational; delta*alpha = delta for alpha in Q. — *Role:* Function theory on Spec K (Krasner hyperfield)
- **THM-PAPER-0080-L4** (Thm 7.13; Sec 7.2). alpha -> phi_alpha gives a bijection of Omega/Aut(Omega) (Omega=algebraic closure of F_p) with the fiber over p in Hom(Z[T],K), compatible with hyperoperations. — *Role:* Fiber over a prime p
- **THM-PAPER-0080-L5** (Lemma 5.2 / Cor 5.3; Sec 5.1). Characterization of sign-convex subsets C of R (x,y in C implies the convex-combination-with-matching-sign set lies in C). — *Role:* Construction of R^convex

### Proof architecture

Survey/overview paper: Sec 2 recalls (with proofs referred to [6]) how Soule's limit q->1 is replaced by integral formula (6) and gives N(u) via zeros, positive for u>1; Sec 3 summarizes monoid-scheme geometry and spectral realization on H^1(P^1_{F_1},Omega); Sec 4 introduces hyperrings and the hyperring structure of H_K; Sec 5 constructs R^convex and S(G); Secs 6-8 develop function theory on Spec K and Spec S by coproducts; Sec 9 summarizes prime elements of H_K and the comparison with the loop groupoid. New proofs are mainly Secs 5-8 (hyperfield and function-theory lemmas); Secs 2-3, 9 are summaries of [6],[8].

Dependency edges: CAND-01310 → CAND-01561 (continues the adele-class-space dictionary in algebraic language); CAND-01928 → CAND-01310 (follows: arithmetic site uses the N(u) counting distribution)

**Imported results.** [6] Lemma 2.1, Thm 2.2 (N(u) formula and positivity); [7] Thm 3.34 (geometric realization of Mo-schemes); [8] Prop 2.6 (R/G contains K), Theorem on prime elements and loop groupoid; Weil explicit formula

**Techniques.** Hasse-Weil limit q->1 (Soule) replaced by integral formula; trace formula / explicit formula as intersection number; Kato-Deitmar monoid schemes and F_1-geometry; Krasner hyperrings/hyperfields, quotient hyperrings R/G; sign-convex sets and hyperfield R^convex; coproduct-induced hyperoperations on Hom(Z[T],-)

## Context and interpretation

**Importance and obstacle overcome.** Resolves the apparent contradiction N(1)=-infinity versus N(q)>0 for q>1 by replacing Soule's limit with a distributional integral and exhibits positivity of N(u) on (1,infinity) unconditionally; supplies hyperring/hyperfield algebraic structure to the adele class space needed for later 'arithmetic site' work.

**Relation to prior work.** Summarizes Connes-Consani [6] (Schemes over F_1 and zeta functions), [7] (Mo-schemes), [8] (hyperring of adele classes), builds on Connes 1999 trace formula; precedes the arithmetic site paper (CAND-01928).

**Limitations and open questions.** No new RH-relevant inequality. The curve C=Spec Z/F_1 remains hypothetical; the intersection-number description of N(q) is a reformulation of explicit formulas. Function theory over Spec S recovers R but not a Weil cohomology or Riemann-Roch. Heavy reliance on [6] and [8] for proofs.

## Research potential

- **Hypotheses that might be weakened.** Thm 2.2 positivity of N(u) on (1,infinity) holds unconditionally; the RH-equivalent statement would be a sign/size property of the oscillatory zero sum inside N(u) uniformly; one can test which part of the zero-sum derivative d/du sum order(rho) u^{rho+1}/(rho+1) is controlled by RH (bounded by u^{3/2} order) versus unconditionally.
- **Generalizations.** Thm 5.10 gives hyperfields S(G) for any totally ordered commutative abelian group G satisfying (70); applicable to tropical/Hahn-type targets and to extensions of the program to other global fields (Thm 9.1 for general K).
- **Candidate connections.** Relation between R^convex hyperaddition and Rmax^+ used in the arithmetic site (CAND-01928); relation of N(u) distribution to Weil's explicit formula positivity and Li coefficients.
- **Reusable lemmas.** Eq (16) explicit expression of N(u) as zeros sum; Thm 5.6 characterization via sign-convexity.
- **Possible experiments.** Truncate the zero sum in (16) at height T and compute the resulting smoothed N(u) to test positivity numerically for u>1 and the behavior near u=1 (finite check; sensitivity to the principal-value term omega(1) must be treated); the checks are illustrative only.
- **Risks / barriers.** No cohomological or positivity mechanism for RH is produced; hypothetical curve C is not constructed; hyperfield results are algebraic and independent of arithmetic of zeta zeros.

## Audit notes (Level 1 reader)

Fetch tool emitted a PDF xref warning; text appears complete. Statement of Thm 2.2 depends on distributional interpretation at u=1 delegated to [6]. none further noticed in inspected portion.

*These notes are a reader's observations, not verified findings; see `audits/` for adjudicated findings.*

## Provenance

- Candidate `CAND-01310`; harvest queries: kw_RH_any, msc_11M06, arxiv_explicit_formula.
- Triage decision: include — Connes-Consani program on absolute arithmetic and the hypothetical curve over F_1.
- Record generated by `tools/make_records.py`; search cutoff 2026-11-17.
