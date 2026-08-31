# Exact marked support beyond the coordinatewise final-activation cone

This is a proof-only refinement of the H25 occupation support reduction.
Its native input is the complete six-moment identity frozen at
`a75f3bbef5f75bb6a4bd7f3c91d051cfb132f3dc`. No coefficient fitting,
root isolation or numerical optimization is performed here. The current
clipped-path scout remains a separate declared experiment.

Write a linear occupation functional as

\[
 \ell=aA+bB+cC+dD+eE+fF,
 \qquad c>0,\quad b<0,\quad
 \alpha=-a/(2c),\quad\beta=-b/(2c)>0.
\]

Let `y(u)=alpha+beta u`, `omega=alpha+beta`, and
`v_*(u)=clip(y(u),0,1)`. With `w` activated at the final planar point,
the minimum planar cost is

\[
 J_* =\int_0^1[c v_*^2+(a+bu)v_*]\,du.
\]

Vertical endpoint segments complete `v_*` to the required endpoints;
they do not change this integral.

## 1. A formula that includes both endpoint clips

For a prescribed single activation at planar point `(s,t)` in the unit
square, the exact optimal planar graph is

\[
 v(u)=\begin{cases}
       \operatorname{clip}(y(u),0,t),&u<s,\\
       \operatorname{clip}(y(u),t,1),&u>s.
      \end{cases}
\]

Vertical segments at `u=s` retain the marked point and its activation
order. Since `y` is increasing, these pointwise minimizers are monotone.
Define `r_+=max(r,0)` and `y_s=alpha+beta s`. The exact excess over `J_*`
is

\[
\begin{split}
 \Delta(s,t)=\frac{c}{3\beta}\big[&|y_s-t|^3
       -(\alpha-t)_+^3-(t-\omega)_+^3\\
       &-(y_s-1)_+^3-(-y_s)_+^3
         +(\alpha-1)_+^3+(-\omega)_+^3\big].          \tag{1}
\end{split}
\]

This formula holds even when `y` is wholly outside `[0,1]`, or when its
crossing of the marked height lies outside the parameter interval. It
is not the unprojected quadratic-completion formula applied after an
endpoint clip was silently discarded.

To prove(1), subtract the original pointwise optimum. On the left the
excess integrand is

\[
 c[(y-t)_+^2-(y-1)_+^2],
\]

and on the right it is

\[
 c[(t-y)_+^2-(-y)_+^2].
\]

Both expressions are nonnegative on their respective domains. Integrate
with `dy=beta du` and combine the two cubic primitives. This proves(1)
and `Delta>=0` directly. In particular `Delta(1,1)=0`, including a
terminal vertical completion when `omega<1`.

## 2. An exact support criterion on a compact square

The single-activation reduction, proved by integration by parts against
the probability measure `dw`, gives the exact full linear support value

\[
 \inf_{\text{actual paths}}\ell
   =J_*+\min_{0\le s,t\le1}K(s,t),
 \qquad
 K(s,t)=\Delta(s,t)+d(1-s)+\frac e2(1-s^2)+f(1-t).    \tag{2}
\]

Thus the final-activation path with planar graph `v_*` minimizes this
linear functional if and only if `K>=0` throughout the square. The
minimum is attained. Formula(1) makes `K` a continuous piecewise cubic
on the finite polygonal subdivision cut out by

\[
 y_s=t,quad y_s=0,quad y_s=1,quad t=\alpha,quad t=\omega.
\]

This is a stronger test than separately requiring
`f>=0`, `d+e/2>=0`, and `d+e>=0`. Those three inequalities make the
activation cost nonnegative everywhere and hence suffice, but they can
fail while the actual planar correction compensates for the negative
activation term.

For example, take

\[
 (a,b,c,d,e,f)=(0,-1,1,-1/16,0,1),\qquad v_*(u)=u/2.
\]

The coordinatewise cone fails because `d<0`. Nevertheless, when
`t<=3/4`, the term `1-t` is at least `1/4`, while the possible negative
term has magnitude at most `1/16`. When `t>=3/4`, the right forced graph
has pointwise excess at least `(t-1/2)^2>=1/16`, since `y(u)<=1/2`.
Therefore `Delta>=(1-s)/16`, again giving `K>=0`. This is an exact
rational linear-functional example, not a new physical metric or a
claim about the numerical coefficients of the current native scout.

For each fixed `s`, `K` is convex in `t`. Indeed, differentiation yields

\[
 \partial_t\Delta=\frac c\beta\big[
 (t-y_s)|t-y_s|+(\alpha-t)_+^2-(t-\omega)_+^2\big],  \tag{3}
\]

or directly

\[
 \partial_t^2\Delta
   =2c\left(|\{u<s:y(u)>t\}|+
             |\{u>s:y(u)<t\}|\right)\ge0.
\]

Consequently each fixed-`s` minimizer is an endpoint or a solution of
`partial_t Delta=f`; all such equations are quadratic on their declared
pieces. In the interior piece `alpha<=t<=omega`, the root is

\[
 t=y_s+\operatorname{sgn}(f)\sqrt{\beta|f|/c},
\]

provided it lies in that piece and in `[0,1]`. Outside that piece one
must retain the other terms in(3), as well as endpoint solutions. This
does not supply a universal unchecked radical formula.

A future certified minimization may use the finite cubic pieces or
the convex one-variable reductions. It must still handle boundary
stationary points, zero coefficients, and positive-dimensional critical
loci; checking only isolated critical points is insufficient. No such
algorithm or exact-real coefficient oracle is claimed by this note.

## 3. What this certifies for the original quadratic

For the original physical coordinates `x=(A,B,C/2,D,E,F)`, write
`I(x)=c_0+2g.x+x^t G x`. At an actual trial source `x_*`, form its exact
gradient `lambda=2(g+G x_*)`. The occupation coefficients are

\[
 (a,b,c,d,e,f)=(\lambda_1,\lambda_2,\lambda_3/2,
               \lambda_4,\lambda_5,\lambda_6).        \tag{4}
\]

If the trial path is the final-activation clipped graph for these same
coefficients and(2) certifies `K>=0`, it minimizes the supporting linear
functional over every actual path. The exact identity

\[
 I(x)-I(x_*)=\lambda\cdot(x-x_*)
                  +(x-x_*)^tG(x-x_*)
\]

then proves the all-path quadratic minimum. Positive definite `G` gives
uniqueness of its source coordinates, not of the path parameterization.

Conversely, failure of this supporting-hyperplane certificate does not
by itself refute optimality on a possibly nonconvex attainable source
set. It refutes the proposed gradient-support certificate. Approximate
self-consistency or a finite grid of marked points is not a substitute
for the exact hypotheses above. No all-path numerical minimum is
asserted here, and no H25 source conclusion is promoted to all heights.
