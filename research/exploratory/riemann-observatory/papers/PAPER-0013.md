# PAPER-0013 — Random matrix theory and \(\zeta(1/2+it)\).

| Field | Value |
|---|---|
| Authors | Keating, Jonathan P.; Snaith, Nina C. |
| Year / stratum | 2000 / S4 |
| Venue | Commun. Math. Phys. 214, No. 1, 57-89 (2000). |
| Identifiers | zbMATH [1051.11048](https://zbmath.org/?q=an:1051.11048) · DOI [10.1007/s002200000261](https://doi.org/10.1007/s002200000261) |
| MSC | 11M50, 11M26, 15B52, 82B44 |
| Families | B |
| Work type | original_paper |
| Evidence level of this record | **L1** |
| Full text | fulltext_read — https://people.maths.bris.ac.uk/~mancs/papers/RMTzeta.pdf |
| Selection | score 4.6124, in-pool citations 185, seed lists 3, triage relevance 5 |

## Mathematical content (Level 1: full text read)

**Research question.** For Z(U,\theta)=\det(I-Ue^{-i\theta}) with U Haar-distributed in U(N), compute exactly the moments of |Z| and Z/Z^*, derive value distributions/cumulants of Re log Z and Im log Z, and use the identification N=\log(T/2\pi) (matching mean densities) to compare with Selberg's theorem, Odlyzko's data near the 10^{20}th zero, and to conjecture the leading constant in the 2k-th continuous moment of |\zeta(1/2+it)|, namely f(\lambda)=G^2(1+\lambda)/G(1+2\lambda) times the arithmetic factor a(\lambda).

**Historical motivation.** Montgomery-Odlyzko law links short-range zero statistics to GUE/CUE; the authors ask whether values (not only zero spacings) of zeta match CUE characteristic polynomials, and whether the long-standing, unknown leading constants f(lambda) in the moments of zeta have a random-matrix origin. Results announced at ESI (Sept 1998) and MSRI (June 1999); Conrey-Gonek independently conjectured f(4).

### Main results

- **THM-PAPER-0013-1** (Intro (i), eq. (6), theorem (exact CUE identity; proof via Selberg integral), scope: finite; Sect. 1 (i), eq. (6); proof Sect. 2.1, eqs. (20)-(26)). For \mathrm{Re}\,s>-1, \quad M_N(s)=\langle |Z(U,\theta)|^s\rangle_{U(N)}=\prod_{j=1}^N \frac{\Gamma(j)\Gamma(j+s)}{(\Gamma(j+s/2))^2}, independent of \theta; for integer k\ge0, M_N(2k) is a polynomial in N of degree k^2.
- **THM-PAPER-0013-2** (Intro (ii), eq. (7), theorem, scope: finite; Sect. 1 (ii), eq. (7); Sect. 2.1). For s\in\mathbb C, \quad L_N(s)=\Big\langle \big(Z/Z^*\big)^{s/2}\Big\rangle_{U(N)}=\prod_{j=1}^N\frac{\Gamma(j)^2}{\Gamma(j+s/2)\Gamma(j-s/2)}, with the branch of arg Z fixed by continuous variation along \theta-i\epsilon, \epsilon\to\infty-type normalization (Im log Z has jump \pi at eigenphases); \theta not an eigenphase.
- **THM-PAPER-0013-3** (Intro (iii), theorem (CLT, new proof; Im part earlier due to Costin-Lebowitz), scope: asymptotic; Sect. 1 (iii); proof Sects. 2.2-2.4). As N\to\infty, \mathrm{Re}\log Z/\sqrt{\tfrac12\log N} and \mathrm{Im}\log Z/\sqrt{\tfrac12\log N} converge in distribution, jointly and independently, to standard Gaussians. Under the identification N=\log(T/2\pi) (eq. (8)) this is the exact analogue of Selberg's theorem (eq. (3)) for \log\zeta(1/2+it)/\sqrt{\tfrac12\log\log T}.
- **THM-PAPER-0013-4** (Intro (iv), eqs. (9)-(14), theorem (exact cumulants and asymptotics), scope: asymptotic; Sect. 1 (iv); Sects. 2.2-2.3). Cumulants of Re log Z: Q_n(N)=\frac{2^{n-1}-1}{2^{n-1}}\sum_{j=1}^N\psi^{(n-1)}(j). Cumulants of Im log Z: R_n(N)=\frac{(-1)^{1+n/2}}{2^{n-1}}\sum_{j=1}^N\psi^{(n-1)}(j) for n even, 0 for n odd. In particular Q_1=R_1=0, Q_2(N)=R_2(N)=\tfrac12\log N+\tfrac12(\gamma+1)+\tfrac1{24N^2}+O(N^{-4}); Q_n(N)=(-1)^n\frac{2^{n-1}-1}{2^{n-1}}\zeta(n-1)\Gamma(n)+O(N^{2-n}) for n\ge3; R_{2k}(N)=\frac{(-1)^{k+1}}{2^{2k-1}}\zeta(2k-1)\Gamma(2k)+O(N^{2-2k}), k>1 (so higher even cumulants of Im log Z tend to constants, proving a Costin-Lebowitz conjecture).
- **THM-PAPER-0013-5** (Intro (v), eqs. (15)-(17), theorem (leading moment asymptotics), scope: asymptotic; Sect. 1 (v) eqs. (15)-(17); Sect. 2.5 eqs. (80)-(83)). f_{CUE}(\lambda):=\lim_{N\to\infty}N^{-\lambda^2}\langle|Z|^{2\lambda}\rangle=\frac{G^2(1+\lambda)}{G(1+2\lambda)} (Barnes G; for \mathrm{Re}\,\lambda>-1/2); for integer k\ge1, f_{CUE}(k)=\prod_{j=0}^{k-1}\frac{j!}{(j+k)!}, giving 1, 1/12, 42/9!, 24024/16! for k=1..4. Also \lim N^{\lambda^2}L_N(2\lambda)=G(1-\lambda)G(1+\lambda).
- **THM-PAPER-0013-6** (Conjecture (19)/(93)-(94), conjecture (Keating-Snaith moment conjecture), scope: asymptotic; Sect. 1 eq. (19); Sect. 3 eqs. (93)-(94), (97)). Assuming the limit in (4) exists, f(\lambda):=\lim_{T\to\infty}\frac{1}{(\log T)^{\lambda^2}}\frac1T\int_0^T|\zeta(1/2+it)|^{2\lambda}dt\Big/a(\lambda) equals f_{CUE}(\lambda)=G^2(1+\lambda)/G(1+2\lambda), i.e. \frac1T\int_0^T|\zeta(\tfrac12+it)|^{2\lambda}dt\sim a(\lambda)\frac{G^2(1+\lambda)}{G(1+2\lambda)}(\log T)^{\lambda^2}, with a(\lambda)=\prod_p(1-1/p)^{\lambda^2}\sum_{m\ge0}\big(\frac{\Gamma(\lambda+m)}{m!\Gamma(\lambda)}\big)^2p^{-m}. Equivalent to f(n)=\prod_{j=0}^{n-1}j!/(j+n)!. *Conditional on:* Existence of the limit (4), heuristic factorization of moments into a CUE factor and a prime-product factor.
- **THM-PAPER-0013-7** (Sect. 4, eqs. (109)-(113), theorem (COE/CSE extension), scope: asymptotic; Sect. 4). For \beta\in\{1,2,4\}, \langle|Z|^s\rangle_{\beta,N}=\prod_{j=0}^{N-1}\frac{\Gamma(1+j\beta/2)\Gamma(1+s+j\beta/2)}{\Gamma(1+s/2+j\beta/2)^2}; cumulants Q^\beta_n(N)=\frac{2^{n-1}-1}{2^{n-1}}\sum_{j=0}^{N-1}\psi^{(n-1)}(1+j\beta/2); Q^\beta_2(N)=\frac1\beta\log N+O(1).
- **THM-PAPER-0013-8** (Eq. (3) (Selberg) and (18) (Goldston), imported theorem (comparison data), scope: asymptotic; Sect. 1 eqs. (3), (18)). Selberg: for any rectangle E, T^{-1}\mathrm{meas}\{t\in[T,2T]:\log\zeta(1/2+it)/\sqrt{\tfrac12\log\log T}\in E\}\to\frac1{2\pi}\int_E e^{-(x^2+y^2)/2}dxdy. Goldston (under RH and Montgomery's pair-correlation conjecture): \frac1T\int_0^T(\mathrm{Im}\log\zeta)^2=\tfrac12\log\log\frac T{2\pi}+\tfrac12(\gamma+1)+\sum_p\sum_{m\ge2}\frac{(1-m)\cdot}{m^2p^m}\ldots+o(1) (exact prime sum as in eq. (18)).

### Principal lemmas

- **THM-PAPER-0013-L1** (Selberg integral (22)-(23); Sect. 2.1, eqs. (22)-(26)). J(a,b,\alpha,\beta,\gamma,N)=\int_{\mathbb R^N}\prod_{j<m}|x_j-x_m|^{2\gamma}\prod_j(a+ix_j)^{-\alpha}(b-ix_j)^{-\beta}dx_j=\frac{(2\pi)^N}{(a+b)^{(\alpha+\beta)N-\gamma N(N-1)-N}}\prod_{j=0}^{N-1}\frac{\Gamma(1+\gamma+j\gamma)\Gamma(\alpha+\beta-(N+j-1)\gamma-1)}{\Gamma(1+\gamma)\Gamma(\alpha-j\gamma)\Gamma(\beta-j\gamma)}, valid under Re a,b,\alpha,\beta>0, Re(\alpha+\beta)>1, -1/N<Re\gamma<\min(\mathrm{Re}\alpha/(N-1),\mathrm{Re}\beta/(N-1),\mathrm{Re}(\alpha+\beta-1)/(2(N-1))). — *Role:* Imported (Mehta, Ch. 17). Evaluates the CUE average after the Cayley-type change x_n=\cot\theta_n, giving M_N(s)=2^{N+sN}(N!(2\pi)^N)^{-1}J(1,1,N+s/2,N+s/2,1,N).
- **THM-PAPER-0013-L2** (eq. (21)-(25); Sect. 2.1). By Haar invariance the average is independent of \theta; set \theta=0, write |e^{i\theta_j}-e^{i\theta_m}|^2=4\sin^2((\theta_j-\theta_m)/2), use \sin(\theta_j-\theta_m)=\sin\theta_j\cos\theta_m-\cos\theta_j\sin\theta_m to reach \prod|\cot\theta_m-\cot\theta_j|^2\prod\sin^{2(N-1)}\ldots, then x_n=\cot\theta_n. — *Role:* Reduction of the CUE moment to a Cauchy-type Selberg integral.
- **THM-PAPER-0013-L3** (eq. (80)-(82); Sect. 2.5). Barnes G: G(1+z)=(2\pi)^{z/2}e^{-[(1+\gamma)z^2+z]/2}\prod_{n\ge1}(1+z/n)^ne^{-z+z^2/(2n)}, G(z+1)=\Gamma(z)G(z), \log G(1+z)=\frac z2(\log2\pi-1)-(1+\gamma)\frac{z^2}2+\sum_{n\ge3}(-1)^{n-1}\zeta(n-1)\frac{z^n}n for |z|<1. — *Role:* Tool for passing from the Gamma-product (6) to the N\to\infty asymptotics (15) and (17); also for the cumulant expansions.
- **THM-PAPER-0013-L4** (Sect. 2.4; Sect. 2.4 (line ~909 of extracted text)). Independence of Re log Z and Im log Z: the joint generating function \langle|Z|^{s}e^{it\,\mathrm{Im}\log Z}\rangle factorizes in the large-N limit (as products of Gamma functions), implying asymptotic independence of the two parts. — *Role:* Gives joint Gaussian limit in (iii). Statement paraphrased from the section heading and introduction; proof body only skimmed.
- **THM-PAPER-0013-L5** (eq. (92); Sect. 1 eq. (8); Sect. 3 eq. (92)). N=\log(T/2\pi) (matrix size matched to the mean zero density at height T). — *Role:* Dictionary between CUE and zeta; used for Selberg comparison, Odlyzko data (N\approx 42 near the 10^{20}th zero) and the moment conjecture. Heuristic, not a theorem.

### Proof architecture

Everything in Sect. 2 flows from the two product formulas (6),(7). Derivation of (6): Weyl density for eigenphases, rewrite |Z|^s with sin factors, set \theta=0, substitute x=\cot\theta, evaluate by Selberg's integral (22). (7) analogously with complex exponents. Then Re log Z / Im log Z value distributions are read off by Fourier inversion of s\mapsto M_N(s), L_N(s); cumulants come from log-derivatives, i.e. polygamma sums (9)-(10); asymptotics via Euler-Maclaurin/Barnes G (Sect. 2.5). Sect. 3 compares with zeta: Selberg's theorem (imported), Odlyzko's numerics at t_{10^{20}} (imported data), Goldston's variance formula (imported, conditional on RH + pair correlation); long-range prime contribution modelled by a convergent Euler product a(\lambda) obtained heuristically via the Gonek/Bogomolny-Keating style truncated Euler product with independent primes; conjecture (93) is the product of the CUE factor and a(\lambda). Sect. 4 repeats with Dyson index \beta.

**Imported results.** Selberg's integral formula (Mehta, Random Matrices, Ch. 17); Selberg CLT for log zeta(1/2+it) (Selberg; Titchmarsh/Ivic); Costin-Lebowitz Gaussian limit for Im log Z (PRL 75 (1995)); Goldston, On the function S(T), J. Number Theory 27 (1987), under RH and Montgomery pair correlation; Hardy-Littlewood f(1)=1; Ingham f(2)=1/12; Conrey-Ghosh f(3)=42/9! and Conrey-Gonek f(4)=24024/16! (conjectural); Odlyzko numerical data near the 10^{20}th zero; Montgomery pair correlation / Rudnick-Sarnak n-level correlations

**Techniques.** Selberg/Cauchy-type integral via x=cot(theta); Barnes G-function asymptotics; polygamma cumulant expansion; Fourier inversion of generating functions for value distributions; matching of mean densities N = log(T/2pi); heuristic Euler-product factorization; comparison with Odlyzko numerics

## Context and interpretation

**Importance and obstacle overcome.** Provides the first uniform prediction for all real lambda (not just integer) of the leading coefficient of the 2k-th moment, reproducing the known k=1,2 and the conjectured k=3,4 values, and explains why Odlyzko's finite-height data deviate from Gaussian. Obstacle: needing an exact evaluation of CUE moments for all N (done via Selberg's integral) and a principled way to attach the arithmetic factor (done heuristically, so the conjecture is not derived).

**Relation to prior work.** 

**Limitations and open questions.** The zeta conjecture (19)/(93) is unproved for every k>=3 (and for non-integer k except in ranges of Heath-Brown/others); the arithmetic factor a(\lambda) is inserted heuristically and RMT does not 'see' it; the identification N=log(T/2pi) predicts only leading order, and lower-order terms (later settled by the Conrey-Farmer-Keating-Rubinstein-Snaith recipe and the hybrid Euler-Hadamard model) are not captured. Value-distribution comparison is numerical at a single height. Leading-order only; no statement about maxima of |zeta| or large deviations.

## Research potential

- **Hypotheses that might be weakened.** Conjecture (19) presupposes existence of the limit in (4); the log-moment version (97) requires only RH-type input for k small. One could ask for the largest lambda with a rigorous upper bound matching f_{CUE}(lambda) a(lambda) (Harper, Soundararajan upper bounds under RH are off by epsilon in exponent); the Gaussian-CLT analogue is sharp for Selberg. RH is not needed for the CUE side at all.
- **Generalizations.** Eq. (110)-(113) already give O and Sp (Dyson index beta); extensions to L-functions families are in CAND-00723; lower-order terms and ratios; shifts (CFKRS); derivative moments (CAND-00749); moments of Z/Z^* give the analogue for zeta ratios / S(T) moments; discrete moments over zeros.
- **Candidate connections.** Hybrid Euler-Hadamard factorization (Gonek-Hughes-Keating) rederives a(lambda) G^2/G; relation to Fyodorov-Hiary-Keating freezing/maxima of |Z| and log-correlated fields; large-deviation and negative-moment conjectures (Re lambda > -1/2 threshold coincides with zeros of zeta at the critical line making negative moments diverge at lambda=-1/2); Selberg-integral and Barnes-G structure suggests Painleve/Toeplitz determinant routes (Fisher-Hartwig).
- **Reusable lemmas.** Formula (6) with the Selberg integral reduction (eqs. 20-26) is a clean, citable closed form for E|det(I-U)|^s; eq. (7) for E[(Z/Z^*)^{s/2}]; cumulant formulas (9)-(10); eq. (15) f_CUE(lambda)=G^2(1+lambda)/G(1+2 lambda).
- **Possible experiments.** Recompute the finite-N polynomial coefficients of M_N(2k) for k up to 10 and compare with moments of zeta computed with rigorous interval arithmetic at heights beyond Odlyzko's (e.g. T near 10^{28}); test the finite-T correction N_eff = log(T/2pi) versus the shifted effective N from CFKRS; measure the deviation of the Im log zeta fourth cumulant from the constant predicted by (14) as a function of T.
- **Risks / barriers.** Even the case k=3 appears out of reach unconditionally; the RMT model cannot by itself decide RH or give arithmetic input; the finite-height convergence in log T/ log log T scales is slow so numerical evidence cannot discriminate lower-order theories without careful extrapolation.

## Audit notes (Level 1 reader)

none noticed in inspected portion. Minor: the extracted text of Goldston's formula (18) is garbled by pdftotext, so the exact prime-sum summand was not recorded verbatim; Sect. 2.2-2.4 proofs and Sect. 3 tables were only skimmed.

*These notes are a reader's observations, not verified findings; see `audits/` for adjudicated findings.*

## Provenance

- Candidate `CAND-00719`; harvest queries: kw_RH_any, msc_11M26, msc_11M50.
- Triage decision: include — Landmark KS conjecture for zeta moments from RMT.
- Record generated by `tools/make_records.py`; search cutoff 2026-11-17.
