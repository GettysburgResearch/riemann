# L-98074 — Vanishing Lorenz hinge supplies a subpower squarefree-shell reserve

Claim ID: `L-98074`  
Status: **PROVED ASYMPTOTIC REDUCTION**  
RH status: **unproved**

For the completed Lorenz slack,
\[
D_X^+(\lambda)=\lambda T_O+\sum_{i\in E}a_i(r_i-\lambda t_i)_+-R_O,
\]
write `R_X=D_X^+(0)` and let `T_{E,+}` be target capacity carried by
positive-scalar even atoms. Then exactly
\[
D_X^+(\lambda)=R_X+\lambda G_X+\mathcal E_X(\lambda),
\quad
G_X=T_O-T_{E,+},
\]
where
\[
\mathcal E_X(\lambda)=
\sum_{\substack{i\in E\\0<r_i/t_i<\lambda}}
a_i(\lambda t_i-r_i)\ge0.
\]

The ordered scalar/target ratio near its zero at `Y=2` gives
\[
Y_\lambda=2+\kappa\lambda+O(\lambda^2),
\quad
\kappa=(16-6\sqrt2)/15,
\]
hence the correction is supported on a thin shell and
\[
\mathcal E_X(\lambda)\ll\lambda^2\sqrt X+\lambda/\sqrt X.
\]

The squarefree-shell theorem gives
\[
G_X=c_*\sqrt X+o(\sqrt X),
\quad
c_*=\frac3{\pi^2}(4\log2+3\sqrt2-6)
=0.3085927362743162\ldots.
\]

For any subpower `L(X)` with `L(X)^2=o(sqrt X)` and
\[
\lambda_X=L(X)/\sqrt X,
\]
we obtain
\[
D_X^+(\lambda_X)=R_X+c_*L(X)+o(L(X)).
\]
The two-orientation cushion is
\[
D_X^+(\lambda_X)+D_X^-(\lambda_X)
\ge(2c_*+o(1))L(X).
\]

Thus eventual nonnegativity, or more generally subpower logarithmic negative
mass, of this vanishing hinge implies subpower negative mass of `R_X`, and
therefore RH by `L-98072`.
