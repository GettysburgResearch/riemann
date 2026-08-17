# L-95301 — The critical root port is an adjacent-dyadic Mertens flux

Claim ID: `L-95301`  
Status: **PROPOSED COMPLETE EXACT ANALYTIC REDUCTION — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-17  
Depends on: `R-95300/L-95300`

Let

\[
\rho_T
=
\sum_{q\le T}b_2(q)
\left(q^{-1/2}-T^{-1/2}\right),
\]

with the \(q=1\) physical column omitted as above, and put

\[
B_2^\circ(T)=\sum_{2\le q\le T}b_2(q).
\]

Since \(b_2=(\varepsilon-\delta_2)*\mu\),

\[
\boxed{
B_2^\circ(T)=M(T)-M(T/2)-1,
}
\tag{L-95301.1}
\]

where \(M(x)=\sum_{n\le x}\mu(n)\).

The entering hinge at \(q=T+1\) vanishes, so

\[
\boxed{
\rho_{T+1}-\rho_T
=
\left[M(T)-M(T/2)-1\right]
\left(T^{-1/2}-(T+1)^{-1/2}\right).
}
\tag{L-95301.2}
\]

Thus the exact root-port evolution is one adjacent-dyadic Mertens flux.

For the continuous endpoint function

\[
\rho(x)
=
\sum_{2\le q\le x}
b_2(q)
\left(q^{-1/2}-x^{-1/2}\right),
\]

one has initially for \(\Re z>1/2\)

\[
\boxed{
\int_1^\infty\rho(x)x^{-z-1}\,dx
=
\frac{1}{2z(z+1/2)}
\left[
\frac{1-2^{-z-1/2}}{\zeta(z+1/2)}
-1
\right].
}
\tag{L-95301.3}
\]

The \(-1\) is the mandatory deleted-column-one correction.

Every hypothetical zeta zero with real part greater than \(1/2\) creates a
nonreal pole in the positive \(z\)-half-plane; the finite dyadic numerator
cannot cancel it. Hence eventual one-sign control of the root port is already
an RH-producing theorem by Landau.

The root port is therefore not a harmless boundary term. It is the exact
arithmetic mode that PICR attempted to suppress.
