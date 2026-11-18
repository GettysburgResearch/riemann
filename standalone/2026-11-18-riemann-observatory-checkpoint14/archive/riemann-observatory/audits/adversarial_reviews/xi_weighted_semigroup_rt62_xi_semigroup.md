# Conditional spectral audit of the xi-weighted translation semigroup

Reviewer rt_repair_62. Assume RH, and let \(F(w)=\xi(1/2+w)\), where \(\xi(s)=\tfrac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s)\). Use \(H^2(\mathbb C_+)\) with boundary norm \(dt/(2\pi)\). The operators examined here are
\[
 (W_\tau f)(w)=H_\tau(w)f(w+\tau),
 \qquad H_\tau(w)=F(w)/F(w+\tau).
\]
For this candidate, \(W_\tau\) is a strongly continuous contraction semigroup. Every positive-time operator is compact, injective and quasinilpotent. Its actual infinitesimal generator has empty spectrum. The compactness proof below uses only the paired product and the classical zero count, without any bounds for the reciprocal of zeta near the line.

## Product input and uniform boundary decay

Classical inputs are the order-one entire xi function and its Hadamard factorization, the xi functional equation, and the Riemann–von Mangoldt formula with \(O(\log T)\) error. See Titchmarsh, second edition, §2.12, in particular (2.12.5), and Theorem 9.4 in the [cached source](../../sources/equivalence_round2/titchmarsh1986.pdf). Only the complete xi function is used at \(s=1\), where its apparent pole is removable. By the zero count \(\sum_{\gamma>0}m_\gamma/\gamma^2<\infty\). Under RH, pair the zeros \(\pm i\gamma\) in the genus-one product. Its factors pair to \(1+w^2/\gamma^2\), and evenness of \(F\) forces the residual exponential to be constant. Thus
\[
 F(w)=Cw^{m_0}\prod_{\gamma>0}(1+w^2/\gamma^2)^{m_\gamma},
 \qquad
 G(w)=F'(w)/F(w)=\frac{m_0}w+
  \sum_{\gamma>0}m_\gamma\left(\frac1{w-i\gamma}+\frac1{w+i\gamma}\right).
\]
The possible central multiplicity \(m_0\) is harmless here, and the derivative series converges locally uniformly off the zeros by pairing. Each reciprocal has nonnegative real part in \(\mathbb C_+\), so \(\Re G\ge0\). Hence \(|H_\tau|\le1\) by integrating \(G\) along the horizontal segment. For every \(\tau>0\), the denominator is nonzero on the closed right half-plane, so \(H_\tau(it)\) is the actual continuous boundary value, including zero at each boundary zero of \(F\).

To prove decay, the positive ordinate count satisfies
\[
 N(T)=\frac{T}{2\pi}\log\frac{T}{2\pi}-\frac{T}{2\pi}+O(\log T).
\]
Take the implied absolute error constant \(C_0\). For sufficiently large fixed \(M\), the main term in \(N(t+M)-N(t-M)\) is \((M/\pi)\log t+O_M(1)\), exceeding the sum of error margins by a fixed positive multiple of \(\log t\). This gives at least \(c\log |t|\) zeros with \(|\gamma-t|\le M\), counting multiplicities. For negative \(t\) use symmetry. Every individual factor of the boundary quotient, indexed by a zero \(i\gamma\), has modulus
\[
 \frac{|t-\gamma|}{\sqrt{\tau^2+(t-\gamma)^2}}\le1.
\]
The factors within the fixed window have modulus at most \(M/\sqrt{M^2+\tau^2}<1\). This bound applies to sufficiently long paired finite products, with the constant canceling, and passes to the locally convergent quotient. Thus \(|H_\tau(it)|\ll_\tau |t|^{-c_\tau}\) for large \(|t|\), a uniform tail estimate for each fixed \(\tau>0\). The normalization \(F(w)=\xi(1/2+w)\) uses ordinary zeta ordinates.

## Contraction, strong continuity, and compactness

Horizontal translation \(T_\tau f=f(\cdot+\tau)\) is a Hardy-space contraction, either by the definition via line norms or by the Paley–Wiener representation. Multiplication by \(H_\tau\) is contractive. The quotient identity \(H_{\tau+\delta}(w)=H_\tau(w)H_\delta(w+\tau)\) gives the semigroup law for \(W_\tau\). For each \(f\), \(W_\tau f(w)\to f(w)\) at each interior point as \(\tau\downarrow0\). Evaluation kernels have dense span, and \(\|W_\tau f\|\le\|f\|\), so this is weak convergence in the Hilbert space. The same norm bound then gives strong convergence by expanding \(\|W_\tau f-f\|^2\). The semigroup law gives strong continuity at positive times.

For \(\tau>0\), the output restricted to \(|t|\le R\) is the bounded multiplier \(H_\tau(it)\) times \(f(\tau+it)\). If \((e_n)\) is an orthonormal basis, then
\[
 \sum_n\int_{-R}^{R}|e_n(\tau+it)|^2\frac{dt}{2\pi}
 =\int_{-R}^{R}\|\operatorname{ev}_{\tau+it}\|^2\frac{dt}{2\pi}<\infty,
\]
because \(\|\operatorname{ev}_{z}\|^2=(2\Re z)^{-1}\). Thus the truncated output map into boundary \(L^2\) is Hilbert–Schmidt. The norm of the omitted part is at most \(\sup_{|t|>R}|H_\tau(it)|\), by contractivity of \(T_\tau\). The latter bound tends to zero, so the full boundary output map is compact. Its range is in the closed Hardy subspace, hence \(W_\tau\) is compact as an operator on \(H^2\). No claim is made that the truncated maps themselves have range in the Hardy subspace. Injectivity follows from nonvanishing of \(H_\tau\) in \(\mathbb C_+\) and analyticity of \(f\).

## Spectral radius and the full generator resolvent

If \(W_\tau f=\lambda f\) with \(f\ne0\) and \(\lambda\ne0\), choose one \(w_0\) with \(f(w_0)\ne0\). Iterating gives
\[
 |f(w_0+n\tau)|=|\lambda|^n |F(w_0+n\tau)|\,|f(w_0)/F(w_0)|.
\]
Stirling's formula in the fixed-imaginary-part horizontal ray gives
\(\log |F(w_0+n\tau)|=(n\tau/2)\log (n\tau)+O_{\tau,w_0}(n)\). This uses \(\zeta(1/2+w_0+n\tau)=1+o(1)\) by absolute convergence, and requires no uniformity over \(w_0\). Thus the right hand side diverges, whereas the Hardy evaluation estimate gives \(O(n^{-1/2})\). Compactness and the absence of nonzero eigenvalues give \(\sigma(W_\tau)=\{0\}\), since zero belongs to the spectrum of any compact operator on this infinite-dimensional space.

Fix one \(\tau>0\). The spectral radius formula gives, for every \(b>0\), a constant \(C_b\) such that \(\|W_\tau^n\|\le C_b e^{-b n\tau}\). Writing times as \(t=n\tau+s\), \(0\le s<\tau\), and using \(\|W_s\|\le1\) gives \(\|W_t\|\le C_b e^{b\tau}e^{-bt}\). For any complex \(\lambda\), the bounded operator
\[
 R_\lambda f=\int_0^\infty e^{-\lambda t}W_t f\,dt
\]
is therefore defined by a norm-convergent vector Bochner integral. To check the resolvent without spectral mapping, the semigroup law gives
\[
 W_hR_\lambda f=e^{\lambda h}\left(R_\lambda f-\int_0^h e^{-\lambda t}W_t f\,dt\right).
\]
The difference quotient at \(h=0\) is \(\lambda R_\lambda f-f\), so \(R_\lambda f\in D(A)\) and \((\lambda-A)R_\lambda f=f\). For \(g\in D(A)\), differentiate \(e^{-\lambda t}W_t g\) using the generator orbit identity and integrate from zero to infinity. The upper endpoint vanishes by the same norm bound, proving \(R_\lambda(\lambda-A)g=g\). This covers every finite \(\lambda\). It does not identify the spectrum of \(A\) by taking logarithms of \(\sigma(W_\tau)\).

## Actual domain and evaluation-kernel behavior

Bounded evaluation of the difference quotient shows that \(Af=f'-Gf\) for \(f\in D(A)\). Conversely, if \(f\in H^2\) and the analytic function \(q=f'-Gf\) is in \(H^2\), the scalar differentiation identity \(\partial_s W_s f(w)=W_s q(w)\) gives
\(W_\tau f-f=\int_0^\tau W_s q\,ds\). The equality holds in \(H^2\) by bounded evaluations of the strongly continuous integrand. Dividing by \(\tau\) and using strong continuity proves
\[
 D(A)=\{f\in H^2:f'-Gf\in H^2\}.
\]
This is the maximal analytic domain, with no requirement that \(f'\) and \(Gf\) separately belong to \(H^2\). The general weighted-composition domain formula has a known antecedent in Gallardo-Gutiérrez, Siskakis and Yakubovich, [arXiv:2110.05247v1](https://arxiv.org/pdf/2110.05247v1), Theorem 2.1(ii). Here the half-plane identity was proved directly.

For \(z=x+iy\), the normalized kernel is \(k_z(w)=\sqrt{2x}/(w+\bar z)\), and \(|k_z(it)|^2dt/(2\pi)=P_x(t-y)dt\). The shifted kernel difference \(T_\tau k_z-k_z\) is \(O_z(\tau)\) in Hardy norm, by integrating its Hardy derivative. Therefore
\[
 \left|\|W_\tau k_z-k_z\|-\|(H_\tau-1)k_z\|\right|=O_z(\tau).
\]
The paired product is the compensated Herglotz representation of \(G\) with \(a=0\) and positive atomic masses \(m_\gamma\). In the logarithmic derivative of the unshifted paired product the compensation terms cancel on \(\pm\gamma\); the full compensated integral is absolutely locally convergent. For applying the Poisson formula at \(z\), replace \(G(w)\) by \(G(w+iy)\). The shifted masses are at \(\gamma-y\), and changing the compensation modifies only the imaginary constant by an absolutely convergent sum, since the change in \(\gamma/(1+\gamma^2)\) is \(O_y((1+\gamma^2)^{-1})\) at large \(|\gamma|\). The [general Herglotz slope formula](herglotz_atomic_energy_rt62_herglotz.md) gives a strictly positive finite limit of \(\tau^{-1}\|(H_\tau-1)k_z\|^2\), since there are zeros and every positive atom has positive slope. Thus \(k_z\notin D(A)\). Independently, near any zero \(i\gamma\), \(G(w)=m_\gamma/(w-i\gamma)+O(1)\), and \(k_z(i\gamma)\ne0\). The local simple pole of \(k_z'-Gk_z\) makes its Hardy line norms unbounded as the line approaches the boundary, giving the same exclusion. The span of all evaluation kernels is dense, and the generator domain is dense by strong continuity. These statements are consistent.

The conclusion excludes this particular Hardy-space generator as an operator whose spectrum lists the zeta zeros, conditional on RH. It does not address other proposed spectral realizations or RH itself. No priority claim is made for the xi specialization.
