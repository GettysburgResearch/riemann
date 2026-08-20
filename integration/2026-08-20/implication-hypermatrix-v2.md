# Semantic implication hypermatrix v2 — 2026-08-20

Numeric claim IDs have collided repeatedly in the repository. This file uses
stable semantic keys and records whether an arrow is an ordinary implication
or a genuine conjunction.

## Frozen source heads

| source | frozen head | role |
|---|---|---|
| PR #652 | `24ab64551225f2dba9aa53a533eb9b0285c6e363` | exact sequential first-owner source |
| PR #660 | `b3830a12e8823ca74d2a2f709581908c8a9e5402` | first-owner Littlewood--Paley / collapse firewalls |
| PR #671 | `2889071e9ebdc412b94cf2cfe74f1fd5142b2857` | positive divisor-renewal coordinates |
| PR #674 | `9962f7f712adc6b4ad72672ecfeace028ba79bdb` | minimal ratio-eight wavelet |
| PR #676 | `9849df6a52bb4791ebf10cf0dd9f0c929d36bdd9` | centered cubic carrier and detector |
| PR #688 | `24a2a748b8b36a70382c88843bb7779caac97e07` | largest-prime wavelet ownership |
| PR #690 | `36cabbe5843eaa417aac72643c1aad0c2041a31b` | complex shifted-square / mixed Bernstein positivity |
| PR #691 | `c85123d6c25b5b2ade89ab30a736f9b18844a489` | first implication-matrix and direct double-owner tensor |

## Stable semantic nodes

| key | type | mathematical object | status |
|---|---|---|---|
| `P-FO` | producer | coefficient-exact sequential first-owner source | proved |
| `P-LO` | producer | unique largest-prime/cofactor source | proved |
| `X-DO-DIRECT` | transport | direct least/greatest selected-prime tensor | proved |
| `X-DO-HAZARD` | transport | positive two-ended survival/difference tensor | proved in `L-100610` |
| `E-DO-LP` | energy | two-ended Littlewood--Paley/ANOVA identity | proved in `L-100611` |
| `K-CUBIC-CVX` | kernel | positive one- and two-ended cubic differences | proved in `L-100612` |
| `K-CUBIC-SHORT` | kernel/arithmetic | every actual-prime ratio-eight interval is positive | proved in `L-100613` |
| `K-CUBIC-POWER` | kernel/arithmetic | every `q<=p^A`, `A<e^(3/4)`, interval is eventually positive | proved in `L-100615` |
| `X-CARRIER-SHORT` | transport | explicit positive `sqrt(X)` carrier and collar-only residual | proved in `L-100614` |
| `A-FO-ROW` | arithmetic | integrated survival-weighted first-owner collar energy `FOCR100610` | open |
| `A-LO-COL` | arithmetic | integrated survival-weighted largest-owner collar energy `LOCR100610` | open |
| `D-CUBIC-NM` | detector | cubic subpower negative mass implies RH | proved on PR #676 |
| `D-WAVELET` | detector | minimal-wavelet/Mertens critical estimate implies RH | proved / RH-equivalent |

## Exact AND-edges

### `AND-OWNER`

```text
P-FO AND P-LO
    -> X-DO-DIRECT
    -> X-DO-HAZARD
    -> E-DO-LP
```

The direct tensor supplies unique coefficient provenance. The hazard tensor
supplies nonnegative outside weights. The energy tensor supplies positive
squares. No one of these three representations substitutes for the other.

### `AND-KERNEL`

```text
X-DO-HAZARD AND K-CUBIC-CVX
    -> root/singleton/adjacent-owner channels nonnegative
    -> possible negativity confined to nonempty interior prime intervals.
```

### `AND-PRIME-WIDTH`

```text
K-CUBIC-CVX AND prime-reciprocal interval mass
    -> K-CUBIC-SHORT
    -> K-CUBIC-POWER.
```

The cubic double-difference Harnack cost is `4/3`; Mertens supplies interval
mass `log A`. Their conjunction proves positivity whenever
`(4/3) log A<1`.

### `AND-CENTERING`

```text
X-DO-HAZARD AND explicit cubic deep carrier
    -> X-CARRIER-SHORT
    -> Schur matrix contains only partial-activation collars.
```

The carrier is nonnegative entry by entry and must be removed before absolute
matrix estimates. Raw row/column suprema are deliberately rejected as
unnecessarily power-sized.

### `AND-OWNER-ENERGY`

```text
A-FO-ROW AND A-LO-COL
    -> pairwise Cauchy bound for the collar interval matrix
    -> subpower cubic negative mass
    -> D-CUBIC-NM
    -> RH.
```

This is the principal new implication-matrix theorem `T-100610`. The inputs
are survival-weighted row and column energies, not unweighted Schur suprema.
The one-row and one-column separators show that neither marginal estimate alone
controls physical multiplicity.

## Regional incoming edges to the two arithmetic energies

| interval region | row-side input | column-side input | exact status |
|---|---|---|---|
| empty interior | first-owner singleton | largest-owner singleton | closed by cubic convexity |
| `q/p<=8` | cubic Harnack | actual-prime residue-class count | closed unconditionally |
| `q<=p^A`, `A<e^(3/4)` | cubic Harnack | Mertens prime-reciprocal interval mass | closed for large `p` |
| fully active interval | exact cubic carrier | same carrier in reverse orientation | residual exactly zero |
| supercritical partial interval | interior finite Euler squaring | cofactor finite Euler squaring | source identities proved; weighted owner energies open |
| divisor-restricted collar | owner difference before renewal | largest owner before renewal | post-sign transport positive, `d^epsilon` cost proved |
| smooth/deep region | finite first-owner base | smooth/deep largest-prime sector | negligible/closed |

## Numbering policy

- Numeric IDs `100610--100615` are unique to this continuation.
- Stable semantic keys above are the normative dependency handles.
- RH-equivalent statements remain valid detector nodes.
- A detector is never counted as producer progress without an independently
  proved incoming edge.
- `FOCR100610` and `LOCR100610` are kept separate; neither may be silently
  renamed as the full scalar estimate.
- The direct min/max source tensor and the positive survival/difference tensor
  are distinct representations and must not be conflated.

## Scientific boundary

```text
all algebraic AND-edges                    proved
short/power-width interval positivity      proved
positive carrier subtraction               proved
survival-weighted owner-energy composition proved
FOCR100610                                  open
LOCR100610                                  open
Riemann Hypothesis                          unproved
```