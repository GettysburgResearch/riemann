# Independent-review guide

Status: proposed proofs and computer-assisted finite realization, not RH.

The primary new mathematical claim to check is Section 4 of PROPOSAL.md:
there exists a finite ferromagnetic weighted-spin law matching the first six
moments of the fixed standardized theta law. No all-order extension is asserted.

## Load-bearing checks

- Theta normalization, full-line versus half-line factor two, variance scaling,
  and the identity M_theta(h)=xi(1/2+h/sigma)/xi(1/2).
- Lee--Yang's hypotheses: zero-field pair ferromagnet, all J>=0, all observable
  weights nonnegative. The isolated-spin bath is part of the SAME finite model.
- The compact-convergence argument is conditional on all-order moment matching.
  Gaussian coefficient domination follows from the Lee--Yang product, not
  merely symmetry or a variance bound for arbitrary probability laws.
- The K8 weight q^(s^2/4), q=exp(2J), including the canceled constant factor.
  Reconstruct cumulants of the EXACT finite L=4096 sign bath. Do not replace it
  by a Gaussian when verifying equations (9)--(12).
- The positive quadratic root t and the radical sign, gamma>0 throughout the
  whole rational q bracket, and strict endpoint signs for the actual interval
  of theta cumulants. IVT proves existence, not uniqueness or high-order match.
- Every theta index beyond four and the complete t>=2 tail must be paid by
  (16),(17). Check the integrated fourth-derivative Simpson remainder (15),
  the sign of the next Machin-arctangent term, exponential range reduction,
  and integer-square-root rounding.
- In the Villain identity, retain normalized Haar measure and every integer
  current. Lee--Yang concerns magnetic field, not the inverse-temperature
  parameter. No zero-location theorem for theta follows directly from (19).

## Scope boundaries

The finite model parameters are defined by the actual theta moments and an
intermediate-value root. Their existence is certified; an exact closed-form
root, minimum graph size, uniqueness, connectedness, eighth-moment match,
all-order realization, new zero-free region and RH are NOT claimed.

The closure theorem is classical. The requested new direction is constructive
source realization, not a novel general theorem about Lee--Yang measures.
A failure for one graph family would not disprove RH, since no ferromagnetic
realization converse is established. Numeric fits at higher orders are excluded
from the accepting certificate.

The first serious theorem still to obtain is a source-preserving extension
rule reaching unbounded moment order, or a direct weak-limit identity for a
prescribed family of positive-coupling models. This is not assigned to the
reviewer as a routine omitted step.
