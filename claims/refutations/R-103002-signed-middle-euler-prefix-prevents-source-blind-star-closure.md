# R-103002 — The signed middle Euler prefix prevents source-blind star closure

Claim ID: `R-103002`  
Status: **EXACT HYPOTHESIS-MATCHING REFUTATION OF THE OVERSTRONG STAR CONCLUSION**  
Created: 2026-08-25  
Applies to: the conclusion of `L-103005` and the star-closed implication in `T-103020`  
RH status: **unproved**

The kernel theorems `L-103000--L-103004` are correct. The star potential in `L-103005` is also zero-sum and monotone. The attempted conclusion that the **complete** radial star current is pointwise one-sided omitted a signed source factor.

PR #730 gives

\[
C_i-C_j
=(x_j-x_i)H^{(1)}_{ij}
-(x_j^2-x_i^2)H^{(2)}_{ij},
\]

where

\[
H^{(1)}_{ij}
=
\int_0^1
\prod_{k\ne i,j}(1-tx_k)\,dt.
\]

This is not a positive source measure.

With one remaining middle label `k`,

\[
\boxed{
H^{(1)}_{ij}=1-\frac12x_k.
}
\tag{R-103002.1}
\]

The singleton middle coefficient is negative.

Take an endpoint pair `i<j` on a physical region where the common-mother Wronskian satisfies

\[
\mathcal W_{p_i,p_j}<0.
\]

The root term of (R-103002.1) preserves that sign, but the literal singleton term contributes

\[
-\frac12x_k\mathcal W_{p_i,p_j},
\]

which has the opposite sign after the declared shift is realized. Thus the same order-concordant endpoint edge contributes both physical orientations across the complete middle-prefix source.

Therefore

\[
\boxed{
\text{monotone star coefficient}
+
\text{TP2 endpoint kernel}
\not\Longrightarrow
\text{one-sided complete star packet}
}
\]

without an estimate for the signed middle Euler prefix.

## Surviving scope

The following remain valid:

```text
explicit two-box spline and log-concavity;
TP2 translation kernel;
derivative-companion Wronskian sign;
source Pluecker/Wronskian identity after the complete coefficient is formed;
star-potential monotonicity and gradient identity;
positive symmetric-rectangle decomposition;
positive scalar ordered-activity carrier.
```

The following are superseded:

```text
L-103005.4 as an unconditional complete-source conclusion;
T-103020's assertion that the radial star is already closed;
any implication which deletes the signed middle prefix before forming the
literal source coefficient.
```

The corrected source-typed frontier is `T-103040`.