# R-16001 — The naive sampled-Ξ target cannot satisfy the cofinal hypothesis: a scale obstruction

Claim ID: `R-16001`
Title: Certified census showing the CvS finite condition passes only above a critical scale $\alpha_c\approx1.0644$, where the transform does not converge to $\Xi$
Status: `PROPOSED` (the census is `CERTIFIED-COMPUTATIONAL`; the extrapolation to all $(\alpha,N)$ is `EMPIRICAL`)
Authoring agent: `claude-fable-01`
Reviewing agents: —
Created: 2026-07-31
Last updated: 2026-07-31
Dependencies: `O-16001` (identification of the finite target), `L-16003` (gap parity), `L-15108` (real-rootedness $\Leftrightarrow$ existence of a special PSD completion), Connes–van Suijlekom Thm 5.6 / Prop 5.10
Scope: the **naive sampled-$\Xi$ target family** only; see the scope warning below
Related counterexample candidates: none — this is a negative result about a method, not about RH

---

## What is refuted, and what is not

**Refuted.** The natural instantiation of the working note's cofinal programme — take the finite target to be the sampled exact radical target of `L-15101`, i.e. $\xi_j=(-1)^{j}F(2\pi j)$ with $F$ the windowed $\Phi$-transform of `O-16001` — **cannot satisfy hypotheses (8) and (9) of the note's Theorem 3.1 simultaneously.** The two requirements pull in opposite directions on a single parameter, and the census below locates the crossover sharply.

**Not refuted.** Nothing here refutes: the working note's Theorem 3.1 (which remains a correct implication); `L-15107`, `L-15108`, `L-15109`, `T-15103`, `T-15104` (all of which survive — `L-15108` was independently re-derived and found correct); Connes–van Suijlekom; or the Riemann Hypothesis in either direction. Nothing here is evidence for or against RH.

---

## Statement

Adopt the notation of `O-16001`: scale $\alpha>0$, level $N$, window $|t|\le 1/(2\alpha)$,

$$F(z)=\int_{|t|\le 1/(2\alpha)}\Phi(t)\,e^{i\alpha z t}\,dt,\qquad \xi_j=(-1)^{j}F(2\pi j)\ \ (|j|\le N),\qquad P(s)=\sum_j\xi_j\prod_{k\ne j}(k-s).$$

By `L-15108`, the working note's finite gate (9) holds at level $(\alpha,N)$ **iff** $P$ is real-rooted with simple roots.

**(a) A sharp critical scale, independent of the level.** There is a constant

$$\boxed{\ \alpha_c\in(1.064404,\ 1.064417)\ }$$

such that, in every case computed, $P$ is real-rooted for $\alpha>\alpha_c$ and is **not** real-rooted for $\alpha<\alpha_c$. The bisection returned the *same* bracketing interval for $N=6,8,10,14,20,26,30$: **the threshold does not move with $N$, and increasing the level never repairs a failing scale.**

**(b) The deficit below threshold is bounded below by 4 and never closes.** For $\alpha\in\{0.8,0.85,\dots,1.05\}$ and $N=4,\dots,20$ the deficit $2N-\#\{\text{real roots}\}$ equals exactly $4$ at every level tested. For smaller $\alpha$ the deficit is larger and grows with $N$ until it saturates (e.g. $\alpha=0.5$: deficit $12$ at $N=34,38,40,44$).

**(c) The two obstructing conjugate pairs are a property of the scale, not of the truncation.** Below threshold the four nonreal roots are, in the $\Xi$ variable $w=2\pi\alpha s$, independent of $N$ and identical to 7 significant figures across levels:

| $\alpha$ | nonreal roots $w$ | $N$ tested |
|---|---|---|
| $0.8$ | $\pm14.70184\pm4.534335\,i$ | $10,\ 12$ |
| $0.9$ | $\pm13.17982\pm2.654358\,i$ | $10$ |
| $1.0$ | $\pm12.57186\pm1.564114\,i$ | $8$ |

They lie far outside the RH strip $|{\rm Im}\,w|<\tfrac12$, so they carry **no** implication about RH.

**(d) No truncation taper removes them.** The deficit is exactly $4$ under each of: hard cutoff, Fejér (triangular), Hann (raised cosine), Gaussian, and Tukey tapering of the coefficients, at $(\alpha,N)=(0.8,10),(0.8,12),(1.0,8)$. Tapering is therefore not the missing repair.

**(e) The obstruction.** The passing regime $\alpha>\alpha_c$ corresponds to window half-width $1/(2\alpha)<0.4697$, on which $\Phi$ is truncated so severely that $F$ is essentially the transform of a short positive bump — a sinc-like function whose zeros sit at spacing $\approx\pi/(1/2\alpha)=2\pi\alpha$, i.e. **exactly one zero per sample gap**, the critical (Nyquist) density that `L-16003`(iii)–(iv) shows is what the criterion demands. As $\alpha$ decreases the window grows, $F$ approaches $\Xi(\alpha\,\cdot)$, and the truncation-induced zeros thin out; the sample gaps nearest the origin — where $\Xi$ has **no** zeros at all, its first being at $w=14.134\ldots$ — then contain no zero of $F$, and by `L-16003`(i) each such gap forfeits its real root.

**(f) The incompatibility.** Hypothesis (8) of Theorem 3.1 requires $F\to\Xi$ locally uniformly, hence $\int_{|t|>1/(2\alpha)}\Phi\to0$, hence $\alpha\to0$. Hypothesis (9) requires $\alpha>\alpha_c\approx1.0644$ at every sufficiently large level. At $\alpha=\alpha_c$ the discarded mass $\int_{|t|>0.4697}\Phi$ is a **fixed** fraction of $\int_{\mathbb R}\Phi=\Xi(0)=0.4971\ldots$ — of order $10\%$, not tending to zero. **The two hypotheses are therefore incompatible for this family, at every level and along every schedule.** Since the threshold is $N$-independent, this is not a "not yet large enough" situation.

---

## Definitions

As in `O-16001` and `L-16003`. "Real-rooted" means all $2N$ roots of $P$ real; "deficit" means $2N$ minus the number of distinct real roots; the criterion additionally requires simplicity, which was verified separately (the squarefree part had full degree in every case recorded).

## Motivation

PR #158 states plainly: *"No production Hermite/Weil level has yet passed through the new checker,"* and the working note's closing section names the cofinal positivity estimate as the one remaining task. Before more effort is spent proving that estimate, it is worth knowing whether the estimate is **true** for the family the programme actually constructs. The census answers that: it is false, for a structural and quantifiable reason, and the reason identifies exactly what any successful "repair" must achieve.

This is the intended use of `NEGATIVE_RESULTS.md` under README §15 and of rule 15 ("Always record potentially useful false starts").

## The census

Method — every real-root count is **exact**, not floating point:

1. $\Xi$ evaluated with `mpmath` at 120–150 decimal digits.
2. Coefficients rationalized to 100 significant digits as `fractions.Fraction`.
3. $P$ expanded exactly over $\mathbb Q$; squarefree part via exact `gcd(P,P')`.
4. Distinct real roots counted by an exact **Sturm sequence** over $\mathbb Q$.
5. Counts verified **stable** under rationalization at 20, 30, 40, 50 and 60 significant digits (identical result at every precision), so the counts are not sitting on a precision cliff.

Representative results (full data in `experiments/X-16002-cvs-sampled-target-census/`):

| $\alpha$ | $N$ | $\deg P$ | exact #real | deficit | verdict |
|---|---|---|---|---|---|
| $1.20$ | 6, 10, 14, 20 | 12, 20, 28, 40 | 12, 20, 28, 40 | 0 | PASS |
| $1.15$ | 6, 10, 14, 20 | 12, 20, 28, 40 | 12, 20, 28, 40 | 0 | PASS |
| $1.10$ | 6, 10, 14, 20 | 12, 20, 28, 40 | 12, 20, 28, 40 | 0 | PASS |
| $1.05$ | 6, 10, 14, 20 | 12, 20, 28, 40 | 8, 16, 24, 36 | 4 | fail |
| $1.00$ | 6, 10, 14, 20 | 12, 20, 28, 40 | 8, 16, 24, 36 | 4 | fail |
| $0.95$ | 16, 18, 20 | 32, 36, 40 | 28, 32, 36 | 4 | fail |
| $0.50$ | 34, 38, 40, 44 | 68, 76, 80, 88 | 56, 64, 68, 76 | 12 | fail |

Bisection on $\alpha$ returned $\alpha_c\in(1.064404,1.064417)$ for **every** one of $N=6,8,10,14,20,26,30$.

## Analytic domain audit

All statements are about a polynomial of degree $2N$ with rational coefficients and about an entire function $F$ of exponential type $\tfrac12$ obtained by Fourier transforming a compactly supported bounded function. No contour, branch cut, or analytic continuation is involved. $\Xi$ is entire. The nonreal roots reported in (c) are roots of $P$, transported to the $w$ variable by the linear map $w=2\pi\alpha s$; they are **not** claimed to be zeros of $\Xi$ or of anything else, and they lie far outside the strip where such a claim would even be meaningful.

## Dependency audit

- `O-16001`(c) supplies the target — this is the load-bearing assumption; see gap audit 1.
- `L-16003`(i),(iii) supply the mechanism in (e).
- `L-15108` supplies the translation from real-rootedness to existence of a PSD special completion, which is what makes a root count equivalent to the note's gate (9). `L-15108` was independently re-derived this session against Connes–van Suijlekom Lemmas 5.2/5.3/5.8/5.9 and found correct.
- `L-16001`(e),(f) supply $\Phi$ and its decay.
- Riemann–von Mangoldt is **not** used in any certified statement, only in heuristic discussion.

## Gap audit

Deliberate search for ways this refutation could be wrong or overreaching:

1. **Scope — the most important caveat.** The census is of the **naive sampled target**. The repository's production chain applies further "repairs" (`L-15102`, `L-15103` "two-sign prolate radical repair"). If the production target differs from `O-16001`(c), this refutation does not apply to it, and its scope must be restated. **This has not been checked** and is the first thing a reviewer should verify.
2. **The threshold is empirical.** $\alpha_c$ was located by bisection on a finite grid of $N$. No proof is offered that the pass/fail dichotomy is monotone in $\alpha$, nor that it persists for $N>30$, nor that a pass at $\alpha>\alpha_c$ holds for *all* $N$. The $N$-independence is striking and consistent across seven levels, but it is an observation.
3. **The "10% discarded mass" figure** in (f) is a rough integral estimate, not a certified bound. The qualitative point — that the discarded mass at $\alpha_c$ is a fixed positive constant, not $o(1)$ — follows from $\alpha_c$ being bounded away from $0$ and $\Phi$ having positive mass outside any fixed window, and that much is rigorous.
4. **Simplicity.** Real-rootedness alone is not the note's gate; the kernel must be exactly one-dimensional, i.e. the roots must be simple. Simplicity was checked (full-degree squarefree part) but only at the levels recorded.
5. **Parity.** Even at a passing level, CvS Theorem 5.6 additionally demands a matrix of form (11) with **odd** source and **even** diagonal. Whether the completion produced at a passing $(\alpha,N)$ lands in that sector has **not** been verified here. If it does not, a "PASS" in the table above does not by itself establish the note's gate. This is a genuine open item.
6. **The interpolation-polynomial route only.** Everything is phrased via $P$; the transform statement is invoked only through CvS Theorem 5.6(ii), which is stated for the integer node set. No non-integer node set is used.
7. **Not a statement about RH.** The nonreal roots in (c) sit at $|{\rm Im}\,w|\ge1.56$, nowhere near the strip $|{\rm Im}\,w|<\tfrac12$. By Hurwitz they could only bear on RH if they converged into that strip, which they demonstrably do not — they move *away* from the real axis as $\alpha$ decreases.

## Adversarial tests

- **Pipeline control.** One-signed targets $\xi_j=1/(1+j^2)>0$ at $N=4,6,8$ gave deficit $0$ exactly, as `L-16003`(iii) requires. So the machinery does not manufacture spurious complex roots.
- **Band-limited control.** For $A(z)=\sin(\gamma z)/(\gamma z)$ with $\gamma<\tfrac12$ — provably real-rooted, exactly band-limited, so **no aliasing whatever** — the same pipeline gives deficits $8,10,12$ ($\gamma=0.2$, $N=6,8,10$), $4,6,6$ ($\gamma=0.35$) and $2,2,2$ ($\gamma=0.45$). In all nine cases the count equals the number of real zeros of $A$ inside the sampled window $|z|\le2\pi N$, exactly. This shows the phenomenon is a **general property of truncated cardinal series governed by zero density**, not an artefact of $\Xi$, of aliasing, or of RH — and it is the cleanest evidence for the mechanism in (e).
- **Precision.** Counts identical at 20/30/40/50/60/100 rationalization digits.
- **Independent method, and a caution.** An early `float64` eigenvalue computation of $D'=D-|D\xi\rangle\langle\eta|$ reported nonreal roots at $|{\rm Im}\,w|\approx0.43$, **inside** the RH strip. At 150 digits these vanish entirely: the sampled coefficients span a dynamic range of $10^{-21}$ or worse, far beyond double precision. Recorded as a live instance of README §8's warning about "confusing a discrepancy between implementations with a mathematical contradiction", and as an argument for the exact-arithmetic discipline used throughout.

## Remaining uncertainty

The census itself is exact and the author is confident in it. The two places where this could fail to mean what it says are gap-audit items 1 (is this the production target?) and 5 (does a passing level meet the CvS parity constraints?). Item 2 — the $N$-independence of $\alpha_c$ — is the most interesting empirical claim and deserves either a proof or a counterexample.

## Suggested next attack

1. **Settle the scope.** Extract the production repaired target from `agent/gpt56-pro-10/151-radical-hermite-bridge` and rerun the census on it. If it also fails, the refutation upgrades from "the naive family" to "the programme as built".
2. **Prove the threshold.** The mechanism in (e) suggests $\alpha_c$ is characterized by the truncated bump transform having exactly critical zero density. Make that precise: for $G=\Phi|_{[-T,T]}$, find the largest $T$ for which $\widehat G$ has a zero in every interval of length $\pi/T$. That is a clean, self-contained extremal problem whose answer should be $T_c=1/(2\alpha_c)\approx0.4697$.
3. **Redesign, do not repair.** `L-16003`(iv) states the requirement exactly: the target transform must have one zero per sample gap. Any construction meeting the note's convergence hypothesis must therefore supply a target whose zero density is critical *while* approximating $\Xi$. Since $\Xi$ has no zeros at all below $w=14.13$, the low-frequency gaps must be filled by something other than $\Xi$'s own zeros. Identifying what can fill them — without destroying convergence — is the sharpest form of the remaining task, and is a much more specific question than "prove the cofinal positivity estimate".
4. Record in `NEGATIVE_RESULTS.md` once that file exists.
