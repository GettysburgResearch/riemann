# A candidate corrected threshold for the weighted closure

2026-11-17. Independent mathematical reconstruction, with novelty and independent proof review pending. The sufficiency proof below adapts Báez-Duarte's Mellin argument. It depends on the quoted uniform Balazard–Saias estimate, classical zeta convexity and the Hadamard product. No outreach.

Put \(t=-(\alpha+1)/2\), \(c=a-1\), and \(b=t-c\), using the notation and the original parameter range from the [weighted closure audit](../../audits/adversarial_reviews/gallardo_seco_weightedcore62_round5.md). The proposed corrected statement for the same target, generators, and parameter range is
\[
 (1-z)^{-c}\in\overline{\operatorname{span}\{(1-z)^{-c}h_k:k\ge2\}}^{D_{\alpha+2}}
 \quad\Longleftrightarrow\quad
 \zeta(s)\ne0\text{ for }\Re s>b .
\]
Necessity is the radial Mellin separation in the audit. If \(b<1/2\), both statements fail unconditionally, as existence and reflection of nontrivial zeros give one with real part at least \(1/2\). If \(b=1\), then \(t=1,c=0\), the Euler product gives the right-hand side and the previously established unconditional Bergman density gives the left-hand side. The rest concerns \(1/2\le b<1\).

## Uniform quotient across the zero-free boundary

Assume \(\zeta(s)\ne0\) for \(\Re s>b\). For \(0<\epsilon\le\epsilon_0<\min(b/2,(1-b)/2,1/4)\), write \(s_\pm=b\pm\epsilon+iy\). Hadamard's canonical product for the completed entire \(\xi\) gives
\[
 \xi(s)=\exp(A+Bs)\prod_{\rho}\left(1-\frac{s}{\rho}\right)e^{s/\rho}.
\]
The product runs over nontrivial zeros with multiplicity and converges on compact sets. For every zero \(\rho\), \(|s_--\rho|\le |s_+-\rho|\) since \(\Re\rho\le b\). The absolute ratio of the corresponding exponential factors is \(\exp(-2\epsilon\Re(1/\rho))\le1\) because \(\Re\rho>0\). The quotient for every partial product is thus bounded by \(\exp(2\epsilon|\Re B|)\). Pass to the limit using \(\xi(s_+)\ne0\). Inserting
\[
 \xi(s)=\tfrac12 s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s)
\]
and applying uniform Stirling bounds on the two vertical lines gives
\[
 \left|\frac{\zeta(s_-)}{\zeta(s_+)}\right|
 \ll_{b,\epsilon_0} (1+|y|)^\epsilon . \tag{1}
\]
For bounded \(y\) the gamma and polynomial factors and their inverses are bounded, since the real parts of \(s_\pm\) lie in a fixed compact subinterval of \((0,1)\). For large \(y\), the quotient of gamma factors in this direction grows as \(|y|^\epsilon\), and the polynomial-factor quotient is bounded.

## Approximation in the unweighted coefficient space at the shifted exponent

Let \(\varrho_k(x)=\{1/(kx)\}\), \(\chi=\mathbf 1_{(0,1)}\), and \(H_b=L^2((0,\infty),x^{2b-1}dx)\). Mellin Plancherel on the line \(\Re s=b\) maps this space isometrically to \(L^2(\mathbb R,dy/(2\pi))\) under \(\mathcal M_bf(y)=\int_0^\infty f(x)x^{b+iy-1}dx\) on the intersection where it converges. The classical absolutely convergent transform in \(0<\Re s<1\) is
\[
 \int_0^\infty \varrho_k(x)x^{s-1}dx=-k^{-s}\frac{\zeta(s)}s.
\]
For fixed \(\epsilon\) in (1) define
\[
 F_{\epsilon,N}(x)=\sum_{k\le N}\frac{\mu(k)}{k^{2\epsilon}}\varrho_k(x).
\]
Then
\[
 \mathcal M_b(x^{-\epsilon}F_{\epsilon,N})(y)
 =-\frac{\zeta(s_-)}{s_-}\sum_{k\le N}\frac{\mu(k)}{k^{s_+}} .
\]
The Balazard–Saias estimate as reproduced in Báez-Duarte's Lemma 2.1 applies for base abscissa \(b\), shift \(\delta=\epsilon\), and every fixed \(\eta>0\). It gives a uniform error \(O_{b,\epsilon,\eta}(N^{-\epsilon/3}(1+|y|)^\eta)\) from \(1/\zeta(s_+)\). Thus the pointwise limit of the transforms as \(N\to\infty\) is \(-\zeta(s_-)/(s_-\zeta(s_+))\). By (1) its absolute value is \(O((1+|y|)^{-1+\epsilon})\). The transform error in absolute value is bounded by
\[
 O_{b,\epsilon,\eta}\big(N^{-\epsilon/3}
 (1+|y|)^{-1+(1-b+\epsilon)/2+2\eta}\big)
\]
using the classical convexity bound on the compact set of real parts in use. Choose \(\eta>0\) small enough that \(4\eta<b-\epsilon\). This bound and the bound on the limit are square-integrable in \(y\). Therefore \(x^{-\epsilon}F_{\epsilon,N}\) converges in \(H_b\) as \(N\to\infty\). [Báez-Duarte, arXiv:math/0202141, Lemma 2.1 and proof of Theorem 1.1](https://arxiv.org/pdf/math/0202141)

For every fixed \(x>0\), cancellation of the linear terms against the floor identity gives the pointwise limit
\[
 F_\epsilon(x)=
 \frac{1}{x\zeta(1+2\epsilon)}
 -\sum_{k\le 1/x}\frac{\mu(k)}{k^{2\epsilon}}
                   \left\lfloor\frac1{kx}\right\rfloor .
\]
The \(H_b\) limit just identified is \(x^{-\epsilon}F_\epsilon\), by uniqueness of the pointwise limit along any subsequence converging almost everywhere in addition to norm. On \((0,1)\), convergence for \(F_{\epsilon,N}\) itself follows since \(x^\epsilon\le1\). On \([1,\infty)\), each \(F_{\epsilon,N}\) equals a scalar times \(1/x\) with scalar converging by absolute convergence. Since \(b<1\), \(1/x\) belongs to \(H_b\) on this interval. Thus \(F_\epsilon\) lies in the \(H_b\) closure of the natural fractional-part span.

As \(\epsilon\downarrow0\), (1) provides the dominating square-integrable bound \(O((1+|y|)^{-1+\epsilon_0})\) for \(\mathcal M_b(x^{-\epsilon}F_\epsilon)\). These transforms tend pointwise for all \(y\) except possible zeros on the boundary line to \(-1/(b+iy)=\mathcal M_b(-\chi)(y)\). The exceptional real ordinates form a discrete set and hence have measure zero. Dominated convergence and Mellin Plancherel give \(x^{-\epsilon}F_\epsilon\to-\chi\) in \(H_b\). Multiplication by \(x^\epsilon\) on \((0,1)\) preserves convergence to \(-\chi\), since it is contractive there and \((x^\epsilon-1)\chi\to0\) in norm. On \([1,\infty)\), \(F_\epsilon=x^{-1}/\zeta(1+2\epsilon)\) converges to zero in \(H_b\) by the pole at 1. Hence \(\chi\) belongs to the \(H_b\) closure of the natural fractional-part span.

Now choose a sequence of finite sums \(G_m=\sum_k d_{k,m}\varrho_k\) converging to \(\chi\) in \(H_b\). On \((1,\infty)\), \(G_m=A_m/x\) with \(A_m=\sum_k d_{k,m}/k\), so \(A_m\to0\). Then \(G_m-A_m\varrho_1\to\chi\) in \(H_b\), and the adjusted sum is a finite linear combination of the functions \(k\varrho_k-\varrho_1\). On \(x\in(1/(n+1),1/n)\), \(k\varrho_k(x)-\varrho_1(x)=r_k(n)\). The \(H_b\) masses of these intervals are comparable to \(n^{-1-2b}\), by the mean value theorem. This proves
\[
 f_0\in\overline{\operatorname{span}\{R_k:k\ge2\}}^{D_{-1-2b}} .
 \tag{2}
\]

## Lifting (2) to the weighted closure

Since \(-1-2b=\alpha+2c\), division by \(h=(1-z)^c\) maps \(D_{-1-2b}\) boundedly to \(D_\alpha\). For \(c=0\) this is the identity. For \(c>0\), let \(p=-\alpha/2\). In normalized coefficient coordinates the positive convolution matrix is bounded entrywise by a constant times
\[
 A_{nj}=(n+1)^{-p}(n-j+1)^{c-1}(j+1)^{p-c}\mathbf1_{j\le n}.
\]
On \(j+1\ge(n+1)/2\), each row and column sum is uniformly bounded: the summand is controlled by a constant times \((n+1)^{-c}(n-j+1)^{c-1}\), and the sum of the last factor over a comparable interval is \(O((n+1)^c)\) for rows and \(O((j+1)^c)\) for columns. On \(j+1<(n+1)/2\), it is bounded by a constant times \((n+1)^{-p+c-1}(j+1)^{p-c}\). Row and column sums are uniformly bounded since \(p-c=b+1/2>0\). The Schur test proves boundedness. It follows from (2) that the same approximants converge in the pullback norm \(\|g/h\|_{D_\alpha}\).

The strict operator repair gives \(T_a:D_{\alpha+2}\to D_\alpha\) a bounded inverse for \(a>t\), which holds in every case under consideration. Thus \(hT_a\) maps \(D_{\alpha+2}\) isomorphically onto \(W_{\alpha,c}\). Its images of \(u,uh_k\) are \(-f_0,R_k\) respectively, proving the sufficiency claim. The excluded pair \(a=t=1\) has already been addressed by unconditional Bergman density. [Coefficient Hardy proof of the strict operator repair](../../audits/adversarial_reviews/gallardo_seco_operator_impact_advocate_round4.md)

## Dependency locations

The adaptation uses Lemma 2.1 in the actual arXiv:math/0202141v2 PDF, p. 3. The authors identify it as Lemma 2 of Balazard–Saias, *Notes sur la fonction ζ de Riemann, 1*, Advances in Mathematics 139 (1998), 310–321. This draft verifies the precise statement in Báez-Duarte's reproduction and does not independently audit the original 1998 proof. The completed-function Hadamard product and functional-equation reflection are in Titchmarsh (1986), §2.12, equation (2.12.5). The zero-count input for \(b<1/2\) is his Theorem 9.4. [Báez-Duarte preprint](https://arxiv.org/pdf/math/0202141v2) [Balazard–Saias DOI](https://doi.org/10.1006/aima.1998.1760) [Titchmarsh local PDF](../../sources/equivalence_round2/titchmarsh1986.pdf)
