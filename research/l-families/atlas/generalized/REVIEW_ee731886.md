# Independent review of circle-probe geometry

Reviewed commit: `ee7318869424ee7c333a03b87992f33e12072bf9`.

Review object: the five-file circle-probe companion introduced at this
commit. Its authenticated precursor is the multiplicative/mixed-parent core
at `8834fdc7a0dfe15f6bb95eefe0729cb77c93c807`, which has a separate review.

Verdict: no mathematical or implementation blocker found for the complete
irrational-circle classification and connected-family corollary as stated.
External novelty, global L-function compatibility, and natural-boundary
claims are not certified or implied.

## Evidence boundary

I independently read the complete proof, producer, manifest, and fourteen
tests, reconstructed the classification, and inspected the final connected
family addition and merged equivalent code branch at the frozen commit.
I did not run any computation. The implementation agent reports Ruff
format/check, producer `--write`, ordinary and optimized `--check`, and
fourteen tests in each of ordinary and optimized Python passing. Those are
reported executions rather than independent executions by this reviewer.

The finite fixture is generated and checked by full source recomputation.
I inspected that acceptance path; I do not claim to have independently
certified analytic nonrecurrence by examining the finite fixture.

## Mathematical checks

The precursor's continuous-multiplicative coordinates remain the correct
starting point: either the map is identically one, including at zero, or
it is `r^a exp(ik theta)` with Re(a)>0, integral k, and value zero at zero.

For every continuous circle function, eventual recurrence on an irrational
orbit gives a finite translation relation on a dense tail. Continuity and
Fourier uniqueness make the function a Laurent polynomial. This argument
does not require the circle function to be nonvanishing; at an
origin-touching probe its value at w=1 is nevertheless nonzero, ensuring
that the resulting Laurent polynomial is not identically zero.

The three geometries are correctly distinguished:

- At c=0 the radial exponent disappears. Every allowed map gives one
  exponential mode and order one.
- At c=1, the local holomorphic germ is
  `(1+w)^a w^((k-a)/2)`. The residue at -1 forces a positive integer N;
  the Laurent order at zero forces `(k-N)/2` to be an integer, without any
  sign restriction. Thus k can be arbitrarily large in either direction
  with the required parity. The global formula
  `w^((k-N)/2)(1+w)^N` is valid on the circle, including w=-1 by continuity,
  and has exactly N+1 nonzero modes. The exceptional N=0 constant map is
  handled separately; nonzero angular weights at N=0 cannot be made
  continuous at zero.
- For 0<c<1, the annulus c<|w|<1/c requires the integral angular factor
  w^k. The manuscript retains it and uses logarithms of 1+c/w and 1+cw.
  Its logarithmic derivative has residues mu and nu at the distinct
  nonzero points -c and -1/c. Both must therefore be nonnegative integers.
  Together with the precursor's c>1 proof this yields exactly the global
  polynomial maps for every nondegenerate c>0, c!=1. Positive Laurent
  coefficients give minimal order m+n+1.

Rotating a general center and dividing by a positive radius changes the
samples by a nonzero scalar and an orbit phase shift. The dense-orbit proof
and nonzero mode coefficients survive that shift. Consequently the
classification depends only on |C|/R, as claimed. A circle centered at zero
and a circle passing through zero are the two exceptional geometries.

## Deformation boundary checked explicitly

The origin-touching chamber has infinitely many angular weights even at
one fixed finite order. The precursor's argument for local constancy used
a finite remaining weight set and cannot simply be reused here. The
companion correctly avoids a general local-constancy assertion for arbitrary
pointwise-continuous parameter spaces.

The weaker connected-family corollary is valid. Evaluation at 2 fixes N
on a connected space. Evaluation at each root of unity separately fixes k
modulo its order. Differences divisible by every positive integer are zero,
so k is constant. This requires all root-of-unity evaluations in the proof;
any fixed finite collection leaves the stated parity-compatible weight
aliases. The final manuscript preserves this distinction.

## Adversarial source/code inspection

- Frozen note and producer identities are authenticated by commit:path,
  blob identifier, normalized content hash, and current primitive bytes
  before the precursor module is executed. The test that replaces
  authentication by a refusal verifies that the importer is not reached.
- Negative formal powers use exact Gaussian-rational division away from
  zero. The continuous map's value at zero is supplied separately, so the
  code does not try to evaluate an undefined negative power there. The
  constant-one value at zero is retained.
- The touching spectra are checked against independent Laurent
  multiplication. Positive and negative angular weights, multiplicativity,
  and the point w=-1 exercise different boundaries.
- Polynomial probes at c=0, 1/2, 1, and 2 distinguish the loss of support at
  c=0 from full support at positive centers. The exotic map's exact values
  at c=1/2 and c=2 reject transplanting its c=1 formula. This single-value
  check does not itself establish nonrecurrence, and the code says so.
- Rows for nonintegral or nonreal radial exponents are explicitly labeled
  specializations of the proved theorem. The checker does not numerically
  evaluate noninteger powers or manufacture analytic certificates from
  finite samples.
- Parameter, signed-power, coefficient-size, and spectrum caps remain
  small. Invalid parity, illegal degree-zero maps, nonunit evaluation
  points, zero negative powers, Boolean/float substitutions, and changed
  source manifests are refused.
- Full payload recomputation, rather than a self-consistent checksum alone,
  is the acceptance condition. The final Ruff branch merge preserves the
  two identical order cases because Python groups each conjunction before
  their disjunction.

No concrete code defect was found in this companion. The exact Git commit
above, rather than a future regeneration of internal hashes, identifies
the packet reviewed here.

## Remaining scope

The useful repository result is the exact classification of probe
degeneracy: finite recurrence on a circle through zero can hide arbitrary
angular weight, while any positive nondegenerate center removes that
particular false positive. This is a theorem about normalized continuous
multiplicative maps and eventual constant-coefficient recurrences.

It is not a prime-indexed family, conductor construction, gamma completion,
analytic natural-boundary result, motivic realization, or RH/GRH result.
The ingredients are classical Fourier, character, and rational-function
arguments; this review does not establish external publication priority.
