# PAPER-0032 — The distribution of the summatory function of the Möbius function

| Field | Value |
|---|---|
| Authors | Ng, Nathan |
| Year / stratum | 2004 / S5 |
| Venue | Proc. Lond. Math. Soc. (3) 89, No. 2, 361-389 (2004). |
| Identifiers | zbMATH [1138.11341](https://zbmath.org/?q=an:1138.11341) · DOI [10.1112/S0024611504014741](https://doi.org/10.1112/S0024611504014741) · arXiv [math/0310381](https://arxiv.org/abs/math/0310381) |
| MSC | 11N56, 11M26 |
| Families | A, C |
| Work type | original_paper |
| Evidence level of this record | **L1** |
| Full text | fulltext_read — arXiv:math/0310381v1 |
| Selection | score 4.5864, in-pool citations 37, seed lists 2, triage relevance 4 |

## Mathematical content (Level 1: full text read)

**Research question.** Under RH and the Gonek-Hejhal bound J_{-1}(T) << T, what can be said about the size and distribution of M(x)=sum_{n<=x} mu(n): bounds, mean squares, existence of a limiting distribution of e^{-y/2}M(e^y), and heuristic true order of large values?

**Historical motivation.** Mertens conjecture was disproved (Odlyzko-te Riele 1985); Heath-Brown asked whether x^{-1/2}M(x) has a distribution function; Odlyzko-te Riele noted no good conjectures on the growth rate of M(x). Ng supplies conditional answers and a heuristic consistent with Gonek's unpublished (log log log x)^{5/4} conjecture.

### Main results

- **THM-PAPER-0032-1** (Theorem 1, theorem, scope: conditional; Introduction p.6; proof Sec. 2). Assume RH and $J_{-1}(T)=\sum_{0<\gamma\le T}|\zeta'(\rho)|^{-2}\ll T$. Then (i) $M(x)\ll x^{1/2}(\log x)^{3/2}$; (ii) $M(x)\ll x^{1/2}(\log\log x)^{3/2}$ outside a set of finite logarithmic measure; (iii) $\int_2^X M(x)^2x^{-1}\,dx\ll X$; (iv) the weak Mertens conjecture $\int_2^X (M(x)/x)^2dx\ll\log X$. *Conditional on:* RH, Gonek-Hejhal k=-1 upper bound.
- **THM-PAPER-0032-2** (Theorem 2, theorem, scope: conditional; Introduction p.7; proof Sec. 3 using Lemmas 6-10). Assume RH and $J_{-1}(T)\ll T$. Then $e^{-y/2}M(e^y)$ has a limiting distribution $\nu$ on $\mathbb R$: $\lim_{Y\to\infty}\frac1Y\int_0^Y f(e^{-y/2}M(e^y))dy=\int f\,d\nu$ for all bounded Lipschitz $f$. *Conditional on:* RH, Gonek-Hejhal k=-1 upper bound.
- **THM-PAPER-0032-3** (Corollary 1, corollary, scope: conditional; Introduction p.8). Assume RH, $J_{-1}(T)\ll T$ and LI (positive ordinates of zeros linearly independent over $\mathbb Q$). Then $\hat\nu(\xi)=\prod_{\gamma>0}\tilde J_0\!\left(\frac{2\xi}{|(\tfrac12+i\gamma)\zeta'(\tfrac12+i\gamma)|}\right)$ with $\tilde J_0(z)=\sum_m(-1)^m(z/2)^{2m}/(m!)^2$. Consequently $\{x:|M(x)|\le\sqrt x\}$ has logarithmic density in (0,1). *Conditional on:* RH, Gonek-Hejhal, LI.
- **THM-PAPER-0032-4** (Theorem 3, theorem, scope: conditional; Introduction p.8-9). Assume RH and $J_{-1}(T)\ll T$. Then $\int_0^Y (M(e^y)e^{-y/2})^2dy\sim\beta Y$ with $\beta=\sum_{\gamma>0}|\rho\zeta'(\rho)|^{-2}<\infty$; equivalently $\int_1^X (M(x)/x)^2dx\sim\beta\log X$. The variance of $\nu$ is $\beta$ (via (19), mean of $e^{-y/2}M(e^y)$ is $o(1)$). *Conditional on:* RH, Gonek-Hejhal.
- **THM-PAPER-0032-5** (Corollary 12, corollary, scope: conditional; Sec. 4.2 end (p.~34-35)). Assume RH, LI, $\sum_{0<\gamma<T}|\rho\zeta'(\rho)|^{-1}\asymp(\log T)^{5/4}$ and $\sum_{\gamma>T}|\rho\zeta'(\rho)|^{-2}\asymp T^{-1}$. Then $\exp(-\exp(\tilde c_1V^{4/5}))\ll\nu([V,\infty))\ll\exp(-\exp(\tilde c_2V^{4/5}))$ for effective $\tilde c_i>0$. *Conditional on:* RH, LI, Gonek-Hejhal-type lower and upper bounds.
- **THM-PAPER-0032-6** (Gonek's Conjecture (20), conjecture (heuristic support only), scope: conditional; Introduction (20); Sec. 4.3). There is $B>0$ with $\limsup_{x\to\infty}M(x)/(\sqrt x(\log\log\log x)^{5/4})=B$ and $\liminf=-B$. Sec 4.3 gives a heuristic (not a proof) from Cor 12 assuming uniform convergence in (69). *Conditional on:* unproved uniformity assumption.

### Key definitions

- $J_{-k}(T)=\sum_{0<\gamma\le T}|\zeta'(\rho)|^{-2k}$
- Gonek-Hejhal conjecture $J_{-k}(T)\asymp T(\log T)^{(k-1)^2}$
- weak Mertens conjecture $\int_2^X(M(x)/x)^2dx\ll\log X$
- LI: positive ordinates of zeros linearly independent over Q
- limiting distribution of $e^{-y/2}M(e^y)$ in the logarithmic-average sense

### Principal lemmas

- **THM-PAPER-0032-L1** (Lemma 1; Sec. 2). (i) $J_{-1/2}(T)\ll T(\log T)^v\Rightarrow\sum_{0<\gamma<T}|\rho\zeta'(\rho)|^{-1}\ll(\log T)^{v+1}$; (ii) $J_{-1}(T)\ll T\Rightarrow\sum_{T<\gamma<2T}|\rho\zeta'(\rho)|^{-2}\ll 1/T$; (iii) tail sums via partial summation for $b>u\ge1$. — *Role:* Converts Gonek-Hejhal moment bounds into the discrete sums used in all later estimates (partial summation).
- **THM-PAPER-0032-L2** (Lemma 4; Sec. 2). Assume RH and simple zeros. For $x\ge2$ and $T$ in a sequence $T_n\in[n,n+1]$ with $1/\zeta(\sigma+iT_n)\ll T^\epsilon$ (Lemma 3): $M(x)=\sum_{|\gamma|<T}x^\rho/(\rho\zeta'(\rho))+\tilde E(x,T)$, $\tilde E\ll x\log x/T+x/(T^{1-\epsilon}\log x)+1$. — *Role:* Explicit formula for M(x), following Titchmarsh Thm 14.27.
- **THM-PAPER-0032-L3** (Lemma 5; Sec. 2 (error term as printed in extracted text is garbled; exact form not verified)). Assume RH and $J_{-1}(T)\ll T$. The explicit formula of Lemma 4 holds for all $T\ge2$ with an extra error term of size $\ll x(\log T)^{1/2}/T$ type, obtained by Cauchy-Schwarz and Lemma 1(ii). — *Role:* Removes the restriction T in {T_n} using the k=-1 Gonek-Hejhal bound.
- **THM-PAPER-0032-L4** (Lemma 6; Sec. 2, eq. (28)). Assume RH and $J_{-1}(T)\ll T$. Then $\int_Z^{e^Z\cdot}\left|\sum_{T\le|\gamma|\le X}x^{i\gamma}/(\rho\zeta'(\rho))\right|^2dx/x\ll(\log T)/T^{?}$ (printed as $(\log T)/T^{1/4}$-type bound in extraction; exact exponent not verified). — *Role:* Key mean-square bound on zero-sum tails; drives Thm 1(ii)-(iv) and weak convergence in Thm 2.
- **THM-PAPER-0032-L5** (Lemma 7; Sec. 3). Kronecker-Weyl variant: for reals $t_1..t_N$ and continuous 1-periodic f, the average of $f(y t_1,...,y t_N)$ over $[0,Y]$ converges to the Haar integral over the closure of the orbit, a J-dimensional sub-torus. — *Role:* Builds limiting measures $\nu_T$ for truncated sums without LI (Rubinstein-Sarnak approach).
- **THM-PAPER-0032-L6** (Lemma 8-9; Sec. 3). Lemma 8: under RH there is a probability measure $\nu_T$ with $\nu_T(f)=\lim\frac1Y\int_0^Yf(\phi^{(T)}(y))dy$ for bounded continuous f. Lemma 9: Helly selection, weak convergence characterization, and Levy continuity theorem. — *Role:* Standard probabilistic machinery for passing $T\to\infty$.
- **THM-PAPER-0032-L7** (Lemma 10; Sec. 3 (p.23)). Assume RH and $J_{-1}(T)\ll T$. For $T\ge2$, $Y\ge\log2$: $\int_{\log2}^Y|\epsilon^{(T)}(y)|^2dy\ll Y(\log T)T^{-1/4}+1$ (exponent as read from extracted text). — *Role:* Shows the truncation error has small mean square, so $\nu_T\to\nu$ and the limit distribution exists.

### Proof architecture

Explicit formula (Lemma 4) with RH and simple zeros; Gonek-Hejhal k=-1 bound converts to discrete tail estimates (Lemma 1) and removes the T_n restriction (Lemma 5). Mean-square bound (Lemma 6) gives Thm 1(ii)-(iv) via Gallagher and Cramer arguments and the existence of the limit distribution (Thm 2) via Rubinstein-Sarnak scheme: Kronecker-Weyl gives nu_T (Lemmas 7-8), Lemma 10 controls truncation, Helly/Levy (Lemma 9) pass to the limit. LI is used only for absolute continuity and the Fourier transform (Cor 1). Tail estimates and the speculation on large values use Montgomery's probabilistic method on the Bessel product.

Dependency edges: Theorem 1 → Lemma 1, Lemma 4, Lemma 5, Lemma 6 (uses); Theorem 2 → Lemmas 6-10 (uses); Corollary 1 → Theorem 2 + LI (extends); Corollary 12 → Corollary 1, Montgomery method (uses); Gonek conjecture (20) → Corollary 12 (heuristic from)

**Imported results.** Titchmarsh Thm 14.27 (explicit formula) and pp.376-380 (weak Mertens implies RH, simple zeros); Cramer 1922 mean-square method; Gallagher 1970 (psi(x)-x outside finite logarithmic measure); Rubinstein-Sarnak 1994 (Lemma 2.3, Chebyshev's bias distribution); Kronecker-Weyl (Hlawka); Helly selection and Levy continuity theorem; Montgomery's unpublished probabilistic argument for psi(x)-x; Odlyzko-te Riele 1985 (disproof of Mertens)

**Techniques.** explicit formula for M(x) via Perron; Cramer / Gallagher mean-square arguments; Rubinstein-Sarnak limiting distribution construction; Kronecker-Weyl equidistribution; Helly selection and Levy continuity; Montgomery probabilistic tail estimates for sums of independent Bessel-type variables

## Context and interpretation

**Importance and obstacle overcome.** Shows that the weak Mertens conjecture and a limiting distribution for M(x)/sqrt(x) follow from RH plus a single negative-moment upper bound J_{-1}(T) << T, which the Gonek-Hejhal / random-matrix conjectures predict (J_{-1}(T) ~ 3T/pi^3). The obstacle is controlling the tail of the explicit-formula sum, where 1/zeta'(rho) is not known to be small; the moment bound gives the mean-square control.

**Relation to prior work.** Follows Cramer, Gallagher, Rubinstein-Sarnak (psi(x)-x and Chebyshev bias), Montgomery's heuristic for psi(x)-x (exponent 2 on log log log x), and Ingham's LI argument for Omega-results of M(x). Theorem 1(i) is attributed to Gonek (unpublished). Liouville function L(x) is claimed to follow similarly via zeta(2s)/zeta(s) but not carried out.

**Limitations and open questions.** All main results are conditional on RH and J_{-1}(T) << T, which implies simple zeros and is unproved; Corollary 1, Cor 12 and the Gonek conjecture additionally need LI or two-sided moment hypotheses. Theorem 2 only for bounded Lipschitz test functions (extension to bounded continuous omitted). The limsup/liminf order of M(x) is only heuristic (Sec 4.3 assumes uniform convergence in (69)). The value of the logarithmic density of {|M(x)|<=sqrt x} is only described as numerically close to 1; the constant B is open.

**Ideas in remarks/appendices/abandoned paths.** Remark that by a more careful calculation an asymptotic can be given in Thm 1(iv) (done in Thm 3); the Liouville extension through zeta(2s); the explanation of the exponent 5/4 vs 2 for M(x) vs psi(x)-x through the discrete moments sum 1/|rho zeta'(rho)| ~ (log T)^{5/4} vs sum 1/|rho| ~ (log T)^2 (Sec 1, p.10).

## Research potential

- **Hypotheses that might be weakened.** Replace J_{-1}(T) << T by a weaker negative-moment or discrete-sum bound; Lemma 6 and Lemma 10 use only the tail bound sum_{T<gamma<2T}|rho zeta'(rho)|^{-2} << 1/T (Lemma 1(ii)), so the existence of nu may need only that. Drop LI for Theorem 2 (already not used).
- **Generalizations.** Liouville function L(x) via zeta(2s)/zeta(s) (stated, not proved); M(x;chi) for Dirichlet L-functions; the analogue with GRH and simple zeros for a single L-function.
- **Candidate connections.** Compare Conrad CAND-01315: both rely on second-moment/LI-type heuristics tied to Montgomery's psi(x)-x conjecture; a failure of the Gonek exponent 5/4 would indicate which negative-moment conjecture fails. Connects to signed Mobius cancellation programme.
- **Reusable lemmas.** Lemma 1 (moment-to-discrete-sum partial summation), Lemma 4/5 (conditional explicit formula for M(x) with controlled error), Lemmas 7-10 (limiting-distribution scaffolding).
- **Possible experiments.** Numerically evaluate sum_{gamma<T}|rho zeta'(rho)|^{-2} using zero tables to estimate beta and the variance of nu; compute the Fourier product (15) truncated to N zeros and compare with the empirical distribution of M(x)/sqrt x on x up to 10^{14}; test J_{-1}(T) ~ 3T/pi^3.
- **Risks / barriers.** The hypothesis J_{-1}(T) << T cannot currently be tested beyond finite computation and implies RH-adjacent simplicity statements; a finite zero census cannot validate the global asymptotic; Cor 12 and the iterated-logarithm conjecture need an unproved uniformity step.

## Audit notes (Level 1 reader)

Introduction p.4 says Odlyzko-te Riele gave no explicit counterexample to '(12)', but (12) is Montgomery's psi(x) conjecture; the Mertens bound |M(x)|<=sqrt x is presumably meant (equation-number slip, arXiv v1). Exponents in Lemmas 6 and 10 and the error term in Lemma 5 are garbled in the extracted text, so exact forms (T^{-1/4}?) are not verified. Sec 4.3 uses an unproved uniformity assumption on (69); it is flagged by the author as heuristic. The statement of Cor 12 requires lower and upper bounds on the discrete sums, beyond Gonek-Hejhal upper bounds.

*These notes are a reader's observations, not verified findings; see `audits/` for adjudicated findings.*

## Provenance

- Candidate `CAND-01212`; harvest queries: kw_RH_any, kw_moments_zeta, msc_11M26, msc_11N56_rh, arxiv_mertens_conj, arxiv_moments_zeta, arxiv_rh_abs.
- Triage decision: include — Conditional limiting distribution of M(x) and weak Mertens; central for Mobius/RH connections.
- Record generated by `tools/make_records.py`; search cutoff 2026-11-17.
