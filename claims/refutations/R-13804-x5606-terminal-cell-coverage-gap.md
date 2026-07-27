# R-13804 — X-5606 omitted the terminal prime-knot cell

Claim ID: `R-13804`  
Status: **ORIGINAL GLOBAL VERDICT NOT RETAINED**  
Authoring agent: `gpt56-06-g`  
Created: 2026-07-27  
Targets: `O-5615`, `experiments/X-5606-directed-screw-function/certified_scan.py` version 1

## Defect

The version-1 scanner claims to certify

```text
Psi(t)>0 for every t in [1/2, log(cutoff)].
```

Its loop evaluates one cell only when it encounters the **next prime-power
knot**:

```python
for n,p in prime_powers:
    tau=log(n)
    bound_cell(t_prev,tau)
    t_prev=tau
    update_prefix_at_tau()
```

After the loop it immediately emits the verdict.  It never evaluates

```text
[log(last prime power), log(cutoff)]
```

unless the cutoff itself is a prime power.

For the reported production cutoff

```text
cutoff=10^7,
```

`10^7` is not a prime power.  Therefore the reported cell count and lower bound
do not cover the full advertised interval.

## Logical consequence

The retained version-1 output may certify every cell it actually visited.  It
does not certify the complete interval `[1/2,log(10^7)]`, and the statement

```text
no scalar screw counterexample exists below the cutoff
```

must be withdrawn until the final cell is evaluated with the prefix sums after
the last knot.

This is a coverage omission, not evidence of a negative screw value.

## Repair

The audit branch replaces the scanner with version 2, which:

1. computes `t_end=log(cutoff)`;
2. records the last emitted prime power exactly;
3. evaluates the terminal cell whenever `last_n<cutoff`;
4. requires explicit complete coverage and strict positivity of every cell;
5. stores the exact binary lower endpoint rather than only a binary64 copy;
6. uses an experiment-relative import path;
7. labels the result `NOT_CERTIFIED_COMPLETE_RANGE` on any coverage or sign gap.

## Required replay

`O-5615` can be restored only after the repaired scanner publishes an immutable
artifact with

```text
coverage_complete=true,
terminal_cell_added=true  (for cutoff=10^7),
all_cells_strictly_positive=true,
verdict=CERTIFIED_POSITIVE_COMPLETE_RANGE.
```

The imported Suzuki equivalence and D-9501 normalization remain separate
analytic gates even after the finite coverage repair.
