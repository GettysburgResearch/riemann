# Independent internal review of the mixed-sign disk theorem

Reviewed `../MIXED_SIGN_STRIP.md`, actual-byte SHA256
`2d528dd1e62031af4fa22bb2f99c938d7356543b2744cb26c7cadcfc06834e5e`.
Reviewer: parallel theta track. No blocking error found in the finite
positive-weight theorem, its symmetric-band zero-weight extension, or
the stated negative-edge price. This is internal component review,
not an external referee decision or actual cofinal theta construction.

The disk contraction is complete in its stated special case. Setting
u=rt,v=st gives a zero-free quadratic on the unit disk. When its
quadratic coefficient is nonzero, the product of the two roots has
modulus at least1, proving |A/D|>=rs. When D=0, A!=0 follows by
evaluating at u=v=0. Fixing every other variable in its allowed open
disk makes this a legitimate iterative multiaffine contraction.

For a positive edge, the displayed modulus difference is strictly
positive inside the unit disk when E<1, and E=1 factors exactly.
For a negative edge, r=E-sqrt(E^2-1) satisfies r^2-2Er+1=0. The
modulus difference is minimized at the negative real u=-rho because
its Re(u) coefficient is positive. At rho<r, the first displayed
linear factor is positive since its value at rho=r is0 and its slope
is negative. The second is positive at rho=r with value1-r^2.
Thus the entire edge polynomial is nonzero in the required disk pair.

I reconstructed the incidence construction: multiplying the complete
edge polynomials and contracting all incidences at each vertex leaves
exactly the two common-spin choices and gives radius exp(-2a_i).
No edge interaction or shared vertex is omitted. Isolated vertices
contribute1+z_i. Global spin reversal gives the exact reciprocal
partition identity and hence the exterior disk region.

The field/frequency substitution is correctly signed:
`z_i=exp(-2h_i-2izw_i)` has modulus exp(-2h_i+2w_i Im z).
Its inner and outer conditions give respectively the lower and upper
exterior regions in(1). The Gibbs normalization and all-up prefactor
are nonzero. The local price identity
`a=atanh sqrt(-tanh J)=(arcosh exp(-2J))/2` for J<0 is exact.
Its weak-coupling square-root cost agrees with the two-spin model.

During review I requested one scope clarification for an unobserved
vertex. Giving it epsilon weight and h=a=0 inserts ratio0, so that
particular argument preserves a symmetric band containing0 and does
not directly preserve an arbitrary asymmetric interval. The reviewed
version explicitly makes this distinction. For the actual symmetric
budget the epsilon-weight argument and local uniform Hurwitz limit
are valid. The limiting characteristic function is not identically
zero because it is entire with value1 at0.

This closes the zero-band dependency left explicit in
NEGATIVE_EDGE_REVIEW.md. The latter remains separately bound to its
own frozen source for negative-cost and normal-family arithmetic.
Neither review supplies the missing growth-controlled cofinal models.
