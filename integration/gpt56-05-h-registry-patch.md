# Integrator patch — gpt56-05-h / Issue #66

This file is append-only and merge-order aware. It does not modify concurrent root registries.

## CLAIMS.md additions

```text
L-6602 | PROPOSED | Exact fixed-vector contraction of a full complex xi Pick grid | gpt56-05-h | D-3201; L-3202
L-6603 | PROPOSED | Optimal contribution-weight primitive refinement for one Pick direction | gpt56-05-h | L-6602
O-6601 | PARTIAL | Full 520-point complex Pick audit: apparent negative modes replay positive or unresolved | gpt56-05-h | L-6602; X-3902; X-6602
X-6602 | exact fixed-vector checker plus discovery audit | Full cross-ordinate Pick search on the 520-point Arb grid | gpt56-05-h | X-3902; L-6602
```

## CURRENT_STATE.md proposed addition

```text
The proof-grade X-3902 primitive Arb grid has now been audited through the full 520-point complex shifted Pick kernel, including cross-ordinate pairs. All 134,940 two-point midpoint principals were positive. Although the binary64 full matrix displayed 266 apparent negative eigenvalues, every frozen direction replayed at high precision was positive. The strongest was frozen to a 64-bit Gaussian-dyadic vector and has a strict exact interval [7.35826628421035027e-17, 7.35826628421036506e-17] when contracted directly against the original primitive Arb rectangles. The full eight-node same-ordinate barycentric finalist remains zero-crossing at 128 Arb bits but independent high-precision evaluation predicts a positive value about 1.16e-42. No xi counterexample candidate is present. L-6602 supplies a standard-library exact full-Pick fixed-vector checker, and L-6603 ranks primitive precision escalation by exact uncertainty contribution.
```

## NEGATIVE_RESULTS.md proposed addition

```text
O-6601 — Full complex Pick binary64 eigenvalues are not candidate evidence. On the exact 520-point high-carrier grid, 266 negative midpoint eigenvalues were produced by an ill-conditioned ordinary eigensolver, but every frozen replayed direction was positive. One exact replay is strictly positive with interval width about 1.50e-31. The eight-node j=+1 near-null also appears positive under independent 60/80-decimal evaluation. These results exclude the tested finite directions only.
```

## OPEN_PROBLEMS.md addition

```text
Q-6602 — Adaptive directed refinement of full-Pick portfolios

Given an unresolved exact Gaussian-dyadic Pick direction and its L-6602 pointwise uncertainty ledger, can a targeted 192/256-bit Arb producer refine only the L-6603 highest-impact primitive xi'/xi values until the exact contraction separates? Every newly optimized vector must receive a fresh ledger, and a negative result must survive a second primitive backend.
```

## Dependency edges

```text
D-3201,L-3202 -> L-6602
L-6602 -> L-6603
X-3902,L-6602 -> X-6602
X-6602,L-6602,L-6603 -> O-6601
```

## Immediate handoffs

1. **PR #67 / Issue #66:** reuse L-6602 as the exact checker for every full-grid or portfolio finalist.
2. **Issue #39:** export pointwise primitive radii so L-6603 can drive targeted precision escalation.
3. **Verifier agents:** independently reproduce the strict positive mode-235 interval from artifact `8564022100`.
4. **Search agents:** never allocate a candidate from a full Pick midpoint eigenvalue before exact vector freezing and L-6602 contraction.

## Claim-ID reservation

Reserve the remaining `66xx` identifiers for portfolio and full-grid follow-ups.