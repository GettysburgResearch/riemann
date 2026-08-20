# L-102007 — Adaptive squaring at the collar threshold bounds the unsquared multiplicative depth

Claim ID: `L-102007`  
Status: **PROVED EXACT COMBINATORIAL REDUCTION; FINAL SIGN ESTIMATE OPEN**  
Created: 2026-08-21  
Depends on: `L-102005--L-102006`; PR #691 `L-100600--L-100603`  
RH status: **not assumed**

Fix one double-owner collar with endpoint primes `p_i<p_j` and physical endpoint `X`. Put

\[
T={X\over p_ip_j}.
\]

By `L-102005`, only interior subset products `m_S>T` can contribute to the centered residual.

Choose the source-side squaring cutoff

\[
\boxed{Z=T^{1/2}.}
\tag{L-102007.1}
\]

Square every interior prime `q<=Z` before physical collapse, using the exact source-faithful completion identity of PR #691. Every unsquared interior prime then satisfies `q>Z`.

If an active residual monomial contains three unsquared primes `q_1,q_2,q_3>Z`, then

\[
q_1q_2q_3>Z^3=T^{3/2}>T.
\]

Thus every depth-three unsquared monomial automatically lies beyond the collar threshold. More generally, if

\[
Z=T^{1/r},
\]

then every monomial with `r+1` unsquared labels automatically exceeds `T`.

For the square-root choice (L-102007.1), the centered collar decomposes exactly into:

```text
squared small-prime core;
unsquared depth 0;
unsquared depth 1;
unsquared depth 2;
unsquared depth >=3, all automatically in the large-product tail.
```

The first three sectors are finite explicit endpoint packets. The depth-`>=3` sector carries at least three unsquared factors and may be charged against the threshold itself.

## Important limitation

This is a depth reduction, not a sign theorem. The depth-`>=3` sector is not absolutely small merely because it lies beyond the threshold: its coefficient count still grows. A valid closure must combine the threshold charge with the joint min--max survival weight and the squared-core owner mass before absolute values.

The lemma's purpose is to reduce the final collar analysis to finitely many explicit unsquared depths plus one threshold-charged tail.