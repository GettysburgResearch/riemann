# L-91411 — Lorenz cutoff determinant reduction

Status: **PROVED EXACT REDUCTION**. RH remains unproved.

Let `E,O` be the positive even and odd measures in score units. Put
\[
S_{sig}=E(D)-O(D)>0.
\]
For one component row write `q(d)=K_R(d)/K_S(d)`. Let `U<=E` be the leftmost submeasure with `U(D)=O(D)`, let `c` be its cutoff atom, and set `nu=E-U`.

The live cutoff theorem gives `c>y`. By `L-91410`, the ratio `q` is nonincreasing on the outer sector. Hence `nu` is supported on `d>=c` and
\[
R(nu)\le q(c)S_{sig}.
\]

Writing
\[
R_{sig}=E_R-O_R,
\qquad S_c=K_S(c)>0,
\qquad R_c=K_R(c),
\]
we obtain
\[
\boxed{
R_{sig}S_c-S_{sig}R_c\ge0
\quad\Longrightarrow\quad
R(nu)\le R_{sig}.
}
\]
Thus the remaining row gate is the single determinant
\[
\boxed{
\Delta_{j,c}(p,y)=
R_{sig}^{(j)}K_S(c)-S_{sig}K_R^{(j)}(c)\ge0.
}
If the cutoff row is inactive, `R_c=0`, so only signed-row positivity is needed.
