# Execution and scope

Executed on 2026-09-18 in the authoring container, Python 3.13.5 / GCC 14.2.0.
The script uses only the Python standard library. There is no package-install
step, external zero table, network dependency, floating-point matrix solve,
or assumed RH condition in the checker.

## Commands actually run

```sh
python verify.py --check results.json --self-test
python -O verify.py --check results.json --self-test
```

Both returned 0. Observed durations were 1.2659 s and 1.2934 s, respectively;
these are one-container execution times, not performance guarantees. Their
stdout was byte-identical, with SHA-256

`f5d0683a83d017a7200ee73e14b29b453b11785faa335dd0f99358eb8888acf9`.

There are 8,940 counted exact comparisons: 119 independent Mobius-recurrence
checks, 1,953 biorthogonality checks, 961 integer Gram entries, 1,457
Ramanujan/dual transport checks, 1,160 Ramanujan differences, 2,314 finite-head
Gram entries, and the remaining source, ramp, coefficient-recovery,
projection, and appended finite-tail identities recorded in results.json.

The six-point vector, its norm 92 and source 1, and the multi-witness lower
bound are rebuilt directly. Exact rational matrix elimination covers the
full sizes 2 through 18 and size 24. The checker's finite loops are not
claimed to cover all indices in the universal theorems.

## Negative controls

Both modes reject/check ten named controls: five altered result records,
dropping adjacent-divisor terms, dropping the rank-one ramp, dropping the
tail, confusing a Gram with its inverse, and duplicate JSON keys. The four
mathematical omissions are explicit non-equality controls, not claimed
mutations of a separately executed source file. Result validation always
reconstructs the expected quantities rather than trusting the incoming
status or a supplied digest.

Two additional actual CLI calls were made. A JSON file with witness norm
91 instead of 92 returned 1 with `certificate differs from reconstruction`.
A duplicate-key JSON file returned 1 with `duplicate JSON key: schema`.
No error was inferred merely from an in-memory annotation.

## What was not done

No whole-repository validator, Lean build, remote CI result, independent
mathematical review, or arbitrary-platform test is claimed. This is an exact
finite regression package, not proof-assistant verification of the written
infinite-dimensional arguments. The trace estimate, completeness statement,
support classification, and target-location lemma depend on the proofs and
stated imported inputs, not on extrapolating the finite tests.

In particular, no upper estimate implying RH has been certified. The
previous conversation's large Gram computations and logarithmic-zeta
integral certificate were not rerun or upgraded in this pass.

Publication is separate from mathematical acceptance. The remote head/PR
receipt and source-object comparison belong to the final GitHub PR record.
