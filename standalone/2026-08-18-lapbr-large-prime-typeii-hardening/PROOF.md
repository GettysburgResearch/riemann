# The Large-Prime Parity Boundary

## A no-go for `LAPBR67` and the exact signed Type-II Bellman frontier

The adaptive small-prime cube of PR #578 is positive. The complementary
large-prime residual is not. At the published depth
`L=O(log log log X)`, the total active reciprocal-prime mass is much larger,
`~log log X`, and a product-safe elementary symmetric-sum bound makes the final odd rough layer dominate. Consequently the
full depth current is negative and the residual is more negative than the
small-prime cube is positive.

The correct architecture resums every large-prime depth. The complete
small-prime cube is positive, every nonempty remaining history is owned by its
largest prime, and the complete source is

\[
U_{\rm full}(X)=U_Z(X)-\sum_{Z<p\le X/2}\frac1pU_{<p}(X/p).
\]

The terminal one-large-prime range `p>X/Z` is negligible. The exact remaining
problem is the signed Type-II estimate

\[
\sum_{Z<p\le X/Z}\frac1p
\sum_{Z<P^-(v),\,P^+(v)<p}\frac{\mu(v)}vU_Z(X/(pv))
\le U_Z(X)-\mathfrak I_Z(X).
\]

This theorem is named `BLPTE67`. It is the sole open arithmetic estimate in the
packet. Its truth implies annular scalar positivity and then RH through the
exact Mellin-Landau consumer. RH remains unproved.
