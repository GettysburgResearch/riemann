# Independent stress test of the negative logarithmic strip counterexample

2026-11-18. The proposed arithmetic spike construction works for every fixed \(q>0\) and gives more than failure of a finite limit: the ordinary inclusive symmetric spectral sum has a subsequence tending to \(-\infty\) and a bounded subsequence. The test is real, smooth on the whole positive axis, zero near zero and one, and satisfies the original value envelopes. Its prime samples all vanish and the ordinary compensated right side is finite. The assertion concerns weights \(\sqrt{1+t^2}/\log^q(e+|t|)\) below the critical \(p=0\) norm, with the literal local condition (A) retained. No canonical mutation or priority claim.

## Packet and strip norm

Fix \(\delta>0\), \(0<\epsilon<\min(\delta,1/2)\), and \(0<A<q\). Use log coordinate \(F(u)=e^{u/2}f(e^u)\). Choose increasing primes \(p_j\) with \(u_j=\log p_j\) separated by at least 2 and \(u_1>2\). Put \(a_j=e^{-(1/2+\delta)u_j}\). For a frequency \(R\) to be chosen much later in the \(j\)-th step let \(w=R^{-1}(\log R)^A\) and
\[
 F_{j,R}(u_j+v)=a_j\,\chi(v/w)\eta(Rv)\sin(Rv).
\]
Choose fixed smooth cutoffs between zero and one, \(\chi=1\) on \([0,1/2]\), \(\chi=0\) for \(v/w\ge1\), and \(\eta=0\) for \(Rv\le1\), \(\eta=1\) for \(Rv\ge2\). This is a smooth test supported in \([u_j+1/R,u_j+w]\). Choose \(w<\frac12\min(1,\log(p_j+1)-u_j)\). The support contains no point \(\log n\) for any integer \(n\ge2\), and no negative logarithm. In particular the factor at \(p_j\) itself is sampled outside the support. The value bound for the eventual sum follows at once from \(a_j\), disjointness, and \(0\le v<1\).

For \(\theta=\beta-1/2\), the Mellin transform on a vertical line is the positive-exponent Fourier transform of \(e^{\theta u}F\). Take out \(a_j e^{\theta u_j} e^{itu_j}\) and denote the remaining physical envelope by \(b(v)=e^{\theta v}\chi(v/w)\eta(Rv)\). Uniformly for \(-\epsilon\le\beta\le1+\epsilon\), one has \(\|b\|_\infty+\|b'\|_1=O(1)\). For \(|t|\le\sqrt R\), one integration by parts at the two frequencies \(t\pm R\) thus gives
\[
 |h_{j,R}(\beta+it)|\ll a_j e^{\theta u_j}/R.
\]
The squared contribution on this low band to the weighted norm is \(O(a_j^2 e^{2\theta u_j}/R)\), since the integral of \(\sqrt{1+t^2}\) there is \(O(R)\). On the high band the inverse log factor is \(O_q((\log R)^{-q})\). The full \(L^2\) norm of the physical packet after tilting is \(O(a_j e^{\theta u_j}\sqrt w)\); its first derivative norm is \(O(a_j e^{\theta u_j}(R\sqrt w+w^{-1/2}+\sqrt R))=O(a_j e^{\theta u_j}R\sqrt w)\), since \(Rw\ge1\). Plancherel and Cauchy–Schwarz bound the square of its Fourier \(H^{1/2}\) norm by the product of its \(L^2\) and \(H^1\) norms. Thus, after integrating over the fixed strip, a uniform conservative bound is
\[
 N_{-q}(h_{j,R})^2
 \ll a_j^2 e^{(1+2\epsilon)u_j}
       \big(R^{-1}+(\log R)^{A-q}\big).
\]
This tends to zero for fixed \(j\). In the same limit, \(\sup_{0\le\beta\le1,\,t\in\mathbb R}|h_{j,R}(\beta+it)|\ll a_j e^{u_j/2}w\) tends to zero by the physical \(L^1\) bound. The two distinct estimates serve different purposes in the assembly.

## Single packet on the actual spectral side

The weight \(W(t)=\sqrt{1+t^2}/\log^q(e+|t|)\) is polynomially moderate, and comparable on bounded shifts. Fixed-disk submean controls point values on the inner strip by \(C N_{-q}/\sqrt W\) and vertical line \(L^2(W)\) norms by \(C N_{-q}\). The folded rectangle on lines \(a=1+\epsilon/2\) and \(1-a\) therefore applies at good height \(T\) within 1 of any large target \(R\), with horizontal error \(O(N_{-q}\log^2 T/\sqrt{W(T)})=o(1)\) when the packet norms are bounded. The good height is chosen from unconditional \(O(\log T)\) local counts and the standard fixed-strip logarithmic derivative estimate. The residue sign and folded test are exactly the ones in the critical contour, namely \(h(a+it)+h(1-a-it)\). The estimates are uniform in packet index apart from its norm. [Critical contour setup](geometry154_critical_contour_and_cusp_adjudication.md)

The \(Q\)-part of the contour is bounded uniformly in finite height by \(C N_{-q}\), for packets and finite sums of packets. Indeed all the packets are exterior to a fixed neighborhood of zero in \(u\). Write \(G_\beta=\mathcal F_+[(1-\chi_0)F_\beta/(iu)]\) on each required line, with fixed \(\chi_0\) supported near zero. The cutoff multiplier and all its derivatives lie in \(L^2\), so weighted convolution and local Sobolev give weighted \(L^2\) bounds on \(G_\beta,G_\beta'\), and \(G_\beta(t)=O(N_{-q}/\sqrt{W(t)})\). Here \(G_\beta'=\mathcal F_+F_\beta\). The separate constant half-axis terms in Stirling use the primitive values, the log term has bounded boundary \(G_\beta(t)\log|t|\) and an absolutely convergent \(G_\beta(t)/t\) integral, and the \(O(1/|t|)\) remainder is absolutely integrable by weighted Cauchy–Schwarz. These estimates remain valid with the inverse log power. They supply no unrestricted sharp Fourier inversion claim for this weight.

On the \(\zeta'/\zeta\) part use the absolutely convergent Dirichlet series at each finite cutoff and the actual sharp inverse, with kernel \(\sin(T(v-u))/(\pi(v-u))\) in the physical coordinate. At the matching right-edge sample \(u=u_j\), first set \(T=R\). The inverse equals
\[
 \frac{a_j e^{(a-1/2)u_j}}{\pi}
 \int_{1/R}^{w} e^{(a-1/2)v}\chi(v/w)\eta(Rv)
             \frac{\sin^2(Rv)}v\,dv
 =
 \frac{a_j e^{(a-1/2)u_j}}{2\pi}\log(Rw)
       +O(a_j e^{(a-1/2)u_j}).
\]
The cutoff changes only bounded logarithmic intervals compared with \([2/R,w/2]\). On that core \(\sin^2(Rv)=(1-\cos(2Rv))/2\), and the integral of the cosine divided by its argument is uniformly bounded after substituting \(Rv\) and integrating by parts. The exponential tilt adds \(O(w)\) inside the integral. Changing to good height \(T\in[R,R+1]\) costs \(O(a_j e^{(a-1/2)u_j}w)\) by the derivative bound on the sine kernel. This is a large partial inverse of a function whose true sample is zero.

Every other sample on the right line, and every reflected sample at \(-\log n\) on the other line, has distance at least \(2w\) from \(u_j\) for large \(R\). For fixed \(j\) there is a positive minimum distance since the set \(\{\log n:n\ge2,n\ne p_j\}\) is locally finite, while negative logs are uniformly separated. The absolute kernel bound by the reciprocal distance shows their total prime-side contribution is \(O_j(a_j w)\), since \(\sum\Lambda(n)n^{-a}<\infty\) on the right line and the fixed tilt factors \(e^{(\beta-1/2)u_j}\) may be included in the constant. Thus the matching term is
\[
 -\frac{\log p_j}{2\pi\sqrt{p_j}}\,a_j\log(Rw)
   +O_j(a_j)
\]
with a genuine negative sign. Since \(\log(Rw)=A\log\log R\to\infty\), the fixed small positive coefficient at each successive prime places no restriction on the achievable magnitude. Shrinking the norm and inflating this partial inverse occur simultaneously. The horizontal and \(Q\) bounds then show that the \(j\)-th packet alone has arbitrarily negative raw symmetric sums at its chosen good height.

## Infinite sum and two subsequences

Proceed recursively. Have the previous finite packets and all their protected heights \(T_i,U_i\), \(i<j\), fixed. Pick \(R\) sufficiently large to satisfy all the following conditions, then choose the admitted good \(T_j\in[R,R+1]\).

1. The \(j\)-th packet's strip norm is at most \(2^{-j}\), and its support obeys the separation conditions above.
2. Its contribution in absolute value to the finite spectral sum at each previously protected height is at most \(2^{-j}\), by the uniform \(a_j e^{u_j/2}w\) bound times the fixed finite count at those heights.
3. Its own sum at \(T_j\) is at most \(-2j\) minus an upper bound for the absolute spectral sum of the preceding finite packet sum at any sufficiently large height. That bound exists because those finitely many compact smooth packets have ordinary convergent explicit formulae. The estimates for the new packet are valid uniformly for the good height chosen within the unit interval.

Then choose \(U_j>T_j+1\) sufficiently large that the finite sum through packet \(j\) is within 1 of its limiting spectral value. This value is uniformly bounded in \(j\): its prime sample terms are zero, and its limiting \(Q\) functional has absolute value at most \(C\sum_i 2^{-i}\), by the direct exterior estimate. The horizontal errors vanish. Protect this \(U_j\) as well in every subsequent stage. Heights may always be chosen increasing.

The physical series is locally finite and smooth, vanishes near zero and one, and has the announced value bounds. Its Mellin transforms agree with the series by dominated log-coordinate integration of the exponentially decaying physical envelopes on the chosen strip. The area norm of the limit is finite by the summable norm bounds (or Fatou followed by the finite-sum triangle inequality). At each protected height there are only finitely many zero samples; the contribution of the future series is bounded by \(\sum_{i>j}2^{-i}\). Thus the full sum at \(T_j\) tends to \(-\infty\) along that subsequence, whereas at \(U_j\) it stays bounded. The argument uses actual zeros with multiplicity through residues, and proves failure in the ordinary inclusive symmetric convention. It even avoids any need to transfer the exploding subsequence from a non-good height. The earlier all-height comparison cannot rescue convergence because a divergent subsequence of good heights already suffices.

All prime samples vanish in both directions. The Mellin pole terms and the compensated archimedean integral are absolutely finite from the value envelopes and vanishing near one. This is a sharp obstruction below zero in the logarithmic-weight family for a universal signed guarantee under the same local assumptions. It is not the \(p=3\) compact cusp outside (A), not the smooth \(p=3\) obstruction to absolute sampling, and not a counterexample in the \(p=0\) class. Stability for other weights and priority are separate questions.
