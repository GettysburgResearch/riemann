# A proposed codimension-18 positive sector for the actual L=1 kernel

Status: PROPOSED_EXACT; arithmetic replay passes; independent review pending.
Scope: one complete continuum window, L=1; positive sector and residual enclosure,
not full-window positivity and not RH.
Exact dependencies: the literal kernel, constrained Fourier identity and coupling
domain in `reviews/C/pass4-math-completion/proofs/OPERATOR_AUDIT.md`, O1-O4,
inherited from PR #792 at `465cb28ed8cbfa1bb071d9a85eeda9890decfe6b`.
What was actually run: `python check_coercivity.py`; rational arithmetic only.
Smallest remaining gap: full continuum lower sign of the 18-dimensional effective
matrix.  The xi/Weil terminal identification remains the predecessor's separate
source input.

## Exact source and statement

Use the source's constants b=3/2, c=1/2,
lambda_j=2j+1/2, q_n=Lambda(n)/sqrt(n), and
C_b=(1-gamma-log(2*pi))/3.  On [-1,1] define the complete source

\[
W(x)=\frac12e^{c|x|}+C_be^{-b|x|}
 +\sum_{j\ge1}\frac{e^{-\lambda_j|x|}}{\lambda_j^2-b^2}
 -\frac1{2b}\sum_{n\ge2}q_n
   \bigl(e^{-b|x-\log n|}+e^{-b|x+\log n|}\bigr).
\]

For complex h,k in L2(0,1), with the first argument conjugated, set

\[
q(h,k)=b\int_0^1\overline{h(t)}\int_0^1W(t-u)k(u)\,du\,dt.
\]

Let V be the L2 orthogonal complement of the 18 functions

\[
e^{-t/2},\quad e^{t/2},\quad\cosh(3t/2),\quad
\sin(j\pi t),\quad 1\le j\le15.
\]

For h in V put
phi(t)=2 integral_0^t sinh((t-u)/2) h(u) du, and
tau_2=sum_(n>=3) Lambda(n)/n^2.  **Proposed theorem:**

\[
q(h,h)\ge\frac65\|\phi'\|_2^2
 +\tau_2\left|\int_0^1\sinh(3t/2)h(t)\,dt\right|^2.
\tag{1}
\]

The 18 functions are linearly independent because their complex exponential
frequencies are distinct; consequently V has exactly codimension 18.  The
norm in (1) is the primitive norm and does not claim a uniform L2 gap.

## 1. The first unnecessary prime cusp can be removed exactly

The prior L=1 audit selected X=3.  In fact **every integer n>=3 has log(n)>1**.
Thus the complete source beyond n=2 already lies outside this window.  The
same elementary exponential identity gives

\[
W(x)-W_2(x)=-(\tau_2/b)\cosh(bx),\qquad |x|\le1,
\]

and hence

\[
q(h,h)-q_2(h,h)=-\tau_2|\langle\cosh(bt),h\rangle|^2
 +\tau_2|\langle\sinh(bt),h\rangle|^2.
\tag{2}
\]

It is sufficient that **the next included integer lie outside the window**;
the stronger integer condition X>=e^L used in the audit is unnecessary.
Here log(3)>1 follows from e<3.  With the first three moment constraints the
negative term in (2) vanishes.

## 2. A globally enclosed digamma multiplier

Write x=omega^2>=0 and

\[
\Omega(\omega)=\Re\psi(1/4+i\omega/2)-\log\pi,
\quad V_2(\omega)=\Omega(\omega)
 -2(\log2/\sqrt2)\cos(\omega\log2).
\]

The exact digamma expansion is

\[
\Omega(\omega)=\Omega(0)+\sum_{k\ge0}
 \frac4{4k+1}\frac{4x}{(4k+1)^2+4x},
\quad \Omega(0)=-\gamma-\pi/2-3\log2-\log\pi.
\]

The checker proves gamma<7/12, log2<139/200, log(pi)<23/20 using pi<22/7;
their rational sum with pi/2<11/7 is <27/5.  Thus Omega(0)>-27/5.
It also proves log2<7/10 and sqrt2>7/5, so 2 log2/sqrt2<1.
Discarding only positive digamma terms therefore yields

\[
V_2(\omega)>v(x):=-\frac{32}5+
 \sum_{k=0}^{64}\frac{16x}{(4k+1)((4k+1)^2+4x)}.
\tag{3}
\]

Put P(x)=(x+1/4)^2/(x+9/4).  Both P and v increase on [0,infinity);
indeed P(x)=x-7/4+4/(x+9/4) and
P'(x)=1-4/(x+9/4)^2>0.  The exact arithmetic checker proves

\[
P(x)v(x)\ge x-448\qquad(x\ge0).
\tag{4}
\]

Here is the complete coverage contract for (4).  On each integer cell
[a,a+1], a=0,...,4095, replace each positive term of v(a) by its downward
integer floor at scale 2^80, giving v_lo(a)<=v(a).  If v_lo(a)<0, use
P(a+1)v_lo(a); otherwise use P(a)v_lo(a).  Both expressions are valid
lower bounds for P(x)v(x) throughout the cell.  The checker verifies that
each lower bound exceeds a+1-448.  The least cell margin is >4, attained
on cell [935,936].  For x>=4096 it checks v_lo(4096)>1, whence
P(x)v(x)>=x-7/4>x-448.  This proves the unbounded frequency tail, without
fitting a trend or sampling uncovered points.  Fractions and integer division
are the only arithmetic used for acceptance.

## 3. Primitive coercivity with 15 sine constraints

The two e^(+/-ct) moment constraints make phi and phi' vanish at both endpoints.
Its zero extension belongs to H2(R) and
h_hat(omega)=-(omega^2+1/4)phi_hat(omega).  The inherited source Fourier identity,
with unnormalized transform h_hat(omega)=integral exp(-i omega t)h(t)dt, is

\[
q_2(h,h)=\frac b{2\pi}\int_\mathbb R
 \frac{V_2(\omega)}{\omega^2+9/4}|\widehat h(\omega)|^2\,d\omega.
\]

Equations (3)-(4) and Plancherel imply

\[
q_2(h,h)\ge b\bigl(\|\phi'\|_2^2-448\|\phi\|_2^2\bigr).
\]

Integration by parts transfers the 15 sine constraints from h to phi.
The Dirichlet expansion then gives
||phi||² <= ||phi'||²/(16² pi²).  Using pi>3,

\[
b\left(1-\frac{448}{16^2\pi^2}\right)
>\frac32\left(1-\frac{448}{2304}\right)
=\frac{29}{24}>\frac65.
\]

Adding the exact tail (2) proves (1).  In particular nonzero h in V has
strictly positive q(h,h), because phi'=0 and its endpoints force phi=0 and h=0.

## 4. Consequence for the actual residual enclosure

The coupling proof uses only W in W^(1,1), the clamped primitive, and the
listed constraints.  All remain valid for this smaller V.  In its notation,
Pi now projects off {1, cos(j pi t):1<=j<=15, sinh(3t/2)}.  Let E=V^perp,
let g_e be the Riesz vector in the q-energy completion, and define the
18-by-18 effective matrix S_ij=q(e_i,e_j)-q(g_ei,g_ej).
For exact trials v_i in V put z_i=e_i-v_i,
U_ij=q(z_i,z_j), R_ij=<Pi F_zi,Pi F_zj>, where
F_z=-K_z'+(1/4) integral_0^t K_z(s)ds and K_z=W*z on the window.  Then

\[
U-(15/8)R\preceq S\preceq U.
\tag{5}
\]

This is the same coefficient as the audited 104-dimensional L=1 construction,
with only 18 complementary dimensions.  The matrices in (5) are **new source
objects** because the subspace and projection changed; previously sampled
matrices cannot be reused as their entries.

No sign of S is established here.  A positive Galerkin S_m still bounds S
from above.  To close this window one must enclose the complete U and R,
including constraints, integrals and rounding, then prove the lower matrix PSD.
To make an RH argument one must additionally supply the source adapter and
the required unbounded family of windows.
