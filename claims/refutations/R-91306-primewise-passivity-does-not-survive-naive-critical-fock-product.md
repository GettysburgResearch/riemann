# R-91306 — Primewise passivity does not survive as a naive critical-boundary Fock product

Claim ID: `R-91306`  
Status: **EXACT METHOD REFUTATION**  
Created: 2026-08-12  
Depends on: `L-91323/L-91324`

Every individual normalized Jordan Euler factor has an explicit lossless Julia
completion. It is tempting to multiply these local positive nodes directly on
the moving critical boundary and conclude that the global completed quotient
has a positive colligation.

This inference is false.

For \(0<a<1/2\), the local detail variance at the critical boundary is

\[
\delta_p^2\sim p^{-1/2+a}.
\]

The total detail number diverges, and at every nonzero boundary frequency the
actual emitted detail energy diverges. Thus the finite-prime inner columns
have no limit in the naive Hilbert direct sum.

The completed Xi quotient is an analytic renormalization of a divergent Euler
object. Its gamma/theta channel is not a finite auxiliary correction to a
convergent prime Fock vector.

A claimed proof is rejected if it:

- exchanges the prime cutoff limit with the critical-line limit;
- treats the critical Euler product as a Hilbert-space coherent vector;
- drops the diverging detail channels;
- invokes local Julia unitarity without constructing a global renormalized
  wave operator;
- uses boundary modulus one to turn a divergent product into an inner
  function.

The exact viable replacement is `T-91305`.
