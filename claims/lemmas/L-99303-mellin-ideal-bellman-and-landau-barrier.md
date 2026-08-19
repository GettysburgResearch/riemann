# L-99303 — The subpolynomial Mellin ideal is Bellman-stable, and Landau gives an exact pole barrier

Claim ID: `L-99303`  
Status: **PROVED ANALYTIC THEOREM**  
Created: 2026-08-20  
RH status: not assumed

## 1. A Bellman-stable error class

Let `S_0` be the class of measurable functions `f` on `[1,infinity)` such that
for every `epsilon>0`,

\[
\|f\|_\epsilon
:=\sup_{X\ge1}X^{-\epsilon}|f(X)|<\infty.
\tag{L-99303.1}
\]

Every `f in S_0` belongs to the absolute Mellin class

\[
\mathcal A_+
=
\left\{
 f:\int_1^\infty |f(X)|X^{-\sigma-1}\,dX<\infty
 \text{ for every }\sigma>0
\right\}.
\tag{L-99303.2}
\]

Indeed, for fixed `sigma>0`, use (L-99303.1) with
`epsilon=sigma/2`.

Consider a positive factor-67 Bellman operator on a finite family of typed
states,

\[
(\mathcal Tf)_v(X)
=
\sum_{w\succ v}a_{vw}(X)
 f_w\!\left(\frac{X}{p_{vw}}\right),
\tag{L-99303.3}
\]

with

\[
a_{vw}(X)\ge0,
\qquad
p_{vw}\ge67,
\qquad
\sum_{w\succ v}a_{vw}(X)\le\kappa<\frac18.
\tag{L-99303.4}
\]

For the supremum seminorm over all states,

\[
\boxed{
\|\mathcal Tf\|_\epsilon
\le
\kappa 67^{-\epsilon}\|f\|_\epsilon.
}
\tag{L-99303.5}
\]

Therefore `I-T` is invertible on every `epsilon` seminorm and

\[
\boxed{
(I-\mathcal T)^{-1}
=
\sum_{r\ge0}\mathcal T^r
}
\tag{L-99303.6}
\]

preserves `S_0`. More explicitly, if `C in S_0`, then the solution of

\[
E=C+\mathcal TE
\tag{L-99303.7}
\]

satisfies

\[
\boxed{
\|E\|_\epsilon
\le
\frac{\|C\|_\epsilon}
 {1-\kappa67^{-\epsilon}}.
}
\tag{L-99303.8}
\]

Hence bounded, polylogarithmic, or any uniformly subpolynomial local
calibration remains Mellin-holomorphic after the complete varying-prime
recursion. A uniform root-source mass estimate is not required.

## 2. Exact Landau trichotomy

Let `D(X)>=0` be locally integrable and suppose its Mellin transform

\[
\mathcal D(s)=\int_1^\infty D(X)X^{-s-1}\,dX
\tag{L-99303.9}
\]

converges on some right half-plane. Let `sigma_c` be its finite abscissa of
convergence. Suppose further that `mathcal D` has a meromorphic continuation to
`Re(s)>0`, is holomorphic at every positive real point, and has a nonreal pole
in that half-plane.

There are only two cases.

* If `sigma_c<=0`, the defining nonnegative integral converges and is
  holomorphic throughout `Re(s)>0`, contradicting the nonreal pole.
* If `sigma_c>0`, Landau's theorem for nonnegative Laplace/Mellin transforms
  makes the real point `s=sigma_c` a singularity. This contradicts the assumed
  positive-real holomorphy.

Thus:

\[
\boxed{
\begin{gathered}
D\ge0,\quad \sigma_c<\infty,\quad
\mathcal D\text{ meromorphic on }\Re s>0,\\
\mathcal D\text{ holomorphic on }(0,\infty)
\quad\Longrightarrow\quad
\mathcal D\text{ has no nonreal pole in }\Re s>0.
\end{gathered}}
\tag{L-99303.10}
\]

This proof does not need the nonreal pole to lie on the convergence boundary,
and it does not need a prior comparison between its real part and `sigma_c`.

## 3. Application to a fixed component row

For the canonical row,

\[
\mathcal C_j(s)
=
\frac{C_j}{s^2}
+
\frac{P_j(s+1/2)}{s^2\zeta(s+1/2)}.
\tag{L-99303.11}
\]

If `D_j>=0` and `E_j=c_j-D_j in S_0`, then the Mellin transform of `E_j` is
holomorphic on `Re(s)>0`. Every off-line zero `rho` with `P_j(rho)!=0` remains
a nonreal pole of `mathcal D_j=mathcal C_j-mathcal E_j`. The canonical row has
polynomial growth, while `E_j` is subpolynomial, so `D_j` has a finite
abscissa of convergence. Equation (L-99303.10) gives the contradiction.

This closes the analytic interface more explicitly than the abbreviated
Landau paragraph in `L-99300` and permits subpolynomial, rather than uniformly
bounded, resolved calibration.
