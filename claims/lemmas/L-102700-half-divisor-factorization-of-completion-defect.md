# L-102700 — The completion defect factors through two half-divisor fields

Claim ID: `L-102700`  
Status: **PROVED EXACT SOURCE FACTORIZATION**  
Created: 2026-08-22  
Depends on: PR #718 `L-102602--L-102604`; PR #707 `L-103304`  
RH status: **not assumed**

Let

\[
\beta=(\delta_1-\delta_{67})*\mu
\]

be the duplicate-\(67\) source, with the two \(67\)-labels retained before
physical collapse. Let \(\lambda\) be the positive-half-divisor source of
PR #707, so that

\[
\boxed{\lambda*\lambda=\beta.}
\tag{L-102700.1}
\]

For an arithmetic function \(a\), define its square lift by

\[
a^\square(n)=
\begin{cases}
a(m),&n=m^2,\\
0,&n\text{ is not a square}.
\end{cases}
\]

Its Dirichlet series is \(A(2z)\). Hence

\[
\lambda^\square*\lambda^\square=\beta^\square,
\]

where \(\beta^\square(m^2)=\beta(m)\).

Put

\[
\lambda_-=\lambda-\lambda^\square,
\qquad
\lambda_+=\lambda+\lambda^\square.
\]

Then

\[
\boxed{
\beta-\beta^\square
=
\lambda_-*\lambda_+.
}
\tag{L-102700.2}
\]

This is the completion-defect source of PR #718.

## Dirichlet-series form

Let

\[
L(z)=\sum_n\frac{\lambda(n)}{n^z}.
\]

Then

\[
L(z)^2=\frac{1-67^{-z}}{\zeta(z)},
\]

and

\[
\boxed{
B_{\rm def}(z)
=
[L(z)-L(2z)][L(z)+L(2z)].
}
\tag{L-102700.3}
\]

No branch choice enters the coefficient identity: it is an equality of formal
Dirichlet series on every finite horizon.

## Root separation

Since

\[
\lambda(1)=\lambda^\square(1)=1,
\]

one has

\[
\boxed{\lambda_-(1)=0,\qquad \lambda_+(1)=2.}
\tag{L-102700.4}
\]

Thus the first factor is root-free. The unique unit/root coordinate is
isolated in the plus field before physical collapse.
