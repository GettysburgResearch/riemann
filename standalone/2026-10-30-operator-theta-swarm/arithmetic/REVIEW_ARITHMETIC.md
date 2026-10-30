# Independent review of the arithmetic zero-kernel packet

Reviewer: spectral-geometry swarm agent, 30 October 2026.

Verdict: the stated component arguments pass this source-level review at the frozen identities below, after one scope correction. This is an independent AI-agent review, not human refereeing, proof-assistant certification, an RH proof, or acceptance into the repository's integrated scientific baseline.

## Frozen files

| File | SHA-256 |
|---|---|
| ARITHMETIC_KERNEL.md | `631bffd147dc3d58d3eef6ad9e7535d89b56311bc91dfc39e6c52447b335f8d9` |
| verify.py | `c785283b3e2813114e057e550b035c78d2893960b66591de1ac3ee1eaa1fd6c8` |
| verification.json | `6eb1d361954dd97c6ccbaf01b8920e9a1d4edfe4bde73cfcdc659bdd1e97acc1` |

The files were read from the author's `work_arithmetic` directory. These hashes were freshly computed after the correction described below.

## Analytic checks

1. **Gamma factorization and signed Lévy measure.** Independently expanded
   `C(alpha-z)/C(alpha)` into the exponential factor, gamma(b+z/2), and inverse gamma(c-z/2). The log-gamma factor produces the claimed negative-jump density; the inverse gamma produces the negative positive-jump density. The exponential variable contributes `exp(-alpha*x)/x` on the positive side. The subtraction signs in (5.4) are correct. The density changes sign precisely when `2*sinh(x)=1`.

2. **Uniqueness argument.** The native law has exponential tails, hence finite second moment. The measure `x^2 nu_alpha(dx)` has finite total variation, including near zero where the signed density is order x^-2. If the law were infinitely divisible, its finite second moment would make the negative second derivative of its log-characteristic function the Fourier transform of a nonnegative finite measure, including a possible Gaussian atom at zero. Finite-measure Fourier uniqueness therefore rules out the negative interval. This is a valid obstruction and does not assume positivity of the signed representation.

3. **Sharp repair threshold.** Adding theta copies in the log-gamma convolution semigroup changes only the positive-jump density to the expression (6.3). It is nonnegative for theta>=1. For 0<=theta<1, its leading `(theta-1)/(2*x^2)` singularity is negative. The same finite-variance uniqueness argument gives necessity. At theta=1 the moment generating functions cancel exactly, yielding the independent exponential plus half-log-gamma law in (6.2). The Stirling deconvolution exponent pi*|t|/4 is correct.

4. **Symmetrization and phase.** Adding the two reflected signed densities gives (7.1). Its positivity follows from the displayed elementary factorization, and its order near zero is x^-1, so it is a valid Lévy density. At alpha=3/2, gamma recurrence reduces the modulus squared exactly to the product of the two centered Laplace characteristic functions in (7.2). Real sum-zero vectors therefore cannot detect this phase obstruction, while complex vectors can.

5. **Finite witness signs.** Expanded the three unordered pairs independently. With the convention `A_ij=L(t_i-t_j)` and the stated coefficient vector, the quadratic is precisely `-8*r8-(5/2)*r16+12*v8-6*v16`. Gamma recurrence and the centered Weierstrass product give the arctangent series (8.3) with the stated sign. The omitted summands are strictly negative. The argument uses the continuous logarithm, avoiding a principal-argument phase-wrap error.

6. **Gauges and transported target.** The gauge `T^(z-alpha/2)` cancels the complex power in the Gram kernel, so the limit is `C(alpha-z-conjugate(w))`. Differentiation supplies the signs `(-1)^(j+l)`. Applying the same gauge to a multiplicity-m zero functional sends the target to `T^(-alpha/2)*(1,log T,...,(log T)^(m-1))`, as stated. The inverse 2-by-2 matrix yields the plus sign `L+C'/C` in (4.3). The lower bound is conditional on a hypothetical zero and does not exclude it.

7. **High-height scope.** Checked the stated fixed-parameter sum/integral proof: the split at sqrt(T), the product error `T/k^2`, the weighted tail, and the model total variation all give the claimed `O(T^(alpha/2))` error uniformly on compact alpha subintervals. The mixed-kernel version uses a compact complex substrip and Cauchy estimates legitimately. The text credits stronger high-height/collision-uniform prior art to Scott Schubr and does not claim Sections 2–4 as novel. I did not inspect the full external Schubr paper or independently establish a priority comparison.

## Correction made during review

The original prose excluded convolution with any infinitely divisible law having finite-variation positive jumps, while invoking the finite-second-moment Fourier argument. Such a noise law need not have finite second moment. I requested either a general Lévy-uniqueness argument or a finite-variance qualification. The author chose the latter and applied it both in Section 5 and in the concluding scope list. The frozen text above contains that repair. The native-law non-ID theorem and the sharp log-gamma threshold were unaffected.

## Executable check

Freshly ran the author's checker using isolated standard-library Python:

    python -I -S -B verify.py

The run succeeded with empty stderr, and its parsed JSON equals the saved `verification.json`. I inspected the rational alternating-series bounds, reciprocal/quadrant reductions for atan, the atanh-series logarithm bound, Machin pi formula, interval sign handling, and the outward rational decimal presentation.

The resulting enclosure is

    -1434571587687/10^12 <= Q16 <= -1434571587686/10^12.

Since every omitted summand is negative, the complete quadratic is strictly below `-717/500=-1.434`. The exact checker authenticates this finite witness and its elementary input bounds. It does not authenticate the infinite analytic classifications, high-height asymptotics, imported Hilbert-space criterion, or RH; those depend on the written arguments at their stated scopes.

## Remaining mathematical boundary

The repaired infinitely divisible law is a different source. Its inverse multiplier has exponential growth, and no estimate transports its positivity back to the native Nyman–Beurling approximation problem. The packet makes that gap explicit. No unsupported global zero-free conclusion was found in the frozen text.
