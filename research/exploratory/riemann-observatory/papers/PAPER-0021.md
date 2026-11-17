# PAPER-0021 — Applications of the \(L\)-functions ratios conjectures

| Field | Value |
|---|---|
| Authors | Conrey, J. B.; Snaith, N. C. |
| Year / stratum | 2007 / S5 |
| Venue | Proc. Lond. Math. Soc. (3) 94, No. 3, 594-646 (2007). |
| Identifiers | zbMATH [1183.11050](https://zbmath.org/?q=an:1183.11050) · DOI [10.1112/plms/pdl021](https://doi.org/10.1112/plms/pdl021) · arXiv [math/0509480](https://arxiv.org/abs/math/0509480) |
| MSC | 11M26, 11M06, 11M50, 11M41, 22C05 |
| Families | B, E |
| Work type | original_paper |
| Evidence level of this record | **L1-partial** |
| Full text | partial_fulltext — https://arxiv.org/abs/math/0509480 |
| Selection | score 4.6055, in-pool citations 66, seed lists 1, triage relevance 4 |

## Mathematical content (Level 1: full text read)

**Research question.** Assuming (and treating as black boxes) the Conrey-Farmer-Zirnbauer ratios conjectures for averages of ratios of shifted L-functions, derive explicit formulas, including all lower-order terms, for one-level density, pair correlation of zeta zeros, mollified second moments, mollified 4th moment, and discrete moments over zeros. Throughout, RH is assumed for all L-functions involved.

**Historical motivation.** Montgomery-Odlyzko pair correlation showed leading-order GUE agreement but Bogomolny-Keating found arithmetic lower-order terms; mollified moments (Selberg, Levinson) required fifty-page computations; Farmer's ratios conjecture and CFZ made these computations routine.

### Main results

- **THM-PAPER-0021-1** (Conjecture 2.1, conjecture (ratios conjecture, zeta, from CFZ), scope: conditional; Sec 2.1, eq (2.10)-(2.11), p.6). For $s=1/2+it$ and shifts obeying (2.11): $\int_0^T \frac{\zeta(s+\alpha)\zeta(1-s+\beta)}{\zeta(s+\gamma)\zeta(1-s+\delta)}dt=\int_0^T\Big[\frac{\zeta(1+\alpha+\beta)\zeta(1+\gamma+\delta)}{\zeta(1+\alpha+\delta)\zeta(1+\beta+\gamma)}A_\zeta(\alpha,\beta,\gamma,\delta)+\Big(\frac{t}{2\pi}\Big)^{-\alpha-\beta}\frac{\zeta(1-\alpha-\beta)\zeta(1+\gamma+\delta)}{\zeta(1-\beta+\delta)\zeta(1-\alpha+\gamma)}A_\zeta(-\beta,-\alpha,\gamma,\delta)\Big]dt+O(T^{1/2+\epsilon})$, with $-1/4<\Re\alpha<1/4$, $1/\log T\ll\Re\delta<1/4$, $\Im\alpha,\Im\delta\ll_\epsilon T^{1-\epsilon}$ (same constraints on all numerator/denominator shifts), error believed uniform so that it may be differentiated in the parameters (Remark 2.4). *Conditional on:* Ratios Conjecture 2.1.
- **THM-PAPER-0021-2** (Conjectures 2.6, 2.8, 2.9, 2.11, conjecture, scope: conditional; Sec 2.2-2.3, p.7-13 (conjecture statements located at text lines ~421, 526, 707, 789)). Analogous ratios conjectures for the symplectic family of $L(s,\chi_d)$ (real quadratic characters), and orthogonal families (twists of the Ramanujan tau L-function; Conj. 2.8 and 2.11 are the second-moment-type versions with $\alpha,\beta,\gamma,\delta\ll 1/\log X$), averaged over $d<X$, with error $O(X^{1/2+\epsilon})$ under the same shift constraints (2.11) with $C=X$. *Conditional on:* CFZ ratios conjectures for symplectic and orthogonal families.
- **THM-PAPER-0021-3** (Theorem 3.1, theorem (conditional), scope: conditional; Sec 3, eq (3.10), p.15). Assuming Conjecture 2.6 and $f$ even satisfying (3.1), the one-level density of zeros $\gamma_d$ of $L(1/2+s,\chi_d)$ over $d\le X$ is $\sum_{d\le X}\sum_{\gamma_d}f(\gamma_d)=\frac1{2\pi}\int_{-\infty}^{\infty}f(t)\sum_{d\le X}\Big(\log\frac d\pi+\frac12\frac{\Gamma'}{\Gamma}(\tfrac14+\tfrac{it}2)+\frac12\frac{\Gamma'}{\Gamma}(\tfrac14-\tfrac{it}2)+2\frac{\zeta'}{\zeta}(1+2it)+A_D'(it;it)-(\tfrac d\pi)^{-it}\frac{\Gamma(1/4-it/2)}{\Gamma(1/4+it/2)}\zeta(1-2it)A_D(-it;it)\Big)dt+O(X^{1/2+\epsilon})$ (as printed, up to extraction of constants). Theorem 3.2 is the orthogonal (tau-twist) analogue from Conj. 2.9. *Conditional on:* Conjecture 2.6.
- **THM-PAPER-0021-4** (Theorem 4.1, theorem (conditional), scope: conditional; Sec 4, eq (4.25), p.20). Assuming Conjecture 2.1 and $f$ as in (3.1): $\sum_{\gamma,\gamma'\le T}f(\gamma-\gamma')=\frac1{(2\pi)^2}\int_0^T\int_{-T}^{T}\Big[2\pi f(0)\log\frac t{2\pi}+f(r)\Big(\log^2\frac t{2\pi}+2\big(\tfrac{\zeta'}\zeta\big)'(1+ir)+\big(\tfrac t{2\pi}\big)^{-ir}\zeta(1-ir)\zeta(1+ir)A(ir)-B(ir)\Big)\Big]dr\,dt+O(T^{1/2+\epsilon})$ (principal value near $r=0$), giving all lower-order arithmetic terms of pair correlation (recovering Bogomolny-Keating). *Conditional on:* Conjecture 2.1, RH.
- **THM-PAPER-0021-5** (Theorems 5.1, 5.2, 5.3, theorem (conditional), scope: conditional; Sec 5, eq (5.22), p.25; Thms 5.2 (p.~29), 5.3 (p.~33)). Theorem 5.1 (unitary): with $P_1(0)=P_2(0)=0$, mollifier $M(s,P)$ of length $T^\theta$, assuming Conj. 2.1, $\frac1T\int_0^T Q_1(\tfrac{-1}{\log T}\tfrac d{d\alpha})Q_2(\tfrac{-1}{\log T}\tfrac d{d\beta})\zeta(s+\alpha)\zeta(1-s+\beta)M(s,P_1)M(1-s,P_2)dt|_{\alpha=\beta=0}=P_1(1)P_2(1)Q_1(0)Q_2(0)+\frac1\theta\,[\ldots]\int_0^1\!\!\int_0^1 P_1(w+r)P_2(z+r)Q_1(w\theta+u)Q_2(z\theta+u)\,dr\,du\big|_{w=z=0}+O(1/\log T)$ (Levinson/Conrey-type mollified second moment for any $\theta>0$). Thms 5.2 and 5.3 give the symplectic ($L(s,\chi_d)$, from Conj. 2.8) and orthogonal analogues for even polynomials. *Conditional on:* Conj. 2.1, 2.8, 2.11 respectively.
- **THM-PAPER-0021-6** (Theorems 6.1, 6.4, theorem (conditional), scope: conditional; Sec 6, eq (6.26) p.~38; Thm 6.4 eq (6.38) p.~40). Theorem 6.1: assuming the 4th-moment ratios conjecture (6.8) and polynomials $P,Q$ vanishing to order 4 at 0, for any $\theta>0$: $\frac1T\int_0^T|\zeta(1/2+it)|^4M_2(1/2+it,Q)M_2(1/2-it,P)dt=P(1)Q(1)+\frac1\theta\int_0^1\frac{(1-\eta)^3}{6}\big[2(Q^{(4)}P'+Q'P^{(4)})+8(Q^{(3)}P''+Q''P^{(3)})+\tfrac2\theta(Q^{(4)}P''+Q''P^{(4)})+\tfrac4\theta Q^{(3)}P^{(3)}+\tfrac{2}{\theta^2}(Q^{(4)}P^{(3)}+Q^{(3)}P^{(4)})+\tfrac1{\theta^3}Q^{(4)}P^{(4)}\big]d\eta+O(1/\log T)$ (coefficients as printed; extraction ambiguous). Theorem 6.4 treats the third-power mollification $I_3$ with two mollifier lengths $\theta_1,\theta_2$. *Conditional on:* ratios conjecture (6.8) for 2 zetas over 2 zetas... generalized 4-over-4 setting.
- **THM-PAPER-0021-7** (Theorem 7.3, theorem (conditional), scope: conditional; Sec 7.1, eq (7.19), p.45). Assuming the ratios conjecture (7.11): $\sum_{\gamma<T}|\zeta'(\rho)|^2=\int_0^T\frac1{24\pi}\log^4\frac t{2\pi}+\frac\gamma{3\pi}\log^3\frac t{2\pi}+\dots(1+O(t^{-1/2+\epsilon}))dt=\frac T{24\pi}\log^4T+O(T\log^3T)$, with full lower-order polynomial in $\log(t/2\pi)$ with coefficients in Euler's $\gamma$ and Stieltjes constants $\gamma_1,\gamma_2,\gamma_3$; leading term agrees with Gonek's theorem (7.1) (RH-conditional). *Conditional on:* ratios conjecture (7.11), RH.
- **THM-PAPER-0021-8** (Theorem 7.6, theorem (conditional), scope: conditional; Sec 7.2, p.49). Assuming ratios conjecture (7.28): there are constants $C_0,\dots,C_6$ such that $\sum_{\gamma<T}|\zeta'(\rho)|^4=\frac1{2\pi}\int_0^T\Big[\frac{\log^9\frac t{2\pi}}{8640\zeta(2)}-\frac{(-2\gamma\zeta(2)+\zeta'(2))\log^8\frac t{2\pi}}{480\zeta^2(2)}+\dots+C_6\log^6\frac t{2\pi}\ldots\Big]dt$ (full lower-order structure given; the paper gives explicit $\log^9,\log^8,\log^7$ coefficients). Theorem 7.7 (Fujii) is an imported RH-conditional lower-order result for comparison. *Conditional on:* ratios conjecture (7.28), RH.

### Key definitions

- $R_\zeta(\alpha,\beta,\gamma,\delta)=\int_0^T\frac{\zeta(s+\alpha)\zeta(1-s+\beta)}{\zeta(s+\gamma)\zeta(1-s+\delta)}dt$
- Arithmetic factor $A_\zeta$ (2.8): absolutely convergent Euler product near 0
- Shift constraints (2.11a-c)
- Mollifier $M(s,P)=\sum_{n\le y} \mu(n)n^{-s}P(\log(y/n)/\log y)$ (length $y=T^\theta$)

### Principal lemmas

- **THM-PAPER-0021-L1** (Theorem 2.5 / 2.7 / 2.10; Sec 2, p.7-13). Differentiation in the shifts of Conj. 2.1 (resp. 2.6, 2.9) yields formulas for $\int \frac{\zeta'}{\zeta}(s+\alpha)\frac{\zeta'}{\zeta}(1-s+\beta)dt$ and one-level auxiliary sums; (2.12) equals $\int_0^T(\zeta'/\zeta)'(1+\alpha+\beta)+(t/2\pi)^{-\alpha-\beta}\zeta(1+\alpha+\beta)\zeta(1-\alpha-\beta)A(\alpha,\beta)-B(\alpha,\beta)\,dt+O(T^{1/2+\epsilon})$. — *Role:* Bridge from the conjecture to pair correlation and one-level density; relies on Remark 2.4 (differentiability of the conjectured error).
- **THM-PAPER-0021-L2** (Remark 2.2-2.4; p.6). The condition $\Re\delta\gg 1/\log C$ can be relaxed if each denominator shift tending to 0 is matched by a numerator shift tending to 0 at same rate; bound $1/4$ on real parts prevents divergence of Euler products; uniformity allows differentiation. — *Role:* Domain/validity hypotheses of the conjecture used in every application.
- **THM-PAPER-0021-L3** (Recipe (Sec 2.1, (2.3)-(2.10)); Sec 2.1, p.4-6). Approximate functional equation $\zeta(s)=\sum_{n\le X}n^{-s}+\chi(s)\sum_{n\le Y}n^{s-1}$, $XY=t/2\pi$; use Dirichlet series for numerators, Moebius series for denominators, keep only terms with equal numbers of $\chi(s)$ and $\chi(1-s)$ factors, retain diagonal terms, extend sums, factor out zeta's as arithmetic factor $A_\zeta$. — *Role:* Heuristic derivation of the ratios conjecture.

### Proof architecture

Not a proof paper: every result is a formal consequence of the ratios conjectures (Conj 2.1, 2.6, 2.8, 2.9, 2.11, and generalized versions in Sec 5-7). Pattern: (i) state ratios conjecture for needed shifts; (ii) differentiate or specialize shifts (legitimate by uniformity assumption); (iii) express target (zero sums via contour integral of log-derivative, mollified moments via Dirichlet-polynomial mollifier terms rewritten as ratios, discrete moments via residue sums); (iv) evaluate by residues / contour shifts, obtaining main term plus lower order terms and error $O(T^{1/2+\epsilon})$ or $O(X^{1/2+\epsilon})$. Random matrix analogues serve as consistency checks. Section 8 reproduces non-vanishing asymptotics for Dirichlet, automorphic and quadratic L-functions.

**Imported results.** Conrey-Farmer-Zirnbauer ratios conjectures [11,12] (conjectural input); Farmer's initial conjecture [16] on $R_\zeta$; Montgomery pair correlation [36]; Bogomolny-Keating lower-order terms [3]; Gonek's mean square $\sum|\zeta'(\rho)|^2$ (7.1); Fujii (Thm 7.7); Levinson/Conrey mollified second moment (for comparison); Hughes-Keating-O'Connell Conjectures 7.1/7.2

**Techniques.** Ratios conjecture recipe (approximate functional equation, diagonal retention); Differentiation of conjectured formula in shifts; Contour integration/residue calculus for zero sums; Mollifier algebra as ratios of zeta products; Comparison with RMT averages of ratios of characteristic polynomials; Taylor expansions in Stieltjes constants for discrete moments

## Context and interpretation

**Importance and obstacle overcome.** Shows that one unified conjectural input (ratios conjecture) reproduces known hard theorems (Levinson mollified 2nd moment, Bogomolny-Keating pair correlation terms, Gonek's discrete moment) and gives new predictions (mollified 4th moment, lower order terms for sums over $|\zeta'(\rho)|^{2,4}$). Obstacle overcome: the Hardy-Littlewood prime-pair analysis and lengthy mollifier calculations are avoided. Also gives a heuristic for 100% non-vanishing of $L^{(k)}(1/2,\chi)$ as $k\to\infty$.

**Relation to prior work.** Applies CFZ ratios conjectures; extends Farmer's conjecture; recovers Bogomolny-Keating (2-pt), Levinson, Conrey-Iwaniec-Soundararajan style mollification asymptotics, Gonek (|zeta'(rho)|^2) and Fujii; companion to CFZ 'Autocorrelation of ratios' (CAND-01203) and Conrey-Snaith n-correlation (CAND-01253).

**Limitations and open questions.** Everything is conditional on unproved conjectures and on RH; no rigorous proof of the ratios conjectures for zeta; the error terms $O(T^{1/2+\epsilon})$ are conjectural; the paper notes some results could be made theorems by other methods, others purely conjectural (e.g. mollified 4th moment, third power mollifier). Lack of RMT analogue for mollification.

**Ideas in remarks/appendices/abandoned paths.** Sec 8 remark that mollifying higher powers might push non-vanishing of $\Lambda^{(k)}(1/2,\chi)$ beyond 2/3; the remark (intro) that mollification has no obvious RMT analogue since nothing corresponds to a partial Dirichlet series (p.4); Sec 6.1 third-power mollification.

## Research potential

- **Hypotheses that might be weakened.** Uniformity range (2.11b) $\Re\delta\gg1/\log C$ and the claim that error remains $O(T^{1/2+\epsilon})$ after differentiation (Remark 2.4); the test-function condition (3.1) in Theorems 3.1/4.1; one could test how far these can be relaxed numerically.
- **Generalizations.** Other families (GL(n), Maass, elliptic curve L-functions) and mollifiers of higher powers than 2 (Theorem 6.1/6.4 structure) to see whether non-vanishing proportion beyond 2/3 for $\Lambda^{(k)}$ is attainable; connection to proportion of zeros on the critical line via Levinson-type argument.
- **Candidate connections.** Mollified 4th moment (Thm 6.1) with $\theta$-dependence could be compared to known lower bounds for proportion of simple/critical zeros; formulas (7.19), (7.28) could be checked against Hughes-Keating-O'Connell RMT for $|Z'|^{2k}$.
- **Reusable lemmas.** Theorem 2.5 (differentiated pair-ratio formula) and the mollifier-to-ratio translation (5.1-5.2) are reusable; the explicit residue evaluation giving $\sum|\zeta'(\rho)|^2$ with Stieltjes constants.
- **Possible experiments.** Numerically evaluate (7.19) and Theorem 7.6 on Odlyzko zeros around $10^{22}$ and compare lower-order corrections; test Theorem 5.1 with $\theta>1/2$ using high zeros and mollifier of length $T^{\theta}$; check Conj 2.1 numerically for small shifts via direct integration of zeta ratios.
- **Risks / barriers.** Ratios conjecture is not provable with current technology and conjectural formulas conditional on RH cannot yield unconditional information on zeros; the heuristic discards off-diagonal terms with no rigorous control; extrapolation to mollifiers beyond $\theta=1/2$ is untested.

## Audit notes (Level 1 reader)

none noticed in inspected portion (text extraction garbles some formulas, e.g., coefficients in (3.10), (6.26); my transcriptions of these are approximate; section 8 and derivation of conjectures 2.6-2.11 not read in detail).

*These notes are a reader's observations, not verified findings; see `audits/` for adjudicated findings.*

## Provenance

- Candidate `CAND-01202`; harvest queries: kw_RH_any, kw_pair_correlation, kw_zeta_zeros, msc_11M06, msc_11M26, msc_11M50, arxiv_mollifier, arxiv_zeta_zeros.
- Triage decision: include — Key applications paper for the ratios conjectures (zero statistics, mollified moments).
- Record generated by `tools/make_records.py`; search cutoff 2026-11-17.
