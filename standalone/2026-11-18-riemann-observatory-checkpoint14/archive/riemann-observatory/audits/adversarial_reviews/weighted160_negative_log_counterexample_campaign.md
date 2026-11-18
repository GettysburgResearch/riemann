# Sharp symmetric divergence below the critical strip weight

For each \(q>0\) there is a real \(C^\infty(0,\infty)\) test with original value decay and finite strip norm for \(w(t)=\sqrt{1+t^2}\log^{-q}(e+|t|)\) whose raw symmetric zero sums are unbounded below. This is unconditional. It addresses negative logarithmic powers within this strip scale.

## Packets and norm

Use \(\widehat G(t)=\int G(u)e^{itu}du\), with inverse measure \(dt/(2\pi)\). Fix \(0<\epsilon<1/4\), the norm strip \([-\epsilon,1+\epsilon]\), the contour line \(a=1+\epsilon/2\), and \(0<A<q\). Take smooth \([0,1]\)-valued cutoffs \(\eta,\chi\) with \(\eta=0\) on \((-\infty,1]\), \(\eta=1\) on \([2,\infty)\), \(\chi=1\) on \([-1/2,1/2]\), and \(\chi=0\) outside \((-1,1)\). At \(u_j=\log p_j\) for a sequence of increasing primes tending to infinity, let
\[
 F_{j,T}(u_j+v)=b_j\chi(v/W)\eta(Tv)\sin(Tv),
 \quad b_j=e^{-u_j},\quad W=(\log T)^A/T.
\]
At fixed \(j\) take \(T\) large enough that \(W<1\) and the support lies below the next prime-power logarithm. The supports are disjoint and all prime samples are zero.

For \(G_\beta=e^{(\beta-1/2)u}F_{j,T}\), uniformly in the strip, \(\|G_\beta\|_1\ll_j b_jW\), \(\|G_\beta\|_2\ll_j b_j\sqrt W\), and \(\|G_\beta\|_{H^1}\ll_j b_jT\sqrt W\). The last bound follows from differentiating the two cutoffs and the carrier, using \(W^{-1}\le T\). Interpolation gives squared \(H^{1/2}\) norm \(O_j(b_j^2 TW)\). Below \(|t|=\sqrt T\), the negative-log weighted squared norm is \(O_j(b_j^2W\sqrt T)\) by Plancherel and \(w(t)\ll 1+\sqrt T\). Above \(\sqrt T\), it is \(O_j(b_j^2TW\log^{-q}T)\) by the interpolation bound. Thus the strip norm tends to zero at each fixed stage.

## Single-packet spectral witness

Write \(h_{j,T}\) for the packet Mellin transform and \(I_{S,\beta}\) for sharp Fourier inversion of \(G_\beta\). The Dirichlet kernel gives
\[
 I_{T,a}(u_j)=\frac{b_je^{(a-1/2)u_j}}{\pi}
 \int_0^\infty e^{(a-1/2)v}\chi(v/W)\eta(Tv)\frac{\sin^2(Tv)}v\,dv
 =\frac{b_je^{(a-1/2)u_j}}{2\pi}\log(TW)+O_j(b_j).
\]
On \([2/T,W/2]\) both cutoffs equal 1 and \(\sin^2=(1-\cos(2Tv))/2\) gives the logarithm, with bounded oscillatory integral by integration by parts. The transitions each cost \(O(1)\) and the exponential replacement costs \(O_a(W)\). Moving \(T\) to \(S\in[T,T+1]\) costs \(O_j(b_jW)\) by \(|\widehat G_a|\le\|G_a\|_1\). All other prime-power arguments and all reflected arguments are a positive distance from this packet uniformly as \(T\to\infty\) at fixed \(j\), by local finiteness. The Dirichlet kernel bound \(1/(\pi|v|)\) away from its center gives \(O_j(b_j W)\) for each of these inversions.

Take a good height \(S\in[T,T+1]\) by removing intervals of radius \(c/\log T\) around the \(O(\log T)\) nearby zero ordinates with \(c\) sufficiently small. On the rectangle with sides \(1-a,a\) the horizontal \(\xi'/\xi\) bound is \(O(\log^2 T)\) by classical local partial fractions. The holomorphic submean estimate \(|h_{j,T}(\beta+it)|\ll N/\sqrt{w(t)}\) on this interior strip, where \(N\) denotes the weighted strip norm, makes the horizontals \(o(1)\). Integrating the submean estimate in the ordinate in its local squared-integral form gives the vertical weighted \(L^2\) traces with norm \(O(N)\). Only fixed-distance comparability of the weight is needed for both estimates. After contour folding by the functional equation the right line test is \(h(a+it)+h(1-a-it)\). Expanding the absolutely convergent prime series gives the term
\[
 -\sum_n\Lambda(n)n^{-a}\bigl(I_{S,a}(\log n)+I_{S,1-a}(-\log n)\bigr).
\]
The previous kernel bounds and \(\sum_n\Lambda(n)n^{-a}<\infty\) control the non-target terms.

The gamma and rational terms are \(O(N)\) uniformly in \(S\). Indeed on each half-line the remainder after the log and constant parts of \(Q=\xi'/\xi-\zeta'/\zeta\) is \(O_a(1/|t|)\) by Stirling, and this and the compact ordinate interval are bounded by weighted Cauchy–Schwarz. For the log and constant parts let \(B_\beta\) be the Fourier transform of \((1-\theta(u))G_\beta(u)/(iu)\) for a smooth compact cutoff \(\theta=1\) near zero disjoint from all packets. Then \(B_\beta'=\widehat G_\beta\). The physical multiplier and all its derivatives are in ordinary \(L^2\); its Fourier transform thus lies in \(L^1\) with every fixed polynomial weight. Polynomial moderation of \(w\) and weighted convolution give \(O(N)\) bounds for \(B_\beta,B'_\beta\) in \(L^2(w)\). The unit-interval Sobolev bound yields \(|B_\beta(t)|\ll N/\sqrt{w(t)}\). Integrating by parts in the log term bounds both the boundary and the integral using \(\log|t|/\sqrt{w(t)}\to0\) and \(\int_3^\infty dt/(t\sqrt{w(t)})<\infty\). The constants use the same primitive, including after reflection on the second line. [Contour details and primary source locator](weighted152_signed_p1_campaign.md)

The packet alone therefore satisfies
\[
 \sum_{|\Im\rho|\le S}h_{j,T}(\rho)
 =-\frac{b_j\log p_j}{2\pi\sqrt{p_j}}\log(TW)+O_j(1)\longrightarrow-\infty
\]
at fixed \(j\). The small coefficient is harmless because \(\log(TW)=A\log\log T\) is unbounded. The arithmetic factor uses \(p_j^{-a}e^{(a-1/2)u_j}=p_j^{-1/2}\).

## Induction and admissibility

Each previously fixed packet has an absolutely bounded zero sum uniformly in height, by its compact smooth profile, repeated integration by parts uniformly for \(\Re\rho\in[0,1]\), and the classical unit-interval zero count. At stage \(j\) require the new witness sum through \(S_j\) to be below \(-j\) minus all these uniform bounds for the earlier packets. Also require its weighted norm to be at most \(2^{-j}\), and its *absolute* sum through each earlier \(S_i\) to be at most \(2^{-j}\). The last requirements concern finitely many zeros and follow from \(|h_{j,T}(\beta+it)|\ll_j b_j W\) on \([0,1]\). All requirements are compatible as \(T\to\infty\) at fixed stage. Take increasing good heights.

The locally finite sum \(F=\sum_j F_{j,T_j}\) is real and smooth. The physical test \(f(x)=x^{-1/2}F(\log x)\) vanishes near zero and near 1, and is \(O(x^{-3/2})\) at infinity by disjointness, \(b_j=e^{-u_j}\), and \(W_j<1\). This meets literal (A) and (B). Absolute physical integration on the closed strip identifies its Mellin transform with the sum of packet transforms. The weighted strip norm is finite by the triangle inequality and Fatou. The sum at each \(S_j\) can be evaluated packetwise since it uses finitely many zeros, and the later packets contribute at most \(\sum_{k>j}2^{-k}\). Conjugate symmetry gives real sums. Thus the full signed sums tend to minus infinity along \(S_j\). All prime samples vanish, and the pole and printed archimedean terms are finite by the value envelope and vanishing near 1.

## One test for all negative logarithmic powers

At stage \(j\) use \(q_j=1/j\), \(A_j=q_j/2\), and require \(N_{-q_j}(h_{j,T_j})\le2^{-j}\). For each individual stage \(A_j\) is fixed and strictly positive, so the witness still grows as \(A_j\log\log T\). The norm still tends to zero as \(T\to\infty\) because \(A_j<q_j\). Constants may depend on \(j\), which is fixed before choosing \(T_j\). The other induction constraints are unchanged. For each fixed \(q>0\), eventually \(q\ge q_j\), giving \(w_{-q}\le w_{-q_j}\) pointwise and hence the same summable weighted norms on the tail. The finite prefix has finite norm for every \(q\) by rapid decay. This single smooth test therefore belongs to each negative logarithmic strip space, with no asserted uniform bound as \(q\downarrow0\).
