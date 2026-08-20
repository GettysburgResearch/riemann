# L-99827 — Exact seven-band compression of every fixed-shell Hardy tail

Claim ID: `L-99827`  
Status: **PROVED EXACT FINITE-BAND REDUCTION**  
Created: 2026-08-20  
Depends on: `L-99824`, `L-99825`  
RH status: **not assumed**

Let `\widetilde K` be the fixed compact kernel of `L-99824`. On every active
cell it has the form

\[
\widetilde K(y)=a_r\sqrt y+b_r+c_r\log y.
\tag{L-99827.1}
\]

The exact cells and coefficients are:

\[
\begin{array}{c|c|c|c}
r&[u_r,v_r)&a_r&b_r\quad;\quad c_r\\ \hline
1&[1,2)&8&-8\quad;\quad-3\\
2&[2,4)&0&
8(\sqrt2-1)-3\sqrt2\log2\quad;\quad3(\sqrt2-1)\\
3&[4,8)&-4&
8\sqrt2-(6+3\sqrt2)\log2\quad;\quad3\sqrt2\\
4&[8,67)&0&
6(\sqrt2-1)\log2\quad;\quad0\\
5&[67,134)&-8/\sqrt{67}&
8-3\log67+6(\sqrt2-1)\log2\quad;\quad3\\
6&[134,268)&0&
8(1-\sqrt2)+3(\sqrt2-1)\log67+(9\sqrt2-6)\log2
\quad;\quad3(1-\sqrt2)\\
7&[268,536)&4/\sqrt{67}&
\sqrt2(-8+9\log2+3\log67)\quad;\quad-3\sqrt2.
\end{array}
\tag{L-99827.2}
\]

Outside `[1,536]` the kernel is zero.

## Proof of the table

For `1<=y<67`,

\[
W(y)=8\sqrt y-8-3\log y,
\]

while for `y>=67`,

\[
W(y)=8(1-67^{-1/2})\sqrt y-3\log67.
\]

Insert the appropriate branch of `W` into

\[
\widetilde K(y)
=W(y)-\sqrt2W(y/2)-W(y/4)+\sqrt2W(y/8).
\]

The only activation points are

\[
1,2,4,8,67,134,268,536.
\]

Collecting the coefficients of `sqrt(y)`, `1`, and `log(y)` gives
(L-99827.2). This is exact algebra in `Q(sqrt(2),sqrt(67),log2,log67)`.

## Three native moment states

Put

\[
A_\beta(t)=\sum_{n\le t}\frac{\beta(n)}n,
\qquad
C_\beta(t)=\sum_{n\le t}\frac{\beta(n)}{\sqrt n},
\qquad
L_\beta(t)=\sum_{n\le t}\frac{\beta(n)\log n}{\sqrt n}.
\tag{L-99827.3}
\]

For a band `[u_r,v_r)` and an integer interval `(M,N]` contained in its
corresponding source range

\[
X/v_r<n\le X/u_r,
\]

one has exactly

\[
\boxed{
\begin{aligned}
\sum_{M<n\le N}\frac{\beta(n)}{\sqrt n}\widetilde K(X/n)
={}&a_r\sqrt X\,[A_\beta(N)-A_\beta(M)]\\
&+(b_r+c_r\log X)[C_\beta(N)-C_\beta(M)]\\
&-c_r[L_\beta(N)-L_\beta(M)].
\end{aligned}
}
\tag{L-99827.4}
\]

Consequently every suffix appearing in the Hardy square,

\[
S_X(v)=\sum_{n\ge v}d_X(n),
\]

is an exact linear combination of at most seven band contributions and hence
of at most twenty-one evaluations of the three states in (L-99827.3).

The fixed-shell Hardy–Carleson gate is therefore finite-dimensional at each
endpoint. The remaining difficulty is the cross-scale signed correlation of
these native moment states; no unrecorded kernel or infinite activation
ledger remains.
