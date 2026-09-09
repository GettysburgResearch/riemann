# O-108505 — Rank-uniform structure of the pointwise-square defect, with an exact rank-4 refutation

```text
Claim ID: O-108505
Status:   OBSERVATION with mixed sub-statuses: PROVED (rank 2, via
          T-108500), EXACT_WITNESS-verified (rank 3), REFUTED_BY_WITNESS
          (the conjectured closed form at rank 4), all exact
Created:  2026-08-30
Programme: #764, axes A/B; feeds the T-108500 follow-up queue
Depends on: T-108500; core/exact.py (stdlib EXACT_RATIONAL runs)
RH status: RH and GRH are unproved; not addressed.
```

## Exact findings (all Fraction-exact, replayable)

For the pointwise square `sum_k h_k^2 T^k` of a generic degree-`d` local
object with elementary symmetric data `(e_1, ..., e_d)`:

1. **Denominator (ranks 2-4, exact):** the minimal denominator is
   `det(1 - Sym^2(A) T)` (degree `C(d+1,2)`), as in the rank-2 theorem.
2. **Numerator degree (ranks 2-4, exact):** `deg N = C(d,2)` — far below
   the naive partial-fraction bound; at rank 3 the bound would give 5, the
   truth is 3.
3. **Gauss-sign exterior-square law:** the closed form

   ```text
   N(T) ?= sum_j (-1)^{j(j-1)/2} e_j(Ext^2 A) T^j
   ```

   is PROVED at rank 2 (it reads `1 + bT`, T-108500), holds EXACTLY at
   rank 3 in all generic instantiations tested, e.g.
   `N = 1 + e2 T - e1 e3 T^2 - e3^2 T^3`, and is **REFUTED at rank 4** by
   exact witnesses: at `(e1..e4) = (1,2,3,2)` the true numerator is
   `[1, 2, -1, -7, 2, -8, -8]` against the predicted
   `[1, 2, -1, -3, 2, 8, -8]` — the discrepancy sits exactly at `j = 3, 5`.
   Three further exact witnesses recorded in the replay. The corrected
   rank-4 law (plausibly involving the self-duality pairing
   `Ext^2 x Ext^2 -> det` special to rank 4) is a follow-up target.
4. **Self-duality is a rank-2 phenomenon:** the defect functional equation
   `N(T) = b^{m(m-1)/2} T^{m-1} N(1/(b^m T))` proved at rank 2 (T-108500)
   FAILS at rank 3 with exact witness: at `(e1,e2,e3) = (1,2,3)`,
   `N = 1 + 2T - 3T^2 - 9T^3` is not palindromic up to any scale.
   Sporadic palindromic instantiations exist at rank 4 (e.g.
   `(1,0,2,-1)` gives the palindrome `[1,0,-3,-5,-3,0,1]`) — recorded as
   data, not interpreted.
5. Degenerate instantiations (e.g. rank 3 at `(1,1,1)`, whose Satake
   polynomial has root-of-unity inverse roots) collapse the defect
   entirely; consistent with the degeneration mechanism of T-108500(5).

## Reading

The obstruction to squaring an L-object is rank-structured: its size is
`C(d,2)` (the exterior square), its leading behaviour at low rank is the
exterior-square characteristic polynomial with Gauss signs, and its
self-duality is exactly as good as the self-duality of the underlying
object. What replaces the Gauss-sign law at rank >= 4 is an open exact
question deposited with witnesses.

Replay: `experiments/X-108505-rank-uniform-defects/verify.py`.
```
