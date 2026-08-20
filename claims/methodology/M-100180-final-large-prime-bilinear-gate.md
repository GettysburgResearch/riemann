# M-100180 — Final large-prime collar as a source-specific bilinear gate

Methodology ID: `M-100180`  
Status: **OPEN CONCLUSION-PRODUCING PROGRAM**  
Created: 2026-08-20  
RH status: **unproved**

After `L-100180` and `L-100182`, every local critical obstruction at scale `X` has been reduced to a depth-one unsquared large-prime collar over a fully squared, strictly subcritical small-prime core.

Write schematically

\[
\mathcal C_X
=\sum_{X^{9/10}<p\le X}{1\over p}\,\mathcal K_X(p;\text{small core}),
\]

where `K_X` is the exact critical Bernstein/activation kernel with all primes `<=X^(9/10)` retained in paired three-state blocks `(1-rS_q)(1+rS_q)=1-r^2S_(q^2)`.

Because two primes in the collar cannot coexist in one active source integer, this is a genuine depth-one bilinear form rather than a many-prime parity cube. The remaining task is to prove subpower logarithmic negative mass for this **signed prime × squared-core form**.

A valid proof must exploit the source-specific kernel and the squared-core positivity. It may use Type-I/II decompositions, prime-reciprocal summation, or a large-sieve estimate only after verifying that the exact kernel and coefficient normalization match the theorem used. A source-blind sieve lower bound is insufficient because of the parity problem.

This is the current shortest honest route from the two-route synthesis to RH.
