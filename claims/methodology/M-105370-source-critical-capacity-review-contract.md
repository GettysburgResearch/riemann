# M-105370 — Hostile review contract for source–critical capacity

Claim ID: `M-105370`  
Status: **REVIEW PROTOCOL**  
Created: 2026-08-23  
Normative theorem: `T-105371`  
RH status: **unproved**

## Normative files

The first drafts `L-105371` and `T-105370` contain malformed display
delimiters and are non-normative. Review only

```text
L-105370  source = critical atoms + boundary reserve
L-105372  corrected Christoffel capacity normal form
T-105371  corrected conclusion frontier
```

for scientific conclusions.

## Required review order

1. For odd `F`, verify `a_0=1` in the germ of `F/F'`.
2. For even `F`, verify that subtracting `rho_0/z`, with
   `rho_0=F(0)/F''(0)`, leaves an analytic odd germ.
3. Recheck the paired-pole identity

   \[
   {\rho_c\over z-c}+{\rho_c\over z+c}
   ={-2\rho_c\over c^2}{z\over1-z^2/c^2}.
   \]

4. Verify coefficientwise that `a_n=beta_n+sum W_c s_c^n`.
5. Verify both matrix identities, including the factor `s_c` in the shifted
   critical block.
6. Review the pseudoinverse range condition before using any singular source
   matrix.
7. Keep the exact operator norm separate from the stronger trace lane.

## Positive-definite versus singular source matrices

The Christoffel formula with an ordinary inverse is used only when
`A_k^(a)` is positive definite. The gate `SCLC105371` includes this
positive-definiteness requirement at the order under review.

If `A_k^(a)` is singular, the sharp statement is

```text
Ran C subseteq Ran A
AND
lambda_max(A^(dagger/2) C A^(dagger/2)) <= 1.
```

No ordinary inverse may be inserted by perturbation without a separate limit
argument.

## Sharp versus sufficient conditions

```text
lambda_max(A^(-1/2) C A^(-1/2)) <= 1  EXACT
trace(A^(-1) C) <= 1                    SUFFICIENT / OVERSTRONG
trace(A^(-1) C) <= k                    NECESSARY UNDER EXACT DOMINATION
```

The trace lane can lose a factor as large as the matrix rank because distinct
critical atoms may occupy overlapping normalized feature directions.

## Xi scope

The source matrices are literal derivatives of the regularized ratio
`Xi^(r)/Xi^(r+1)` at the origin. Their positivity and conditioning are not
proved by the finite replay. Likewise, no estimate is supplied for the actual
critical weights or Christoffel leverage.

## Binding boundary

```text
source/critical/boundary split                 PROVED EXACT
pseudoinverse capacity equivalence             PROVED EXACT
Christoffel trace implication                  PROVED EXACT
source matrices positive for all Xi orders     OPEN
OSCC105371                                     OPEN
SCLC105371                                     OPEN / OVERSTRONG
CRVH105330                                     OPEN
Riemann Hypothesis                             UNPROVEN
```
