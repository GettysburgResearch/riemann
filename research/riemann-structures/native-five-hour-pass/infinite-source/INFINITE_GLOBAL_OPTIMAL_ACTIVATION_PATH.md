# The global optimal activation path for the original infinite observation

**Status: source-exact, post-registered continuum certificate.** The
preregistration deviation is recorded explicitly in
`variational_QUADRATIC_DUAL_PREREGISTRATION.md`.

This theorem is conditional only on the authenticated directed artifacts
named below. It concerns the fixed primes `2,3,5`, the literal twenty
source moments, and the original `L^2(nu)` physical norm.

## 1. The path and its physical self-consistency

There is a unique root in the directed five-dimensional box recorded by
`variational_ordered_dual_refutation.verification.json`. Approximately,

\[
(\lambda_v,\mu_v,\lambda_w,\mu_w,t)=
(-.0823330570,1.1226168381,-.5082335933,.5775184400,.9383761444).
\]

Let `f(u)=clip(lambda_v+mu_v u)` and
`g(u)=clip(lambda_w+mu_w u)`. Follow `(u,f(u),0)` until `u=t`, complete
`v` vertically, raise `w` vertically to `g(t)`, then follow
`(u,1,g(u))`; complete `w` at the endpoint. This is a legal completed
coordinatewise monotone path, including its vertical pieces.

Its twenty literal moments are the seven-column affine current in
`variational_ORDERED_DUAL_THEOREM.md`. The four profile equations are
the exact original-physical self-consistency equations and identify
`f,g` as the corresponding clipped minimizers. The fifth says that the
two pointwise branch costs agree at the switch. Its directed energy is
about `179.358344`.

## 2. A nonlinear source-owned calibration

Let `theta` be the candidate's half-gradient and let `R` denote the
`dw` coefficient of its literal source one-form. Use

\[
 \Phi=\theta_{10}u^2v+wR-3u^2w(1-v).                 \tag{1}
\]

Exact differentiation gives

\[
 \alpha-d\Phi={\cal A}\,du+w{\cal B}\,dv+3u^2(1-v)\,dw.          \tag{2}
\]

The polynomials `A,B` are those of the ordered-dual theorem with
`K` replaced by `6u` in `A` and by `3u^2` in `B`. The directed
certificate proves on the entire cube that

\[
 {\cal B}\geq0,qquad
 {\cal A}\geq\min\{q_v(u,f(u)),q_v(u,1)+q_w(u,g(u))\}.             \tag{3}
\]

The first inequality has a certified lower bound greater than `.1267`.
The quadratic coefficient in `w` is greater than `2.43`.

No grid enters (3). The producer removes `w` exactly. It separately
checks the lower-clipped `f=0` region, the unclipped early region, and
the late region. The early quadratic cases use `p`, `p+2q`, and their
directed vertex numerator. In the late region the `w=0` numerator is
the exact calibrated square

\[
 4c_wc_v(x-r_0)^2+rQ(r,x),\qquad r=u-t, x=1-v,                    \tag{4}
\]

with `Q>=0`; the vertex numerator has the exact factor `x`. The fifth
root equation sets the sole early calibrated constant to zero. Every
other coefficient remains an outward Arb interval. Bernstein ranges
certify 1 clipped cell, 35 early cells and 45 late cells, to maximum
depth 17, well below the declared cap. Independent rational holdouts
check the degree of every interpolated polynomial. The initial output
which omitted the lower-clipped interval is retained under an explicit
`invalid_...` filename and is not used.

Here the late quadratic coefficient `C` is exactly the same positive
profile polynomial `q(v)` whose strict lower bound is certified on the
whole interval. Thus the late vertex elimination never divides by an
uncertified sign.

## 3. Global optimality

Integrating (2) on any completed monotone path and using (3) gives the
same lower bound as the two scalar pointwise branch minima. On the path
above every residual vanishes: `w=0` on its first arc, `v=1` on its
second, and the branch values agree at the vertical switch. It therefore
minimizes the linear source functional defined by `theta` over **all**
legal monotone paths.

For any competitor with current difference `Delta F`, the original
physical energy identity is

\[
 E(\gamma)-E(\gamma_*)=2\int_{\gamma-\gamma_*}\alpha
                         +\|\Delta F\|_{L^2(\nu)}^2\geq0.          \tag{5}
\]

Thus this path is a global minimizer of the original infinite physical
energy. The positive infinite frame makes its twenty-coordinate observed
source vector unique. This proof does not assert uniqueness of a chosen
parametrization or exclude source paths with the same twenty moments.

## 4. Exact scope and dependencies

The physical Gram and all-horizon frame packet is frozen at
`a454106bd685d618f61231549e6fd99bf5b5a1ad`. The variational base is
frozen at `4218c3c15`; the five-dimensional ordered root and refutation
packet is frozen at `b3624ed2d467ff4d1ec2581e6ff0f7ac442f8cd2`.
The quadratic producer authenticates their exact LF hashes before use.

The theorem is an infinite-horizon fixed-prime source result. Persistence
of the same support type at a finite horizon requires a separate
quantitative perturbation certificate. It does not identify the full
post-renewal retained-gamma family, vary the primes, or imply a statement
about zeros of the zeta function.
