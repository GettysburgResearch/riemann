# L-96305 — The one-row Mellin consumer has a strictly positive Volterra derivative profile

Claim ID: `L-96305`  
Status: **PROVED EXACT PIECEWISE PROFILE**  
Created: 2026-08-17  
Depends on: the positive infinitesimal row `p_s` of PR #495  
RH status: **not assumed**

Define

\[
p_s^*=5p_s(2)+3p_s(3).
\]

Using

\[
g_s(m)=\left(\sqrt m-\frac m{\sqrt s}\right)\mathbf1_{m\le s}
\]

inside the exact component-row map gives

\[
\boxed{
p_s^*=
\begin{cases}
0,&1\le s<2,\\
15\sqrt2-30s^{-1/2},&2\le s<3,\\
15\sqrt2-9\sqrt3-3s^{-1/2},&3\le s<4,\\
15\sqrt2-9\sqrt3-6+9s^{-1/2},&4\le s<5,\\
15\sqrt2-9\sqrt3+3\sqrt5-6-6s^{-1/2},&s\ge5.
\end{cases}}
\tag{L-96305.1}
\]

Every branch is nonnegative, and it is strictly positive for `s>2`.

The signs follow from monotonicity in `s^{-1/2}` and elementary rational radical bounds. For example,

\[
15\sqrt2-10\sqrt3>0
\]

by squaring, while on the two last branches one may use

\[
\sqrt2>7/5,\qquad \sqrt3<7/4,
\qquad 2<\sqrt5<9/4.
\]

Consequently the continuum scalar row has the exact representation

\[
\boxed{
5\overline c_X(2)+3\overline c_X(3)
=
\int_1^X\frac{2\mathscr L(X/s)}s p_s^*\,ds.
}
\tag{L-96305.2}
\]

The consumer profile itself therefore contains no sign obstruction. All remaining sign is in the scalar reciprocal-zeta density or, more weakly, its affine cell moments.
