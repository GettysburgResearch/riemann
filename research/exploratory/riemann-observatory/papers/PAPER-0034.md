# PAPER-0034 — More than 41\% of the zeros of the zeta function are on the critical line

| Field | Value |
|---|---|
| Authors | Bui, H. M.; Conrey, Brian; Young, Matthew P. |
| Year / stratum | 2011 / S5 |
| Venue | Acta Arith. 150, No. 1, 35-64 (2011). |
| Identifiers | zbMATH [1250.11083](https://zbmath.org/?q=an:1250.11083) · DOI [10.4064/aa150-1-3](https://doi.org/10.4064/aa150-1-3) · arXiv [1002.4127](https://arxiv.org/abs/1002.4127) |
| MSC | 11M26, 11M06 |
| Families | A, B |
| Work type | original_paper |
| Evidence level of this record | **L1-partial** |
| Full text | partial_fulltext — https://arxiv.org/abs/1002.4127 |
| Selection | score 4.5836, in-pool citations 35, seed lists 4, triage relevance 5 |

## Mathematical content (Level 1: full text read)

**Research question.** Improve the lower bound for the proportion kappa of nontrivial zeros of zeta on the critical line (and kappa* of simple critical zeros) in the Levinson-Conrey method by replacing the one-piece mollifier of Conrey (1989, kappa>=0.4088) with a two-piece mollifier psi=psi_1+psi_2, revisiting an approach of Lou.

**Historical motivation.** Hardy 1914; Hardy-Littlewood; Selberg 1942 positive proportion; Levinson 1974 (1/3); Conrey 1989 (0.4088, 0.4013); Lou's unpublished two-piece idea (Durham 1979) which the authors adapt after finding Lou's P_2(x)=x and L^{-2} factor suspect (P_2 must vanish to third order).

### Main results

- **THM-PAPER-0034-1** (Theorem 1.1, theorem (unconditional), scope: asymptotic; Sec 1, eq (1.1)). $\kappa\ge 0.4105$ and $\kappa^*\ge 0.4058$, where $\kappa=\liminf_{T\to\infty}N_0(T)/N(T)$, $\kappa^*=\liminf N_0^*(T)/N(T)$, $N_0$ counts zeros $\rho=\tfrac12+i\gamma$, $0<\gamma<T$, and $N_0^*$ counts the simple ones.
- **THM-PAPER-0034-2** (Eq (2.1) (Levinson-Conrey reduction), standard reduction, scope: asymptotic; Sec 2.1). With $V(s)=Q(-\frac1L\frac d{ds})\zeta(s)$, $Q(0)=1$, $Q(x)+Q(1-x)=\text{const}$, $L=\log T$, $\sigma_0=\frac12-\frac RL$, and any mollifier $\psi$: $\kappa\ge1-\frac1R\log\Big(\frac1T\int_1^T|V\psi(\sigma_0+it)|^2dt\Big)+o(1)$ (Littlewood's lemma plus Jensen/AM-GM). Choosing $Q$ linear gives the version for $\kappa^*$.
- **THM-PAPER-0034-3** (Mollifier definition (2.2)-(2.3), definition, scope: finite; Sec 2.1). $\psi_1(s)=\sum_{n\le y_1}\mu(n)P_1[n]n^{\sigma_0-1/2}n^{-s}$ with $y_1=T^{\theta_1}$, $P_1(0)=0,P_1(1)=1$, $P_1[n]=P_1(\log(y_1/n)/\log y_1)$; $\psi_2(s)=\chi(s+\tfrac12-\sigma_0)\sum_{hk\le y_2}\frac{\mu_2(h)h^{\sigma_0-1/2}k^{1/2-\sigma_0}}{h^{s}k^{1-s}}P_2[hk]$, $\mu_2$ = coefficients of $1/\zeta^2$, $P_2(0)=P_2'(0)=P_2''(0)=0$, $y_2=T^{\theta_2}$, $\theta_2<\theta_1$.
- **THM-PAPER-0034-4** (Theorem 2.1, theorem (mean value), scope: asymptotic; Sec 2.1 (eq 2.5)). For $\theta_1=4/7-\varepsilon$, $\theta_2=1/2-\varepsilon$ ($\varepsilon>0$ small): $\frac1T\int_1^T|V\psi(\sigma_0+it)|^2dt=c(P,Q,R,\theta_1,\theta_2)+o(1)$ with $c=c_1+2c_{12}+c_2$ given by (3.2),(3.4),(3.6).
- **THM-PAPER-0034-5** (Theorem 2.2 (smoothed), theorem, scope: asymptotic; Sec 2.3 (2.9)). For $w$ smooth, $0\le w\le1$, supported in $[T/4,2T]$, $w^{(j)}\ll\Delta^{-j}$ with $\Delta=T/L$, and $\sigma=\frac12-\frac RL$, uniformly for $R\ll1$: $\int w(t)|V\psi(\sigma+it)|^2dt=c(P,Q,R,\theta_1,\theta_2)\hat w(0)+O(TL^{-1+\varepsilon})$.
- **THM-PAPER-0034-6** (Theorem 3.1 (Conrey, imported), imported theorem, scope: asymptotic; Sec 3.1 (3.1)-(3.2)). For $\theta_1<4/7$: $\int_1^T|V\psi_1(\sigma_0+it)|^2dt\sim c_1T$, $c_1=1+\frac1{\theta_1}\int_0^1\!\!\int_0^1e^{2Rv}\big(Q(v)P_1'(u)+\theta_1Q'(v)P_1(u)+\theta_1RQ(v)P_1(u)\big)^2du\,dv$.
- **THM-PAPER-0034-7** (Theorem 3.2 / Lemma 3.4 (cross term), theorem, scope: asymptotic; Sec 3.1, Lemma 3.4, Lemma 5.1). For $\theta_2<\theta_1<4/7$ (with (5.1): $\frac52\theta_1+\theta_2<2$, $\frac53\theta_1+\theta_2<\frac43$, $\theta_2<\frac23\theta_1$ for the proof): $I_{12}=\int w|V|^2\psi_1\overline{\psi_2}=c_{12}\hat w(0)+O(T/L)$ with explicit $c_{12}$ (3.4) involving $\frac{d^2}{dxdy}$ of a triple integral with $Q,P_1,P_2''$; the shifted version is $I_{12}(\alpha,\beta)=c_{12}(\alpha,\beta)\hat w(0)+O(T/L)$ uniformly in $\alpha,\beta\ll L^{-1}$.
- **THM-PAPER-0034-8** (Theorem 3.3 / Lemma 3.5 (second diagonal), theorem, scope: asymptotic; Sec 3.1 (3.5)-(3.6), Lemma 3.5). For $\theta_2<1/2$: $I_2=\int w|V|^2|\psi_2|^2=c_2\hat w(0)+O(TL^{-1+\varepsilon})$, $c_2$ given by the 4-dimensional integral (3.6) with $P_2''$ factors; proof via a twisted second moment (Prop 4.2).

### Key definitions

- kappa, kappa^* (liminf proportion of critical zeros, of simple critical zeros)
- Two-piece mollifier psi=psi_1+psi_2
- V(s)=Q(-(1/log T) d/ds) zeta(s)
- shifted moments I_12(alpha,beta), I_2(alpha,beta)

### Principal lemmas

- **THM-PAPER-0034-L1** (Lemma 4.1; Sec 4.1). For $L^2\le|t|\le2T$, uniformly for $\alpha,\beta\ll L^{-1}$: $\zeta(\tfrac12+\alpha+it)\zeta(\tfrac12-\beta+it)=\sum_{l\ge1}\frac{\sigma_{\alpha,-\beta}(l)}{l^{1/2+it}}e^{-l/T^3}+O(T^{-1+\varepsilon})$. — *Role:* One-long-sum approximate functional equation; the exponential cutoff truncates l at T^3 and makes the off-diagonal analysis tractable
- **THM-PAPER-0034-L2** (Proposition 4.2; Sec 4.2). For $ab\le T^{1-\varepsilon}$, uniformly in $\alpha,\beta\ll L^{-1}$, $\int w(t)(a/b)^{-it}\zeta(\tfrac12+\alpha+it)\zeta(\tfrac12+\beta-it)dt$ equals the diagonal main terms $\sum_{am=bn}$ (two pieces with $V_t$ kernel) $+O(T^{-1/2})$. — *Role:* Twisted second moment (implicit in Balasubramanian-Conrey-Heath-Brown); only diagonal terms contribute for ab<=T^{1-eps}
- **THM-PAPER-0034-L3** (Lemma 5.1; Sec 5.1). Under (5.1), $I_{12}(\alpha,\beta)=\sum_{n\le y_1;hk\le y_2;hl=nk}\frac{\mu(n)\mu_2(h)\sigma_{\alpha,-\beta}(l)}{(hkln)^{1/2}}P_1[n]P_2[hk]e^{-l/T^3}\int(\frac t{2\pi})^{-\beta}w(t)dt+O_B(T/L^B)$. — *Role:* Diagonal main term of the cross term
- **THM-PAPER-0034-L4** (Lemma 5.2; Sec 5.2 (proof lengthy)). Under (5.1), the off-diagonal contribution $C$ (terms $hl\ne nk$) satisfies $C\ll_B T/L^B$ for any $B\ge0$. — *Role:* Key analytic difficulty for the longer mollifier: off-diagonal bound via Kloosterman-sum/Deshouillers-Iwaniec-type input in the style of Conrey 1989
- **THM-PAPER-0034-L5** (Lemma 5.4; Sec 5.2). Under (5.1), $C=C_0+O(T^{1-\varepsilon})$ with $C_0$ an explicit sum over $h\le ny_2/\Delta^{1-\varepsilon}$, $b|f$, $f\ne0$. — *Role:* Isolates a main contribution from the near-diagonal in the off-diagonal sum, which cancels against terms in the main evaluation
- **THM-PAPER-0034-L6** (Sec 6.2 computation; Sec 5.6, 6.2). The arithmetical factor satisfies $B_0(s,s,s)=\sum_{h_1k_2m=h_2k_1n}\frac{\mu_2(h_1)\mu_2(h_2)}{(h_1k_1h_2k_2mn)^{1/2+s}}=\sum_{l_1m=l_2n}\frac{\mu(l_1)\mu(l_2)}{(l_1l_2mn)^{1/2+s}}=1$ using $\sum_{h|l}\mu_2(h)=\mu(l)$; similarly $A(0,0,0)=1$ in Sec 5.6. — *Role:* Shows the Euler-product arithmetic factors collapse to 1 at the origin

### Proof architecture

(1) Levinson-Conrey reduction via Littlewood's lemma: kappa >= 1-(1/R) log (mean square of mollified V on sigma_0=1/2-R/L). (2) Mollifier psi=psi_1+psi_2: psi_1 is Conrey's, length y_1=T^{4/7-eps}; psi_2 is chi(s+1/2-sigma_0) times a double Dirichlet polynomial in h^{-s}k^{s-1} built from 1/zeta^2, length y_2=T^{1/2-eps}, motivated by chi(s)zeta(1-s)/zeta^2(s)=1/zeta(s). (3) Expand |V psi|^2=I_1+2 Re I_12+I_2; I_1 is quoted from Conrey (Thm 3.1); I_12 and I_2 are computed via shifted integrals I_12(alpha,beta), I_2(alpha,beta) and recovered by the operator Q(-(1/log T)d/dalpha)Q(-(1/log T)d/dbeta) (Cauchy integral formula on radius ~1/L). (4) Lemma 4.1 one-long-sum approximate functional equation for the cross term; diagonal hl=nk gives main term, off-diagonal bounded (Lemma 5.2) under (5.1) via splitting |f|<=Delta^{-1+eps}hl and Kloosterman/Estermann-type sums. (5) Main terms rewritten as contour integrals, evaluated by residues (Lemma 5.7 etc.), with arithmetical factors A(0,0,0)=B(0,0,0)=1. (6) For I_2 use the twisted second moment Prop 4.2 and a contour evaluation. (7) Plug in optimized polynomials (numerical Mathematica evaluation) to get 0.4105 and 0.4058.

Dependency edges: CAND-01215 → Conrey 1989 (kappa>=0.4088) (extends (quotes Theorem 2 for I_1)); CAND-01215 → Lou 1979 (unpublished two-piece mollifier) (revisits and corrects); CAND-01215 → CAND-01232 (contemporaneous independent two-piece mollifier (Feng))

**Imported results.** Conrey 1989: Theorem 2 of 'More than two fifths of the zeros...' (J. Reine Angew. Math. 399), Thm 3.1 here, mean value of |V psi_1|^2 for theta_1<4/7; Balasubramanian-Conrey-Heath-Brown 1985 twisted second moment (Prop 4.2 stated without proof); Levinson 1974 and Conrey 1983 for the zeta + zeta' framework; Selberg 1942, Levinson 1974 history; Deshouillers-Iwaniec Kloosterman sum estimates via Conrey [C1]

**Techniques.** Levinson method (zeta + (log T)^{-1} zeta' perturbation, here Q(-(1/L)d/ds)zeta); Littlewood's lemma and convexity/Jensen; mollifier methods with two pieces of different shape (psi_2 uses chi and 1/zeta^2 coefficients); ratios conjecture heuristics to guess the main term (Conrey-Snaith, CFZ) then rigorous proof; twisted second moment of zeta; Balasubramanian-Conrey-Heath-Brown diagonal/off-diagonal analysis; Kloosterman sum bounds for off-diagonal terms (via Conrey 1989 / Deshouillers-Iwaniec); Euler-Maclaurin sums and contour integral evaluation; numerical optimization of polynomials Q,P_1,P_2 and R

## Context and interpretation

**Importance and obstacle overcome.** Raises the unconditional proportion of zeros on the critical line from 0.4088 to 0.4105 (and simple critical zeros from 0.4013 to 0.4058). The obstacle is to evaluate the mean value with a second mollifier of different shape while keeping the long first mollifier theta_1 = 4/7: requires delicate treatment of off-diagonal terms in the cross term and a twisted second moment for the chi-twisted piece.

**Relation to prior work.** Builds on Conrey 1989 (reduces to the same Levinson framework and quotes his result for I_1). Mentions Feng's independent two-piece mollifier (CAND-01232) and says its formulas were checked except the claimed length theta=4/7-eps for the new mollifier; with theta=1/2-eps (admissible) Feng's would surely improve 0.4088. Later superseded by Feng 0.4128 (JNT) and then Pratt-Robles-Zaharescu-Zeindler (2020, >5/12).

**Limitations and open questions.** Proportion method cannot give 100%: Levinson-type approaches need R->0 or different f(s); extra gains need longer mollifiers (Farmer theta=infinity conjecture) or more pieces. The proof uses unproved-here Proposition 4.2 (stated 'without proof', implicit in BCHB). The numerical constants rely on Mathematica evaluation of the multi-dimensional integral formula (no certified bound given). Condition theta_2<1/2 for I_2 vs theta_2<2/3 theta_1 etc. for the cross term (5.1) restrict the pair (theta_1, theta_2).

## Research potential

- **Hypotheses that might be weakened.** The constraint set (5.1) on (theta_1,theta_2) and theta_2<1/2 in Thm 3.3: relaxing theta_2 past 1/2 requires bounds for the twisted second moment with ab up to T^{1+eps}; the shape condition P_2(0)=P_2'(0)=P_2''(0)=0 is derived heuristically (ratios conjecture) and could be revisited with a third piece.
- **Generalizations.** Replace psi_2 by more general multi-piece mollifiers (as Feng, and later Pratt et al.); apply to other L-functions (Dirichlet, Dedekind, GL(2)) in the Levinson-Conrey framework; use generalized Q with higher derivatives, V(s)=sum a_j zeta^{(j)}.
- **Candidate connections.** Ratios-conjecture-driven heuristics for mollified moments give a machine for predicting c(P,Q,R,theta) in new setups; connect with the 'L-function families' programme and with local zero census vs global functional distinctions (a positive proportion is not a global statement). Also with simple zeros and the Small Gap/Montgomery pair correlation (Feng's remark).
- **Reusable lemmas.** Lemma 4.1 (one-long-sum approximate functional equation with e^{-l/T^3} cutoff) and Prop 4.2 (twisted second moment with a,b twists) are reusable; the final polynomial optimization is a finite-dimensional variational problem whose formulas (3.2),(3.4),(3.6) can be re-evaluated independently.
- **Possible experiments.** Independently re-implement c(P,Q,R,4/7,1/2) from (3.2),(3.4),(3.6) with the stated polynomials Q,P_1,P_2,R=1.28 in exact rational/interval arithmetic and verify 1-(1/R)log c >= 0.4105; then run a numerical optimization over higher-degree P_1,P_2,Q and test the sensitivity to theta_2 in [0,1/2); also compare with Feng's four-piece prime-sum mollifier formulas.
- **Risks / barriers.** Gains are marginal (0.4088 to 0.4105) and the method saturates; extending theta_1 beyond 4/7 needs better Kloosterman-type input; the whole framework is a local zero census-style positive proportion result and cannot decide RH.

## Audit notes (Level 1 reader)

Abstract on arXiv v2 says 'at least 41.05%' while the title says 'More than 41%'; consistent with Theorem 1.1 (0.4105). Lemma 5.1 hypothesis (5.1) includes theta_2<(2/3)theta_1, which at theta_1=4/7 gives theta_2<8/21 ~0.381, but the Remark says theta_1=4/7 translates to theta_2<4/7; as extracted from the text these do not look identical (the extraction of (5.1) is garbled: it reads 5/2 theta_1+theta_2<2, 5/3 theta_1+theta_2<4/3, theta_2<2/3 theta_1 or similar), so the exact form of (5.1) and its relation to the Remark and to theta_2=1/2-eps in Theorem 2.1 should be checked in the PDF. Prop 4.2 is stated without proof. I did not verify the numerical value 0.4105; the formulas (3.2),(3.4),(3.6) were not re-evaluated.

*These notes are a reader's observations, not verified findings; see `audits/` for adjudicated findings.*

## Provenance

- Candidate `CAND-01215`; harvest queries: kw_moments_zeta, kw_zeta_zeros, msc_11M06, msc_11M26, arxiv_critical_line.
- Triage decision: include — Current record proportion of critical zeros (Levinson-Conrey line).
- Record generated by `tools/make_records.py`; search cutoff 2026-11-17.
