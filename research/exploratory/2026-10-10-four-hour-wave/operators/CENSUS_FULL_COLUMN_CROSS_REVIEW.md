# Independent audit of the complete-census companion column

Verdict: **ACCEPT at the stated source-qualified analytic scope.** This is
an independent mathematical review of FC1--FC14 in
[CENSUS_FULL_COLUMN_SECTOR.md](../xi/outer-ray/CENSUS_FULL_COLUMN_SECTOR.md),
frozen at SHA256
`db662f2f7c57a61413ecf16d3f4760fd1d5d315f8328bed70984340083960c43`.
Review time: 2026-10-10 14:30 UTC. The reviewer also read the complete
[CENSUS_LOCALIZATION.md](../xi/outer-ray/CENSUS_LOCALIZATION.md) and
[THEOREM.md](../xi/outer-ray/THEOREM.md) dependencies. No mathematical
correction was found. This review does not reproduce the imported finite
zero-count computation or turn the synthetic polynomial controls into a
native numerical certificate.

The complete finite product approximants retain the whole zero strip and
the absence of nonreal zeros in the central census range. The conjugate-pair
imaginary logarithmic-derivative sign localizes each successive derivative
with loss at most A in real part. Gauss--Lucas, differentiated local uniform
convergence, Hurwitz, and the positive imaginary-axis source anchor give the
strict limiting sign. The real simplicity induction is valid: a zero of
H_j in its protected interval cannot also be a simple zero of H_(j-1), and
the strictly negative derivative of H_j/H_(j-1) makes the new zero simple.

For every fixed derivative H_j, parity gives H_j(z)=z^epsilon G_j(z^2).
The source moments determine the zero factor at the origin exactly; the
order of G_j is below one. Its complete genus-zero product has a constant
exponential factor, so FC5 omits no exponential derivative. Positive source
mass away from zero gives exponential imaginary-axis growth for each fixed
derivative and excludes a finite zero set. The complete inverse-square
derivative sum is locally absolutely convergent. The imaginary parts of
the individual inverse-linear zero terms also converge absolutely because
the imaginary parts of the roots are bounded and the inverse-square zero
sum converges. Grouping conjugate blocks therefore preserves their signs.

In the protected slab, every nonreal zero of H_r has horizontal distance
strictly larger than 2A from the evaluation point. For 0<y<=A this is larger
than |y+Im rho|, so its real inverse-square term is positive. Every nonreal
conjugate block contributes a positive imaginary logarithmic derivative.
The real-zero terms have positive imaginary contributions a_alpha. Their
integer multiplicities give
(sum m_alpha a_alpha)^2 >= sum m_alpha a_alpha^2; the inequality is first
valid for finite sets and passes monotonically to the complete set.
Substitution in 2(Im q)^2-Re q' yields exactly m_alpha/den for each real
zero, plus the positive nonreal inverse-square terms. The complete zero
set is nonempty, so the complex Laguerre numerator is strictly positive,
including the case that one of these two types of zero is absent.

Finally direct multiplication gives the constant, linear, and quadratic
coefficients in FC13 with exactly the displayed signs. The constant and
quadratic coefficients are the two strict imaginary logarithmic-derivative
signs; the linear coefficient is the strict complex Laguerre numerator.
Consequently the sector holds for every lambda>0 on the entire slab.
The slab includes y=A. The outer theorem supplies y>A and the localized
simple-real-zero theorem supplies y=0, so no joining or limiting gap remains.

For actual Xi the resulting range is all y>=0, every lambda>0, and
|T|<8192-(r+2)/2 for integer 0<=r<=16381. Its hypotheses retain the
complete classical zero strip and the explicitly imported complete native
census through 8192. This gives a finite real-part column with unbounded
lower depth. It supplies no claim at unbounded real part and no RH proof.
