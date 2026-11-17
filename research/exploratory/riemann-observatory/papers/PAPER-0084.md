# PAPER-0084 — On Montgomery's pair correlation conjecture: a tale of three integrals

| Field | Value |
|---|---|
| Authors | Carneiro, Emanuel; Chandee, Vorrapan; Chirre, Andrés; Milinovich, Micah B. |
| Year / stratum | 2022 / S6 |
| Venue | J. Reine Angew. Math. 786, 205-243 (2022). |
| Identifiers | zbMATH [1494.11073](https://zbmath.org/?q=an:1494.11073) · DOI [10.1515/crelle-2021-0084](https://doi.org/10.1515/crelle-2021-0084) · arXiv [2108.09258](https://arxiv.org/abs/2108.09258) |
| MSC | 11M06, 11N05 |
| Families | B |
| Work type | original_paper |
| Evidence level of this record | **L1-partial** |
| Full text | partial_fulltext — https://arxiv.org/abs/2108.09258 |
| Selection | score 4.4205, in-pool citations 7, seed lists 0, triage relevance 4 |

## Mathematical content (Level 1: full text read)

**Research question.** Under RH, quantify how close one can prove the three integrals equivalent to Montgomery's pair correlation conjecture are to their conjectured asymptotics: (I) integral of F(alpha,T) over [b,b+l], (II) Selberg's J(beta,T) for variance of primes in short intervals, (III) I(a,T), the second moment of zeta'/zeta near the critical line. Method: reduce to Fourier extremal problems (Beurling-Selberg type), including sharp embedding between Hilbert spaces of entire functions.

**Historical motivation.** Montgomery's pair correlation conjecture is equivalent to asymptotics for F(alpha,T) on bounded intervals beyond alpha=1, for Selberg's J(beta,T) beyond beta=1, and for I(a,T). Under RH only O-bounds with poorly controlled constants were known (Goldston; Goldston-Gonek; Goldston-Gonek-Montgomery). This paper systematizes bounds as Fourier optimization problems, in the spirit of earlier work on |zeta| and arg zeta bounds via Beurling-Selberg.

### Main results

- **THM-PAPER-0084-1** (Theorem 1 / Corollary 2, theorem (conditional on RH), scope: asymptotic; Section 1.3.1, p.3; Section 2.4 (C+ in 2.52, C- in 2.57)). Assume RH, $b\ge1$, $\varepsilon>0$. For large $\ell$, as $T\to\infty$: $(C^--\varepsilon)\ell+o(1)\le\int_b^{b+\ell}F(\alpha,T)\,d\alpha\le(C^++\varepsilon)\ell+o(1)$, with $C^\pm$ defined by extremal problems (2.52), (2.57) and $0.9278<C^-\le C^+<1.3302$. Corollary 2: $0.9278\,\ell+o(1)\le\int_b^{b+\ell}F\,d\alpha\le1.3302\,\ell+o(1)$. Previous best constants 1/3 (lower) and 2 (upper) (Goldston; Goldston-Gonek). Conjectured value is $\ell+o(1)$.
- **THM-PAPER-0084-2** (Theorem 7, theorem (conditional on RH; general bound), scope: asymptotic; Section 2.1.2, p.8; defs in Section 2.1 (2.1)-(2.10)). Assume RH, $b\in\mathbb R$, $\ell>0$. As $T\to\infty$: $W^-(\ell)+o(1)\le W^-_*(b,b+\ell)+o(1)\le\int_b^{b+\ell}F(\alpha,T)\,d\alpha\le W^+(\ell)+o(1)$, where $W^+(\ell)$ is the infimum of $\sum_j\rho(g_j)$ over finite families $g_j\in\mathcal A,\xi_j\in\mathbb R$ with $\sum_j\hat g_j(\alpha-\xi_j)\ge\chi_{[0,\ell]}(\alpha)$ (EP1), $W^-$ the supremum of $\sum_j(2g_j(0)-\rho(g_j))$ over families with $\sum_j\hat g_j(\alpha-\xi_j)\le\chi_{[0,\ell]}(\alpha)$ (EP2), $W^-_*$ the supremum in EP3. Here $\mathcal A$ = continuous even nonnegative $g\in L^1$ with $\hat g(\alpha)\le0$ for $|\alpha|\ge1$, and $\rho(g)=\hat g(0)+\int_{-1}^1\hat g(\alpha)|\alpha|\,d\alpha$.
- **THM-PAPER-0084-3** (Theorem 9 (Triangle bounds), theorem (conditional on RH), scope: asymptotic; Section 2.3.1, p.~12). Assume RH, $b\ge1$, $\ell>0$. Then $C_N^-(\ell)+o(1)\le\int_b^{b+\ell}F\le C_N^+(\ell)+o(1)$ with explicit $C_N^\pm$; for $\ell\ge1$ the upper bound is $C_N^+(\ell)=\frac43(\ell+1)+\frac{\{\ell\}^3}{12}-\frac{\{\ell\}}{3}-\frac14(1-\{\ell\}-\{\ell\}^2)_+$ (as transcribed, one branch shown). In particular $W^-(\ell)>0$ for $\ell>6-2\sqrt6=1.10102\dots$. Uses the Fejer (triangle) test function and shows $W^+\le 4\ell/3+O(1)$.
- **THM-PAPER-0084-4** (Theorem 10 / Corollary 11, theorem (conditional on RH), scope: asymptotic; Section 2.3.2, pp.~14-16 (2.38)-(2.49)). Assume RH, $\beta>1$, $c_0=\min_{x}\sin x/x=-0.21723\dots$. Then $C^-(1,\beta)+o(1)\le\int_1^\beta F\le C^+(1,\beta)+o(1)$ with $C^+(1,\beta)=C_N^+(2\beta)/2-1$ and $C^-(1,\beta)=\max_nG_n(\beta)\ge(1+c_0/3)(\{\beta\}-1)-(\pi+1)/3$. Corollary 11 combines to $C^\pm(b,\beta)$ via $C^-(b,\beta)=\max\{C_N^-(\ell),C^-(1,\beta)-C^+(1,b)\}$ and $C^+(b,\beta)=\min\{C_N^+(\ell),C^+(1,\beta)-C^-(1,b)\}$. The constant $1+c_0/3=0.92758\dots$ (eq. 1.9) is the lower-bound mechanism: Dirichlet kernels cannot be too negative.
- **THM-PAPER-0084-5** (Theorem 3 / Corollary 4 / Theorem 14, theorem (conditional on RH), scope: asymptotic; Section 1.3.2, p.4; Section 3.3 Thm 14, Cor 15). Assume RH, $\varepsilon>0$. For large $\beta$: $\big((L^-C^--\varepsilon)\beta+o(1)\big)\frac{\log^2T}{T}\le J(\beta,T)\le\big((L^+C^++\varepsilon)\beta+o(1)\big)\frac{\log^2T}{T}$, with $L^-=0.9028\dots$, $L^+=1.0736\dots$ (Fejer-kernel 'sunrise' constants, (3.1),(3.2)); Corollary 4: $0.8376\,\beta\le\cdot\le1.4283\,\beta$ (previous 0.153 and 10.824). Theorem 14 (Tauberian step): for $\beta>b>0$, $L^-\lim_{\varepsilon\to0^+}\liminf_\tau\int_{b+\varepsilon}^{\beta-\varepsilon}F(\alpha,\tau)d\alpha\cdot\frac{\log^2T}{T}\le J(\beta,T)-J(b,T)\le L^+\lim\limsup\int_{b-\varepsilon}^{\beta+\varepsilon}F\cdot\frac{\log^2T}{T}$. Here $J(\beta,T)=\int_1^{T^\beta}(\psi(x+x/T)-\psi(x)-x/T)^2x^{-2}dx$.
- **THM-PAPER-0084-6** (Theorem 5, theorem (conditional on RH), scope: asymptotic; Section 1.3.3, p.5; proof Section 4). Assume RH. For $T^{-1}(\log T)^{5/2}\le a\le(\log T)^{1/4}/(\log\log T)^{1/2}$: $(1+o(1))U^-(a)\,T\log^2T\le I(a,T)\le(1+o(1))U^+(a)\,T\log^2T$, with $U^-(a)=\frac{1-(1+2a)e^{-2a}}{4a^2}+\big(\frac1{2a}+\frac1{\sqrt3}\big)e^{-2a(1+1/\sqrt3)}$ and $U^+(a)=\frac{\coth a(\operatorname{csch}a)^2}{4a^2}-\frac{\coth a}{4a}+\frac{\coth a}{2}-\frac12$ ($o(1)=O(1/\sqrt{\log\log T})$). With $G^\pm(a)=U^\pm(a)\big/\frac{1-e^{-2a}}{4a^2}$: $G^-(0^+)=1$, $G^+(0^+)=4/3$, $\min G^-=0.899\dots$ at $a=0.998\dots$, $\max G^+=1.434\dots$ at $a=0.620\dots$, both tending to 1 rapidly; improves Goldston-Gonek-Montgomery $V^\pm$. Here $I(a,T)=\int_1^T|\frac{\zeta'}{\zeta}(\frac12+\frac a{\log T}+it)|^2dt$.
- **THM-PAPER-0084-7** (Theorem 19 (Appendix B), theorem (unconditional, pure analysis), scope: global; Section 6.1, p.~38 (statement); Appendix B). Let $\mathcal B_2(\pi)$ be the Paley-Wiener space of entire functions of exponential type $\pi$ in $L^2(\mathbb R)$ and $d\mu$ the pair-correlation measure from (6.1). The sharp embedding constant is $D^2=\inf_{f\in\mathcal B_2(\pi),f\ne0}\|f\|^2_{L^2(d\mu)}/\|f\|_2^2=1-\frac1{2\pi^2\theta^2}=0.3244\dots$ where $0<\theta<\tfrac12$ is the unique root of $(\pi\theta)\tan(\pi\theta)=1$ ($\theta=0.27385\dots$). The extremizer is unique up to scalar: $f(z)=\frac{\sin\pi(z+\theta)}{\pi(z+\theta)}+\frac{\sin\pi(z-\theta)}{\pi(z-\theta)}$.

### Key definitions

- $F(\alpha,T)$ Montgomery form factor with $w(u)=4/(4+u^2)$; $N(\beta,T)$ pair counting function
- $J(\beta,T)$ Selberg short-interval variance integral; $I(a,T)$ log-derivative second moment
- Class $\mathcal A$, subclass $\mathcal A_0$ (supp $\hat g\subset[-1,1]$), functional $\rho(g)$
- Extremal problems EP1-EP5 and constants $W^\pm,W_*^-,C^\pm,L^\pm,U^\pm$
- Montgomery's pair correlation conjecture (I) and equivalent forms (II)-(IV)

### Principal lemmas

- **THM-PAPER-0084-L1** (Proposition 6; Section 2.1.1, pp.7-8). $W^+,W^-,W_*^-$ are non-decreasing in $\ell$; $W^-(\ell)\le W_*^-(b,b+\ell)$; $W^+$ is subadditive and $W^-$ superadditive in $\ell$; $W_*^-(b,d)\ge W_*^-(b,c)+W_*^-(c,d)$. — *Role:* Structural properties used to patch interval estimates and to chain bounds in Corollary 11.
- **THM-PAPER-0084-L2** (Corollary 8; Section 2.1.2, p.9). Assume RH, $\beta>1$: $\frac{W^-_*(-\beta,\beta)}{2}-1+o(1)\le\int_1^\beta F\,d\alpha\le\frac{W^+(2\beta)}2-1+o(1)$, using $\int_{-1}^1F=2+o(1)$ (from 1.6) and evenness of F. — *Role:* Symmetrization giving the b=1 bounds used in Theorem 10.
- **THM-PAPER-0084-L3** (Lemma 16 (Goldston-Gonek-Montgomery); Section 4.1.1, p.~28). Assume RH, $0<a\le\sqrt{\log T}$. Then $I(a,T)=\log T\sum_{0<\gamma,\gamma'\le T}h_{a/\pi}\!\big((\gamma-\gamma')\tfrac{\log T}{2\pi}\big)w(\gamma-\gamma')-\tfrac12\int_1^T\log^2\tfrac t{2\pi}dt+O(\log^4T/a^2)+O(aT\log T)$ with Poisson kernel $h_b(x)=b/(b^2+x^2)$. — *Role:* Converts I(a,T) into a pair-correlation sum, enabling Beurling-Selberg extremal majorants/minorants for the Poisson kernel.
- **THM-PAPER-0084-L4** (Lemma 13 / Lemma 17; Sections 3.2, 4). Auxiliary asymptotic lemmas for the Tauberian step (Lemma 13: continuous nonnegative f(t,eta) << log^2(t+2)) and for I(a,T) (Lemma 17). Statements not extracted in detail. — *Role:* Technical estimates for Theorem 14 and Theorem 5.
- **THM-PAPER-0084-L5** (Proposition 18; Section 6, ~p.40). Explicit bounds for n in N tied to Theorem 19's extremal problem (EP8); statement not extracted in detail. — *Role:* Support for the sharp embedding computation.

### Proof architecture

Section 2: via (1.5), the identity sum_{gamma,gamma'} g(gamma-gamma' scaled) w = (T log T/2pi) integral g-hat(alpha)F(alpha)dalpha, nonnegativity of F and the asymptotic (1.6) on |alpha|<=1 convert upper/lower bounds for integral of F on [b,b+l] into the Fourier-extremal problems EP1 (majorant, supp-constraint g-hat<=0 outside [-1,1], cost rho(g)) and EP2/EP3 (minorants). Feasible test families (Fejer/triangle functions, 'sunrise' approximations, shifted Dirichlet-kernel sums with the observation min sin x/x=-0.2172) give C^- > 0.9278 and C^+ < 1.3302. Section 3: a Tauberian argument with Fejer-type kernels relates J(beta,T) increments to integrals of F, giving Theorem 3 and Theorem 14. Section 4: GGM identity (Lemma 16) writes I(a,T) as a pair sum with Poisson kernel, apply the known Beurling-Selberg extremal majorant/minorant for the Poisson kernel (Carneiro-Littmann et al.) and Montgomery-type theorem to get U^+, and a Carneiro-Chandee-Littmann-Milinovich small-gaps technique to get U^-. Appendix B: sharp Hilbert-space embedding via Paley-Wiener, Krein decomposition and interpolation/variational methods.

**Imported results.** Montgomery 1973 / Goldston-Montgomery 1987 Lemma 8: F(alpha,T)=T^{-2alpha}log T+alpha(1+O(sqrt(loglogT/logT))) uniformly 0<=|alpha|<=1 under RH (eq. 1.6); Gallagher-Mueller: J(beta,T)~(beta^2 log^2T)/(2T)... as stated for 0<=beta<=1 (eq. 1.2); Goldston-Gonek-Montgomery equivalences (II)-(IV) with pair correlation conjecture; and their Theorem 1 formula for I(a,T); Goldston 1981, Goldston-Gonek 1993 earlier bounds; Carneiro-Chandee-Littmann-Milinovich earlier gap results ([3]); Selberg's RH bound for I(a,T) with a>=10 and J=O_beta(log^2T/T) for beta>1; Beurling-Selberg extremal solution for the Poisson kernel ([5],[6])

**Techniques.** Fourier optimization / Beurling-Selberg extremal functions; Montgomery pair-correlation function F(alpha,T) and Goldston-Montgomery asymptotics; Tauberian argument with Fejer kernels; Poisson-kernel majorants/minorants (Carneiro-Littmann type); Paley-Wiener spaces, Krein decomposition, interpolation formulas; explicit numerical optimization of test configurations

## Context and interpretation

**Importance and obstacle overcome.** Narrows the gap between the best provable (RH-conditional) bounds and the conjectured asymptotics for the equivalent integrals: lower bound 0.9278 vs conjectured 1 and upper 1.3302 vs 1 for the F integral; J(beta,T) within factors 0.8376-1.4283 of linear growth rate; I(a,T) within a factor 0.899-1.434 of its conjectured value. The obstacle overcome is finding good extremal test configurations; the lower bound exploits that Dirichlet kernels cannot be too negative (min sin x/x).

**Relation to prior work.** Extends Carneiro-Chandee-Littmann-Milinovich (small gaps, bounds on N(beta,T)) and Goldston-Gonek-Montgomery; improves Goldston's Lemma A and Goldston-Gonek's Lemma constants (1/3 and 2) and their bounds on J. Related to Radziwill's work on limits of mollification (Section 2.5) and to Carneiro-Chirre-Milinovich on bounds for S_n(t).

**Limitations and open questions.** All results assume RH and stop short of the conjectured asymptotics; the constants C^+ (< 1.3302) and C^- (> 0.9278) are not claimed sharp, and EP4/EP5 are not solved exactly (only test configurations). Closing the gap to exactly 1 would prove Montgomery's pair correlation conjecture (II) and hence (I),(III),(IV). Open: sharp solution of EP1-EP5; identifying the exact value of W^+(l) for general l.

**Ideas in remarks/appendices/abandoned paths.** Section 2.5 connects Theorem 1 to Radziwill's limits of mollification. Appendix B (Theorem 19) is an independent sharp functional-analytic inequality with explicit extremizer sum of two sinc functions at +-theta, theta solving pi*theta*tan(pi*theta)=1; this exact constant 0.3244 may reappear in other pair-correlation Hilbert-space embeddings. Remark following Theorem 14: for b<=1 the epsilon-shifts in the integrals can be removed using (1.2) and (1.6).

## Research potential

- **Hypotheses that might be weakened.** RH enters twice: nonnegativity of F(alpha,T) via real zeros in the sum, and the asymptotic (1.6) on |alpha|<=1. The unconditional version of (1.6) (Baluyot-Goldston-Suriajaya-Turnage-Butterbaugh, CAND-02364) shows F is still real, even, nonnegative and has the same asymptotics unconditionally; this suggests that Theorem 7 and the bounds of Theorems 1/9/10 might be re-run under a thin-box or zero-density assumption on the zeros, with the same Fourier optimization.
- **Generalizations.** Replace zeta by other L-functions in Selberg class (degree d form factor with (log T)^d analogs); incorporate higher-correlation constraints (Rudnick-Sarnak) into the extremal problems; extend EP3 to intervals [b,beta] with b<1 using exact F data on [-1,1]; apply to pair correlation of zeros of other families (Katz-Sarnak).
- **Candidate connections.** Link with Lagarias-Rodgers (CAND-01989): the AH point process has pair form factor K_Alt which agrees with K_GUE only on |xi|<1, so integrals of F over [1,beta] are exactly the observables that distinguish AH from GUE; the bounds C^- >= 0.9278 per unit length can be tested against the AH value (which integrates to ~2 per unit mean over periods). Connect with the 0.606894 small-gap constant of Carneiro et al., with the Pratt-Robles-Zaharescu-Zeindler critical-line proportion results, and with Baluyot et al. (unconditional F).
- **Reusable lemmas.** Proposition 6 (monotonicity/sub-superadditivity of W^pm) and Corollary 8 (symmetrization about alpha=1) are reusable for any Fourier-optimization bound on F; Lemma 16 reusable for any Poisson-kernel majorant; Theorem 19 is a standalone sharp inequality in Paley-Wiener spaces.
- **Possible experiments.** Numerically solve EP1/EP2 by linear/semidefinite programming over families of (g_j,xi_j) with g-hat supported in a fixed compact set to improve 1.3302 and 0.9278; compare with the empirical F(alpha,T) from Odlyzko data at height 10^22 over [1,beta]; compute the AH-process value of integral of K_Alt over [1,1+l] to see whether the 0.9278l lower bound already excludes AH-like fluctuations at this scale.
- **Risks / barriers.** The extremal problems have a fundamental limit: any bound obtained from F>=0, (1.6) and test functions with g-hat<=0 outside [-1,1] cannot beat the true value of W^pm; since AH is consistent with all data in |alpha|<=1 (Lagarias-Rodgers), no method using only these inputs can reach the conjectured constant 1, only the sharp solutions of EP1/EP2.

## Audit notes (Level 1 reader)

Partial reading only (proofs of Theorems 5, 9, 10 and Appendices not checked line by line). Observations: (i) Corollary 2's ranges (0.9278, 1.3302) are stated as 'large l' while Theorem 9/10 formulas carry explicit l-dependence; the transcribed branch of C_N^+ in Theorem 9 in the extracted text is garbled so exact piecewise form should be taken from the paper, not from this record. (ii) The abstract lists the third integral as the second moment of zeta'/zeta near the critical line, while the arXiv metadata/triage description (from zbMATH) mentions only two of three. Otherwise none noticed in inspected portion.

*These notes are a reader's observations, not verified findings; see `audits/` for adjudicated findings.*

## Provenance

- Candidate `CAND-01897`; harvest queries: kw_RH_any, kw_pair_correlation, msc_11M06, msc_11N05, arxiv_critical_line, arxiv_pair_corr, arxiv_rh_abs.
- Triage decision: include — Further pair correlation integrals, Selberg variance connection.
- Record generated by `tools/make_records.py`; search cutoff 2026-11-17.
