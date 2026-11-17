# PAPER-0129 — Selberg's conjectures and Artin \(L\)-functions

| Field | Value |
|---|---|
| Authors | Murty, M. Ram |
| Year / stratum | 1994 / S4 |
| Venue | Bull. Am. Math. Soc., New Ser. 31, No. 1, 1-14 (1994). |
| Identifiers | zbMATH [0805.11062](https://zbmath.org/?q=an:0805.11062) · DOI [10.1090/S0273-0979-1994-00479-3](https://doi.org/10.1090/S0273-0979-1994-00479-3) · arXiv [math/9407219](https://arxiv.org/abs/math/9407219) |
| MSC | 11M41, 11R42, 11R39 |
| Families | E |
| Work type | original_paper |
| Evidence level of this record | **L1** |
| Full text | fulltext_read — https://arxiv.org/abs/math/9407219 |
| Selection | score 3.8695, in-pool citations 20, seed lists 1, triage relevance 4 |

## Mathematical content (Level 1: full text read)

**Research question.** Show that Selberg's orthonormality conjecture (Conjecture B) for primitive elements of the Selberg class implies Artin's holomorphy conjecture, and, for solvable Galois groups over Q, the Langlands reciprocity conjecture.

### Main results

- **THM-PAPER-0129-1** (Theorem 3.1, conditional theorem, scope: conditional; Sec. 3). Conjecture B implies Artin's conjecture: for K/k Galois and $\rho\neq1$ irreducible, $L(s,\rho,K/k)$ is entire. *Conditional on:* Conjecture B.
- **THM-PAPER-0129-2** (Corollary 3.2, corollary, scope: conditional; Sec. 3 (after Thm 3.1)). Let K/Q be Galois and $\chi$ an irreducible character of $\mathrm{Gal}(K/\mathbb Q)$. Conjecture B implies $L(s,\chi)$ is primitive. *Conditional on:* Conjecture B.
- **THM-PAPER-0129-3** (Theorem 4.3, conditional theorem, scope: conditional; Sec. 4). Assume Conjecture B. Let K/Q be Galois with solvable group G and $\chi$ irreducible of degree n. Then there is an irreducible cuspidal automorphic representation $\pi$ of $GL_n(\mathbb A_{\mathbb Q})$ with $L(s,\chi)=L(s,\pi)$. *Conditional on:* Conjecture B, Arthur-Clozel base change/automorphic induction for cyclic prime degree.
- **THM-PAPER-0129-4** (Proposition 2.5, conditional, scope: conditional; Sec. 2). (a) If $F=F_1^{e_1}\cdots F_r^{e_r}$ with $F_i$ primitive then Conjecture B implies $n_F=\sum e_i^2$. (b) Conjecture B implies F primitive iff $n_F=1$. *Conditional on:* Conjecture B.
- **THM-PAPER-0129-5** (Remark 4.4, remark, scope: conditional; Sec. 4). If K/Q is arbitrary Galois and $\zeta_K$ is automorphic, Conjecture B implies Langlands reciprocity for Gal(K/Q) in the same way. *Conditional on:* Conjecture B, automorphy of zeta_K.

### Principal lemmas

- **THM-PAPER-0129-L1** (Proposition 2.4 [CG]; Sec. 2). Conjecture B implies every F in S has unique factorization into primitives. — *Role:* Core of Thm 3.1: compare factorizations of $L(s,\chi_1)/L(s,\chi_2)$.
- **THM-PAPER-0129-L2** (Lemma 4.2; Sec. 4). Assume Conjecture B. If $\pi$ is irreducible cuspidal on $GL_n(\mathbb A_{\mathbb Q})$ satisfying Ramanujan, then $L(s,\pi)$ is primitive. — *Role:* Identifies automorphic L-functions with primitives; uses Rankin-Selberg (Jacquet-Shalika, Shahidi) for prime sum asymptotics (note: this part is unconditional) and Prop 2.5(b).
- **THM-PAPER-0129-L3** (Lemma 4.1 [AC]; Sec. 4). Base change and automorphic induction exist for cyclic prime-degree extensions (imported). — *Role:* Imported theorem enabling solvable case.

### Proof architecture

Thm 3.1: pass to normal closure; by Brauer induction and Artin reciprocity write $L(s,\varphi)=L(s,\chi_1)/L(s,\chi_2)$ with Hecke L-functions in S; unique factorization gives $L(s,\varphi)=\prod F_i^{e_i}$, $e_i\in\mathbb Z$; compare prime coefficients $\varphi(p)=\sum e_ia_p(F_i)$, square and sum with weight 1/p: Conjecture B gives $(\sum e_i^2)\log\log x$, Chebotarev gives $(\sum_C|C|/|G|\,|\varphi(g_C)|^2)\log\log x=\langle\varphi,\varphi\rangle \log\log x=\log\log x$, so $\sum e_i^2=1$, a single $e_i=\pm1$; positivity of the Dirichlet-series multiplicities (orders at $\zeta$-type poles absent for nontrivial $\varphi$) then forces exponent +1, so entire. (Final steps were taken from the standard argument; text read through the Chebotarev step.) Thm 4.3: solvable tower of cyclic prime-degree extensions, Arthur-Clozel, Lemma 4.2, unique factorization of $\zeta_K$.

**Techniques.** Brauer induction; Chebotarev density theorem; prime-sum orthonormality; unique factorization in the Selberg class; Rankin-Selberg nonvanishing on Re s=1

## Context and interpretation

**Importance and obstacle overcome.** Shows the Selberg orthonormality conjecture is strong enough to imply Artin's conjecture by a purely analytic route avoiding Langlands functoriality.

**Relation to prior work.** 

**Limitations and open questions.** Conditional on Conjecture B (itself open, and unique factorization is the crucial piece). Solvability needed only for automorphic identification. Murty suggests unique factorization might be attacked by finding zeros separating distinct primitives.

## Research potential

- **Hypotheses that might be weakened.** Only unique factorization plus the identity $\sum e_i^2 = n_F$ (Prop 2.5) is used; investigate whether Conjecture B(ii) orthogonality alone for the finitely many primitives appearing in a given Artin L-function suffices.
- **Generalizations.** Same argument for Hecke/Artin L-functions over number fields, or for Rankin-Selberg quotients (Murty-Murty); extend to Selberg class elements with non-integral exponents.
- **Candidate connections.** Unique factorization and Selberg orthonormality are used in GRH-for-families work (e.g. Conrey-Ghosh, Kaczorowski-Perelli) and Selberg-class degree conjecture.
- **Reusable lemmas.** Prop 2.5 / Lemma 4.2: n_F as sum of squared exponents; Artin L-function as quotient of Hecke L-functions plus second-moment prime sum.
- **Possible experiments.** Compute $\sum_{p\le x}|a_p|^2/p-\log\log x$ for small-degree Artin/GL(2) L-functions to test the O(1) constant behaviour and orthogonality for pairs of primitives.
- **Risks / barriers.** Everything is conditional on an open conjecture; no RH content, only Artin/Langlands consequences.

## Audit notes (Level 1 reader)

Proof of Thm 3.1 in the inspected text stops with the Chebotarev step before the concluding exponent argument, which was not inspected in detail (the transition from $\sum e_i^2=1$ to exponent +1 is my reconstruction). Lemma 4.2 states Ramanujan assumption; the use of Rankin-Selberg unconditional results is consistent.

*These notes are a reader's observations, not verified findings; see `audits/` for adjudicated findings.*

## Provenance

- Candidate `CAND-01031`; harvest queries: kw_function_field_rh, citation_expansion.
- Triage decision: include — Selberg conjectures and Artin L-functions; pool cited.
- Record generated by `tools/make_records.py`; search cutoff 2026-11-17.
