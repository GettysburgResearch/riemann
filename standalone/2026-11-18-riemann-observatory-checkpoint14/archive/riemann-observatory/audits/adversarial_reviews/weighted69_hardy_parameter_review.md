# Independent audit of parameterized global Hardy variation

The parameterized proof with \(r=1607/1000\), \(d=143/500\), \(w=22\), and Cauchy radii \(219/1000,433/1000\) gives an analytic tail upper expression \(0.4590615084631102969276294270054364588\ldots\) at \(Y=10000\). I replayed at 192 bits, checked the complex-rectangle conditions and the signed cubic endpoint terms, and found no failure of either the updated method or the previously reviewed enclosure. The variant with a time-dependent phase inside the Hilbert forms also works, but its upper expression \(0.4753587058905768513\ldots\) at the same parameters is larger. The older independent \(0.49071483259\ldots\) verification is unchanged. [Parameterized implementation](../../scripts/prime69_parameterized_hardy_tail_checks.py) · [Variable-phase check](../../scripts/weighted69_variable_phase_checks.py) · [Prior independent audit](weighted67_global_skeptic.md)

## Admissible parameters and complex dimensions

Set \(T_0=Y-w\), \(M=\lceil dT\rceil\), and \(\rho=\max(a_1,a_2)\). The following sufficient conditions cover the optimizing rational choices:
\[
\begin{gathered}
1<r,\quad d>0,\quad 0<a_1,a_2,\quad \rho<1/2,\quad T_0>e^5,\quad dT_0\ge34,\\
0<w<Y,\quad Y\le rT_0,\quad d^2T_0>1,\quad
r+\rho/T_0<2\pi,\quad (r+\rho/T_0)/d<2\pi .
\end{gathered}
\]
The condition on \(dT_0\) accommodates the explicit first 32 terms in the finite polynomial quadrature. The condition \(Y\le rT_0\) lets the transition use the same rectangle inequalities as a main block. For a block \([T,U]\), \(U\le rT\), every radius-\(\rho\) disk in the complex height variable lies in the rectangle
\[
 \tfrac12-\rho\le \sigma\le\tfrac12+\rho,\qquad
 T-\rho\le v\le U+\rho,\qquad s=\sigma+iv.
\]
The Fourier mode denominators and the Euler pole term have positive bounds throughout this rectangle. In particular, setting \(\sigma_+=1/2+\rho\), use
\[
 c_+(T)=\frac{r+\rho/T}{d},\quad c_-(T)=\frac{1-\rho/T}{d+1/T},\quad
 c_s(T)=c_+(T)+\frac{\sigma_+^2}{2dT(T-\rho)},\qquad
 \frac{M}{|s-1|}\le\frac{d+1/T}{1-\rho/T}.
\]
They bound \(v/M\) above, \(v/M\) below, and \(|s|/M\) above, respectively. The estimate for \(|s|\) follows from \(\sqrt{v^2+\sigma^2}\le v+\sigma^2/(2v)\). Each block may use \(U/T\) instead of \(r\), as the code does. The positive Fourier mode then has strictly positive phase derivative for \(x\ge M\). The negative mode is bounded using the positive lower bound \(c_-(T)\). The original integration-by-parts estimate remains valid because \(x^{-\sigma}/(2\pi nx\mp v)\) is decreasing to zero for \(\sigma>0\) and positive denominators. Its boundary value plus total variation gives twice the boundary value. The coefficients of the Abel-damped Fourier series are bounded by \(1/(2\pi n)\) per sign. Absolute convergence of the integrated series and bounded Poisson convolution justify its use with the remainder.

The scalar Euler remainder constant is consequently bounded by
\[
 \frac{d+1/T}{1-\rho/T}+\frac12+
 \frac{c_s(T)}{\pi}\left[
 \sum_{n=1}^{8}\left(\frac1{n(2\pi n-c_+)}+
                    \frac1{n(2\pi n+c_-)}\right)
 + \left(\frac{\pi^2}{6}-\sum_{n=1}^{8}n^{-2}\right)
   \left(\frac1{2\pi-c_+/9}+\frac1{2\pi}\right)\right].
\]
Both \(c_+\) and \(c_s\) decrease with \(T\), and \(c_-\) increases. Each nonnegative term in the displayed bound decreases as required for the uniform residual. The constants are properties of the rectangle and apply simultaneously on all the smaller Cauchy disks.

The Hardy multiplier satisfies
\[
 |\partial_\sigma\log|A|^2-\log T|
 \le \log\frac{2\pi}{1-\rho/T}+\frac{\pi}{T-\rho}
            +\frac{\sigma_+^2}{2(T-\rho)^2}.
\]
To get this bound, compare each real digamma value with \(\log(v/2)\), using \(\Re s/2\) or \(\Re(1-s)/2\) in its argument. The assumption \(v/T<2\pi\) allows the lower height to majorize the absolute logarithmic deviation. The bound above decreases with \(T\). Integrate horizontally from \(\sigma=1/2\) to get \(|A|^2\le e^{Ka}T^{\sigma-1/2}\) on a radius-\(a\) disk whenever the displayed bound is at most \(K\). The rectangle is simply connected, avoids the gamma poles and zeros, and admits the Hardy square-root choice. The factor \(T^{\sigma-1/2} M^{-2\sigma}\) is maximal at the lowest \(\sigma\), since \(M^2>T\). Using \(M\ge dT\), the bound for the modulus of the Hardy remainder is \(C(T)e^{Ka/2}d^{a-1/2}T^{(a-1)/2}\). This proves the Cauchy constants using the whole disk. For the residual, after normalization this term is proportional to \(C(T)T^{(a-1)/2}(\log T)^{-j-1/2}\), decreasing for each allowed radius.

For the fixed residual envelope \( |\log x-b|\le(\log T+2)/2\), \(1\le x\le2M\), the sufficient conditions are
\[
 \sqrt r\le2\pi,\qquad
 \bigl(2(d+1/T_0)\bigr)^2\frac{2\pi}{\sqrt r}<e^2 .
\]
The lower log endpoint uses \(0<b\le\frac12\log T\). The upper endpoint follows by inserting the phase center \(b=\frac12\log(T\sqrt r/(2\pi))\) and \(M\le dT+1\). These conditions apply on the main ratio blocks. The transition uses the exact log envelopes from finite moments. The normalized polynomial from this envelope is the one checked in the prior audit. The infinite geometric quotient is \(e^{\log r((2j+1)/\log V-1)}<1\), where \(V\) is the first residual base.

At \(Y=10000,w=22\), the 128-bit rectangle check gives \(c_+<5.619032852\), \(c_s<5.619032867\), \(c_->3.495126997\) and multiplier deviation less than \(1.838235333<1.86\). The residual envelope ratio is less than \(1.622812359<e^2\). The first block base \(T_0=9978\) controls the subsequent ones by the monotonicities above.

## Cubic cutoff identity and signed endpoint

Write \(H=G/t\), \(f=\phi H\), and take all derivatives of the cubic on \([Y-w,Y]\) from that interval. Expanding the squared first derivative and integrating the cross term gives
\[
 \|f'\|_2^2=\int\phi^2|H'|^2-\int_{Y-w}^Y\phi\phi''|H|^2 .
\]
The boundary is zero because \(\phi\phi'\) vanishes at both ends. Expanding the squared second derivative and integrating its cross terms yields the interior coefficients \(2\phi'^2-4\phi\phi''\) on \(|H'|^2\) and \(\phi\phi''''=0\) on \(|H|^2\). The boundary term on the transition is
\[
 \left[2\phi\phi''\Re(H'\overline H)
         +(\phi'\phi''-\phi\phi''')|H|^2\right]_{Y-w}^{Y}.
\]
At the lower endpoint this is zero. At \(Y\) it equals
\[
 12|H(Y)|^2/w^3-12\Re(H'(Y)\overline{H(Y)})/w^2 .
\]
This is the boundary term from the one-sided integration, while \(f'\) stays continuous and \(f''\) is interpreted almost everywhere. The interior coefficient is \(24x^3(2-x)/w^2\) with \(x=(t-Y+w)/w\), bounded above by \(24/w^2\). Also \(-\phi\phi''\le6/w^2\). These inequalities prove the majorants in the implementation, including their signed endpoint term.

For \(J(t)=Q_2(1/2+it)\zeta(1/2+it)/t\), one has \(H=A J\). On the real height line, \(|H|^2=|J|^2\) and \(\Re(H'\overline H)=\Re(J'\overline J)\) because \(A'\overline A=i\theta'\) is purely imaginary. The acb Taylor series along direction \(i\) returns the derivative with respect to height. The quotient derivative in the implementation uses \((q'\zeta+q\,d\zeta/dt-J)/t\), which is \(J'\). At 10000, the two enclosed real values are approximately \(2.0555544969291882\cdot10^{-9}\) and \(-3.3946332687903577\cdot10^{-8}\). The second value is negative, so retaining its sign increases the squared-norm bound in this instance.

## Variation of Hilbert coefficients

The alternative variable-phase calculation uses \(x_n(t)=d_nn^{-1/2}(\theta'(t)-\log n)^j\). Its squared weighted norm is the diagonal \(\int wD_j(t)\), \(w=t^{-2}\), plus the integrated off-diagonal. Put \(J_j(t)\) equal to the earlier gap-weighted upper sum for this array, with the sparse parity exception. The fixed Hermitian quadratic Hilbert form has weighted operator norm at most \(3\pi/2\) in the norm squared \(\sum |x_n|^2/\delta_n\). The bound on its bilinear version follows from that Hermitian operator norm by conjugating with the diagonal matrix of gap weights. Integration by parts against the off-diagonal exponentials now gives an upper bound on the off-diagonal of
\[
 \frac{3\pi}{2}\left[
 w(T)J_j(T)+w(U)J_j(U)+\int_T^U |w'|J_j
 + 2j\int_T^U w\,|\theta''| \sqrt{J_jJ_{j-1}}\right].
\]
In the last term differentiate just the amplitude array. Its derivative has gap-weighted norm bounded by \(j|\theta''|\sqrt{J_{j-1}}\). The case \(j=0\) omits that term. The pointwise diagonal and gap-weighted sums are convex in the real phase center because each even log power is convex. The bounds at the two ends of a phase bracket thus suffice for each short slice within a block. The upper bracket \(t\mapsto\frac12\log(t/(2\pi))+\pi/(2t)+1/(16t^2)\) and its lower counterpart both increase for \(t\ge1000\). Slice endpoints give a valid bracket. The endpoint forms use even tighter brackets at the exact times. The \(i\theta''P_0\) term in the second derivative is bounded separately in \(L^2\). For the infinite residual the script reverts to a conservative fixed-center triangle bound with envelope \((\log T+3)/2\), valid by the checked endpoint condition and \(d\le1/2\).

This alternative has its own quadrature and independently evaluated complex Euler constants. It certifies a weaker bound \(0.475359\) with the optimized parameters stated above. The remaining gain comes from the constant-center norm bound and the sharper signed-mode treatment in the parameterized proof. No larger finite census is involved. To replay the alternate bound, run PYTHONPATH=/workspace/riemann-runtime python scripts/weighted69_variable_phase_checks.py --precision 192 --upper .475359 from the repository root.
