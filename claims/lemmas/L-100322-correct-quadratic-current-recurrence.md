# L-100322 — Exact recurrence and distributional current identity

Claim ID: `L-100322`  
Status: **PROVED EXACT ALGEBRAIC IDENTITY**  
Created: 2026-08-20  
Depends on: definitions only  
RH status: **not assumed**

With

\[
A_N=\sum_{n\le N}\frac{\beta(n)}n,
\qquad
B_N=\sum_{n\le N}\frac{\beta(n)}{\sqrt n},
\qquad
C_N=3B_N-4\sqrt N A_N,
\]

one has

\[
\boxed{
C_{N+1}=C_N-\frac{\beta(N+1)}{\sqrt{N+1}}
-4(\sqrt{N+1}-\sqrt N)A_N.
}
\tag{L-100322.1}
\]

Equivalently, for the right-continuous real current

\[
C(x)=3B_{1/2}(x)-4\sqrt x A(x),
\]

where

\[
A(x)=\sum_{n\le x}\frac{\beta(n)}n,
\qquad
B_{1/2}(x)=\sum_{n\le x}\frac{\beta(n)}{\sqrt n},
\]

the distributional derivative is

\[
\boxed{
dC(x)
=-\sum_{n\ge1}\frac{\beta(n)}{\sqrt n}\delta_n(dx)
-2x^{-1/2}A(x)\,dx.
}
\tag{L-100322.2}
\]

In logarithmic coordinate `x=e^u`, this becomes

\[
\boxed{
dC(u)
=-\sum_{n\ge1}\frac{\beta(n)}{\sqrt n}\delta_{\log n}(du)
-2e^{u/2}A(e^u)\,du.
}
\tag{L-100322.3}
\]

The identity is useful as a coordinate check inside Route A.  It supplies no
positive owner measure: both the atom and the continuous driver retain the
native sign.
