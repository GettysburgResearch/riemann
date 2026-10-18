# Scoped reconstruction of the growing row-Gauss Gram theorem

Reviewed `../eisenstein/GROWING_GAUSS_GRAM.md`, actual file-byte SHA256
`6953daaa8ddf829d68b28458de59025aa5d25b19db0c8486415b18a9df638e5e`.
No blocking error found at its stated projection scope. This is internal
team component review. The full sixth-power-free extension was suggested
by this reviewer from the separately reconstructed kernel in
`ACTUAL_SIXTHFREE_SECTOR.md`; it is not an independent external discovery
or acceptance. No complete mixed moment or new zeta boundary follows.

1. Distinct sixth-power-free ideal labels have nontrivial valuation
   difference modulo six at a good prime. The corresponding tame
   primitive character is nonprincipal, and a fixed supported ray
   character cannot remove this good-prime ramification. The remaining
   zero mask at primes with principal quotient phase is retained.

2. Primitive planar Poisson gives the smooth all-element bound
   `min(X,sqrt(NC))` with the explicit moving zero mask paid by its
   divisor sum. In the squarefree expansion, `theta(a^2)` need not equal
   one; only its modulus at most one is used. Splitting at
   `(U/sqrt(NC))^(1/2)` gives `sqrt(U)*(NC)^(1/4)`.

3. The squarefree diagonal density has local deleted-prime ratio
   `Q/(Q+1)`. Its square-root lattice error costs
   `sqrt(U)*sum_(Na<=sqrt(U))1/Na`, and the mask divisor sum is subpower.
   Actual diagonal normalization therefore gives the off-diagonal bound
   `U^(-1/2)K^(1/2+epsilon)`. There are O(K) ideal labels, so the stated
   Gershgorin range `K<=U^(1/3-eta)` follows.

4. On the complete sixth-power-free physical domain, a common chosen
   unit phase cancels in every Gram entry. It is correctly distinguished
   from a raw imprimitive Gauss sum that may vanish. The sixth-power-free
   expansion gives `U^(1/6)*(NC)^(5/12)` by splitting at
   `(U/sqrt(NC))^(1/6)`. The diagonal's square-root lattice error has
   summable weight `(Na)^(-3)`. Normalization and the O(K) labels give
   `U^(-5/6)K^(11/6+epsilon)`, hence `K<=U^(5/11-eta)`.

5. The actual inverse moment at length U and plain moment at length
   sqrt(U) each cost `U^(1+epsilon)`, with the source's fixed profile and
   height resources. Direct Cauchy consequently pays every bounded flat
   row probe. Applying this to all diagonally normalized columns and the
   actual orthogonal projection `V G^(-1)V*` gives projected energy
   `U^(1+epsilon)K^(1+epsilon)`. This step does not require Gauss-phase
   cancellation or a functional equation.

The result pays a polynomially growing, conditioned row-label span. It
does not show that this span contains every large singular direction;
the orthogonal complement remains unbounded. The finite convention
checker described in Section 6 was not rerun for this analytic review
and is not evidence for the infinite Gram estimate.
