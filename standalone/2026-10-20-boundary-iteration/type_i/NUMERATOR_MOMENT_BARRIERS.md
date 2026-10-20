# Why the amplified second moment does not improve the critical numerator

Date: 2026-10-20. Status: exact comparison of specified supplied estimates,
not a lower bound for an actual numerator moment.

Source: Liu, [arXiv:2610.26835v1](https://arxiv.org/html/2610.26835v1),
Theorem 12.14, (14.3)--(14.6), and Proposition 14.3. The inspected HTML
has SHA256 5b128f3cedb4d6ecfe3a3d57b1290cb576cac03092cf0b807c6f8092abf864c6.
The argument retains the source's full prime annuli, finite character
basis, row exclusions, and common smooth profile. It grants all available
prime capacity optimistically; this only strengthens the compared method.

## 1. Exact second-moment comparison

Let a detected class have cardinality \(O(U^{R+\epsilon})\), amplitude
parameter \(0<\delta\le5/6\), and selected prime amplitudes
\(0\le g_i\le\delta/2\). Put \(13/18\le\kappa\le1\), and retain the
source count inequality
\[
 R\le1-2\delta/3.                                      \tag{N1}
\]
A centrally normalized ordinary AFE block of length \(U^m\) costs \(m\)
in the ordinary product moment. Using one ordinary factor and the
constant unit factor in Theorem 12.14 permits prime length
\[
 z\le(1-m)/(6\kappa).                                  \tag{N2}
\]
The constant factor is a fixed norm-one annular polynomial; alternatively,
granting it as a free factor enlarges the estimate system and suffices for
the obstruction below.

Write \(G(z)\) for the sum of the selected amplitudes times their lengths.
It may use the actual best ordered profile, rather than the mean amplitude.
Every such selection, including an optimistic fractional final factor,
satisfies
\[
 G(z)\le\delta z/2.                                    \tag{N3}
\]
The original full-annulus factor is retained in the M2 invocation; only
whole prime positions are selected, with the source mesh losses.
The lower bound on its size is used only on the detected class.
The second moment and Cauchy give the block exponent
\[
 E_2(m)=\frac{R+1}{2}-G(z)-\theta m
 \quad\text{on the raised line }1/2+\theta.             \tag{N4}
\]
At the largest balanced AFE block \(m=1/2\), (N2)--(N3) imply
\[
 E_2(1/2)\ge\frac{R+1}{2}-\frac{\theta}{2}
                           -\frac{\delta}{24\kappa}.   \tag{N5}
\]
The source fourth-moment estimate for that same block, with no remaining
prime capacity, is
\[
 E_4(1/2)=\frac{3R+1}{4}-\frac{\theta}{2}.              \tag{N6}
\]
Consequently
\[
 E_2(1/2)-E_4(1/2)
 \ge \frac{1-R}{4}-\frac{\delta}{24\kappa}
 \ge\delta\left(\frac16-\frac1{24\kappa}\right)
 \ge\frac{17\delta}{156}>0.                            \tag{N7}
\]

Thus the amplified second-moment endpoint is strictly worse at the
largest balanced block throughout the source range, even with the best
possible amplitude profile and full prime supply. Mesh and capacity
losses cannot reverse this comparison. Interpolating this endpoint with
the supplied fourth moment cannot improve their minimum for this block.

This does not prove that a class has many rows of full conductor, or
that its longest block is large. It identifies the supplied upper-bound
obstruction. A theorem removing that block on the critical class, or an
improved mean for it, would change the inputs.

## 2. Higher moments obtained from the same fourth moment

Suppose the common Hecke zero-free premise has boundary
\(\beta=(1+\kappa)/2\). The conductor-uniform bound for \(L\) itself,
obtained by the same logarithm argument as for its reciprocal, and
annular Mellin inversion give
\[
 |S_m(u)|\ll U^\epsilon U^{\kappa m/2}.                 \tag{N8}
\]
The row inducing character is nonprincipal and belongs to the stated
global family. No arbitrary prime coefficient is substituted.

For real \(q\ge2\), using (N8) on \(2q-4\) copies and the ordinary
fourth moment on the other four gives at \(m=1/2\)
\[
 E_{2q}=
 \left(1-\frac1{2q}\right)R+\frac1{2q}
 +\frac{(q-2)\kappa}{4q}-\frac{\theta}{2}.
 \tag{N9}
\]
There is no prime capacity after the two half-length ordinary factors.
Exact subtraction yields
\[
 E_{2q}-E_4=\frac{q-2}{4q}(R+\kappa-1).                \tag{N10}
\]
The source also has \(R\ge1-\delta\). Hence for
\(\delta<\kappa\), all \(q>2\), including the sixth moment \(q=3\),
are strictly worse. Every critical witness in the inherited barrier
certificate has \(\delta<12/25<13/18\le\kappa\), so this covers that
certificate's entire witness set.

A genuinely new sixth moment is not ruled out. Equation (N10) concerns
only moments manufactured by multiplying the current fourth moment by
the available pointwise bound.

The source's buffered detector actually gives the stronger local
pointwise exponent \(\delta m/2\), in place of \(\kappa m/2\).
It applies to every presentation in the same row class, including the
numerator, within the retained height budget: see the proof of
Lemma 13.3 immediately before (13.14). Replacing \(\kappa\) by
\(\delta\) in (N8)--(N10) gives
\[
 E_{2q,\mathrm{local}}-E_4
       =\frac{q-2}{4q}(R+\delta-1)\ge0,                 \tag{N10a}
\]
using the source lower bound \(R\ge1-\delta\). Thus even this stronger
version supplies no sixth-moment improvement on the longest block.

## 3. Exact reduction of the local-buffer block hybrid

This section allows different methods on different AFE blocks and
optimizes the raised numerator line continuously. It therefore addresses
more than a comparison of one moment at the longest block.

Put \(K=(3R+1)/4\), \(g=\delta x\), \(0\le x\le1/2\), and
\(\theta_0=g/(6\kappa)\). Grant the fourth moment unlimited prime supply
up to its formal capacity. This optimistic permission can only improve
the bound; actual supply and rounding losses can subsequently worsen it.
For \(0\le m\le1/2\), the pointwise count and amplified fourth moment
give the two pre-weight block exponents
\[
 R+\frac{\delta m}{2},\qquad
 K-\frac{\theta_0}{2}+\theta_0m.                       \tag{N12}
\]
The actual prime amplitudes are used through the source's ordered
selection argument, which guarantees gain \(gz\), up to its mesh loss.
This is the same mean-amplitude guarantee used in Proposition 14.3.
It does not assert arbitrary bounded prime coefficients. On the critical
classes \(x=1/2\), every positive-length position has
\(g_i=\delta/2=g\), so optimizing the actual amplitude profile cannot
improve that guarantee.

The source inequalities \(1-\delta\le R\le1-2\delta/3\) imply that
the intersection
\[
 m_*=\frac{(1-R)/4-\theta_0/2}{\delta/2-\theta_0}
     =\frac{1-R-2\theta_0}{2\delta-4\theta_0}             \tag{N13}
\]
lies in \((0,1/2]\). The denominator is positive since
\(\theta_0\le\delta/(12\kappa)<\delta/2\).
The pointwise line is the smaller one before \(m_*\), and the
fourth-moment line is smaller afterward.

After the raised-line AFE factor \(U^{-\theta m}\), the largest
pre-reflection numerator exponent is consequently
\[
 N(\theta)=
 \begin{cases}
 K-\theta/2,&0\le\theta\le\theta_0,\\
 R+(\delta/2-\theta)m_*,&\theta_0\le\theta\le\delta/2.
 \end{cases}                                          \tag{N14}
\]
This is an exact maximization over the continuous block interval.
For \(\theta\ge\delta/2\) the same formal envelope equals \(R\),
although such lines are not needed or granted here.

At a row length \(U=Z^d\), the final class exponent has the form
\[
 E(\theta)=A+dN(\theta)+(d-l_y)\theta,                  \tag{N15}
\]
where \(A\) is independent of \(\theta\). The term \(d\theta\) is
the reflected conductor factor, and \(-l_y\theta\) is the change
in the numerator contour factor. Therefore (N14) shows:

* On \(0\le\theta\le\theta_0\), (N15) is affine between the two
  existing averaged endpoints.
* On \(\theta_0\le\theta\le\delta/2\), it is affine between the
  existing full-capacity averaged endpoint and the existing pointwise
  endpoint \(N(\delta/2)=R\).

More explicitly, writing \(E_4=E(\theta_0)\) and
\(E_L=E(\delta/2)\),
\[
 E(\theta)=
 \frac{\delta/2-\theta}{\delta/2-\theta_0}E_4+
 \frac{\theta-\theta_0}{\delta/2-\theta_0}E_L.           \tag{N16}
\]
Thus no intermediate line improves the minimum of these endpoints.
The licensed source range \(0\le\theta\le\min(\delta/2,1/10)\) is a
subset of the range already granted in this comparison.

At the final row scale \(d=h=l_y+2\ell\), the slope on the second
segment is \(2\ell-hm_*\). It can indeed be negative at some unequal
lengths. This does not create a new endpoint: (N16) still applies.
Hence this local-buffer refinement remains inside the four-endpoint
system of
[the inherited free-length barrier](../../2026-10-20-liu-all-field-artin-and-barrier/beyond_free_length_barrier.md),
including its critical witnesses with \(x=1/2\).

## 4. A direct-side input that is already present

Xu--Sang, [arXiv:2610.17675v1](https://arxiv.org/html/2610.17675v1),
Lemma 4.1 gives a Gauss-average main scale \(q^{5/6}L^{-2/3}\).
At the direct-average lengths \(q=XY,L=Y\), this is
\(X^{5/6}Y^{1/6}\). That same scale is already in Liu (13.7):
\[
 \frac QY\left(1+(Y^2/Q)^{1/6}
                    +(Y^2/Q)^2/Y\right)
 =X+X^{5/6}Y^{1/6}+Y/X.                               \tag{N11}
\]
In logarithmic lengths it supplies the \(b/12\) term in the final
Cauchy exponent. Liu explicitly retains the auxiliary coefficient one,
fixed ray sectors and separated norm-height profiles in this calculation.
Replacing a coarser bound \(Y\) by the Xu--Sang scale would count a saving
already used in the current zero-free boundary. No new numerical
boundary follows from that replacement.
