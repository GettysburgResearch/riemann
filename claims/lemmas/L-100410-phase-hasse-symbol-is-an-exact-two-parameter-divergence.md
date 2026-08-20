# L-100410 — The symmetric phase-Hasse symbol is an exact two-parameter divergence

Claim ID: `L-100410`  
Status: **PROVED EXACT PRODUCT IDENTITY**  
Created: 2026-08-20  
Depends on: PR #672 `L-99990--L-99991`  
RH status: **not assumed**

Let the labelled activities be \(0<a_i<1\), put

\[
z_i(\gamma)=p_i^{i\gamma},
\]

and define

\[
P(t,\eta;\gamma)
=
\prod_i
\left[
1-a_it+\eta a_i(1-t)z_i(\gamma)
\right].
\]

Set

\[
A(t,\eta;\gamma)
=
\sum_i a_i(1-z_i)
\prod_{h\ne i}
\left[
1-a_ht+\eta a_h(1-t)z_h
\right].
\]

Direct differentiation gives the exact divergence identity

\[
\boxed{
A
=
-\left(
\partial_t+\frac{1+\eta}{1-t}\partial_\eta
\right)P.
}
\]

Indeed, the coefficient attached to the \(i\)-th deleted factor is

\[
a_i(1+\eta z_i)-(1+\eta)a_iz_i=a_i(1-z_i).
\]

The symmetric phase-Hasse symbol of PR #672 is

\[
\mathscr S_B(\gamma)
=
\frac12\sum_i a_i(1-z_i)
\int_0^1
\left[B_i^+(t,\gamma)-B_i^-(t,\gamma)\right]dt.
\]

Using

\[
B_i^+-B_i^-=
\int_{-1}^1\partial_\eta B_i(t,\eta)\,d\eta
\]

gives the exact area formula

\[
\boxed{
\mathscr S_B(\gamma)
=
\frac12\int_0^1\int_{-1}^1
(1-t)
\sum_{i\ne j}
a_ia_j(1-z_i)z_j
\prod_{h\ne i,j}
[1-a_ht+\eta a_h(1-t)z_h]
\,d\eta\,dt.
}
\]

Consequences:

1. the degree-zero sector is absent;
2. the degree-one sector is absent;
3. every surviving term contains one physical phase difference \(1-p_i^{i\gamma}\);
4. the two labelled copies of \(67\) remain separate;
5. \(\mathscr S_B(0)=0\) before physical collapse.

This is a stronger root-free normal form than the first product expression in
PR #672.
