# All orders, the complete native family, and the actual critical-line gap

**Status: PROPOSED source-qualified component proofs. No RH proof, no new global
zero-free boundary, and no independently accepted theorem. NOT PUSHED in this
execution.** The all-order calculation is useful, but the diagonal-power native
hierarchy requested by the user has not been established.

## Read first

1. **NATIVE_ALL_MOMENTS.md** proves a full all-order coefficient-family bound,
   without a Mellin-twist average. For the sextic family it is

       M_2k(X,H) << (HX)^epsilon [H X^k + H^(1/6)X^(2k)
                         + H^(5/6)X^(4k/3) + H^(1/3)X^(11k/6)].

   All rows, ideal tuples, conjugate primes, product columns and divisibility
   masks are included. It yields complete diagonal order H X^k for H>=X^(2k),
   explicitly paying a row-height exponent that grows with k. The common coefficient array may be native Mobius.
   The price is displayed rather than hidden: at fixed H=X^h, the excess above
   H X^k grows like k. No critical bound follows.

2. **ALL_NUMERATOR_MOMENTS.md** gives every fixed even order and every fixed
   interior real line for all character orders n>=3, with an analytic-conductor
   form and an explicit piecewise exponent. The complete AFE and its actual
   primitive conductor are retained. For every n>=3, orders 2r>=8 saturate at

       K_n,r(sigma)=max(1+r(1-2sigma)_+, r(1-sigma)).

   Thus the method's U-sized numerator moments occur at sigma>=1-1/r, moving
   toward ONE as r increases, not toward one half. These are numerator L-value
   moments, not native reciprocal coefficient moments. The central specialization
   at n=6 overlaps #968; no claim is made to have first discovered the general
   AFE/powering/large-sieve method.

3. **CRITICAL_ROUTE.md** proves the exact sufficiency theorem: an unbounded
   sequence of fixed native orders with excess e_k=o(k) and row exponent h=o(k)
   would imply critical-line zero exclusion. In particular a SINGLE fixed extra
   power X^C in M_2k<<H X^(k+C+epsilon) suffices along all those orders.
   Constants need not be uniform in k. This arithmetic bound remains OPEN.

   The same note gives the exact native product sign and a source-specific
   restricted quadratic-form target. A separate 8/9 number is only the floor
   of a specified symmetric POSITIVE upper-estimate model, not a new zero-free
   theorem. It explains why these numerator estimates alone do not complete RH.
   The distinct free-Mellin/first-finite-part alternatives in #962/#974 are
   credited, with their missing signed projections still explicit.

## Scope of what was accomplished

This pass derives complete general bounds and tests whether a full hierarchy
closes the problem. It does not achieve the requested critical-line theorem.
The full native bound is a direct general corollary of the stated DF sieve;
its methods are classical, and no exhaustive literature-priority claim is made.
The pointwise / family / numerator / inverse / cumulative / growing-order
quantifiers must not be interchanged. Taking absolute values in the sieve step
still loses exactly the native signed information needed by the critical target.

## Verification

Run `python replay.py` in this directory. It verifies the byte manifest, normal
and optimized exact reports, and nine separately executed corrupted scripts.
The finite arithmetic fixture uses ALL 54 nonzero Eisenstein elements of norm
at most 13 and ALL five good squarefree ideal columns of norm at most 13, through
moment order 16. A separate complete ideal census runs through norm 256.
No actual L-values, infinite theta sum, zero population or asymptotic fit occurs.

The same author wrote the proofs and code. There is no independent referee,
formal proof build, full upstream sieve reconstruction or remote CI result.
See SOURCES.md and VALIDATION.md for the exact reading and execution boundaries.
