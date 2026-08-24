# Wick cancellation and the low-order Xi Pick model

Let

\[
A(s)=\sum_{n\ge2}\Lambda(n)n^{-s},
\qquad
R_L(s)=(L-A(s))^{-1}.
\]

Its coefficient at `N>1` is

\[
b_L(N)=\sum_{m=1}^{\Omega(N)}L^{-m-1}\Lambda^{*m}(N).
\]

The frozen xi-prime coefficient family is

\[
C(N;L)=-\Lambda(N)+
\sum_{m=1}^{\Omega(N)}L^{-m}
[(\Lambda\log)*\Lambda^{*(m-1)}](N).
\]

Since

\[
\log N\,\Lambda^{*m}(N)
=m[(\Lambda\log)*\Lambda^{*(m-1)}](N),
\]

we obtain the exact bridge

\[
-\partial_LC(N;L)=\log N\,b_L(N).
\]

For the finite entire prime polynomial `A_X`, set

\[
W_{L,X}=\exp(-A_X/(2L)).
\]

It never vanishes, so it changes every finite critical-residue matrix by an
invertible congruence. With `x=A_X/L`,

\[
{LW_{L,X}^2\over L-A_X}
={e^{-x}\over1-x}
=1+\sum_{m\ge2}c_mx^m,
\qquad
c_m=\sum_{j=0}^m{(-1)^j\over j!}.
\]

The coefficient of `x` is exactly zero.

For squarefree `n=p_1...p_m`,

\[
\Lambda^{*m}(n)=m!\prod_j\log p_j.
\]

PNT and `u_j=log p_j/L` give

\[
L^{-2m}
\sum_{p_1<...<p_m\atop p_1...p_m\le e^L}
\prod_j{(\log p_j)^2\over p_j}
\to{1\over m!(2m)!}.
\]

Repeated prime powers lose one `L^2` prime integral and are negligible;
dominated convergence gives

\[
\sum_{n\le e^L}{a_L(n)^2\over n}
\to
\mathcal D_W=\sum_{m\ge2}c_m^2{m!\over(2m)!}.
\]

The first three terms and a geometric tail yield

\[
\mathcal D_W
\le{1\over48}+{1\over1080}+{3\over35840}
+{11\over1270080}
<{7\over320}.
\]

The correctly normalized two-sided symbol is

\[
\boxed{
f_L(t)=1+2\Re\sum_{n\le e^L}
a_L(n)n^{-1/2-it}.
}
\]

An earlier version omitted `n^-1/2` while retaining `/n` in the energy; that
display is corrected by `L-105520`.

The symbol has mean `1+o(1)` and mean square below `167/160+o(1)` by the
Montgomery--Vaughan mean-value theorem. Any constant-diagonal finite
compression therefore has normalized effective rank at least `160/167`.
After one-percent trace/HS transfer this becomes

\[
{160\over167}\left({99\over101}\right)^2
={1568160\over1703567}.
\]

With the T-105310 nuisance index `821/10000`, exact reverse Rolle gives

\[
2{1568160\over1703567}-1-{821\over5000}
={5765136493\over8517835000}
=0.676831\ldots .
\]

The remaining theorem is the actual-Xi transfer `WXFER105320`. The model
calculation does not itself prove a new zero proportion or RH.  At a physical
cutoff `e^(alpha L)`, the scaled energy law of `L-105520` must be used.
