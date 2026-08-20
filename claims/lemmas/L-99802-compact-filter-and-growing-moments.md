# L-99802 — Compact zero-safe filter and growing moment tower

Let \((S_af)(x)=f(x/a)\), with zero extension below one, and define

\[
\mathcal K=(I-S_2)(I-2S_4).
\]

For \(T(y)=(4\sqrt y-3)\mathbf1_{y\ge1}\),

\[
(\mathcal KT)(y)=
\begin{cases}
4\sqrt y-3,&1\le y<2,\\
(4-2\sqrt2)\sqrt y,&2\le y<4,\\
6-2\sqrt2\sqrt y,&4\le y<8,\\
0,&y\ge8.
\end{cases}
\]

Its Mellin multiplier is

\[
K(s)=(1-2^{-s})(1-2\,4^{-s}).
\]

Its zeros lie only on \(\Re s=0\) and \(\Re s=1/2\); hence it cannot cancel a
pole at \(s=\rho-\tfrac12\) with \(\tfrac12<\Re\rho<1\).

On \(2^L\le x<2^{L+1}\), put

\[
M_L=\max\!\left(
1,\left\lfloor\frac{L}{(\log(L+e))^3}\right\rfloor
\right),
\qquad
\mathcal F_L=(I-S_2)^{M_L}\mathcal K.
\]

Then:

\[
\text{forward mass}=2^{M_L}=2^{o(L)},
\]

\[
\text{support ratio}=2^{M_L+3}=2^{o(L)},
\]

and

\[
(I-S_2)^{-M_L}
=\sum_{k\ge0}\binom{M_L+k-1}{k}S_{2^k}.
\]

On the block, the active inverse mass is at most

\[
\boxed{
\binom{M_L+L+1}{M_L}=2^{o(L)}.
}
\]

Thus all filter-combinatorial and diagonal costs are subpower. The compact
kernel is signed; no pointwise positivity is asserted.
