# Full law of a Fourier band in derivative-square rooted CUE

18 November 2026. Fix \(0<a<b<\infty\). This statement is entirely within the circular unitary ensemble. Give a pair \((U,j)\), with Haar \(U\in U(N)\) and a selected eigenvalue index \(j\), probability proportional to \(|Z_U'(\theta_j)|^2\) against Haar measure times counting measure. Rotate the chosen eigenvalue to \(1\), write the resulting angles as \(\vartheta_\ell\), and include the chosen root itself among the \(N\) angles. Define
\[
 X_N=-\sum_{aN<k\le bN}\frac1k\sum_{\ell=1}^N\cos(k\vartheta_\ell).
\]
Then \(X_N\) converges in distribution, and all its fixed moments converge. The law below gives a precise comparison candidate for polynomial prime bands in the range of the existing arithmetic moment calculations. No identification of the full arithmetic band law is asserted. [Finite tilted density and first two arithmetic moments](prime71_hlz_band_covariance.md)

## The law

Set
\[
 f(u)=-\int_a^b\frac{\cos(2\pi x u)}{x}\,dx,\qquad
 e_0(u)=\int_0^1 e^{2\pi isu}\,ds,\qquad
 e_1(u)=\sqrt{12}\int_0^1(s-\tfrac12)e^{2\pi isu}\,ds.
\]
Let \(\mathcal X\) be the determinantal process on \(\mathbb R\) with kernel
\[
 K(u,v)=\int_0^1 e^{2\pi is(u-v)}\,ds
         -e_0(u)\overline{e_0(v)}-e_1(u)\overline{e_1(v)} .
\]
With \(d(u)=|e_0(u)|^2+|e_1(u)|^2\), its intensity is \(K(u,u)=1-d(u)\). Define
\[
 S=\lim_{R\to\infty}^{L^2}
 \left(\sum_{u\in\mathcal X\cap[-R,R]} f(u)
          -\int_{-R}^R f(u)K(u,u)\,du\right),
 \qquad \mu=f(0)-\int_{\mathbb R} f(u)d(u)\,du .
 \tag{1}
\]
The full limiting law is \(\mu+S\). For \(b\le1\) the mean simplifies to
\[
 \mu=\log(b/a)-4(b-a)+\tfrac23(b^3-a^3).
\]
For arbitrary finite \(b\) it is \(\int_a^b(A(x)-1)\,dx/x\), where \(A(x)=2-4x+2x^3\) on \(0\le x\le1\) and vanishes for \(x>1\).

Write \(P\) for the orthogonal projection with kernel \(K\), \(M_g\) for multiplication by \(g\), and \(\det_2\) for the Hilbert–Schmidt regularized determinant. The characteristic function of the full law, for real \(t\), is
\[
 e^{it\mu}\det\nolimits_2(I+P M_{e^{itf}-1}P)
 \exp\left\{\int_{\mathbb R}
       (e^{it f(u)}-1-it f(u))K(u,u)\,du\right\}.                  \tag{2}
\]
The determinant can be taken on \({\rm Ran}(P)\), or on all of \(L^2(\mathbb R)\) with identity on its complement. The integrated correction converges absolutely.

## From the tilted density to the limiting process

The tilt is global. It weights the matrix marginal as well as the selected root. It differs from drawing a Haar matrix first and normalizing the root weights inside that fixed matrix. The Haar Vandermonde squared has one factor \(|1-e^{i\vartheta_\ell}|^2\) for each remaining eigenvalue after rotating the selected root to 1. The weight \(|Z_U'(\theta_j)|^2\) supplies a second such factor. Thus the \(N-1\) free angles have joint density proportional to the Vandermonde squared of their eigenvalues times \(\prod_\ell |1-e^{i\vartheta_\ell}|^4\), and the distinguished point is deterministic. This is the finite density in Hughes–Keating–O’Connell §2(a), equations (2.2)–(2.7), with derivative moment parameter 1. It is also the circular Jacobi density with \(\beta=2,\delta=2\) in Bourgade–Nikeghbali–Rouault (1.6), with \(N-1\) free points. [Hughes–Keating–O’Connell](../../sources/analytic64_prime_phase_clt_priority/hko.pdf) · [Bourgade–Nikeghbali–Rouault](../../sources/prime77_rmt/bourgade_nikeghbali_rouault_2009.pdf)

The free angles form the orthogonal-projection process onto \((z-1)^2\) times polynomials of degree at most \(N-2\) in \(L^2(d\theta/(2\pi))\). This follows by multiplying each row of the Vandermonde determinant by \((z-1)^2\) and orthonormalizing the columns. Inside the mode space spanned by \(1,z,\ldots,z^N\), the subspace consists of polynomials with value and first derivative zero at 1. Its orthogonal complement is spanned in coefficient coordinates by the vector whose entries are 1 and the vector whose entries are \(j-N/2\), \(j=0,\ldots,N\).

Use the representative \(\vartheta\in[-\pi,\pi)\) and scale \(u=N\vartheta/(2\pi)\) to the interval \(I_N=[-N/2,N/2)\). With Lebesgue measure in this coordinate, the unchanged mode kernel is
\[
 E_N(u,v)=\frac1N\sum_{j=0}^N e^{2\pi i j(u-v)/N}.
\]
The two normalized removed functions are
\[
 e_{0,N}(u)=\frac1{\sqrt{N(N+1)}}\sum_{j=0}^N e^{2\pi i j u/N},
 \qquad
 e_{1,N}(u)=\frac{\sum_{j=0}^N(j-N/2)e^{2\pi i j u/N}}
                    {\sqrt{N\sum_{j=0}^N(j-N/2)^2}} .
\]
The exact scaled kernel is \(K_N=E_N-\sum_{\nu=0}^1 e_{\nu,N}\otimes e_{\nu,N}^*\). These expressions converge uniformly on compact rectangles to the functions in \(K\), by Riemann sums. Also \(0\le K_N(u,u)\le (N+1)/N\le2\) and \(\int_{I_N}\sum_\nu |e_{\nu,N}|^2=2\).

In the limiting Fourier representation with inverse transform \(g\mapsto\int g(s)e^{2\pi i su}\,ds\), \(K\) is the projection onto the transforms of \(L^2[0,1]\) orthogonal to \(1,\sqrt{12}(s-\tfrac12)\) in that frequency space. It is locally trace class because the Fourier extension map from \(L^2[0,1]\) into \(L^2(B)\) is Hilbert–Schmidt for every bounded \(B\), and compression of \(K\) is a product of such maps. The positive-contraction existence theorem for determinantal processes therefore applies. This is also the coalescent limit of the reduced two-point Palm sine process at distinct points \(0,h\) as \(h\to0\), in the gauge using frequencies \([0,1]\). For distinct roots the Palm kernel is the removed projection onto the complement of the two evaluation vectors, by the Schur complement of the two-point Gram block in the correlation determinant. In frequency space these vectors span \(1,e^{-2\pi ish}\), and subtracting their constant projection and dividing by the nonzero \(h\) gives a limit proportional to \(s-\tfrac12\). This limit is a well-defined collision procedure, rather than conditioning on an event of two exactly coincident points. [Soshnikov, Theorem 3 and local determinant formula](../../sources/sine_gram_round3/soshnikov2000.pdf) · [Bufetov, §2.6 for the projection Palm formula and Theorem 1 for the broader hierarchy](../../sources/prime77_rmt/bufetov_2401.00518.pdf)

## Centered tails and the uncentered mean

In the scaled coordinates,
\[
 f_N(u)=-\sum_{aN<k\le bN}\frac{\cos(2\pi k u/N)}{k},
 \qquad X_N=f_N(0)+\sum_{u\ {\rm free}} f_N(u).
\]
Uniformly on fixed compact sets \(f_N\to f\) by Riemann sums. The crude bound is \(|f_N(u)|\le C_{a,b}\). For \(0<|u|\le N/2\) the partial sums of \(e^{2\pi i k u/N}\) are \(O(1/|\sin(\pi u/N)|)\). Summation by parts against the decreasing \(1/k\) bounds the whole sum by \(C_{a,b}/(N|\sin(\pi u/N)|)\le C_{a,b}/|u|\). The continuum bound is the same by integrating \(f\) by parts in \(x\). In particular \(f\in L^2(\mathbb R)\), and
\[
 |f_N(u)|+|f(u)|\ll_{a,b}\min(1,|u|^{-1})
 \quad\hbox{on }I_N.
 \tag{3}
\]

For a real bounded compactly supported test \(h\), a projection process satisfies
\[
 \operatorname{Var}\left(\sum h\right)
 =\int h(u)^2K(u,u)\,du
    -\operatorname{Tr}\big((P M_h P)^2\big)
 \le \int h(u)^2K(u,u)\,du .
\]
This follows from the one- and two-point densities, and the trace being subtracted is nonnegative even when \(h\) changes sign. It holds with \(K_N\) on \(I_N\) as well. Applying it to differences of interval truncations of \(f\) proves the \(L^2\) limit in (1), with squared tail error \(O_{a,b}(1/R)\) by (3). The variance of the centered finite-\(N\) part outside \([-R,R]\) is likewise \(O_{a,b}(1/R)\), uniformly in \(N\).

Fix \(R\). The law of the finite-\(N\) statistic truncated to \([-R,R]\) converges to the corresponding limit-process statistic. For example expand its characteristic function in the correlation series using \(e^{itf_N}-1\) on \([-R,R]\). The local kernels and the tests converge uniformly, and Hadamard's determinant bound controls an \(m\)-point term by a constant to the \(m\)-th power divided by \(m!\) after integration. This proves convergence for each \(t\) without a trace-norm kernel assumption. The local means also converge. Comparing the centered full characteristic functions to the centered truncations costs \(O_{a,b}(|t|/\sqrt R)\) on both sides. Taking \(N\to\infty\) first and then \(R\to\infty\), followed by Lévy continuity, proves \(X_N-E X_N\Rightarrow S\).

The constant-intensity term of the exact free-point mean is zero, since \(\int_{I_N} f_N(u)\,du=0\) by Fourier orthogonality. Thus
\[
 E X_N=f_N(0)-\int_{I_N} f_N(u)
                \big(|e_{0,N}(u)|^2+|e_{1,N}(u)|^2\big)\,du
   \longrightarrow \mu .
\]
Compact convergence suffices for the integral on \([-R,R]\), and the integral outside has modulus at most \(C/R\) by (3) and the removed mass 2. The same estimates apply in the limit by Fourier Plancherel. The formula for \(\mu\) follows from the autocorrelations \(1-x\) and \(12\int_0^{1-x}(s-\tfrac12)(s+x-\tfrac12)\,ds\) of the two frequency functions at \(0\le x\le1\), zero for \(x>1\). This gives \(A(x)\) and the asserted polynomial mean. The symmetric uncentered truncations also converge in \(L^2\) after adding the root, because
\[
 \int_{-R}^R f(u)\,du=-\frac1\pi\int_a^b\frac{\sin(2\pi Rx)}{x^2}\,dx
 \longrightarrow 0
\]
and the removed-intensity mean converges absolutely. The theorem uses the compensated statistic or this symmetric convention, and does not need absolute convergence of the original point sum.

## Determinant and moment convergence

Put \(g_t=e^{itf}-1\), \(g_{t,R}=g_t\mathbf1_{[-R,R]}\). For the compact truncation the multiplicative functional gives the determinant of \(I+P M_{g_{t,R}}P\) on \({\rm Ran}(P)\). Equivalently use the standard Fredholm determinant on \([-R,R]\) and the cyclic \(AB,BA\) identity. The compact operator is trace class since it factors using \(M_{\sqrt{|g_{t,R}|}}P\) and its adjoint, which are Hilbert–Schmidt. Its trace is \(\int g_{t,R}K(u,u)\,du\). After subtracting the mean the characteristic function is therefore its \(\det_2\) times
\[
 \exp\left\{\int_{-R}^R (g_t(u)-itf(u))K(u,u)\,du\right\}.
\]
Since \(P\) is a projection, \(\int |K(u,v)|^2\,dv=K(u,u)\). It follows that
\[
 \|P M_{g_t-g_{t,R}}P\|_{\rm HS}
 \le\|M_{g_t-g_{t,R}}P\|_{\rm HS}
 \le |t|\left(\int_{|u|>R} f(u)^2 K(u,u)\,du\right)^{1/2}\to0.
\]
The regularized determinant is continuous in Hilbert–Schmidt norm, and \(|g_t-itf|\le t^2 f^2/2\) supplies absolute convergence of the trace correction. Passing to the limit gives (2).

For real \(t\), use instead \(g=e^{t f_N}-1\) on the finite system and center. On the projection range \(I+P_N M_g P_N=P_N M_{e^{t f_N}}P_N\) is strictly positive, so the eigenvalue inequality \(\log(1+\lambda)\le\lambda\) gives
\[
 E e^{t(X_N-E X_N)}
 \le \exp\left\{\int_{I_N}(e^{t f_N(u)}-1-t f_N(u))K_N(u,u)\,du\right\}
 \le \exp(C_{t,a,b}).
\]
The last inequality uses bounded \(\|f_N\|_\infty\) and uniformly bounded \(\int f_N^2 K_N(u,u)\,du\) from (3). Apply this for both \(t\) and \(-t\). It gives uniform integrability of all fixed absolute powers, proving moment convergence in addition to the weak convergence. The same localization proof also treats finite real linear combinations of cosine and sine bands bounded away from frequency zero, with zero contribution from the chosen root for sine. The RMT proof imposes no \(b<1/6\) restriction. Cutoffs in the arithmetic proof arise from the length of the Dirichlet polynomials and remain separate. Publication priority for the band statistic itself is unassessed.
