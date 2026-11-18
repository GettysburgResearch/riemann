# Full centered third tensor for cosine and sine prime bands

18 November 2026. Assume RH for the arithmetic calculation. Take weights supported in a common interval \([a,b]\), with \(0<a<b<1/6\). The weights may be any fixed bounded real Riemann-integrable functions, so different tests can use different, even disjoint, sub-bands. With \(x_p=\log p/\log Y\), put
\[
 C_f=\sum_p \frac{f(x_p)}{\sqrt p}\cos(\gamma\log p),\qquad
 S_g=\sum_p \frac{g(x_p)}{\sqrt p}\sin(\gamma\log p).
\]
Use the symmetric strict derivative-weighted tail and center by the actual means. On the random-matrix side, use the global derivative-square rooted CUE law and the tests
\[
 C_{f,N}=-\sum_k \frac{f(k/N)}k\sum_\ell\cos(k\vartheta_\ell),\qquad
 S_{g,N}=-\sum_k \frac{g(k/N)}k\sum_\ell\sin(k\vartheta_\ell),
\]
where the angles are relative to the chosen root, including the deterministic root. The two centered third tensors agree in the limit. For cosine arguments with weights \(f_1,f_2,f_3\), the common functional is the integral of \(\prod_i f_i(x_i)\) times the centered cosine kernel
\[
 C_{ccc}(x,y,z)
 =8xyz[-1+3(x^2+y^2+z^2)-3(x^2y^2+y^2z^2+z^2x^2)+2x^2y^2z^2]
\]
against \(dx\,dy\,dz/(xyz)\). For one cosine and two sine arguments the new common kernel and the resulting factorization are
\[
 \begin{split}
 C_{css}(x,y,z)&=12xy^2z^2(x^2-2),\\
 \lim\kappa(C_f,S_g,S_h)
   &=12\left(\int_a^b f(x)(x^2-2)\,dx\right)
       \left(\int_a^b g(y)y\,dy\right)
       \left(\int_a^b h(z)z\,dz\right).
 \end{split}                                                       \tag{1}
\]
Permutation of arguments gives the corresponding tensor entries. All entries with an odd number of sine arguments vanish exactly by reflection, at every finite cutoff on each side. Both sides have uniform fourth-moment bounds for these tests. The common tensor does not identify the full arithmetic band law. [Earlier cosine cubic](prime72_hlz_band_third_cumulant.md) · [Earlier cosine/sine covariance](prime71_hlz_band_covariance.md) · [Rooted CUE full-law construction](prime77_rooted_cue_band_limit.md)

## Arithmetic signed coefficient

The source is HLZ Theorem 5, its \(J\) in equation (5), and its auxiliary differentiated \(I\) in equation (24). In the following coefficient calculation \(x,y,z\) denote the scaled prime logs \(\log p_i/\log T\) at a prefix \(T\ge Y\); the deterministic weights on those primes are still evaluated at \(\log p_i/\log Y\). For a distinct prime use \(e_p(\rho)=p^{-1/2}e^{-i\gamma\log p}\) in the \(h\) slot and its conjugate in the \(k\) slot. The cosine contributes half the sum of the two phases, while the sine contributes \(i/2\) times the \(h\)-phase minus the \(k\)-phase. With two sine entries the common factor \(i^2=-1\) remains.

Write \(\alpha,\beta,c\) for the scaled shifts on separated Cauchy circles, and \((u,v,w,t)\) for the \(I\) tuples
\[
 (\alpha,\beta,c,0),\quad(-\beta,-\alpha,c,-\alpha-\beta),
 \quad(\alpha,-c,-\beta,-\beta-c).
\]
The leading \(h\) factor is \(e^{-v\xi}\) and the leading \(k\) factor is \(A(\xi)=e^{-u\xi}+e^{-w\xi}-1\), with a uniform \(O(1/p_i)\) local error. The latter follows from the exact single-prime local quotient and its factor \(p_i^{-1+O(1/\log T)}\). Therefore the \(I\) factor apart from its scaled quotient and time factor is
\[
 -\tfrac18(e^{-vx}+A(x))(e^{-vy}-A(y))(e^{-vz}-A(z)).
\]
If \(F(\xi)=1-4\xi+2\xi^3\) is the earlier one-prime kernel, this formula still has to be differentiated before centering. For \(J\) the corresponding three factors in the direct term are
\[
 -\tfrac18(e^{-\beta x}+e^{-\alpha x})
          (e^{-\beta y}-e^{-\alpha y})(e^{-\beta z}-e^{-\alpha z}),
\]
and in the dual they have \(e^{\alpha \xi}, e^{\beta \xi}\) in the first and second slots. The scalar \(J\) factors are \(1/(\alpha+\beta)\) and \(-e^{-\alpha-\beta}/(\alpha+\beta)\). Each \(I\) factor is multiplied by \(v e^t/((u+v)(v+w))\), then add the reflected \(I\) with outer shifts interchanged.

As in the pure cosine extraction, simultaneous rotation of the Cauchy circles selects cubic exponential terms for \(J\) and quartic ones for \(I\) before the auxiliary derivative. Extract \(\alpha\beta\) after applying \(\partial_c\) at zero to the reflected \(I\). The exact coefficients are
\[
 J_{\alpha\beta}=\tfrac12[-xyz-y^2z-yz^2+yz],\qquad
 I_{\alpha\beta}^{\rm summed}
       =\tfrac12[xyz-y^2z^2+y^2z+yz^2-yz].
\]
Division by the untwisted coefficient \(1/12\) gives the raw mixed coefficient \(-6y^2z^2\) for distinct primes. Subtract \(F(x)\) times the raw two-sine coefficient \(-6y^2z^2\), since each sine mean is zero, to get (1). In particular this is a signed extraction from the primary \(J,I\) formula, with no inference of the mixed coefficient from the all-cosine average. [Primary HLZ equations (5), (24)](../../sources/classical63_derivative_moments/hlz2022print.pdf) · [Exact arithmetic script](../../scripts/prime81_joint_third_check.py)

For uniformity, expand the products by using \(D_f(s)=\sum_p f(x_p)p^{-s}\) and its conjugate on the critical line. All polynomial product coefficients have fixed bounds depending only on the three weight bounds, and their lengths are at most \(Y^{3b}\). Each conjugate pair of signed products is evaluated by the previously checked bounded, divisor-closed padding and four-sign polarization at a declared \(T^\delta\) with \(3b<\delta<1/2\). Terms with \(i^2=-1\) have real scalar coefficients in this aggregate. The source error after normalization is a common \(o(1)\) for the finite list of whole polynomial pairs. The main local errors for distinct primes sum to \(o(1)\) because they carry the lcm factor \(1/(pqr)\), \(H=\sum_{Y^a<p\le Y^b}1/p=O(1)\), and \(\min p\to\infty\). This uses the sharp continuous input for all uniformly padded arrays. [Uniform aggregate proof](prime70_hlz_cutoff_extension.md) · [Sharp continuous estimate](prime75_hlz_sharp_aggregate_review.md)

If the two sine arguments use the same prime, the constant term of \(\sin^2\) contributes \(\tfrac12(\sum_p g(x_p)h(x_p)/p)E_T C_f+o(1)\). It cancels the corresponding diagonal in \((E C_f)(E S_gS_h)\) after transferring to the strict tail. A cosine–sine same-prime pairing has no constant term because \(\cos\vartheta\sin\vartheta=\sin(2\vartheta)/2\). All other repeated-prime terms have exponent two at a prime in their reduced signed word, with lcm factor bounded by \(1/(p^2q)\) for \(p\ne q\). Their aggregate versions have the same bounded coefficients and length, and their main terms vanish as \(H\sum_{p>Y^a}p^{-2}\to0\). All equal triples cost \(O(\sum_{p>Y^a}p^{-3/2})\) pointwise. In the three-cosine case the same cancellation occurs once for each of the three pair allocations. These arguments remain valid if a test's weight vanishes on one of the pair's supports.

For the strict tail, replacing the prefixes’ scaled logs by their values at \(T=Y\) changes the bounded main targets by \(O(\log(T/Y)/\log Y)\), by polynomial Lipschitz bounds and bounded harmonic sums. The inverse-quadratic Stieltjes integration transfers this to \(O(1/\log Y)\) with correct strict endpoint as before, and also transfers the aggregate \(o(1)\) errors. Mertens weighted Riemann sums converge to \(dx/x\) with the chosen bounded Riemann-integrable weights; excluding coincident labels loses \(o(1)\) in the product measure. The raw-to-centered subtractions therefore give exactly (1) and the stated cosine tensor. For a fixed test write it as the real or imaginary part of \(D_f\) and majorize its fourth absolute power by \(|D_f^2|^2\), of length \(Y^{2b}\). The bounded main multipliers and Poisson-product absolute coefficient majorant give \(O(1)\) since the harmonic band sum is bounded. This works also with signed \(f\) by the absolute coefficient majorant. Tail transfer and the bounded means give the uniform fourth bound for centered tests. A finite vector then has uniformly integrable monomials of total degree at most three by Hölder or the fourth power of its Euclidean norm.

## Independent rooted CUE tensor

For the globally tilted rooted CUE, the free points are the projection ensemble \(P=E-Q\), where \(E\) projects onto Fourier degrees \(0,\ldots,N\) and \(Q\) removes the two vectors with coefficients proportional to \(1\) and \(j-N/2\). This follows from the exact derivative-square tilted density \(\prod |1-z_\ell|^4\) times the free-particle Vandermonde squared. It does not require an arithmetic model assumption. The deterministic chosen root affects no third cumulant. [Finite tilt and projection](prime77_rooted_cue_band_limit.md) · [Hughes–Keating–O’Connell derivative moment density](../../sources/analytic64_prime_phase_clt_priority/hko.pdf)

Let \(A,B,C\) be the three commuting Fourier multiplication operators. Expansion of the logarithm of the determinantal generating function gives the mixed third trace
\[
 \operatorname{Tr}(PABC)
 -\operatorname{Tr}(PAPBC)-\operatorname{Tr}(PBPAC)-\operatorname{Tr}(PCPAB)
 +\operatorname{Tr}(PAPBPC)+\operatorname{Tr}(PAPCPB).
 \tag{2}
\]
For three signed exponentials of frequencies \(k,l,m\), the same expression with \(P=E\) is zero. It is zero if the signed total is nonzero by shift tracing. At resonance the trace counts are \(N+1\) for the one-block term, \(N+1-|k|,N+1-|l|,N+1-|m|\) for the two-block terms, and \(N+1-\max(|k|,|l|,|m|)\) for each three-block term. The last count follows from the span of the three visited offsets and uses \(3b<1\). Since the largest absolute frequency is half the sum of the three absolute frequencies at signed total zero, their trace combination in (2) cancels, including when two magnitudes agree.

Each remaining term has one or more rank-two removals. Split its cyclic trace at all occurrences of \(Q\), and multiply the resulting \(2\times2\) path-transfer matrices. For a segment of signed normalized shifts \(\delta_1,\ldots,\delta_j\) in operator order put \(t_0=0,\ t_i=\delta_j+\cdots+\delta_{j-i+1}\), \(l=-\min_i t_i\), \(r=1-\max_i t_i\). In the limiting orthonormal basis \(u(s)=(1,\sqrt{12}(s-\tfrac12))^{\mathsf T}\), the matrix is
\[
 \int_l^r u(s+t_j)u(s)^{\mathsf T}\,ds .
\]
All intervals have nonnegative length in this range. This follows by summing the two discrete \(Q\) basis vectors over the surviving paths and passing to a Riemann sum. The error is uniform, because the discrete vectors are normalized polynomial functions of \(j/N\), the integration endpoints are bounded, and the integrands are low-degree polynomials. Simultaneous conjugation by the fixed diagonal scaling \({\rm diag}(1,\sqrt{12})\) gives the rational integrand with entries \(1,12(s-\tfrac12),s+t_j-\tfrac12,12(s+t_j-\tfrac12)(s-\tfrac12)\), used for exact polynomial operations.

For \(x=k/N,y=l/N,z=m/N>0\) write \(L(\epsilon_x x,\epsilon_y y,\epsilon_z z)\) for the correction obtained from (2) using these path matrices. Fourier expansion of the three negatively signed trigonometric tests yields
\[
 \frac14\sum_{\epsilon_y,\epsilon_z=\pm1}
       \epsilon_y\epsilon_z L(x,\epsilon_y y,\epsilon_z z)
\]
for the cosine–sine–sine entry, because the two sine multipliers supply an additional minus sign in addition to the three negative outer signs. Reflection identifies simultaneous sign reversals so only four terms remain. For the three cosines the combination is \(-\frac14\sum L(x,\epsilon_y y,\epsilon_z z)\). The exact path endpoints can change order only at equal frequencies or when the sum of the two smaller frequencies equals the largest. Check each permutation of the three positive frequencies and the two signs of that latter comparison within each order. These are 12 chambers. On each chamber rational polynomial expansion of (2) and its four sign choices gives precisely \(12xy^2z^2(x^2-2)\) for the mixed entry and \(C_{ccc}\) for the three cosines. The polynomial identities extend to the boundaries by continuity of the path integrals, and the calculation never uses an arithmetic coefficient inside a CUE trace. Summing with \(f(k/N)g(l/N)h(m/N)/(klm)\) gives the stated frequency integral by Riemann summation. [Exact 12-chamber replay](../../scripts/prime81_joint_third_check.py) · [Recorded output](../../experiments/results/prime81_joint_third_check.txt)

Uniform fourth bounds follow on this side from the finite projection exponential-moment inequality used in the full-law proof. For these tests the trigonometric polynomial has bounded sup norm. By Fourier orthogonality its squared integral against \(d\theta/(2\pi)\) is \(O(\sum_{aN\le k\le bN}1/k^2)=O(1/N)\), also for signed weights. The free-particle density is bounded by \(N+1\) relative to this measure. Thus the exponential-moment bound for each centered test is uniform for every fixed real argument, which supplies uniform fourth moments and joint cubic uniform integrability.

## Consequence

For the same unweighted band, writing \(\Delta_j=b^j-a^j\), (1) gives
\[
 \lim\kappa(C_1,S_1,S_1)=(\Delta_3-6\Delta_1)\Delta_2^2<0 .
\]
The value is \(-21537/1280000000\) on \([1/20,1/10]\). More generally it is negative for a cosine test with nonnegative weights and two sine tests with nonnegative weights whenever the three relevant integrals are nonzero. In particular, take a single sine test twice, possibly on a band disjoint from the cosine support. The cosine and sine tests have exact zero covariance by reflection. Uniform fourth moments imply that in any weak subsequential limit their centered mixed cubic still has the nonzero value (1). Independence in such a limit would force that cubic to vanish. Thus the joint arithmetic limit cannot have independent cosine and sine components in those cases, even across disjoint frequency bands. This does not settle whether a sine marginal alone is Gaussian, or whether the entire arithmetic vector converges.
