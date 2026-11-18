# Signed raw-height explicit formula at the logarithmic endpoint

The signed endpoint has a different outcome from absolute sampling. With the original value decay and local \(C^1\) at \(x=1\), a finite logarithmic strip norm yields the raw symmetric height formula at \(p=3\). In fact the following argument gives it for all \(p>1\), using the actual unconditional zeta zero distribution. This does not restore absolute convergence at \(p=3\) or address \(p=1\). [Absolute endpoint countermodel](weighted138_critical_endpoint_campaign.md) · [Pinned Bombieri–Lagarias manuscript](../../sources/uniform121_bombieri_lagarias/bombieri_lagarias_author.pdf)

## Claim and inputs

Let \(f\) be real and continuous on \((0,\infty)\), satisfy the value bounds (B) for an exponent \(\delta_0>0\), and be \(C^1\) on a neighborhood of \(1\). Put \(h=\widehat f\), \(F(u)=e^{u/2}f(e^u)\), and let
\[
 w_p(t)=\sqrt{1+t^2}(\log(e+|t|))^p,\qquad
 N_p(h)^2=\int_{-\epsilon}^{1+\epsilon}\int_\mathbb R
                            w_p(t)|h(\beta+it)|^2\,dt\,d\beta
\]
be finite for \(p>1\), \(0<\epsilon<\delta_0\). Local \(H^1\) of \(F\) near zero suffices instead of local \(C^1\). Under the stated conditions, \(\lim_{T\to\infty}\sum_{|\Im\rho|\le T}h(\rho)\) exists and equals the arithmetic expression on manuscript p. 6. Full (A) for a continuous original test implies the local \(H^1\) condition whenever its permitted derivative jumps have finite one-sided limits.

I checked the unconditional inputs in the rendered Titchmarsh–Heath-Brown second edition. Theorem 9.19(C), p. 237, gives Selberg's \(N(\sigma,T)\ll T^{1-(\sigma-1/2)/4}\log T\) uniformly for \(1/2\le\sigma\le1\). Equation (9.25.1), p. 245, at \(k=1\) gives the unconditional bound \(\int_0^T|S(t)|^2\,dt\ll T\log\log T\). The latter note distinguishes Selberg's earlier conditional treatment. These checks concern the cited statements. I did not reconstruct Selberg's full 1946 proof. The usual Riemann–von Mangoldt formula also gives \(O(\log t)\) ordinates in a unit interval, with multiplicity. [Rendered inputs from Titchmarsh](../../sources/equivalence_round2/titchmarsh1986.pdf)

## Horizontal projection error

Fixed-radius Cauchy and submean estimates bound both \(h\) and \(h'\) on a unit ordinate cell \([j,j+1]\), uniformly for \(0\le\Re s\le1\), by
\[
 C_{\epsilon,p}w_p(j)^{-1/2}I_j^{1/2},
\]
where \(I_j\) is the full strip norm integral restricted to an expanded ordinate cell, with bounded overlap. For the derivative, apply Cauchy's estimate within a slightly larger disk and submean to bound its supremum by the \(L^2\) norm on a still larger fixed disk inside the strip. The same local bound integrated along the central line gives \(\int w_p(t)(|h(1/2+it)|^2+|h'(1/2+it)|^2)dt\ll N_p(h)^2\). The pointwise bound also gives \(|h(1/2+it)|\ll w_p(t)^{-1/2}N_p(h)\).

Let \(b_j=\sum_{j\le\gamma<j+1}|\beta-1/2|\), over nontrivial zeros with multiplicity. On \(T\le\gamma\le2T\), reflection and the Selberg density estimate give
\[
 \sum_{T\le\gamma\le2T}|\beta-1/2|^2
 \ll T\log T\int_0^{1/2}u e^{-c u\log T}\,du
 \ll T/\log T.
\]
Here the layer-cake integral for the squared displacement is valid with strict or weak counting convention, since the values at jump parameters do not affect the integral. The unit-interval zero count and Cauchy–Schwarz within each cell now give \(\sum_{j\asymp T}b_j^2\ll T\). Consequently \(\sum_{j\ge1}b_j^2/w_p(j)\ll \sum_{r\ge1}r^{-p}<\infty\), by dyadic summation. Applying the derivative cell bound to each horizontal segment from \(1/2+i\gamma\) to \(\beta+i\gamma\), and then Cauchy–Schwarz across the cells, proves
\[
 \sum_{\gamma>0}|h(\beta+i\gamma)-h(1/2+i\gamma)|
 \ll_{\epsilon,p} N_p(h).
\]
Thus the projection difference is absolutely summable and continuous in the strip norm. This avoids making any assertion of pointwise critical-line proximity for individual zeros.

## Projected signed count

Write \(H(t)=h(1/2+it)\), \(M(t)=\frac{t}{2\pi}\log\frac{t}{2\pi e}+7/8\), and put \(R(t)=N(t)-M(t)\) using the right-continuous inclusive count. For almost all \(t\), \(R(t)=S(t)+O(1/t)\). At a zero ordinate \(R(t)=O(\log t)\) still holds, by the unit-height count and the standard bound away from jumps. These facts and Selberg's second moment give
\[
 \int_3^\infty\frac{R(t)^2}{w_p(t)}\,dt
 \ll 1+\sum_{r\ge2}\frac{\log r}{r^p}<\infty .
\]
On a finite interval \((3,T]\), integrate \(H(t)\,dN(t)\) by parts against \(R\). The boundary \(R(T)H(T)\) tends to zero for all large \(T\), since \(\log T/\sqrt{w_p(T)}\to0\). The integral \(\int_3^\infty R(t)H'(t)dt\) is absolutely convergent by the weighted derivative line estimate. It defines a continuous functional of \(h\). This step retains the signed cancellation in \(dN\).

It remains to show convergence of \(\int_3^T H(t)M'(t)dt\). Pick a smooth compact cutoff \(\chi(u)\) supported in the neighborhood where \(F\) is \(H^1\), equal to one near \(u=0\). The Fourier transform of \(\chi F\) is absolutely integrable against \(M'(t)\ll 1+\log t\), by \(H^1\) and Cauchy–Schwarz with the integrable factor \((1+\log t)^2/(1+t^2)\). For the other part set
\[
 G(t)=\int_\mathbb R\frac{(1-\chi(u))F(u)}{iu}e^{itu}\,du.
\]
Then \(G'\) is the transform of \((1-\chi)F\), by the value decay and differentiation. Both \(G,G'\) have weighted \(L^2(w_p)\) bounds \(O(N_p(h))\). Indeed the multiplier \(m(u)=(1-\chi(u))/(iu)\), extended smoothly by zero near \(u=0\), and all its derivatives lie in ordinary \(L^2\). Consequently its Fourier transform has \(L^1\) norm with any fixed polynomial frequency weight by Cauchy–Schwarz and Plancherel. Weight moderation \(w_p(t+v)\ll_p w_p(t)(1+|v|)^{1+p}\) and weighted Young give the bound for \(G\). The usual smooth cutoff multiplier gives it for \(G'\). The unit-interval Sobolev estimate for \(G\), with comparability of \(w_p\) there, gives \(|G(T)|\ll w_p(T)^{-1/2}N_p(h)\). Now
\[
 \int_3^T G'(t)M'(t)\,dt
   =[G(t)M'(t)]_3^T-\int_3^T G(t)M''(t)\,dt.
\]
The upper boundary tends to zero and the remaining integral is absolutely convergent, using \(M''(t)=1/(2\pi t)\) and the weighted \(L^2\) bound. This proves the smooth-count part as a signed limit.

For real \(f\) the negative-ordinate sum is the conjugate of the positive-ordinate sum at every inclusive cutoff, so the symmetric height sum converges. The preceding bounds show continuity of the signed trace in \(N_p(h)+\|\chi F\|_{H^1}\). This is a signed estimate. It does not bound the sum of the absolute values of the projected evaluations.

## Identifying the limit

The cutoff and exponentially tilted mollifier argument from the prior logarithmic repair gives \(F_j\in C_c^\infty\) converging in strip norm also at \(p>1\). Choose the cutoffs identically one on a slightly larger neighborhood of \(\operatorname{supp}\chi\). Mollification converges in local \(H^1\) there, so \(\|\chi(F_j-F)\|_{H^1}\to0\) as well. The compact smooth Weil formula applies to the corresponding \(f_j(x)=x^{-1/2}F_j(\log x)\). Its signed spectral term now passes to the limit by the proved continuity.

On the arithmetic side, the same interior slice argument on \(\beta=-\epsilon/2,1+\epsilon/2\) gives pointwise weighted value bounds by \(N_p\) because \(\int w_p^{-1}<\infty\) for \(p>1\). These control the prime sum and the two pole integrals. Local \(H^1\) gives a \(1/2\)-Hölder modulus and controls the trace at \(x=1\); for the difference \(f_j-f\), the modulus and the trace tend to zero on a fixed neighborhood. This handles the simple archimedean singularity directly. Away from 1 the slice bounds and explicit normalization subtraction give an integrable tail. Thus all terms of the compact formula tend to those in the manuscript formula. This needs no \(p>3\) Dini estimate from the strip alone.

## Bounded comparison with other source test classes

Weil's 1952 paper, inspected in the French transcription around its conditions (A), (B) and terminal formula, asks that both \(F\) and \(F'\) have the exponential pointwise decay for the test class there. Its spectral term has a symmetric height limit. This is relevant to the earlier mismatch in the author manuscript, which states value decay alone, but it does not furnish the present logarithmic-strip closure for wild derivatives. The French file is a transcription, not a facsimile of the journal. [Weil 1952 transcription](https://denisevellachemla.eu/transc-Weil-1952.pdf)

Burnol's primary preprint math/9810169, pp. 6–12, §§3–4, uses separately specified weighted-variation hypotheses. Its “Explicit Formula” statement at pp. 11–12 gives an equivalence between existence of the spectral raw height limit and existence of the corresponding archimedean limit, and under additional derivative hypotheses evaluates that limit. It does not state the strip-norm closure above. I rendered Barner's 1981 article pp. 140–141 (Göttingen volume PDF pp. 145–146). Its statement of Weil's theorem uses the same bounds on both the test and its derivative. Barner's own Theorem 1 replaces the derivative tail condition with finite total variation of \(F(x)e^{(1/2+b)|x|}\), midpoint normalization, and a local \(F_\chi(x)+F_\chi(-x)-2F(0)=O(|x|)\) condition. It still gives the signed symmetric height limit, with a different tail hypothesis from the present logarithmic strip norm. Guinand's 1948 DOI was verified, but the direct publisher PDF endpoint returned HTTP 403 and was not read. These are bounded comparisons, not an exhaustive antecedent search. [Burnol preprint](https://arxiv.org/pdf/math/9810169) · [Barner's Göttingen volume](https://gdz.sub.uni-goettingen.de/download/pdf/PPN243919689_0323/PPN243919689_0323.pdf) · [Guinand bibliographic DOI](https://doi.org/10.1112/plms/s2-50.2.107)

**Disposition.** The stated unconditional estimates convert the strip hypothesis to a signed raw-height formula for \(p>1\) plus the local \(H^1\) trace assumption. The proof does not decide whether the signed condition is optimal or whether the endpoint \(p=1\) is accessible. No canonical file was changed.
