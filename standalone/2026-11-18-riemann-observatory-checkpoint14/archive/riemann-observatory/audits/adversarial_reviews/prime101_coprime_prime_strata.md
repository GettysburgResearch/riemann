# Short von Mangoldt factors, shared factors, and higher powers in the smooth twist

18 November 2026. The remaining smooth sum for the fourth cosine moment can be restricted further. With the cutoff width chosen sufficiently close to the height on a power scale, all genuine powers \(p^j\), \(j\ge3\), and all powers sharing a prime with their modulus contribute \(o(T)\) in aggregate. A separate Poisson argument removes a small-factor range to arbitrary power savings, retaining the exact gcd improvement. The remaining strata are coprime primes and prime squares in the longer range. [Fixed-coefficient reduction](prime98_fixed_arithmetic_sequence.md) · [Smooth saddle reduction](prime96_smooth_saddle_review.md)

## The effective modulus and short-factor estimate

Write \(T\asymp Y\), \(y=Y^\theta\), \(\theta=4b\in(1/2,2/3)\), \(H=T^\kappa\), and \(\kappa>(1+\theta)/2\). Let \(w_T\) be the smooth compact cutoff at heights comparable to \(T\), with \(j\)-th derivative \(O_j(H^{-j})\). After opening \(d_2*(\Lambda\log^2)\), let \(\nu\) be the von Mangoldt factor and \(s\) the divisor variable. Define
\[
S_{k,\nu}
 =\sum_{s\ge1}d_2(s)w_T(2\pi\nu s/k)
   \left[e(-\nu s/k)-\frac1{\varphi(k)}\sum_{u\bmod k}^{*} e(u\nu s/k)\right].
\]
The remaining aggregate is \(\sum_{k\le y}(a_k/k)\sum_{\nu}\Lambda(\nu)\log^2\nu\,S_{k,\nu}\), with \(0\le a_k\le24\). Every sum has finite support. For fixed \(k,\nu\), put \(g=(k,\nu)\), \(q=k/g\), and \(M=kT/\nu\). By surjectivity of the unit-map modulo \(k\) to units modulo \(q\), the average in brackets is exactly the unit average on \(q\) after multiplying by the unit \(\nu/g\). The case \(q=1\) contributes zero identically. If the support contains any positive integer \(s\), then \(M\) is bounded below by a positive constant. [Unit-average identity](prime98_fixed_arithmetic_sequence.md)

Expand \(d_2(s)\) as a sum over \(d e=s\). A smooth symmetric hyperbola split makes \(d\ll\sqrt M\) in each of two interchanged halves. For fixed \(d\), the smooth function of \(e\) is supported on \(e\asymp M/d\), has derivatives of scale \(kH/(\nu d)\), and has Fourier transform bounded by
\[
 \ll_B (M/d)(1+(kH/(\nu d))|\xi|)^{-B}
\]
for every fixed \(B\). For a unit numerator \(v\bmod q\), Poisson summation samples this at \(\xi=\ell-vd/q\). If \(q\mid d\), the entire inner sum cancels under the unit-average subtraction. Otherwise the nearest sample is at least \((q,d)/q\) from zero. All other samples are separated by unit spacing. Thus the true factor in the decay from the nearest sample is \(H\gcd(k,\nu d)/(\nu d)\). When \(Hg/\sqrt{kT\nu}\) is larger than a sufficiently large fixed constant, the sampling scale \(kH/(\nu d)\) is at least 1 uniformly, so these nonnearest samples have a summable \(B>1\) bound. Using \(\gcd(k,\nu d)\ge g\) and summing \(d\) harmonically, or using the trivial divisor bound when \(Hg/\sqrt{kT\nu}\) is bounded, gives
\[
 |S_{k,\nu}|\ll_B M\log(2+M)
       \Bigl(1+\frac{Hg}{\sqrt{kT\nu}}\Bigr)^{-B}.
\]
For any fixed \(\delta_0>0\), this discards, with arbitrary power savings in the full weighted aggregate, the pairs satisfying
\[
 \frac{\nu}{(k,\nu)^2}\le \frac{H^2}{kT}\,T^{-\delta_0}.
\]
Indeed the decay is \(O(T^{-B\delta_0/2})\), and the total of the triangle bounds before this gain is \(O(yT\log^{O(1)}T)\) by harmonic summation. The condition includes \(\nu\le T^{2\kappa-1-\theta-\delta_0}\) uniformly in \(k\), up to fixed scale constants. It also includes \(\nu=p^j\) with \(p\mid k\) and \(j\le2v_p(k)\), since \(\nu/(k,\nu)^2\le1\) there and \(\delta_0\) can be chosen smaller than \(2\kappa-1-\theta\). This part works for every fixed \(\kappa\) in the original range.

## Exact polar cancellation and a pointwise bound with an adjustable transition

There is a second bound, useful for larger \(\nu\). For a unit \(v\bmod q\), use the divisor Dirichlet series
\[
 Z(s;v/q)=\sum_{n\ge1}d_2(n)e(vn/q)n^{-s}
  =q^{-2s}\sum_{r,t=1}^q e(vrt/q)\zeta(s,r/q)\zeta(s,t/q).
\]
Both polar coefficients at \(s=1\) are independent of \(v\). Indeed, the double pole comes from \(\sum_{r,t}e(vrt/q)=q\), and the two simple-pole contributions from the finite parts of the Hurwitz zeta functions select \(r=q\) or \(t=q\) by finite Fourier orthogonality. The expansion of \(q^{-2s}\) also has no dependence on the numerator. Consequently \(Z(s;v/q)\) minus its unit average is entire.

On \(\Re s=-B\) for any fixed \(B>0\), apply the Hurwitz zeta Fourier expansion there. It writes each factor \(\zeta(s,r/q)\) as a linear combination of absolutely convergent sums \(\sum_{n\ge1}e(\pm nr/q)n^{s-1}\), with coefficients bounded by \(O_B((1+|\Im s|)^{1/2+B})\) by Stirling. For any residues \(h,j\), the finite Fourier sum
\[
 \sum_{r,t=1}^q e((vrt+hr+jt)/q)
\]
has modulus \(q\), since summing over \(t\) fixes the unique residue \(vr+j=0\bmod q\). This gives the uniform bound \(O_B(q^{1+2B}(1+|\Im s|)^{1+2B})\) for the series and its centered difference. [Hurwitz zeta Fourier expansion, DLMF §25.11](https://dlmf.nist.gov/25.11)

For \(F(x)=w_T(2\pi\nu x/k)\), set \(\Delta=H/T\). Mellin integration by parts in the logarithmic coordinate gives
\[
 |\widetilde F(-B+it)|\ll_{B,j} M^{-B}(1+\Delta|t|)^{-j}.
\]
The bound without integrations uses the compact support \(x\asymp M\). In the integrated bound each derivative costs at most \(\Delta^{-1}\). Shift the Mellin contour of the centered difference to \(-B\). There are no poles, and the horizontal edges tend to zero by rapid Mellin decay and polynomial vertical bounds for the finite collection of Hurwitz zeta products. Taking \(j>2+2B\) bounds the result by
\[
 |S_{k,\nu}|
 \ll_B q\,\Delta^{-2}\Bigl(\frac{q^2}{M\Delta^2}\Bigr)^B .
\]
The case that \(M\) is less than a fixed positive constant gives an empty original sum, and need not be bounded by this estimate. For all other \(M\), use \(q^2/M\ll y^2\). Thus for each prescribed \(\varepsilon>0\), one can choose \(\kappa<1\) sufficiently close to 1 and then fixed \(B>0\) sufficiently small, so that this bound is \(O_\varepsilon(q T^\varepsilon)\). Explicitly the exponent overhead is \(2(1-\kappa)+2B(\theta+1-\kappa)\). This is a permissible choice for the earlier saddle and endpoint comparisons. It is not an arbitrarily small \(T^\varepsilon\) loss at a preassigned, fixed \(\kappa\) bounded away from 1. Also,
\[
 |S_{k,\nu}|\ll M\log(2+M)
\]
by the ordinary divisor sum and the bound 2 for the bracket. Both bounds hold uniformly for all gcd blocks after the exact reduction to \(q\).

## Two eliminated strata and the remaining obstacle

Every prime factor of a modulus \(k\) in the actual band is at least \(Y^a\), and \(k\) has at most four distinct prime factors. For each such \(p\), the \(j\) with \(p^j\ll kT\) form a set of bounded cardinality, with bound depending only on \(a,b\). Using \(qT^\varepsilon\le kT^\varepsilon\) for each, the total weighted shared-prime contribution is \(O(yT^\varepsilon\log^3T)=o(T)\) after choosing \(\varepsilon<1-\theta\).

For genuine higher powers with \(\nu=p^j\le T\), \(j\ge3\), use the pointwise \(kT^\varepsilon\) bound and the count \(O(T^{1/3}\log T)\). For \(\nu>T\), use the bound \(M\log(2+M)\) and
\[
 \sum_{\substack{p^j>T\\j\ge3}}\frac{1}{p^j}\ll T^{-2/3}\log T,
\]
which follows from the same count on dyadic shells. Since \(\Lambda(\nu)\log^2\nu=O(\log^3T)\) throughout the actual support \(\nu\ll kT\), these two ranges give \(O(yT^{1/3+\varepsilon}\log^{O(1)}T)=o(T)\) for \(\varepsilon<2/3-\theta\). Primality estimates are unnecessary for this counting step. The same argument applied to all squares gives \(O(yT^{1/2+\varepsilon}\log^{O(1)}T)\), which does not reach the target for \(\theta>1/2\).

The remaining problem concerns the coprime \(\nu=p\) and \(\nu=p^2\) outside the short-factor cutoff. A basic obstruction to an estimate by individual character bounds can already be seen at divisor argument \(s=1\), with squarefree \(k\asymp y\) in the band. Its primitive-character terms have Gauss size \(\sqrt k\) and normalization \(1/\varphi(k)\). Even a hypothetical uniform pointwise bound of square-root size \((kT)^{1/2}T^\varepsilon\) for each prime sum yields a triangle-inequality budget \(T^{1/2+\varepsilon}\) per \(k\) after the extra \(1/k\). There are order \(y/\log^4T\) such weighted moduli, by using four distinct primes from a fixed multiplicative subinterval near \(Y^b\) and the prime number theorem. The proportion of primitive characters at these squarefree moduli tends to 1, since their prime factors tend to infinity. The resulting absolute-sum budget exceeds \(T\log^4T\). This calculation identifies the limitation of that approach; the actual signed sum may be smaller through joint cancellation over characters or moduli.

The removed strata are unconditional estimates for the smooth signed sum. The application to the derivative-weighted fourth moment still uses the earlier RH contour reduction and an estimate for the remaining two prime strata.
