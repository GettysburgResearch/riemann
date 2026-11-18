# Airy asymptotics for every fixed positive real zero after the first

**Proposed theorem.** In the Polymath15 normalization let \(x_j(-b)\) be the \(j\)-th positive real zero, in increasing order, and let \(0<\alpha_1<\alpha_2<\cdots\) satisfy \(\operatorname{Ai}(-\alpha_j)=0\). Put \(A=\pi/16\). For each fixed \(j\ge2\) the zero is simple for sufficiently large \(b\) and
\[
 \boxed{\displaystyle x_j(-b)=
 \frac{\pi b}{4}-3 A^{1/3}b^{2/3}
 +3^{1/3} A^{-1/9}\alpha_{j-1} b^{4/9}
 +\frac{23}{6} A^{-1/3} b^{1/3}+ O_j(b^{2/9}).}
\]
The [first real zero](heat-first-real-ray-nov18.md) has the smaller limiting speed \(0.6388300536\ldots\). Here the Airy regime is the leading edge of the modular cusp for fixed index, on the side \(x<\pi b/4\). The [separate sign-change estimate](heat-real-cusp-nov18.md) treats a growing number of indices. Polymath15 identified an Airy mechanism for its numerical high-index patterns in different coordinates. [Polymath15, January 2019 discussion](https://terrytao.wordpress.com/2018/12/28/polymath-15-eleventh-thread-writing-up-the-results-and-exploring-negative-t/)

## The merging saddles

Set \(c=\pi/8\), \(d_0=(A/b)^{1/3}\), \(y_*=c-d_0\), \(x_*=2bc-3bd_0\),
\[
 \ell=(d_0^4/(3A))^{1/3},\qquad \eta=\ell/d_0 .
\]
Thus \(d_0=3A\eta^3\). We use the independently derived [modular cusp expansion and global strip bound, equations (1)–(2)](heat-real-cusp-nov18.md). For \(x=x_*+\lambda/\ell\), divide \(H_{-b}(x)\) by the nonzero factor
\[
 -\pi C\ell\,d_0^{-9/2}\exp(by_*^2-xy_*-A/d_0),
\]
where \(C>0\) is the leading constant in that expansion. Call the quotient \(U_b(\lambda)\). Uniformly on compact subsets of complex \(\lambda\),
\[
 U_b(\lambda)=f(\lambda)+\eta\left[-\tfrac{23}{6} f'(\lambda)
              -\tfrac{\lambda^2}{3}f(\lambda)\right]+O(\eta^2),
 \qquad f(\lambda)=\operatorname{Ai}(-\lambda). \tag{1}
\]

Use the full Fourier integral with its factor \(1/2\), and shift to \(u=i y_*+\ell z\), \(z=s-i\), \(s\in\mathbb R\). This contour is lower than the merging saddle, so the limiting cubic integral has Gaussian decay. The cusp parameter is \(d_0+i\ell z\). The central constant in the exponent is the one in the normalization. The linear terms from the Gaussian, Fourier phase, and \(-A/(d_0+i\ell z)\) then sum to \(i\lambda z\) since \(A/d_0^2=bd_0\). The quadratic terms cancel since \(A/d_0^3=b\). The cubic and quartic terms are \(-iz^3/3\) and \(-\eta z^4/3\). The algebraic amplitude from the cusp is \((1+i\eta z)^{-9/2}=1-(9/2)i\eta z+O(\eta^2|z|^2)\) locally. The cusp's own analytic error is \(O(d_0(1+\eta |z|))\). Thus the first correction to the integral against \(e^{i(\lambda z-z^3/3)}dz/(2\pi)\) is the multiplier \(-(9/2)iz-z^4/3\).

Here are uniform estimates justifying the expansion. Write \(d=d_0+\ell\) and \(w=\ell s\). For \(|w|\le2d\), the modulus of the normalized integrand is bounded by a constant times
\[
 \exp\{-(b-A/d^3)w^2 + |\Im\lambda|\,|s|\}.
\]
Indeed the ratio of cusp exponent moduli between \(w\) and \(0\) is \(\exp(Aw^2/[d(d^2+w^2)])\); the algebraic amplitude ratio is at most one up to a uniform constant. The normalized modulus at \(w=0\) stays bounded by the expansion at \(z=-i\), uniformly on compact \(\lambda\)-sets. Since \((b-A/d^3)\ell^2\to1\), the displayed bound is integrable uniformly in \(s\). For \(|w|>2d\) use the global strip bound \(O(d^{-5/2})\) in place of the modular expansion. Relative to the same normalization this costs a power of \(b\) times \(e^{A/d}\), while the Gaussian contributes \(e^{-bw^2+O(|w|/\ell)}\). Since \(b d^2\ge A/d\gg b^{1/3}\) up to fixed constants and \(b d\ell\to\infty\), this entire tail is exponentially small. On \(|s|\le\eta^{-1/12}\), the neglected exponent after the quartic term is \(O(\eta^2|z|^5)\). Expanding the exponential and the algebraic amplitude through first order costs \(O(\eta^2(1+|z|^{10}))\) times the integrable Gaussian majorant. Outside this range that majorant gives an error smaller than any power of \(\eta\).

The shifted cubic integral is the standard Fourier contour for \(\operatorname{Ai}(-\lambda)\), since \(z\mapsto-z\) moves it onto a line above the real axis in the usual Airy representation. Its first correction equals \(-(9/2)f'-f^{(4)}/3\). The Airy equation \(f''=-\lambda f\) yields (1). Each simple root \(\alpha_j\) has by Rouché a unique nearby root of \(U_b\), necessarily real by conjugation symmetry. Equation (1) then puts it at \(\alpha_j+(23/6)\eta+O_j(\eta^2)\), and excludes other zeros on every compact real interval whose endpoints avoid the Airy zeros. Conversion back to \(x\) gives the displayed four terms with remainder \(O_j(\eta^2/\ell)=O_j(b^{2/9})\).

## Excluding additional real zeros before this edge

The interior-ray result excludes any extra positive real zeros on a compact range of rays \(x/b<2c\). It remains to consider sequences \(x/b\to2c\) with \((x-x_*)\ell\to-\infty\). For each such sequence take the unique solution \(d>d_0\) of
\[
 x=2b(c-d)-A/d^2 .
\]
One has \(d\to0\) and \((d-d_0)/\ell\to\infty\). For the latter assertion, if \(d-d_0=O(\ell)\), Taylor expansion at \(d_0\) would give \((x_*-x)\ell=O(1)\). Put \(q=b-A/d^3\). Then \(d\sqrt q\to\infty\) and \(A/(d^4 q^{3/2})\to0\). If \(d/d_0\) stays bounded away from one, use \(q\gg b\) and \(A/(d_0^4b^{3/2})=O(b^{-1/6})\). If \(d/d_0\to1\), use \(q\ell^2\sim(d-d_0)/\ell\) and \(A/d_0^4=1/(3\ell^3)\).

Shift now to \(u=i(c-d)+w\). The saddle equation cancels the linear phase. After extracting the nonzero central factor \(-\tfrac12 C d^{-9/2}\exp(b(c-d)^2-x(c-d)-A/d)\), the integral is asymptotic to \(\sqrt{\pi/q}\). Indeed on \(w=s/\sqrt q\) for fixed real \(s\) the exponent tends to \(-s^2\) after cancellation, by the cubic bound just established, and the algebraic ratio tends to one. Throughout \(|w|\le2d\) the same modulus argument as above gives \(O(e^{-q w^2})\). The remaining Gaussian tail is negligible since \(b d^2\ge A/d\) and \(b d^2\ge b d_0^2\asymp b^{1/3}\). Consequently the real heat function is strictly negative on each such sequence eventually. This excludes any intervening root. Combining this exclusion with (1) on compact \(\lambda\)-intervals and the earlier unique interior zero proves the index assignment for all fixed \(j\ge2\).
