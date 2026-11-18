# Independent audit of the sharper dyadic Hardy moment

The sharpened block bound \(3600\,T\log T/r^3\), with \(r=\min(1/4,2/\log T)\), holds for every \(T\ge100\). The resulting critical-line coefficient tail is unconditional. I reconstructed the strip bound, the cutoff Rolle argument and the radius-switched summation. Exact rational enclosures verify the scalar constants and tail benchmarks. The 1% target at height \(2\cdot10^{11}\) also needs a certified complete finite derivative sum at that height. [Sharper proof](prime64_sharper_moments.md) · [Earlier explicit tail](prime64_explicit_log4_tail.md) · [Height-100 finite certificate](prime64_finite_remainder.md)

## Normalization and strip endpoints

Write \(s=\sigma+it\), \(d=\sigma-1/2\), \(H=\log T\) and \(I=[0.89T,2.01T]\). The gamma logarithm is analytic in the right half-plane and real on the positive ray. The completed functional equation gives \(\zeta(1-s)=A(s)^2\zeta(s)\) for the \(A\) defined in the sharper proof. Since \(A(1-s)A(s)=1\) and \(A\) respects conjugation, \(A(s)\zeta(s)\) is symmetric under \(s\mapsto1-s\), and \(\mathcal Z(t)=A(1/2+it)\zeta(1/2+it)\) is real. At each critical-line zero, differentiating in \(t\) leaves \(iA(s)\zeta'(s)\), of modulus \(|\zeta'(s)|\). The radius-\(r\) circle in the \(w\)-plane is in the holomorphic strip \(|\Im w|<1/2\), including when \(r=1/4\). [Completed functional equation and normalization](https://dlmf.nist.gov/25.4#E3)

For \(z=a+ib\), \(a>0\), \(b\ne0\), subtract \(\int_0^N(z+x)^{-1}\,dx\) from the left-endpoint sum of \((z+n)^{-1}\) for \(0\le n<N\). On each unit interval, the absolute error is bounded by the integral there of \(|(z+x)^{-2}|\). The digamma series and \(H_N-\log N\to\gamma_E\) give
\[
 |\psi(z)-\log z|\le \int_0^\infty\frac{dx}{(x+a)^2+b^2}\le\frac{\pi}{2|b|}.
\]
For both gamma arguments here, \(a\le3/8\) and \(|b|=t/2\). The gap \(\log|z|-\log(t/2)=\frac12\log(1+4a^2/t^2)\) lies between 0 and \(9/(32t^2)\). Differentiating \(\log|A|^2\) gives \(-\log\pi+\frac12\Re(\psi(s/2)+\psi((1-s)/2))\). Its distance from \(\log T\) is at most \(\log(2\pi/0.89)+\pi/89+9/(32\cdot89^2)<2\) uniformly, using \(t\ge89\) and \(2.01<2\pi\). Integration in \(\sigma\) produces \(|A(s)|^2\le T^d e^{2|d|}\le(5/3)T^d\) on both halves of the strip. [Digamma series](https://dlmf.nist.gov/5.7#E6)

## Continuous mean square

The integer cutoff \(M=\lceil T/2\rceil\) satisfies \(T/2\le M\le0.51T\) for \(T\ge100\). Euler summation on \((M,\infty)\) gives the pole term \(M^{1-s}/(s-1)\), the edge term \(-M^{-s}/2\) and the sawtooth integral with factor \(-s\). The identity follows first for \(\sigma>1\) and extends to \(\sigma>0\) away from the pole by absolute convergence of the remainder. Since \(t/M\le4.02\), each Fourier phase \(\pm2\pi nx-t\log x\) has \(|\phi_n'|\ge(2\pi-4.02)n>2n\). The boundary and amplitude derivative in integration by parts cost \(M^{-\sigma-1}/n\) in total. Differentiating \(1/\phi_n'\) costs at most \(tM^{-\sigma-2}/(4n^2(\sigma+2))\), with \(\sigma+2\ge9/4\). Their sum is at most \(\tfrac{3}{2n}M^{-\sigma-1}\). Both Fourier signs, coefficients of modulus \(1/(2\pi n)\) and \(\sum n^{-2}\le2\) give the factor \(3/\pi\). Abel damping preserves the sawtooth bound and allows dominated convergence, while the integrated Fourier series converges absolutely. Because \(|s|/M<4.04\), \(M/|s-1|\le M/t\le0.51/0.89\), and \(4.04(3/\pi)+1/2+0.51/0.89<6\), the three Euler errors total at most \(6M^{-\sigma}\). Thus
\[
 \int_I |A(\zeta-P)|^2
 \le 1.12T(5/3)36\,M^{-1}(T/M^2)^d
 \le 1.12\cdot120e^2<1000.
\]
Here \(T/M\le2\), \(1/T\le T/M^2\le1\), and \(|d|\log T\le2\). [Euler summation source and derivation](prime64_explicit_log4_tail.md#proof-of-the-continuous-bound)

The Gaussian centered at \(1.45T\) with scale \(V=0.8T\) is at least \(e^{-0.49}\) on \(I\). The Fourier Gram matrix row-sum bound follows from \(|\log(n/m)|\ge|n-m|/M\) and the integral majorant
\[
 2\sum_{k\ge1}e^{-V^2k^2/(4M^2)}\le 2\int_0^\infty e^{-V^2x^2/(4M^2)}dx=2\sqrt\pi M/V .
\]
Applying \(2|uv|\le |u|^2+|v|^2\) gives a bound of \(7.6T\) times the sum of squared coefficients. With the Hardy phase included, those coefficients satisfy
\[
 T^d\sum_{n\le M}n^{-1-2d}
 \le T^d\left(1+\int_1^T x^{-1-2d}\,dx\right)
 =e^{dH}+H\frac{\sinh(dH)}{dH}<3.5H .
\]
The integrand is decreasing for \(d\ge-1/4\), and the ratio has the usual continuous value at zero. This is the Hardy phase cancellation on the left half of the strip. The polynomial has squared norm at most \((5/3)\cdot7.6\cdot3.5\,TH<45TH\). The remainder cost \(1000<2.2TH\) holds already at \(T=100\). Minkowski gives \((\sqrt{45}+\sqrt{2.2})^2TH<68TH\).

## Cutoff and two-sign block weight

Cauchy and angular Cauchy–Schwarz give \(\int_{0.9T}^{2T}|Z^{(j)}|^2\le68(j!)^2TH/r^{2j}\) for \(j=0,1,2\). At a fixed angle the horizontal \(s\)-offset is \(-r\sin\theta\) and the height shift is \(r\cos\theta\). The shifted interval is in \(I\), since \(r\le1/4\le0.01T\). The \(j=0\) case also follows directly from the real-line strip bound.

The left cutoff \(3x^2-2x^3\), \(x=10t/T-9\), has derivative bounded by \(15/T\) and second derivative by \(600/T^2\). Its first derivative vanishes at both ends. For \(f=\varphi Z\), \(f'\) is absolutely continuous and vanishes at \(0.9T\). That endpoint serves as the first stationary point, and Rolle supplies a point in each later gap between selected zeros. Integrating \((f'^2)'=2f'f''\) on the disjoint intervals from those points to their right zeros gives \(2\|f'\|_2\|f''\|_2\). The product-rule bounds contribute factors \(1+15r/T\) and \(2+30r/T+600r^2/T^2\) after removing \(r^{-1}\) and \(r^{-2}\), respectively. The 2 in the second factor comes from \(2!\) in Cauchy's bound. Reflection and the weight \(|2^{1-\rho}-1|^2\le(1+\sqrt2)^2<6\) change the overall factor 2 to 24. With \(r/T\le1/400\), the increasing polynomial gives
\[
 24\cdot68(1+15/400)(2+30/400+600/400^2)<3600.
\]
Multiple zeros have vanishing derivative and the argument requires no separation. The strict left and inclusive right endpoints allocate each dyadic boundary zero to exactly one block.

## Dyadic arithmetic and certification

Dividing each block by \(T^2\) is valid termwise. With \(h=\log Y\), \(b=\log2\) and \(T=2^jY\), the sum is bounded by the sum of \(3600\,2^{-j}(h+jb)\max(64,(h+jb)^3/8)/Y\). The Euler derivatives \((x\,d/dx)^k(1-x)^{-1}\) at \(x=1/2\) give \(2,2,6,26,150\) for \(k=0,\ldots,4\). Expanding \((h+jb)^4\) gives coefficients \(2,8,36,104,150\). The loose all-height bound uses \(\max(64,H^3/8)\le64+H^3/8\). The exact switch uses 64 for blocks with \(T<e^8\) and \(H^3/8\) thereafter. At \(Y=100\), the five smaller blocks begin at \(100,200,400,800,1600\). The quartic starts at \(3200\), since \(\log1600<8<\log3200\). Its leading large-\(Y\) upper coefficient is \(3600\cdot2/8=900\).

I independently used rational interval arithmetic. For \(\log x\), reduce \(x=2^k u\) with \(1\le u\le2\) and \(z=(u-1)/(u+1)\). The first 28 terms of \(2\sum_{j\ge0}z^{2j+1}/(2j+1)\) bound \(\log u\) from below, with remaining tail at most \(2z^{57}/[57(1-z^2)]\). The quartic coefficients are nonnegative, so substitution of rational endpoints brackets each tail. Writing \(B\) for the majorant, this gives
\[
 24958.59090232409<B(100)<24958.59090232410,\qquad
 0.00231149948<B(2\cdot10^{11})<0.002312 .
\]
For the other scalar checks, I bounded \(\pi\) with 18 terms plus the alternating-series remainder in Machin's arctangent formula, exponentials with 29 terms and the geometric tail beginning at \(x^{29}/29!\), and square roots with integer square roots on a \(10^{-18}\) grid. These rational checks independently verify the strict scalar inequalities. The companion Arb no-flag run reproduced the height-100 bound with ball radius \(9.05\cdot10^{-34}\). [Companion arithmetic](../../scripts/prime64_sharper_moments_checks.py)

The height-100 majorant plus the certified finite upper endpoint is itself less than 24959, since \(24958.59090232410+0.25253801685456460<24959\). The sufficient width for 1% is \(0.25253801685456458/100=0.0025253801685456458\). At \(2\cdot10^{11}\), \(0.002312+0.00021=0.002522\) is smaller. The companion proof relies on the established height-100 finite certificate for the lower endpoint and supplies no finite sum at the much larger height. [Finite certificate](prime64_finite_remainder.md#one-evaluated-enclosure)

## Optional integral splice

The block contribution bound is \(24\sqrt{J_1J_2}/T^2\), where each \(J_j\) is a certified upper endpoint for the corresponding squared norm integral. The remaining analytic tail starts at the first uncovered dyadic endpoint. The callback passes the installed python-flint acb.integral analyticity contract. It evaluates a holomorphic derivative squared on each polynomial piece separately, so the second derivative jump of the cutoff is outside the interior of either integration interval. On the real path the derivative is real, making the square equal to the squared norm integrand. A guard returns a nonfinite ball unless the entire ball satisfies \(|\Im w|<1/4\), putting both gamma arguments in \(\Re z>1/8\) and keeping the zeta pole outside. This guard applies on every call, including requests for analyticity. The real square root is applied after integration to enclosures of the nonnegative integrals. [Optional integration callback](../../scripts/prime64_sharper_moments_checks.py)

My independent Arb rerun gave a contribution below \(2.22\) for \((100,200]\). The independently bracketed analytic tail from 200 is between \(14348.278\) and \(14348.279\), proving the one-block splice bound \(C_2<14351\) after adding the earlier finite endpoint. I also reproduced the segmented two-block run, which returned the upper-majorant ball \(8248.94\pm0.00448\) and passed the strict bound \(8248.95\) for the tail. Its combination with the finite upper endpoint is below \(8249.21\). [Splice results and rerun command](prime64_sharper_moments.md#certified-size-and-integration-splice)

The 41-record statistics shard was also rechecked against its source hash manifest. The checks changed neither the source scripts nor the canonical registries. [Statistics source hashes](../../sources/analytic64_statistics/SHA256SUMS)
