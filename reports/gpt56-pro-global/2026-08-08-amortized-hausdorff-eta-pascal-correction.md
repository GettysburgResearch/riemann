# Amortized correction to the triangular eta–Pascal proposal

Agent: `gpt56-pro-global`  
Date: 2026-08-08  
Issue: #298  
Status: **CORRECTED FULL PROPOSAL PENDING ADVERSARIAL REVIEW; RH UNVERIFIED**

## 1. Self-audit result

The first version of PR #301 assigned the strict eta factor

\[
\theta_*<2/3
\]

to every boundary jet by tensoring the scalar eta pair with one identical internal label.  The actual shifted and unshifted first-omitted legs can carry unequal values.  The literal tensor proof is therefore too strong at that scope.

The uniform arbitrary-label boundary contraction is withdrawn in `R-29802`.

## 2. Correct source property

The source values are not arbitrary.  After the positive stopped-power resolution they are pure-power finite differences and exact Euler remainders.

For

\[
v_j=(x+jh)^{-s},
\]

there is a positive Hausdorff moment representation

\[
v_j=\int_0^1y^j\,d\nu(y).
\]

Consequently

\[
\Delta^mv_j=\int_0^1y^j(1-y)^m\,d\nu(y)
\]

and

\[
R_K^{(m)}
=\int_0^1{y^K(1-y)^m\over1+y}\,d\nu(y)
\]

are positive and decreasing in the quotient index.

Thus, on the common paired tail, the shifted-even source value dominates the unshifted-odd source value.

## 3. Amortized eta/Pascal invariant

For one pair let

\[
M={V_e\over2k},
\qquad
T={V_o\over2k+1},
\qquad V_e\ge V_o\ge0.
\]

Then `T<=M` and

\[
Me_{2k}-Te_{2k+1}
=(M-T)e_{2k}+T(e_{2k}-e_{2k+1}).
\]

The second term is the exact balanced sibling switch.  Its cost is

\[
T\log((2k+1)/(2k)).
\]

Hence

\[
(M-T)+T\log((2k+1)/(2k))\le M.
\]

So one incoming source unit pays both:

- its residual lower-scale boundary source;
- its complete Pascal objective cost.

The boundary state need not contract by a fixed factor.  It has a conserved amortized budget.

## 4. Global recurrence

Let `J_a` be boundary source mass, `C_a` paid Pascal cost, and `I_a` new analytic/collar injection.  Then

\[
J_{a+1}+C_a\le J_a+I_a.
\]

Therefore

\[
J_A+\sum_{a<A}C_a
\le J_0+\sum_{a<A}I_a.
\]

The analytic bulk still contracts strictly:

\[
A_{a+1}\le(6/7)A_a.
\]

Its total boundary injection is summable, while the explicit unmatched first-omitted collar is polylogarithmic at each of only `O(log X)` half-scale levels.  Hence

\[
J_A+\sum C_a=O(\log^B X).
\]

This supplies the exact quantity needed by the Cycle-Debt consumer on PR #272.

## 5. Corrected full chain

```text
positive stopped-power resolution
-> 6/7 analytic bulk contraction
-> Hausdorff-decreasing jets and exact remainders
-> amortized capacity-feasible eta/Pascal payment
-> polylog total boundary source + objective cost
-> Dyadic Commutator Debt
-> factor-1/2 Cycle Debt recurrence
-> sharp complete prime-power ramp
-> square-screw/Landau
-> RH.
```

The corrected theorem is `T-29802`.

## 6. Remaining adversarial hinge

Reviewers must reconstruct the actual finite source manifest and verify:

1. the common tail is paired with shifted-even argument smaller than unshifted-odd argument;
2. all unmatched initial terms are retained in the declared collar;
3. every paired dipole is one of the balanced Pascal currents in the debt metric;
4. repeated destinations are recombined before capacity is charged;
5. no boundary row regenerates current-scale analytic bulk.

One exact counterexample rejects the proposal.

## 7. Exact regression

The new standard-library checker verifies 24,576 rational shifted-jet pairs and the residual-plus-cost inequality.  Retained classification:

```text
EXACT_HAUSDORFF_PASCAL_AMORTIZED_BUDGET_VERIFIED
```

Digest:

```text
23f5fd5b6b1e89d413489e6630b232412baac6ad3c56a7b291f2bbeafd1a26e2
```

The checker does not certify the complete source manifest or RH.
