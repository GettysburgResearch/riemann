# PAPER-0081 — Partial Euler products on the critical line

| Field | Value |
|---|---|
| Authors | Conrad, Keith |
| Year / stratum | 2005 / S5 |
| Venue | Can. J. Math. 57, No. 2, 267-297 (2005). |
| Identifiers | zbMATH [1068.11058](https://zbmath.org/?q=an:1068.11058) · DOI [10.4153/CJM-2005-012-6](https://doi.org/10.4153/CJM-2005-012-6) |
| MSC | 11M41, 11G40 |
| Families | A, C, E |
| Work type | original_paper |
| Evidence level of this record | **L1** |
| Full text | fulltext_read — https://kconrad.math.uconn.edu/articles/eulerprod.pdf |
| Selection | score 4.4265, in-pool citations 13, seed lists 1, triage relevance 4 |

## Mathematical content (Level 1: full text read)

**Research question.** How do partial Euler products over primes of norm <= x of a normalized L-function behave on the critical line Re(s)=1/2? In particular, explain Goldfeld's sqrt2 factor in the Birch-Swinnerton-Dyer partial-product asymptotics and determine when such asymptotics hold.

**Historical motivation.** Birch and Swinnerton-Dyer's original conjecture was an asymptotic prod_{p<=x} #E(F_p)/p ~ A (log x)^r. Goldfeld showed this implies RH for L(E,s) and found an unexpected factor sqrt2 in the constant; Conrad extends to general L-functions on their critical line.

### Main results

- **THM-PAPER-0081-1** (Theorem 1.1 (Goldfeld), imported theorem (restated), scope: conditional; Sec 1). Let $E/\mathbb Q$ be an elliptic curve. If $\mathrm{Prod}(E,x)=\prod_{p\le x}\#E_{ns}(\mathbb F_p)^{-1}p\sim C/(\log x)^r$ with $C>0$, $r\in\mathbb R$, then $L(E,s)$ satisfies RH ($L(E,s)\ne0$ for $\Re s>1$), $r=\mathrm{ord}_{s=1}L(E,s)$ and $C=\frac{L^{(r)}(E,1)}{r!}\cdot\frac1{\sqrt2\,e^{r\gamma}}$. *Conditional on:* partial-product asymptotic (1.2).
- **THM-PAPER-0081-2** (Theorem 1.2, theorem, scope: conditional; Intro; Thm 5.11 (full statement also gives L(s)!=0 on Re s>1/2 and r_t=ord)). Let $L(s)=\prod_p\prod_{j\le d}(1-\alpha_{p,j}Np^{-s})^{-1}$ over a number field with $|\alpha_{p,j}|\le1$, holomorphic on $\Re s\ge1/2$, and with second-moment Euler product $L_2(s)=\prod(1-\alpha_{p,j}^2Np^{-s})^{-1}$ holomorphic nonvanishing on $\Re s=1$ except at $1+it_0$ with order $R_0\in\mathbb Z$. If $\prod_{Np\le x}(\ldots)\sim C_t(\log x)^{-r_t}$ at $1/2+it$ with $C_t\in\mathbb C^\times$, then with $B_t$ the leading Taylor coefficient of $L$ at $1/2+it$: $C_t=B_t/e^{r_t\gamma}$ if $t\ne t_0/2$ and $C_t=B_t/(\sqrt2^{R_0}e^{r_t\gamma})$ if $t=t_0/2$. *Conditional on:* partial-product asymptotic.
- **THM-PAPER-0081-3** (Theorem 1.3 / 6.2 / 6.3, theorem, scope: conditional; Sec 6, Thm 1.3, 6.2, 6.3 (Kuo-Murty independently prove 1.3)). For $E/\mathbb Q$ (Thm 1.3), $\prod_{p\le x}$ asymptotic (1.2) is equivalent to $\psi_E(x)=\sum_{p^k\le x,(p,N)=1}(\alpha_p^k+\beta_p^k)\log p=o(x\log x)$. General form Thm 6.3: for a normalized Euler product with analytic continuation, functional equation and second-moment hypothesis, the following are equivalent: (1) the partial-product asymptotic at $1/2+it$ for some real t, (2) for all real t, (3) $\psi_L(x)=o(\sqrt x\log x)$. Thm 6.2 (no second moment): convergence of $\sum_{n\le x}b_nn^{-1/2-it}+m_t\log\log x$ is equivalent to $\psi_L(x)=o(\sqrt x\log x)$.
- **THM-PAPER-0081-4** (Theorem 4.3 / 4.9, theorem, scope: asymptotic; Sec 4). Thm 4.3: if $\tilde L$ is a normalized Euler product extending holomorphically nonvanishing to $\Re s=1$ except order $R_0$ at $1+it_0$, then $\lim_{x\to\infty}\sum_{\sqrt x<Np\le x}(\beta_{p,1}+\ldots+\beta_{p,d})Np^{-1-it}$ equals $0$ if $t\ne t_0$ and $-R_0\log2$ if $t=t_0$. Thm 4.9: under the second-moment hypothesis, $\sum_{Np\le x}\sum_{k\ge1}=\sum_{Np^k\le x}+o(1)$ if $t\ne t_0/2$ and $+(-R_0\log\sqrt2)+o(1)$... (printed: $-R_0\log\sqrt2$) if $t=t_0/2$. This explains $\sqrt2$ as a prime-vs-prime-power rearrangement.
- **THM-PAPER-0081-5** (Theorem 3.3, Theorem 5.3, theorem, scope: conditional; Sec 3, Sec 5). Thm 3.3: for $\Re s_0>1/2$, nonzero limit of the partial Euler product at $s_0$ is equivalent to existence of $\lim\sum_{Np^k\le x}\sum_j\alpha_{p,j}^k/(kNp^{ks_0})$, and then $L$ continues holomorphically nonvanishing to $\Re s>\Re s_0$ with $L(s)=$ the limit. Thm 5.3: if $\sum_{Np^k\le x}\sum_j\alpha_{p,j}^k/(kNp^{k/2})=-r\log\log x+C'+o(1)$ then $L$ is holomorphic nonvanishing on $\Re s>1/2$ and $L(s)\sim e^{C'}e^{r\gamma}(s-1/2)^r$ as $s\to1/2^+$.
- **THM-PAPER-0081-6** (Theorem 7.1 (Stark), theorem, scope: global; Sec 7). If $f(s)=\sum a_nn^{-s}$ converges for $\Re s\ge\sigma_0>\sigma_1$ and has a meromorphic continuation to $\Re s\ge\sigma_1$ with a simple pole on the line $\Re s=\sigma_1$, then the Dirichlet series converges at no point of that line. Consequently the Dirichlet series of $L'/L$ converges nowhere on the critical line.
- **THM-PAPER-0081-7** (Theorem 8.2, 8.4, Corollary 8.5, theorem, scope: global; Sec 8). Function fields over $\mathbb F_q$: with $L(z)$ entire and satisfying (8.4), the partial-product asymptotic at $|u|=1/\sqrt q$ holds with $C_u=B_u/e^{m_u\gamma}$ (or with extra $\sqrt2^{R_0}$ when $u^2=z_0$) under RH and the second moment hypothesis (Cor 8.5, unconditional in suitable cases); Thm 8.4: the convergence condition is equivalent to all inverse zeros satisfying $|\lambda_i|=\sqrt q$. Lemma 3.2 (logs vs. products) fails over function fields (Example 8.3).

### Key definitions

- normalized Euler product of degree <= d with |alpha_{p,j}|<=1
- partial Euler product over Np<=x
- second moment $L_2(s)=\prod(1-\alpha_{p,j}^2Np^{-s})^{-1}$ (not the series with $a_n^2$)
- $\psi_L(x)=\sum_{Np^k\le x}\sum_j\alpha_{p,j}^k\log Np$ (explicit definition in Sec 6)
- second moment hypothesis (Def 4.4)

### Principal lemmas

- **THM-PAPER-0081-L1** (Lemma 3.1; Sec 3). For $\Re s\ge1/2$: $\sum_{Np\le x}\sum_{k\ge1}\frac{\sum_j\alpha_{p,j}^k}{kNp^{ks}}=\sum_{Np^k\le x}(\cdots)+\sum_{\sqrt x<Np\le x}\frac{\sum_j\alpha_{p,j}^2}{2Np^{2s}}+o(1)$, and the middle sum is $o(1)$ for $\Re s>1/2$. — *Role:* Switches sums over primes vs prime powers; source of the sqrt2 effect at the center.
- **THM-PAPER-0081-L2** (Lemma 3.2; Sec 3). For $\gamma_{p,i}$ in the open unit disk tending to 0 with Np, the product asymptotic $\sim C/(\log x)^r$ is equivalent to $-\sum\log(1-\gamma_{p,i})=-r\log\log x+C'+o(1)$. — *Role:* Reduces product asymptotics to sums over number fields (false over function fields).
- **THM-PAPER-0081-L3** (Theorem 4.1; Sec 4). Tauberian theorem: for $f=\sum a_nn^{-s}$ with $a_n\ge0$ and a simple pole at 1 only on Re s=1, and $g=\sum b_nn^{-s}$, $|b_n|\le Ca_n$, with $g=r\log(s-1)+G(s)$ then $\sum_{n\le x}b_n/n=-r\log\log x-r\gamma+G(1)+o(1)$. Proof omitted. — *Role:* Source of $e^{r\gamma}$.
- **THM-PAPER-0081-L4** (Lemma 5.1, Lemma 5.2; Sec 5). Lemma 5.1: as $s\to0^+$ asymptotics giving $e^\gamma$; Lemma 5.2: Abelian lemma for piecewise continuous h with $h(x)\to0$. — *Role:* Abelian-direction ingredients (statements not read in detail).
- **THM-PAPER-0081-L5** (Lemma 6.1; Sec 6). If $\sum_{n\le x}c_n=o(\sqrt x\log x)$ then an associated Dirichlet-series/partial-sum quantity converges (exact form not read). — *Role:* Used in Theorem 6.2 to link $\psi_L(x)=o(\sqrt x\log x)$ with convergence of the log series via explicit formulas.

### Proof architecture

Section 3 reduces product asymptotics to sums via principal-branch logarithms (Lemma 3.2) and compares sums over primes with sums over prime powers (Lemma 3.1). Section 4 shows via a Tauberian theorem (Thm 4.1, Wiener-Ikehara-type) applied to the second-moment L-function that the prime/prime-power rearrangement contributes -R_0 log sqrt2 at the exceptional point t_0/2, producing the sqrt2 factor. Section 5 uses an Abelian argument (Thm 5.3) and Lemma 5.1 to extract e^{r gamma} and the order of vanishing, giving the generalized Goldfeld theorem (Thm 5.11). Section 6 uses explicit formulas to show the sum-convergence condition is equivalent to psi_L(x)=o(sqrt x log x) (Thm 6.2, 6.3). Section 7 discusses Dirichlet series on the critical line (Stark's Thm 7.1) and Section 8 repeats the analysis over function fields where RH is a theorem for curves.

Dependency edges: Theorem 5.11 → Theorem 4.9 + Theorem 5.3 (uses); Theorem 6.3 → Theorem 5.11 + Theorem 6.2 (uses); Theorem 1.3 → Theorem 6.2 (special case); Theorem 4.9 → Theorem 4.3 (uses)

**Imported results.** Goldfeld's theorem (Goldfeld 1982); Wiener-Ikehara-type Tauberian theorem (Thm 4.1 proof omitted); modularity of elliptic curves (Wiles et al.); Kuo-Murty independent proof of Thm 1.3; Montgomery's heuristic for psi(x)-x; Weil RH for curves over finite fields; Shimura's symmetric-square results (Example 4.7)

**Techniques.** partial Euler products and logarithms; Tauberian and Abelian theorems for Dirichlet series; second-moment (symmetric over exterior square) L-function; explicit formulas; Wiener-Ikehara type argument; function field analogues with Weil RH

## Context and interpretation

**Importance and obstacle overcome.** Explains the sqrt2 in Goldfeld's theorem as a prime-versus-prime-power rearrangement effect governed by the second moment, and characterizes the partial-product asymptotics as equivalent to psi_L(x)=o(sqrt x log x), which is deeper than RH (RH is equivalent to psi_L(x)=O(sqrt x (log x)^2)) yet plausible by Montgomery's conjecture. Obstacle: Euler products are outside absolute convergence on the critical line, so order of terms matters.

**Relation to prior work.** Extends Goldfeld (1982) and the BSD original asymptotic; Kuo-Murty independently prove the elliptic-curve case of Thm 1.3; relates to Montgomery's heuristic and to Nagao's rank formula.

**Limitations and open questions.** The equivalence statements are conditional on hypotheses (analytic continuation, functional equation, second moment) that are known for the main examples but not general L-functions. The condition psi_L(x)=o(sqrt x log x) is not proven for any L-function with unproven GRH; its proof is open and the author notes convergence of the log Dirichlet series on the critical line is plausible but not provable at present. Over number fields nothing unconditional is obtained; unconditional results only over function fields. Author notes a planned follow-up with R. Murty on a convergent alternative to Nagao's rank formula.

**Ideas in remarks/appendices/abandoned paths.** Sec 6 end: an alternative to Nagao's (non-convergent) heuristic rank formula that provably converges to the analytic rank under psi_L(x)=o(sqrt x log x) (Sec 6, final paragraph); Examples 5.8-5.10 give concrete cases (chi_4, rank-3 curve, CM curves over the CM field) where sqrt2 appears, flips to numerator, or disappears; Sec 7 remark (Rohrlich) that the ordinary Dirichlet series of an entire L-function should converge for Re s > 1/2 - 1/(2D).

## Research potential

- **Hypotheses that might be weakened.** The second moment hypothesis (Def 4.4) could be replaced by weaker information on L_2 near Re s=1; check where Thm 4.3's holomorphy of L_2 on Re s=1 is used beyond the exceptional point.
- **Generalizations.** Partial products at other lines or for non-self-dual L-functions; Rankin-Selberg products; the alternative rank formula suggested by Thm 6.2 vs Nagao's.
- **Candidate connections.** psi_L(x)=o(sqrt x log x) is a Robin/Mertens-type growth statement linking to Ng CAND-01212 (M(x) ~ sqrt x (logloglog x)^{5/4}) and to the signed native/Mobius cancellation programme; sqrt2 factor relates to Gonek-Hejhal / Montgomery second-moment heuristics.
- **Reusable lemmas.** Lemma 3.1 (prime vs prime-power sums), Thm 5.3 (Abelian extraction of order and leading coefficient), Thm 7.1 (Stark: no convergence at a pole on the line).
- **Possible experiments.** Numerically compute prod_{p<=x} L_p(1/2)^{-1} for zeta-like L-functions (Dirichlet characters, elliptic curves of known rank) and check the sqrt2 factors and the exponent r; test psi_E(x)/(x log x) trend.
- **Risks / barriers.** Finite computations of partial products at x up to 1e12 cannot distinguish o(x log x) from slightly larger growth; convergence is extremely slow (log log x). A numerical match would not be evidence for RH since the hypothesis is stronger than RH.

## Audit notes (Level 1 reader)

Thm 4.9 statement printed in extracted text as '-R_0 log sqrt 2' for the exceptional case; the displayed intermediate text elsewhere (Sec 4 intro) says sqrt2 arises while Thm 4.3 gives -R_0 log 2 for the sum over sqrt x<Np<=x of beta/Np^{1+it}; these are consistent since Thm 4.9 uses half of it (the 1/2 factor in alpha^2/2), as the proof states, but the raw text rendering is ambiguous. Not all proofs (Sec 5.2, 6, 8) were read line by line. Version read is author's posted PDF; not compared against the journal version.

*These notes are a reader's observations, not verified findings; see `audits/` for adjudicated findings.*

## Provenance

- Candidate `CAND-01315`; harvest queries: kw_RH_any, citation_expansion.
- Triage decision: include — Conrad's partial Euler products at center, linking convergence to RH and GRH (Birch-Swinnerton-Dyer relevance).
- Record generated by `tools/make_records.py`; search cutoff 2026-11-17.
