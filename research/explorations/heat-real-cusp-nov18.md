# Many real zeros at the cusp speed at large negative time

**Proposed theorem.** In the normalization \(H_t(x)=\int_0^\infty e^{tu^2}\Phi(u)\cos(xu)\,du\), fix \(\epsilon>0\). As \(b\to\infty\) there are
\[
 \gg_\epsilon\frac{\sqrt b}{\log b}
\]
distinct sign-changing zeros of \(H_{-b}\) in \(((\pi/4-\epsilon)b,(\pi/4+\epsilon)b)\) on the positive axis, after intersecting with that axis if necessary. In particular the \(j\)-th positive real zero satisfies \(x_j(-b)/b\to\pi/4\) for **every fixed \(j\ge2\)**, counting with or without multiplicities. The first zero has a smaller slope as proved in the [interior-ray theorem](heat-first-real-ray-nov18.md). This gives a rigorous low-index limit and a growing count near the speed suggested by the Polymath15 negative-time computations. The finer high-index spacing and Airy patterns are outside this proof. [Polymath15 negative-time discussion](https://terrytao.wordpress.com/2018/12/28/polymath-15-eleventh-thread-writing-up-the-results-and-exploring-negative-t/)

## The cusp and a moving interior sample

Write \(c=\pi/8\), \(F(y)=\Phi(iy)\), and \(A=\pi/16\). The modular transformation in the interior-ray theorem gives, for \(z\to0\) in every fixed sector \(|\arg z|\le\theta<\pi/2\),
\[
 F(c-z)=-C z^{-9/2}e^{-A/z}(1+O_\theta(z)),\qquad C>0. \tag{1}
\]
Indeed \(Y=\tfrac12\cot(2z)=1/(4z)+O(z)\), \(D=1+4Y^2\), and the leading term is proportional to \(-D^{5/4}Q_0(Y)e^{-\pi Y/4}\), with \(Q_0(Y)\sim 4P_0^2Y^2\). The transformed theta series is normally convergent there and all remaining modes are exponentially small relative to the first. The power uses the branch positive on the positive real axis. Also
\[
 \sup_{w\in\mathbb R}|\Phi(w+i(c-d))|\ll d^{-5/2}\qquad(0<d<1/10). \tag{2}
\]
For \(w\ge0\) this follows from \(\cos(4(c-d))\gg d\) and \(\sum_{n\ge1} n^j e^{-q n^2}\ll_j q^{-(j+1)/2}\) for \(j=2,4\), with \(q\asymp d e^{4w}\). The leftover power of \(e^w\) is at most one. Evenness and conjugation handle \(w<0\).

For each fixed \(h>0\), uniformly for \(x\) in the unit interval beginning at \(2b(c-h b^{-1/4})\), put \(d'=c-x/(2b)\). The contour-shift identity of the companion theorem implies
\[
 \frac{2\sqrt b\, e^{x^2/(4b)}H_{-b}(x)}
      {\sqrt\pi\,F(c-d')}
 \longrightarrow \exp\{-A^2/(4h^4)\}>0. \tag{3}
\]
In fact the integrand after the change \(w=u/\sqrt b\) is \(e^{-u^2}F(c-d'-iu/\sqrt b)/F(c-d')\). For fixed \(u\), (1) gives limit \(e^{-u^2}e^{i A u/h^2}\). On \(|u|\le d'\sqrt b/2\) the quotient has magnitude \(\ll \exp(Au^2/(b d'^3))\) by (1) and the exact real part of \(1/(d'+iw)\); thus \(e^{-u^2/2}\) times a constant dominates for \(b\) large. On the complement (2), the Gaussian tail, and (1) at \(d'\) give total \(O(b^{O(1)}e^{-b d'^2/4+O(1/d')})=o(1)\). This proves (3) by the Gaussian Fourier transform, uniformly since \(d'=h b^{-1/4}+O(1/b)\).

## Small signed moments and the cost of too few changes of sign

Set \(d=b^{-1/2}\), \(y=c-d\) and \(X=(2c+\epsilon)b\). Write
\[
 d\nu(x)=H_{-b}(x)e^{yx-by^2}\,dx.
\]
On the unit interval \(I\) of (3) one has
\[
 |d\nu/dx|\ge \exp\{-(h^2+o(1))\sqrt b\}. \tag{4}
\]
Indeed \(b(y-x/(2b))^2=(h^2+o(1))\sqrt b\), and the logarithm of the remaining factor in (3) is \(O_h(b^{1/4}+\log b)\).

For every complex \(|z|\le d/4\), Fourier inversion on a horizontal line gives
\[
 \int_{\mathbb R} e^{z(x-2by)}\,d\nu(x)=\pi e^{bz^2} F(y+z).
\]
Both sides are analytic on this disk by the kernel decay and horizontal contour shifts. By (1) the right side has modulus \(\ll b^{O(1)}e^{-(A/3)\sqrt b}\), as \(\Re(1/(d-z))\ge 1/(3d)\). Cauchy's estimate bounds the \(k\)-th centered moment by this quantity times \(k!(4\sqrt b)^k\).

Suppose there are \(m\le\sqrt b\) sign changes in \([0,X]\), and let \(P(x)=\prod_{j=1}^m(x-r_j)\) with one factor for each sign-changing root there. Multiple zeros of even order require no factor. Then \(H_{-b}P\) keeps a single sign on \([0,X]\). In the coordinate \(x-2by\), the absolute values of the coefficients of \(P\) are bounded termwise by those of \((z+C_\epsilon b)^m\). Since \(k!\le b^{k/2}\) for \(k\le m\), the centered moment bounds give
\[
 \left|\int P\,d\nu\right|\le b^{O(1)}(C'_\epsilon b)^m e^{-(A/3)\sqrt b}. \tag{5}
\]

For \(x\ge X\), shift the Fourier contour to height \(y'=c-d/2\) and apply (2). This bounds the absolute density by \(b^{O(1)}\exp[-(d/2)(x-b(y+y'))]\). At \(X\) its exponent is at most \(-\epsilon\sqrt b/2\). Since \(|P(x)|\le x^m\le X^m e^{m(x-X)/X}\), for \(m=o(\sqrt b)\) the integral over this tail is bounded by \(b^{O(1)}X^m e^{-\epsilon\sqrt b/2}\). On the other tail \(x\le0\), the original Fourier integral gives \(|H_{-b}(x)|\ll1\); using \(|P(x)|\le X^m e^{m|x|/X}\) gives an exponentially smaller bound \(O(X^m e^{-by^2})\).

Remove from \(I\) intervals of radius \(1/(4(m+1))\) about each \(r_j\). At least one half of its length remains, with \(|P|\ge[4(m+1)]^{-m}\). By (4) and the single sign on \([0,X]\), its integral there has absolute value at least
\[
 \tfrac12[4(m+1)]^{-m} e^{-(h^2+o(1))\sqrt b}.
\]
Choose \(h^2<\tfrac14\min(A/3,\epsilon/2)\). This lower bound exceeds the sum of the full signed moment bound (5) and both tail bounds whenever \(m\le c_\epsilon\sqrt b/\log b\) for a sufficiently small positive \(c_\epsilon\). Indeed \(m\log(C'_\epsilon b)+m\log(4(m+1))\le (3/2+o(1))c_\epsilon\sqrt b\). The contradiction proves the stated count on \([0,X]\). For a strict upper endpoint use \(\epsilon/2\) in that argument. The interior-ray theorem removes at most one positive zero below \((2c-\epsilon)b\). Letting \(\epsilon\downarrow0\) gives the individual limits from both sides.
