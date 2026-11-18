# PAPER-0018 — Multiplicative functions in short intervals

| Field | Value |
|---|---|
| Authors | Matomäki, Kaisa; Radziwiłł, Maksym |
| Year / stratum | 2016 / S6 |
| Venue | Ann. Math. (2) 183, No. 3, 1015-1056 (2016). |
| Identifiers | zbMATH [1339.11084](https://zbmath.org/?q=an:1339.11084) · DOI [10.4007/annals.2016.183.3.6](https://doi.org/10.4007/annals.2016.183.3.6) · arXiv [1501.04585](https://arxiv.org/abs/1501.04585) |
| MSC | 11N37, 11N56 |
| Families | A, H |
| Work type | original_paper |
| Evidence level of this record | **L1** |
| Full text | fulltext_read — https://arxiv.org/abs/1501.04585 |
| Selection | score 4.6089, in-pool citations 29, seed lists 0, triage relevance 4 |

## Mathematical content (Level 1: full text read)

**Research question.** Show that short-interval averages of a real multiplicative function f:N->[-1,1] over [x,x+h] agree with the long average over [X,2X] for almost all x, uniformly in f and with h allowed to grow arbitrarily slowly. Consequences: cancellation of mu(n) in almost all intervals [x,x+psi(x)], psi->infinity; X^eps-smooth numbers in [x,x+C(eps)sqrt(x)]; a non-trivial bound on the Liouville correlation lambda(n)lambda(n+h); positive proportion of sign changes of multiplicative functions.

**Historical motivation.** Cancellation of mu in short intervals was known only conditionally (density hypothesis for h>=x^eps; RH for h>(log X)^A, unpublished Gao) or unconditionally for h>=x^{1/6+eps} (Ramachandra). Earlier: Matomaki-Radziwill on cusp form coefficients; Chowla's conjecture and Hildebrand's remark that even lim inf of lambda(n)lambda(n+1) average <1 was unknown.

### Main results

- **THM-PAPER-0018-1** (Theorem 1, theorem, scope: asymptotic; Section 1, p.1-2). Let $f:\mathbb N\to[-1,1]$ be multiplicative. There are absolute constants $C,C'>1$ (one may take $C'=20000$) such that for all $2\le h\le X$ and $\delta>0$: $\left|\frac1h\sum_{x\le n\le x+h}f(n)-\frac1X\sum_{X\le n\le 2X}f(n)\right|\le\delta+C'\frac{\log\log h}{\log h}$ for all but at most $CX\left(\frac{(\log h)^{1/3}}{\delta^2h^{\delta/25}}+\frac1{\delta^2(\log X)^{1/50}}\right)$ integers $x\in[X,2X]$.
- **THM-PAPER-0018-2** (Theorem 2, theorem, scope: asymptotic; Section 1, p.2 (display garbled in extracted text; normalization of the main term should be checked against the PDF)). Let $f:\mathbb N\to[-1,1]$ be multiplicative. For $10\le h\le x$, the bilinear average $\frac{1}{h\sqrt x\log 2}\sum_{x\le n_1n_2\le x+h,\ \sqrt x\le n_1\le2\sqrt x}f(n_1)f(n_2)$ equals $\frac1{\sqrt x}\big(\ldots\big)$ the product of long averages $\frac1{\sqrt x}\sum_{\sqrt x\le n\le2\sqrt x}f(n)$ squared, up to an error $O\big(\frac{\log\log h}{\log h}+\frac1{(\log x)^{1/100}}\big)$ (the precise normalization of the main term is as printed on p.2: the square of the mean of f over [sqrt x,2 sqrt x]). Uniform in h and f.
- **THM-PAPER-0018-3** (Corollary 1, corollary, scope: asymptotic; Section 1, p.2-3). For every $\varepsilon>0$ there is $C(\varepsilon)>0$ such that $[X,X+C(\varepsilon)\sqrt X]$ contains at least $\sqrt X(\log X)^{-4}$ integers that are $X^{\varepsilon}$-smooth, for all large X. For small fixed eps one can take $C(\varepsilon)=\rho(1/\varepsilon)^{-13}$ (via Theorem 4); remark: $\rho^{-7}$ and exponent $\log 4$ with extra work.
- **THM-PAPER-0018-4** (Corollary 2, corollary, scope: asymptotic; Section 1, p.3). For every integer $h\ge1$ there is $\delta(h)>0$ with $\left|\frac1X\sum_{n\le X}\lambda(n)\lambda(n+h)\right|\le1-\delta(h)$ for all large X; same for any completely multiplicative $f:\mathbb N\to[-1,1]$ with f(n)<0 for some n. For h=1 also valid for multiplicative f completely multiplicative at 2.
- **THM-PAPER-0018-5** (Corollary 3, corollary, scope: asymptotic; Section 1, p.4). A multiplicative $f:\mathbb N\to\mathbb R$ has a positive proportion of sign changes in $[1,x]$ iff $f(n)<0$ for some $n>0$ and $f(n)\ne0$ for a positive proportion of integers n.
- **THM-PAPER-0018-6** (Corollary 4, corollary, scope: asymptotic; Section 1, p.4; refinement in Section 2, p.7). If f real multiplicative, f(n)<0 for some n, and f(n)!=0 on a positive proportion of integers, then for any $\psi(x)\to\infty$ almost every interval $[x,x+\psi(x)]$ contains a sign change of f. Via Theorem 3, exceptional set in [X,2X] has measure $O_\varepsilon(Xh^{-1/6+\varepsilon}+(\log X)^{-1/50})$ for intervals of length h.
- **THM-PAPER-0018-7** (Corollary 5, corollary, scope: asymptotic; Section 1, p.5). If $f$ is completely multiplicative, f(n)<0 for some n, and f!=0 on a positive proportion of integers, there is C>0 with a sign change of f in $[x,x+C\sqrt x]$ for all large x. In particular every $[n,n+C\sqrt n]$ contains integers with even and with odd Omega.
- **THM-PAPER-0018-8** (Corollary 6, corollary, scope: asymptotic; Section 1, p.5). For $\psi(x)\to\infty$ and fixed $u>0$, for almost all x the number of $x^{1/u}$-smooth integers in $[x,x+\psi(x)]$ is $\sim\rho(u)\psi(x)$.
- **THM-PAPER-0018-9** (Theorem 3 / Theorem 4, theorem, scope: asymptotic; Section 2, p.6-7). Variants of Theorems 1 and 2 restricted to a dense set $S_X$ of integers with a prime factor in each of a chain of intervals $[P_j,Q_j]$, $j\le J$ (parameter $\eta\in(0,1/6)$, $[P_1,Q_1]\subset[1,h]$). Theorem 3: $\frac1X\int_X^{2X}\left|\frac1h\sum_{x\le n\le x+h,n\in S}f(n)-\frac1X\sum_{X\le n\le2X,n\in S}f(n)\right|^2dx\ll\frac{(\log h)^{1/3}}{P_1^{1/6-\eta}}+\frac1{(\log X)^{1/50}}$.

### Key definitions

- Multiplicative f:N->[-1,1]
- Distance D(f,g;x)^2=sum_{p<=x}(1-Re f(p)conj(g(p)))/p
- Dense set S_X of integers with a prime factor in each [P_j,Q_j], j<=J
- Sets T_j and exceptional set U of the t-range
- Sign change of a multiplicative function allowing zeros (k sign changes if integers n_1<...<n_{k+1} with f(n_i)!=0 alternating)

### Principal lemmas

- **THM-PAPER-0018-L1** (Proposition 1; Section 8). For f real multiplicative with |f|<=1 and S as in Section 2, $\int_{-T}^{T}|F(1+it)|^2dt\ll(T+1)\left(\frac{(\log Q_1)^{1/3}}{P_1^{1/6-\eta}}+\frac1{(\log X)^{1/50}}\right)$ in the form printed (check against PDF), where $F(s)=\sum_{X\le n\le2X,n\in S}f(n)n^{-s}$; this mean-square bound on $\int_{(\log X)^{1/15}}^{X/h}$ gives (5) and hence Theorems 3-4. — *Role:* Core analytic input: mean square of the restricted Dirichlet polynomial on the line Re s=1
- **THM-PAPER-0018-L2** (Lemma 1; Section 3). Halász-type pointwise bound: for f real multiplicative, $|F(\sigma+it)|\ll x^{1-\sigma}\big(M e^{-M}+\frac1{T_0}+\frac{\log\log x}{\log x}\big)$ with $M=\min_{|t_0|\le T_0}D(f,p^{it+it_0};x)^2$. — *Role:* Gives saving on Dirichlet polynomials for |t|>(log X)^{1/15}, because f real cannot pretend to be n^{it}
- **THM-PAPER-0018-L3** (Lemma 2; Section 3). For $|f|\le1$ real multiplicative, fixed A, $1\le|\alpha|\le x^A$: $D(f,p^{i\alpha};x)\ge(\frac1{2\sqrt3}-\varepsilon)\sqrt{\log\log x}+O(1)$. — *Role:* Lower bound on pretentious distance (after Granville-Soundararajan)
- **THM-PAPER-0018-L4** (Lemma 9; Section 6). Halász inequality for integers: for well-spaced T, $\sum_{t\in T}|A(it)|^2\ll(N+|T|\sqrt T)\log2T\sum_{n\le N}|a_n|^2$. — *Role:* Imported large-values estimate (Iwaniec-Kowalski Thm 9.6)
- **THM-PAPER-0018-L5** (Lemma 11; Section 6, proof via duality principle (Lemma 10)). Halász inequality for primes: for $P(s)=\sum_{P\le p\le2P}a_pp^{-s}$ and well-spaced $\mathcal T\subset[-T,T]$, $\sum_{t\in\mathcal T}|P(it)|^2\ll\big(P+|\mathcal T|P\exp(-\frac{\log P}{(\log T)^{2/3+\varepsilon}})\big)\sum_{P\le p\le2P}\frac{|a_p|^2}{\log P}$. — *Role:* New: recovers the log factor lost by the generic large-sieve for prime-supported polynomials when |T| is tiny; this is what saves the final power of log in the exceptional set U
- **THM-PAPER-0018-L6** (Lemma 12; Section 7, footnote 1 p.9). Mean-value estimate for the Buchstab/Ramaré-type decomposition: for bounded sequences with $a_{mp}=b_mc_p$ whenever $p\nmid m$, the integral over T of $|Q_{v,H}R_{v,H}|^2$ is bounded in terms of sums over short ranges of p; correct form uses the indicator 1_{(p,m)=1} (footnote 1: published version had a gap here, repaired in v4). — *Role:* Handles the iterative decomposition over the sets T_j; footnote credits Sedunova and Wang for finding the gap in the published version
- **THM-PAPER-0018-L7** (Identity (9); Section 2.1, p.9). Buchstab/Ramaré-type identity for completely multiplicative f: $\sum_{n\in S}\frac{f(n)}{n^{1+it}}=\sum_{P_j\le p\le Q_j}\frac{f(p)}{p^{1+it}}\sum_{m\in S_j}\frac{f(m)}{m^{1+it}}\frac1{\#\{P_j\le q\le Q_j:q|m\}+1_{(p,m)=1}}$ (restricted to X/p<=m<=2X/p). — *Role:* Extracts a short prime polynomial that is small when t is in T_j

### Proof architecture

Use the Parseval/Plancherel-type reduction: short-interval average minus long average is controlled by int over (log X)^{1/15}<=|t|<=X/h of |F(1+it)|^2 (eq. (5)), where F is the Dirichlet polynomial of f over a dense set S of integers having a prime factor in each of a ladder of ranges [P_j,Q_j] (choice (4)). Integers outside S are few by sieve. The t-range is split into sets T_j (where all narrow subpolynomials of sum_{p in [P_j,Q_j]} f(p)p^{-1-it} are small) and a sparse exceptional set U (measure O(T^{1/2-eps})). On T_j apply the Buchstab/Ramaré identity (9) to pull out a prime polynomial pointwise small, and a mean-value theorem for the remaining polynomial; for j>1 the remaining polynomial is too short so one uses the existence of a large narrow prime polynomial in [P_{j-1},Q_{j-1}] and raises it to a power l (11) so that the length reaches X/h; conditions (2),(3) on the ladder arise from this. On U use the same decomposition, Halász's large values for well-spaced points (Lemma 9), the new prime version (Lemma 11), and Halász's theorem on multiplicative functions (Lemma 1, uses f real so not close to n^{it}). Theorems 1,2 follow by removing S via sieve. Imported: Halász's theorem and large sieve/mean value theorems for Dirichlet polynomials (Iwaniec-Kowalski, Montgomery-Vaughan), Granville-Soundararajan distance lower bound.

**Imported results.** Halász's theorem on mean values of multiplicative functions (Granville-Soundararajan corollary form); Mean value theorem for Dirichlet polynomials / Halász-Montgomery large values (Iwaniec-Kowalski Thm 9.6); Granville-Soundararajan lower bound for pretentious distance; Duality principle (Lemma 10)

**Techniques.** Halász's theorem on mean values of multiplicative functions and pretentious distance; Parseval/Plancherel reduction of short-interval variance to Dirichlet-polynomial mean square on Re s=1; Buchstab / Ramaré-type identity to factor out a prime Dirichlet polynomial; Iterative decomposition over a ladder of prime ranges [P_j,Q_j]; Mean value and Halász large-values theorems for Dirichlet polynomials; New Halász inequality for prime-supported polynomials via duality principle; Sieve to control the exceptional integers; Bilinear (n1 n2) structure to eliminate large prime factors

## Context and interpretation

**Importance and obstacle overcome.** Breaks the barrier that cancellation of mu in short intervals required zero-density input (density hypothesis gives h>=x^eps, RH gives (log X)^A). The obstacle is that on the critical line near 1 + it one has no pointwise control of the full Dirichlet polynomial for large t, which they overcome by decomposing into prime ranges so that Halász (via real-valuedness of f) supplies the saving without zeta zero information. Settled long-standing folklore conjecture lambda(n)lambda(n+1) bounded by 1-delta, and gave the first positive proportion of sign changes of mu (previous best x/(log x)^{7+eps}).

**Relation to prior work.** Improves on Ramachandra (x^{1/6+eps} unconditional), Harman-Pintz-Wolke (sign changes of mu, x/(log x)^{7+eps}), Hildebrand and Croot (sign changes of multiplicative functions), Soundararajan (smooth numbers in [x,x+sqrt x], conditional on RH), Croot, Matomaki, Balog. Extends the authors' cusp-form paper [30] and precedes Matomaki-Radziwill-Tao on complex f and averaged Chowla.

**Limitations and open questions.** Result is for almost all x, not all x. Theorem 1 fails for complex f (f(p)=p^{it}); extension to non-n^{it}-pretentious complex f is in Matomaki-Radziwill-Tao. Not all short intervals: for y(x)<exp(((2+o(1))log x loglog x)^{1/2}) no general result is possible (rigged signs on distinct primes). Intervals of length ~sqrt(X) only with bilinear structure (Theorem 2); the full conjecture that every [x,x+sqrt x] contains x^eps-smooth numbers is open (Corollary 1 gives only a positive proportion count at the C(eps) scale). Chowla's conjecture itself is not proved; only delta(h)>0 gap from the trivial bound. Authors flag forthcoming work on multiplicative functions vanishing on primes, k-fold divisor function, and smooth numbers with theta>1/2.

## Research potential

- **Hypotheses that might be weakened.** Real-valuedness of f is used to apply Halász (no pretending to n^{it}); extended to non-pretentious complex f in MRT. Hypothesis f=mu with h=X^eps needs only a simple argument (their short note [29]); the full uniform range in log h requires J>1 ladder steps. Constraint 2<=h with exceptional set bound h^{-delta/25}: improving the exponent delta/25 or the (log X)^{-1/50} would matter for effective applications.
- **Generalizations.** Replace mu by f with f(p)=0 on a positive proportion of primes (announced); k-fold divisor function (|f(p)| not bounded by 1); Fourier coefficients of cusp forms (Matomaki-Radziwill, Lester); function fields; arithmetic progressions; polynomial phases.
- **Candidate connections.** Signed native/Möbius cancellation programme: Theorem 1 with f=mu gives an unconditional almost-all-short-interval cancellation statement of Mertens-type partial sums over [x,x+psi(x)], which is incomparable to RH (which needs the global bound M(x)=O(x^{1/2+eps})). Chowla-type correlations via Corollary 2 and Tao's log-averaged results. Can be used to test whether any short-interval sign-pattern argument could substitute for density hypotheses in explicit-formula arguments.
- **Reusable lemmas.** Lemma 11 (Halász inequality for primes) and Lemma 12 are reusable large-values tools for prime-supported polynomials; Lemma 1/2 packaged Halász consequence; identity (9) as a decomposition tool; the ladder design (2)-(4) of prime ranges.
- **Possible experiments.** Numerically measure the proportion of x in [X,2X] for which |sum_{x<=n<=x+h} mu(n)|/h exceeds delta, for h from 10 to 10^6 and X up to 10^9, and compare with the bound C(log h)^{1/3}/(delta^2 h^{delta/25}) to see how pessimistic the exponent delta/25 is. Also compute smallest C(eps) empirically for x^eps-smooth numbers in [x,x+C sqrt x].
- **Risks / barriers.** Almost-all structure is intrinsic: nothing here gives information on individual x, hence nothing on M(x) pointwise and no implication to RH. Bounds on the exceptional set (log X)^{-1/50} are weak. Methods are insensitive to zeros of zeta (by design), so they cannot yield RH-type information.

## Audit notes (Level 1 reader)

Footnote 1 p.9 records a correction in v4 to the published (Annals) version: the indicator 1_{(p,m)=1} was written as 1, creating a gap in the proof of Lemma 12; cite v4 rather than the published text for that lemma. The extracted text garbles the display of Theorem 2 (exact normalization of main term) and Proposition 1; those displays should be checked against the PDF. Otherwise none noticed in inspected portion.

*These notes are a reader's observations, not verified findings; see `audits/` for adjudicated findings.*

## Provenance

- Candidate `CAND-01787`; harvest queries: citation_expansion, arxiv_rh_abs.
- Triage decision: include — Landmark short-interval multiplicative function result, Mobius cancellation.
- Record generated by `tools/make_records.py`; search cutoff 2026-11-17.
