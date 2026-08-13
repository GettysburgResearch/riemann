# R-91402 — A tail child cannot reintroduce the fixed small-prime block

Claim ID: `R-91402`  
Status: **EXACT SCOPE REFUTATION / RESET FIREWALL**  
Created: 2026-08-13  
Depends on: paired least-prime recursion  
RH status: **unproved**

## 1. Tail index is part of the state

The exact paired child after a least prime `p_k` is

\[
\mathbf P_{k+1}^{(a)}(x/p_k),
\]

not `\mathbf P_1^{(a)}(x/p_k)`. It contains only squarefree integers whose prime factors are strictly larger than `p_k`.

## 2. Invalid reset

The finite-block expansion

\[
\mathbf P_1^{(a)}
=\sum_{d\mid P_{53}}d^{-1/2}S^{\omega(d)}\mathbf P_m^{(a)}(\cdot/d)
\]

is valid at prime index one. Applying the same expansion to `\mathbf P_{k+1}^{(a)}` would reintroduce primes already excluded by the least-prime condition and duplicate arithmetic source atoms.

Thus the implication

```text
rough child at a smaller endpoint
  -> fresh copy of the same P_53 finite forcing
```

is false without an additional exact canonicalization map.

## 3. Consequence

`L-91404` is an exact one-generation expansion at index one. It is not by itself an all-generation self-similar producer.

A valid recursive proof must do one of:

1. construct a producer uniform in the tail prime index `j`;
2. construct a source-faithful positive canonical reset from `P_j` to `P_1` which does not reintroduce excluded primes;
3. keep the prime index as part of the packet state and prove the packet envelope uniformly over all indices.

## 4. Firewall

```text
one-generation finite-block expansion          EXACT
same P_53 block at every child                  FALSE WITHOUT NEW MAP
tail-index packet envelope                      POSSIBLE / OPEN
canonical prime-index reset                     OPEN / RH-BEARING
Riemann Hypothesis                              UNPROVED
```
