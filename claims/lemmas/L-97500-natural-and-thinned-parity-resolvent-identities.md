# L-97500 — Natural and thinned parity-resolvent identities

Claim ID: `L-97500`  
Status: **PROVED EXACT FINITE SOURCE/OPERATOR THEOREM**  
Created: 2026-08-17  
RH status: **not assumed**

Let `V` be a finite acyclic first-owner state set. The natural least-prime
operator is the positive nilpotent operator

\[
 (R f)_v=\sum_{w\in\operatorname{Ch}(v)}r_{vw}f_w,
 \qquad r_{vw}=p(v,w)^{-1/2}.
\]

Cumulative rough parity gives the exact signed recursion

\[
 \boxed{(I+R)F=b.}
 \tag{L-97500.1}
\]

Here `b` is the depth-zero grouped P61 packet and `F` is the complete signed
rough expansion.

Let `A` be any second positive nilpotent child operator on the same directed
edges. If a proposed contractive representation writes

\[
 \boxed{(I+A)F=g_A,}
 \tag{L-97500.2}
\]

then necessarily

\[
 \boxed{g_A=b-(R-A)F.}
 \tag{L-97500.3}
\]

This is obtained by subtracting (L-97500.2) from (L-97500.1). In particular, if
`0<=A<R`, the current contains the complete all-depth signed residual
`(R-A)F`. It is not determined by the local parent packet and the first child
alone.

Moreover,

\[
 \boxed{g_A-A g_A=(I-A^2)F.}
 \tag{L-97500.4}
\]

Consequently the sufficient M-matrix premise `g_A>=A g_A` is exactly a global
two-step parity-residual inequality.

## Three-state coefficient witness

Consider a chain `0 -> 1 -> 2` with natural weights `r,s` and thinned weights
`a,b`. Let the depth-zero packets be `u_0,u_1,u_2`. The natural recursion gives

\[
 F_2=u_2,
 \qquad F_1=u_1-su_2,
 \qquad F_0=u_0-r u_1+rsu_2.
\]

The thinned current at the root is therefore

\[
 \boxed{
 g_{A,0}=u_0-(r-a)u_1+(r-a)s u_2.
 }
 \tag{L-97500.5}
\]

A local parent-minus-reserved-child expression

\[
 u_0-(r-a)u_1
\]

misses the cross-depth term `(r-a)s u_2`.

For the exact rational fixture

\[
 r=\frac12,
 \quad s=\frac13,
 \quad a=\frac14,
 \quad b=\frac16,
 \quad u_0=u_1=u_2=1,
\]

one has

\[
 F_0=\frac23,
 \qquad g_{A,0}=\frac56,
 \qquad
 u_0-(r-a)u_1=\frac34.
\]

The omitted all-depth residual is exactly `1/12`.
