# PAPER-0114 — Around the Davenport-Heilbronn function

| Field | Value |
|---|---|
| Authors | Bombieri, E.; Ghosh, A. |
| Year / stratum | 2011 / S5 |
| Venue | Russ. Math. Surv. 66, No. 2, 221-270 (2011); reprinted from Usp. Mat. Nauk 66, No. 2, 15-66 (2011). |
| Identifiers | zbMATH [1247.11116](https://zbmath.org/?q=an:1247.11116) · DOI [10.1070/RM2011v066n02ABEH004740](https://doi.org/10.1070/RM2011v066n02ABEH004740) |
| MSC | 11M41, 11M26, 11E45 |
| Families | B, G |
| Work type | original_paper |
| Evidence level of this record | **L1** |
| Full text | fulltext_read — https://www.mathnet.ru/php/getFT.phtml?jrnid=rm&paperid=9410&what=fullteng&option_lang=eng |
| Selection | score 4.1371, in-pool citations 22, seed lists 0, triage relevance 4 |

## Mathematical content (Level 1: full text read)

**Research question.** Which Dirichlet series with an RH-type functional equation but no Euler product (Davenport-Heilbronn type, f=(L(s,chi1 psi) e^{-i theta}+conj)/(2cos theta)-type combinations of two Euler products) have zeros in sigma>1, how far right do such zeros reach, and how large can the coefficients b_n of the reciprocal series 1/f(s) be (Landau/Hille problem)? Includes survey of critical-line zero counts for linear combinations of L-functions.

**Historical motivation.** Potter-Titchmarsh 1935 observed Epstein zeta m^2+5n^2 has a zero (0.93+15.67i) off the critical line; Davenport-Heilbronn 1936 and Cassels 1961 proved zeros in sigma>1; question here refined to location of those zeros and coefficient growth of reciprocal.

### Main results

- **THM-PAPER-0114-1** (Theorem 3, theorem (refinement of Landau), scope: global; Sec. 3.4, p. 234-236). Let $f(s)=\sum a_n n^{-s}$, $a_1\neq0$, absolutely convergent for $\sigma>\sigma_a$, and suppose $f$ has a zero in $\sigma>\sigma_a$. Put $\alpha(f)=\sup\{\Re\rho: f(\rho)=0,\ \Re\rho>\sigma_a\}$. Then $1/f(s)=\sum b_n n^{-s}$ converges for $\sigma>\alpha(f)$ and $\limsup_{n\to\infty}\log|b_n|/\log n=\alpha(f)$.
- **THM-PAPER-0114-2** (Theorem 5 / Corollary 6, theorem, scope: asymptotic; Sec. 4, p. 236-238 (proof via Carlson-type truncation of 1/f, reversed)). Let $f(s)=\sum a_n n^{-s}$ with $a_1=1$, $a_n=O(n^{\varepsilon})$, and suppose $f$ has a zero $\rho$ with $\Re\rho=\beta>1$. Then for $1/f=\sum b_n n^{-s}$: $\sum_{n\le X}|b_n|^2/n\gg X^{2\beta-1+o(1)}$ as $X\to\infty$. Corollary 6: with $\sigma^*>1$ the supremum of real parts of zeros, $\sum_{n\le X}|b_n|^2/n\gg X^{2\sigma^*-1+o(1)}$.
- **THM-PAPER-0114-3** (Theorem 7, theorem, scope: global; Sec. 5, p. 241 (via Kronecker's theorem on log p independence, as in Bombieri-Mueller)). For the Davenport-Heilbronn-type family $f(s,\xi;\psi)=\tfrac12[(1-i\xi)L(s,\chi_1\psi)+(1+i\xi)L(s,\chi_3\psi)]$ (chi mod 5 quartic characters, psi principal mod q), let $\sigma(\xi,q)$ be the sup of $\sigma>1$ with a zero at height some $t$. (1) For $\xi=\tan\theta$ real, $\sigma(\xi,q)$ is the unique $\sigma>1$ with $\sum_{p\equiv2,3\ (5),(p,q)=1}\arctan(p^{-\sigma})=\pi/2-|\theta|$. (2) For $\xi$ purely imaginary, $|\xi|>1$, it is the $\sigma>1$ with $\sum_{p\equiv 2,3(5),(p,q)=1}\log\frac{1+p^{-\sigma}}{1-p^{-\sigma}}=\log\frac{1+i\xi}{1-i\xi}$.
- **THM-PAPER-0114-4** (Theorem 8 / Remark 13, theorem, scope: global; Sec. 5 p. 241 and Sec. 7.4 p. 261). For $\xi$ real and a set $P$ of primes, $\sigma(\xi,P)$ solves $\sum_{p\in P,\ p\equiv2,3(5)}\arctan(p^{-\sigma})=\pi/2-|\theta|$. For $P=\{p,q\}$, $p\equiv2,q\equiv3 \pmod 5$, a zero with $\sigma>1$ exists iff $|\xi|>(pq-1)/(p+q)$. Numerically $\sigma(\tau_-,\{2,3\})=2.314909762289685\ldots$ for the second Davenport-Heilbronn function.
- **THM-PAPER-0114-5** (Theorem 9 / Corollary 11, theorem, scope: asymptotic; Sec. 5, p. 242-243). For $\xi$ real, $\sigma(\xi,q)\le\sigma(\xi,1)-\delta(q)$ where $\delta(q)=\frac{S}{1+S}(\sigma(\xi,1)-1)>0$, $S=\sum_{p|q,\,p\equiv2,3(5)}\arctan p^{-\sigma(\xi,1)}$. Consequently, for $n$ coprime to $P(z)=\prod_{p\le z,p\equiv2,3(5)}p$, $b(n,\xi)=O(n^{\sigma(\xi,1)-\nu(z)+o(1)})$ with $\nu(z)\sim z^{-\sigma(\xi,1)}$.
- **THM-PAPER-0114-6** (Lemma 12 + Theorem 14, lemma and theorem (coefficient growth along 2^h 3^k), scope: asymptotic; Sec. 7.4-7.5, p. 260-262). For $p\equiv2,q\equiv3 \pmod 5$ and $\alpha(u,\xi;\{p,q\})=\limsup_{h/(h+k)\to u}\log|b(p^hq^k,\xi)|/\log(p^hq^k)$: $\alpha\le-\frac{u\log|r(u)|+(1-u)\log|s(u)|}{4(u\log p+(1-u)\log q)}$, with $(r,s)$ the minimizing admissible critical point among the list in Lemma 12 (singular points of the generating polynomial $f(z,w)$); equality holds when $(r,s)=(z_\pm(u),z_\pm(1-u))$ with $z_\pm$ given by (7.39). Lemma 12 locates the extrema of $m\log|z|+n\log|w|$ on $\{f=0,|z|,|w|<1\}$, $\xi\ne0,\xi^4\ne1$.
- **THM-PAPER-0114-7** (Sec. 7.6 numerical identification, computational / conjectural identification, scope: computational; Sec. 7.6, p. 262-263 (Fig. 2)). For $p,q=2,3$, $\xi=\tau_-$: $\max_u\alpha(u,\tau_-;\{2,3\})$ is attained at $u=0.71201279109227\ldots$ with value $2.31490976228968512350665794\ldots=\sigma(\tau_-,\{2,3\})$, agreeing with Theorem 3 (which equates limsup growth with $\alpha(f)$). Authors note a direct proof of this equality of the two numbers is not known.
- **THM-PAPER-0114-8** (Sec. 2.1 survey statements, survey (cited, not new), scope: asymptotic; Sec. 2.1, p. 224-227). Linear combinations of L-functions with functional equation of L-type: Selberg's method gives $N_0(f;T)>c\,n^{-1}T\log T$ zeros on the critical line (GL(1)-type, n terms); Bombieri-Hejhal give $\sim n(2\pi)^{-1}T\log T$ zeros on the line under (i) Euler products with Ramanujan, (ii) same functional equation, (iii) independence, (iv) a Riemann hypothesis for the constituents, (v) a weak pair-correlation property; Montgomery conjectured almost all zeros on the line.

### Key definitions

- Davenport-Heilbronn function f(s;tau_pm) with tau_pm=-phi pm sqrt(1+phi^2)
- alpha(f)=sup Re rho over zeros in absolute-convergence half-plane
- sigma(xi,q) rightmost real part of zeros of coprime-to-q truncation
- alpha(u,xi;{p,q}) directional limsup growth exponent

### Principal lemmas

- **THM-PAPER-0114-L1** (Theorem 1 (Landau, Satz 5); Sec. 3, p. 232). If $a_1\ne0$, $f=\sum a_nn^{-s}$ converges for $\sigma>1$ then $1/f$ is a Dirichlet series for large $\sigma$; if moreover $f\ne0$ for $\sigma>1$, then $b_n=O(n^{1+\varepsilon})$. — *Role:* baseline bound sharpened by Theorem 3
- **THM-PAPER-0114-L2** (Theorem 2 (Landau, Satz 12); Sec. 3, p. 232-233). If $f$ converges and has no zeros for $\sigma>\alpha$, $a_1\ne0$, then $1/f$ converges for $\sigma>\alpha$. — *Role:* gives abscissa of 1/f
- **THM-PAPER-0114-L3** (Hille truncation argument inside proof of Thm 3; p. 234-236). Truncation $f_z$ to $\langle P_z\rangle$ (z-smooth integers) preserves a zero near rho by Rouche/argument principle; Landau applied to $1/f_z$ gives upper bound, pole at $\rho_z$ forces $\sum_{n\in\langle P_z\rangle}|b_n|n^{-\beta_z}$ divergent; counting $\#\{n\le2^\nu\}\le\nu^z$ gives $|b_n|>n^{\alpha(f)-o(1)}$. — *Role:* core lower-bound mechanism
- **THM-PAPER-0114-L4** (Kronecker step (5.3); Sec. 5, p. 239-240). For psi principal mod q, the closure of $\{g(\sigma+it,\psi)\}$ equals $V(\sigma,q)=\{\sum F(p^{-\sigma-i\theta_p})\}$ with independent $\theta_p$, where $F(z)=\log\frac{1+z}{1-z}$; zeros with $\sigma>1$ correspond to $\alpha+2i\theta+(2k+1)\pi i\in V(\sigma,q)$. — *Role:* reduces two-Euler-product combinations to a prime-supported series; used exactly because only two Euler products appear
- **THM-PAPER-0114-L5** (Generating function (Sec. 8); Sec. 8, p. 263-264). $\sum_{h,k}a(p^hq^k,\xi)x^hy^k=\frac{1+\xi x-\xi y+xy}{(1+x^2)(1+y^2)}$ for p=2,q=3; reciprocal generating function $F(x,y;\xi)=\frac{(1+x^2)(1+y^2)}{1+\xi x-\xi y+xy}$. — *Role:* alternative (Bohr power series) route to coefficient asymptotics

### Proof architecture

Two independent routes to growth of b_n for f with zeros right of 1: (a) abstract Landau-Hille argument (Thm 1,2,3): zeros of f in sigma>sigma_a give poles of 1/f, so limsup log|b_n|/log n = sup Re rho; (b) explicit arithmetic for two-L-function combinations: Kronecker independence of log p turns zero-existence into the vanishing of a prime-supported series (Thm 7, 8), sieving by primes q moves the rightmost zero left (Thm 9, Cor 11), and a singularity analysis of the algebraic curve f(z,w)=0 for two primes gives the exact multiplicative growth rate (Lemma 12, Thm 14). Sec. 8 recovers rates via Bohr power series in x_i=p_i^{-s}. Value distribution (Sec. 2.2) is cited via Bohr almost periodicity plus Rouche.

Dependency edges: Theorem 3 → Theorem 1 (Landau) (refines); Theorem 3 → Hille truncation argument (uses); Theorem 7 → Kronecker theorem (imports); Theorem 8 → Theorem 7 (generalizes); Theorem 9 → Theorem 7 (derives from); Theorem 14 → Lemma 12 (uses); Sec 7.6 identification → Theorem 3 (depends on)

**Imported results.** Landau 1921 Satz 5, Satz 12 (Dirichlet series reciprocal); Hille: maximal order of t(n) is n^{rho_0+o(1)}; Kronecker theorem (Titchmarsh Ch. XI 11.4); Bohr almost periodicity / Rouche; Bombieri-Hejhal 1995 critical line zeros for linear combinations; Selberg, Karatsuba, Voronin zero-counting results (cited); Bombieri-Mueller (coefficient method)

**Techniques.** Landau/Hille Dirichlet-series inversion; Bohr almost periodicity and Rouche; Kronecker equidistribution for log p; Carlson-type truncation of reciprocal series; algebraic-curve critical-point analysis (resultants, Mathematica); generating functions in infinitely many variables

## Context and interpretation

**Importance and obstacle overcome.** Quantifies the rightmost zero abscissa of the Davenport-Heilbronn functions and ties it exactly to maximal order of Mobius-type coefficients; shows why lacking an Euler product (a single failed axiom) destroys RH even with the right functional equation. Obstacle: Kronecker cannot be applied directly to non-Euler Dirichlet series (log n dependent), overcome by passing to the ratio of two Euler products.

**Relation to prior work.** Extends Bombieri-Mueller on coefficients of reciprocals of Dirichlet series and Landau/Hille; surveys Selberg, Karatsuba, Voronin, Bombieri-Hejhal results on critical-line zeros of linear combinations of L-functions; dedicated to Karatsuba.

**Limitations and open questions.** Explicit analysis restricted to combinations of exactly two Euler products with prime-supported logarithm; Thm 14 handles two primes only; direct proof that max alpha equals sigma(tau_-,{2,3}) not given (identified only via Thm 3); unconditional example sharpening (3.7) (|b_n|>n^{alpha-1-eps}) is asked for (mu(n) example is RH-conditional); Montgomery's conjecture of ~ n(2pi)^{-1}T log T critical zeros open even for zeta; Selberg's lower bound proof for GL(2)-linear combinations not published; simultaneous vanishing of two L-functions not excluded; finite multiplicative relations among n+a for algebraic a open.

## Research potential

- **Hypotheses that might be weakened.** Thm 5 requires a_n=O(n^eps) and a_1=1; try a_n of polynomial growth by shifting sigma_a. Thm 7 needs psi principal mod q; allow nonprincipal psi with |psi(p)|<p.
- **Generalizations.** Replace mod 5 by higher moduli (dimension >1 solution spaces, noted in Sec. 5): Kronecker then needs several ratios, giving a multi-dimensional V(sigma,q) problem. Extend Thm 14 beyond two primes.
- **Candidate connections.** Link sigma(xi,P) formula to Bombieri-Hejhal hypothesis (iv): the same two-Euler-product ratio picture says exactly where RH fails in a nontrivial combination; relate to Farmer-type linear-combination Principle 13.1/13.2 (CAND-02664) and to Selberg-class axiom necessity. Coefficient growth of 1/f vs Mobius-sum bounds relevant to Robin/Mertens-type arguments.
- **Reusable lemmas.** Theorem 3 is a clean general lemma: abscissa of 1/f equals sup Re zeros in the abs. conv. half-plane, usable for any Dirichlet series with zeros right of the abscissa. Equation sum arctan(p^{-sigma})=pi/2-|theta| is a reusable explicit zero-location formula.
- **Possible experiments.** Reproduce Fig. 2 and sigma(tau_-,{2,3})=2.3149097622896851 to high precision from Thm 8 and from the coefficient limsup; extend to {2,3,7,8-type} prime sets and moduli 7, 8 with generating functions; test Thm 9 delta(q) numerically.
- **Risks / barriers.** All explicit results are for zeros in sigma>1 where almost periodicity helps; nothing here constrains the critical strip, so it gives no direct route to RH, only to what must fail without Euler products.

## Audit notes (Level 1 reader)

none noticed in inspected portion (Thm 14 proof and Sec. 6 were only skimmed; the paper itself flags that the equality of max alpha with sigma(tau_-,{2,3}) rests on Theorem 3 rather than a direct computation)

*These notes are a reader's observations, not verified findings; see `audits/` for adjudicated findings.*

## Provenance

- Candidate `CAND-01539`; harvest queries: msc_11M26.
- Triage decision: include — Davenport-Heilbronn function is the classic instructive failure of GRH-type behavior.
- Record generated by `tools/make_records.py`; search cutoff 2026-11-17.
