# A global dual certificate for an ordered two-arc optimizer

This is a deterministic theorem for the original twenty-coordinate
source. It turns a five-dimensional ordered-face root into a global
three-coordinate optimum if two explicit polynomial inequalities pass.
No numerical candidate or inequality is asserted here.

Let `theta_j` be the half-gradient coefficients of a candidate current.
In the literal moment order, the corresponding source one-form is

\[
 \alpha=P\,du+Q\,dv+R\,dw,
\]
\[
\begin{aligned}
P={}&\theta _1v+\theta _2w+\theta _4vw+\theta _6w^2
 +\theta _7v^2+\theta _8v^2w^2+\theta _{15}vw^2
 +\theta _{17}v^2w,\\
Q={}&\theta _3w+\theta _5uw+\theta _9w^2+\theta _{10}u^2
 +\theta _{11}u^2w^2+\theta _{16}uw^2+\theta _{19}u^2w,\\
R={}&\theta _{12}v^2+\theta _{13}u^2+\theta _{14}u^2v^2
 +\theta _{18}uv^2+\theta _{20}u^2v.
\end{aligned}                                                  \tag{1}
\]

Put

\[
 \Phi_K=\theta _{10}u^2v+wR-Kuw(1-v),\qquad K\geq0.
\]

A direct differentiation, retaining the endpoint potential, gives

\[
 \alpha-d\Phi_K={\cal A}_K\,du+w{\cal B}_K\,dv
                 +Ku(1-v)\,dw,                                  \tag{2}
\]
where

\[
\begin{aligned}
{\cal A}_K={}&(\theta _1-2\theta _{10}u)v+\theta _7v^2\\
&+w[\theta _2-2\theta _{13}u
 +(\theta _4-2\theta _{20}u)v
 +(\theta _{17}-\theta _{18}-2\theta _{14}u)v^2]\\
&+w^2(\theta _6+\theta _{15}v+\theta _8v^2)+Kw(1-v),             \tag{3}\\
{\cal B}_K={}&\theta _3+\theta _5u+(\theta _{19}-\theta _{20})u^2
 -2v(\theta _{12}+\theta _{18}u+\theta _{14}u^2)\\
&+w(\theta _9+\theta _{16}u+\theta _{11}u^2)-Ku.                \tag{4}
\end{aligned}
\]

These identities explain the correction: it charges motion through the
interior without changing a path on `w=0` followed by `v=1`.

Define the two scalar profile quadratics

\[
 q_v(u,z)=(\theta _1-2\theta _{10}u)z+\theta _7z^2,
\]
\[
 q_w(u,z)=(\theta _2+\theta _4+\theta _{17}-\theta _{18}
 -2u(\theta _{13}+\theta _{14}+\theta _{20}))z
 +(\theta _6+\theta _8+\theta _{15})z^2.                         \tag{5}
\]

Assume their quadratic coefficients are strictly positive. Let
`f(u)` and `g(u)` be their unique clipped-affine minimizers on `[0,1]`,
and set

\[
 m(u)=\min\{q_v(u,f(u)),\ q_v(u,1)+q_w(u,g(u))\}.                 \tag{6}
\]

Suppose the following two inequalities are certified on the whole unit
cube:

\[
 {\cal B}_K(u,v,w)\geq0,\qquad {\cal A}_K(u,v,w)\geq m(u).        \tag{7}
\]

If the two entries in (6) have one ordered crossing `t`, use the completed
monotone graph that follows `(u,f(u),0)` up to `t`, completes `v`
vertically at fixed `u=t`, raises `w` to `g(t)` at fixed `v=1`, and then
follows `(u,1,g(u))`; endpoint vertical pieces complete all coordinates.
It is a global minimizer of the linear functional `integral alpha` over
**all** completed coordinatewise monotone paths.

Indeed (2), monotonicity and (7) give

\[
 \int_\gamma\alpha\geq\Phi_K(1,1,1)-\Phi_K(0,0,0)+\int_0^1m(u)du.
\]

Every residual vanishes on the displayed path, including both vertical
pieces, so equality holds. No assumption that the two profiles meet
continuously is needed.

Finally suppose `theta` is the physical Gram half-gradient of the same
candidate. For any legal competitor with current difference `Delta F`,

\[
 E(\gamma)-E(\gamma_*)=2\int_{\gamma-\gamma_*}\alpha
                       +\|\Delta F\|_{L^2(\nu)}^2\geq0.           \tag{8}
\]

Thus (7) promotes the linear support certificate to a global minimizer of
the original quadratic energy. Faithfulness makes its observed source
vector unique. It does not by itself prove a unique parametrized path.

For exact certification, (4) is quadratic in `u` and affine in `v,w`, so
its endpoints and any rationally enclosed interior vertex suffice.
After splitting `u` at the clipping points and crossing in (6), subtracting
the relevant branch from (3) leaves a quadratic in `w`; it can be removed
exactly. Here is a useful certificate contract. Write

`Lv=theta1-2 theta10 u`, `cv=theta7`, and in the early branch write
`A_K-q_v(u,f)=cv(v-f)^2+w p+w^2 q`. Then, according as

1. `p>=0`, no further inequality is needed;
2. `-2q<=p<0`, prove `q(2cv v+Lv)^2-cv p^2>=0`;
3. `p<-2q`, prove `(2cv v+Lv)^2+4cv(p+q)>=0`.

For the late branch put `x=1-v`, `Lw` for the linear coefficient in
`q_w`, and write

`A_K-[q_v(u,1)+q_w(u,g)]=C w^2+L w+N0/(4cw)`,

where `C=cw+x H2`, `L=Lw+x H1`, and
`N0=Lw^2+4cw x H0` are obtained by polynomial division in `x`.
According as `L>=0`, `-2C<=L<0`, or `L<-2C`, prove respectively

`N0>=0`, `C N0-cw L^2>=0`, or
`N0+4cw(L+C)>=0`.

Thus every gate is only a low-degree bivariate polynomial in `(u,v)`.
Directed Bernstein subdivision or Sturm isolation can prove it. A grid
cannot.

The theorem concerns the fixed-prime source and original Mellin norm. It
does not assert that an ordered candidate passes (7), extend to varying
prime sets, or identify a retained-gamma family.
