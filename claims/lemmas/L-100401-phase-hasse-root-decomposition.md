# L-100401 — Exact phase-Hasse root decomposition

Claim ID: `L-100401`  
Status: **PROVED EXACT FINITE PRODUCT IDENTITY**  
Created: 2026-08-20  
RH status: **not assumed**

Let labelled activities satisfy `0<a_i<1`, put

\[
z_i=p_i^{i\gamma},
\qquad
P_B(\gamma)=\prod_i(1-a_iz_i),
\qquad
s_B=\prod_i(1-a_i).
\]

For each `i`, define

\[
B_i^\pm(t,\gamma)
=\prod_{h\ne i}
[1-a_ht\pm a_h(1-t)z_h],
\]

\[
\mathscr S_B(\gamma)
={1\over2}\sum_i a_i(1-z_i)
\int_0^1[B_i^+(t,\gamma)-B_i^-(t,\gamma)]dt,
\]

and

\[
\mathscr T_B(\gamma)
=\sum_i a_i(1-z_i)\int_0^1B_i^+(t,\gamma)dt.
\]

Differentiate

\[
R(t)=\prod_i[1-a_it-a_i(1-t)z_i].
\]

Since

\[
-R'(t)=\sum_i a_i(1-z_i)B_i^-(t,\gamma),
\]

and

\[
R(0)=P_B(\gamma),
\qquad
R(1)=s_B,
\]

integration gives

\[
\sum_i a_i(1-z_i)\int_0^1B_i^-(t,\gamma)dt
=P_B(\gamma)-s_B.
\]

Therefore

\[
\boxed{
\mathscr S_B(\gamma)
={1\over2}[\mathscr T_B(\gamma)+s_B-P_B(\gamma)].
}
\tag{L-100401.1}
\]

At `gamma=0`, both `mathscr T_B(0)` and `s_B-P_B(0)` vanish, so
`mathscr S_B(0)=0`.  For nonzero phase, however, the symbol retains
`-P_B(gamma)/2`.
