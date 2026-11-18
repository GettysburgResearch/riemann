# Positive Gaussian averages of the actual 5:3 Möbius detector

Status — Proposed all-scale arithmetic positivity theorem with a finite interval checker, and a separate exact asymptotic criterion.

Let \(w(v)=5c_{e^v}(2)+3c_{e^v}(3)\) for \(v\ge0\), extended by zero for \(v<0\). For \(U,\epsilon>0\) set
\[
 g_\epsilon(U)=\int_\mathbb R
   \frac{\exp[-(v-U)^2/(4\epsilon U)]}{\sqrt{4\pi\epsilon U}}w(v)\,dv .
\]
Then **\(g_\epsilon(U)>0\) for every \(U>0\) and every \(\epsilon\ge10^{-6}\)**. The variance in logarithmic coordinates is \(2\epsilon U\). The kernel depends on the center, which changes the relation between the transform and the zeros.

The finite spectral certificate also proves positivity of the **unsmoothed** row for every real \(2<X\le2\cdot10^{13}\), by the quantitative deconvolution in Section 4.\n\nThere is also an exact formula for the infimum of parameters giving *eventual* positivity:
\[
 \epsilon_*=\sup_{\rho=\beta+i\gamma}
    \frac{\max(\beta-1/2,0)}{\gamma^2-(\beta-1/2)^2}.
 \tag{1}
\]
The supremum runs over nontrivial zeta zeros. The denominators are positive since \(|\gamma|>14\). The published zero census to height \(3\cdot10^{12}\) gives \(\epsilon_*<5.56\cdot10^{-26}\). Thus even at \(\epsilon=5.56\cdot10^{-26}\) the averages are strictly positive for all sufficiently large centers. RH is equivalent to \(\epsilon_*=0\). The possible positive value below the verified upper bound remains unresolved. [Platt and Trudgian, The Riemann hypothesis is true up to \(3\cdot10^{12}\)](https://arxiv.org/abs/2004.09765)

## Arithmetic data

The physical source and its transform on \(\Re s>1/2\) are
\[
 \begin{split}
 q(n)&=6{\bf1}_{n=1}-6\mu(n)+9{\bf1}_{2\mid n}\mu(n/2)
                         -3{\bf1}_{4\mid n}\mu(n/4),\\
 w(v)&=\sum_{n\le e^v}q(n)n^{-1/2}(v-\log n),\\
 F(s)&=\frac{H(s)}{s^2},\quad H(s)=6+\frac{P(1/2+s)}{\zeta(1/2+s)},\quad
 P(z)=-3(2^{-z}-1)(2^{-z}-2).
 \end{split}
\]
Let \(A=H(0)>6\) and \(B=H'(0)>-1\). On the critical strip \(P\) never vanishes. [Frozen 5:3 row identity](https://github.com/GettysburgResearch/riemann/blob/433fd3662f7b2e4ba384ce64f196380e88624090/claims/lemmas/L-99261-five-three-row-zero-free-mellin-witness.md)

## 1. A finite rectangle determines the large-center sign

Write \(p_\epsilon(s)=s+\epsilon s^2\). The Gaussian Fourier identity and the initial absolutely convergent transform give
\[
 g_\epsilon(U)=\frac1{2\pi i}\int_{1-i\infty}^{1+i\infty}
                       e^{U p_\epsilon(s)}F(s)\,ds .
 \tag{2}
\]
For instance Fourier inversion applies to \(e^{-v}w(v)\), since \(F(1+it)=O((1+t^2)^{-1})\). Its inverse integral can be integrated against the Gaussian by absolute convergence.

Fix \(\epsilon>0\). Choose \(0<b<\min(1,1/(2\epsilon))\) and \(H_0\) sufficiently large that \(1+\epsilon-\epsilon H_0^2<-1\), keeping the lines \(\Re s=-b\) and \(\Im s=\pm H_0\) away from poles in the finite rectangle. The two tails on the initial line contribute \(O(e^{-U})\) by absolute integrability. The finite horizontal segments satisfy the same bound, as \(\sigma+\epsilon\sigma^2\) on \([-b,1]\) is maximized at 1. The bounded left segment contributes \(O(e^{(-b+\epsilon b^2)U})\). The double pole at zero supplies \(AU+B\). The remaining terms are the residues of nontrivial shifted zeros in the rectangle, each an exponential \(e^{U p_\epsilon(s_\rho)}\) times a polynomial in \(U\), where \(s_\rho=\rho-1/2\). Every pole with \(\Re p_\epsilon(s_\rho)\ge0\) is crossed, since
\[
 \Re p_\epsilon(s_\rho)=a+\epsilon(a^2-\gamma^2),\qquad a=\Re\rho-1/2.
\]
In particular such a pole has \(a>0\), and the choice of height includes it.

If \(\epsilon>\epsilon_*\), all nonreal residues in this finite sum decay exponentially, including their polynomial factors. We obtain
\[
 g_\epsilon(U)=AU+B+O_\epsilon(e^{-d_\epsilon U})
\]
for some \(d_\epsilon>0\). If \(0<\epsilon<\epsilon_*\), the largest crossed real exponent \(\lambda\) is positive. Among the poles attaining it select the largest order \(m\). After division by \(e^{\lambda U}U^{m-1}\) the leading sum is a nonzero real trigonometric polynomial with zero mean, up to \(o(1)\). Indeed each leading Laurent coefficient is multiplied by \(p_\epsilon'(s_\rho)^{m-1}/(m-1)!\ne0\). Distinct leading poles have distinct images under \(p_\epsilon\), since equal images for distinct points would force their sum to equal \(-1/\epsilon\), while both have positive real part. Their imaginary frequencies \(\gamma(1+2\epsilon a)\) are nonzero. A finite real trigonometric polynomial of this kind attains both signs bounded away from zero on every sufficiently long interval: its first mean is \(O(1/L)\) and its second mean tends uniformly on intervals of length \(L\) to a strictly positive sum of squared coefficients. Boundedness then gives uniformly positive averages of both one-sided parts. Thus \(g_\epsilon\) has exponentially large values of each sign in every sufficiently long interval of large centers. These two implications give the infimum (1) without deciding the sign at equality.

For the numerical asymptotic upper bound, any off-line zero has \(|\gamma|>3\cdot10^{12}\) by the cited census, while \(a<1/2\). Substitution in (1) gives \(\epsilon_*\le(1/2)/[(3\cdot10^{12})^2-1/4]<5.56\cdot10^{-26}\). This use of the large census is separate from the following all-center certificate, which only requires ordinates through 2000.

## 2. A certificate at \(\epsilon=10^{-6}\) for \(U\ge4\)

Use (2) with the rectangle \(-1\le\Re s\le1\), \(|\Im s|\le2000\). The [checker](check_detector_diffusion_nov18.py) verifies the complete set of 1517 positive ordinates below this height with indexed FLINT enclosures, the exact critical real parts and nonzero derivative enclosures. Together with their conjugates the sum of the absolute residues of \(F\) at these shifted zeros is less than \(0.37\). Their exponential factors have modulus \(e^{-\epsilon\gamma^2 U}\le1\). The checker also encloses \(|F|<1\) on each of 256 closed boxes covering the upper horizontal line. Conjugation covers the lower line.

The right tails satisfy \(|F(1+it)|\le40/(1+t^2)\) by \(|1/\zeta(3/2+it)|\le\zeta(3/2)<3\). After division by \(2\pi\), the total contribution of right tails and both horizontal lines has modulus at most \(2e^{-2U}\), since \(1+\epsilon-\epsilon(2000)^2<-2\).

On the left line the functional equation and the gamma recurrence give the exact modulus
\[
 |\chi(-1/2+it)|=\frac{\sqrt{1/4+t^2}}{2\pi},
 \qquad \zeta(z)=\chi(z)\zeta(1-z).
\]
Thus \(|1/\zeta(-1/2+it)|\le4\pi\zeta(3/2)<38\). Here \(|P(-1/2+it)|\le3(1+\sqrt2)(2+\sqrt2)<25\). We obtain \(|F(-1+it)|\le 956/(1+t^2)\); the left contribution has modulus less than \(500e^{-0.99U}\). The residue from zero is \(AU+B\), and the checker verifies \(A>6,\ B>-1\). Consequently
\[
 g_\epsilon(U)>6U-1-0.37-500e^{-0.99U}-2e^{-2U}>0\quad(U\ge4).
\]

## 3. The native prefix for \(0<U\le4\)

The checker verifies nonnegativity of \(w\) up to \(v=8\). It sieves the exact Möbius coefficients, updates the piecewise-constant derivative and integrates it to every knot through \(\log3000>8\). The source is zero through \(\log2\) and the later knot values are positive; linearity fills the intervals. On \([1,21/20]\) precisely the \(n=2\) term contributes, giving \(w(v)=(15/\sqrt2)(v-\log2)>3\).

For \(v\ge0\), \(|w(v)|\le96e^{v/2}\). To see this, use \(|q(n)|\le24\) and compare the decreasing nonnegative summand \(x^{-1/2}(v-\log x)\) with its integral from 1 to \(e^v\) plus its first value. The resulting bound is \(24(4e^{v/2}-4-v)\le96e^{v/2}\).

Write \(d=4\epsilon U\le16\cdot10^{-6}\) and omit the common positive Gaussian normalizing factor. The contribution from \([1,21/20]\) is at least \((3/20)e^{-9/d}\), since \(|v-U|\le3\) there. The possible negative contribution from \(v\ge8\) is at most
\[
 96 e^4\frac{e^{-16/d}}{8/d-1/2},
\]
using \((v-U)^2\ge16+8(v-8)\). The ratio of this upper bound to the positive term is at most \(640 e^4e^{-7/d}<1\). All remaining contributions up to 8 are nonnegative. This proves the claimed strict sign on the entire small-center range.

## 4. Finite unsmoothing without enumerating the arithmetic interval

The preceding spectral certificate implies a statement about the original arithmetic function at **every real** \(X\le2\cdot10^{13}\):
\[
 w(\log X)=0\quad(1\le X\le2),\qquad
 w(\log X)>0\quad(2<X\le 2\cdot10^{13}).
 \tag{5}
\]
In particular its cumulative negative mass is zero through that endpoint.

More generally take an integer \(H\ge2000\) and assume the following two finite predicates: all positive ordinates below \(H\) are simple critical zeros with total signed-ordinate absolute \(F\)-residue sum below 1, and \(|F(\sigma+iH)|<1\) for \(-1\le\sigma\le0.51\), with no zero on that segment. Then (5) extends through \(X=5H^4/4\). The indexed root count must pass the height before termination. The earlier 2000-height checker verifies these predicates. The [height-parameterized checker](check_detector_unsmoothed_prefix_nov18.py) verifies them for additional heights.

**Lower bound for the average.** Use \(\epsilon=2/(3H^2)\) and the same finite rectangle, now moving the right line in (2) to \(0.51\), still inside absolute convergence. On the right \(|F(0.51+it)|\le1200/|0.51+it|^2\), by \(\zeta(1.01)<101\) and the bounded dyadic numerator. The two omitted right tails and two horizontal segments together, including \(1/(2\pi)\), contribute at most \(e^{-0.15u}\) at center \(u>0\): their unweighted integrals total at most \(2(1200)/H+2(1.51)<2\pi\), and \(\max_{\sigma\in[-1,0.51]}(\sigma+\epsilon\sigma^2-\epsilon H^2)<-0.15\). The left estimate from Section 2 is at most \(500e^{-0.99u}\). Since the spectral residue sum is below 1 and the critical zeros have purely imaginary shifted frequencies, it follows that
\[
 g_\epsilon(u)\ge Au+B-1-500e^{-0.99u}-e^{-0.15u}>6.5u
 \qquad(u\ge8).
\]
For the last strict comparison the checker gives \(A>6.77,\ B>-0.5\); at \(u=8\) the inequality holds and its margin increases thereafter.

**Pointwise deconvolution.** Write \(t=\epsilon u\), \(X=e^u\). With the nonnegative hinge correction \(R_t\) in Section 6, the exact difference \(g_\epsilon(u)-w(u)\) is \(\sum q(n)n^{-1/2}R_t(u-\log n)\). To retain the arithmetic sparsity, the four residue classes \(n\equiv 2^j\pmod{2^{j+1}}\), \(0\le j\le3\), have \(|q(n)|\le v_j\) where \(v=(6,15,12,3)\); all other classes contribute zero. Thus \(\sum v_j=36\) and \(\sum v_j/2^{j+1}=135/16\).

For \(f(x)=x^{-1/2}R_t(u-\log x)\), its sum on any positive arithmetic progression of spacing \(b\) is bounded by \(b^{-1}\int_0^\infty f(x)dx+\operatorname{Var}(f)\). Integrate the deviation from each sampled value on the interval extending one spacing to its right to see this bound. The integral is \(4\sqrt{X}(e^{t/4}-1)\). In fact \(R_t''=G_t-\delta_0\) with \(G_t\) the centered Gaussian of variance \(2t\). Integrating against \(e^{y/2}\) gives \(\int e^{y/2}R_t(y)dy=4(e^{t/4}-1)\); the boundary terms vanish by Gaussian decay. For the variation, differentiate \(f(e^v)\) in \(v\), substitute \(y=u-v\), and use
\(|R_t'(y)|=\operatorname{erfc}(|y|/(2\sqrt t))/2\le e^{-y^2/(4t)}/2\). This bounds the variation by \(X^{-1/2}[2(e^{t/4}-1)+\sqrt{\pi t}e^{t/4}]\). Hence
\[
 g_\epsilon(u)-w(u)\le
 \frac{135}4\sqrt X(e^{t/4}-1)
 +36X^{-1/2}\left(2(e^{t/4}-1)+\sqrt{\pi t}\,e^{t/4}\right).
 \tag{6}
\]
For \(8\le u\le\log(5H^4/4)\) and \(H\ge2000\), one has \(t<10^{-5}\), since \(\log(5H^4/4)/H^2\) decreases in this range. Use \(e^{t/4}-1\le(t/4)e^{t/4}\): the first term in (6) is at most \((45\sqrt5/16)e^{t/4}u<6.30u\). The second term is less than 0.01 since \(X^{-1/2}\le e^{-4}\). Subtracting (6) from the lower bound for the average proves strict positivity on this whole interval. The native arithmetic prefix through 3000 proves the assertion for \(u<8\), with its initial zero interval accounted for separately. No tabulation through \(5H^4/4\) is used.

## 5. Increasing the variance preserves positivity

For \(s\) real and sufficiently large,
\[
 \widehat g_\epsilon(s)=q_\epsilon'(s)F(q_\epsilon(s)),\qquad
 q_\epsilon(s)=\frac{\sqrt{1+4\epsilon s}-1}{2\epsilon}.
 \tag{3}
\]
Indeed the integral in \(U\) of the Gaussian density times \(e^{-sU}\) is
\(q_\epsilon'(s)e^{-vq_\epsilon(s)}\) for \(v\ge0\), by the elementary Gaussian integral. Fubini holds when \(q_\epsilon(s)>1/2\) by the primitive absolute arithmetic bound.

If \(\eta>\epsilon\), set \(k=\epsilon/\eta\) and \(\phi(s)=k s+(1-k)q_\eta(s)\). Then \(q_\epsilon(\phi(s))=q_\eta(s)\). Differentiation in (3) gives
\[
 \widehat g_\eta(s)=\phi'(s)\int_0^\infty e^{-u\phi(s)}g_\epsilon(u)\,du .
\]
Here \(\phi'(s)=k+(1-k)(1+4\eta s)^{-1/2}\) is the transform of a positive measure with an atom of mass \(k\) at zero. For \(u>0\), \(e^{-u\phi(s)}\) is the Laplace transform of a strictly positive density on \((ku,\infty)\): translate by \(ku\) the inverse Gaussian density
\[
 \frac{z}{\sqrt{4\pi\eta t^3}}\exp[-(t-z)^2/(4\eta t)],\quad
 z=(1-k)u,\quad t>0 .
\]
Its transform is \(e^{-zq_\eta(s)}\) by the same Gaussian integral. Thus the right side is the transform of a positive measure whenever \(g_\epsilon\ge0\). If \(g_\epsilon>0\) for all \(u>0\), the atom already contributes a strictly positive density at every positive time. More explicitly, near each \(U>0\) restrict \(u\) to a small fixed closed subinterval of \((0,U/k)\), where both the inverse Gaussian kernel and \(g_\epsilon\) have uniform positive lower bounds. Uniqueness of Laplace transforms and continuity of \(g_\eta\) give \(g_\eta(U)>0\) for all \(U>0\). Sections 2–3 at \(\epsilon=10^{-6}\) therefore prove the full all-center statement.

## 6. An upper bound for the unsmoothed mass using only local signed curvature

Fix \(\epsilon=10^{-6}\), \(d=0.002\), \(X=e^u\), and write
\[
 R_t(y)=\sqrt{t/\pi}\exp[-y^2/(4t)]
            -\frac{|y|}{2}\operatorname{erfc}\left(\frac{|y|}{2\sqrt t}\right),\qquad
 D^{\rm loc}(u)=\sum_{X^{1-d}\le n\le X^{1+d}}\frac{q(n)}{\sqrt n}
                             R_{\epsilon u}(u-\log n).
\]
Then **for every \(Y\ge1\)**,
\[
 \left|\int_1^Y W(X)_-\,\frac{dX}{X}
 -\int_0^{\log Y}\big(D^{\rm loc}(u)-Au-B\big)_+\,du\right|<2400 .
 \tag{4}
\]
Thus the only curvature charged is the positive signed excess over the actual affine term. The four Möbius dilates in \(q\) are combined before taking this excess.

Indeed \(R_t(y)=\mathbb E[(y+\sqrt{2t}Z)_+]-y_+\) for a standard normal \(Z\), by direct integration. It is nonnegative by convexity and is at most its first displayed term. Applying this identity to each primitive ramp shows the *full* sum \(D(u)\) equals \(g_\epsilon(u)-w(u)\); Fubini follows by the absolute source bound or directly by Gaussian decay. Since \(w_-=(D-g_\epsilon)_+\), the 1-Lipschitz positive-part operation gives the integrated error budget
\[
 \int_0^\infty |g_\epsilon(u)-Au-B|\,du
 \le \frac{0.37}{196\cdot10^{-6}}+\frac{500}{0.99}+1<2394.
\]
Here each of the 1517 conjugate residue pairs has \(|\gamma|>14\) and the remaining terms were bounded on the same contour, valid at every \(u>0\).

For the omitted curvature terms use \(|q(n)|\le24\). Put \(f(x)=x^{-1/2}\exp[-(u-\log x)^2/(4\epsilon u)]\). It increases below \(X^{1-d}\) and decreases above \(X^{1+d}\), since \(d>\epsilon\). On each omitted tail, sum \(f(n)\) by the integral plus one boundary value. Each boundary value is at most \(e^{-1.499u}\). In the upper integral use \(\log x=(1+d)u+y\), \(y\ge0\). Its integrand after change of variable is bounded by
\[
 \exp\!\left[\left((1+d)/2-d^2/(4\epsilon)\right)u
                  -(d/(2\epsilon)-1/2)y\right].
\]
The lower tail has \((1-d)/2\) and \(d/(2\epsilon)+1/2\) in the corresponding positions. Thus the two integrals total at most \(0.0021e^{-0.499u}\). Multiplying by \(24\sqrt{\epsilon u/\pi}\) and integrating in \(u>0\) gives less than \(0.1\), using \(\int_0^\infty \sqrt{u}e^{-pu}du=\sqrt\pi/(2p^{3/2})\). This proves (4).

A qualitative version uses \(d=4\cdot10^{-13}\) and \(\epsilon=5.56\cdot10^{-26}\) instead. Then \(d^2/(4\epsilon)>(1+d)/2\) and \(d>\epsilon\), so the same discarded curvature is integrable. Section 1 and the published height give \(\int_0^\infty|g_\epsilon-Au-B|\,du<\infty\). The resulting two integrals differ by \(O(1)\) uniformly in \(Y\); this smaller-width version has no stated numerical additive constant.

Proving a subpower upper bound for the second integral of (4), even on an unbounded subsequence of horizons, would exclude every off-line zero by the [positive-isolation theorem](detector-positive-isolation-nov18.md). A fixed power saving \(N_W(Y)\ll Y^{1/2-\delta}\) would already exclude every zeta zero with \(\Re\rho>1-\delta\). The classical Vinogradov–Korobov Mertens bound does give the actual unconditional upper bound
\[
 N_W(Y)\ll \sqrt Y\,\exp\left[-c(\log Y)^{3/5}(\log\log Y)^{-1/5}\right]
 \qquad(Y\ge e^e)
\]
for some \(c>0\), by partial summation in the fixed Möbius dilates and logarithmic integration with a smaller \(c\). Equation (4) transfers this known estimate to the localized positive excess with the same form. The missing arithmetic improvement concerns that excess.

The [backward-heat analysis](detector-backward-heat-nov18.md) evaluates the native primitive diagonal, isolates the necessary large reduced ratios, and gives a squarefree counterexample to scale inversion without odd-prime multiplicativity.

## 7. A positive inversion using only one fixed annulus

There is an unconditional upper bound for the unsmoothed mass in terms of a *fixed-width* arithmetic excess. Define
\[
 C_h(v)=\sum_{|\log n-v|\le h}\frac{q(n)}{\sqrt n}
                          \frac{(h-|v-\log n|)^2}{4h}.
\]
For each line in the table there is a finite constant \(C\) such that for all \(T\ge1\),
\[
 \int_0^T w_-\,du
 \le C+(1+cT)\int_{-h}^{(1+ch)T+h}\big(C_h(v)-k\big)_+\,dv .
 \tag{7}
\]

| Log half-width \(h\) | Steps per unit center \(c\) | Threshold \(k\) | Imported critical zero census |
|---:|---:|---:|---:|
| \(1\) | \(1/14\) | \(94\) | height 2000, local checker |
| \(1\) | \(1/56\) | \(379\) | height \(3\cdot10^{12}\) |
| \(10^{-12}\) | \(1/2\) | \(13\) | height \(3\cdot10^{12}\) |

The threshold applies **after** summing the signed primitive weights. For instance in the second row only excess above 379 within a factor \(e\) of the center is charged. Subpower growth of the right-hand integral even on an unbounded sequence of horizons suffices for RH, by applying (7) at the corresponding rescaled cutoffs and using the fixed-row [positive-isolation theorem](detector-positive-isolation-nov18.md). Under RH the Mertens bound gives subpower growth for \(C_h\) and hence the converse. The finite constant in (7) need not equal the 2400 in (4).

**Positive iteration.** Let \(P_h\) denote the probability average on \([-h,h]\). Its Laplace multiplier is \(\Phi_h(s)=\sinh(hs)/(hs)\). The uniform-average hinge identity gives \(P_hw-w=C_h\) on the full real line, including negative centers. For the listed \(h,c\) and \(n(u)=\lfloor cu\rfloor\),
\[
 (P_h^{\,n(u)}w)(u)=Au+B+O(e^{-b_0u})\qquad(u\to\infty)
 \tag{8}
\]
for some \(b_0>0\). Here the power is fixed while evaluating its convolution at a given \(u\). To prove (8) use the inverse integral of \(e^{su}\Phi_h(s)^{n(u)}F(s)\) on \(\Re s=1\). Truncate at fixed sufficiently large heights \(\pm H_1\) away from poles, and move the central segment to \(\Re s=-b\) for sufficiently small fixed \(b>0\). On the original tails and horizontal edges \(|\Phi_h|\le\cosh(h\max(1,b))/(hH_1)\), so \(e^u|\Phi_h|^{\lfloor cu\rfloor}\) decays exponentially after fixing \(H_1\). On the left \(|\Phi_h|\le\sinh(hb)/(hb)\) by the positive integral representation, and \(-b+c\log(\sinh(hb)/(hb))<0\) for small \(b\). Choose the finite contour away from poles. At zero the double-pole contribution is \(Au+B\) because \(\Phi_h(0)=1,\ \Phi'_h(0)=0\).

At each crossed critical zero \(|\Phi_h(i\gamma)|=|\sin(h\gamma)/(h\gamma)|<1\). At each other nontrivial zero \(s_\rho=\rho-1/2\) we have
\[
 |\Phi_h(s_\rho)|\le \cosh(h/2)/(hH_*)\,,\qquad
 \tfrac12+c\log\big(\cosh(h/2)/(hH_*)\big)<0
\]
using its census height \(H_*\) in the table. Thus all nonreal pole contributions decay exponentially. For order \(m\) they include at most polynomial factors in \(u,n(u)\) after differentiation; if \(\Phi_h\) vanishes at the pole, the pole is eventually canceled exactly. Only finitely many poles are crossed. This proves (8).

In each row \(A>ck\), so (8) gives \(P_h^{n(u)}w(u)\ge k n(u)\) at all sufficiently large centers. Telescoping the actual positive operator,
\[
 w_-(u)\le\sum_{j<n(u)}P_h^j(C_h-k)_+(u).
\]
For \(u\le T\) the largest \(j\) is at most \(cT\). Each probability convolution is supported in \([-jh,jh]\), and \((C_h-k)_+=0\) below \(-h\). Integrate, enlarge to the single indicated interval, and add the finite initial negative mass to prove (7). This argument preserves one-sided information when removing the repeated smoothing.

## Verification scope

Run the finite checker at the repository root with python-flint 0.9.0.

    python research/explorations/check_detector_diffusion_nov18.py

The 96-bit ball computation returns total signed-ordinate absolute residue sum \(0.366816599536684361093675\) with printed radius \(5.57\cdot10^{-25}\). Coverage uses FLINT's consecutive indexed zero routine from index one through a certified height above 2000. Finite arithmetic and analytic continuation rely on Arb/FLINT; this is a single implementation. Checker SHA-256 is 5588e799dccd8d35d45942ff4237f211e52e6d2300587bc78d0d9be5a95e3b5e.

The proof supplies global positivity for the stated averages. As the variance is proportional to \(U\), it does not yield an upper bound for the negative mass of the unsmoothed source or exclude an off-line zero above the verified census.

The separate height-parameterized replay at height 20000 completed at 96 bits. Its output was

```text
Completed 22491 zeros below 20000
H=20000, 22491 positive ordinates, residue sum [0.36900019484777974138858 +/- 2.36e-24]
Accepted horizontal boxes=360, certified upper X=200000000000000000
```
