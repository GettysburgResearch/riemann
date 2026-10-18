# Same-author adversarial audit

The following is a mathematical self-audit, NOT an independent referee or
second-agent report. Proofs and code have one author. No worldwide priority
or best-known-bound review has been completed.

## Rank and arithmetic source

- The supplied argument identifies jet depth with the incidence constant.
  The new rank lemma redoes the resultant count with different J and M.
  The pure-w factor contributes (J-M)e_0; it is retained and bounded by
  (J-M)_+S. Omitting this term when J>M would be an error.
- Specializations of positive-z-degree irreducibles cannot be zero
  polynomials. The Sylvester rank proof tolerates leading-degree drops.
- Both real and imaginary quadratic fields use a positive trace-expanded
  Gram form. For real quadratic fields complex conjugation is identity,
  but trace sums both real embeddings, not just the chosen embedding.
- The lattice Z[sqrt(d)] is sufficient and need not be the maximal order.
  All repeated grid points, jet columns and factorials are retained.
- Ordinary derivatives remain p-divisible even at and above order p.
  Hasse derivatives fail this property. This is tested by an actual mutation.

## All-scale estimates and constants

- R>=q is used in bounding D and the balanced grid, not silently removed.
  A single absolute large-R threshold makes M<=J=S uniformly in d.
- The ceiling grid has 4R<=ab<=9R, while its actual embedding height costs
  (1/2)log R+(1/4)log D+O(1). Both embeddings and trace factor 2 are paid.
- The normalized derivative cost is O(1), since J=floor(R/ceil(log(2R))).
- Small inert primes are NOT assigned the full asymptotic valuation weight.
  They cost O(log log R); the p^-2 error above P approximately log R is O(1).
- The Laplace transfer retains y<log q using the trivial estimate, at cost
  O(t(log q)^2). It does not apply T1 below its stated conductor threshold.
- Ramified prime mass is O(log log q), proved by splitting at log q.
  All k>=2 prime-power tails are absolutely bounded on Re s>=1.
- The last step uses t=(log q)^-2, not t=0. Inverting the inequality is
  justified only after its positive right side is established for large q.
- No numerical value is claimed for the absolute error constants or the
  finite threshold. The real-gap conclusion is asymptotic, not an explicit
  finite-conductor table and not a new complex strip.

## Prescribed-zero route

- A valuation lower template is not the actual determinant valuation.
  Second differences of lower inequalities cannot be used without their slacks.
- Inert primes have pole weight (m_chi-m_zeta)/2. The common-zero case is
  retained, and a mutation rejects replacing it by m_chi/2.
- Raw Hermite determinant log-volume has transform -zeta', which erases
  the target poles. Integrality alone therefore cannot support RH closure.
- The signed desieving retains full divisor fibers and EVERY prime power.
  Its resulting integer is a classical product of lcms; no false new-object
  or new RH-criterion claim is made.
- The exact one-sided continuum is (x-1)^2/2, not x^2/2. Its Gaussian
  convolution, lower boundary and infinite tails are retained.
- Integer endpoints control all real x with a paid error at most 1/8.
  The nonzero residue includes multiplicity and the factor rho(rho+1).
- The open primitive height bound is explicitly RH-strength. Neither the
  real-character result nor the identity for A_N establishes it.
- Separable unitary phases cannot encode a new height into a Gram determinant.
  A complex-zero extension requires genuinely new arithmetic control.

## Priority external review

Review Lemma 1 with J>M first; then the balanced height and full p-adic
ordinary-jet argument; the uniform small-prime/Laplace costs; and the precise
real-zero/Hadamard comparison. Review the zero-sensitive desieving separately
from the still-open signed height estimate. Finite checking comes after, not
instead of, those analytic and algebraic reviews.
