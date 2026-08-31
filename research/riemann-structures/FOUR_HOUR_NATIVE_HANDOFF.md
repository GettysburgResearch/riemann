# Four-hour native continuation: source ordering, principal readout and decoder boundary

Programme: [issue #763](https://github.com/gfreund123/riemann/issues/763).
Publication: [PR #770](https://github.com/gfreund123/riemann/pull/770),
branch `codex/rs763-five-hour-source`. This continuation began from the
existing native worktree and retained its frozen PR #765 ancestry. It did
not rebase, merge or edit the concurrent agent's branch. The earlier
[fixed-conductor handoff](FIXED_CONDUCTOR_NATIVE_HANDOFF.md) remains a
historical record; the current integration map is
[NATIVE_CONTINUATION_TARGET_ASSESSMENT.md](NATIVE_CONTINUATION_TARGET_ASSESSMENT.md).

These are scoped exact research results and bounded replays, not an
integration verdict or a proof/refutation of RH. The complete native gamma
decoder, principal moment and signed additive/Kummer estimates remain open.

## 1. Read these results first

1. The [source-first adapter](SOURCE_FIRST_BOOLEAN_PRINCIPAL_ADAPTER.md)
   verifies the controlling order: raw squarefree quotient, Boolean
   multiplier and owner allocation, then completion and observation.
   The induced gauge is the identity. Completion has exact principal
   squared norm ratio `ell*rho*c_ell*c_rho/(c*d)<=3` on the clean odd
   chart, and both coefficient and complete Boolean-history maps have
   subpower diagonal bounds. Ambient postcompletion square-shift results
   are not obstructions to that correctly ordered gauge.
2. [PQR](POST_QUOTIENT_PRINCIPAL_READOUT_BARRIER.md) shows sharp
   diagonal-relative amplification on the actual fixed-conductor source,
   while that particular example stays absolutely small.
   [OAC](NATIVE_OFF_ATOMIC_CONDUCTOR_CANCELLATION.md) realizes a cofinal
   power-sized additive/Kummer history correction after literal Wick
   subtraction, whose principal difference is small. The predecessor
   SRECOMB identity already explains this correction; OAC supplies its
   actual source saturation.
3. The [dense-owner family](DENSE_OWNER_PRINCIPAL_COEFFICIENT_FAMILY.md)
   has principal coefficient energy `Theta(Y^(1/2)/log(Y)^11)` and
   shrinking literal diagonal `Theta(Y^(-1/6)/log(Y)^7)`. All actual
   quadratic classes and owner sums are kept. This is a coefficient
   projection, not an orthogonal restriction of the full native source.
4. The [complete Boolean fibre theorem](COMPLETE_BOOLEAN_FIBRE_POSITIVITY_OBSTRUCTION.md)
   removes that restriction-only limitation for the precisely defined
   arithmetic candidate: all allowed core cofactors in the selected
   rough fibres are classified. Three-prime cores cancel, and all
   surviving two-prime coefficients are positive. The complete
   ratio-eight candidate has lower bound `Y^(1/2)/log(Y)^11`; even the
   entirely unmasked clean candidate has lower bound
   `Y^(1/2)/log(Y)^14`. This still does not identify it with the native
   gamma source. Conditional on a subpower native moment, a decoder to
   either candidate needs a power-sized correction in the original
   principal Hilbert norm.

The last point is the sharpest source-facing outcome. A paid diagonal or
an unobserved Boolean product identity does not make the positive
arithmetic candidate a usable small-error native decoder.

## 2. What the earlier branches of the investigation established

The continuation did not assume its initial architecture was correct.
It followed the actual source definitions through several failures:

* NQ distinguishes counting, occupation and probability measures and
  retains the transport lost by re-completion. Its word-history example
  is not asserted to be the native gamma atomization.
* SCB gives an observed subcritical coefficient restriction, with genuine
  balanced histories and the native Fourier kernel. It is not a lower
  bound for the complete signed current.
* EA and GC bind explicit Euler/half-divisor homotopies and the missing
  `G' E` connection. Their raw mixed-exponent projections differ from
  the correctly ordered canonical Boolean source.
* PSG, PPT, PLC and RMI analyze the ambient postcompletion gauge:
  selector amplification, a protected positive transfer, off-sector
  connection cancellation, and a large ratio-masked inverse. They are
  warnings about that alternative operator, not failures of the induced
  source-first quotient gauge. A single unchanged narrow shell has
  different square-insertion behavior from a global horizon.
* MOP sums every marked split-root owner configuration, retaining the
  class square and literal diagonal. Its source is the ordered root
  configuration with an explicit rational owner weight; an unordered
  quotient would add nonsplit rational points and was rejected before
  freeze. MKO proves the corresponding finite Kummer-orbit obstruction
  in its stated generic category. Neither packet transfers the polynomial
  projection to all integer gamma geometry or excludes every possible
  derived/correspondence parent.

The proof notes retain their original hypotheses. Later ordering findings
were recorded in new front-door documents, not by silently editing old
reviewed proofs.

## 3. Scientific freezes and replay entry points

Each row names the producer stem under `research/riemann-structures/`.
The test is `tests/test_<stem>.py`, and the generated artifact is
`<stem>.json`. Source locks are embedded in the producer or in its adjacent
manifest. Exact-SHA independent reviews are preserved separately.

| Packet | Scientific commit | Producer stem | Tests per mode |
| --- | --- | --- | ---: |
| NQ | `c2a999ab9e945954e0211cae530a239ae1a23fd4` | `native_weighted_source_quotient` | 10 |
| SCB | `1623f1924c62035918a94bcacf2ccad7d3bb6cf7` | `subcritical_observed_boolean_block` | 11 |
| MOP | `faf74a47dac33927d081a890f2b5a7ead48b869b` | `complete_marked_owner_pushforward` | 13 |
| MKO | `6551c743d4a86e2664d4b5a62da3c303fa805c7e` | `marked_kummer_orbit_obstruction` | 9 |
| EA | `5ef9a0800e7d0f03bfef1ad4ba467f8843a90058` | `euler_activation_source_adapter` | 10 |
| GC | `e501c45ecc39f71b3f26abfe952366eb529c7c2d` | `gauge_connection_source_transport` | 9 |
| PSG | `ce0cc6e48e3cdaedd9d5f52fb087b03e8f86c257` | `principal_selector_gauge_obstruction` | 9 |
| PPT | `1c9b5cf8aefcb9440dd96feea57c950c15a5b290` | `phase_protected_principal_gauge_transfer` | 10 |
| PLC | `bbcad77cf87f093b2c0513420069f3ee97791789` | `native_phase_leakage_connection_cancellation` | 9 |
| RMI | `5a8b6285acafac7fa2c33f8c6dde2761b799ff8b` | `ratio_masked_principal_gauge_inverse_barrier` | 10 |
| Source-first | `e365528d750fded282bd3f7261898d8455c41e0a` | `source_first_boolean_principal_adapter` | 10 |
| PQR | `57907ac05f7f00f147f6ede570c924ae101afec2` | `post_quotient_principal_readout_barrier` | 11 |
| OAC | `cc861747bd78c6cf90cd73316341fd85ec8cb721` | `native_off_atomic_conductor_cancellation` | 10 |
| Dense owner | `1fea3c9ce079325d19f5b43c6daa59c76afff921` | `dense_owner_principal_coefficient_family` | 10 |
| Complete fibres | `4353858fbfedc3acacb568bf8357c39a16da093f` | `complete_boolean_fibre_positivity_obstruction` | 10 |
| Full-core range correction | `94eb10f59be1f0118d165ac23a31b648600d224e` | `fixed_core_owner_range_correction` | 10 |

All sixteen rows passed Ruff, producer write/replay in ordinary and
optimized Python, and the listed tests in both modes: 161 tests per mode
across their individually validated packets. The earlier FCM/NMO packets
add 22 tests per mode and remain unchanged. A combined final rerun, when
reported, is a separate execution record rather than an inference from
this total.

The complete-fibre scientific freeze is
`4353858fbfedc3acacb568bf8357c39a16da093f`; its bound proof object is
`f4275aa164d7be8e2538a95a096f4c19bf233b3bbb336f0f24b80df45c6c50ac`.
Its ten ordinary and ten optimized tests ran in 1.502 and 1.483 seconds,
respectively. The source and proof files were unchanged after the final
binding replay. Independent exact-SHA review is preserved separately.

Run sequentially from the repository root, using the project Python:

```text
python research/riemann-structures/<stem>.py --check
python -O research/riemann-structures/<stem>.py --check
python -m unittest discover -s tests -p test_<stem>.py
python -O -m unittest discover -s tests -p test_<stem>.py
```

`--write` rebuilds the producer's own artifact; it must not be used to
bypass a failed frozen source authentication. Acceptance checks exact
source blobs, the current proof/producer/test bindings, and strict typed
canonical JSON. Authenticated executable primitives are loaded only from
rehashed frozen Git bytes. No proof of an infinite analytic estimate is
inferred from a finite replay.

## 4. Source acquisition and concurrent work

The old acquisition instructions remain in
[CONTINUATION_SOURCE_REPLAY.md](CONTINUATION_SOURCE_REPLAY.md) and
[FIXED_CONDUCTOR_NATIVE_HANDOFF.md](FIXED_CONDUCTOR_NATIVE_HANDOFF.md).
The additional contemporary source is PR #765's head
`5b25f2dace65dd4d46e16d566f2dc7a34b98f41d`, containing the canonical
Boolean principal-diagonal theorem and exploratory decoder diagnostic.
Its branch name was read directly from the PR during publication:

```text
git fetch --no-tags origin refs/heads/codex/rs763-five-hour-source
git fetch --no-tags origin refs/heads/codex/riemann-structures-marked-descent-gate0
git fetch --no-tags origin refs/heads/research/gpt56-pro/106000-cvxd-lfamily-hybrid-moments
git fetch --no-tags origin refs/heads/research/gpt56-pro/102700-half-divisor-defect-factorization
```

These are acquisition aids, not mutable substitutes for the locked
commit/path/blob identities. Shallow history may need deepening. Fetching
does not require merging another agent's work. Missing frozen source
objects are a replay failure to resolve explicitly, not permission to
change the proof's source SHA.

The concurrent canonical diagonal result overlaps the coefficient-diagonal
question and is cited without a priority claim. Its open decoder interface
is directly relevant to the complete-fibre lower bound. No theorem about
its full native identification was imported: that identification remains
open in the predecessor itself.

## 5. Review and resource discipline

All computational jobs were serialized by the parent agent while another
Codex process was active. The working memory target was at most 1 GiB per
job with a 2.5 GiB free-memory floor. There were no parallel sweeps, large
builds or zero searches. Scouts used hard candidate caps; published prime
fixtures are independently verified by exact trial division or the pinned
Proth certificates. The dense-owner scout examined 103 odd candidates
in total, under its 200-per-window cap, and supplied eleven small primes.

The independent reviewer reconstructed proofs and inspected source/code;
its reports distinguish that audit from the parent agent's actual test
executions. Repaired findings included strict JSON numeric acceptance,
literal versus merged-history diagonals, nonsplit points in an unordered
finite-field quotient, duplicated-67 scope, physical prime/gcd guards, and
the old NMO fixture's different schema. Corrections were made before each
scientific freeze and revalidated. Later summaries do not alter frozen
input identities.

## 6. The next scientifically meaningful task

The next task is the complete native decoder, not another positive
coefficient majorant. Starting from a named source occurrence and physical
observation, reconstruct its actual carrier, endpoint-colour, selector,
renewal and Boolean weights over a whole tuple. Identify the exact
principal-Hilbert-space image, including leftovers and their norm.

The complete arithmetic candidate now provides a falsifiable benchmark:
a decoder cannot simply identify it with the native member up to a
subpower error while also proving the intended native principal moment
subpower. The required correction is quantitatively large on that
comparison. A successful map must retain the missing cancellations or
choose a demonstrably different candidate/readout with paid leftovers.
No actual full native residual or complete source moment estimate has
been proved in this continuation.

The [source-map audit](NATIVE_DECODER_OBSERVATION_GAP.md), first frozen at
`78262e88f`, separates the exact Boolean/Wick maps from their fixed-observation
quotient costs and the unproved principal-norm transfer. The immediate
[fibre-distribution corollary](NATIVE_DECODER_FIBRE_DISTRIBUTION.md) makes the
conditional decoder requirement systematic: if the native principal moment
is subpower in the same space, the correction must have norm at least a
constant times `1/log(U)^4` on all but `U^o(1)` of the
`Theta(U^3/log(U)^3)` selected complete four-class triple blocks. This is
not an actual construction of that native correction.

## 7. A named local source-range import needed correction

The final [full-core owner-range correction](FIXED_CORE_OWNER_RANGE_CORRECTION.md)
identifies a separate concrete error in the archival L-106124 application.
L-102958 proves `P<=2gd,Q<=2gc` for full cores `gc,gd`; L-106124 instead
imports reduced-core ranges `P<<d,Q<<c`. Its interval lemma is correct on
those shorter ranges, but they do not contain the complete physical source
uniformly in `g`. The corrected uniform Hilbert bound has the factor
`(ell+2gc)(rho+2gd)<=9g^2cd`. After the actual source coefficient and weight,
the bound is `Y^o(1)*ell*rho/(cd)`, with no extra uniform `1/g^2` saving.

The existing dense canonical source provides an exact range witness and,
on one actual quadratic class, observed additive energy at least a constant
times `1/log(U)^8` at `g~U`. The conservative direct Gauss comparison retains
its exact factor, bounded below by `9/16`. This disproves the proposed uniform
extension of the old local coefficient estimate to the true physical range;
it does not refute the correctly restricted abstract interval lemma or
identify the complete native gamma vector.

The independent downstream audit found affected local-use prose in
L-106123/R-106123 and retained-results lists in R-106122/R-106124. The direct
principal atomic calculation, finite tensor/Wick identities and conditional
T-106130/T-106140 chains do not quantitatively use that false common-core
saving. None of the earlier frozen continuation proofs uses it. No upstream
source or earlier scientific packet was silently edited.

The correction is frozen at `94eb10f59be1f0118d165ac23a31b648600d224e`, with
proof object `6145fcb1b88180448808bfecc29a82a5bcda06b5b87c13f3c6ed27d57be9235e`.
Ruff, producer write/check/optimized-check, and ten tests in each mode passed;
the ordinary and optimized test runs took 0.959 and 0.953 seconds. It adds
no prime search, large phase enumeration or imported executable. The source
audit and fibre-distribution corollary are documentary deductions and add no
extra producer or test count.
