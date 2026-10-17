# Validation and mathematical review boundaries

## What was run

The final chks/check.py ran successfully in ordinary Python and under
`python -O`; both outputs agree byte-for-byte with RESULTS.json.

The producer and its second coefficient construction include EVERY positive
rational integer through 131072 in 20 family/degree/profile cases:
native at m=6; coupled, two-channel and geometric at m=2,4,6; principal and
fixed mod-4 ordinary twists with two powerful phase profiles. Primes 2,3
are masked. Both 5^6 and 7^6 are included. These are rational integer
coefficients, NOT Eisenstein ideal data or a three-prime semigroup.

The main exact comparisons are:
- 2621440 complete coefficient comparisons between local Euler recursion
  and the unique (r,d) support construction;
- 1600 complete CRT solution-set comparisons on their declared finite n range;
- 1018 nonzero affine determinant identities and 3054 cofactor equalities;
- 54 complete retained affine-correlation identities, assembled independently
  from direct paired coefficients and the gamma/CRT progression formula;
- 240 local density identities and 120 geometric-density tail identities;
- complete exact rational additive-filter Gram identities on a smaller,
  separately declared masked source containing a genuine sixth-power term.

The report also counts millions of repeated coefficient and prefix/tail
budget guards. Those are not independent analytic cases or theorem counts.
The point of those guards is to catch missing support, shared primes and
incorrect power weights. The two coefficient implementations share the SPF,
Mobius and totient tables; they are not independent arithmetic libraries.

All arithmetic in this checker is integer or fractions.Fraction, including
Gaussian-integer numerator pairs for n*F(n). There is no floating numerical
claim, no fit, no zero census, and no numerical evidence for a little-o rate.
The Gaussian analytic consequence is proved in the note, not numerically
certified by these coefficient checks.

## Hostile controls actually executed

Four separate optimized-Python processes intentionally change the source:
1. erase an original prime mask;
2. multiply a powerful coefficient by an extra prime;
3. delete a shared-prime term from the two-channel source;
4. use the wrong CRT determinant scale.

Each exits nonzero at the intended explicit predicate, not because Python
assertions were disabled or because an unrelated dependency was missing.
MUTATIONS.json records the return codes and failures. The proportional-form
case is also retained as a mathematical negative control in the proof and
as a finite positive-square check.

## Development corrections retained transparently

A first diagnostic wrote the expected stored numerator at 5^6 as -5^18.
The two actual coefficient constructions already agreed on -5^8, because
the stored quantity is n*F(n), with F(5^6)=-5^2. The explicit expectation
was corrected, and all final runs use it. No analytic formula was changed.

The first small-cap mutation run used cap 256 while an auxiliary coefficient
fixture requires 512. That run failed with an unrelated index error and is
NOT counted as a successful hostile control. The accepted minimum is now
512; all four mutation processes were rerun successfully at that cap.

The fixed-shift example in the proof explicitly uses h=6 with exclusions
{2,3}. At h=1 with 2 excluded the product vanishes trivially. The separate
unmasked h=1 illustration is not confused with that masked case.

The final proof audit made R explicitly a positive integer, as in the
checker. This is the precise scope of the elementary bound
sum_(d>R) d^-2<=1/R; no real-cutoff interpolation is asserted.

## What was not done

There was no independent agent or human mathematical review, proof-assistant
build, transitive audit of the new ordinary-correlation release, or full-
repository CI. Tao's established logarithmic theorem is an explicit imported
input, not reconstructed by the checker. The stronger ordinary conclusion
remains separately source-dependent. The proof and checker have one author.

The limiting fixed-window theorem has no quantitative uniformity for H=H(X),
for growing Dirichlet conductors, or for the aggregated Eisenstein norm
coefficients. Those omissions are part of the theorem's scope, not inferred
from a finite check.
