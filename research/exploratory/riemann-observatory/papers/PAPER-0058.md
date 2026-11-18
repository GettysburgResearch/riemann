# PAPER-0058 — Lower order terms in the full moment conjecture for the Riemann zeta function

| Field | Value |
|---|---|
| Authors | Conrey, J. B.; Farmer, D. W.; Keating, Jonathan P.; Rubinstein, M. O.; Snaith, N. C. |
| Year / stratum | 2008 / S5 |
| Venue | J. Number Theory 128, No. 6, 1516-1554 (2008). |
| Identifiers | zbMATH [1141.11040](https://zbmath.org/?q=an:1141.11040) · DOI [10.1016/j.jnt.2007.05.013](https://doi.org/10.1016/j.jnt.2007.05.013) · arXiv [math/0612843](https://arxiv.org/abs/math/0612843) |
| MSC | 11M26, 11M06 |
| Families | A, B |
| Work type | original_paper |
| Evidence level of this record | **L1-partial** |
| Full text | partial_fulltext — https://arxiv.org/abs/math/0612843 |
| Selection | score 4.5506, in-pool citations 24, seed lists 0, triage relevance 4 |

## Mathematical content (Level 1: full text read)

**Research question.** Given the CFKRS full moment conjecture $\int_0^T|\zeta(1/2+it)|^{2k}dt=\int_0^TP_k(\log\frac t{2\pi})dt+O(T^{1/2+\epsilon})$ with $P_k$ a degree-$k^2$ polynomial defined by a $2k$-fold residue, how can one compute all lower-order coefficients $c_r(k)$ (meromorphically in $k$ and numerically), and do numerics support the conjecture, including non-integer $k$?

**Historical motivation.** CFKRS (2005) conjectured full polynomial asymptotics for the moments, matching Ingham (k=1) and Heath-Brown (k=2) including all lower terms, but only listed coefficients for k<=7 without explanation. Testing the conjecture numerically for k>=3 requires all lower-order terms because the effective main contribution at accessible t comes from r ~ k^2/ (some fraction), not r=0 (e.g. k=4: c_0=2.5e-13 vs c_13 = 38.2).

### Main results

- **THM-PAPER-0058-1** (Conjecture (1.1)-(1.4) [from CFKRS, restated], conjecture (imported), scope: asymptotic; Sec. 1.1). For positive integer $k$ and $\epsilon>0$: $\int_0^T|\zeta(\tfrac12+it)|^{2k}dt=\int_0^TP_k(\log\tfrac t{2\pi})dt+O_{k,\epsilon}(T^{1/2+\epsilon})$, where $P_k(x)=\dfrac{(-1)^k}{k!^2(2\pi i)^{2k}}\oint\!\!\cdots\!\oint\dfrac{G(z)\Delta^2(z)\,e^{\frac x2\sum_{i=1}^k(z_i-z_{i+k})}}{\prod_{i=1}^{2k}z_i^{2k}}dz$, $G=A_k(z)\prod_{i,j\le k}\zeta(1+z_i-z_{j+k})$, $A_k$ the Euler product (1.4)=(1.5). *Conditional on:* unproved conjecture.
- **THM-PAPER-0058-2** (Theorem 1.2 (1.16)-(1.17), theorem (algebraic identity for conjectured polynomial), scope: global; Sec. 1.2, proved Sec. 2.1-2.2). Writing $P_k(x)=c_0(k)x^{k^2}+c_1(k)x^{k^2-1}+\dots+c_{k^2}(k)$: $c_r(k)=a_k\prod_{l=0}^{k-1}\frac{l!}{(k+l)!}\sum_{|\alpha|+|\beta|=r}2^{1-\delta(\alpha;\beta)}b_k(\alpha;\beta)N_k(\alpha;\beta)$, where $a_k=\prod_p(1-p^{-1})^{k^2}{}_2F_1(k,k;1;1/p)$, $b_k(\alpha;\beta)$ are Taylor coefficients of $a_k^{-1}A_k(z)\prod_{i,j}(z_i-z_{j+k})\zeta(1+z_i-z_{j+k})$, $\delta(\alpha;\beta)=1$ iff $\alpha=\beta$, and $N_k(\alpha;\beta)=2^{k^2-r}\big(\prod_l\frac{l!}{(k+l)!}\big)^{-1}\sum_{\text{distinct rearrangements}}\tilde M_k(\sigma(\alpha),\tau(\beta))$ with $\tilde M_k$ a $2k\times2k$ determinant (2.63). (Exponent of 2 in $N_k$ as extracted: $1/2^{k^2-r}$ prefactor.)
- **THM-PAPER-0058-3** (Leading coefficient (1.6)-(1.7), theorem (computed from the conjecture), scope: asymptotic; Sec. 1.1, derived Sec. 2.1 (2.2)-(2.8), Lemmas 2.1-2.3). $c_0(k)=a_k\prod_{j=0}^{k-1}\dfrac{j!}{(j+k)!}$ with $a_k=\prod_p(1-p^{-1})^{k^2}{}_2F_1(k,k;1;1/p)$, agreeing with the Keating-Snaith leading constant.
- **THM-PAPER-0058-4** (Theorem 1.3, theorem, scope: global; Sec. 1.2, proof Sec. 3 (Lemma 3.1, Theorem 3.2)). $N_k(\alpha;\beta)$ is a polynomial in $k$ of degree at most $2(|\alpha|+|\beta|)$ (hence determined by evaluation at $2(|\alpha|+|\beta|)+1$ integer values and interpolation).
- **THM-PAPER-0058-5** (Theorem 1.4, theorem, scope: global; Sec. 1.2, proof Sec. 2.1). The Taylor coefficients $b_k(\alpha;\beta)$ are polynomials in $k$, the Taylor coefficients of $s\zeta(1+s)$, and the Taylor coefficients of $\log A_k(z_1,\dots,z_{2k})$; the latter are sums over primes $p$ of rational functions in $k,p,\log p$ and finitely many ${}_2F_1(k_1,k_2;m;1/p)$, $k_1,k_2\ge k$, $m\ge1$.
- **THM-PAPER-0058-6** (Lemma 1.1 (CFKRS Sec 2.5), lemma (imported), scope: global; Sec. 1.1 (1.11)). For $F$ symmetric in $u_1..u_k$ and in $v_1..v_k$, regular near 0, and $f$ with a simple pole of residue 1 at 0, $H=F\prod_{i,j}f(u_i-v_j)$: the $2k$-fold residue $\frac{(-1)^k}{k!^2(2\pi i)^{2k}}\oint H\Delta^2/\prod_{i,j}(z_i-\alpha_j)$ equals $\sum_{\sigma\in\Xi}H(\alpha_{\sigma(1)},\dots,\alpha_{\sigma(2k)})$, over the $\binom{2k}k$ permutations with $\sigma(1)<..<\sigma(k)$, $\sigma(k+1)<..<\sigma(2k)$.
- **THM-PAPER-0058-7** (Shifted moment conjecture (1.9)-(1.10), conjecture (imported), scope: asymptotic; Sec. 1.1). $\int_0^TZ(\tfrac12+it+\alpha_1)\cdots Z(\tfrac12+it+\alpha_{2k})dt\sim\int_0^TP_k(\alpha,\log\frac t{2\pi})dt$ with $Z(s)=\chi(s)^{-1/2}\zeta(s)$, $-1/4<\Re\alpha_j$, $P_k(\alpha,x)$ the residue integral (1.10) around poles $z_i=\alpha_j$.
- **THM-PAPER-0058-8** (Numerical verification (Sec. 5, Tables 1-6), computational evidence, scope: computational; Sec. 5). For $k=3,\dots,7$ and seventeen intervals $[50000n,50000(n+1)]$, $n=0..16$, the integral of $|\zeta|^{2k}$ (computed by integrating between consecutive zeros) agrees with $\int P_k(\log\frac t{2\pi})dt$ to ~3 significant figures or better (relative differences plotted in Figure 1); for non-integer $k=0.5,1.8,3.2,0.5+i$ the truncated series $\sum_{r\le R}c_r(k)\log(t/2\pi)^{k^2-r}$ is compared at $D=10^3,10^4,10^5$.

### Key definitions

- P_k(x): moment polynomial of degree k^2
- A_k(z_1..z_{2k}): arithmetic Euler product (1.4)-(1.5)
- a_k: arithmetic factor A_k(0)
- b_k(alpha;beta): Taylor coefficients of a_k^{-1} A_k prod (z_i - z_{j+k}) zeta(1+z_i-z_{j+k})
- N_k(alpha;beta): polynomial-in-k combinatorial weights

### Principal lemmas

- **THM-PAPER-0058-L1** (Lemma 2.1; Sec. 2.1). $\Delta(\partial_{x_1},\dots,\partial_{x_n})\prod_if(x_i)=\det\big(f^{(j-1)}(x_i)\big)_{n\times n}$. — *Role:* Converts Vandermonde differential operator into a Wronskian-type determinant.
- **THM-PAPER-0058-L2** (Lemma 2.2; Sec. 2.1). $\Delta(\partial_{x_{1..2k}})\Delta(\partial_{x_{1..k}})\Delta(\partial_{x_{k+1..2k}})\prod_{i\le2k}f(x_i)$ at $x_{1..k}=1$, $x_{k+1..2k}=-1$ equals $k!^2\det$ of a $2k\times2k$ matrix with the first $k$ rows $f^{(i+j-2)}(1)$ and last $k$ rows $f^{(i+j-2)}(-1)$. — *Role:* Gives the leading coefficient and the determinant $\tilde M_k$ for lower coefficients (with $f(x)=x^{2k-1}/(2k-1)!$ exponential generating structure).
- **THM-PAPER-0058-L3** (Lemma 2.4; Sec. 2.2). The determinant $\tilde M_k(\sigma(\alpha),\tau(\beta))$ in (2.63) vanishes unless $\alpha_{\sigma_1},\dots$ satisfy a distinctness/consecutiveness condition on the shifted indices (so only $O_r(1)$ rearrangements contribute). — *Role:* Makes the sum over rearrangements finite and independent of $k$ in count.
- **THM-PAPER-0058-L4** (Lemma 3.1; Sec. 3). For $e_i,f_i$ with $e_1,e_2+1,..,e_k+k-1$ distinct and likewise $f$, the $2k\times2k$ determinant of reciprocal Gamma values reduces to a $k\times k$ determinant of binomial-type entries after eliminating the complementary subset $c_1..c_k$ of $\{0,..,2k-1\}$. — *Role:* Step reducing $2k\times 2k$ to $k\times k$ determinant to prove polynomiality in $k$.
- **THM-PAPER-0058-L5** (Theorem 3.2; Sec. 3 (3.10)). If $c_j=k+j-1-\epsilon_j$ with $\epsilon_j=0$ for $j>t$ and $\tilde\lambda_1\ge\dots\ge\tilde\lambda_s>0=\tilde\lambda_{s+1}=\dots=\tilde\lambda_k$, then $\det\big((c_i)_{\tilde\lambda_j+k-j}\big)_{k\times k}=(-1)^{k(k-1)/2}\Delta(c)\times(\text{polynomial in }k\text{ of degree}\le2\sum\tilde\lambda_i)$. — *Role:* Core of the polynomiality proof via Chen-Louck factorial Schur functions [CL].
- **THM-PAPER-0058-L6** (Lemma 2.3; Sec. 2.1, Lemma 2.3 (statement summarized from line 787; hypotheses A,B>=1 integers, 0<=t<1)). Evaluation of the Euler-factor integral $\int_0^1\prod_j(1-e(\theta)/p^{1/2+z_j})^{-1}(1-e(-\theta)/p^{1/2-z_{k+j}})^{-1}d\theta$ at zero shifts gives ${}_2F_1(k,k;1;1/p)$ (A,B,C integer statement; used to show $A_k(0)=a_k$). — *Role:* Identifies leading arithmetic factor.

### Proof architecture

Three layers. (1) Algebra: rewrite the 2k-fold residue by introducing auxiliary variables x_i, extracting the Vandermonde as a differential operator (2.4)-(2.8), reducing to the 2k x 2k determinant of Lemma 2.2; Taylor-expand A_k * prod (z_i - z_{j+k}) zeta(1+z_i-z_{j+k}) (the poles of zeta cancel k^2 Vandermonde factors, leaving a degree-k^2 polynomial) to define b_k(alpha;beta); sum gives Thm 1.2 and Thm 1.4 (b_k explicit via log A_k Taylor coefficients and hypergeometric sums over primes). (2) Polynomiality in k of N_k (Thm 1.3): Lemma 3.1 reduces the 2k x 2k determinant to a k x k determinant of factorial-power entries, Thm 3.2 (Chen-Louck factorial Schur functions) gives polynomial dependence; interpolation at 2(|alpha|+|beta|)+1 integers then gives meromorphic expressions in k. (3) Numerics: Method 1 (tables of N_k polynomials + Taylor data of A_k) for first ~10 coefficients incl. non-integer k; Method 2 (combinatorial sum (1.11) with tiny distinct shifts and very high working precision to defeat order-k^2 pole cancellation) for all k^2+1 coefficients, k<=8. Then comparison with integrals of |zeta|^{2k} between consecutive zeros on 17 intervals of length 50000, plus non-integer k as asymptotic series.

**Imported results.** CFKRS 'Integral moments of L-functions' (Proc LMS 91, 2005): conjecture (1.1)-(1.4), Lemma 1.1, Euler product A_k; Chen-Louck, 'The factorial Schur function', J. Math. Phys. 34 (1993), Thms 3.2, 3.3; Keating-Snaith leading term; Ingham/Heath-Brown for k=1,2 full agreement; Rubinstein L-function calculator for zeros

**Techniques.** multidimensional residue calculus; Vandermonde as differential operator; factorial Schur functions (Chen-Louck); polynomial interpolation in k; hypergeometric-function evaluation of Euler factors; high-precision cancellation of apparent poles with small distinct shifts; numerical integration of |zeta|^{2k} between consecutive zeros

## Context and interpretation

**Importance and obstacle overcome.** Provides an algorithm and closed-form structure (polynomial in k) for all conjectured lower order terms, enabling genuine numerical tests and study of non-integer k (where P_k is an asymptotic series). Obstacle: the Vandermonde prevents separating integrals and the individual terms in (1.11) have poles that cancel only in the sum; solved by differential-operator trick and high-precision small-shift cancellation.

**Relation to prior work.** 

**Limitations and open questions.** The moment conjecture itself remains unproved for k>=3 (and for all k>2 even the leading order is open; asymptotic results known only for k=1 [Ingham] and k=2 [Heath-Brown]). The authors note debate over the error term O(T^{1/2+eps}) (cf. other families, Zhang), and that numerics are limited ('not too extensive'). For non-integer k, P_k is an infinite asymptotic series with no stated remainder. Uniformity in k is not addressed.

## Research potential

- **Hypotheses that might be weakened.** The conjecture's error O(T^{1/2+eps}) could be tested at larger heights with 'more detailed testing concerning the nature of the remainder' (authors' own suggestion); the restriction to positive integer k can be relaxed to real/complex k as an asymptotic series.
- **Generalizations.** Method (residue + factorial Schur polynomiality in k) extends to unitary, symplectic, orthogonal families (Sec. 6) and could be applied to ratios conjecture, to moments of zeta'(1/2+it)-type derivatives, to moments over short intervals, and to Dedekind/GL(2) L-functions.
- **Candidate connections.** Feeds the maximum-size conjecture of Farmer-Gonek-Hughes (CAND-01208): their formula (3.3) is the leading-order version used for maximum bounds, and the lower-order structure here quantifies corrections in k ~ sqrt(log T/loglog T) regime; Soundararajan (CAND-01201) gives RH-conditional upper bound T(log T)^{k^2+eps}, consistent with c_0(k)x^{k^2}; Harper's sharp upper bound (log T)^{k^2} (RH) and Heap-Radziwill-Soundararajan; Hughes thesis; Basor-Bleher-Buckingham-Grava-Its-Its-Keating on exact large-k asymptotics of c_r(k) via Painleve.
- **Reusable lemmas.** Lemma 2.1-2.2 (Vandermonde-differential-operator to determinant) and Theorem 3.2 (factorial Schur reduction) are reusable for any Cauchy-type multi-residue with Vandermonde squared.
- **Possible experiments.** Recompute the table with higher k (k<=10) and larger T (Odlyzko zero data near 10^{20}-10^{23}) to test the T^{1/2+eps} remainder; compare c_r(k) polynomial structure in k with random-matrix exact coefficients (Keating-Snaith) to isolate the arithmetic effect; test Theorem 1.3 degree bound by interpolation for small |alpha|+|beta| and check against stated tables; fit zero distribution of P_k(x) (Sec. 5.1 zeros of P_k) to find uniform asymptotics.
- **Risks / barriers.** No proof strategy for the moment conjecture; numerics at T<=10^6 rely on very high lower-order terms (r ~ k^2/ some fraction), so discrepancy in leading order could be masked; numerical stability of method 2 requires extreme precision (order k^2 pole cancellation); results are only as reliable as the unproved CFKRS recipe (recipe validity for k>=3 with error T^{1/2} contested).

## Audit notes (Level 1 reader)

In Theorem 3.2's proof statement the Vandermonde $\Delta(c)$ is defined with index bound '1<=i<j<=m' while c has k entries (likely m=k; notational slip, Sec. 3 around (3.11)). In the introduction the text says 'In Section 2.1 we prove Theorems 1.2 and 1.4' while Section 2.2 'Determining c_r(k)' contains the final assembly of Thm 1.2; minor organizational inconsistency. The extracted statement of (1.17) has prefactor 1/2^{k^2-r}; I read it from OCR and did not verify the power of 2 against the proof. Statement of Lemma 2.3 and Lemma 2.4 recorded from partial reading (headers and surrounding text), not full verification. I did not verify the numerical tables beyond their structure.

*These notes are a reader's observations, not verified findings; see `audits/` for adjudicated findings.*

## Provenance

- Candidate `CAND-01239`; harvest queries: msc_11M06, msc_11M26, arxiv_moments_zeta.
- Triage decision: include — Full moment conjecture with lower-order terms and numerics.
- Record generated by `tools/make_records.py`; search cutoff 2026-11-17.
