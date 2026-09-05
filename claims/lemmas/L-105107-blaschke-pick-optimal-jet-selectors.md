# L-105107 — Blaschke–Pick optimal top-jet selectors

Claim ID: L-105107

Status: **PROPOSED EXACT FINITE-WINDOW THEOREM**

Created: 2026-08-23

Depends on: L-105103; L-105105; L-105106

RH status: **unproved**

## 1. The admissible selector class

Let \(\mathbb D=\{z:|z|<1\}\).  Fix distinct nodes \(S\subset\mathbb D\),
actual pole orders \(d_a\ge1\), a target set
\(\mathcal T\subseteq S\), and top-primary data \(\gamma_c\ne0\).  An
admissible bounded analytic selector satisfies

\[
W(z)\equiv\gamma_c(z-c)^{d_c-1}
 \pmod{(z-c)^{d_c}}
\quad(c\in\mathcal T)
\tag{L-105107.1}
\]

and

\[
W(z)\equiv0\pmod{(z-a)^{d_a}}
\quad(a\in S\setminus\mathcal T).
\tag{L-105107.2}
\]

As in L-105106, the orders are the complete post-cancellation pole orders
from L-105103.  The target data in L-105105 have precisely this top-primary
form.

## 2. Forced-inner factorization

Use the disk Blaschke factor

\[
b_a(z)=\frac{z-a}{1-\overline a z}.
\tag{L-105107.3}
\]

Define the forced zero orders

\[
n_a=
\begin{cases}
d_a,&a\notin\mathcal T,\\
d_a-1,&a\in\mathcal T,
\end{cases}
\qquad
N_0=\sum_{a\in S}n_a
=D-|\mathcal T|,
\tag{L-105107.4}
\]

and the finite inner function

\[
I_0(z)=\prod_{a\in S}b_a(z)^{n_a}.
\tag{L-105107.5}
\]

For a target \(c\), remove its forced factor and set

\[
I_{0,c}(z)=\frac{I_0(z)}{b_c(z)^{n_c}},
\qquad
\beta_c=
\left(\frac1{1-|c|^2}\right)^{n_c}I_{0,c}(c),
\qquad
y_c=\frac{\gamma_c}{\beta_c}.
\tag{L-105107.6}
\]

The derivative \(b_c'(c)=(1-|c|^2)^{-1}\) is load-bearing.

Every admissible selector has the unique factorization

\[
\boxed{W=I_0H,\qquad H(c)=y_c\quad(c\in\mathcal T),}
\tag{L-105107.7}
\]

with \(H\in H^\infty(\mathbb D)\).  Conversely every such \(H\) produces an
admissible \(W\).  This follows by dividing out exactly the zeros forced by
(L-105107.1)--(L-105107.2); the quotient has removable singularities.  At a
target,

\[
I_0(z)=\beta_c(z-c)^{d_c-1}+O((z-c)^{d_c}),
\tag{L-105107.8}
\]

so the single value \(H(c)=y_c\) supplies the required top coefficient.
Thus the confluent-looking selector problem reduces to ordinary value
interpolation at the targets.

Because \(I_0\) is inner,

\[
\|W\|_{H^\infty}=\|H\|_{H^\infty}.
\tag{L-105107.9}
\]

## 3. Exact Pick optimum

Enumerate the targets \(c_1,\ldots,c_t\), put

\[
K_{jk}=\frac1{1-c_j\overline{c_k}},
\qquad
D_y=\operatorname{diag}(y_{c_1},\ldots,y_{c_t}),
\tag{L-105107.10}
\]

and for \(u\ge0\) define

\[
\boxed{
P_u=u^2K-D_yKD_y^*
=\left[
\frac{u^2-y_{c_j}\overline{y_{c_k}}}
{1-c_j\overline{c_k}}
\right]_{j,k=1}^t.
}
\tag{L-105107.11}
\]

The classical finite Nevanlinna–Pick theorem and (L-105107.7) give

\[
\exists W\ {\rm admissible},\ \|W\|_\infty\le u
\quad\Longleftrightarrow\quad
P_u\succeq0.
\tag{L-105107.12}
\]

Consequently the exact optimum is

\[
\boxed{
\tau^2=
\lambda_{\max}\!\left(
K^{-1/2}D_yKD_y^*K^{-1/2}
\right).
}
\tag{L-105107.13}
\]

For nonempty \(\mathcal T\), \(\tau>0\), the matrix \(P_\tau\) is singular,
and the extremal \(H_*/\tau\) is the unique finite Blaschke solution of the
singular Pick problem.  It has degree at most \(t-1\).  Therefore

\[
W_*=I_0H_*,
\qquad
\|W_*\|_\infty=\tau,
\qquad
W_*/\tau\ {\rm is\ finite\ inner\ of\ degree\ at\ most}\ D-1.
\tag{L-105107.14}
\]

In particular, \(W_*\) is rational, has no pole on
\(\overline{\mathbb D}\), extends holomorphically past the unit circle, and
has constant boundary modulus

\[
|W_*(e^{i\theta})|=\tau.
\tag{L-105107.15}
\]

If the target set is empty, \(W_*=0\) and \(\tau=0\).

## 4. Single-target closed form

For \(\mathcal T=\{c\}\), the Pick problem has one value and
\(H_*\equiv y_c\).  Thus

\[
\boxed{
W_*=\frac{\gamma_c}{\beta_c}I_0,
\qquad
\tau=
|\gamma_c|(1-|c|^2)^{d_c-1}
\prod_{a\ne c}\rho(c,a)^{-d_a},
}
\tag{L-105107.16}
\]

where

\[
\rho(c,a)=|b_a(c)|
=\left|\frac{c-a}{1-\overline a c}\right|.
\tag{L-105107.17}
\]

Equation (L-105107.16) attains the Blaschke lower bound used in L-105106.
It also shows exactly what bounded analytic replacement can and cannot
improve: avoidable polynomial boundary growth disappears, while intrinsic
pseudohyperbolic coalescence remains.

For several targets, other targets enter the forced product with exponent
\(d_a-1\), not \(d_a\).  Their remaining interaction is exactly the full
Pick matrix, not its diagonal.

## 5. Transport to a regular window

Let \(\Omega\) be a bounded simply connected Jordan domain and
\(\phi:\Omega\to\mathbb D\) a conformal map.  Put

\[
\alpha_a=\phi(a),
\qquad
B_a(z)=b_{\alpha_a}(\phi(z)).
\tag{L-105107.18}
\]

Carathéodory extension makes \(\phi\) and every \(B_a\) continuous on
\(\overline\Omega\), with \(|B_a|=1\) on \(\partial\Omega\).  Replace
\(b_a\) by \(B_a\) in (L-105107.4)--(L-105107.7).  The target normalization
becomes

\[
\boxed{
\beta_c^\Omega=
\left(
\frac{\phi'(c)}{1-|\alpha_c|^2}
\right)^{d_c-1}
\prod_{a\ne c}
b_{\alpha_a}(\alpha_c)^{n_a}.
}
\tag{L-105107.19}
\]

The same Pick matrix is formed at the target images \(\alpha_c\), with
\(y_c^\Omega=\gamma_c/\beta_c^\Omega\).  Equations
(L-105107.11)--(L-105107.15) then give the exact optimum in

\[
A(\Omega)=\operatorname{Hol}(\Omega)\cap C(\overline\Omega).
\tag{L-105107.20}
\]

For one target, writing

\[
r_\Omega(c)=\frac{1-|\phi(c)|^2}{|\phi'(c)|},
\qquad
\rho_\Omega(c,a)=
|b_{\phi(a)}(\phi(c))|,
\tag{L-105107.21}
\]

gives

\[
\tau=
|\gamma_c|\,r_\Omega(c)^{d_c-1}
\prod_{a\ne c}\rho_\Omega(c,a)^{-d_a}.
\tag{L-105107.22}
\]

This quantity is conformally intrinsic.

No holomorphic extension of \(\phi\) through polygon corners is asserted.
For a rectifiable Jordan boundary, including a rectangle, the continuous
selector in (L-105107.20) is sufficient for the usual contour residue
formula.  Neighbourhood-of-closure holomorphy would require analytic boundary
or a separate extension argument.

## 6. Exact residue bridge and edge envelope

Assume in addition that \(\partial\Omega\) is rectifiable.

Let \(h\) be meromorphic in \(\Omega\), continuous on its boundary, with no
boundary pole and complete actual-pole manifest \((S,d)\).  Write

\[
q_c=\lim_{z\to c}(z-c)^{d_c}h(z).
\tag{L-105107.23}
\]

At a target,

\[
\operatorname{Res}_c(W_*h)=\gamma_cq_c,
\tag{L-105107.24}
\]

and every nontarget pole is removable after multiplication by \(W_*\).
Therefore

\[
\boxed{
\frac1{2\pi i}\int_{\partial\Omega}W_*(z)h(z)\,dz
=\sum_{c\in\mathcal T}\gamma_cq_c.
}
\tag{L-105107.25}
\]

Taking \(h=F/F'\), \(d_c=r_c\), and \(\gamma_c=1\) recovers the first
L-105105 jet moment.  Taking \(h=F^2/(F'F'')\),
\(d_c=2r_c-1\), and \(\gamma_c=r_c\) recovers the second moment.

On any boundary edge \(E\),

\[
\boxed{
\left|
\frac1{2\pi i}\int_EW_*h\,dz
\right|
\le
\frac{\operatorname{len}(E)}{2\pi}\,
\tau\,\|h\|_E.
}
\tag{L-105107.26}
\]

The selector minimizes its own boundary norm.  It need not minimize
\(\|W h\|_{\partial\Omega}\) for a fixed nonuniform \(h\).

## 7. Conjugation and parity

Suppose the window, manifest, orders, targets, and data are stable under
conjugation.  Then conjugating the unique extremal produces the same Pick
problem, so

\[
W_*(\overline z)=\overline{W_*(z)}.
\tag{L-105107.27}
\]

For sign symmetry and desired parity \(\sigma\in\{1,-1\}\), the exact
compatibility condition is

\[
\gamma_{-c}=\sigma(-1)^{d_c-1}\gamma_c.
\tag{L-105107.28}
\]

Then uniqueness gives \(W_*(-z)=\sigma W_*(z)\).  The L-105105 data have
even target powers and equal paired amplitudes, so \(\sigma=1\).  The exact
four-edge and half-rectangle identities from L-105101--L-105102 remain
available with the optimal selector.

For a centred symmetric rectangle, the normalized Riemann map
\(\phi(0)=0\), \(\phi'(0)>0\) obeys

\[
\phi(\overline z)=\overline{\phi(z)},
\qquad
\phi(-z)=-\phi(z)
\tag{L-105107.29}
\]

by uniqueness.  For nonextremal feasible selectors, conjugation or parity
averaging preserves the data and does not increase the norm, but the average
need not remain inner.

## 8. Sharp fixtures and exterior-pole firewall

With target zero and nontargets \(\pm i\varepsilon\), each of order \(m\),

\[
W_*(z)=
\left(
\frac{1+z^2/\varepsilon^2}
{1+\varepsilon^2z^2}
\right)^m,
\qquad
\tau=\varepsilon^{-2m}.
\tag{L-105107.30}
\]

This attains the L-105106 lower bound.  At
\(\varepsilon=1/5,m=2\), the optimal norm is \(625\), whereas the reduced
polynomial selector has norm \(676\).

For the paired quartic fixture of L-105106, the optimal first and second
selector norms are

\[
\tau_1=\varepsilon^{-2},
\qquad
\tau_2=3\varepsilon^{-4},
\tag{L-105107.31}
\]

instead of the polynomial norms
\(1+\varepsilon^{-2}\) and
\((1+\varepsilon^{-2})(1+3\varepsilon^{-2})\).

The rational extremals have reflected poles outside the current disk.  They
are harmless for the current contour, but may enter a later enlarged window.
Every window must recompute the conformal selector or authenticate that all
exterior poles remain outside.  A single rational formula may not be carried
through a cofinal enlargement without this check.

## 9. Boundary of the result

The theorem closes the optimal selector norm on a supplied finite regular
window.  It does not supply:

- the Xi actual-pole manifest;
- certified conformal coordinates for changing Xi rectangles;
- cofinal bounds for the Pick optimum, conformal radii, or
  pseudohyperbolic products;
- estimates for the unweighted boundary quotients \(F/F'\) and
  \(F^2/(F'F'')\);
- cofinal weighted-edge decay, multiplicity-defect control, or strict
  jet coherence;
- RCMV104530 or RH.

No repository Pick claim is used as a dependency.  The accepted low-order
actual-Xi Pick matrices concern a different kernel.  The historical
ID-colliding L-91014 and the quarantined growing-order L-92302 are not used.
No novelty is claimed for the classical finite Nevanlinna–Pick theorem,
finite Blaschke products, or conformal transport.  The new contribution is
their exact top-jet residue-selector factorization and the resulting
boundary-optimal finite-window bridge.
