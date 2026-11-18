# The rooted derivative-square CUE band limit

18 November 2026. Fix a band \(0<a<b<\infty\). Select a Haar \(U(N)\) and an eigenangle label under the joint probability tilted by the squared derivative of the characteristic polynomial at that eigenangle. Rotate the selected eigenangle to zero and include it in
\[
 X_N=-\sum_{aN<k\le bN}\frac1k
              \sum_{j=1}^N\cos\bigl(k(\theta_j-\theta_{\rm root})\bigr).
\]
Write \(f(u)=-\int_a^b\cos(2\pi xu)\,dx/x\). The centered \(X_N-\mathbb EX_N\) converges in law to the centered linear statistic \(S(f)\) of the point process with projection
\[
 K=E_\infty-Q_\infty,\qquad
 E_\infty(u,v)=\int_0^1 e^{2\pi is(u-v)}\,ds,\quad
 Q_\infty(u,v)=e_0(u)\overline{e_0(v)}+e_1(u)\overline{e_1(v)},
\]
where \(e_0(u)=\int_0^1e^{2\pi isu}ds\) and \(e_1(u)=\sqrt{12}\int_0^1(s-\tfrac12)e^{2\pi isu}ds\). The definition is the \(L^2\) limit of centered bounded-window statistics. The raw \(X_N\) converges to \(S(f)+m_{a,b}\), with
\[
 m_{a,b}= f(0)-\int_{\mathbb R} f(u)\bigl(|e_0(u)|^2+|e_1(u)|^2\bigr)\,du.
\]
The same proof gives joint convergence for any fixed list of such bands. This is a random-matrix law, independent of RH and of an arithmetic full-law transfer. [Finite rooted law and moment comparison](weighted73_rooted_cue_band_match.md)

## Kernel and local convergence

After rotation, the remaining \(N-1\) angles have density proportional to \(\prod_{i<j}|z_i-z_j|^2\prod_i|1-z_i|^4\) against Haar on the circle. The law uses a joint Haar-label tilt, since normalizing the derivative-square weights separately within each matrix would change this density. The \(N-1\) functions \((1-z)^2z^j\), \(0\le j\le N-2\), span the subspace of Fourier polynomials of degrees \(0,\ldots,N\) that vanish to order two at 1. Their determinant is the deformed Vandermonde. Thus the rotated other points form the projection DPP \(P_N=E_N-Q_N\), where \(E_N\) is the degree \(0,\ldots,N\) projection and the two \(Q_N\) coefficient vectors are
\[
 u_{0,N}(j)=(N+1)^{-1/2},\qquad
 u_{1,N}(j)=(j-N/2)\{N(N+1)(N+2)/12\}^{-1/2}.
\]

Identify the angles with \(u=N\theta/(2\pi)\) on \(J_N=[-N/2,N/2)\) and extend the kernels by zero off this interval. Because \(d\theta/(2\pi)=du/N\), the rescaled Fourier functions are \(N^{-1/2}e^{2\pi iju/N}1_{J_N}(u)\). Therefore
\[
 E_N^{\rm loc}(u,v)=\frac1N\sum_{j=0}^N e^{2\pi ij(u-v)/N},\qquad
 e_{r,N}^{\rm loc}(u)=\frac1{\sqrt N}\sum_{j=0}^N
                         u_{r,N}(j)e^{2\pi iju/N}\quad(r=0,1)
\]
on \(J_N\). Riemann sums are uniform on any fixed compact window. Consequently \(P_N^{\rm loc}\to K\) locally uniformly as kernels. On all of \(J_N\), \(0\le P_N^{\rm loc}(u,u)\le1+1/N\), and \(0\le K(u,u)\le1\). The removed local finite vectors are orthonormal on \(J_N\) in \(du\), and \(e_0,e_1\) are orthonormal by Plancherel. The projection \(E_\infty\) is Fourier multiplication by \(1_{[0,1]}\). Thus \(K\) is an orthogonal projection. Compact compressions are trace class, since \(1_JE_\infty\) is Hilbert–Schmidt for each bounded interval \(J\), and \(Q_\infty\) is finite rank.

On any such \(J\), uniform kernel convergence gives Hilbert–Schmidt convergence and the diagonal integrals give trace convergence of the positive compressions. These imply trace-norm convergence. To see it, choose a finite-rank projection capturing all but a prescribed small trace of the limiting positive compression. Its diagonal block converges in trace norm by finite rank, and the complementary block traces converge by subtracting that trace from the full trace. The off-diagonal blocks have trace norms at most the square root of the product of their two diagonal traces, by Hilbert–Schmidt factorization using positive square roots. Let the chosen trace tail tend to zero. No global trace-norm assertion is used. In particular compactly supported bounded multipliers have convergent determinantal characteristic functions, including multiplication by indicators of closed windows. Equivalently one can use the finite-window Fredholm series and the uniform diagonal bound to dominate its coefficient integrals.

## Test functions and \(L^2\) tail control

Set
\[
 f_N(u)=-\sum_{aN<k\le bN}\frac{\cos(2\pi k u/N)}{k},\qquad u\in J_N.
\]
It converges uniformly to \(f\) on each compact interval and is uniformly bounded by a constant depending on \(a,b\). For \(0<|u|\le N/2\), the geometric partial sums of \(e^{2\pi iku/N}\) have absolute value at most \(1/|\sin(\pi u/N)|\). Abel summation against the decreasing weights \(1/k\) gives \(C/(aN|\sin(\pi u/N)|)\ll_a 1/|u|\). Integration by parts gives the same decay for \(f\). In particular both functions are bounded by \(C_{a,b}\min(1,1/|u|)\) on their domains. The lower band endpoint must be strictly positive.

For any real bounded compactly supported \(h\) and a projection DPP with projection \(P\), the first two intensities yield
\[
 \operatorname{Var}\left(\sum h\right)
  =\operatorname{Tr}(P M_{h^2}P)-\operatorname{Tr}((P M_hP)^2)
  \le\int h(u)^2P(u,u)\,du .
\]
The square on the right of the equality is a self-adjoint operator square, so its trace is nonnegative even if \(h\) changes sign. This handles finite \(N\) on the entire bounded interval, and the continuum on any bounded annulus. Hence the centered finite-\(N\) statistic minus its centered radius-\(R\) truncation has \(L^2\) norm \(O_{a,b}(R^{-1/2})\), uniformly in \(N\). Similarly centered continuum truncations \(S_R\) form an \(L^2\)-Cauchy family, with \(\|S(f)-S_R\|_2=O_{a,b}(R^{-1/2})\). For fixed \(R\), local convergence holds for \(f_N1_{[-R,R]}\) since both the kernels and the multipliers converge there and the expectations converge by the diagonal formulas. Testing with bounded Lipschitz functions, let \(N\) tend to infinity at fixed \(R\) and then let \(R\) tend to infinity. This proves the full centered convergence, with the root automatically disappearing under centering. The same uniform bounds apply to a fixed linear combination of bands, giving joint convergence by Cramér–Wold.

The absolute sum of the continuum test values actually diverges almost surely. Indeed
\[
 f(u)=\frac{a^{-1}\sin(2\pi a u)-b^{-1}\sin(2\pi b u)}{2\pi u}+O_{a,b}(|u|^{-2}).
\]
The bounded numerator has a strictly positive limiting mean square on \([R,2R]\), since \(a\ne b\), and hence its mean absolute value there is bounded below. Thus \(\int|f|\,du=\infty\). Removing the rank-two diagonal changes the absolute intensity integral by at most \(2\|f\|_\infty\), so the expectations of the growing positive absolute sums diverge. Their variances are uniformly bounded by \(\int f^2K(u,u)du\). Chebyshev's inequality gives divergence in probability, and the sums are monotone, so divergence is almost sure. No unordered absolutely convergent raw point sum represents the law.

## Mean and regularized characteristic function

The finite-\(N\) mean from \(E_N^{\rm loc}\) vanishes. Its constant diagonal multiplies \(\int_{J_N}f_N=0\), by the exact integral of the nonzero integer modes. The finite root contributes \(f_N(0)\to f(0)=-\log(b/a)\). For the removed part \(Q_N^{\rm loc}\), the diagonal integral is exactly 2. Local convergence plus \(\sup_{|u|>R}|f_N(u)|\ll R^{-1}\) therefore gives convergence of the means to \(m_{a,b}\). In the continuum a symmetric truncation satisfies
\[
 \int_{-R}^R f(u)\,du=-\frac1\pi\int_a^b\frac{\sin(2\pi Rx)}{x^2}\,dx\to0,
\]
by integration by parts or Riemann–Lebesgue. Thus the rooted raw statistic also equals the \(L^2\) limit using symmetric truncation and no explicit compensations, with this convention for the mean. No such assertion is made for arbitrary summation of the point values.

By Plancherel,
\[
 m_{a,b}=\int_a^b\frac{-1+
      1_{\{x<1\}}(2-4x+2x^3)}{x}\,dx .
\]
In fact the Fourier transform of the removed diagonal on \(0\le x<1\) is the sum of autocorrelations of \(1\) and \(\sqrt{12}(s-1/2)\) on \([0,1]\), namely \(2-4x+2x^3\), and is zero on \(x\ge1\). This matches the earlier low-band mean \(F(x)=1-4x+2x^3\) including the deterministic root.

For real \(t\) work on the Hilbert space \(\mathcal H=\operatorname{Ran}K\), and set
\[
 A_t=K M_{e^{itf}-1}K|_{\mathcal H},\qquad
 B_t=K M_{e^{itf}-1-itf}K|_{\mathcal H}.
\]
The \(A_t\) are Hilbert–Schmidt since \(\|M_g K\|_2^2=\int |g|^2K(u,u)\,du\), and \(|e^{itf}-1|\le |t f|\). The identity for the Hilbert–Schmidt norm follows from the projection kernel identity \(\int |K(u,v)|^2dv=K(u,u)\), or from expanding in an orthonormal basis of the range. The \(B_t\) are trace class by the factorization through \(|e^{itf}-1-itf|^{1/2}\) and the bound \(|e^{itf}-1-itf|\le t^2 f^2/2\). Their trace is the integral of that multiplier, with its complex sign, against \(K(u,u)\,du\). Compact truncation \(f_R=f1_{[-R,R]}\) gives \(A_{t,R}\to A_t\) in Hilbert–Schmidt norm and \(B_{t,R}\to B_t\) in trace norm by those same estimates on the tails. For compact support one has the ordinary determinantal formula. Passing to regularized determinants there and then taking \(R\to\infty\) gives
\[
 \mathbb E e^{itS(f)}
    =\det\nolimits_2(I_{\mathcal H}+A_t)
       \exp\left\{\int_{\mathbb R}
             (e^{itf(u)}-1-itf(u))K(u,u)\,du\right\}.
\]
Indeed \(\det(I+A_{t,R})=\det_2(I+A_{t,R})e^{\operatorname{Tr}A_{t,R}}\), and centering subtracts \(it\int f_R K(u,u)du\). The Hilbert–Schmidt continuity of \(\det_2\) and the \(L^2\) limit justify passage to the limit. For the raw rooted limiting law multiply this formula by \(e^{it m_{a,b}}\). The trace term is essential and converges absolutely. An ordinary global Fredholm determinant of \(I+A_t\) has no trace-class justification from these hypotheses.

## Primary lineage

- The finite Haar-derivative joint tilt comes from Hughes–Keating–O'Connell, Proc. Roy. Soc. Lond. A 456 (2000), Theorem 1.2 and (2.2)–(2.9). The density for the other \(N-1\) points is the circular Jacobi unitary ensemble with exponent parameter \(s=2\) in \(|1-z|^{2s}\). The general circular Jacobi density is (1.6) in Bourgade–Nikeghbali–Rouault's IMRN paper, and their separate *Ewens measures on compact groups and hypergeometric kernels*, Theorem 5, gives the general local kernel limit. Here the integer parameter permits the elementary two-dimensional projection computation above. [HKO paper](../../sources/classical63_lfunctions/hko2000.pdf) · [Circular Jacobi density](https://arxiv.org/pdf/0804.4512) · [General local kernel result](https://cims.nyu.edu/~bourgade/papers/SemProb.pdf)
- At distinct \(0,h\), the reduced double-Palm DPP of the sine projection removes the span of \(E_\infty(\cdot,0)\) and \(E_\infty(\cdot,h)\). The finite circle version follows from conditioning at distinct roots and its Vandermonde. The general reduced-Palm projection theorem is attributed to Shirai–Takahashi, with the projection form reproduced as Bufetov arXiv:1409.2068, Proposition 2.16. As \(h\to0\), the difference quotient of the two representers converges in \(L^2\) by their Fourier representation. After the first projection is removed, only the centered frequency \(s-\tfrac12\) remains. The rank-two projections thus converge in operator norm, giving precisely \(K\). This is the confluent reduced double Palm, with both conditioned points removed. The present statistic re-inserts one deterministic root only. [Reduced Palm projection formula](https://arxiv.org/pdf/1409.2068)
- Bufetov's arXiv:2401.00518, Theorem 1, describes the Palm hierarchy for the confluent hypergeometric family using the Cayley coordinate at infinity. Gorbunov arXiv:2504.09732 §1.3 explicitly describes positive integer \(s\) as the corresponding repeated sine Palm, and Theorem 2.1 restates the microscopic circular Jacobi limit with its kernel gauge convention. Those results already supply the point-process lineage. The calculation here gives the centered localized-frequency statistic, the necessary nonabsolute summation convention, its mean including the root, and a regularized characteristic function. No priority assertion is made. [Palm hierarchy](https://arxiv.org/pdf/2401.00518) · [Kernel and Palm description](https://arxiv.org/pdf/2504.09732)
