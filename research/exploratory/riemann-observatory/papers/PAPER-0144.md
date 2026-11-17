# PAPER-0144 — The Riemann Hypothesis: Past, Present and a Letter Through Time

| Field | Value |
|---|---|
| Authors | Alain Connes |
| Year / stratum | 2026 / S7 |
| Venue | Preprint, arXiv:2602.04022 [math.NT] (2026) |
| Identifiers | zbMATH [arXiv:2602.04022](https://zbmath.org/?q=an:arXiv:2602.04022) · arXiv [2602.04022](https://arxiv.org/abs/2602.04022) |
| MSC | 11M06, 11M55, 58B34, 33D60, 34B20 |
| Families | C, D, G |
| Work type | survey |
| Evidence level of this record | **L1** |
| Full text | fulltext_read — arxiv:2602.04022 |
| Selection | score 2.4, in-pool citations 0, seed lists 2, triage relevance 4 |

## Mathematical content (Level 1: full text read)

**Research question.** Survey of approaches to RH plus a proposed route: minimize the Weil quadratic form Q_W restricted to test functions supported in [1/lambda, lambda] (equivalently using primes <= x=lambda^2), show the Mellin transform of the minimizer has all zeros on the critical line, observe numerically that these zeros approximate the first 50 zeta zeros to up to 55 digits using primes <= 13, and reduce RH to convergence of the minimizers as x to infinity (Hurwitz theorem).

**Historical motivation.** Commissioned survey for 165 years of RH; new perspective of approximating zeta zeros by zeros of Mellin transforms of minimizers of Weil's form on finitely many primes, in a 'letter to Riemann'.

### Main results

- **THM-PAPER-0144-1** (Theorem 6.1 (Connes-van Suijlekom), theorem (cited from [32], statement given), scope: global; Sec. 6.1, p. 26 (proof only sketched: trigonometric basis, finite matrices, Hurwitz)). Let $L>0$, $D$ a real distribution on $[0,L]$ and $\tilde D$ the associated even distribution on $[-L,L]$. Assume the quadratic form with Schwartz kernel $\tilde D(x-y)$ defines a lower-bounded selfadjoint operator on $L^2([-L/2,L/2])$ whose minimum of the spectrum is a simple isolated eigenvalue with even eigenfunction $\eta$. Then all zeros of the entire function $\hat\eta(z)$ lie on the real line.
- **THM-PAPER-0144-2** (Letter claim (abstract and Sec. 5), numerical observation plus conditional theorem, scope: computational; Sec. 5, p. 25 (table of 'upper bound' differences)). For the Weil quadratic form restricted to functions supported in $[1,13]$ (primes <= 13, prime powers 2,3,4,5,7,8,9,11,13), the Mellin transform of the minimizer eta has zeros on the critical line (provided the minimum eigenvalue is simple and even, footnote 12), and its first 50 zeros differ from the true zeta zeros by amounts listed from $2.60179\times10^{-55}$ (first zero) up to $0.0209081$ and $0.00212727$ (last listed); computed with trigonometric truncation N=100. *Conditional on:* simplicity and evenness of lowest eigenvalue (footnote 12), convergence as x to infinity (explicitly not proved).
- **THM-PAPER-0144-3** (Proposed proof strategy (end of Sec. 5, Sec. 6.6), conditional reduction / programme, scope: conditional; Sec. 5 p. 25 and Sec. 6.6 p. 30). If the minimal eigenvectors eta_x (recentered theta_x(u)=eta_x(x^{1/2}u)) converge in a suitable sense so that their Fourier transforms converge uniformly on compacts to Riemann's Xi, then by Hurwitz and Thm 6.1 all zeros of Xi are real, i.e. RH. Remaining steps: show the lowest eigenvalue of Q_{W_lambda} is simple with even eigenvector, and that k_lambda approximates theta_x well enough. *Conditional on:* simplicity of smallest eigenvalue of Q_W,lambda, convergence of eta_x (theta_x) to E(h), uniform convergence of Fourier transforms on compacts.
- **THM-PAPER-0144-4** (Fact 6.2, fact (Riemann's formula), scope: global; Sec. 6.2, p. 26-27). $\Xi(t)=\int_0^\infty k(u)u^{it}d^*u$ with $k=E(h)$, $E(f)(u)=u^{1/2}\sum_{n\ge1}f(nu)$, and $h$ (up to scalar) the unique linear combination of Hermite functions $h_0,h_4$ (eigenfunctions of $H=-\partial^2+4\pi^2u^2$) with vanishing integral; explicitly $h(u)=\frac{\pi}{2}(2\pi u^2-3)e^{-\pi u^2}$ up to normalization.
- **THM-PAPER-0144-5** (Fact 6.3, fact (Slepian-Pollak-Landau), scope: asymptotic; Sec. 6.3, p. 28). Eigenvalues $\nu_n(\lambda)$ of $P_\lambda\hat P_\lambda P_\lambda$ on $L^2([-\lambda,\lambda])^{ev}$ are simple, $1>\nu_0>\nu_1>\dots>0$, eigenfunctions the even prolate spheroidal functions $h_{2n,\lambda}$ of the prolate operator $PW_\lambda=-\partial_x(\lambda^2-x^2)\partial_x+(2\pi\lambda x)^2$; $1-\chi_0,1-\chi_2\to0$ exponentially in $x=\lambda^2$; $1-\chi_2\sim\frac{2^{14}}{3}\sqrt{2\pi}\,e^{-4\pi e^{L}+9L/2}$-type double-exponential decay in $L=2\log\lambda$ (cited from [47] Thm 1).
- **THM-PAPER-0144-6** (Fact 6.4, fact (cited/sketched), scope: asymptotic; Sec. 6.5, p. 29-30). The Fourier transform of $k_\lambda=E(h_\lambda)|_{[\lambda^{-1},\lambda]}$ (with $h_\lambda$ the combination of $h_{0,\lambda},h_{4,\lambda}$ with vanishing integral) converges as $\lambda\to\infty$ to Riemann's $\Xi$ uniformly on closed substrips of the strip of width 1; on $\Im z=\alpha$, $\alpha\in(-1/2,1/2)$, the difference is $\le c\lambda^{-1/2-\alpha}(1-2\alpha)^{-1}$.
- **THM-PAPER-0144-7** (Theorem 7.1 (from [24]), theorem (cited), scope: local; Sec. 7.2, p. 31). Let $g\in C_c^\infty(\mathbb R_+^*)$ be supported in $[2^{-1/2},2^{1/2}]$ with Fourier transform vanishing at $i/2$ and $0$. Then $W_\infty(g*g^*)\ge \mathrm{Tr}(\vartheta(g)S\vartheta(g)^*)$, $S$ the projection on the Sonin space.
- **THM-PAPER-0144-8** (Theorem 7.3 ([28]), theorem (cited, conditional on RH), scope: asymptotic; Sec. 7.5, p. 32-33). Assuming RH, with $D$ self-adjoint with spectrum the ordinates of the zeros, as $t\to0$: $\mathrm{Tr}\exp(-tD^2)\sim\frac{2\log(1/t)}{4\sqrt\pi\sqrt t}-\frac{\log4\pi+\gamma/2}{\sqrt2\sqrt\pi\sqrt t}+2\exp(t/4)+\sum a_nt^{n/2}$, $a_0=-1/4$, with $a_{2k-1},a_{2k}$ given by Bernoulli and Euler numbers; the series is divergent (factorial growth). *Conditional on:* RH.
- **THM-PAPER-0144-9** (Theorem 7.2 and Sec. 7.6, theorem / results (cited), scope: asymptotic; Sec. 7.3 p. 31; Sec. 7.6 p. 33-34). The sheaf $\mathcal O\rtimes\mathbb G_m$ on Spec Z has sections $S(\mathbb A_S)\rtimes\mathbb Z_S^\times$ over $S^c$, generic stalk $S(\mathbb A_{\mathbb Q})\rtimes\mathbb Q^\times$, global sections $S(\mathbb R)\rtimes\{\pm1\}$. Prolate operator $PW_\lambda$ restricted to Sonin space has discrete negative spectrum $\nu_k$ with $2\sqrt{-\nu_k}$ (for $\lambda=\sqrt2$) matching the UV asymptotics of $\rho-1/2$ (Connes-Moscovici [27]).

### Key definitions

- E(f)(u)=u^{1/2} sum_{n>=1} f(nu)
- Weil quadratic form Q_W,lambda and operator A_lambda
- prolate operator PW_lambda
- Sonin space (functions vanishing with their Fourier transform on [-lambda,lambda])
- theta_x(u)=eta_x(x^{1/2}u)

### Principal lemmas

- **THM-PAPER-0144-L1** (Weil positivity (Sec. 4.1) as used in Sec. 6.4; Sec. 4.1 (p. 20) and Sec. 6.4 (p. 28)). RH iff the Weil quadratic form Q_W is positive on test functions; restricted form Q_{W_lambda} on support [1/lambda,lambda] has smallest eigenvalue epsilon(lambda)>0 under RH, tending to 0 exponentially in mu=lambda^2 (numerics of [25]). — *Role:* framing of the minimization
- **THM-PAPER-0144-L2** (Poisson relation (18); Sec. 6.4, p. 29). $E(\hat f)(x)=E(f)(x^{-1})$ for $f\in S_0^{ev}$ (f(0)=\hat f(0)=0); hence E(f) with f supported in [-lambda,lambda] and \hat f supported there too would lie in the radical of Q_{W_lambda}; obstruction is $P_\lambda\cap\hat P_\lambda=\{0\}$ but the projections nearly intersect. — *Role:* conceptual justification of the near-radical ansatz k_lambda
- **THM-PAPER-0144-L3** (Equation (19); Sec. 7.1, p. 30-32). $W_\infty(f)=\log(TW)f(1)+\mathrm{Trace}(\vartheta(f)(1-P_T-\hat P_W))$ (archimedean trace formula), extended by (22) to include primes in S. — *Role:* bridge between explicit formulas and time/band limiting

### Proof architecture

Not a proof of RH. Chain: Weil positivity <=> RH (Sec. 4.1) -> restrict to finitely many primes (support [1/lambda,lambda]) -> minimizer eta_x exists (Hilbert Dirichlet-principle style) -> Thm 6.1 (zeros of Fourier/Mellin transform real) given simple even minimum -> numerics (primes <=13) -> missing steps: simplicity of bottom eigenvalue, convergence eta_x to E(h) (comparison with prolate-based ansatz k_lambda, Facts 6.3-6.4), then Hurwitz gives RH. Geometric Sec. 7 (semilocal trace formula, Sonin space positivity) is background support, not part of the logical chain.

Dependency edges: Letter conclusion (RH) → Theorem 6.1 (uses); Letter conclusion (RH) → convergence of eta_x (unproved) (requires); Fact 6.4 → Facts 6.2, 6.3 (derives from); Theorem 6.1 → Hurwitz theorem (imports); Sec 6.4 ansatz → Weil positivity criterion (framed by)

**Imported results.** Weil positivity criterion (Weil 1952); Slepian-Pollak-Landau prolate theory; Connes-van Suijlekom quadratic forms and real zeros [32]; Connes-Consani-Moscovici/Connes-Moscovici results [24],[25],[27],[28],[30]; Hurwitz theorem; Caratheodory-Fejer on Toeplitz matrices (footnote 12); Hilbert Dirichlet principle

**Techniques.** Weil quadratic form / explicit formula; Hilbert-style variational minimization; Toeplitz/Caratheodory-Fejer type argument for real zeros; prolate spheroidal wave functions and Slepian-Pollak commutation; Hurwitz theorem on limits of zero-free sets; semilocal adele class space and trace formula; heat expansion of zeta-zero operator

## Context and interpretation

**Importance and obstacle overcome.** Reframes RH as stability of real-rootedness under an increasing-primes limit: for every finite prime set the approximants have exactly real zeros (conditional on simplicity), so only a limiting statement remains. Strong numerical evidence (55 digits at the first zero with 6 primes).

**Relation to prior work.** Builds on Connes-Consani-Moscovici (Weil positivity, prolate functions, Sonin space) and Connes-van Suijlekom; surveys classical (Hardy, Selberg, Levinson-type), Voronin, random matrix and equivalent-criteria literature.

**Limitations and open questions.** Convergence of the finite-prime minimizers to the zeta zeros is explicitly not proved (p. 25). Simplicity and evenness of the lowest eigenvalue of Q_W,lambda is not proved (Sec. 6.6, footnote 12). Fact 6.4 is for k_lambda, not for the true minimizer theta_x; closeness k_lambda vs theta_x is still missing. Thm 6.1's finite-support zeros give no information on the limit unless uniform convergence on compacts is established.

## Research potential

- **Hypotheses that might be weakened.** Prove simplicity and evenness of the lowest eigenvalue of Q_W,lambda for small lambda (finite checks with rigorous interval arithmetic); weaken Thm 6.1's 'isolated' to a spectral gap statement for finite truncations.
- **Generalizations.** Replace Q by the Weil form for Dirichlet L(s,chi) or GL(2) L-functions and test the same primes-<=x approximation; test with prime sets not initial segments to see whether the approximation quality depends on contiguous primes.
- **Candidate connections.** Prolate operator Sonin-space spectrum (Connes-Moscovici) and Weil positivity; relation to Burnol's work and to Li coefficients; compare with fixed-prime-set vs growing-prime control issue: current numerics show a fixed finite P still approximates low zeros, but a theorem for growing P is exactly the missing step.
- **Reusable lemmas.** Thm 6.1 (real zeros of Fourier transform of bottom eigenfunction) is reusable for any lower-bounded translation-invariant-kernel quadratic form with simple even ground state.
- **Possible experiments.** Recompute the 50-zero table with certified (interval) arithmetic and varying truncation N to check whether the reported 'upper bounds' are rigorous; compute eigenvalue gap of the two lowest eigenvalues versus x to test simplicity; check how errors scale with x (differences go from 1e-55 to 1e-2 across the first 50 zeros).
- **Risks / barriers.** Hurwitz needs convergence to Xi of the actual minimizers, not of an ansatz; exponentially small eigenvalues epsilon(lambda) make numerical conditioning severe; positive-semidefiniteness (Weil positivity itself) is not used or proved; letter is heuristic.

## Audit notes (Level 1 reader)

Abstract says approximation accuracies range 'from 2.6e-55 to 1e-3', but the table on p. 25 ends with 0.0209081, 0.00313565, 0.00212727, so the stated range is inconsistent with the table (location: Abstract vs Sec. 5 table). Table entries are called 'upper bound of' differences without a stated rigorous-error method (N=100 trig truncation, footnote 14). 'Primes less than 13' vs support [1,13] including 13. Fact 6.4 is stated for the strip with Im z<1/2 but the error bound is given for alpha in (-1/2,1/2); only minor. Fact 6.4 and Fact 6.3 asymptotic are cited, not proved here.

*These notes are a reader's observations, not verified findings; see `audits/` for adjudicated findings.*

## Provenance

- Candidate `CAND-02653`; harvest queries: kw_RH_any, msc_11M06, arxiv_critical_line, arxiv_rh_abs, arxiv_rh_ti, arxiv_zeta_zeros2.
- Triage decision: include — Connes' commissioned 165-year survey of approaches to RH with new perspective.
- Record generated by `tools/make_records.py`; search cutoff 2026-11-17.
