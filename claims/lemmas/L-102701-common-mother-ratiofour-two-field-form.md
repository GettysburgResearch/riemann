# L-102701 — The common mother converts the defect into one ratio-four two-field packet

Claim ID: `L-102701`  
Status: **PROVED EXACT SOURCE/KERNEL FACTORIZATION**  
Created: 2026-08-22  
Depends on: `L-102700`; PR #696 `L-102009`; PR #715 `L-102500`  
RH status: **not assumed**

Let \(A\) be the positive two-box spline of PR #696:

\[
\widehat A(s)
=
\frac{(1-2^{-s})(1-\sqrt2\,2^{-s})}
{s(s-\frac12)},
\qquad
\operatorname{supp}A\subset[1,4].
\]

Put

\[
A_-=(D-\tfrac12)A.
\]

PR #715 gives

\[
m_\Phi(s)
=
\frac{2(1-\sqrt2\,2^{-s})^2(1-2^{-s})^2}
{s^2(s-\frac12)}.
\]

Therefore

\[
\boxed{
\Phi_*=2\,A_- *_M A.
}
\tag{L-102701.1}
\]

Define the two physical half-divisor fields

\[
F_-(Y)
=
\sum_d\frac{\lambda_-(d)}{\sqrt d}A_-(Y/d),
\]

\[
F_+(Z)
=
\sum_e\frac{\lambda_+(e)}{\sqrt e}A(Z/e).
\]

Finite arithmetic and Mellin Fubini now give

\[
\boxed{
H_{\rm def}(X)
=
2\int_0^\infty
F_-(Y)F_+(X/Y)\frac{dY}{Y}.
}
\tag{L-102701.2}
\]

Because both kernels are supported in \([1,4]\), every finite-horizon integral
is compact.

The first kernel is the explicit dyadic step

\[
A_-(y)=
\begin{cases}
1,&1<y<2,\\
-\sqrt2,&2<y<4,\\
0,&\text{otherwise}.
\end{cases}
\]

Thus the entire completion defect is a same-occurrence ratio-four packet with:

```text
left source:   root-free half-divisor difference lambda_-;
right source:  half-divisor sum lambda_+;
left kernel:   exact half-order dyadic step A_-;
right kernel:  positive two-box spline A.
```

No Cauchy inequality or regional absolute value has yet been used.
