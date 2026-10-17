# Validation and review boundaries

Status: same-author proof development with reproducible finite diagnostics.
No independent human/agent referee, proof-assistant build, remote CI, imported
theta replay, or full-repository validator was performed. An unconditional
written argument is not the same as independently accepted mathematics.

## Exact diagnostics actually run

`python verify.py` and `python -O verify.py` produced byte-identical CHECKS.json.
The final report contains **34,361 explicit predicates**,
including repeated prefix/setup checks; these are not that many asymptotic
cases. No correctness condition uses an assert that vanishes under -O.

Coverage:
- All 153 permutations through degree five: residue-degree tensor formulas
  versus direct permutation action on ordered pairs, including dimension
  and degree-one multiplicity. Seven named group actions compare orbit
  counting and Burnside. These are finite group tests, not new field builds.
- 1,152 local source/phase/degree configurations through local degree 40,
  literal zero masks and uniform critical tail budgets. Odd m cases use
  square prime norms to keep all tested weights rational.
- Complete good-ideal censuses through norm 512 in Q and Q(omega), excluding
  primes above 2 and 3. Every good ideal is retained, including source-zero
  columns, for four coefficient families at m=2,4,6 (24 cases). Norm
  multiplicities are separately checked by rational/divisor-character
  formulas. Ideal-vector and rational-norm Euler assemblies agree exactly.
- 72 complete hard-window cases at caps 16,32,64, fields Q/Q(omega), all
  four sources at m=2, and orders 2,4,6. Direct ordered ideal tuples are
  compared with grouped norm convolutions, absolute majorants and the
  bounded-gap inequalities. Higher geometric powers beyond these caps are
  not claimed present; their local formulas are tested separately.
- Exact rational Gaussian square completions, higher-order Jacobians,
  pointwise normalizations, tuple balance and sparse graph inequalities.
- A literal split norm-7 sextic row witness, and the negative norm-49
  same-norm cross-ideal term. This is not a large physical-row census.

The source formulas and splitting data are shared between the two ideal
assemblies; they are not independent arithmetic backends. No finite norm
cap, predicate count, or small error is extrapolated to an analytic exponent.

## Five actual optimized-Python mutation processes

`python run_mutations.py` launches separate `python -O verify.py` processes.
Every declared mutation exits nonzero at a substantive failed predicate:
remove a conjugate ideal, alter the tensor coefficient, erase a nonunit mask,
use the wrong higher-order Jacobian, and equate the ideal and norm diagonals.
MUTATIONS.json records the observed failures. These are actual executions,
not just five descriptions of potential errors. Six additional exact
false-substitution controls remain inside the unmutated checker.

## Numerical kernel diagnostics, separately labeled

`python numerical_kernel.py` and its optimized counterpart reproduced
NUMERICAL.json byte-for-byte. Ordinary mpmath at 65 decimal digits was used;
this is NOT directed/certified interval arithmetic. Three finite native
Eisenstein Gaussian polynomials, with ALL good columns through norm 13,
were checked at orders 2,4,6. They use the explicitly stated three physical
rows, one with a genuine nonunit zero. Direct quadrature in log scale agrees
with the norm-grouped pair kernel within the stated 1e-48 tolerance; pointwise
grouping is tested separately. Shared coefficients are not an independent
primitive arithmetic implementation. The full infinite source, asymptotic
constant, and theta average were not evaluated numerically.

## Recovered predecessor

All nine ramified-dilation files are byte-preserved against the original user
ZIP. Its own eight-payload manifest passes. Its 3,679-predicate checker was
freshly run in ordinary and optimized Python and both match the original
results.json. Its old NOT PUSHED labels are preserved, not overwritten.
The new norm-fiber theorem does not depend analytically on that packet.

## Proof audit and changes during this pass

The written argument was checked for: the difference between ideal and norm
collisions; non-Galois kappa rather than degree; uniform m local majorants;
fixed k constants; absolute infinite Fubini; Gaussian Jacobian and CDF shift;
fixed-scale and compact-window sector scope; fixed-profile versus moving-
profile asymptotics; and signed versus absolute tuple selection.

The fixed-scale Gaussian and direct compact-test corollaries were added
before the final freeze. Dedicated exact pointwise and complete compact-
window checks were then added and BOTH final exact runs and mutation runs
were repeated. The earlier smaller predicate total is not the final report.
No corrected numerical result is being presented as a proof of the theorem.

## Review priorities

First inspect THEOREM.md Lemma NF4 (rational norm multiplicities and local
critical tail), then NF1c (original fixed-scale compact test) and NF3 (Euler
limit and positive Tauberian step). Check EXAMPLES.md's excluded-prime
factors and sign convention. Finally replay the checker and manifests.

The smallest load-bearing unresolved *review* issue is correctness of the
uniform local coefficient comparison and its finite-etale pole order. The
smallest unresolved *full-moment* issue is different: the dense signed
unequal-product-norm remainder is not bounded. Neither finite checks nor
these sector theorems remove that arithmetic obligation.

## Publication and transport

This pass has not created a remote branch, commit or PR. Current GitHub
connector discovery exposes read/search actions only. Plugin discovery
returned the installed hybrid GitHub connector, not an available alternative
writer. No authenticated GitHub CLI was available in the container; a Git
remote access attempt failed DNS. No clean full-repository worktree is
claimed. The outer patch is add-only and tested against a fresh local
fixture, not the entire frozen #950 checkout. See RECOVERY_AND_PUBLICATION.md.

The manifest binds final payload bytes, not mathematical truth. The final
ZIP and patch checks are recorded in the outer TRANSPORT.json; they do not
claim remote read-back or mathematical independence.
