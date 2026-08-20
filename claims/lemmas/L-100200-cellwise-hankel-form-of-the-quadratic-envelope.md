# L-100200 — The quadratic envelope is one moving Rayleigh form of a 2x2 arithmetic state

Claim ID: `L-100200`  
Status: **PROVED EXACT CELLWISE REDUCTION**  
Created: 2026-08-20  
Base: PR #672, `L-99980--L-99981`  
RH status: **not assumed**

Put

\[
\beta(n)=\mu(n)-\mathbf1_{67\mid n}\mu(n/67),
\qquad
\Delta=\sum_{n\ge1}\frac{\beta(n)}{n^{3/2}}
=\frac{1-67^{-3/2}}{\zeta(3/2)}.
\]

For an integer \(N\ge1\), define

\[
A_\sigma(N)=\sum_{n\le N}\frac{\beta(n)}{n^\sigma},
\qquad
R_{3/2}(N)=\Delta-A_{3/2}(N).
\]

The quadratic SHARP transform and its upper-envelope defect are

\[
\mathfrak H_2(X)
=\sum_{n\le X}\frac{\beta(n)}{\sqrt n}
\left(4\sqrt{X/n}-3\right)^2,
\]

\[
\mathcal E_2(X)=16\Delta X-\mathfrak H_2(X).
\]

For \(N\le X<N+1\), finite expansion gives

\[
\boxed{
\frac{\mathcal E_2(X)}X
=
16R_{3/2}(N)
+24X^{-1/2}A_1(N)
-9X^{-1}A_{1/2}(N).
}
\tag{L-100200.1}
\]

Define

\[
M_N=
\begin{pmatrix}
R_{3/2}(N)&A_1(N)\\
A_1(N)&-A_{1/2}(N)
\end{pmatrix},
\qquad
z_X=
\begin{pmatrix}
4\\ 3X^{-1/2}
\end{pmatrix}.
\]

Then

\[
\boxed{
\frac{\mathcal E_2(X)}X=z_X^{\mathsf T}M_Nz_X.
}
\tag{L-100200.2}
\]

Thus the whole mixed-activation problem is a moving Rayleigh form of a two-dimensional arithmetic state.

## Exact cell minima

Write

\[
a=A_1(N),\qquad b=A_{1/2}(N),\qquad r=R_{3/2}(N).
\]

On the open cell,

\[
D_N(X)=16r+24aX^{-1/2}-9bX^{-1}
\]

and

\[
D_N'(X)=X^{-2}\left(9b-12a\sqrt X\right).
\tag{L-100200.3}
\]

There is at most one interior minimum.

- If \(a\ge0\), an interior critical point is a maximum; the minimum is at an endpoint.
- If \(a<0\) and \(b\ge0\), the function is increasing; the minimum is at the left endpoint.
- If \(a<0\) and \(b<0\), the only possible interior minimum is

\[
X_*=\left(\frac{3b}{4a}\right)^2.
\]

When \(N<X_*<N+1\),

\[
\boxed{
D_N(X_*)
=16\left(r-\frac{a^2}{-b}\right).
}
\tag{L-100200.4}
\]

Hence the interior condition is the two-by-two Schur inequality

\[
\boxed{
(-A_{1/2}(N))R_{3/2}(N)-A_1(N)^2\ge0.
}
\tag{L-100200.5}
\]

## Exact equivalent gate

Eventual nonnegativity of the quadratic envelope is equivalent to:

1. nonnegativity of both one-sided endpoint values of every sufficiently large integer cell; and
2. (L-100200.5) on every sufficiently large cell for which \(A_1(N)<0\), \(A_{1/2}(N)<0\), and \(X_*\in(N,N+1)\).

Call this criterion `CEHC100200`. Since PR #672 proves that eventual \(\mathcal E_2\ge0\) implies RH,

\[
\boxed{\mathrm{CEHC100200}\Longrightarrow RH.}
\]

The criterion is not proved here.