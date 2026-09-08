# L-91411 — The completed finite Gamma–Beta reservoir has a dimension-free spectral gap at least one half

Claim ID: `L-91411`  
Status: **EXACT FINITE-DIMENSIONAL BAKRY–EMERY THEOREM**  
Created: 2026-08-12  
Depends on: PR #401 `L-91107`; `L-91409`  
RH status: **unproved**

## 1. Conditioned completed Beta law

Fix an integer `m>=1`, positive weights `w_1,...,w_m`, and put

\[
 A=\sum_{i=1}^m w_i,
 \qquad
 D(v)=\sum_{i=1}^m w_iv_i.
\]

On `(-1,1)^m`, let

\[
 d\mu_w(v)
 =Z_w^{-1}(A^2-D(v)^2)^{1/4}
  \prod_{i=1}^m\frac34(1-v_i^2)\,dv_i.
\tag{L-91411.1}
\]

This is exactly the finite BPY two-copy Beta reservoir after conditioning on the Gamma variables, since the completed half-size tilt is `(A^2-D^2)^(1/4)`.

Its reversible Dirichlet form is

\[
 \mathcal E_w(f,f)
 =\frac14\sum_i
  \int(1-v_i^2)|\partial_{v_i}f|^2d\mu_w.
\tag{L-91411.2}
\]

## 2. Euclidean angular coordinates

Write

\[
 v_i=\sin\theta_i,
 \qquad
 -\frac\pi2<\theta_i<\frac\pi2,
\]

and normalize

\[
 \alpha_i=\frac{w_i}{A},
 \qquad
 d(\theta)=\frac DA=\sum_i\alpha_i\sin\theta_i.
\]

Up to a constant, the angular density is `exp(-U(theta))`, where

\[
 \boxed{
 U(\theta)
 =-3\sum_i\log\cos\theta_i
  -\frac14\log(1-d(\theta)^2).
 }
\tag{L-91411.3}
\]

Moreover

\[
 \mathcal E_w(f,f)
 =\frac14\int|\nabla_\theta f|^2d\mu_w.
\tag{L-91411.4}
\]

## 3. Uniform Hessian lower bound

Put

\[
 g(d)=-\frac14\log(1-d^2).
\]

Then

\[
 g'(d)=\frac{d}{2(1-d^2)},
 \qquad
 g''(d)=\frac{1+d^2}{2(1-d^2)^2}>0.
\]

The Hessian of `U` is

\[
\begin{aligned}
 \nabla^2U
={}&3\,\operatorname{diag}(\sec^2\theta_i)\\
&+g''(d)aa^T
-g'(d)\operatorname{diag}(\alpha_i\sin\theta_i),
\end{aligned}
\tag{L-91411.5}
\]

where `a_i=alpha_i cos(theta_i)`.

The rank-one term is positive. It remains to control the possibly negative diagonal term. Suppose first that `d sin(theta_i)>0` and `d>=0`. Since

\[
 \alpha_i\cos^2\theta_i
 \le2\alpha_i(1-\sin\theta_i)
 \le2(1-d),
\]

\[
 \frac{d\alpha_i\sin\theta_i\cos^2\theta_i}
      {2(1-d^2)}
 \le\frac d{1+d}\le1.
\tag{L-91411.6}
\]

For `d<=0`, use instead

\[
 \alpha_i\cos^2\theta_i
 \le2\alpha_i(1+\sin\theta_i)
 \le2(1+d)
\]

to obtain the same bound. If `d sin(theta_i)<=0`, the diagonal contribution is nonnegative already.

Thus, in every coordinate,

\[
 -g'(d)\alpha_i\sin\theta_i
 \ge-\sec^2\theta_i.
\]

Consequently

\[
 \boxed{
 \nabla^2U(\theta)
 \succeq2\,\operatorname{diag}(\sec^2\theta_i)
 \succeq2I_m.
 }
\tag{L-91411.7
}

The estimate is uniform in the dimension and in all positive weights.

## 4. Uniform Poincare and Poisson bounds

The Brascamp–Lieb/Bakry–Emery inequality applied to (L-91411.7) gives

\[
 \operatorname{Var}_{\mu_w}(f)
 \le\frac12\int|\nabla_\theta f|^2d\mu_w
 =2\mathcal E_w(f,f).
\tag{L-91411.8}

Hence the self-adjoint generator associated with (L-91411.2) has spectral gap at least

\[
 \boxed{\lambda_w\ge\frac12.}
\tag{L-91411.9}
\]

If `g` has mean zero and `h` is the mean-zero Poisson solution

\[
 -\mathcal L_wh=g,
\]

then

\[
 \boxed{
 \|h\|_2\le2\|g\|_2,
 \qquad
 \mathcal E_w(h,h)
 =\langle g,(-\mathcal L_w)^{-1}g\rangle
 \le2\|g\|_2^2.
 }
\tag{L-91411.10}

## 5. Consequence for the Brownian/theta route

The finite completed Gamma–Beta Poisson problem of `L-91409` is therefore well posed with cutoff-uniform coercivity after conditioning on every Gamma reservoir. No spectral degeneration occurs as the number of Beta coordinates increases or the weights become uneven.

The remaining work is not existence or norm blow-up of the Poisson solution. It is the source-specific sign/factorization of the conditional boundary port

\[
 \mathbb E[\Gamma_w(h_Z,Z)\mid Z],
\]

and its identification with the theta variance reserve.

Passing from finite conditioned reservoirs to the infinite Gamma mixture requires the usual closability and uniform-integrability checks; no such passage or RH conclusion is asserted here.
