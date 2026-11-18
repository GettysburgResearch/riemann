# Inverse data from the factorial-target error forms

17 November 2026. The proposed normalization and cross-form reconstruction hold. In fact all singleton limits already determine the actual simple-zero measure, because it is purely atomic. On arbitrary finite symmetric positive measures the singleton limits determine the atoms and cross forms also recover the diffuse part. This is a conditional consequence of the stated prime-array limit under RH, together with classical Fourier arguments. No publication-priority claim is made. [Prime-array proponent proof](jump_factorial_prime_array63_proponent.md) · [Independent prime-array proof](generator63_tapered_prime_array_skeptic.md)

## The quadratic form and its normalization

The factorial target satisfies \(MR_k(s)=-[\zeta(s)(k^{1-s}-1)]'/s\). At a simple zero \(\rho=1/2+i\gamma\), its value is \(-\zeta'(\rho)(k^{1-\rho}-1)/\rho\). At a multiple zero it vanishes. For a fixed finite combination \(\sum_k c_kR_k\), replace the analytic factor \(k^{1-s}-1\) by \(\sum_k c_k(k^{1-s}-1)\) and its prime-array coefficients by the same linear combination. The taper and anchoring are linear. The source's residue bounds and summable local tail extend by a finite sum of the fixed-\(k\) bounds. The local constant at a simple zero is the same squared modulus for the combined factor. Alternatively, the fixed finite zero profiles for each residual can be combined before taking their common scaled Gram limit. For the optimal approximation form the same upper construction and the linear compact-jet lower tests apply to the combined target. This uses fixed finite combinations and a fixed asymptotic \(N\to\infty\) for each combination. [Prime-array error and local model](generator63_tapered_prime_array_skeptic.md)

Write

\[
 \nu=\sum_{\substack{\rho=1/2+i\gamma\\\rho\,\mathrm{simple}}}
       \frac{|\zeta'(\rho)|^2}{|\rho|^2}\delta_\gamma,
 \qquad F(t)=\int e^{-it\gamma}\,d\nu(\gamma),
 \qquad B=F(0),\qquad a_k(\gamma)=\sqrt{k}\, e^{-i\gamma\log k}-1.
\]

Both ordinate signs are included once. Conjugacy makes \(\nu\) symmetric. The fixed-strip convexity and Cauchy estimate used in the prime-array proof gives \(|\zeta'(1/2+i\gamma)|\ll (2+|\gamma|)^{3/8}\). Together with the unit-window count this bounds the sum of weights by a convergent sum of \(O(j^{-5/4}\log(2+j))\), so \(\nu\) is finite. The limiting quadratic form in the source's \(dt/(2\pi)\) norm is consequently

\[
 Q\Bigl(\sum c_kR_k\Bigr)=\int\Bigl|\sum c_ka_k\Bigr|^2d\nu.
\]

No further factor of two or \(2\pi\) enters. Symmetry gives real even \(F\) and real Gram entries \(G_{kl}=\int a_k\overline{a_l}\,d\nu\). Thus, with \(C_k=Q(R_k)\),

\[
 C_k=(k+1)B-2\sqrt{k}F(\log k),\qquad B=\lim_{k\to\infty}\frac{C_k}{k}.
\]

The limit uses \(|F|\le B\). It is a limit over target indices of the already obtained limiting constants, with no asserted uniformity in the original approximation length. One also has the finite mass bounds

\[
 \frac{C_k}{(\sqrt{k}+1)^2}\le B\le\frac{C_k}{(\sqrt{k}-1)^2},\qquad k\ge2.
\]

In particular an exactly zero singleton form implies \(\nu=0\) in the positive model class. For nonzero \(\nu\), every singleton form is positive.

The Gram identity and the simpler difference identity are

\[
 \begin{aligned}
 G_{kl}&=\sqrt{kl}F(\log(k/l))-\sqrt{k}F(\log k)-\sqrt{l}F(\log l)+B,\\
 Q(R_k-R_l)&=(k+l)B-2\sqrt{kl}F(\log(k/l)).
 \end{aligned}
\]

Real polarization gives \(G_{kl}=[Q(R_k+R_l)-Q(R_k-R_l)]/4\), since symmetry makes its imaginary part zero. The difference data alone would also recover \(B\) from \(Q(R_k-R_l)/k\) with \(l\ge2\) fixed and \(k\to\infty\). Since the ratios with \(k,l\ge2\) are all positive rationals, continuity recovers \(F\) on \(\mathbb R\). Fourier uniqueness follows, for example, by convolving the difference of two measures with a Gaussian. Fourier inversion and Fubini give zero for every such convolution, and passage through the Gaussian approximate identity gives equality of the measures.

## Singleton measurements already recover the atomic part

For every finite measure and every fixed real \(x\), direct dominated convergence gives the atomic inversion identity

\[
 \nu\{x\}=\lim_{L\to\infty}\frac1L\int_0^L F(t)e^{itx}\,dt.
\]

Indeed the averaging kernel is bounded by 1, tends to zero at every ordinate different from \(x\), and equals 1 at \(x\). The function \(t\mapsto F(t)e^{itx}\) is uniformly continuous, since the Fourier transform of a finite measure is uniformly continuous by dominated convergence in the translation difference. The intervals with endpoints \(\log k,\log(k+1)\) have lengths tending to zero. The total length of any fixed initial segment contributes \(o(1)\) after division by \(\log(K+1)\). Uniform continuity controls all subsequent Riemann-sum errors uniformly in their positions. Hence the singleton data yield the explicit formula

\[
 \nu\{x\}=\lim_{K\to\infty}\frac{1}{\log(K+1)}
  \sum_{k=1}^K \log(1+1/k) F(\log k)e^{ix\log k},
 \qquad F(\log k)=\frac{(k+1)B-C_k}{2\sqrt k},
\]

where \(F(\log1)=B\). At each nonzero atom this recovers a simple-zero ordinate and then \(|\zeta'(1/2+i x)|^2=(1/4+x^2)\nu\{x\}\). The reconstruction gives derivative magnitudes. Multiple-zero ordinates do not contribute to these limiting forms. The earlier prefix inversion recovers instead the total \(1/|\rho|^2\) weights by multiplicity class. [Prefix-germ comparison](director_prefix_inverse_round8.md)

For an arbitrary finite symmetric positive measure, the diagonal data alone can miss a diffuse component. Choose a nonzero smooth, compactly supported real even frequency function \(H\) supported in \(0<a<|t|<b<\log2\). Its inverse Fourier transform \(g\) is real even and Schwartz. Since \(H(0)=0\), \(g\) has zero integral. The measures \(g_+(x)dx\) and \(g_-(x)dx\) are distinct positive symmetric measures with equal mass and equal \(F(\log k)\) for every \(k\). Their singleton limits coincide. Cross-form inversion recovers the whole measure in this situation.

## Complex measurements and asymmetric competitors

For a finite positive measure without symmetry, \(F(-t)=\overline{F(t)}\). Real combinations of the targets still see only its reflected symmetrization. With a linear-first inner product, complex polarization adds

\[
 \Im G_{kl}=\frac{Q(R_k+iR_l)-Q(R_k-iR_l)}4 .
\]

The general Gram identity replaces the second linear term \(F(\log l)\) in the first line above by \(F(-\log l)\). The imaginary parts at \(\log k\) are not supplied by diagonal forms. Instead, use simultaneous scaling. For fixed \(k,l\ge2\),

\[
 \frac{G_{mk,ml}}{m\sqrt{kl}}
 = F(\log(k/l))-
 \frac{F(\log(mk))}{\sqrt{ml}}-
 \frac{F(-\log(ml))}{\sqrt{mk}}+
 \frac{B}{m\sqrt{kl}}.
\]

The last three terms tend to zero by boundedness. This recovers the full complex Fourier sample from the exact complex forms, and continuity and uniqueness finish the general positive-measure reconstruction. For zeta, real forms suffice because the actual measure is symmetric.

## Finite data, rounding and a positivity certificate

For any finite list of measurements \(Q(\sum c_kR_k)\), each observation is the integral of a bounded trigonometric polynomial in \(\gamma\). On symmetric measures use its even part. Let \(v(x)\) denote the resulting vector of test values at a symmetric pair \(\sigma_x=(\delta_x+\delta_{-x})/2\), with an added mass coordinate equal to 1. With \(d\) observations, choose \(d+2\) distinct positive \(x\). The columns \(v(x)\) have a real linear dependence. Its coefficients have both signs because their sum is zero. Taking positive and negative parts gives two distinct finite symmetric positive measures of equal mass with exactly the same observations. The atom pairs can be chosen inside any prescribed nonempty positive interval. These are synthetic measure countermodels.

A single finite datum can also admit a fixed positive amount of arbitrarily remote mass. The span of \(v(x)\) for \(x\) in any bounded open interval equals the full span, because a linear relation on the first set extends identically by real analyticity. Choose a basis of columns \(v(x_i)\) there and a measure with fixed strictly positive masses \(b_i\) on those pairs. For any remote \(x\), write \(v(x)=\sum_i\lambda_i(x)v(x_i)\). The coefficient vectors are uniformly bounded since the columns \(v(x)\) are bounded and the selected basis is fixed. Therefore there is a fixed \(\eta>0\) such that the measures

\[
  \sum_i (b_i-\eta\lambda_i(x))\sigma_{x_i}+\eta\sigma_x
\]

are positive and have the same datum for every remote \(x\). A known quantitative tail cap changes the allowed amount of remote mass. Separately, two distinct nearby atoms of the same weight give arbitrarily close finite observations and remain separated in total variation. Thus no generic exact height bound or total-variation stability follows from the finite measurements.

For certified interval inputs the absolute error in singleton inversion obeys

\[
 |\delta F(\log k)|\le\frac{k+1}{2\sqrt k}|\delta B|+\frac{|\delta C_k|}{2\sqrt k}.
\]

The difference-form extraction uses instead the mass error coefficient \((k+l)/(2\sqrt{kl})=\cosh(\tfrac12\log(k/l))\), bounded on a bounded ratio range. A known bound on a fractional moment \(\int|\gamma|^\alpha d\nu\) with \(0<\alpha\le1\) gives a rigorous Fourier interpolation modulus through \(|e^{-ih\gamma}-1|\le 2|h\gamma|^\alpha\). The actual-zero estimate above supplies finiteness for \(0<\alpha<1/4\). A numerical certificate needs a numerical bound on that moment.

For uniform samples \(F(jh)\), \(|j|\le d\), the Toeplitz matrix \(T_{ij}=F((j-i)h)\), \(0\le i,j\le d\), is PSD. This follows by interpreting \(c^*Tc\) as the integral of \(|p(e^{-ih\gamma})|^2\) with \(p(z)=\sum_j c_jz^j\). For example if \(h=\log k\) with integer \(k\ge2\), the singleton values at powers of \(k\) furnish these samples once \(B\) is available. Exact singularity forces support on the preimage of the unit-circle zeros of a nonzero kernel polynomial. A single grid leaves height aliases spaced by \(2\pi/h\). Two singular grids with incommensurable spacings, such as \(h=\log2,\log3\), force support in the finite intersection of their aliases, because any pair of residue classes has at most one common real point. Independent single-grid tests do not guarantee joint real-line feasibility. For instance \(F(h_1)=B>0\) and \(F(h_2)=-B\) each have individual rank-one realizations, but their support conditions are incompatible when \(h_1/h_2\) is irrational.

On a single grid Toeplitz positivity is sufficient for a positive circle measure with those moments. Indeed Fejér–Riesz factorization makes positivity on squares equivalent to positivity on nonnegative trigonometric polynomials of the measured degree. If the normalized moment vector lay outside the compact convex hull of the circle's evaluation vectors, a separating trigonometric polynomial would contradict that positivity. For the entire dense group \(G=\log\mathbb Q_{>0}\), positivity of all finite matrices \(F(t_j-t_i)\), \(t_i\in G\), must be accompanied by continuity at zero in the real topology. The Gram inequality gives \(|F(t+h)-F(t)|^2\le 2B(B-\Re F(h))\), so this continuity extends the function uniquely to a continuous positive-definite function on \(\mathbb R\). The classical Bochner theorem then supplies a finite positive real-line measure. The continuity condition is substantive. The character \(F(\log q)=(-1)^{v_2(q)}\), with \(v_2\) the exponent of 2 in the rational \(q\), satisfies every Gram test but is discontinuous along \(q=(2n+1)/(2n)\) for odd \(n\).

For certified intervals, a rigorous bound \(c^*Tc\le U\) implies \(\nu\{\gamma:|p(e^{-ih\gamma})|^2\ge\kappa\}\le U/\kappa\) for \(\kappa>0\). It yields an exact support constraint if \(U=0\) and positive feasibility is known. With continuous Fourier data on \([-L,L]\), a nonperiodic mass bound is also available. The triangularly weighted Fourier integral at \(x\) equals

\[
 \frac1L\int_{-L}^{L}(1-|t|/L)F(t)e^{itx}\,dt
 =\int \left(\frac{\sin(L(\gamma-x)/2)}{L(\gamma-x)/2}\right)^2d\nu(\gamma).
\]

It bounds \(\nu\{x\}\) from above. Its excess is at most \(\nu\{0<|\gamma-x|<r\}+4B/(L^2r^2)\). Thus a known gap around a selected node permits a quantitative atomic enclosure. These constraints apply to the asymptotic-error data or rigorous enclosures of it. They give no direct replacement by finite-\(N\) residual values.

Exact control fixtures used \(k=4,l=16\) and \(\gamma=\pi/(2\log4)\). For the asymmetric unit atom the calculation gives \(G_{kl}=5+10i\) and a difference form of 20, checking the sign of complex polarization. For its symmetric pair, the degree-two Toeplitz kernel is \(1+z^2\), checking the alias certificate.
