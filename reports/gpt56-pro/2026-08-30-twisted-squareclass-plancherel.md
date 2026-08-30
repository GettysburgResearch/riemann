# Twisted squareclass Plancherel continuation

Date: 2026-08-30  
PR: #771  
Status: **complete deep nonresonant function-field fibres closed; live boundary open**

The physical map \((Q,d)\mapsto Qd^2\) is a twisted convolution. Fourier
transform diagonalizes it exactly and shows that the complete nonresonant
operator norm is the largest surviving core character coefficient, not the
sum over the character family.

Combining this rank-free theorem with the nonprincipal function-field
half-source shell estimate of PR #751 removes the conductor-family \(q^m\)
tax and closes every complete deep nonresonant shared-conductor fibre under
the explicit inequality in `T-107301`.

The remaining work is the signed completion boundary for the literal joint
source masks, together with the explicit quadratic/principal rows. RH and GRH
remain unproved.
