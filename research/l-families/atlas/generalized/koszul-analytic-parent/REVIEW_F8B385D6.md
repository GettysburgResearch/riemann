# Independent review of the critical Koszul boundary checkpoint

Reviewed scientific commit: `f8b385d69c8b5eea13ef7f474a23835bf0dbbd2f`.
Review date: 2026-08-31. Reviewer: independent `recent_landscape` agent.

Result: no mathematical or source/code blocker found in the stated scope.
This is an independent reading of the proof, producer, tests and replay
contract, not a claim that this reviewer executed the suite or formally
verified the mathematics. All computational jobs were reserved for the
root agent to respect the shared machine's memory limit.

## Exact scope inspected

The five added files under
`research/l-families/atlas/generalized/koszul-analytic-parent/` are
`CRITICAL_GRADE_BOUNDARY.md`, `CRITICAL_BOUNDARY_REPLAY.md`,
`critical_boundary_replay.py`, `tests/test_critical_boundary.py` and
`critical_boundary.verification.json`. The bound proof's LF SHA-256 is
`6d83c759a177d85d6f64c8f64e8ffcb9527416c187191bd37d4959d9df240216`.
The producer authenticates the previous scientific checkpoint
`4499c6e44d425b6e43fbf004f2750123a9b20c31` before importing its code.
That dependency chain remains a substantive part of this result.

## Mathematical checks

* The strengthened estimate `epsilon_n rho^n=1/n+O(theta^n)` follows
  from the unique largest reciprocal Hilbert root and the previously
  bounded proper-divisor terms. Finite exceptional initial grades do not
  affect the tail estimate. This statement is only used on the declared
  nonexceptional rank profiles.
* For every unitary input at `|t|=rho^(1/p)`, the singular values really
  occur in intrinsic grade blocks with multiplicity `epsilon_n`. The
  derivation `J_n~R^(n+1)/((R-1)n)` is sufficient for both endpoints.
  In particular the two constants are respectively
  `log(R)/(R-1)` and `R log(R)/(R-1)`: replacing them by a single
  asymptotic equivalent would be false. The proof retains the oscillation.
* The additive constant in the singular-power partial sum is correctly
  `gamma+sum(e_n)-log(log R)`. A partial terminal block contributes
  `O(1/n)`, so the statement holds for every growing cutoff, not just
  grade endpoints. With the explicitly given sequence definition the
  Schatten--Lorentz condition is exactly `q>p`, including the weak
  endpoint; membership in the vanishing weak class does not imply
  membership in `S_p`.
* At identity input the sign in the leading logarithmic series is
  `(-1)^(n+1) z^n/n`. The remainder is holomorphic on a neighborhood
  of the closed unit disk: the two requirements `eta theta<1` and
  `eta^2<R` control its two pieces. This proves arc convergence away
  from `z=-1`, with the source grading and order retained explicitly.
* At the exceptional point the leading series is `-H_N`. Consequently
  the factor is `N`, and the limit is
  `exp(-gamma) rho F'_1(-rho)`, with no missing sign or factor of rho.
  The derivative is positive by the simple ordered root factorization.
  For `(2,3)` this is `16 exp(-gamma)/81`.
* Scalar phase twists rotate the exceptional point as stated. The
  manuscript correctly does not extend this identity/scalar-phase proof
  to an arbitrary nonscalar tuple. It does not call the boundary product
  an ordinary Fredholm determinant, assert reordering invariance, or
  equate the separately divergent even/odd factors with convergent
  ordinary determinants.

## Exact replay and adversarial reading

The singular-value controls keep integer multiplicities compressed and
do not allocate a list of repeated states. The bounds on ranks, grade
cutoffs, logarithm terms and Gaussian powers are enforced without Python
`assert`. The source recurrence used for these multiplicities comes from
the frozen predecessor rather than a fitted table in this fixture.

The rational logarithm implementation has the stated atanh remainder,
correct signed range reduction, and outward floor/ceiling rounding. For
the boundary blocks it multiplies the raw interval by the full integer
multiplicity before rounding, which is essential at the large final
grades. The strip error estimate and its geometric grouping yield the
displayed `delta_N`; the Gaussian-rational arc check uses the squared
norm and `b/(1-b)` only when `b<1`. The exceptional point is explicitly
rejected by that arc route and has its own rate control.

The finite logarithm-versus-tail checks test compatibility of rigorous
intervals with the proved error bound. They are not being treated as a
machine proof of the infinite convergence theorem. The actual complex
arc products are independently formed from the finite grade factors and
compared with the exact scalar rational function; the extra phase
`3/5+4i/5` is a useful held-out check.

I read all 16 tests, including invalid rational/boolean inputs, caps,
negative rounding, source authentication and counterfeit fixture refusal.
Full-payload canonical JSON comparisons preserve the distinction between
integer values and booleans/floats. No test was run by this reviewer.

## Execution evidence and limits

The root/writer reported a successful serialized Ruff check, producer
write/check, optimized producer check, and 16 ordinary plus 16 optimized
tests, including the final proof/contract fixture regeneration. Those
are root-reported execution results, separate from this independent
source review.

The finite controls illustrate three identity rank strips and named
phases; they do not establish the all-rank asymptotic or convergence
theorems by sampling. The source construction and the earlier Koszul/PBW
and root theorems remain imported dependencies. The present estimates
are classical operator/series deductions from that source; this review
does not establish external novelty. No integer prime source, global
arithmetic completion, RH/GRH implication, or nonzero singular trace is
obtained here. Later nonscalar extensions require their own review.
