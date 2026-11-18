# Polynomial prime-band covariance and its rooted CUE counterpart

18 November 2026. Assume RH for the arithmetic statements. Draw an ordinate \(\gamma\) from the symmetric strict derivative-weighted tail \(|\gamma|>Y\), with masses proportional to \(|\zeta'(1/2+i\gamma)|^2/(1/4+\gamma^2)\). For fixed \(0<a<b<1/4\) put
\[
 S_Y=\{p:Y^a<p\le Y^b\},\quad
 W_c=\sum_{p\in S_Y}\frac{\cos(\gamma\log p)}{\sqrt p},
 \quad W_s=\sum_{p\in S_Y}\frac{\sin(\gamma\log p)}{\sqrt p},
 \quad \Delta_j=b^j-a^j .
\]
The mean, true centered variances and cross covariance are
\[
 \begin{aligned}
 \lim E W_c&=\log(b/a)-4\Delta_1+\tfrac23\Delta_3=:\mu,\\
 \lim\operatorname{Var}(W_c)&=\tfrac12\log(b/a)
       -4\Delta_1^2+4\Delta_1\Delta_3-\tfrac49\Delta_3^2=:V_c,\\
 E W_s&=0,\qquad \lim\operatorname{Var}(W_s)=\tfrac12\log(b/a)-\tfrac32\Delta_2^2=:V_s,\\
 \operatorname{Cov}(W_c,W_s)&=0 .
 \end{aligned}
\]
In particular \(\lim E W_c^2=\mu^2+V_c\) and \(\lim E W_s^2=V_s\). Both limiting variances are strictly smaller than the independent Poisson-circle prediction \(\frac12\log(b/a)\). The same mean and covariance are obtained by a high Fourier band of the log characteristic polynomial in the derivative-square tilted rooted CUE ensemble, as proved separately below. The agreement concerns first and second moments. It gives no distributional limit for either high band, no unweighted zero statement, and no transfer of a random-matrix CLT. Publication priority is unassessed. [Earlier first-moment computation](prime70_hlz_cutoff_extension.md) · [HLZ primary source, Theorem 5 and equations (5), (24)](../../sources/classical63_derivative_moments/hlz2022print.pdf)

## 1. The three HLZ coefficients

At a symmetric prefix height \(T\ge Y\), set \(x=\log p/\log T,\ y=\log q/\log T\). The normalized factor for one prime is \(F(x)=1-4x+2x^3\) as before. For distinct primes \(p,q\), put
\[
 K_0(x,y)=F(x)+F(y)-1+12xy-2xy(x^2+y^2).
\]
The normalized arithmetic factors, leaving the original lcm denominators outside, are
\[
 K_{\rm ratio}(x,y)=K_0(x,y)-6x^2y^2,\qquad
 K_{\rm prod}(x,y)=K_0(x,y)+6x^2y^2,
 \qquad K_{\rm square}(x)=1-8x+6x^2+10x^3+x^4.
\]
The first corresponds to \((m,n)=(p,q)\), the second to \((pq,1)\), and the last to \((p^2,1)\). The lcm denominators are \(pq,pq,p^2\), respectively. These are coefficient formulas for the main term, with a common shifted error only asserted for the aggregate polynomials used below.

Here are details of the extraction. Scale the three shifts to \(\alpha,\beta,c\) in units of \(1/\log T\), on the separated circles as in the earlier audit. Write \(A(z)=e^{-uz}+e^{-wz}-1\) for a tuple of shifted variables \(u,v,w\) in \(I\). In the exact local quotient, a prime in the \(h\) slot supplies \(e^{-vx}\), and a prime in the \(k\) slot supplies \(A(x)+O(1/p)\) at exponent one. At exponent two the latter supplies \(e^{-2ux}+e^{-(u+w)x}+e^{-2wx}-e^{-ux}-e^{-wx}+O(1/p)\). Both estimates follow by setting \(z=p^{-1+O(1/\log T)}\) to zero in the exact local quotient from the first-moment proof. All exponential factors are bounded uniformly on the circles and the errors are uniform in the band. Thus the leading symmetrized \(I\) factors for ratio and product are
\[
 \tfrac12\{e^{-vx}A(y)+e^{-vy}A(x)\},\qquad
 \tfrac12\{e^{-v(x+y)}+A(x)A(y)\}.
\]
For the square, average the exponent-two expression above and \(e^{-2vx}\).

The three \((u,v,w,t)\) tuples in \(I(\alpha,\beta)\) are \((\alpha,\beta,c,0)\), \((-\beta,-\alpha,c,-\alpha-\beta)\), and \((\alpha,-c,-\beta,-\beta-c)\). After integrating the time factors and dividing by \(T\), the fourth slot supplies \(e^t\). The zeta quotient supplies \(\log T\) times \(v/((u+v)(v+w))\). The analogous \(J\) terms supply \(1/(\alpha+\beta)\) and \(-e^{-\alpha-\beta}/(\alpha+\beta)\) with their monomial factors, after extracting its time logarithm and \((\log T)^2\). These replacements have normalized errors \(O(1/\log T)\) uniformly on the circles. For \(J\) at ratio \(p/q\), the two symmetrized direct exponents are \(-\beta x-\alpha y,-\beta y-\alpha x\), and the two dual exponents besides \(-\alpha-\beta\) are \(\alpha x+\beta y,\alpha y+\beta x\). At the product and square they are the corresponding one-slot exponents with \(x+y\) and \(2x\).

In the Cauchy coefficient integrals, simultaneous rotation keeps just total degree two in \(J\) and three in \(I\) before the auxiliary derivative. Therefore take cubic exponential terms in \(J\) and quartic ones in \(I\), multiply by their zeta quotient rational factors, and differentiate once in \(c\) at zero in \(I\). Add the reflected \(I\) with outer shifts exchanged. The symmetries are the same as used in the four-sign polarization, which requires only the real coefficients here. The resulting coefficients of \(\alpha\beta\) in \(J\) and \(I+I^{\rm refl}\) sum to the displayed \(K/12\), all checked by exact rational polynomial operations. The factor \(1/12\) is the untwisted leading coefficient under the normalization \(T(\log T)^4/(2\pi)\). Errors from the local replacements and rescaling are \(O(1/\log T+1/p+1/q)\) after extracting normalized coefficients, with \(1/q\) omitted for the square. [Exact coefficient program and CUE check](../../scripts/prime71_hlz_band_variance_check.py) · [Recorded output](../../experiments/results/prime71_hlz_band_variance_check.txt)

## 2. Aggregate error, strict tail and variance

Write \(D(s)=\sum_{p\in S_Y}p^{-s}\), so \(W_c=\Re D(\rho)\), \(W_s=-\Im D(\rho)\). Use the exact identities
\[
 W_c^2=(|D(\rho)|^2+\Re(D(\rho)^2))/2,\qquad
 W_s^2=(|D(\rho)|^2-\Re(D(\rho)^2))/2.
\]
The first quadratic term uses a polynomial of length \(Y^b\). The second uses polarizing \(D^2\) against \(1\), hence length \(Y^{2b}\). The coefficients of \(D,D^2,1\) are bounded by \(1,2,1\) respectively. The divisor-closed baseline and exact four-sign cancellation in the earlier note apply uniformly at a fixed declared HLZ length \(T^\delta\) with \(2b<\delta<1/2\). In particular the logarithmic saving in the source is for the complete polarized polynomial pair. It is never multiplied by the number of primes or distinct prime pairs. Declaring length \(Y^b\) for \(D^2\) would give an unsupported range.

The \(p=q\) terms in \(|D|^2\) are exactly \(\sum_{p\in S_Y}1/p\). The \(p=q\) terms in \(\Re(D^2)\) have main part \(\sum_{p\in S_Y}K_{\rm square}(x)/p^2\), which tends to zero, as does its normalized aggregate error. The distinct ordered pairs appear with factor \(1/(pq)\) and symmetric real kernels. The local and scaling errors sum to \(o(1)\) since \(H_S=\sum_{p\in S_Y}1/p=O(1)\) and \(\min S_Y\to\infty\). Therefore the arithmetic symmetric prefix second moments are a diagonal half-\(H_S\) plus the distinct ordered pair sum with kernels \((K_{\rm ratio}\pm K_{\rm prod})/2\), with \(o(1)\) uniform for \(T\ge Y\).

Both kernels are Lipschitz on \([0,b]^2\). Substituting \(\log Y\) for \(\log t\) in the prefix comparison changes the main target by \(O(H_S^2\log(t/Y)/\log Y)\). As with the first moment, the strict Stieltjes boundary is exact at \(t=Y\), and the integral of this change divided by the tail mass is \(O(H_S^2/\log Y)\) using \(A(t)\asymp t(\log t)^4\). So the tail moments have the same target at \(T=Y\). Mertens on fixed bands gives convergence of the measures \(\sum_{p\in S_Y}p^{-1}\delta_{\log p/\log Y}\) to \(dx/x\) on \([a,b]\). Removing \(p=q\) from the product measures costs \(o(1)\).

Subtract the true limiting cosine mean squared by subtracting \(F(x)F(y)\) under the double integral. The resulting covariance kernel away from the diagonal is
\[
 C_c(x,y)=xy[-4+6x^2+6y^2-4x^2y^2],\qquad
 C_s(x,y)=-6x^2y^2 .
\]
Integrating against \(dx/x\,dy/y\) yields the formulas stated above. Both corrections are strictly negative on the band. For example \(C_c/(xy)\le -4+12b^2<0\). Reflection gives the zero sine mean and vanishing mixed covariance exactly without a one-sided complex HLZ theorem. All steps also work for fixed bounded Riemann-integrable factors \(f(\log p/\log Y)\) and \(g(\log p/\log Y)\) multiplying the respective prime weights, with possible distinct sub-bands of a common \([a,b]\). For two cosine tests the covariance is \(\tfrac12\int fg\,dx/x+\iint f(x)g(y)C_c(x,y)dx\,dy/(xy)\); for two sine tests use \(C_s\). Their main correction operators have ranks at most two and one, respectively, because \(C_c\) is spanned by \(x,x^3\) in each slot and \(C_s\) is a product of \(x^2,y^2\). The weighted-test proof follows by polarizing the same bounded arrays, or expanding the product into the same pairs. Products of bounded Riemann-integrable weights with the continuous kernels have the required Riemann-sum limits.

## 3. Exact first-two-moment comparison with the derivative-square tilted rooted CUE

Let \(U\) be Haar on \(U(N)\). Distinguish an eigenvalue by giving the pair \((U,j)\) weight proportional to \(|Z'(\theta_j)|^2\), where \(Z\) is the usual unitary characteristic polynomial as a function of angle, and rotate so the distinguished eigenvalue is 1. The Haar density and identity \(|Z'(\theta_j)|=\prod_{m\ne j}|e^{i\theta_m}-e^{i\theta_j}|\) are equations (2.2)–(2.7) of Hughes–Keating–O'Connell, §2(a). Consequently the \(N-1\) free eigenvalues in the rotated configuration have density proportional to their circular Vandermonde squared times \(\prod_m|1-e^{i\theta_m}|^4\). This is a finite-\(N\) identity, using rotation invariance and the square weight. The cited paper studies the derivative and does not supply the Fourier-band calculation below. [Hughes–Keating–O'Connell, Proc. R. Soc. Lond. A 456 (2000), DOI 10.1098/rspa.2000.0628](../../sources/analytic64_prime_phase_clt_priority/hko.pdf)

The free eigenvalues form a projection determinantal ensemble on the circle, with reference measure \(d\theta/(2\pi)\). To see the projection directly, take the span of \((z-1)^2z^j,\ 0\le j\le N-2\), for \(z=e^{i\theta}\). The squared determinant of evaluation of this basis is exactly the density just described, up to its normalizing constant. After orthonormalizing the basis, it is the projection determinant. If \(P_0\) projects onto the modes \(0,\ldots,N\), this subspace is the kernel of evaluation and derivative at \(z=1\) inside \(P_0\), so its projection is \(P=P_0-Q\). In mode coordinates \(j=0,\ldots,N\), the rank-two projection \(Q\) has orthonormal vectors proportional to \(1\) and \(j-N/2\). The chosen root itself is then included as one additional deterministic point.

Use the negative cosine and sine band sums \(-\sum_{aN<k\le bN}k^{-1}\sum_{\lambda}\cos(k\arg\lambda)\) and its sine counterpart, over the free points and the root. They are the real and an imaginary Fourier-band component of the usual logarithm of the characteristic polynomial, up to the angle/sign convention that does not affect these comparisons. Let \(S_k\) denote the unitary shift on all integer mode coordinates, and \(C_k=(S_k+S_{-k})/2,\ B_k=(S_k-S_{-k})/(2i)\). The free point mean of a test \(A\) is \(\operatorname{Tr}(PA)\). For \(k>0\), \(\operatorname{Tr}(P_0 S_k)=0\); the deterministic root contributes one to the unnegated cosine trace. Write \(x=k/N\). By a Riemann sum the shift trace of \(Q\) approaches
\[
 A(x)=1-x+12\int_0^{1-x}(t-\tfrac12)(t+x-\tfrac12)\,dt
      =2-4x+2x^3
 \qquad(0\le x\le1).
\]
So the negative cosine mean per mode tends to \(A(x)-1=F(x)\), and summing \(1/k\) across the band yields the arithmetic mean. The sine mean vanishes by reflection.

For any two real multiplication tests \(A,B\), the projection determinantal first two correlation functions give the covariance
\(\operatorname{Tr}(PAB)-\operatorname{Tr}(PAPB)\). This follows by integrating the one-point density \(P(z,z)\) and the off-diagonal term \(-|P(z,w)|^2\) of the two-point covariance. The difference compared with \(P_0\) is
\[
 -\operatorname{Tr}(QAB)+\operatorname{Tr}(QAP_0B)+
 \operatorname{Tr}(QBP_0A)-\operatorname{Tr}(QAQB).
 \tag{*}
\]
For \(P_0\) the cosine and sine frequency covariances are both diagonal, \(k/2\) at \(k\) in the band. Indeed in \(\operatorname{Tr}(P_0A(1-P_0)B)\) a shift must be followed by its inverse to contribute to the trace, and the \(k\) modes at each edge each have squared shift coefficient \(1/4\). The base band variance converges to \(\frac12\log(b/a)\).

For completeness, the rank-two correction in (*) can be computed with the continuum normalized mode vectors \(\phi_0(t)=1\) and \(\phi_1(t)=\sqrt{12}(t-1/2)\) on \([0,1]\), extended by zero outside. Put \(x=k/N\), \(y=l/N\) and first take \(x\ge y\). The \(QAB\) trace for cosine is \(\{A(x+y)+A(x-y)\}/2\); for sine it is \(\{A(x-y)-A(x+y)\}/2\). These follow by multiplying shifts, with \(x+y<1\). To evaluate the middle two traces, apply the sum or difference of the \(+x,-x\) shifts and of the \(+y,-y\) shifts to each \(\phi_i\), and take their overlap on \([0,1]\). Both traces have the same value, with the sine factors taken with conjugation as inner products. On the left they split at \(0,y,x\), and the central interval is \([x,1-x]\). The right intervals are the reflections. Let \(l(t)=t-1/2\) and \(E=\frac14\int_0^y l(t+x)l(t+y)\,dt\). The constant and linear overlap contributions are
\[
\begin{array}{c|cc}
 & \phi_0 & \phi_1\\ \hline
 \cos & 2(y/4+(x-y)/2)+1-2x
 &12\left[2E+\int_y^x l(t+x)l(t)\,dt+\int_x^{1-x} l(t)^2\,dt\right]\\
 \sin & y/2
 &12\left[2E+y\int_y^x l(t+x)\,dt+(1-2x)xy\right].
\end{array}
\]
Finally \(QC_xQ\) is diagonal in the constant and linear basis by reflection, with entries \(1-x,1-3x+2x^3\). For \(QB_xQ\) the diagonal vanishes by reflection and the off-diagonal entries are conjugates with magnitude \(\sqrt{12}\,x(1-x)/2\) and a common imaginary sign for \(x>0\). Thus the last trace in (*) is respectively \((1-x)(1-y)+(1-3x+2x^3)(1-3y+2y^3)\) and \(6xy(1-x)(1-y)\). Substituting into (*) gives \(C_c(x,y)\) and \(C_s(x,y)\) exactly. All continuum formulas here follow from uniform Riemann sums in mode coordinates: the summands are polynomials on finitely many shift-defined intervals, and their degrees and coefficients are bounded on the fixed band. Diagonal correction terms have bounded size and contribute \(O(\sum_{k>aN}k^{-2})=o(1)\). Off-diagonal sums with weights \(1/(kl)\) give the same double integrals as for primes, now by ordinary Riemann sums. Reflection also yields zero mixed covariance. This verifies the mean and variance match in the rooted CUE model directly; the calculation does not assert Gaussianity of these high-band statistics. [Exact verification of both rank-two simplifications](../../scripts/prime71_hlz_band_variance_check.py)
