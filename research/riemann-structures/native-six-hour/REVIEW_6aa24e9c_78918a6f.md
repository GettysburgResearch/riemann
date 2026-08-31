# Review of the complete pair body and the singular limiting minor

I read both complete proof notes and checked that the reviewed working bytes agree with these freezes:

| Note | Commit | Blob |
|---|---|---|
| `NATIVE_PAIR_MOMENT_COMPLETE_BODY.md` | `6aa24e9c81c5a618ae7b740872f48266a5a86892` | `c81751156911e984a62e0664ef3a1312eab7c3bc` |
| `NATIVE_FIXED_MINOR_INFINITY_DEFECT.md` | `78918a6f3297d4c88b3b3c42140eba4c0f11778e` | `70691bb9cca63cb97b08fac1caf3f5b71bbd949c` |

No proof blocker was found. These are proof reviews, not scientific executions.

## Complete pair body

The strict concavity of the Gini functional forces every minimizing threshold law to be extreme. The four-set perturbation then bounds its support by three atoms. I checked both additional strict reductions: the fixed-weight variance ellipse excludes three interior atoms, and the full feasible interval for the middle atom of a `{0,b,c}` law excludes a boundary three-atom minimizer. The two-atom separation optimization gives the stated upper envelope and all equality cases, including the two reflected profiles at `A=1/2`, the unique constant and threshold boundary cases, and the degenerate endpoints.

The explicit interpolation between the frozen lower profile and an upper profile preserves `A,B`, realizes every intermediate `C`, and remains a single completed monotone graph. Its quadratic root and the lower-profile variational sign are correct. The final two-coordinate source statement retains the endpoint integrals `1,A,C,1,1-A,1-2B`; it does not promote this three-moment body to a higher-arity compatibility theorem or a physical-energy optimum.

Independence disclosure: I supplied algebraic checks of the upper-envelope reductions during development. I authored the earlier threshold-law and lower-envelope notes imported here, so this report is not an independent revalidation of those predecessor proofs. Another team reviewer independently reviewed those frozen predecessors. The present complete-body note was authored separately, and I read it in full.

## Singular limiting minor and quantitative degeneration

I reopened the frozen `3ba47924` local-source and coordinate formulas. The factor-two identity, determinant sign, original `1/g` alias weight, and absolutely convergent product factorization agree with the new proof. The eight selected pure-prime rows collapse to at most three dimensions, giving limiting rank at most fifteen. This leaves finite event certificates valid but rules out every honest strict uniform Neumann-tail certificate for this fixed selection, including positive reweightings and residual-controlled approximate inverses.

I independently recomputed the local coefficient norm `2+sqrt(2)`, the three-prime norm `S=(2+sqrt(2))^3`, and the source curvature bound `18 S^2`. The resulting matrix tail bound `L/sqrt(H)`, five small singular values, determinant upper bound of order `H^(-5/2)`, and inverse lower bound of order `sqrt(H)` follow with the displayed constants. No matching rate or exact limiting rank is asserted.

Section 5's algebraic comparison estimates and positive-diagonal-weighting argument are correct conditional on its explicitly designated exact-rational checks of the stored artifact. I did not execute those checks or independently verify their numerical premises. Sections 2–4 and the quantitative rate do not depend on that diagnostic record. Infinite full-source faithfulness, the original physical-energy problem, and the full retained-gamma interface remain separate.
