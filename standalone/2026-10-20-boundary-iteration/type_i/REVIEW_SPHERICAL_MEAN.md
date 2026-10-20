# Review of the guarded spherical mean

Date: 2026-10-20. Reviewer: Type-I subagent, independently of the author
of ../global/GUARDED_SPHERICAL_MEAN.md.

Reviewed SHA256:
6d69e24c325089ebeed5596ea393308581a80cb3ec82f9d5206f543707a1b23b.
The quadratic-pair mean and its normalization were separately reviewed
in REVIEW_QUADRATIC_PAIR.md. The present review concerns the new
angular-order-zero interface.

**Verdict:** no outstanding issue was found in the stated extension.
The nonunit primitive quadratic conductor is essential. This is a
proposed source-dependent theorem, not an assertion about arbitrary
spherical twists or an improved numerical zero-free boundary.

At a prime dividing the quadratic conductor, the two reflected
characters have sextic digits \(3\) and \(1\). The coefficient
projector is applied to the complete index \(cd^3\), so the cube
coefficient remains \(\xi_S(d)\). The four profiles at \(3\) and
the coprime cubic level do not change this local digit.

Writing the additive projector as
\[
 v_j=\sum_z\alpha_j(z)\pi(n(z/\pi))v_0,
\]
one has \(\alpha_j(b^{-1}z)=\chi(b)^j\alpha_j(z)\).
Consequently a cube unit \(b\) with \(\chi(b)=-1\) gives
\(\pi(a(b))v_j=-v_j\) for both digits. The ordinary Jacquet
module, on the other hand, is trivial on these cube units by the
unramified central inducing datum. Exactness and semisimplicity of
the relevant finite compact quotient rule out a hidden extension.
The Jacquet image of each projected vector is therefore zero.

Weyl conjugation changes \(a(b)\) to \(a(b^{-1})\), with the scalar
cube unit \(bI\). Its central action is trivial. Thus the reflected
vector has the same eigenvalue \(-1\) and likewise has zero Jacquet
image. This is cancellation of both actual constant terms, including
every ramified profile, rather than a claim about one original scalar
series alone.

There is also a native Eisenstein cross-check that avoids relying on
an all-field theorem outside its stated field scope: the exact finite
Fourier computation in EISENSTEIN_SPHERICAL_REFLECTION.md gives residue
support only at digits \(0,4\), for every fixed ramified profile.
Both digits \(3,1\) lie outside that support. The local central-datum
argument and this explicit cusp calculation agree.

At \(s=1/2-\delta+it\), the order-zero gamma quotient has numerator
real parts \(1/3+\delta,2/3+\delta\) and denominator real parts
\(1/3-\delta,2/3-\delta\). These are positive for \(0<\delta<1/6\).
The quotient has the same height power \((1+|t|)^{4\delta}\).
The finite-profile ratios converge on \(\Re s>1/6\), and the
required reflected strip lies inside that region. Entire continuation
removes every theta pole in the Gaussian contour shift.

The complete arithmetic reflection, the \(j=0\leftrightarrow2\)
exchange, the divisor resummation, and the three convergent cube
sums are independent of nonzero angular order. The finite-cutoff
absorption in the quadratic-pair note therefore applies unchanged.
Its constants are uniform in the nonunit quadratic conductor,
with exactly the displayed three conductor terms.

For a fixed conductor those terms are all \(O_S(R^{1+\epsilon})\).
Mellin inversion and the absolutely convergent inverse cube factor
on \(\Re s>1/2\) therefore give \(A^{1/2}B(AB)^\epsilon\), and
the balanced exponent \(3/4+\epsilon\).
The existing moving-conductor costs remain present if \(S\) varies.
This result does not remove the separate mixed-terminal obstacle.
