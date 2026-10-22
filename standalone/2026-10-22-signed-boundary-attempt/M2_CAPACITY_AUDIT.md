# Why reducing the selected-prime coefficient needs a new estimate

22 October 2026. **Status: exact obstruction for one specified proof
architecture. No lower bound for an actual character moment and no new
zero-free boundary are asserted.**

Source: Baiying Liu, [arXiv:2610.26835v1](https://arxiv.org/html/2610.26835v1),
Sections 12.7.1--12.8.1, especially (12.4), (12.6), (12.7), and the
prime-factor removal paragraph on printed page 80. The analysis below
concerns those displayed inequalities, including the triangle inequality
on the nonexceptional centered child. It does not assume that every bound
can be saturated by actual arithmetic data.

## 1. Question

The product moment used by the zero detector is available under

\[
 n_1+n_2+6\kappa z\le M.
\]

Here \(z\) is the total selected-prime length, \(M\) is the row length
plus the full displayed moving radical, and the global zero-free input
supplies the pointwise prime-product bound
\(|Q|^2\ll Z^{\kappa z+\epsilon}\).
Reducing the coefficient \(6\kappa\) would make more prime amplification
available in both the count and the reflected numerator.

Write a proposed replacement as

\[
 A+(\lambda-1)z\le M,
 \qquad A=n_1+n_2+z.
\tag{1}
\]

For a proposed coefficient \(\lambda>3\), we show that **the existing
main-amplifier edge, followed by exactly the existing pointwise stripping
step, requires \(\lambda\ge6\kappa\)**. This rules out obtaining a
marginal reduction of the current coefficient merely by improving
the slack in that edge's scalar calculation. No claim about a different
small-coefficient architecture with \(\lambda\le3\) is made here.

## 2. An allowed equality face of the exponent system

Take the original moving-support exponent to be zero. In the first
transform take the two full columns to have no common prime support:

\[
 c=d=p=R=E=q=0,\qquad K=K_0=2A-M>0.
\]

These choices set \(B_c=0\) in (12.3). Take the main amplifier term,
so \(w=w_o=0\). In the notation of (12.4), \(J=0\). If the amplifier
prime length is \(\ell=\sigma/3\), the source uses

\[
 g=2\sigma=6\ell.
\]

In the second transform again take no genuine common support:
\(c_2=d_2=b_2=p_2=g_2=t_2=V=0\). Formula (12.6) then gives

\[
 M'=M-6\ell,
\tag{2}
\]

while (12.7) gives the *exact* available excess

\[
 \Delta'=b_2-p_2+w+B_c+\ell=\ell.
\tag{3}
\]

There are no genuine factor removals on this face, so the child's
original lengths are still \(A,z\). Suppose (1) is saturated. Its
defect at the new width is exactly

\[
 A+(\lambda-1)z-M'=6\ell.
\tag{4}
\]

The face is nonempty at the level of the stated continuous exponent
constraints. For example, set \(M=1,A=5/6\) and
\(z=(1/6)/(\lambda-1)\), with the two ordinary lengths both
\((A-z)/2\). For \(\lambda>3\) these ordinary lengths exceed
\(M/4\), all lengths are positive, and \(K_0=2/3\). Choose
\(\ell>0\) sufficiently small that \(6\ell<\lambda z\).
Thus the argument does not depend on bounded or negative-length
terminals or on running out of prime factors. Small strict buffers
can be added and then sent to zero.

## 3. The necessary payment

Removing prime factors of total length \(d_z\) decreases \(A\)
and \(z\) by the same amount. It therefore repairs (1) at rate
\(\lambda d_z\). Equation (4) requires

\[
 d_z\ge\frac{6\ell}{\lambda}.
\]

The source pays for those factors using its global pointwise estimate,
whose squared-norm exponent is \(\kappa d_z\). The available
allowance (3) can pay this exponent only if

\[
 \frac{6\kappa\ell}{\lambda}\le\ell,
 \qquad\text{that is,}\qquad \lambda\ge6\kappa.
\tag{5}
\]

Whole-factor overshoot, profile losses, and discretization can only
increase the payment. The argument already grants their complete
absence.

## 4. What would change the conclusion

This is a barrier for the *supplied upper bounds*, not for the product
moment itself. A smaller selected-prime coefficient could still follow
from an estimate that changes this face, for example:

* preserving cancellation in the nonexceptional centered child instead
  of bounding its two rectangles separately;
* obtaining a strict saving for its prescribed Gauss coefficients;
* retaining an additional arithmetic restriction that excludes this
  face throughout the transformed family;
* replacing the sixth-power amplifier by a different source-preserving
  transform with a better ratio of width loss to density gain.

Substituting a better local zero-free parameter of the original
detected rows into (5) does not supply such a change. The child rows
have new characters and the original class restriction has already
been removed. The separate route audit records that distinction.

No zero-free theorem is inferred from this obstruction. Its purpose is
to locate a specific analytic estimate that must change, rather than
to label the constant six an arbitrary numerical choice.
