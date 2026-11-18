# PAPER-0029 — Quelques applications du théorème de densité de Chebotarev

| Field | Value |
|---|---|
| Authors | Serre, Jean-Pierre |
| Year / stratum | 1981 / S4 |
| Venue | Publ. Math., Inst. Hautes Étud. Sci. 54, 123-202 (1981). |
| Identifiers | zbMATH [0496.12011](https://zbmath.org/?q=an:0496.12011) · DOI [10.1007/BF02698692](https://doi.org/10.1007/BF02698692) |
| MSC | 11R45, 11R39, 14H52, 14G99, 11S37, 11F11, 14K15 |
| Families | A, E |
| Work type | original_paper |
| Evidence level of this record | **L1** |
| Full text | fulltext_read — http://www.numdam.org/item/PMIHES_1981__54__123_0.pdf |
| Selection | score 4.5977, in-pool citations 77, seed lists 1, triage relevance 4 |

## Mathematical content (Level 1: full text read)

**Research question.** Use quantitative (Lagarias-Montgomery-Odlyzko, Lagarias-Odlyzko) forms of Chebotarev, unconditional and under GRH, applied to l-adic Galois images, to bound the density of primes where a Frobenius lies in a thin l-adic analytic subvariety of the Galois group. Applications: vanishing of Fourier coefficients of modular forms (supersingular primes, Lehmer-type questions), non-lacunarity of Euler products, and effective surjectivity of mod-l representations of elliptic curves (GRH).

**Historical motivation.** Lang-Trotter conjectures on Frobenius fields, Lehmer's conjecture on tau(n), Serre's own earlier open-image theorem for elliptic curves, and the new effective Chebotarev of Lagarias-Montgomery-Odlyzko.

### Main results

- **THM-PAPER-0029-1** (Theorem 4 (Lagarias-Odlyzko, with Serre's removal of log d term), imported theorem with improvement, scope: conditional; Section 2.4, Th. 4, formula (14_R)). There is an absolute constant $c_0>0$ such that, under GRH for $\zeta_L$, for $L/K$ finite Galois with group $G$, $C\subset G$ stable under conjugation, all $x\ge 2$: $\left|\pi_C(x)-\frac{|C|}{|G|}\mathrm{Li}(x)\right|\le c_0\frac{|C|}{|G|}\,x^{1/2}\,(\log d_L+n_L\log x)$, where $n_L=[L:\mathbb Q]$, $d_L$ the absolute discriminant. (Oesterle: $c_0=2$.) *Conditional on:* GRH for the Dedekind zeta function of L (only no zeros with Re s>1/2 is needed).
- **THM-PAPER-0029-2** (Theorem 5, theorem (stated in LO; Serre completes), scope: conditional; Section 2.5, Th. 5, (21_R),(22_R)). There is an absolute constant $c_5>0$ such that under GRH, if $C\neq\emptyset$, then $\pi_C(x)\ge 1$ for all $x\ge c_5(\log d_L)^2$ (Oesterle: $c_5=70$). *Conditional on:* GRH.
- **THM-PAPER-0029-3** (Theorem 6, theorem, scope: conditional; Section 2.5, Th. 6, (25_R)). Let $L/\mathbb Q$ be Galois of degree $n$, unramified outside a finite set $S$ of primes, $G=\mathrm{Gal}(L/\mathbb Q)$. Under GRH, for every conjugacy class $C$ of $G$ there is a prime $p\notin S$ with $\sigma_p\in C$ and $p\le c_6 n^2(\log n+\sum_{q\in S}\log q)^2$ (proof gives $c_6=4c_5^{}$-type bound; $c_6=280$ using Oesterle). *Conditional on:* GRH.
- **THM-PAPER-0029-4** (Theorem 10, theorem, scope: asymptotic; Section 4.1, Th. 10, (64)-(69_R)). Let $G$ be a compact $\ell$-adic Lie group of dimension $N\ge1$, $E/K$ an infinite Galois extension with group $G$ unramified outside finite $S$, $C\subset G$ closed, conjugation-stable with $\dim_{\ell} C\le d<N$; $a=(N-d)/N$. Then (i) $\pi_C(x)=O(x/\log x\cdot \varepsilon(x)^{-a})$ unconditionally, with $\varepsilon(x)=(\log x)(\log\log x)^{-1}(\log\log\log x)^{-1}$; (ii) under GRH $\pi_C(x)=O(\mathrm{Li}(x)/x^{a/2}\cdot\ldots)$, precisely $\pi_C(x)=O(\mathrm{Li}(x)/\varepsilon_R(x)^{a})$ with $\varepsilon_R(x)=x^{1/2}/(\log x)^2$. Corollary 1: $\pi_C(x)=O(x/(\log x)^{1+a-\delta})$ for all $\delta>0$, and $O(x^{1-a/2+\delta})$ under GRH. Implied constants depend on $K,S,G,C,d$. *Conditional on:* (ii) only: GRH.
- **THM-PAPER-0029-5** (Theorem 12, theorem, scope: asymptotic; Section 5.1, Th. 12, (100)-(102_R)). Same setting; let $r=\inf_{s\in C} r(s)$ (r(s)=dim of centralizer-type invariant, dimension of the conjugacy class complement) and $\beta=(N-d)/(N-r/2)$ . Then (i) $\pi_C(x)=O(\mathrm{Li}(x)/\varepsilon(x)^{\beta})$; (ii) under GRH $\pi_C(x)=O(\mathrm{Li}(x)/\varepsilon_R(x)^{\beta})$. Since $\beta\ge a$, with strict improvement iff $r\ge1$ (no finite conjugacy classes in C). [Exact definition of r and the displayed formula for beta should be re-checked against the scan: text reads $\beta=(N-d)/(N-r/2)$.] *Conditional on:* (ii): GRH.
- **THM-PAPER-0029-6** (Theorem 15 (with Intro (c),(d_R)), theorem, scope: asymptotic; Introduction; Section 7.1-7.3 Th. 15; Section 8 Th. 20). For a non-CM weight-2 newform (example $f=q\prod(1-q^n)^2(1-q^{11n})^2$, elliptic curve $y^2-y=x^3-x^2$) and $P(x)=\#\{p\le x: a_p=0\}$: $P(x)=O(x/(\log x)^{3/2-\varepsilon})$ for all $\varepsilon>0$, and under GRH $P(x)=O(x^{4/5})$. For general weight and h=... ($h\neq0$ branch) exponent 1/4 in (177),(178_R) replaced by 1/2 when h=0. For elliptic curves (Th. 20): $P_E^{a}(x)=O(\mathrm{Li}(x)/\varepsilon(x)^{1/4})$, and under GRH $O(\mathrm{Li}(x)/\varepsilon_R(x)^{1/4})$; exponent 1/3 if $A\ne\pm2$, 1/2 if $A=0$. Intro (e): $M_f(x)\ge\alpha x$-type non-lacunarity with explicit constant for the level-11 form. *Conditional on:* GRH for the GRH parts.
- **THM-PAPER-0029-7** (Theorem 13, theorem, scope: asymptotic; Section 6, Th. 13 and 14 (non-lacunarity)). If $P(x)$ (Frobenius-type count) satisfies $\pi(x)\ll x/(\log x)^{1+\lambda... }$ i.e. $\sum$-bound with $0\le\lambda<1$, then the number $M(x)$ of $n\le x$ with $a(n)\neq0$ (multiplicative $a$) satisfies $M(x)\gg x/(\log x)^{\lambda}$ (with constant $\gamma_a>0$). Consequence: L-functions of l-adic representations with connected Zariski closure are not lacunary ($\lambda=0$).
- **THM-PAPER-0029-8** (Theorem 22 (with Th. 21, 21'), theorem, scope: conditional; Section 8, Th. 21, 21', 22, Lemmas 15-19). Let $E/\mathbb Q$ be an elliptic curve without complex multiplication with conductor-type product $N_E$ of bad primes. Under GRH there is an absolute $c$ such that $\mathrm{Im}(\rho_\ell)=\mathrm{GL}_2(\mathbb Z_\ell)$ for every prime $\ell\ge c(\log N_E)(\log\log 2N_E)^3$. Th. 21: under GRH, if $a_p\ne a'_p$ for infinitely many p (two curves, case (b)), there is $p\notin S$ with $a_p\neq a'_p$ and $p\le c_{34}(\log N_S)... (\log\log 2N_S)^{12}$-type bound (formula (251_R) reads roughly $p<c(\log N)(\log\log 2N)^{12}$; exact form not verified). *Conditional on:* GRH.

### Key definitions

- GRH: no zeros of Dedekind zeta of a number field with real part >1/2 (zeta of field E only is needed)
- pi_C(x): number of unramified places v with Nv<=x and Frobenius class in C
- l-adic dimension of closed subset of l-adic Lie group
- Exceptional zero beta of zeta_L

### Principal lemmas

- **THM-PAPER-0029-L1** (Proposition 5 (Section 1.3); Section 1.3 and Section 2.4). Discriminant ramification bound used to replace $\sum_{v\in V(E/K)}\log Nv\le\log d_L$ by $\le \frac{1}{|I|}$-type improvement (18). — *Role:* Removes the parasitic $\log d_L$ term in Lagarias-Odlyzko's GRH error, giving Th. 4.
- **THM-PAPER-0029-L2** (Theorem 8 / Theorem 9 (Section 3); Section 3, Th. 7-9). Closed analytic subspace of an l-adic analytic variety X of dimension <= d has l-dimension <= d; the number of points of Y mod l^n is O(l^{nd}) and equals vol(Y) l^{nd} for n large. — *Role:* Converts dimension of the exceptional Frobenius locus into a counting bound on a finite quotient G/G(n), feeding Chebotarev.
- **THM-PAPER-0029-L3** (Lemma 1 / Section 5.2; Section 5, Lemma 1). Compactness estimate for sets of endomorphisms of a free Z_l-module underlying improved exponent beta. — *Role:* Improves Th. 10 to Th. 12 when C avoids finite conjugacy classes.
- **THM-PAPER-0029-L4** (Lemmas 2-7 (Section 6); Section 6.2-6.3). Estimates for counts of integers with prime factorization supported on a set of primes with density-zero control; Dedekind-type counts. — *Role:* Prove Th. 13/14 (non-lacunarity of Euler products).
- **THM-PAPER-0029-L5** (Lemmas 15-19 (Section 8); Section 8, Lemmas 15-19). Group-theoretic exclusion of maximal subgroup types (Borel, normalizer of Cartan, exceptional) for mod-l images, using inertia of order (l-1)/4 and GRH Chebotarev to locate Frobenius with trace/determinant conditions. — *Role:* Gives Th. 22: GL_2(F_l) surjectivity for all l above log N_E bound under GRH.

### Proof architecture

Section 1: ramification/discriminant bounds. Section 2: quantitative Chebotarev (unconditional Th. 2,3; GRH Th. 4-6). Section 3: counting points mod l^n on l-adic analytic varieties. Section 4: apply Chebotarev to the finite quotients G/G(n) with n chosen as a function of x (balancing the discriminant of the field cut out against x), obtaining Th. 10. Section 5 sharpens exponents using that conjugacy classes in C are big. Sections 6-8 specialize: Euler product non-lacunarity (6), modular forms via Deligne's l-adic representations (7), elliptic curves, with comparison and surjectivity theorems (8). Imported: LMO and LO effective Chebotarev, Deligne/Ribet/Eichler-Shimura-Igusa, Serre's open-image theorem.

Dependency edges: CAND-00728 → Lagarias-Odlyzko 1977 (imports effective Chebotarev (GRH) and improves via Prop. 5); CAND-00728 → Lagarias-Montgomery-Odlyzko 1979 (imports unconditional Th. 3)

**Imported results.** Lagarias-Odlyzko, Effective versions of the Chebotarev density theorem (1977); Lagarias-Montgomery-Odlyzko, A bound for the least prime ideal in the Chebotarev density theorem (Invent. Math. 1979); Oesterle, Versions effectives du theoreme de Chebotarev sous GRH (Asterisque 61, 1979); Deligne l-adic representations of modular forms; Ribet CM characterization; Serre 1972 open image theorem for elliptic curves

**Techniques.** effective Chebotarev under GRH; l-adic Lie group dimension/volume counting; discriminant bounds via Hensel; optimizing level n(x) of the finite quotient; Zariski closure of l-adic images; Deligne representations of modular forms

## Context and interpretation

**Importance and obstacle overcome.** First systematic use of effective Chebotarev with l-adic Galois images to give nontrivial upper bounds for thin Frobenius loci (zero Fourier coefficients, supersingular primes), and a GRH-conditional effective version of the open image theorem. The key obstacle (dimension-dependent loss) is handled by choosing the finite level adapted to x and by Section 5 refinements.

**Relation to prior work.** Builds on Lagarias-Odlyzko (1977) and Lagarias-Montgomery-Odlyzko (1979); Oesterle's constants (unpublished, [30]); Serre's 1972 Inventiones paper on l-adic representations; Deligne and Ribet for modular forms.

**Limitations and open questions.** Serre states none of the exponents is optimal even under GRH; Lang-Trotter predicts $x^{1/2}/\log x$ for supersingular primes versus the proven $x^{4/5}$ under GRH. Th. 5 exponent 2 in $(\log d_L)^2$ conjectured improvable to $1+\varepsilon$ (Chowla: least prime in progression is $O(m^{1+\varepsilon})$). Unconditional versions rely on exceptional zero treatment.

## Research potential

- **Hypotheses that might be weakened.** Th. 4/5/6/22 need only absence of zeros with Re s>1/2 for zeta_L for the specific fields L cut out (remark 1 of 2.4): a statement for the finite set of relevant fields (rather than full GRH) is natural; in Th. 22 only fields Q(E[l]) matter.
- **Generalizations.** Replace GL_2 by higher-dimensional Galois images (abelian varieties, Sato-Tate type groups, motives) and recover x^{1-a/2} upper bounds on Frobenius loci; improve beta in Th. 12 using finer structure of C.
- **Candidate connections.** Quantitative Chebotarev/GRH error term x^{1/2}(log d + n log x) is a direct GRH-to-prime-counting translator: any unconditional zero-free region improvement transfers to Th. 10(i). Connection to Lang-Trotter and Murty-Murty-Saradha supersingular primes bounds; to Kowalski-type large sieve for Frobenius.
- **Reusable lemmas.** Th. 4 with Oesterle constant c0=2 as a clean GRH-to-effective statement; Prop. 5 (ramification-sensitive discriminant bound); Th. 10 as a black box for density-zero Frobenius loci.
- **Possible experiments.** Numerically count primes p<=10^8 with a_p=0 for the level-11 curve and compare with x^{1/2}/log x versus Serre's x^{4/5}; test Th. 22 threshold on random non-CM curves with large N_E to look for non-surjective l near the bound.
- **Risks / barriers.** Exponents are far from conjectured; improving them needs zero-density or large-sieve input beyond GRH-Chebotarev; unconditional bounds are hostage to exceptional zeros and Siegel-type constants.

## Audit notes (Level 1 reader)

OCR scan: displayed formulas in Th. 10, 12, 13, 21 are garbled in the text extract (e.g. exponent in (251_R), definition of r in Th. 12), so those statements are reconstructed and flagged for verification against the scan. Otherwise none noticed in inspected portion.

*These notes are a reader's observations, not verified findings; see `audits/` for adjudicated findings.*

## Provenance

- Candidate `CAND-00728`; harvest queries: kw_GRH, kw_RH_any, kw_function_field_rh.
- Triage decision: include — Serre's effective Chebotarev under GRH, widely used.
- Record generated by `tools/make_records.py`; search cutoff 2026-11-17.
