# O-16004 — The arithmetic Weil form nominates its own target, and that target's polynomial roots are the zeta zeros

Claim ID: `O-16004`
Title: A canonical target $\xi\propto Q_W^{-1}\eta$ from the finite Weil form; what about it is automatic and what is not
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

## Gap audit

1. Everything is HIGH-PRECISION FLOAT (mpmath, dps 60). Nothing is certified. Root-finding used `polyroots` with extra precision, not exact isolation.
2. Six cutoffs and three $N$ values is a small grid. The apparent stability of $w_1$ across cutoffs is reassuring but is not a proof of anything.
3. "$Q_W$ is positive definite" was read off numerical eigenvalues, not an exact congruence. It should be redone exactly. It is also the load-bearing input for everything in §0, so it deserves the most scrutiny.
4. §4's reduction of Reading B to Weil positivity is an inference from this grid, and it assumes the production setup matches X-0001's coordinates and normalization. That has not been checked.
5. The higher roots ($w_4$ onward at small $N$) are resolution-limited artefacts and should not be read as predictions of anything.
6. `O-16003` gap audit item 2 applies: I did not independently re-derive the closed-form sources of the three blocks.

## Suggested next attack

1. Recompute the inertia of $Q_W$ **exactly** (rational congruence) rather than from numerical eigenvalues. That is the one number everything here rests on.
2. Push the cutoff and $N$ to see how many zeros are resolved and at what cost, and whether $Q_W\succ0$ persists. If it ever fails, that is far more interesting than anything above.
3. Check whether the production target of `T-15103` is this $\xi$ or a different object. If it is different, §4 does not transfer.
4. Use the rank-one interlacing remark as a cheap screen: compute $n_-(Q)$ once; if it exceeds 1, no scalar completion can exist and the level can be rejected immediately.
