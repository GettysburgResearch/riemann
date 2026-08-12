# L-91302 — The theta ground state gives an explicit passive defect curve and the BPY reservoir has one hyperbolic tangent direction

Claim ID: `L-91302`  
Status: **PROVED EXACT THETA/BPY IDENTITIES; COMPLETE-PICK DOMINATION OPEN**  
Created: 2026-08-12  
Corrected: 2026-08-12 — the exact defect state has two `(cosh,sinh)` channels  
Depends on: `L-91106`, `L-91107`, `L-91108`  
RH status: **unproved**

## 1. The theta ground state and its boundary atom

For `v>=0` put

\[
 B(v)=\sum_{n\ge1}e^{v/4-\pi n^2e^v},
 \qquad
 \Psi(v)=\Phi(v/2).
\]

The theta Gibbs calculation in `L-91108` gives

\[
 \boxed{
 \Psi(v)=4B''(v)-\frac14B(v).
 }
\tag{L-91302.1}
\]

The Jacobi theta transformation gives the exact half-line reflection law

\[
 \boxed{
 B(-v)=B(v)+\sinh(v/4).
 }
\tag{L-91302.2}
\]

Differentiating at zero,

\[
 \boxed{B'(0)=-\frac18.}
\tag{L-91302.3}
\]

The constant `1/8` is the archimedean boundary port omitted by a bulk-only
factorization.

## 2. Exact one-port Green identity

For real `q` with `|q|<1/2`, define

\[
 M(q)=\int_0^\infty\Phi(t)\cosh(qt)\,dt
\tag{L-91302.4}
\]

and

\[
 U(q)=\int_0^\infty B(v)\cosh(qv/2)\,dv.
\tag{L-91302.5}
\]

Changing variables `v=2t` and integrating (L-91302.1) twice by parts gives

\[
\begin{aligned}
 2M(q)
 &=\int_0^\infty\Psi(v)\cosh(qv/2)\,dv\\
 &=-4B'(0)
   +\left(q^2-\frac14\right)
    \int_0^\infty B(v)\cosh(qv/2)\,dv.
\end{aligned}
\]

Using (L-91302.3),

\[
 \boxed{
 2M(q)=\frac12+\left(q^2-\frac14\right)U(q).
 }
\tag{L-91302.6}
\]

Because `Phi>0`, one has `M(q)>0`.  Since `U(q)>0`, equation
(L-91302.6) also gives `M(q)<1/4` for `|q|<1/2`.

## 3. The exact two-channel Hilbert-ball defect curve

The scalar integral `U(q)` is linear in `cosh(qv/2)`.  Its exact Hilbert
realization uses the half-angle identity

\[
 \cosh(qv/2)=\cosh^2(qv/4)+\sinh^2(qv/4).
\]

On

\[
 \mathcal H_\theta
 =L^2((0,\infty),dv)\oplus L^2((0,\infty),dv),
\]

define

\[
 \boxed{
 x_q(v)
 =\sqrt{2\left(\frac14-q^2\right)B(v)}
  \binom{\cosh(qv/4)}{\sinh(qv/4)}.
 }
\tag{L-91302.7}
\]

Then

\[
\begin{aligned}
 \|x_q\|_{\mathcal H_\theta}^2
 &=2\left(\frac14-q^2\right)
   \int_0^\infty B(v)
   [\cosh^2(qv/4)+\sinh^2(qv/4)]dv\\
 &=2\left(\frac14-q^2\right)U(q).
\end{aligned}
\]

Equation (L-91302.6) therefore gives

\[
 \boxed{
 \|x_q\|^2=1-4M(q)<1.
 }
\tag{L-91302.8}
\]

Thus the complete theta source produces one explicit two-channel curve inside
the open unit ball.  The boundary atom `1/2` in (L-91302.6) is exactly the
scalar port which makes the pointwise defect positive.

Let

\[
 \ell_a(r)
 =\frac{\int_0^\infty
       \Phi(t)\sinh(rt)\sinh(at)dt}
       {\int_0^\infty
       \Phi(t)\cosh(rt)\cosh(at)dt}
\]

as in `L-91108`, with `|r|+a<1/2`.  Hyperbolic product identities give

\[
 \ell_a(r)
 =\frac{M(r+a)-M(r-a)}{M(r+a)+M(r-a)}.
\tag{L-91302.9}
\]

Using (L-91302.8),

\[
 \boxed{
 \ell_a(r)
 =\frac{\|x_{r-a}\|^2-\|x_{r+a}\|^2}
        {2-\|x_{r+a}\|^2-\|x_{r-a}\|^2}.
 }
\tag{L-91302.10}
\]

The Xi impedance is therefore the finite radial defect of a completely
explicit theta-state curve.  The desired Pick kernel is no longer an unknown
ratio of theta integrals; it is the complete-Pick/Schwarz--Pick question for
this resident two-channel curve.

Diagonal contractivity `||x_q||<1` is not sufficient.  The missing statement is
the matrix defect inequality for the complete curve.

## 4. Hyperbolic coordinates in the BPY two-copy reservoir

Condition on the Gamma reservoir of `L-91107` and put

\[
 c_n=\frac{G_n}{\pi^2n^2},
 \qquad
 A=\sum_nc_n,
 \qquad
 D=\sum_nc_nV_n.
\]

Then `|D|<A`.  For the two half-biased Brownian log-range coordinates,

\[
 \boxed{
 S=Z_++Z_-
 =\frac12\log(A^2-D^2)+\log\frac\pi2,
 }
\tag{L-91302.11}
\]

\[
 \boxed{
 \Delta=Z_+-Z_-
 =\frac12\log\frac{A+D}{A-D}
 =\operatorname{artanh}(D/A).
 }
\tag{L-91302.12}
\]

The two-copy tilt becomes

\[
 \boxed{
 (A^2-D^2)^{1/4}
 =A^{1/2}\operatorname{sech}^{1/2}\Delta.
 }
\tag{L-91302.13}
\]

Thus the nontrivial coupling is a hyperbolic boundary weight in one imbalance
coordinate.

## 5. Exact tangent direction of the beta product form

At fixed Gamma reservoir,

\[
 \frac{\partial\Delta}{\partial D}
 =\frac{A}{A^2-D^2}
 =\frac{\cosh^2\Delta}{A},
\]

\[
 \frac{\partial S}{\partial D}
 =-\frac{D}{A^2-D^2}
 =-\frac{\sinh\Delta\cosh\Delta}{A}.
\]

Since `partial_(V_n)D=c_n`, every smooth function `F(S,Delta)` satisfies

\[
 \boxed{
 \partial_{V_n}F
 =\frac{c_n\cosh^2\Delta}{A}
  \left(\partial_\Delta-	anh\Delta\,\partial_S\right)F.
 }
\tag{L-91302.14}
\]

The un-tilted Beta(2,2) carré du champ therefore reduces exactly to

\[
 \boxed{
 \Gamma_\beta(F,F)
 =\frac{\cosh^4\Delta}{4A^2}
  \left[\sum_nc_n^2(1-V_n^2)\right]
  \left|
   (\partial_\Delta-	anh\Delta\partial_S)F
  \right|^2.
 }
\tag{L-91302.15}
\]

This is the concrete boundary-energy direction hidden in the abstract
Dirichlet form of `L-91107`.  It is positive before any averaging or limiting
operation.

## 6. The sharpened DtN target

For the Brownian reflection integrand

\[
 \mathcal A_F(S,\Delta)
 =\int_{-S/2}^{S/2}
   \overline{F(x+\Delta/2)}F(x-\Delta/2)dx,
\]

the remaining theorem can now be asked in one of two equivalent constructive
forms:

1. identify the cross-multiplied Xi kernel as the boundary trace of the
   carré-du-champ (L-91302.15), plus an explicit nonnegative endpoint square;
2. prove that the explicit two-channel theta curve has the particular
   complete-Pick defect dictated by the Xi scalar port.

Either construction gives the boundary triple requested by `L-91108` and hence
RH through `T-91101` of the Brownian--theta branch.

The pointwise norm identity (L-91302.8) alone does not prove either matrix
statement.

## 7. Proof boundary

```text
theta supersymmetric bulk                       EXACT
modular boundary atom B'(0)=-1/8                 EXACT
one-port Green identity                          EXACT
exact two-channel Hilbert-ball curve              EXACT
Xi impedance as radial defect ratio              EXACT
BPY hyperbolic coordinates                       EXACT
beta tangent/carre-du-champ direction             EXACT
complete-Pick or DtN boundary domination          OPEN / RH-BEARING
Riemann Hypothesis                                UNPROVED
```
