# Session report — `claude-fable-01`, 2026-07-31

Agent: `claude-fable-01`
Issue: #151 (Exact Weil-radical Hermite bridge for the positive RH program); relates to PR #158, #157, #164
Branch: `claude/agentic-polymath-riemann-jjj23a`
Model: `claude-fable-5`

---

## Starting hypothesis

The task was to advance the programme of the working note *"A Cofinal Finsler–Bézoutian Completion Criterion for the Riemann Hypothesis"* (PR #158), which reduces RH to one cofinal finite positivity statement and names that statement as the sole remaining task.

My opening hypothesis, formed from the note alone, was that the remaining task might be **vacuous**: the note's Finsler condition quantifies over the isotropic cone of $B_p=\operatorname{diag}(\eta_i/p_i)-\eta\eta^{\mathsf T}$, and for a strictly positive target with $\eta=\mathbf 1$ one has $x^{\mathsf T}B_px=\sum x_i^2/p_i-(\sum x_i)^2\ge0$ by Cauchy–Schwarz, so the cone is empty. Since the exact radical target of `L-15101` is built from Pólya's strictly positive $\Phi$, every target looked positive.

**That hypothesis was wrong**, and finding out exactly *why* turned out to be the most useful thing in the session.

---

## Approaches attempted

1. **Independent re-derivation of the `L-15101` target's analytic normalization** (Hermite decomposition, Mellin transform, Poisson summation), rather than importing it.
2. **The Cauchy–Schwarz collapse**, developed to a full lemma and verified in exact rational arithmetic on a minimal instance.
3. **Retrieval and close reading of the primary source**, Connes–van Suijlekom arXiv:2511.23257 — which refuted (2)'s applicability.
4. **Reconstruction of the correct finite target** from the corrected interface, and an exact-arithmetic census of its real-root behaviour.
5. **Gap-parity analysis**, converting the finite gate into a combinatorial condition on the target's sign pattern.
6. **Controlled experiments** on families where the answer is known independently, to separate mechanism from artefact.

---

## New results

### Proved

- **`L-16001`** — The exact Weil-radical target of `L-15101` is Pólya's function, and the transform normalization in `L-15101.7` is wrong by a factor $4$: with $h(x)=\tfrac\pi2x^2(2\pi x^2-3)e^{-\pi x^2}$ and $k(u)=u^{1/2}\sum_{n\ge1}h(nu)$,
  $$h=\tfrac1{64}\psi_4-\tfrac3{16}\psi_0,\qquad Mh(s)=\tfrac{s(s-1)}8\pi^{-s/2}\Gamma(s/2),\qquad \widehat k(z)=\tfrac14\,\Xi(z).$$
  With $K(t)=k(e^t)$ and $\Phi:=4K$, $\Xi(z)=\int_{\mathbb R}\Phi(t)e^{izt}dt$. The dictionary to the classical (Titchmarsh) kernel is $\Phi_{\mathrm{cl}}(u)=2K(2u)=\tfrac12\Phi(2u)$ — a factor **and** a change of variable; the de Bruijn–Newman parameter is calibrated to $\Phi_{\mathrm{cl}}$ and does not transfer verbatim. Verified to 32–40 digits including complex $z$.

- **`L-16002`** — For any one-signed target with $\eta=\mathbf 1$: $B_p\succeq0$ with $\ker B_p=\mathbb Rp$; the Finsler isotropic cone is empty; and a feasible rational $c$ exists for **every** special $Q$, namely any $c>-\mu_{\min}$ of the pencil. This confirms working-note Lemma 4.2 in the corner $n_-=0$ and agrees exactly with Connes–van Suijlekom Appendix B.1.

- **`L-16003`** — *Gap parity.* On each node gap the number of roots of the interpolation polynomial is odd if the adjacent target coordinates share a sign and even otherwise. Hence $\#\{\text{real roots}\}\ge\#\{\text{same-sign adjacent pairs}\}$, with equality forced (and interlacing) in the one-signed case. Transported through `O-16001`, this says the finite gate is a condition on how well the sampling **resolves the zeros of $\Xi$**: an unresolved close pair contributes no sign change and forfeits real roots. The failure mode is Lehmer's phenomenon at the sampling scale.

### Established by reading the primary source

- **`O-16001`** — The Connes–van Suijlekom coordinates $\xi_j$ are Fourier **coefficients**, not point samples; $\eta=\sum_je_j$ is verbatim all-ones; the finite transform is the windowed cardinal series $\widehat\xi(z)=2e^{-iz/2}\sin(z/2)\sum_j\xi_j/(z-2\pi j)$, **not** $\sum_j\xi_je^{ijz}$. Consequently the finite target is
  $$\xi_j=(-1)^{j}F(2\pi j)\approx(-1)^{j}\,\Xi(2\pi\alpha j),$$
  the samples of $\Xi$ itself, which alternate in sign. Independently confirmed against the production chain: `T-15103` §4 yields $\eta_np_n=(-1)^n\Xi(\lambda_n)/(4\sqrt{2\ell})$, with measured inertias $(19,18)$, $(104,97)$, $(141,140)$ — maximally indefinite.

### Certified computational

- **`R-16001`** — Exact Sturm census (150-digit evaluation, 100-digit rationalization, exact rational arithmetic in every decision path, counts stable at 20/30/40/50/60 digits). The finite gate passes **only above a sharp critical scale**
  $$\alpha_c\in(1.064404,\ 1.064417),$$
  and the bisection returns the *same* interval for $N=6,8,10,14,20,26,30$: the threshold does not move with the level. Below it the deficit is exactly $4$ throughout $\alpha\in[0.8,1.05]$, $N=4..20$, rising to $12$ at $\alpha=0.5$, $N=34..44$. The obstructing conjugate pairs depend only on $\alpha$, not on $N$, and survive hard, Fejér, Hann, Gaussian and Tukey tapering unchanged.

  **The consequence.** Hypothesis (8) of the note's Theorem 3.1 forces $\alpha\to0$; hypothesis (9) forces $\alpha>\alpha_c$. At $\alpha_c$ the discarded mass is a fixed fraction of $\int\Phi=\Xi(0)$, not $o(1)$. For this target family the two hypotheses are **incompatible**, at every level and along every schedule.

  **The mechanism.** Passing requires the target transform to carry one zero per sample gap — critical (Nyquist) density, per `L-16003`. Above $\alpha_c$ the window is so short that $F$ is a sinc-like bump transform with exactly that density. Below $\alpha_c$ — that is, as soon as $F$ genuinely converges to $\Xi$ — the sample gaps nearest the origin contain no zero of $F$ at all, since $\Xi$'s first zero is at $w=14.134\ldots$, and each empty gap forfeits a real root.

---

## Candidate counterexamples

**None.** Nothing in this session is evidence for or against RH. The nonreal roots found sit at $|{\rm Im}\,w|\ge1.56$, far outside the strip $|{\rm Im}\,w|<\tfrac12$ where such a claim would even be meaningful, and they move *away* from the real axis as the approximation improves — the benign behaviour Hurwitz predicts.

---

## Certified computations

- `experiments/X-16001-finsler-cone-collapse/` — exact rational verifier, standard library only, all propositions pass; certificate `certificates/collapse.json`, sha256 `2eacce19f8a8…`.
- `experiments/X-16002-cvs-sampled-target-census/` — the census, with reproduction instructions.

---

## Failed approaches (preserved deliberately)

1. **The positivity collapse.** "Pólya's $\Phi>0$, so the finite target is positive, so the Finsler cone is empty, so the cofinal task is vacuous." **False**, because the CvS coordinates are Fourier coefficients, not values. Recorded in full as `O-16001`(e) so no later agent repeats it. `L-16002` is retained as correct mathematics with its scope explicitly restricted.

2. **A zero-counting threshold law.** I predicted $N_0(\alpha)=\alpha^{-1}e^{1+1/\alpha}$ from matching $\deg P=2N$ against the Riemann–von Mangoldt count in the sampled window, predicting first passes at $(\alpha,N)=(1.0,6)$ and $(0.8,10)$. **Wrong**: the exact census shows a residual deficit of $4$ that the count argument does not see, and the true threshold is in $\alpha$ alone and is $N$-independent. The count argument is a correct *lower* bound only (`L-16003`(ii)); the equality strengthening is false, refuted in 13 of 18 sampled-$\Xi$ cases.

3. **Tapering the truncation.** Five taper families all left the deficit at exactly $4$. The obstruction is a property of the scale, not of the cutoff shape.

4. **A `float64` eigenvalue computation** of $D'=D-|D\xi\rangle\langle\eta|$ reported nonreal roots at $|{\rm Im}\,w|\approx0.43$, *inside* the RH strip. At 150 digits these vanish entirely — the sampled coefficients span a dynamic range of $10^{-21}$ or worse. Preserved as a live instance of README §8's warning against "confusing a discrepancy between implementations with a mathematical contradiction". **Do not use double precision for this computation.**

---

## Potential errors

- `L-16001`(f) (positivity of $\Phi$) is **imported** as classical, not re-proved here.
- `R-16001`'s $N$-independence of $\alpha_c$ is an observation over seven levels, not a theorem; no monotonicity in $\alpha$ is proved.
- **CvS parity was not verified at passing levels.** Theorem 5.6 demands a matrix of form (11) with *odd* source and *even* diagonal. A "PASS" in the census is necessary for the note's gate but possibly not sufficient. This is the most important open check on the positive side.
- `L-16003`(v) and `R-16001` inherit the target identification of `O-16001`, which — although now cross-checked against `T-15103` §4 by an independent audit — should be re-derived by a reviewer.
- The "$\approx10\%$ discarded mass" figure is a rough integral estimate; only the qualitative statement (fixed positive constant, not $o(1)$) is rigorous.

---

## Files changed

```text
claims/lemmas/L-16001-polya-identification-and-normalization.md
claims/lemmas/L-16002-universal-slope-positivity.md
claims/lemmas/L-16003-gap-parity-and-sign-change-bound.md
claims/observations/O-16001-cvs-coordinates-are-fourier-coefficients.md
claims/refutations/R-16001-sampled-target-scale-obstruction.md
experiments/X-16001-finsler-cone-collapse/
experiments/X-16002-cvs-sampled-target-census/
reports/claude-fable-01/2026-07-31-151-cvs-sampled-target-scale-obstruction.md
```

## Claims affected

- **Added:** `L-16001`, `L-16002`, `L-16003`, `O-16001`, `R-16001` (all `PROPOSED`), `X-16001`, `X-16002`.
- **Erratum requested:** `L-15101.7` asserts $\widehat k=\Xi$; the correct identity is $\widehat k=\tfrac14\Xi$. Harmless for zero location, wrong as an identity, and must be corrected in any quantitative error budget derived from it.
- **Confirmed, not weakened:** `L-15107` (Lemma 4.2 corner case), `L-15108` (independently re-derived against CvS Lemmas 5.2/5.3/5.8/5.9 and found correct), `L-15109`, `T-15103`, `T-15104`, and the note's Theorem 3.1 as an implication.
- **Scope narrowed:** `T-15102` and `T-15104` remain valid implications, but `R-16001` shows their hypotheses are not jointly satisfiable by the target sequence the repository currently constructs.

---

## Recommended next actions

1. **Verify CvS parity at a passing level** ($\alpha=1.1$, $N=6$ is the cheapest). Construct the special $Q$ explicitly via `L-15108` §4, and check the source is odd and the diagonal even. If parity fails, the "PASS" region is void and `R-16001` strengthens further; if it holds, the project has its first production-level pass of the finite gate, at a scale where the transform does not converge — which is itself worth recording precisely.
2. **Prove the threshold.** The mechanism suggests $\alpha_c$ solves a clean extremal problem: for $G=\Phi|_{[-T,T]}$, find the largest $T$ such that $\widehat G$ has a zero in every interval of length $\pi/T$. The prediction is $T_c=1/(2\alpha_c)\approx0.4697$.
3. **Prove the converse half of `L-16003`** — that the roots not forced by gap parity are nonreal. An argument-principle or Jensen count on $\widehat\xi$ (exponential type $\tfrac12$, hence linear zero density) is the natural route. This would turn the census into a theorem.
4. **Redesign rather than repair.** `L-16003`(iv) states the requirement exactly: the target transform must have one zero per sample gap while approximating $\Xi$. Since $\Xi$ has no zeros below $w=14.13$, the low-frequency gaps must be filled by something other than $\Xi$'s own zeros. Identifying what can fill them without destroying convergence is the sharpest available form of the remaining task — far more specific than "prove the cofinal positivity estimate".
5. Bootstrap `CURRENT_STATE.md`, `CLAIMS.md`, `OPEN_PROBLEMS.md`, `CANDIDATES.md`, `NEGATIVE_RESULTS.md` — none exists on any branch.

---

## Organizational improvement ideas

1. **Interface claims deserve first-class status.** The single most consequential finding of this session is not a theorem but an *interface fact*: whether $p$ denotes samples or Fourier coefficients. Nothing in PR #158 states which, and the two readings have opposite sign structure, with one making the whole criterion vacuous. I suggest a mandatory **`NOTATION.md` interface table** (already in README §16's recommended structure but not yet created), and a required "coordinates and normalization" line in every claim header naming which space each vector lives in.

2. **Record refuted leads, not just refuted claims.** README §7 has statuses for claims; it has no home for a *line of reasoning* that was pursued and killed. The positivity collapse was attractive, took real work to kill, and would recur. I have recorded it inside `O-16001`(e), but a dedicated `NEGATIVE_RESULTS.md` section for "attractive traps" would serve better.

3. **A precision floor for this problem class.** The `float64` run produced apparent nonreal zeros inside the critical strip. Given the repository's mission, a plausible-looking artefact of exactly that shape is the most dangerous possible failure. I suggest a project rule: **any zero-location claim must be produced at $\ge100$ digits and re-verified at a second precision**, and any certificate that cannot state its dynamic range is rejected.

4. **Cheap screening tests belong in the checker.** `L-16002` gives a one-line screen: a one-signed coefficient vector makes the Finsler condition vacuous, so such a level carries no information. `L-16003` gives another: compare the real-root count against the same-sign pair count before doing anything expensive. Both are $O(n)$ and would have saved this session considerable work.

5. **State the logical status of the whole programme up front.** The Laguerre–Pólya class is closed under locally uniform limits, so "there exists a sequence of real-rooted approximants converging to $\Xi$" is *equivalent* to RH, not merely sufficient. Any cofinal hypothesis of that shape is therefore a reformulation, and no purely structural proof of it can exist — genuine arithmetic input is required. Stating this prominently would help agents calibrate where to spend effort.
