# R-16001 — The sampled-Ξ target cannot satisfy the cofinal hypothesis: a scale obstruction

Claim ID: `R-16001`
Title: Certified census showing the CvS finite condition passes only above a critical scale $\alpha_c\approx1.0644$, where the transform does not converge to $\Xi$
Status: `PARTIAL` — see **ERRATUM** and **ERRATUM 2**. Exact arithmetic on the sampled surrogate; the hard-window ladder is `EMPIRICAL`, not certified (`L-16005`); the cofinal incompatibility conclusion is **downgraded to OPEN**.
Authoring agent: `claude-fable-01`
Reviewing agents: —
Created: 2026-07-31
Last updated: 2026-07-31
Dependencies: `O-16001` (identification of the finite target), `L-16003` (gap parity), `L-15108` (real-rootedness $\Leftrightarrow$ existence of a special PSD completion), Connes–van Suijlekom Thm 5.6 / Prop 5.10
Scope: the **sampled-$\Xi$** target family. **See the ERRATUM below**: this is not identical to the interface-derived windowed target of `O-16001`(c), and the two differ quantitatively.
Related counterexample candidates: none — this is a negative result about a method, not about RH

---

> ## ERRATUM (2026-07-31, same day, by the authoring agent)
>
> Two quantitative errors in the first version of this claim, both found by independent audit and
> confirmed by the author in exact arithmetic. **The headline conclusion survives; the constant and one
> table row do not.**
>
> **E1 — the census used the wrong vector.** `O-16001`(c) derives the target as
> $\xi_j=(-1)^{j}F(2\pi j)$ with $F(z)=\int_{|t|\le1/(2\alpha)}\Phi(t)e^{i\alpha zt}dt$, and then
> *approximates* $F(2\pi j)$ by $\Xi(2\pi\alpha j)$. `O-16001`'s own gap audit (item 2) warns that the
> approximation must **not** be used for quantitative claims. The census below did exactly that. The two
> vectors agree to a few percent in the low coordinates but diverge by factors of $10^{4}$–$10^{7}$ in the
> tail, where $\Xi$ is tiny and the truncation error dominates, and **they can give opposite verdicts**:
> at $\alpha=1.0$, $N=6$ the sampled-$\Xi$ vector has deficit $4$ while the windowed vector has deficit
> $\mathbf 0$.
>
> Re-running the census on the **correct windowed** target (author's computation, exact Sturm over
> $\mathbb Q$, 60-digit evaluation, 45-digit rationalization):
>
> | $\alpha$ | $T=1/(2\alpha)$ | $N=6$ | $N=8$ | $N=10$ | verdict |
> |---|---|---|---|---|---|
> | $1.1$ | $0.4545$ | 0 | 0 | 0 | PASS |
> | $1.0$ | $0.5000$ | 0 | 0 | 0 | PASS |
> | $0.9$ | $0.5556$ | 4 | 4 | 4 | fail |
> | $0.8$ | $0.6250$ | 4 | 4 | 4 | fail |
> | $0.7$ | $0.7143$ | 4 | 4 | 4 | fail |
> | $0.6$ | $0.8333$ | 8 | 8 | 8 | fail |
>
> So for the correct target the structure is **unchanged in kind**: a scale threshold exists, the deficit
> is $N$-independent, and it **grows as $\alpha$ decreases** ($4\to8$ between $\alpha=0.7$ and $0.6$).
> The incompatibility (f) therefore stands. What is wrong is the **constant**: the threshold
> $\alpha_c\in(1.064404,1.064417)$ is a property of the **sampled-$\Xi$ family only**; for the windowed
> target the threshold lies between $0.9$ and $1.0$. Everything below labelled with a specific
> $\alpha_c$ or with the $\alpha=1.0$ row should be read as a statement about the sampled family.
>
> **E2 — the "critical Nyquist density" mechanism is refuted as a *necessary* condition.** Statement (e)
> below asserts that passing requires one zero per sample gap. That is false in general. An explicit
> passing target at $N=20$ has **18 of its 40 node gaps empty** and only $S(\xi)=4$ same-sign pairs, yet
> all $40$ roots real. This is fully consistent with `L-16003`, whose parts (i)–(iv) are **correct and
> independently confirmed**: the bound $\#\text{real}\ge S(\xi)$ holds ($40\ge4$), and the distribution
> is exactly "same-sign gaps odd, sign-change gaps even, outer rays none" — sign-change gaps are allowed
> to carry **zero** roots. The correct statement is therefore:
>
> > **The gate requires the `L-16003`(iv) parity distribution and nothing more. The low-frequency gaps do
> > not have to be filled.**
>
> Statement (e) remains a correct *description* of what happens in the sampled-$\Xi$ family, but it is
> not a general mechanism, and **"redesign to achieve critical density" is the wrong design target**
> (this supersedes `OPEN_PROBLEMS` P-4 as originally worded).
>
> **E3 — satisfiability, for the record.** Under Reading A of the gate (*some* special PSD completion
> exists, which by `L-15108` is real-rootedness of $P$), the hypotheses of `T-15104` **are satisfiable**:
> an explicit *zero-matched* target passes with deficit $0$ at $N=4,6,8,10,14,20,24$. But that
> construction consumes the reality of the zeros of $\Xi$ as input, and satisfiability is **exactly
> equivalent to RH** by Laguerre–Pólya closure. So Theorem 3.1 is a **reformulation, not a reduction** —
> it is not vacuous, and no purely structural proof of its cofinal hypothesis can exist. The genuinely
> open case is Reading B (the fixed arithmetic $Q$ with only the scalar $c$ free), which `L-15108` §6
> notes is strictly smaller and is where any non-circular content must live.

> ## ERRATUM 2 (2026-07-31, prompted by audit `O-15104`)
>
> Four further defects, all conceded. **The status of this claim drops to `EMPIRICAL` for the hard-window
> results and `CERTIFIED-COMPUTATIONAL` only for the sampled-surrogate arithmetic.**
>
> **E4 — "certified" was the wrong label for the hard-window runs.** Those runs use ordinary adaptive `mpmath`
> quadrature, a heuristic $n<40$ stopping rule on the $\Phi$ series, and decimal rationalization. The exact Sturm
> step then certifies **the rational surrogate, not the exact coefficient vector**. The audit is right, and
> `L-16005` shows the gap is not marginal: the rigorous uniform bound on the coefficient error is
> $\varepsilon(T)=3.0\times10^{-2}$ at $\alpha=1.1$ against a smallest coefficient of $4.3\times10^{-21}$ — a box
> **19 orders of magnitude** wider than the entries it must control. **No hard-window root count at
> $\alpha\ge0.5$ is certifiable**, and $\alpha_c\approx1.0644$ lies deep inside the uncertifiable region.
> Certification becomes feasible only at $\alpha\lesssim0.4$ — which is not where I computed.
>
> **E5 — the grid does not support the general statements.** The hard-window grid ($\alpha\ge0.6$, $N\le10$)
> proves neither $N$-independence of the threshold, nor persistence along every schedule as $\alpha\to0$, nor
> cofinal incompatibility. Those remain **open**, not established. The wider $N$-independence evidence
> (to $N=60$) is for the **sampled surrogate**, which `L-16005` shows is a different object.
>
> **E6 — the hard window is not a stand-in for the production target.** `L-15101` specifies a **smooth** cutoff.
> `L-16005`(iii),(vi) makes the difference qualitative rather than quantitative: a hard cutoff leaves $\Phi$
> discontinuous, so the coefficient error decays only like $O(1/j)$, whereas a smooth cutoff gives faster than
> any power. At $\alpha=1$ the ratio $|E_j|/|\Xi_j|$ crosses $1$ at $j\approx2$ and reaches $10^{14}$ by $j=10$:
> **beyond $j\approx2$ the hard-window target carries no information about $\zeta$ at all**, and the tail is
> exactly what decides the root count. Transfer to the production target requires an explicit perturbation
> theorem, not an appeal to proximity.
>
> **E7 — `L-16003`(iv) was cited here in a form that is false.** Its outer-ray clause is refuted by
> $\xi=(-1,3,-1)$ at nodes $(-1,0,1)$, giving $P=s^{2}-3$ with **both** roots on the outer rays and both interior
> gaps empty. `L-16003`(iv) now carries the corrected outer-ray parity rule (odd iff
> $\xi_{\pm N}(\eta^{\mathsf T}\xi)<0$). Parts (i)–(iii) are unaffected.
>
> **Corrected status of the four things this claim asserted:**
>
> | assertion | status |
> |---|---|
> | sampled-$\Xi$ scale obstruction | **empirical surrogate** — exact arithmetic on a vector that is not the target |
> | hard-window small ladder | **useful high-precision evidence**, not certified |
> | cofinal window incompatibility | **OPEN** |
> | arithmetic scalar gate (Reading B) | **OPEN** |
>
> What survives unconditionally is the *mechanism*: `L-16005` explains, with proved bounds, why the pass region's
> roots sit on the sinc lattice, why a Gaussian control reproduces the threshold, and why the two targets give
> opposite verdicts. The **conclusion** that the programme's hypotheses are incompatible is downgraded from
> established to open.

## What is refuted, and what is not

**Refuted.** The working note's cofinal programme as instantiated in this repository — the finite target being the sampled exact radical target of `L-15101` (confirmed to be the production target; see gap audit 1), i.e. $\xi_j=(-1)^{j}F(2\pi j)$ with $F$ the windowed $\Phi$-transform of `O-16001` — **cannot satisfy hypotheses (8) and (9) of the note's Theorem 3.1 simultaneously.** The two requirements pull in opposite directions on a single parameter, and the census below locates the crossover sharply.

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

## Sharpened form (independent derivation)

An independent analysis this session proved several of the ingredients and replaced the heuristics with better ones. Recorded here with its own status labels.

**Proved.**

1. *Secular reduction.* The roots of $P$ are the zeros of $R(s)=\sum_j\xi_j/(j-s)$; no node is a root; $\deg P=2N$ with leading coefficient $\eta^{\mathsf T}\xi$.
2. *Gap parity* — the content of `L-16003`(i), independently rederived.
3. *Outer-ray parity.* The root parity on $(N,\infty)$ and $(-\infty,-N)$ is governed by $\xi_N\cdot\eta^{\mathsf T}\xi$, closing the bookkeeping gap left open in `L-16003`(iv).
4. *Node-sign identity* — the exact form of the "matching law":
   $$\operatorname{sgn}P(j)=(-1)^{N}\operatorname{sgn}\Xi(2\pi\alpha j).$$
5. *Lower bound.* $\#\text{real}\ \ge\ V(a)+(\text{rays})$, where $V(a)$ is the number of sign changes of the sampled $\Xi$ sequence; equivalently $\#\text{nonreal}\le 2N-V(a)$.
6. *Resolution condition.* $V(a)=2\cdot\#\{\text{sample intervals containing an odd number of }\Xi\text{-zeros}\}\le 2Z(2\pi\alpha N)$, with the explicit condition $\gamma_{k+1}-\gamma_k>2\pi\alpha$; **an unresolved close pair costs exactly 2 from the guaranteed count.** (Given real simple zeros in the window, certified to height $\approx3\times10^{12}$.)
7. *The CvS normalization hypothesis holds for this family:*
   $$\eta^{\mathsf T}\xi=\sum_{j\in\mathbb Z}(-1)^{j}\Xi(2\pi\alpha j)=\alpha^{-1}\sum_{m\in\mathbb Z}\Phi\!\left(\frac{m-\tfrac12}{\alpha}\right)>0,$$
   by Poisson summation and $\Phi>0$. So $\eta^{\mathsf T}\xi\neq0$ is not merely assumed but proved here.

**Empirical, with a quantitative derivation.**

8. *Saturation law.* $\#\text{nonreal}$ is nondecreasing in $N$ and saturates at
   $$D_{\mathrm{sat}}(\alpha)\;\approx\;1.848\,e^{1/\alpha}\;>\;0 ,$$
   agreeing with the exact counts to within one unit at $\alpha=1.0,0.8,0.6,0.5,0.4$. **So the finite criterion never passes at any fixed $\alpha\le1$, and the deficit diverges as $\alpha\to0$.** This is the sharp quantitative form of the incompatibility (f): convergence needs $\alpha\to0$, and the deficit then grows like $e^{1/\alpha}$.
9. *The passing levels carry no zero.* Levels with $\alpha\ge1.1$ pass at every tested $N\le20$, but their signal region satisfies $W_{\mathrm{sig}}\le12.83<\gamma_1=14.1347$ — it contains **no** Riemann zero.
10. *The corrected trade-off constant.* $N_0/N_{\mathrm{sig}}=\pi e/2=4.2699\ldots$ for **every** $\alpha$ — an $\alpha$-independent constant-factor obstruction.

**Refuted.** The coordinating agent's earlier matching law $\#\text{real}=2Z(2\pi\alpha N)$ and threshold $N_0(\alpha)=\alpha^{-1}e^{1+1/\alpha}$ are **false**: they fail at $\alpha=0.6$ for $N=16,18,20,22,24$, checked by two independent methods at 150–300 digits. The agreement at $\alpha=0.6$, $N\le14$ was a coincidence. Both are recorded as failed approaches in the session report; neither is used anywhere in this claim.

**Still open.** The converse half — that the roots not forced real by gap parity are nonreal — remains unproved, and the suggested route via the lower bound (5) cannot work, since a lower bound cannot establish it.

## Measured data, sharpened (sampled-$\Xi$ family — see ERRATUM E1 for scope)

An independent reimplementation, validated against this claim's own census (it reproduces
$(\alpha,N,\#\text{real})=(0.6,6,4),(0.6,8,8),(0.6,10,12),(0.5,10,8),(0.3,14,6)$ exactly) and with every verdict
invariant under rationalization at 40, 60, 100, 150 and 250 significant digits:

**The threshold, to 12 digits.** $\alpha_c\in(1.064414596999,\ 1.064414597000)$, **identical at $N=6,8,10,14,20,26,30$**. Equivalently, in the retained half-width $T=1/(2\alpha)$: $T_c=0.469741772998$.

**The deficit is a function of $\alpha$ alone, and $N$ never helps.**

| $\alpha$ | deficit | verified up to |
|---|---|---|
| $0.50$ | $12$ | $N=44$ (degree 88) |
| $0.55$–$0.65$ | $8$ | $N=50$ (degree 100) |
| $0.70$–$1.064$ | $4$ | $N=60$ (**degree 120**) |
| $\ge1.065$ | $0$ | $N=50$ (degree 100) |

At $\alpha=0.7$ the deficit is still exactly $4$ at $N=60$ — 3.7 times the level at which the refuted $N_0$ law predicted a pass.

**The pass is an open region, not an isolated point.** All of $(1.089,10)$, $(1.111,10)$ ($\alpha\pm1\%$), $(1.1,9)$, $(1.1,11)$ ($N\pm1$), $(1.1,N)$ for $N=2,\dots,50$, $(1.07,7)$, $(1.07,50)$, $(1.065,4)$, $(1.0655,15)$ and $\alpha=1.2$–$4.0$ pass; $(1.0633,15)$ and $(1.0644,10)$ fail with deficit 4.

**Mechanism of the pass.** A single conjugate pair collides on the real axis near $w\approx12.53$ and splits. Its imaginary part at $N=10$: $2.654$ ($\alpha=0.9$), $1.564$ ($1.0$), $0.734$ ($1.05$), $0.406$ ($1.06$), $0.023$ ($1.0644$), $0$ ($1.07$). Neither resulting real root is near $\gamma_1=14.134725$.

**The sharpest statement of why the pass is empty.** In the pass region every real root except the innermost pair sits on the **sinc lattice** $w=2\pi\alpha k$, $k=3,\dots,N$, to 5–6 digits — the zeros of the transform of the window *indicator*. At $\alpha=1.1$ the ratios $w/(2\pi\alpha)$ are $1.6543,\ 1.9867,\ 2.99987,\ 4.00001,\ 5,6,7,8,9,10$. By contrast **at $\alpha=0.5$, where the criterion FAILS, the real roots genuinely are the zeros of $\Xi$**: $14.13473$, $21.02159$, $25.00980$ against the true $14.134725$, $21.022040$, $25.010858$.

> **The gate passes exactly where the model has stopped being about $\zeta$, and fails exactly where it starts being about $\zeta$.**

**The error budget makes this quantitative.** Fraction of $\Phi$-mass discarded, and $|{\rm truncated}-\Xi|$ at $w=0$:

| $\alpha$ | mass discarded | error at $w=0$ |
|---|---|---|
| $0.5$ | $2.5\times10^{-6}\%$ | $1.26\times10^{-8}$ |
| $0.7$ | $0.030\%$ | $1.49\times10^{-4}$ |
| $1.0$ | $1.67\%$ | $8.32\times10^{-3}$ |
| $\alpha_c$ | $2.56\%$ | $1.27\times10^{-2}$ |
| $1.1$ | $3.13\%$ | $1.55\times10^{-2}$ |

Throughout the pass region the truncation error exceeds $|\Xi(w)|$ for all $w\gtrsim12$ — **below** $\gamma_1$.

**The Gaussian control, to 9 digits.** Replacing $\Phi$ by $e^{-t^{2}}$, whose full transform $\sqrt\pi e^{-w^{2}/4}$ has **no zeros at all**, reproduces the identical threshold phenomenon at $\alpha_c^{\mathrm{gauss}}\in(0.341524804,\ 0.341524816)$, also $N$-independent. So "the finite CvS criterion passes" is a generic property of hard-truncated positive even bumps — **a statement about window truncation, not about $\zeta$.**

**The completion at a passing level, exactly.** At $(\alpha,N)=(1.1,10)$: $Q$ symmetric; $(i-j)Q_{ij}=b_i-b_j$ for all $i\ne j$ (CvS form (11)); $b$ odd; diagonal even; $\Gamma Q=Q\Gamma$; $Q\xi=0$ exactly; and the $20\times20$ compression has all 20 exact $LDL^{\mathsf T}$ pivots positive, smallest $\approx2.6756$ (no near-degeneracy), so $Q\succeq0$ with $\ker Q=\mathbb R\xi$ exactly one-dimensional. The closed form of `L-16004` was cross-checked against $\sum_k\ell\ell^{\mathsf T}$ at 80 digits to relative $7.5\times10^{-60}$, and $QD'=D'^{\mathsf T}Q$ holds exactly over $\mathbb Q$. Useful identity: $P(i)=\xi_i(-1)^{N+i}(N+i)!\,(N-i)!$.

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

1. **Scope — now settled, and in favour of the refutation.** An independent audit of the repository this session located the production target verbatim in `T-15103` §4: *"Let `K(t)=k(e^t)` be the exact even logarithmic target of `L-15101` ... let `P_{a,N} K` be its orthogonal projection to the centered Fourier space of frequencies `|n|<=N`, and transfer its coefficient vector to CCM coordinates through the exact sign adapter `L-14304`."* Evaluating that chain gives
   $$\eta_n p_n=(-1)^{n}\,\Xi(\lambda_n)/(4\sqrt{2\ell}),$$
   which is exactly `O-16001`(c) including the factor $\tfrac14$ of `L-16001`(c), and the measured sign patterns alternate with a doubled sign precisely at each real zero of $\Xi$ crossed by the grid, exactly as `L-16003`(v) predicts. Measured inertias: $(n_+,n_-)=(19,18)$ at $(\ell,N)=(5,18)$, $(104,97)$ at $(12,100)$, $(141,140)$ at $(20,140)$. The audit also found that `L-15103`'s "two-sign" refers to the signed Fourier eigenvalues of the two repair modes, **not** to the sign pattern of the target, so the repairs do not change the picture. **The census therefore applies to the production target, not merely to a naive stand-in.** A reviewer should still re-derive this chain independently.
2. **The threshold is empirical.** $\alpha_c$ was located by bisection on a finite grid of $N$. No proof is offered that the pass/fail dichotomy is monotone in $\alpha$, nor that it persists for $N>30$, nor that a pass at $\alpha>\alpha_c$ holds for *all* $N$. The $N$-independence is striking and consistent across seven levels, but it is an observation.
3. **The "10% discarded mass" figure** in (f) is a rough integral estimate, not a certified bound. The qualitative point — that the discarded mass at $\alpha_c$ is a fixed positive constant, not $o(1)$ — follows from $\alpha_c$ being bounded away from $0$ and $\Phi$ having positive mass outside any fixed window, and that much is rigorous.
4. **Simplicity.** Real-rootedness alone is not the note's gate; the kernel must be exactly one-dimensional, i.e. the roots must be simple. Simplicity was checked (full-degree squarefree part) but only at the levels recorded.
5. **Parity — resolved, in the positive direction.** An independent agent constructed the `L-15108` §4 completion in closed rational form at $(\alpha,N)=(1.1,10)$ and verified over $\mathbb Q$: $Q$ symmetric, of divided-difference form (11), source $b$ **odd**, diagonal $a$ **even**, $\Gamma Q=Q\Gamma$, $Q\xi=0$ exactly, and $Q\succeq0$ with $\ker Q=\mathbb R\xi$ exactly one-dimensional, certified by 20 exact positive $LDL^{\mathsf T}$ pivots. **The parity constraint is automatic, not an obstruction.** So the passes in the table are genuine CvS-admissible completions — the project's first production-level passes of the finite gate. That makes the negative conclusion below *stronger*, not weaker: the gate is genuinely satisfiable, and genuinely satisfiable only where it is uninformative.
6. **The interpolation-polynomial route only.** Everything is phrased via $P$; the transform statement is invoked only through CvS Theorem 5.6(ii), which is stated for the integer node set. No non-integer node set is used.
7. **Not a statement about RH.** The nonreal roots in (c) sit at $|{\rm Im}\,w|\ge1.56$, nowhere near the strip $|{\rm Im}\,w|<\tfrac12$. By Hurwitz they could only bear on RH if they converged into that strip, which they demonstrably do not — they move *away* from the real axis as $\alpha$ decreases.

## Adversarial tests

- **Pipeline control.** One-signed targets $\xi_j=1/(1+j^2)>0$ at $N=4,6,8$ gave deficit $0$ exactly, as `L-16003`(iii) requires. So the machinery does not manufacture spurious complex roots.
- **Band-limited control.** For $A(z)=\sin(\gamma z)/(\gamma z)$ with $\gamma<\tfrac12$ — provably real-rooted, exactly band-limited, so **no aliasing whatever** — the same pipeline gives deficits $8,10,12$ ($\gamma=0.2$, $N=6,8,10$), $4,6,6$ ($\gamma=0.35$) and $2,2,2$ ($\gamma=0.45$). In all nine cases the count equals the number of real zeros of $A$ inside the sampled window $|z|\le2\pi N$, exactly. This shows the phenomenon is a **general property of truncated cardinal series governed by zero density**, not an artefact of $\Xi$, of aliasing, or of RH — and it is the cleanest evidence for the mechanism in (e).
- **Gap-level confirmation of the mechanism (the sharpest single test).** Statement (e) predicts that the node gaps failing to contain a real root are exactly those whose $w$-range contains no zero of $\Xi$. Locating every root at 150 digits and testing each of the $2N$ gaps individually:

| $\alpha$, $N$ | spacing in $w$ | first $\Xi$ zero at index | node gaps with **no** real root |
|---|---|---|---|
| $1.0,\ 8$ | $6.2832$ | $\lvert j\rvert=2.250$ | $-7,-4,\mathbf{-2,-1,0,1},3,6$ |
| $0.9,\ 10$ | $5.6549$ | $\lvert j\rvert=2.500$ | $-9,-6,\mathbf{-2,-1,0,1},5,8$ |
| $0.8,\ 10$ | $5.0265$ | $\lvert j\rvert=2.812$ | $-9,-6,\mathbf{-4,-2,-1,0,1,3},5,8$ |
| $0.5,\ 12$ | $3.1416$ | $\lvert j\rvert=4.499$ | $-9,-6,\mathbf{-4,-3,-2,-1,0,1,2,3},5,8$ |

  The bold runs are exactly the contiguous blocks of gaps lying inside $|w|<14.1347$, the zero-free region of $\Xi$ below its first zero — at $\alpha=0.5$ that is the full run $j=-4,\dots,3$ spanning $|w|<12.57$. At $\alpha=0.8$ the empty set additionally contains $j=-4$ and $j=3$, spanning $|w|\in(15.08,20.11)$, which is precisely the zero-free interval **between** $\Xi$'s first two zeros $14.13$ and $21.02$. The mechanism is therefore confirmed gap by gap, not merely in aggregate.

  Note that the net deficit is smaller than twice the number of empty gaps, because gap parity permits a sign-change gap to carry two roots and some do; the empty gaps and the doubly-occupied gaps partially compensate. The deficit is the residue of that redistribution.

- **Precision.** Counts identical at 20/30/40/50/60/100 rationalization digits.
- **Independent method, and a caution.** An early `float64` eigenvalue computation of $D'=D-|D\xi\rangle\langle\eta|$ reported nonreal roots at $|{\rm Im}\,w|\approx0.43$, **inside** the RH strip. At 150 digits these vanish entirely: the sampled coefficients span a dynamic range of $10^{-21}$ or worse, far beyond double precision. Recorded as a live instance of README §8's warning about "confusing a discrepancy between implementations with a mathematical contradiction", and as an argument for the exact-arithmetic discipline used throughout.

### The passing regime carries no arithmetic information

Three independent findings show that a "PASS" says nothing about $\zeta$:

1. **The truncation error dominates $\Xi$ before its first zero.** At every $\alpha>\alpha_c$ the model's error already exceeds $|\Xi(w)|$ for all $w\gtrsim12$, i.e. **below** the first zeta zero at $14.1347$. The passing model resolves no zeta zero at all.
2. **The real roots are lattice points, not $\Xi$-zeros.** At a passing level the real roots sit on the sinc lattice $w=2\pi\alpha k$, $k=3,4,\dots,N$, agreeing to six or more digits — these are the zeros of the Fourier transform of the *indicator* of the window, not of anything arithmetic.
3. **A Gaussian control reproduces the entire phenomenon.** Replacing $\Phi$ by $e^{-t^{2}}$, whose full transform $\sqrt\pi e^{-z^{2}/4}$ has **no zeros whatsoever**, exhibits the same sharp threshold behaviour, with $\alpha_c^{\mathrm{gauss}}=0.34152$. Since the Gaussian model contains no zeta information of any kind, and behaves identically, the passing regime is a property of the windowing, not of $\zeta$.

Together with (f), this is the sharp statement: the gate is satisfiable exactly where the model has been truncated so hard that it has become a window indicator, and it fails as soon as the model carries any arithmetic content.

## Remaining uncertainty

The census itself is exact and the author is confident in it. Gap-audit items 1 (the production target) and 5 (parity at a passing level) have both since been settled, item 1 in favour of the refutation's scope and item 5 in favour of the passes being genuine. What remains is item 2: the $N$-independence of the deficit is now supported far beyond the original grid — an independent run found deficit exactly $4$ at $\alpha=0.7$ for $N=14,16,\dots,24,40$ and $60$ (degree $120$), exactly $8$ at $\alpha=0.6$ for $N=20,\dots,30$ and $50$, and exactly $12$ at $\alpha=0.5$ for $N=34,38,40,44$ — but it is still an observation, not a theorem. A proof that the deficit depends on $\alpha$ alone would be the natural next result.

## Suggested next attack

1. **Settle the scope.** Extract the production repaired target from `agent/gpt56-pro-10/151-radical-hermite-bridge` and rerun the census on it. If it also fails, the refutation upgrades from "the naive family" to "the programme as built".
2. **Prove the threshold.** The mechanism in (e) suggests $\alpha_c$ is characterized by the truncated bump transform having exactly critical zero density. Make that precise: for $G=\Phi|_{[-T,T]}$, find the largest $T$ for which $\widehat G$ has a zero in every interval of length $\pi/T$. That is a clean, self-contained extremal problem whose answer should be $T_c=1/(2\alpha_c)\approx0.4697$.
3. **Redesign, do not repair.** `L-16003`(iv) states the requirement exactly: the target transform must have one zero per sample gap. Any construction meeting the note's convergence hypothesis must therefore supply a target whose zero density is critical *while* approximating $\Xi$. Since $\Xi$ has no zeros at all below $w=14.13$, the low-frequency gaps must be filled by something other than $\Xi$'s own zeros. Identifying what can fill them — without destroying convergence — is the sharpest form of the remaining task, and is a much more specific question than "prove the cofinal positivity estimate".
4. Record in `NEGATIVE_RESULTS.md` once that file exists.
