# Independent check of a Sobolev–Mellin repair for the raw height formula

The proposed repair is sufficient. The strip norm controls both the absolute zero sum and point values of the physical test. Compact smooth approximants converge in that norm, and the arithmetic terms pass to the limit. The repair is distinct from the piecewise smooth formula used for the compact jump tests in Theorem 2. [Pinned author manuscript, pp. 5–6](../../sources/uniform121_bombieri_lagarias/bombieri_lagarias_author.pdf) · [Countermodel to the literal broad class](weighted130_explicit_formula_countermodel_review.md)

## Norm and trace estimates

Let \(f:(0,\infty)\to\mathbb C\) be continuous, with the two value bounds (B) for some \(\delta_0>0\). Write \(h=\widehat f\) for its Mellin transform and suppose
\[
 \|h\|_{\epsilon,s}^2=
 \int_{-\epsilon}^{1+\epsilon}\int_{\mathbb R}
       (1+t^2)^s |h(\beta+it)|^2\,dt\,d\beta <\infty,
 \qquad s>\tfrac12.
\]
Take \(0<\epsilon<\delta_0\) by restriction if necessary, so the integral representation of \(h\) is valid throughout the narrower strip. The transform is holomorphic there. If one starts with a larger analytic strip and uses its norm, this restriction avoids having to infer a Mellin integral representation from analytic continuation alone.

Use a fixed-radius disk, with radius positive and smaller than both \(\epsilon/4\) and \(1/4\), for the submean inequality on \(|h|^2\). For every point with \(0\le\beta\le1\) and \(t\in[j,j+1]\), enlarge the disk to the containing rectangle with \(\beta\) in the full norm strip and \(t\in[j-1,j+2]\). With
\[
 I_j=\int_{-\epsilon}^{1+\epsilon}\int_{j-1}^{j+2}
       (1+t^2)^s|h(\beta+it)|^2\,dt\,d\beta ,
\]
this gives \(\sup |h(\beta+it)|\ll_{\epsilon,s}(1+j^2)^{-s/2} I_j^{1/2}\) on the cell. The usual zero count gives \(O(\log(2+|j|))\) zeros in that cell, with multiplicity. The Cauchy–Schwarz inequality and bounded overlap of the expanded cells give
\[
 \sum_\rho |h(\rho)|
 \ll_{\epsilon,s}
 \Bigl(\sum_{j\in\mathbb Z}(1+j^2)^{-s}\log^2(2+|j|)\Bigr)^{1/2}
 \Bigl(\sum_j I_j\Bigr)^{1/2}
 \ll_{\epsilon,s}\|h\|_{\epsilon,s}.
\]
Thus this norm makes the spectral sum absolutely convergent, including the raw symmetric height sum in the manuscript. Its proof uses neither RH nor simplicity. The summability at the last step requires \(s>1/2\); this argument supplies no endpoint theorem.

The same submean inequality with disks centered on a fixed interior vertical line, followed by integration in the ordinate, gives
\[
 \int_{\mathbb R}(1+t^2)^s |h(\beta+it)|^2\,dt
 \ll_{\epsilon,s}\|h\|_{\epsilon,s}^2
 \quad\left(-\epsilon/2\le\beta\le1+\epsilon/2\right).
\]
Indeed the weight is comparable at ordinates a bounded distance apart, and each point in the strip is covered by disk centers in a \(t\)-interval of uniformly bounded length. Put \(F(u)=e^{u/2}f(e^u)\) and \(F_\beta(u)=e^{(\beta-1/2)u}F(u)\). With the \(e^{itu}\) convention, \(h(\beta+it)\) is the Fourier transform of \(F_\beta\). The slice estimate and Plancherel therefore give uniform \(H^s(\mathbb R)\) control of \(F_\beta\) on the indicated interior lines. Fourier inversion and Cauchy–Schwarz show the embedding into \(C^{0,\alpha}\) for \(0<\alpha<\min(1,s-1/2)\): use \(|e^{itu}-1|\ll_\alpha |tu|^\alpha\) in the inversion integral. The representatives agree with the original continuous \(F_\beta\), since they agree almost everywhere.

In particular the norm bounds \(f(1)\) and a Hölder norm of \(f\) on a fixed neighborhood of 1. It also gives global estimates \(|f(x)|\ll_{\epsilon,s}\|h\|_{\epsilon,s}x^{\epsilon/2}\) for \(x\le1\) and \(|f(x)|\ll_{\epsilon,s}\|h\|_{\epsilon,s}x^{-1-\epsilon/2}\) for \(x\ge1\), by taking respectively \(\beta=-\epsilon/2\) and \(\beta=1+\epsilon/2\). These estimates apply after the narrower integral-representation choice above. The assumed value decay remains the convenient starting condition proving that the Mellin transform is represented by the physical test.

## Density while retaining the exponential weights

Via Plancherel, the strip norm is a fixed constant times the \(L^2\) integral in \(\beta\) of \(\|F_\beta\|_{H^s}^2\). Take a smooth compact real cutoff \(\chi\) equal to 1 near 0, and write \(\chi_R(u)=\chi(u/R)\), \(R\ge1\). Cutting off \(F\) gives the slices \(\chi_RF_\beta\). These multipliers have a uniform \(H^s\) operator bound independent of \(R,\beta\): in Fourier space use weighted Young's inequality and
\[
 \int_{\mathbb R}(1+v^2)^{s/2}|\widehat{\chi_R}(v)|\,dv
 =\int_{\mathbb R}(1+w^2/R^2)^{s/2}|\widehat\chi(w)|\,dw\ll_s1 .
\]
They converge strongly to the identity, by the uniform bound and density of compact smooth functions in \(H^s\). Dominated convergence in \(\beta\) yields convergence in the full strip norm.

For smoothing, let \(\varphi_\eta\) be a compact smooth mollifier of mass 1 on \(|u|\le\eta\le1\). If \(G\) denotes the cutoff \(F\), the slice of \(\varphi_\eta*G\) equals
\[
 (e^{(\beta-1/2)\,\cdot}\varphi_\eta)*G_\beta .
\]
The kernels have a uniformly bounded \(L^1\) norm on the whole integration strip. Their Fourier transforms converge pointwise to 1 as \(\eta\to0\), so these convolutions converge strongly in \(H^s\) at almost every \(\beta\), and by domination also in the full strip norm. Choosing a diagonal sequence in \(R,\eta\) produces \(F_j\in C_c^\infty(\mathbb R)\) and \(f_j(x)=x^{-1/2}F_j(\log x)\in C_c^\infty((0,\infty))\) with \(\|\widehat f_j-h\|_{\epsilon,s}\to0\). All transforms in this comparison retain the required holomorphy. In addition the original exponential value envelope for \(F\) is stable under the multiplier and convolution with support of radius at most 1, with a constant uniform in the approximants.

## Extension of the explicit formula

Use the usual compact smooth Guinand–Weil formula for each \(f_j\), in exactly the manuscript's Mellin normalization \(\widetilde f(x)=x^{-1}f(1/x)\). The spectral difference is at most \(C\|\widehat f_j-h\|_{\epsilon,s}\) by the zero sampling bound. The pole integrals of \(f_j,\widetilde f_j\), and the prime sums, converge by dominated convergence from the uniform value decay and pointwise convergence. In particular \(\sum_{n\ge2}\Lambda(n)n^{-1-\epsilon/2}<\infty\). Alternatively these limits follow at once from the two exterior slice trace bounds applied to \(f_j-f\).

The archimedean integral has kernel \(x/(x^2-1)\) on \(x>1\), multiplying
\[
 f(x)+\widetilde f(x)-2f(1)/x^2.
\]
The trace gives \(f_j(1)\to f(1)\). Each numerator is \(O(|x-1|^\alpha)\) near 1 with a uniform constant, by the centered \(H^s\) slice bound and the smooth inversion \(x\mapsto1/x\) there. The integrands are therefore dominated by \(C(x-1)^{\alpha-1}\) near 1. Away from 1 they have a uniform integrable tail by the value bounds and the explicit subtraction. This proves convergence of the archimedean integral, completing the extension of the compact smooth formula. All bounds can also be applied directly to differences of test functions and show continuity of the corresponding arithmetic functional in the strip norm.

The condition is sufficient. It does not claim that \(s>1/2\) or integrated strip control is necessary for the raw height sum by other methods. In particular \(g_{n,\varepsilon}\) in the manuscript has a genuine jump at \(1\), since its limiting values there are \(n\) and 0. Its central slice cannot be in \(H^s\) for \(s>1/2\) by the continuous representative conclusion, so this new argument does not subsume the separate compact piecewise smooth treatment of those approximants. No field-priority or canonical classification is proposed.
