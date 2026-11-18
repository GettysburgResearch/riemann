# How long a hypothetical off-line zero survives heat flow

**Proposed theorem for independent review.** Write
\[
 F_u(s)=\mathbb E\,\xi(s+V),\qquad V\sim N(0,2u),\qquad F_0=\xi .
\]
In Polymath15's convention \(F_u(1/2+iz)=8H_{4u}(2z)\). If \(\xi(1/2+\delta+iT)=0\), \(0<\delta<1/2\), \(T\ge100\), and \(0\le u\le c\delta^2/\log(2T)\), then \(F_u\) has a zero in the open disk of radius \(\delta/2\) about that zero. Here and below absolute positive constants are unevaluated. In particular the classical de Bruijn–Newman constant satisfies \(\Lambda\ge c'\delta^2/\log(2T)\). No separation, simplicity or isolation of the zero is required.

This addresses the persistence calculation in Polymath15, Remark 9.4 and §10. A recent preprint reports the explicit lower bound \(\delta^2/(70\log T\log\log T)\) by a zero-dynamics argument. Here the reverse Gaussian gives the logarithmic height scale directly and locates a surviving zero. The [one-sided refinement](nov18b-heat-drift.md) gives a stronger conclusion for larger horizontal defects. [Polymath15](https://arxiv.org/abs/1904.12438) · [Cross-Energy of Dirichlet Partial Sums, Part 35](https://hexagonmath.org/2610.00207)

## Two exact Gaussian identities

Let \(\Phi\) be the even bilateral theta density for \(\Xi(z)=\xi(1/2+iz)\), with Fourier kernel \(e^{izv}\). Multiplication by \(e^{uv^2}\) gives \(F_u(1/2+iz)\). For \(u>0\) the two transform identities are
\[
 F_u(s)=\int_{\mathbb R}g_u(h)\xi(s+h)\,dh,\qquad
 \xi(s)=\int_{\mathbb R}g_u(h) F_u(s+ih)\,dh,\qquad
 g_u(h)=(4\pi u)^{-1/2}e^{-h^2/(4u)}.                 \tag{1}
\]
Fubini follows from the double-exponential theta tails. In the second formula the Gaussian restores the Fourier multiplier \(e^{-uv^2}\). We write \(L=\log(2T)\).

We record growth and anchor bounds used also in the refinement. Put
\(G(s)=s(s-1)\pi^{-s/2}\Gamma(s/2)/2\) and \(\alpha=G'/G\). For \(0<u\le1/L\), \(-10\le\sigma\le12\), and \(v\in\mathbb R\),
\[
 |F_u(\sigma+iv)|\le
   \exp\{-\pi|v|/4+C\log(2+|v|)+Cu\log^2(2+|v|)\}.          \tag{2}
\]
Indeed, Stirling in the right half-plane, reflection \(\xi(s)=\xi(1-s)\) on the left, and polynomial growth of zeta on bounded strips give
\[
 |\xi(\sigma+r+iv)|\le e^{-\pi|v|/4}(2+|v|)^C
                 \exp(C|r|\log(2+|v|+|r|)).
\]
For the angular factor in Stirling use \(|v|\arctan((1+|\sigma+r|)/|v|)\le1+|\sigma+r|\). Bounded arguments of the entire function are harmless. In the Gaussian integral absorb \(C|r|\log(2+|r|)\) into \(r^2/(8u)+C'\), uniformly for \(u\le1\), then complete the square.

For \(v\asymp T\), \(T\) sufficiently large, set
\[
 D_u(s)=F_u(s)/(G(s)e^{u\alpha(s)^2}).
\]
Then \(|D_u(4+iv)-1|<0.8\). To see this, tilt the Gaussian in the first integral of (1) by \(e^{(\Re\alpha)r}\). Its center becomes \(2u\Re\alpha=u\log(v/(2\pi))+O(u/v)\le1+o(1)\). On any fixed \(|r|\le B\), Stirling gives \(G(s+r)/G(s)=e^{\alpha r}(1+O_B(1/T))\). For \(r\ge-2\) the Dirichlet series gives \(|\zeta(4+r+iv)-1|\le\zeta(2)-1<0.65\). After division by \(|e^{u\alpha^2}|\) the absolute Gaussian mass is \(e^{u(\Im\alpha)^2}=1+o(1)\). On \(-B\le r<-2\) the elementary bound \(|\zeta(4+r+iv)|\ll_{B,\epsilon}T^{(-3-r)_++\epsilon}\) suffices by the functional equation and convexity. The tilted Gaussian contributes at most \(e^{-(r-2u\Re\alpha)^2/(4u)}\). Its exponent beats that growth by a fixed multiple of \(L\) since \(r^2/4+|r|/2>(-3-r)_++1\) for \(r<-2\), with harmless \(o(1)\) in the coefficient of \(|r|\). Integration preserves the saving, also for arbitrarily small \(u\), by keeping a fixed fraction of the Gaussian tail. Outside \(|r|\le B\), the original bound above gives the same saving on choosing \(B\) larger than the absolute growth constants. The pure full Gaussian exponential integrates to \(e^{u\alpha^2}\). These estimates prove the anchor assertion.

## A disk without a heat zero

Suppose \(w=1/2+\delta+iT\) and \(F_u\) has no zero in \(B(w,\delta/2)\). By (2) and the anchor at \(4+iT\), Jensen's formula gives \(O(L)\) zeros in the disk of radius 7 about the anchor, using an outer radius 8 and increasing the fixed strip in (2) by one if needed. Divide \(e^{\pi T/4}F_u\) by its finite disk Blaschke product in any zero-avoiding radius between 6 and 7. The quotient's log modulus is bounded above by \(CL\) and at the anchor is at least \(-CL\). Harnack and interior harmonic derivative estimates give absolute bounds \(CL\) for its log modulus and its first two derivatives on radius 5. Each Blaschke numerator has its zero at distance at least \(\delta/2\) from \(w\), and the reflected denominators are uniformly separated. Consequently
\[
 |(\log F_u)'|\ll L/\delta,\quad |(\log F_u)''|\ll L/\delta^2
 \quad\text{on } B(w,\delta/4),\qquad
 |F_u(w)|\ge e^{-\pi T/4-CL(1+\log(1/\delta))}.
\]
For every complex \(|b|\le1\), including points past a possible intervening zero,
\[
 |F_u(w+b)/F_u(w)|\le e^{CL|b|}(1+2|b|/\delta)^{CL}.        \tag{3}
\]
This compares the individual numerators directly. [Disk factorization details](weil-contour-nov18.md)

## Noncancellation at the complex saddle

In the second integral in (1) put \(P(h)=-h^2/(4u)+\log(F_u(w+ih)/F_u(w))\) near zero. With \(r=\delta/32\), the map \(h\mapsto 2ui(\log F_u)'(w+ih)\) maps \(|h|\le r/10\) into itself and is a contraction when \(u\le c\delta^2/L\), by choosing the absolute \(c\) sufficiently small. Its fixed point \(h_0\) satisfies \(P'(h_0)=0\), \(|h_0|\ll uL/\delta\) and \(|P(h_0)|\ll uL^2/\delta^2\). On \(|h|\le2r\), \(|P''+1/(2u)|\le1/(100u)\).

Translate \([-r,r]\) to \(h_0+[-r,r]\) with two straight connectors. The integrand on the translated segment equals \(e^{P(h_0)}\exp(-x^2/(4u)+E(x))\), where \(|E(x)|\le x^2/(200u)\). Integration using \(|e^E-1|\le |E|e^{|E|}\) gives relative error less than \(1/10\) from the full Gaussian mass. Its truncated tails and the two connectors cost \(O((1+r/\sqrt u)e^{-c_1r^2/u})\) in the same relative units, for an absolute \(c_1>0\). Here \(r^2/u\gg L/c\).

For real \(r\le |h|\le1\), (3) bounds the log gain over \(|F_u(w)|\) by \(CL(|h|+\log(1+2|h|/\delta))\le C'Lh^2/\delta^2\). For \(|h|>1\), (2) and the lower bound at \(w\) give a log gain \(O(L(1+\log(1/\delta))+|h|+u\log^2(2+|h|))\). In both regions the Gaussian leaves at least \(-h^2/(8u)\) net decay. The normalized total relative to \(|F_u(w)|\) is \(O(e^{-c_2 r^2/u})\). Decreasing \(c\) makes \(|P(h_0)|\le c_2r^2/(2u)\), so the tails cannot cancel the saddle. Equation (1) therefore gives \(\xi(w)\ne0\). The result holds at any smaller bounded \(T\) by the same estimates with enlarged constants, using compact nonvanishing of the anchor as \(u\downarrow0\).

The argument quantifies what a genuine displaced zero would imply. It does not determine whether one exists.
