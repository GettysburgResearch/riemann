# A sharper explicit dyadic critical-line derivative moment

Let \(Z(t)\) be the real Hardy function, with phase and normalization as in the earlier effective proof. Let
\[
 \mathcal T(Y)=\sum_{\substack{\rho=1/2+i\gamma\\|\gamma|>Y}}
  \frac{|\zeta'(\rho)|^2|2^{1-\rho}-1|^2}{1/4+\gamma^2}.
\]
The sum uses distinct critical-line zeros and is unconditional. Multiple zeros have zero contribution. For \(T\ge100\), set \(H=\log T\) and \(r=\min(1/4,\,2/H)\). Then the full two-sign dyadic block satisfies
\[
 \sum_{\substack{\rho=1/2+i\gamma\\T<|\gamma|\le2T}}
           |\zeta'(\rho)|^2|2^{1-\rho}-1|^2
 \le 3600\,TH/r^3.                                                     \tag{1}
\]
For \(Y\ge100\) put \(h=\log Y\) and \(b=\log2\). Summation gives the explicit tail
\[
 \boxed{\mathcal T(Y)\le \frac{3600}{Y}
 \left[128(h+b)+\frac{2h^4+8bh^3+36b^2h^2+104b^3h+150b^4}{8}\right].}   \tag{2}
\]
For \(Y\ge e^8\), one may drop the term \(128(h+b)\). For general \(Y\), one may sum the dyadic blocks below \(e^8\) using \(r=1/4\), then apply the bound without that term from the first dyadic endpoint above \(e^8\). This keeps the \(\log^4Y/Y\) order and reduces its coefficient. The earlier effective proof and its arithmetic checks remain unchanged. [Earlier explicit tail](prime64_explicit_log4_tail.md)

## Local Hardy mean square

The holomorphic extension is \(\mathcal Z(w)=A(1/2+iw)\zeta(1/2+iw)\), where
\[
 A(s)=\pi^{-(s-1/2)/2}\exp\{(\log\Gamma(s/2)-\log\Gamma((1-s)/2))/2\}.
\]
The gamma logarithms are holomorphic on the right half plane. On the enlarged real height interval \(I=[0.89T,2.01T]\) and horizontal offsets \(d=\sigma-1/2\), \(|d|\le r\), we claim
\[
 \int_I|A(\sigma+it)\zeta(\sigma+it)|^2\,dt\le68\,TH.                \tag{3}
\]
First, for \(a>0,b_0\ne0\), comparison of the digamma series with the integral of \((x+a+ib_0)^{-1}\) gives
\[
 |\psi(a+ib_0)-\log(a+ib_0)|\le \int_0^\infty
       \frac{dx}{(x+a)^2+b_0^2}\le \frac{\pi}{2|b_0|}.
\]
Indeed the difference on each unit interval between the left-endpoint value and the integral is at most the integral of the modulus of the derivative on that interval. The difference between the limiting log of the upper endpoint and \(\log N\) vanishes. Since \(s/2\) and \((1-s)/2\) have real parts in \([1/8,3/8]\) and imaginary parts of modulus \(t/2\), both real digamma values differ from \(\log(t/2)\) by at most \(\pi/t+(9/32)t^{-2}\). Also \(\partial_\sigma\log|A|^2=-\log\pi+(\Re\psi(s/2)+\Re\psi((1-s)/2))/2\). The bounds on \(I\) give
\[
 \left|\partial_\sigma\log|A|^2-\log T\right|
 \le\log(2\pi/0.89)+\pi/89+(9/32)/89^2<2 .
\]
Integrating from the critical line yields \(|A(\sigma+it)|^2\le(5/3)T^d\).

Next truncate the Euler sum at \(M=\lceil T/2\rceil\), so \(T/2\le M\le0.51T\). Write \(P(s)=\sum_{n\le M}n^{-s}\). The same Euler identity used in the previous explicit proof gives \(P\), the pole term \(M^{1-s}/(s-1)\), the edge term \(-M^{-s}/2\), and the periodic Bernoulli integral \(-s\int_M^\infty B_1(\{x\})x^{-s-1}dx\). For the Fourier phase \(\phi_n(x)=\pm2\pi n x-t\log x\), \(|\phi_n'(x)|\ge2n\) because \(t/M\le4.02\), and \(|\phi_n''(x)|=t/x^2\). Integration by parts gives for each sign
\[
 \left|\int_M^\infty e^{i\phi_n(x)}x^{-\sigma-1}dx\right|
 \le M^{-\sigma-1}\left(\frac{2}{2n}+
           \frac{t}{4n^2M(\sigma+2)}\right)
 \le \frac{3}{2n}M^{-\sigma-1}.
\]
The Fourier coefficients have modulus \(1/(2\pi n)\). Abel damping justifies passage to the original bounded Bernoulli function by dominated convergence. With \(\sum n^{-2}\le2\) this bounds the integral without the \(s\) factor by \(3M^{-\sigma-1}/\pi\). The bounds \(|s|/M\le4.04\), \(M/t\le0.51/0.89\) then give \(|\zeta(s)-P(s)|\le6M^{-\sigma}\), including both the edge and pole terms. Hence
\[
 \int_I |A(\zeta-P)|^2\,dt
 \le 1.12T\cdot(5/3)\cdot36 M^{-1}(T/M^2)^d
 \le 1.12\cdot120 e^2<1000.
\]
Here \(1/T\le T/M^2\le1\) and \(|d|\le2/H\).

For the main polynomial use the Gaussian centered at \(1.45T\) with width \(V=0.8T\). On \(I\) the Gaussian is at least \(e^{-0.49}\). Its whole-line Gram matrix has entry moduli \(\sqrt\pi V\exp[-V^2(\log(n/m))^2/4]\). Since \(|\log(n/m)|\ge |n-m|/M\), after division by \(\sqrt\pi V\) each row sum is at most \(1+2\sqrt\pi M/V\), by comparison of the decreasing Gaussian sum with its integral. Applying \(2|uv|\le |u|^2+|v|^2\) gives
\[
 \int_I|P(\sigma+it)|^2\,dt\le
 e^{0.49}\sqrt\pi V(1+2\sqrt\pi M/V)\sum_{n\le M} n^{-1-2d}
 < 7.6T\sum_{n\le M}n^{-1-2d}.
\]
After multiplying the coefficient norm by \(T^d\), monotone integral comparison, with upper endpoint \(T\ge M\), gives
\[
 T^d\sum_{n\le M}n^{-1-2d}
 \le e^{dH}+H\frac{\sinh(dH)}{dH}
 \le e^2+H\frac{\sinh2}{2}<3.5H.
\]
The ratio has continuous value one at zero. Thus \(\int_I|AP|^2\le45TH\). Since \(1000\le2.2TH\) for \(T\ge100\), Minkowski's inequality gives (3) from \((\sqrt{45}+\sqrt{2.2})^2<68\).

## Discrete moment by a cutoff and Rolle's theorem

For each integer \(0\le j\le2\), Cauchy's integral formula on the radius-\(r\) circle in \(w\), followed by Cauchy–Schwarz in its angular parameter, yields
\[
 \int_{0.9T}^{2T}|Z^{(j)}(t)|^2\,dt
 \le68(j!)^2 TH\,r^{-2j}.
\]
For \(j=0\) the formula is the mean-value bound. Every angularly shifted real interval remains inside \(I\) and its \(s\)-real part satisfies the offset bound in (3).

Let \(\varphi=1\) on \([T,2T]\) and let \(\varphi(t)=3x^2-2x^3\) for \(x=(t-0.9T)/(0.1T)\) on \([0.9T,T]\). Then \(\varphi(0.9T)=\varphi'(0.9T)=0\), \(0\le\varphi\le1\), \(|\varphi'|\le15/T\), and \(|\varphi''|\le600/T^2\) almost everywhere. The product \(f=\varphi Z\) is continuously differentiable, its derivative is absolutely continuous, and \(f'=Z'\) on the block \([T,2T]\). Use the endpoint \(0.9T\) with \(f'=0\) before the first selected zero. Rolle gives a stationary point of \(f\) within each subsequent gap between selected zeros. Integrating \((f'^2)'=2f'f''\) from each such point to the right zero gives
\[
 \sum_{T<\gamma\le2T}|\zeta'(1/2+i\gamma)|^2\le 2\|f'\|_2\|f''\|_2 .
\]
The intervals in this argument are disjoint and all norms are over \([0.9T,2T]\). With \(G=(68TH)^{1/2}\) the product rule gives
\[
 \|f'\|_2\le G(1/r+15/T),\qquad
 \|f''\|_2\le G(2/r^2+30/(Tr)+600/T^2).
\]
Reflection and \(|2^{1-\rho}-1|^2<6\) give (1), since
\[
 24\cdot68(1+15r/T)(2+30r/T+600r^2/T^2)<3600
 \quad (r/T\le1/400).
\]
All the critical-line zeros in the block are real zeros of \(Z\), with no need for separation or RH. The upper bound handles a first zero in the block even if its predecessor is below the interval. [Earlier unlocalized Rolle argument](prime64_explicit_log4_tail.md)

To sum (1) take the disjoint dyadic blocks \(T=2^jY\), divide by \(T^2\), and bound \(r^{-3}=\max(64,H^3/8)\le64+H^3/8\). The sums of \(j^k2^{-j}\) for \(k=0,1,2,3,4\) are \(2,2,6,26,150\), from differentiation of the geometric series. This gives (2). If \(Y\ge e^8\), every block uses \(r=2/H\) and the exact maximum selects \(H^3/8\).

## Certified size and integration splice

For \(Y=100\), the radius-switched version of (2) is less than \(24{,}959\), compared with the previous explicit bound \(1.715\cdot10^8\). Together with the height-100 derivative certificate this gives \(C_2\in[0.25253801685456458,24959]\) for the series, unconditionally. RH identifies the series with the scaled prime-array limit. The leading coefficient of the new upper bound is \(900\) when written as \(\log^4Y/Y\) times a function with an explicit limit. The earlier leading upper coefficient was \(6.24\cdot10^6\).

A sufficient 1% target relative to the previously certified lower bound is \(0.0025253801685456458\). At \(Y=2\cdot10^{11}\), the new analytic tail is below \(0.002312\), so a complete finite derivative sum through that height with width below \(0.00021\) would meet the target. This reduces the previous sufficient cutoff \(6\cdot10^{15}\). No zero list was computed for this sharpening. [Height-100 finite derivative sum](prime64_finite_remainder.md)

To replace analytic block bounds by finite integral certificates, write \(I_j=\int_{0.9T}^{2T}|(\varphi Z)^{(j)}|^2dt\) for \(j=1,2\). Certified upper endpoints \(J_j\ge I_j\) give a rigorous contribution at most \(24\sqrt{J_1J_2}/T^2\) from that block. Apply the analytic tail to the first dyadic endpoint beyond the validated blocks. The companion script uses Arb integration on the two polynomial pieces of \(\varphi\), or just checks the arithmetic constants when run without optional blocks. It integrates the holomorphic square of the derivative, which equals the real squared derivative on the integration path. For complex evaluations the callback explicitly restricts \(|\Im w|<1/4\), ensuring the log-gamma branches are holomorphic and the zeta pole is outside. [Reproducible checks](../../scripts/prime64_sharper_moments_checks.py)

For the first block \((100,200]\), a 64-bit Arb integration with FLINT 3.6.0 gave \(24\sqrt{I_1I_2}/100^2<2.22\). The analytic tail at 200 is less than \(14348.279\). This first splice alone gives \(\mathcal T(100)<14350.499\), and retaining the same finite derivative sum gives \(C_2<14351\) for the series. The companion script repeats the integral at this height with the flag --blocks 1. The checked arithmetic is at 128 bits.

The same run on the second block \((200,400]\) gave contribution \(<2.13\). Using the full Arb precision of both integral bounds and the analytic tail from 400 gives \(\mathcal T(100)<8248.95\) and
\[
 \boxed{C_2\in[0.25253801685456458,\ 8249.21]}
\]
for the derivative series. This splice uses only finite dyadic integrals and the previously certified height-100 zero sum. Its numerical check is --blocks 2. Each interval is split into pieces of width at most 50 before integration to keep the evaluations finite.
