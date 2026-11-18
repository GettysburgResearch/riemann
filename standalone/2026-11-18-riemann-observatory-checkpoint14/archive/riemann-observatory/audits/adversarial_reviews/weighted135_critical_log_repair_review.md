# Independent check of a logarithmic strip condition for the raw explicit formula

The critical logarithmic repair works with \(p>3\). It bounds the absolute zero trace and provides a Dini modulus for the physical test, sufficient for the archimedean term. It enlarges every fixed strip \(H^s\) class with \(s>1/2\). These are sufficient conditions and are separate from the compact piecewise smooth formula. [Earlier \(H^s\) repair](weighted132_mellin_trace_repair_review.md) · [Pinned author manuscript](../../sources/uniform121_bombieri_lagarias/bombieri_lagarias_author.pdf)

## Strip trace and the raw zero sum

Suppose \(f\) is continuous with the two value-decay conditions (B) on manuscript p. 5. Choose \(0<\epsilon<\delta_0\) where \(\delta_0\) is an available value-decay exponent, so \(h=\widehat f\) is represented by its Mellin integral throughout the integration strip. Set
\[
 w_p(t)=\sqrt{1+t^2}\,(\log(e+|t|))^p,\qquad
 N_p(h)^2=\int_{-\epsilon}^{1+\epsilon}\int_{\mathbb R}
                       w_p(t)|h(\beta+it)|^2\,dt\,d\beta .
\]
Assume \(N_p(h)<\infty\). Fixed-radius holomorphic submean on the central region \(0\le\beta\le1\) bounds the sup on each ordinate cell \(j\le t\le j+1\) by \(C_{\epsilon,p}w_p(j)^{-1/2}I_j^{1/2}\), where \(I_j\) is the norm integral over the full strip and expanded ordinate cell \([j-1,j+2]\). The weight is comparable when ordinates differ by a bounded amount, including near zero. The \(O(\log(2+|j|))\) unit-height zero count includes multiplicity. Cauchy–Schwarz and bounded overlap give, for \(T\ge3\),
\[
 \sum_{|\Im\rho|>T}|h(\rho)|
 \ll_{\epsilon,p} N_p(h)
  \left(\sum_{|j|\ge T-1}\frac{\log^2(2+|j|)}{w_p(j)}\right)^{1/2}
 \ll_{\epsilon,p} N_p(h)(\log T)^{(3-p)/2}.
\]
Here the summand is comparable at large \(j\) to \(1/(|j|(\log |j|)^{p-2})\). The central finite set is also bounded by the norm. Thus the raw symmetric height sum is absolutely convergent for \(p>3\), with no assumption on RH or simplicity.

The same fixed-radius submean, integrated in the ordinate, yields a uniform weighted line estimate
\[
 \int_{\mathbb R}w_p(t)|h(\beta+it)|^2\,dt
 \ll_{\epsilon,p} N_p(h)^2
 \quad(-\epsilon/2\le\beta\le1+\epsilon/2).
\]
Fubini and comparability of the weight across a disk justify this integration. On these lines \(h(\beta+it)\) is the Fourier transform, in the \(+it\) convention, of \(F_\beta(u)=e^{\beta u}f(e^u)\).

## Dini modulus in physical space

For \(p>1\), \(\int w_p(t)^{-1}dt<\infty\), so the interior transform is integrable by Cauchy–Schwarz. Fourier inversion gives its physical continuous representative, agreeing with \(F_\beta\). For a displacement \(0<|v|\le1/4\), put \(X=1/|v|\). The square of its uniform difference modulus, divided by \(C_{\epsilon,p}N_p(h)^2\), is at most
\[
 \int_{\mathbb R}\frac{|e^{itv}-1|^2}{w_p(t)}\,dt .
\]
The part \(|t|>X\) is \(O((\log(e+X))^{1-p})\) by integration of \(1/(t(\log t)^p)\). Below \(X\), use \(|e^{itv}-1|\le |tv|\). On \(0\le t\le\sqrt X\), \(t^2/w_p(t)\ll t\) gives \(O(X^{-1})\) after multiplication by \(X^{-2}\). On \(\sqrt X\le t\le X\), \(\log(e+t)\gg\log(e+X)\), yielding \(O((\log(e+X))^{-p})\). Hence the modulus is
\[
 O_{\epsilon,p}\bigl(N_p(h)(\log(e/|v|))^{(1-p)/2}\bigr).
\]
This majorant is Dini exactly when \(p>3\). On a neighborhood of \(x=1\) the changes between \(u=\log x\) and \(x\), multiplication by a fixed smooth power of \(x\), and \(x\mapsto1/x\) preserve the modulus up to a constant and an \(O(|x-1|)\) term. The archimedean numerator
\[
 f(x)+x^{-1}f(1/x)-2f(1)/x^2
\]
therefore vanishes with a Dini modulus. Dividing by the source's simple \(x=1\) singularity in \(x/(x^2-1)\) gives an integrable function. The trace also bounds \(f(1)\) itself. The two lines \(\beta=-\epsilon/2\) and \(1+\epsilon/2\) give the global pointwise bounds \(f(x)\ll N_p(h)x^{\epsilon/2}\) for \(x\le1\) and \(f(x)\ll N_p(h)x^{-1-\epsilon/2}\) for \(x\ge1\). These control the pole integrals and prime sum.

## Norm approximation

The weight is moderate in frequency:
\[
 w_p(t+v)\ll_p w_p(t)(1+|v|)^{1+p}.
\]
For instance, first use \(1+|t+v|\le(1+|t|)(1+|v|)\) and then use \(\log(e+|t+v|)\ll\log(e+|t|)\log(e+|v|)\). Thus convolution by a Fourier multiplier kernel with finite weighted \(L^1\) norm against \((1+|v|)^{(1+p)/2}\) is bounded on the weighted \(L^2\) space by Young's inequality.

Cut off \(F(u)=e^{u/2}f(e^u)\) by \(\chi_R(u)=\chi(u/R)\) with \(\chi\in C_c^\infty\) equal to one near zero. On each slice it multiplies \(F_\beta\) by \(\chi_R\). The scaled Fourier transforms \(\widehat{\chi_R}\) have a common bound in the indicated weighted \(L^1\) norm. They converge as multipliers strongly on the physical weighted-frequency space. To see density without assuming compact smooth density first, use density of Schwartz transforms in weighted \(L^2\), and note that multiplication by \(\chi_R\) converges on physical Schwartz functions in Schwartz topology. The uniform multiplier bound gives strong convergence on the entire space. Dominated convergence in \(\beta\) then gives convergence in the strip norm.

Mollifying a cut-off physical \(F\) by a compact mollifier \(\varphi_\eta\) induces convolution of each slice by \((e^{(\beta-1/2)\,\cdot}\varphi_\eta)\). These kernels have uniformly bounded ordinary \(L^1\) norm on the integration strip, and their Fourier transforms converge pointwise to one. Dominated convergence works in the weighted Fourier \(L^2\) norm and in \(\beta\). A diagonal choice gives compact smooth physical tests converging in the strip norm. All resulting approximants have an entire Mellin transform. The norm estimates for the spectral side, archimedean side and other arithmetic terms apply to differences, so the usual compact smooth explicit formula extends to this class by continuity. There is no need to derive derivative bounds on the original \(f\).

## Strict enlargement and scope

For any \(s>1/2\), the bound \(w_p(t)\ll_{p,s}(1+t^2)^s\) gives the inclusion from the earlier strip norm. Strictness can be witnessed within the physical class. Choose a nonzero nonnegative smooth bump \(\psi\) of compact support, and set
\[
 F(u)=\psi(u)\sum_{j\ge1}a_j\cos(2^j u),
 \qquad a_j=2^{-j/2}j^{-p/2-2},\qquad
 f(x)=x^{-1/2}F(\log x).
\]
The series converges uniformly, giving a compactly supported continuous \(f\) on \((0,\infty)\). A single packet on any fixed bounded strip has weighted Fourier norm \(O(a_j\,w_p(2^j)^{1/2})\), by moderation and the uniform rapid Fourier decay of \(e^{(\beta-1/2)u}\psi(u)\). The sum of these norms converges since the bound is \(O(j^{-2})\). On a fixed small frequency interval about \(2^j\), the matching packet contributes at least \(c a_j\) in real part, uniformly in \(\beta\) on the strip, by positivity of the bump. Every other carrier is at distance \(\gg 2^j\) and the sum of those terms is \(O_M(2^{-Mj})\), since \(\sum a_j<\infty\). Hence for any \(s>1/2\) the earlier strip \(H^s\) norm diverges, by the lower bound \(\sum_j 2^{2sj}a_j^2=\infty\). This demonstrates strict weakening while respecting the Mellin and value-decay conditions.

The coincidence of \(p>3\) for the spectral sum and Dini estimate concerns the proved majorants. It shows no necessity or endpoint sharpness for the raw formula. In particular the compact jump functions in the manuscript have a discontinuity at 1, while the present weighted strip condition forces a continuous representative. Their piecewise smooth explicit formula remains a separate input. No canonical file was changed.

## Strict enlargement within the original smooth value-decay class

The compact Fourier-series example above is a continuous example and makes no \(C^1\) assertion. There is also a \(C^\infty\) example satisfying the original literal (A) and (B). Normalize a nonnegative \(\psi\in C_c^\infty((-1/8,1/8))\) so \(\int\psi=1\), put \(\Gamma_j=2^{j^2}\), and set
\[
 a_j=\Gamma_j^{-1/2}(\log(e+\Gamma_j))^{-p/2}j^{-2}e^{-2j},
 \qquad
 F(u)=\sum_{j\ge1}a_j\psi(u-j)\cos(\Gamma_j u),
 \qquad f(x)=x^{-1/2}F(\log x).
\]
The supports in \(u\) are disjoint and locally finite. Thus \(f\) is smooth on \((0,\infty)\), vanishes near zero, and on each support is \(O(e^{-5j/2})\), hence \(O(x^{-2})\) at infinity. The pointwise decay follows from \(a_j\ll e^{-2j}\) and does not require any bound on its derivatives.

Use the previously proved moderate-weight translation estimate on the strip \(-1/4\le\beta\le5/4\). On a \(\beta\)-slice the weighted Fourier norm of packet \(j\) is at most
\[
 C_{\psi,p}\,a_j e^{(\beta-1/2)j}w_p(\Gamma_j)^{1/2}
 \ll_{\psi,p} j^{-2}e^{-5j/4}.
\]
The factor \(e^{(\beta-1/2)j}\) comes from translating the physical bump. The remaining transform, of \(e^{(\beta-1/2)v}\psi(v)\), is uniformly Schwartz, so the displayed bound is uniform on the strip. The summed norm is finite by the triangle inequality. Absolute convergence of the Mellin integral and dominated convergence identify its limit with \(\widehat f\).

For the reverse comparison introduce
\[
 J_\beta(\tau)=\int_{\mathbb R}e^{(\beta-1/2)v}\psi(v)e^{i\tau v}\,dv .
\]
There is a fixed \(c>0\) such that \(|J_\beta(\tau)|\) is bounded below by a positive constant for \(|\tau|\le c\), uniformly on the indicated strip. The real part of this integral already gives that bound by positivity on the small support. On the frequency window \(|t-\Gamma_j|\le c\) the matching term of \(\widehat f(\beta+it)\) is
\[
 \tfrac12 a_j e^{(\beta-1/2)j}\,
        e^{i(t-\Gamma_j)j}J_\beta(t-\Gamma_j).
\]
The last exponential is a phase of modulus one. The lower bound is on the **modulus** of the matching term throughout a fixed-width interval. Its real part need not retain one sign across that entire interval.

All other carriers, including the unmatched sign of packet \(j\), are at distance \(\gg\Gamma_j\) from the window. The sum of their absolute contributions is \(O_M(\Gamma_j^{-M})\) for every fixed \(M>0\), uniformly in \(\beta\), by the uniform Schwartz estimate and \(\sum_k a_k e^{3k/4}<\infty\). For any fixed \(M>1/2\) this is \(o(a_je^{-3j/4})\), so it is smaller than the main term uniformly even at the left end of the strip. On \(1/2\le\beta\le3/4\) one therefore has \(|\widehat f(\beta+it)|\gg a_j\) on the entire window for all sufficiently large \(j\). Integrating over this fixed subset of the strip and the disjoint frequency windows, the squared \(H^s\) strip norm for \(s>1/2\) has lower bound a constant times
\[
 \sum_j \Gamma_j^{2s-1}(\log(e+\Gamma_j))^{-p}j^{-4}e^{-4j}.
\]
The summands tend to infinity since \(\log\Gamma_j=j^2\log2\). This proves strict enlargement even among the original smooth tests with prescribed value decay. It neither asserts a necessary repair nor conflicts with the separate broad-class countermodel, whose carrier amplitudes are deliberately much larger.
