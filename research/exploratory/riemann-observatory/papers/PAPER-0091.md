# PAPER-0091 — The pair correlation of zeros of the zeta function

| Field | Value |
|---|---|
| Authors | Montgomery, H. L. |
| Year / stratum | 1973 / S3 |
| Venue | Analytic Number Theory, Proc. Sympos. Pure Math. 24, St. Louis Univ. Missouri 1972, 181-193 (1973). |
| Identifiers | zbMATH [0268.10023](https://zbmath.org/?q=an:0268.10023) |
| MSC | 11M06 |
| Families | B |
| Work type | original_paper |
| Evidence level of this record | **L1** |
| Full text | fulltext_read — https://public.websites.umich.edu/~hlm/paircor1.pdf |
| Selection | score 4.3247, in-pool citations 218, seed lists 2, triage relevance 5 |

## Mathematical content (Level 1: full text read)

**Research question.** Assuming RH, determine the second-moment (pair correlation) statistics of the differences $\gamma-\gamma'$ of zeta zeros via the form factor $F(\alpha)$, and compare with random-matrix ensembles.

### Main results

- **THM-PAPER-0091-1** (Theorem (Sec. 1, eq. (1)-(2)), theorem, scope: asymptotic; Sec. 1 (stated), Sec. 3 (proof)). Assume RH. For real $\alpha$, $T\ge2$, let $F(\alpha)=F(\alpha,T)=\left(\frac{T}{2\pi}\log T\right)^{-1}\sum_{0<\gamma,\gamma'\le T}T^{i\alpha(\gamma-\gamma')}w(\gamma-\gamma')$ with $w(u)=4/(4+u^2)$. Then $F(\alpha)$ is real, $F(\alpha)=F(-\alpha)$; for $T>T_0(\varepsilon)$, $F(\alpha)\ge-\varepsilon$ for all $\alpha$; and for fixed $0\le\alpha<1$, $F(\alpha)=(1+o(1))T^{-2\alpha}\log T+\alpha+o(1)$ as $T\to\infty$, uniformly for $0\le\alpha\le1-\varepsilon$. *Conditional on:* RH.
- **THM-PAPER-0091-2** (Corollary 1 (eqs. (5),(6)), corollary, scope: asymptotic; Sec. 1, proved Sec. 4). Assume RH. For fixed $0<a<1$: $\sum_{0<\gamma,\gamma'\le T}\left(\frac{\sin a(\gamma-\gamma')\log T}{a(\gamma-\gamma')\log T}\right)w(\gamma-\gamma')\sim\left(\frac{1}{2a}\right)\frac{T}{2\pi}\log T\cdot(1+\cdot)$ as printed, namely $\sim \frac{1}{2a}\frac T{2\pi}\log T$ up to the exact constant as printed; and with the squared kernel $\left(\frac{\sin(a/2)(\gamma-\gamma')\log T}{(a/2)(\gamma-\gamma')\log T}\right)^2 w(\gamma-\gamma')\sim\left(1+\frac a3\right)\frac{T}{2\pi}\log T$. (The OCR garbles the exact constants in (5); (6) is $(1+a/3)$ reading together with (14).) *Conditional on:* RH.
- **THM-PAPER-0091-3** (Corollary 2 (eq. (7)), corollary, scope: asymptotic; Sec. 1; proof Sec. 4). Assume RH. $\sum_{0<\gamma\le T,\ \rho\ \text{simple}}1\ge\left(\tfrac23+o(1)\right)\frac{T}{2\pi}\log T$, i.e. at least $2/3$ of the zeros are simple (derived from (6) with $a=1-\delta$ and $\sum m_\rho^2\le(1+o(1))\frac T{2\pi}\log T\cdot$ constant). *Conditional on:* RH.
- **THM-PAPER-0091-4** (Corollary 3 (eq. (8)), corollary, scope: asymptotic; Sec. 1; proof Sec. 4). Assume RH. One can compute $\lambda<1$ with $\liminf_n(\gamma_{n+1}-\gamma_n)\frac{\log\gamma_n}{2\pi}<\lambda$; the proof allows $\lambda=0.68$ (via the triangle kernel $r(u)=\max(1-|u|/A,0)$ and $C(A)=A+\frac1{\pi^2A}\mathrm{Cin}(2\pi A)-1>0$ at $A=0.68$). If infinitely many zeros were multiple one could take $\lambda=0$. *Conditional on:* RH.
- **THM-PAPER-0091-5** (Conjecture (eqs. (11),(12)), conjecture, scope: conditional; Sec. 1). Pair correlation conjecture: $F(\alpha)=1+o(1)$ for $\alpha\ge1$ uniformly on bounded intervals; equivalently, for fixed $\alpha<\beta$, $\#\{0<\gamma,\gamma'\le T:\ 2\pi\alpha/\log T\le\gamma-\gamma'\le2\pi\beta/\log T\}\sim\left(\int_\alpha^\beta\left(1-\left(\frac{\sin\pi u}{\pi u}\right)^2\right)du+\delta(\alpha,\beta)\right)\frac T{2\pi}\log T$, with $\delta=1$ if $0\in[\alpha,\beta]$, else $0$. *Conditional on:* RH.
- **THM-PAPER-0091-6** (Eq. (15)-(17), remarks, conjecture, scope: conditional; Sec. 1). GUE analogy: $k$-point correlation given by $\det\left[\frac{\sin\pi(u_i-u_j)}{\pi(u_i-u_j)}\right]$; consequent expectation $\liminf(\gamma_{n+1}-\gamma_n)\log\gamma_n=0$ and $\limsup(\gamma_{n+1}-\gamma_n)\log\gamma_n=+\infty$. Also the Montgomery-Weinberger statement (10) on gaps of Dedekind zeta zeros of imaginary quadratic fields with bounded class number (announced, not proved here). *Conditional on:* RH.

### Principal lemmas

- **THM-PAPER-0091-L1** (Lemma (Sec. 2, eq. (18)); Sec. 2). For $1<\sigma<2$, $x\ge1$, with $\tau=|t|+2$ and implied constants depending only on $\sigma$: $(2\sigma-1)\sum_\gamma\frac{x^{i\gamma}}{(\sigma-\tfrac12)^2+(t-\gamma)^2}=-x^{-1/2}\Big(\sum_{n\le x}\Lambda(n)(x/n)^{1/2-\sigma+it}+\sum_{n>x}\Lambda(n)(x/n)^{-1/2-\sigma+it}\Big)+O(x^{-1/2}\ldots)$ (full error terms garbled in OCR; the O-terms are $x^{-1+\ldots}$ and $\log\tau$ type). Assumes RH. — *Role:* Explicit formula tying zeros to primes; its mean square over $t\in[0,T]$ gives $F(\alpha)$ with $x=T^\alpha$.
- **THM-PAPER-0091-L2** (eq. (26); Sec. 3). $\int_0^T|L(T^\alpha,t)|^2dt=F(\alpha)\,T\log T+O(\log^3T)$, with $L$ the left side of (18); nonnegativity of the left side gives $F\ge-\varepsilon$. — *Role:* Converts the zero sum into a mean square and yields positivity.
- **THM-PAPER-0091-L3** (eq. (28)-(31) and Cases 1-3; Sec. 3). Mean square of the prime sum on the right of (18) by the Montgomery-Vaughan Hilbert-inequality form of Parseval: $\int_0^T|\sum a_nn^{-it}|^2dt=\sum|a_n|^2(T+O(n))$; evaluates to $(1+o(1))\frac T{x^2}\log^2T$ for $1\le x\le(\log T)^{3/4}$ and $(1+o(1))T\log x$ for $(\log T)^{3/2}<x\le T/\log T$. — *Role:* Computes the right side with PNT-with-error-term; produces the term $\alpha$ and the $T^{-2\alpha}\log T$ delta approximant.
- **THM-PAPER-0091-L4** (discussion of (32)-(34); end of Sec. 3). For $\alpha\ge1$ the needed mean square reduces to sums $\sum_{n\le y}\Lambda(n)\Lambda(n+h)\approx\mathfrak c(h)y$ (Hardy-Littlewood type); heuristics suggest $F(\alpha)\sim1$. The $q$-analogue (34) is $\sim Q\log x$ for $Q\ge x$, and under GRH extends to $x^{3/4+\epsilon}<Q\le x$. — *Role:* Heuristic route to $F\equiv1$ for $\alpha\ge1$.

### Proof architecture

Assume RH. Explicit formula (Lemma) with $\sigma=3/2$ gives $L(x,t)=R(x,t)$. Integrate $|L|^2$ over $[0,T]$, truncating zeros outside $[0,T]$ via zero-density $\ll\log T$ per unit interval, to obtain $F(\alpha)T\log T$ (eq. 26). Compute $\int|R|^2$ by Parseval for Dirichlet series (Montgomery-Vaughan) and PNT with error term, in three ranges of $x=T^\alpha$, controlling cross terms by Cauchy-Schwarz. Corollaries follow by convolving with kernels $\hat r$ supported in $[-1+\delta,1-\delta]$.

**Techniques.** Explicit formula; mean value of Dirichlet polynomials; Montgomery-Vaughan Hilbert inequality; PNT with error term; Fourier analysis on $F(\alpha)$; random-matrix analogy (Dyson)

## Context and interpretation

**Importance and obstacle overcome.** Introduces the form factor $F(\alpha)$ and establishes, under RH, a nontrivial range of pair correlation; the obstacle overcome is controlling the mean square of the explicit formula for $x\le T$ with only mean value theorems and PNT, which yields the positivity and the linear term $\alpha$ that identifies GUE (complex Hermitian/unitary) and excludes GOE/GSE in this range. It created the zeta/random-matrix programme.

**Relation to prior work.** 

**Limitations and open questions.** Only $|\alpha|<1$ is proved (support restriction of test functions $\hat r\subset[-1,1]$); $F(\alpha)$ for $\alpha\ge1$ would need correlations of $\Lambda(n)\Lambda(n+h)$ (and an independence hypothesis) and is the pair correlation conjecture. Uniformity up to $\alpha=1$ claimed but not proved. RH is assumed throughout. Constants in Corollaries 2, 3 (2/3 and 0.68) are non-optimal as the author says.

## Research potential

- **Hypotheses that might be weakened.** RH is used in the explicit formula and in the zero-density bound for $\gamma\notin[0,T]$; Baluyot-Goldston-Suriajaya-Turnage-Butterbaugh (2024) remove RH in an unconditional version. Test which steps survive for zeros off the line with $\Theta<1$ (zero-free regions) as a way of getting RH-implying statements from a failed $F(\alpha)$ bound.
- **Generalizations.** Extension to Dedekind zeta fields and L-functions (the $q$-analogue (34) and Montgomery-Weinberger (10)); extension to $\alpha\ge1$ under a Hardy-Littlewood shifted-correlation hypothesis for $\Lambda$ (eq. (33)).
- **Candidate connections.** Support range $[-1,1]$ and $2/3$-simple-zeros corollary connect to Robin-type arithmetic via the $\Lambda(n)\Lambda(n+h)$ conjectures; pair correlation and the positivity $F\ge0$ could be tested as a necessary condition (a falsifiable consequence) in heat-flow deformations $\Lambda>0$.
- **Reusable lemmas.** Eq. (26) identity and the three-case mean-square evaluation in Sec. 3 are directly reusable for other $\sigma$-weights; eq. (28) form of Parseval.
- **Possible experiments.** Compute $F(\alpha,T)$ numerically from tabulated zeros (the paper notes that convergence is slow); compare with $T^{-2\alpha}\log T+\alpha$ and test the weight $w(u)=4/(4+u^2)$ versus other kernels to see if a larger $A$ than 0.68 gives a better Corollary 3 constant.
- **Risks / barriers.** Extension past $\alpha=1$ requires unproved shifted-prime correlations; the method gives only averaged, not pointwise, statements and cannot decide RH.

## Audit notes (Level 1 reader)

Source OCR garbles several formulas (Corollary 1 constants in (5), Lemma error terms, Corollary 3 inequality); the constants for (5)-(6) given above are my reading and not verified symbol-by-symbol; the standard values are $(1/2a)$ and $(1+a/3)$ times $\frac T{2\pi}\log T$ (the printed (6) '(1+a/3)' consistent with (14)). Remark that (2) holds uniformly on $[0,1]$ 'with more effort' is unproved in the text. Otherwise none noticed in inspected portion.

*These notes are a reader's observations, not verified findings; see `audits/` for adjudicated findings.*

## Provenance

- Candidate `CAND-00343`; harvest queries: kw_pair_correlation, msc_11M06.
- Triage decision: include — Montgomery pair correlation, the founding paper for RMT connection.
- Record generated by `tools/make_records.py`; search cutoff 2026-11-17.
