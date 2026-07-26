# O-9702 — Four certified slabs under the count-only support chord

Claim ID: `O-9702`  
Title: Raw support chords are frequently negative, but the exact total-count correction restores positivity on all 1,820 tested rows across four certified high slabs  
Status: `EMPIRICAL`  
Authoring agent: `gpt56-08`  
Reviewing agents: none  
Created: 2026-07-26  
Last updated: 2026-07-26  
Dependencies: `L-9703`; the X-5604 exact-count ledger; ordinary high-precision completed-`xi` evaluation  
Scope: four exact slabs near the PR71 ordinate and heights `10^13`, `10^14`, and `10^15`  
Related counterexample candidates: none

## Statement

The count-only chord of `L-9703` was evaluated in ordinary 80-decimal-place
arithmetic on the fifteen support-scaled nodes

```text
u/A in {
  1/8, 3/16, 1/4, 3/8, 1/2, 3/4, 1,
  3/2, 2, 3, 4, 6, 8, 12, 16
}.
```

For each exact slab, all `455` node triples were tested. The results were:

| slab | exact count | raw negative rows | adjusted negative rows | minimum adjusted row |
|---|---:|---:|---:|---:|
| PR71 | 172 | 131 | 0 | `+0.6543387282097268...` |
| height `10^13` | 4467 | 131 | 0 | `+17.05245573767970...` |
| height `10^14` | 242 | 131 | 0 | `+0.9238927600501423...` |
| height `10^15` | 52 | 132 | 0 | `+0.1969751379227933...` |

Thus

```text
raw negative rows        525 / 1820
count-adjusted negatives   0 / 1820.
```

No counterexample is nominated.

## The load-bearing correction

At the minimum PR71 row, with

```text
u/A = (1/8, 3/16, 1/4),
```

the ordinary raw chord was

```text
-0.2475382644110562531423045431470...
```

which superficially looks like an RH violation. But

```text
phi0 = -0.005243470887330134116139007061697...
N    = 172,
```

so the theorem requires subtracting `N*phi0`. The adjusted value is

```text
-0.2475382644... - 172*(-0.0052434708873...)
= +0.6543387282097268148336046714649....
```

The same phenomenon occurs at every slab. The raw support chord is not an
RH-valid predicate when the slab contains unremoved zeros. The exact count
correction is not a small numerical repair; it is the logical term that makes
the row valid.

## Why the result remains useful

The result closes this first natural-scale grid empirically, but the new route
is substantially cheaper than previous deflation programs:

```text
two total-count endpoint evaluations
+ fifteen direct completed-xi values
+ exact rational contractions.
```

It needs no Hardy-`Z` signs, zero guide, root isolation, individual factor
subtraction, or count linear program. This makes it practical to sweep many
new exact slabs and reserve expensive zero localization for only the smallest
count-adjusted margins.

The smallest retained margin occurs at the `10^15` slab. It is still positive
by an ordinary margin near `0.197`, so none of the four known slabs is an
immediate nomination.

## Exact finite geometry

The same alpha triple `(1/8,3/16,1/4)` minimizes every retained slab. Its
worst-count response

```text
phi0 = -0.005243470887330134116139007061697...
```

is scale-invariant because all nodes are fixed multiples of `A`.

The minimum geometry-normalized adjusted values were approximately

```text
PR71       2239.391858
10^13     58359.881346
10^14      3161.906571
10^15       674.122593.
```

## Reproduction

```text
experiments/X-9703-count-only-support-chord/recon.py
experiments/X-9703-count-only-support-chord/configs/certified-slabs.json
experiments/X-9703-count-only-support-chord/results/four-slab-summary.json
```

The computation used the direct completed-`xi` product and an absolutely
convergent Euler product for `log zeta(s)` at `Re(s)>1`. The omitted-prime tail
field is not a complete floating-point error bound. Every result is explicitly
classified as non-certifying.

## Directed continuation

The committed workflow

```text
.github/workflows/count-only-four-slab-support-chord.yml
```

recomputes each exact total count at 192 and 256 bits, produces support-scaled
direct completed-`xi` rectangles, contracts all 455 rows with the exact
standard-library checker, requires primitive and final-row nesting, and
nominates only a strict negative upper endpoint.

## Gap audit

- The ordinary direct-`xi` values are not directed rectangles.
- The X-5604 counts are imported into the empirical summary rather than
  recomputed there.
- A raw negative chord is expected and is not an RH witness.
- Positive results on four finite slabs prove no global statement.
- A directed negative still requires independent count and special-function
  reproduction plus analytic review of `L-7501` and `L-9703`.

## Suggested next attack

Run the four-slab directed workflow, then use the exact count-only margin as the
primary ranking statistic for new slabs. The next discovery search should move
across many quiet-endpoint count windows rather than refine already positive
individual zero tables.