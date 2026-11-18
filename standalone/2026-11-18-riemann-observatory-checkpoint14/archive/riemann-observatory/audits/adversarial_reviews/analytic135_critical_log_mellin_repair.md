# Critical logarithmic Mellin norm for the raw-height explicit formula

The weighted strip repair extends to a half-derivative scale with a logarithmic weight. A logarithmic exponent \(p>3\) gives both absolute zero sampling and the Dini modulus needed at the archimedean endpoint. No separate central-trace assumption or RH is required. This is a sufficient condition. The endpoint \(p=3\) and optimality are outside the result. [Previous Sobolev repair](analytic132_mellin_trace_repair.md) · [Pinned formula and scope](analytic131_explicit_formula_countermodel_adjudication.md)

## Statement and zero sampling

Let \(f:(0,\infty)\to\mathbb C\) be continuous, with \(f(x)=O(x^\delta)\) near zero and \(f(x)=O(x^{-1-\delta})\) near infinity for some \(\delta>0\). Fix \(0<\epsilon<\delta\), \(p>3\), and write
\[
 w_p(t)=\langle t\rangle[\log(e+|t|)]^p,qquad
 \mathcal N_p(f)^2=\int_{-\epsilon}^{1+\epsilon}\int_{\mathbb R}
          w_p(t)|\widehat f(\beta+it)|^2dt\,d\beta<\infty .
\]
Here \(\langle t\rangle=(1+t^2)^{1/2}\) and \(\widehat f(z)=\int_0^\infty f(x)x^{z-1}dx\), holomorphic on the whole value-decay strip. Then the absolute zero sum is at most \(C_{p,\epsilon}\mathcal N_p(f)\), and its tail for \(T\ge2\) satisfies
\[
 \sum_{|\Im\rho|\ge T}|\widehat f(\rho)|
 \le C_{p,\epsilon}\mathcal N_p(f)[\log(2+T)]^{(3-p)/2}.
\]
All zeros carry their multiplicities. For \(\widetilde f(x)=x^{-1}f(1/x)\), the ordinary raw-height explicit formula in the pinned p. 6 normalization is
\[
\begin{aligned}
 \sum_\rho \widehat f(\rho)
 &=\int_0^\infty [f(x)+\widetilde f(x)]dx
   -\sum_{n\ge1}\Lambda(n)[f(n)+\widetilde f(n)]\\
 &\quad -(\log\pi+\gamma)f(1)
   -\int_1^\infty
       \left(f(x)+\widetilde f(x)-\frac{2f(1)}{x^2}\right)
       \frac{x\,dx}{x^2-1}.
\end{aligned}
\]
All displayed terms are absolutely defined.

For the sampling bound choose \(r=\min(\epsilon/4,1/4)\) and let \(E_n\) be the weighted strip energy on heights \([n-r,n+1+r]\). A disk of radius \(r\) centered anywhere in \([0,1]+i[n,n+1]\) stays inside the strip and this height interval. The mean inequality for \(|\widehat f|^2\), with comparability of \(w_p\) on expanded unit intervals, gives the uniform cell bound \(C_{p,\epsilon}w_p(n)^{-1/2}E_n^{1/2}\). The intervals have bounded overlap. The unconditional number of zeros in a unit-height strip with multiplicity is \(O(\log(2+|n|))\). Hence Cauchy–Schwarz bounds the sum in any block collection by the square root of its energy times the square root of
\[
 \sum_n \frac{\log^2(2+|n|)}{w_p(n)}.
\]
This series is finite for \(p>3\). For the tail, the relevant cells have \(|n|\ge T-1\), and the series there is \(O_p([\log(2+T)]^{3-p})\) by integrating \(1/(t\log^{p-2}t)\). No location inside the critical strip enters beyond inclusion in it.

The same bound on the cell supremum gives \(\sup_{\beta\in[0,1]}\|\widehat f(\beta+i\cdot)\|_{L^2(w_pdt)}\le C_{p,\epsilon}\mathcal N_p(f)\) after integrating over each unit cell and summing. In particular the central trace is controlled for the **specified** line \(\beta=1/2\), without selecting a line of almost-everywhere regularity.

## From the central trace to an integrable endpoint modulus

Put \(G_\beta(u)=e^{\beta u}f(e^u)\), \(F=G_{1/2}\). These profiles are in \(L^1\cap L^2\) throughout the closed excess strip. Our Mellin transform on each line is the Fourier transform of \(G_\beta\) with positive phase. Since \(w_p^{-1}\in L^1\), Cauchy–Schwarz shows that the Fourier transform of \(F\) is integrable, so Fourier inversion identifies the original continuous \(F\) pointwise.

Let \(0<|h|\le1/4\) and \(R=|h|^{-1}\). Fourier inversion and Cauchy–Schwarz give
\[
 \sup_u|F(u+h)-F(u)|
 \ll_{p,\epsilon}\mathcal N_p(f)
 \left(\int_{\mathbb R}\frac{\min(4,|h|^2t^2)}{w_p(t)}dt\right)^{1/2}.
\]
The part \(|t|\le\sqrt R\) costs \(O(R^{-1})\), since \(t^2/\langle t\rangle\le |t|\). For \(\sqrt R<|t|\le R\), use \(\log(e+|t|)\gg\log R\) and integrate \(|t|\) to obtain \(O_p((\log R)^{-p})\) after the factor \(h^2\). Finally the tail \(|t|>R\) costs \(O_p((\log R)^{1-p})\) by integrating \(1/(t\log^p t)\). Thus
\[
 \omega_F(h)\ll_{p,\epsilon}
 \mathcal N_p(f)[\log(e/|h|)]^{(1-p)/2}.
\]
This modulus is Dini for \(p>3\), since its quotient by \(h\) is integrable near zero under the change of variable \(v=\log(e/h)\).

For the archimedean denominator set \(x=e^u\), \(u>0\). The numerator is
\[
 e^{-u/2}(F(u)+F(-u))-2e^{-2u}F(0)
   =O(\omega_F(u)+|F(0)|u).
\]
The measure \(x\,dx/(x^2-1)\) is \(O(du/u)\) near zero. The Dini bound and the value bounds therefore make the archimedean integral absolutely convergent. The same value bounds apply to \(\widetilde f\) and make the ordinary integrals and the prime sum absolutely convergent.

## Approximation in the same critical norm

Equip log-coordinate profiles with the norm \(\|m_p\widehat G\|_2\), where \(m_p=w_p^{1/2}\). The weight is moderate in the multiplicative form
\[
 m_p(t+v)\le C_p m_p(t)m_p(v).
\]
Indeed \(\langle t+v\rangle\ll\langle t\rangle\langle v\rangle\), while \(\log(e+|t+v|)\le\log(e+|t|)+\log(e+|v|)\le2\log(e+|t|)\log(e+|v|)\). Choose smooth even compact \(\chi\) with \(0\le\chi\le1\), equal to one on \([-1,1]\), and set \(\chi_R(u)=\chi(u/R)\) for \(R\ge1\). The weighted \(L^1(m_pdt)\) norms of \(\widehat\chi_R\) are uniformly bounded by scaling and Schwartz decay. Thus multiplication by \(\chi_R\) is uniformly bounded on the profile spaces by weighted Young's inequality.

For completeness, strong convergence of these multipliers follows by density of Schwartz profiles in the weighted Fourier space and then approximating a Schwartz profile by its cutoffs. Schwartz density follows by approximating its Fourier transform in weighted \(L^2\) by compact smooth functions. For a Schwartz profile the cutoff error tends to zero in every fixed integer \(H^j\), by the product rule and rapid decay. A sufficiently large \(j\) controls the critical log norm as well. Uniform multiplier boundedness then proves strong convergence for all profiles in the space. Apply this on almost every \(\beta\)-line and use integrated dominated convergence to show \(\mathcal N_p(f_R-f)\to0\) for \(f_R(x)=\chi_R(\log x)f(x)\). Sampling gives convergence of their zero sums. In the ordinary and prime terms, the value envelopes dominate the cutoffs, and evenness gives the same cutoff for \(\widetilde f_R\). Near 1 the archimedean numerator is unchanged.

At fixed \(R\), mollify \(\chi_R F\) by a nonnegative real even smooth compact approximate identity \(\varphi_\tau\). Mapping back gives smooth compact log-coordinate tests \(f_{R,\tau}(x)=x^{-1/2}(\varphi_\tau*(\chi_R F))(\log x)\). The \(\beta\)-profiles are convolutions of \(\chi_R G_\beta\) against \(e^{(\beta-1/2)u}\varphi_\tau(u)\). The Fourier multipliers are uniformly bounded on the whole excess strip and converge pointwise to one. Dominated convergence gives \(\mathcal N_p(f_{R,\tau}-f_R)\to0\).

The central profiles \(\chi_R F\) have Dini modulus, because the product adds at most a fixed Lipschitz term to the preceding modulus. Convolution with the nonnegative mollifier preserves this common modulus at fixed \(R\). Therefore the mollified archimedean numerators are dominated near zero by a common Dini modulus plus a linear term, as above. The other arithmetic terms converge by uniform convergence on common compact support at fixed \(R\), including the finitely many prime arguments. Apply the usual smooth compact explicit formula to \(f_{R,\tau}\), let \(\tau\downarrow0\) at fixed \(R\), and then let \(R\to\infty\). This proves the displayed formula using only its classical smooth compact starting class. [Compact starting formula and cutoff conventions](analytic132_mellin_trace_repair.md)

The matching logarithmic thresholds in this proof come from the \(\log t\) unit zero count, squared for sampling, and the \(du/u\) singularity, integrated against the central modulus. Fixed compact jump tests used in Theorem 2 have a discontinuous central log profile, so cannot have this central Fourier integrability. Their endpoint and midpoint argument is separate. No canonical edit or priority claim is made. [Compact jump justification](analytic131_explicit_formula_countermodel_adjudication.md)
