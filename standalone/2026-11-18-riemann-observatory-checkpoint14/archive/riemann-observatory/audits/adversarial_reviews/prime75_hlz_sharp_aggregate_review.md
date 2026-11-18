# Sharp continuous input for the HLZ shifted theorem

18 November 2026. I checked the continuous \(J\) interface in Heap–Li–Zhao, journal pp. 1607–1608, §4.1, against Pratt–Robles, arXiv:1706.04593v3, §1.2 and proof §3. The literal smoothed theorem does not by itself supply the claimed arbitrary-log-saving sharp interval. The sharp continuous input needed by HLZ does hold, uniformly for any fixed length exponent below \(1/2\). The direct product approximate-functional-equation proof below avoids all shrinking-cutoff seminorms. It applies to the full bounded coefficient arrays, including the padded polynomials in the prime-moment applications. This review concerns the continuous term only. [HLZ journal PDF](../../sources/classical63_derivative_moments/hlz2022print.pdf) · [Pratt–Robles v3 primary PDF](../../sources/finite_moment63_uniform/pratt_robles_1706.04593v3.pdf)

## Source interface and shrinking transitions

At their (1.2), Pratt–Robles take \(\Phi\) smooth, supported on \([1,2]\), with \(\|\Phi^{(j)}\|_\infty\ll_j(\log X)^j\) at height \(X\). Theorem 1.1 is stated with this weight. For generic coefficients its two error terms are \(X^{3/20}N^{33/20}\) and \(N^{1/2}X^{1/2+\epsilon}\). HLZ §4.1 gives the unweighted integral from \(1\) to \(T\), with the corresponding error sizes, as a rephrasing. One cannot insert a plateau taper of width \(X/(\log X)^B\) with \(B>1\) into the literal stated weight class. Already a normalized transition from 0 to 1 over dimensionless width \((\log X)^{-B}\) needs a first derivative of size \((\log X)^B\) somewhere. At \(B=1\) the main transition mass need not give a log saving of arbitrary order. For \(Q=1\) at zero shifts the main density is \(\log(t/(2\pi))+2\gamma_{m E}\), and a transition interval of length \(X/\log X\) has main mass of order \(X\).

The parts of the Pratt–Robles proof where one would have to track a wider weight class include the repeated time integrations before (3.2), the repeated integrations for large \(h\) in §3.2.2 and in the error of §3.2.4, and Mellin separation of \(\Phi\) in §3.2.3. A finite set of derivative seminorms with polynomial dependence would cost only fixed log powers at fixed \(B\), and the length exponents have power-saving margin for \(N\le X^\vartheta\) with fixed \(\vartheta<1/2\). This expectation is not a statement of the printed Theorem 1.1. The direct proof below does not require a uniform reanalysis of those parts or the precise sharp error exponents quoted by HLZ.

Here is what a smoothing argument would need to accomplish. For \(Y_0=T^\kappa\) with \(2\delta<\kappa<1\), where the polynomial length is \(y\le T^\delta\), decompose \(Y_0\le t\le T\) into dyadic-scale pieces at \(X\). Then \(y\ll X^{\delta/\kappa}\). A version of the smoothed result uniform on plateau and transition majorants with seminorms \(O_j((\log X)^{Bj})\) and power-saving errors would suffice here. At endpoints one can shift the dyadic scale by a bounded factor to put a transition majorant in the interior of its normalized support. The main integrand is \(O_M((\log T)^4)\) on these pieces, by the lcm sum and the separated shifts below. To handle the complex product on a transition, apply Cauchy–Schwarz against the positive local transition majorant and use the shifted square bounds for \((\alpha,\bar\alpha)\) and \((\bar\beta,\beta)\). The transition loss is then \(O(X(\log T)^{4-B})\) plus a power-saving error. Inserting the \(\log(t/(2\pi))\) weight costs at most one more log power. The support \(t<Y_0\) still requires a separate estimate because the polynomial is padded at \(T\), not at \(t\). The local bounds in the direct proof control it. Thus wide-class smoothing with the required uniformity would give the needed conclusion. The narrowly stated theorem alone and an appeal to positivity do not verify those hypotheses.

## Uniform sharp estimate

Fix \(0<\delta<1/2\), \(y\le T^\delta\), \(L=1+\log T\), and \(Q(s)=\sum_{n\le y}a_n n^{-s}\), \(|a_n|\le M\). Write
\[
 F(t)=\zeta(\tfrac12+\alpha+it)\zeta(\tfrac12+\beta-it)
       |Q(\tfrac12+it)|^2,\qquad d=\alpha+\beta .
\]
For complex \(|\alpha|,|\beta|\le c/\log T\) with fixed small \(c>0\), put
\[
 {\cal M}(t)=\sum_{g,h,k:\,gh,gk\le y,\;(h,k)=1}
 \frac{a_{gh}\overline{a_{gk}}}{ghk}
 \left[
 \frac{\zeta(1+d)}{h^\beta k^\alpha}
  + h^\alpha k^\beta(t/2\pi)^{-d}\zeta(1-d)
 \right].
\]
Interpret the bracket by holomorphic extension at \(d=0\). The two residues in \(d\) cancel because the two multipliers agree at \(\beta=-\alpha\). For \(w_0(t)=1\) and \(w_1(t)=\log(t/2\pi)\), the direct result is
\[
 \int_1^T w_j(t)F(t)\,dt
 =\int_0^T w_j(t){\cal M}(t)\,dt
     +O_{\epsilon,c,M}\bigl(T^\epsilon(y\sqrt T+\sqrt y\,T^{3/4})\bigr),
 \qquad j=0,1.                                                     \tag{1}
\]
Uniformity at the poles of the individual summands follows by first proving (1) on the separated circles \(|\alpha|=2c/\log T,\ |\beta|=3c/\log T\). Both sides are holomorphic on the interior product region, so the bound extends to the smaller shift disk by Cauchy or the maximum modulus principle. A locally integrable \(t^{-\Re d}\) majorant justifies holomorphy of the \(t\in(0,1)\) integral there. The same proof works on any comparable sharp subinterval of \([X,2X]\), with \(T\) still setting the length and shifts. Constants depend on the single coefficient bound \(M\), not on support, phases or padding pattern.

### Product AFE and sharp interval integration

Use the product AFE (Pratt–Robles (2.1)–(2.4)) with \(G_d(w)=e^{w^2}(1-4w^2/d^2)\). The normalizations and the uniform first \(t\)-derivative bounds are as in the direct fixed-twist proof. Explicitly, on \(t\asymp X\ge1\), the first weight and the dual weight including its functional-equation multiplier satisfy
\[
 |V(uv,t)|+X|\partial_t V(uv,t)|
    \ll_A L^2\min(1,(X/(uv))^A).
\]
The factor \(L^2\) accounts for the pole annihilator on the separated circles. On fixed Mellin lines of real part \(-1/4,2,A\), Stirling gives powers of \(t\) for the gamma ratio and the digamma difference gives its first derivative with \(1/t\) gain. For \(|\Im w|>t/2\) the Gaussian absorbs the fixed-strip polynomial factors. The relevant gamma factors have positive real parts, and the ratio has no exponential growth from the imaginary gamma magnitudes, since the two denominator heights have opposite signs and the numerator heights translate by the same amount. The negative line gives the residue 1 for \(uv\le X\), with derivative zero for that residue. The positive line gives rapid decay otherwise. The dual prefactor is \((t/(2\pi))^{-d}(1+O(1/t))\), uniformly bounded up to \(T\), with \(t\)-derivative bounded by \(O(1/t)\). The small completed-zeta residues in the AFE are \(O_A(L^2(1+t)^{-A})\); their poles occur at imaginary height of order \(t\) in the Gaussian and contribute that rapid decay after gamma normalization. Since \(|Q(1/2+it)|^2\ll_M y\), the integrated AFE residue error is \(O_M(yL^2)\) with either weight. [Fixed-shift AFE details and contour normalization](prime64_q2_sharp_j.md)

For a sharp subinterval of \([X,2X]\), the \(t\)-integral at an off-diagonal frequency \(K_2/K_1\) is bounded by
\[
 O_A\!\left(\frac{L^3\min(1,(X/(uv))^A)}
                    {|\log(K_1/K_2)|}\right)
\]
by one integration by parts retaining both endpoints. Here \(K_1=mu\), \(K_2=nv\), where \(m,n\le y\) are polynomial indices and \(u,v\) are zeta indices. The coefficients apart from the shifts and \(a_m\overline{a_n}\) are \((K_1K_2)^{-1/2}\). The phase is \((nv/(mu))^{it}\); reflection in the dual still leaves that phase. The shifts cost at most \((uv)^{O(c/\log T)}\). It is important to sum the comparable frequency pairs collectively, before bounding individual twist errors.

For \(uv\le P\) one has \(K_1K_2\le y^2P\). If \(K_1/K_2\in[1/2,2]\), then \(K_i\le\sqrt{2}\,y\sqrt P\), and
\[
 \frac{(K_1K_2)^{-1/2}}{|\log(K_1/K_2)|}
   \ll |K_1-K_2|^{-1}\quad(K_1\ne K_2).
\]
For given \(K_1,K_2\), the factorization multiplicities are at most \(\tau(K_1)\tau(K_2)\), since \(m\mid K_1,n\mid K_2\). The elementary bound \(\tau(n)\ll_\eta n^\eta\) and the harmonic gap sum therefore give \(O_{\eta,M}(y\sqrt P\,(y\sqrt P)^{2\eta}\log(2yP))\), before the shift and AFE weight. Outside comparability, the inverse logarithm is bounded by an absolute constant, and one may sum \(m,n\) absolutely and then \(u,v\); the resulting bound is \(O_M(y\sqrt P\log(2P))\). Use \(P=X\) for the first block and \(P=2^j X\) for the higher product shells, where the Mellin weight has geometric decay in \(j\). The shift factor at \(X\le T\) is bounded at the base and costs only \(2^{jO(c/\log T)}\) thereafter. Choosing fixed \(A\) large and \(\eta\) small proves the unconditional total off-diagonal estimate \(O_{\epsilon,c,M}(T^\epsilon y\sqrt X)\) on each sharp block. No assumption on the image support gaps of the padded polynomials is used.

### Diagonal and the functional-equation correction

Write \(m=gh,n=gk\), \((h,k)=1\). On the diagonal \(u=k\ell,v=h\ell\), \(\ell\ge1\). The first diagonal weight has arithmetic factor \(a_{gh}\overline{a_{gk}}(ghk)^{-1}k^{-\alpha}h^{-\beta}\) and Mellin integral
\[
 \frac1{2\pi i}\int_{(2)}G_d(w)\,g_{\alpha,\beta}(w,t)
                    (hk)^{-w}\zeta(1+d+2w)\frac{dw}{w}.
\]
Move to \(\Re w=-1/4\). The pole at \(-d/2\) is annihilated, the gamma factors have no poles on the crossed strip, and the residue at zero is \(\zeta(1+d)\). By the fixed strip bound for zeta and the Gaussian, the remainder is \(O(L^2(hk/X)^{1/4})\) at \(t\asymp X\). It need not be small at an individual low height. The dual argument gives the corresponding residue with \(d\) reversed and the same remainder bound. Replacing the exact dual prefactor in its residue by \((t/(2\pi))^{-d}\) costs \(O(L/t)\) inside the square bracket. For both sums of diagonal terms,
\[
 \sum_{m,n\le y}\frac1{\operatorname{lcm}(m,n)}
     \le\sum_{g\le y}\frac1g\left(\sum_{h\le y/g}\frac1h\right)^2
     \ll \log^3(2y),
 \qquad (hk)^{1/4}\le\sqrt y .
\]
Thus after integration on a block the diagonal residual is \(O(\sqrt y\,X^{3/4}L^6+L^5)\). Summing the dyadic \(X\) and the off-diagonal bounds proves (1). Extending the main term from 1 to 0 costs \(O_{c,M}(L^4)\), since the powers of \(t\) in the bracket have real exponent greater than \(-1/2\) for large \(T\), and the logarithmic weight is integrable there. For \(y\le T^\delta\) both powers in (1) are strictly below \(T\), after choosing \(\epsilon\) small depending on \(\delta\).

Finally HLZ's initial continuous integrand has an extra \(O(1/t)\) term from \(\chi'/\chi\). To control it uniformly, take the unweighted local sharp bound for the two conjugate-shifted square integrals on \([X,2X]\). From the proof before summing over \(X\), each is
\[
 \ll_{\epsilon,c,M} T^\epsilon(X+y\sqrt X+\sqrt y\,X^{3/4}+y).
\]
At the symmetric shifts that may satisfy \(d=0\), use the same maximum-modulus argument on each block, and bound the main kernel on the outer separated circles by the lcm sum times \(O(L)\). Nonnegativity of the square and Cauchy–Schwarz therefore bound \(\int |F(t)|\,dt\) on that interval by the same expression. Weighting by \(1/X\) and summing dyadically gives \(O_{\epsilon,c,M}(T^\epsilon(y+\sqrt y+\log T))\). It saves a power uniformly in the required lengths and proves the full continuous comparison \(J_{\rm contour}=J_{\rm main}+O_A(T(\log T)^{-A})\) for every fixed \(A\), including the \(1/(2\pi)\) convention in HLZ. No RH hypothesis is needed for this continuous step. Any RH assumptions in the discrete moment applications are separate.
