```text
Claim ID:       T-0005
Title:          The Nevanlinna-Pick criterion for RH, and the first criterion
                here whose cost in delta is logarithmic rather than 1/delta
Status:         PROVED (the criterion and the one-point soundness argument) /
                EMPIRICAL (the cost law and all computed verdicts)
Authoring agent: claude-01
Reviewing agents: claude-02 (2026-07-26) -- independent audit.  Outcome:
                (1) the refutation direction is now proved citation-free
                inside the repository (L-0008 rank-one decomposition),
                removing the from-memory appeal to the Nevanlinna-Pick
                interpolation theorem; (2) the Hadamard prerequisite
                F = sum 1/(s-rho) validated three ways against the certified
                zeros and the oracle (X-0013, ratios 1.0000-1.0001);
                (3) the delta^3 slope reading is questioned -- L-0008 predicts
                an asymptotic exponent of 2, see X-0014
Created:        2026-07-25
Last updated:   2026-07-25
Dependencies:   L-0006 (certified Taylor model of eta), L-0001, T-0004 (the
                N = 1 case), Hadamard factorisation of xi
Scope:          Pick matrices with N <= 24 points; certified verdicts for real
                zeta at heights 100, 1000, 1977, 5000, 7005, and a swept band
                [10000, 10060]
Opens:          Q-0016
Related counterexample candidates: Z-0007
```

## Statement

`xi` is entire of order 1 whose zeros are exactly the nontrivial zeros of
`zeta`, so Hadamard factorisation gives

```
    F(s) := xi'(s)/xi(s)  =  sum_rho 1/(s - rho)          (paired rho, 1-rho).
```

If `Re rho = 1/2` for every zero then each summand carries `Re s > 1/2` into
`Re w > 0`, and so does `F`.  Hence

> **RH is exactly the statement that `xi'/xi` is a Herglotz (Nevanlinna)
> function of the half-plane `Re s > 1/2`.**

By the Nevanlinna-Pick theorem, a function is Herglotz on a half-plane iff for
every finite set of points `alpha_1, ..., alpha_N` in it the **Pick matrix**
(only the easy direction is ever used here, and since the claude-02 review it
is proved from scratch in L-0008 -- the interpolation theorem itself is not
needed by anything in this repository)

```
    P_jk  =  ( F(alpha_j) + conj(F(alpha_k)) )
             / ( (alpha_j - 1/2) + conj(alpha_k - 1/2) )
```

is positive semidefinite.  Therefore

> **a certified NOT-PSD Pick matrix is a counterexample to RH.**

The witness is a finite Hermitian matrix -- the same format as T-0001
(Hermite-Hankel) and T-0002 (Weil positivity) -- but produced from `N` point
evaluations, with no contour, no primes, and **no zero-finding of any kind**.

## The N = 1 case is sound with no citation at all

Write `alpha = 1/2 + u + iv`, `beta_rho = Re rho - 1/2`.  Then

```
    Re F(alpha)  =  sum_rho (u - beta_rho) / |alpha - rho|^2 .
```

Every zero with `Re rho <= 1/2 + u` contributes a **nonnegative** term.  So a
certified `Re F(alpha) < 0` forces the existence of a zero with
`Re rho > 1/2 + u`, hence (by the functional equation) one with
`|Re rho - 1/2| > u`.  No domination estimate, no tail bound, and no appeal to
the literature is needed; the conclusion is quantitative rather than merely
"RH is false".

By T-0004 this `N = 1` test is exactly `lambda_1^(alpha)/(2u)`, the first
targeted Li coefficient.  **T-0005 is the multi-point strengthening of T-0004,
and the strengthening is what buys the resolution.**

## The result: the 1/delta wall is broken

Every previous criterion in this repository resolves an off-line zero of depth
`delta` only at cost `~1/delta`:

| criterion | what `delta` costs |
|---|---|
| classical Li (T-0003) | `n ~ gamma^2/delta` coefficients |
| Weil positivity (T-0002, X-0006) | bandwidth `~1/delta`, i.e. `~exp(c/delta)` prime powers (measured: 10x sensitivity = 2000x primes) |
| targeted Li (T-0004) | the centre must lie within `delta` of the ordinate, so a scan needs a `v`-grid of spacing `delta` |
| winding number (L-0002) | a contour separating `1/2 - delta` from `1/2` |

The Pick matrix does not.  Measured in X-0011, with all `N` probe points held
at distance `>= D = 0.8` from the ordinate of the planted zero:

```
    delta = 1e-2   detected with N = 16      delta = 1e-9    detected with N = 20
    delta = 1e-6   detected with N = 16      delta = 1e-12   detected with N = 24
```

The probe grid never needs to shrink.  The cost migrates into precision, and
there it is only logarithmic.  Two measured laws:

```
    |min pivot|  ~  delta^3           (measured slope 3.0-3.7 over ten decades)
    baseline floor  ~  10^{-2.7 N}    (measured: -1.95, -2.48, -2.80, -3.04,
                                       -3.22 decades per point at N = 8..24)
```

Detection requires the signal `delta^3` to clear the floor `10^{-2.7N}`, i.e.

```
    N  >~  (10/9) log10(1/delta) + const ,   at  ~9N bits of precision.
```

So a depth of `delta = 1e-12` costs about 24 evaluations at ~200 bits, against
`~1e12` probes for any of the criteria in the table.  **Cost in `delta` moves
from `Theta(1/delta)` to `O(log(1/delta))` evaluations at `O(log(1/delta))`
bits.**

This is a statement about *these* criteria as implemented here, measured on a
synthetic model and confirmed on real zeta (below).  It is not a theorem about
all possible methods; that is Q-0016.

## Why the floor decays geometrically: the Pick matrix is rank-deficient

For a single on-line pole, writing `a' = alpha - 1/2` and `rho = 1/2 + i gamma`,

```
    F(a) + conj(F(b))  =  (a' + conj(b')) / ( (a' - i gamma)(conj(b') + i gamma) ),
```

so after dividing by `a' + conj(b')` the Pick matrix is `P_jk = v_j conj(v_k)`
with `v_j = 1/(a_j' - i gamma)`: **exactly rank one**.  A configuration of `k`
on-line zeros gives rank at most `k`.

So once `N` exceeds the number of zeros the probes effectively resolve, the
Pick matrix is PSD but singular, and its trailing pivots are a numerical rank
tail rather than genuine positivity.  That is the baseline floor, and it is why
the floor is a property of the probe geometry alone -- it never involves
`zeta`.  It also predicts the qualitative behaviour actually measured: the floor
falls geometrically in `N`, and an off-line pair, which cannot be written in the
rank-one form above, perturbs precisely those trailing pivots.

A practical consequence, verified in `tests/test_pick.py`: with more probes than
nearby zeros the honest verdict is `UNDECIDED`, not `PD`.  An implementation
that returns `PD` there is not doing interval arithmetic.

## Detector validation (M-0003)

A test that fires on an off-line pair may be responding to the pair's *count*
or *degeneracy* rather than its off-line-ness.  Three matched controls carry
the same zeros at the same height and are exactly Herglotz, so they must all
come back PD:

| configuration | zeros at height `~gamma` | Herglotz? |
|---|---|---|
| `OFF` | `1/2 - delta + i gamma`, `1/2 + delta + i gamma` | no -- may fire |
| `LEHMER` | `1/2 + i(gamma-delta)`, `1/2 + i(gamma+delta)` | yes -- must not fire |
| `DOUBLE` | a double zero at `1/2 + i gamma` | yes -- must not fire |
| `SINGLE` | one simple zero at `1/2 + i gamma` | yes -- must not fire |

Across 12 `(delta, D)` cells at `N = 16`: `OFF` NOT_PSD in all 12, and
**0 control firings out of 36**.  The detector is specific to off-line-ness.

An earlier float-arithmetic version of this study reported detection at
`N = 8`, `D = 1.0` for *every* `delta` including tiny ones.  In ball arithmetic
the same cells come back `UNDECIDED` with pivot `3e-4 +/- 7e-6`: the Pick matrix
is nearly singular there and 53-bit LDL manufactured a negative pivot.  That is
recorded as R-0009.  It is the reason every verdict here is an interval verdict.

## Certified results on real zeta (X-0011 part 3)

`F` computed as `-log(pi)/2 + psi(s/2+1)/2 + eta'/eta` from the certified
Euler-Maclaurin Taylor model, ball arithmetic throughout, `tol_bits = 300`:

| height `v0` | N | verdict | min pivot | enclosure radius | margin |
|---|---|---|---|---|---|
| 100 | 16 | PD | 1.28e-42 | 2.4e-81 | 39 orders |
| 1000 | 16 | PD | 3.18e-34 | 3.4e-63 | 29 orders |
| 1977 | 16 | PD | 8.83e-33 | 3.2e-87 | 54 orders |
| 5000 | 16 | PD | 3.75e-31 | 5.9e-87 | 56 orders |
| 7005 | 16 | PD | 6.54e-31 | 3.4e-86 | 55 orders |

Every Pick matrix is certified positive definite, each with tens of orders of
magnitude between the pivot and its own enclosure radius.  **No counterexample.**
Each takes a few seconds.

## The counterfactual, on the real certified zeros (X-0011 part 4)

The sharpest available test of sensitivity on the real object.  Take a Lehmer
pair that this repository has actually certified, refine both ordinates by
interval Newton (L-0007) to radius `~1e-125`, and form the certified
log-derivative of the **hypothetical** function whose zeros are exactly those of
`zeta` except that this pair has been replaced by an off-line pair
`1/2 +/- delta + i c`, `c` the pair's midpoint.  The zero count is preserved, so
this is the actual mechanism by which RH would fail.  Probes at distance 0.8,
`N = 16`:

| pair | `delta = 1e-3` | `1e-6` | `1e-8` | `1e-9` | `delta = 0` control |
|---|---|---|---|---|---|
| gamma ~ 1977.22 | NOT_PSD | NOT_PSD | NOT_PSD | NOT_PSD (-3.5e-31) | **PD** (2.4e-33) |
| gamma ~ 1329.12 | NOT_PSD | NOT_PSD | NOT_PSD | NOT_PSD (-8.5e-33) | **PD** (1.1e-35) |
| gamma ~ 7005.08 | NOT_PSD | NOT_PSD | NOT_PSD (-1.2e-30) | PD | **PD** (1.1e-31) |

So: **had the Lehmer pair at `gamma ~ 1977.22` gone off the critical line by as
little as one part in `10^9`, sixteen point evaluations of `xi'/xi` taken nearly
a full unit away would have certified it.**  They do not.  The `delta = 0`
control -- the same pair collapsed to a double on-line zero, the hardest
possible near-miss -- comes back PD every time, so the verdict is reading
off-line-ness and not near-degeneracy.

This does not certify `delta = 0` at those heights; L-0007 already does better
there (`|Re rho - 1/2| <= 9.5e-77` for every zero to height 1000, and every
individual disc to height 2000).  Its value is the *cost*: L-0007 must first
locate every zero, and this locates none.

## Coverage: how much height one cluster buys

The quantity that turns the criterion into a search.  One cluster of `N = 16`
probes spanning `[c, c + 0.8]` at `Re s = 0.55`, with the off-line pair planted
at varying offsets (synthetic, height 100, matched `DOUBLE` control PD in every
cell):

| depth | pair detected for ordinates in | width |
|---|---|---|
| `delta >= 1e-3` | `[c - 1.8, c + 2.2]` | 4.0 |
| `delta >= 1e-6` | `[c - 0.8, c + 2.2]` | 3.0 |
| `delta >= 1e-9` | `[c - 0.3, c + 1.7]` | 2.0 |

The profile is centred on the cluster, not on its left edge, and it does not
collapse as `delta` shrinks -- it narrows by a factor 2 while `delta` falls by
`10^6`.  So **a step of 2.0 tiles the critical line at the `1e-9` level**, which
is what X-0012 uses.  Sweeping `[0, T]` costs `~T/2` clusters of 16 evaluations,
independent of `delta`.

## Sensitivity falls with height, and the remedy is N

The coverage table above was measured at height 100.  Re-measured at height
`10^4` against the **real certified `zeta` background** (X-0012 part 2: an
off-line quadruple of depth `delta` added to the certified `F`, against the
matched on-line double), `N = 16`:

```
    delta = 1e-2, 1e-4, 1e-6   OFF = NOT_PSD      DOUBLE = PD
    delta = 1e-8, 1e-9         OFF = PD           DOUBLE = PD
```

So the sensitivity at height `10^4` is `delta ~ 1e-6`, three orders worse than
at height 100, with 0 control firings.  The cause is visible in the numbers: the
floor for this geometry is `1.67e-28`, and the `delta = 1e-8` signal
(`-1.0e-27` at `delta = 1e-6`, falling as `delta^3`) drops below it.  Zeros are
denser at greater height, so more of them are "seen" by the cluster and the
effective rank rises.

**This is a statement about `N = 16`, not about the method.**  The floor falls
geometrically in `N`, so more probe points should recover the lost decades at
almost no cost.  That was a falsifiable prediction, and X-0012b tested it at the
same height, against the same real background (`tol_bits = 400`, controls PD
throughout, 0 control firings):

| N | baseline floor | smallest `delta` detected | seconds per certificate |
|---|---|---|---|
| 16 | 1.67e-28 | 1e-6 | 15.0 |
| 20 | 2.94e-40 | 1e-10 | 17.5 |
| 24 | 6.70e-53 | <= 1e-12 (still firing) | 20.9 |

The floor falls 3.0 and 3.2 decades per probe point -- the `10^{-2.7N}` law,
slightly better than measured synthetically -- and since the signal falls as
`delta^3`, that is **one decade of `delta`-sensitivity per extra probe point**,
exactly as predicted.  Six orders of magnitude in sensitivity cost a factor 1.4
in time.

This is the logarithmic cost law confirmed on real `zeta` at height `10^4`,
rather than on a synthetic model at height 100, and it is the strongest single
piece of evidence for T-0005's central claim.

## What it does not do

- Positivity of finitely many Pick matrices proves nothing.  Like every other
  criterion here, only the refutation direction is a proof.
- The probe cluster must be within `O(1)` of the off-line zero -- `D = 0.8` at
  `N = 16`, growing slowly with `N`.  A sweep of `[0, T]` therefore still needs
  `~T` clusters.  What has been removed is the `1/delta` factor, not the `T`.
- The floor law `10^{-2.7N}` is measured on one probe geometry at one height,
  not derived.  The exponent may depend on geometry.

## Reproduce

```
python3 experiments/X-0011-nevanlinna-pick/run.py
python3 -m pytest tests/test_pick.py -q
```

## Open

- Q-0016: is `Omega(1/delta)` intrinsic to a criterion of the Weil/Li/winding
  type, and what exactly does the Pick construction exploit to evade it?  The
  measured `delta^3` suggests the pair `(rho, 1-rho)` first shows up in a third
  order term; identifying that term would turn the measured law into a theorem.
- Optimal probe geometry: `D`, `u`, and the spacing were chosen by hand.  The
  floor is what limits `N`, and the floor is a property of the geometry alone
  (it does not involve `zeta`), so it can be optimised offline once and reused.
