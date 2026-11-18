# An arithmetic lower bound at the outer edge of negative heat zeros

**Proposed theorem.** Let \(L=\log X\), \(L^\nu\le F\le\sqrt L\) for fixed \(0<\nu\le 1/2\), \(u=F/L^2\), \(h=F/L\), and fix \(0<\eta<1\). For all sufficiently large \(X\), there are at least \(X/(hL^{C})\) distinct roots of \(J=F_{-u}\) satisfying
\[
 X<\Im\rho<2X,\qquad
                 (1-\eta)h<\Re\rho-1/2<(1+\eta)h .                     \tag{1}
\]
One can take an absolute \(C\); the starting height depends on \(\nu,\eta\). This complements the [positive-density root count](nov18b-heat-negative.md), which covers smaller \(F\) and allows all defects up to \(4h\). Here an arithmetic mean-square calculation forces roots arbitrarily close to the leading outer scale at regular physical ordinates. This theorem concerns strictly negative times.

## A large Dirichlet polynomial inside the candidate edge

Fix \(0<b<1\). Write \(s=1/2+bh+iT\), \(T\in[X,2X]\), \(G(s)=s(s-1)\pi^{-s/2}\Gamma(s/2)/2\), \(\alpha=G'/G\), and
\[
       D(T)=\frac{J(s)}{G(s)e^{-u\alpha(s)^2}},\qquad g_b=(1-b)^2/4 .
\]
There are absolute \(C_0,C_1\) such that
\[
 \int_X^{2X}|D|^2\,dT\gg_b X L F^{-1/2} e^{2g_b F},\qquad
 \int_X^{2X}|D|^4\,dT\ll_b X L^{C_0} e^{4g_b F}.                       \tag{2}
\]
In particular a set of measure at least \(X L^{-C_1}\) has \(|D(T)|>e^{g_b F/2}\). This follows by the second-moment lower bound, Cauchy–Schwarz on the upper level set, and the fourth-moment upper bound.

For the proof apply the balanced Hardy–Littlewood approximate functional equation to \(\zeta(s+ix)\) in the exact inverse Gaussian integral for \(J\), first for \(|x|\le1\). The standard sharp-cutoff error in a compact substrip of \(0<\sigma<1\) is \(O(T^{-\sigma/2})\) at balanced cutoffs; changing either cutoff to \(N_T=\lfloor\sqrt{T/(2\pi)}\rfloor\) changes at most one term of that same size. The gamma and functional equation factors have logarithmic Taylor errors \(O(1/T)\) on this interval, and the two raw absolute sums are \(O(X^{1/4+o(1)})\). The omitted Gaussian tail \(|x|>1\) dominates fixed powers of \(T\) by \(1/u\ge L^{3/2}\), using the fixed-strip bound for \(\xi\). The Gaussian integrals of either resulting exponential can be extended back to the full line at the same negligible cost. Normalization by \(e^{-u\alpha^2}\) costs \(e^{O(F)}=X^{o(1)}\). Thus
\[
 \begin{split}
 D(T)={}&\sum_{n\le N_T} n^{-s}
            e^{u(2\alpha\log n-\log^2 n)}\\
 &+\chi(s) e^{u\alpha^2}
       \sum_{n\le N_T}n^{s-1}
         e^{-u(\alpha+\chi'/\chi+\log n)^2}
             +O(X^{-1/6}),                                           \tag{3}
 \end{split}
\]
where \(\zeta(s)=\chi(s)\zeta(1-s)\). The error exponent can be replaced by a smaller fixed positive constant. For the classical balanced formula see Hardy–Littlewood, *The approximate functional equation for the zeta-function*, §4, or Titchmarsh, *The Theory of the Riemann Zeta-function*, Theorem 4.12.

Set \(q=(\log n)/L\), so \(q\le1/2+O(1/L)\), and write \(L_T=\log(T/(2\pi))\). Stirling gives \(2\alpha=L_T+i\pi/2+O(1/X)\), \(\chi'/\chi=-L_T+O(1/X)\). After extracting \(n^{-1/2}\), the real logarithmic weights of the two polynomials, including \(|\chi(s)|\) in the latter, are respectively
\[
        F[(1-b)q-q^2]+O(h),\qquad
        F[(1+b)q-q^2-b]+O(h).                                     \tag{4}
\]
The first parabola has maximum \(g_b\) at \(q_b=(1-b)/2\). The second has maximum on this range at the right endpoint, with value \(g_b-b^2/4+O(1/L)\). Fix \(q_1\) strictly between \(q_b\) and \(1/2\). The first polynomial restricted to \(q>q_1\) has an analogous strict loss.

For completeness, the mean fourth power of
\[
           \sup_{Y\le 2\sqrt X}\left|\sum_{n\le Y}n^{-1/2-iT}\right|
\]
is \(O(XL^{C_2})\). Decompose each prefix into at most \(O(L)\) dyadic index blocks of a decomposition of \([1,2^{\lceil\log_2(2\sqrt X)\rceil}]\). The fourth power of a prefix is bounded by \(O(L^3)\) times the sum of the fourth powers of its blocks. On one level the mean-value theorem for the squared Dirichlet polynomials, of length \(O(X)\), bounds the summed integrals by \(O(X\sum_{n\ll X}d(n)^2/n)=O(XL^4)\). In fact the sum of squared divisor counts restricted to disjoint blocks at a given product is at most \(d(n)^2\). Summing the levels proves the claim. Positive imaginary signs have the same bound by conjugation. Abel summation now bounds each weighted truncated polynomial in fourth mean by the same norm times the fourth power of its maximum weight and an extra fixed power of \(L\). Indeed on \(0\le q\le1/2+O(1/L)\) the complex weights are exponentials of quadratic polynomials with derivative \(O(1+F)\) times their magnitude, uniformly in \(T\). Any constant phase in the dual factor can be extracted first. This proves the upper bound in (2), and the second term and discarded first tail are exponentially smaller in \(F\) in quadratic mean than its proposed lower bound, since \(F\ge L^\nu\).

On \(q\le q_1\) replace \(2\alpha\) by \(L\). The remaining fixed weighted polynomial has coefficients of absolute size \(n^{-1/2}e^{F((1-b)q-q^2)}\). The squared coefficient sum \(S\asymp_b LF^{-1/2}e^{2g_bF}\) follows by summing \(1/n\) in the Gaussian window of width \(\asymp1/\sqrt F\) in \(q\), or by integral comparison. The mean-value theorem gives squared norm \((X+O(X^{q_1}))S\). To bound the replacement error, expand \(e^{u(2\alpha-L)\log n}-1\) in powers of \(u\log n\), with \(|2\alpha-L|\ll1\). The quadratic norm of each fixed polynomial with an additional \((\log n)^j\) costs at most \((q_1L)^j O(\sqrt{XS})\). Triangle inequality and summation in \(j\ge1\) lose \(O(h\sqrt{XS})\). This proves the lower bound in (2). The same ordinary balanced approximate functional equation, partial summation and fourth-mean bound imply \(\int_X^{2X}|\zeta(1/2+h+iT)|^2dT\ll XL^{C_2}\); the direct primal weight decreases, while the dual weight with \(|\chi|\) is bounded and has bounded variation. We only need this deliberately coarse mean estimate.

## Contradiction if an annulus is free of roots

Put \(b_0=1-\eta\), choose \(b\) strictly between \(b_0\) and 1, and use the physical regularity bounds from the [mesoscopic estimate](nov18b-heat-local-density.md). Their failure fraction is \(O_A(F^{-A})\), where \(A\) can be chosen after \(\nu,C_1\). On deleting this exceptional set, the heights within a fixed distance of the dyadic ends, and the set with
\[
             |\zeta(1/2+h+iT)|>e^{g_bF/10},
\]
at least \(X L^{-C_1}/2\) large-value heights from (2) remain, for sufficiently large \(X\). The last deletion uses the preceding quadratic bound and \(F\ge L^\nu\).

We detail the change to the outer-cone and continuation estimates for negative time in the [gap argument](nov18b-heat-negative.md). At a retained center the outer estimate \(J'/J=L/2+O(\epsilon L+L/F)\) holds for \(r=\Re s-1/2\ge(1+\eta/2)h\) in any fixed aperture \(|\Im s-T|\le B r\), up to a fixed upper bound on \(r\). Indeed its saddle in \(\xi\) has real displacement \(r-h+O(\epsilon h)\), now at least \(\eta h/3\). Use physical control with the corresponding smaller positive depth, and restrict the inner Taylor disk to \(c_\eta h\). The dyadic tail argument there uses distances to source poles \(\gg_{\eta,B} h\), their count \(O_{\eta,B}(kL)\) for radii \(k\ge h\), and the outer Gaussian comparison is unchanged after increasing its fixed cutoff. Decrease the minimum displacement a little further for the Cauchy derivative. In particular the comparison of stationary size at \(r=2h\) with the real approximate saddle gives, with \(s_2=1/2+2h+iT\),
\[
 \log\left|\frac{J(s_2)}{G(s_2)e^{-u\alpha(s_2)^2}}\right|
          \le \log|\zeta(s_2-h)|+O(\epsilon F)+O(1).
                                                                    \tag{5}
\]
To see the normalization, the stationary factor is \(e^{F/4}\xi(s_2-h)\) up to a log-modulus error \(O(\epsilon F+1)\), by the saddle displacement estimate and integrating the physical log derivative locally. Stirling gives \(\log|G(s_2-h)/G(s_2)|=-F/2+O(h)\), and \(u\Re\alpha(s_2)^2=F/4+O(h)\).

Suppose that no \(J\)-zero of defect in \((b_0 h,(1+\eta)h)\) has ordinate within \(K h\) of the retained center, with a sufficiently large fixed \(K\). In the symmetric local disk about that center, the remaining reflected pole pairs either have \(|a|\le b_0h\), or are separated in ordinate from \(T\) by at least \(4|a|\). This follows from the hypothesis for the middle annulus and the outer cone for higher pairs; for middle pairs outside \(Kh\), use \(K>4(1+\eta)\). At the anchor \(4h\) every pair, including the small pairs, consequently contributes real part \(\gg h/(h^2+(T-\gamma)^2)\) by the paired Poisson formula. The disk factorization therefore gives the weighted count \(\sum h/(h^2+(T-\gamma)^2)\ll L\) as before. On each compact subset of the rescaled strip \(\Re z>b_0\) of bounded width and bounded rescaled height around \(T\), all denominators \(1/2+hz+iT-\rho\) have modulus \(\gg h+|T-\gamma|\) on taking \(K\) and the cone aperture sufficiently large, because a small pair now has real separation \(\gg h\). Subtract the pole sum at \(4h\). The weighted count gives a normal family of scaled logarithmic derivatives, and identity continuation from the outer disk gives
\[
 \left|J'/J(1/2+r+iT)-L/2\right|\le\epsilon' L
                      \qquad(bh\le r\le 2h)
\]
for every prescribed \(\epsilon'>0\). In this assertion choose the physical tolerance sufficiently small after fixing \(\epsilon'\), as in the compactness proof in the gap argument. Integrating in \(r\), subtracting the log derivative of \(G e^{-u\alpha^2}\), and applying (5) bound \(\log |D(T)|\) by \(g_bF/10+O((\epsilon+\epsilon')F)+O(1)\). Choosing the tolerances small contradicts \(|D(T)|>e^{g_bF/2}\).

Each retained large-value height therefore forces one root in (1) within \(Kh\). A root covers at most \(2Kh\) heights, which proves the stated count after changing \(C\). Both the Fourier weights in (3) and the leading coefficient one in (1) depend on the physical arithmetic content of xi.
