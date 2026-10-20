# Independent review of the conditional scalar sensitivity

Reviewed 20 October 2026. This receipt binds
`CONDITIONAL_BOUNDARY_SENSITIVITY.md`, SHA256
`e683b79fdeedc8169f4dd4ce016add910f6e8ccc789cabae72c0181e15e7a191`.

The new analytic premise in that note is explicitly unproved. This
review checks its conditional scalar consequence against the displayed
source interfaces, not the missing inverse theorem or all imported
analytic dependencies.

The short/long intersection and derivative in (3)--(4) are correct.
The complete improved inverse envelope also has its flat part at
\(r\le1/(1-\eta)\); the note now retains this condition. The
critical crossing lies strictly above it for sufficiently small
\(\eta\), and its count strictly exceeds \(1-\delta\), so the
flat part does not dominate there. Using the new input only in a
fixed neighborhood of the critical long length suffices: the old
increasing long branch has a strict margin on the complementary
shorter lengths.

For the endpoint, \(E\) is affine in \(b\), so
\(E_{bb}=0\). With \(\kappa=5/6-\ell/2\), the first row of
the critical Jacobian is
\((E_\ell-E_\kappa/2,0,0)\), and its determinant is exactly
\(- (E_\ell-E_\kappa/2)E_{b\delta}^2\). The source signs cited
in Lemmas 14.9--14.10 therefore give nonsingularity. The completed
square has a strictly negative second \(\delta\)-derivative at
its zero, and its positive first discriminant coefficient gives
the stated one-sided \(x\)-derivative. Lemma 14.10 states that
the critical zero is unique on the compact parameter rectangle,
which supplies the required strict margin away from a neighborhood.

Differentiating only the first endpoint equation at that critical
point reproduces the coefficient \(\rho\) in (8). The response
of the optimizing \(\delta,b\) does not enter this first
derivative because their two endpoint derivatives vanish there.
The source's strict remaining inequalities persist locally.

No numerical interval enclosure was used in this review, and the
displayed ordinary high-precision decimals are correctly excluded
from the proof of positivity. No numerical zero-free improvement
has been achieved merely by proving this conditional implication.
