# O-91703 — The root Hall row identity is the single surviving entry equation

Claim ID: `O-91703`  
Status: **BLOCKER LOCALIZATION / REVIEW PROTOCOL**  
Created: 2026-08-14  
Frozen construction branch: PR `#424` at `2bd4625bb2e3cf41318be5b22f6f8e8d0827fef1`  
Compared proposal: PR `#447`; independent review PR `#450`  
RH status: **unproved**

## 1. Exact equation to prove

For the finite equality row

\[
 c_X(j)=\sum_{k\le X/j}\frac{\mu(k)}{\sqrt k}Q_{X/k}(j),
 \tag{O-91703.1}
\]

construct positive post-Hall sources `c_s,c_h` and positive target-null row
bonuses `B_s,B_h` such that, coefficientwise for every literal row index `j`,

\[
 \boxed{
 c_X(j)
 =R_{s,X}(c_s)(j)+R_{h,X}(c_h)(j)+B_s(j)+B_h(j).
 }
 \tag{O-91703.2}
\]

The same source coefficients must satisfy the exact target identity and the
native row-budgeted score superordination.  No coefficient may occur in both a
raw residual and an independently retained raw child.

Equation (O-91703.2), not a scalar equality of target masses, is the remaining
root-entry gate for the direct-row route.

## 2. Proposed finite derivation

A valid proof should be one finite Fubini calculation in the following order.

1. Split `k=da` uniquely, with `d|P_61` and every prime factor of `a` at least
   `67`.
2. Assign every nontrivial rough monomial `a` to its least rough prime.
3. At each least-prime node, pair the raw arithmetic residual with its **unique**
   exact raw child.
4. Apply the exact controlled cocycle of `L-91560` pointwise in the signed
   coefficient `mu(d)/sqrt(d)`.
5. On each complete stopped one-prime leaf, apply the deterministic no-upward
   target-Hall transport.
6. Use the target-normalized component-row ordering of `L-91562` to obtain the
   positive row bonus of `L-91545`.
7. Sum only the positive residual sources and positive bonuses over mutually
   singular labeled leaves.

Every equality is finite before the stopping-line limit.  A countable limit, if
used, must be taken only after all outputs are nonnegative, by monotone
convergence.

## 3. What follows immediately

If (O-91703.2) is proved on the same frozen definitions, then:

- `L-91702` gives a coefficientwise nonnegative current row and an exact
  current-plus-child row/capacity/score identity;
- `L-91622` gives the fixed-67 target-mass packet envelope and `O(log X)`
  normalized loss;
- `L-91634` supplies the corrected one-use five-level score moat on the complete
  reset window;
- the resident endpoint consumer may then be applied, subject to its own
  independent review.

Thus the recursive physical problem no longer contains an unidentified
ordinary/detail residual inequality.  It contains one source-to-row identity.

## 4. Mandatory reconstruction checklist

A reviewer should reject the root entry unless the packet contains all of the
following in one normalization.

1. The exact equality-row formula (O-91703.1), including causal support.
2. The complete `P_61` divisor block and rough threshold `67`.
3. A unique least-prime label for every rough squarefree monomial.
4. The raw residual plus unique child identity in every row coordinate.
5. The controlled survival/hazard target, native-score and row coefficients.
6. The explicit Hall graph and exact no-upward transport.
7. Target-normalized row monotonicity on every Hall edge.
8. Explicit formulas for `c_s,c_h,B_s,B_h`.
9. Coefficientwise verification of (O-91703.2).
10. A one-use audit showing bonuses are current-only and children occur once.

Randomized Hall examples or scalar coefficient checks do not replace items
1--9.

## 5. Status

```text
scalar complement route                         REFUTED AS AN INFERENCE / R-91701
post-Hall current-plus-child theorem             EXACT / L-91702
root equality-row Hall identity                  OPEN / LOAD BEARING
fixed-67 recursion after root identity           EXACT ON RESIDENT INPUTS
review-ready unconditional RH proof              NOT YET PRESENT
Riemann Hypothesis                               UNPROVEN
```
