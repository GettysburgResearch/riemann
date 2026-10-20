# Explicit angular cost for the joint pair

20 October 2026. Proposed extension of the independently reviewed
joint mean. Its inputs are
../mixed/JOINT_PAIR_UNEQUAL_CUTOFFS.md, SHA256
36277fce41d0c5d425b534b885cd08cd3444a33fbeb49dfa45303f1c13d195c7,
and ANGULAR_UNIFORMITY.md, SHA256
9735a9cf2a7c75495a86da9c80ff9ddb7e2efb1e19bb6acad226aaec00b99385.

Use precisely the former note's family, F_j, V, W and c_j, and put
\(L=1+|\ell|+|t|\). For \(0<\delta<1/6\),
\[
 \mathcal M_j(R,H;1/2+\delta+it)
 \ll_{\delta,\epsilon}
 (RH)^\epsilon F_j(R,H)L^{2-4\delta+\epsilon}.
\tag{JA1}
\]
The constant is independent of R,H,ell,t. The field and finite
bad-place profiles remain fixed. The vector includes both angular
signs. Angular order zero is allowed only with the separate
nonunit quadratic guard of ../global/GUARDED_SPHERICAL_MEAN.md; all
conductors in the dyad H<NS<=2H are nonunit.

Here are the additional uniformity checks. All ramified cusp
conversion matrices are uniformly bounded in angular order,
and the moving factors \(\alpha(r)^{2\ell}\alpha(S)^{2\ell}\)
are unit phases. The exact gamma ratio satisfies
\[
 |G_\ell(1/2-\delta+it)|\ll_\delta L^{4\delta}.
\]
This includes both relative size regimes for ell and t, by pairing
gamma functions with fixed real shifts. On a right absolute line
the complete series is uniformly bounded in angular order.
On a preliminary left line -eta, its reflection gives a fixed
polynomial in Nr,NS times \(L^{2+4\eta}\). Gaussian three-lines
therefore bounds the original line by a fixed conductor polynomial
times \(L^{1-2\delta+2\eta}\). After squaring, this makes a
supremum normalized by the right side of (JA1) finite for finite
conductor and angular cutoffs, before any absorption.

The original-side sieves are uniform in ell and t: these variables
enter their column coefficients only through unit phases. The cube
sums are the same four convergent sums in the joint proof.
The reflected partner factor is
\(R^{2\delta+\eta}H^{4\delta}Y_j^{-4\delta}L^{8\delta}\).
Choose
\[
 Y_2=C_0(RH)^\theta V L^2,\qquad
 Y_0=C_0(RH)^\theta W L^2.
\]
The factors c_j cancel with the corresponding F_j weights exactly.
Choose all sieve/divisor losses below 4delta theta, and choose
theta inside the final epsilon loss. The largest original-side
angular power is \(L^{2-4\delta}\); the other two nonconstant
powers are smaller. A fixed large C0 contracts both maps.
The Gaussian height convolution costs a fixed constant, since
\(1+|\ell|+|t+v|\le L(1+|v|)\).

Reflection keeps S, decreases r, and changes only the included
angular sign and partner, so all finite cutoffs close. Letting
them increase gives (JA1). At ell=0, the separate guard supplies
entire continuation, and bounded gamma arguments on the preliminary
left line cause no pole when \(0<\eta<1/6\).

The free-column consumer (JQ16) consequently has the uniform form
\[
 |T_j(A,R,H)|
 \ll_{\delta,\epsilon,W}
 (ARH)^\epsilon(1+|\ell|)^{1-2\delta+\epsilon}
 A^{1/2+\delta}(RH F_j(R,H))^{1/2}.
\tag{JA2}
\]
Only a fixed number of radial seminorms is needed for the height
integral. The inverse cube factor is absolutely bounded uniformly
in all finite and angular conductors on this line. No angular
derivative of order depending on ell enters this step.

The fixed-angular numerical exponent overlaps the supplied recursive
source as stated in the reviewed joint proof. Equation (JA1)
records an explicit additional angular cost; it is not a claim
of a new best conductor exponent or a stricter detector bound.
