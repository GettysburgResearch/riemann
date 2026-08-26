# L-103000 — The common two-box spline is log-concave and TP2

Claim ID: `L-103000`  
Status: **PROVED EXACT KERNEL THEOREM**  
Created: 2026-08-25  
Depends on: `L-102701`  
RH status: **not assumed**

Let `A` be the positive ratio-four two-box spline used in the exact common-mother factorization

\[
\Phi_*=2A_-*_M A,
\qquad
A_-=(D-\tfrac12)A.
\]

Put

\[
L=\log2,
\qquad
a(u)=A(e^u).
\]

`L-102701` gives

\[
a'(u)-\frac12a(u)=
\begin{cases}
1,&0<u<L,\\
-\sqrt2,&L<u<2L,\\
0,&u\notin(0,2L),
\end{cases}
\]

and `A` vanishes at the endpoints of its support. Solving the two first-order equations gives the exact formula

\[
\boxed{
a(u)=
\begin{cases}
2(e^{u/2}-1),&0<u<L,\\[1mm]
2\sqrt2\left(1-e^{(u-2L)/2}\right),&L<u<2L,\\[1mm]
0,&\text{otherwise}.
\end{cases}
}
\tag{L-103000.1}
\]

The two interior formulas agree at `u=L`, so `a` is continuous and strictly positive on `(0,2L)`.

## 1. Strict logarithmic concavity

On the first interval,

\[
(\log a)''(u)
=-\frac{e^{u/2}}{4(e^{u/2}-1)^2}<0.
\]

On the second interval, with `z=e^{(u-2L)/2}`,

\[
(\log a)''(u)
=-\frac{z}{4(1-z)^2}<0.
\]

At `u=L`, the one-sided logarithmic derivatives satisfy

\[
(\log a)'(L^-)
=\frac{\sqrt2}{2(\sqrt2-1)}
>
-\frac1{2(\sqrt2-1)}
=(\log a)'(L^+).
\]

Thus the logarithmic derivative has a downward jump. Hence

\[
\boxed{
a\text{ is globally strictly log-concave on }(0,2\log2).
}
\tag{L-103000.2}
\]

## 2. Translation total positivity of order two

Define the translation kernel

\[
K(u,x)=a(u-x).
\]

For

\[
u_1<u_2,
\qquad
x_1<x_2,
\]

the function

\[
x\longmapsto
\log a(u_2-x)-\log a(u_1-x)
\]

is nondecreasing wherever both terms are finite, because `(log a)'` is nonincreasing. Taking endpoint limits when one translate leaves the support gives

\[
\boxed{
K(u_1,x_1)K(u_2,x_2)
-
K(u_1,x_2)K(u_2,x_1)
\ge0.
}
\tag{L-103000.3}
\]

Therefore the common positive two-box spline is a `TP_2` translation kernel.

## 3. Multiplicative form

For positive physical scales `X_1<X_2` and source locations `n_1<n_2`, equation (L-103000.3) becomes

\[
\boxed{
A(X_1/n_1)A(X_2/n_2)
-
A(X_1/n_2)A(X_2/n_1)
\ge0.
}
\tag{L-103000.4}

This theorem is source-blind but exact. It supplies a fixed sign for every order-concordant two-source minor of the positive common-mother half-kernel. It does not orient arbitrary signed arithmetic coefficients; that limitation is frozen in `R-103000`.