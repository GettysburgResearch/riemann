# Independent scoped review of the sampled-moment criterion

Reviewer: moment-obstructions subagent. Result: **PASS**, for the theorem statements and retained conditional scope in the exact file reviewed.

Reviewed file: attack3_averaging.md, intended release name SAMPLED_MOMENT_CRITERION.md.

Reviewed SHA256:

    18bf2fdad438eb21ae3318eba7d42e9c03803b2dd1abc4d8f6448fb3b04499de

The review read the entire note. It did not execute a finite numerical test, assume an unproved arithmetic sampled moment, or independently authenticate the imported analytic theorems.

## Load-bearing checks

1. The infinite convolution gives a smooth compactly supported probability density, and its Mellin product is nonzero off the imaginary axis. The derivative estimate follows from differentiating distinct interval-density factors as measures, using the next factor for the supremum norm. The bounded consecutive-ratio hypothesis supplies the single exponential constant needed when the derivative order grows. No uncontrolled sequence of smooth seminorm constants is used.

2. The measurable-set interpolation proof is valid for arbitrary measurable retained sets of the stated local density. Chebyshev leaves a positive-measure set with controlled point values; the greedy separated-point argument works even when the original integral is zero. The factorial denominator in the Lagrange basis absorbs the growing interpolation degree. The complex remainder is justified by the divided-difference integral, not a real mean-value-point assertion. The partition argument sums errors in the actual Lp norm and does not acquire a factor equal to the number of cells.

3. The order choice m = ceil(4 log(X)/r_X) remains valid if r_X is larger than log(X), when m may equal one. Under the stated conditions, m = o(log X), the observational factor is X raised to o(1), and the derivative error after raising to the fixed p-th power is O(X^(h-p)). The measurable sets may vary with X. No joint regularity in that variation is needed for the dyadic conclusions.

4. In the grid argument each node participates in only O(m) interpolation blocks, including the repeated block near the upper endpoint. Its cost is absorbed into a fixed constant raised to m. The mesh hypothesis ensures both m <= N+1 and the derivative-error bound. The normalization includes the endpoints with total weight log(2)+Delta, so the moment reduction's controlled term costs no new power.

5. The recovered row budget is exactly X^h on D in [X,2X], not the discontinuous moving budget D^h. The sixth-power replica cutoff is the measurable step function Y_r(D) = (X^h/Nr)^(1/6), and it satisfies the required uniform lower bound by a fixed multiple of D^(h/6). Jensen uses the original literal zero masks and loses D^(-h/6); possible unit multiplicity changes only a fixed constant. Combining this with the recovered dyadic moment gives exponent k+5h/6+e-2k sigma. This yields the displayed boundary 1/2+5h/(12k)+e/(2k).

6. The use of the source causal moving-cutoff theorem is correctly separated from the elementary sampling proof. The target row remains fixed in cofinal extraction. Mellin nonvanishing of the fixed detector and nonvanishing of the finite Euler correction prevent a zero of the fixed primitive L-function from being canceled in the initial Mellin identity. The note explicitly retains the contragredient-family condition for any reflected critical-line conclusion.

7. The one-sided signed-remainder averaging does not introduce an absolute value of the remainder. It integrates the existing pointwise upper inequality with nonnegative sampling weights. The interpolation is applied to the original smooth fixed-row inverse sums, so it does not require regularity of an internal arithmetic cutoff in the signed remainder.

8. The wide-modulation statement follows by grouping tuples by the integer product norm, using the ideal divisor bound and the elementary Dirichlet-polynomial mean-square inequality. Its finite-aperture loss and the restored aperture factor when returning to a fixed modulation interval are correctly stated. This does not prove a fixed-test generalized moment.

No release-blocking mathematical error was found. The open input remains the sampled arithmetic moment or signed sampled-conductor bound, with the source hypotheses identified in the note; the sampling theorems do not supply it.
