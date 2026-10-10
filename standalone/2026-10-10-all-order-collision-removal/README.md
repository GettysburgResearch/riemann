# All-order collision removal for the Möbius/sextic moment program

**Proposed component proofs. No new arithmetic higher moment or zero-free boundary is proved. Independent review is required.**

This add-only packet is designed to follow PR #910 at the frozen source commit
`670a76c1a3a8f325c43c1755b1cfc24d313a3e3c`.

## Main result

For every fixed order 2k, all shared-prime patterns in A_u(D)^k can be removed using one explicit positive-coefficient convolution. The transformed sums have pairwise-coprime squarefree factors and only the original fixed bad-prime set S. **There is no remaining moving coprimality exclusion in the new analytic target.**

The local reconstruction kernel is

\[
 R_k(z_1,\ldots,z_k)=\frac{\prod_i(1-z_i)}{1-\sum_i z_i}.
\]

Its coefficients are nonnegative integers. On squarefree multi-indices of support s they are the derangement numbers !s; on every other multi-index they satisfy an explicit positive recurrence. Its inverse coefficients are simply 1 minus the support size, apart from the constant term.

The square-root weighted kernel mass has exact order

\[
 (\log D)^{\binom{k}{2}}.
\]

Consequently the energy transfer costs only `(log D)^(k(k-1))`: `(log D)^2` for the fourth moment and `(log D)^6` for the sixth. A reverse transfer proves equivalence, up to these logarithmic factors, between a full-scale envelope of higher moments and fixed-mask rectangular collision-free mean squares.

**The rectangle qualification matters:** factor lengths become unequal. An estimate for equal lengths alone is not sufficient. The new reduction removes a moving-mask hypothesis, but does not prove the stronger rectangular cancellation estimate.

## A less demanding route to a stronger boundary

If an actual 2k-th moment is bounded by `H D^(k+lambda+epsilon)` at `H=D^h`, exact prime extraction yields the conditional exponent

\[
 \frac12+\frac{\lambda+5h/6}{2k}.
\]

At row length near D, a fourth moment with lambda<2/3 already improves numerically on 7/8. Lambda=1/2 would give 5/6; lambda=0 gives 17/24. For an unbounded sequence of orders, `(lambda_k+h_k)/k -> 0` suffices for the critical-line conclusion. Perfect moments at every order are not logically required.

These are implications, not achieved new zero-free theorems.

## Contents

- [PROOF.md](PROOF.md): exact kernel identities; positivity; sharp mass asymptotic; all-order reversible norm transfer; a moving-exclusion adapter; a synthetic-phase countermodel to an invalid shortcut.
- [MOMENT_FRONTIER.md](MOMENT_FRONTIER.md): defect-aware extraction, all-scale Mellin nonvanishing, and the weakened hierarchy criterion.
- [checks/check_all_order.py](checks/check_all_order.py): standard-library exact algebra checker with an explicit `--check` mode.
- [results/exact_checks.json](results/exact_checks.json): the reconstructed finite result.
- [VALIDATION.md](VALIDATION.md): executed scope and limitations.
- [PROVENANCE.json](PROVENANCE.json): frozen parent and inspected source identities.

The analytic proofs use elementary ideal counting in the Eisenstein lattice. The final extraction uses the classical fixed-field prime ideal theorem, as does the pinned predecessor. No use of an unverified higher-moment theorem is hidden in the collision-removal proof.

## Smallest remaining gap

For every required smooth test and all `1/b <= X_i <= D`, bound the literal complete-row mean square of the fixed-S collision-free polynomial by

    H * product(X_i) * D^(lambda+epsilon),       H=D^h,

with a useful lambda and then with sublinear defects at unbounded orders. The all-order algebraic adapter is supplied; this genuinely arithmetic off-diagonal estimate remains open.

## Publication

This folder is an add-only contribution. It neither changes main nor promotes prior draft claims into the integrated record. See the enclosing delivery's `PUBLICATION.md` for the actual push status; a planned branch name is not a remote publication receipt.
