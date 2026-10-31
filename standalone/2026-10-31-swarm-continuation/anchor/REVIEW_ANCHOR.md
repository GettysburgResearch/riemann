# Independent review of the moving-anchor follow-up

Reviewer: the Bessel/local-sign swarm lane, October 31, 2026.

Verdict: **the proposed component theorems check at their stated scopes**. The old positive-part budget is unconditionally obstructed in the claimed regime. The replacement support-window limit, complete-prime transfer, and lower-spectral-bound theorem have complete arguments. No unbounded-window positivity, RH, or improved zero-free boundary is established.

## Frozen scope

The two manuscripts and the exact checker were read in full at these SHA-256 identities:

| File | SHA-256 |
|---|---|
| `LAGUERRE_WINDOW_BRIDGE.md` | `a4400b5ef341afecdcbe2a84e050ff5f706b259822b9aeaf8edbd7aa17089fca` |
| `ANCHOR_BUDGET_OBSTRUCTION.md` | `60b317d3d85c0e71aa4004ba045ac23d7c030ec597fe94b06adf763ff9c0dd33` |
| `verify_anchor_followup.py` | `703e9fcd4cbbe722cafb7f68d4c7648092e53d472fef0dbf61b19f66ce3af7e8` |
| `ANCHOR_FOLLOWUP_CHECKS.json` | `7a479b437c29fb3140ca226b0a2997fcc70b0ac6eaed9020d85a65fe727fe1b2` |

The reviewer did not author the exponential cross-projection observation. It was supplied by the parent and anchor lane before this independent review. I independently expanded its geometric coefficients and checked its consequences below. The parent also reviewed this lane's Bessel work, so this is an internal cross-review among AI agents, not external human refereeing or proof-assistant verification.

## 1. Proportional limit and exponential weights

I independently integrated the Laguerre/exponential coefficient and summed its cross-product. The ratio in the geometric sum is `(a-b)(a-c)/((a+b)(a+c))`, and its logarithm is `-2(b+c)/a+O(a^-3)` for fixed b,c. This gives the support length **2L**, not L. Density of positive exponentials and uniform contraction extend the convergence weakly to all L2 vectors. The displayed squared-norm argument correctly upgrades it to strong convergence because the limit is an orthogonal projection. It does not assert norm convergence of finite-rank operators to an infinite-rank projection.

For the weighted estimate, the substitution `y=(2a-eta)u` gives the prefactor `q=a/(a-eta/2)`. The Laguerre dilation coefficients are `binom(n,k)q^k(1-q)^(n-k)`. The absolute column norm is exactly `(2q-1)^N`, and the infinite row-sum majorant is valid because a>eta makes 1<q<2. Multiplying the two Schur norms gives precisely the stated W, whose logarithm tends to 2*eta*L. The tail argument at any larger exponent then legitimately upgrades strong L2 convergence to every fixed exponential weight.

## 2. The whole arithmetic sum

Right translation preserves the finite Laguerre span. The tail identity
`||T_t phi||²=integral_t^infinity |phi|²` and the weighted bound give the factor `exp(-eta*t/2)*sqrt(W)`. After the prime coefficient m^(-1/2), the dominating series has exponent `(1+eta)/2>1`. Its entire von Mangoldt series converges. Both the termwise strong limits and the adjoint limits therefore pass through the complete sum using a uniform operator-norm tail.

The support-window compression vanishes for t>=2L, including equality almost everywhere. Thus only prime powers m<exp(2L) survive. The first visibility threshold is L>(log 2)/2, and the older L=1/100 family has zero limiting prime operator. The note correctly distinguishes this limiting statement from deleting primes in finite matrices.

## 3. Gamma, pole, and prime normalization

I checked the actual source formula against
`xi'/xi(s)=1/s+1/(s-1)-(log pi)/2+psi(s/2)/2+zeta'/zeta(s)`.

For A=1/2+B, the two rational semigroup integrals give
`2*cosh(t/2)*Re C_phi(t)`. Symmetrizing the double integral for
`F_+*conjugate(F_-)` gives exactly this term, without an extra factor of two.

The digamma difference at A/2 relative to 1/4, followed by the substitution of twice the integration variable, produces
`k(t)=exp(-t/2)/(1-exp(-2t))` and the constant
`kappa=psi(1/4)/2-(log pi)/2`. Testing on the normalized exponential h_b gives
`[psi(1/4+b/2)-psi(1/4)]/2`, which agrees with the scalar matrix source. The prime term is `-sum Lambda(m)m^(-1/2) Re C_phi(log m)`, also with the correct normalization. Thus the identity with q*Gq checks.

No numerical constant from an external normalization is imported by this review. In particular, I did not replay the separate recent support-length-1.6 certificate cited in the manuscript.

## 4. Compactness of moving minimizers

This is the load-bearing step beyond strong fixed-vector convergence. The Fourier multiplier
`d(tau)=integral k(t)(1-cos(tau*t))dt` is nonnegative. Its lower bound follows from k(t)>=exp(-1/2)/(2t) on (0,1] and the integration-by-parts bound for the cosine integral. The upper logarithmic bound follows from splitting at inverse frequency and at one. Hence a bounded D energy gives uniformly small Fourier tails, although only at a logarithmic rate.

For minimum-eigenvalue vectors with bounded upper energy, the exponential estimate controls every prime and both pole moments uniformly. The exact source identity therefore bounds D above and the eigenvalues below. Spatial tails are uniformly small by the exponential estimate. Spatial cutoff composed with Fourier cutoff is Hilbert–Schmidt; the two discarded tails control the approximation error. This proves strong L2 precompactness of the varying minimizers.

The limit is in the support window because `P_j phi_j=phi_j`, `phi_j->phi` strongly, and `P_j->Q` strongly. Its norm remains one. The exponential-weight upgrade controls the pole moments and supplies a summable dominating series for the full arithmetic quadratic form. D is lower semicontinuous as a nonnegative Fourier multiplier. These facts prove the claimed **liminf inequality**, not merely convergence on preselected trial vectors. No unsupported passage of an unbounded form through bare strong convergence occurs.

## 5. Prime thresholds and continuity

The truncated shift decomposes into finite chains of length at most `ceil(ell/t)` almost everywhere. The half-adjacency matrix of each chain has extreme eigenvalues `+/-cos(pi/(n+1))`. At an integral ratio ell/t, the longer chain occurs only on a measure-zero fiber and must be discarded; the stated ceiling formula does so correctly.

A newly exposed prime delay consequently has non-small operator norm even when the newly exposed interval is short. The spectral-floor continuity proof nevertheless works: bounded families of almost-minimizers have the same spatial/frequency compactness, and the bounded prime/pole forms are continuous under their strong L2 limits. Interior core approximation follows by slight contraction and translation in the logarithmic Fourier norm, then mollification. This gives the upper-semicontinuity direction as stated. It cannot propagate positivity through arbitrarily large windows without another estimate.

## 6. Absolute-budget obstruction

The trace estimate uses B_+>=B, trace invariance under the rotation, and
`tr B=(N+1)g_1`, `d g_0/d log a=g_1`. It is valid independently of the sign of the endpoint difference.

I independently expanded the alternating Fejer vector. The logarithmic-source coefficients are
`[1+(-1)^(n+1)q^n]/(4n)`, giving the claimed weighted sum. The alternating contribution is nonpositive; Bernoulli's inequality yields the harmonic loss and `(1-q)N/4`. The complete remainder contributes at most `3/19+1/19=4/19` after comparison with the actual diagonal. These constants give the stated 3/4 upper margin.

For the endpoint, the real digamma bound and negative Mangoldt sum give
`f(s)<log(s/(2pi))/2+1/(2s)+1/(s-1)`. At s=a1+1/2>=3/2, the rational terms are at most 7/3 and s/(2pi*a1)<1/4. The displayed 5/3 bound follows. Combining the two parts yields exactly 29/12 in the final inequality. The three-term rational lower bound for log 2 validates the ratio-128 threshold.

The two-dimensional positive-model control also checks: G=I+a*ones has minimum eigenvalue one; the positive B eigenvector angle is 3pi/8; the rotation gives the stated sine-squared integral. The elementary chord and exponential bounds give 245/121>2, which defeats both the scalar and fixed-relative sufficient budgets while every actual endpoint matrix remains positive.

## Reproduction and limits

I ran the original exact checker with isolated standard-library Python into my own review directory. All **606 exact checks** passed, and the parsed JSON equals the author's saved receipt. This replay authenticates finite identities and rational margins; the independent part of the review is the reconstruction of the analytic arguments above.

The unbounded support-window positivity theorem remains open. These manuscripts invalidate one proposed transport budget and supply a justified alternative interface; they do not establish its missing all-window input.
