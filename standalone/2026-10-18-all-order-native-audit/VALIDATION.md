# What the computations do and do not establish

## New exact replay

`verify.py` uses only Python's standard library, exact integers and Fraction.
Every acceptance guard uses an explicit exception, so optimized Python does
not disable checks. Ordinary and optimized reports are byte-identical.

The final report has **69,602 predicates including repeated guards**.
Of these, **56,160** are repeated sixth-power-mask identities on the same finite
fixtures, and **5,760** are endpoint identities. They are not independent
analytic cases. The useful coverage is:

- All 73 good squarefree Eisenstein ideals of norm at most 256. Distinct split
  prime ideals are separately enumerated. The aggregate native norm coefficients
  agree with an independently assembled mu*(mu chi_-3) convolution, with the
  exterior exclusions, at every integer norm 1 through 256.
- All 54 nonzero Eisenstein elements of norm at most 13, and ALL five allowed
  squarefree ideal columns of norm at most 13: the unit and the two prime ideals
  over each of 7 and 13. This is a complete SMALL hard-cutoff source, not the
  infinite Gaussian, not a large theta computation, and not a random-prime model.
- Orders 2,4,...,16 of that full row/column fixture. Direct powering in Q(omega)
  equals complete ideal-product convolution, independently evaluated using
  multinomial coefficients. All product ideals are retained: exponent 6,7,8
  cases authenticate the literal zero and shared-factor conventions.
- General-order and functional-equation exponent identities for n=3,4,6,12,
  r=1,...,12 and the specified fixed real lines; all endpoint calculations
  for five unbalanced AFE choices per case; native row-exponent losses; the
  stated symmetric estimate-model diagnostic; and the order-before-scale
  arithmetic in the sublinear-excess criterion. Written algebra, not these
  finite samples, establishes the universal parameter claims.

`run_mutations.py` creates NINE actual corrupted copies in temporary directories
and runs each in a separate `python -O` process. Each fails at its specified
gate. Mutations erase a sixth-power mask, add false coprimality, collapse a
conjugate prime, delete the sieve length term, lose the dual conductor weight,
delete the full-row length term, pretend that the native excess is bounded,
change the Mellin shift, or discard the native product sign. MUTATIONS.json
records the actual successful rejection outcomes.

No L-function value, zero, native asymptotic moment or infinite automorphic
projection was computed. The full moment theorem rests on the stated DF sieve
and the written derivation. The conditional critical-line sufficiency theorem
rests on its displayed hypothesis, which remains unproved.

## Pending packet replay and publication

The accompanying older thirteen-file eighth-moment-composition packet was
extracted from the conversation ZIP without changing any source bytes. Its
original manifest passed, and both full checker modes reproduce its original
9,959-predicate CHECKS.json byte-for-byte. That is preservation and replay,
not an independent audit of its proposed 163/180 consequence. Its historical
mutation records are preserved; they were not newly generated in this execution.

Live GitHub reads confirm #971 at 3f1d2a07631eb6cca1f2716be01f64e874667639.
A PR search for eighth-moment-composition did not find a published counterpart;
that search alone is not asserted to rule out every unindexed object or
unseen concurrent branch. The patch is explicitly add-only against that frozen
base and refuses to overwrite already present paths.

The current 48 exposed GitHub actions are read-only. Plugin discovery found
the installed GitHub connector but no additional publishing action or skill.
A direct Git read failed DNS for github.com; no authenticated CLI publishing
route succeeded. No remote commit, branch or PR was created in this execution.
The outer receipt and patch record local identities only.

## Exploratory attempt, not a theorem

A floating-point linear-program exploration tried higher Holder exponents on
both the numerator and mollifier in the selected zero detector. A first large
batch exceeded its 20-second execution limit; a reduced batch completed. It
found no qualitative all-order improvement, and its numerical optimum is NOT
claimed rigorous or global. Neither script output nor any LP estimate is an
input to the three proof notes or final exact checker. The exact unbalanced-AFE
and growing-order calculations in the proofs are separate from that exploration.

Before final freeze, the restricted quadratic-form target was clarified to
require hard-prefix bounds at EVERY H and X. Its written Gaussian transfer now
keeps H fixed during the integral over rescaled column lengths. This is an
analytic quantifier correction to the draft exposition, not something that
finite exponent checking could have supplied.

## Review obligations

Same-author proof and code; no separate mathematical referee, proof assistant,
full upstream rebuild, remote CI or full-repository validator. First challenge
all-line AFE conductor/gamma separation and the complete n-power column removal;
then the full-row ideal/physical adapter and all Gaussian annuli; then the exact
quantifiers in CRITICAL_ROUTE. A defect in these arguments is not repaired by
passing a numerical identity checker. The missing signed upper bound is stated,
not concealed inside an asymptotic or test count.
