# PAPER-0002 — Bounding \(|\zeta (\frac12 +it)|\) on the Riemann hypothesis

| Field | Value |
|---|---|
| Authors | Chandee, Vorrapan; Soundararajan, K. |
| Year / stratum | 2011 / S5 |
| Venue | Bull. Lond. Math. Soc. 43, No. 2, 243-250 (2011). |
| Identifiers | zbMATH [1238.11078](https://zbmath.org/?q=an:1238.11078) · DOI [10.1112/blms/bdq095](https://doi.org/10.1112/blms/bdq095) · arXiv [0908.2008](https://arxiv.org/abs/0908.2008) |
| MSC | 11M06 |
| Families | A |
| Work type | original_paper |
| Evidence level of this record | **L1** |
| Full text | fulltext_read — https://arxiv.org/abs/0908.2008 |
| Selection | score 4.8721, in-pool citations 37, seed lists 2, triage relevance 4 |

## Mathematical content (Level 1: full text read)

**Research question.** Under RH, find the sharp constant for the Littlewood-type bound |zeta(1/2+it)| << exp(C log t/loglog t), by reframing the problem as optimal band-limited minorization of f(x)=log((4+x^2)/x^2) and invoking the Carneiro-Vaaler extremal functions together with the explicit formula (the analogue of Goldston-Gonek's treatment of S(t)).

**Historical motivation.** Littlewood 1924 gave |zeta(1/2+it)|<<exp(C log t/loglog t) on RH; only the constant C was improved (Ramachandra-Sankaranarayanan, Soundararajan C>0.3724 = (1+lambda_0)/4). Goldston-Gonek's sharp S(t) bound (1/2+o(1)) log t/loglog t via Selberg extremal majorants suggested a matching sharp method for |zeta|, as asked by Soundararajan.

### Main results

- **THM-PAPER-0002-1** (Theorem 1.1, theorem (conditional on RH), scope: asymptotic; Sec 1, Thm 1.1 (p.1)). Assume RH. For large real $t$, $|\zeta(\tfrac12+it)|\ll\exp\Big(\frac{\log2}{2}\frac{\log t}{\log\log t}+O\Big(\frac{\log t\,\log\log\log t}{(\log\log t)^2}\Big)\Big)$. Equivalent: $\log|\zeta(\frac12+it)|\le(\frac{\log2}2+o(1))\frac{\log t}{\log\log t}$. *Conditional on:* RH.
- **THM-PAPER-0002-2** (Eq (2), identity (conditional on RH), scope: asymptotic; Sec 2, eq (2)-(3)). On RH with $\rho=\tfrac12+i\gamma$: $\log|\zeta(\tfrac12+it)|=\log t+O(1)-\tfrac12\sum_\gamma f(t-\gamma)$, where $f(x)=\log\frac{4+x^2}{x^2}$ (from Hadamard factorization of $\xi$ at $s=\frac12+it$ and $-\frac32+it$ and Stirling). *Conditional on:* RH.
- **THM-PAPER-0002-3** (Proposition 2.1, proposition (unconditional), scope: global; Sec 2 (statement), Sec 3 (proof)). For each $\Delta>0$ there is an entire $g_\Delta$ with (i) $-C/(1+x^2)\le g_\Delta(x)\le f(x)$ for real $x$ and $|g_\Delta(x+iy)|\ll\frac{\Delta^2}{1+\Delta|x+iy|}e^{2\pi\Delta|y|}$; (ii) $\hat g_\Delta$ real, supported in $|\xi|\le\Delta$, $|\hat g_\Delta|\ll1$; (iii) $\int_{-\infty}^\infty(f-g_\Delta)\,dx=\frac1\Delta\big(2\log2-2\log(1+e^{-4\pi\Delta})\big)$ [as printed; the exact normalization should be checked in the source].
- **THM-PAPER-0002-4** (Eq (5), inequality (conditional on RH), scope: asymptotic; Sec 2 p.3). For any $\Delta>0$ (RH): $\log|\zeta(\tfrac12+it)|\le\frac{\log t}{2\pi\Delta}\log\frac{2}{1+e^{-4\pi\Delta}}+\frac12\mathrm{Re}\sum_{n\ge2}\frac{\Lambda(n)}{n^{1/2+it}}\hat g_\Delta\big(\frac{\log n}{2\pi}\big)+O\Big(\frac{\Delta^2e^{\pi\Delta}}{1+\Delta t}+1\Big)$. With $\sum_n\Lambda(n)n^{-1/2}|\hat g_\Delta(\log n/2\pi)|\ll e^{\pi\Delta}$ and the choice $\pi\Delta=\log\log t-3\log\log\log t$ one gets Thm 1.1. *Conditional on:* RH.

### Key definitions

- f(x)=log((4+x^2)/x^2)
- g_Delta (L1-optimal entire minorant of f_Delta of exponential type 2 pi Delta)

### Principal lemmas

- **THM-PAPER-0002-L1** (Lemma 2.2; Sec 2). Explicit formula for $\sum_\rho h(\gamma)$ for $h$ analytic in $|\mathrm{Im}\,s|\le\frac12+\epsilon$, real on reals, $|h(s)|\ll(1+|s|)^{-(1+\delta)}$: $\sum h(\gamma)=h(\frac1{2i})+h(-\frac1{2i})-\frac1{2\pi}\hat h(0)\log\pi+\frac1{2\pi}\int h(u)\mathrm{Re}\frac{\Gamma'}\Gamma(\frac14+\frac{iu}2)du-\frac1{2\pi}\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}\big(\hat h(\frac{\log n}{2\pi})+\hat h(-\frac{\log n}{2\pi})\big)$. — *Role:* Converts sum over zeros of g_Delta(t-gamma) into a short prime sum (imported, standard)
- **THM-PAPER-0002-L2** (Carneiro-Vaaler Theorem 1.1 (imported); Sec 3). For $f_\mu(x)=\int_0^\infty(e^{-\lambda|x|}-e^{-\lambda})d\mu(\lambda)$ with $0<\int\lambda/(\lambda^2+1)d\mu<\infty$, $G_\mu(z)=\lim_N(\cos\pi z/\pi)^2\sum_{n=-N}^{N+1}\big[\frac{f_\mu(n-1/2)}{(z-n+1/2)^2}+\frac{f_\mu'(n-1/2)}{z-n+1/2}\big]$ is entire of exponential type at most $2\pi$, $G_\mu\le f_\mu$ on R, and minimizes $L^1$ distance to $f_\mu$ among such minorants. — *Role:* Source of the extremal minorant g_Delta
- **THM-PAPER-0002-L3** (Identity (7); Sec 3 eq (7)). $\int_0^\infty(e^{-\lambda|x|}-e^{-\lambda})\frac{2(1-\cos2\Delta\lambda)}{\lambda}d\lambda=\log\frac{4\Delta^2+x^2}{x^2}-\log(4\Delta^2+1)$, i.e. $f_\Delta(x)=f(x/\Delta)-f(1/\Delta)$ is of Carneiro-Vaaler type for $d\mu_\Delta=\frac{2(1-\cos2\Delta\lambda)}\lambda d\lambda$. — *Role:* Shows log((4+x^2)/x^2) is covered by the Carneiro-Vaaler class
- **THM-PAPER-0002-L4** (Bound (9); Sec 3). $|G_\Delta(x+iy)+f(1/\Delta)|\ll\frac{\Delta^2}{1+|x+iy|}e^{2\pi|y|}$ via Poisson summation $\sum(\cos\pi z/\pi)^2(z-n+\frac12)^{-2}=1$ and $f(x)\le4/x^2$, $|f'(x)|\le8/(|x|(4+x^2))$. — *Role:* Growth control needed to apply the explicit formula

### Proof architecture

Hadamard factorization of xi evaluated at 1/2+it and -3/2+it gives log|zeta(1/2+it)|=log t+O(1)-(1/2) sum_gamma f(t-gamma) under RH. Replace f by an entire minorant g_Delta of exponential type 2 pi Delta (so that sum f >= sum g_Delta) with explicit L1 error; apply the explicit formula (Lemma 2.2) with h(z)=g_Delta(t-z), obtaining a main term (log t/(2 pi Delta)) log(2/(1+e^{-4 pi Delta})) (using the Stirling integral) and a short prime sum supported on n<=exp(2 pi Delta). Trivial bound on the prime sum (<< e^{pi Delta}) with pi*Delta=loglog t-3 logloglog t gives (log 2/2)(log t/loglog t) plus lower order. Proposition 2.1 is obtained from Carneiro-Vaaler's optimal minorant for f_Delta (identity (7), growth bound (9), and a cruder lower bound replacing the expected nonnegativity of G_Delta+f(1/Delta)).

Dependency edges: CAND-01180 → Carneiro-Vaaler extremal functions (imports Theorem 1.1); CAND-01180 → Goldston-Gonek 2007 (adapts method from S(t) to log|zeta|); CAND-01180 → Soundararajan 2009 (C>(1+lambda_0)/4) (improves constant)

**Imported results.** Carneiro-Vaaler, Some extremal functions in Fourier analysis II/III (Theorem 1.1); Explicit formula, Lemma 1 of Goldston-Gonek [5] / Iwaniec-Kowalski Thm 5.12; Hadamard factorization of xi (Davenport Ch. 12); Stirling's formula

**Techniques.** Hadamard product for xi, partial fractions; explicit formula (Weil-Guinand) with band-limited test functions; extremal functions of exponential type (Beurling-Selberg-Vaaler-Carneiro-Vaaler); Poisson summation; choice of parameter pi*Delta=loglog t-3logloglog t

## Context and interpretation

**Importance and obstacle overcome.** Improves the best constant in the conditional Lindelof-type bound to log2/2 ~ 0.3466 (from 0.3724 of Soundararajan). Obstacle: f has a logarithmic singularity at 0 so classical Selberg functions do not apply; resolved by recognizing f_Delta as a Laplace-type mixture and using Carneiro-Vaaler's optimal minorants.

**Relation to prior work.** Improves Soundararajan (2009, C>0.372) and Chandee (explicit version for L-functions). Parallels Goldston-Gonek for S(t) and uses the same family of tools as Soundararajan's M(x) paper (CAND-01251). Lower bound known unconditionally: |zeta(1/2+it)|>=exp((1+o(1)) sqrt(log t/loglog t)) infinitely often (Soundararajan, Bondarenko-Seip later improved). Farmer-Gonek-Hughes conjecture suggests true size exp((1/2+o(1)) sqrt(log t loglog t)).

**Limitations and open questions.** Conditional on RH; is claimed to attain the limit of existing methods (the explicit formula with the trivial prime-sum bound e^{pi Delta}); the true maximal order is conjecturally exp(sqrt(log t loglog t)/sqrt2...) i.e. exponent (1/2+o(1)) sqrt(log t loglog t), far smaller. Improvement would require non-trivial cancellation in the prime sum.

## Research potential

- **Hypotheses that might be weakened.** Only RH is used; the constant log2/2 uses the trivial bound for prime sum. Any smoothing that exploits oscillation of sum Lambda(n) n^{-1/2-it} g-hat could lower the constant (cf. Soundararajan resonance, Bondarenko-Seip lower bounds).
- **Generalizations.** Carry the same method to L(1/2+it,chi) and to L-functions in the Selberg class under GRH (Chandee's earlier explicit version), to log|zeta'| bounds, and to Re log zeta(sigma+it) for sigma>1/2; Carneiro-Vaaler minorants also give optimal constants for arg of L(s,chi) at higher derivative.
- **Candidate connections.** Combine with CAND-01251 (typical/atypical points) to bound the measure of t where log|zeta| exceeds a large value, giving improved M(x) bounds; connect to the 'xi geometry and derivative descent' programme via the Hadamard-product identity (2) linking log|xi(1/2+it)| to sum f(t-gamma) of zero spacings.
- **Reusable lemmas.** Prop 2.1 (explicit minorant g_Delta with L1 error (2log2-2log(1+e^{-4 pi Delta}))/Delta) is a reusable extremal-function lemma; eq (5) is a clean RH-conditional inequality for log|zeta(1/2+it)| in terms of a band-limited prime sum.
- **Possible experiments.** Numerically compute the optimal minorant G_Delta by the Carneiro-Vaaler series and verify Prop 2.1(iii) numerically, then compute actual sup_{t<=T} of the right side of (5) using Odlyzko zeros to see how tight log2/2 * log t/loglog t is at accessible heights (log t/loglog t is tiny there, so compare with (5) for fixed Delta).
- **Risks / barriers.** Bound is the endpoint of the extremal-function method with trivial prime-sum estimate; beating log 2 / 2 requires input on correlation of prime sums with t not yet available. Only valid under RH, so no evidence regarding RH itself.

## Audit notes (Level 1 reader)

Triage summary says 'Beurling-Selberg extremal majorants'; the paper actually uses Carneiro-Vaaler minorants (a generalization) - minor labeling issue. Proposition 2.1(i) lower bound is -C/(1+x^2) rather than non-negativity (authors remark that G_Delta+f(1/Delta)>=0 is expected but not proved; a cruder bound suffices). The exact constant in 2.1(iii) is as printed in the extraction; the factorization 2 log 2 - 2 log(1+e^{-4 pi Delta}) over Delta should be double-checked against the main-term log(2/(1+e^{-4 pi Delta})) in (5). The final lower-order terms (O(log t logloglog t/(loglog t)^2)) arise from pi*Delta=loglog t-3logloglog t but the derivation was summarized rather than written out. Otherwise none noticed in inspected portion.

*These notes are a reader's observations, not verified findings; see `audits/` for adjudicated findings.*

## Provenance

- Candidate `CAND-01180`; harvest queries: kw_RH_any, msc_11M06, arxiv_rh_abs, arxiv_rh_ti.
- Triage decision: include — Improves Littlewood's RH bound for |zeta(1/2+it)| via Fourier-analytic extremal problem.
- Record generated by `tools/make_records.py`; search cutoff 2026-11-17.
