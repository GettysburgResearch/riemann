# Validation and independence boundary

Date: 2026-09-14. The analytic manuscript is proposed and has not received
independent mathematical acceptance. This document distinguishes the original
seven-point theorem, its fresh replay, new bounded checks, and the imported
number-theoretic interface.

## Complete seven-point replay

`vendor/` contains byte-identical copies of the two pinned repository sources.
The ordinary run executes the unchanged search directly; the optimized run
executes it through `verify.py --full-seven`. The raw outputs are
`seven_result.json` and `seven_result.optimized.json`; elapsed time differs,
while every mathematical result/hash agrees. Their recorded process exits
are in EXECUTION.json.

Each complete replay exhausts 713,315 search nodes from 729 initial boxes,
with 356,293 splits, 3,072 linear-pressure leaves, 259,807 interval leaves,
94,143 convex-tangent leaves, and zero unclosed terminal cells. The exact
count and three table/traversal hashes match the earlier source. This
reconstructs the continuum certificate rather than merely verifying a hash
or a sample of gaps.

The inherited implementation's elementary functions and accepting Hessian
LDL tests use 128-bit outward dyadic intervals. Range-minimum tables and
nonnegative accumulations use binary64 with explicit outward `nextafter`.
The ordinary floating Hessian calculation is a rejection screen only.
This is the same numerical backend in both modes. A fresh replay is NOT a
new independently authored implementation or an independent referee report.

## New exact bounded reconstruction

`verify.py` reconstructs, with integer/Fraction arithmetic:

- the majorant polynomial, its strict rational endpoint and derivative margins;
- the Fourier mass and the exact/actual separated-block spectral ceilings;
- all 8,191 short/long gap patterns through 13 points, including odd-cluster
  leftovers and pair budgets;
- pair and gap charges for 74 window sizes and 512 multiplicity-count cases;
- rational enclosures of the old and new constants from alternating
  sine/cosine series, with integer-square-root bounds for the 280-block constant.

The default command also authenticates the two vendor sources and checks the
stored seven-point receipt against the pinned expected result. Its printed
scope is explicitly `BOUNDED_CONTROLS_AND_SEVEN_RECEIPT_ONLY`; it is not a
full replay. Both ordinary and optimized default modes pass.

The bounded semantic digest is
`09ada6338446bfa0fc7393f89f235508693ab2bfc5082f8a7ce0864af5560c4e`.

## Adverse and cross-check tests

Both ordinary and optimized three-method suites pass. Each includes a
separate Bernoulli-series enclosure of the trace baseline, one actual pristine
bounded CLI acceptance, and eight actual bounded CLI refusals. The refusals
cover false RH status, a numeric/Boolean scope alias, an altered proportion,
duplicate JSON, a changed search count, two changed mathematical code paths,
and a changed vendor source. The two code-path mutations are rejected during
rational/combinatorial reconstruction, not by a hash of verify.py.

These are NOT eight complete seven-point executions. No altered prime-side
analytic proof is checked by the tests. The manifest supplies archive integrity;
the default checker specifically authenticates its two vendor sources and
mathematical receipts, not every prose file.

An additional 140-case binary64 Gram scout, with a fixed random seed, found no
counterexample. It is ordinary nondirected exploration, not an accepting
certificate or an ingredient in the proof.

## Development corrections and non-executions

An attempted PTY launch was unavailable and ran no mathematical computation;
the complete runs then used directly supervised subprocesses. An initial
bounded-report build tried to JSON-encode a Fraction tuple and failed; that
redundant serialization line was removed. The successful final reconstruction
uses only explicit rational checks and serializable result fields. Neither
failed attempt is counted as a completed replay or as mathematical evidence.

The actual finite-grid Loewner comparison, trace pinching, all-cardinality
cluster theorem, prime-side trace/mean-square asymptotics and zero-tail transfer
are analytic arguments. They are not machine-proved by the finite tests.
The imported Theorem D paper was read at the relevant proof interface, not
independently rederived in full. No proof assistant, full repository validator,
remote CI, all-PR audit, new zero computation, or world-record adjudication
was executed or claimed.

## Preservation and publication

The delivery uses a new sibling standalone path and an add-only patch.
Minimal Git-fixture and clean-archive checks are recorded in the outer
DELIVERY.json. They preserve a sentinel and earlier supplied packet bytes;
they are not a complete riemann checkout.

GitHub reads confirm #875's moment-cone publication at
`00af30b4b3f810c7cd03fe94ba2f43b6c6b90538`. No write action was exposed, and
direct Git returned `Could not resolve host: github.com`. The author session
did not push this addition. The outer publisher is supplied for the same
existing PR and never force-pushes or changes canonical status.
