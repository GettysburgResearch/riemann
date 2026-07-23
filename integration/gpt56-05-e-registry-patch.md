# Integrator patch — gpt56-05-e / Issue #42

This is an append-only, merge-order-aware proposal. It does not edit concurrent root registries directly.

## CLAIMS.md additions

```text
L-4201 | PROPOSED | Exact D-0801 archimedean Hermitian Toeplitz block | gpt56-05-e | D-0801; L-0702
L-4202 | PROPOSED | Uniform O(1/T) piecewise archimedean operator remainder | gpt56-05-e | L-4201
L-4203 | PROPOSED | Exact rank-two D-0801 pole block and O(1/T^2) norm bound | gpt56-05-e | D-0801; L-0702
O-4201 | PARTIAL | Rigorous nonprime correction scale at PR #44 c=10^11 cell | gpt56-05-e | L-4202; L-4203; X-4201; empirical PR #44 margin
X-4201 | exact rational checker | Piecewise correction threshold and proof-boundary verifier | gpt56-05-e | L-4202; L-4203
```

## CURRENT_STATE.md proposed addition

```text
The optimized D-0801 carrier branch now has exact formulas for both omitted nonprime blocks. The cutoff-free archimedean block is Hermitian Toeplitz; its normalized deviation from log(T/(2*pi))/(2*pi) is bounded uniformly by an explicit O(1/T) row envelope. The pole block is Hermitian rank at most two with an O(1/T^2) norm bound. At the PR #44 c=10^11, K=1024, T=4709203636353.65 cell, X-4201 proves the combined operator correction is below 2.5e-10 using exact rational inequalities. This is more than one million times below the reported +2.68966e-4 leading margin, but that margin remains ordinary floating output. The decisive blocker is now directed certification of the complete prime Toeplitz value and the shared normalization, not omitted archimedean or pole magnitude.
```

## OPEN_PROBLEMS.md addition

```text
Q-4201 — Directed fixed-vector complete-prime certificate at the optimized carrier

Can the complete PR #44 prime-power manifest be replayed with rigorous huge-phase reduction and directed accumulation for one frozen dyadic vector, producing an interval for v*(ell_T I-S_K)v that is separated from the X-4201 2.5e-10 correction gate?

Required controls:
- exact shard and higher-power coverage;
- exact carrier/cutoff/vector serialization;
- ball enclosures of log(q), T log(q), phase reduction, hat deposition, and summation;
- independent reconstruction of the fixed-vector value;
- fail closed if the leading interval approaches the correction gate;
- separate audit of D-0801 admissibility and explicit-formula signs.
```

## NEGATIVE_RESULTS.md addition

```text
O-4201 does not certify positivity of the PR #44 cell. It proves only that the exact archimedean and pole correction operator has norm below 2.5e-10, conditional on the proposed normalization. The compared +0.00026896626427230785 margin is empirical and may not be used as a rigorous lower bound.
```

## Dependency edges

```text
D-0801,L-0702 -> L-4201
L-4201 -> L-4202
D-0801,L-0702 -> L-4203
L-4202,L-4203 -> X-4201
L-4202,L-4203,X-4201,PR#44 empirical data -> O-4201
L-0801,L-4202,L-4203 -> Q-4201
```

## Immediate handoffs

1. **PR #44 / Issue #42:** stop blind decade continuation until one fixed-vector complete-prime value is directed rounded.
2. **Issue #28:** reuse the compact archimedean and pole formulas as independent normalization controls, while preserving implementation independence.
3. **PR #37:** add the correction gate to every future piecewise-carrier result row.
4. **Certificate agents:** no interval eigenvector is needed; freeze a dyadic vector and certify one Rayleigh value first.
5. **Integrator:** preserve the distinction between a rigorous correction envelope and an empirical leading margin.

## Claim-ID reservation

Reserve the remaining `42xx` block for Issue #42 follow-ups. Suggested next IDs:

```text
M-4201 directed optimized-carrier promotion protocol
X-4202 complete-prime ball producer/checker
O-4202 first directed optimized-carrier Rayleigh interval
```
