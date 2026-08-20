# L-103100 — Exact Haar-Gram formula for the half-completed Vaughan field

**Status:** PROVED EXACT.

Let

\[
\eta(p^k)=\frac{\binom{2k}{k}}{4^k},\qquad
b_U(n)=\mu(n)\mathbf 1_{n>U},\qquad h_U=b_U*\eta.
\]

Retain the ratio-four kernel of PR #696,

\[
A_-(y)=
\begin{cases}
1,&1<y<2,\\
-\sqrt2,&2<y<4,\\
0,&\text{otherwise}.
\end{cases}
\]

For a finite cutoff `N>U`, define

\[
H_{U,N}(Y)=\sum_{U<n\le N}\frac{h_U(n)}{\sqrt n}A_-(Y/n).
\]

The field is supported in `[U,4N]`. Put `h=log 2` and

\[
\psi(u)=\mathbf 1_{(0,h)}(u)-\sqrt2\,\mathbf 1_{(h,2h)}(u).
\]

Then `A_-(e^u)=psi(u)` and, with

\[
R(v)=\int_{\mathbb R}\psi(u)\psi(u+v)\,du,
\]

one has

\[
\boxed{
\int_U^{4N}|H_{U,N}(Y)|^2\frac{dY}{Y}
=
\sum_{U<m,n\le N}
\frac{h_U(m)h_U(n)}{\sqrt{mn}}
R\!\left(\log\frac mn\right).
}
\tag{L-103100.1}
\]

The kernel is even and explicit:

\[
\boxed{
R(v)=
\begin{cases}
3h-(3+\sqrt2)|v|,&0\le |v|\le h,\\
-\sqrt2(2h-|v|),&h\le |v|\le2h,\\
0,&|v|\ge2h.
\end{cases}}
\tag{L-103100.2}
\]

In particular, the Gram matrix has exact multiplicative support

\[
\boxed{R(\log(m/n))=0\quad\text{unless}\quad 1/4<m/n<4.}
\tag{L-103100.3}
\]

## Proof

The support assertion makes every sum finite. Expanding the square and setting `Y=e^u` gives

\[
\sum_{m,n}\frac{h_U(m)h_U(n)}{\sqrt{mn}}
\int\psi(u-\log m)\psi(u-\log n)\,du,
\]

which is (L-103100.1) after translation. Formula (L-103100.2) follows by measuring the three interval overlaps. For `0<=v<=h`, the two same-sign overlaps have total weight `3(h-v)` and the first-to-second overlap contributes `-sqrt(2)v`. For `h<=v<=2h`, only the first-to-second overlap remains, of length `2h-v`.
