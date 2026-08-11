# Chebyshev–Christoffel Hankel and rational-safe-pole attack — 2026-08-11

## Freeze

```text
repository:  gfreund123/riemann
base PR:     #395
base head:   7106b3b2e06b8193861851890db12767a03b5df4
branch:      research/gpt56-pro/395-chebyshev-hankel-amplifier
RH status:   unproved
```

## Executive result

PR #395 identifies the universal high-carrier safe-line background as the beta-`(3/2,3/2)` Stieltjes law

\[
 d\nu(\lambda)=\pi^{-1}\sqrt{\lambda(1-\lambda)}d\lambda.
\]

The present continuation diagonalizes that background exactly, upgrades scalar coefficient positivity to a growing **full Hankel matrix theorem**, computes the optimal finite-degree detector for one off-line pair, and opens a faster rational-safe-pole route.

The principal proposed unconditional theorem is

\[
 H_n(x)=(a_{i+j}(x))_{0\le i,j\le n}\succ0
\]

for all sufficiently large `|x|` and every

\[
 n\le\left(\frac1{2\log3}-\varepsilon\right)
 \log\log|x|.
\]

This proves positivity of every polynomial sum-of-squares test using the first `2n+1` safe-line moments, not merely of selected coefficients.

All analytic claims require independent review. No Riemann-data violation is asserted and RH remains unproved.

## I. Exact Chebyshev preconditioner

For

\[
 e_j(\lambda)=\sqrt8U_j(2\lambda-1),
\]

one has exactly

\[
 \int_0^1e_j e_k\,d\nu=\delta_{jk}.
\]

Thus the Catalan moment matrix becomes the identity in shifted Chebyshev-`U` coordinates. This is the natural nonlinear preconditioner for the safe-line moment hierarchy.

The degree-`n` reproducing kernel is

\[
 K_n(\lambda,\mu)=8\sum_{j=0}^n
 U_j(2\lambda-1)U_j(2\mu-1).
\]

It solves the exact minimax problem

\[
 \sup_{\deg p\le n,\int|p|^2d\nu=1}|p(\lambda_*)|^2
 =K_n(\lambda_*,\lambda_*).
\]

## II. One matching pair is an optimal negative rank-one perturbation

For depth `y`, put

\[
 w_y=1-y^2,
 \qquad
 \lambda_y=w_y^{-1},
 \qquad
 \alpha_y=2\operatorname{artanh}y.
\]

The pair contributes to every polynomial square as

\[
 Q_{\rm pair}[p]
 =-4my^2w_y^{-3}|p(\lambda_y)|^2.
\]

In Chebyshev coordinates this is one negative rank-one matrix. Its exact nonzero eigenvalue is

\[
 -4my^2w_y^{-3}K_n(\lambda_y,\lambda_y),
\]

where

\[
 K_n(\lambda_y,\lambda_y)
 =\frac8{\sinh^2\alpha_y}
 \sum_{j=1}^{n+1}\sinh^2(j\alpha_y).
\]

The optimal polynomial detection degree is therefore

\[
 n_{\rm det}(x,y)
 \sim\frac{\log\log|x|}{4\operatorname{artanh}y}.
\]

At the deepest strip edge `y->1/2`,

\[
 n_{\rm edge}(x)
 \sim\frac{\log\log|x|}{2\log3}
 =0.4551196\ldots\log\log|x|.
\]

This is a factor

\[
 \frac{2\log3}{\log(4/3)}
 =7.6376833\ldots
\]

smaller than the raw-coefficient detection order from PR #395.

## III. Full Hankel positivity from the entire safe parabola

The direct Euler domain is

\[
 \Re\sqrt{1-w}>\frac12,
\]

not merely the inscribed disc `|w|<3/4`. Its boundary curves are

\[
 w=1-(c+iv)^2,
 \qquad c>1/2.
\]

On this parabola, with

\[
 \lambda=1/w,
 \qquad
 q=(1+r)/(1-r),
\]

one has

\[
 U_j(2\lambda-1)=q^j+q^{j-2}+\cdots+q^{-j}
\]

and

\[
 |q|\le\frac{1+c}{1-c}.
\]

Taking `c=1/2+1/(n+4)` gives the sharp growth constant

\[
 |q|=3+O(1/n).
\]

The parabolic Cauchy argument yields

\[
 \left|Q_x[p]-\ell_xQ_\nu[p]\right|
 \ll(n+4)^7 9^nQ_\nu[p].
\]

Hence the full preconditioned Hankel matrix equals

\[
 \ell_xI+O_{\rm op}(n^7 9^n),
\]

which proves the growing-matrix theorem through every fixed fraction below `1/(2 log 3)`.

This range is sharp at leading order for the complete polynomial-Hankel architecture: it is exactly where an optimally amplified deepest pair can first compete.

## IV. Rational safe-pole acceleration

For `b>4/3`, put

\[
 z_b(\lambda)=\frac{\lambda(b-1)}{b-\lambda},
 \qquad
 R_{n,b}(\lambda)=T_n(2z_b(\lambda)-1).
\]

The map sends `[0,1]` to `[0,1]`, so

\[
 |R_{n,b}(\lambda)|\le1
\]

on the critical-line support. At a target depth,

\[
 R_{n,b}(\lambda_y)
 =\cosh\left(n\operatorname{arccosh}X_{b,y}\right).
\]

As `b->4/3+`,

\[
 \operatorname{arccosh}X_{b,y}
 \longrightarrow2\operatorname{artanh}(2y).
\]

The formal rational detection degree is therefore

\[
 n_{\rm rat}(x,y)
 \sim\frac{\log\log|x|}{4\operatorname{artanh}(2y)},
\]

a factor two improvement for shallow pairs.

Every finite test is computable from derivatives of `A_x` at the single safe point `w=1/b<3/4`, hence from absolutely convergent Euler series at one fixed sample in `Re(s)>1`.

## V. Multipole optimality

In the radial variable `r`, every safe half-plane Blaschke factor obeys

\[
 \left|\frac{y+\overline a}{y-a}\right|
 \le\frac{1/2+y}{1/2-y}
 =e^{2\operatorname{artanh}(2y)}
 \qquad(\Re a\ge1/2).
\]

Thus no finite multipole, complex-pole, or general safe-inner rational design improves the leading exponent of the repeated boundary pole. The one-pole Chebyshev family is Green-function optimal in this broad class.

This exact no-go prevents wasting effort on elaborate safe multipole banks. A stronger route must use annular poles, non-inner growth, matrix arithmetic, or carrier-specific cancellation.

## VI. Verification

```bash
cd experiments/X-91010-chebyshev-hankel-amplifier
python3 verify.py --json /tmp/verification.json
cmp /tmp/verification.json results/verification.json
sha256sum -c SHA256SUMS
```

Retained verdict:

```text
PASS_CHEBYSHEV_HANKEL_AMPLIFIER
```

The replay checks exact rational orthogonality, exact inverse-Hankel/Christoffel agreement, the rank-one pair identity, the closed hyperbolic kernel, synthetic detection scales, the parabolic constant `3`, and the rational accelerator. It does not certify the analytic parabolic remainder estimate.

## Exact frontier

```text
Catalan Hankel -> shifted-Chebyshev identity       EXACT
optimal Christoffel pair amplifier                 EXACT
one pair -> negative rank-one Hankel block         EXACT
full Hankel PSD to 0.455... loglog|x|              PROPOSED COMPLETE
polynomial SOS edge constant 1/(2 log 3)           SHARP
one-safe-pole rational acceleration                EXACT
safe multipole exponent                            EXACTLY OPTIMAL
critical-degree Hankel sign                        OPEN / RH-BEARING
uniform rational Pick sign at safe boundary        OPEN / RH-BEARING
annular/cofinal Pick positivity                     OPEN / RH-EQUIVALENT
Riemann Hypothesis                                 UNPROVED
```
