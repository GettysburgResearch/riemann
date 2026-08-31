# Architecture E addendum: Loewner decomposition and a total-positivity sum firewall

Status: **PROVED ALGEBRAIC/ANALYTIC LEMMAS; RH REMAINS UNPROVED.**

This addendum sharpens two interfaces in
[`XI_SOURCE_HERMITE_STIELTJES_CLOSURE.md`](XI_SOURCE_HERMITE_STIELTJES_CLOSURE.md).
First, it identifies the safe Pick kernel as an exact difference of two
Loewner matrices.  Second, it rules out a tempting shortcut from
termwise Pólya-frequency kernels to the completed theta sum: positive
linear combinations do not preserve `PF_infinity` in general, and the
relevant theta sum has an explicit Gamma-zeta transform whose nonreal zeros
make the failure unavoidable.

No numerical zero location is used.  The only zeta input in the firewall is
the classical existence of nontrivial zeros.

## 1. Safe kernel as a Loewner difference

Retain

\[
 Y(x)=\xi_{\rm R}(1/2+x),\qquad
 F(x)=Y'(x)/Y(x),\qquad
 p(t)=F(\sqrt t)/\sqrt t.
\]

For positive nodes `x_i` put `t_i=x_i^2`, and for any scalar function `h`
write its Loewner matrix

\[
 L_h[\mathbf t]_{ij}=
 \begin{cases}
 \dfrac{h(t_i)-h(t_j)}{t_i-t_j},&i\ne j,\\[1.2ex]
 h'(t_i),&i=j.
 \end{cases}
\]

Let `D_x=diag(x_1,...,x_N)`.  The safe Pick matrix is

\[
 {\cal H}[\mathbf x]_{ij}
 =\frac{F(x_i)+F(x_j)}{x_i+x_j}
 =\frac{x_i p(t_i)+x_jp(t_j)}{x_i+x_j}.
\]

A direct divided-difference calculation gives

\[
 \boxed{\qquad
 {\cal H}[\mathbf x]
 =L_{tp}[\mathbf t]-D_xL_p[\mathbf t]D_x.
 \qquad}
 \tag{EL1}
\]

For `i ne j`, the numerator of the right side is

\[
 t_ip(t_i)-t_jp(t_j)-x_ix_j(p(t_i)-p(t_j))
 =(x_i-x_j)(x_ip(t_i)+x_jp(t_j)),
\]

and division by
`t_i-t_j=(x_i-x_j)(x_i+x_j)` proves the identity.  On the diagonal,

\[
 (tp)'(t_i)-x_i^2p'(t_i)=p(t_i),
\]

which is the diagonal of the safe kernel.

Thus the sufficient all-order Loewner target is

\[
 -L_p[\mathbf t]\succeq0,
 \qquad
 L_{tp}[\mathbf t]\succeq0
 \tag{EL2}
\]

for every finite positive packet.  Under (EL2), both terms on the right of
(EL1) are positive semidefinite.

## 2. Stieltjes functions give both Loewner squares

If

\[
 p(t)=\int_0^\infty\frac{d\mu(r)}{t+r},\qquad \mu\ge0,
 \tag{EL3}
\]

then

\[
 -L_p[\mathbf t]_{ij}
 =\int_0^\infty
 \frac{d\mu(r)}{(t_i+r)(t_j+r)},
 \tag{EL4}
\]

and

\[
 L_{tp}[\mathbf t]_{ij}
 =\int_0^\infty
 \frac{r\,d\mu(r)}{(t_i+r)(t_j+r)}.
 \tag{EL5}
\]

Both are Gram matrices.  Substitution in (EL1) recovers the two-channel
factorization

\[
 {\cal H}_{ij}
 =\int_0^\infty
 \frac{r+x_ix_j}{(x_i^2+r)(x_j^2+r)}\,d\mu(r).
 \tag{EL6}
\]

In standard operator-monotone terminology, a nonnegative Stieltjes function
is operator monotone decreasing on the positive half-line, while `t p(t)` is
a complete Bernstein function and is operator monotone increasing.  Equations
(EL4)--(EL5) are the source-exact finite-matrix content needed here; no appeal
to terminology is necessary.

The identity also clarifies the low-order frontier.  Scalar monotonicity of
`p` and `tp` pays only the two-node Loewner inequalities.  Matrix monotonicity
at every order is the Stieltjes completion, hence—by the closure note—the RH
endpoint.  A fixed low order must not be promoted to the all-order statement.

## 3. Positive sums of PF-infinity kernels: exact counterexample

Fix real `nu>0` and distinct positive `alpha,beta`.  Define

\[
 f_\alpha(x)=\exp(-\nu x-\alpha e^{-x}),\qquad x\in\mathbb R.
 \tag{TP1}
\]

Its bilateral Laplace transform, with the convention
`Bf(s)=integral_R f(x)e^{-sx}dx`, is

\[
 \boxed{\qquad
 {\cal B}f_\alpha(s)
 =\Gamma(s+\nu)\alpha^{-(s+\nu)},
 \qquad \Re(s+\nu)>0.
 \qquad}
 \tag{TP2}
\]

This follows from `y=e^{-x}`.  The reciprocal

\[
 \frac{\alpha^{s+\nu}}{\Gamma(s+\nu)}
\]

is a real translate and zero-free exponential multiple of `1/Gamma`, whose
canonical product has only the real zeros `s=-nu,-nu-1,...`.  Hence each
`f_alpha` is a classical `PF_infinity` kernel.

The positive sum has transform

\[
 {\cal B}(f_\alpha+f_\beta)(s)
 =\Gamma(s+\nu)
 \left(\alpha^{-(s+\nu)}+\beta^{-(s+\nu)}\right).
 \tag{TP3}
\]

The parenthesis vanishes whenever

\[
 s+\nu=
 \frac{(2k+1)\pi i}{\log(\beta/\alpha)},
 \qquad k\in\mathbb Z.
 \tag{TP4}
\]

These are nonreal zeros.  A bilateral Laplace transform of an integrable
`PF_infinity` function has the Schoenberg form `E/Psi`, with `E` zero-free
and `Psi` Laguerre--Pólya; in particular its meromorphic continuation has no
zeros.  Therefore

\[
 \boxed{\quad
 f_\alpha,f_\beta\in PF_\infty,
 \qquad
 f_\alpha+f_\beta\notin PF_\infty.
 \quad}
 \tag{TP5}
\]

Thus `PF_infinity` is not closed under arbitrary positive linear
combinations.  Closure under convolution and locally uniform limits of an
already totally-positive sequence does not imply closure under addition.

## 4. Application to the primitive-cycle theta sum

The logarithmic theta kernel in Watson,
*The Riemann Xi-function from primitive Markovian cycles I: A canonical
construction*, arXiv:2602.01248, is stated in the form

\[
 \Phi_W(x)=C_0 e^{-3x/4}
 \sum_{m\in\mathbb Z\setminus\{0\}}
 e^{-\alpha m^2e^{-x}},
 \qquad C_0,\alpha>0.
 \tag{TP6}
\]

Termwise use of (TP2), justified on the absolute-convergence half-plane,
gives the exact transform

\[
 \boxed{\quad
 {\cal B}\Phi_W(s)
 =2C_0\Gamma(s+3/4)\alpha^{-(s+3/4)}
 \zeta(2s+3/2),
 \qquad \Re s>-1/4.
 \quad}
 \tag{TP7}
\]

The cited manuscript proves each summand `PF_infinity` and then invokes
closure under positive linear combinations.  Equation (TP5) shows that
closure step is invalid.  More decisively, analytic continuation of (TP7)
has a nonreal zero at

\[
 s=(\rho-3/2)/2
\]

for every nontrivial zeta zero `rho`; the Gamma and exponential factors do
not vanish.  Since nontrivial zeta zeros are known to exist, `Phi_W` cannot
be an integrable `PF_infinity` function.  This conclusion is independent of
RH: even a critical-line zero gives a nonreal zero in the `s`-plane above.

The Archimedean completion and Mellin identification in that manuscript are
separate calculations; this firewall addresses only the asserted
`PF_infinity` closure and the proposed Laguerre--Pólya bridge.

## 5. Consequence for Architecture E

Termwise total positivity of theta atoms cannot supply the source positivity
in Architecture E.  The arithmetic mode sum is exactly where the zeta factor
and its zero divisor enter.  The viable theorem remains the polarized
positivity

\[
 {\cal A}_\Phi\succeq0,
\]

or equivalently the all-order Loewner/Stieltjes condition of Sections 1--2.
Any proof must control the complete coupled theta sum; it cannot obtain the
result by summing modewise `PF_infinity` certificates.
