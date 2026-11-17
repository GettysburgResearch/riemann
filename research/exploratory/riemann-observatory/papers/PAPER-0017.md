# PAPER-0017 — Zeroes of zeta functions and symmetry

| Field | Value |
|---|---|
| Authors | Katz, Nicholas M.; Sarnak, Peter |
| Year / stratum | 1999 / S4 |
| Venue | Bull. Am. Math. Soc., New Ser. 36, No. 1, 1-26 (1999). |
| Identifiers | zbMATH [0921.11047](https://zbmath.org/?q=an:0921.11047) · DOI [10.1090/S0273-0979-99-00766-1](https://doi.org/10.1090/S0273-0979-99-00766-1) |
| MSC | 11M06, 14G10, 11M41, 81Q99 |
| Families | B, E |
| Work type | original_paper |
| Evidence level of this record | **L1** |
| Full text | fulltext_read — https://web.williams.edu/Mathematics/sjmiller/public_html/ntprob19/handouts/general/KatzSarnak_Zeroes%20of%20zeta%20functions%20and%20symmetry%20BAMS%201999.pdf |
| Selection | score 4.61, in-pool citations 140, seed lists 3, triage relevance 5 |

## Mathematical content (Level 1: full text read)

**Research question.** What is the symmetry behind the Montgomery-Odlyzko law (GUE local statistics of high zeros), and what do families of zeta/L-functions say about a spectral interpretation of the zeros? Survey of function-field theorems (monodromy equidistribution), number-field theorems for low-lying zeros of families, and numerics.

**Historical motivation.** Hilbert-Polya idea; Odlyzko's numerics and Montgomery's pair correlation; Katz-Sarnak function field theory (abstract, Section 1).

### Main results

- **THM-PAPER-0017-1** (Montgomery theorem (9)-(10), imported theorem (survey), scope: asymptotic; Section 1, eqs (9)-(10)). For $\phi\in\mathcal S(\mathbb R)$ with $\operatorname{supp}\hat\phi\subset(-1,1)$: $\lim_{N\to\infty}\frac1N\sum_{1\le j\ne k\le N}\phi(\widehat{\gamma}_j-\widehat{\gamma}_k)=\int\phi(x)\bigl(1-(\sin\pi x/\pi x)^2\bigr)dx$, where $\widehat\gamma_j$ are zero ordinates scaled by mean density (under RH). Conjectured for all supports. *Conditional on:* RH.
- **THM-PAPER-0017-2** ((37)-(38), theorem (imported, Katz-Sarnak [K-S1]), scope: asymptotic; Section 3, p.11). For curves of genus $g$ over $\mathbb F_q$ with moduli $\mathcal M_g(\mathbb F_q)$ and $k\ge1$: $\lim_{g\to\infty}\lim_{q\to\infty}\frac1{\#\mathcal M_g(\mathbb F_q)}\sum_{C}D(\mu_k(C/\mathbb F_q),\mu_k(GUE))=0$; hence almost all curves obey the Montgomery-Odlyzko law as $q,g\to\infty$ (order of limits: $q$ first).
- **THM-PAPER-0017-3** ((41), theorem (imported [K-S1]), scope: asymptotic; Section 3-4, p.13). For hyperelliptic family $\Delta\in H_n(\mathbb F_q)$ (monic squarefree degree n, $g=g(n)$) and $f\in C_0(\mathbb R_{\ge0})$: $\lim_{n\to\infty}\lim_{q\to\infty}\frac1{\#H_n}\sum_\Delta f(\theta_j(\Delta)2g/2\pi)=\int f\,d\nu_j(Sp)$ (monodromy full $Sp(2g)$).
- **THM-PAPER-0017-4** ((42), (48), (49) conjectures and Legendre-curve twist, conjecture / theorem, scope: asymptotic; Section 4, pp.13-14). Conjecture: (41) holds without inner $q\to\infty$ limit. For twists $E\otimes\chi_\Delta$ of the Legendre curve (monodromy $O(N)$), sign +1 sub-family gives $SO(even)$ and sign -1 gives $SO(odd)$ distribution of $j$-th zero as $n\to\infty$, $q\to\infty$ first.
- **THM-PAPER-0017-5** (Density Conjecture (Remark 1, Sec. 4), conjecture, scope: asymptotic; Section 4, Remark 1, p.20). For a family $\mathcal F$ of L-functions ordered by conductor, $W(X,\mathcal F,\phi)=\frac1{\#\mathcal F_X}\sum_{c_f\le X}\sum_j\phi(\gamma_f^{(j)}\log c_f/2\pi)\to\int\phi\,w(G(\mathcal F))$ for all Schwartz $\phi$ (no support restriction), with $G(\mathcal F)$ the symmetry type.
- **THM-PAPER-0017-6** (Family I (Dirichlet quadratic) I(b), theorem (imported [K-S2], Ozluk-Snyder), scope: asymptotic; Section 4, p.15). Under RH for $L(s,\chi)$, quadratic primitive $\chi$ of conductor $\le X$: $W\to\int\phi\,w(Sp)$ for $\operatorname{supp}\hat\phi\subset(-2,2)$. Symmetry type Sp; Rubinstein: n-level densities for small support. *Conditional on:* RH (GRH) for the L-functions in family.
- **THM-PAPER-0017-7** (Families II-IV, theorems (imported), scope: asymptotic; Section 4, pp.17-20). II: $f\otimes\chi$ quadratic twists of GL2 form: $SO(even)/SO(odd)$ for $\operatorname{supp}\hat\phi\subset(-1,1)$ [K-S2]. III: weight-2 Hecke eigenforms for $\Gamma_0(N)$, N prime: $SO(even)/SO(odd)$ for $\operatorname{supp}\hat\phi\subset(-2,2)$ [Iwaniec-Luo-Sarnak]. IV: $L(s,\mathrm{sym}^2f)$ weight k: Sp for $\operatorname{supp}\hat\phi\subset(-4/3,4/3)$ [I-L-S]. All assume RH for family members. *Conditional on:* GRH for family members.
- **THM-PAPER-0017-8** ((56),(57) and Applications, derived consequence, scope: conditional; Section 5, pp.20-21). Density Conjecture implies $\#\{f\in\mathcal F_X:\epsilon_f=1,L(1/2,f)\neq0\}/\#\{\epsilon_f=1\}\to1$ and the analogue for $L'(1/2,f)$ with $\epsilon_f=-1$; with Kolyvagin and BSD gives Goldfeld's conjecture on ranks of quadratic twists (rank 0 for 100% of $\epsilon=+1$, rank 1 for 100% $\epsilon=-1$). Approximation II(b) gives, assuming RH, rank$(E_D)=0$ for at least 25% of D with $\epsilon=1$ (Brumer-Heath-Brown). *Conditional on:* Density Conjecture, BSD, RH.
- **THM-PAPER-0017-9** (Conclusion (Section 6), heuristic/philosophy, scope: conditional; Section 6, pp.23-24). Zeros of each $L(s,f)$ should be eigenvalues of operator $U(f)$ on a space $H$, equidistributed in a symmetry class as $f$ varies; since $\zeta$ lies in Family I (symplectic), the putative operator should preserve a symplectic form (footnote 4).

### Key definitions

- $\mu_k$: k-th consecutive spacing measure; $\nu_j(G)$: distribution of j-th eigenangle near 1 for $G(N)$, $N\to\infty$
- $W(X,\mathcal F,\phi)$, $\Delta(f,\phi)$ level density statistics (54)-(55)
- Symmetry type $G(\mathcal F)\in\{U,Sp,SO(even),SO(odd)\}$
- Density Conjecture

### Principal lemmas

- **THM-PAPER-0017-L1** (Equidistribution (40); Section 3, p.12). Deligne's equidistribution: for continuous class function f on $USp(2g)$, $\lim_{q\to\infty}\sum_C f(\theta(C/\mathbb F_q))/\#\mathrm{Aut}/\sum 1/\#\mathrm{Aut}=\int f\,dA$. — *Role:* Second ingredient of (37); needs Zariski-dense monodromy = full Sp(2g) (via $M_{g,3K}$)
- **THM-PAPER-0017-L2** (Law of large numbers (22) of Section 2; Sections 2-3). Spacing measures of Haar-random elements of $G(N)$ concentrate as $N\to\infty$ (type II groups give GUE spacings). — *Role:* Third ingredient of (37)
- **THM-PAPER-0017-L3** (Monodromy computations; Sections 3-4). Monodromy of hyperelliptic family is $Sp(2g)$; of the Legendre-curve quadratic-twist family is $O(N)$ ([K-S1],[KA2]); footnote 2 explains the Sp/O switch via cup-product duality. — *Role:* Identifies symmetry type for each family

### Proof architecture

Survey. Function field: (1) monodromy of family is big (full Sp, O); (2) Deligne equidistribution of Frobenius classes in the compact group as $q\to\infty$; (3) random-matrix scaling limits and law of large numbers as $N\to\infty$. Number field: families of L-functions, test-function level densities computed through the explicit formula and Petersson/Kuznetsov (families III, IV) or character-sum (I, II) averaging; results hold for restricted Fourier support, with the Density Conjecture asserting the full range. Support extending beyond $[-1,1]$ is notable because $\hat w$ is discontinuous at $\pm1$ (Remark 3).

Dependency edges: CAND-00721 → CAND-00748 (cites as heuristic derivation of unrestricted n-level correlations); CAND-00721 → CAND-00733 (thematic: spectral interpretation and symmetry of Hilbert-Polya operator)

**Imported results.** Weil/Deligne Riemann Hypothesis for curves/varieties over finite fields; Deligne equidistribution theorem (Weil II); Montgomery 1973 pair correlation; Hejhal triple correlation; Rudnick-Sarnak n-level correlations; Katz-Sarnak [K-S1] 'Random matrices, Frobenius eigenvalues and monodromy'; [K-S2]; Iwaniec-Luo-Sarnak 'Low lying zeros of families of L-functions'; Kolyvagin; Brumer-Heath-Brown

**Techniques.** Frobenius monodromy and Deligne equidistribution; Random matrix scaling limits ($\nu_k$, $w(G)$); Explicit formula and level densities; Kloosterman-sum/Petersson analysis; Numerics (Odlyzko; Rubinstein for $q\sim10^{12}$)

## Context and interpretation

**Importance and obstacle overcome.** Reframes the GUE phenomenon as monodromy symmetry of a family, distinguishing universal local statistics from low-lying (family-dependent) statistics, and introduces the Density Conjecture; origin of symmetry-type classification of L-function families.

**Relation to prior work.** Expository synthesis of [K-S1], [K-S2], ILS, Rubinstein, Montgomery, Odlyzko; Conant Prize paper.

**Limitations and open questions.** Function field results require $q\to\infty$ before $g\to\infty$; fixed-$q$ is conjectural ((42),(48),(49)). Number field level-density theorems have restricted Fourier support and assume GRH for the family. No spectral interpretation of zeta zeros is proved (Table 2 entries 3-A and 6-A are '?'). Whether a monodromy group exists for L-functions over Q is posed as a question. Numerics converge slowly ($1/\log q$).

**Ideas in remarks/appendices/abandoned paths.** Footnote 3 (p.16): characters of order >2 give unitary symmetry and no repulsion at $s=1/2$. Remark on Gouvea-Mazur (p.21): arithmetically forced zeros affect numerics for moderate X. Footnote 1: Connes' spectral suggestion.

## Research potential

- **Hypotheses that might be weakened.** Remove the $q\to\infty$-first limit in (41)/(42) (fixed-$q$ statistics: e.g. Sawin, Entin type results; open); extend $\operatorname{supp}\hat\phi$ in Families I-IV beyond the stated bounds toward the Density Conjecture.
- **Generalizations.** Other families listed in Remark 4 (not read in detail); orthogonal vs symplectic prediction for family containing zeta (Family I) as constraint on any Hilbert-Polya operator.
- **Candidate connections.** Symplectic structure remark (footnote 4, p.24) links to Connes' trace-formula operator approach and H=xp models (CAND-00733); n-level correlation heuristic of Bogomolny-Keating (CAND-00748) and the unrestricted-support conjecture; Montgomery pair correlation.
- **Reusable lemmas.** Table 1/Table 2 dictionary (function field vs number field) as a checklist for transferring statements; level density equivalence (56)-(57) mapping density to non-vanishing proportions.
- **Possible experiments.** Reproduce Rubinstein's one-level density for quadratic Dirichlet L-functions at moderate conductors and test the $1/\log q$ corrections; test whether first-zero mean 0.7827 (Sp) is approached.
- **Risks / barriers.** No number-field monodromy group is known; restricted-support theorems do not discriminate the symmetry types beyond what is seen at support in $(-1,1)$ for Family II.

## Audit notes (Level 1 reader)

none noticed in inspected portion. (Section 2 only skimmed. Note the survey states some results with 'for any $\phi$ with support in ...' only; Family I(b) support $(-2,2)$ is as printed. Remark 3 states all except Family II allow support beyond $[-1,1]$ ; consistent.)

*These notes are a reader's observations, not verified findings; see `audits/` for adjudicated findings.*

## Provenance

- Candidate `CAND-00721`; harvest queries: kw_pair_correlation, kw_zeta_zeros, msc_11M06.
- Triage decision: include — Katz-Sarnak symmetry types for families, foundational.
- Record generated by `tools/make_records.py`; search cutoff 2026-11-17.
