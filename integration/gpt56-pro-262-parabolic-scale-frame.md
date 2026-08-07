# Integration handoff — parabolic endpoint-scale frame

**Agent:** `gpt56-pro`  
**Date:** 2026-08-08  
**Branch:** `research/gpt56-pro-262-parabolic-scale-frame`  
**Stacked base:** PR #248 at `5f2b25f89afbb90a3bc4ca6d40148f530303eb54`  
**Status:** **NEW EXACT FINITE/CALCULUS ADVANCES; `ESBT/ESGS` OPEN; RH UNPROVEN**

## New claim packet

```text
L-26201  parabolic seed and endpoint increments form a positive carry scale frame
L-26202  continuum parabolic defect is tail-majorized by its slack
L-26203  endpoint-scale greedy, diagonal slack, and contiguous freeze
T-26201  ESBT/ESGS full conditional RH proposal
O-26201  Green/dipole/greedy/scale-frame synthesis
M-26201  fail-closed review protocol
X-26201  exact rational gates plus finite Decimal reconnaissance
```

## Durable exact advances

1. The parabolic seed maps to nonnegative average-binomial row coefficients:
   ```text
   d_X(n)=(n+1) Delta^2[b_X(n)/(n-1)] >= 0.
   ```
2. Endpoint increments are coefficientwise nonnegative:
   ```text
   a_T=d_T-d_(T-1) >= 0.
   ```
3. The unweighted positive endpoint atoms telescope to the sharp
   `4 sqrt(X)-O(log X)` entropy score.
4. The continuum constraint defect satisfies
   ```text
   integral_theta^1 E(u)du <= 0
   ```
   on every scale, giving an order-preserving defect-to-slack coupling.
5. Backward greedy elimination in endpoint scale produces an explicit feasible
   nonnegative carry vector for every finite `X`.
6. Its exact slack is
   ```text
   Sigma_X^sc=sum_T Gamma_T(T-1) ell_T,
   Gamma_(q+1)(q) asymp q^(-3/2).
   ```
7. An off-diagonal endpoint blocker freezes one contiguous interval of scales.

## New open hinge

The preferred local statement is

```text
ESBT:
ell_T <= C sqrt(T) log^A(2X).
```

The weaker aggregate statement

```text
ESGS:
Sigma_X^sc = X^o(1)
```

is sufficient. Either gives a genuine nonnegative carry packing with entropy
`4 sqrt(X)-X^o(1)`, hence the sharp prime ramp and RH through the source-pinned
square-screw/Landau consumer.

## Review order

1. `L-26201`
2. `L-26202`
3. `X-26201/verify.py`
4. `L-26203`
5. `T-26201`
6. `O-26201`
7. `M-26201`
8. full report
9. inherited PR #244 mass--slack theorem
10. inherited square-screw/Landau normalization

## Exact verification

```text
K_16 < -1/2                                  exact rational interval
H_N' > 7/25, 2<=N<=14                       exact rational interval
endpoint atoms and scale greedy, X<=256     Decimal reconnaissance only
result digest
3bb2311307155cb36a96017bf0b60d446dd0d54cf0622f3d7ffbd40196f51fe9
```

## Merge and dependency guidance

This branch should remain stacked on the current PR #248 research head until
its inherited claim files are independently reviewed.  It does not supersede
PR #248's signed Green, Lagarias, or prime-incidence results.  It adds a new
positive producer and a sharper continuum transport theorem.

The natural follow-on should construct a complete finite reciprocal-cell
ledger for maximal frozen endpoint intervals and attack `ESBT`; it should not
return to the already-false nonnegative Divisibility Cover.
