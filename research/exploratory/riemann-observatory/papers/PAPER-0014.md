# PAPER-0014 — Zeros of principal \(L\)-functions and random matrix theory

| Field | Value |
|---|---|
| Authors | Rudnick, Zeév; Sarnak, Peter |
| Year / stratum | 1996 / S4 |
| Venue | Duke Math. J. 81, No. 2, 269-322 (1996). |
| Identifiers | zbMATH [0866.11050](https://zbmath.org/?q=an:0866.11050) · DOI [10.1215/S0012-7094-96-08115-6](https://doi.org/10.1215/S0012-7094-96-08115-6) |
| MSC | 11M50, 11M26, 11F66, 11F70, 11M41 |
| Families | B, E |
| Work type | original_paper |
| Evidence level of this record | **L1** |
| Full text | fulltext_read — https://www.math.tau.ac.il/~rudnick/papers/nlevelDuke.pdf (text read from https://empslocal.ex.ac.uk/people/staff/mrwatkin/zeta/rudnick-sarnak.pdf, 54-page scan of Duke Math. J. 81 (1996) 269-322) |
| Selection | score 4.6112, in-pool citations 165, seed lists 3, triage relevance 5 |

## Mathematical content (Level 1: full text read)

**Research question.** For primitive principal L-functions L(s,\pi) of cuspidal automorphic representations of GL_m/\mathbb Q, do the n-level correlations of the normalized zeros follow the GUE (Dyson determinant) law, universally in \pi, for test functions with restricted Fourier support?

**Historical motivation.** Montgomery's pair correlation and Odlyzko's numerics suggested GUE; Hejhal did n=3 for zeta; the paper establishes all n for all principal L-functions, and shows universality despite non-universal coefficient distributions (Sato-Tate etc.).

### Main results

- **THM-PAPER-0014-1** (Theorem 1.1, theorem, scope: asymptotic; Introduction, Theorem 1.1 (pp. 4-5)). Let $\pi$ be a cuspidal automorphic representation of $GL_m/\mathbb Q$ and assume $m\le3$ or Hypothesis (1.7) (equivalently H: $\sum_p |a_\pi(p^k)\log p|^2/p^k<\infty$ for each fixed $k\ge2$). Let $f$ satisfy TF1-3 (symmetric; $f(x+t\mathbf 1)=f(x)$; rapid decay on $\sum x_j=0$) and $\mathrm{supp}\,\hat f\subset\{\xi:\sum_j|\xi_j|<2/m\}$. Let $g\in C_c^\infty(\mathbb R)$, $h(r)=\int g(u)e^{iru}du$. Then as $T\to\infty$, $R_n(T,f,h)\sim\frac{m}{2\pi}T\log T\int_{-\infty}^\infty h(r)^ndr\int_{\mathbb R^n}f(x)W_n(x)\delta\big(\tfrac{x_1+\dots+x_n}{n}\big)dx$, where $R_n(T,f,h)=\sum^{\ne}h(\gamma_{j_1}/T)\cdots h(\gamma_{j_n}/T)f(\tfrac L{2\pi}\gamma_{j_1},\dots)$, $L=m\log T$, $W_n=\det K(x_i-x_j)$, $K(x)=\sin\pi x/\pi x$. No RH needed.
- **THM-PAPER-0014-2** (Theorem 1.2, theorem, scope: asymptotic; Introduction, Theorem 1.2 (p. 5)). With the assumptions of Theorem 1.1 and RH for $L(s,\pi)$: $R_n(B_N,f)\to\int_{\mathbb R^n}f(x)W_n(x)\delta(\tfrac{x_1+\dots+x_n}{n})dx$ as $N\to\infty$, where $B_N$ are the first $N$ normalized zeros $\tilde\gamma=\frac m{2\pi}\gamma\log|\gamma|$. *Conditional on:* RH for L(s,\pi).
- **THM-PAPER-0014-3** (Proposition 2.4, proposition, scope: global; Section 2.4, p. 17). Hypothesis H holds for $1\le m\le3$ (proved using $|\alpha_\pi(j,p)|\le p^{1/2-1/(m^2+1)}$ from (2.3), $|\alpha_2|=1$, $|\alpha_3|=1/|\alpha_1|$ for $m=3$, and Rankin-Selberg).
- **THM-PAPER-0014-4** (Proposition 2.2 / 2.3, proposition, scope: asymptotic; Section 2.4, pp. 15-17). Assuming H, $\sigma(x)\sim(\log x)^2/2$ and $\sum_{n\le x}|c_\pi(n)|^2/n=\tfrac12\log^2x+O(\log x)$ where $c_\pi(n)=\Lambda(n)a_\pi(n)$. This second-moment universality (independent of $\pi$) is the source of universality of GUE. *Conditional on:* H.
- **THM-PAPER-0014-5** (Theorem 3.1, theorem, scope: asymptotic; Section 3, p. 20 (eq. 3.8-3.9)). For $\Phi\in C^1(\mathbb R^n)$ supported in $\sum|\xi_j|<2/m$ and $f(x)=\int\Phi(\xi)\delta(\xi_1+\dots+\xi_n)e(-x\cdot\xi)d\xi$: $\sum_{\text{all indices}}h_1(\tfrac{\gamma_1}T)\cdots h_n(\tfrac{\gamma_n}T)f(\tfrac L{2\pi}\gamma_1,\dots)=\kappa(h)\frac{TL}{2\pi}\int\Phi(v)C_O(v)dv+O(T)$, with $\int\Phi C_O=\Phi(0)+\sum_{r=1}^{[n/2]}\sum_{\text{r disjoint pairs}}\int\cdots\int|v_1|\cdots|v_r|\Phi(v_1e_{i(1),j(1)}+\dots+v_re_{i(r),j(r)})dv$.
- **THM-PAPER-0014-6** (Theorem 3.2, theorem, scope: asymptotic; Section 3, p. 20). Assuming RH for $L(s,\pi)$ and $\Phi\in C^2$ supported in $\sum|\xi_j|<2/m$, the unrestricted-in-height sums satisfy $C_n(f,T)\sim N(T)\int\Phi(u)C_O(u)du+O(T)$. *Conditional on:* RH for L(s,\pi).
- **THM-PAPER-0014-7** (Theorem 4.1 (with Props 4.1-4.3), theorem, scope: finite; Section 4, pp. 43-44). For $\sum_j|u_j|<2$, the Fourier transform $\hat W_n(u)$ of the GUE determinant $W_n(x)=\det K(x_i-x_j)$ equals $R_O(u)$, the combinatorial sieved prime-pair expression (4.16). Proposition 4.3: for $S$ with $\sum_{l\in S}u_l=0$, $\sum|u_l|<2$, $X_S(u)=(-1)^{|S|-1}Y_S(u)$.

### Key definitions

- principal (primitive) L-function: attached to cuspidal $\pi$ on $GL_m/\mathbb Q$
- n-level correlation $R_n(B_N,Q)=\frac1N\#\{$distinct $j_1..j_n: (\tilde\gamma_{j_1}-\tilde\gamma_{j_2},..)\in Q\}$
- TF1-3
- $W_n$ GUE density
- Hypothesis H / (1.7)
- $c_\pi(n)=\Lambda(n)a_\pi(n)$

### Principal lemmas

- **THM-PAPER-0014-L1** (Proposition 2.1 (Explicit Formula); Section 2.3, eq. (2.16)). For $g\in C_c^\infty$, $h(r)=\int g(u)e^{iru}du$: $\sum h(\gamma_\pi)=\delta(\pi)\{h(-i/2)+h(i/2)\}+\frac1{2\pi}\int h(r)\big(\log Q_\pi+\sum_j\tfrac{\Gamma_R'}{\Gamma_R}(\tfrac12+\mu_\pi(j)+ir)+\tfrac{\Gamma_R'}{\Gamma_R}(\tfrac12+\mu_\pi(j)-ir)\big)dr-\sum_n\tfrac{c_\pi(n)}{\sqrt n}g(\log n)+\tfrac{c_{\tilde\pi}(n)}{\sqrt n}g(-\log n)$. — *Role:* Converts zero sums to prime sums.
- **THM-PAPER-0014-L2** (Rankin-Selberg facts RS1-RS3 / Prop 5.1 / eq. (2.3); Section 2.1 and Appendix 5.4). Bound $|\alpha_\pi(j,p)|\le p^{1/2-1/(m^2+1)}$ at all finite p, obtained by a global argument via Rankin-Selberg $L(s,\pi\times\tilde\pi)$. — *Role:* Controls prime-power terms and ramified places; proves H for m<=3.
- **THM-PAPER-0014-L3** (Lemmas 3.4-3.9; Section 3, pp. 25-33). Estimates for sums over prime tuples $n_1\cdots n_r=n_{r+1}\cdots n_{r+s}$ ($C_{r,s}(T)$): only distinct primes matter (Lemma 3.8), and $C_{r,s}(T)=O(T)$ unless $r=s>0$ (Lemma 3.9/3.10). Statements skimmed, not read in detail. — *Role:* Show off-diagonal contributions are lower order inside the support region.
- **THM-PAPER-0014-L4** (Lemma 3.10; Section 3, pp. 33-34). $C_{r,s}(T)=O(T)$ unless $r=s>0$; for $r=s$, $C_{r,r}(T)=\frac{TL}{2\pi}\kappa(h)\sum_{\sigma\in S_r}\int_0^{1/m}\!\!\cdots\!\int_0^{1/m}v_1\cdots v_r\,\Phi(-v_1,..,-v_r,v_{\sigma(1)},..,v_{\sigma(r)},0,..,0)dv+O(T)$. — *Role:* Identifies the diagonal main terms (permutation pairings).
- **THM-PAPER-0014-L5** (Lemma 4.4 (Spitzer, Thm 2.1 of [34]); Section 4). For $u=(u_1,\dots,u_r)$ in generic position there is a unique cyclic rotation whose random walk lies below its chord. — *Role:* Drives the identity of Prop 4.3 matching the pairing structure to cycle structure of the determinant.
- **THM-PAPER-0014-L6** (Proposition 4.1; Section 4, p. 43). $\sum_F\mu(O,F)C_F(u)=\sum_F\delta_F(u)\prod_{j}X_{F_j}(u)$ with $X_S(u)=(-1)^{|S|-1}(|S|-1)!+(-1)^{|S|-2}\sum_{S=S^+\cup S^-}(|S^+|-1)!(|S^-|-1)!\,|\sum_{l\in S^+}u_l|$. — *Role:* Moebius inversion over the partition lattice to distinct indices.
- **THM-PAPER-0014-L7** (Proposition 4.2; Section 4, p. 44). $\hat W_n(u)=\sum_F\delta_F(u)\prod_j(-1)^{|F_j|-1}Y_{F_j}(u)$ with $Y_S(u)=\sum_{\text{cyclic perms}}\int f_2(v)f_2(v+u_{i_1})\cdots f_2(v+u_{i_1}+..+u_{i_m})dv$, $f_2=\mathbf 1_{[-1/2,1/2]}$. — *Role:* Expands the Fourier transform of the sine-kernel determinant by cycles.

### Proof architecture

(1) Section 2: background on cuspidal GL_m L-functions, functional equation, explicit formula (Prop 2.1), Rankin-Selberg theory giving the second-moment asymptotic $\sum|c_\pi(n)|^2/n\sim\frac12\log^2x$ under H (Props 2.2-2.4). (2) Section 3: apply the explicit formula n times with test functions $h(r/T)e^{-irL\xi}$, obtain n-fold sums over prime powers; using $\sum|\xi_j|<2/m$ the only main terms are diagonal pairings $n_1\cdots n_r=n_{r+1}\cdots n_{r+s}$ with $r=s$ (Lemma 3.10), yielding Theorem 3.1 (smooth, unconditional) and Theorem 3.2 (RH, sharp cutoff). (3) Section 4: sieving from all-index sums to distinct-index sums via Moebius function on set-partition lattice (Prop 4.1), and identification of the result with the Fourier transform of $\det K$ (Prop 4.2, 4.3) using Spitzer's lemma (Lemma 4.4). Theorem 1.1 then follows from 3.1 and Thm 4.1; Theorem 1.2 follows by an approximation argument. Appendix computes Rankin-Selberg local factors at ramified places and proves bounds (2.3), (2.5).

Dependency edges: CAND-00720 → CAND-00864 (full proofs and GL(m) generalization of); CAND-00720 → CAND-00743 (extends n=3 case to all n); CAND-00750 → CAND-00720 (heuristic extension past support restriction)

**Imported results.** Godement-Jacquet: entire continuation and functional equation of Phi(s,pi); Jacquet-Piatetski-Shapiro-Shalika: Rankin-Selberg convolutions L(s,pi x pi') with nonvanishing/analytic properties on Re s>=1; Jacquet-Shalika bound |alpha|<p^{1/2}; Dyson 1962: determinantal n-level density of GUE; Montgomery 1973 (n=2 case); Spitzer 1956 combinatorial lemma; Gelfand-Kazhdan/Shalika: local components of cuspidal reps are generic

**Techniques.** smooth explicit formula; Rankin-Selberg second moment; diagonal pairing from unique factorization; Moebius inversion on set partitions; Spitzer's combinatorial lemma; local Langlands/Rankin-Selberg at ramified places

## Context and interpretation

**Importance and obstacle overcome.** Landmark theorem on the fine statistics of zeros of general L-functions. Obstacles: (i) deriving the determinantal form of GUE from sums over primes (solved by partition-lattice sieving plus Spitzer); (ii) uniformity in pi: only the second moment of the coefficients enters, supplied by Rankin-Selberg theory; (iii) avoiding RH by a smoothed formulation.

**Relation to prior work.** Generalizes Montgomery 1973 (n=2, zeta) and Hejhal 1994 (n=3, zeta); extends to Dirichlet and GL_m L-functions (cf. Rumely's numerics for Dirichlet). Announced in CRAS 319 (CAND-00864). Bogomolny-Keating (CAND-00750) give a Hardy-Littlewood-based heuristic beyond the support restriction. Remark 2 shows zeros of distinct primitive L-functions are uncorrelated, so products are not GUE.

**Limitations and open questions.** Support restriction $\sum|\xi_j|<2/m$ (for $m=1$ natural; for $m\ge2$ the authors expect diagonals dominate up to $\sum|\xi_j|<2$, a heuristic via eqs. (3.67)-(3.69) using square-root cancellation in shifted correlations of $a(m)a(m+h)$). Removing the restriction is conjectured to hold (full universality) but open. Hypothesis H needed for $m\ge4$. Primitivity is crucial (Remark 2). Statements concern local statistics and do not give information on RH.

**Ideas in remarks/appendices/abandoned paths.** Remark 1 (Section 3, eqs. 3.67-3.70): heuristic that for GL(2) cusp forms the off-diagonal term is bounded by $T^{\xi-1}\log^2T$ under square-root cancellation in shifted sums, versus Dirichlet characters where twin-prime-type conjectures (3.70) give no cancellation; this explains why the zeta/Dirichlet range $<2$ is sharp for diagonal dominance. Remark 2: zeros of distinct primitive L-functions are uncorrelated, predicting superposition of independent GUEs for products.

## Research potential

- **Hypotheses that might be weakened.** (a) Hypothesis H for m>=4 (follows from Ramanujan or from any bound $|a(p^k)|\ll p^{\theta}$ with small $\theta$; could be derived from better Luo-Rudnick-Sarnak bounds). (b) Support $2/m$ to $2$ for m>=2 requires nontrivial bounds on shifted sums $\sum c(m)c(m+h)$ (eq. 3.68); a cheap partial gain would come from known GL(2) shifted-convolution (Kloosterman/spectral) bounds. (c) RH for $L(s,\pi)$ only needed for sharp cutoff.
- **Generalizations.** Number field base (later work), families, derivative/mollified correlations; joint statistics of zeros of two non-equivalent L-functions (Remark 2, uncorrelated claim).
- **Candidate connections.** Extension beyond support via Hardy-Littlewood (Bogomolny-Keating, CAND-00750; Conrey-Snaith arXiv:math/0610495 for triple correlation); the diagonal-pairing computation parallels the Katz-Sarnak family statistics.
- **Reusable lemmas.** Props 4.1-4.3 and Lemma 4.4 (partition-lattice sieve + Spitzer) for any correlation computation; Prop 2.3 second-moment asymptotic of $\Lambda(n)a_\pi(n)$.
- **Possible experiments.** Test numerically the conjectured widening to $\sum|\xi_j|<2$ for degree 2 L-functions (CM and non-CM, holomorphic and Maass), as the authors themselves suggest in Remark 1; compute $R_3$ with Fourier support in $(2/m,2)$.
- **Risks / barriers.** Pure local statistics, cannot imply RH; extending support past $\sum|\xi|=2$ hits genuine off-diagonal terms (Hardy-Littlewood) equivalent to hard conjectures; no implication for nearest-neighbour spacing or small gaps without full support.

## Audit notes (Level 1 reader)

none noticed in inspected portion. Minor: the intro text states the zero counting function as $N_\pi(T)\sim\frac mpi T\log T$ (eq. 2.11, for $|{\rm Im}\rho|<T$, consistent with the stated density $\frac m{2\pi}\log T$ per unit height); OCR of displayed formulas is imperfect so reconstructed formulas should be checked against the printed paper.

*These notes are a reader's observations, not verified findings; see `audits/` for adjudicated findings.*

## Provenance

- Candidate `CAND-00720`; harvest queries: kw_RH_any, kw_weil_positivity, kw_zeta_zeros, msc_11M26, msc_11M50.
- Triage decision: include — Landmark n-level correlations of zeros match GUE for all n.
- Record generated by `tools/make_records.py`; search cutoff 2026-11-17.
