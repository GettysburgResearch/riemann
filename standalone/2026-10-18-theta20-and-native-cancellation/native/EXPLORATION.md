# Exploration boundary

Status: exploratory attempts and the precise remaining gap.
Scope: native Möbius amplitude beyond #988; no generic impossibility theorem.
Exact sources are in SOURCES.md. Successful finite executions are in
CHECKS.json and REPLAY.json.

The initial attempt was to improve the high-product Fourier bound by keeping
the bilinear shape exp(K/(ab)). Rational frequencies near a large denominator
can cluster on the denominator-squared scale. A multiplicative phase can
also have a stationary product, so separability alone does not visibly pay
the relevant resonance. These observations did not produce a valid sharper
unconditional bound for the actual Möbius signs. They are not published as
a theorem ruling out a method.

Grouping the COMPLETE products by reduced denominator retained a factorable
coefficient that a product cutoff had obscured. The exact mask factorization
then gave a uniform native upper estimate. Its square special case exposed
the second successful bound: small squarefree cores have small complete
global L2 norm, even at large denominators. These are the proved positive
component results in PROOF.md.

No quantitative gap bound between reciprocal crossings was found. The
source-qualified #848 all-prefix exponent limit is therefore essential to
the proposed sparse-cutoff consumer. It cannot be replaced by cofinality
alone or by an unproved interpolation rule.

#991 improves the extraction cost and fixes a shift-average target; it does
not provide the missing critical arithmetic upper estimate. #990 supplies
uniform growing-order bounds at its stated imported exponent, not a native
critical recurrence. Neither result closes the remaining large-denominator,
large-squarefree-core cancellation estimate.

The smallest remaining analytic gap is a fixed subquadratic bound for the
exact rough-core norm in PROOF.md (7.9), along an unbounded set of native
reciprocal crossings. No bound of that strength has been obtained here.
