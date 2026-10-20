# Validation and review scope

Date: 20 October 2026. All checks below are author-side local checks.
There was no independent reviewer, separate reviewing agent, proof-assistant
run, repository-wide validation, or GitHub Actions run.

## Executed finite checks

The exact Python checker uses the standard library only and performs no
floating-point acceptance tests. Arithmetic for finite transforms is in
Z[z]/Phi_n(z). It constructs F_7, F_13, F_19, F_31, F_4 and F_25, and
checks every nontrivial multiplicative character over those fields.

The successful receipt contains 87 characters, 1,983 transform identities,
198 additional identities retaining a nontrivial ad=h unit, and 87 exact
Gauss norms. There are 99 zero-frequency checks within the transform
checks, not 99 additional tests. The stream hash is

    bad68b06a44c3a9be3386e8772bc3b72b1afea0df0edf4f2295a3162545807d2

The tests compare the original double finite sum with the derived product
of Gauss transforms, including the Ramanujan case and nonunit zeros. They
also compare the exact squared conductor mass at a unit. Composite
moduli are treated analytically by CRT in the proof, not by a separate
numerical composite-modulus census.

Further exact checks cover local cube inversion through valuation 24,
the rational exponent identities, the full sixth-order local type table,
the all-prime cleared identity for F_Q(1), and the marked example 791/960.
A rational sign change and derivative enclosure isolate the displayed
quartic root between 0.874886647039964 and 0.874886647039965. Subsequent
rational bisection and decimal formatting evaluate its exponents; they
are not evidence for a zero-free theorem.

Executed commands:

    python -I -S -B verify.py
    python -I -S -B -O verify.py

Both output files were byte-identical to REPLAY.json. Python syntax
compilation also passed. The checker uses explicit exceptions, not
assert statements disabled by -O.

## Executed negative controls

Each command below was run both normally and with -O, for six rejected
runs in total:

    python -I -S -B verify.py --mutation forget-cubic
    python -I -S -B verify.py --mutation cheap-quadratic
    python -I -S -B verify.py --mutation erase-zero

All returned exit code 1 at the intended check. The first omits kappa in
the transformed character and fails the local identity at q=7, psi=1,
v=1, h=1. The second replaces the nonmatching squared mass q^2 by q and
fails the conductor-mass check at q=7, psi=1. The third erases a natural
zero and fails the local identity at q=7, psi=1, v=0, h=1.

## What still needs mathematical review

The load-bearing analytic steps are the generalized psi^3 completion,
the complete dual coefficient majorant, uniform strip convexity, the
conductor-uniform reciprocal lemma, and the short-mark/mask transfer.
They are written in PROOF.md; the finite code does not certify them.
The imported Dunn--Radziwill functional equation and Liu zero-free theorem
are dependencies, not newly proved results. The former was read at its
specific interfaces; the latter was not independently reconstructed in
full. We do not import the GRH-dependent prime or dispersion conclusions
from Dunn--Radziwill.

The full mixed norm and physical adapters remain unproved in this
packet. There is no new global zero-free boundary and no integration
approval. MANIFEST.json authenticates the listed bytes only and omits
its own hash. The publication commit and branch are recorded by the PR,
rather than embedding a self-referential commit identifier in these files.
