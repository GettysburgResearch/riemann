# Fixed-conductor native continuation: handoff and source acquisition

Programme: [Riemann Structures, issue #763](https://github.com/gfreund123/riemann/issues/763).
Publication: [PR #770](https://github.com/gfreund123/riemann/pull/770), branch
`codex/rs763-five-hour-source`, stacked on the frozen PR #765 source
`a30276a5be049749ebb2147f30f000dd5659298b`. This continuation did not edit
the other agent's worktree or its PR head.

Status: exploratory exact mathematics and bounded finite replay. Not an
integrated packet or a proof of RH/GRH. All hypotheses in the individual
proofs remain binding on this summary.

## Results and what changed during the work

The initial target was an explicit source object with a signed-diagonal or
uniform-complexity obstruction. Reading the advanced PR #765 head showed
that source algebra, live finite collisions and paid history recombination
were already present. Repeating those statements would add little. The
remaining concrete source gate was whether real live multiplicities grow.

1. [FCM-1/2](LIVE_FIXED_CONDUCTOR_MULTIPLICITY.md) construct arbitrarily
   large owner-disjoint live rectangles in one physical residue cell at
   fixed conductors 5 and 7. The common core varies with the horizon.
   Every one-sided core has exactly two positive Boolean histories, with
   the actual equal-pair share `1/15`. This makes the source-algebra
   faithful-carrier rank obstruction unconditional at its stated scope.
2. [FCM-3/4](FIXED_CONDUCTOR_POWER_RANK_BARRIER.md) strengthen the count
   to sharp order `Y^(1/3)/(log Y)^2` for maximal fully owner-disjoint
   rectangles in the declared window/core class. The only imported
   analytic input is fixed-modulus PNT for 1, 5 and 7. There is no effective
   horizon threshold or count of all source atoms.
3. [NMO-1/2](NATIVE_RESTRICTED_MELLIN_OBSERVABILITY.md) authenticate a
   specified coefficient-level finite-shell projection, its native
   irrational coefficients and its physical dilation generator. Distinct
   owner labels make every arithmetic-pair Mellin frequency distinct.
   The generator has minimal dimension `mn` among exact autonomous linear
   state/readout models, even for this one fixed vector. A faithful
   source-algebra action and arbitrary coefficient freedom are not assumed.
   The two one-sided flows already give an `m+n` dimensional direct sum
   with the bilinear readout `conj(A)B`. Tensoring converts this to the
   minimal `mn` dimensional linear-readout realization. Neither dimension
   is a universal lower bound for all source parents.
4. The same note proves that this projection is inexpensive analytically:
   its source-dual restricted literal Wick, principal and Kummer integrals
   are absolutely `O(Y^(-2/3)/(log Y)^4)`. No cross terms with the
   complementary source are included. Large exact state dimension does
   not imply a difficult analytic contribution; even the zero approximation
   has small uniform absolute error here.

The exact diagonal convention matters. Four equal literal histories with
sum `Z` have energy `|Z|^2/4`. The literal form pulled back to ordinary
aggregate coordinates differs from a newly centered aggregate form by its
paid history correction. These operators must not be identified.

## Frozen sources and acquisition

The qualitative and quantitative FCM packet was frozen at
`9547f4cdc2c8e27a36704029fd74470de844d401`. Its
[independent exact-SHA report](FIXED_CONDUCTOR_MULTIPLICITY_REVIEW_9547F4CD.md)
is preserved verbatim in commit
`6db74e33635257b363a6b169fd2ace6b0c6b79b2`. Its finite proof-object digest is
`3b50959d6464a9284d3d43189f2a6c9c230fb9db520d57a9759d44e2a712991b`.

The restricted Mellin packet was frozen separately at
`6dbab098bb057d76748d12e37900efeff571f8a9`. Its
[independent exact-SHA report](NATIVE_RESTRICTED_MELLIN_REVIEW_6DBAB098.md)
found no remaining blocker within its stated coefficient-projection and
linear-realization scope. Its finite proof-object digest is
`f4dd93b81eba3adfa36e96276540030504482ea741eb6d162b15cef17b1055c7`.
Both review reports distinguish independent proof/code inspection from the
parent agent's serialized executions.

The two manifests authenticate commit/path/blob identities, not mutable
branch tips. In a shallow or single-branch clone, acquire the missing
historical objects without merging the branches:

```text
git fetch --no-tags origin refs/heads/codex/rs763-five-hour-source
git fetch --no-tags origin refs/heads/research/gpt56-pro/106000-cvxd-lfamily-hybrid-moments
git fetch --no-tags origin refs/heads/codex/l-function-sheaf-amplifier
git fetch --no-tags origin refs/heads/research/gpt56-pro/102700-half-divisor-defect-factorization
```

These provide, respectively, the reviewed FCM source, `86cac1d6...`,
`99163530...`, and `ec6635b4...`. Publication-time ancestry checks verified
those acquisition paths; ref names remain acquisition aids only. A shallow
history may need deepening to reach a locked ancestor. Never replace the
locked SHA or blob with a newly fetched tip merely to make replay pass.
The older [continuation acquisition note](CONTINUATION_SOURCE_REPLAY.md)
records the broader PR #765 provenance closure.

## Exact replay and resource contract

Run from the repository root, using its Python environment:

```text
python research/riemann-structures/live_fixed_conductor_multiplicity.py --check
python -O research/riemann-structures/live_fixed_conductor_multiplicity.py --check
python -m unittest discover -s tests -p test_live_fixed_conductor_multiplicity.py
python -O -m unittest discover -s tests -p test_live_fixed_conductor_multiplicity.py
python research/riemann-structures/native_restricted_mellin_observability.py --check
python -O research/riemann-structures/native_restricted_mellin_observability.py --check
python -m unittest discover -s tests -p test_native_restricted_mellin_observability.py
python -O -m unittest discover -s tests -p test_native_restricted_mellin_observability.py
```

The producer's `--write` rebuilds its own canonical JSON; it is not a way
to bypass a failing source authentication. Acceptance recomputes the
complete finite fixture and hashes current proof/producer/test/manifest
files. The first replay authenticates twelve source blobs. The second
authenticates ten manifest blobs plus the predecessor's twelve sources,
with overlap, and checks the exact predecessor executable bytes before
import. There are ten FCM tests and twelve NMO tests.

Final execution passed Ruff format/check, producer write and ordinary plus
optimized replay for both packets, and all 22 tests in ordinary Python and
all 22 under `-O`. Two review findings were repaired before their respective
scientific freezes: the literal/aggregated diagonal wording in FCM, and an
incorrect rational-square test assumption in NMO. The latter changed only
the test, not the native coefficients or theorem.

Only two fixed finite panels are replayed: `U=256` with a `3x3` grid and
the held-out `U=1024` with a `4x3` grid. These meet the general direct
source inequalities; they are not claimed to lie in every narrower
asymptotic interval used by the existence proof. The only discovery scout
tested 5,578 candidates under a 20,000-candidate cap. No conductor sweep,
large sieve, zero scan, large build or many-worker computation was used.
All computational commands were serialized by the parent agent because
another Codex process was active. The independent reviewer reconstructed
proofs and inspected code, without claiming an independent test execution.

## Remaining gates, ranked by relevance

1. Specify what a proposed source parent must preserve. If it must preserve
   this complete projected Mellin function through an exact autonomous
   linear interface, NMO-2 applies. If it retains only the final scalar
   integral or another quotient, a new binding theorem is needed. Neither
   source faithfulness nor exact finite-state preservation may be assumed
   simply because it would make a rank bound available.
2. For the analytic target, inspect complementary cross terms with all
   carrier, marked-prime, renewal, phase and incidence labels retained.
   The selected grid's internal contribution is already absolutely paid;
   repeating its mode count will not estimate those cross terms.
3. A geometric or transfer-operator comparator should distinguish actual
   local source binding, reflection/duality and spectral radius control.
   The native result does not prohibit a rank-one object upstairs, a
   growing parameter space, derived cancellation, nonlinear readouts or
    approximate compression.

No binding theorem for a full source parent, effective rank upper bound
for that parent,
ONEPLACEWEIL/RELTRACE estimate, complete signed current estimate, RH or
GRH follows from these packets. No external priority claim was checked.
