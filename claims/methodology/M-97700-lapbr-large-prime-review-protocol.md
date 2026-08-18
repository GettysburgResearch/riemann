# M-97700 - Hostile review protocol for the large-prime parity boundary

1. Reconstruct the positive layers `B_r(X)` from the literal `P_61` annular base.
2. Check the product-safe cutoff `Y=X^(1/(2r))`: every selected `r`-prime product
   is at most `sqrt X`, so the base lower asymptotic applies uniformly.
3. Recompute the repeated-coordinate collision bound
   `r!e_r >= A^r-binomial(r,2)S_2 A^(r-2)`.
4. Verify `r=O(log log log X)`, `A~Lambda~log log X`, and
   `r log r/Lambda -> 0`.
5. Check the final odd layer dominates with the correct sign when `L` is even.
6. Confirm `L_res=C_L-S_X`, so a negative full current and positive small cube
   force `L_res<-S_X`.
7. Recompute the complete small-prime cube using exact Euler products; do not
   replace its signed constant term by unsigned mass.
8. Verify largest-prime ownership in the Bellman telescoping identity.
9. Expand one finite prime set and check every nonempty history appears once.
10. Check the Type-I cutoff `p>X/Z` really makes the large-prime child empty.
11. Preserve the Möbius signs and the constraint `P^+(v)<p` in Type II.
12. Reject any proof using rowwise absolute values, an unrestricted reservoir,
    or a source-blind large sieve for `mathfrak T_Z`.
13. Reconstruct the annular Mellin transform and Landau hypotheses before any
    RH-level promotion.

The packet fails if the product cutoff is not activation-safe, if a collision
term has the wrong orientation, if one owner is duplicated, or if the Type-II
sum is replaced by a norm that discards its signs.
