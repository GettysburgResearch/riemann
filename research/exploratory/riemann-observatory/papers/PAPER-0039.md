# PAPER-0039 — Li coefficients for automorphic \(L\)-functions

| Field | Value |
|---|---|
| Authors | Lagarias, Jeffrey |
| Year / stratum | 2007 / S5 |
| Venue | Ann. Inst. Fourier 57, No. 5, 1689-1740 (2007). |
| Identifiers | zbMATH [1216.11078](https://zbmath.org/?q=an:1216.11078) · DOI [10.5802/aif.2311](https://doi.org/10.5802/aif.2311) · arXiv [math/0404394](https://arxiv.org/abs/math/0404394) |
| MSC | 11M26, 11M36, 11F66 |
| Families | C, E |
| Work type | original_paper |
| Evidence level of this record | **L1** |
| Full text | fulltext_read — arxiv.org/abs/math/0404394 (v4, 4 May 2005) |
| Selection | score 4.5801, in-pool citations 32, seed lists 1, triage relevance 4 |

## Mathematical content (Level 1: full text read)

**Research question.** How can Li's coefficients be defined for principal automorphic L-functions L(s,pi) on GL(N)/Q, how do they relate to the Weil quadratic functional, what are their unconditional asymptotics, and what do they become under GRH?

**Historical motivation.** Li (1997) gave positivity of lambda_n as an RH criterion; Keiper and Maslanka studied growth numerically; Bombieri-Lagarias reformulated via Weil positivity. This paper extends the whole framework to GL(N) and obtains rigorous asymptotics.

### Main results

- **THM-PAPER-0039-1** (Eq. (1.1)-(1.2), (1.9), definition and symmetry, scope: global; Sect. 1 Eqs. (1.1),(1.2),(1.9),(1.10); Sect. 2). \lambda_n(Z)=\sum'_{\rho\in Z}[1-(1-1/\rho)^n] (\ast-convergent, \lim_{T}\sum_{|\rho|\le T}), well defined for all n\in\mathbb Z for multisets Z omitting 0 and 1. For Z=Z(\pi), the zeros of \xi(s,\pi), one has \lambda_{-n}(\pi)=\lambda_n(\pi) and \lambda_n(\pi^\vee)=\lambda_n(\pi).
- **THM-PAPER-0039-2** (Sect. 1 (observation of [4], Bombieri-Lagarias), criterion (imported), scope: global; Sect. 1 Eqs. (1.6)-(1.7), Sect. 2). For a multiset Z with \sum_{\rho}\mathrm{Re}(\rho)/(1+|\rho|)^2<\infty, invariant under \rho\mapsto 1-\bar\rho and omitting 0 and 1: \mathrm{Re}\,\lambda_n(Z)\ge0 for all n>0 iff all \mathrm{Re}\,\rho=1/2. In particular RH for L(s,\pi) holds iff \mathrm{Re}\,\lambda_n(\pi)\ge0 for all n\ge0.
- **THM-PAPER-0039-3** (Theorem 3.1, theorem, scope: global; Sect. 3, Theorem 3.1). For the Li test functions G_n(s)=1-(1-1/s)^n and the Weil scalar product \langle\cdot,\cdot\rangle_{W(\pi)}: \langle G_n,G_m\rangle_{W(\pi)}=\lambda_n(\pi)+\lambda_{-m}(\pi)-\lambda_{n-m}(\pi), hence \|G_n\|^2_{W(\pi)}=\lambda_n(\pi)+\lambda_{-n}(\pi)=2\,\mathrm{Re}\,\lambda_n(\pi).
- **THM-PAPER-0039-4** (Lemma 4.2 / Eq. (1.11), arithmetic formula (unconditional), scope: global; Sect. 4, Lemma 4.2). For all n\ge1: \lambda_n(\pi)=S_\infty(n,\pi^\vee)-S_f(n,\pi^\vee)+\delta(\pi), where S_\infty(n,\pi)=\sum_{j=1}^n\binom nj\tau_{j-1}(\pi), S_f(n,\pi)=\sum_{j=1}^n\binom nj\eta_{j-1}(\pi), and \delta(\pi)=1 for \pi trivial on GL(1), else 0.
- **THM-PAPER-0039-5** (Theorem 5.1, asymptotic (unconditional), scope: asymptotic; Sect. 5, Theorem 5.1; Eq. (1.12)-(1.13)). S_\infty(n,\pi) is real, and for n\ge K(\pi)=\max_j|\kappa_j(\pi)|^2: S_\infty(n,\pi)=\tfrac N2 n\log n+C_1(\pi)n+O(N(K(\pi)+1)), with C_1(\pi)=\tfrac N2(\gamma-1-\log 2\pi)+\tfrac12\log Q(\pi), Q(\pi) the conductor; the O-constant is absolute and C_1 is independent of the archimedean parameters.
- **THM-PAPER-0039-6** (Theorem 6.1, asymptotic (unconditional bound), scope: asymptotic; Sect. 6, Theorem 6.1; Eq. (1.15)-(1.16)). S_f(n,\pi)=\lambda_n(\sqrt n,\pi^\vee)+O_\pi(\sqrt n\log n), where \lambda_n(T,\pi)=\sum_{|\mathrm{Im}\rho|<T}[1-(1-1/\rho)^n] is the incomplete Li coefficient. If GRH holds for L(s,\pi), then \lambda_n(\sqrt n,\pi^\vee)=O(\sqrt n\log n).
- **THM-PAPER-0039-7** (Theorem 1.1, theorem, scope: asymptotic; Sect. 1, Theorem 1.1 (proved by Lemma 4.2 + Thm 5.1 + Thm 6.1)). For pi irreducible cuspidal unitary automorphic on GL(N)/Q and n\ge1: \lambda_n(\pi)=\tfrac N2 n\log n+C_1(\pi)n-\lambda_n(\sqrt n,\pi)+O_\pi(\sqrt n\log n). If RH holds for L(s,\pi): \lambda_n(\pi)=\tfrac N2 n\log n+C_1(\pi)n+O_\pi(\sqrt n\log n). If RH fails the incomplete term can be exponentially large in n. *Conditional on:* GRH for L(s,pi) (second formula only).
- **THM-PAPER-0039-8** (Theorem 7.1, theorem, scope: asymptotic; Sect. 7, Theorem 7.1). (1) For every such pi there is an entire function F_\pi(z) of order one and exponential type with F_\pi(n)=\lambda_n(\pi) for n\in\mathbb Z and F_\pi(-\bar z)=\overline{F_\pi(z)}-type reality on the imaginary axis (7.1)-(7.2). (2) Under GRH for L(s,\pi) there is a unique F_\pi of exponential type at most \pi satisfying (i) and such that F_\pi(z)-e(\tfrac12,\pi)(1-\cos\pi z) has type strictly less than \pi, where e(1/2,pi) is the order of the zero of \xi(s,\pi) at s=1/2; on the real axis |F_\pi(x)|\le C(|x|+2)\log(|x|+2). Its tempered Fourier transform has countable support in [-\pi,\pi] with 0 as the only limit point. *Conditional on:* GRH for L(s,pi) in part (2).

### Key definitions

- \lambda_n(\pi)=\sum'_{\rho\in Z(\pi)}[1-(1-1/\rho)^n]
- \xi(s,\pi), Q(\pi) conductor, \kappa_j(\pi) archimedean parameters
- incomplete Li coefficient \lambda_n(T,\pi)
- \ast-convergence: \lim_{T\to\infty}\sum_{|\rho|\le T}
- Li test functions G_n(s)=1-(1-1/s)^n
- Weil scalar product \langle\cdot,\cdot\rangle_{W(\pi)}

### Principal lemmas

- **THM-PAPER-0039-L1** (Theorem 2.1 (part); Sect. 2, Theorem 2.1). Standard properties: |a_n(\pi)|\le C(\pi)d(n)n^{N/2}; \mathrm{Re}\,\kappa_j>-1/2; zeros of \Lambda(s,\pi) lie in 0<\mathrm{Re}\,s<1; N^\pm_\pi(T)=\tfrac N{2\pi}T\log T+C_0(\pi)T+O(\log T). — *Role:* Imported analytic input on the Godement-Jacquet L-functions needed to define and control lambda_n(pi).
- **THM-PAPER-0039-L2** (Kernel k_n and contour argument; Sect. 6, proof of Theorem 6.1 (Eq. 6.4) and the Lemma 6.1 estimates). k_n(s)=(1+1/s)^n-1=\sum_{j=1}^n\binom nj s^{-j}; S_f is obtained by integrating (L'/L)(s,\pi) k_n(s) over a rectangle with horizontal segments at height \pm\sqrt n, the vertical segments around the strip, and a residue at s=0. — *Role:* Core of the proof of Theorem 6.1.
- **THM-PAPER-0039-L3** (Lemma 5.1, Lemma 5.2; Sect. 5, Lemmas 5.1-5.2). Gamma-function estimates for \mathrm{Re}(z)\ge-3/4 and n\ge|z|+2 (digamma/Stirling-type with explicit error), used to evaluate S_\infty(n,\pi) via the archimedean parameters kappa_j. — *Role:* Archimedean asymptotics in Theorem 5.1.
- **THM-PAPER-0039-L4** (Lemma 4.1; Sect. 4, Lemma 4.1, Lemma 4.3). Power series expansion of (\xi'/\xi)(s,\pi) at s=1 in terms of the Euler-product logarithmic coefficients (\eta_j) and archimedean coefficients (\tau_j). — *Role:* Gives the arithmetic formula (4.6).

### Proof architecture

Sect. 2 constructs xi(s,pi) and shows lambda_n(pi) is *-convergent, with the symmetries. Sect. 3 identifies lambda_n with the Weil quadratic form on Li test functions. Sect. 4 expands (xi'/xi)(s,pi) at s=1 to split lambda_n into an archimedean sum S_infty and an arithmetic sum S_f over finite places (Lemma 4.2). Sect. 5 computes S_infty by Gamma-function/digamma analysis (Theorem 5.1). Sect. 6 bounds S_f by a contour integral of k_n(s) L'/L and compares with the incomplete Li sum at height sqrt(n) (Theorem 6.1). Theorem 1.1 combines these. Sect. 7 constructs the interpolating entire function from an integral over the zeros using Paley-Wiener-type type estimates and uniqueness under GRH.

Dependency edges: CAND-01219 → CAND-01183 (generalizes the Voros asymptotics rigorously with O(sqrt n log n) remainder under GRH); CAND-01219 → CAND-01333 (realizes Weil positivity on Li test functions)

**Imported results.** Li (1997) criterion for RH and Li's GRH criterion for Dedekind zeta functions; Bombieri-Lagarias (1999) Li criterion for general multisets Z, arithmetic formula and Weil positivity; Godement-Jacquet theory of L-functions for GL(N), analytic continuation and functional equation; Zero-counting asymptotics for L(s,pi); Weil's explicit formula

**Techniques.** Godement-Jacquet automorphic L-functions and their functional equations; Weil's explicit formula / Weil positivity; Contour integration of the logarithmic derivative against kernel k_n; Digamma/Stirling asymptotics; Paley-Wiener type arguments for entire functions of exponential type; Tempered distribution Fourier transform

## Context and interpretation

**Importance and obstacle overcome.** Defines Li coefficients for all principal automorphic L-functions, connects them to Weil positivity, and establishes unconditional asymptotics whose RH-case matches (N/2) n log n + C_1 n with an explicit conductor-dependent constant. The obstacle is controlling the finite-place sum S_f with only zero-density-free tools, handled by truncation to height sqrt(n) and a contour argument.

**Relation to prior work.** Builds on Li, Keiper, Bombieri-Lagarias and Maslanka. The author notes that Voros had obtained asymptotics for zeta by a saddle-point method; here the authors give a rigorous arithmetic-formula approach valid for GL(N).

**Limitations and open questions.** The remainder O(sqrt n log n) under GRH is not claimed sharp; the author notes Maslanka's data allow S_f of smaller order, which 'remains to be explained'. Unconditional bound requires incomplete coefficient lambda_n(sqrt n), which is large if RH fails. For n much smaller than T^2/(log T)^2 the bound holds under RH only up to height T. The structure and spectral meaning of F_pi, its Fourier support and the relation to Cramer's V-function or Voros's functions are left open.

## Research potential

- **Hypotheses that might be weakened.** Theorem 6.1's GRH-case bound uses only RH for L(s,pi) and zero counting; one can ask whether partial RH to height T = sqrt(n) (stated in text for n <= T^2/(4 log^2 T)) suffices in a smaller range. The restriction to cuspidal unitary pi over Q might be relaxed to the Selberg class.
- **Generalizations.** Extend to number-field base (Dedekind and Hecke L-functions via Li's original GRH criterion), to the Selberg class, and to function fields where lambda_n can be computed exactly.
- **Candidate connections.** Voros (CAND-01183) for the sharp dichotomy; Bombieri-Lagarias [4] Weil positivity; Maslanka's computations of lambda_n for n<=3300; Cramer's V-function and Voros's spectral functions as a possible relation to F_pi.
- **Reusable lemmas.** Theorem 3.1 gives an exact Gram matrix formula for the Li vectors in the Weil Hilbert space, usable to test positive semidefiniteness numerically. Lemma 4.2 and Theorem 5.1 give the explicit archimedean main term for any N.
- **Possible experiments.** Compute lambda_n(pi) for a few GL(2) pi (Ramanujan Delta, low-conductor Maass forms) using the arithmetic formula plus the archimedean term, and check that S_f(n)/sqrt(n) stays bounded. Test whether Re lambda_n >= 0 and the Gram matrix <G_n,G_m> remain positive semidefinite numerically.
- **Risks / barriers.** Positivity of all lambda_n is equivalent to GRH, so no unconditional lower bound on Re lambda_n at the main-term scale is available without controlling S_f at large n. Numerical positivity up to n about 10^4 gives no information on zeros at heights beyond about n/2.

## Audit notes (Level 1 reader)

Detailed proofs in Sect. 5-7 were read only at the level of statements and proof outlines, so sub-lemma correctness was not checked. Statement (7.2) in the text extraction reads 'F_pi(-z-bar)=F_pi(z)' with overlines lost, so the exact reality symmetry above is reconstructed and should be checked against the source. Theorem 6.1 proof header 'Lemma 6.1' appears twice (lines for Lemma 6.1 at two places in the extraction) which looks like a labeling duplication in the arXiv version. Otherwise none noticed in inspected portion.

*These notes are a reader's observations, not verified findings; see `audits/` for adjudicated findings.*

## Provenance

- Candidate `CAND-01219`; harvest queries: kw_RH_any, kw_li_criterion, msc_11M26, msc_11M36, arxiv_li_criterion, arxiv_rh_abs.
- Triage decision: include — Extends Li criterion to automorphic L-functions via Weil functional.
- Record generated by `tools/make_records.py`; search cutoff 2026-11-17.
