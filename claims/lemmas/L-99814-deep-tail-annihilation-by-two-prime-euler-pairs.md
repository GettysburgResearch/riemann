# L-99814 — Two-prime Euler pairing annihilates the critical half-order tail

Claim ID: `L-99814`  
Status: **PROVED EXACT OPERATOR THEOREM**  
Created: 2026-08-20  
Depends on: `L-99813`  
RH status: **not assumed**

For primes `p<q`, let

\[
\mathcal B_{p,q}=(I-p^{-1/2}U_p)(I-q^{-1/2}U_q).
\]

If on a multiplicative interval a function has the critical deep form

\[
F(y)=A-B y^{-1/2},
\]

then whenever all four shifted arguments remain in that interval,

\[
\boxed{
\mathcal B_{p,q}F(y)
=A(1-p^{-1/2})(1-q^{-1/2}).
}
\tag{L-99814.1}

Indeed the entire half-order mode cancels exactly:

\[
y^{-1/2}-p^{-1/2}(y/p)^{-1/2}
-q^{-1/2}(y/q)^{-1/2}
+(pq)^{-1/2}(y/(pq))^{-1/2}=0.
\]

Thus a complete two-prime Euler pair removes the critical `y^{-1/2}` tail rather than merely shrinking it. In the SHARP box potential, the deep region has exactly this form with

\[
A=8(1-67^{-1/2}),\qquad B=3\log67.
\]

Consequently every fully deep pair outputs a positive constant. Any failure of pairwise positivity under subsequent Euler factors can therefore be created only when at least one shifted argument crosses an activation collar.

This theorem isolates the remaining many-prime problem to compositions in which successive pairs encounter the compact collar. It does not by itself prove that the collar state is invariant under arbitrary further pairs.
