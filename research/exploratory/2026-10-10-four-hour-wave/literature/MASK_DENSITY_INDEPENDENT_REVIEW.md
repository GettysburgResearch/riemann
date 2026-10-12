# Independent elementary mask-density review

Date: 2026-10-10. Full mathematical audit: PASS at
`arithmetic/MASK_DENSITY_REFINEMENT.md` SHA256
ecddc2ee84fac81d6905663e3f08c7fbff62d54c08f2a01aa402f9e640b98d2c.
This is an ideal-counting result. The application to conditional CRT
nonreturn still assumes U_B; no moment or zero-free input is proved.

R-M1's rational Chebyshev argument counts both split prime ideals,
the inert norm-square ideals and the fixed ramified prime correctly.
The resulting theta_K(y)<<y and ideal-count split at sqrt(y) give
pi_K(y)<<y/log y. Partial summation supplies both log-weighted
harmonic and inverse-square-root sums with the displayed orders.
The bounded small range can be covered by fixed field constants.

R-M4's logarithmic ratio is bounded by
(sigma-1)sum log(Np)/(Np-1), which is O(1) at
sigma=1+1/log L. The truncated product at sigma is at most the
absolutely convergent Dedekind zeta Euler product. The elementary
ideal count gives zeta_K(sigma)<<1/(sigma-1) on this bounded
sigma range. Hence the claimed O(log L) small-prime product requires
neither a prime-ideal theorem nor a Mertens product asymptotic.

For an arbitrary mask, large primes above L number at most
log(Nh)/log L. Splitting at L=max(9,log(3Nh)) proves the first
product bound. Splitting at L=max(9,log(3Nh)^2) proves the stated
second bound. The second is valid but can be sharpened; see
the separate `MASK_PRODUCT_REFINEMENT.md` for a smaller split.
The positive lower bound log log3 handles Nh=1 and every fixed
small mask without an undefined logarithm or varying constant.

R-M7 preserves the already independently reviewed uniform C-M3
main term and error. At Nh<=C_S D^A, the product error is
D^(1/2+o(1)) uniformly in the moving mask. The monotonicity
argument correctly separates the fixed bounded range before
using t/log t at larger t. The positive main difference at two
fixed scales is D/log log(3D), dominating that error. The
weighted smooth mass and its uniform sufficiently-large threshold
therefore follow.

The final contradiction uses the exact retained nonunit source
mask and explicit U_B. A log-log loss does not affect the positive
exponent gap for B<1. Physical CRT frequency transport remains
unpaid as in the source. No finite numerical control is advertised
as proving these asymptotic products, and none is needed for this
written elementary proof.
