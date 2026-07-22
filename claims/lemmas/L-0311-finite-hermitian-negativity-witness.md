# L-0311 — Finite Hermitian negativity has a rational witness

Claim ID: L-0311  
Title: A negative finite Hermitian form admits a rational or dyadic witness  
Status: PROPOSED  
Authoring agent: `gpt56-03`  
Reviewing agents: none  
Created: 2026-07-22  
Last updated: 2026-07-22  
Dependencies: continuity of a polynomial; density of rational points  
Scope: exact witness extraction from a finite negative direction  
Related counterexample candidates: finite Weil or other matrix-positivity witnesses

## Statement

Let `A` be an `m x m` Hermitian matrix over `C`, and define
\[
 q(v)=v^*Av.
\]
The following are equivalent:

1. `A` has a negative eigenvalue.
2. There exists `v in C^m` with `q(v)<0`.
3. There exists `w in (Q+iQ)^m` with `q(w)<0`.
4. There exists a nonzero dyadic vector
   `d in (Z[1/2]+i Z[1/2])^m` with `q(d)<0`.

If `A` is real symmetric, `w` and `d` may be chosen real.

Moreover, suppose interval data certify upper bounds `U_ij` sufficient to
compute a rigorous upper enclosure `Q^+(d)` for `d^*Ad`.  If `Q^+(d)<0`,
the finite tuple `(d, interval data)` is an exact negative certificate.

## Proof

`(1)=>(2)`: Let `v` be an eigenvector for a negative eigenvalue `lambda`.
Then
\[
 q(v)=v^*Av=\lambda\|v\|^2<0.
\]

`(2)=>(1)`: By the spectral theorem, write an orthonormal eigenbasis and
`v=sum_j c_j e_j`.  Then
\[
 q(v)=\sum_j\lambda_j|c_j|^2.
\]
If every eigenvalue were nonnegative, this sum could not be negative.
Therefore some eigenvalue is negative.

`(2)=>(3)`: The map `q:C^m->R` is a polynomial in the real and imaginary
coordinates, hence continuous.  If `q(v)<0`, choose `epsilon>0` such that
`q(x)<0` whenever `||x-v||<epsilon`.  The set `(Q+iQ)^m` is dense in `C^m`,
so such a ball contains a rational complex vector `w`.

`(3)=>(4)`: Write every real and imaginary coordinate of `w` with a common
positive integer denominator `D`.  Dyadic vectors are also dense, so the same
continuity argument directly gives a dyadic `d`; alternatively approximate
`w` by dyadics inside a smaller negative neighborhood.

`(4)=>(2)` is immediate.

For real symmetric `A`, a negative real eigenvector exists by the real spectral
theorem, and the density argument stays in `R^m`.

Finally, interval arithmetic is inclusion monotone: if the matrix-entry
intervals contain the exact entries and the exact rational evaluation proves
`d^*Ad <= Q^+(d)<0`, then the exact quadratic value is negative.  ∎

## Motivation

A floating eigenvector is not a witness.  This lemma proves that genuine finite
negativity can always be converted to finite rational or dyadic data, matching
the exact certificate architecture on agent #1's branch.

## Analytic domain audit

Pure finite-dimensional linear algebra.  No analytic continuation or branch.

## Dependency audit

The spectral theorem supplies the eigenvalue equivalence.  Continuity and
density supply exact witness extraction.

## Gap audit

- A numerically negative eigenvalue can be a rounding artifact; the lemma starts
  from exact negativity.
- Entrywise intervals must enclose the intended exact matrix.
- Complex off-diagonal terms require conjugation and correct interval
  dependency handling.
- Rounding an eigenvector too coarsely can lose the negative margin.

## Adversarial tests

- A matrix with smallest eigenvalue `-2^-100` requires precision escalation.
- Widen intervals until the Rayleigh upper endpoint reaches zero; reject.
- Verify invariant results under exact scaling of `d`.
- Compare full complex and reduced real-even coordinate conventions.

## Remaining uncertainty

No mathematical gap is known.  Application to `D-0001` depends entirely on
the independent correctness of its matrix-entry enclosures.

## Suggested next attack

Add a generic exact dyadic Rayleigh verifier shared by all finite-matrix
criteria, with normalization metadata hashed into the certificate.
