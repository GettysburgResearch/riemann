# A dominated conditional retuning of the Xu–Sang comparison

**Status:** Exact rational check of a proposed conditional consequence; no significant new zero-free region or novelty is claimed. No independent review of the imported analytic work is performed.

**Sources:** Yuanda Xu and Hejian Sang, *Amplified moments and a refinement of the quasi-Riemann hypothesis*, [arXiv:2610.15291v2](https://arxiv.org/abs/2610.15291), PDF SHA-256 `e881519b3d2447ae2afee43650fac5e65a47e73fd52c236e1122823a7b64885f`, especially §6.2, Proposition 6.1, Proposition 7.1, and Lemma 8.1. Conditional dependence includes their Section 2 analytic inputs and the correctness of the cited propositions. This is not a standalone unconditional proof.

**Comparison:** Baiying Liu, [arXiv:2610.26835v1](https://arxiv.org/abs/2610.26835), claims the stronger bound `0.874886647039964...` for finite-order Hecke characters of arbitrary number fields. We have not independently verified Liu's full proof or checked literature exhaustively. The construction below is therefore already dominated by that claim and is valuable, if at all, as a reproducible check of an admissibility interface.

## Conditional statement

Assume the analytic inputs and propositions used by Xu and Sang, including their first-stage bound `B0 = 69991/80000` and the continuations of §8. Then their comparison gives zero-freeness, apart from principal poles, for finite-order Hecke L-functions over `Q(sqrt(-3))` and for Dirichlet L-functions in

    Re(s) > 262465997/300000000 = 0.874886656666666... .

This is `13/300000000` to the left of their printed `B1`, but to the right of Liu's claimed region above. We have not established its priority or significance. The proof inherits all prerequisites, quantifiers, uniformity and family transfer from the cited source and does not certify those prerequisites.

## Parameter verification

Fix

    kappa = 29991/40000, b = 17307/200000,
    ell = 4178001/25000000,
    g = 1/10^9, zeta = 1/10^11, g_star = 1/10^10.

With the definitions in Xu–Sang equations (10), (21), (28) and (29), `check.py` verifies every item in their §6.2 admissibility list using exact rational arithmetic. The prior bound licenses the moment because `(1+kappa)/2 = B0`. Their propositions imply the stated conditional consequence if their hypotheses hold.

For the continuum endpoint, write `J` and `E` as in (21) and (28), and set `y=1/2-x`. On the specified domain `J>0`: `alpha-delta >= 0`, `delta>0`, and both `D` and `P` are positive. The script forms the polynomial identity

    J(-E-g) = A(y) delta^2 + B(y) delta + C(y).

Every coefficient of `A(y)` and of `4 A(y) C(y) - B(y)^2` is positive. For `y>=0`, completing the square proves `J(-E-g)>0` for every real delta, and hence the required endpoint inequality throughout the entire rectangle. This is not a sampled-grid argument. All other conditions are rational comparisons.

**What was run:** `python research/exploratory/xu_sang_retuning/check.py` using Python 3 and SymPy 1.14.0; all assertions passed and the script printed the exact boundary and improvement.

**Smallest remaining gap:** An independent reviewer should check the formulas and every condition against the pinned source, including the logical use of the first-stage result. No checker here validates Xu–Sang's analytic propositions or Liu's later theorem.
