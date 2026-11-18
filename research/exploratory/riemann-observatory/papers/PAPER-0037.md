# PAPER-0037 — Explicit zero density for the Riemann zeta function

| Field | Value |
|---|---|
| Authors | Kadiri, Habiba; Lumley, Allysa; Ng, Nathan |
| Year / stratum | 2018 / S6 |
| Venue | J. Math. Anal. Appl. 465, No. 1, 22-46 (2018). |
| Identifiers | zbMATH [1446.11158](https://zbmath.org/?q=an:1446.11158) · DOI [10.1016/j.jmaa.2018.04.071](https://doi.org/10.1016/j.jmaa.2018.04.071) · arXiv [2101.12263](https://arxiv.org/abs/2101.12263) |
| MSC | 11M06 |
| Families | A |
| Work type | original_paper |
| Evidence level of this record | **L1** |
| Full text | fulltext_read — https://arxiv.org/abs/2101.12263 |
| Selection | score 4.583, in-pool citations 19, seed lists 2, triage relevance 4 |

## Mathematical content (Level 1: full text read)

**Research question.** Give explicit bounds for the zero-density function N(sigma,T) (zeros with Re>sigma, 0<Im<T) of Ingham type T^{8(1-sigma)/3}(log T)^5, generalizing Ramare's explicit version (improving it numerically) by Ingham's argument with a general weight, using Littlewood's lemma, a mollifier M_X(s)=sum_{n<=X}mu(n)n^{-s}, an explicit van der Corput bound for zeta, and explicit control of arg of a holomorphic function.

**Historical motivation.** Bohr-Landau (1913) N(sigma,T)=O(T/(sigma-1/2)); Ingham (1937) N(sigma,T)=O(T^{(2+4c)(1-sigma)}(log T)^5) given zeta(1/2+it)=O(t^{c+eps}); few explicit versions exist: Kadiri (2013) explicit Bohr-Landau, and Ramare's unpublished then published (2016) explicit Ingham result. Applications: explicit prime counting errors, primes in short intervals.

### Main results

- **THM-PAPER-0037-1** (Theorem 1.1, theorem, scope: finite; Section 1, p.2; proof via Lemma 4.14, (4.70)-(4.73)). Let $\frac{10^9}{H_0}\le k\le1$ (displayed as 109/H_0 in text), $d>0$, $H\in[1002,H_0)$, $\alpha>0$, $\delta\ge1$ (see Lemma 4.14: $\delta>0$), $\eta_0=0.23622\ldots$, $1+\eta_0\le\mu\le1+\eta$, $\eta\in(\eta_0,\tfrac12)$ fixed, $\sigma>\tfrac12+\tfrac d{\log H_0}$, with $H_0=3.0610046\cdot10^{10}$ (Platt: RH verified for |Im rho|<=H_0). Then there exist $C_1,C_2>0$ (defined in (4.72),(4.73)) such that for all $T\ge H_0$: $N(\sigma,T)\le\frac{(T-H)\log T}{2\pi d}\log\Big(1+\frac{C_1(\log kT)^{2\sigma}(\log T)^{4(1-\sigma)}T^{\frac83(1-\sigma)}}{T-H}\Big)+\frac{C_2}{2\pi d}(\log T)^2$ (1.6), hence (1.7): $N(\sigma,T)\le\frac{C_1}{2\pi d}(\log kT)^{2\sigma}(\log T)^{5-4\sigma}T^{\frac83(1-\sigma)}+\frac{C_2}{2\pi d}(\log T)^2$. *Conditional on:* Uses unconditional verification of RH up to height H_0 (Platt) only to subtract N(sigma,H); no RH assumed for the bound.
- **THM-PAPER-0037-2** (Examples after Theorem 1.1 / Table 1, numerical, scope: computational; Section 1 and Section 5, Tables 1-2). For example $N(0.90,T)<11.499(\log T)^{16/5}T^{4/15}+3.186(\log T)^2$ (for T>=H_0), and $N(0.90,H_0)<130.07$ from (1.6). Table 1 lists A=C_1/(2 pi d), B=C_2/(2 pi d) in $N(\sigma,T)\le A(\log kT)^{2\sigma}(\log T)^{5-4\sigma}T^{\frac83(1-\sigma)}+B(\log T)^2$ for sigma in {0.60,0.65,...,0.99}; Table 2 lists bounds for N(sigma,H_0) for sigma 0.60-0.99 (e.g. 520.28 at sigma=0.60; 130.07 at 0.90; 106.18 at 0.99).
- **THM-PAPER-0037-3** (Comparison with Ramare (1.5), imported result, scope: asymptotic; Section 1, eq. (1.5) and footnote 1). Ramare [24]: for sigma>=0.52 fixed and T>=2000, $N(\sigma,T)\le965(3T)^{8(1-\sigma)/3}(\log T)^{5-2\sigma}+51.5(\log T)^2$; gives $N(0.90,H_0)<2.1529\cdot10^{10}$. (Footnote 1: the originally published constant 4.9 was wrong; a corrected proof was sent by Ramare.)
- **THM-PAPER-0037-4** (Proposition 4.10, proposition, scope: finite; Section 4, (4.30)-(4.32)). Let $\eta>0$, f holomorphic for Re s>=-eta, real for real s, with $|f(s)|\le M$ for Re s>=1+eta and $|\Re f(1+\eta+it)|\ge m>0$ for all t. For $\sigma\in(0,1+\eta]$ and U not an ordinate of a zero of f, there is an increasing sequence of naturals N_k with $|\arg f(\sigma+iU)|\le\frac\pi{L_k}\ldots+\frac\pi{\log\ldots}$ (precise bound (4.32) not transcribed); sharper version of a lemma of Titchmarsh p.213; Corollary 4.11 specializes with eta_0=0.23622..., X>=10^9.

### Key definitions

- N(sigma,T)=#{rho=beta+i gamma: zeta(rho)=0, 0<gamma<T, sigma<beta<1}
- RH(H_0): all nontrivial zeros with |Im|<=H_0 have real part 1/2
- M_X(s)=sum_{n<=X}mu(n)n^{-s}, f_X=zeta M_X-1, h_X=1-f_X^2
- Weight g(s)=((s-1)/s)exp(alpha(s/T)^2)
- M_{g,T}(X,sigma)=int|g(sigma+it)|^2|f_X(sigma+it)|^2dt
- eta_0=0.23622...

### Principal lemmas

- **THM-PAPER-0037-L1** (Lemma 3.1 (Rademacher); Section 3.1). For $-\tfrac12\le-\eta\le\sigma\le1+\eta\le\tfrac32$: $|\zeta(s)|\le3\left|\frac{1+s}{1-s}\right|\left(\frac{|1+s|}{2\pi}\right)^{\frac12(1-\sigma+\eta)}\zeta(1+\eta)$. — *Role:* Explicit convexity bound (imported)
- **THM-PAPER-0037-L2** (Lemma 3.2 (Hiary); Section 3.1). $|\zeta(\tfrac12+it)|\le0.63\,t^{1/6}\log t$ for t>=3 and $\max_{|t|\le T}|\zeta(\tfrac12+it)|\le0.63T^{1/6}\log T+2.851$. — *Role:* Explicit van der Corput subconvexity for zeta (imported, Hiary Indag. Math. 2016)
- **THM-PAPER-0037-L3** (Lemma 3.6 (Montgomery-Vaughan type); Section 3, eq. before Lemma 3.7). Explicit mean value theorem for Dirichlet polynomials with real sequence (u_n): bound for $\int_0^T|\sum u_nn^{-it}|^2dt$ with explicit constants (Preissmann version). — *Role:* Bounds M_{g,T}(X,sigma_2) and the mollified second moment
- **THM-PAPER-0037-L4** (Lemma 4.1; Section 4.1.1). For T>0, X>=kH_0: $\int_0^T|M_X(\tfrac12+it)|^2dt\le(C_1T+C_2X)\log X$ (explicit constants from Ramare's bounds, Lemmas 3.3-3.4). — *Role:* Second moment of mollifier on the critical line
- **THM-PAPER-0037-L5** (Lemma 3.7; Sections 2.3 and 3). Weight $g(s)=\frac{s-1}{s}e^{\alpha(s/T)^2}$ satisfies (2.12) with beta=2, explicit omega_1,omega_2 giving upper bound $|g(\sigma+it)|\le\omega_1e^{-\alpha(t/T)^2}$ and lower bound $\omega_2\le|g|$ on [H,T]. — *Role:* New weight function giving better constants than Ingham's cos-weight (beta=1) and Ramare's s(cos(s/2T))^{1/2}
- **THM-PAPER-0037-L6** (Lemmas 4.5-4.9; Section 4). Explicit bounds for $M_{g,T}(X,\sigma)$ at sigma=1/2 and sigma_2 slightly above 1, combining Lemmas 3.2-3.6 with the weights, and the convexity estimate (2.17) $M(X,\sigma)\le M(X,\tfrac12)^{\frac{\sigma_2-\sigma}{\sigma_2-1/2}}M(X,\sigma_2)^{\frac{\sigma-1/2}{\sigma_2-1/2}}$ (Hardy-Ingham-Polya). — *Role:* Core Ingham smoothing and interpolation
- **THM-PAPER-0037-L7** (Lemma 4.14; Section 4, p.19-20). With $\alpha,d,\delta>0$, $\eta_0=0.23622\ldots$, $\eta\in[\eta_0,\tfrac12)$, $\mu\in[1+\eta_0,1+\eta]$, $H_0=3.0610046\cdot10^{10}$, $1002\le H\le H_0$, $\frac{10^9}{H_0}\le k\le1$, $T\ge H_0$, $X=kT$, $\sigma>\tfrac12+\tfrac d{\log H_0}$, $U(\alpha,k,H_0)>1$ and $U(\alpha,k,T)$ decreasing in T: (4.70)/(4.71) hold with C_1,C_2 as in (4.72),(4.73). — *Role:* Technical form of Theorem 1.1 with all parameter constraints

### Proof architecture

Littlewood's lemma applied to h(s)=zeta(s)M_X(s)(2-zeta(s)M_X(s))=1-f_X(s)^2 with f_X=zeta M_X-1 (mollifier M_X=sum_{n<=X}mu(n)n^{-s}); N(sigma,T)-N(sigma,H)<=N_h(sigma,T)-N_h(sigma,H) since RH holds to height H_0. Averaging over tau in [sigma',mu] gives (2.3): integral of log|h(sigma'+it)| over [H,T], two arg integrals on horizontal sides, and log|h(mu+it)| on the right. Jensen/concavity of log gives $\int_H^T\log|h|\le(T-H)\log(1+\frac1{T-H}\int_H^T|f_X|^2)$. Then the second mollified moment F_X(sigma,T)=int_0^T|f_X(sigma+it)|^2dt is bounded via Ingham's smoothing with the new weight g (Lemma 3.7), reducing to M_{g,T}(X,sigma); the Hardy-Ingham-Polya convexity (2.17) interpolates between sigma=1/2 (bounded using explicit Hiary subconvexity, Lemma 3.2, mollifier second moment, Lemma 4.1, and Montgomery-Vaughan Lemma 3.6) and sigma_2>1 (Dirichlet series). The argument terms are controlled by a new explicit version of Titchmarsh's arg lemma (Proposition 4.10, Corollary 4.11, Lemma 4.12). Optimization of parameters (alpha,delta,k,d,mu,eta,H) gives Tables 1-2. Imported: Rademacher convexity, Hiary's explicit van der Corput, Ramare's explicit bounds for sums of mu, Montgomery-Vaughan/Preissmann inequality, Platt's RH verification to H_0.

**Imported results.** Rademacher explicit convexity bound for zeta (Math. Z. 1959, Thm 4); Hiary explicit van der Corput bound |zeta(1/2+it)|<=0.63 t^{1/6} log t (Indag. Math. 2016); Ramare explicit estimates for mollifier moments and sums involving mu (Math. Comp. 2016); Montgomery-Vaughan / Preissmann mean value theorem for Dirichlet polynomials; Hardy-Ingham-Polya convexity theorem for mean values; Titchmarsh's lemma on arg of holomorphic functions (improved here); Platt: RH verified up to H_0=3.0610046e10 (N(H_0)=103,800,788,359 zeros); Littlewood's lemma

**Techniques.** Littlewood's lemma on zeros in a rectangle; Bohr-Landau mollifier M_X and h=1-f_X^2 trick; Ingham's smoothing with a Gaussian-type weight g(s)=((s-1)/s)exp(alpha(s/T)^2); Hardy-Ingham-Polya convexity of mean values; Explicit Montgomery-Vaughan mean value theorem (Preissmann); Explicit van der Corput bound for zeta (Hiary); Explicit bound for arg of a holomorphic function (improvement of Titchmarsh p.213); Numerical optimization over a high-dimensional parameter space with Eudoxus machine

## Context and interpretation

**Importance and obstacle overcome.** Provides fully explicit zero-density estimates N(sigma,T) of Ingham type with improved constants over Ramare (e.g. N(0.90,H_0)<130.07 vs 2.15e10 and 11.499(log T)^{16/5}T^{4/15} vs 1293.48(log T)^{16/5}T^{4/15}) and over Kadiri's earlier explicit Bohr-Landau-type bound. Explicit zero density estimates are inputs to explicit prime-counting error terms and primes in short intervals. The obstacle was the loss in Ramare's weight and in the argument bounds; solved by the Gaussian weight and the new explicit arg lemma.

**Relation to prior work.** Generalizes Ingham 1937 and Ramare (Math. Comp. 2016, D.E.A. memoir) by using a general weight and improves the explicit constants (and Kadiri's 2013 explicit Bohr-Landau result); uses Kadiri-Ng's explicit arg lemma ideas for Dedekind zeta (Prop. 4.10 generalizes Titchmarsh/Kadiri-Ng).

**Limitations and open questions.** Bounds are only meaningful for T>=H_0 and each tuple of parameters only for a specific sigma; constants C_1 grow rapidly (Table 2: C_1~10^13 at sigma=0.90 for N(sigma,H_0)), so for T=H_0 the bound (1.6) beats the asymptotic shape only through the log(1+x) saving. Exponent 8/3 (Ingham with van der Corput c=1/6) is not improved: explicit use of Bourgain's 13/84 is not attempted. The best weight g is stated as an open problem (Section 2.3). Only upper bounds for N(sigma,T), no lower bound or relation to RH. The authors note numerical optimization chose k=1 for sigma>=0.75 and smaller k for sigma<=0.70.

## Research potential

- **Hypotheses that might be weakened.** Dependence on H_0 (Platt's verification) enters through the unconditional subtraction N(sigma,H) and conditions k>=10^9/H_0; a larger verified height would improve the finite-height constants. The restriction sigma>1/2+d/log H_0 is a technical condition on the mollifier parameter d; relaxing it would extend towards sigma near 1/2 (where Table values are poor).
- **Generalizations.** Replace Hiary's c=1/6 by an explicit version of Huxley's 32/205 or Bourgain's 13/84 to lower the exponent from 8/3 to 2(1+2c)=2(1+26/84)... (about 2.62) for large T; extend to Dirichlet L-functions and Dedekind zeta functions (cf. Kadiri-Ng); optimize the weight g (open problem).
- **Candidate connections.** Explicit primes in short intervals (Kadiri-Lumley), explicit PNT error terms via zero-free regions plus zero-density. Robin arithmetic: finite-range zero-density constants give explicit estimates for sums over zeros appearing in explicit formulas for psi(x); Mobius mollifier connects with signed native/Mobius cancellation programme (second moment of mollified zeta).
- **Reusable lemmas.** Proposition 4.10/Corollary 4.11 (explicit arg bound), Lemma 3.7 (weights satisfying (2.12)-(2.14)), Lemma 4.1 (explicit mollifier second moment), and Lemma 4.14 as a black box for N(sigma,T) with T>=H_0.
- **Possible experiments.** Recompute Tables 1-2 with independent parameter search (and rigorous interval arithmetic) to confirm A,B constants; test sensitivity to using a bigger k range; test Ramare's corrected (1.5) numerically; evaluate N(sigma,T) from actual zeros up to 10^6 to see how large the slack of the bounds is at sigma=0.90.
- **Risks / barriers.** Method fundamentally gives exponent 8/3 unless a better explicit subconvexity is used, and cannot approach the density hypothesis exponent 2 without Lindelof. Constants depend on many parameters and are not given in closed form (C_1,C_2 depend through (4.72)-(4.73), U, V, M(k,delta), C_7, C_8, b_12), making rigorous reproduction error-prone.

## Audit notes (Level 1 reader)

Introduction cites Bourgain's 13/84 as '[3] (2017)' but reference [3] in the bibliography is Bourgain's 2000 IMRN paper on large values estimates for Dirichlet polynomials and the density hypothesis, not the 2017 JAMS paper 'Decoupling, exponential sums and the Riemann zeta function' (CAND-01954); likely a bibliography mismatch (location: p.2 and reference list). The introduction also states that the exponent in (1.4) is T^{(2+4c)(1-sigma)}, so with c=1/6 one has 8/3, consistent with (1.7). The Theorem 1.1 hypothesis line in the extracted text is garbled ('9/10 H_0 <= k') and Lemma 4.14 reads 10^9/H_0<=k<=1; use Lemma 4.14 as authoritative. Footnote 1 records an error in Ramare's originally published constant (4.9 vs 965), so literature quoting (1.1) of Ramare should be treated with care. Otherwise none noticed in inspected portion.

*These notes are a reader's observations, not verified findings; see `audits/` for adjudicated findings.*

## Provenance

- Candidate `CAND-01804`; harvest queries: kw_zero_density, msc_11M06, arxiv_zero_density, arxiv_zeta_zeros.
- Triage decision: include — Explicit Ingham-type zero density estimate, key input for explicit results.
- Record generated by `tools/make_records.py`; search cutoff 2026-11-17.
