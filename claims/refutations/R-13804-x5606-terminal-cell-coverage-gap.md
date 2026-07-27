# R-13804 — X-5606 version 1 omitted the terminal prime-knot cell

Claim ID: `R-13804`  
Status: **ORIGINAL PROOF OBJECT REFUTED; FINITE CONCLUSION RESTORED BY REPLAY**  
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

After the loop it immediately emits the verdict. It never evaluates

```text
[log(last prime power), log(cutoff)]
```

unless the cutoff itself is a prime power.

For the reported production cutoff

```text
cutoff=10^7,
```

the last prime power is `9,999,991`. Therefore version 1 covered 665,134 cells
while the advertised range contains 665,135 cells.

## Logical consequence

The version-1 output does not certify the complete interval
`[1/2,log(10^7)]`. Its global verdict cannot be retained as a proof object.
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

## Directed terminal replay

A terminal-only replay at 128 Arb bits gave

```text
[log(9,999,991),log(10,000,000)]
Psi lower bound
[0.037976880209225143510091755 +/- 4.85e-28] > 0.
```

This establishes that the omitted cell itself is not a counterexample.

## Complete repaired replay

The full range was then partitioned into four disjoint index chunks and replayed
with an independently structured efficient prime-power manifest. The retained
summary is:

```text
prime powers                       665,134
cells including terminal           665,135
all cells strictly positive        true
terminal cell included             true
maximum bisection depth             0

global lower bound
[0.023227951374527490554974016282146664631 +/- 2.98e-40]

verdict
CERTIFIED_POSITIVE_COMPLETE_RANGE
```

The source, four chunk outputs, exact binary minima, summary, and SHA-256 ledger
are retained in `experiments/X-5606-directed-screw-function/`.

Therefore:

```text
VERSION-1 PROOF OBJECT: REFUTED
CORRECTED FINITE RANGE SIGN: RESTORED POSITIVE
```

## Scope after repair

The repaired finite computation excludes only the scalar predicate

```text
Psi(t)<0 for 1/2 <= t <= log(10^7)
```

under the exact D-9501 normalization. It does not close:

- non-arithmetic screw matrices;
- Gaussian or metric screw witnesses;
- heights above the cutoff;
- the imported Suzuki equivalence or its sign convention;
- common python-flint/Arb implementation risk.

The audit replay uses the same Arb library and analytic formula, so it is an
implementation/coverage cross-check under `M-13802`, not an independent
special-function backend.
