# T-97700 - `BLPTE67` is the exact large-prime theorem sufficient for RH

Claim ID: `T-97700`  
Status: **UNCONDITIONAL REDUCTION; ONE SIGNED TYPE-II ESTIMATE OPEN**  
Created: 2026-08-18  
Inputs: `R-97700`, `L-97700`, `L-97701`, PR #547's annular Mellin-Landau consumer  
RH status: **unproved**

The PR #578 small-prime theorem is valid, but its complementary assertion
`LAPBR67` is false by `R-97700`. The corrected chain uses the complete
small-prime cube and the exact largest-prime Bellman identity.

At an admissible state, let `U_Z` be the complete small-prime cube, and let
`mathfrak I_Z`, `mathfrak T_Z` be the Type-I/Type-II terms of `L-97701`. Then

\[
 U_{\rm full}(X)=U_Z(X)-\mathfrak I_Z(X)-\mathfrak T_Z(X).
\]

If `BLPTE67` holds at every state, this identity gives

\[
 U_{\rm full}(X)\ge0.
\]

The child endpoints in every Bellman term are strictly smaller, so the argument
is a finite induction on endpoint/rank; the finitely many initial endpoints are
checked directly.

At the root this is eventual nonnegativity of

\[
 \mathcal A_X=
 5[c_X(2)-c_{X/4}(2)]+3[c_X(3)-c_{X/4}(3)].
\]

Its exact Mellin transform is

\[
 (1-4^{-s})\left[
 \frac6{s^2}-
 \frac{3(1-2^{-z})(2-2^{-z})}{s^2\zeta(z)}
 \right],
 \qquad z=s+\frac12.
\]

The annular factor is nonzero for `Re s>0`, and the finite numerator has no zero
for `Re z>0`. Landau's theorem therefore gives

\[
 \boxed{\mathrm{BLPTE67}\Longrightarrow\mathrm{RH}.}
\]

## Exact boundary

```text
PR #578 adaptive small-prime cube            RETAINED
LAPBR67 residual nonnegativity                FALSE
complete small-prime cube                     PROVED POSITIVE
largest-prime Bellman identity                PROVED EXACT
terminal one-large-prime Type I               CLOSED
balanced signed Type II BLPTE67               OPEN / RH-BEARING
BLPTE67 -> annular scalar positivity -> RH    PROVED CONDITIONAL
Riemann Hypothesis                            UNPROVED
```
