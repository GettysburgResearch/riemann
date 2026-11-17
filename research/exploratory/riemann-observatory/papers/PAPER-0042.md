# PAPER-0042 — A note on \(S(t)\) and the zeros of the Riemann zeta-function

| Field | Value |
|---|---|
| Authors | Goldston, D. A.; Gonek, S. M. |
| Year / stratum | 2007 / S5 |
| Venue | Bull. Lond. Math. Soc. 39, No. 3, 482-486 (2007). |
| Identifiers | zbMATH [1127.11058](https://zbmath.org/?q=an:1127.11058) · DOI [10.1112/blms/bdm032](https://doi.org/10.1112/blms/bdm032) · arXiv [math/0511092](https://arxiv.org/abs/math/0511092) |
| MSC | 11M26 |
| Families | A, B |
| Work type | original_paper |
| Evidence level of this record | **L1** |
| Full text | fulltext_read — https://arxiv.org/abs/math/0511092 |
| Selection | score 4.5765, in-pool citations 31, seed lists 2, triage relevance 4 |

## Mathematical content (Level 1: full text read)

**Research question.** Under RH, what is the sharp constant in Littlewood's bound S(t) << log t/loglog t and in the bound for increments S(t+h)-S(t), and what follows for the largest multiplicity of a zero and the largest gap between consecutive ordinates?

**Historical motivation.** Littlewood's 1924 RH bound S(t)<<log t/loglog t was unimproved in its constant for 80 years; Selberg conjectured/computed the true size is ~ sqrt(loglog t) in mean-square, Farmer-Gonek-Hughes conjecture sqrt(log t loglog t)/(pi sqrt 2) for limsup. This note gives the first explicit constant (1/2) via Selberg-type extremal majorants, matching the Montgomery-Odlyzko approach to gaps.

### Main results

- **THM-PAPER-0042-1** (Theorem 1 (5)-(6), theorem, scope: asymptotic; Sec. 1, p.2). Assume RH. For $t$ large and $0<h\le\sqrt t$: $N(t+h)-N(t)-\dfrac h{2\pi}\log\dfrac t{2\pi}\le\Big(\dfrac12+o(1)\Big)\dfrac{\log t}{\log\log t}$; equivalently $S(t+h)-S(t)\le(\tfrac12+o(1))\frac{\log t}{\log\log t}$. *Conditional on:* RH.
- **THM-PAPER-0042-2** (Theorem 2 (7), theorem, scope: asymptotic; Sec. 1, p.2). Assume RH. For $t$ sufficiently large, $|S(t)|\le\Big(\dfrac12+o(1)\Big)\dfrac{\log t}{\log\log t}$. *Conditional on:* RH.
- **THM-PAPER-0042-3** (Corollary 1 (9), corollary, scope: asymptotic; Sec. 1, p.2). Assume RH. For $\gamma$ large, the multiplicity of the zero $\tfrac12+i\gamma$ satisfies $m(\gamma)\le(\tfrac12+o(1))\dfrac{\log\gamma}{\log\log\gamma}$. *Conditional on:* RH.
- **THM-PAPER-0042-4** (Corollary 1 (10), corollary, scope: asymptotic; Sec. 1, p.2). Assume RH. If $\gamma<\gamma'$ are consecutive zero ordinates, $\gamma'-\gamma\le\dfrac{\pi}{\log\log\gamma}(1+o(1))$. *Conditional on:* RH.

### Key definitions

- N(t) = #{rho=1/2+i gamma: 0<gamma<=t}
- S(t)=(1/pi) arg zeta(1/2+it) by continuous variation, average value at jumps
- m(gamma)=multiplicity of zero 1/2+i gamma

### Principal lemmas

- **THM-PAPER-0042-L1** (Lemma 1; Sec. 2, (11)). Guinand-Weil explicit formula: for $h$ analytic in $|\mathrm{Im}\,s|\le\tfrac12+\epsilon$, $|h(s)|\ll(1+|s|)^{-(1+\delta)}$, real on the reals, $\sum_\rho h(\tfrac{\rho-1/2}i)=h(\tfrac1{2i})+h(-\tfrac1{2i})-\tfrac1{2\pi}\hat h(0)\log\pi+\tfrac1{2\pi}\int h(u)\mathrm{Re}\tfrac{\Gamma'}{\Gamma}(\tfrac14+\tfrac{iu}2)du-\tfrac1{2\pi}\sum_{n\ge2}\tfrac{\Lambda(n)}{\sqrt n}(\hat h(\tfrac{\log n}{2\pi})+\hat h(-\tfrac{\log n}{2\pi}))$. — *Role:* Imported (Iwaniec-Kowalski Thm 5.12, (25.10)); converts zero counting to prime sums.
- **THM-PAPER-0042-L2** (Lemma 2; Sec. 2). For $L,\delta>0$ there exist even entire $F_\pm$ with $F_-\le\chi_{[-L,L]}\le F_+$, $\int F_+\le2L+1/\delta$, $\int F_-\ge2L-1/\delta$, $F_\pm(w)\ll e^{2\pi\delta|\mathrm{Im}\,w|}$, $F_\pm(u)\ll\min(1,\delta^{-2}(|u|-L)^{-2})$ for $|u|>L$, $\hat F_\pm(x)=0$ for $|x|\ge\delta$, $\hat F_\pm(x)=\frac{\sin2\pi Lx}{\pi x}+O(1/\delta)$. — *Role:* Selberg/Beurling-Vaaler majorant-minorant of an interval of band-limit delta; imported (Montgomery-Odlyzko, Vaaler).
- **THM-PAPER-0042-L3** ((15); Sec. 2, (15)). With $h(w)=F(w-t)$, $\delta\ge1$, $0<L\le2\sqrt t$: $\sum_\gamma F(\gamma-t)=\dfrac{\hat F(0)}{2\pi}\log\dfrac t{2\pi}+O(e^{\pi\delta})$. — *Role:* Key estimate: prime-sum side bounded trivially by $\sum_{n\le e^{\pi\delta}}n^{-1/2}\ll e^{\pi\delta}$ using $\mathrm{supp}\,\hat F\subset[-\delta,\delta]$.

### Proof architecture

Apply explicit formula with h(w)=F_pm(w-t). Gamma-factor integral gives (log(t/2))F^(0)/(2pi)+O(1) (13) for L<=2 sqrt t, delta>=1. Prime sum is supported on n<e^{2 pi delta}-type range (F^ vanishes for |x|>=delta) and is bounded trivially by e^{pi delta}. Then sum_gamma F_+(gamma-t) >= #zeros in [t-L,t+L] gives count <= (1/2pi)log(t/2pi)(2L+1/delta)+O(e^{pi delta}); choose pi*delta = loglog t - 2 logloglog t so error e^{pi delta}=o(1/delta * log t) and the 1/(2 pi delta) log t term gives (1/2) log t/loglog t. F_- gives lower bound; combine and recentre (t -> t+h/2, L=h/2) for Thm 1. Thm 2 from Thm 1 using unconditional Littlewood integral int_0^T S(u)du << log T, which yields h<=log^2 t with S(t+h)<=1 (resp. >=-1). Corollary 1 by taking window h=o(1/loglog gamma) around a zero (multiplicity) and N(t+h)-N(t)=0 (gap).

**Imported results.** Iwaniec-Kowalski, Analytic Number Theory, Thm 5.12 (explicit formula); Selberg/Vaaler/Montgomery extremal functions (Lemma 2; Montgomery-Odlyzko 1984 Lemma 2); Littlewood 1924: int_0^T S(u)du << log T (unconditional) and RH bound S(t)<< log t/loglog t; Riemann-von Mangoldt formula with S(t)

**Techniques.** Guinand-Weil explicit formula; Selberg/Beurling-Vaaler band-limited extremal majorants and minorants; trivial bound on prime sum due to compact Fourier support; Littlewood's integral of S(t) to remove the shift; parameter optimization (pi*delta = loglog t - 2 logloglog t)

## Context and interpretation

**Importance and obstacle overcome.** Obstacle: Littlewood's method yields an unspecified constant. Using a majorant of the interval indicator with Fourier support width delta, the prime-sum error is e^{pi delta} while the main error is log t/(2 pi delta), giving the optimal tradeoff and the constant 1/2. Consequences: multiplicity bound (1/2) log gamma/loglog gamma and max gap <= pi/loglog gamma (1+o(1)) (which, as stated, is a gap in normalized units far from the average spacing 2 pi/log gamma).

**Relation to prior work.** 

**Limitations and open questions.** RH-conditional; constant 1/2 later improved (Carneiro-Chandee-Milinovich: |S(t)|<=(1/4+o(1)) log t/loglog t). Unconditional multiplicity bound is not addressed. The gap bound (10) is not known to be sharp and is weaker than Montgomery-Odlyzko-style bounds that average. Gap between S bound (log t/loglog t) and conjectured sqrt(log t loglog t) remains huge.

## Research potential

- **Hypotheses that might be weakened.** RH is used only to put zeros on the line so that sum over zeros of F(gamma-t) counts zeros; a zero-density version (Selberg-type, unconditional) could give a bound for #zeros off-line contribution. Constraint h<=sqrt t could be widened.
- **Generalizations.** The same extremal-function argument extends to S_1(t) and to L-functions in the Selberg class and to Dirichlet L-functions (done later by Carneiro-Chandee-Milinovich, Chandee-Soundararajan for log|zeta|); apply to S(t,chi) and to counting zeros of zeta' (Levinson-type) or of Dedekind zeta.
- **Candidate connections.** Directly parallels Soundararajan's Proposition in 'Moments of the Riemann zeta function' (CAND-01201), which cites this note and treats Re log zeta by the same explicit-formula/majorant-in-primes philosophy; Chandee-Soundararajan 'Bounding |zeta(1/2+it)| on RH' gives constant (log 2)/2; Farmer-Gonek-Hughes (CAND-01208) Conjecture B for the true size of S(t).
- **Reusable lemmas.** (15) is a clean, reusable inequality: sum_gamma F_pm(gamma-t) = F^(0)/(2pi) log(t/2pi) + O(e^{pi delta}); the Lemma 2 majorants are standard tools for any pair-correlation or gap argument.
- **Possible experiments.** Compute S(t) numerically from Odlyzko/Platt zero tables for t up to 10^{20} and compare max|S| against (1/4) log t/loglog t and against sqrt(log t loglog t)/(pi sqrt2); verify (15) numerically for F_+ with explicit Beurling-Selberg function and small delta to see where e^{pi delta} dominates.
- **Risks / barriers.** Constant 1/4 (or 1/2 * 1/2) is believed to be the limit of the Fourier-support method; breaking the log t/loglog t barrier would require genuinely new input (e.g. conjectural moments). Barrier: prime-sum bound is trivial; any nontrivial cancellation in primes would require (Montgomery-type) pair-correlation hypotheses.

## Audit notes (Level 1 reader)

Minor typographic issues in extracted text only. In the proof the prime sum is displayed as bounded 'sum_{n<e^{pi delta}}'/'<< e^{pi delta}'; since supp F^ in [-delta,delta] and F^(log n/2pi) requires log n < 2 pi delta, the actual range is n < e^{2 pi delta} (giving e^{pi delta} after trivial bound sum n^{-1/2}); the printed 'n<e^{...}' bound and the choice 'pi delta = loglog t - 2 logloglog t' are consistent with e^{pi delta} error. The step 'N(t+L)-N(t-L)-(L/pi)log(t/2pi) <= ...' combines upper (F_+) and lower (F_-) in a single two-sided statement with constant 1/2; the lower statement has constant -1/2 and they write the combined bound in absolute value, which is fine. Otherwise none noticed in inspected portion.

*These notes are a reader's observations, not verified findings; see `audits/` for adjudicated findings.*

## Provenance

- Candidate `CAND-01222`; harvest queries: kw_RH_any, kw_weil_positivity, kw_zeta_zeros, msc_11M26, arxiv_rh_abs.
- Triage decision: include — Sharpened constants for S(t) under RH with consequences for zero multiplicity and gaps.
- Record generated by `tools/make_records.py`; search cutoff 2026-11-17.
