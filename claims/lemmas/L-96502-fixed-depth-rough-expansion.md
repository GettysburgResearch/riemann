# L-96502 - Exact fixed-depth rough-prime expansion and parity of the recursive frontier

Claim ID: `L-96502`
Status: **PROVED EXACT SOURCE PARTITION**
Created: 2026-08-17
RH status: **unproved**

Let `P_j(x)` be the positive paired source whose allowed rough primes are
`p_j,p_(j+1),...`, let `S(E,O)=(O,E)`, and let `b_j(x)` be the base with no
allowed rough prime. Unique least-prime factorization gives

\[
P_j(x)=b_j(x)\oplus
\bigoplus_{k\ge j}p_k^{-1/2}S P_{k+1}(x/p_k).
\tag{L-96502.1}
\]

Iterating exactly `L` times gives

\[
\boxed{
\begin{aligned}
P_j(x)={}&
\bigoplus_{r=0}^{L-1}
\ \bigoplus_{j\le k_1<\cdots<k_r}
(p_{k_1}\cdots p_{k_r})^{-1/2}S^r
b_{k_r+1}\!\left(\frac{x}{p_{k_1}\cdots p_{k_r}}\right)\\
&\oplus
\bigoplus_{j\le k_1<\cdots<k_L}
(p_{k_1}\cdots p_{k_L})^{-1/2}S^L
P_{k_L+1}\!\left(\frac{x}{p_{k_1}\cdots p_{k_L}}\right),
\end{aligned}}
\tag{L-96502.2}
\]

with the `r=0` term interpreted as `b_j(x)`.

The source classes are disjoint and exhaustive: a history of length `r<L`
terminates in exactly one current base, and a history of length at least `L`
has exactly one first ordered `L`-tuple. Coefficient magnitudes factor exactly.
The recursive frontier has cumulative parity `(-1)^L` and endpoint at most

\[
\frac{x}{p_jp_{j+1}\cdots p_{j+L-1}}.
\]

For `L=2`, the recursive frontier is canonically even and contracts by at least
`67*71`. This source identity is exact. It does **not** imply that the signed
current block is nonnegative; `R-96501` proves that every fixed even depth has
the opposite asymptotic sign.
