# L-103102 — Fractional Nyman representation and exact near-collision equivalence

**Status:** PROVED EXACT REDUCTION; TERMINAL CORRELATION OPEN.

Define the finite Dirichlet polynomial

\[
P_{U,N}(z)=\sum_{U<n\le N}\frac{h_U(n)}{n^z}.
\]

Mellin Plancherel applied to `L-103100` gives

\[
\boxed{
\int_U^{4N}|H_{U,N}(Y)|^2\frac{dY}{Y}
=
\frac1{2\pi}\int_{\mathbb R}
|\widehat A_-(i\gamma)|^2
|P_{U,N}(1/2+i\gamma)|^2\,d\gamma.
}
\tag{L-103102.1}
\]

For `Re z>1`, the untruncated source has the exact Dirichlet series

\[
\sum_{n\ge1}\frac{h_U(n)}{n^z}
=
\left(\frac1{\zeta(z)}-\sum_{n\le U}\frac{\mu(n)}{n^z}\right)\zeta(z)^{1/2}
=
\zeta(z)^{-1/2}-M_U(z)\zeta(z)^{1/2}.
\tag{L-103102.2}
\]

Thus the field energy is a compactly weighted, finite fractional Nyman--Beurling approximation error.

Write the exact Gram energy as

\[
\mathcal H_{U,N}=\mathcal D_{U,N}+\mathcal O_{U,N},
\]

where the off-diagonal is

\[
\boxed{
\mathcal O_{U,N}
=
\sum_{\substack{U<m,n\le N\\m\ne n\\1/4<m/n<4}}
\frac{h_U(m)h_U(n)}{\sqrt{mn}}
R\!\left(\log\frac mn\right).
}
\tag{L-103102.3}
\]

Because `H>=0` and `D=N^{o(1)}` by `L-103101`, the field-energy condition of PR #696 is equivalent to the one-sided estimate

\[
\boxed{
\int_{2^L}^{2^{L+1}}
[\mathcal O_{U_X,N_X}]_+\frac{dX}{X}=2^{o(L)},
\quad
U_X=\lfloor X^{1/3}\rfloor,
\quad
N_X=\lfloor X/U_X\rfloor.
}
\tag{HCNC103100}
\]

Indeed `O_+<=H`, while `H<=D+O_+`. Hence `HCNC103100` is neither an absolute correlation nor a coefficient diagonal; it is the exact signed ratio-four cross-core left by the half-completed Vaughan reduction.
