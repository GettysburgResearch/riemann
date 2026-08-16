# Upstream spine reconstruction after PR #494

PR #494's one-shot closing implementation is frozen. This successor reconstructs the upstream Hall/profile, positive whole-cell endpoint measure, explicit martingale quantizer, all-column/terminal reserve, native `Y_4` cost, prime-square drift and Mellin–Landau endpoint chain.

The principal simplifications are:

1. whole cells remove activation collars and partial-cell ownership;
2. actual child responses stay internal, so no full-child capacity is reserved;
3. every auxiliary Schur demand is zero because no state completion is used;
4. Chebyshev plus Stieltjes integration improves the thinning cost below `6006` and the complete native deficit below `55000`;
5. the prime-square step needs only a positive limiting constant, and the explicit interval `1/sqrt(2)<u<1` gives `C_square>1/10`, avoiding any dependency on evaluating `zeta(1/2)`.

PRs #508/#509 were inspected as possible stronger producers. Shared ancestry is not treated as confirmation, and no claim from either is normative here. RH remains unproved pending hostile reconstruction of `T-92911`.
