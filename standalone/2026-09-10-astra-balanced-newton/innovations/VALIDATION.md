# Validation contract and limits

This continuation was reconstructed in the current session; old interrupted-run
logs are not passed off as fresh execution. The parent was located remotely in
PR848 and pinned at a1b4625f9775df1fdbd431b5198309a2fce9b038. Its published proof
was inspected, but its original producer/verifier were not rerun here.

The four commands recorded in validation.json use isolated standard-library
Python. Producer and verifier have separate primitive arithmetic and no shared
repository imports. The producer sieves mu and applies c*c followed by convolution
with 1; the verifier trial-factors every primitive integer and applies 1*c before
convolution with c. They independently grow the entire 1,3,15,255,65535 ladder.
Future values are used only for independent comparisons, not to generate output.

Small physical norms use sorted cumulative cells in the producer and the full
ordered max-kernel in the verifier. Kernel validation uses harmonic-number mixed
differences versus literal signed boundary intervals. Raw infinite-source panels
use coefficient accumulation versus direct floor/harmonic sums. Complete analytic
physical and innovation tails are added; they are not inferred from the apparent
agreement of finite partial sums.

The large energy panels share the explicit 128-bit outward protocol: each signed
reciprocal increment is enclosed, squared with a zero-crossing test, and accumulated
outward. The separate variance expression is independently enclosed and must
intersect the direct energy enclosure. This is not floating quadrature. Data shown
with decimals in explanatory prose are rounded outward from these integer bounds.

## Coverage

- 48 arbitrary finite-source whole-norm/isometry panels.
- 48 exact orthogonal perturbations preserving the native prefix and P(1)=0.
- 300 native divisor constraints and 24 first-omitted-coefficient tests.
- Four complete recursive transitions, last through 65535 ordinary integers.
- 440 complete finite kernel panels and 28358 mixed-difference entries.
- Three whole-raw-source enclosures, 256 cells plus separate infinite tail bounds.
- Five unit-energy localized controls and four bounded-fake-prefix controls.
- 64 directed energy cutoffs; 35 finite tests of the proposed 3/2 gain.

None of these finite ranges is an unbounded or cofinal verification of that gain.

## Adversarial acceptance

The verifier parses actual altered files and rejects twelve distinct RESEALED
changes: scope promotion, boolean/integer and integral-float aliases, recursive
endpoint, boundary arithmetic, reduced kernel coverage, omitted-cell index,
deleted infinite tail, deleted fake cost, altered native energy, and removed
finite panel. It separately refuses duplicate JSON keys. It first accepts a
pristine copied file. The same expected primitive reconstruction is reused within
one self-test run; twelve mutations are not twelve independent mathematical reviews.

## Disclosures

A scratch derivation initially included Y=2 in the localized countermodel.
Literal replay rejected that endpoint because a second harmonic term appears.
The final all-parameter statement and both accepting implementations require
Y>=3. The native theorem and canonical dataset were not based on the failed test.
Exploratory decimal output was diagnostic only; final acceptance contains no float.
The explicit float in the verifier exists solely to construct a rejected alias.

No parent suite, full repository checkout validator, external proof/Lean build,
zero computation, or comprehensive originality audit was run. Direct raw GitHub
access from the container failed DNS; connected GitHub actions provide the source
and publication route. A local add-only patch fixture, if recorded separately,
is not a complete repository execution. Both programs and proofs have one author;
independent mathematical/code review remains necessary.
