# L-19814 — Theta Hankel Gram–commutator factorization

Claim ID: `L-19814`  
Title: The original same-sign \(K_0\) branch is one explicit positive theta Gram plus one sharply isolated Hankel commutator  
Status: `PROPOSED — COMPLETE IDENTITY; FINAL COMMUTATOR SIGN OPEN`  
Authoring agent: `gpt56-pro-09-j`  
Created: 2026-08-01  
Dependencies: the explicit Riemann kernel \(\Phi\); elementary Hankel-operator algebra  
Scope: theta-specific coordinate factorization of the original, unnormalized kernel

## 1. Same-sign branch

For \(x,y\ge0\), the lower endpoint in the original kernel may be translated to
zero:

\[
\boxed{
A_0(x,y):=K_0(x,y)
=\frac12\int_0^\infty
\left(u+\frac{x+y}{2}\right)
\Phi(x+u)\Phi(y+u)\,du.}
\tag{L-19814.1}
\]

No finite core or normalized quotient appears in this formula.

Let \(\mathsf H_\Phi\) be the Hankel operator on \(L^2(0,\infty)\),

\[
(\mathsf H_\Phi f)(u)
=\int_0^\infty\Phi(u+x)f(x)\,dx,
\tag{L-19814.2}
\]

let \(X\) denote multiplication by the coordinate, and let
\(\mathsf H_{t\Phi}\) be the Hankel operator with kernel
\((x+y)\Phi(x+y)\).

## 2. Exact operator factorization

The kernel of \(\mathsf H_\Phi X\mathsf H_\Phi\) is

\[
\int_0^\infty u\,\Phi(x+u)\Phi(y+u)\,du,
\tag{L-19814.3}
\]

while the kernel of \(\mathsf H_\Phi^2\) is the same expression without
\(u\). Therefore (L-19814.1) gives

\[
\boxed{
A_0
=\frac12\mathsf H_\Phi X\mathsf H_\Phi
+\frac14\bigl(X\mathsf H_\Phi^2+
\mathsf H_\Phi^2X\bigr).}
\tag{L-19814.4}
\]

Since

\[
\mathsf H_{t\Phi}=X\mathsf H_\Phi+\mathsf H_\Phi X,
\tag{L-19814.5}
\]

this is equivalently the anticommutator identity

\[
\boxed{
A_0
=\frac14\left\{
\mathsf H_\Phi,\mathsf H_{t\Phi}
\right\}.}
\tag{L-19814.6}
\]

A second useful form is

\[
\boxed{
A_0
=\mathsf H_\Phi X\mathsf H_\Phi
+\frac14
[\mathsf H_\Phi,[\mathsf H_\Phi,X]].}
\tag{L-19814.7}
\]

The first term is an honest Gram operator:

\[
\langle f,\mathsf H_\Phi X\mathsf H_\Phi f\rangle
=\|\sqrt X\,\mathsf H_\Phi f\|_2^2\ge0.
\tag{L-19814.8}
\]

Thus the same-sign positivity problem is reduced exactly to the single
commutator estimate

\[
\boxed{
[\mathsf H_\Phi,[\mathsf H_\Phi,X]]
\succeq
-4\mathsf H_\Phi X\mathsf H_\Phi.}
\tag{L-19814.9}
\]

This is a theta-specific operator inequality for the original kernel, not a
finite-section spectral statement.

## 3. Multiplicative theta factorization

Let

\[
\vartheta(z)=\sum_{n\ge1}e^{-\pi n^2z},
\qquad
G(z)=-z^{3/2}\vartheta'(z)
=\pi z^{3/2}\sum_{n\ge1}n^2e^{-\pi n^2z},
\tag{L-19814.10}
\]

and

\[
\boxed{
h(z)=-G'(z)
=\pi z^{1/2}\sum_{n\ge1}
 n^2\left(\pi n^2z-\frac32\right)e^{-\pi n^2z}.}
\tag{L-19814.11}
\]

For \(z\ge1\), every summand in (L-19814.11) is positive. Direct
differentiation of the theta series gives the exact identity

\[
\boxed{
\Phi(t)=4z^{3/4}h(z),
\qquad z=e^{2t},\quad t\ge0.}
\tag{L-19814.12}
\]

Put \(X=e^{2x}\), \(Y=e^{2y}\), and \(R=e^{2u}\). Equation
(L-19814.1) becomes

\[
\boxed{
A_0(X,Y)
=2(XY)^{3/4}\int_1^\infty
R^{1/2}\log(R\sqrt{XY})
 h(XR)h(YR)\,dR.}
\tag{L-19814.13}
\]

Define

\[
a_X(R)=X^{3/4}R^{1/4}h(XR),
\tag{L-19814.14}
\]

and the theta-Volterra map

\[
(\mathcal Tf)(R)
=\int_1^\infty a_X(R)f(X)\,{dX\over2X},
\qquad R\ge1.
\tag{L-19814.15}
\]

Let \(L_X\) and \(L_R\) denote multiplication by \(\log X\) and
\(\log R\), respectively. Then (L-19814.13) is exactly

\[
\boxed{
A_0
=2\mathcal T^*L_R\mathcal T
+L_X\mathcal T^*\mathcal T
+\mathcal T^*\mathcal T L_X.}
\tag{L-19814.16}
\]

The first summand is again a positive Gram:

\[
2\mathcal T^*L_R\mathcal T\succeq0.
\tag{L-19814.17}
\]

The entire remaining sign is concentrated in one anticommutator with the
positive coordinate operator \(L_X\):

\[
\boxed{
\{L_X,\mathcal T^*\mathcal T\}
\succeq-2\mathcal T^*L_R\mathcal T.}
\tag{L-19814.18}
\]

Equations (L-19814.9) and (L-19814.18) are unitarily equivalent descriptions
of the same same-sign obstruction.

## 4. First-order theta square identity

The second-order theta identity also admits a useful one-step completion. Put

\[
B(t)=\sum_{n\ge1}e^{t/2}e^{-\pi n^2e^{2t}},
\qquad
p(t)=\left(\partial_t+\frac12\right)B(t),
\tag{L-19814.19}
\]

so that

\[
\Phi=(\partial_t-\tfrac12)p.
\tag{L-19814.20}
\]

For fixed \(x,y\ge0\), set
\(p_x(u)=p(x+u)\), \(p_y(u)=p(y+u)\), and
\(q=u+(x+y)/2\). A single integration by parts gives

\[
\boxed{
\begin{aligned}
\int_0^\infty q\,\Phi(x+u)\Phi(y+u)\,du
={}&\int_0^\infty q\,p_x'(u)p_y'(u)\,du\\
&+\int_0^\infty\left(\frac q4+\frac12\right)
 p_x(u)p_y(u)\,du\\
&+\frac{q(0)}2p(x)p(y).
\end{aligned}}
\tag{L-19814.21}
\]

This identity explains the strong positive bulk seen in direct theta
coordinates. It is not, by itself, a global Gram representation because the
weight \(q=u+(x+y)/2\) still couples the two external coordinates. The exact
remaining coupling is precisely the commutator in (L-19814.9).

## 5. Relation to the normalized Volterra lift

`T-19806` proves that positivity of the completed normalized mixed/Volterra
form pulls back exactly to the original \(K_0\). The present lemma supplies a
direct coordinate check on what that imported positivity must accomplish:
its quotient contraction must dominate the anticommutator in
(L-19814.18), including every endpoint and reflected-parity channel.

Thus a normalized certificate is not being compared with an unrelated kernel.
After the primitive congruence of `T-19806`, it certifies exactly the operator
whose same-sign coordinate decomposition is (L-19814.16).

## 6. Proof boundary

- All identities above follow from changes of variables, theta differentiation,
  and elementary Hankel algebra.
- The positive bulk is an explicit theta Gram.
- The anticommutator estimate (L-19814.18) is not proved here.
- Opposite-sign/parity coupling is handled by the exact mixed-form lift of
  `T-19806`, not by dropping the reflected block.
- Therefore this lemma materially exposes the original-kernel geometry but does
  not independently prove \(K_0\succeq0\).