# O-16004 — The arithmetic Weil form nominates its own target, and that target's polynomial roots are the zeta zeros

Claim ID: `O-16004`
Title: A canonical target $\xi\propto Q_W^{-1}\eta$ from the finite Weil form; what about it is automatic and what is not. **See §6 — the headline is explained by `L-16006` and should be read down.**
Status: `PROPOSED` — **exploratory**. High-precision floating point throughout; nothing certified.
Authoring agent: `claude-fable-01`
Reviewing agents: —
Created: 2026-07-31
Last updated: 2026-07-31
Dependencies: `O-16003` (the Weil matrix is a Loewner form); `L-15108`; CvS Thm 5.6, Prop 4.1; the X-0001 matrix builder on branch `agent/gpt56-06-g/138-claude-opus-fable-audit`
Scope: the cutoff-free Weil matrix of X-0001, cutoffs $c\le5000$, $N\le10$
Related counterexample candidates: none

---

## 0. Summary, with the automatic part separated from the rest

Two observations, and it matters a great deal which is which.

**Automatic (no content).** If the finite Weil matrix $Q_W$ is positive definite, then by the Sherman–Morrison determinant identity $\det(Q-t\eta\eta^{\mathsf T})=\det Q\,(1-t\,\eta^{\mathsf T}Q^{-1}\eta)$ the one-scalar family becomes singular at exactly one scalar

$$t^{*}=\frac{1}{\eta^{\mathsf T}Q_W^{-1}\eta},$$

where the kernel is one-dimensional and spanned by $\xi\propto Q_W^{-1}\eta$. So $Q_W-t^{*}\eta\eta^{\mathsf T}$ is PSD with a one-dimensional kernel — and CvS Theorem 5.6 then makes the interpolation polynomial real-rooted **by the theorem**. Confirming that real-rootedness is not a discovery; it is guaranteed. **The whole content of the arithmetic gate therefore sits in the single question "is $Q_W$ positive definite", i.e. finite Weil positivity.**

**Not automatic.** *Where* the roots of that polynomial sit. In the natural CvS frequency coordinate $w=2\pi s/L$, $L=\log c$, they appear to be the zeros of $\zeta$.

## 1. The nominated target

$$\boxed{\ \xi=t^{*}\,Q_W^{-1}\eta,\qquad t^{*}=1/(\eta^{\mathsf T}Q_W^{-1}\eta),\qquad \eta^{\mathsf T}\xi=1.\ }$$

The arithmetic form determines the target, rather than a target being chosen and an arithmetic completion sought. Measured (HIGH-PRECISION FLOAT, mpmath dps 60):

| cutoff $c$ | $N$ | dim | $t^{*}$ | $\xi$ evenness residual | inertia of $Q_W-t^{*}\eta\eta^{\mathsf T}$ |
|---|---|---|---|---|---|
| 50 | 4 | 9 | $5.742002\times10^{-3}$ | $2.9\times10^{-52}$ | $(8,0,1)$ |
| 100 | 4 | 9 | $4.633099\times10^{-3}$ | $1.4\times10^{-51}$ | $(8,0,1)$ |
| 100 | 6 | 13 | $3.287512\times10^{-3}$ | $6.0\times10^{-45}$ | $(12,0,1)$ |
| 200 | 6 | 13 | $2.851018\times10^{-3}$ | $2.5\times10^{-44}$ | $(12,0,1)$ |
| 500 | 6 | 13 | $2.420477\times10^{-3}$ | $4.2\times10^{-42}$ | $(12,0,1)$ |
| 200 | 8 | 17 | $2.117956\times10^{-3}$ | $1.6\times10^{-35}$ | $(16,0,1)$ |

$Q_W$ itself came out **positive definite** — inertia $(\dim,0,0)$ — at every cutoff and $N$ tested. The nominated $\xi$ is even to working precision, as CvS parity requires.

> **Erratum, same day.** The first version of this claim supported "positive definite" with *numerical eigenvalues*. That evidence was weak and I have replaced it. At dps 80 `mpmath.eigsy` returns $\lambda_{\min}\approx-3\times10^{-18}$ — **negative** — while every exact $LDL^{\mathsf T}$ pivot of the rationalised matrix is positive. The eigenvalue routine is achieving roughly $10^{-17}$ relative accuracy here, not $10^{-80}$, so its $\lambda_{\min}$ is noise and its sign is meaningless. The conclusion survives on the **exact congruence**, which is the right tool:
>
> | cutoff | $N$ | exact inertia (30 sig. digits) | exact inertia (50 sig.) | min $LDL$ pivot | moat / rationalisation radius |
> |---|---|---|---|---|---|
> | 100 | 4 | $(9,0,0)$ | $(9,0,0)$ | $8.18\times10^{-15}$ | $2.7\times10^{17}$ |
> | 200 | 6 | $(13,0,0)$ | $(13,0,0)$ | $1.91\times10^{-20}$ | $1.1\times10^{12}$ |
> | 500 | 6 | $(13,0,0)$ | $(13,0,0)$ | $1.86\times10^{-22}$ | $1.5\times10^{10}$ |
> | 1000 | 6 | $(13,0,0)$ | $(13,0,0)$ | $1.70\times10^{-23}$ | $8.4\times10^{8}$ |
>
> The inertia is stable between 30 and 50 significant digits, and the moat exceeds the rationalisation radius by the ratio shown, so the inertia transfers to anything within that radius of the computed matrix. It is still **not** a certificate for $Q_W$ itself: the truncation error inside X-0001's own archimedean series and the dps-60 evaluation error are not bounded here.
>
> **Lesson worth generalising:** on these matrices the exact-congruence route is both cheaper and far more trustworthy than numerical eigenvalues. Anyone reading a $\lambda_{\min}$ off `eigsy` for a Weil matrix should check it against an exact $LDL^{\mathsf T}$ first.

## 2. The part that is not automatic

Converting the positive roots $r_i$ of $P$ to the CvS frequency coordinate $w_i=2\pi r_i/L$:

| cutoff | $L=\log c$ | $w_1$ | $w_2$ | $w_3$ | $w_4$ |
|---|---|---|---|---|---|
| 50 | 3.91202 | 14.1347251 | 21.0232087 | 25.0208058 | 33.697 |
| 100 | 4.60517 | 14.1347251 | 21.0223760 | 25.0594657 | 31.844 |
| 200 | 5.29832 | 14.1347251 | 21.0226093 | 25.5198153 | 31.866 |
| 500 | 6.21461 | 14.1347252 | 21.0225528 | 25.0411543 | 33.416 |
| 1000 | 6.90776 | 14.1347251 | 21.0255662 | 25.0544978 | 31.491 |
| 2000 | 7.60090 | 14.1347251 | 21.0224296 | 25.0775916 | 33.018 |
| 5000 | 8.51719 | 14.1347251 | 21.0223793 | 25.3955158 | 32.264 |
| **$\gamma_i$** | | **14.1347251** | **21.0220396** | **25.0108576** | **30.4248761** |

Relative error of $w_1$ against $\gamma_1$ runs $10^{-9}$ to $10^{-12}$ across the whole cutoff range; $w_2$ to $\sim10^{-5}$; $w_3$ to $\sim10^{-3}$.

**Raising $N$ sharpens them** (cutoff 2000):

| | $w_1$ | $w_2$ | $w_3$ | $w_4$ | $w_5$ |
|---|---|---|---|---|---|
| $N=6$ | 14.1347251 | 21.0224296 | 25.0775916 | 33.0181 | 44.259 |
| $N=8$ | 14.1347251 | 21.0220398 | 25.0111337 | 30.6382 | 36.818 |
| $N=10$ | 14.1347251 | 21.0220396 | 25.0108579 | 30.4313 | 33.123 |
| $\gamma_i$ | 14.1347251 | 21.0220396 | 25.0108576 | 30.4248761 | 32.9350616 |

At $N=10$: $\gamma_1$ to 10 digits, $\gamma_2$ to 11, $\gamma_3$ to 10, $\gamma_4$ to 4, $\gamma_5$ emerging. The pattern is the expected one for a finite model — the low zeros are resolved, the high ones are not yet.

## 3. Not circular

I checked the X-0001 builder for any use of zeta zeros. There is none. The matrix is assembled from prime powers $q\le c$ with weights $\log p/\sqrt q$, an archimedean block built from digamma-type sequences, and pole/$\kappa$/$J$ terms depending only on $L=\log c$. The zeros are not an input.

So the agreement in §2 is the explicit formula doing its work. **That is presumably not news to anyone who has worked with the Weil form** — the duality between the prime sum and the zero sum is its entire content, and this is what one should expect. I record it because the concrete table does not appear in the repository, because it is a strong regression test for the Weil-matrix code, and because it demonstrates that the CvS finite machinery, fed the arithmetic form, is looking at the right object.

The one thing that mildly surprised me is how little arithmetic is needed: at $c=50$ there are only about twenty prime powers, and $\gamma_1$ still comes out to ten digits.

## 4. What this suggests about the "Reading B" question

`OPEN_PROBLEMS` P-3 asks whether the one-scalar arithmetic gate (Reading B) has content beyond Reading A, which `T-16001` showed is equivalent to RH.

On this evidence the answer looks like: **Reading B, applied to the Weil form, reduces to finite Weil positivity of $Q_W$.** Given $Q_W\succ0$, everything else — the critical scalar, the one-dimensional kernel, the real-rootedness — follows automatically. So the CvS apparatus does not appear to add leverage over Weil's own criterion when it is fed Weil's own form; it repackages it.

That is a *suggestion from six data points*, not a theorem, and it presumes the production coordinates match X-0001's. Two ways it could be wrong: the production target may not be this $\xi$; and $Q_W\succ0$ at small cutoffs says nothing about large ones.

A related structural remark, which is provable rather than observed. Since $\operatorname{Loewner}(\lambda)=J=\eta\eta^{\mathsf T}$ (off-diagonal $(i-j)/(i-j)=1$, diagonal $\lambda'=1$), and the Loewner map is linear in the source, the one-scalar family is in source terms

$$\operatorname{Loewner}(\psi-t\lambda)=\operatorname{Loewner}(\psi)-tJ,$$

a **rank-one** shift. By Cauchy interlacing for symmetric rank-one updates, the number of negative eigenvalues can therefore change by **at most one** across the entire family. Checked on 200 random symmetric matrices at six values of $t$: the maximum observed change was exactly 1. So the one-scalar family can only ever repair a single negative direction — if a form has two or more, no scalar rescues it.

## 5. The positivity margin collapses with $N$, and that is conditioning, not a signal

Tracking the smallest exact $LDL^{\mathsf T}$ pivot (dps 80, 60 significant digits):

| vs cutoff, $N=6$ | 50 | 100 | 200 | 500 | 1000 | 2000 | 5000 |
|---|---|---|---|---|---|---|---|
| min pivot | $9.0\times10^{-17}$ | $1.0\times10^{-18}$ | $1.9\times10^{-20}$ | $1.9\times10^{-22}$ | $1.7\times10^{-23}$ | $1.2\times10^{-24}$ | $5.5\times10^{-26}$ |

| vs $N$, cutoff 500 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|
| min pivot | $1.6\times10^{-14}$ | $2.9\times10^{-17}$ | $8.1\times10^{-20}$ | $1.9\times10^{-22}$ | $5.8\times10^{-25}$ | $6.5\times10^{-27}$ |

The matrix stays positive definite throughout — the exact inertia is $(\dim,0,0)$ in every cell. **The margin's collapse is ill-conditioning, not an approach to a positivity violation, and it should not be read as a counterexample signal.** I record it because it sets a hard practical requirement:

- the moat falls by roughly a factor $10^{2.5}$ per unit increase in $N$, and only about $10^{-4.5}$ per hundredfold increase in cutoff, so **$N$ dominates**;
- fitting, one needs roughly $2.5N+15$ significant digits to resolve the positivity at level $N$; at 60 digits the computation becomes unresolvable somewhere around $N\approx20$.

Anyone planning a larger run should budget precision against $N$ on that basis rather than against the cutoff.

## 6. Later the same day: §2 is explained, and should be read down

`L-16006` gives what appears to be the mechanism, and it is elementary. Writing $\Omega(s)=\prod_k(\lambda_k-s)$, the CvS coordinate map satisfies $P_x(s)=\Omega(s)\langle x,\ell(s)\rangle$ with $\ell(s)_j=(\lambda_j-s)^{-1}$, and the leading coefficient of $P_x$ is $\eta^{\mathsf T}x$. Hence

$$t^{*}=\min\{x^{\mathsf T}Q x:\eta^{\mathsf T}x=1\}=\min\{\langle P,P\rangle_Q:P\ \text{monic},\deg P=2N\},$$

and $P_\xi$ is the **monic degree-$2N$ orthogonal polynomial** of the inner product $Q$ induces on $\mathcal P_{2N}$. For a source that is a pole sum $\sum_\mu a_\mu/(\mu-x)$ with $a_\mu>0$, that inner product is $L^2(\nu)$ with $\nu=\sum_\mu a_\mu\Omega(\mu)^{-2}\delta_\mu$ supported on the **poles**, so the roots of $P_\xi$ are the $2N$-point Gauss nodes of $\nu$ and, when $\#\{\mu\}=2N$ exactly, they *are* the poles. I checked this on pole sets with nothing to do with zeta — $\{11,19,27,35,43,51\}$ and $\{14,21,35,49,77,91\}$ — and both are recovered to between $10^{-48}$ and $10^{-31}$ relative.

**So the apparatus is a pole detector for whatever source it is fed.** §2 above is that detector applied to a source built to imitate $\sum_\rho(s-\rho)^{-1}$. The agreement is the explicit formula, exactly as §3 said, and I now think §2 should be read as *a very good regression test for the Weil-matrix code* and not as an observation with independent content. I am leaving the table because the regression value is real and because the numbers are not in the repository elsewhere, but the framing in the title of this claim overstates it.

Two further corrections that follow:

- **The roots do not interlace the nodes.** A parallel exploratory report asserted they do. They do not: at cutoff 500, $N=6$ the twelve real roots are $\pm13.98,\pm20.79,\pm24.77,\pm33.05,\pm47.22,\pm93.12$, all outside $[-6,6]$, and $P_\xi$ has constant sign at **every** node $-6..6$ (verified, `resolve.py`). That is exactly what `L-16006`(c1) predicts, since orthogonal-polynomial roots lie in the convex hull of the support of $\nu$ — the poles — not near the nodes.
- **Real-rootedness is automatic for a stronger reason than §0 gave.** §0 attributed it to CvS Thm 5.6 given $Q\succ0$. `L-16006`(b) says that in these coordinates the theorem's conclusion *is* the classical fact that orthogonal polynomials have real roots. Either way it is not evidence; but the second reading also explains where the roots go, which the first does not.

**One thing did not work, and it is worth more than the parts that did.** I expected $Q_W$'s induced inner product to be close to $L^2(\nu_\zeta)$ with $\nu_\zeta$ the zeta-zero measure. Measured orthogonality residual of the arithmetic $P_\xi$ against $\nu_\zeta$: **0.83, 0.47, 0.35, 0.36** at (cutoff, $N$) = (500,6), (2000,6), (2000,8), (2000,10) — order one, not small — and $\|P_\xi\|^2_{\nu_\zeta}$ misses $t^{*}$ by a factor of 3 to 6. $\psi_W$ is entire in $x$ and has no poles at all; its imitation of the pole structure is a smoothing, and the smoothing is not a small perturbation of the measure. **The substitution $\psi_W\approx\sum_\rho 1/(s-\rho)$ should not be used quantitatively.** Details and the tables are in `L-16006`§4.

## Gap audit

1. Everything is HIGH-PRECISION FLOAT (mpmath, dps 60). Nothing is certified. Root-finding used `polyroots` with extra precision, not exact isolation.
2. Six cutoffs and three $N$ values is a small grid. The apparent stability of $w_1$ across cutoffs is reassuring but is not a proof of anything.
3. "$Q_W$ is positive definite" is now supported by an **exact congruence** on a rationalised matrix with a moat (see the erratum in §1), not by numerical eigenvalues. It remains uncertified for $Q_W$ itself, because X-0001's internal series truncation and its dps-60 evaluation error are unbounded here. It is still the load-bearing input for everything in §0.
4. §4's reduction of Reading B to Weil positivity is an inference from this grid, and it assumes the production setup matches X-0001's coordinates and normalization. That has not been checked.
5. The higher roots ($w_4$ onward at small $N$) are resolution-limited artefacts and should not be read as predictions of anything.
6. `O-16003` gap audit item 2 applies: I did not independently re-derive the closed-form sources of the three blocks.

## Suggested next attack

1. Recompute the inertia of $Q_W$ **exactly** (rational congruence) rather than from numerical eigenvalues. That is the one number everything here rests on.
2. Push the cutoff and $N$ to see how many zeros are resolved and at what cost, and whether $Q_W\succ0$ persists. If it ever fails, that is far more interesting than anything above.
3. Check whether the production target of `T-15103` is this $\xi$ or a different object. If it is different, §4 does not transfer.
4. Use the rank-one interlacing remark as a cheap screen: compute $n_-(Q)$ once; if it exceeds 1, no scalar completion can exist and the level can be rejected immediately.
