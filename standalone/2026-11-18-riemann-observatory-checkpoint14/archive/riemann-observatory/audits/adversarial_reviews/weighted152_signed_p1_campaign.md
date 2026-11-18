# Signed explicit formula at \(p=1\) by sharp Fourier inversion

For a continuous test with the original value decay and local \(C^1\) at \(x=1\), finite \(p=1\) Mellin strip norm does imply the signed formula with the raw inclusive symmetric height cutoff. The argument below in fact gives the same conclusion for \(p=0\), with strip weight \(\sqrt{1+t^2}\). It avoids needing finer Selberg variance cancellation, by treating the prime side on an absolutely convergent vertical line. It does not give absolute convergence of the spectral terms or a necessity claim. [Earlier signed \(p>1\) proof](weighted146_signed_endpoint_research.md) · [Absolute endpoint countermodel](weighted138_critical_endpoint_campaign.md) · [Pinned Bombieri–Lagarias manuscript](../../sources/uniform121_bombieri_lagarias/bombieri_lagarias_author.pdf)

## Statement and sharp inversion lemma

Let \(f\) be real continuous on \((0,\infty)\), satisfy the value bounds (B) with exponent \(\delta_0>0\), and be \(C^1\) on a neighborhood of 1. It suffices that \(F(u)=e^{u/2}f(e^u)\) be locally \(H^1\) near \(u=0\). Let \(h=\widehat f\) be the manuscript's Mellin transform, and assume for \(0<\epsilon<\min(\delta_0,1/2)\) and \(p\ge0\) that
\[
 N_p(h)^2
 =\int_{-\epsilon}^{1+\epsilon}\int_{\mathbb R}
 \sqrt{1+t^2}\log^p(e+|t|)|h(\beta+it)|^2\,dt\,d\beta<\infty .
\]
A wider available norm strip can always be restricted to this one. Write \(w_p(t)=\sqrt{1+t^2}\log^p(e+|t|)\). Fixed disk submean gives pointwise control \( |h(\beta+it)|\ll_{\epsilon,p}N_p(h)w_p(t)^{-1/2}\) on \(-\epsilon/2\le\beta\le1+\epsilon/2\), and also uniform weighted \(L^2\) control on each of those vertical lines after integrating the submean inequality in the ordinate. These estimates are exactly the earlier strip trace argument and require only comparability of \(w_p\) over bounded distances. They do not require \(\int w_p^{-1}<\infty\).

Put \(F_\beta(u)=e^{\beta u}f(e^u)\), so the Fourier transform in the positive sign convention is \(h(\beta+it)\). On each of these lines \(F_\beta\) is continuous, decays exponentially at both ends, and is therefore uniformly continuous. Define the sharp inversion integral
\[
 I_{T,\beta}(u)=\frac1{2\pi}\int_{-T}^{T}
                            h(\beta+it)e^{-itu}\,dt .
\]
Its Gaussian counterpart with multiplier \(e^{-t^2/T^2}\) converges uniformly in \(u\) to \(F_\beta\) by approximate identity. For the difference, the multiplier \(m_T(t)={\bf1}_{|t|\le T}-e^{-t^2/T^2}\) obeys
\[
 \int_\mathbb R\frac{|m_T(t)|^2}{\sqrt{1+t^2}}\,dt\le C
\]
uniformly, by replacing the denominator by \(|t|\), substituting \(t=Tv\), and noting the numerator is \(O(v^4)\) near \(v=0\) and rapidly decreasing for \(|v|>1\). For \(p>0\) this improves to \(O((\log T)^{-p})\). Split at \(|t|=\sqrt T\): below that threshold the square of the low-frequency multiplier adds \(O(T^{-2})\), and above it \(\log(e+|t|)\gg\log T\). Cauchy–Schwarz with the line norm therefore makes the difference \(o(1)\), uniformly in \(u\). For \(p=0\), split the Cauchy–Schwarz bound instead at a fixed large ordinate \(R\). Below \(R\) the multiplier tends uniformly to zero. Above \(R\) use the uniform kernel bound and the small weighted \(L^2\) tail of the fixed transform. Letting first \(T\) and then \(R\) tend to infinity proves the same \(o(1)\) result. Consequently
\[
 \sup_{u\in\mathbb R}|I_{T,\beta}(u)-F_\beta(u)|\longrightarrow0 .
\]
This does not assert absolute Fourier integrability. The difference of the two cutoffs, which has negligible low-frequency part, is what permits the endpoint comparison.

## Folding the contour and evaluating the prime terms

Take \(a=1+\epsilon/2\) and the rectangle with vertical sides \(1-a,a\) and heights \(\pm T\). The entire Riemann \(\xi\)-function has exactly the nontrivial zeta zeros with multiplicity. On good heights at distance \(\gg1/\log T\) from every zero ordinate, its logarithmic derivative is \(O(\log^2 T)\) throughout the horizontal segment, by the classical local partial-fraction bound and Stirling. Such a height exists within bounded distance of any large target by deleting small intervals about the \(O(\log T)\) nearby ordinates. The two horizontals contribute
\[
 O_{\epsilon,p}\bigl(N_p(h)\log^2T/\sqrt{w_p(T)}\bigr)=o(1).
\]
Applying residue calculus and then \(\xi'/\xi(1-s)=-\xi'/\xi(s)\) gives on good heights
\[
 \sum_{|\Im\rho|\le T}h(\rho)
 =\frac1{2\pi}\int_{-T}^T
    \bigl(h(a+it)+h(1-a-it)\bigr)\frac{\xi'}{\xi}(a+it)\,dt+o(1).
\]
The plus sign comes from the reversed left contour and the sign of the reflected logarithmic derivative. Arbitrary heights, inclusive of any endpoint zero, differ from a good height by \(O(\log T)\) terms of size \(O(N_p(h)w_p(T)^{-1/2})\). This difference tends to zero. [Classical local logarithmic derivative, Titchmarsh §9.6(A)](../../sources/equivalence_round2/titchmarsh1986.pdf) · [Good-height reconstruction in the Gonek source review](geometry88_gonek_whole_advocate.md)

On the right edge write \(\xi'/\xi=\zeta'/\zeta+Q\), with
\[
 Q(s)=\frac1s+\frac1{s-1}-\frac12\log\pi+\frac12\frac{\Gamma'}{\Gamma}(s/2).
\]
For the \(\zeta'/\zeta\) term use its absolutely convergent Dirichlet series at \(a>1\). Each finite truncation can be integrated termwise, because \(\sum_n\Lambda(n)n^{-a}<\infty\). The resulting two kernels are exactly \(I_{T,a}(\log n)\) and \(I_{T,1-a}(-\log n)\). Uniform convergence in the sharp inversion lemma allows passage to the limit through the Dirichlet series. It yields
\[
 -\sum_n \Lambda(n)n^{-a}
                 \bigl(F_a(\log n)+F_{1-a}(-\log n)\bigr)
 =-\sum_n\Lambda(n)\bigl(f(n)+n^{-1}f(1/n)\bigr).
\]
No uniformly summable absolute bound for \(\int |h(a+it)|dt\) is used. This is the part for which the signed Selberg variance splitting was unnecessary.

## Gamma term and local regularity

On \(a+it\), Stirling gives \(Q(a+it)=\frac12\log|t|+c_\pm+O_a(1/|t|)\) for \(\pm t\ge3\), with fixed constants. The \(O(1/|t|)\) part is absolutely integrable against either vertical test by the weighted line estimate. The remaining log and constant integrals are convergent on each half-line, as follows.

Choose a smooth compact cutoff \(\chi\) near \(u=0\), equal to one on a smaller neighborhood, supported where \(F\) is locally \(H^1\). The central piece \(\chi F_\beta\) has \(H^1\) norm bounded by a constant times the local \(H^1\) norm of \(F\), for \(\beta=a,1-a\). Its transform is integrable against \(1+\log(2+|t|)\) by Cauchy–Schwarz. For the exterior piece define
\[
 G_\beta(t)=\int_{\mathbb R}\frac{1-\chi(u)}{iu}F_\beta(u)e^{itu}\,du .
\]
Then \(G_\beta'\) is the Fourier transform of \((1-\chi)F_\beta\). The physical multiplier \(m(u)=(1-\chi(u))/(iu)\) and each of its derivatives are in ordinary \(L^2\). By Cauchy–Schwarz and Plancherel its Fourier transform is in \(L^1\) with every fixed polynomial frequency weight. Weight moderation gives weighted \(L^2(w_p)\) bounds for \(G_\beta\) and \(G_\beta'\), each bounded by the strip norm. The unit-interval Sobolev estimate yields \(|G_\beta(t)|\ll N_p(h)/\sqrt{w_p(t)}\). Integration by parts now gives convergence of the log term, with vanishing boundary \(G_\beta(t)\log |t|\) and absolutely convergent derivative-weighted integral \(\int |G_\beta(t)|/|t|\,dt\) away from the origin. The constant term follows from \(G_\beta(t)\to0\). The same argument handles \(h(1-a-it)\) after \(t\mapsto-t\). In particular the gamma functional is continuous for \(N_p(h)\) plus the local \(H^1\) norm near \(u=0\).

One may also move the two \(Q\)-integrals to \(1/2\) by their own rectangles. The crossed pole of \(Q\) at 1 supplies \(h(1)+h(0)\) from the two terms. Horizontal connectors vanish as above, with \(Q=O(\log T)\). On the middle line the two rational parts cancel after reflection in \(t\), leaving the usual digamma kernel. This is consistent with the compact smooth normalization.

For exact identification with the printed arithmetic formula, cut off and mollify \(F\) as in the earlier logarithmic strip proof. The Fourier weight stays moderate for \(p\ge0\), and the exponentially tilted mollifier converges on every strip line in weighted \(L^2\), with bounded domination in the line parameter. Arrange the cutoffs to equal one on a fixed larger neighborhood of the local \(H^1\) interval, and take a diagonal sequence giving convergence also in that local norm. The approximants preserve an exponential physical value envelope uniformly and converge pointwise. Therefore the prime values and pole integrals pass by dominated convergence. Local \(H^1\) gives a \(1/2\)-Hölder bound at \(x=1\) and convergence of that trace, so the printed archimedean integrand has a common integrable majorant near 1. Its tail follows from the value envelope. The gamma functional on the contour converges by the bounds above. Thus the compact smooth Guinand–Weil identity passes to exactly the p. 6 manuscript formula with its raw symmetric height sum.

## Scope of the endpoint and source comparison

The previous Selberg route merely lacks an absolute majorant for \(\int S(t)H'(t)dt\) at \(p=1\). One can improve its horizontal projection part by pairing \(\rho\) with \(1-\bar\rho\) first. They share the same ordinate, so the linear term in \(\beta-1/2\) cancels and the remainder costs \((\beta-1/2)^2\) times a second derivative cell bound. The same Selberg density implies fourth displacement moment \(O(T/\log^3T)\), so this projected difference remains absolutely harmless. The present proof instead avoids that whole decomposition. Neither the earlier dyadic majorant nor its failure proves a signed obstruction.

The bounded source comparison in the earlier note checked Weil's 1952 French transcription and Barner's rendered pp. 140–141. Weil imposes exponential decay on both the physical test and its derivative. Barner's sufficient class uses exponential weighted total variation and an explicit local condition. Those arguments use raw symmetric height limits, but their quoted hypotheses differ from the strip \(L^2\) condition here. The present method uses the usual compact smooth formula as input and proves the extension from that input. Guinand's 1948 publisher PDF remained unavailable in the earlier comparison. No field-priority assertion, negative \(p\) assertion, or canonical change was made. [Bounded Weil–Barner source comparison](weighted146_signed_endpoint_research.md)
