# Full hybrid Hecke energy, not another selected covariance sector

**Status:** proposed unconditional mathematics with complete proofs and finite
diagnostics. No independent review; no fixed-principal moment or RH result.

The main theorem averages the ACTUAL Gaussian coefficient source over genuine
Mellin twists and angular Hecke characters (plus the finite class group when
needed). It covers every fixed imaginary quadratic field, all original masks,
any nonnegative fixed row measure, and both native Mobius and coupled 0/1/m
coefficients, uniformly in m>=2.

With both spectral window widths R and row mass Z,

    |mean full critical energy - identical-ideal diagonal| << Z D/R^2,
    diagonal << Z log(3D).

At R=sqrt(D) the ENTIRE averaged energy is its diagonal plus O(Z). Large
incomparable and conjugate equal-norm pairs are included, not carved away.
Each width is square-root-sized; their TOTAL parameter volume is still D.
This is NOT a bound for the principal twist and is not a same-family numerical
improvement over the one-parameter theorem in #954.

A fixed width schedule R=sqrt(D)exp((log(3D))^(3/4)) gives an error smaller than
D^-B for every fixed B. Consequently the diagonal expansion from #953 becomes
an expansion of the FULL averaged sixth-power source:

    L log D + C + J D^(-1/6) + O(D^(-1/4+epsilon)), L,J>0.

The sign of this secondary term is positive. #953's negative prime-quotient
secondary term is a different subtotal. Its existing residue calculation is
credited, not claimed a second time.

The higher-moment theorem proves, at every fixed k,

    mean |B(X)|^(2k) << Z[X^k+X^(2k)/R^2]log(3X)^(k^2-1).

At R=X^(k/2) it has the diagonal X^k power. This requires family volume X^k,
not the original near-linear physical-row range. No growing-k constants,
new metaplectic covers, or fixed-member extraction are claimed.

## Reading and replay

Read THEOREMS.md for the all-pair estimate, imaginary-quadratic class adapter,
Gaussian tails, full-average asymptotic, and sharpness boundary. Read
HIGHER_MOMENTS.md for the actual product coefficients and all fixed orders.
SOURCES.md distinguishes classical methods and the exact repository inputs.
VALIDATION.md records the finite scope and the absence of independent review.

    python check_hybrid.py > /tmp/hybrid-exact.json
    python -O check_hybrid.py > /tmp/hybrid-exact-o.json
    cmp EXACT.json /tmp/hybrid-exact.json
    cmp EXACT.json /tmp/hybrid-exact-o.json
    python check_hybrid.py --numerical > /tmp/hybrid-numerical.json
    python -O check_hybrid.py --numerical > /tmp/hybrid-numerical-o.json
    cmp NUMERICAL.json /tmp/hybrid-numerical.json
    cmp NUMERICAL.json /tmp/hybrid-numerical-o.json
    python verify_manifest.py

Numerical mode requires mpmath. Its 60-digit computations are NOT certified
intervals and do not evaluate an infinite arithmetic source. Exact mode uses
the standard library. The general number-field large-sieve/Hecke mean-value
method is classical; no worldwide priority claim is made for these methods.

Base: #953, a93d382951f8fac7b0c28783061a7ddb99fcf0a4.
Only this new standalone directory is added. Integrated status is unchanged.
