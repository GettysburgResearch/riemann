# Rebuilt angular all-order packet after interrupted run (2026-10-18)

**Status:** proposed complete elementary component proofs; independent mathematical review required. **No RH/GRH proof, critical principal-character estimate, or improved zero-free boundary.** This is a newly reconstructed, deliberately scoped packet, NOT a byte-for-byte recovery of the interrupted workspace. The crashed session's actual unpublished file bytes were unavailable.

Stacked directly on [#972](https://github.com/GettysburgResearch/riemann/pull/972). This is **different from #976**: #976 studies CT theta moments; here the objects are actual ideal angular moments of the original signed Mobius source.

## Main results

1. **Every fixed imaginary quadratic field, sharp angular second mean:** for a fixed rationally saturated exclusion set S containing all ramified primes and a unitary infinite-order angular Hecke character Psi, the literal ideal Mobius source obeys
   `sum_l p_R(l-l0) |sum_(X/2<NI<=X) mu_K^S(I) (NI)^(it) Psi(I)^l|^2 <<_(K,S) (1+|t|)^2 X(1+X/R)`.
   Its **full Gaussian** satisfies the critical energy estimate
   `sum_l p_R(l-l0) integral_0^D |A_l^c(X;t)|^2 dX/X^2 <<_(K,S,c) (1+|t|)^2(log(3+D)+D/R)`.
   Thus R=D gives O(log D) with radial t=0 fixed. No principal angular member is isolated. For class number >1, the proof controls different classes separately; it does NOT assert an exact global ray-diagonal identity.

2. **Every fixed even order and every fixed number of independently capped columns:** if each column has divisor-bounded ideal coefficients and all share the SAME angular parameter, with upper norm caps X_1,...,X_k and T=product X_i, then
   `sum_l p_R(l-l0)|prod_i A_i(l;X_i)|^2 <<_(K,k,epsilon) T^(1+epsilon)(1+T/R)`.
   This includes `2k` moments of Mobius and arbitrary fixed polynomial phases in each norm, uniformly in the phase coefficients, and all fixed-length coupled numerator/reciprocal-product Dirichlet coefficients sharing the same angular twist. Full Gaussian bands and their cross terms are retained. This is a divisor-count theorem and does **not** improve the RH-bearing principal source.

3. **Exact higher-moment signs:** for the k-fold native Mobius column with original cuts, every coefficient is `lambda_K(I) c_k(I)` with `c_k(I)>=0` the ACTUAL number of admissible squarefree ordered ideal factorizations. Writing I=(a)J with J rational-primitive gives the precise signed ray coefficient
   `B_J=lambda_K(J) sum_a chi_D(a)c_k((a)J)`.
   Unlike order 2, one may NOT restrict (a,NJ)=1. Over Eisenstein integers the sign of a pair of primitive rays equals `lambda(T_trace^2+3h_det^2)`. The remaining cross-ray sum is a genuine polynomial-Liouville correlation, not controlled by polynomial exponential-sum orthogonality.

4. **Sharpness and no free extraction:** for K=Q(sqrt(-3)), the averaged `2k`-moment at R>=C_k X^k is >=c_k X^k/(log X)^k for large X. Positivity extraction of l=0 from the upper bound costs p_R(0)^(-1) asymptotic to R and yields at best X^(1+epsilon), even after taking arbitrarily large fixed k. This formalizes the failure of a naive all-moment-to-RH argument.

Read [PROOF.md](PROOF.md), [SIGNED_DETERMINANT.md](SIGNED_DETERMINANT.md), and [VALIDATION.md](VALIDATION.md).

**What is new relative to the inherited work:** the complete class-group adapter, all-fixed-order/rectangular angular theorem with source-faithful caps and full Gaussian tails, and the exact high-order Liouville ray formula. The k=1 Eisenstein theorem and rational-ray idea are inherited from #972; the preceding higher CT theta moments are credited to #976. These estimates are not published as a solution to RH.
