# Coordinating review of the other completed mathematical arguments

This record concerns direct mathematical reading by the coordinating agent.
The authors of the reviewed notes are separate agents in the same session.
It is not an external referee report or a claim to have reconstructed every
classical analytic input.

## Native crossing calculation

The reviewed native note has SHA-256
ecb78edf41a1632c8b9ef06a3edb7e8e11ecef605df924b5d9fc893f5935b457.

I checked the corrected crossing-only quantifier in Section 1 and compared
it with Section 5 of the exact inherited native proof at commit
c93ca65a510b6acaf167f929b9bf7e67d742b05a. An earlier draft stated the
constant balance norm without making its crossing restriction explicit.
The published statement supplies the general-\(Y\) bound first and uses
\(|m(Y)|\le1/Y\) only on its defined native crossing set.

In the new Section 6, Stieltjes partial summation of the entire prefix gives

\[
G_Y(s)=Y^{1-s}m(Y)+(s-1)\int_1^Y m(x)x^{-s}\,dx.
\]

The unit coefficient is included; there is no lower-boundary subtraction
missing from this formula. The exact square expands into the stated
interior term and two boundary terms.

For \(A_Y^{\rm old}(s)=\int_1^Y m(x)x^{-s}\,dx\), changing variables
\(x=e^u\) proves

\[
\frac1{2\pi}\int_{\mathbb R}|A_Y^{\rm old}(1/2+it)|^2\,dt
=\int_1^Y |m(x)|^2\,dx=F_{Y-1}.
\]

The first boundary term therefore costs at most
\(Y^{-1}T^{13/42+\varepsilon}F_Y\) in squared frequency norm at a crossing.
The second costs \(Y^{-2}\), because
\(\zeta(1/2+it)/(-1/2+it)\) is square integrable. I checked the cited
Bourgain exponent against Theorem 5 of the v2 paper itself; its abstract
metadata still lists an older exponent, so the theorem text is the
relevant source. Substitution \(T=Y^{84/71}\) gives
\(-1+(84/71)(13/42)=-45/71\).

The final physical window is applied after frequency projection.
Plancherel and contraction by that window justify the root-norm
comparison; the omitted high-frequency part is supplied by the separately
identified inherited theorem. The remaining complete interior term has no
factor \(m(Y)\). The note makes no contraction or global zero-free claim.
I found no mathematical defect in this final Section 6.

## Joint numerator comparison

The reviewed file has SHA-256
aa854ac365a480523bd26295c8a1e17359ba51963711fe86f45fbd02e23a12ce.

I independently checked the exact expression

\[
J-K=(P_m-R)/4+(q/2)|z(m)-z(v)|.
\]

It follows by substitution, including the physical supply truncations.
The piecewise-affine numerator envelope has the stated crossing point,
and its full reflection/outside-scale objective is minimized at one of
the two stated endpoints. The scope explicitly allows a relaxed contour
domain for the algebraic obstruction rather than asserting that every
such contour is analytically licensed. A separate independent review is
also present in this packet.

## Direct-estimate floor

The reviewed file has SHA-256
aaa1e14bcd08e364b85a3dd5ebc52759962906330284f2d0f0958907226099f6.

The nonnegative slack identity

\[
B_{\rm low}=\frac{13}{15}+\frac{17k}{60}
+d+\frac{3s_1+s_2}{60}
\]

is exact after substituting \(l_x=(M-b)/2\).
The stated sharp example has positive allowed lengths and satisfies the
relaxed direct inequalities. The proof keeps the variable principal
exponent, so its conversion from a power of the probe to a boundary in
\(s\) is consistent. This result limits the specified upper-bound recipe;
it makes no assertion of a lower bound for the actual arithmetic source.

## Principal and quartic calculation

The reviewed file has SHA-256
f67d4c44d512bdc87620cafb6e61a81b6d472917744ed72e929c1c9218b90774.

I checked the simultaneous dilation exponent and the coefficient of the
double-pole residue. The expansion of \(L_u(s-\tau)/L_u(s)\) contributes
\(-\tau L'_u/L_u\); this explains the negative sign of the logarithmic
derivative in the published residue. The conductor factor contributes
\((Y/Q_u)^\tau\), with its stated cost on a left shift. No new uniform
row bound is inferred from the meromorphic diagonal cancellation.

The cross-scale cancellation claim is explicitly conditional on the
rank-one cross-Gram formula. A diagonal upper bound is not used as proof
of that premise. Under the premise, the common \(Y^{-1/3}\) dependence
does annihilate the principal target at the same time as the proposed
exceptional term.

For the quartic identity I checked multiplicativity after squaring the
CRT factor, the primary inert-prime convention, and the squarefree
support. The angular factor is retained. Conjugating the two-component
Suzuki relation is compatible with its real residue-class matrix;
applying the inverse matrix and then taking the bilinear tensor gives
the published power \(N(m)^{1/2-s}\). A nonzero theta normalization is
not assumed.

The linear central-character obstruction is restricted to invariant
untwisted scalar integration. It leaves the explicitly compensated
period open. Torus integration of a product selects the displayed
additive index relation, so it cannot be replaced by the equal-index
diagonal without another construction. These exact identities specify
the missing signed object; they do not establish its analytic estimate.

## Quadratic and theta arguments

I read the quadratic Gauss completion, the finite cyclotomic interpolation
argument, and the inert-prime branch proof. The target at zero frequency
is retained throughout. The linear-disjointness condition is essential to
the exact recovery theorem and is stated explicitly. The separate native
agent's independent quadratic review is also present.

I read the kernel-instability construction. Its finite moment correction
uses an invertible covariance/Vandermonde matrix, while two high-frequency
cosines supply independent real and imaginary correction directions.
The perturbation coefficients decay faster than every fixed inverse power
of the frequency. This preserves positivity, the stated curvature margin,
and every fixed tilted Schwartz seminorm, while the new zeros escape in
their real part. It therefore does not contradict local uniform
convergence or Hurwitz's theorem. Exact modular structure is not retained.

For the reverse-heat example, the three-spin law gives the specified
variance and initial zero band. Tilting by the square of the observable
adds the displayed couplings, which become nonnegative by the stated
time. The Lee--Yang conclusion uses external fields with a common strict
real sign. The absence of a uniform exponential-moment envelope across the
constructed family is recorded.

Finally, the gamma-convolution identities preserve the Mellin/Laplace
distinction. The shape-one Mellin factor has its stated zeros without any
possible cancellation by the entire xi factor. No Stieltjes property for
the target logarithmic Mellin derivative is inferred from Laplace
positivity.

No blocking mathematical or scope issue was found in these reviewed
arguments. Their file identities are included in the exhaustive packet
manifest. The main global boundary has its own two independent reports
and exact algebra reconstructions.
