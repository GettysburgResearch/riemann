# Open stability and quantitative control of near-optimal native paths

This proof-only corollary starts from the actual H25 clipped-path
discovery frozen at `a10385170ae8d1555299b6e1ed981e44c5d1c6e5`.
That packet certifies a self-consistent root, positive source Gram matrix,
strict support margins, and the strict lower-clipped/non-upper-clipped
regime. The arguments below do not rerun its Newton or interval jobs.

Keep the same six native coordinates `x=(A,B,C/2,D,E,F)` and the same
actual monotone-path source class. Write

\[
 I_\theta(x)=c_0+2g^tx+x^tGx,\qquad G=G^t>0.
\]

Perturbing `(c_0,g,G)` below means perturbing coefficients of a quadratic
on this fixed source chart. No claim is made that every such perturbation
comes from an arithmetic measure, changes the prime labels naturally, or
extends the chart to larger horizons. Any admissible perturbation of the
original physical kernel which induces sufficiently nearby coefficients
is covered as a special case.

## 1. Source-derived nondegeneracy of self-consistency

For a strict nonempty clipping band `(u_0,u_1)`, let

\[
 v_*(u)=\operatorname{clip}(\lambda+\mu u,0,1),\quad
 x(\lambda,\mu)=(A,B,C/2,0,0,0),\quad L=g+Gx.
\]

The final activation of `w` is at `(u,v)=(1,1)`. Define

\[
 F(\lambda,\mu;\theta)=
 \begin{pmatrix}L_0+\lambda L_2\\L_1+\mu L_2\end{pmatrix},
 \quad
 M=\int_{u_0}^{u_1}
       \begin{pmatrix}1&u\\u&u^2\end{pmatrix}\,du,
 \quad
 N=\begin{pmatrix}1&0\\0&1\\\lambda&\mu\\0&0\\0&0\\0&0\end{pmatrix}.
                                                               \tag{1}
\]

The matrix `M` is positive definite because the band has positive length.
Differentiating the exact clipped moments gives

\[
 D_{(\lambda,\mu)}x=NM.                              \tag{2}
\]

The moving endpoint terms cancel: at a lower clip the graph equals0,
and at an upper clip the active graph equals the adjacent constant1.
The three nonzero rows in(2) are respectively
`(integral1,integral u)`, `(integral u,integral u^2)`, and
`(integral v_*,integral u v_*)`, all over the band. This also checks
the `C/2` convention.

Since `F=N^tL`, its Jacobian is

\[
 J_F=L_2 I_2+N^tGNM,\qquad
 MJ_F=L_2M+MN^tGNM.                                  \tag{3}
\]

If the source coefficient `c=L_2/2` is positive, the last matrix is
positive definite. Thus the self-consistency Jacobian is nonsingular.
This is a consequence of the actual moment derivatives and positivity;
it is not inferred solely from a small numerical residual or from the
chosen preconditioner in one interval computation.

## 2. An open family of actual globally optimal paths

Within a fixed strict clipping regime the moments are real-analytic
functions of `(lambda,mu)`: their formulas involve polynomial primitives
and the rational breakpoints `-lambda/mu` and `(1-lambda)/mu` where used.
Equations(1)--(3) and the implicit function theorem therefore give a
unique nearby real-analytic root `(lambda(theta),mu(theta))` for every
sufficiently small coefficient perturbation around the frozen root.

Positive definiteness of `G`, positive `c`, and the strict margins

\[
 f=L_5>0,\qquad
 \kappa=\min(L_3+L_4/2,L_3+L_4)>0                    \tag{4}
\]

persist on a smaller neighborhood. So do the strict lower-clipping and
terminal-height inequalities. The same source support theorem proves
that each of these nearby roots is an all-path global minimum, with a
unique optimal source-coordinate vector. Its parameters, moments and
minimum energy depend real-analytically on the coefficients there.

This is a local theorem. It supplies neither a numerical radius for that
coefficient neighborhood nor a claim that no clipping or support-cone
transition occurs under a larger perturbation. A nearby admissible
physical kernel inherits the result only after its coefficient change
is controlled in this fixed source chart.

## 3. A coercive bound for every competing actual path

Fix one of these strictly certified optima and set
`(a,b,c,d,e,f)=(L_0,L_1,L_2/2,L_3,L_4,L_5)` at that optimum.
For a general competitor,
represent the planar graph by a monotone `v(u)`; its values at vertical
segments do not affect integrals against `du`. The pointwise quadratic
projection inequality gives

\[
 \int_0^1[c v^2+(a+bu)v]\,du-J_*
       \ge c\int_0^1|v(u)-v_*(u)|^2\,du.             \tag{5}
\]

This includes clipped portions, where the projection's first-order
residual is nonnegative. Every monotone path has `D>=0`, `F>=0` and
`D/2<=E<=D`. Therefore the exact energy identity implies

\[
 I(x)-I(x_*)\ge (x-x_*)^tG(x-x_*)
       +2c\int_0^1|v-v_*|^2\,du+2\kappa D+2fF.       \tag{6}
\]

All terms on the right are nonnegative. In particular, if the energy
excess is at most `epsilon`, then

\[
 \|x-x_*\|_G\le\sqrt\epsilon,\qquad
 \int_0^1|v-v_*|^2\,du\le\frac\epsilon{2c},\qquad
 D+F\le\frac\epsilon{2\min(\kappa,f)}.               \tag{7}
\]

No new lower eigenvalue estimate is needed for the stated `G`-norm.
An independently certified lower eigenvalue would additionally convert
it into a Euclidean coordinate bound.

## 4. Where activation mass and the planar graph must concentrate

Integration by parts identifies the probability measure `dw` with

\[
 D=\int(1-u)\,dw,\qquad F=\int(1-v)\,dw.
\]

For every `eta>0`,(7) gives

\[
 \int_{\{u\le1-\eta\}\,\cup\,\{v\le1-\eta\}}dw
       \le\frac\epsilon{2\eta\min(\kappa,f)}.        \tag{8}
\]

Thus a near-minimizer can put only this much activation mass outside
the indicated final planar corner. This concerns one actual path's
activation measure, not a convex mixture of observed fields.

The profile bound also controls graph values away from the planar
endpoints. Fix `0<delta<=1/2` and put
`e_v=integral_0^1|v-v_*|^2 du`. At any oriented planar point whose
u-coordinate lies in `[delta,1-delta]`, let `h=|v-v_*(u)|`.
Monotonicity of `v` and the Lipschitz constant `mu` of `v_*` imply

\[
 e_v\ge\frac{h^2}{4}\min\left(\frac h{2\mu},\delta\right).
\]

For a positive discrepancy use the interval to its right; for a
negative discrepancy use the interval to its left. Over the displayed
length the discrepancy remains at least `h/2`. Vertical values are
handled by the same one-sided monotonicity argument. Consequently

\[
 |v-v_*(u)|\le
 \max\left\{
        \left(\frac{4\mu\epsilon}{c}\right)^{1/3},
        \left(\frac{2\epsilon}{c\delta}\right)^{1/2}
      \right\}
 \quad(\delta\le u\le1-\delta).                      \tag{9}
\]

These are quantitative near-optimality estimates in source coordinates,
oriented planar geometry and activation mass. They do not control an
arbitrary clock parameter: monotone reparameterizations and pauses leave
the source unchanged. The terminal vertical completion is deliberately
excluded from the interior graph comparison. The constants can be chosen
uniformly on a sufficiently small closed neighborhood of coefficients
where(4), positive `c` and the clipping inequalities retain margins.

## 5. A nonnegative second-order error bound for a rational witness

Let the nearby actual final-activation path have the rational profile
`q(u)=clip(lambda_0+mu_0 u,0,1)`, with `mu_0>=0`; let
`p(u)=v_*(u)`. Set `delta_lambda=lambda_0-lambda_*` and
`delta_mu=mu_0-mu_*`. Both paths have `D=E=F=0`. The following estimate
allows different clipping breakpoints and needs no second derivative
bound for those moving breakpoints.

For real targets `y_0` and `y_*`, the projection inequality for
`q=clip(y_0)` implies `(q-p)(q-y_0)<=0`. Therefore

\[
\begin{split}
 0&\le(q-y_*)^2-(p-y_*)^2\\
  &=2(q-p)(q-y_0)+2(q-p)(y_0-y_*)-(q-p)^2\\
  &\le(y_0-y_*)^2.                                  \tag{10}
\end{split}
\]

Integrating(10) gives

\[
 0\le\ell(x_0)-\ell(x_*)
    \le c\left(\delta_\lambda^2+
          \delta_\lambda\delta_\mu+
          \frac{\delta_\mu^2}{3}\right).              \tag{11}
\]

Projection is also nonexpansive: `|q-p|<=|y_0-y_*|`. If the certified
parameter box gives `|delta_lambda|<=R_lambda` and
`|delta_mu|<=R_mu`, define the nonnegative rational bounds

\[
 \eta=R_\lambda^2+R_\lambda R_\mu+R_\mu^2/3,\qquad
 r=\left(R_\lambda+R_\mu/2,
          R_\lambda/2+R_\mu/3,
          R_\lambda+R_\mu/2\right).                  \tag{12}
\]

The three changed physical source coordinates satisfy
`|Delta x_i|<=r_i`. For `A` and `B`, integrate respectively
`|q-p|` and `u|q-p|`. For `C/2`, use
`|(q^2-p^2)/2|<=|q-p|`. The exact original quadratic identity now yields

\[
 0\le I(x_0)-I(x_*)
    \le 2c\eta+\sum_{0\le i,j<3}|G_{ij}|r_i r_j.    \tag{13}
\]

For the frozen isotropic box of radius `R=2^-30`, this becomes

\[
 I(x_0)-I(x_*)\le R^2\left[
       \frac{14c}{3}+\sum_{0\le i,j<3}|G_{ij}|s_i s_j
     \right],\qquad s=(3/2,5/6,3/2).                 \tag{14}
\]

Certified rational upper bounds for `c` and the absolute Gram entries
can be substituted directly into(13) or(14). This produces a nonnegative
source-faithful error bound of second order in the certified parameter
radius. It does not interpret a negative lower endpoint from subtracting
two energy enclosures as a negative actual excess. No numerical value
for this additional bound is claimed without its separate evaluation.

No numerical metric-stability radius, new replay, all-height optimum or
retained-gamma identification is asserted by this proof-only corollary.
