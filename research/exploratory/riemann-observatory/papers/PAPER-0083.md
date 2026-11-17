# PAPER-0083 — Effective approximation of heat flow evolution of the Riemann \(\xi \) function, and a new upper bound for the de Bruijn-Newman constant

| Field | Value |
|---|---|
| Authors | Polymath, D. H. J. |
| Year / stratum | 2019 / S6 |
| Venue | Res. Math. Sci. 6, No. 3, Paper No. 31, 67 p. (2019). |
| Identifiers | zbMATH [1423.30022](https://zbmath.org/?q=an:1423.30022) · DOI [10.1007/s40687-019-0193-1](https://doi.org/10.1007/s40687-019-0193-1) · arXiv [1904.12438](https://arxiv.org/abs/1904.12438) |
| MSC | 30D20, 30C15 |
| Families | B, C, F |
| Work type | original_paper |
| Evidence level of this record | **L1-partial** |
| Full text | partial_fulltext — https://arxiv.org/abs/1904.12438 |
| Selection | score 4.4205, in-pool citations 7, seed lists 4, triage relevance 5 |

## Mathematical content (Level 1: full text read)

**Research question.** How to obtain effective, numerically checkable approximations of the heat flow H_t(z)=int_0^infty e^{tu^2}Phi(u)cos(zu)du of the Riemann xi function in the region 0<t<=1/2, 0<=y<=1, x>=200, and use them together with zero-dynamics and the known numerical verification of RH to improve the upper bound for the de Bruijn-Newman constant Lambda?

**Historical motivation.** de Bruijn 1950 (Lambda<=1/2), Newman 1976 conjecture Lambda>=0, Rodgers-Tao 2018 proof of Lambda>=0, Ki-Kim-Lee Lambda<1/2, Csordas-Smith-Varga zero dynamics; Polymath15 project led by Tao.

### Main results

- **THM-PAPER-0083-1** (Theorem 1.1, theorem, scope: computational; Sec. 1, Sec. 8). $\Lambda\le0.22$ (unconditional). Combined with Rodgers-Tao $\Lambda\ge0$ and RH$\Leftrightarrow\Lambda\le0$. *Conditional on:* Platt's numerical RH verification up to T=3.06e10, correctness of the interval-arithmetic zero-free certificates for H_t in regions (b),(c).
- **THM-PAPER-0083-2** (Theorem 1.2 (Upper bound criterion), theorem, scope: finite; Sec. 1 p.2; proof Sec. 3 (Prop 3.3 + de Bruijn Thm 3.2)). Let $t_0,X>0$, $0<y_0\le1$. Suppose (i) no zeros $\zeta(\sigma+iT)=0$ with $\frac{1+y_0}{2}\le\sigma\le1$, $0\le T\le X/2$; (ii) no zeros of $H_{t_0}(x+iy)$ with $x\ge\sqrt{X+1-y_0^2}$, $y_0\le y\le\sqrt{1-2t_0}$; (iii) no zeros of $H_t(x+iy)$ with $X\le x\le\sqrt{X+1-y_0^2}$, $\sqrt{y_0^2+2(t_0-t)}\le y\le\sqrt{1-2t}$, $0\le t\le t_0$. Then $\Lambda\le t_0+\tfrac12y_0^2$ (barrier-region criterion; as printed the X-thresholds are in extracted form and the barrier is x in [X, sqrt(X+1-y0^2)] shape).
- **THM-PAPER-0083-3** (Theorem 1.3 (Effective Riemann-Siegel approximation), theorem, scope: finite; Sec. 1 pp.5-6; proof Sec. 6). For $0<t\le1/2$, $0\le y\le1$, $x\ge200$: $\frac{H_t(x+iy)}{B_t(x+iy)}=f_t(x+iy)+O_{\le}(e_A+e_B+e_{C,0})$ with $f_t=\sum_{n\le N}\frac{b_n^t}{n^{s_*}}+\gamma\sum_{n\le N}\frac{b_n^t}{n^{\bar s_*...}}$ (as in (14)), $b_n^t=\exp(\frac t4\log^2n)$, $N=\lfloor\sqrt{x/4\pi+t/16}\rfloor$, $B_t(x+iy)=M_t(\frac{1+y-ix}2)$, $M_t(s)=\exp(\frac t4\alpha(s)^2)M_0(s)$, and explicit error terms e_A,e_B,e_{C,0} (eqs (23),(24), (71)-(74)); with $|\gamma|\le e^{0.02y}(x/4\pi)^{-y/2}$, $\Re s_*\ge...$, $|\kappa|\le ty/(2(x-6))$.
- **THM-PAPER-0083-4** (Corollary 1.4, corollary, scope: finite; Sec. 1 p.7, (25)). If $|f_t(x+iy)|>e_A+e_B+e_{C,0}$ in region (5) then $H_t(x+iy)\ne0$. *Conditional on:* Theorem 1.3.
- **THM-PAPER-0083-5** (Theorem 1.5 (Distribution of zeros of H_t), theorem, scope: asymptotic; Sec. 1 pp.9-10; proof Sec. 9). Let $0<t\le1/2$, C large, c small absolute constants; $g(x,t)=\frac x{4\pi}\log\frac x{4\pi}-\frac x{4\pi}+\frac{11}8+\frac t{16}\log\frac x{4\pi}$, $x_n$ the unique solution $>4\pi$ of $g(x_n,t)=n$. (i) If $x\ge\exp(C/t)$ and $H_t(x+iy)=0$ then $y=0$ and $x=x_n+O(x^{-ct})$ for some n. (ii) For $n\ge\exp(C/t)$ there is exactly one zero in $|z-x_n|\le\log^{-c}x_n$ (real, within $O(x^{-ct})$ of $x_n$). (iii) For $X\ge\exp(C/t)$: $N_t(X)=g(X,t)+O(1)$. (iv) For all $X\ge0$: $N_t(X+1)-N_t(X)\le O(\log(2+X))$ and $N_t(X)=g(X,t)+O(\log(2+X))$.
- **THM-PAPER-0083-6** (Table 1 (Sec. 10), computation, scope: conditional; Sec. 10, Table 1). Conditional on numerical RH verification to height T (e.g. $T\approx4.5\times10^{21}$), one obtains $\Lambda\le0.1$ using $X=9\times10^{21}+70686$, $t_0=0.093$, $y_0=0.11832$; intermediate rows give $\Lambda\le0.21,\dots,0.11$. Heuristic: $\Lambda\le O(1/\log T)$ is the natural limit. *Conditional on:* numerical verification of RH to the listed heights.

### Key definitions

- $H_t(z)=\int_0^\infty e^{tu^2}\Phi(u)\cos(zu)du$, $\Phi(u)=\sum_{n\ge1}(2\pi^2n^4e^{9u}-3\pi n^2e^{5u})\exp(-\pi n^2e^{4u})$, $H_0(z)=\xi(\tfrac12+\tfrac{iz}2)$ (up to the 1/8 normalisation in (1))
- $\Lambda=\inf\{t:H_t\text{ has only real zeros}\}$
- $M_0(s)=\frac18\frac{s(s-1)}2\pi^{-s/2}\sqrt{2\pi}\exp(\frac s2\mathrm{Log}\frac s2-\frac s2)$, $M_t=\exp(\frac t4\alpha^2)M_0$, $\alpha=(\log M_0)'$, $B_t(x+iy)=M_t(\frac{1+y-ix}2)$
- $O_\le(X)$: quantity bounded in modulus by X

### Principal lemmas

- **THM-PAPER-0083-L1** (Proposition 3.1; Sec. 3, (28)-(30)). (i) At a simple zero $z_j(t_0)$ of $H_{t_0}$: $\frac{dz_j}{dt}=2\sum'_{k\ne j}\frac1{z_j-z_k}$. (ii) At a zero of order $m\ge2$ the m zeros nearby behave as $z_j+\sqrt{2}(t-t_0)^{1/2}\lambda_i+O(|t-t_0|)$ with $\lambda_i$ the roots of Hermite polynomial $He_m$. — *Role:* Zero dynamics for all t (including complex or repeated zeros, i.e. t<=Lambda), extending Csordas-Smith-Varga.
- **THM-PAPER-0083-L2** (Theorem 3.2 (de Bruijn [5, Thm 13]); Sec. 3). If $H_{t_0}$ has no zeros $x+iy$ with $x\in\mathbb R$, $y>y_0$, then for $t>t_0$ no zeros with $y>\max(y_0^2-2(t-t_0),0)^{1/2}$; in particular $\Lambda\le t_0+\frac12y_0^2$. — *Role:* Converts a zero-free 'canopy' at time t_0 into a bound on Lambda.
- **THM-PAPER-0083-L3** (Proposition 3.3; Sec. 3, (34)). Under hypotheses (i)-(iii) (barrier region version) there are no zeros of $H_{t_0}(x+iy)$ with $y\ge y_0$. — *Role:* Barrier/continuity argument: first time t_1 a zero crosses the boundary Y(t)=sqrt(y_0^2+2(t_0-t)) forces dY/dt=-1/Y > Im dz/dt, using (28) and y_k^2<= (x-x_k)^2+Y^2 for zeros outside the barrier, a contradiction.
- **THM-PAPER-0083-L4** (Proposition 6.1/6.2/6.3; Sec. 6). Effective estimates for the main terms r_{t,n} and the remainder R_{t,N} in the Riemann-Siegel-type decomposition obtained from a saddle-point contour shift after writing H_t as a Gaussian convolution of H_0. — *Role:* Core analytic estimates for Theorem 1.3.
- **THM-PAPER-0083-L5** (Lemma 8.2, Lemma 8.5 (improved triangle inequality); Sec. 7-8). Fast numerical bounds for sums f_t via Taylor expansion over multiple x and Euler-product mollification (Sec. 8.5, Sec. 7 fast evaluation of multiple sums). — *Role:* Make verification of (ii),(iii) at X~6e10 feasible.
- **THM-PAPER-0083-L6** (Proposition 9.1; Sec. 9). Asymptotics $e_A,e_B,e_{C,0}=O(x^{-ct})$, $f_t=1+O(x^{-ct})$ for fixed t,y and x large (region of x >= 200, |y|<=10). — *Role:* Feeds Theorem 1.5.

### Proof architecture

Theorem 1.1 follows from the criterion Thm 1.2 with t_0=0.2, y_0=0.2, X=6e10+83952-0.5. Hypothesis (i) is Platt's RH verification (height 3.06e10, zeros sigma>=0.6); (ii) and (iii) are verified by computer using Corollary 1.4 / the Riemann-Siegel approximation Thm 1.3, with the quotient H_t/B_t used to remove the e^{-pi x/8} decay, Taylor-expanded evaluation, Euler-product mollification (shift 83952 chosen to make the partial Euler product large), and argument-principle/winding-number checks in some subregions. Thm 1.2 itself rests on Prop 3.3 (barrier at x in [X, ...]) plus de Bruijn's Theorem 3.2. Thm 1.3 is obtained by convolving H_0's Riemann-Siegel expansion with the Gaussian heat kernel and using saddle-point contour shifts with effective error terms. Thm 1.5 follows from Prop 9.1 asymptotics and Lemma 9.2 on M_t.

**Imported results.** de Bruijn Theorem 13 (zero-free canopy => Lambda bound), Thm 3.2; Platt: RH verified for 0<T<=3.06e10 (with zeros in sigma>=... ) [18]; Newman/de Bruijn: existence and defining property of Lambda; Polya monotonicity in t; Rodgers-Tao: Lambda>=0; Hadamard factorisation of order-1 entire functions; Standard Riemann-Siegel/Stirling asymptotics (effective versions proved in Sec. 5-6)

**Techniques.** backwards heat equation partial_t H_t=-H_t''; zero-dynamics dz_j/dt=2 sum 1/(z_j-z_k) and barrier/continuity argument; effective Riemann-Siegel with explicit error terms O_<=; saddle point method with explicit constants; normalisation by Stirling-type Gamma factor B_t=M_t((1+y-ix)/2); Taylor expansion for fast simultaneous evaluation, Euler-product mollifier; argument principle / winding number certification; interval arithmetic computation

## Context and interpretation

**Importance and obstacle overcome.** First effective-uniform asymptotic/Riemann-Siegel approximation of the heat flow H_t with explicit constants for t>0 and moderate x, giving the first improvement of de Bruijn's 1/2 (Ki-Kim-Lee: <1/2) to 0.22, and a conditional dictionary RH verified to height T => Lambda <= O(1/log T). Obstacle: exponential decay of H_t in x requiring huge precision; overcome by dividing by B_t and the barrier method that reduces the problem to a compact region plus asymptotics.

**Relation to prior work.** Improves Ki-Kim-Lee (Lambda<1/2) and de Bruijn; Theorem 1.5 refines Ki-Kim-Lee Theorems 1.3-1.4 with effective, uniform constants; relies on Platt's numerical RH verification and de Bruijn Thm 13; complements Rodgers-Tao lower bound.

**Limitations and open questions.** Bound 0.22 is limited by (a) the height 3.06e10 of rigorous RH verification (needed for (i)) and (b) the numerical feasibility of verifying (ii) for t_0,y_0 near 0.2. Heuristic in Sec. 10: Lambda<=O(1/log T) from RH verified to height T; improvement beyond this would require excluding RH violations at height T (a breakthrough in zero-free regions). The main theorem is conditional on computer verification (not independently re-run here).

**Ideas in remarks/appendices/abandoned paths.** Remark 1.6 (gas/liquid/solid analogy of zeros of H_t; zeros 'solidify' for x>=exp(C/t)). Sec. 10 heuristic argument that Lambda=O(1/log T) is the natural barrier. Sec. 1: a correction term -C_t/B_t gives an even more accurate approximation with smaller error e_C (eq. (69), Figure 8). Final remark in Sec. 1: Theorem 1.5 conclusion suggests N_t(X)=g(X,t)+O(X^{-ct}) after removing the sawtooth. Sec. 8.1: choice of X by making Euler product prod_{p<=11}(1-1/p^{(1-iX)/2})^{-1} large (ad hoc search over q<=1e5, seven candidates).

## Research potential

- **Hypotheses that might be weakened.** Hypothesis (i) of Theorem 1.2 can be replaced by any zero-free region result for zeta in {(1+y_0)/2<=sigma<=1, T<=X/2}; an explicit zero-density/zero-free region improvement at moderate height would directly lower Lambda. Hypothesis y_0<=1 and region (5) constants (1/2,1,200) were chosen arbitrarily.
- **Generalizations.** The barrier method and Thm 1.3-type effective approximation should adapt to heat flows of other L-functions (Dirichlet L, Hecke, Selberg class members with Riemann-Siegel formulas), giving explicit Lambda bounds for generalised de Bruijn-Newman constants; Theorem 1.5's 'solidification' of zeros for x>=exp(C/t) is a candidate lemma for study of Lambda lower bounds for families.
- **Candidate connections.** Rodgers-Tao Lambda>=0 (companion lower bound; dichotomy reduces RH to Lambda=0 rigidity); gap results of Bui-Milinovich (CAND-01835) relate to dynamics via dz/dt formula (small gaps push zeros apart; large gaps weaker repulsion); extreme values (CAND-01786/01957) as inputs for ratio |H_t/B_t|.
- **Reusable lemmas.** Proposition 3.1 (zero dynamics incl. repeated zeros, Hermite roots); Proposition 3.3 (barrier criterion) is a general-purpose lemma for any heat-flow of entire function with real-on-axis symmetry; Corollary 1.4.
- **Possible experiments.** Reproduce Table 1 using the published code; test the 1/log T heuristic by computing the minimal admissible t_0 for each X; try replacing the Euler-product shift q (83952) by a systematic optimiser to see how low Lambda goes for X=6e10; run the same pipeline on L(s,chi) for small conductors.
- **Risks / barriers.** Reaching Lambda<=0 (RH) is not approachable: the method yields Lambda<=O(1/log T) at best. Rigorous interval-arithmetic code reliance; Platt's computation is itself computer-assisted.

## Audit notes (Level 1 reader)

Inspected portion: none noticed in mathematics of Sec. 3 (proof of Prop 3.3 followed: inequality reduces to y_k^2<=(x-x_k)^2+Y^2 using |x_k|>= sqrt(X+1-Y^2) and y_k<1, consistent). Extraction-level garbling of Theorem 1.2 (i) range (the original is zero-free for (1+y_0)/2<=sigma<=1, 0<=T<=X/2) and of Theorem 1.3 formula (14) should be checked against the source typeset. Proof of Theorem 1.3 (Sec. 6) and the numerical verifications (Sec. 8.3-8.5) were not audited line by line. Remark in Sec. 1: the approximation H_t/B_t -> 1 is not uniform as t->0.

*These notes are a reader's observations, not verified findings; see `audits/` for adjudicated findings.*

## Provenance

- Candidate `CAND-01890`; harvest queries: kw_RH_any, kw_debruijn_newman, citation_expansion, arxiv_debruijn_newman, arxiv_rh_abs, arxiv_verification_zeros.
- Triage decision: include — Polymath15 upper bound Lambda<=0.22 with effective heat-flow approximation.
- Record generated by `tools/make_records.py`; search cutoff 2026-11-17.
