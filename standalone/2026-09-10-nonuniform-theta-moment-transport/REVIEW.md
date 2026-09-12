# Independent-review handoff

Status: PROPOSED, not accepted; no RH proof. Immediate source parent:
`bc561659684f50a6374bcd8d4afb0caf9fb65027` (PR #842).

## Load-bearing scope

**NMT1, PROOF Sections 1 and 3:** reconstruct the literal full-line theta
normalization, derivative recurrence, complete L1 order-24 error, all later
theta indices and the whole t>2 tail. Check the division by mass and variance.
The raw computation uses 128 midpoint cells of degree 23, not the earlier
Simpson rule. Verify range-reduced exponential and pi endpoints, including the
very small exponential upper allowance multiplied by high-degree polynomials.

**NMT2, Sections 2 and 4:** check all 73 spins, 2564 positive edges and the exact
1170-state multiplicity reduction. Couplings are log(q1)/2, log(q2)/2,
log(101/100)/4, and log(1001/1000)/2. The hub connects only to the core.
Check the covariance derivatives, standardized-moment derivatives, exact
rational preconditioner and whole-box row norm. Its numerical origin is not
trusted. The contraction proves existence and uniqueness ONLY within the
specified box for the actual theta target and an explicit neighboring target
box. Rounded centers are not the exact solution. All ten moments include odd
moments by exact spin flip and variance by exact normalization.

**NMT3, Section 5:** reconstruct the nonzero sign cumulants and Vandermonde
Jacobian at every fixed order. Verify that adding an overall base-observable
scale makes the low-five cumulant map invertible. The two implicit-function
steps preserve the five exact low cumulants, positive weights and couplings.
Surjectivity on the low-moment fiber requires the full-rank joint map AND an
invertible low base block; both are supplied. The connected graph after adding
r leaves has 73+r spins and 2564+r edges. This is a LOCAL neighborhood around
constructed higher moments, not a neighborhood centered on the higher theta
values. No order-uniform conditioning is proved.

**NMT4, Section 6:** the conditional closure to RH is classical Lee--Yang plus
variance domination and Hurwitz. Its source-realization premise remains OPEN.
No finite certificate or full-rank local response is substituted for it.

## What the programs authenticate

`certify.py --check` rederives the complete source, all graph sums and the
four-dimensional existence inequalities and compares the complete receipt.
Manifest verification authenticates byte identities only. It is not evidence
of mathematical truth. `test_certify.py` independently enumerates six small
individual-spin systems and reconstructs source derivatives by formal
composition, integrated polynomial errors, and finite cumulant Jacobians.
Those bounded tests do not prove the all-order local theorem.

No parent full campaign, high-order continuation, large graph enumeration
beyond the stated compressed 73-spin law, numerical zeta spectrum, full repo
validator, Lean/Comparator proof, native Windows run or remote CI result is
claimed. Same-author independent formulas are not independent referee review.

## Main remaining theorem

Construct admissible pair graphs reaching theta moments at unbounded order
(or its exact weak-limit law). An explicit chain of local certificates is one
possible strategy, but target reachability, positivity boundaries and growing
conditioning are not solved in this packet. A failure of the current graph
family would not refute RH or every other Lee--Yang realization.
