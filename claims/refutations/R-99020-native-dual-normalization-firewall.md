# R-99020 — Native radix-four slack is not the complete parabolic score loss

Claim ID: `R-99020`  
Status: **PROVED EXACT NORMALIZATION FIREWALL**  
Created: 2026-08-18  
RH status: **unproved**

Let `C_d(q)` be the ordinary carry response of a finite row `d`, put

\[
\Xi_d(q)=C_d(q)-2C_d(4q),
\qquad
\Omega_X(q)=w_X(q)-2w_X(4q),
\]

and define the positive radix-four adjoint

\[
Y_4(q)=\sum_{h=0}^{v_4(q)}2^h\Lambda(q/4^h).
\]

The finite recurrence

\[
Y_4(q)-2\mathbf1_{4\mid q}Y_4(q/4)=\Lambda(q)
\]

gives, by finite summation by parts,

\[
\mathcal H(d)=\sum_q\Lambda(q)C_d(q)=\sum_qY_4(q)\Xi_d(q)
\]

and

\[
P_\Lambda(X)=\sum_q\Lambda(q)w_X(q)=\sum_qY_4(q)\Omega_X(q).
\]

Therefore the exact physical slack identity is

\[
\boxed{
P_\Lambda(X)-\mathcal H(d)
=\sum_qY_4(q)[\Omega_X(q)-\Xi_d(q)].
}
\tag{R-99020.1}

The positive parabolic benchmark is a different scalar,

\[
J_\Lambda(X)=\sum_{m=2}^{X}b_X(m)\log\frac m{m-1},
\]

and the complete arithmetic gap is

\[
F_\Lambda(X)=J_\Lambda(X)-P_\Lambda(X).
\]

Consequently

\[
\boxed{
J_\Lambda(X)-\mathcal H(d)
=F_\Lambda(X)+
 \sum_qY_4(q)[\Omega_X(q)-\Xi_d(q)].
}
\tag{R-99020.2}

Thus the vanished `L-94024` identity which replaced `P_Lambda` by `J_Lambda`
is false. The present candidate never makes that replacement. It proves a
direct lower bound for the literal score of one feasible row and uses

\[
F_\Lambda(X)\le J_\Lambda(X)-\mathcal H(d).
\]

This firewall is mandatory in every endpoint proof.
