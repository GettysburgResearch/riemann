# Execution and review boundary

Status: finite exact source certificate and algebraic replay completed; the
analytic proofs and all-support positivity are not independently reviewed.

## Source binding and arithmetic

`verify_gluing.py` refuses to import the parent unless both literal Git blobs
in SOURCE_LOCK.json match: the mathematical proof and the interval producer.
It recomputes the Euler--Maclaurin/Cauchy source constants P2 and C_b, then
all matrix entries and cross-cell derivative enclosures. It never loads the
parent's saved result as primitive data. The logarithm, exponential and gamma
remainders are those stated in the unchanged parent proof.

All accepted arithmetic is rational, rounded outward internally on 10^-40.
The result file rounds interval exports further outward to 10^-12. Integer
square roots provide directed algebraic endpoints. There is no floating-point
or special-function library in acceptance. Exploratory 45-digit mpmath values
were used to select the six-window fixture only; they are not proof inputs.

## Completed checks

The new producer completed 183 checks in normal Python and the same 183
under `python -O`, with byte-identical output matching result.json:

- 144 independently expanded polynomial cross integrals, including endpoint
  masses, mean-primitive terms, regular curvature and a derivative-jump overlap;
- 5 algebraic square-root enclosure controls;
- 34 source/geometric/matrix checks, including all 15 cross-cell knot lists,
  the six strict LDL pivots, and the full primitive/mass error budget.

The imported source-constant function additionally executes its own two
anchor checks; they are not added to the new 183 count. The complete unchanged
parent suite was separately rerun: 194 checks in each interpreter mode, with
byte-identical outputs. No other predecessor suite was rerun in this pass.

Eight corruptions were rejected in each mode: altered saved pivot, float
alias for an integer, integer alias for a Boolean, duplicate JSON key, altered
new proof, altered parent-commit lock, altered parent producer and altered
parent proof. Each child returned exit code 1 with its exact expected error.
Only those sixteen recorded child refusals are counted. Two initial oversized
orchestration batches reached the 45-second command cap; bounded replacement
batches supplied the complete child receipts. No timed-out batch is counted
as an additional successful suite.

The compact REPLAY.json records output hashes and the completed refusal cases.
The eight-file directory's SHA256SUMS covers exactly its other seven files.
A clean extraction of the downloadable bundle is replayed separately in its
publication receipt; that receipt is not an additional theorem or test count.

## What the certificate means

The interval producer proves the stated finite inequalities provided the
parent analytic special-function remainder formulas are valid. The proof
then uses distributional integration by parts and Hilbert-space inequalities
to cover every L2 function on the six-window support. The executable does
not machine-prove those infinite-dimensional arguments.

No RH proof, all-N center-matrix bound, new zero census, prime distribution
estimate, broad prime or zero scan, Lean build, independent referee acceptance,
or remote CI success is claimed. The whole convex hull between the six short
intervals is not covered by this positivity theorem.
