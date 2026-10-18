# Validation, mathematical scope, and publication boundary

Status: proposed research components, 2026-10-18. This packet contains
analytic proofs, algebraic identities, directed finite existence
certificates, and explicitly numerical construction records. It establishes
neither RH nor a new global zero-free boundary for ordinary zeta.

## Frozen dependencies and complete coverage

The sole publication parent is PR #1001 at
`f6beb3774ae7ff5eca4cb046786eae10e4f88abc`. The complete theta arithmetic
backend is inherited from PR #994 at
`c93ca65a510b6acaf167f929b9bf7e67d742b05a`, in
`standalone/2026-10-18-theta20-and-native-cancellation/theta/pr886_primitive.py`.
Its Git blob is `c32015f110d10186538ffabcb4689ba5bbc060d0` and its SHA-256 is
`2eba75b7fc82617342c20f6a06270462b6d82f1e7162f66847c029e7e5a9fa55`.
The new source producer authenticates that blob before loading it. The
default path uses the earlier packet in the same repository checkout.

The fresh source through moment 26 uses 512 fractional bits, Taylor degree
220, all 162 declared cells, all eleven declared explicit theta indices,
and complete Taylor, time, and theta-index remainders. The source proof
derives the physical xi normalization and the variance-one conversion.
There is no unbounded tail replaced by a numerical cutoff. The exact
source JSON has SHA-256
`c171903e4f60c189a929ccfcce36f7db034508e9ca10c85ed766338625558dcf`.

Each directed existence check uses the entire closed active-coordinate
cube of radius `10^-50`, every factor in every required power sum, and
every active Jacobian entry on that cube. The target intervals come from
the authenticated complete source. Inactive factors are fixed exact
rationals. The two incremental checks additionally enforce that all
twenty newest nodes are fixed and identical. The strict contraction and
self-mapping guards remain active under optimized Python. The derivative
bound also proves invertibility of the specified preconditioner, so the
fixed-point conclusion is an exact solution of the moment equations.

The source calculation and interval checks do not load the numerical zero
table used to seed exploratory searches. Ordinary Decimal or floating-point
searches produce candidates; their residuals are not acceptance criteria.

## What the finite replays cover

The manifest declares six acceptance lanes. Each runs in ordinary and
optimized Python with site packages disabled. Every generated receipt must
match the corresponding frozen file byte-for-byte.

| Lane | Accepting script | Meaning of its successful replay |
|---|---|---|
| Arithmetic identities | `arithmetic/check_arithmetic.py` | Exact local-state expectations, local optimizer and coefficient identities, full finite masks, and displayed rational exponent arithmetic. It does not prove the analytic large-sieve estimates by execution. |
| Negative interactions | `analytic/check_negative_coupling.py` | Complete finite incidence contractions and spin configurations for its fixtures, edge budgets, and the exact rational variance barrier. General graph and analytic conclusions rest on the proof. |
| Direct theta models | `theta/check_gaussian.py` | Complete source authentication, fresh full source reconstruction in the ordinary lane, and the three directed existence cubes for orders 22, 24, and 26. |
| Incremental endpoints | `theta/check_incremental.py` | Directed existence of the 84-factor order-24 and 104-factor order-26 endpoints, including all fixed new factors. It does not certify the connecting trajectories. |
| Power-sum extension | `theta/extension/check_power_extension.py` | Exact polynomial identities on 24 rational charts, eleven confluent determinant fixtures, collision powers through degree 26, the strip conversion, positivity counterexample, and rational theta barrier. General continuation rests on the analytic proof. |
| Graph extension | `theta/extension/check_extension.py` | Complete finite graph identities, including the declared 128 spin configurations and moments through degree 26, and the variance barrier. This is not a new theta root certificate. |

The direct finite receipt is bound at
`6277f3aadcac04b130ec066c9432a9f77b31db209b253f61c5327e7be8fd6c3a`;
the incremental receipt is bound at
`8e90e9b681e5e12015eb9d5edaec4957c1e1fd0d36dcd3eae5b6543622ec5599`.
All remaining receipt identities, proofs, candidate inputs, and checker
sources are enumerated in `MANIFEST.json`.

The packet verifier additionally runs four deliberately corrupted inputs
in separate optimized subprocesses. An altered source interval must fail
at source authentication; a negative node must fail the positivity gate;
a zero preconditioner must fail the full-cube contraction gate; and an
insufficient radius must fail strict self-mapping. A generic crash is not
accepted as a successful negative control, and a rejected input must not
write an accepting receipt.

Run from a checkout containing the frozen dependencies:

```bash
python -S -B standalone/2026-10-18-theta26-and-critical-family/verify_packet.py --replay --report /tmp/theta26-replay.json
```

The verifier authenticates the exact payload inventory, sizes, SHA-256
hashes, and Git blob identities. It writes generated receipts only to
temporary paths. The command completes twelve positive finite replays and
four designated rejection controls. This is an integrity and reproduction
gate; it is not a proof assistant for the accompanying mathematics.

The exploratory producers and selected search records are also preserved.
The three direct searches were replayed against the selected centers,
targets, and Newton histories; both rational parameter producers reproduced
their frozen parameter files byte-for-byte. Some exploratory optimizers
require NumPy or SciPy. The accepting lanes require only Python's standard
library and the authenticated inherited backend. Large intermediate logs
are not part of the acceptance evidence; the curated experiment records
retain the selected complete endpoint states and identify their provenance.

## Independent mathematical review

The following reviews were performed by agents other than the respective
component authors and bind the exact reviewed file hashes:

| Review | Scope |
|---|---|
| [ARITHMETIC_AUDIT.md](audit/ARITHMETIC_AUDIT.md) | Actual-family tail, all square parts and row masks, growing residual transfers, the local optimum, and the native high-frequency consumer. |
| [LOW_FREQUENCY_AUDIT.md](audit/LOW_FREQUENCY_AUDIT.md) | The general-coefficient obstruction, exact smooth balances, full zeta multiplier, physical restriction, and the limitation to a class larger than Möbius coefficients. |
| [THETA_GAUSSIAN_AUDIT.md](audit/THETA_GAUSSIAN_AUDIT.md) | Complete theta normalization and remainder proof, full source replay, direct finite cubes, Gaussian and canonical bounds, and their conditional scope. |
| [WEIGHTED_CANONICAL_AUDIT.md](audit/WEIGHTED_CANONICAL_AUDIT.md) | Half-plane branches, quartic bound, global remainder, limit identification, and the positive weighted all-order consumer. |
| [INCREMENTAL_AND_POWER_EXTENSION_REVIEW.md](audit/INCREMENTAL_AND_POWER_EXTENSION_REVIEW.md) | Both new endpoint cubes, moving anchors, quantified continuation, collision coordinates, strip barrier, and the classical Stieltjes consumer. |
| [NEGATIVE_COUPLING_INDEPENDENT_REVIEW.md](audit/NEGATIVE_COUPLING_INDEPENDENT_REVIEW.md) | Local disks, full graph contraction, reference comparison, and the continuous physical variance barrier. |

These are independent agent reviews within one research session. They are
not external human referee reports or formal verification. Repeating the
directed calculation with the same authenticated interval backend does
not constitute a second transcendental arithmetic implementation. The
general graph extension identities were additionally read and replayed by
the coordinating agent; their scope is that of the displayed component
theorems and finite fixtures.

## Conditions not supplied by this packet

No finite replay establishes feasibility at unbounded moment orders.
The weighted canonical and classical Stieltjes arguments are sufficient
consumers with an explicitly open all-order positivity premise. The
64/order-22 to 84/order-24 to 104/order-26 construction is an empirical
two-step path with separately certified endpoints; it is not a certified
continuous path between the exact roots or an induction theorem.

The actual-family estimates hold on fixed compact subsets of
`1/2<Re(s)<1`; neither endpoints nor a height growing with the conductor
are silently included. Auxiliary Euler variance can be removed, but the
ordinary zeta scalar remains. At a zeta zero the full residual remains
one. The complete high-frequency estimate leaves a low-frequency
arithmetic bound open. The coefficient counterexample does not satisfy
the full Möbius convolution identities and is not a refutation of a
Möbius-specific contraction.

The strip theorems pay a physical half-width of `1/3` exactly, with the
correct variance rescaling. A cofinal matching construction within that
strip would give the zeta boundary `5/6`. Such a construction is not
provided. Nor is a negative-coupling theta-matching finite model certified.

Publication adds only this standalone packet on a new research branch
stacked on the frozen parent. It does not modify inherited packets or
integrated claim status. The immutable publication commit, complete remote
tree readback, and independent proof-hash readback are recorded in the PR.
