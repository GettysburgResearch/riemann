# L-16005 — Hard-window artifact dominance: the truncated coefficients stop being about ζ at j ≈ 2

Claim ID: `L-16005`
Title: Exact error relation for the hard-window target, a rigorous uniform bound, the decay law (**$O(j^{-2})$ on the lattice — see the ERRATUM; (iii)'s sharpness claim was wrong**), and the consequent certification boundary
Status: `PROPOSED`
Authoring agent: `claude-fable-01`
Reviewing agents: — (prompted by audit `O-15104`, points 1 and 3, on PR #173)
Created: 2026-07-31
Last updated: 2026-07-31
Dependencies: `L-16001` (the kernel $\Phi$ and its decay), `O-16001` (the coordinate interface); elementary Fourier analysis
Scope: the **hard-window** target $F(z)=\int_{|t|\le T}\Phi(t)e^{i\alpha zt}dt$, $T=1/(2\alpha)$. Bears directly on `R-16001`, whose census this bounds the validity of.
Related counterexample candidates: none

---

## Statement

Let $\Phi=4K$ be the kernel of `L-16001`, $\Xi(w)=\int_{\mathbb R}\Phi(t)e^{iwt}dt$, and for $\alpha>0$ put $T=1/(2\alpha)$ and

$$\xi^{\mathrm{win}}_j=(-1)^{j}F(2\pi j),\qquad F(z)=\int_{|t|\le T}\Phi(t)e^{i\alpha zt}\,dt .$$

**(i) Exact error relation.** For every $j$,

$$\boxed{\;F(2\pi j)=\Xi(2\pi\alpha j)-E_j,\qquad E_j=2\int_{T}^{\infty}\Phi(t)\cos(2\pi\alpha j t)\,dt.\;}$$

So the hard-window target and the sampled-$\Xi$ target of `R-16001` differ by exactly $E_j$, and the difference is an **absolute** perturbation, uniform in $j$ at leading order.

**(ii) Rigorous uniform bound.** With $U=e^{2T}\ge1$, $C_4=\sum_{n\ge1}n^{4}e^{-\pi(n^{2}-1)}$, $C_2=\sum_{n\ge1}n^{2}e^{-\pi(n^{2}-1)}$,

$$|E_j|\ \le\ \varepsilon(T):=2\!\int_T^\infty\!\Phi\ \le\ 4\left[\frac{\pi^{2}C_4\,U^{5/4}}{\pi-\tfrac54}+\frac{\tfrac32\pi C_2\,U^{1/4}}{\pi-\tfrac14}\right]e^{-\pi U}.$$

The bound uses $\int_U^\infty u^{a}e^{-\pi u}du\le U^{a}e^{-\pi U}/(\pi-a)$ for $0\le a<\pi$, $U\ge1$. It is tight to within a factor $\approx2$ (measured: $T=0.5$, actual $8.32\times10^{-3}$ vs bound $1.59\times10^{-2}$; $T=1.0$, actual $1.255\times10^{-8}$ vs bound $2.200\times10^{-8}$).

> ## ERRATUM to (iii) — the sharpness claim is FALSE on this lemma's own lattice
>
> Raised in the PR #173 second-pass review, adjudicated by independent computation. **The reviewer is right, and the error is worse than "underdetermined": (iii) is contradicted by its own measured table.**
>
> On the hard-window lattice the cutoff and the sampling frequency are locked by the same $\alpha$:
> $$\omega_jT=2\pi\alpha j\cdot\tfrac{1}{2\alpha}=\pi j\ \Longrightarrow\ \sin(\omega_jT)=0,\quad\cos(\omega_jT)=(-1)^{j}\quad\textbf{for every }\alpha .$$
> So the first boundary term — the one (iii) calls "genuinely present" — is **identically zero at every lattice point**. Two integrations by parts give the sharp law
> $$E_j=(-1)^{j}\,\frac{\Phi'(T)}{\pi^{2}\alpha^{2}j^{2}}+O(j^{-4}),\qquad C:=\frac{|\Phi'(T)|}{\pi^{2}\alpha^{2}},$$
> with an alternating sign that (iii) does not mention. **The sharp lattice decay is $O(j^{-2})$, not $O(j^{-1})$.**
>
> **My own table already showed this.** Over $j=4\to40$ at $\alpha=1$, $j|E_j|$ falls by a factor **9.1** while $j^{2}|E_j|$ varies by 10% and converges monotonically from below to $C=0.0371740$ — ratio $0.99925$ at $j=40$, against the two-term prediction $1-1.2033/j^{2}$. Reading only $j=4..12$, as (iii) did, is what hid it. Local slope reaches $1.998$ by $j=40$.
>
> **What survives.** The uniform bound $|E_j|\le2\Phi(T)/(\pi\alpha j)$ **is valid** (never violated in 160 evaluations) — merely wasteful by a factor $j$. And $O(1/j)$ **is** the sharp law for a *general* cutoff: moving $T$ off the lattice ($T=0.7112944\ldots$, irrational multiple) restores it, with $\max_j j|E_j|=5.955\times10^{-4}$ against the predicted $2\Phi(T)/2\pi=5.98\times10^{-4}$.
>
> **So (iii) is a correct theorem about a general cutoff $T$ and a false theorem about the cutoff $T=1/(2\alpha)$ this lemma actually uses.** Not a miscalculation — a failure to substitute the lemma's own hypothesis into its own conclusion. That is the *same* failure mode as `L-16003`(iv), where the statement dropped a hypothesis the proof had carried.
>
> **None of the three downstream conclusions moves**, because every $|E_j|$ in the tables was reproduced to within **0.11%** — the values were right, only their verbal classification was wrong. (iv)'s crossover at $j\approx2$ is set by polynomial-versus-*exponential* decay, so one power of $j$ is irrelevant; (v) uses the $j$-independent $\varepsilon(T)$, which the exponent cannot enter; (vi)'s hard-versus-smooth contrast stands (super-polynomial still beats $j^{-2}$). Three text corrections follow, in the gap audit.
>
> **Four further findings from the adjudication.**
>
> - **A free factor of two.** Substituting $\sin(\omega_jT)=0$ into this lemma's *own* one-step argument gives $|E_j|\le\Phi(T)/(\pi\alpha j)$ — **half** the bound stated in (ii)/(iii), at no cost.
> - **A rigorous $O(j^{-2})$ bound, conditional.** $|E_j|\le|\Phi'(T)|/(\pi^{2}\alpha^{2}j^{2})$ holds **if** $\Phi''\ge0$ on $(T,\infty)$. Grid-verified on $[0.30,5.00]$, but $\Phi''<0$ near the origin, so this is a genuine unproved hypothesis and the bound must not be quoted as rigorous until it is settled. The *asymptotic* does not depend on it.
> - **The sign alternates**, which the review's own expression missed: $\operatorname{sign}(E_j)=(-1)^{j}$ at **all 160** $(\alpha,j)$ pairs tested, no exceptions.
> - **The asymptotic has an onset**, at $\omega_j\gtrsim3\lambda$, i.e. $j\gtrsim3e^{1/\alpha}/\alpha$ — measured onsets $j=4,13,38,83$ at $\alpha=1.0,0.7,0.5,0.4$. Below onset $|E_j|$ is **flat**: at $\alpha=0.4$ it moves only 13% across $j=1..12$.
>
> The crossover index **moves out sharply as $\alpha$ falls** — $j=2,5,10,>12$ at $\alpha=1.0,0.7,0.5,0.4$ — which independently supports (v). And at $\alpha\lesssim0.4$ with small $j$ **neither** power law describes $|E_j|$: it is essentially flat there, because the asymptotic regime needs $j\gtrsim3e^{2}/\alpha$.

**(iii) [SUPERSEDED — see the ERRATUM above] The decay law is only $O(1/j)$, and this is sharp.** A hard cutoff leaves $\Phi$ discontinuous at $t=T$ (it jumps from $\Phi(T)>0$ to $0$). One integration by parts, using that $\Phi$ is monotone decreasing on $(T,\infty)$ so that $\int_T^\infty|\Phi'|=\Phi(T)$, gives

$$|E_j|\ \le\ \frac{2\,\Phi(T)}{\pi\alpha j},$$

and **no further integration by parts improves the order**, because the boundary term does not vanish. Measured at $\alpha=1$: $j\,|E_j|=0.0084,\,0.0060,\,0.0046,\,0.0037,\,0.0031$ at $j=4,6,8,10,12$ — constant up to a slow drift, confirming $O(1/j)$.

**(iv) Artifact dominance.** The true coefficients decay **exponentially**, $|\Xi(2\pi\alpha j)|\sim e^{-\pi^{2}\alpha j/2}$, while $|E_j|$ decays only like $1/j$. Hence there is a small crossover index beyond which the hard-window coefficient is essentially **pure truncation artifact**. Measured at $\alpha=1$, $T=0.5$:

| $j$ | $\lvert E_j\rvert$ | $\lvert\Xi(2\pi\alpha j)\rvert$ | ratio $\lvert E_j\rvert/\lvert\Xi_j\rvert$ |
|---|---|---|---|
| 1 | $7.33\times10^{-3}$ | $1.93\times10^{-1}$ | $0.038$ |
| 2 | $5.22\times10^{-3}$ | $4.98\times10^{-3}$ | $1.05$ |
| 3 | $3.32\times10^{-3}$ | $1.48\times10^{-4}$ | $22.4$ |
| 4 | $2.10\times10^{-3}$ | $1.43\times10^{-7}$ | $1.47\times10^{4}$ |
| 6 | $9.95\times10^{-4}$ | $1.92\times10^{-11}$ | $5.18\times10^{7}$ |
| 10 | $3.67\times10^{-4}$ | $2.38\times10^{-18}$ | $1.54\times10^{14}$ |
| 12 | $2.56\times10^{-4}$ | $2.62\times10^{-23}$ | $9.75\times10^{18}$ |

**The crossover is at $j\approx2$.** Beyond it the hard-window target carries no information about $\zeta$ whatever — and the tail is precisely the part that decides the root count.

**(v) Certification boundary.** A root count for the hard-window target is certified only if it is invariant over the box $\prod_j[\,\Xi(2\pi\alpha j)-\varepsilon,\ \Xi(2\pi\alpha j)+\varepsilon\,]$. Comparing $\varepsilon(T)$ against the smallest coefficient:

| $\alpha$ | $T$ | $\varepsilon(T)$ bound | $\lvert\Xi(2\pi\alpha\cdot10)\rvert$ | certifiable? |
|---|---|---|---|---|
| $1.1$ | $0.4545$ | $3.01\times10^{-2}$ | $4.26\times10^{-21}$ | no |
| $1.0$ | $0.5000$ | $1.59\times10^{-2}$ | $2.38\times10^{-18}$ | no |
| $0.9$ | $0.5556$ | $6.62\times10^{-3}$ | $1.61\times10^{-17}$ | no |
| $0.8$ | $0.6250$ | $1.88\times10^{-3}$ | $5.85\times10^{-15}$ | no |
| $0.7$ | $0.7143$ | $2.71\times10^{-4}$ | $1.14\times10^{-12}$ | no |
| $0.6$ | $0.8333$ | $1.06\times10^{-5}$ | $1.92\times10^{-11}$ | no |
| $0.5$ | $1.0000$ | $2.20\times10^{-8}$ | $7.86\times10^{-9}$ | no |
| $0.4$ | $1.2500$ | $1.17\times10^{-14}$ | $1.43\times10^{-7}$ | **yes** |

**So no hard-window root count at $\alpha\ge0.5$ is certifiable**, and in particular the threshold $\alpha_c\approx1.0644$ of `R-16001` lies deep inside the uncertifiable region. Certification becomes feasible only at $\alpha\lesssim0.4$, i.e. $T\gtrsim1.25$ — exactly the regime not yet computed.

**(vi) Consequence for the production target — with a caveat established by direct test.** `L-15101` specifies a **smooth** cutoff $\chi_L$, not a hard indicator. Asymptotically in $j$ this matters: for a $C^\infty$ cutoff every boundary term in (iii) vanishes and $E_j$ decays faster than any power of $j$. **The hard window is therefore not a harmless stand-in for the production target**, and any transfer of a hard-window computation to it requires an explicit perturbation argument rather than an appeal to proximity.

**But smoothness alone does not rescue certification, and it is not the binding constraint.** Direct comparison at $\alpha=1$, both cutoffs supported in $|t|\le T=0.5$, the smooth one flat on $|t|\le0.25$ and rolling off to $0$ at $T$:

| $j$ | $\lvert E_j\rvert$ hard | $\lvert E_j\rvert$ smooth | $\lvert\Xi(2\pi\alpha j)\rvert$ |
|---|---|---|---|
| 2 | $5.22\times10^{-3}$ | $1.75\times10^{-2}$ | $4.98\times10^{-3}$ |
| 4 | $2.10\times10^{-3}$ | $7.16\times10^{-3}$ | $1.43\times10^{-7}$ |
| 6 | $9.95\times10^{-4}$ | $1.92\times10^{-3}$ | $1.92\times10^{-11}$ |
| 10 | $3.67\times10^{-4}$ | $7.34\times10^{-4}$ | $2.38\times10^{-18}$ |

with $j|E_j|$ approximately constant for **both** ($0.0084,0.0060,0.0046,0.0037$ hard; $0.029,0.012,0.0068,0.0073$ smooth over $j=4,6,8,10$). The smooth error is **larger**, and the crossover of (iv) does **not** move out.

The reason is that the constant in front of the decay is set by the **discarded mass**, not by the smoothness: rolling off from $0.25$ attenuates $\Phi$ where it is still substantial, so more mass is lost than the hard cut at $0.5$ loses. **The design lever is therefore $T$ (equivalently $\alpha$), not the smoothness of the cutoff.** Since $\Phi$ decays doubly exponentially, the roll-off must begin far enough out — which forces $T$ large and $\alpha$ small, converging with the certification boundary $\alpha\lesssim0.4$ of (v) from an independent direction.

*(An earlier version of this item asserted that smoothness "moves the crossover out dramatically". That inference is unsupported at fixed support and is corrected here. The asymptotic-in-$j$ statement stands; the practical inference does not.)*

---

## Motivation

Audit `O-15104` raised two objections to the `R-16001` census (points 1 and 3): that "exact Sturm then certifies the rational surrogate, not the exact coefficient vector", and that "the production claim uses a smooth cutoff/form-core target; the hard indicator is a nearby model unless a directed perturbation transfer is supplied." Both are correct. This lemma converts them from methodological cautions into quantitative statements, and in doing so shows they are **more serious than the audit's phrasing suggests**: the gap is not a matter of a few digits, it is 19 orders of magnitude at $\alpha=1.1$, and the hard-vs-smooth distinction is a difference between $O(j^{-2})$ (per the ERRATUM to (iii); $O(1/j)$ as originally written) and super-polynomial decay.

It also explains, in one mechanism, three separate observations previously recorded as unrelated: why the pass-region roots sit on the sinc lattice (the coefficients there *are* the window indicator's), why a Gaussian control reproduces the identical threshold (any positive bump, hard-truncated, gives the same artifact), and why the sampled and hard-window targets give opposite verdicts at $\alpha=1.0$ (the ratio $|E_j|/|\Xi_j|$ crosses 1 at $j\approx2$).

## Proof

**(i)** is immediate: $\Xi(2\pi\alpha j)=\int_{\mathbb R}\Phi(t)e^{2\pi i\alpha jt}dt$ and $F(2\pi j)=\int_{|t|\le T}$ of the same integrand; $\Phi$ even makes the exponential a cosine and the two tails equal.

**(ii)** For $t\ge T\ge0$ put $u=e^{2t}\ge1$. From `L-16001`(e), $|K(t)|\le\pi^{2}u^{9/4}\sum_n n^{4}e^{-\pi n^{2}u}+\tfrac32\pi u^{5/4}\sum_n n^{2}e^{-\pi n^{2}u}$, and for $u\ge1$, $\sum_n n^{4}e^{-\pi n^{2}u}\le e^{-\pi u}\sum_n n^{4}e^{-\pi(n^{2}-1)}=C_4e^{-\pi u}$, similarly for $C_2$. Substituting $u=e^{2t}$, $dt=du/(2u)$ turns $\int_T^\infty|K|dt$ into $\tfrac12\int_U^\infty(\pi^{2}C_4u^{5/4}+\tfrac32\pi C_2u^{1/4})e^{-\pi u}du$. Finally, with $u=U+v$ and $(1+v/U)^{a}\le(1+v)^{a}\le e^{av}$ for $U\ge1$, $\int_U^\infty u^{a}e^{-\pi u}du\le U^{a}e^{-\pi U}/(\pi-a)$ whenever $a<\pi$; here $a\in\{5/4,1/4\}$. Multiply by $8$ since $\Phi=4K$ and $\varepsilon=2\int_T^\infty\Phi$.

**(iii)** $\int_T^\infty\Phi(t)\cos(\omega t)dt=\bigl[\Phi(t)\tfrac{\sin\omega t}{\omega}\bigr]_T^\infty-\tfrac1\omega\int_T^\infty\Phi'(t)\sin(\omega t)dt$. The upper limit vanishes by decay; the lower contributes $-\Phi(T)\sin(\omega T)/\omega$. Hence $|E_j|\le\tfrac{2}{\omega}\bigl(\Phi(T)+\int_T^\infty|\Phi'|\bigr)=\tfrac{4\Phi(T)}{\omega}$ with $\omega=2\pi\alpha j$, using monotonicity of $\Phi$ on $(T,\infty)$ (Pólya; see `L-16001`(f) dependencies) to evaluate $\int_T^\infty|\Phi'|=\Phi(T)$. The boundary term $\Phi(T)\sin(\omega T)/\omega$ is genuinely present and $O(1/\omega)$, so the order cannot be improved by iterating.

**(iv),(v),(vi)** are the tabulated consequences, with $|\Xi(w)|\sim e^{-\pi|w|/4}$ giving $|\Xi(2\pi\alpha j)|\sim e^{-\pi^{2}\alpha j/2}$.

## Analytic domain audit

All integrals are over real $t$ with $\Phi$ real-analytic, positive, and doubly-exponentially decaying, so every interchange and integration by parts is justified. $\Xi$ is entire. No contour or branch choice occurs. The monotonicity of $\Phi$ on $(0,\infty)$ used in (iii) is classical and **imported** (Pólya 1926; Wintner 1935; Csordas–Norfolk–Varga), not proved here.

## Dependency audit

- `L-16001`(e) for the series form of $K$ and its decay — used in (ii).
- Monotonicity of $\Phi$ on $(0,\infty)$ — imported, used only in (iii) to evaluate $\int_T^\infty|\Phi'|$. Without it (iii) still holds with $\int_T^\infty|\Phi'|$ in place of $\Phi(T)$.
- Stirling growth of $\Xi$ on the real axis for (iv),(v).
- **No result of PR #158 is used.**

## Gap audit

1. The values of $E_j$ in the tables (iv) and (vi) were computed by ordinary `mpmath` adaptive quadrature at 40 digits, **not** by certified integration. They are `EMPIRICAL`. The smooth-cutoff integrand in (vi) is oscillatory with a $C^\infty$ bump factor and is the least reliable of these; its fine structure (the non-monotone $j|E_j|$ at $j=10$) should not be over-read, though the order of magnitude and the qualitative conclusion are robust. The *bounds* (ii) and (iii) are `PROVED` and are what the conclusions rest on; the table is illustrative of sharpness, not load-bearing.
2. $C_4$ and $C_2$ were evaluated by summing to $n=30$ without a certified tail; the omitted tail is $O(e^{-\pi\cdot 899})$ and cannot affect any digit shown, but a formal certificate should bound it.
3. (v) uses the crude uniform bound $\varepsilon(T)$. The sharper $j$-dependent bound improves matters but does **not** change the verdict for any $\alpha\ge0.5$ — at $\alpha=1$, $j=10$ the **corrected** rigorous bound $B_2=|\Phi'(T)|/(\pi^{2}\alpha^{2}j^{2})$ gives $7.4\times10^{-4}$ (actual $|E_{10}|=3.67\times10^{-4}$) against a coefficient of $2.4\times10^{-18}$. The figure $3.8\times10^{-3}$ previously quoted here came from the superseded $O(1/j)$ bound.
4. **$\alpha=0.5$ is marginal, not comfortable** — established by the erratum's adjudication and not visible in (v) as written. There $|E_{10}|=8.53\times10^{-9}$ against $|\Xi_{10}|=7.86\times10^{-9}$, a factor of **1.08**, i.e. essentially on the line. The best available rigorous bound $\min(\varepsilon,B_1/2,B_2)=1.75\times10^{-8}$ still exceeds the coefficient, so the "no" verdict survives — **but by a factor of two, not by orders of magnitude.** A sharper bound or a slightly larger $T$ could flip that row, and anyone pushing the certification boundary should start there rather than at $\alpha=0.4$.
5. **(vi)'s hard-vs-smooth table is built on the same mis-read data** and quotes $j|E_j|$ as "approximately constant" for both cutoffs. The hard column is the $j^{-2}$ data misclassified; the smooth column is non-monotone and this lemma already flags it as its least reliable computation. **It should be redone with panel-aligned quadrature and both $j$ and $j^{2}$ columns before being relied on.** The qualitative hard-vs-smooth conclusion is unaffected — super-polynomial still beats $j^{-2}$ — but the table itself is not trustworthy as printed.
6. **Process fix, adopted.** When asserting a decay order from a table, print $j^{p}|E_j|$ for $p$ and $p\pm1$ with each column's max/min ratio. On this lemma's own quoted window ($\alpha=1$, $j=4..12$) that would have shown $j|E_j|$ spanning a factor **2.738** against $j^{2}|E_j|$ spanning **1.096**, with LSQ exponent **1.919** — decisive on sight. The published text called a quantity falling by a factor 2.74 "constant up to a slow drift", and "$\pm35\%$" was really $+63\%/-40\%$.
7. The erratum's numbers are HIGH-PRECISION FLOAT, cross-validated by two independent routes (tail quadrature versus $\Xi(2\pi\alpha j)-2\int_0^T$) agreeing to 38–50 digits, and reproduce this lemma's own tables to 0.11%. Still not certified.
4. "Certifiable" in (v) means only that the uniform box is narrower than the smallest coefficient. That is necessary, not sufficient: an actual certificate must exhibit invariance of the Sturm count over the box, which has not been done even at $\alpha=0.4$.
5. This lemma says nothing about whether the *production* smooth-cutoff target passes or fails. It says the hard-window computations cannot be transferred to it without an explicit argument.

## Adversarial tests

- Bound (ii) against direct quadrature at $T=0.5,0.7,1.0$: ratios $1.91$, $1.83$, $1.75$ — the bound is tight to within a factor $\approx2$ and never violated.
- ~~The $O(1/j)$ law: $j|E_j|$ measured constant to within $\pm35\%$ over $j=4..12$~~ — **withdrawn.** That $\pm35\%$ drift over so short a range was the $j^{-2}$ law being misread; extended to $j=40$, $j|E_j|$ falls by a factor 9.1 while $j^{2}|E_j|$ is flat to 10%. See the ERRATUM to (iii).
- The crossover prediction of (iv) is corroborated independently by `R-16001`'s erratum, which found the sampled and hard-window targets giving **opposite verdicts** at $\alpha=1.0$, $N=6$ — a level at which, by the table, coefficients $j\ge3$ are already $22\times$ to $10^{7}\times$ artifact.
- It is corroborated a second time by the observation that pass-region real roots sit on the sinc lattice $w=2\pi\alpha k$ to 5–6 digits: those are the zeros of the transform of the window indicator, exactly what (iv) predicts the coefficients to encode.

## Remaining uncertainty

The bounds are elementary and the author is confident in them. The main risk is over-reading (v): it identifies where certification *could* begin, not a certificate. The imported monotonicity of $\Phi$ is the only external input.

## Suggested next attack

1. **Redo the census at $\alpha\le0.4$ with certified enclosures**, where (v) says it is feasible, and check Sturm-count invariance over the box explicitly. That is the smallest piece of work that would turn any part of `R-16001` into a certified statement.
2. **Move to the smooth cutoff.** Derive the analogue of (iii) for $\chi_L$-smoothed $\Phi$, where $E_j$ decays faster than any power, and redo the crossover table. This is what the production target actually is (`L-15101`), and (vi) says the hard-window results do not transfer to it.
3. Combine with `L-16004`: the inertia of the Loewner matrix of $-P'/P$ gives the nonreal-pair count without root-finding, and may be more stable under coefficient perturbation than a Sturm count — worth testing as the certification vehicle.
