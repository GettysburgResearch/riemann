# Validation and publication boundaries

Status: exact finite diagnostics and same-author proof reconstruction. There is
no independent agent or human review, formal proof-assistant build, repository
CI run, or promotion to integrated accepted mathematics.

## What actually ran

Environment: Python 3.13.5, NumPy 2.3.5.

1. The published verify.py passed normally and with python -O; outputs match
   verification.json byte for byte. It performs 3663 explicit predicates,
   including setup and deliberately false-substitution controls.
2. Every one of the 15 cases in results.json was computed by the final census
   engine and recomputed under optimized Python. Decoded results agree exactly;
   the original per-case JSON serializations also matched byte for byte.
3. All file SHA-256 and Git blob identities are recorded in MANIFEST.json.
   These authenticate source bytes; they do not certify the written theorem.

The initial high-memory factor-tuple implementation timed out during a batched
D=8192 computation. No partial value from that attempt is used. The final
fourth-product engine uses injective symbolic integer labels and stores a
representative column pair, then reconstructs the physical ideal support.
It agrees with the original factor-tuple engine on the explicit bounded tests.
All 15 final cases completed and were independently rerun in the second Python
mode. A requested streaming-container launch was unsupported; no asynchronous
worker or background result is claimed.

## Arithmetic and coverage

The row set is all integer pairs (a,b) with 0<a^2-ab+b^2<=H. The bounding box
follows from a^2-ab+b^2 >= 3a^2/4 and its symmetric counterpart. No units,
imprimitive elements or nonunit rows are omitted.

Columns are ALL integral ideals in D/2<Nn<=D outside 2 and 3. Splitting is
literal: each p=1 modulo 3 supplies both roots of omega^2+omega+1 modulo p;
each p=2 modulo 3 supplies the inert degree-two field when p^2<=D. A finite
prime-factor recursion enumerates all ideals, and Mobius selects exponent zero
or one. The Liouville census retains all repeated exponents.

Every ideal count through norm 256 was checked against the independent geometric
half-open generator sector 0<=b<a. Squarefreeness was checked there by Euclidean
divisibility by prime-generator squares, rather than by reusing exponent labels.
Every row count through norm 1024 was checked against the divisor-sum formula
6 sum_(d|n) chi_-3(d). These are bounded cross-checks; completeness of the larger
census also rests on the stated enumeration argument, not on an unperformed
second full enumeration at every large scale.

All 54 nonzero rows through norm 13 were tested against direct Euclidean-ring
modular exponentiation for every good prime ideal through norm 96. Nonzero
sextic values are represented exactly in Z[omega]; zero is a separate seventh
symbol. The main vector engine was checked against direct scalar sums on the
listed small norm balls. Prime powers never convert a zero into a one.

The general principal formula was compared with explicit row-by-row charge
aggregation at orders 2,4,6 for four complete small cases and both sources.
The two fourth-product engines were compared on the same cases. Further
fixtures force both nonsquarefree fourth-order aliases and squarefree order-12
aliases. Counterexamples reject forgetting masks, collapsing conjugate ideals
by norm, or assigning the signed remainder a universal sign.

## Numeric contract

NumPy is used only for bounded integer array arithmetic. The code checks its
int64 and int32 bounds before use. Sixth symbols are exact residue powers,
not rounded complex exponentials. Sums are pairs of integers in Z[omega].
Their squared moduli and powers through order eight are evaluated using
unbounded Python integers. There is no floating-point quadrature, zeta oracle,
interval inference, fitted exponent, or probabilistic sampling in acceptance.
Percentages in README are only displays derived from exact integers.

## Mathematical boundaries

The theorem concerns a fixed Schwartz row profile; a separate theorem prices
the sharp ball error. The finite column window is a hard annulus, not a
C-infinity approximation. There are no source-dependent error constants hidden
behind the finite matching percentages. No full nonprincipal remainder is
proved small. Same-author alternate derivations and normal/optimized execution
are not independent mathematical review.

The new branch is intended to add only this standalone packet on #939's exact
head. Existing source files, main and integrated claims must remain unchanged.
Remote source identities are to be checked before announcing publication; the
local artifact alone is not evidence of a successful GitHub push.
