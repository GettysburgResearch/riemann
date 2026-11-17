# PAPER-0045 — More than five-twelfths of the zeros of \(\zeta\) are on the critical line

| Field | Value |
|---|---|
| Authors | Pratt, Kyle; Robles, Nicolas; Zaharescu, Alexandru; Zeindler, Dirk |
| Year / stratum | 2020 / S6 |
| Venue | Res. Math. Sci. 7, No. 1, Paper No. 2, 74 p. (2020). |
| Identifiers | zbMATH [1505.11116](https://zbmath.org/?q=an:1505.11116) · DOI [10.1007/s40687-019-0199-8](https://doi.org/10.1007/s40687-019-0199-8) · arXiv [1802.10521](https://arxiv.org/abs/1802.10521) |
| MSC | 11M26, 11L07, 11M06, 05A18 |
| Families | A, B |
| Work type | original_paper |
| Evidence level of this record | **L1-partial** |
| Full text | partial_fulltext — https://arxiv.org/abs/1802.10521 |
| Selection | score 4.5652, in-pool citations 15, seed lists 4, triage relevance 5 |

## Mathematical content (Level 1: full text read)

**Research question.** Unconditionally compute the twisted second moment of zeta with Dirichlet polynomials whose coefficients are (mu * Lambda^{*k_1} * ... * Lambda^{*k_d})(n) (using ratios-conjecture-style combinatorics), push the admissible length to theta=4/7 for the whole family, mollify the whole perturbed function V(s) (Q-derivative of zeta plus lambda_j zeta^{(j)}/L^j), and thereby raise the proportion kappa of zeros of zeta on the critical line above 5/12.

**Historical motivation.** Levinson (1974) kappa>1/3; Conrey (1989) kappa>2/5; Bui-Conrey-Young 41.05%; Feng's 41.28% claim relied on the unproved square-free reduction ('Feng's conjecture') and error terms; Pratt-Robles repaired to 6/11. This paper (dedicated to Conrey, 30 years after 'two-fifths') removes the square-free restriction, reaches 4/7 for the whole family, and crosses 5/12.

### Main results

- **THM-PAPER-0045-1** (Theorem 1.2, theorem, scope: global; Sec. 1.3, p. 9; numerics Sec. 8, p. 56). More than five-twelfths of the non-trivial zeros of $\zeta(s)$ lie on the critical line, i.e. $\kappa>5/12$. Proved with $d=1$, $K=3$, $\theta=4/7-\epsilon$, $R=1.3036$ and explicit polynomials $P_1,P_2,P_3,Q$ (Sec. 8), giving $\kappa\ge0.417293962$; and $\kappa^*\ge0.407511457$ for the proportion of simple zeros on the line (linear $Q$, $R=1.1167$).
- **THM-PAPER-0045-2** (Theorem 4.1, theorem, scope: asymptotic; Sec. 4, p. 18). Let $\alpha,\beta\ll L^{-1}$, $\psi_1=\sum_{n\le N}a_nn^{-s}$, $\psi_2=\sum_{n\le N}b_nn^{-s}$, $N=T^\theta$. Then $I(\alpha,\beta)=\int\zeta(\tfrac12+\alpha+it)\zeta(\tfrac12+\beta-it)\psi_1\psi_2(\tfrac12+it)\Phi(t/T)dt=\sum_{d,e\le N}\frac{a_db_e(d,e)^{\alpha+\beta}}{[d,e]d^\alpha e^\beta}\int(\zeta(1+\alpha+\beta)+\zeta(1-\alpha-\beta)(\frac{2\pi de}{t(d,e)^2})^{\alpha+\beta})\Phi(t/T)dt+O(E)$ with $E=T^{3/20}N^{33/20}+N^{1/2}T^{1/2+\epsilon}$ if $a_n\ll n^\epsilon$ (as read); $E=T^\epsilon(N^{11/6}+N^{11/12}T^{1/2})$ if $a_n=\mu^2(n)(\mu*\Lambda^{*k_1}_1*\cdots*\Lambda^{*k_D}_D)(n)$; $E=T^\epsilon(N^{7/4}+N^{7/8}T^{1/2})$ if $a_n=(\mu*\Lambda^{*k_1}_1*\cdots*\Lambda^{*k_D}_D)(n)$ with no square-free restriction. Hence $\theta<4/7$ for the whole family.
- **THM-PAPER-0045-3** (Sec. 5.1 (Proof of Feng's conjecture), theorem, scope: asymptotic; Sec. 5.1, pp. 23-27). Feng's unproved claim that terms with $\mu^2(n)=0$ contribute only a lower-order term to the mean value integral is proved in the case $K=2$ (other $K$ asserted to work out similarly) by splitting $a_d=b_d+c_d$ with $b_d$ the Feng coefficient (sum over distinct primes $q_1\ne q_2|d$) and showing the remainder $c_d$ contributes lower order.
- **THM-PAPER-0045-4** (Theorem 7.1, theorem, scope: asymptotic; Sec. 7.2, pp. 44-45). For the general mollifier coefficients $a_d,b_e$ of (7.1),(7.2) built from $(\mu*\Lambda^{*\ell_1}*\cdots)$ with polynomials $P_{d,\ell_d}$, the mollified twisted moment equals $\sum_{i,j}\frac{p_{d,\ell_d,i}p_{d,\bar\ell_d,j}\,i!\,j!}{(\log N)^{i+j}}\frac1{(2\pi i)^2}\iint\frac{1}{(\log N)^{\sum r_\ell\ell+\sum\bar r_{\bar\ell}\bar\ell}}\Big[\frac1{(2\pi i)^{L_d+\bar L_d}}\oint\oint M_{\alpha,\beta}(z,w;s,u)DZ\,DW-T^{-\alpha-\beta}\oint\oint M_{-\beta,-\alpha}(z,w;s,u)DZ\,DW\Big]\frac{ds\,du}{s^{i+1}u^{j+1}}+O(T^{1-\epsilon})$ (up to the normalization of the integral sign as printed), where $M_{\alpha,\beta}$ is a ratio of products of shifted zeta functions times an arithmetical factor $A_{\alpha,\beta}$ with $A(0,0;\beta,\alpha)=M(0,0;\beta,\alpha)=1$ (7.6)-(7.7).
- **THM-PAPER-0045-5** (Conjecture 1.1 / Theorem 1.1 (recalled), conjecture (imported), scope: conditional; Sec. 1.2, pp. 3-5). Conrey-Farmer-Zirnbauer ratios conjecture for $R(\alpha,\beta,\gamma,\delta)=\int\frac{\zeta(s+\alpha)\zeta(1-s+\beta)}{\zeta(s+\gamma)\zeta(1-s+\delta)}dt$ with main term $\frac{\zeta(1+\alpha+\beta)\zeta(1+\gamma+\delta)}{\zeta(1+\alpha+\delta)\zeta(1+\beta+\gamma)}A(\alpha,\beta,\gamma,\delta)$ plus the $(t/2\pi)^{-\alpha-\beta}$ swapped term and error $O(T^{1/2+\epsilon})$; the Conrey-Snaith derivation is for $\int\zeta'/\zeta\cdot\zeta'/\zeta$. Used only as the template for the rigorous contour-integral combinatorics. *Conditional on:* ratios conjecture (motivational only).

### Key definitions

- V(s)=Q(-(1/L)d/ds)zeta(s)
- M(s,d) inverse of perturbed zeta
- kappa and kappa^* (proportion of simple zeros)
- partial and complete Bell polynomials, Bell diagrams
- Lambda^{*k} k-fold convolution

### Principal lemmas

- **THM-PAPER-0045-L1** (Mollifier inversion (1.5), (3.2)-(3.3); Sec. 1.3 and Sec. 3). $M(s,d)=1/(\zeta(s)+\lambda_1\zeta'/L+\cdots+\lambda_d\zeta^{(d)}/L^d)$; for $d=1$, $M(s,1)=\sum_k\frac1{\log^kT}\sum_n\frac{(\mu*\Lambda^{*k})(n)}{n^s}$; for square-free $n$, $(\mu*\Lambda^{*k})(n)=(-1)^k\mu(n)\sum_{p_1\cdots p_k|n}\log p_1\cdots\log p_k$ (Feng's formula); general coefficients are organized by Bell-polynomial combinatorics (Secs. 3.4-3.5; e.g. 250 diagrams in one case). — *Role:* Defines the new family of mollifier coefficients.
- **THM-PAPER-0045-L2** (Proof of Theorem 4.1 (extending Pratt-Robles Thm 1.2); Sec. 4, pp. 18-20). Main terms are unchanged from Pratt-Robles; only error terms change. To separate $d$ from $n_1$ in $(\mu*\Lambda^{*\ell_1}*\cdots)(dn_1)$, factor $n_1\to hn_1$ with $h|d^\infty$ and $n_1$ coprime to $d$, so $\mu^2$ is no longer needed; then Vaughan/Heath-Brown identities and additivity of the logarithm yield length $4/7$. — *Role:* Key step improving 6/11 to 4/7.
- **THM-PAPER-0045-L3** (Lemmas 7.1, 7.2; Sec. 7, text lines ~4177 and ~4496). Technical evaluations of sums over $\ell_r$, truncation parameters and arithmetic-factor identities supporting the residue/contour computation of Theorem 7.1 (statements in Sec. 7; not read in detail). — *Role:* Support the main-term evaluation of Theorem 7.1.

### Proof architecture

(1) Levinson's method requires mollifying the whole perturbed function V(s), not zeta; invert the d-th order linear combination to get coefficients (mu * Lambda^{*k...}). (2) Bell-polynomial/diagram combinatorics organizes these coefficients (Sec. 3). (3) Evaluate the twisted second moment unconditionally: error terms of Pratt-Robles are re-proved without the square-free restriction (Thm 4.1), giving theta=4/7; main terms are evaluated by a rigorous version of the ratios-conjecture recipe (Secs. 5-7, Thm 7.1), with arithmetical factors and derivatives cancelling or absorbed in errors. (4) Insert in the Levinson/Littlewood-lemma inequality, choose d=1, K=3, R=1.3036 and polynomials, compute kappa>=0.417293962 (Sec. 8).

**Imported results.** Pratt-Robles main-term machinery (arXiv 1706.04593, CAND-01881); Bettin-Chandee-Radziwill generic length 17/33; Bettin-Chandee trilinear Kloosterman fractions; Deshouillers-Iwaniec; Levinson 1/3, Conrey 2/5 (theta=4/7), Bui-Conrey-Young 41.05%, Feng's numerical setup; Conrey-Snaith and CFKRS ratios conjecture as heuristic

**Techniques.** autocorrelation of ratios of zeta (recipe) used rigorously; mollification of the whole perturbed zeta (Levinson method); Bell polynomials and diagram combinatorics; Vaughan and Heath-Brown identities; Deshouillers-Iwaniec / Bettin-Chandee Kloosterman bounds; Littlewood lemma / Levinson inequality

## Context and interpretation

**Importance and obstacle overcome.** Pushes the proportion of critical zeros past 5/12 unconditionally and supplies a rigorous 'ratios-conjecture machine' for mollified twisted moments. Coefficients of (mu*Lambda^{*k}) for non-square-free n lack a closed form (handled by n_1->h n_1 with h|d^infty); the combinatorial explosion is handled by Bell polynomial bookkeeping.

**Relation to prior work.** Direct successor of Pratt-Robles (CAND-01881): same moment formula with better error terms and a proof of Feng's conjecture; same Levinson framework as Conrey, Bui-Conrey-Young, Feng; uses CFKRS/Conrey-Snaith ratios techniques unconditionally; Wu independently did Dirichlet L-functions.

**Limitations and open questions.** Still limited by theta=4/7. Sec. 9 lists open problems: extension to the Selberg class and other L-functions, effects on discrete/log moments and pair correlation, increasing length without over-specializing a_n, and combining the full Feng-type mollifier with the Bui-Conrey-Young second piece (1.4), expected to improve kappa. Numerics use only d=1, K=3; general d>=2 formulas are exhibited but not optimized. Secs. 6-7 combinatorics not independently reproduced here.

## Research potential

- **Hypotheses that might be weakened.** theta<4/7 is the sole analytic bottleneck: any improved bound for sums of Kloosterman fractions with convolution-structured coefficients raises kappa immediately via Theorems 4.1/7.1. The restriction to d=1, K=3 in the numerics is inessential.
- **Generalizations.** Selberg-class / Dirichlet L-function analogues (Sec. 9 item 1), d>=2 mollifier optimization, combination with the BCY second piece (Sec. 9 item 4), proportion of simple zeros kappa^*, zeros of zeta^{(k)} on Re s=1/2.
- **Candidate connections.** Bettin-Gonek (theta=infinity Conrey mollifier implies RH) and Farmer's theta=infinity conjecture; the family M(s,d) of full inverses gives a systematic route toward near-perfect mollification; ratios conjecture/RMT connection (no RMT analogue of mollifying).
- **Reusable lemmas.** Theorem 4.1 (error terms without square-free restriction) and Theorem 7.1 (main-term contour-integral formula) are reusable black boxes for mollified twisted second moments of zeta; Bell-diagram bookkeeping reusable for ratios with many zeta factors.
- **Possible experiments.** Re-run the Sec. 8 optimization with the published polynomials to reproduce kappa=0.417293962; extend to d=2 or add a BCY piece; numerically compare square-free vs full convolution coefficients (plots in Sec. 5) at moderate T.
- **Risks / barriers.** Method cannot exceed what mollifier length allows: theta=4/7 gives kappa~0.4173; 100% needs unbounded theta; connection to RH only via Bettin-Gonek theta=infinity, far out of reach.

## Audit notes (Level 1 reader)

Theorem 4.1 exponents consistent (N=T^{4/7}: N^{7/4}=T and N^{7/8}T^{1/2}=T). The generic-case error term was read from a garbled text layer. Sec. 5.1 proves Feng's conjecture explicitly only for K=2 ('higher K similarly'), while the numerics use K=3 - a possible rigor gap at Sec. 5.1, p. 23. Secs. 6-7 proofs not independently checked.

*These notes are a reader's observations, not verified findings; see `audits/` for adjudicated findings.*

## Provenance

- Candidate `CAND-01813`; harvest queries: kw_zeta_zeros, msc_11M06, msc_11M26, arxiv_mollifier, arxiv_moments_zeta, arxiv_zeta_zeros.
- Triage decision: include — Current record for proportion of critical zeros via mollification.
- Record generated by `tools/make_records.py`; search cutoff 2026-11-17.
