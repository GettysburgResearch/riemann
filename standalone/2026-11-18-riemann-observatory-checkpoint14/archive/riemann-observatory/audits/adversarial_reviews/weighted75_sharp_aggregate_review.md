# Independent check of the sharp aggregate continuous term in HLZ

A direct product approximate functional equation gives the sharp logarithm-weighted \(J\) term in HLZ with error \(O_\varepsilon(T^\varepsilon[y\sqrt T+\sqrt y\,T^{3/4}])\) for two bounded coefficient arrays supported through \(1\le y\le T^\delta\), fixed \(\delta<1/2\). This verifies the proposed replacement for the sharp-endpoint step in §4.1. It gives a power saving throughout that range and needs no RH, submultiplicativity, or time smoothing. A common fixed divisor-log envelope also suffices by absorption into \(T^\varepsilon\). The review concerns the continuous term, independently of the remaining discrete contour argument and the separate diagonal smoothing lemma. [HLZ Theorem 5 and §4.1, pp. 1605, 1607–1608](../../sources/classical63_derivative_moments/hlz2022print.pdf) · [Primary product AFE representation, Pratt–Robles (2.1)–(2.4)](../../sources/finite_moment63_uniform/pratt_robles_1706.04593v3.pdf) · [Earlier fixed-ratio sharp proof](prime64_q2_sharp_j.md)


Pratt–Robles (1.2) and Theorem 1.1 use a weight \(\Phi(t/X)\) supported in the fixed normalized interval \([1,2]\) with \(\|\Phi^{(j)}\|_\infty\ll_j(\log X)^j\). A transition of dimensionless width \((\log X)^{-B}\) for \(B>1\) cannot fit this first-derivative bound by the mean-value theorem. Thus the cited smoothed statement alone supplies no such arbitrary-log-saving unsmoothing, though a suitable wider weight theorem could. The argument below instead keeps both sharp endpoint terms directly.

## Exact normalization and shifts

Let \(Q_1(s)=\sum_{r\le y}a_r r^{-s}\), \(Q_2(s)=\sum_{s'\le y}b_{s'}(s')^{-s}\), with \(|a_r|,|b_{s'}|\) bounded by a common number. Write \(\ell(t)=\log(t/(2\pi))\), \(L=\log T\), \(d=\alpha+\beta\). The sharp integral of
\[
 \ell(t)\,\zeta(\tfrac12+\alpha+it)\zeta(\tfrac12+\beta-it)
       Q_1(\tfrac12+it)Q_2(\tfrac12-it)
\]
over \([1,T]\), divided by \(2\pi\), has main term
\[
 \frac1{2\pi}\sum_{\substack{g,h,k\ge1\\gh,gk\le y,\ (h,k)=1}}
   \frac{a_{gh}b_{gk}}{ghk}
   \int_0^T\ell(t)
   \left[
    \frac{\zeta(1+d)}{k^\alpha h^\beta}
    +(t/(2\pi))^{-d}\,h^\alpha k^\beta\zeta(1-d)
   \right]dt .
\]
The factor and slots are those of HLZ (5). For a sesquilinear continuous form replace the second array by its conjugate before applying the formula. The proof works first on nested fixed Cauchy circles of radii \(c/L\) and \(2c/L\), where \(|d|\ge c/L\). The original integral and combined main term are holomorphic on the corresponding closed bidisk and a neighborhood. In the main term, the apparent \(d=0\) poles cancel for every \((g,h,k)\) because \(k^{-\alpha}h^{-\beta}=h^\alpha k^\beta\) at \(\beta=-\alpha\), with the time power then one. Its time integral down to zero is locally holomorphic for \(\Re d<1\) by uniform integrability of the time power and logarithm. Iterated maximum modulus extends the remainder bound on the product tori to the closed bidisk. A larger nested pair still of size \(O(1/L)\) gives the same argument for a prescribed fixed small common shift radius. Coincident shifts are thus covered without evaluating a pole-annihilator at \(d=0\).

## Uniform product AFE on a sharp block

Write \(s_1=\frac12+\alpha+it\), \(s_2=\frac12+\beta-it\), and define
\[
 H_d(w)=e^{w^2}(1-4w^2/d^2),\qquad
 G_{\alpha,\beta}(w,t)=\pi^{-w}
 \frac{\Gamma((s_1+w)/2)\Gamma((s_2+w)/2)}
      {\Gamma(s_1/2)\Gamma(s_2/2)}.
\]
Integrate the two completed zeta factors shifted by \(w\) on \(\Re w=2\) against \(H_d(w)/w\) and move to \(-2\). The even kernel and the functional equation give two Dirichlet sums. The first has coefficients \(m^{-1/2-\alpha}n^{-1/2-\beta}\), phase \((n/m)^{it}\), and
\[
 V_{\alpha,\beta}(u,t)=\frac1{2\pi i}\int_{(2)}
           H_d(w)G_{\alpha,\beta}(w,t)u^{-w}\frac{dw}{w},\qquad u=mn .
\]
The dual has \((-\beta,-\alpha)\) in the same slots and \(\chi(s_1)\chi(s_2)\) as multiplier. In particular it keeps the phase \((n/m)^{it}\); the positive-height zeta factor in the dual has shift \(-\beta\). The additional four completion poles at \(w=-s_i,1-s_i\) are simple and separated for \(t\ge1\) and sufficiently small shifts. At any such pole the other completed argument has imaginary part \(2t+O(1)\) in absolute value. Its gamma factor cancels the exponential size from normalization by the two original gammas. The Gaussian at the pole gives \(e^{-t^2+O(t)}\), times a polynomial in \(t\) and a fixed power of \(L\). The total leftover is \(O_A(L^2(1+t)^{-A})\) for every fixed \(A\), after adjusting the constant. This bound is on the AFE for the zeta product only; allowing the two outer polynomials costs \(O(y)\) by the absolute coefficient sum.

For a dyadic block \(X\le t\le2X\) within \([1,T]\), and a fixed \(A\ge2\), the weights satisfy
\[
 |V(u,t)|+t|\partial_tV(u,t)|\ll_A L^2 \min(1,(X/u)^A).
\]
The same holds with the dual multiplier included. The fixed contour real parts used are \(-1/4,2,A\); the gamma arguments there have real parts in positive compact intervals. For \(|\Im w|\le t/2\), all imaginary parts in an interpolated gamma ratio remain of order \(t\). The exponential factors cancel since the opposite height signs are preserved, and the powers give \(G\ll_A t^{\Re w}\). The differentiated log gamma ratio is a sum of digamma differences under translation by \(w/2\). Integrating the trigamma estimate \(O(1/t)\) along the translation gives \(t|\partial_tG|\ll_A t^{\Re w}(1+|w|)\). For the remaining tails in \(\Im w=v\), the combined absolute imaginary parts in the numerator cannot drop below those of the original opposite-sign pair. This remains true for complex \(\alpha,\beta\): a common translation by \(v\) preserves the distance between the two imaginary heights, which originally equals their absolute sum. Stirling and the digamma bound thus leave at most polynomial growth, controlled after differentiation by \(e^{-v^2}\). The factor \(H_d(w)\) costs \(O(L^2(1+|w|)^2)e^{(\Re w)^2-v^2}\). Move to \(A\) when \(u\ge X\), or to \(-1/4\) when \(u\le X\), where the only weight pole is at zero with residue one and zero time derivative. This proves the displayed estimates, including bounded \(t\ge1\).

Pairing the same-sign imaginary arguments in the gamma quotient for \(\chi(s_1)\chi(s_2)\) shows that each pair differs by \(-d/2\) in real-complex increment. Stirling gives \(\chi(s_1)\chi(s_2)=(t/(2\pi))^{-d}(1+O(1/t))\) uniformly in these shifts for \(t\ge1\), with a larger fixed constant covering bounded \(t\). Digamma differences and the same trigamma integration give \(t|\partial_t(\chi(s_1)\chi(s_2))|\ll1\). Its modulus is bounded for \(1\le t\le T\) since \(d=O(1/L)\).

## Sharp off-diagonal estimate

Insert both outer polynomials. The phase becomes \(\exp(it\log(k_2/k_1))\) for \(k_1=rm\), \(k_2=s'n\). Integration by parts on each full or truncated dyadic block retains the two sharp endpoint terms and bounds the nonzero frequency integral by
\[
 \frac{O_A(L^3)\min(1,(X/(mn))^A)}{|\log(k_2/k_1)|}.
\]
Indeed \(|\ell(t)|\ll L\), its derivative is \(1/t\), and the derivative bound of the weight on the block gives the asserted variation. For a product cutoff \(mn\le P\), all compressed pairs have \(k_1k_2\le y^2P\). The original absolute unshifted coefficient is at most a constant times \((k_1k_2)^{-1/2}\) per representation, and there are at most \(\tau(k_1)\tau(k_2)\) representations. No assumption is needed on the sequence of rational gaps after compression.

For \(k_2/k_1\in[1/2,2]\), \(k_1\ne k_2\), the product of \((k_1k_2)^{-1/2}\) and the inverse log gap is \(O(1/|k_1-k_2|)\). There are \(O(y\sqrt P)\) values of \(k_1\), and for each fixed one the sum over the signed nonzero integer gaps is harmonic, \(O(\log(2y^2P))\). For the noncomparable pairs, the inverse log gap is bounded and the coefficient sum over \(k_1k_2\le y^2P\) is also \(O(y\sqrt P\log(2y^2P))\), by summing the inner \(k_2^{-1/2}\). Insert \(\tau(k_1)\tau(k_2)\ll_\eta(k_1k_2)^\eta\) with a fixed sufficiently small \(\eta>0\), and split \(mn\) into \(mn\le X\) and \(2^j X<mn\le2^{j+1}X\). Since \(y^2X\le T^2\), the initial divisor loss is \(T^{2\eta}\), and on the \(j\)-th piece the shift factors \(m^{-\Re\alpha}n^{-\Re\beta}\), or their dual counterparts, cost at most a fixed constant times \(2^{O(j/L)}\). Any further divisor loss is \(2^{O(j\eta)}\). Taking \(A\ge3\) makes the weighted dyadic sums converge. Choosing \(\eta\) sufficiently small and absorbing the logarithms gives \(O_\varepsilon(T^\varepsilon y\sqrt X)\) per height block. This grouping covers both AFE sums and neither discards oscillatory signs near the diagonal nor assumes they cancel.

## Diagonal and endpoint terms

Write \((r,s')=g(h,k)\) with coprime \(h,k\). Zero frequency means \(m=ku,n=hu\) for \(u\ge1\). The coefficient outside the first diagonal integral is \(a_{gh}b_{gk}k^{-\alpha}h^{-\beta}/(ghk)\). Inside it appears
\[
 \frac1{2\pi i}\int_{(2)}H_d(w)G_{\alpha,\beta}(w,t)
             (hk)^{-w}\zeta(1+d+2w)\frac{dw}{w}.
\]
Moving the line to \(-1/4\) crosses the pole at zero with residue \(\zeta(1+d)\). The possible zeta pole at \(-d/2\) has been killed by \(H_d\). The gamma arguments stay in their positive strips. A fixed-strip polynomial zeta bound on the new line is enough owing to the Gaussian. This gives error \(O(L^2 X^{-1/4}(hk)^{1/4})\) inside the indicated coefficient. The bound is valid even where \(hk\gg X\); this contour shift is used only for the diagonal, independently of the previous large-product weight estimate. Shifts on \(k,h\le y\) contribute \(O(1)\), and the aggregated size is controlled by
\[
 \sum_{g\le y}g^{-1}
   \sum_{h,k\le y/g}(hk)^{-3/4}
 \ll \sqrt y\sum_{g\le y}g^{-3/2}\ll\sqrt y .
\]
The dual gives the \(1-d\) pole and the correct reversed shift factors. For its residue, replacing the gamma multiplier by the time power costs \(O(L^2)\) after time integration per \(1/(ghk)\) times \(|\zeta(1-d)|=O(L)\). The outer harmonic sum is \(O((1+\log y)^3)\), so the total change is polylogarithmic. Integrating the diagonal remainder on a block with the logarithm costs \(O(L^3\sqrt y X^{3/4})\). Summing the geometric height blocks for both off-diagonal and diagonal remainders proves the asserted two error terms.

The main term extends from \(t=1\) to \(0\) at an additional polylogarithmic cost. The shift exponent is \(O(1/L)\), the \(t^{-d}\ell(t)\) integral on \((0,1]\) is uniformly bounded, zeta on the small separated circles is \(O(L)\), and the outer harmonic sum is as above. If using an actual extra integral over a bounded height segment down to zero, its holomorphic shifted zeta factors are bounded on the fixed critical strip away from \(s=1\), its logarithm is integrable, and the two polynomial factors cost at most \(O(y)\).

Finally, the logarithmic-derivative factor on the HLZ half-line is \(-\chi'/\chi(\frac12+it)=\ell(t)+O(1/t)\) with the \(J\) orientation in §4. The correction integral is \(O_\varepsilon(yT^{1/2+\varepsilon})\), since each \(\zeta(\frac12+\alpha+it)\) or \(\zeta(\frac12+\beta-it)\) is \(O_\varepsilon((1+t)^{1/4+\varepsilon})\) by the fixed small convexity strip, the outer polynomials have product \(O(y)\), and \(\int_1^T (1+t)^{1/2+\varepsilon}dt/t\ll T^{1/2+\varepsilon}\). This uses no new discrete mean-value input. If shifting that factor’s vertical line to \(1/2\) as in §4, its horizontal edges have the same allowed size by the complementary convexity exponents and the complementary elementary polynomial sums, absorbing logarithms. No gamma or shifted zeta pole is crossed at heights at least 1 on that short horizontal range.

Uniform boundedness of the coefficient arrays suffices for every step. More generally a common fixed divisor-log majorant yields \(\sup_{n\le y}|a_n|+\sup_{n\le y}|b_n|\ll_\eta y^\eta\) for every fixed \(\eta>0\), and rescaling the arrays absorbs this loss into the arbitrarily small power of \(T\). This extends the replacement to the corresponding portion of the printed HLZ coefficient class without a changing smoothing scale. The proof supplies neither an adjudication of the full shifted discrete theorem nor a correction to its unrelated diagonal-smoothed formulation.
