# PAPER-0141 — On the zeta function of a hypersurface. I

| Field | Value |
|---|---|
| Authors | Dwork, Bernard |
| Year / stratum | 1962 / S3 |
| Venue | Publ. Math., Inst. Hautes Étud. Sci. 12, 5-68 (1962). |
| Identifiers | zbMATH [0173.48601](https://zbmath.org/?q=an:0173.48601) · DOI [10.1007/BF02684275](https://doi.org/10.1007/BF02684275) |
| MSC | 14G10, 14G15, 14J20 |
| Families | E |
| Work type | original_paper |
| Evidence level of this record | **L1-partial** |
| Full text | partial_fulltext — https://www.numdam.org/item/PMIHES_1962__12__5_0.pdf |
| Selection | score 2.7192, in-pool citations 5, seed lists 0, triage relevance 4 |

## Mathematical content (Level 1: full text read)

**Research question.** For a hypersurface S of degree d in P^n over F_q (q=p^a), with a fixed coordinate system, prove by p-adic analysis that the Weil-conjecture factor P in the zeta function has the predicted degree and is a polynomial. The paper does this under (2,p,d)=1, and under a nonsingularity hypothesis on all coordinate sections it identifies P as a characteristic polynomial. Note that the rationality of the zeta function itself was proved in Dwork's earlier paper [1] (1960). The triage note attributes rationality to this paper, which is inaccurate.

### Main results

- **THM-PAPER-0141-1** (Theorem 4.1, theorem, scope: global; Section 4, p. ~55). For each eigenvalue \lambda of the p-adic endomorphism \alpha, with W_\lambda the generalized eigenspace and r_\lambda=\dim W_\lambda/\sum_i D_i W_\lambda, the function satisfies \prod_{\lambda}(1-\lambda t)^{r_\lambda}-type identity: the quotient of characteristic series \chi_F(t)/\chi_F(qt) is a polynomial expressed through the eigenvalues (the formula is garbled in the OCR; statement paraphrased).
- **THM-PAPER-0141-2** (Theorem 4.2, theorem, scope: global; Section 4). \chi_F(t)/\chi_F(qt)-type product equals \det(I-t\alpha) on the quotient \mathfrak{B}=L(b)/\sum_i D_i L(b), provided b>1/(p-1) (OCR-garbled exact formulation).
- **THM-PAPER-0141-3** (Theorem 4.3, theorem, scope: global; Section 4). The map \alpha induced on \mathfrak{B} is a nonsingular endomorphism, hence the relevant factor (called f^{(1+n)} in the OCR) is a polynomial of degree d^n-type (exact degree formula not legible).
- **THM-PAPER-0141-4** (Theorem 4.4, theorem, scope: global; Section 4). \det(I-t\alpha)=\prod_{A}\det(I-t\alpha_A), the product over all subsets A of S={1,...,n+1}, where \alpha_A is the restriction to the image of the subspace of power series divisible by X_1...X_{n+1}-type monomials.
- **THM-PAPER-0141-5** (Corollary to Theorem 4.4, corollary, scope: global; Corollary p. ~63; Introduction p. 5). If (2,p,d)=1 then P_S(t)=\det(I-t\alpha_S) and \deg P_S = \frac{(d-1)^{n+1}+(-1)^{n+1}(d-1)}{d} (as read from the OCR; the paper's own formula is d^{-1}\{(d-1)^{n+1}+(-1)^{n+1}(d-1)\}). This is the polynomiality and degree part of the Weil conjectures for the hypersurface.
- **THM-PAPER-0141-6** (Theorem 2.2, theorem, scope: global; Section 2). If F has coefficients in a finite extension K_0 of Q_p and \lambda^{-1} is a zero of order \mu of \chi_F, then the kernel in L(b) of (I-\lambda^{-1}... \alpha)^\nu has dimension at least \mu, with \mu independent elements in L(b)\cap K_0(\lambda)[[X]].
- **THM-PAPER-0141-7** (Theorems 2.3-2.5, theorem, scope: global; Section 2). A p-adic spectral theory for \alpha on L': Thm 2.3 bounds the kernel dimension of (I-\lambda\alpha)^\mu by the multiplicity of \lambda^{-1} as a zero of \chi_F; Thm 2.4 says for s\ge s_\lambda the generalized eigenspace stabilizes, lies in L(b), and has dimension equal to the zero multiplicity; Thm 2.5 gives a surjectivity statement (I-\lambda\alpha)(K[[X]]\cap L(b)) for algebraic \lambda.
- **THM-PAPER-0141-8** (Theorem 3.1, theorem, scope: global; Section 3). A Koszul-type exactness criterion: if a certain complex of spaces of power series is exact in degree r=0 for all pairs of subsets 0\ne A\subset B of S, then it is exact for all r.

### Principal lemmas

- **THM-PAPER-0141-L1** (Theorem 1.1, 1.2; Section 1). Function-theoretic properties of one-variable p-adic power series over the completion \Omega of the algebraic closure of Q_p: factorization of entire series by Newton polygon and a Hurwitz-type theorem on limits of zero sets (OCR garbled; statement paraphrased). — *Role:* Supplies the zero-counting tools used to relate \chi_F zeros to eigenvalues of \alpha.
- **THM-PAPER-0141-L2** (Lemma 3.6; Section 3d). L(1/(p-1)) = V + \sum_i D_i L(1/(p-1)) for the relevant finite-dimensional V; so \alpha maps onto \mathfrak{B} in Theorem 4.3. — *Role:* Surjectivity giving nonsingularity of \alpha on the quotient.
- **THM-PAPER-0141-L3** (Lemma 3.11; Section 3d, line ~2103 of OCR). For b>1/(p-1), V\cap\sum_i D_i L(b)=\{0\}. — *Role:* Makes the quotient space finite-dimensional with the correct dimension.
- **THM-PAPER-0141-L4** (Lemmas 3.10, 3.15, 3.17-3.19; Sections 3d-3e). Dimension and independence statements for the action of differential operators D_i on L(b) and on subspace L_S(b) of power series divisible by X_1...X_{n+1}; Lemma 3.19 computes dimensions via a polynomial identity. — *Role:* Used to prove Theorem 4.4 by identifying the A-parts of the quotient with images of L_A.
- **THM-PAPER-0141-L5** (Equation (4.35); Introduction p. 6). \alpha\circ D_i = q\,D_i\circ\alpha-type commutation relations (OCR garbled) for the differential operators D_i. — *Role:* Explains the pairing of zeros \lambda^{-1} and (q\lambda)^{-1} in the characteristic series and is the reason to pass to the quotient by \sum D_i L(b).

### Proof architecture

Fix coordinates and set up the Dwork-style operator \alpha=\psi_p\circ F on a Banach-type space L(b) of p-adic power series in n+1 variables, so that the zeta function factors through \chi_F(t)/\chi_F(qt). Section 1: one-variable p-adic function theory. Section 2: spectral theory of \alpha with generalized eigenspaces whose dimensions equal zero multiplicities of \chi_F (Thms 2.1-2.5). Section 3: a Koszul-style analysis of the quotient by the differential operators D_i satisfying \alpha D_i = q D_i \alpha (Thm 3.1 and Lemmas 3.6, 3.10, 3.11, 3.15-3.19). Section 4: for nonsingular coordinate sections, the product over subsets A of S equals the characteristic polynomial of \alpha on the quotient (Thms 4.1-4.3), which gives polynomiality. The main complication is Thm 4.4 and the Corollary, isolating P_S as the characteristic polynomial of the restriction to the subspace divisible by X_1...X_{n+1}, which requires (2,p,d)=1. Section 4c uses a suggestion of Igusa to drop the nonsingularity of all S_A. Imported: rationality from Dwork 1960 ([1] in the paper); Weil's conjectures [3] are the target, not an input.

**Techniques.** p-adic analysis (Newton polygons, entire functions over \Omega); Dwork operator \alpha=\psi\circ F and Fredholm determinant; spectral theory of completely continuous operators on p-adic spaces; Koszul-type exactness for differential operators; coordinate-section inclusion-exclusion (product over subsets of S)

## Context and interpretation

**Importance and obstacle overcome.** Provides the first purely p-adic proof that the Weil factor for a hypersurface is a polynomial of exactly the predicted degree, going beyond the rationality in [1]. The obstacle is that the operator \alpha on the full space has too many eigenvalues, with spurious zeros paired by \alpha D_i = q D_i\alpha, which is overcome by passing to the quotient by \sum D_i L(b). The paper also introduced the p-adic cohomology-style spaces that Monsky-Washnitzer, Katz and Dwork's later work developed. It does not touch RH.

**Relation to prior work.** 

**Limitations and open questions.** As stated in the introduction, the paper makes no comment on the Riemann hypothesis |\theta_i|=q^{(\cdot)/2} for the zeros or on the functional equation. The hypothesis (2,p,d)=1 excludes p=2 with d even, because 1/(p-1)=1/p-type comparison fails only at p=2 (Introduction, p. 7). Complete intersections are only conjectured to follow by the same methods. The title says Part I, and the sequel treated the unit-root and functional-equation questions.

## Research potential

- **Hypotheses that might be weakened.** The condition (2,p,d)=1 (Section 3e and Theorem 4.4) arises from the failure of b>1/(p-1)-type inequality at p=2 with p|d. Removing it would require a modified choice of \alpha, which the paper notes in 4a.
- **Generalizations.** Complete intersections (stated as expected in the introduction). Toric or exponential-sum versions of the same Fredholm determinant, as in Adolphson-Sperber.
- **Candidate connections.** The Koszul exactness in Thm 3.1 and the quotient by \sum D_i L(b) is the p-adic analogue of Griffiths-Dwork reduction, which connects to L-function and Hasse-Weil approaches to RH analogues. The use of Fredholm determinants over non-archimedean fields suggests testing operator-theoretic ideas on archimedean zeta zeros.
- **Reusable lemmas.** Theorems 2.2-2.5 (generalized eigenspaces for \alpha equal zero multiplicities) are reusable for any Dwork-type operator.
- **Possible experiments.** For small p and d, compute \det(I-t\alpha) on the quotient numerically on truncated bases for Fermat hypersurfaces and compare with point counts over F_{p^k}; this tests degree and, indirectly, RH purity of the roots.
- **Risks / barriers.** The method gives polynomiality but yields no information about absolute values of roots, so it cannot by itself yield RH. The OCR here is poor; formulas must be rechecked against the scan before reuse.

## Audit notes (Level 1 reader)

Triage note says the paper proves rationality, but rationality is from the earlier article [1] (1960); this paper proves polynomiality and degree of the Weil factor under (2,p,d)=1. All formula-level statements above are paraphrased from garbled OCR and were not verified against the scan; proofs of Sections 2-4 were not read line by line.

*These notes are a reader's observations, not verified findings; see `audits/` for adjudicated findings.*

## Provenance

- Candidate `CAND-00680`; harvest queries: kw_function_field_rh.
- Triage decision: include — Dwork's proof of rationality of zeta of varieties, first Weil conjecture.
- Record generated by `tools/make_records.py`; search cutoff 2026-11-17.
