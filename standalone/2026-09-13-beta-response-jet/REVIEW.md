# Independent-review handoff — BJR26

Status: proposed components, no RH proof. Review the exact new files, not the live title alone.

## Main analytic dependencies

The parent #876 provides the literal fixed laws, third-order scale ordering, response construction, and Brownian endpoint normalization. #878 provides source density and Laguerre conventions. Both remain proposed paper mathematics here. We have read their full supplied manuscripts; this does not retroactively accept every parent argument.

## Load-bearing checks

1. **Weighted operator.** Verify the shared-uniform exponent `u^10/(u^2+x)^8`, the beta identity with tilted shapes `(11/2,5/2)`, the two square-root bounds, and the complete rational numerator of `2/3-B(x)`. The proof is all x>=0; sample evaluations are not its justification.
2. **Mellin response.** The remainder is a positive MEASURE, not just a nonnegative Laplace function inferred without a measure representation. Check its source convolution and the real inverse-moment bound before complex absolute values. Distinguish this positive truncation from the signed finite-tree comparison, which explicitly retains `1/|Gamma(-p)|`.
3. **Parameter analyticity.** Check the Banach norm, quadratic map constants, complex ball invariance, and identification of the holomorphic solution with the real source. Complex extensions are not probability laws. Check the nonvanishing normalization denominator at s=1.
4. **Finite C1 approximation.** Reconstruct both forcing-error terms and their signs before absolute values. The gamma seed is fixed in theta; every scale node's derivative is retained. The geometric result is a finite-tree error bound, not a claim of efficient tree enumeration.
5. **Endpoint density derivative.** Check the reversible beta–gamma Markov operator, exclusion of the constant/mean/variance modes, its Laguerre eigenvalues, and L2 integrability of the one-step forcing. This justifies the derivative series without differentiating an unknown tail in the parent series.
6. **Exact series tail.** Check the convolution split, `23/4`, `2047/11`, the binomial tail sum and decreasing Pochhammer factor. The center parameter is EXACTLY theta=0; no all-theta version of this special tail is asserted.
7. **Native local zero.** The gamma phase bracket counts a zero of H_0, not xi. Validate the complete interval for the phase derivative and response on that bracket; verify the sign in `t'(0)=-Im R/phi'`. Symmetry and the analytic implicit function theorem give an unevaluated local interval, not a tested all-parameter tube.

## Attempts that must not be promoted

The operator positivity does not give a sign to its oscillatory Mellin transform. The two complex logarithmic amplitude signs are not collision signs. The positive simple-zero velocity is not a double-zero birth/death calculation. No bound on the total nonreal-zero functional is obtained. No proposed all-height statement has been delegated to a reviewer as routine.

## Code and execution questions

The primitive code is adapted from the earlier #853 backend; normal/optimized runs and the two series degrees do not constitute implementation independence. Check the Bernoulli-integral Gamma remainder at Re(z)>=64, all interval rounding directions, strict parser types, the source-independent raw-moment coefficient checks, and the controlling test exit status. The suite contains ten actual altered-receipt CLI calls, not ten full copies of the analytical proof.

Source files and execution scope are recorded in SOURCES.json and VALIDATION.md. A repository-wide build and the parent numerical suites were not run. No independent acceptance or formal proof is claimed.
