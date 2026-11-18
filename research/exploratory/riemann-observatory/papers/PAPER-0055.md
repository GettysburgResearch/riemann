# PAPER-0055 — Bandlimited approximations and estimates for the Riemann zeta-function

| Field | Value |
|---|---|
| Authors | Carneiro, Emanuel; Chirre, Andrés; Milinovich, Micah B. |
| Year / stratum | 2019 / S6 |
| Venue | Publ. Mat., Barc. 63, No. 2, 601-661 (2019). |
| Identifiers | zbMATH [1454.11154](https://zbmath.org/?q=an:1454.11154) · DOI [10.5565/PUBLMAT6321906](https://doi.org/10.5565/PUBLMAT6321906) · arXiv [1710.10362](https://arxiv.org/abs/1710.10362) |
| MSC | 11M06, 11M26, 41A30 |
| Families | A, B |
| Work type | original_paper |
| Evidence level of this record | **L1** |
| Full text | fulltext_read — https://arxiv.org/abs/1710.10362 |
| Selection | score 4.5533, in-pool citations 13, seed lists 0, triage relevance 4 |

## Mathematical content (Level 1: full text read)

**Research question.** Assuming RH, give explicit sharp upper and lower bounds for S_{0,alpha}(t)=pi^{-1}arg zeta(alpha+it), S_{-1,alpha}=pi^{-1}Re zeta'/zeta(alpha+it), and the antiderivatives S_{n,alpha}(t) for 1/2<alpha<1, extending the critical-line bounds of Carneiro-Chandee-Milinovich and Carneiro-Chirre, via Beurling-Selberg extremal bandlimited functions and the Guinand-Weil formula.

**Historical motivation.** Littlewood (1924) S_n(t)=O(log t/(loglog t)^{n+1}) under RH; Goldston-Gonek introduced the explicit-formula method; Chandee-Soundararajan, CCM and Carneiro-Chirre optimized constants on the critical line. This paper moves into the strip.

### Main results

- **THM-PAPER-0055-1** (Definitions (1.1), definition, scope: global; Sec. 1.1). $S_{0,\alpha}(t)=\frac1\pi\arg\zeta(\alpha+it)$ (continuous variation from 2, averaged at zeros); $S_{n,\alpha}(t)=\int_0^tS_{n-1,\alpha}(\tau)d\tau+\delta_{n,\alpha}$ with $\delta_{2k-1,\alpha}=\frac{(-1)^{k-1}}{\pi}\int_\alpha^\infty\!\!\int_{\sigma_{2k-2}}^\infty\cdots\int_{\sigma_1}^\infty\log|\zeta(\sigma_0)|d\sigma_0\cdots d\sigma_{2k-2}$ and $\delta_{2k,\alpha}=\frac{(-1)^{k-1}(1-\alpha)^{2k}}{(2k)!}$; $S_{-1,\alpha}(t)=\frac1\pi\operatorname{Re}\frac{\zeta'}\zeta(\alpha+it)$.
- **THM-PAPER-0055-2** (Theorem 1 (recalled from [3,5]), theorem (imported), scope: asymptotic; Sec. 1.2, p. 2). Assume RH. For $n\ge0$: $-(C_n^-+o(1))\frac{\log t}{(\log\log t)^{n+1}}\le S_n(t)\le(C_n^++o(1))\frac{\log t}{(\log\log t)^{n+1}}$ with $C_0^\pm=\frac14$; for $n=4k+1$: $C_n^-=\frac{\zeta(n+1)}{\pi2^{n+1}}$, $C_n^+=\frac{(1-2^{-n})\zeta(n+1)}{\pi2^{n+1}}$; for $n=4k+3$ the roles swap; for even $n\ge2$, $C_n^+=C_n^-=\Big(\frac{2(C_{n+1}^++C_{n+1}^-)C_{n-1}^+C_{n-1}^-}{C_{n-1}^++C_{n-1}^-}\Big)^{1/2}$. *Conditional on:* RH.
- **THM-PAPER-0055-3** (Theorem 2, theorem, scope: asymptotic; Sec. 1.3, pp. 3-4). Assume RH, $n\ge-1$, $\frac12<\alpha<1$, $c>0$, $\log\log t\ge4$ and $(1-\alpha)^2\log\log t\ge c$. (i) $n=-1$: $-C^-_{-1,\alpha}(t)(\log t)^{2-2\alpha}+O_c\big(\frac{(\alpha-\frac12)(\log t)^{2-2\alpha}}{(1-\alpha)^2\log\log t}\big)\le S_{-1,\alpha}(t)\le C^+_{-1,\alpha}(t)(\log t)^{2-2\alpha}+O_c\big(\frac{(\log t)^{2-2\alpha}}{(\alpha-\frac12)(1-\alpha)^2\log\log t}\big)$. (ii) $n\ge0$: $-C^-_{n,\alpha}(t)\frac{(\log t)^{2-2\alpha}}{(\log\log t)^{n+1}}+O_{n,c}\big(\frac{(\log t)^{2-2\alpha}}{(1-\alpha)^2(\log\log t)^{n+2}}\big)\le S_{n,\alpha}(t)\le C^+_{n,\alpha}(t)\frac{(\log t)^{2-2\alpha}}{(\log\log t)^{n+1}}+O_{n,c}(\text{same})$. For odd $n\ge-1$: $C^\pm_{n,\alpha}(t)=\frac1{2^{n+1}\pi}H_{n+1}\big(\pm(-1)^{(n+1)/2}(\log t)^{1-2\alpha}+\frac{2\alpha-1}{\alpha(1-\alpha)}\big)$ with $H_n(x)=\sum_{k\ge0}x^k/(k+1)^n$; $n=0$ uses (1.8) (built from $C^\pm_{1,\alpha}$ and $C^-_{-1,\alpha}$); even $n\ge2$ uses interpolation formula (1.9), the strip analogue of the formula in Thm 1. *Conditional on:* RH.
- **THM-PAPER-0055-4** (Corollary 3, corollary, scope: asymptotic; p. 4). Assume RH. For $t$ large, $|S(t)|\le\frac14\frac{\log t}{\log\log t}+O\big(\frac{\log t}{(\log\log t)^2}\big)$ (new proof of the CCM bound, with a $\log\log\log t$ factor removed from the error). *Conditional on:* RH.
- **THM-PAPER-0055-5** (Corollary 4, corollary, scope: asymptotic; pp. 4-5). Assume RH. For large $t$: $\log|\zeta(\tfrac12+it)|\le\frac{\log2}{2}\frac{\log t}{\log\log t}+O\big(\frac{\log t}{(\log\log t)^2}\big)$, deduced from the lower bound for $S_{-1,\alpha}$ in Thm 2 together with the strip bound $\log|\zeta(\sigma+it)|\le\log\frac1{1-\sigma}+O(\frac{(\log t)^{2-2\sigma}}{(1-\sigma)\log\log t})$ for $\frac12+\frac1{\log\log t}\le\sigma\le1-\frac1{\log\log t}$. *Conditional on:* RH.
- **THM-PAPER-0055-6** (Corollary 5, corollary, scope: asymptotic; p. 4). Assume RH, $n\ge-1$, fixed $\frac12<\alpha<1$. Then $|S_{n,\alpha}(t)|\le\frac{\omega_n}{2^{n+1}\pi}\Big(1+\frac{2\alpha-1}{\alpha(1-\alpha)}+o(1)\Big)\frac{(\log t)^{2-2\alpha}}{(\log\log t)^{n+1}}$ as $t\to\infty$, where $\omega_n=1$ for $n$ odd and $\omega_n=\sqrt2$ for $n$ even. *Conditional on:* RH.
- **THM-PAPER-0055-7** (Lemma 7 (Representation lemma), lemma, scope: global; Sec. 2, p. 8; kernels (1.10)-(1.12)). Assume RH. For $n\ge-1$, $t\ge2$: $S_{2m,\alpha}(t)=\frac{(-1)^m}{\pi(2m)!}\sum_\gamma f_{2m,\alpha}(t-\gamma)+O_m(1)$ and $S_{2m+1,\alpha}(t)=\frac{(-1)^m}{2\pi(2m+2)!}(\frac32-\alpha)^{2m+2}\log t-\frac{(-1)^m}{\pi(2m)!}\sum_\gamma f_{2m+1,\alpha}(t-\gamma)+O_m(1)$ (second formula as read), with $f_{2m,\alpha}(x)=\int_\alpha^{3/2}(\sigma-\alpha)^{2m}\big(\frac{x}{(\sigma-\frac12)^2+x^2}-\frac x{1+x^2}\big)d\sigma$, $f_{2m+1,\alpha}(x)=\frac12\int_\alpha^{3/2}(\sigma-\alpha)^{2m}\log\frac{1+x^2}{(\sigma-\frac12)^2+x^2}d\sigma$, $f_{-1,\alpha}(x)=\frac{\alpha-\frac12}{(\alpha-\frac12)^2+x^2}$. *Conditional on:* RH.

### Key definitions

- S_{n,alpha}(t) with constants delta_{n,alpha}
- H_n(x)=sum x^k/(k+1)^n
- kernels f_{n,alpha}
- C^pm_{n,alpha}(t)

### Principal lemmas

- **THM-PAPER-0055-L1** (Lemma 6; Sec. 2, p. 7). Under RH, for $n\ge0$, $\frac12\le\alpha\le1$: $S_{n,\alpha}(t)=-\frac1\pi\operatorname{Im}\{\frac{i^n}{n!}\int_\alpha^\infty(\sigma-\alpha)^n\frac{\zeta'}\zeta(\sigma+it)d\sigma\}$; and $S_{-1,\alpha}=\frac1\pi\operatorname{Re}\frac{\zeta'}\zeta(\alpha+it)$. — *Role:* Integral representation (Selberg/Fujii) for all iterates, by induction on n.
- **THM-PAPER-0055-L2** (Lemma 8; Sec. 2, ~line 536 of text). Guinand-Weil explicit formula (as in CAND-01806). — *Role:* Imported tool.
- **THM-PAPER-0055-L3** (Lemma 9 (Poisson kernel extremals); Sec. 3.2). For $\beta>0$, $\Delta>0$ there is a unique pair of real entire functions $m^\pm_{\beta,\Delta}$ of exponential type $2\pi\Delta$ with $m^-\le h_\beta\le m^+$ on $\mathbb R$ ($h_\beta$ the Poisson kernel) minimizing $\int(m^+-m^-)$; they are even with explicit Fourier transforms. — *Role:* Step 2 for n=-1 (Gaussian subordination of Carneiro-Littmann-Vaaler).
- **THM-PAPER-0055-L4** (Lemma 10; Sec. 3.3, p. 15). For $m\ge0$, $\frac12\le\alpha\le1$, $\Delta\ge1$ there is a unique pair of extremal minorant/majorant $g^\pm_{2m+1,\alpha,\Delta}$ of exponential type $2\pi\Delta$ for $f_{2m+1,\alpha}$ minimizing the $L^1$ gap, with explicit Fourier transforms. — *Role:* Step 2 for odd n.
- **THM-PAPER-0055-L5** (Lemma 11 (Sum over prime powers I); Sec. 4.1). Under RH, for $0<\beta<\frac12$, $\Delta\ge1$: $\frac1\pi\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}m^\pm_\Delta(\frac{\log n}{2\pi})\cos(t\log n)$ is bounded below by an explicit expression (4.1) of size $-O(\beta e^{(1-2\beta)\pi\Delta}/\ldots)$ plus $O(\Delta^4/\beta)$. — *Role:* Prime-power sum for n=-1 with alpha>1/2.
- **THM-PAPER-0055-L6** (Lemma 12 (Sum over prime powers II); Sec. 4.2). For $m\ge0$, $\frac12\le\alpha<1$, $\Delta\ge1$, $\pi\Delta(1-\alpha)^2\ge c$: $\mp\frac1\pi\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}\hat g^\pm_\Delta(\frac{\log n}{2\pi})\cos(t\log n)\le\frac{(2\alpha-1)(2m)!e^{(2-2\alpha)\pi\Delta}}{\alpha(1-\alpha)(2\pi\Delta)^{2m+2}}+O_{m,c}\big(\frac{e^{(2-2\alpha)\pi\Delta}}{(1-\alpha)^2\Delta^{2m+3}}\big)$. — *Role:* Technical heart: prime sum for alpha>1/2, much harder than alpha=1/2.
- **THM-PAPER-0055-L7** (Sec. 6 interpolation; Sec. 6.1 (p. 30 on), Sec. 6.2 for n=0). Even $n$ (and $n=0$) obtained from odd neighbors via the mean value theorem $S_{n,\alpha}(t)-S_{n,\alpha}(t-h)=hS_{n-1,\alpha}(t^*_h)$ and optimization of $h$, giving (1.9) with the $\sqrt2$ loss of Cor. 5. — *Role:* Step 4: handles odd kernels f_{2m,alpha} for which the Beurling-Selberg problem is unsolved.

### Proof architecture

(1) Lemma 6 gives S_{n,alpha} as an integral of zeta'/zeta; Lemma 7 rewrites it as a sum over zeros of a kernel f_{n,alpha}(t-gamma). (2) Replace the kernel by extremal bandlimited majorants/minorants of exponential type 2 pi Delta (Gaussian subordination for even kernels, i.e. odd n; Lemmas 9, 10). (3) Apply Guinand-Weil to g^pm(t-.): RH makes gamma real so the pointwise inequality applies termwise; prime sum bounded by Lemmas 11, 12; optimize Delta to get Theorem 2 for odd n and n=-1. (4) Even n from odd neighbors by mean value interpolation; n=0 by a modified interpolation using S_1 bounds and only the lower bound for S_{-1}. (5) Corollaries 3-4 follow by letting alpha->1/2+ and using Soundararajan's strip bound.

**Imported results.** Guinand-Weil explicit formula (Iwaniec-Kowalski Thm 5.12); Carneiro-Littmann-Vaaler Gaussian subordination framework; Montgomery/Soundararajan strip bound on log|zeta(sigma+it)| under RH (Titchmarsh-Heath-Brown Cor. 13.16 form); Carneiro-Chandee-Milinovich (S, S_1) and Carneiro-Chirre (S_n, n>=2) critical-line bounds; Chandee-Soundararajan bound on log|zeta|

**Techniques.** Beurling-Selberg extremal majorants/minorants; Gaussian subordination (Carneiro-Littmann-Vaaler); Guinand-Weil explicit formula; Selberg/Fujii iterated integrals of S(t); mean-value interpolation; asymptotic analysis of prime-power sums

## Context and interpretation

**Importance and obstacle overcome.** First explicit RH-conditional uniform bounds for arg zeta(alpha+it) and all antiderivatives inside the critical strip, recovering the critical-line constants as alpha->1/2 with sharper error terms. The prime-power sum for strip kernels (Lemma 12) required deep use of explicit Fourier transforms, and the even-n kernels lack solved extremal problems (handled by interpolation).

**Relation to prior work.** Extends CCM (n=0,1) and Carneiro-Chirre (n>=2) from alpha=1/2 to 1/2<alpha<1 by the same method; compare with Selberg's unconditional bounds and Soundararajan's strip bound.

**Limitations and open questions.** All results are conditional on RH. Even n (including n=0 for alpha>1/2) cannot be done directly because the Beurling-Selberg problem for the odd kernels f_{2m,alpha} is unsolved, so interpolation loses sqrt 2 (Cor. 5). Upper bounds for S_{-1,alpha} blow up as alpha->1/2+ because the Poisson kernel tends to a delta. Alpha near 1 is not treated. Optimality of the constant 1/4 for S(t) remains open.

## Research potential

- **Hypotheses that might be weakened.** RH is used so zeros gamma are real and the majorant inequality applies termwise; a zero-density or zero-free-region hypothesis might give weaker conditional bounds. The condition (1-alpha)^2 loglog t >= c could be relaxed by treating alpha near 1.
- **Generalizations.** Dirichlet L-functions and Selberg-class members under GRH; S_n in strip for higher degree; other one-sided approximations for the odd kernels f_{2m,alpha} to remove the sqrt 2 loss.
- **Candidate connections.** Same Fourier-optimization toolkit as Carneiro-Milinovich-Soundararajan prime gaps (CAND-01806); bounds on Re zeta'/zeta(alpha+it) relate to Lagarias-Suzuki/Robin-type conditions and Nyman-Beurling L^1-approximation; link with pair correlation via extremal functions.
- **Reusable lemmas.** Lemma 7 (zero-sum representation) and Lemma 12 (prime-power sum with extremal Fourier transform) are reusable for any extremal-function bound of a zeta-related quantity; Theorem 2's explicit H_n(...) constants can be tested numerically.
- **Possible experiments.** Compute S_{-1,alpha}(t) and S_{0,alpha}(t) from Odlyzko zeros for alpha=0.6, 0.75 at large t and compare with C^pm_{n,alpha}(t)(log t)^{2-2alpha}/(loglog t)^{n+1}; solve the Beurling-Selberg problem numerically for f_{2,alpha}.
- **Risks / barriers.** Constants are not sharp since extremals are L^1-optimal only; no unconditional strip bounds; no information about RH itself since RH is assumed throughout.

## Audit notes (Level 1 reader)

The text layer is heavily garbled, so formulas (1.8)-(1.9), (2.3) and (4.1) were transcribed as read and may contain small errors; consult the source before reuse. Otherwise none noticed in inspected portion (proofs of Secs. 3-5 only skimmed).

*These notes are a reader's observations, not verified findings; see `audits/` for adjudicated findings.*

## Provenance

- Candidate `CAND-01821`; harvest queries: kw_RH_any, msc_11M06, msc_11M26, arxiv_critical_line, arxiv_explicit_formula, arxiv_rh_abs.
- Triage decision: include — Sharp RH-conditional bounds for S(t) and antiderivatives in the strip.
- Record generated by `tools/make_records.py`; search cutoff 2026-11-17.
