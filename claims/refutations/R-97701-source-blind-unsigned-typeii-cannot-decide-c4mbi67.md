# R-97701 - Source-blind unsigned Type-II data cannot decide the C4MBI67 sign

Claim ID: `R-97701`  
Status: **PROVED EXACT COUNTERMODEL TO A PROOF MECHANISM**  
Created: 2026-08-18  
Depends on: `L-97703`  
RH status: **the actual C4MBI67 inequality is not refuted**

Consider two source atoms with the same declared dyadic block, owner class and
positive coefficient magnitude, but with distinct kernel responses

\[
K_1>K_2>0.
\]

The signed source vectors

\[
\sigma=(+1,-1),
\qquad
\widetilde\sigma=(-1,+1)
\]

have identical:

1. support;
2. coefficient magnitudes;
3. `ell^1` and `ell^2` norms;
4. unsigned owner mass in every block;
5. every quadratic or large-sieve datum depending only on magnitudes.

Nevertheless their one-sided boundary functionals are

\[
\langle\sigma,K\rangle=K_1-K_2>0,
\]

\[
\langle\widetilde\sigma,K\rangle=-K_1+K_2<0.
\]

Thus no implication using only those unsigned data can determine the sign of a
nonconstant Type-II kernel uniformly over signed sources.

The four-band kernel `kappa_X(pm)/log(pm)` in `L-97703` is nonconstant because
its activation formula changes across the four bands.  Therefore a proof of
`C4MBI67` must use an arithmetic covariance tying the actual Möbius signs to
that kernel.  A rowwise absolute value, an unsigned largest-prime mass bound,
or a source-blind large sieve erases precisely the information needed for the
one-sided conclusion.

This countermodel does **not** show that the genuine Möbius source violates
`C4MBI67`.  It rejects only a proof mechanism that retains no signed covariance.
