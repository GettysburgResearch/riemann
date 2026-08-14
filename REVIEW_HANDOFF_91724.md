# Review handoff — factor-67 activation-knot collar repair

## Placement

```text
repository:       gfreund123/riemann
base PR:          #476
base SHA:         9f16ce483954d4233b68ee09cb6bec47400aa3cc
review PR:        #479
branch:           research/gpt56-pro/91723-factor67-all-column-reserve
```

This packet extends the all-column reserve repair already resident on PR #479.

## Correction

`L-91695` infers convergence in a capacity-normalized root norm from
piecewise Lipschitz continuity and positive interpolation.  This is not valid
at a knot where the normalizing capacity vanishes.  `R-91724` gives the exact
counterexample `V(t)=c(t)=t^2`.

## Repair

`L-91724` uses the actual atomless endpoint measure

```text
dnu(x)=2L(x) dx/x,
density <183/50<4
```

and omits arbitrarily small positive collars around the finite activation set.
On the retained compact cells, every active capacity has a positive minimum,
the deterministic Hall map is Lipschitz, and positive barycentric refinement
has relative error `L_eta h/(2m_eta)`.

Choose the mesh so that the conservative amplified error is less than half of
the `1/(sqrt(K)+130)` reserve from `L-91723`.  The final nonterminal detail
reserve is

```text
Omega_X(q)/(2(sqrt(K)+130)).
```

The collar is removed before the causal split, so `L-91694` preserves the
mass-weighted child contraction.  Collar and interpolation score costs can be
made vanishing.

## Replay

```bash
cd experiments/X-91724-factor67-knot-collar-relative-refinement
python3 verify.py
python3 -m py_compile verify.py
sha256sum -c SHA256SUMS
```

Expected:

```text
PASS_FACTOR67_KNOT_COLLAR_RELATIVE_REFINEMENT
```

Digest:

```text
78b06f7dc034f76c1b65bb0146ec22164588581134dc887771d19315d9b71550
```

## Review order

1. `R-91724`
2. `L-91724`
3. `T-91722`
4. `X-91724`
5. report and dependency lock
6. frozen `L-91107/L-91110/L-91689/L-91692/L-91694/L-91723`

## Exact boundary

```text
small physical columns                       repaired / L-91723
activation-knot relative interpolation        repaired / L-91724
mass-weighted child contraction               exact / L-91694
frozen producer/consumer stack                independent review required
Riemann Hypothesis                            unproved
```
