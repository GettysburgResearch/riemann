# DCN26 validation and publication boundary

## What passed

The final executable packet was copied into two fresh directories with no
reports and replayed in this session using Python 3 standard library only:

```sh
python -S -B replay.py
python -S -O -B replay.py
```

Both complete replays exited 0. Each regenerated all three reports, matched
the committed semantic SHA-256 receipts, ran the separate verifier, and
passed all 14 regression methods. Standalone transport/harmonic check
entrypoints and the test suite were also executed in both modes. No
accepting sign or inequality uses a floating-point approximation.

The final PROOF.md subsequently received two LaTeX-only substack line-break
repairs. No executable, numerical report, or mathematical statement changed.

## Scope of the separate implementation

Seven stages Y=3,7,15,31,63,127,255 are included. The largest full output is
65535. Counts below include overlapping stages, as recorded in
verification_scope.json:

- 6,075,611 physical near-sector pairs are independently checked by quotient
  enumeration, versus the producer's shifted-divisor sieve.
- 1,556,594 original comparable prime triples are independently summed.
- All 87,369 harmonic coefficient indices and the complete Q norms are
  independently checked by product fibres and cumulative reciprocal sums.
- 1,317 selected small harmonic Gram entries, including the complete selected
  sectors through Y=15, are independently re-summed.
- 42 further kernel entries across all seven stages are checked through a
  different union-of-floor-jumps formula, including above-endpoint products.

The harmonic producer computes 535,590 selected off-diagonal entries through
9,308,708 floor events. The LARGE harmonic sector totals are authenticated
producer replays, NOT complete independent second sums. A failure of those
large aggregate implementation details would not be excluded solely by the
sampled kernel checks. Both implementations have the same author and share
exact.py interval primitives and strict JSON helpers. This is implementation
cross-checking, not independent mathematical acceptance.

The zero-cube producer checks 27,519 disjoint cubes containing 146,728 terms.
Pointwise tests also independently verify the divisor and full LCM identities
on complete small domains, with arbitrary positive prime weights. The
E_17 counterexample is an exact point count at one good prime, not an
L-value, rank, height, or zero computation.

## Report authentication and exact arithmetic

Reports are canonical typed JSON. EXPECTED.json stores SHA-256 digests of
canonical JSON without its trailing newline. replay.py writes the reports
under reports/ and verifies all digests before accepting. Complete reports
are included in the chat ZIP but not duplicated as hand-transmitted Git
matrices. Re-running the committed programs reconstructs the same reports.

The fixed common interval denominator is 2^112. Harmonic reciprocals use
integer outward rounding. Natural logarithms use range reduction and a
48-term rational atanh expansion with an explicit geometric remainder.
Decimal values in README.md are descriptive only. Exact rational arithmetic
is used for capped-completion coefficients and product moment identities.

Tests cover both nearest-multiple orientations and ties, the truncated
zero-cube boundary, nonnative divisor defects, the E_17 sign failure,
above-endpoint product deletion, reciprocal/log moments, general divisor
moment inequalities, full LCM fibres and their kernel subtraction, ten
altered report variants, numeric-type aliases, duplicate keys and nonfinite
JSON. Python optimization does not remove the validation guards.

The receipt comparison is part of the acceptance boundary. verify.py alone
checks its documented core fields; it is not a schema-complete replacement
for replay.py and the immutable semantic receipts.

## Interrupted exploratory runs and changes

An early independent verifier accumulated very large exact rational squares
and exceeded the local execution timeout. It was changed to keep exact
rational coefficients while accumulating norms with the same outward
integer-interval discipline used elsewhere. The complete final verifier
then passed. An attempted combined normal-plus-optimized transport command
was interrupted after the normal half passed; the optimized command was
rerun separately and passed. The two final clean replays above passed in
full. No interrupted command is counted as a successful replay.

## What was not done

No full Riemann checkout validator, external formal build, remote CI,
independent mathematical review, broad literature-priority certification,
full native far-covariance estimate, RH/GRH proof, global CM computation,
or whole L-function calculation is claimed. The generic shifted-divisor
bounds do not establish native cancellation among the remaining far pairs.

## Additive publication

The intended parent is 530cc8f706b1f1e3dc7aff77efdced82e4ac73ad on the
existing draft PR #903. Only this new directory is added. Previous proofs,
status files and workflows are preserved. A publication receipt outside this
directory records the actual child commit, tree verification and remote
read-back after the nonforced reference update. This file does not declare
publication successful before that update takes place.
