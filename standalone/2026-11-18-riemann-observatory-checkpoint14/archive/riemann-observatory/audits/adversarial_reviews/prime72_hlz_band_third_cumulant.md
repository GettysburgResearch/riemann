# Third cumulant of a polynomial cosine prime band

18 November 2026. Assume RH and use the symmetric strict derivative-weighted tail on \(|\gamma|>Y\) from the earlier band proof. For fixed \(0<a<b<1/6\), let
\[
 W=\sum_{Y^a<p\le Y^b}\frac{\cos(\gamma\log p)}{\sqrt p},
 \qquad \Delta_j=b^j-a^j .
\]
The third cumulant calculation gives
\[
 \lim_{Y\to\infty} E\bigl[(W-EW)^3\bigr]
 =-8\Delta_1^3+24\Delta_1^2\Delta_3-8\Delta_1\Delta_3^2
      +\frac{16}{27}\Delta_3^3.                                         \tag{1}
\]
The right side is strictly negative, with exact value \(-818904257/864000000000\) on \([1/20,1/10]\). The proof below also supplies the uniform fourth-moment bound needed to use (1) as an obstruction to a Gaussian weak limit. The arithmetic calculation takes its kernels directly from HLZ. It does not use a random-matrix moment as input. Publication priority and higher-moment agreement remain unassessed. [HLZ primary source, Theorem 5 and equations (5), (24)](../../sources/classical63_derivative_moments/hlz2022print.pdf) · [First two band moments](prime71_hlz_band_covariance.md)

## 1. The coefficient for three distinct primes

For a prefix at \(T\ge Y\), write \(x=\log p/\log T,\ y=\log q/\log T,\ z=\log r/\log T\) for three distinct band primes. Set \(D(s)=\sum_{Y^a<p\le Y^b}p^{-s}\), so \(W=\Re D(\rho)\). The exact aggregate identity
\[
 (\Re D)^3=\tfrac14\Re(D^3)+\tfrac34\Re(D^2\overline D)
\]
uses polynomial lengths at most \(Y^{3b}\). All polynomial coefficients have a common absolute upper bound \(6\); the exact divisor-closed padding and four-sign polarization therefore apply at a fixed declared length \(T^\delta\) with \(3b<\delta<1/2\). This yields a common normalized \(o(1)\) analytic remainder for the entire polynomial pairs. The two-sign arithmetic weights and ordered coefficient comparisons are as in the first-two-moment proof. No individual relative prime-character error with numerical factor \(1/(pqr)\) is needed.

For the distinct-prime coefficients in the ordered expansion of \(W^3\), the eight phase-sign assignments for \(p,q,r\) are equally weighted. At each assignment the product of signed phases is represented by \(m^{-\rho}n^{-\bar\rho}\), with each prime assigned to one of \(m,n\), and the lcm is \(pqr\). The factor \(1/(pqr)\) appears in the main coefficient from HLZ before normalizing by the untwisted leading derivative sum. Write \(K_3(x,y,z)\) for the remaining normalized leading polynomial. We obtain
\[
 K_3(x,y,z)=\sum_{\xi\in\{x,y,z\}}F(\xi)-2
       +\sum_{\{\xi,\eta\}}[12\xi\eta-2\xi\eta(\xi^2+\eta^2)]
       -24xyz,                                                        \tag{2}
\]
where \(F(\xi)=1-4\xi+2\xi^3\) and the second sum uses the three unordered pairs.

To extract (2), take scaled shift variables \(\alpha,\beta,c\) on fixed separated Cauchy circles. For a term of \(I\) let \(u,v,w\) be its shifted zeta parameters and \(t\) its limiting exponent from the time power. The quotient of zeta factors before the auxiliary derivative is \((\log T)v/((u+v)(v+w))+O(1)\), uniformly on the scaled circles. At leading order a prime in the \(h\) slot contributes \(e^{-v\xi}\), and one in the \(k\) slot contributes \(e^{-u\xi}+e^{-w\xi}-1\) by the exact local ratio. Thus after phase-sign averaging the \(I\) factor is
\[
 2^{-3}\prod_{\xi=x,y,z}(e^{-v\xi}+e^{-u\xi}+e^{-w\xi}-1).
\]
The tuples \((u,v,w,t)\) are \((\alpha,\beta,c,0)\), \((-\beta,-\alpha,c,-\alpha-\beta)\), and \((\alpha,-c,-\beta,-\beta-c)\), and the reflected \(I\) exchanges \(\alpha,\beta\). The associated integral of the time power divided by \(T\) is \(e^t+O(1/\log T)\). For \(J\) the two averaged arithmetic factors are \(2^{-3}\prod_{\xi}(e^{-\alpha\xi}+e^{-\beta\xi})\) and \(2^{-3}\prod_{\xi}(e^{\alpha\xi}+e^{\beta\xi})\); their respective scaled zeta/time multipliers are \(1/(\alpha+\beta)\) and \(-e^{-\alpha-\beta}/(\alpha+\beta)\). The factor \(\log(t'/(2\pi))\) has been scaled by \(\log T\). The exact comparisons are uniformly \(O(1/\log T+1/p+1/q+1/r)\) after scaling on the circles.

The \(J\) coefficient of \(\alpha\beta\) comes from cubic terms of the exponential numerator divided by \(\alpha+\beta\). The \(I\) coefficient of \(\alpha\beta c\) comes from quartic terms times \(v/((u+v)(v+w))\). To justify selecting these degrees even before simplifying the rational denominators, rotate all the Cauchy circles together. Only their respective total degrees two and three survive. For \(I\), differentiate the resulting homogeneous rational term once in \(c\) at zero, and simplify the sum of terms before reading the \(\alpha\beta\) coefficient. The polynomial identities and exact normalization by \(1/12\) are reproduced in the companion program. Summing the scaled main coefficient errors weighted by \(1/(pqr)\) gives \(o(1)\) uniformly for \(T\ge Y\), because the band harmonic sum is bounded and its smallest prime goes to infinity. [Exact coefficient check](../../scripts/prime72_hlz_third_cumulant_check.py) · [Recorded output](../../experiments/results/prime72_hlz_third_cumulant_check.txt)

## 2. Coincident primes and the strict-tail third cumulant

Write \(X_p=p^{-1/2}\cos(\gamma\log p)\) and \(H=\sum_{Y^a<p\le Y^b}1/p\). In the ordered expansion of \(W^3\), the all-equal terms are negligible by the pointwise bound \(\sum p^{-3/2}=o(1)\) on the band. The exactly-two-equal terms are \(3\sum_{p\ne q}X_p^2X_q\). Since
\[
 X_p^2=\frac{1}{2p}+\tfrac12\Re(p^{-2\rho}),
\]
their non-oscillatory part contributes \(\frac32H E_T W+o(1)\) at the prefix. The \(p=q\) correction from this part is bounded by \(\frac32\sum p^{-3/2}=o(1)\). The other part is estimated in the aggregate by putting \(D_2(s)=\sum_{Y^a<p\le Y^b}p^{-2s}\). The product \(\Re D_2\,\Re D\) equals \(\frac12\Re(D_2D)+\frac12\Re(D_2\overline D)\); its HLZ inputs satisfy the same fixed coefficient envelopes and length \(Y^{3b}\). The leading arithmetic factors at pairs of indices \(p^2,q\) or \(p^2q,1\) are uniformly bounded, also at the repeated prime. For \(p\ne q\), the lcm denominators are \(p^2q\), giving a total \(O(H\sum p^{-2})=o(1)\). If \(p=q\) the lcm is at least \(p^2\), still summing to \(o(1)\). Removal of the equal prime from the original trigonometric product also costs \(o(1)\) pointwise. Thus the surviving exactly-two-equal term is \(\frac32H E_T W+o(1)\), uniformly for \(T\ge Y\).

For the ordered distinct triple sum, fix the scaled logs at \(T=Y\). The difference compared with the actual prefix target is \(O(H^3\log(T/Y)/\log Y)\), from bounded derivatives of \(K_3\) on \([0,b]^3\). The strict Stieltjes integration in the earlier note transfers this to an \(O(H^3/\log Y)\) normalized error, since \(\log(t/Y)\) is integrable against the normalized weight profile \(t^{-2}(\log t)^4\,dt\) uniformly in \(Y\). The constant \(H\) in the coincident-prime term is independent of \(T\), so its transferred contribution is \(\frac32H EW+o(1)\). The tail first and second moments are as in the earlier note, with the raw second diagonal \(H/2\). That diagonal cancels the surviving repeated-prime term upon subtracting \(3(EW^2)(EW)\). Distinct prime sums converge to the corresponding product integrals against \(dx/x\) by Mertens on fixed bands; removing repeated indices from a product sum simply loses \(O(H\sum p^{-2})\).

Let \(K_0(x,y)\) be the cosine raw two-prime kernel, as in the second-moment note. The remaining third cumulant kernel is
\[
 K_3(x,y,z)-K_0(x,y)F(z)-K_0(y,z)F(x)-K_0(z,x)F(y)
     +2F(x)F(y)F(z).
\]
Dividing this polynomial by \(xyz\), to incorporate the three harmonic measures, gives the integrand
\[
 -8+24(x^2+y^2+z^2)-24(x^2y^2+y^2z^2+z^2x^2)+16x^2y^2z^2.
\]
Its integral over \([a,b]^3\) is (1). It is strictly negative pointwise on that cube, because it is at most \(-8+72b^2+16b^6<0\) for \(b<1/6\).

## 3. Fourth moment and implication for Gaussian limits

The fourth absolute moment is bounded uniformly: use \(|\Re D(\rho)|^4\le |D(\rho)^2|^2\). This HLZ polynomial is \(D^2\) with coefficient bound \(2\) and length \(Y^{2b}\), so it is covered for \(b<1/4\) by the same padding argument. The bound uses only boundedness of its main multipliers and the corresponding positive Poisson-model weighted moment of \(|D|^4\). The latter is bounded uniformly because \(H=O(1)\), each centered independent real and imaginary summand is bounded by \(2/\sqrt p\), and their variance sums are bounded. Equivalently expand the fourth centered moments by independence and then add the bounded means. This yields \(E_T|W|^4=O(1)\) uniformly for \(T\ge Y\), hence the same bound on the strict tail by the positive Stieltjes transfer. The means are bounded, so the bound also holds for \(W-EW\).

In particular \(|W-EW|^3\) is uniformly integrable because the tails above a threshold \(R\) contribute \(O(1/R)\). If a subsequence of the centered bands converged weakly to a Gaussian, the first and third moments would converge by uniform integrability. The limit would have mean zero and third moment zero, contradicting (1). The obstruction concerns these polynomial bands. It does not apply to the cumulative scalar with its diverging normalization and weak Gaussian limit, nor does it identify a full limiting distribution for the band. [Cumulative scalar theorem](prime70_hlz_cutoff_extension.md)
