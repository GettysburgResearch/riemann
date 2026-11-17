# PAPER-0059 — Explicit zero density estimate for the Riemann zeta-function near the critical line

| Field | Value |
|---|---|
| Authors | Simonič, Aleksander |
| Year / stratum | 2020 / S6 |
| Venue | J. Math. Anal. Appl. 491, No. 1, Article ID 124303, 40 p. (2020). |
| Identifiers | zbMATH [1469.11302](https://zbmath.org/?q=an:1469.11302) · DOI [10.1016/j.jmaa.2020.124303](https://doi.org/10.1016/j.jmaa.2020.124303) · arXiv [1910.08274](https://arxiv.org/abs/1910.08274) |
| MSC | 11M06, 11M26, 11Y35 |
| Families | A |
| Work type | original_paper |
| Evidence level of this record | **L1-partial** |
| Full text | partial_fulltext — https://arxiv.org/abs/1910.08274 |
| Selection | score 4.5425, in-pool citations 12, seed lists 0, triage relevance 4 |

## Mathematical content (Level 1: full text read)

**Research question.** Give a fully explicit version of Selberg's zero-density estimate N(sigma,T) << T^{1-(sigma-1/2)/4} log T near the critical line, together with explicit approximate functional equations for zeta and zeta^2 and an explicit upper bound for the second moment of zeta on the critical line.

**Historical motivation.** Selberg's near-critical-line zero density has no explicit version except Karatsuba-Korolev with non-explicit T_0; explicit zero-density estimates are needed for explicit prime-number-theorem error terms and S(t)/pair-correlation applications, but existing explicit ones (Kadiri, Kadiri-Lumley-Ng) are good only near the 1-line.

### Main results

- **THM-PAPER-0059-1** (Theorem 1, theorem, scope: asymptotic; Sec 1, Thm 1; proof Sec 4.5). Let $T\ge H_0=3.0610046\cdot10^{10}$ and $\sigma\in[1/2,0.831]$. Then $N(\sigma,2T)-N(\sigma,T)\le a\,T^{1-\frac14(\sigma-\frac12)}\log T+b\log^2T+c\log T\log\log T+d\log T$ with $a=10395.2,\ b=1.104,\ c=0.173,\ d=0.51$. Here N(sigma,T) counts zeros with real part >sigma and 0<Im<=T.
- **THM-PAPER-0059-2** (Corollary of Thm 1 (unnumbered), corollary, scope: asymptotic; Sec 1). For T>=2H_0: $N(\sigma,T)\le \frac{10395.21}{2^{1-\frac14(\sigma-\frac12)}-1}\,T^{1-\frac14(\sigma-\frac12)}\log\frac T2$; of interest only for sigma in (1/2,5/8] relative to Kadiri-Lumley-Ng bound (4).
- **THM-PAPER-0059-3** (Eq (5) (remark), theorem, scope: asymptotic; Sec 1, eq (5)). For larger verification height (T>=10^{50}) and sigma in [1/2,0.569]: $N(\sigma,2T)-N(\sigma,T)\le5.357\,T^{1-\frac14(\sigma-\frac12)}\log T+1.11\log^2T$; the method cannot give a leading constant below 3.259.
- **THM-PAPER-0059-4** (Theorem 4 / Theorem 6, theorem, scope: asymptotic; Sec 2, Thm 4, Tables 1-3; general-parameter version Thm 6). Explicit approximate functional equation $\zeta(s)=\sum_{n\le x}n^{-s}+\chi(s)\sum_{n\le y}n^{s-1}+R_1(s;x,y)$, $2\pi xy=|t|$, x,y>=1, sigma in [1/2,1], |t|>=2pi, with $|R_1|\le E x^{-\sigma}+F(|t|/2\pi)^{1/2-\sigma}y^{\sigma-1}$ and E,F tabulated (e.g. |t|>=2pi: E=36.094 (x<=y), F=127.126 (x>y); symmetric x=y: E=4.257; |t|>=10^3: 10.983/15.726/1.195).
- **THM-PAPER-0059-5** (Theorem 7, theorem, scope: asymptotic; Sec 3, Thm 7). For sigma in (1/2,sigma_0], T>=T_0>=2pi, coprime integers 1<=mu_1<=mu_2<=T/2pi, S(z)=\int_T^{2T}|\zeta(\sigma+it)|^2(2\mu_1/\mu_2)^{it}... dt; then $|S-\tilde S|\le S_1(z)(\mu_2/\mu_1)^\sigma T^{1-\sigma/2}\log\frac{T\mu_2}{\pi\mu_1}+S_2(z)\mu_1\mu_2T^{1-\sigma}\log\frac{T\mu_1\mu_2}{\pi}$ with main term tilde S = zeta(2sigma)/(mu1 mu2)^sigma T + ...; S_1,S_2 explicit and bounded for fixed sigma_0,T_0.
- **THM-PAPER-0059-6** (Corollary 5, corollary, scope: asymptotic; Sec 3, Cor 5). For T>=2pi, $\int_0^T|\zeta(1/2+it)|^2dt=T\log T-(1+\log2\pi-2\gamma)T+E(T)$ with $|E(T)|\le13.803\,T^{3/4}\log\frac T{2\pi}+83.964\sqrt T\log\frac T{2\pi}+2\cdot10^3\log T+3691.24$ (proof via T_0=10^3, T>=2T_0).
- **THM-PAPER-0059-7** (Corollary 1 / Corollary 4, corollary, scope: asymptotic; Sec 2 (Cor 1), Sec 3 (Cor 4)). Explicit approximate functional equations for zeta^2 (Dirichlet polynomials of length ~ |t|/2pi form) with explicit remainders for sigma in [1/2,1], |t|>=10^3.

### Principal lemmas

- **THM-PAPER-0059-L1** (Proposition 2; Sec 4). For sigma_0 in (1/2,1), T>=T_0, X=T^{1/6-eps}, 0<eps<=1/6-1/((sigma_0-1/2)log T_0) (garbled in extraction): $\int_T^{2T}|\Phi_X(\sigma+it)|^2dt\le T+\phi(\sigma_0,T_0,\epsilon,T)T^{1-2(1/6-\epsilon)(\sigma-1/2)}$ for sigma in [1/2+1/((1/6-eps)log T), sigma_0], where Phi_X is the Selberg mollified zeta (zeta times Dirichlet-polynomial mollifier). — *Role:* Explicit mean square of mollified zeta at height off the line; main input to Littlewood's lemma.
- **THM-PAPER-0059-L2** (Proposition 3; Sec 4). For U>=T_0>2sigma_1-1>=3.8, U not an ordinate of a zero of Phi_X: $|\arg\Phi_X(\sigma+iU)|\le\frac{\pi(\frac12+\sigma_1)}{2\log2}\log U+\frac{\pi\sigma_1}{2\log2}\log X+\frac{\pi}{2\log2}\log\log X+b_3$, sigma in (0,sigma_1]. — *Role:* Explicit bound for the argument of mollified zeta, needed for horizontal segments in Littlewood's lemma.
- **THM-PAPER-0059-L3** (Corollary 6 / Corollary 7; Sec 4). Corollary 7 (T or 2T not an ordinate of zero, X=T^{1/8}): $\frac1{2\pi}\int_\sigma^{\sigma_1}|\arg\Phi_X(\tau+2iT)|+|\arg\Phi_X(\tau+iT)|d\tau\le\frac1{2\pi}(\sigma_1-\frac12)\bigl(\frac{\pi(9\sigma_1+4)}{8\log2}\log T+\frac{\pi}{2\log2}\log\log T-\frac{\pi}{2}(11/2-\sigma_1)+2b_3\bigr)$. — *Role:* Explicit contributions of arguments at horizontal edges.
- **THM-PAPER-0059-L4** (Lemma 4, Lemma 6, Lemma 7; Sec 3 (Lemma 3-7)). Explicit versions of Montgomery-Vaughan-type mean value/large-sieve inequalities for Dirichlet polynomials (Lemma 4 with sequences a_n, n<=X) and oscillatory integral/sum lemmas. — *Role:* Control off-diagonal terms in Theorem 7 and Proposition 2.
- **THM-PAPER-0059-L5** (Lemma 10, Lemma 11; Sec 4). Explicit bounds for Dirichlet-series tails (sigma>=sigma_1>=2.4) and for zeta in the strip sigma in [1-sigma_1,sigma_1] used to bound log|Phi_X| on the right line. — *Role:* Anchor Littlewood's lemma at sigma_1>=2.4.

### Proof architecture

Follows Selberg's 1946 proof with H=T. (1) Explicit Hardy-Littlewood approximate functional equation (Thm 2-6) with uniform constants E,F. (2) Use it to prove explicit second-moment asymptotics with a twist (2 mu_1/mu_2)^{it} (Thm 7), hence explicit mean square of Selberg's mollifier Phi_X(s)=zeta(s)*mollifier, X=T^{1/6-eps} (Prop 2). (3) Apply Littlewood's lemma to Phi_X (count zeros of Phi_X, which include zeros of zeta, in rectangles sigma..sigma_1): integral of N(tau,2T)-N(tau,T) dtau bounded by mean square of log|Phi_X| (Jensen) plus argument bounds (Prop 3, Cor 7) (Sec 4.5, eq 73). (4) Handle sigma in [1/2,1/2+8/log T] trivially via the Riemann-von Mangoldt count (1) and pass from integrated to pointwise bound using monotonicity of N(sigma,T). Parameters eps=1/24, T_0=e^{24}. Imported: explicit Riemann-von Mangoldt (Platt-Trudgian, Trudgian), Platt's RH height H_0, Arias de Reyna explicit Riemann-Siegel bounds for the symmetric case, Hardy-Littlewood/Siegel classical AFE.

Dependency edges: CAND-01828 → Selberg 1946 zero density near critical line (makes_explicit); CAND-01828 → Kadiri-Lumley-Ng 2018 (complements); CAND-01818 → CAND-01828 (related_but_uses_different_density)

**Imported results.** Platt 2017: RH verified for |Im rho|<=H_0=3.0610046e10; Platt-Trudgian/Trudgian explicit Riemann-von Mangoldt: N(T) bound (1); Arias de Reyna 2011 explicit Riemann-Siegel remainder (symmetric AFE constants); Selberg 1946 N(sigma,T) strategy; Hardy-Littlewood AFE; Siegel 1932 formula

**Techniques.** Selberg mollifier; Littlewood's lemma for zero counting; explicit approximate functional equation via Hardy-Littlewood/Siegel; explicit second moment with twist; explicit Montgomery-Vaughan mean value; explicit Riemann-von Mangoldt formula

## Context and interpretation

**Importance and obstacle overcome.** Provides the first fully explicit Selberg-type bound near sigma=1/2, with explicit constant a=10395.2 and domain T>=H_0, sigma<=0.831. Obstacle: obtaining explicit mean square of the mollified zeta off the critical line required an explicit approximate functional equation in the unbalanced case x != y and an explicit second-moment bound with twists.

**Relation to prior work.** 

**Limitations and open questions.** Constant a=10395.2 is large; method cannot go below 3.259. Selberg's exponent 1/4 (Jutila 1-eps, Conrey 8/7-eps) not improved. Useful only for sigma in (1/2,5/8] relative to (4). The density conjecture would need constant 2 in place of 1/4 in the exponent, not reached.

## Research potential

- **Hypotheses that might be weakened.** T>=H_0 via Platt-Trudgian new height 2.5e12/3e12; sigma range up to 0.831 (higher sigma superseded by Ingham-type); raising the Selberg mollifier length X=T^{1/6-eps} with eps=1/24 optimization.
- **Generalizations.** Explicit Selberg-type zero density for Dirichlet L-functions (needs explicit AFE and second moment for L(s,chi)); Jutila/Conrey exponent explicit versions.
- **Candidate connections.** Feeds explicit PNT error terms in zero-density approach (Johnston-Yang, CAND-01818, uses KLN-type density near 1 rather than this one); local zero census for RH verification programmes (distinction: finite verification vs global statements).
- **Reusable lemmas.** Theorem 4/6 (explicit unbalanced approximate functional equation with tabulated E,F) and Corollary 5 (explicit mean square with 3/4 power error) are reusable lemmas for any explicit zeta moment argument.
- **Possible experiments.** Recompute a(T_0) and Table values with the updated verification height and with exact mollifier optimization; numerically test the explicit mean square bound Cor 5 against Odlyzko-type data for T up to 1e8 to see how sharp 13.803 T^{3/4} log is.
- **Risks / barriers.** Selberg-type zero density near 1/2 does not yield RH or even positive proportion; constants huge. Must not be read as unconditional zero-free statement.

## Audit notes (Level 1 reader)

The extracted text shows 'T>=1050' in remark (5) likely meaning T>=10^50 (superscript lost); the leading exponent notation in the abstract and Theorem 1 is garbled by extraction (checked against stated Selberg form T^{1-(sigma-1/2)/4}). Proposition 2 parameter conditions garbled in extraction; not independently reconstructed. Proof details Sec 2-4 not read line by line. Otherwise none noticed in inspected portion.

*These notes are a reader's observations, not verified findings; see `audits/` for adjudicated findings.*

## Provenance

- Candidate `CAND-01828`; harvest queries: kw_zero_density, msc_11M06, msc_11M26, msc_11Y35, arxiv_critical_line.
- Triage decision: include — Explicit Selberg zero-density near the critical line.
- Record generated by `tools/make_records.py`; search cutoff 2026-11-17.
