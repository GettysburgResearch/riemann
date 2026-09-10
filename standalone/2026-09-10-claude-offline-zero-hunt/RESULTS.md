# Results

**No off-critical zeta zero was found. RH is neither proved nor disproved.**
Every number below is a certified Arb enclosure. Each experiment was designed so
that one certified sign violation would refute RH; none occurred.

## E1 — derivative-free xi/Pick/Loewner predicates against actual zeta

203 certified predicates per ordinate (secant, two-channel, cross-Loewner 2x2,
barycentric Pick at widths 3 and 4, alternating divided differences), at the 13
dyadic offsets `2^-17 ... 2^-5`.

| band | ordinate range | step | ordinates | predicate evaluations | certified violations | inconclusive | rejected points |
|---|---|---|---|---|---|---|---|
| mid | `[1e6, 1e6 + 36.820]` | `2^-8` | 9 427 | 1 913 681 | **0** | 0 | 0 |
| high | `[3e12, 3e12 + 48.563]` | `3/16` | 260 | 52 780 | **0** | 0 | 0 |

Worst (smallest) certified lower bound over all predicates: `1.92e-15` in the
mid band, `7.04e-13` in the high band; medians `6.25e-12` and `5.16e-9`. Every
predicate was conclusive — no ordinate produced a ball straddling zero, and no
point failed the `xi` division guard.

The high band begins at `3e12`, the Platt–Trudgian certified verification
height, so it is the first evaluation of these predicates above verified
territory. Before this run the packet had been evaluated at two ordinates in
total, both as fixed synthetic controls.

### Detection boundary (what the sweep actually excludes)

`results/e1_calibration.json` injects an off-line mirror pair at horizontal
displacement `delta` and ordinate offset `tau` into the RH-form resolvent
against a realistic local zero field (mean gap 0.22), and bisects for the
largest `tau` still producing a certified violation.

| `delta` | `tau_max` | ordinate step needed |
|---|---|---|
| `1.562e-2` | `9.28e-2` | `1.86e-1` |
| `9.766e-4` | `1.87e-2` | `3.74e-2` |
| `6.104e-5` | `4.61e-3` | `9.23e-3` |
| `7.629e-6` | `1.63e-3` | `3.26e-3` |

Detection succeeded at every `delta` tested, down to `7.6e-6`. The window scales
like `tau_max ~ sqrt(delta)`, i.e. **much wider than `delta`**, which is the fact
that makes a feasible grid meaningful. Combining the table with the grids used:

* mid band excludes an off-line pair with `delta >= ~1.5e-5` anywhere in
  `[1e6, 1e6 + 36.82]`;
* high band excludes an off-line pair with `delta >= ~1.6e-2` anywhere in
  `[3e12, 3e12 + 48.56]`.

These are narrow windows. The honest summary is that the predicates work, are
now instrumented, and that the binding constraint is ordinate coverage, not
sensitivity.

## E2 — de Bruijn–Newman flow and the Laguerre inequality

No zeta evaluator and no zero table is used anywhere in E2.

**Normalisation, pinned by the run.** `H_0(z)` is proportional to `Xi(z/2)`: a
certified sign change brackets `z = 2 x 14.134725...` while the `Xi(z)`
alternative shows none. The census independently recovers zeros at
`z = 28.25, 42.25, 50.25, 60.75, 65.75, 75.25`, i.e. twice the classical
ordinates `14.13, 21.02, 25.01, 30.42, 32.94, 37.59` — the whole `Phi` pipeline
reproducing the low zeta zeros from scratch.

**The hunt (t = 0).** Census over `z` in `[26, 1500]` (`gamma` in `[13, 750]`),
step `0.3`, 4 914 points, all conclusive:

* **0 certified `L_0(x) < 0`.** A single one would have refuted RH.
* 462 certified sign changes of `H_0`, i.e. 462 zeros located from `Phi` alone.
* 0 uninformative points (precision auto-scaled as `0.5665 z + 260` bits, since
  `|Xi(z/2)| ~ exp(-pi z / 8)`).

**The Lambda ladder (t < 0).** At the tightest pair in the census (`z ~ 982`),
bisection in `t` for the largest `t` carrying a certified `L_t < 0`:

```
certified:   Lambda > -0.0100273
witness:     z = 982.0142857,  t = -0.0100274,
             L_t = [-1.2836723e-333 +/- 6.62e-342]     (certified negative)
adjacent:    t = -0.0100272 -> L_t = +2.2958500e-334   (certified positive)
```

The witness value underflows float64, so `results/e2_lambda_ladder.json` records
it as `-0.0` in its float field; the certified enclosure above is the real
content, re-verified directly at 900-bit working precision.

**Calibration of this number, stated plainly.** Rodgers–Tao proved
`Lambda >= 0` unconditionally, which supersedes every lower bound including this
one, and Csordas–Smith–Varga reached `Lambda > -5.895e-9` from a far tighter
pair at much greater height. `-0.0100273` is therefore **not competitive**; its
only merits are that it is self-contained (derived from `Phi` by certified
integration, with no imported zeros) and that it is the first de Bruijn–Newman
computation in this repository. It is reported as an apparatus check and a
starting rung, not as a result.

The bound is limited by census height: the tightest gap found is grid-limited at
the step `0.3`, and collision time scales as `-gap^2/8`, so a finer scan at
greater height moves the rung directly.

## E3 — Weil explicit-formula quadratic form

**Validation first.** `e3_validate.py` compares each `tau(m)` against a direct
sum over 569 zeros obtained independently from mpmath's Hardy Z function:

```
  m       tau(m) coded    tau(m) from zeros     ratio     abs diff
  0       0.0129331915         0.0129331185    1.0000    7.295e-08
  1      -0.0114179391        -0.0114178906    1.0000    4.848e-08
  ...
  8      -0.0117679375        -0.0117679368    1.0000    6.770e-08
VALIDATION: PASS
```

**Result.** For every family tried, the certified `LDL^T` completes with all
pivots positive: the Weil form is **positive definite**, so no test function in
the family violates Weil positivity. This is stronger than "no violation found".

| family | `A` | prime cutoff | `LDL^T` | min certified pivot | float min eigenvalue |
|---|---|---|---|---|---|
| `d=0.25, N=32` | 8.250 | 6 320 | positive definite | `5.128e-5` | `2.135e-8` |
| `d=0.25, N=48` | 12.250 | 344 561 | positive definite | `2.432e-5` | `9.960e-9` |
| `d=0.125, N=96` | 12.125 | 236 816 | positive definite | `3.692e-5` | `2.069e-9` |
| `d=0.5, N=24` | 12.500 | 729 426 | positive definite | `1.658e-5` | `2.776e-8` |

**The margin is the interesting part.** The diagonal is `tau(0) ~ 1.29e-2` while
the smallest eigenvalue is `2e-9` to `3e-8` — Weil positivity holds in these
families with roughly six to seven orders of magnitude of slack relative to the
diagonal scale, and the slack **shrinks as the family grows** (`2.14e-8` at
N=32, `9.96e-9` at N=48, `2.07e-9` at N=96 with finer resolution). The form is
strictly positive definite for a structural reason — an entire `F` of
exponential type `A` has at most `~A T / pi` zeros below height `T`, fewer than
the `~(T/2pi) log(T/2pi)` zeta ordinates, so `h = |F|^2` cannot vanish at all of
them — but the quantitative margin was not previously measured here.

## What none of this establishes

No result above bears on RH's truth. E1 covers two narrow ordinate windows; a
pair with small `delta` between grid points, or at any height outside those
windows, is untouched. E2's census reaches `gamma = 750`, deep inside
exhaustively verified territory, and its `Lambda` rung is far weaker than the
literature. E3 certifies positivity for four finite-dimensional families of
compactly supported test functions and says nothing about the full Weil
criterion. The three experiments were chosen for variance, and the variance did
not pay out.
