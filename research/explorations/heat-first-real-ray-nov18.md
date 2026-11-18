# The first real zero at large negative de Bruijn–Newman time

**Proposed theorem.** In the standard Polymath15 normalization, the first positive real zero of \(H_{-b}\) exists and is simple for all sufficiently large \(b\). It satisfies
\[
 x_1(-b)=2 y_0 b+\frac{F''(y_0)}{2F'(y_0)}+O(b^{-1})
 =0.63883005360059357748537349728704913113745\ldots\, b
  +26.4644379427396792460766166281250724670\ldots+O(b^{-1}).
\]
Here \(F(y)=\Phi(iy)\) and \(y_0\) is its unique zero in \((0,\pi/8)\). For every fixed \(2y_0<c<\pi/4\), exactly one positive real zero of \(H_{-b}\) lies in \([0,cb]\) for sufficiently large \(b\). The macroscopic slope differs from the \(\pi/4\) extrapolation for the *first* real zero suggested in the discussion of surviving real zeros in Polymath15. The high-index half-integer and Airy patterns studied in that discussion concern a different regime. [Polymath15 discussion, 31 December 2018](https://terrytao.wordpress.com/2018/12/28/polymath-15-eleventh-thread-writing-up-the-results-and-exploring-negative-t/) · [Kernel normalization](https://arxiv.org/abs/1904.12438) · [Directed numerical certificate](check_heat_first_ray_nov18.py)

## A uniform interior saddle

Use \(H_t(x)=\int_0^\infty e^{t u^2}\Phi(u)\cos(xu)\,du\) with
\[
 \Phi(u)=\sum_{n\ge1}(2\pi^2n^4e^{9u}-3\pi n^2e^{5u})e^{-\pi n^2e^{4u}}.
\]
The theta transformation makes \(\Phi\) even. It is analytic on \(|\Im u|<\pi/8\), and decays faster than any exponential on either horizontal end of each compact substrip, by the series on the right and evenness on the left. Its derivatives have the same bounds on smaller substrips. Thus for every real \(|y|<\pi/8\) shifting the full Fourier integral from the real axis to \(\Im u=y\) gives exactly
\[
 \frac{2\sqrt b}{\sqrt\pi} e^{b y^2}H_{-b}(2by)
 =\sqrt{b/\pi}\int_{\mathbb R}e^{-b w^2}\Phi(w+iy)\,dw.
\]
On each compact subinterval of \((-\pi/8,\pi/8)\), Taylor expansion with the bounded fourth derivative and Gaussian moments yields \(F(y)-F''(y)/(4b)+O(b^{-2})\), uniformly with one \(y\)-derivative by the same argument with the fifth derivative. The reality of \(F\) follows from evenness and conjugation. The sign and simple-root results proved below then give uniqueness, and a first-order Taylor expansion at \(y_0\) gives the formula for the corresponding physical zero. The uniform limit also excludes every other real zero on each compact range of interior rays.

## The first kernel zero and the rest of the cusp

The 192-bit Arb checker evaluates \(F\) on all 3,170 adjoining closed intervals of width \(10^{-4}\) from zero to 0.317. Each interval has strictly positive image. It proves \(F'<0\) throughout the next forty intervals to 0.321 and \(F(0.321)<0\). For orders zero, one and two it sums the first sixteen kernel terms; for the rest their absolute values are bounded by \(10^5 n^8 e^{-4n^2/5}\) throughout this range because \(\pi\cos(4y)>4/5\). The ratio of consecutive majorants for \(n\ge17\) is below one half. Bisection and a final evaluation give
\[
 y_0=0.31941502680029678874268674864352456556872\ \pm 6.0\cdot10^{-42},
 \qquad F'(y_0)=-259.1967971748293290413412681099013767324\ \pm 9\cdot10^{-38}.
\]
The additive displacement displayed above has certified error below \(5\cdot10^{-38}\).

For the rest of the interval a modular transformation gives a sign right up to the open endpoint. Put \(D=1+4Y^2\), \(Y=\tfrac12\tan(\pi/4+2y)\), \(P_k=\pi(k+1/2)^2\), and \(\epsilon_k=(-1)^{k(k+1)/2}\). With \(q(y)=e^{iy}\vartheta_3(0\mid i e^{4iy})\) one has
\[
 q(y)=\sqrt2\,D^{1/4}\sum_{k\ge0}\epsilon_k e^{-P_kY},
 \qquad F(y)=-\frac{q''(y)+q(y)}{16}.
\]
Indeed for \(\tau=i e^{4iy}\), \(-1/(\tau+1)=-1/2+iY\). Applying the theta translation and inversion \(\vartheta_3(\tau)=\vartheta_4(\tau+1)=(-i(\tau+1))^{-1/2}\vartheta_2(-1/(\tau+1))\) cancels the phases exactly. The second identity follows by twice differentiating the original theta series. As \(Y'=D\), the contribution to \(q''+q\) from each term, after extracting \(\sqrt2 D^{5/4}\), is
\[
 \epsilon_k e^{-P_kY}Q_k(Y),\qquad Q_k(Y)=3-12P_kY+P_k^2(1+4Y^2).
\]
For \(y\ge0.321\) one has \(Y\ge3.45\). Here \(Q_0/Y^2>1/50\) by direct evaluation at 3.45 and monotonicity. For \(k\ge1\), \(|Q_k|/Y^2<10P_k^2\). The ratio of the sum of absolute errors to the positive leading term is at most \(500\sum_{k\ge1} P_k^2 e^{-(P_k-P_0)Y}<1\). Indeed the first summand with its prefactor is below one half, and successive unscaled terms have ratio at most \((5/3)^4e^{-4\pi Y}<1/2\). These strict elementary inequalities are also checked with directed arithmetic. Thus \(F(y)<0\) on the entire remaining interval. This classifies all interior-ray positive real zeros; the contour argument degenerates as the saddle reaches \(\Im u=\pi/8\).

The neighboring regimes have separate proofs. A [modular cusp and signed-moment argument](heat-real-cusp-nov18.md) forces many real crossings near speed \(\pi/4\). The [Airy expansion](heat-real-airy-edge-nov18.md) locates each fixed-index successor through four terms, and the [periodic theta profile](heat-real-half-integers-nov18.md) identifies one simple crossing per half integer in every fixed supercritical slope interval.

## A finite heat-time enclosure

At the actual time \(t=-10^{16}\), the same directed checker puts the first positive real zero in \(6\,388\,300\,536\,005\,962.240\pm0.002\). To make the Taylor error explicit, on \(|\Im u|\le0.34\) one has \(|\Phi(u)|\le M=10^6\). By evenness take \(U=e^{4\Re u}\ge1\). Then \(\pi\cos(4\Im u)>0.6\), so each exponential is bounded by \(e^{-0.3U-0.3n^2}\). Both powers of \(U\) are at most \(U^3\), with \(U^3e^{-0.3U}<50\). To sum the remaining majorant bound the first three \(n^4\) terms by 98 and sum \(n^4 e^{-1.2n}\) for the tail. The generating function and the resulting strict substrip bound are checked directly. Take Cauchy radius \(r=0.01\). On \(0\le y\le0.321\) all needed horizontal derivatives of \(\Phi\) have bounds \(k! M r^{-k}\). For the normalized heat function in the contour identity, the errors from \(F,F'\) are respectively at most \(M/(2br^2)\) and \(3M/(2br^3)\). The previous adjoining intervals remain positive or strictly decreasing with these added allowances. At each endpoint \(x=2by_0+F''(y_0)/(2F'(y_0))\pm0.001\), the approximation \(F(x/(2b))-F''(x/(2b))/(4b)\) has strict opposite signs after allowing \(3M/(4b^2r^4)\) for the fourth-order remainder. This gives the stated rounded enclosure.
