# PAPER-0041 — Fourier optimization and prime gaps

| Field | Value |
|---|---|
| Authors | Carneiro, Emanuel; Milinovich, Micah B.; Soundararajan, Kannan |
| Year / stratum | 2019 / S6 |
| Venue | Comment. Math. Helv. 94, No. 3, 533-568 (2019). |
| Identifiers | zbMATH [1429.42001](https://zbmath.org/?q=an:1429.42001) · DOI [10.4171/CMH/467](https://doi.org/10.4171/CMH/467) · arXiv [1708.04122](https://arxiv.org/abs/1708.04122) |
| MSC | 42A05, 41A30, 11M06, 11M26, 11N05 |
| Families | A, H |
| Work type | original_paper |
| Evidence level of this record | **L1** |
| Full text | fulltext_read — https://arxiv.org/abs/1708.04122 |
| Selection | score 4.5776, in-pool citations 18, seed lists 1, triage relevance 4 |

## Mathematical content (Level 1: full text read)

**Research question.** Define two Fourier-analytic extremal problems (bandlimited-type with a penalty on Fourier mass outside [-1,1]); determine existence/uniqueness of extremizers and bounds for sharp constants C(A), C^+(A); and use them via the Guinand-Weil explicit formula plus Brun-Titchmarsh to improve, under RH, the Cramer-type bound for gaps between consecutive primes.

**Historical motivation.** Cramer (1936) gave O(sqrt p log p) under RH; Goldston, Ramare-Saouter, Dudek improved the constant to 1. The authors recast Goldston-type explicit-formula arguments as a Fourier extremal problem related to Beurling-Selberg and Cohn-Elkies.

### Main results

- **THM-PAPER-0041-1** (Problems (1.1)-(1.4), definition, scope: global; Sec. 1.1, p. 2). For $1\le A<\infty$: $C(A)=\sup_{0\ne F\in\mathcal A}\frac1{\|F\|_1}\big(|F(0)|-A\int_{[-1,1]^c}|\hat F(t)|dt\big)$; $C(\infty)=\sup_{F\in\mathcal E}|F(0)|/\|F\|_1$ ($\mathcal E$: $\operatorname{supp}\hat F\subset[-1,1]$). $C^+(A)=\sup_{F\in\mathcal A^+}\frac1{\|F\|_1}\big(F(0)-A\int_{[-1,1]^c}(\hat F(t))_+dt\big)$ over even real continuous $F\in L^1$; $C^+(\infty)=\sup F(0)/\|F\|_1$ over even real $F\in L^1$ with $\hat F(t)\le0$ for $|t|\ge1$. $\hat F(t)=\int e^{-2\pi ixt}F(x)dx$.
- **THM-PAPER-0041-2** (Theorem 1, theorem, scope: global; Sec. 1.1, p. 3). (a) $A=\infty$: there is an even real extremizer $G\in\mathcal E$, $G(0)=1$, for (1.2); all extremizers are $cG$; $C(\infty)\int\operatorname{sgn}(G)F=F(0)$ for all $F\in\mathcal E$; $1.08185\ldots\le C(\infty)\le1.09769\ldots$ (Gorbachev). (b) $C(1)=2$, no extremizers. (c) For $1<A<\infty$ an even real extremizer exists and, with $c_0=1.07995\ldots$, $d_0=1.09769\ldots$, $\lambda(A)\in(0,1)$ solving $1-\frac1A=\sin\frac{\pi\lambda}2-\frac{\pi\lambda}2\cos\frac{\pi\lambda}2$: $\max\{2A-2\sqrt{A(A-1)},\frac{\pi Ac_0}2\cos\frac{\pi\lambda(A)}2\}\le C(A)\le\min\{\frac{d_0}{1-(A-2)^{-0.3}},2\}$, the first upper bound only for $2.6\le A<\infty$ (exponent 0.3 as read from the text).
- **THM-PAPER-0041-3** (Theorem 2, theorem, scope: global; Sec. 1.1, p. 4). (a) $A=\infty$: an extremizer $G\in\mathcal E^+$ exists and $C(\infty)\le C^+(\infty)<1.2$. (b) $C^+(1)=2$, no extremizers. (c) For $1<A<\infty$ an even real extremizer exists and $C(A)\le C^+(A)\le\min\{\frac{1.2}{1-(A-1)^{-0.222}},2\}$ (first bound for $A>1.222$); for $A=36/11$ a numerical example gives $25/21<C^+(36/11)$.
- **THM-PAPER-0041-4** (Theorem 3, theorem, scope: asymptotic; Sec. 1.2, p. 5; proof Sec. 5.2, inequality (5.11)). Assume RH. Let $B:=\limsup_{x\to\infty}\frac{\pi(x+\sqrt x)-\pi(x)}{\sqrt x/\log x}$ (so $1\le B\le36/11$ by PNT and Iwaniec). Then for any $\alpha\ge0$, $\inf\{c>0:\liminf_{x\to\infty}\frac{\pi(x+c\sqrt x\log x)-\pi(x)}{\sqrt x}>\alpha\}\le\frac{1+2\alpha}{C^+(B)}<\frac{21}{25}(1+2\alpha)$. *Conditional on:* RH.
- **THM-PAPER-0041-5** (Corollary 4, corollary, scope: asymptotic; p. 5). Assume RH. Then $\limsup_{n\to\infty}\frac{p_{n+1}-p_n}{\sqrt{p_n}\log p_n}\le\frac1{C^+(B)}<\frac{21}{25}$ (improving Dudek's $c=1$; the method cannot go below $1/2$ since $C^+\le2$). The case $\alpha=1$ gives constant $3/C^+(B)<63/25$ (vs Dudek's 3). *Conditional on:* RH.
- **THM-PAPER-0041-6** (Theorem 5, theorem, scope: global; Sec. 1.2, pp. 5-6; proof Sec. 6). Assume RH. For every $x\ge4$ there is a prime in $[x,x+\frac{22}{25}\sqrt x\log x]$; equivalently $p_{n+1}-p_n\le\frac{22}{25}\sqrt{p_n}\log p_n$ for all $p_n>3$. Proved with a dilation of $H(x)=\cos2\pi x/(1-16x^2)$ and Montgomery-Vaughan's explicit Brun-Titchmarsh; for $x\le4\cdot10^{18}$ it follows from verified $p_{n+1}-p_n<\log^2p_n$. *Conditional on:* RH.
- **THM-PAPER-0041-7** (Sec. 2 and Prop. 10, theorem, scope: global; Sec. 2; Sec. 7.2). Existence of extremizers by compactness (weak $L^2$ limits plus Fatou) for problems (1.1)-(1.4); Proposition 10: a radial extremizer exists for the Cohn-Elkies sphere-packing problem (7.1) in every dimension.

### Key definitions

- C(A), C^+(A), C(infinity), C^+(infinity)
- Brun-Titchmarsh constant B in sqrt x scale (1.11)
- classes A, A^+, E, E^+

### Principal lemmas

- **THM-PAPER-0041-L1** (Lemma 6 (Guinand-Weil explicit formula); Sec. 5). For $h$ analytic in $|\operatorname{Im}s|\le\frac12+\epsilon$ with $h(s)\ll(1+|s|)^{-(1+\delta)}$: $\sum_\rho h(\frac{\rho-1/2}{i})=h(\frac1{2i})+h(-\frac1{2i})-\frac1{2\pi}\hat h(0)\log\pi+\frac1{2\pi}\int h(u)\operatorname{Re}\frac{\Gamma'}{\Gamma}(\frac14+\frac{iu}2)du-\frac1{2\pi}\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}(\hat h(\frac{\log n}{2\pi})+\hat h(-\frac{\log n}{2\pi}))$. — *Role:* Imported (Iwaniec-Kowalski Thm 5.12); links zeros to primes.
- **THM-PAPER-0041-L2** (Inequality (5.2); Sec. 5.1, p. 18). Under RH, for $f(z)=\Delta F(\Delta z)$ with $\operatorname{supp}\hat F\subset[-N,N]$ and $2\pi\Delta N\le\log a$, applying Lemma 6 to $h(z)=f(z)a^{iz}$ gives $f(\frac1{2i})a^{1/2}+f(-\frac1{2i})a^{-1/2}\le\sum_\gamma|f(\gamma)|+\frac1{2\pi}\hat f(-\frac{\log a}{2\pi})\log\pi+\frac1{2\pi}\int f(u)a^{iu}\operatorname{Re}\frac{\Gamma'}\Gamma du+\frac1{2\pi}\sum\frac{\Lambda(n)}{\sqrt n}(\hat f(\tfrac{\log(n/a)}{2\pi})_++\hat f(-\tfrac{\log(n/a)}{2\pi})_+)$. — *Role:* Core inequality: LHS detects a short interval with few primes; RH makes all zeros real so |f(gamma)| terms are controlled; edge primes bounded by Brun-Titchmarsh.
- **THM-PAPER-0041-L3** (Sec. 5.2 asymptotics / (5.11); Sec. 5.2-5.2.3, pp. 19-21). LHS equals $\Delta F(0)(a^{1/2}+a^{-1/2})+O(\Delta^2a^{1/2})$; combining estimates for zero sum, gamma-factor and prime sum along a sequence of $x$ with few primes in $[x,x+c\sqrt x\log x]$ yields $c\le(1+2\alpha)\|F\|_1/(F(0)-B\int_{[-1,1]^c}(\hat F)_+)$. — *Role:* Translation to extremal problem (1.3).
- **THM-PAPER-0041-L4** (Theorem 1 (a.3) proof (Sec. 3); Sec. 3). Extremal $G$ for (1.2) satisfies $C(\infty)\int\operatorname{sgn}(G(x))F(x)dx=F(0)$ for all $F\in\mathcal E$; uniqueness uses that a nonnegative function with $\hat{}$ supported in $[-2,2]$ is the square of a function with transform supported in $[-1,1]$. — *Role:* Optimality characterization for A=infinity.
- **THM-PAPER-0041-L5** (Lemmas 7 and 9; Sec. 6, pp. 21-26). Lemma 7 gives explicit Fourier-analytic estimates for the dilated $H$ (with $\vartheta\delta=\pi/2$, $a>e^\delta$); Lemma 9 gives explicit bounds for the zero sum via $N(x)$; with Montgomery-Vaughan's explicit Brun-Titchmarsh these make all errors effective. — *Role:* Explicit version of the prime gap bound.

### Proof architecture

Secs. 2-4 analyze the Fourier extremal problems: compactness for existence; duality and the sign-function identity plus squares of bandlimited functions for uniqueness (A=infinity); explicit test functions (H, Gorbachev's construction) for bounds. Sec. 5: take even bandlimited F, rescale to f(z)=Delta F(Delta z), apply Guinand-Weil to f(z)a^{iz}; under RH zeros contribute via sum|f(gamma)|; prime contributions in the window carry the main sign information; edge primes bounded by Brun-Titchmarsh constant B; the limit yields (5.11), optimized to C^+(B). Sec. 6 repeats with explicit constants for Theorem 5.

**Imported results.** Iwaniec Brun-Titchmarsh bound giving B<=36/11 (Iwaniec Thm 14); Gorbachev numerical bounds for C(infinity); Iwaniec-Kowalski Thm 5.12; Montgomery-Vaughan explicit Brun-Titchmarsh; Oliveira e Silva-Herzog-Pardi verification of p_{n+1}-p_n<log^2 p_n to 4e18; Dudek 2016 (c=1) and Dudek-Grenie-Molteni

**Techniques.** Guinand-Weil explicit formula; one-sided bandlimited extremal problems; compactness / weak L^2 limits; duality and sign-function characterization; Brun-Titchmarsh inequality (Iwaniec 36/11 in sqrt x scale); explicit N(T) estimates

## Context and interpretation

**Importance and obstacle overcome.** Breaks the constant-1 barrier for RH-conditional prime gaps (22/25 explicit for p_n>3) by isolating the optimization inside the explicit formula approach. Classical extremal tools do not solve the signed problem with penalty outside [-1,1]; the authors obtain existence/uniqueness and two-sided numerics instead.

**Relation to prior work.** Builds on Goldston, Dudek, Ramare-Saouter; part of the Carneiro et al. bandlimited-approximation program (same tools as CAND-01821); related to Cohn-Elkies sphere packing LP.

**Limitations and open questions.** Exact values of C(A), C^+(A) unknown; only 1.08185<=C(inf)<=1.09769 and 25/21<C^+(36/11). The method's limit is constant 1/2 (from C^+<=2) unless B is improved; everything is conditional on RH. Under RH plus pair correlation the limsup is 0 (cited). Cramer's O(log^2 p) is open.

## Research potential

- **Hypotheses that might be weakened.** RH enters only through bounding |f(gamma)| termwise over real gamma; a zero-density substitute might give unconditional but weaker gap results. Improving the Brun-Titchmarsh constant B directly improves C^+(B).
- **Generalizations.** Multidimensional or other-symmetry versions (Sec. 7.1); same optimization for gaps in arithmetic progressions, number fields, or L-functions under GRH (least primes, quadratic non-residues).
- **Candidate connections.** Links RH-conditional bounds on pi(x+h)-pi(x) to Cohn-Elkies linear programming and one-sided Beurling-Selberg majorants (also CAND-01821); contrast with pair-correlation approaches giving limsup 0.
- **Reusable lemmas.** Inequality (5.2)-(5.11) is a template for any 'short interval with few primes' argument; Theorem 1(a.3) sign characterization is reusable for L^1-constrained bandlimited extremal problems.
- **Possible experiments.** Solve the discretized extremal problem (1.3) by semi-infinite LP for A=36/11 to sharpen 25/21<C^+(36/11) and test sensitivity to B; compare actual maximal gaps up to 4e18 with 22/25 sqrt p log p.
- **Risks / barriers.** Even optimal C^+(1)=2 gives constant 1/2, far from Cramer's log^2 p; B only known as 36/11; cannot decide RH.

## Audit notes (Level 1 reader)

The text layer garbled superscripts (e.g. 1/C^+(B) printed without superscript in (1.13)/(1.14)); I reconstructed from (5.11). The exponents 0.3 in (1.6) and 0.222 in (1.8) are transcribed as read. Otherwise none noticed in inspected portion.

*These notes are a reader's observations, not verified findings; see `audits/` for adjudicated findings.*

## Provenance

- Candidate `CAND-01806`; harvest queries: kw_RH_any, msc_11M06, msc_11M26, msc_11N05, arxiv_rh_abs.
- Triage decision: include — Fourier extremal methods improving prime gap bound under RH.
- Record generated by `tools/make_records.py`; search cutoff 2026-11-17.
