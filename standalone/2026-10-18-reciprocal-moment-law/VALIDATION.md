# Validation and review boundary

## What was proved on paper, and what was tested

The proposed analytic claims are the full-family mean-square LM-1 estimate,
its complete arithmetic character means, the positive Euler constants, and
the good-family/capped reciprocal asymptotics. These are SAME-AUTHOR written
arguments, not externally refereed or formally verified mathematics.

`verify.py` contains no L-value oracle, zero list, asymptotic fit, or floating
point input. It authenticates finite exponent, divisor, residue, ideal, and
mask algebra. Passing it is not certification of the large sieve, its source
family, the Mellin contour argument, or the inverse-value moment asymptotic.

Coverage is recorded in CHECKS.json, including repeated parameter guards:
- Main dyadic breakpoint and actual-conductor dual inequalities on declared
  exact rational grids. The all-parameter inequalities themselves have written
  proofs, rather than being inferred from the grid.
- Complete compressed valuation counts modulo q^n for six local finite-field
  cases n=3,...,8. Leading residue classes and exact lift multiplicities are
  enumerated; q^n individual rows are NOT looped over or called distinct tests.
- Root-of-unity moments through k=n+1, including the first non-equality balanced
  residue at k=n. Cyclotomic arithmetic uses Fractions and exact polynomial
  division. The local law is a finite algebra fixture, not a global ray family.
- Independent integer Mobius constructions through 1024; all power decompositions
  through 512 for n=3,...,8; exact flat-cutoff polynomial products, with unit and
  endpoint cancellation; actual cubic characters modulo 7 with masks at 2,3,7.
  The finite cutoff taper is rational/piecewise linear, NOT the smooth analytic
  test in the theorem. Only its coefficient identity is being tested.
- All 38 integral Eisenstein ideals outside primes over 2,3 through norm128,
  compared with a separate rational-norm Euler recurrence. Both constructions
  share the elementary prime sieve and splitting rule; not a separately authored
  arithmetic backend. Ten squarefree columns through32 and three complete small
  product-tuple cases test the correct ideal/congruence diagonal. Distinct
  conjugate ideals of norm7 are explicitly NOT collapsed.

Ordinary and optimized Python reproduce the same CHECKS.json. Eight separate
optimized corrupted processes are actually executed by run_mutations.py and
rejected at their expected gates; see MUTATIONS.json. They alter the dual
conductor sign, cap size, modular diagonal, local probability, unit subtraction,
shared-prime condition, nonunit mask, or conjugate-ideal distinction. The cap
mutation tests the claimed error budget; it is not an arithmetic counterexample
to uncapped inverse moments. The fresh-extraction replay authenticates all
payload hashes and repeats both accepting runs and all eight negative controls.

## Attempts and corrections before freezing

Exploratory floating-point optimization of selected numerator/mollifier Holder
bounds did not improve #979's 5/7 density exponent in the tested model. This is
not a general optimality or impossibility theorem. It motivated estimating LM-1
before taking separate absolute bounds. A first attempted longer mollifier
argument would have combined the dual conjugate character and the mollifier
character incorrectly. That simplification is NOT used in the frozen proof.
The complete dual is bounded before multiplication by the pointwise mollifier
bound; the resulting explicit allowed range is a<=sigma-1/2. No failed candidate
is counted as a proved improvement. Exploratory optimizer scripts are not
proof inputs, and their numerical minima are not certificates.

The fixed-twist density scope was expanded explicitly during self-review;
it is not silently attributed verbatim to DF's printed corollary. The original
root/coprimality probability was checked against the n-free local row law,
which differs from a squarefree family and from unrestricted physical elements.

## Highest-priority independent review

1. The exact flat-cutoff functional-equation remainder, all small-conductor
   dyads and finite-S tails, followed by the main LM cancellation.
2. The complete reciprocity/ray-class Dirichlet series, nonprincipal ramification
   test, imprimitive masks and conductor rather than formal-label cost.
3. The fixed-twist zero-density adapter and common good-set logarithm estimate.
4. Absolute convergence of all balanced tuples, their Rankin tail, and the
   Cauchy transfer to inverse values with the cap and losses retained.

No independent agent/human referee, proof assistant, full upstream reconstruction,
actual L-value computation, full-repository validator, or remote CI is claimed.
Publication/readback authenticates the frozen files, not mathematical truth.
