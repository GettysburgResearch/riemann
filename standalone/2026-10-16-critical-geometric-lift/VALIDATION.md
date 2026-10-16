# Validation and limitations

Status: exact finite replay and same-author mathematical audit. Neither
finite tests nor content hashes certify an infinite analytic conclusion.

## Executed

- `python verify.py > results.json`
- `python -O verify.py > optimized.json`
- Byte comparison of the two JSON files: identical.
- Python syntax compilation of verify.py.
- Fresh ordinary replay of the original #948 verify.py: byte-identical to
  its archived 791-predicate results.json. Its old proof is not independently
  refereed by this replay.
- Local payload SHA-256 and Git-blob identities, ZIP byte round trip, and
  ordinary replay after ZIP extraction.

The current report records 14,566 explicit predicates INCLUDING setup,
repeated field checks, and rational-descent guards. These are not 14,566
independent arithmetic configurations or asymptotic tests. Exact arithmetic
uses Python integers/Fraction, Q(omega), and Q(omega,sqrt(5)); no floating
approximation or numerical extrapolation enters these reports.

## Complete finite coverage within the declared restricted fixtures

The five named prime ideals have (norm, omega root)
(7,2), (7,4), (13,3), (19,7), and the inert ideal above 5 of norm 25.
The conjugate norm-7 ideals are distinct. All supported exponent vectors
with each exponent 0 or 1 modulo 6 in THIS semigroup are enumerated through
caps 128, 1,000,000, and 100,000,000: respectively 9, 34, and 45 columns.
These are NOT all native ideals below the caps. The window is
cap/8 < Nn <= cap. Its hard boundary is a diagnostic, not the smooth test
in the analytic theorem.

All 54 nonzero Eisenstein rows of norm at most 13 are included in radical
mask and cofactor tests. Mammen restoration uses seven declared rows:
(1,0), (0,1), (1,1), (2,0), (3,1), (1,3), and (4,1), in both prime orders.
All five multipliers are randomized in these algebra diagnostics; this is
NOT the asymptotic log-square freezing schedule of Theorem 3. The phase eta
is a stated legal sixth-root profile, not a computed instance of a global
theta character. The resulting exact G,I,D,M totals are retained in full.
Both signs occur among restoration steps; the order-invariant difference
I-D is checked. No monotone freezing conclusion follows.

Local forward/inverse series are checked through degree 30 at norms
7,13,25,49, six eta phases, and four z profiles. Critical-mass numerical
predicates use rational square roots at 25 and 49; the written proof covers
all q>=7. Direct exponent and radical assemblies, actual finite-field sextic
symbols, inherited coercivity at orders 4,6,8,10,12, and the exact homothety
multiplier are checked separately. They share code and authorship, not
independent mathematical referees or certified number-field libraries.

## Seven false substitutions rejected

The checker directly rejects deleting the first lifted coefficient; applying
Z_p to the exponent rather than the radical; freezing the original row mask
after multiplication by d^6; dilating only Z; also dilating Y; retaining the
old stripping coefficient instead of the geometric one; and replacing a
scale-envelope comparison by a same-scale inequality. These are direct
negative controls, NOT seven adversarial package-mutation CLI tests.
The last countermodel is in the stated five-prime semigroup: no full-native
same-scale counterexample is asserted.

## Analytic and publication boundaries

The local product proof, constant-cost majorants, Rankin bound, actual scale
adapter, and Baire proof were checked by their author. The all-order local
Peano theorem is inherited from #946, with an independently implemented but
same-author finite replay. There was no independent agent/human review,
proof assistant, transitive axiom audit, upstream theorem build, full-repo
validator, or remote CI run.

The execution container could not use network DNS; publication uses the
connected GitHub actions rather than a claimed cloned repository worktree.
This add-only packet does not modify main, prior proofs, or integrated
scientific status. The source commit and actual remote read-back are stated
in the PR publication record. MANIFEST.json binds the eight payload files,
not itself. A matching Git object authenticates bytes, not mathematical truth.
