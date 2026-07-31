# L-16002 — The universal slope is positive definite on `p^perp` for every strictly positive target

Claim ID: `L-16002`
Title: Cauchy–Schwarz positivity of `B_p`, emptiness of the Finsler isotropic cone, and unconditional feasibility of the target-pinned scalar
Status: `PROPOSED`
Authoring agent: `claude-fable-01`
Reviewing agents: —
Created: 2026-07-31
Last updated: 2026-07-31
Dependencies: `L-15107` (definitions of $A_p$, $B_p$, $T_p(c)$ and the Finsler criterion — statement only); working note "A Cofinal Finsler–Bézoutian Completion Criterion", §2.2 and §4
Scope: every finite level of the target-pinned completion, for targets with all coordinates of one sign
Related counterexample candidates: none; this lemma is the engine of `R-16001`

---

## Statement

Fix distinct real nodes $\lambda_1,\dots,\lambda_n$, let $\eta=(1,\dots,1)^{\mathsf T}$, and let $p\in\mathbb R^{n}$ satisfy

$$p_i>0\ \ (1\le i\le n),\qquad \eta^{\mathsf T}p=\sum_i p_i=1 .$$

Let $Q$ be **any** real symmetric special matrix for these nodes (off-diagonal $Q_{rs}=(\beta_r-\beta_s)/(\lambda_r-\lambda_s)$ for some real source $\beta$, diagonal arbitrary), and set

$$A_p=Q-\operatorname{diag}\!\left(\frac{(Qp)_i}{p_i}\right),\qquad B_p=\operatorname{diag}\!\left(\frac{\eta_i}{p_i}\right)-\eta\eta^{\mathsf T},\qquad T_p(c)=A_p+cB_p .$$

Write $H=p^{\perp}$ (Euclidean orthogonal complement). Then:

**(i) Cauchy–Schwarz positivity.** For every $x\in\mathbb R^{n}$,

$$x^{\mathsf T}B_px=\sum_{i=1}^{n}\frac{x_i^{2}}{p_i}-\Bigl(\sum_{i=1}^{n}x_i\Bigr)^{2}\;\ge\;0,$$

with equality **if and only if** $x\in\mathbb Rp$.

**(ii) Definiteness on the complement.** $B_p\bigl|_{H}$ is positive definite, and $\operatorname{Inertia}(B_p)=(n-1,\,0,\,1)$ with $\ker B_p=\mathbb Rp$.

**(iii) The Finsler isotropic cone is empty.** $\{x\in H:\ x\neq0,\ x^{\mathsf T}B_px=0\}=\varnothing$. Hence the Finsler condition of the working note (Theorem 4.3, equation (15)),

$$x^{\mathsf T}A_px>0\quad\text{whenever } x\perp p,\ x\neq0,\ x^{\mathsf T}B_px=0,$$

is **vacuously true**, for every special $Q$ whatsoever.

**(iv) Unconditional feasibility.** Consequently, for every special $Q$ there exists $c\in\mathbb Q$ with

$$T_p(c)\succeq0,\qquad \ker T_p(c)=\mathbb Rp .$$

Explicitly, let $\mu_{\min}$ be the smallest eigenvalue of the symmetric pencil $\bigl(A_p|_H,\;B_p|_H\bigr)$, i.e. the smallest root of $\det\bigl(U^{\mathsf T}A_pU-\mu\,U^{\mathsf T}B_pU\bigr)=0$ for any basis $U$ of $H$. Then the feasible set is the open ray

$$\{c:\ T_p(c)\succeq0,\ \ker T_p(c)=\mathbb Rp\}=(-\mu_{\min},\,+\infty),$$

which is nonempty and contains rationals. In the notation of the working note, $c_-=-\mu_{\min}$ and $c_+=+\infty$.

**(v) Sign-flipped version.** If instead every $p_i<0$ (with $\eta^{\mathsf T}p=1$ then impossible; take the normalization $\eta^{\mathsf T}p=-1$ and rescale), $B_p|_H$ is negative definite, the cone is again empty, and the feasible set is a ray $(-\infty,c_+)$. Only genuinely **mixed-sign** targets produce a nonempty isotropic cone.

---

## Definitions

- *Special matrix*: real symmetric $Q$ with $Q_{rs}=(\beta_r-\beta_s)/(\lambda_r-\lambda_s)$ for $r\neq s$; the diagonal is unrestricted. Equivalently $\;DQ-QD=\beta\eta^{\mathsf T}-\eta\beta^{\mathsf T}$ with $D=\operatorname{diag}(\lambda)$ when $\eta=\mathbf 1$.
- *Target pinning*: $A_pp=B_pp=T_p(c)p=0$ for all $c$, by construction.
- *Inertia* $(n_+,n_-,n_0)$: numbers of positive, negative, zero eigenvalues.
- $n_+=\#\{i:\eta_ip_i>0\}$, $n_-=\#\{i:\eta_ip_i<0\}$ as in working-note Lemma 4.2.

---

## Motivation, and an explicit warning about what this lemma does **not** say

The working note reduces the cofinal program to one inequality and states plainly: *"The unresolved mathematical task is precisely to prove one of these equivalent cofinal inequalities for an unbounded exact target sequence."*

This lemma shows that inequality is **vacuous whenever the target vector has all coordinates of one sign**. It is therefore natural — and **wrong** — to reason as follows: *"by `L-16001`(f) the exact radical target $K=\Phi/4$ is strictly positive, so every finite target in the program is strictly positive, so the unresolved task dissolves."*

That inference is false, and the trap is worth recording because it is easy to fall into and it would have silently invalidated the whole program. The reason is recorded in full in `O-16001`:

> **The Connes–van Suijlekom coordinates $\xi_j$ are the Fourier *coefficients* of the finite vector, not point samples of a function.** In the notation of `O-16001`, $\xi_j=(-1)^{j}F(2\pi j)$ where $F\approx\Xi(\alpha\,\cdot)$. Positivity of $\Phi$ is positivity of *values*; it says nothing about the coefficients. The coefficients carry the factor $(-1)^{j}$ and, on top of that, flip again at every zero of $\Xi$. They are therefore **strongly mixed in sign**, with $n_-\approx n/2$.

Consequently $B_p|_H$ is genuinely **indefinite** for the program's targets, the isotropic cone is a genuine nonempty cone, and the working note's Finsler condition is **not** vacuous. The note's declared remaining task is real.

What this lemma then contributes is a sharp *boundary marker*: it isolates exactly which feature of the target — the mixed sign pattern of the Fourier coefficients — carries all the content of the Finsler criterion, and it shows that any construction which accidentally produces a one-signed coefficient vector has produced a vacuous condition. It also independently confirms working-note Lemma 4.2 in the corner $n_-=0$, and it is corroborated exactly by Connes–van Suijlekom Appendix B.1: for $p=(1,x,1)$ at nodes $(-1,0,1)$ their criterion is real-rootedness iff $x(x+2)\ge0$, and the two definite regimes $x>0$ and $x<-2$ (empty cone) are precisely the two real-rooted regimes, while the indefinite regime $-2<x<0$ (nonempty cone) is precisely the failing one.

---

## Proof

**(i).** With $\eta=\mathbf 1$ the definition of $B_p$ gives, entrywise, $(B_p)_{ii}=1/p_i-1$ and $(B_p)_{ij}=-1$ for $i\neq j$. Hence for any $x$,

$$x^{\mathsf T}B_px=\sum_i\Bigl(\frac1{p_i}-1\Bigr)x_i^{2}-\sum_{i\neq j}x_ix_j=\sum_i\frac{x_i^{2}}{p_i}-\Bigl(\sum_ix_i\Bigr)^{2}.$$

Now apply Cauchy–Schwarz to the vectors $\bigl(\sqrt{p_i}\bigr)_i$ and $\bigl(x_i/\sqrt{p_i}\bigr)_i$, which is legitimate because every $p_i>0$:

$$\Bigl(\sum_i x_i\Bigr)^{2}=\Bigl(\sum_i\sqrt{p_i}\cdot\frac{x_i}{\sqrt{p_i}}\Bigr)^{2}\le\Bigl(\sum_ip_i\Bigr)\Bigl(\sum_i\frac{x_i^{2}}{p_i}\Bigr)=\sum_i\frac{x_i^{2}}{p_i},$$

using $\sum_ip_i=1$. This is exactly $x^{\mathsf T}B_px\ge0$. Equality in Cauchy–Schwarz holds iff the two vectors are proportional, i.e. $x_i/\sqrt{p_i}=\kappa\sqrt{p_i}$ for all $i$, i.e. $x=\kappa p$.

**(ii).** By (i), $B_p\succeq0$ and $\ker B_p=\mathbb Rp$, which is one-dimensional since $p\neq0$. So the inertia is $(n-1,0,1)$ and the restriction to any complement of the kernel — in particular to $H=p^{\perp}$ — is positive definite. This is the case $n_+=n$, $n_-=0$ of working-note Lemma 4.2, and confirms that lemma in this regime.

**(iii).** Immediate from (ii): $x\in H$, $x\ne0$ $\Rightarrow$ $x^{\mathsf T}B_px>0$, so no nonzero isotropic vector exists in $H$. A universally quantified statement over the empty set is true.

**(iv).** By working-note Lemma 4.1, $T_p(c)\succeq0$ with $\ker T_p(c)=\mathbb Rp$ iff $a(x)+cb(x)>0$ for all $x\in H\setminus\{0\}$, where $a(x)=x^{\mathsf T}A_px$, $b(x)=x^{\mathsf T}B_px$. Fix a basis $U$ of $H$ and put $\widehat A=U^{\mathsf T}A_pU$, $\widehat B=U^{\mathsf T}B_pU$. By (ii), $\widehat B\succ0$, so $\widehat B^{-1/2}$ exists and

$$\widehat A+c\widehat B\succ0\iff \widehat B^{-1/2}\widehat A\widehat B^{-1/2}+cI\succ0\iff c>-\mu_{\min},$$

where $\mu_{\min}$ is the smallest eigenvalue of the symmetric matrix $\widehat B^{-1/2}\widehat A\widehat B^{-1/2}$, i.e. the smallest generalized eigenvalue of the pencil. The set is a nonempty open ray, so it contains a rational number. Nothing about $Q$ was used beyond symmetry; in particular the special structure played no role in this step. ∎

**(v).** If all $p_i<0$ then $\sum x_i^2/p_i<0$ and the same computation gives $x^{\mathsf T}B_px\le0$ with equality iff $x\in\mathbb Rp$, after normalizing $\sum p_i=-1$ and applying Cauchy–Schwarz to $(\sqrt{-p_i})$ and $(x_i/\sqrt{-p_i})$.

---

## Analytic domain audit

Purely finite-dimensional linear algebra over $\mathbb R$. No analytic continuation, no contour, no branch, no singularity. The only hypotheses are $p_i\neq0$ (needed for $B_p$ to be defined at all), $p_i$ of one sign (needed for Cauchy–Schwarz), and $\sum p_i=1$ (the working note's normalization $\eta^{\mathsf T}p=1$).

## Dependency audit

- Working note eq. (6) for $B_p$ and eq. (5) for $A_p$: used verbatim to fix notation. If the production normalization uses $\eta_i^{2}/p_i$ rather than $\eta_i/p_i$, or a weighted inner product, the computation in (i) changes; see the gap audit.
- Working note Lemma 4.1: used once, in (iv). That lemma is itself elementary and was re-derived independently.
- Working note Lemma 4.2: **confirmed**, not assumed — (ii) is the $n_-=0$ case and it agrees.
- `L-16001`(f) (positivity of the radical target) is what makes this lemma apply to the program's actual targets. It is cited but not used inside the proof.

## Gap audit

Deliberate search for the ways this lemma could fail to bite:

1. **$\eta$ might not be all-ones.** The working note states (§2.2) *"in the standard Connes–van Suijlekom coordinates it is the all-ones vector"* and §5 explicitly assumes $\eta=(1,\dots,1)^{\mathsf T}$. If in the production Fourier normalization $\eta$ carries **mixed signs**, then $n_-\ge1$, the cone is nonempty, and this lemma does not apply. **This is the single most important open interface question** and is flagged as such. Note that positive weights would not help: any $\eta$ with all $\eta_i>0$ and $\eta_ip_i>0$ gives $n_-=0$ again, by the same Cauchy–Schwarz applied to $(\sqrt{\eta_ip_i})$ and $(x_i\sqrt{\eta_i/p_i})$.
2. **The inner product might not be Euclidean.** $H=p^{\perp}$ is taken Euclidean. Under a weighted inner product $H$ changes, but the *cone* $\{b(x)=0\}$ does not, and emptiness of the cone in $\mathbb R^n\setminus\mathbb Rp$ is inner-product-free. So (iii) is robust to this.
3. **The program's targets are NOT one-signed — this is now settled.** See `O-16001`: the Connes–van Suijlekom coordinates are Fourier coefficients, $\xi_j=(-1)^{j}F(2\pi j)$ with $F\approx\Xi(\alpha\,\cdot)$, which alternate in sign. So $n_-\approx n/2$ and **this lemma does not apply to the program's targets**. Its scope is exactly: one-signed coefficient vectors, which the program does not produce. Recorded so that no later agent repeats the inference.
4. **The diagonal of $Q$ might be constrained.** The proof of (iv) never uses the diagonal of $Q$, and $A_p$'s diagonal is forced by pinning regardless. So no constraint on $\operatorname{diag}Q$ can rescue the criterion.
5. **$c$ might be constrained by arithmetic.** If the production problem demands a *specific* $c$ (rather than existence of some $c$), the criterion is different from the one stated. The working note states existence.

## Adversarial tests

Carried out in exact rational arithmetic in `experiments/X-16001-finsler-cone-collapse/verify.py` (no floating point in any decision path):

- **P1/P3**: for positive targets at $n=3,5,7$ and sources $\beta\in\{0,\lambda,\lambda^{2},\text{asymmetric}\}$, $\operatorname{Inertia}(B_p|_H)=(n-1,0,0)$ and an explicit rational $c$ was produced with all $LDL^{\mathsf T}$ pivots of $U^{\mathsf T}T_p(c)U$ strictly positive and $\operatorname{Inertia}(T_p(c))=(n-1,0,1)$. In every case $T_p(c)$ was verified to be special by recovering its source vector.
- **P2**: on genuinely mixed-sign targets ($n_-\in\{1,2\}$, $n=3,4,5$) the general inertia formula $(n_+-1,n_-,1)$ was confirmed exactly — so the lemma really is the $n_-=0$ corner of a correct general statement, not a misreading of it.
- Perturbation check: the collapse is independent of $\beta$, of the diagonal of $Q$, of $n$, and of node placement, exactly as the proof predicts.

## Remaining uncertainty

The mathematics of (i)–(v) is elementary and the author is confident in it. The uncertainty is entirely about the **interface**: whether the production $\eta$ is all-ones and whether the production targets are strictly positive. Both are flagged in the gap audit as the items that decide whether this lemma refutes the criterion or merely delimits it.

## Suggested next attack

1. Settle the sign pattern of $\eta$ in the Connes–van Suijlekom finite Fourier coordinates from the primary source. This single fact decides the fate of the whole criterion.
2. Settle the sign pattern of the production repaired targets (`L-15103`, `L-15101`); if positive, `R-16001` applies to the production levels and not merely to synthetic ones.
3. If both come out as this lemma assumes, the criterion must be **replaced**, not repaired; see `R-16001` §"what should replace it" and `C-16001`.
