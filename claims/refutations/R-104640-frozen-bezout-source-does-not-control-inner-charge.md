# R-104640 — Exact frozen Bézout source transport does not control the physical inner-factor charge

Claim ID: `R-104640`
Status: **PROVED EXACT SOURCE-TO-INNER-FACTOR COUNTERMODEL**
Created: 2026-08-30
Depends on: `L-104637`; strengthens the source-module interpretation of
`R-106700`
RH status: **not assumed**

The exact polynomial source transport of `L-104637` has zero algebraic
residual.  This refutation proves that such a relation—even at lower degree,
with a perfectly frozen carrier—does not control the endpoint model-space
charge.

## 1. A positive-source periodic family

Fix \(c>1\), an integer \(n\ge1\), and put

\[
F_n(t)=c+\cos(nt).
\]

Its Fourier source is the positive even measure

\[
c\delta_0+\frac12\delta_n+\frac12\delta_{-n}.
\]

Set

\[
z=e^{int},
\qquad
w=z^{-1}=e^{-int},
\qquad
h(w)=\frac12+cw+\frac12w^2.
\]

Then

\[
F_n(t)=e^{int}h(e^{-int}).
\]

Freeze the carrier exactly at \(\omega=n\), take \(q=0\), and define the
source operator of `L-104637` by

\[
\mathcal X={i\over n}D.
\]

Since

\[
\mathcal Xw^k=kw^k,
\]

one obtains coefficient-exactly

\[
\boxed{\mathcal Xh=cw+w^2,}
\tag{R-104640.1}
\]

\[
\boxed{(2-\mathcal X)h=1+cw,}
\tag{R-104640.2}
\]

\[
\boxed{(1-\mathcal X)^5h={1-w^2\over2},}
\tag{R-104640.3}
\]

\[
\boxed{\mathcal X(1-\mathcal X)^5h=-w^2,}
\tag{R-104640.4}
\]

and

\[
\boxed{(2-\mathcal X)(1-\mathcal X)^5h=1.}
\tag{R-104640.5}
\]

Thus the frozen denominator and numerator source vectors in `L-104637.1` are

\[
\boxed{
\mathbf d=
\begin{pmatrix}
cw+w^2\\
1
\end{pmatrix},
\qquad
\mathbf n=
\begin{pmatrix}
1+cw\\
-w^2
\end{pmatrix}.
}
\tag{R-104640.6}
\]

## 2. The degree-six Bézout transport is exact with zero residual

Let

\[
A(X)={-X^5+7X^4-20X^3+30X^2-25X+11\over2}
\]

and let \(\mathcal M(X)\) be the matrix of `L-104637.5`.  The exact identity

\[
XA(X)+\frac12(2-X)(1-X)^5=1
\]

gives

\[
\boxed{\mathbf n=\mathcal M(\mathcal X)\mathbf d.}
\tag{R-104640.7}
\]

No approximation, moving carrier, source tail, or omitted grade occurs.  In
fact the fixture has source degree two, well inside the seven-grade span.

## 3. Physical multiplication creates the full adverse inner charge

The physical denominator and numerator products are

\[
D(w)=(cw+w^2)\cdot1=w(c+w),
\]

\[
N(w)=(1+cw)(-w^2)=-w^2(1+cw).
\]

Therefore

\[
\boxed{
U_n(t)={N\over D}
=-{z+c\over z(cz+1)}
=-{1\over z\,b_{-1/c}(z)},
}
\tag{R-104640.8}
\]

where

\[
b_{-1/c}(z)={z+1/c\over1+z/c}
\]

is a degree-one disk Blaschke factor.

Because \(c>1\), the numerator zero \(-c\) is outside the unit disk, while the
denominator zeros \(0\) and \(-1/c\) are inside it.  After reduction, the
numerator inner factor is constant and the denominator inner factor has degree
two.  Hence on every period

\[
\boxed{
-\operatorname{wind}U_n=2,
\qquad
\|H_{U_n}\|_{\mathcal S_2}^2=2.
}
\tag{R-104640.9}
\]

Equivalently, the numerator model space has no direction available and the
exact primal residual is two.

The nontrivial denominator zero has upper-half-plane height

\[
\boxed{{\log c\over n}\longrightarrow0.}
\tag{R-104640.10}
\]

Thus the failure persists in the arbitrarily shallow regime.

## 4. What this refutes

This family simultaneously has:

```text
positive even Fourier source;
constant exact carrier;
zero carrier perturbation;
exact L-104637 degree-six source transport;
no source-module residual;
arbitrarily shallow nontrivial denominator zero;
full endpoint inner-factor charge.
```

Consequently there is no universal theorem of the form

\[
\text{exact finite differential/Bézout source transport}
\Longrightarrow
\text{subpower or small physical inner-factor Gram}.
\]

The obstruction is not the polynomial source algebra.  It is the nonlinear
passage through physical multiplication, inner factorization, and the
topological unit spectrum.

This does not refute an Xi-specific microscopic theorem.  It proves that such
a theorem must use information absent from `L-104637` and the source
mean-square carrier estimate `L-104638`.

```text
frozen source transport                    EXACT / ZERO RESIDUAL
physical inner-factor charge               TWO PER PERIOD
shallow-height limit                       ZERO
universal source-to-inner promotion         REFUTED
Xi-specific microscopic charge estimate    OPEN
more than ninety percent                   UNPROVED
Riemann Hypothesis                          UNPROVED
```
