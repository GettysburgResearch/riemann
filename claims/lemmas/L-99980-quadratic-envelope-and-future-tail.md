# L-99980 — Exact quadratic upper envelope, future-tail identity, and pole audit

Claim ID: `L-99980`  
Status: **PROVED EXACT REDUCTION; ENVELOPE SIGN OPEN**  
Created: 2026-08-20  
Base: PR #668 at `15719b975115ecad1b23264c6a6303899b4c99dc`  
RH status: **unproved**

Put

\[
\beta(n)=\mu(n)-\mathbf1_{67\mid n}\mu(n/67),
\qquad
B_\beta(z)=\frac{1-67^{-z}}{\zeta(z)},
\]

\[
T(y)=(4\sqrt y-3)\mathbf1_{y\ge1},
\qquad
\mathfrak H_m(X)=
\sum_{n\le X}\frac{\beta(n)}{\sqrt n}T(X/n)^m.
\]

PR #668 proves \(\mathfrak H_2(X)>0\) for every \(X\ge1\).
Define

\[
C_2=16B_\beta(3/2)
=16\frac{1-67^{-3/2}}{\zeta(3/2)}
\]

and the quadratic upper-envelope defect

\[
\boxed{\mathcal E_2(X)=C_2X-\mathfrak H_2(X).}
\tag{L-99980.1}
\]

## 1. Exact all-integer kernel

Absolute convergence of \(\sum|\beta(n)|n^{-3/2}\) permits completion of the
leading term. One obtains

\[
\boxed{
\mathcal E_2(X)=
\sum_{n\ge1}\frac{\beta(n)}{\sqrt n}R(X/n),
}
\tag{L-99980.2}
\]

where

\[
R(y)=
\begin{cases}
16y,&0<y<1,\\
24\sqrt y-9,&y\ge1.
\end{cases}
\tag{L-99980.3}
\]

Indeed, for \(n>X\) only the completed \(16Xn^{-3/2}\) term remains; for
\(n\le X\),

\[
16(X/n)-T(X/n)^2=24\sqrt{X/n}-9.
\]

Thus the candidate is an actual convergent Euler source, not an asymptotic
subtraction.

## 2. Exact future-tail identity

Let \(G_2(u)=e^{-u}\mathfrak H_2(e^u)\). PR #668 gives, as measures,

\[
dG_2(u)=
\sum_n\frac{\beta(n)}{n^{3/2}}\delta_{\log n}(du)
+3e^{-u}\mathfrak H_1(e^u)\,du.
\]

Since \(G_2(u)\to C_2\),

\[
\boxed{
\mathcal E_2(X)
=
X\sum_{n>X}\frac{\beta(n)}{n^{3/2}}
+
3X\int_X^\infty\mathfrak H_1(t)\frac{dt}{t^2}.
}
\tag{L-99980.4}
\]

This is a future average of the critical scalar plus its exact atomic tail.
It is strictly different from pointwise IHR67 and from the total negative-mass
criterion.

## 3. Mellin transform

For \(\Re s>1\),

\[
\int_1^\infty\mathfrak H_2(X)X^{-s-1}\,dX
=
B_\beta(s+1/2)
\frac{2s^2+5s+9}{s(s-1)(2s-1)}.
\]

Hence

\[
\boxed{
\mathcal M\mathcal E_2(s)
=
\frac{C_2}{s-1}
-
B_\beta(s+1/2)
\frac{2s^2+5s+9}{s(s-1)(2s-1)}.
}
\tag{L-99980.5}
\]

The apparent pole at \(s=1\) cancels by the definition of \(C_2\), and the
apparent pole at \(s=1/2\) is cancelled by the zero of \(1/\zeta(s+1/2)\) at
\(s=1/2\). The expression is holomorphic at every positive real \(s\).

If \(\rho\) is a zeta zero with \(\Re\rho>1/2\), then
\(s=\rho-1/2\) is a pole: \(1-67^{-\rho}\ne0\), and
\(2s^2+5s+9\) has both roots in \(\Re s<0\).

Therefore the specialized Landau theorem gives

\[
\boxed{
\mathcal E_2(X)\ge0\ \text{eventually}
\quad\Longrightarrow\quad RH.
}
\tag{L-99980.6}
\]

The envelope sign is not proved here.
