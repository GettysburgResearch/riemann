# PAPER-0067 — A bound for the least prime ideal in the Chebotarev density theorem

| Field | Value |
|---|---|
| Authors | Lagarias, J. C.; Montgomery, H. L.; Odlyzko, A. M. |
| Year / stratum | 1979 / S3 |
| Venue | Invent. Math. 54, 271-296 (1979). |
| Identifiers | zbMATH [0401.12014](https://zbmath.org/?q=an:0401.12014) · DOI [10.1007/BF01390234](https://doi.org/10.1007/BF01390234) |
| MSC | 11R45, 11R42 |
| Families | A, E |
| Work type | original_paper |
| Evidence level of this record | **L1** |
| Full text | fulltext_read — https://typeset.io/pdf/a-bound-for-the-least-prime-ideal-in-the-chebotarev-density-39uklzpcnb.pdf |
| Selection | score 4.5033, in-pool citations 37, seed lists 1, triage relevance 4 |

## Mathematical content (Level 1: full text read)

**Research question.** Unconditional upper bound for the least prime ideal in a Chebotarev class: given Galois L/K and conjugacy class C, show the least prime P of K unramified in L with Artin symbol C and norm a rational prime has norm at most $d_L^{A_1}$, without GRH.

**Historical motivation.** Lagarias-Odlyzko 1977 proved N P < b (log d_L)^2 under GRH (and effective unconditional error terms, which only give least prime above exp(d_L^c)); the unconditional polynomial-in-d_L least prime was open.

### Main results

- **THM-PAPER-0067-1** (Theorem 1.1, theorem, scope: global; Sec.1, (1.3), p.272). There is an absolute, effectively computable constant $A_1$ such that for every finite extension $K/\mathbb{Q}$, every finite Galois extension $L/K$ and every conjugacy class $C\subset \mathrm{Gal}(L/K)$, there exists a prime ideal $P$ of $K$ unramified in $L$ with $\left[\frac{L/K}{P}\right]=C$, $N_{K/\mathbb{Q}}P$ a rational prime, and $N_{K/\mathbb{Q}}P\le 2\,d_L^{A_1}$.
- **THM-PAPER-0067-2** (Theorem 1.2, theorem, scope: conditional; Sec.1, p.273). There is an absolute effectively computable constant $A_2$ such that for every number field $K$ and Hecke character $\chi$ of $K$: if $\zeta_K(s)L(s,\chi,K)$ has no zeros $\rho=\beta+i\gamma$ with $1-\delta\le\beta<1$, $0<|\gamma|\le \delta^{-2}... $ (region of height $\delta^{2}(\log A(\chi))(1+c_3(\log A(\chi))^{1/2})$ as printed; OCR garbled) for some $\delta$ with $(c_2\log A(\chi))^{-1}\le\delta\le 1/2$, and $\zeta_K$ has no zero on $[1-\delta,1]$, then there is a prime ideal $P$ of degree 1 over $\mathbb{Q}$ with $\chi(P)\neq1$ and $N_{K/\mathbb{Q}}P<(A_2\,\delta^{-1}\log A(\chi))^{1/\delta}$ (exact form of last bound garbled). Here $A(\chi)=d_KN_{K/\mathbb{Q}}f(\chi)$. *Conditional on:* zero-free region of the stated shape.
- **THM-PAPER-0067-3** (Corollary 1.3, corollary, scope: conditional; Sec.1, (1.4)-(1.5), p.273). There is an absolute effective constant $A_3$ such that for every number field $K$ and Hecke character $\chi$ of $K$, if $\zeta_K(s)L(s,\chi,K)$ has no zeros $\rho=\beta+i\gamma$ in the region $\tfrac12<\beta<1$ (written 1/2<beta<1, with |gamma| bounded as in Thm 1.2 at delta=1/2; OCR garbled), then there is a degree-1 prime $P$ with $\chi(P)\ne1$ and $N_{K/\mathbb{Q}}P<A_3(\log A(\chi))^2$. (K=Q: Ankeny.)
- **THM-PAPER-0067-4** (Theorem 5.1 (Deuring-Heilbronn phenomenon), theorem, scope: global; Sec.5, (5.1), p.289). There are absolute effective constants $c_7,c_8>0$ such that if $\zeta_L(s)$ has a real zero $\beta_0>0$ then $\zeta_L(\sigma+it)\ne0$ for $\sigma>1-c_8\,\log\!\big(c_7 d_L^{-1}... /\log\tau...\big)/\log d_L\tau^{n_L}$ with $\tau=|t|+2$, apart from $\sigma+it=\beta_0$ (displayed bound garbled in OCR).
- **THM-PAPER-0067-5** (Corollary 5.2, corollary, scope: global; Sec.5, p.290). There is an absolute effective constant $c_{10}$ such that any real zero $\beta_0$ of $\zeta_L(s)$ satisfies $1-\beta_0>d_L^{-c_{10}}$.
- **THM-PAPER-0067-6** (Theorem 1.4, theorem (sketched), scope: global; Sec.1, p.274; proof sketched in Sec.7). There are absolute effective constants $A_4,A_5$ such that if $L\ne\mathbb{Q}$ and $x>\exp\{A_4(\log d_L)(\log\log d_L)(\log\log\log d_L^{e^{2}})\}$ (OCR garbled), then $\pi_C(x)\le A_5\frac{|C|}{|G|}\mathrm{Li}(x)$.
- **THM-PAPER-0067-7** (Theorem 4.2 (power-sum inequality), theorem, scope: finite; Sec.4, p.288-289). Let $s_j=\sum_{n\ge1}b_nz_n^j$ with (i) $|z_n|<|z_1|$ for all $n>1$, (ii) $b_n$ real, (iii) $b_n\ge0$ for those $n$ with $\tfrac13|z_1|<|z_n|<\ldots$ (as printed). Set $L=(b_1|z_1|)^{-1}\sum_n|b_nz_n|$. Then there exists $j_0$ with $1\le j_0\le 24L$ such that $\mathrm{Re}\,s_{j_0}>\tfrac{b_1}{8}|z_1|^{j_0}$ (fraction printed ambiguously).

### Key definitions

- A(chi)=d_K N f(chi)
- Artin symbol [L/K, P]
- pi_C(x)
- exceptional zero
- kernel k(s;x,y)

### Principal lemmas

- **THM-PAPER-0067-L1** (Lemma 2.1 ([LO77, Lemma 5.4]); Sec.2, (2.8)). The number $n_\chi(T)$ of zeros $\rho=\beta+i\gamma$ of $L(s,\chi,K)$ with $0<\beta<1$, $|\gamma-T|<1$ is $\ll \log A(\chi)+n_K\log(|T|+2)$. — *Role:* zero density (local count) used throughout
- **THM-PAPER-0067-L2** (Lemma 2.2; Sec.2, (2.11)). For $\mathrm{Re}(s)>1$ and $r>0$, $n(r;s)\ll 1+r(\log A(\chi)+n_K\log(|s|+2))$ for the number of zeros within r of s. — *Role:* counts zeros near 1 for small radii
- **THM-PAPER-0067-L3** (Lemma 2.3; Sec.2, p.277). There is an absolute effective constant $c_2$ such that $L(s,\chi,K)$ has at most one zero $\rho=\beta+i\gamma$ with $\beta>1-(c_2\log A(\chi))^{-1}$, $|\gamma|<(c_2\log A(\chi))^{-1}$; it can occur only if $\chi^2=\chi_0$, is real and simple (exceptional zero), and apart from it no zero has $\beta>1-c_2\{\log A(\chi)+n_K\log(|\gamma|+2)\}^{-1}$. — *Role:* zero-free region with exceptional zero; the only input about zeros besides density
- **THM-PAPER-0067-L4** (Lemma 3.1, 3.2, 3.3; Sec.3, p.285-287). Estimates for ramified prime contributions and for prime powers of non-rational-prime norm in the Mellin sum expressing the Artin-symbol-weighted prime count through Hecke L-functions (Artin L eliminated). — *Role:* reduction of Artin L-function sums to Hecke L-functions
- **THM-PAPER-0067-L5** (Lemma 4.1; Sec.4, p.288). With $P(r,\theta)=\sum_{j\ge1}(1-j/J)r^j\cos j\theta$ type Fejer-kernel sums: (i) $P>-1/2$ for $0\le r\le1$, (ii) $P(1,\theta)=J/2$-type value, (iii) $|P(r,\theta)|<3r$ for small r (OCR garbled). — *Role:* ingredient for Theorem 4.2

### Proof architecture

Theorem 1.2 first (cleaner): sum $\sum \chi(P)\Lambda(P)(NP)^{-s}$ against a kernel k(s;x,y) whose inverse Mellin transform f(u) is supported on x^2<u<y^2 and weights small norms strongly. Contour shift gives Sum = -sum over zeros of k(rho;x,y); real zeros give a sign-definite term and are dropped; non-real zeros are bounded using Lemma 2.1 and Lemma 2.2. If chi(P)=1 for all P with small norm, the left side is instead the same sum with zeta_K, which is large because of the pole at s=1 unless there is an exceptional zero; contradiction. For Theorem 1.1: Sec.3 writes the Artin-class prime counting function as a sum of Hecke L-function logarithmic derivatives over a cyclic-subgroup reduction (Lemmas 3.1-3.3); two kernels are used, one when zeta_L has no real zero in [1-(log d_L)^{-2},1], and one when it does. The exceptional zero case uses the Deuring-Heilbronn repulsion (Thm 5.1, proved via the Hadamard product, Thm 4.2 power-sum inequality and differentiation in s), which says other zeros are pushed away from 1 when a real zero beta_0 exists; Cor 5.2 bounds 1-beta_0 below by d_L^{-c10}. Sec.6 gives the final lower bounds. Sec.7 sketches the upper bound Thm 1.4 with Gaussian-type kernel k(s)=x^{s^2}.

Dependency edges: CAND-00332 → Lagarias-Odlyzko 1977 Effective versions of Chebotarev (uses lemmas); CAND-00332 → Deuring-Heilbronn phenomenon (proves general version for zeta_L)

**Imported results.** Lagarias-Odlyzko 1977, Effective versions of the Chebotarev density theorem (Lemma 5.4, 5.6, constants, Hecke L-function facts); Linnik's theorem (comparison only); Stark's exceptional zero bounds (comparison); Ankeny (K=Q case of Cor 1.3)

**Techniques.** Mellin transform with kernel weighting small prime ideals; power-sum (Turan-type) inequality via Fejer kernel; Deuring-Heilbronn zero-repulsion; Hadamard product and its derivatives at real s; reduction of Artin L-functions to Hecke L-functions; zero counting (Lemmas 2.1-2.2)

## Context and interpretation

**Importance and obstacle overcome.** First unconditional polynomial bound d_L^{A1} for the least prime in a Chebotarev class, valid for all number fields, without zero-density estimates. Obstacle: the possible exceptional zero of zeta_L, handled by a new Deuring-Heilbronn type theorem proved with a Turan-style power-sum inequality that avoids Turan's second main theorem. Authors note the exponent is probably the best attainable for K=Q, L=Q(sqrt D), since it would give a bound on the least quadratic non-residue.

**Relation to prior work.** Complements Lagarias-Odlyzko (1977) GRH bound (log d_L)^2; improves nothing in Linnik's theorem; uses the kernels related to Guinand-Weil explicit formulas; Ankeny's result (K=Q, GRH-like) generalized as Cor 1.3.

**Limitations and open questions.** Constant A1 not made explicit here (later work, e.g. Ahn-Kwon, Zaman, gives explicit values); does not prove a lower bound pi_C(x)>= (|C|/|G|)Li(x)(1-eps) for x>2 d_L^{A} (stated impossible with these techniques); what zero-free region suffices for the log^2 bound (1.5) is open (they only know it for no zeros in 1/2<beta<1, |gamma|<=log log A or similar).

## Research potential

- **Hypotheses that might be weakened.** In Theorem 1.2 the height of the zero-free region |gamma|<delta^2 log A(chi)(...) is the hypothesis to optimize; the authors remark (1.5) holds with only |gamma|<~ log log A(chi) using kernel Gamma(s)x^s, and leave open whether a box 1/2<beta<1, |gamma|<1/2 suffices.
- **Generalizations.** Replace conjugacy class by Artin-symbol conditions in non-Galois settings; other L-functions with Dirichlet series over primes (automorphic least-prime problems).
- **Candidate connections.** Zero-repulsion plus kernel positivity is a template for effective Linnik-type statements and for unconditional power savings in explicit formulas; Theorem 4.2 is a reusable substitute for Turan's second main theorem in any Dirichlet series with positive coefficients at real points.
- **Reusable lemmas.** Theorem 4.2 (power-sum inequality), Theorem 5.1 (Deuring-Heilbronn for zeta_L of arbitrary number fields), Lemma 2.3 zero-free region for Hecke L.
- **Possible experiments.** Verify the inequality of Theorem 4.2 numerically with random z_n, b_n to get a sharp constant in place of 24 and 1/8 (supplied by OCR ambiguity), and test its effect on c8 in Thm 5.1.
- **Risks / barriers.** Exponent A1 limited by the least quadratic non-residue barrier; improving requires zero-density estimates (Linnik).

## Audit notes (Level 1 reader)

OCR of a third-party mirror has many garbled formulas (Thm 1.2's region, Thm 5.1's displayed exponent, Thm 4.2 constants, Thm 1.4's range). Statements above flag these; a clean check against the publisher version is needed before quoting. No genuine math error noticed in inspected portion.

*These notes are a reader's observations, not verified findings; see `audits/` for adjudicated findings.*

## Provenance

- Candidate `CAND-00332`; harvest queries: kw_GRH, kw_RH_any, kw_zero_free, citation_expansion.
- Triage decision: include — Lagarias-Montgomery effective Chebotarev with zero-density machinery.
- Record generated by `tools/make_records.py`; search cutoff 2026-11-17.
