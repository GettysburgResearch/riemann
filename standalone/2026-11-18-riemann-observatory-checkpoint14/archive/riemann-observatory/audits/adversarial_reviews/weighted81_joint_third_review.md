# Joint third cumulants of the cosine and sine prime bands

Assume RH and use the derivative-weighted strict two-sided tail. On a fixed band \(0<a<b<1/6\) put
\[
 W_Y=\sum_{Y^a<p\le Y^b}\frac{\cos(\gamma\log p)}{\sqrt p},
 \qquad S_Y=\sum_{Y^a<p\le Y^b}\frac{\sin(\gamma\log p)}{\sqrt p}.
\]
The mixed third cumulant has limit
\[
 \boxed{\displaystyle
 \kappa(W_Y,S_Y,S_Y)\longrightarrow
 [(b^3-a^3)-6(b-a)](b^2-a^2)^2 .}
\]
It is strictly negative. The centered distinct-prime joint kernel is \(12xy^2z^2(x^2-2)\), where \(x\) is the cosine frequency. The derivative-square rooted CUE model has the same mixed kernel and the same integrated cumulant. Together with the already checked cosine third cumulant, this determines the real third-cumulant tensor. Entries containing an odd number of sine slots vanish exactly by reflection. This comparison concerns the third tensor and does not identify a joint limiting law. [HLZ Theorem 5, (5), (24)](../../sources/classical63_derivative_moments/hlz2022print.pdf) · [Cosine cubic and rooted CUE measure](weighted73_rooted_cue_band_match.md) · [Exact symbolic checks](../../scripts/weighted81_joint_third_checks.py)

For the same band write \(\Delta=b-a\), \(\Delta_3=b^3-a^3\). In tensor notation the other nonzero limiting entry is \(ccc=-8\Delta^3+24\Delta^2\Delta_3-8\Delta\Delta_3^2+16\Delta_3^3/27\). The \(css\) entry above also applies to its two permutations, by symmetry of the joint cumulant.

## Signed allocations and the exact arithmetic kernel

Write \(D(s)=\sum_{Y^a<p\le Y^b}p^{-s}\). On RH, \(D(\rho)=W_Y-iS_Y\) and \(D(1-\rho)=\overline{D(\rho)}\). The identity
\[
 W_Y S_Y^2=\tfrac14\bigl(\Re(D^2\overline D)-\Re D^3\bigr)
\]
exhibits the two needed quadratic polarizations, \(D^2\) against \(D\), and \(D^3\) against \(1\). All coefficient arrays before polarization are real, including for real deterministic band multipliers. Each reflection recovers precisely the real part of the two ordered cross terms, which is enough for the two-sided cosine-sine product. The divisor-closed pads have bounded coefficients uniformly in \(Y,T\), since a coefficient of \(D^j\) counts at most \(j!\) permutations. The outer shifts use the separated Cauchy tori from the prior reconstruction. For all \(T\ge Y\) the longest support is \(Y^{3b}\), which fits a fixed declared HLZ length \(T^\delta\) with \(3b<\delta<1/2\). The arbitrary log-saving remainder belongs to the two whole polarizations, before expanding their main terms. This also works for separate polynomials in the three slots, by assigning each sign to its corresponding product before the same four-sign real polarization. [Uniform bounded-array scope and polarizations](weighted70_hlz_cutoff_review.md) · [Sharp continuous \(J\) audit](weighted75_sharp_aggregate_review.md)

For three distinct primes set \(x=\log p/\log T\), \(y=\log q/\log T\), \(z=\log r/\log T\). Denote by \(K_{+++}\) the leading normalized real kernel for all primes against \(1\). Let \(K_{-++}, K_{+-+}, K_{++-}\) denote the three real kernels with the indicated prime on the opposite side. Each retained arithmetic weight in the aggregate is \(1/(pqr)\). A sine slot contributes its sign divided by \(i\) relative to a cosine slot. Pairing a sign assignment with its global negative leaves the weights unchanged for two sine slots. The resulting raw kernel in the ordered cosine, sine, sine slots is
\[
 K^{\mathrm{raw}}_{css}(x,y,z)
 =\tfrac14\bigl(-K_{+++}-K_{-++}+K_{+-+}+K_{++-}\bigr).
\]
In particular, the minus sign associated with flipping the cosine frequency is the same as the all-positive term. Changing the convention for both sine signs leaves this formula unchanged.

To check the four kernels from the source, for a given ordered allocation let \(H,K\) be the two lists of scaled prime logs and let \(X,Z\) be their sums. In (5) the symmetrized leading quotient has numerator
\[
 e^{-\beta X-\alpha Z}+e^{-\beta Z-\alpha X}
 -e^{-\alpha-\beta+\alpha X+\beta Z}
 -e^{-\alpha-\beta+\alpha Z+\beta X}
\]
and denominator \(2(\alpha+\beta)\). In (24), a scaled tuple \((u,v,w,\lambda)\) contributes
\[
 \frac{ve^\lambda}{(u+v)(v+w)}
 \cdot\frac{e^{-vX}\prod_{t\in K}(e^{-ut}+e^{-wt}-1)
   +e^{-vZ}\prod_{t\in H}(e^{-ut}+e^{-wt}-1)}2 .
\]
There are the usual tuples \((\alpha,\beta,\xi,0)\), \((-\beta,-\alpha,\xi,-\alpha-\beta)\), \((\alpha,-\xi,-\beta,-\beta-\xi)\), and the reflected set with \(\alpha,\beta\) exchanged. The exact local prime quotient in (24) differs from \(e^{-ut}+e^{-wt}-1\) by \(O(1/p)\) for a prime in \(K\), uniformly on the fixed scaled circles. This error retains the arithmetic factor \(1/(pqr)\). The time-power integral after dividing by \(T\) is \(e^\lambda+O(1/\log T)\); the logarithm in (5) supplies its leading \(\log T\). These and the zeta Laurent expansions are uniform for \(T\ge Y\) and the stated supports.

On the separated Cauchy radii take the cubic numerator terms of (5) and the quartic terms of (24), as justified by simultaneous rotation of all Cauchy variables. Differentiate (24) first in the auxiliary variable, then take the mixed outer coefficient. In the signed combination above the coefficient from (5) alone is \(-yz(x+y+z-1)/2\). The coefficient from (24) with reflection is \(yz(x-yz+y+z-1)/2\). Their sum is \(-y^2z^2/2\), and the untwisted normalizing coefficient is \(1/12\). Thus
\[
 K^{\mathrm{raw}}_{css}(x,y,z)=-6y^2z^2.
\]
The independence of \(x\) is a raw-kernel identity after the four signs. It would not hold in the other mixed sign combinations. [Independent symbolic extraction and integration](../../scripts/weighted81_joint_third_checks.py)

## Collisions, centering and the strict tail

If \(q=r\) are the two sine slots, use \(\sin^2 u=(1-\cos 2u)/2\). Its constant term contributes \(\frac12 H_Y E_T W_Y+o(1)\), where \(H_Y=\sum_{Y^a<p\le Y^b}1/p\) and \(E_T\) is the normalized derivative-weighted prefix. The error for falsely including the all-three-equal terms in the constant term is \(O(\sum_{p>Y^a}p^{-3/2})=o(1)\). If the cosine prime equals one of the sine primes, \(\cos u\sin u=\sin(2u)/2\) has no constant term. In all nonconstant repeated-prime terms the lcm weight at the repeated prime is at most \(p^{-2}\). For example \(p^2\) against a distinct \(q\) gives \(1/(p^2q)\), and \(p^2\) against \(p\) gives \(1/p^2\). The exact prime-power local quotients and small shifts are uniformly bounded on these fixed supports. Summing over primes on the band costs \(o(1)\), since \(\sum 1/p\) is bounded and \(\sum_{p>Y^a}1/p^2=o(1)\). This classification is performed in the aggregate main term. It does not sum source errors over repeated prime tuples. The actual all-three-equal term also vanishes absolutely by \(\sum p^{-3/2}\).

Reflection gives \(E_T S_Y=0\) when the prefix is taken two-sided, and gives \(E_{\rm tail}S_Y=0\) exactly. One can use positive-prefix estimates for the real even products \(W_Y,W_YS_Y^2,S_Y^2\). The product of the cosine mean with the sine diagonal \(H_Y/2\) cancels the repeated sine term in the cumulant. For distinct primes the sine second-moment kernel is \(-6y^2z^2\), and the cosine mean kernel is \(F(x)=1-4x+2x^3\). Hence the centered kernel is
\[
 C_{css}=-6y^2z^2-F(x)(-6y^2z^2)=12xy^2z^2(x^2-2).
\]
Centering by any deterministic constant instead of the exact cosine mean does not change the cumulant.

All prefix formulas have uniformly vanishing errors for \(T\ge Y\): the fixed-band reciprocal sums are bounded, the scaled-shift error is \(O(1/\log Y)\) after summation, and the finite-prime kernel errors vanish with the lower cutoff. For the strict tail use the usual Abel formula with \(k(T)=(T^2+1/4)^{-1}\) and the inclusive prefix at \(Y\), so a zero at that ordinate is excluded. On \(Y\le T\le Y e^{\sqrt{\log Y}}\) the scaled coordinates can be replaced uniformly by their \(L_Y=\log Y\) versions. The farther part is negligible by the prefix mass asymptotic and the bounded normalized raw moments. Thus the raw moment formulas transfer before subtracting their products. Prime reciprocal measure converges to \(dx/x\) on each band, and diagonals of the product reciprocal measure have mass \(o(1)\). The triple integral of \(C_{css}\) then factors as
\[
 12\int_a^b(x^2-2)\,dx
       \left(\int_a^b y\,dy\right)^2
 =[(b^3-a^3)-6(b-a)](b^2-a^2)^2.
\]
If the exceptional-prime restriction is invoked for effectivity, restore the omitted term before tail partial summation. Its supremum on a fixed band is \(O(Y^{-a/2})\). Bounded even moments of the remaining cosine and sine sums follow from the aggregate square of \(D\) or \(D^2\), and bound the restoration in the cubic product by Hölder. [Exact strict-tail normalization and lower-order diagonal](weighted71_hlz_band_second_moment.md)

For separate bounded piecewise continuous real multipliers \(f,g,h\) supported on compact bands contained in \((0,b]\), the same argument yields the mixed tensor entry
\[
 12\!\int f(x)(x^2-2)\,dx \int g(y)y\,dy \int h(z)z\,dz.
\]
In case of overlap between the sine supports the diagonal cancellation uses the reciprocal overlap \(\sum g(\log p/L_Y)h(\log p/L_Y)/p\). For a cosine-sine overlap there is no zero-frequency diagonal. These formulas cover disjoint bands as a case.

## Independent rooted CUE calculation

Use the globally derivative-square tilted root law obtained from HKO (2.2) and (2.8) with moment exponent 1. In root-centered angles the remaining points have projection \(P=E-Q\), with \(E\) on Fourier indices \(0,\ldots,N\) and \(Q\) the rank-two span of the constant and centered linear coefficient vectors. The root itself is deterministic. The real observables use the negatives of the cosine and sine Fourier sums with weights \(1/k\), as in the earlier cosine comparison. The sign of the sine convention can be reversed without changing any entry with two sine slots. Reflection kills the odd-sine entries. [HKO original, §2(a)](../../sources/classical63_lfunctions/hko2000.pdf) · [Rooted law and Fourier projection derivation](weighted73_rooted_cue_band_match.md)

For \(F=S^{k},G=S^{\ell},H=S^{m}\) on the Fourier space, the joint third DPP cumulant is
\[
 \operatorname{Tr}(PFGH)-\operatorname{Tr}(PFPGH)-\operatorname{Tr}(PGPFH)
 -\operatorname{Tr}(PHPFG)+\operatorname{Tr}(PFPGPH)+\operatorname{Tr}(PFPHPG).
\]
The base \(E\) cumulant is zero even when \(k+\ell+m=0\). In that case the two-step traces remove \(|k|,|\ell|,|m|\) from the \(N+1\) available indices and each three-step trace removes the path span \(\max(|k|,|\ell|,|m|)\). The expression cancels since the sum of those magnitudes equals twice their maximum. Otherwise all base traces vanish by the nonzero net Fourier shift.

Expand \(P=E-Q\) in the cyclic trace, splitting each nonempty \(Q\) contribution into segments. With \(u(t)=(1,\sqrt{12}(t-1/2))^{\mathsf T}\), and a segment's successive visited normalized offsets \(d_0=0,\ldots,d_j\) starting from the rightmost shift, its continuum matrix is
\[
 \int_{-\min d_i}^{1-\max d_i}u(t+d_j)u(t)^{\mathsf T}\,dt .
\]
The trace of the product of these matrices comes with sign \((-1)^{\#Q}\). The discrete versions converge uniformly with \(O(1/N)\) error because the paths have span \(\le3b<1\), their segment endpoints are grid-aligned, and the integrands are bounded polynomial Riemann sums. Take one quarter of the all-positive complex cumulant plus the one with minus on the first slot, minus the two with minus on sine slots. This sign arrangement is the negative of the arithmetic *raw* sign arrangement because each of the three CUE observables already carries a minus. The DPP expression here is centered from the outset.

The symbolic check considers the three possible positions of \(x\) among the ordered positive magnitudes, allowing \(y,z\) to be exchanged. Each sorted-magnitude chamber splits only on whether the largest frequency exceeds the sum of the smaller ones. Indeed the sign of every difference of visited offsets is determined by a sum of a signed subset of at most three distinct shifts. Those are the six necessary open chambers; exact polynomial equality with \(12xy^2z^2(x^2-2)\) holds in each. Boundary equality follows from continuity of the segment matrices. Riemann summation of the \(1/k\)-weighted tensor gives the claimed integrated match, with no additional resonant term. The root shift adds no centered third term. No canonical promotion is made. [Exact six-chamber check](../../scripts/weighted81_joint_third_checks.py)
