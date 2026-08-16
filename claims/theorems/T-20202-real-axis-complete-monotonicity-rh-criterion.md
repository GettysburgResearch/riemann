# T-20202 — A real-axis complete-monotonicity and one-point Hankel criterion for RH

Claim ID: `T-20202`  
Title: One dyadic logarithmic-derivative ratio on the absolutely convergent real axis is completely monotone exactly under RH  
Status: `PROPOSED — COMPLETE ARGUMENT PENDING INDEPENDENT REVIEW OF THE LAPLACE-UNIQUENESS STEP`  
Authoring agent: `gpt56-pro-09-n`  
Created: 2026-08-07  
Dependencies: `T-20201`; Bernstein–Widder and Stieltjes moment theorems; the standard positive theta-kernel representation of `xi`  
Scope: a global criterion using only real values `s>1`

## 1. The real-axis function

Let

\[
 F(s)=\frac{\xi'(s)}{\xi(s)}.
\]

For `y>1`, define

\[
\boxed{
 \mathcal L_2(y)=\frac2{y^2}
 \left[
 2F\left(\frac12+y\right)
 -F\left(\frac12+\frac y2\right)
 \right].}
\tag{1}
\]

Both arguments exceed `1`, so the zeta logarithmic derivative is represented by an absolutely convergent Dirichlet series; no high critical-line ordinate or zero-exclusion computation is needed.

Putting `z=iy` in `T-20201` gives

\[
\boxed{
 \mathcal L_2(y)=\int_0^\infty
 \mathcal D(t)e^{-yt}\,dt,
 \qquad y>1.}
\tag{2}
\]

## 2. Complete monotonicity criterion

The following are equivalent:

1. RH;
2. `mathcal L_2` is completely monotone on `(1,infinity)`:
   \[
   (-1)^k\mathcal L_2^{(k)}(y)\ge0
   \quad(k\ge0,y>1).
   \]

### RH implies complete monotonicity

Under RH, `T-20201` gives `mathcal D(t)>=0`. Differentiating (2) under the integral yields

\[
 (-1)^k\mathcal L_2^{(k)}(y)
 =\int_0^\infty t^k\mathcal D(t)e^{-yt}dt\ge0.
\]

### Complete monotonicity implies RH

Assume `mathcal L_2` is completely monotone. Bernstein–Widder applied to

\[
 x\mapsto\mathcal L_2(1+x)
\]

produces a positive measure `nu` on `[0,infinity)` whose Laplace transform is this function. Fix `y_0>1`. Then for every `x>0`,

\[
\int_0^\infty e^{-xt}e^{-y_0t}\mathcal D(t)dt
=
\int_0^\infty e^{-xt}e^{-(y_0-1)t}d\nu(t).
\tag{3}
\]

Both sides are Laplace transforms of finite signed measures. Uniqueness gives

\[
 e^{-y_0t}\mathcal D(t)dt
 =e^{-(y_0-1)t}d\nu(t)\ge0.
\]

Since `mathcal D` is continuous, it is nonnegative everywhere. `T-20201` then yields RH.

Thus

\[
\boxed{
 \mathrm{RH}
 \iff
 \mathcal L_2\text{ is completely monotone on }(1,\infty).}
\tag{4}
\]

## 3. Zeroth order is unconditional

Use the positive Riemann theta-kernel representation

\[
 X(y)=\xi(1/2+y)=\int_0^\infty\Phi(t)\cosh(yt)dt,
 \qquad \Phi(t)>0.
\]

Then `X` is positive, increasing for `y>0`, and log-convex. Hence

\[
 y\mapsto F(1/2+y)=\frac{X'(y)}{X(y)}
\]

is nonnegative and increasing. Consequently

\[
 2F(1/2+y)-F(1/2+y/2)>0
 \qquad(y>1),
\]

so

\[
\boxed{\mathcal L_2(y)>0\quad(y>1)}
\tag{5}
\]

holds unconditionally. The RH content begins in the higher derivative/Hankel constraints, not in the raw sign.

## 4. A one-point Stieltjes moment criterion

Fix any rational `y_0>1` and define

\[
 \mu_k=(-1)^k\mathcal L_2^{(k)}(y_0),
 \qquad k\ge0.
\tag{6}
\]

For every `n>=0`, form

\[
 H_n^{(0)}=(\mu_{i+j})_{0\le i,j\le n},
 \qquad
 H_n^{(1)}=(\mu_{i+j+1})_{0\le i,j\le n}.
\tag{7}
\]

Then

\[
\boxed{
 \mathrm{RH}
 \iff
 H_n^{(0)}\succeq0
 \text{ and }
 H_n^{(1)}\succeq0
 \text{ for every }n.}
\tag{8}
\]

Under RH these are Gram matrices of the positive measure

\[
 e^{-y_0t}\mathcal D(t)dt.
\]

Conversely, the two Hankel families are the Stieltjes moment conditions and yield a positive measure with moments `mu_k`. The actual signed measure has an exponential moment because `y_0>1` and `mathcal D(t)` has exponential order one. Its even moments therefore satisfy a factorial bound, giving Carleman determinacy. The positive measure has the same bound and hence an exponential moment as well. Equality of all moments forces equality of the two Laplace transforms near the origin and then equality of the measures. Therefore `mathcal D>=0`, and `T-20201` gives RH.

This compresses the full problem to an all-order rational Hankel hierarchy at **one ordinary real point**, for example `y_0=2`.

## 5. Arithmetic accessibility

At `s>1`,

\[
 \frac{\zeta'}{\zeta}(s)
 =-\sum_{n=2}^\infty\frac{\Lambda(n)}{n^s}
\]

converges absolutely, and every derivative is an absolutely convergent log-moment series. The gamma, rational, and pi terms are explicit. Therefore every finite Hankel matrix in (8) can be enclosed without Riemann–Siegel evaluation, high zeros, or a moving prime cutoff.

The live full-problem attack is now:

1. derive a structural Gram or total-positivity factorization of the sequence `mu_k` from the Euler/gamma decomposition at `y_0=2`; or
2. find the first exact negative Hankel direction, which would disprove RH.

Finite positive matrices remain finite. A proof requires a uniform all-order factorization or recurrence preserving both Stieltjes Hankel cones.

## 6. Prior-art boundary

Complete-monotonicity criteria for genus-zero entire functions and real-zero location exist in the literature. The new object here is the **fixed dyadic Haar defect**, its pole-descent converse, and the real-axis ratio (1) obtained from that defect. This claim remains proposed until its relationship to those criteria is independently mapped.

## 7. Proof boundary

- The implication RH to complete monotonicity is immediate from the Haar square.
- The converse uses uniqueness of Laplace transforms and `T-20201`.
- The one-point criterion additionally uses the Stieltjes moment theorem and determinacy from exponential moments.
- No all-order Hankel positivity proof is supplied here.
- No finite numerical matrix can be promoted to RH.
