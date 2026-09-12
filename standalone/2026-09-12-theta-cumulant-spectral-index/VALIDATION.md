# Validation scope and execution contract

This packet contains proposed PAPER theorems and two computer-assisted finite
matrix predicates. Neither Python acceptance nor publication is independent
mathematical approval. OPEN-CSI remains unproved.

## What the accepting calculation actually reconstructs

`certify.py --check certificate.json` authenticates the exact ten-file inventory
and nine manifest entries, parses strict typed JSON, executes the independent
finite algebra controls, and then regenerates the full native calculation:

- raw moments0,2,...,36 of the UNMODIFIED theta density;
-128 disjoint midpoint Taylor cells covering[0,3], degree63, indices1--8;
- complete omitted index and physical tails, with L1 derivative error;
- normalization by the newly enclosed zeroth moment;
-18 logarithmic power sums, checked against an independent binomial cumulant
  recurrence using the same raw source intervals;
- both complete9x9 scaled Hankel forms and all18 interval LDL pivots;
- the whole moment-tail upper bound M(sqrt(20))<9/5, giving the
  source-only absolute divisor-square-sum bound1/8 in the paper.

Every arithmetic value uses Python integers/Fractions and768-bit outward dyadics.
The code does not call a zeta/gamma evaluator, root table, NumPy, SciPy, or mpmath.
The elementary interval backend is adapted from the frozen NMT26 code identified
in SOURCES.json. Normal/optimized agreement is ONE implementation, not a second
primitive backend or independent authorship.

`--emit PATH` is producer mode and does not authenticate an existing packet.
It must not be reported as acceptance. Preliminary8x8 source runs and the final9x9 producer used emit;
the final sealed normal and optimized --check commands are separate replays.
A combined final orchestration timed out after its producer; that orchestration
is excluded from completed final acceptance. Subsequent separate accepting
commands are recorded in the delivery receipt.

## Finite controls in test_check.py

Four test methods exercise:

1. Six synthetic spectral configurations with one/two/three selected conjugate
   pairs, each with an ENTIRE geometric tail. Three of these tails also contain
   infinitely many complex pairs. Exact negative witness Grams and finite Hankel
   inertia are reconstructed. Three additional tests vary multiplicity without
   changing the number of distinct negative directions. None is a zeta zero.
2. Six positive atomic quadrature examples, dimensions1--6, checking all
   moments through2n-1 against exact matrix powers and complete rational Grams.
3. Three independent formal exponential compositions, each through order64,
   compared with the theta derivative recurrence. Three finite spectral products
   separately check the Newton signs and analytic multiplicity accounting.
4. Complete cell coverage,64 exact monomial integration coefficients, five
   exponential interval comparisons, and the nine elementary source-tail/divisor bounds.

These are finite controls of the supplied algebra, not a machine proof of the
infinite index theorem, classical factorization, or all-order positivity.
No source quadrature cutoff is inferred from these controls.

## Failed/limited reconnaissance

Before the cumulant pivot, ordinary floating calculations tried one positive
edge on #854's six-group seed, additional #842 block couplings, and added leaf
weights. They supplied no verified higher-moment solution and no global
infeasibility result. A failed solver, a local derivative sign and an out-of-range
linear prediction were NOT used as theorem inputs. Their scripts and unquantified
moment values are not part of acceptance.

An initial high-order source run timed out. The final calculation avoids enormous
rational exponents by using the declared monotone high-Q derivative bound at2048;
this changes only the proved enclosing evaluation, not the source or integration
formula. Its first complete output was then reproduced by the sealed checkers.

## Delivery and limits

The accompanying delivery receipt records actual command exit codes, transcript
hashes and roundtrip results. A clean ZIP extraction and an add-only patch in a
minimal Git fixture are byte comparisons plus the declared test replays, not a
complete riemann checkout, remote CI, Linux/Windows portability proof or Lean
build. SHA256 authenticates bytes, not mathematical truth.

No new remote commit is asserted by these payload files. A publisher must bind
an actual new branch head separately and preserve all parent material. If the
branch has advanced since the frozen base, do not force-push or overwrite it.
