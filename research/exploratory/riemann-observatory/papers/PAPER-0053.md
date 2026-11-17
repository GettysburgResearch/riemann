# PAPER-0053 — An unconditional Montgomery theorem for pair correlation of zeros of the Riemann zeta-function

| Field | Value |
|---|---|
| Authors | Baluyot, Siegfred Alan C.; Goldston, Daniel Alan; Suriajaya, Ade Irma; Turnage-Butterbaugh, Caroline L. |
| Year / stratum | 2024 / S7 |
| Venue | Acta Arith. 214, 357-376 (2024). |
| Identifiers | zbMATH [1556.11092](https://zbmath.org/?q=an:1556.11092) · DOI [10.4064/aa230612-20-3](https://doi.org/10.4064/aa230612-20-3) · arXiv [2306.04799](https://arxiv.org/abs/2306.04799) |
| MSC | 11M06, 11M26 |
| Families | B |
| Work type | original_paper |
| Evidence level of this record | **L1** |
| Full text | fulltext_read — https://arxiv.org/abs/2306.04799 |
| Selection | score 4.5591, in-pool citations 3, seed lists 0, triage relevance 4 |

## Mathematical content (Level 1: full text read)

**Research question.** Can Montgomery's pair correlation theorem (F(alpha) asymptotics for 0<=alpha<=1) be proved without assuming RH, and can it yield a positive proportion of simple zeros without RH? Answer: Theorem 1 gives F unconditionally; Theorems 2-3 give >=61.7% simple zeros under a thin-box hypothesis (all zeros with T^{3/8}<gamma<=T within |beta-1/2|<1/(2 log T)) or under a strong zero-density hypothesis, neither of which implies RH.

**Historical motivation.** Montgomery's 1973 theorem assuming RH gave >2/3 simple zeros; Montgomery-Taylor 67.2%, Chirre-Goncalves-de Laat 67.9%. Selberg's conjecture on N(sigma,T) and Aryan's work used density-type assumptions as RH substitutes; the authors ask whether pair correlation itself can be made unconditional.

### Main results

- **THM-PAPER-0053-1** (Theorem 1, theorem (unconditional), scope: asymptotic; Section 1, p.1; proof Section 2, pp.2-5). Define $F(x,T)=\sum_{\rho,\rho'\,(0<\gamma,\gamma'\le T)}x^{\rho-\rho'}w(\rho-\rho')$ with $w(u)=\frac{4}{4-u^2}$ and $F(\alpha)=\frac{T^{-1}}{\,}\!\left(\tfrac{T}{2\pi}\log T\right)^{-1}\!F(T^\alpha,T)$ i.e. $F(\alpha)=(\tfrac{T}{2\pi}\log T)^{-1}\sum T^{\alpha(\rho-\rho')}w(\rho-\rho')$ (zeros counted with multiplicity). Then $F(\alpha)$ is real, even and nonnegative, and $F(\alpha)=T^{-2\alpha}(\log T+O(1))+\alpha+O(1/\sqrt{\log T})$ as $T\to\infty$, uniformly for $0\le\alpha\le1$.
- **THM-PAPER-0053-2** (Theorem 2, theorem (conditional on a thin-box zero-location hypothesis, weaker than RH-free statement), scope: asymptotic; Section 1, p.2; proof Section 7, pp.10-12). Suppose all zeros $\rho=\beta+i\gamma$ of $\zeta$ with $T^{3/8}<\gamma\le T$ satisfy $\frac12-\frac1{2\log T}<\beta<\frac12+\frac1{2\log T}$. Then for all sufficiently large $T$, at least $61.7\%$ of the nontrivial zeros $0<\gamma\le T$ are simple (precisely: $\liminf\frac1{N(T)}\#\{\text{simple }\rho\}\ge0.6174837\dots$ with the Montgomery-Taylor kernel; $0.6086\dots$ with the Fejer kernel).
- **THM-PAPER-0053-3** (Theorem 3, theorem (conditional on a zero-density hypothesis), scope: asymptotic; Section 1, p.2; Sections 6-7). Assume $N(\sigma,T)=o(T^{2(1-\sigma)})$ for $\frac12+\frac1{2\log T}\le\sigma\le\frac{25}{32}+\eta$, for every fixed $\eta>0$, where $N(\sigma,T)=\#\{\rho:\beta\ge\sigma,0<\gamma\le T\}$. Then as $T\to\infty$ at least $61.7\%$ of the nontrivial zeros are simple.

### Key definitions

- Unconditional F(x,T) with $w(u)=4/(4-u^2)$, $F(\alpha)$ normalized by $\tfrac T{2\pi}\log T$
- Theta(t)=max real part of zeros up to height t; zero-free region 1-eta(t)
- Tsang kernel K via $\hat K(t)=j(2\pi t)\operatorname{sech}(2\pi t)$; Fejer j_F and Montgomery-Taylor j_M
- Thin box 1/2 +- 1/(2 log T); strong density hypothesis (1.6)

### Principal lemmas

- **THM-PAPER-0053-L1** (Lemma 1 (Montgomery); Section 2, p.3). For $\rho=\tfrac12+\delta+i\gamma$, $x\ge1$ and all $t$: $\sum_\rho\frac{2x^{\delta+i(\gamma-t)}}{1+((t-\gamma)+i\delta)^2}=-\sum_{n\ge1}\frac{\Lambda(n)}{n^{1/2+it}}\min(\tfrac nx,\tfrac xn)+x^{-1}(\log(|t|+2)+O(1))+O(\tfrac{x^{1/2}}{1+t^2})+O(\tfrac{x^{-5/2}}{|t|+2})$. Derived from Landau's explicit formula using $s=\sigma$ and $1-\sigma$ at $\sigma=3/2$, without RH. — *Role:* Unconditional replacement of Montgomery's explicit formula identity (valid for zeros with real parts different from 1/2).
- **THM-PAPER-0053-L2** (Lemma 3; Section 2, p.3-4). For $x>0$, $T\ge3$: $F(x,T)=\frac2\pi\int_{-\infty}^\infty\left|\sum_{0<\gamma\le T}\frac{x^{\rho-1/2}}{1-(\rho-(1/2+it))^2}\right|^2dt$ (unconditional; shown by residues using $\int(1+t^2)^{-1}(1+(t+a)^2)^{-1}dt=2\pi/(4+a^2)$). Hence F(x,T)>=0 and real. — *Role:* Establishes nonnegativity and reality of F(alpha) without RH (the weight $w(u)=4/(4-u^2)$ replaces $4/(4+(\gamma-\gamma')^2)$).
- **THM-PAPER-0053-L3** (Lemma 4; Section 2, p.4-5). For $x\ge1$, $T\ge3$ and a zero-free region $\sigma>1-\eta(t)\ge\Theta(t)$: $F(x,T)=\frac1{2\pi}L(x,T)+O(x^{1-2\eta(T\log^2T)}\log^3T)+O(x)$ where $L(x,T)=\int_0^T|\sum_\rho\frac{2x^{\delta+i\gamma}}{1+((t-\gamma)+i\delta)^2}|^2dt$. With Vinogradov-Korobov $\eta(t)=c/((\log t)^{2/3}(\log\log t)^{1/3})$ the error is $O(T)+O(x)$ for $1\le x\le T$. — *Role:* Replaces Montgomery's truncation argument by an explicit loss controlled by the unconditional zero-free region; this is the only place where non-RH zeros cost anything.
- **THM-PAPER-0053-L4** (Lemma 5; Section 3, p.6-7). If $r\in L^1$ is real, even, supported in $[-1,1]$ and Lipschitz at 0, then $\sum_{0<\gamma,\gamma'\le T}\hat r(i(\rho-\rho')\tfrac{\log T}{2\pi})w(\rho-\rho')=\tfrac T{2\pi}\log T\big(r(0)+2\int_0^1\alpha r(\alpha)d\alpha+O(1/\sqrt{\log T})\big)$ (unconditional). — *Role:* Unconditional version of Montgomery's sum over pairs of zeros for kernels with Fourier transform supported in [-1,1].
- **THM-PAPER-0053-L5** (Lemma 6 (K.-M. Tsang); Section 4, p.7). The Tsang kernel $K(z)=\frac1\pi\int_0^1 j(\alpha)\operatorname{sech}(\alpha)\cos(z\alpha)d\alpha$ ($\hat K(t)=j(2\pi t)\operatorname{sech}(2\pi t)$) is even entire with (a) $K(x)>0$ on R, (b) $K(z)\ll e^{|\Im z|}/|z|^2$, (c) $\Re K(x+iy)>0$ for $|y|<1$. — *Role:* Positivity of Re K(-i(rho-rho')log T) in the region |beta-beta'|<1/log T lets one bound sum m_rho by the pair sum, off the half line.
- **THM-PAPER-0053-L6** (Lemma 7; Section 5, p.8). With $K$ the Tsang kernel: $2\pi\sum_{\rho,\rho',\,|\beta-\beta'|<1/\log T}\Re K(-i(\rho-\rho')\log T)+S(T)=\big(\hat K(0)+2\int_0^1\alpha\hat K(\tfrac\alpha{2\pi})d\alpha+O(1/\sqrt{\log T})\big)\tfrac T{2\pi}\log T$, where $S(T)=2\pi\Re\sum_{|\beta-\beta'|\ge1/\log T}K(-i(\rho-\rho')\log T)w(\rho-\rho')$. — *Role:* Splits pair sum into diagonal-near terms (positive) and an error S(T) controlled by zero-density or thin-box hypotheses.
- **THM-PAPER-0053-L7** (Section 6 claim (6.3); Section 6, pp.9-10). Either the thin-box hypothesis (6.1) or the density hypothesis (6.2) implies $S(T)=o(T\log T)$, via $|K(-i(\rho-\rho')\log T)|\ll T^{|\beta-\beta'|}/(\ldots)^2$, AM-GM $T^{|\beta-\beta'|}\le\frac12(T^{|2\beta-1|}+T^{|2\beta'-1|})$, reduction to $\sum_{\beta\ge1/2+1/(2\log T)}T^{2\beta-1}=o(T\log T)$ via partial summation against $N(u,T)$, and Bourgain's $N(\sigma,T)=o(T^{2(1-\sigma)})$ for $\sigma\ge25/32+\eta$. — *Role:* The only place the extra hypothesis is used; shows RH is not needed, only that off-line zeros are rare/near the line.

### Proof architecture

Theorem 1: Montgomery's explicit-formula identity (Lemma 1) is proved unconditionally via Landau's formula at sigma and 1-sigma. Lemma 3 expresses the unconditionally defined F(x,T) with weight 4/(4-u^2) as an L^2 integral, giving positivity. Lemma 4 compares F with L(x,T) (an integral of the Dirichlet-polynomial side) at an error controlled by the Vinogradov-Korobov zero-free region. Montgomery/Goldston-Montgomery evaluation of the Dirichlet-polynomial side R(x,T) (eq. 2.19) then gives F(alpha) for 0<=alpha<=1. Theorems 2-3: apply Lemma 5-7 with Tsang's kernel K (positive real part within |beta-beta'|<1/log T) to bound sum of multiplicities m_rho by (1/K(0)) sum Re K over close pairs, control the far-pair contribution S(T) via zero-density (Section 6), then use #simple>=sum(2-m_rho) giving proportion >=2-(K-hat(0)+2 int alpha K-hat(alpha/2pi))/(2 pi K(0)); with Fejer kernel 0.6086, with Montgomery-Taylor kernel 0.6175. Imported: Landau's explicit formula, Bourgain's density bound, Vinogradov-Korobov zero-free region, Tsang's kernel properties, Goldston-Montgomery (2.19), N(T) asymptotics.

**Imported results.** Montgomery 1973 pair correlation theorem and Goldston-Montgomery 1987 Lemma 8 (explicit R(x,T) evaluation, eq. 2.19); Landau's explicit formula (2.3); Bourgain 2000: N(sigma,T)=o(T^{2(1-sigma)}) for sigma>=25/32+eta; Vinogradov-Korobov zero-free region sigma>=1-c/((log t)^{2/3}(loglog t)^{1/3}); Tsang 1993 Lemma 1 (kernel K properties); Montgomery-Taylor 1974 kernel j_M; Riemann-von Mangoldt N(T) formula (Lemma 2)

**Techniques.** Montgomery pair correlation without RH (weight 4/(4-u^2), complex exponents); Landau explicit formula at sigma and 1-sigma; Tsang kernel with positive real part in a strip; Montgomery-Taylor kernel optimization; zero-density estimates (Bourgain) and partial summation against N(sigma,T); Vinogradov-Korobov zero-free region for truncation error

## Context and interpretation

**Importance and obstacle overcome.** First unconditional form of Montgomery's pair correlation theorem (the weight w(u)=4/(4-u^2) becomes complex off the line; positivity is rescued via the L^2 identity Lemma 3), and first pair-correlation proof of a positive proportion (61.7%) of simple zeros that does not assume RH (and neither requires nor decides whether zeros lie on the critical line). Obstacle: controlling terms with beta != beta', where T^{|beta-beta'|} growth is tamed using zero-density input.

**Relation to prior work.** Direct non-RH counterpart of Montgomery 1973, Goldston-Montgomery 1987, Montgomery-Taylor 1974 and Chirre-Goncalves-de Laat (67.9% under RH); the 61.7% is below RH-based 67.9% and 70.37% (Conrey-Ghosh-Gonek; Bui-Heath-Brown under RH). Complements Aryan 2022 (Selberg-type density conjecture implying Montgomery's simple-zero result). Provides the unconditional F needed by Carneiro-Chandee-Chirre-Milinovich-type Fourier-optimization arguments (CAND-01897).

**Limitations and open questions.** Theorems 2 and 3 are conditional on extra hypotheses about zero locations that are not known (they follow from RH, but are not implied by known results), so no unconditional simple-zero proportion is obtained. Theorem 1 only covers 0<=alpha<=1; extending beyond alpha=1 is the pair correlation conjecture itself. The 61.7% constant is optimized only over the Montgomery-Taylor kernel, not over all admissible j. Open: replace thin-box by weaker zero-density input; unconditional version of Chirre et al.'s 67.9%.

**Ideas in remarks/appendices/abandoned paths.** Remark after Lemma 7: pairs with |beta-beta'|<(1-eps)loglogT/logT suffice, suggesting a weaker thin-box. The Remark after Theorem 1 notes that Montgomery-Vaughan's forthcoming book has a refined unconditional version; also that GM87's extraneous log log T factor can be removed. Selberg's conjecture (1.7) is remarked to imply all but o(T) zeros lie in the thin box, giving an alternative route.

## Research potential

- **Hypotheses that might be weakened.** Theorem 2's thin box 1/(2 log T) is used only through (6.3) S(T)=o(T log T), so it can be relaxed to any hypothesis giving sum_{beta>=1/2+1/(2 log T)} T^{2beta-1}=o(T log T) (for instance a log-power zero-density bound near sigma=1/2 using the remark after Lemma 7 that pairs with |beta-beta'|<(1-eps)loglogT/logT already suffice). The height cutoff T^{3/8} is also tied to Bourgain's range sigma>=25/32 via N(T^{3/8})<<T^{3/8}log T; improving density exponents (Guth-Maynard 2024) should enlarge it.
- **Generalizations.** Extend to L-functions in the Selberg class (Aryan-type), to Dirichlet L-functions (simple zeros), to higher-order moments/pair correlation of zeros of derivatives, and to F(alpha) integrals in [1,beta] unconditionally (Carneiro et al. bounds with RH dropped using thin-box hypothesis).
- **Candidate connections.** Combine with CAND-01897: the unconditional F can replace RH in the Fourier-optimization bounds 0.9278<=integral F<=1.3302 under a thin-box or density hypothesis; with Lagarias-Rodgers (CAND-01989): AH-type models require F(alpha) beyond 1, outside Theorem 1. Link with zero-density estimates (Bourgain; Guth-Maynard) and the Selberg conjecture N(sigma,T)=O(T^{1-c(sigma-1/2)}sqrt(log T/loglog T)).
- **Reusable lemmas.** Lemma 3 (L^2 representation of F making positivity unconditional), Lemma 4 (non-RH truncation via zero-free region), Lemma 7 (decomposition into near-line and far-line pairs) are reusable for any pair-correlation argument; the AM-GM step T^{|beta-beta'|}<=(T^{|2beta-1|}+T^{|2beta'-1|})/2 reduces pair sums to one-zero sums.
- **Possible experiments.** Optimize the kernel j beyond Montgomery-Taylor by solving the associated extremal problem (maximize reduction ratio 2-(K-hat(0)+2 int alpha K-hat(alpha/2pi))/(2 pi K(0)) subject to j even, nonnegative, supp in [-1,1], K positive in the strip) to see whether 0.6175 can be increased; compute numerically the S(T) contribution from known zero data (all on-line, so S(T)=0) vs hypothetical off-line zeros to test sensitivity.
- **Risks / barriers.** The method cannot give any information about whether zeros are on the line; any improvement must come from better kernels or better density control. Reaching the RH-conditional 67.9% unconditionally seems to require controlling zeros with |beta-beta'| of order 1/log T, which is a genuine thin-box type statement.

## Audit notes (Level 1 reader)

none noticed in inspected portion except presentational points: (i) In the displayed definition (1.3) of F(alpha) the extraction duplicates the normalization T^{-1}/(log T/2pi); as written in the paper F(alpha)=(T/(2pi) log T)^{-1} F(T^alpha,T). (ii) Lemma 5's proof produces an error O(log log T/log T) in one term and O(1/sqrt(log T)) from Theorem 1; the stated final error O(1/sqrt(log T)) is consistent. (iii) In Section 7 the critical computations are numerical constants (1.291387636/0.929..., 1.289389678/0.932639...) not independently recomputed here beyond the arithmetic 2-1.289389678/(2*0.4663199124)=0.61748 which checks. (iv) Theorem 3's 'for any fixed eta>0' uses Bourgain only beyond 25/32+eta; hypothesis (1.6) restricted to 1/2+1/(2 log T)<=sigma<=25/32+eta is genuinely extra.

*These notes are a reader's observations, not verified findings; see `audits/` for adjudicated findings.*

## Provenance

- Candidate `CAND-02364`; harvest queries: kw_pair_correlation, kw_zero_density, kw_zeta_zeros, msc_11M06, msc_11M26, arxiv_critical_line, arxiv_pair_corr, arxiv_rh_abs, arxiv_zero_density, arxiv_zeta_zeros.
- Triage decision: include — Unconditional version of Montgomery pair correlation theorem.
- Record generated by `tools/make_records.py`; search cutoff 2026-11-17.
