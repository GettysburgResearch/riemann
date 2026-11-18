# PAPER-0122 — A survey on the theory of universality for zeta and \(L\)-functions

| Field | Value |
|---|---|
| Authors | Matsumoto, Kohji |
| Year / stratum | 2015 / S5 |
| Venue | Kaneko, Masanobu (ed.) et al., Number theory. Plowing and starring through high wave forms. Proceedings of the 7th China-Japan Seminar, Fukuoka, Japan, October 28 -- November 1, 2013. Hackensack, NJ: World Scientific (ISBN 978-981-4644-92-1/hbk; 978-981-4644-94-5/ebook). Series on Number Theory and Its Applications 11, 95-144 (2015). |
| Identifiers | zbMATH [1381.11070](https://zbmath.org/?q=an:1381.11070) · DOI [10.1142/9789814644938_0004](https://doi.org/10.1142/9789814644938_0004) · arXiv [1407.4216](https://arxiv.org/abs/1407.4216) |
| MSC | 11M06, 11M35, 11-02 |
| Families | E, F |
| Work type | survey |
| Evidence level of this record | **L1** |
| Full text | fulltext_read — https://arxiv.org/abs/1407.4216 |
| Selection | score 4.0253, in-pool citations 45, seed lists 0, triage relevance 4 |

## Mathematical content (Level 1: full text read)

**Research question.** Survey (not a research paper) of 40 years of universality theory: for which zeta/L-functions phi and regions D(a,b) does every non-vanishing holomorphic target on a compact set K with connected complement get approximated by vertical shifts phi(s+i tau) on a set of tau of positive lower density, and what are the joint, strong, discrete, hybrid, quantitative and ergodic variants. RH enters through the strong-recurrence criterion (Bagchi) and the incompatibility of strong universality with zero-density estimates.

**Historical motivation.** Voronin 1975 extended Bohr-Courant denseness of zeta(sigma+i t) to a function-space statement; the survey organizes three stages (1975-87, 1996-2007, 2007-) and notes that universality shows how inaccessible critical-strip behavior is, suggesting a dynamical-systems reading of RH.

### Main results

- **THM-PAPER-0122-1** (Theorem 1 (Voronin), theorem (imported, classical), scope: asymptotic; Sec. 1, (1.2)). Let $K\subset D(1/2,1)=\{1/2<\sigma<1\}$ be compact with connected complement and $f\in H_0^c(K)$ (continuous on $K$, holomorphic in the interior, non-vanishing on $K$). Then for every $\varepsilon>0$, $\liminf_{T\to\infty}\frac1T\,\mathrm{meas}\{\tau\in[0,T]:\sup_{s\in K}|\zeta(s+i\tau)-f(s)|<\varepsilon\}>0$.
- **THM-PAPER-0122-2** (Theorem 4 (Nagoshi-Steuding), theorem (cited), scope: asymptotic; Sec. 3, (3.4)). Let $\varphi(s)=\sum a(n)n^{-s}$ lie in the Selberg class with degree $d_\varphi$, $\sigma_\varphi=\max\{1/2,1-d_\varphi^{-1}\}$, and suppose $\sum_{p\le x}|a(p)|^2=(\lambda+o(1))x/\log x$ for some $\lambda>0$. Then $\varphi$ is universal in $D(\sigma_\varphi,1)$.
- **THM-PAPER-0122-3** (Theorem 9 (Mishou), theorem (cited), scope: asymptotic; Sec. 4, Theorem 9). For normalized Hecke eigen cusp forms $g,g_1,g_2$: (i) $\zeta,L(s,g)$ jointly universal in $D(1/2,1)$; (ii) $L(s,g_1),L(s,g_2)$ jointly universal in $D(1/2,1)$ if $g_1\ne g_2$; (iii) $\zeta, L(s,\mathrm{sym}^2 g)$ in $D(2/3,1)$; (iv) $\zeta, L(s,g_1\otimes g_2)$ in $D(3/4,1)$ for $g_1\neq g_2$; (v) $L(s,g_1), L(s,g_1\otimes g_2)$ in $D(3/4,1)$.
- **THM-PAPER-0122-4** (Theorem 11, theorem (with proof via Rouche), scope: asymptotic; Sec. 5, (5.3); proof with f(s)=s-sigma_0 on a disc). If $\varphi$ is strongly universal in $D(a,b)$ (universality for all $f\in H^c(K)$, zeros allowed), then there is $C>0$ with $N(T;\sigma_1,\sigma_2;\varphi)\ge CT$ for all $a<\sigma_1<\sigma_2<b$.
- **THM-PAPER-0122-5** (Corollary 2, corollary, scope: asymptotic; Sec. 9). $\zeta$ is not strongly universal in $D(1/2,1)$, since $N(T;\sigma_1,\sigma_2;\zeta)=o(T)$ for $1/2<\sigma_1<\sigma_2<1$ (zero-density estimates).
- **THM-PAPER-0122-6** (Theorem 20 (Bagchi), theorem (cited), scope: asymptotic; Sec. 9, Theorem 20). RH for $\zeta$ holds iff for every compact $K\subset D(1/2,1)$ with connected complement and every $\varepsilon>0$, $\liminf_T \frac1T\mathrm{meas}\{\tau\in[0,T]:\sup_{s\in K}|\zeta(s+i\tau)-\zeta(s)|<\varepsilon\}>0$ (strong recurrence, (9.1)). Extended to Dirichlet L-functions (Bagchi) and Beurling zeta functions (R. Steuding).
- **THM-PAPER-0122-7** (Theorem 21 (Garunkstis, Nakamura, Pankowski), theorem (cited), scope: asymptotic; Sec. 9, Theorem 21, (9.3)-(9.4)). For $d$ irrational, or $d=a/b$ non-zero rational with $(a,b)=1$ and $|a-b|\ne1$: $\liminf_T\frac1T\mathrm{meas}\{\tau\le T:\sup_K|\zeta(s+i\tau)-\zeta(s+id\tau)|<\varepsilon\}>0$ (9.3). The log version (9.4) holds for every $d\ne0$; (9.3) at $d=0$ is the RH-equivalent (9.1), and (9.4) at $d=0$ would imply RH.
- **THM-PAPER-0122-8** (Theorem 32 (Garunkstis), theorem (cited), scope: asymptotic; Sec. 16, Theorem 32). For $0<\varepsilon\le1/2$, $f\in H(K(0.05))$ with $\max_{K(0.06)}|f|\le1$: $d(\log\zeta,f,K(0.0001),\varepsilon)\ge\exp(-\varepsilon^{-13})$ and $\tau(\log\zeta,f,K(0.0001),\varepsilon)\le\exp\exp(10\varepsilon^{-13})$.

### Key definitions

- universality of a Dirichlet series phi in D(a,b): (1.3) positive lower density for every K, f in H_0^c(K), eps
- strong universality: same for f in H^c(K), zeros allowed
- joint universality: simultaneous approximation of several functions by shifts of a tuple
- strong recurrence (9.1)
- composite universality F(zeta) (Laurincikas), Lip(alpha) class
- jointly ergodic universal (18.1)

### Principal lemmas

- **THM-PAPER-0122-L1** (Remark 1 (Kronecker-Weyl); Sec. 1). If $\alpha_1,\dots,\alpha_m$ are linearly independent over $\mathbb Q$, then for any $\theta_k$ and $\varepsilon>0$, $\lim_T\frac1T\mathrm{meas}\{\tau\le T:\|\tau\alpha_k-\theta_k\|<\varepsilon\ \forall k\}>0$. — *Role:* Applied to $\alpha_p=\log p/2\pi$ to realize arbitrary phases of finitely many Euler factors.
- **THM-PAPER-0122-L2** (Remark 2 (Mergelyan); Sec. 1). Every $f\in H^c(K)$, $K$ compact with connected complement, is a uniform limit of polynomials on $K$. — *Role:* Used by Gonek and Bagchi to reduce arbitrary targets to polynomial/exponential targets.
- **THM-PAPER-0122-L3** (Positive density method, (3.2)-(3.4); Sec. 3). Replacing the Mertens-type asymptotic $\sum_{p\le x}|a(p)|^2/p=\log\log x+a_1+O(\cdot)$ by a PNT-type positive density $\sum_{p\le x}|\tilde a(p)|^2=(1+o(1))x/\log x$ suffices for Bagchi's argument. — *Role:* Extends universality from $\zeta$ to cusp-form L-functions (Laurincikas-Matsumoto, Theorem 3), Selberg class (Thm 4).
- **THM-PAPER-0122-L4** (Rouche argument in Thm 11; Sec. 5). If $\sup_{|s-\sigma_0|\le\delta}|\varphi(s+i\tau)-(s-\sigma_0)|<\delta$, then $\varphi(\cdot+i\tau)$ has exactly one zero in $|s-\sigma_0|<\delta$. — *Role:* Converts strong universality into a positive-density zero count off the critical line.

### Proof architecture

Survey. Core scheme (Sec. 1): finite Euler-product truncation approximates zeta in a mean-square sense in 1/2<sigma<1; Kronecker-Weyl gives arbitrary phases on finitely many primes; targets are reduced to exponentials/polynomials by Mergelyan (Bagchi) or Pecherskii rearrangement (Voronin) or Hadamard-three-circles/Hahn-Banach (Good). Generalization to other L-functions needs a prime-number-type asymptotic for a(p) (positive density method) and a Ramanujan-type bound; joint universality needs an orthogonality/linear independence condition (Selberg orthogonality, matrix conditions for twists, Mishou's method). Strong universality (no non-vanishing) holds for Hurwitz zeta with transcendental or rational parameter, and implies positive-density zero counts via Rouche, contradicting zero-density estimates for zeta. RH link: zero-freeness of zeta in D(1/2,1) is exactly what makes f=zeta admissible, giving Bagchi's equivalence.

Dependency edges: CAND-01610 → CAND-02263 (survey context: effective universality (Sec. 16) later improved by)

**Imported results.** Voronin 1975; Bagchi thesis 1981; Mishou 2007 joint universality; Nagoshi-Steuding 2010; Garunkstis 2002 effective bound; Deligne bound for cusp forms

**Techniques.** Kronecker-Weyl equidistribution; Mergelyan approximation; functional limit theorems (Bagchi); positive density method; Rouche theorem; zero-density estimates; Selberg orthogonality; discrepancy estimates (Schmidt, Niederreiter); Baker theorem / six exponentials (Nakamura, Pankowski)

## Context and interpretation

**Importance and obstacle overcome.** Single entry point to the universality literature with exact classes and regions. The main obstacle tracked is extending beyond Euler products with Ramanujan (positive density method, Maass forms without Ramanujan via 4th power mean, Nagoshi) and obtaining ineffective-to-effective results.

**Relation to prior work.** Companion to Laurincikas book (1996) and Steuding's lecture notes (2007); cites the author's earlier surveys [136][137]. Does not cover later effective result of Lamzouri-Lester-Radziwill (2016) since predates it.

**Limitations and open questions.** Conj. 1 (Steuding): distinct primitive Selberg-class functions are jointly universal; counterexamples to the stated iff form (Nagoshi, Mishou). Conj. 2 (Linnik-Ibragimov) is false as stated (a_n=1 on powers of 2, Remark 6). Conj. 3 (Mishou): joint strong universality for Lerch zeta functions with any distinct lambda_j and transcendental alpha. Open: algebraic irrational alpha for Hurwitz strong universality; (9.4) at d=0 (implies RH); effective rates; universality in D(1/2,1) for general Dedekind zeta (known only in D(1-1/d_F,1) beyond abelian fields).

## Research potential

- **Hypotheses that might be weakened.** Theorem 4 needs the PNT-type (3.4); replacing by a Rankin-Selberg-free lower density would enlarge the class. Region D(sigma_phi,1) with sigma_phi=1-1/d is limited by mean-value estimates; improving to D(1/2,1) via density hypotheses (Lee for Hecke L-functions).
- **Generalizations.** Extend Bagchi-type RH equivalence (Thm 20) to GRH for Selberg-class members and to the zero-free-in-a-strip statement for Rankin-Selberg or Dedekind zeta; quantify via effective universality (CAND-02263).
- **Candidate connections.** Strong recurrence (9.1) and (9.4) at d=0 link to almost periodicity (Bohr) and to Nakamura-Pankowski; compare with the observatory family F (L-function families) and E (derivative/descent) via derived-function universality (Sec. 17).
- **Reusable lemmas.** Rouche step of Theorem 11 as a template to turn any positive-density approximation of a function with a simple zero into a zero count; Kronecker-Weyl plus Mergelyan reduction.
- **Possible experiments.** Numerically estimate density d(zeta,f,K,eps) for small K and f=exp(polynomial) to compare with Garunkstis lower bound exp(-eps^{-13}); test (9.1) numerically for Dirichlet L-functions with/without Siegel-type zeros as a stress test, noting finite data cannot decide RH.
- **Risks / barriers.** Universality is compatible with RH and with its failure; it only yields equivalences (Bagchi) whose strong-recurrence side is itself as hard as RH. Effective forms give only logarithmic rates.

## Audit notes (Level 1 reader)

none noticed in inspected portion. (Survey v1 of 2014; later arXiv versions may differ. Sections 6-8 and 10-15 were not read in detail.)

*These notes are a reader's observations, not verified findings; see `audits/` for adjudicated findings.*

## Provenance

- Candidate `CAND-01610`; harvest queries: msc_11M06, arxiv_universality_zeta.
- Triage decision: include — Best survey on Voronin universality.
- Record generated by `tools/make_records.py`; search cutoff 2026-11-17.
