# Signed-history recombination: exact-SHA adversarial audit

Reviewed source: `e1a10bc821c22cb341424b18ce6838634262af31`.

Verdict: **the identities and inherited principal payment survive; one
residual-target scope clarification is required and applied with a new
identity.** No new signed estimate, native coefficient freedom, geometric
realization, RH result or novelty claim is certified.

The review read the literal locked T-106140, corrected L-106121, L-106120,
L-106131, L-106191, L-102883 and T-102990, then checked the Boolean source,
owner kernel, frozen-horizon and live-collision dependencies. Implementation
and source authentication also received an independent read-only audit.

## Finding and repair

**P2: distinct retained groups are not necessarily distinct arithmetic
tuples.** At the reviewed SHA, note lines 64--66 retain `(P,Q,c,d')` and all
non-history labels in `a`. Consequently `a!=b` in (2.3) need not imply that
the arithmetic tuples differ. The next-target wording at lines 21--22 and
419--424 could exclude still-unpaid equal-tuple interactions distinguished
by retained source labels.

Smallest counterexample to that exclusion: two singleton groups at one
arithmetic tuple but different retained labels, with symbolic coefficients
`z_1,z_2`. Every within-group correction is zero, whereas their principal
cross term is `2p Re(z_1 conjugate(z_2))`. Specializing to `z_1=z_2=1` gives
`Delta=0` and `2p>0`. This is an algebraic obstruction to dropping those
terms, not a construction of an admissible native coefficient pair.

The repair names the residual as **all distinct retained groups**, preserves
these equal-tuple/different-label terms, adds the exact singleton regression,
and rebinds the changed note and tests in the fixture. No uniqueness assumption
or additional payment theorem is introduced. The source algebra itself was
already correct.

## Mathematical checks that survived

1. With `ztilde=g*ell*rho*z`, the three atomic weights are exactly
   `d=(ell-1)(rho-1)/(ell*rho)`, `p=c_ell*c_rho/(ell*rho)`, and `d-p`.
   Thus `C_A=d Delta`, `C_K=(d-p)Delta`, and `C_P=p Delta`; the dangerous
   conductor factor is cancelled before absolute values. No separate A/K
   payment is claimed.
2. The complete member is unchanged because every grouped feature agrees and
   coefficients are summed literally. Therefore the full uncentered `P_PP`
   is exactly invariant. The centered traces differ by their stated ledger;
   the literal Wick convention is not silently replaced.
3. For complex amplitudes, Cauchy gives `-E<=delta<=(m-1)E`. The absolute
   bound follows for `m>=2`, while `m=1` gives exactly zero. Its negative
   part needs no multiplicity factor. An empty source has zero correction.
4. The one-sided Boolean histories are disjoint ordered triples of the
   fixed full core, so their count is at most `d_3(core)`; L-106080 also
   states the squarefree bound `3^omega(core)`. L-102883 supplies the
   polylogarithmic dyadic-label count. Active finite-horizon products bound
   the cores by a fixed power of `Y`. Taking the product of the two counts
   gives uniform `m_Y=Y^o(1)` **only for the declared history grouping**.
   No carrier, conductor or other retained-label multiplicity is absorbed.
5. T-106140.9--.10 and corrected L-106121.9 give precisely the principal
   diagonal with `dmu=|kappa_hat(t)|^2 dt/(2pi)` and the complete source
   conductor sum. Multiplication by `m_Y-1` proves the asserted global
   principal correction and total-variation bound. No pointwise-in-`t`,
   extra supremum, new shell projection or moved maximum is used.
6. The hundred-history control has sum `4`, energy `676`, and correction
   `-660` after its common exact native factor is removed. Its three grouped
   channels vanish. Both live four-pair panels retain off-diagonal
   coefficient `16d`; opposite-corner interactions are untouched. Native
   Mellin amplitudes remain constrained symbolic quantities, not free knobs.

## Replay and authentication

The reviewed SHA was checked in a new worktree with fresh Windows checkout
line endings. Both producer modes and all **17 original tests** passed;
Ruff check/format and `git diff --check` passed. Nine frozen Git blobs and
eleven inherited primitive bindings authenticated. The collision producer's
loaded bytes match its frozen source after LF normalization; fixture
comparison is canonical and type-strict. No primitive-data source-lock
bypass or optimized-mode validation omission was found.

An additional independent read-only exact complex-amplitude calculation
checked **729 assignments**, directly summing off-history terms and verifying
all three correction identities and uncentered principal invariance.

After the scoped repair, the two producer modes and **18 tests in each
mode** pass, as do Ruff check/format and `git diff --check`:

```text
python -B research/l-families/atlas/function_field/ffps_signed_history_recombination.py --check
python -B -O research/l-families/atlas/function_field/ffps_signed_history_recombination.py --check
python -B -m unittest tests.test_ffps_signed_history_recombination
python -B -O -m unittest tests.test_ffps_signed_history_recombination
python -B -m ruff check research/l-families/atlas/function_field/ffps_signed_history_recombination.py tests/test_ffps_signed_history_recombination.py
python -B -m ruff format --check research/l-families/atlas/function_field/ffps_signed_history_recombination.py tests/test_ffps_signed_history_recombination.py
git diff --check
```

## Remaining load-bearing hypotheses

The smallest algebraic failure would be grouping atoms with different family
features. The smallest analytic failure would be using a grouping whose
multiplicity is not uniformly subpower, or a different measure/source for
which the imported principal diagonal has not been paid. The two historical
analytic imports are inspected and explicitly inherited, not independently
reproved by this finite replay. The complete cross-group signed estimate,
native geometric realization, admissible coefficient-family questions,
`WCEQ`, `WCADD/WCCORR`, `WCKUM`, RH and GRH remain open.
