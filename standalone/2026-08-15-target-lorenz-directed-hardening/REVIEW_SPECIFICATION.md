# Hostile review specification — Target-Lorenz directed hardening

## A. Publication and genealogy

1. Confirm the base is PR #497 at exact SHA
   `bd2a3c32ab50d8a8cec39c4b51ccd63349b23a74`.
2. Confirm the successor is add-only and does not reintroduce any `93420` claim
   path.
3. Recompute the local `93420` SHA-256 values and compare them with the PR #497
   content manifest and the audit TSV.
4. Confirm the corrected heads of PRs #490--#494 against live GitHub metadata.

## B. Directed tail

1. Reconstruct the Hurwitz Euler--Maclaurin formula and differentiated `B_2`
   remainder in `L-93780`.
2. Run `check_zeta.py` and verify the rational outer intervals contain the
   generated narrow intervals.
3. Audit `directed_tail.cpp` for every conversion out of exact `uint128_t`.
4. Confirm `#pragma STDC FENV_ACCESS ON`, saved rounding state,
   `-frounding-math` and `-fno-fast-math` are all active.
5. Run full mode, not only quick mode.
6. Verify all 65 final-tail persistence polynomials are directedly positive.
7. Verify the row-66 upper enclosure is compared with lower enclosures for all
   competing rows, and reject any pointwise-order overclaim.

## C. Compact/tail join

1. Fetch `L-91781` blob `2c16327...` and its result blob `2fda156...`.
2. Confirm its domain is every real `x<166000`, not just integer endpoints.
3. Confirm the tail domain is every real `x>=166000`.
4. Verify the boundary is owned once and has positive directed margin.

## D. Typed leaf and common parent

1. Verify the label tuple is disjoint and exhaustive under the frozen stopping
   line and first-owner theorem.
2. Check `nu=E-U` coefficientwise and `T(U)=T(O)`.
3. Check score orientation `S(U)<=S(O)`.
4. Check the complete AVLT implies `B=R(U)-R(O)>=0` in every required row.
5. Check `B` has zero source target by type, one leaf owner and no child copy.
6. Check the exact physical marginal `R(nu)+B=R(E)-R(O)`.
7. Check ordinary observations at `q` and `4q` use the same aggregate row before
   detail formation.

## E. Native allocation

1. Reconstruct the ideal common-parent native identity from the frozen endpoint
   frame and stopping tree.
2. Confirm all actual child responses remain internal colours.
3. Confirm signed comparison vectors are outside the positive source cone.
4. Re-run the all-column estimate for every `q>=2`, especially `q<K`.
5. Re-run the terminal `581X^-3/2` reserve.
6. Verify positive radix-four inversion gives ordinary feasibility.
7. Confirm exported recursion and root port are both exactly zero.

## F. `Y_4` and endpoint consumer

1. Reconstruct `L-91378` and the sparse sums of `L-19885`.
2. Recompute every named charge in `L-93785`.
3. Reject any use of `J_Lambda-4sqrt(X)`.
4. Review the cross-branch endpoint inputs at the exact PR #352/#353 SHAs in
   the lock.
5. Reconstruct the one-sided finite-dual orientation, prime-square moat, Mellin
   pole survival and Landau argument.

A failure at any item rejects the frozen candidate. It does not establish RH or
its negation by itself.
