# L-99723 — A positive ratio-four B-spline is a zero-safe reciprocal-zeta detector

Claim ID: `L-99723`  
Status: **PROVED EXACT POSITIVE-KERNEL REDUCTION**  
Created: 2026-08-20  
Depends on: PR #653 scalar Mellin--Landau consumer  
RH status: **not assumed**

Put

\[
G(y)=2(\sqrt y-1)\mathbf1_{y\ge1},
\qquad
(S_2F)(y)=F(y/2),
\]

and define

\[
\boxed{
B=(I-S_2)(I-\sqrt2\,S_2)G.
}
\tag{L-99723.1}
\]

## 1. Exact positive compact kernel

Direct calculation gives

\[
\boxed{
B(y)=
\begin{cases}
2(\sqrt y-1),&1\le y<2,\\
\sqrt2(2-\sqrt y),&2\le y<4,\\
0,&\text{otherwise}.
\end{cases}
}
\tag{L-99723.2}
\]

Hence

\[
B(y)\ge0,
\qquad
\operatorname{supp}B\subset[1,4],
\qquad
B(1)=B(4)=0.
\]

Writing `a=log 2` and `u=log y`, its bilateral Laplace transform factors as

\[
\widehat B(s)
=
\frac{1-e^{-as}}s
\frac{1-e^{-a(s-1/2)}}{s-1/2}.
\tag{L-99723.3}
\]

Equivalently, `B(e^u)` is the convolution of the two positive functions

\[
\mathbf1_{[0,a]}(u)
\quad\text{and}\quad
 e^{u/2}\mathbf1_{[0,a]}(u).
\]

Thus the detector is a genuine positive multiplicative B-spline, not merely a
signed finite filter.

## 2. Exact scalar transform

Let

\[
\beta(n)=\mu(n)-\mathbf1_{67\mid n}\mu(n/67)
\]

and define

\[
b(X)=\sum_{n\le X}\frac{\beta(n)}{\sqrt n}B(X/n).
\tag{L-99723.4}
\]

For `Re(s)>1/2`, finite/absolute Fubini gives

\[
\boxed{
\int_1^\infty b(X)X^{-s-1}\,dX
=
\frac{
(1-67^{-(s+1/2)})
(1-2^{-s})
(1-2^{1/2-s})
}
{s(s-1/2)\zeta(s+1/2)}.
}
\tag{L-99723.5}
\]

The apparent singularities at `s=0` and `s=1/2` are removable in the kernel
factor. Its two finite-difference factors have zeros only on

\[
\Re s=0
\quad\text{and}\quad
\Re s=1/2.
\]

If `rho` is a nontrivial zeta zero with

\[
1/2<\Re\rho<1,
\]

then `s=rho-1/2` lies strictly between those two lines. Moreover
`1-67^{-rho}` is nonzero. Therefore no off-line reciprocal-zeta pole is
cancelled.

Consequently either eventual nonnegativity of `b`, or subpower logarithmic
negative mass of `b`, implies RH by the specialized Landau theorem of PR #653.

## 3. What this repairs and what it does not

The positive B-spline removes three avoidable complications:

```text
signed compact observation kernel;
activation jump at the left endpoint;
nonzero terminal value at the right endpoint.
```

It does not solve squarefree parity. On every prime interval `X/2<p<=X`, the
singleton contributions have one coherent sign because `B(X/p)>0`. Thus the
prime-interval separator of `R-99721` still refutes a universal branchwise
Carleson embedding.

The surviving source-orbit theorem may therefore use `B` in place of the
ratio-eight kernel, but it must still control covariance among distinct
squarefree cores. The kernel is now positive and double-clamped; the remaining
sign is entirely arithmetic.
