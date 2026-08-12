# L-91304 — The theta state curve is a strict Schur map and Xi is exactly its missing scalar conservative port

Claim ID: `L-91304`  
Status: **PROVED STRICT-SCHUR/DEFECT IDENTITY; SCALAR PORT COMPLETION REMAINS RH-BEARING**  
Created: 2026-08-12  
Corrected: 2026-08-12 — the exact state has two `(cosh,sinh)` channels  
Depends on: `L-91302`  
RH status: **unproved**

## 1. Disk normalization

For `z in D`, put `q=z/2` and define the analytic two-channel state

\[
 \boxed{
 \mathbf x(z;v)
 =\frac1{\sqrt2}\sqrt{1-z^2}\,\sqrt{B(v)}
  \binom{\cosh(zv/8)}{\sinh(zv/8)},
 \qquad v>0.
 }
\tag{L-91304.1}
\]

The square-root branch is normalized to one at `z=0`.  For real `z`, this is
exactly the Hilbert-ball curve of the corrected `L-91302`.

## 2. Uniform strict Schur bound

For `w in C`,

\[
 |\cosh w|^2+|\sinh w|^2=\cosh(2\operatorname{Re}w).
\tag{L-91304.2}
\]

Hence, for `|z|<1`,

\[
 |\cosh(zv/8)|^2+|\sinh(zv/8)|^2
 \le e^{v/4}.
\]

Also `|1-z^2|<2`. Therefore

\[
\begin{aligned}
 \|\mathbf x(z)\|^2
 &\le\int_0^\infty B(v)e^{v/4}dv\\
 &=\sum_{n\ge1}\int_1^\infty
   y^{-1/2}e^{-\pi n^2y}dy\\
 &\le\sum_{n\ge1}\frac{e^{-\pi n^2}}{\pi n^2}\\
 &\le\frac{e^{-\pi}}\pi\sum_{n\ge1}\frac1{n^2}
 =\frac{\pi e^{-\pi}}6
 <\frac1{32}.
\end{aligned}
\tag{L-91304.3}
\]

Thus

\[
 \boxed{
 \sup_{z\in\mathbb D}\|\mathbf x(z)\|<\frac1{4\sqrt2}<1.
 }
\tag{L-91304.4}
\]

In particular `x` is an unconditional vector-valued Schur-class function, and
its de Branges--Rovnyak kernel

\[
 \boxed{
 \frac{1-\langle\mathbf x(z),\mathbf x(w)\rangle}
      {1-z\overline w}
 \succeq0
 }
\tag{L-91304.5}
\]

is positive on the disk.

This is a genuine complete matrix positivity theorem for the theta bulk state.
It does not yet identify the prescribed Xi scalar port.

## 3. Symmetric bilinear defect is Xi

Let

\[
 [f,g]=\int_0^\infty
  \bigl[f_1(v)g_1(v)+f_2(v)g_2(v)\bigr]dv
\]

be the symmetric bilinear form on the complexification of the real two-channel
state space.  Since

\[
 \cosh^2w+\sinh^2w=\cosh(2w),
\]

one has

\[
\begin{aligned}
 [\mathbf x(z),\mathbf x(z)]
 &=\frac12(1-z^2)
   \int_0^\infty B(v)\cosh(zv/4)dv.
\end{aligned}
\tag{L-91304.6}

Put `q=z/2`.  Then the integral in (L-91304.6) is `U(q)`, and the Green identity
of `L-91302` gives

\[
 4M(q)=1-2\left(\frac14-q^2\right)U(q).
\]

Because

\[
 \frac12(1-z^2)=2\left(\frac14-q^2\right),
\]

we obtain the exact analytic identity

\[
 \boxed{
 1-[\mathbf x(z),\mathbf x(z)]
 =4M(z/2).
 }
\tag{L-91304.7}

Here

\[
 M(q)=\int_0^\infty\Phi(t)\cosh(qt)dt
\]

is the centered completed-xi moment.  Up to the fixed positive normalization,
`M(q)` is `Xi(iq)`.

For real `z`, the symmetric bilinear form equals the Hilbert norm and

\[
 4M(z/2)=1-\|\mathbf x(z)\|^2>0.
\tag{L-91304.8}

Off the real diameter, however, (L-91304.7) is a symmetric analytic defect, not
a Hilbert norm.

## 4. The missing scalar port

A conservative one-input column completion of the theta state would require an
analytic scalar port `a(z)` satisfying

\[
 \boxed{
 a(z)^2+[\mathbf x(z),\mathbf x(z)]=1.
 }
\tag{L-91304.9}

By (L-91304.7), this is exactly

\[
 \boxed{
 a(z)^2=4M(z/2).
 }
\tag{L-91304.10}

Hence the scalar boundary port is not unspecified: it is the analytic square
root of the completed Xi moment.

An off-line zero of Xi inside the critical disk is a zero of the right side and
therefore an obstruction to a zero-free conservative scalar port.  Conversely,
if the completed Xi moment is zero-free in the disk, the branch normalized by
`a(0)>0` exists analytically.

Thus

\[
 \boxed{
 \text{theta state completion by the Xi scalar port}
 \Longleftrightarrow
 \text{zero-freeness of the completed defect in the disk},
 }
\tag{L-91304.11}

before the additional boundary-unitarity normalization is imposed.

## 5. Why generic Schur positivity is insufficient

The strict Schur estimate (L-91304.4) gives a canonical outer defect operator
for the Hilbert kernel (L-91304.5).  It does not force that outer defect to equal
the particular symmetric scalar `2 sqrt(M(z/2))` in (L-91304.10).

Replacing the Xi port by an arbitrary spectral factor would prove positivity
for another passive system, not for the completed-zeta impedance.  The exact
port identification is therefore the conclusion-bearing step.

This separates two issues that were previously conflated:

```text
theta bulk state is contractive               UNCONDITIONAL AND STRICT;
its prescribed scalar completion is Xi         EXACT;
that prescribed completion is zero-free        RH-BEARING.
```

## 6. Connection to the BPY boundary form

`L-91302` identifies the beta-product tangent direction

\[
 \partial_\Delta-\tanh\Delta\partial_S.
\]

A successful Brownian/theta DtN construction must realize the scalar port
(L-91304.10), rather than merely some outer defect factor of the strict Schur
state.  Equivalently, it must identify the Brownian reflection boundary energy
with the symmetric theta defect (L-91304.7).

This gives a fail-closed test for every proposed passive-network completion.

## 7. Proof boundary

```text
analytic two-channel theta state                EXACT
uniform strict Schur bound                       EXACT
Hilbert de Branges--Rovnyak kernel               EXACT POSITIVE
symmetric analytic defect = completed Xi moment  EXACT
Xi scalar port identification                    EXACT
zero-free Xi scalar completion                   OPEN / RH-EQUIVALENT
Brownian/theta DtN realization of that port      OPEN
Riemann Hypothesis                               UNPROVED
```
