# L-100300 — Exact cellwise coarea for the quadratic critical deficit

Claim ID: `L-100300`  
Status: **PROVED EXACT REAL-VARIABLE REDUCTION**  
Created: 2026-08-20  
Depends on: PR #679 `T100200`; PR #681 `L-100160--L-100163`  
RH status: **not assumed**

Use the finite-cell notation of PR #679. On one activation cell let

\[
S_\sigma=\sum_{P_A\le y}(-1)^{|A|}P_A^{-\sigma},
\qquad
\overline S_{3/2}=\Delta-S_{3/2},
\]

where all three quantities are constant on the open cell. The quadratic
upper-envelope packet is

\[
\boxed{
\mathcal E(y)
=16\overline S_{3/2}+24S_1y^{-1/2}-9S_{1/2}y^{-1}.
}
\tag{L-100300.1}
\]

Put \(t=\sqrt y\) and write

\[
A=16\overline S_{3/2},\qquad B=24S_1,\qquad C=-9S_{1/2}.
\]

Then

\[
\boxed{t^2\mathcal E(t^2)=P(t):=At^2+Bt+C.}
\tag{L-100300.2}
\]

Hence the negative set on a cell is obtained by intersecting its \(t\)-interval
with the at-most-two components of \(\{P(t)<0\}\). No numerical minimization is
needed.

For every connected negative component \((\alpha,\beta)\), direct integration
gives

\[
\boxed{
\int_{\alpha^2}^{\beta^2}[-\mathcal E(y)]\,\frac{dy}{y}
=
\left[-2A\log t+\frac{2B}{t}+\frac{C}{t^2}\right]_{\alpha}^{\beta}.
}
\tag{L-100300.3}
\]

Indeed, the derivative of the bracket is
\(2[-\mathcal E(t^2)]/t\).

In the only sector admitting an interior minimum,

\[
S_1=-u<0,\qquad S_{1/2}=-v<0,
\]

formula (L-100300.1) becomes

\[
\mathcal E(t^2)=16T-\frac{24u}{t}+\frac{9v}{t^2},
\qquad T=\overline S_{3/2}.
\tag{L-100300.4}
\]

If \(T>0\), the negative interval is nonempty exactly when

\[
u^2-Tv>0,
\tag{L-100300.5}
\]

and its untruncated roots are

\[
\boxed{t_\pm=\frac{3}{4T}\left(u\pm\sqrt{u^2-Tv}\right).}
\tag{L-100300.6}
\]

Thus the pointwise Turán gate of PR #679 is the zero-deficit special case of
the exact logarithmic area formula above.

Activation jumps occur at a set of logarithmic measure zero. They affect the
initial value of the next cell but contribute no separate atom to
\(\int(\mathcal E)_-\,dy/y\). Therefore, after summing (L-100300.3) over all
activation cells up to \(Y\),

\[
\boxed{
\mathfrak D(Y):=\sum_{\text{cells }I\subset[1,Y]}\mathfrak D_I
=\int_1^Y(\mathcal E(y))_-\,\frac{dy}{y}.
}
\tag{L-100300.7}
\]

This replaces the stronger pointwise gate `PATG100200` by a completely explicit
one-sided coarea quantity. Every cell contribution is an elementary expression
in the three native moments and the two activation endpoints.
