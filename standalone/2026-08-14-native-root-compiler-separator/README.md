# Native-root compiler and exact separator

This packet attacks the Native-Root Capacity Theorem on the live descendant of PR `#468`.

## Frozen frontier

```text
requested PR #468 head: a41f81466f85d52597c97b41505756a8860698d0
live descendant PR #469: 3cf685181bd367b92cdcfeef9249e0b9b542a09e
root-Hall proposal PR #464: 2eb70463f3d0ae791a9f140694d2ace7032ae864
causal/Lorenz PR #467: d5e03a3a63bd05b43abf4b5e37905f86e9ec59d6
primal/Farkas PR #454: a0409d54250bc211d62718a1aedb6fa020d7f091
```

## New durable results

```text
R-91686  exact native q=2 separator for the raw current+child basis,
          including an infinite asymptotic current-only overdraw family;

L-91686  proof that the target-Lorenz cutoff is the exact simultaneous
          optimum of the full stopped-leaf score/row box LP;

L-91687  exact direct radix-four slack LP and Y4-zero score-free
          triangular repair directions;

T-91659  clause-by-clause compilation of PR #464 into T-91314,
          returning the exact finite-realization discrepancy and capacity
          separator rather than a false NRCT pass;

O-91686  source-owned current thinning as the preferred next generator.
```

## Top-level classification

```text
EXACT_NATIVE_ROOT_COMPILATION_DISCREPANCY_AND_SEPARATOR
PASS_NATIVE_ROOT_CAPACITY_THEOREM = false
Riemann Hypothesis = unproved
```

## Decisive obstruction

At `(X,p,q)=(136,67,2)`, the raw current alone saturates both native ordinary and detail capacity, while its exact terminal child adds

\[
\delta=\frac1{\sqrt{134}}\log\frac{68}{67}>\frac1{810}.
\]

For every prime `p>=71`, the raw current itself overdraws ordinary column `2` at `X=2(p+1)` by more than `5/834`.

## Decisive reduction

The full stopped-leaf LP does not require arbitrary basis discovery. Under the frozen monotone profiles, the leftmost target cutoff minimizes score and maximizes every row. A negative leftmost margin is already an exact Farkas separator.

## Preferred next theorem

`SONTR` — Source-Owned Native Thinning and Realization:

```text
one atomwise source partition;
one source-owned recursive packet with mass <1/8;
one detail-slack vector s;
current row reconstructed by the exact triangular inverse;
ordinary/detail/port one-use feasibility;
nonnegative rows and target/score constraints;
bounded Y4-weighted slack.
```

## Review order

1. `claims/refutations/R-91686-...`
2. `claims/lemmas/L-91686-...`
3. `claims/lemmas/L-91687-...`
4. `claims/theorems/T-91659-...`
5. `audits/gpt56-pro/2026-08-14-t91314-native-root-clause-compiler.tsv`
6. experiment and retained JSON
7. report
8. integration lock

## Replay

```bash
cd experiments/X-91686-native-root-compiler-separator
python3 verify.py
python3 -m py_compile verify.py
sha256sum -c SHA256SUMS
```
