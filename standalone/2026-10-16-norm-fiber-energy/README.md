# Unconditional native norm-collision and sparse-gap sectors

**Status: PROPOSED unconditional component mathematics; complete proofs, no
independent mathematical review. Not a full moment or a new zero-free bound.**

This continuation moves from a criterion for the unknown full covariance to
an actual upper bound for a specified part of it. It also preserves the
preceding unpushed ramified-dilation packet unchanged in the sibling directory.
Nothing in this bundle has been published to a new remote branch in this pass.

## The principal result

Fix a number field F, a fixed moment order 2k, one bounded compact column test
W (or the literal Gaussian of the Dedekind source), and any finite physical
row measure of mass Z. Keep the actual Mobius coefficients, sextic phases,
prime exclusions and nonunit zeros. The coupled, two-channel and geometric
completions are also covered, uniformly in their auxiliary integer degree m>=2.

Expand the original moment into ordered pairs of k-tuples of ideals. Let
N and M be the products of the rational norms on its two sides. Then the
sum of the ABSOLUTE VALUES of all terms with |N-M|<=R obeys

    S_R(X) <= C_(F,W,k) (2R+1) Z X^k
                                (1+log X)^(kappa k^2),   X>=1, R>=0.

Here R is an integer and kappa is the number of field factors in F tensor_Q F.
For the Eisenstein field kappa=2; for Q it is 1. Consequently every subpower
window R(X)=X^o(1), including exp(sqrt(log(2X))), has the required diagonal
POWER bound O_epsilon(Z X^(k+epsilon)). The implied constants are fixed-field
and fixed-order constants; no uniform growing-k conclusion is claimed.

This is a theorem about the original FIXED column scale, not just a Gaussian
scale average or an independent-prime reference. It includes ALL ideals and
all tuples satisfying the relation, not a selected prime semigroup. The
equal-norm relation can contain nonprincipal characters and rough singleton
primes: THEOREM.md Section 7 gives a literal conjugate-prime example.

For the Gaussian cumulative critical energy, the equal-product-norm block
has the stronger normalized form O(Z(1+log D)^(kappa k^2)). Its complete
higher-order pair kernel and correct dX/X^(k+1) normalization are derived.

## A signed arithmetic asymptotic, not only an upper bound

At order two with the principal scalar source, the COMPLETE equal-rational-
norm block is asymptotic to a positive explicit constant times (log D)^kappa.
For a nontrivial field its distinct-ideal cross subtotal has that same main
term, since the literal ideal diagonal is only O(log D). In particular, for
native Mobius over Q(omega),

    same-norm signed cross-ideal energy ~ C_E (log D)^2, C_E>0.

EXAMPLES.md displays the convergent Euler product for C_E. Individual fibers
can still have negative cross interference; an exact norm-49 coupled example
is included as a negative control. No assertion about the sign of the full
unequal-norm covariance follows.

## Why this remains short of the full problem

The dense pairs of distinct product norms outside the selected window remain
unbounded at the required strength. The new theorem does not control that
remainder, the theta comparison residual, or the complete signed injection
minus compensation. No native full 2k-th moment exponent or zeta zero-free
boundary improves. The logarithmic exponent is a safe upper bound, not an
optimal higher-order matching exponent.

This is a bounded unconditional advance, not a claimed breakthrough on RH.
The Euler-product/permutation-character and Tauberian methods are classical.
Their exact field invariant is credited to the literature, and the result
is not claimed to be the first of its kind outside this repository.

## Reading and reproduction

Read THEOREM.md (NF1, NF1b, NF1c, NF2, NF3), then EXAMPLES.md, SOURCES.md and
VALIDATION.md. The proofs have no unproved RH/GRH or native moment premise.

```sh
python check_manifest.py
python verify.py > /tmp/norm-fiber-checks.json
cmp CHECKS.json /tmp/norm-fiber-checks.json
python -O verify.py > /tmp/norm-fiber-checks-O.json
cmp CHECKS.json /tmp/norm-fiber-checks-O.json
python run_mutations.py
python numerical_kernel.py
```

The first two scripts use the standard library. Numerical kernel diagnostics
require mpmath; they use ordinary 65-digit arithmetic, not directed intervals.
The exact report has 34,361 predicates, including repeated setup and prefix
checks. Five actual optimized-Python mutant processes are rejected. Three
finite Gaussian quadratures check the derived pair kernel at orders 2,4,6.
These checks are not proofs of an infinite asymptotic or independent review.

Publication status, exact source refs and recovery details are in
RECOVERY_AND_PUBLICATION.md. The outer bundle includes an add-only patch and
APPLY.md for the frozen #950 base. No existing integrated record is changed.
