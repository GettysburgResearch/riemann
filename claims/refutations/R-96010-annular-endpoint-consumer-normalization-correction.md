# R-96010 — The native endpoint consumer in PR #535 is invalid after the exact \(J_\Lambda/P_\Lambda/F_\Lambda\) audit

Claim ID: `R-96010`  
Status: **EXACT NORMALIZATION CORRECTION / SUPERSESSION**  
Created: 2026-08-16  
Frozen target: PR #535 at `988e9bfa55e7ed13c0ddbcab2f6138a83fd4f743`  
Correction source: PR #541 at `e381f444191e214cc992208b16d30a8d5fd461ac`  
RH status: **unproved**

Let

\[
w_X(q)=q^{-1/2}\log(X/q)\mathbf 1_{q\le X},
\qquad
\Omega_X(q)=w_X(q)-2w_X(4q),
\]

and

\[
Y_4(q)=\sum_{4^a\mid q}2^a\Lambda(q/4^a).
\]

For every finitely supported ordinary response \(C\), finite reindexing gives

\[
\sum_qY_4(q)[C(q)-2C(4q)]=\sum_q\Lambda(q)C(q).
\tag{R-96010.1}
\]

Consequently,

\[
\langle Y_4,\Omega_X\rangle
=P_\Lambda(X)
:=\sum_{q\le X}\frac{\Lambda(q)}{\sqrt q}\log(X/q),
\tag{R-96010.2}
\]

not the parabolic benchmark \(J_\Lambda(X)\). For a physical row \(d\),

\[
\langle Y_4,\Xi_d\rangle=\mathcal H(d).
\]

Thus the exact identity is

\[
\boxed{
J_\Lambda(X)-\mathcal H(d)
=F_\Lambda(X)+
\langle Y_4,\Omega_X-\Xi_d\rangle,
}
\tag{R-96010.3}
\]

where \(F_\Lambda=J_\Lambda-P_\Lambda\).

Even exact saturation \(C_d=w_X\) gives only

\[
\mathcal H(d)=P_\Lambda(X),
\qquad
J_\Lambda(X)-\mathcal H(d)=F_\Lambda(X).
\]

It does not prove \(F_\Lambda\le0\), a square-root bound, or RH. Therefore the
endpoint conclusion in `T-94201` on PR #535 is withdrawn. The finite annular
telescope remains exact algebra; only its old consumer is invalidated.
