# L-99220 — One typed child kernel propagates score and every physical capacity coordinate

Claim ID: `L-99220`  
Status: **PROVED EXACT ABSTRACT COMPOSITION THEOREM; LOCAL ARITHMETIC INPUTS EXPLICIT**  
Created: 2026-08-19  
Frozen parent: PR #625 at `b7164582c458b53aeefecf7d4044984c9fa4686a`  
RH status: **unproved**

Let `V` be a finite scale DAG. At each typed state `v`, let

- `m_v>=0` be actual target mass;
- `S_v` be the ideal literal score;
- `Omega_v` be the complete ordinary/radix-four capacity vector in an ordered
  real vector space;
- `P_v` be the ideal typed physical packet.

Assume there is one positive child measure `kappa_v` and one current-owned
packet `C_v` such that, in every typed coordinate,

\[
P_v=C_v\oplus\int P_w\,d\kappa_v(w),
\tag{L-99220.1}
\]

\[
m_v=c_v+\int m_w\,d\kappa_v(w),
\qquad c_v=m(C_v),
\tag{L-99220.2}
\]

\[
S_v=s_v+\int S_w\,d\kappa_v(w),
\tag{L-99220.3}
\]

\[
\Omega_v=\omega_v+\int\Omega_w\,d\kappa_v(w).
\tag{L-99220.4}
\]

The same `kappa_v` must appear in all four equations. Survival and
lambda-current terms are contained in `C_v`; only normalized alpha-children
belong to `kappa_v`.

Let `R` be the positive linear physical-response map and `H` the nonnegative
linear literal-score functional. Suppose the current packet has a realization
`\widehat C_v` satisfying

\[
R(\widehat C_v)\le\omega_v,
\tag{L-99220.5}
\]

\[
H(\widehat C_v)\ge s_v-D_0c_v
\tag{L-99220.6}
\]

for one constant `D_0>=0`.

Define recursively

\[
\widehat P_v
=
\widehat C_v\oplus
\int\widehat P_w\,d\kappa_v(w).
\tag{L-99220.7}
\]

Then

\[
\boxed{R(\widehat P_v)\le\Omega_v}
\tag{L-99220.8}
\]

and

\[
\boxed{H(\widehat P_v)\ge S_v-D_0m_v}
\tag{L-99220.9}
\]

at every state.

## Proof

Backward induction applies because the scale DAG is finite. If the conclusions
hold at every child, positivity and Tonelli give

\[
\begin{aligned}
R(\widehat P_v)
&=
R(\widehat C_v)
+\int R(\widehat P_w)\,d\kappa_v(w)\\
&\le
\omega_v+\int\Omega_w\,d\kappa_v(w)
=\Omega_v.
\end{aligned}
\]

Likewise,

\[
\begin{aligned}
H(\widehat P_v)
&=
H(\widehat C_v)
+\int H(\widehat P_w)\,d\kappa_v(w)\\
&\ge
s_v-D_0c_v
+\int(S_w-D_0m_w)\,d\kappa_v(w)\\
&=
S_v-D_0m_v.
\end{aligned}
\]

This proves both assertions.

## Positive endpoint integration as a virtual root

Let `nu` be a finite positive endpoint measure and suppose every endpoint
packet carries the same typed feature list. Introduce a virtual root `star`
with `C_star=0` and child measure `nu`. Then

\[
m_\star=\int m_v\,d\nu(v),\quad
S_\star=\int S_v\,d\nu(v),\quad
\Omega_\star=\int\Omega_v\,d\nu(v).
\]

The theorem applies unchanged. Thus the continuum endpoint construction and
the varying-prime recursive tree are one cone-valued Bellman system. No
row-only Caratheodory compression is required for existence.

## Statement-to-use boundary

This theorem closes the composition step only. It does not prove:

- positivity or exact normalization of the endpoint measure;
- the local current inequalities;
- the all-column arithmetic bounds;
- the endpoint or Mellin–Landau consumer.
