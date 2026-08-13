# L-91653 — Complete endpoint theorem data

Claim ID: `L-91653`  
Status: **PROVED DEFINITIONAL THEOREM**  
Created: 2026-08-13  
Depends on: `L-91112`, `L-90027`, `L-90029`, `L-91406`  
RH status: **unproved**

A typed endpoint datum is

\[
P=(\ell,J,T,S,q,\Gamma,\Xi,b),
\]

where `ell` is the arithmetic provenance label, `J` is the benchmark, `T` is
the SHARP target, `S` is the declared score, `q` is the nonnegative component
row, `Gamma` and `Xi` are its ordinary and radix-four responses, and `b` is the
finite boundary-reserve vector. All coordinates are additive and positively
homogeneous.

For `u>=1`, let `Q_u(j)` be the exact component row of `L-91112`. Put

\[
T(u)=4\sqrt u-3,
\qquad
S(u)=5\sqrt u-3,
\]

and

\[
E(u)=\sum_{2\le m\le u}
\frac{\log m}{\sqrt m}\log\frac um.
\]

The native datum has benchmark `J=S(u)`, target `T(u)`, declared score `S(u)`,
row `q_j=Q_u(j)`, exact linear responses `Gamma,Xi`, and zero boundary reserve.
Its literal row score is `E(u)`.

Let `F_X(P)` be the cone of nonnegative endpoint rows whose ordinary,
radix-four and finite-boundary uses do not exceed the corresponding coordinates
of `P`. Define

\[
\boxed{
\Delta_X(P)=J(P)-
\sup_{d\in F_X(P)}\operatorname{Score}_X(d).
}
\]

The native row is feasible against its own response coordinates, so

\[
\Delta_X(P_u)\le S(u)-E(u).
\]

For `r=p^{-1/2}` and `u>=p`, the causal datum is the complete coordinatewise
difference

\[
P_u-rU_pP_{u/p}.
\]

Its two endpoint labels are retained. `L-91654` proves its nonnegative target,
row and response coordinates; `L-91656` bounds its literal deficit. Finite
Hall, collar, terminal and boundary corrections are represented by one separate
nonrecursive datum in `L-91655`.