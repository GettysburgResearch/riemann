# Independent-review checklist

Review a component paper, not a purported complete RH proof.

1. Check that the scale measure has weights 2/n^2, not shape weights 2. Its
   jth moment is 2 sum n^(-2j-2), so degree-2r exactness means cumulants through
   2r+1. The endpoint atom becomes a positive DRIFT, not a zero-scale gamma.
2. Reconstruct orthogonality for x*d sigma, Radau positivity, uniqueness and
   the strictly positive first missing cumulant. The rule's poles are in the
   Laplace variable; they are not Fourier/Mellin zeros of the reciprocal law.
3. Check the exact Hermite remainder (19), including sign, s^(2r+1), and the
   squared denominator. In (20) K has total mass E_r/(2r+2). The positive
   measure representation does not make its differentiated generator positive.
4. At Re s=-1/2, check the complete positive-law interpolation, both mgf
   ceilings, the head bound, and the INTEGRAL over every real frequency.
   N>=r+2 is needed for the retained head factors. Verify the resulting
   epsilon=64 E_r (r+2)^(4r+6)/(2r+2), not a fixed-r big-O assertion.
5. Check the common lower normalization, support endpoints, square-root error,
   factorial derivative bound and all numerical constants in (31)--(36).
   In particular substituting the growing strip is justified explicitly; it
   is not substituting into an unknown fixed-strip constant.
6. Reconstruct the generalized Dirichlet factor for positive NONINTEGER gamma
   shapes, the complex zero-free tube, and the exact endpoint powers. The
   inherited fixed-stage theorem then applies, but no uniform exterior radius
   or cofinal real-rootedness follows.
7. Check the uniform complete inverse-square tail before passing to the zero
   defect. Multiplicities of real splitting clusters remain in the limit.
   The finite radial repair is a different operation and need not preserve
   a positive density. The unproved final estimate is OPEN-RGT, not a check
   assigned to a referee.
8. Inspect the checker separately. Exact rational finite measures test the
   error identities; actual infinite-tail moments are obtained by complete
   Bernoulli/pi formulas with an Euler--Maclaurin comparison. The high-r rows
   evaluate proven BOUNDS, not high-r quadrature nodes or Fourier spectra.
   Interval overlap corroborates two containing enclosures, not an equality
   proof by itself. The equality identities have their written/exact controls.

No novelty claim is made for Gaussian quadrature, positive gamma laws, or
classical moment/zero methods. Verify source-specific statements and explicit
quantifiers rather than the number of accepting finite checks.

For the optional changed-source test RGT7, retain its dependency on CG4 in #855.
Verify the density convergence and common envelope before Rouche, the modified
head's eta-dependent frequency scale, and the final eta^(-1/2) cost. Check the explicit allowance 48*2^-128 against the inherited rational
Rouche margin. No new defining-integral zero computation is provided. This stress test is independent of
the zero-free assumptions of the primary approximation theorem.
