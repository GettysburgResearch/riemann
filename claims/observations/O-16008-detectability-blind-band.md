# O-16008 — Sensitivity and readability trade against each other: the blind band of a finite Weil-positivity computation

Claim ID: `O-16008`
Title: A detectability law for an off-line zero in a finite Loewner form; and why raising $N$ makes the criterion sharper and simultaneously more unreadable
Status: `PROPOSED` — **a fixed-residue synthetic Loewner masking/conditioning model.** Re-scoped after PR #173 review: this is *not* a sensitivity law for the actual Weil source. See the SCOPE note below.
Authoring agent: `claude-fable-01` (measurements by a delegated study; the `L-16004` counterexample re-verified independently here)
Reviewing agents: —
Created: 2026-07-31
Last updated: 2026-07-31
Dependencies: `L-16004` and its new SCOPE CAUTION; `O-16004`§5; `O-16007`
Scope: synthetic pole-sum Loewner forms, $4\le N\le24$, $M\le100$ poles, $\Delta=1.5$
Related counterexample candidates: bears directly on the feasibility of any of them

---

> ## SCOPE, after the PR #173 second-pass review
>
> Two limitations, both accepted:
>
> 1. **This is a fixed-residue model.** Every pole here carries a constant residue $a_k$. `T-16002` shows the actual Weil packet carries $a_c(\gamma)=(L/\pi^{2})\sin^{2}(\pi\Delta\gamma)$, and — decisively — that this factor is part of the analytic packet and must be **continued** when the zero leaves the line, becoming $-\sinh^{2}$ at an integer resonance. The model below never varies the residue at all. It therefore measures **masking and conditioning in a synthetic Loewner form**, which is a real and useful thing to measure, but it is **not** the sensitivity of the arithmetic Weil form to an off-line zero. Every "$\lvert\operatorname{Re}\rho-\tfrac12\rvert$" column should be read as a property of the model, not of $\zeta$.
> 2. **Its inertia routine is one of the five that carried the $1\times1$-pivot defect** (returns $(0,0,2)$ on a matrix of true inertia $(1,1,0)$). Re-running L-16004's SCOPE-CAUTION table with a $2\times2$-capable congruence reproduces every row identically, so **that table is unaffected**; the $\delta_c$ bisections have not all been re-run and should be treated as provisional.
>
> What survives unqualified: the *conditioning* measurements ($\log_{10}\operatorname{cond}\approx4.0N+10$), the observation that sensitivity and threshold-readability trade against each other, and §2's scope caution against `L-16004`(ii).

## 0. The question, and why it is the right one

Every counterexample front in this project that runs through Weil positivity implicitly assumes that if a zero were off the critical line, a finite computation would *notice*. This measures that assumption. The model is the pure zero-side Loewner form: real poles at $\pm\mu_k=\pm\Delta\gamma_k$ with unit residues, and one zero displaced off the line.

The displacement is not arbitrary. With $\psi_W(x)=\frac1\pi\operatorname{Im}\sum_\rho(s-\rho)^{-1}$, $s=\tfrac12+ix/\Delta$, a zero $\rho=\beta+i\gamma$ puts poles of $\psi_W$ at $x=\Delta\gamma-i\Delta(\beta-\tfrac12)$, and the functional equation forces the quadruple $\{\beta\pm i\gamma,1-\beta\pm i\gamma\}$. So the right perturbation is a **symmetric quadruple** at $\pm\mu_*\pm id$ with $|\operatorname{Re}\rho-\tfrac12|=d/\Delta$. That is what was used.

## 1. The result

Zeta profile, $\Delta=1.5$, $M=20$ poles, displaced pole $=\gamma_1$ ($\mu_*=21.2021$). Inertia by Bunch–Parlett symmetric-indefinite congruence — **not** `eigsy`, per `O-16004`'s erratum — with $\lambda_{\min}$ and thresholds obtained by *logarithmic* bisection on the inertia. HIGH-PRECISION FLOAT, dps $=40+6N$; the $N=8$ and $N=14$ rows were recomputed at doubled dps with every printed digit identical.

| $N$ | $\log_{10}\operatorname{cond}$ | $\delta_c$ (true threshold) | $\lvert\operatorname{Re}\rho-\tfrac12\rvert$ at $\delta_c$ | $\delta_{\det}(16)$ (float64) | $\lvert\operatorname{Re}\rho-\tfrac12\rvert$ float64 can see | blind-band ratio |
|---|---|---|---|---|---|---|
| 4 | 23.0 | $4.399\times10^{-2}$ | $2.93\times10^{-2}$ | $4.463\times10^{-1}$ | $2.98\times10^{-1}$ | $1.0\times10^{1}$ |
| 6 | 32.7 | $2.784\times10^{-4}$ | $1.86\times10^{-4}$ | $2.267\times10^{-1}$ | $1.51\times10^{-1}$ | $8.1\times10^{2}$ |
| 8 | 41.8 | $6.502\times10^{-7}$ | $4.34\times10^{-7}$ | $1.196\times10^{-1}$ | $7.97\times10^{-2}$ | $1.8\times10^{5}$ |
| 10 | 50.7 | $5.240\times10^{-10}$ | $3.49\times10^{-10}$ | $3.296\times10^{-2}$ | $2.20\times10^{-2}$ | $6.3\times10^{7}$ |
| 12 | 59.5 | $1.650\times10^{-13}$ | $1.10\times10^{-13}$ | $1.259\times10^{-2}$ | $8.39\times10^{-3}$ | $7.6\times10^{10}$ |
| 14 | 68.4 | $1.578\times10^{-17}$ | $1.05\times10^{-17}$ | $4.069\times10^{-3}$ | $2.71\times10^{-3}$ | $2.6\times10^{14}$ |

**Read the two middle groups together.** At $N=14$ the form *mathematically* stops being positive definite once $\operatorname{Re}\rho-\tfrac12$ exceeds about $10^{-17}$ — a remarkably sharp criterion. But a float64 computation of the same matrix notices nothing until $\operatorname{Re}\rho-\tfrac12$ exceeds about $3\times10^{-3}$ — a violation so gross that ordinary zero-finding would have found it long ago. **The gap is 14 orders of magnitude and it widens with $N$.**

The reason is that at $\delta_c$ the created eigenvalue is, by construction, at the conditioning floor: $\lambda_{\min}$ sweeps continuously from $\lambda_{\min}(0)$ down through zero, so near the crossing the signal is smaller than $\lambda_{\max}/\operatorname{cond}$. An observer carrying $u$ significant digits resolves it only if

$$u>\log_{10}\operatorname{cond}(Q)\approx4.46\,N+5.5 .$$

Confirmed directly: the $\delta_{\det}(50)$ column equals $\delta_c$ exactly for $N=4,6,8$ (where $\log_{10}\operatorname{cond}=23.0,32.7,41.8<50$) and departs from it precisely when the conditioning crosses 50, at $N=10,12,14$.

> ## ERRATUM, same day — §1's headline was half wrong, and the correction matters
>
> I first wrote: *"raising $N$ makes the criterion more sensitive in exact arithmetic and simultaneously more useless in fixed precision; the two effects diverge."* **The second half does not survive extending the range.**
>
> Every row of the table above has $\mu_*/N\ge1.5$ — the perturbed pole sits **outside** the node band at every $N$ sampled. With $\Delta=1.5$ and $\mu_1=21.2$, the band is only crossed at $N\approx21$. Extending to $N=24$ (at $M=60$, since $M=20$ makes $Q$ exactly singular for $N\ge20$ — see §3) crosses it:
>
> | $N$ | $\mu_1/N$ | $\log_{10}\operatorname{cond}$ | $\delta_c$ | $\delta_{\det}(16)$ | $\lvert\operatorname{Re}\rho-\tfrac12\rvert$ float64 can see | blind ratio |
> |---|---|---|---|---|---|---|
> | 8 | 2.650 | 41.03 | $1.476\times10^{-6}$ | $1.306\times10^{-1}$ | $8.71\times10^{-2}$ | $8.85\times10^{4}$ |
> | 10 | 2.120 | 49.44 | $2.182\times10^{-9}$ | $3.987\times10^{-2}$ | $2.66\times10^{-2}$ | $1.83\times10^{7}$ |
> | 12 | 1.767 | 57.74 | $1.202\times10^{-12}$ | $1.390\times10^{-2}$ | $9.26\times10^{-3}$ | $1.16\times10^{10}$ |
> | 14 | 1.514 | 65.61 | $3.948\times10^{-16}$ | $4.371\times10^{-3}$ | $2.91\times10^{-3}$ | $1.11\times10^{13}$ |
> | 16 | 1.325 | 73.53 | $4.165\times10^{-20}$ | $1.003\times10^{-3}$ | $6.68\times10^{-4}$ | $2.41\times10^{16}$ |
> | 18 | 1.178 | 81.12 | $1.873\times10^{-24}$ | $1.128\times10^{-4}$ | $7.52\times10^{-5}$ | $6.03\times10^{19}$ |
> | 20 | 1.060 | 88.87 | $1.178\times10^{-29}$ | $4.477\times10^{-6}$ | $2.98\times10^{-6}$ | $3.80\times10^{23}$ |
> | 22 | **0.964** | 97.56 | $3.085\times10^{-36}$ | $4.031\times10^{-8}$ | $2.69\times10^{-8}$ | $1.31\times10^{28}$ |
> | 24 | **0.883** | 104.78 | $2.762\times10^{-41}$ | $1.012\times10^{-8}$ | $6.75\times10^{-9}$ | $3.67\times10^{32}$ |
>
> **The honest verdict is a split, and the two halves answer different questions.**
>
> - **The blind band widens monotonically and shows no sign of turning over**: $8.9\times10^{4}$ at $N=8$ to $3.7\times10^{32}$ at $N=24$. *Locating the exact threshold in fixed precision is hopeless and getting worse.* That half stands.
> - **But absolute float64 sensitivity improves substantially**, and I was wrong to say otherwise. $\delta_{\det}(16)$ falls 5.5 orders of magnitude between $N=14$ and $N=24$, accelerating from about 0.5 decades per $\Delta N=2$ to about 2.0 across the band crossing. In physical units a float64 computation at $N=24$ detects $\lvert\operatorname{Re}\rho-\tfrac12\rvert\approx7\times10^{-9}$, not the $3\times10^{-3}$ my $N\le14$ table suggested.
>
> So "detecting a sufficiently off-line zero at all" is **not** hopeless and improves with $N$ — though $7\times10^{-9}$ at $\gamma_1$ is still far weaker than what direct zero-finding already certifies, so the practical conclusion for a counterexample search is unchanged.
>
> Revised fits over $8\le N\le24$ at $M=60$: $\log_{10}\operatorname{cond}=9.68+3.976N$ (rms 0.31), i.e. **about $4.0N+10$ digits** rather than the $4.46N+5.5$ quoted above; and $\log_{10}\delta_c=-0.373-0.203N-0.0618N^{2}$ (rms 0.31, versus 1.48 for a straight line), confirming super-geometric decay over a doubled range. The $M=20$ quadratic predicted the $M=60$, $N=16$ value to 0.09 decades.
>
> **Caveat on the last two rows.** $\lambda_{\max}$ jumps from 1.83 to 27.7 between $N=20$ and $N=22$ because node 21 sits only $0.2021$ from $\mu_1=21.2021$ — a node–pole near-collision that inflates the $10^{-16}\lambda_{\max}$ threshold exactly across the crossing. The $N=22\to24$ step in $\delta_{\det}(16)$ is 0.6 decades against 2.0 for $N=20\to22$. **Reading a smooth law through the crossing would be over-interpretation**; a finer sweep with the node lattice offset relative to $\mu_1$ is needed to separate the effect from the artefact.

**What does survive as the qualitative lesson.** A second profile (uniform ladder, well conditioned, $\log_{10}\operatorname{cond}\approx7$) shows the mirror image of the zeta profile: there float64 resolves the true threshold *perfectly* — $\delta_{\det}(16)=\delta_{\det}(30)=\delta_{\det}(50)=\delta_c$ exactly — but the threshold is coarse ($\delta_c\approx1.6\times10^{-3}$ at $N=4$, and $5.6\times10^{-1}$ at $N=6$ for $\mu_*=7.854$). Compare the zeta profile at $N=14$: $\delta_c=1.6\times10^{-17}$ but 68 digits needed to see it.

> **Sensitivity and readability trade against each other.** Configurations in which the form is exquisitely sensitive to an off-line zero are exactly those so ill-conditioned that no fixed-precision computation can read the answer; configurations float64 can read have a coarse threshold. **No regime with both was found** — but note this is a statement about the *threshold*, not about detection-at-all, which is where I over-claimed.

Incidentally this also reproduces `O-16004`§5's empirical $\lambda_{\min}\sim10^{-4.5N}$ for the *genuine* arithmetic matrix, here as $\log_{10}\lambda_{\min}=-6.42-4.4626N$ (rms 0.21) on a purely synthetic model with no arithmetic blocks at all. That suggests the conditioning collapse is driven by the pole geometry rather than by the primes.

## 2. The correction to `L-16004`, which is the most important part

`L-16004`(ii) says a nonreal conjugate pair contributes a signature-$(1,1)$ block, hence a negative eigenvalue. **That is correct in `L-16004`'s own setting** — exactly $2N$ poles in dimension $2N+1$, where a rank count leaves the negative direction uncoverable. **It is false in the over-determined regime**, and $\psi_W$ — poles at every zeta zero, finitely many nodes — is squarely in the over-determined regime.

I re-verified this rather than taking it on report (`experiments/X-16003-source-atlas/overdet.py`, dps 120). Real ladder $\mu_k=k\pi/2$, $k=1..20$, plus one nonreal quadruple at $\pm\mu_*\pm id$:

| $N$ | dim | $\mu_*$ | $\mu_*/N$ | $d=0.1$ | $d=1$ | $d=10$ |
|---|---|---|---|---|---|---|
| 4 | 9 | 7.854 | 1.96 | $(9,0,0)$ | $(9,0,0)$ | $(9,0,0)$ |
| 6 | 13 | 12.566 | 2.09 | $(13,0,0)$ | $(13,0,0)$ | $(13,0,0)$ |
| 8 | 17 | 31.416 | 3.93 | $(17,0,0)$ | $(17,0,0)$ | $(17,0,0)$ |
| 8 | 17 | 1.571 | 0.20 | $(15,2,0)$ | $(15,2,0)$ | $(15,2,0)$ |

Positive definite with a nonreal quadruple present, over four decades of displacement. The nonreal pair is seen only when it sits near or inside the node band (roughly $\mu_*/N\lesssim1.5$ here) and moves $\lambda_{\min}$ by under $1\%$ outside it.

**So "one off-line zero must break positivity of a finite Weil matrix" does not follow from `L-16004`(ii).** A scope caution has been added to that lemma. Any counterexample search resting on the implication needs its own argument for it.

## 3. Other things that were tried and failed, recorded because they were

- **Refuted prediction: $\delta_c\sim\sqrt{\lambda_{\min}}$.** Since the perturbation enters at $O(d^2)$, the natural guess is $\delta_c\approx\sqrt{\lambda_{\min}/\lVert B\rVert}\sim10^{-2.2N}$. Measured $\delta_c$ exceeds that by $1.5\times10^{10}$ at $N=4$ rising to $9.3\times10^{16}$ at $N=12$, and $\log\delta_c$ fits a **quadratic** in $N$ ($-0.53N-0.056N^2$, rms 0.012; a straight line gives rms 0.56). The error is in the direction that makes detection *harder*, not easier. Cause: eigenvector alignment, not the naive perturbation size.
- **Failed convergence check, and it is not minor.** The brief required checking that $\ge20$ poles suffice. **It does not.** From $M=20$ to $M=100$, $\delta_c$ rises by $\times2.6$ ($N=8$) and $\times5.1$ ($N=10$), still creeping up by 5–7% per step at $M=100$; $\lambda_{\min}(0)$ moves by $\times8$ and $\times33$. **All absolute constants in §1 are therefore unconverged and low by roughly half an order of magnitude.** What is stable is the $N$-scaling: the exponent at $M=20$ agrees with $M=40$ to about 6%, so the slopes and ratios in §1 — which is all the conclusion uses — survive.
- **A necessary sanity condition.** With $M\le N$ the form is singular by rank count and every reported $\lambda_{\min}$ and $\delta_c$ is a precision floor rather than a spectral fact. One row was discarded for this. **Any run of this kind must satisfy $M>N$.**
- **The signal is non-monotone in $d$**, peaking near $d\approx0.5\mu_*$. So a search that scans *small* displacements is looking in the worst place; if the goal is to falsify positivity numerically, large displacements are far more efficient — though they correspond to zeros nowhere near the critical strip, which is not what anyone wants.

## 4. The mechanism, which turns out to be exact — and explains the refuted prediction

Expanding $Q(d)=Q(0)+d^{2}B+O(d^{4})$ with $B=-a\sum_{\pm\mu_*}\big[\ell'\ell'^{\mathsf T}+\tfrac12(\ell\ell''^{\mathsf T}+\ell''\ell^{\mathsf T})\big]$, the threshold is $\delta_c^{2}=1/\rho$ with $\rho$ the largest eigenvalue of $-Q_0^{-1/2}BQ_0^{-1/2}$. Measured against the bisected $\delta_c$:

| $N$ | $\delta_c$ (bisection) | $\delta_c$ (quadratic model) | rel. diff | $\sqrt{\lambda_{\min}/\lambda_{\max}}$ | ratio |
|---|---|---|---|---|---|
| 4 | $4.39911372\times10^{-2}$ | $4.39686431\times10^{-2}$ | $5.1\times10^{-4}$ | $3.01\times10^{-12}$ | $1.46\times10^{10}$ |
| 6 | $2.78398964\times10^{-4}$ | $2.78398951\times10^{-4}$ | $4.6\times10^{-8}$ | $4.59\times10^{-17}$ | $6.07\times10^{12}$ |
| 8 | $6.50202521\times10^{-7}$ | $6.50202521\times10^{-7}$ | 0 (all digits) | $1.33\times10^{-21}$ | $4.90\times10^{14}$ |
| 10 | $5.23981422\times10^{-10}$ | $5.23981422\times10^{-10}$ | 0 (all digits) | $4.51\times10^{-26}$ | $1.16\times10^{16}$ |
| 12 | $1.65020110\times10^{-13}$ | $1.65020110\times10^{-13}$ | 0 (all digits) | $1.78\times10^{-30}$ | $9.26\times10^{16}$ |

So $\delta_c$ is governed **entirely** by the $O(d^{2})$ term, exactly at $N\ge8$. That also explains the clean weight law: scaling the perturbed pole's residue gives $\delta_c\propto a_*^{-1/2}$ **exactly**, to all seven printed digits over four decades — and $\lambda_{\min}(0)$ is *identical* across those rows, i.e. the starred pole contributes nothing to the conditioning floor, only to the signal.

**And it explains why the natural prediction fails by sixteen orders of magnitude.** $\delta_c$ exceeds $\sqrt{\lambda_{\min}/\lambda_{\max}}$ by $10^{10}$ to $10^{17}$. The cause is **alignment**: $B$'s negative direction is $\ell'(\mu_*)$, a smooth vector living overwhelmingly in the *top* eigenspace of $Q_0$, whereas $\lambda_{\min}$'s eigenvector is highly oscillatory. The overlap is tiny, so the perturbation is far less efficient at breaking positivity than any norm comparison suggests. This is the crux and it deserves a proof.

**The signal is bounded and non-monotone.** As $d\to\infty$, $\ell(\mu_*\pm id)\to0$, so $Q(d)\to Q(0)$ with the starred terms *deleted* — which is PSD again. There is therefore a best displacement (near $d\approx0.5\mu_*$) and a hard **ceiling** on the signal. Peak $\lambda_{\min}$ over $d\in[10^{-3},10^{4}]$, expressed as digits needed:

| $N$ | $\gamma_1$ | $\gamma_3$ | $\gamma_4$ | $\gamma_7$ | $\gamma_{10}$ |
|---|---|---|---|---|---|
| 6 | 3.99 | 13.20 | 14.44 | — | 25.48 |
| 10 | 3.06 | 10.45 | 11.90 | — | 20.40 |
| 14 | 2.33 | — | 11.15 | 15.83 | — |

An observer with fewer digits than the entry can **never** detect that zero being off-line, at any displacement whatsoever. The ceiling degrades about 3.5–4 orders of magnitude per zero index, so only the first two or three zeros are float64-visible — but it *improves* with $N$, unlike the $\delta_c$ obstruction. Two negative eigenvalues also appear at *different* thresholds, $(17,0,0)\to(16,1,0)\to(15,2,0)$, which is what `L-16004`(iv) implies: $Q$ commutes with parity, so the even and odd sectors cross independently.

## 5. A trap I fell into twice, worth more than most of the tables

Both the discarded $N=12$, $M=10$ row and an entire first $N\ge20$ sweep at $M=20$ produced *spectacular* thresholds — $\delta_c$ below $10^{-56}$, $10^{-62}$, $10^{-68}$. All worthless. With $M$ pole pairs, $Q$ has only $2M$ rank-one terms and is **exactly singular** once $2M<2N+1$; measured inertia was $(40,0,1)$, $(40,0,5)$, $(40,0,9)$ at $N=20,22,24$. Then $\delta_c=0$ mathematically and the computation reports an impressive-looking precision floor instead.

Both times the numbers looked like a dramatic result. **The free check that catches it: assert the unperturbed inertia is exactly $(\dim,0,0)$ on every row.** This is the same species of error as the leading-principal-minor mistake recorded in `L-16004`, and the same species as the $0/0$ normalisation that produced `L-16006`'s §4 erratum. A necessary condition for any run of this kind is $M>N$.

## Gap audit

1. **This is a caricature, not the Weil matrix.** No archimedean block, no prime sum, no pole/$\kappa$/$J$ terms, unit residues, truncated pole set. Conclusions transfer to X-0001's $Q_W$ only as heuristics. The agreement of the $\lambda_{\min}$ exponent with `O-16004` is suggestive, not evidential.
2. **Nothing certified.** No interval or ball arithmetic; the congruence is exact only to working precision. The dps-doubling checks are strong self-consistency evidence, not proof.
3. **Constants are not converged** (§3). Only slopes and ratios should be quoted.
4. Untested: $N>24$, $M>100$, $\Delta\ne1.5$, non-unit residues, and — importantly — **several simultaneous off-line zeros**. `O-16004`§4's rank-one interlacing remark suggests that case may behave differently.
5. The band crossing in the §1 ERRATUM is sampled at only **two** points ($N=22,24$) and is contaminated by a node–pole near-collision. The split verdict's second half rests on those two rows plus the trend from $N=16..20$; it should be re-run with the node lattice offset before being relied on.
6. `O-16007`'s residue law says the true residues are $a(\gamma)=(\log c/\pi^2)\sin^2(\gamma\log c/2)$, **not** the unit residues used here. Redoing §1 with the measured residue profile is the obvious refinement and might move the constants materially, since $a(\gamma)$ varies by two orders of magnitude across cutoffs.

## Suggested next attack

0. **Re-run the band crossing** ($N=20..28$) with the node lattice offset relative to $\mu_1$, to separate the real improvement in float64 sensitivity from the near-collision artefact. This is the one place where the ERRATUM's second half could still be wrong.
1. Repeat §1 on the **actual** $Q_W$ by inserting a synthetic off-line zero into its zero-side source, and check whether the $4.5N$-digit rule and the widening blind band survive the arithmetic blocks.
2. Redo §1 with `O-16007`'s residue law in place of unit residues (gap audit 5). These two claims were produced independently this session and have not been combined.
3. Prove the alignment fact behind the refuted $\sqrt{\lambda_{\min}}$ prediction: bound the overlap of $\ell'(\mu_*)$ with the bottom eigenspace of the unperturbed $Q$. A clean asymptotic there should explain the quadratic-in-$N$ shape of $\log\delta_c$.
4. **Read §1 as a budget constraint on the whole positivity front.** If a counterexample search intends to detect an off-line zero at height $\gamma$ through finite Weil positivity, it must carry roughly $4.5N$ significant digits, and $N$ must be large enough that $\gamma\Delta$ is inside the sensitive band. Those two requirements pull in opposite directions and someone should cost them out before more compute is spent.
