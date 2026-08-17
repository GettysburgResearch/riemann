# L-96503 - Global parity-aware common-source gluing has an exact primal-dual theorem

Claim ID: `L-96503`
Status: **PROVED EXACT FINITE-DIMENSIONAL GLUING / SEPARATION THEOREM**
Created: 2026-08-17
RH status: **unproved; the global producer remains open**

Fix an endpoint after expanding the entire finite rough-prime source tree and
incorporating every cumulative history parity. Let `E` and `O` be the actual
positive even and odd atoms, with coefficients `a_e,b_o>=0`. Each atom has a
strictly positive target `t_i`, a score `s_i`, and a row vector `r_i` in a
closed finite-dimensional cone `K`.

A global common-source removal is a vector

\[
0\le u_e\le a_e
\]

satisfying the exact target identity

\[
\boxed{\sum_eu_et_e=\sum_ob_ot_o.}
\tag{L-96503.1}
\]

Use the same `u_e` in target, score, and every row. If additionally

\[
\boxed{
\sum_eu_er_e-\sum_ob_or_o\in K,
\qquad
\sum_eu_es_e\le\sum_ob_os_o,}
\tag{L-96503.2}
\]

then define

\[
\nu_e=a_e-u_e\ge0,
\quad
B=\sum_eu_er_e-\sum_ob_or_o\in K,
\quad
\sigma=\sum_ob_os_o-\sum_eu_es_e\ge0.
\]

The signed source has the exact positive typed decomposition

\[
R(E)-R(O)=R(\nu)+B\in K,
\]

with exact signed target carried by `nu` and nonnegative score surplus `sigma`.
Every source coefficient is spent once.

Conversely, the coefficient box is compact and convex and the target/row/score
constraints are closed and convex. If they are infeasible, strong separation
supplies a dual functional excluding **every** common-source removal, not just a
chosen greedy or leafwise Hall map.

For rows two and three, take `K=R_+^2`. The resulting all-endpoint statement is
called `GPHT23`. It is the clean parity-covariant successor to the invalid
leafwise gluing theorem. It is finite at each endpoint but not proved uniformly
in this packet.
