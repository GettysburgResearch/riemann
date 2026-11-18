# Independent review of Suzuki finite-window controls

Date 2026-11-17. I verified the polynomial quartet construction, the real-axis norm computation and time envelope, and the compact-compression perturbation. The finite-model identity holds with Lebesgue measure and the corrected factor of \(\pi\). The spectral data change by \(O(B^{-2})\) and the phase data by \(O(B^{-1})\), uniformly on a fixed compact time window. The review uses the signed convention and normalization already adjudicated for the merged paper. The Landau criterion has its own adjudication. [Proposed finite-certificate bounds](effective_cluster62_suzuki_finite_certificates.md) · [Signed-time correction](director_suzuki_correction_round8.md) · [Tail criterion](director_suzuki_landau_round8.md)

## Exact polynomial reference model

Let \(A_0\) be a real even polynomial with distinct nonzero real roots \(\Gamma_0\). Write \(r=A_0'/A_0\), \(M_0=(1-ir)^{-1}\), and \(c_\gamma(t)=(e^{-i\gamma t}-1)/\gamma\). The corrected line on the real axis is
\[
 S_{0,t}(x)=-i M_0(x)\sum_{\gamma\in\Gamma_0}\frac{c_\gamma(t)}{x-\gamma}.
\]
At each root \(\gamma\), the multiplier has a simple zero and the corresponding product has a removable singularity. All the resulting rational summands are square integrable. In particular, the *unmultiplied* sum can have a real pole and its square integral is generally divergent.

An elementary contour calculation fixes the orthogonality and normalization. Define \(H(z)=(1+ir(z))^{-1}\). Since \(r(z)=\sum_{\gamma\in\Gamma_0}(z-\gamma)^{-1}\) has negative imaginary part in the open upper half-plane when the root set is nonempty, \(H\) is holomorphic there. At a root \(\gamma\), \(H(z)=-i(z-\gamma)+O((z-\gamma)^2)\). On the real line \(\Re H=|M_0|^2\). For distinct \(\gamma,\delta\), the quotient \(H(z)/[(z-\gamma)(z-\delta)]\) is holomorphic through the boundary and decays as \(O(|z|^{-2})\), so its integral on the real line vanishes. For \(\delta=\gamma\), the quotient has a boundary pole with residue \(-i\). The clockwise upper semicircle indented at that pole contributes \(-i\pi(-i)=-\pi\), so the principal value real-line integral is \(\pi\). Its real part is an ordinary convergent integral because the residue is purely imaginary. Thus
\[
 \int_{\mathbb R}\frac{|M_0(x)|^2}{(x-\gamma)(x-\delta)}\,dx
   =\pi\,\mathbf 1_{\{\gamma=\delta\}}.
\]
This proves the needed finite orthogonal identity directly. For a real root of multiplicity \(m\), the same calculation gives \(\pi/m\) for the squared norm, which combines with the coefficient \(m c_\gamma(t)\) to restore the spectral weight \(m\).

With the inner product linear in its first argument, the Gram sum divided by \(\pi\) is \(\sum_\gamma c_\gamma(t)\overline{c_\gamma(u)}\). Pairing \(\gamma\) and \(-\gamma\) gives
\[
 \frac{\langle S_{0,t},S_{0,u}\rangle}{\pi}
   =\sum_{\gamma\in\Gamma_0}
       \frac{1-\cos(\gamma t)-\cos(\gamma u)+\cos(\gamma(t-u))}{\gamma^2}
   =G_{-\Psi_0}(t,u).
\]
The diagonal is \(\|S_{0,t}\|_2^2/(2\pi)=\Psi_0(t)\). For increments with common base time \(v\), each coefficient is multiplied by \(e^{-i\gamma v}\); its product with its conjugate is one. The identities therefore hold for all real signed times and basepoints, with no need to prove completeness or handle an atom at infinity.

## Quartet perturbation and uniform tails

Fix \(a>0\) and let \(A_B=A_0((z-B)^2+a^2)((z+B)^2+a^2)\) for \(B>0\). The roots \(\pm B\pm ia\) are distinct and simple, disjoint from the real roots. They correspond to parameters \(s=1/2-iz\) with real parts \(1/2\pm a\). For every fixed \(T\) and \(a\), each new cosine numerator on \(|t|\le 2T\) is bounded independently of \(B\), and \(|\gamma|^2=B^2+a^2\). The uniform difference in \(\Psi\) and in the screw kernel on \([-T,T]^2\) is \(O_{T,a}(B^{-2})\).

On the real axis write \(M_B=(1-i(r+q_B))^{-1}\), where
\[
 q_B(x)=\frac{2(x-B)}{(x-B)^2+a^2}+rac{2(x+B)}{(x+B)^2+a^2}.
\]
Both multipliers have modulus at most one. At points outside the old root set the resolvent identity gives \(M_B-M_0=i q_B M_B M_0\). The contribution from varying the multiplier on the old sum is therefore bounded pointwise by \(|q_B|\,|S_{0,t}|\), with the bound extending through removable points. The old path has \(|S_{0,t}(x)|\le C_{A_0,T}/(1+|x|)\) by the finite sum of canceled rational terms. Since \(q_B\to0\) pointwise and \(|q_B|\le 2/a\), this already proves convergence in \(L^2\) uniformly in time. The bound improves to \(O_{A_0,T,a}(B^{-1})\). On \(|x|\le B/2\), use \(|q_B|\le 8/B\) with the uniform old norm. On the complement use \(|S_{0,t}|\le 2 C_{A_0,T}/B\) and the uniform \(L^2\) bound on \(q_B\). Each translate \(2y/(y^2+a^2)\) has squared norm \(2\pi/a\).

For a new root \(\gamma\), \(|c_\gamma(t)|\le(e^{aT}+1)/B\) and \(\|(x-\gamma)^{-1}\|_2=\sqrt{\pi/a}\). Multiplication by \(M_B\) can only decrease this norm. The four new terms contribute \(O_{T,a}(B^{-1})\). The integral tails can also be taken uniformly over \(B\ge 1\). If \(|x|\le 2B\), then \((1+|x|)/(B|x-\gamma|)\le3/a\). If \(|x|>2B\), use \(|x-\gamma|\ge |x|/2\). Combining these bounds with the old envelope and \(|q_B|\le 2/a\) gives
\[
 \sup_{B\ge 1,\,|t|\le T}|S_{B,t}(x)|\le \frac{C_{A_0,T,a}}{1+|x|},
 \qquad
 \sup_{B\ge 1,\,|t|\le T}\int_{|x|>R}|S_{B,t}(x)|^2\,dx=O_{A_0,T,a}(R^{-1}).
\]
It follows by Cauchy–Schwarz that the phase Gram and squared norms converge at rate \(O_{A_0,T,a}(B^{-1})\), as does the norm defect relative to the zero defect of the reference model. The maximum modulus principle rules out the inner-function hypothesis for \(\Theta_B\), a nonconstant function that takes the value \(-1\) at a simple upper-half-plane root of \(A_B\).

The perturbed model eventually exhibits a negative screw diagonal. Take \(B>a\) and \(t_k=2\pi k/B\). Every quartet cosine at \(t_k\) equals \(\cosh(a t_k)\), so
\[
 \Psi_B(t_k)-\Psi_0(t_k)
  =4\frac{B^2-a^2}{(B^2+a^2)^2}\bigl(1-\cosh(a t_k)\bigr).
\]
The reference contribution is uniformly bounded in time. Hence \(G_{-\Psi_B}(t_k,t_k)=2\Psi_B(t_k)\) is negative for all large \(k\), and the defect satisfies \(e^{-\omega t_k}D_B(t_k)\to+\infty\) for \(0\le\omega<a\). These late failures coexist with arbitrarily close data throughout any fixed compact window.

Strictly positive finite spectral compressions persist under the perturbation by the least-eigenvalue margin. For any prescribed distinct nonzero real times \(t_1,\ldots,t_n\), such a strict reference matrix is available. Choose \(\delta>0\) small enough that the \(w_i=e^{-i\delta t_i}\) are distinct and differ from \(1\), and use reference roots \(\pm j\delta\), \(1\le j\le n\). The coefficient matrix restricted to the positive roots, after scaling, has entries \(w_i^j-1=(w_i-1)(1+w_i+\cdots+w_i^{j-1})\) and is invertible by the Vandermonde determinant. Times equal to zero or duplicate times give structural rank deficiencies. Taking \(\omega<a<1/2\) retains geometric strip confinement for any target \(\omega<1/2\). This argument concerns finite positive margins and approximate data for real even polynomials. In this class exact spectral agreement on an interval with interior would imply global agreement by analyticity in time. The polynomial construction has no arithmetic zeta input.

The delayed perturbation in the last paragraph of the proposal also checks out in the generic Laplace-data class. Its transform is \(e^{-uT_0}(\frac14\sum_{\lambda\in\{\pm a\pm iB\}}(u-\lambda)^{-1}-u^{-1})\). Each of the four residues is nonzero. When adding it to pre-existing meromorphic data, take \(B\) away from the original pole set if a genuine new pole is needed. The delay preserves the data up to and including \(T_0\).

## Arithmetic norm computation on bounded time intervals

I checked the two real-axis cancellation ratios directly in (1.5)–(1.6). On \(x\in\mathbb R\), \(A\) and \(A'\) are real, \(\xi'(1/2-ix)=iA'(x)\), and \(E^\sharp=A-iA'\). The phase factor \(A/E^\sharp\) and the ratio \(\xi'/E^\sharp\) have modulus at most one. At a real zero of order \(m\), the denominator has order \(m-1\) and both ratios extend. This cancels the entire singular part of the log derivative on the real line after applying the completed-zeta identity. The remaining gamma, rational and constant terms times \((e^{-ixt}-1)/x\), and the bounded-time prime and polar terms, satisfy (B) with explicit constants. The prime summand is continuous when written with \((t-\log n)_+\) inside the exponential difference. [Journal formulas (1.5)–(1.6) and (4.3)](https://doi.org/10.4153/S0008414X25101739) · [Author erratum](https://drive.google.com/file/d/1Gi7cUoqA_izzdsH5lzEL48bl20Lf9c8_/view?usp=sharing)

For the fixed digamma difference and the Lerch difference, put \(b_n=n+1/4\). Each series is bounded in absolute value by \((|x|/2)\sum_{n\ge0}1/[b_n|b_n-ix/2|]\), since the Lerch powers have absolute value at most one. For \(|x|\ge1\), the part with \(b_n\le |x|\) is bounded by a harmonic sum and the complementary part by \((|x|/2)\sum_{b_n>|x|}b_n^{-2}\). For \(|x|\le1\), the whole bound is \((|x|/2)\sum b_n^{-2}\). Division by \(x\), with the limit at zero, gives (B). Evaluating the Lerch *difference* by its absolutely convergent subtracted series is essential at \(t=0\), where the individual first-order Lerch series at \(q=1\) diverge. The two archimedean differences cancel there, consistently with \(S_0=0\). Signed negative times preserve the absolute value bound.

The envelope gives a computable squared tail \(O(B_T^2(1+\log R)^2/R)\) and bounds cross-product tails as well. On a compact real integration interval, subdivide and retain cells with certified nonvanishing denominator. The zeros of \(E^\sharp\) are isolated and finite on that interval. Every point outside them is eventually in a safely certified neighborhood, so the uncaptured length can be certified smaller than any specified positive tolerance. The envelope bounds the lost integral by this length times a uniform bound on the product. On the retained cells, the regular expression and the absolutely convergent subtracted sums admit interval quadrature. This is an absolute-tolerance algorithm at computable times and uses no certificate of real-zero multiplicities. The separate spectral truncation employs the unconditional \(O(\log(2+k))\) multiplicity count in unit-height windows and \(|\Im\gamma|<1/2\). Summing \(\log(2+k)/k^2\) past \(R\) yields the stated \(O(\log R/R)\) factor. A spectral computation by this route must account for all enclosed zeros.

The displayed time modulus away from zero also extends through zero. For \(0<h\le1/2\), the time-dependent Lerch part after division by \(x\) is a fixed multiple of \(\sum e^{-2b_nt}/[b_n(b_n-ix/2)]\). Its increment between nonnegative times at distance \(h\) is bounded in absolute value by a constant times
\[
 \sum_{n\ge0}\frac{\min(2b_nh,1)}{b_n^2}=O(h\log(2/h)),
\]
uniformly in \(x\). The other time-dependent terms have an increment bounded by \(C_T h(1+\log(2+|x|))\), by the canceled log derivative and the finite hinged prime sum. Split the squared integral of the total increment at \(|x|=1/h\), using these estimates inside and (B) outside. This gives \(\|S_t-S_u\|_2\le C_T\sqrt h\log(2/h)\) throughout \([-T,T]\), with the signed reflection on each half-line and the triangle inequality across zero. Formula (4.3) gives \(|\Psi(t)-\Psi(u)|=O_T(h\log(2/h))\) by the same sum bound for its \(e^{-2b_n|t|}/b_n^2\) term, and a Lipschitz bound on the remaining terms. At zero the sharper expansion is \(\Psi(t)=\frac12|t|\log(1/|t|)+O(|t|)\). It follows by replacing \(1-e^{-2b_n|t|}\) by \(2b_n|t|\) below \(b_n=1/|t|\) and bounding both the Taylor error and the rest of the sum by \(O(|t|)\). Thus the away-from-zero Lipschitz assertion requires its stated domain, and the weaker modulus certifies the norm defect throughout the compact interval. A finite grid plus such a modulus yields bounds on its chosen compact interval.

The same continuity makes the conjugated path in (1.7) Bochner integrable against any compactly supported smooth test, with \(\|\widehat{P D\psi}\|_2\le C_T\|\psi'\|_1\) for tests supported in \([-T,T]\). The map \(D=i\,d/dt\) takes the compact smooth tests bijectively to the compact smooth tests of integral zero, by taking a primitive from \(-\infty\). If the asserted global equality holds on this domain, the nonnegative squared norm yields Weil positivity directly. The finite computation above concerns the defined norm and its compact-time regularity.

## Compact-compression control

Let \(K\ge0\) be compact self-adjoint on an infinite-dimensional Hilbert space and \(P\) project onto any finite-dimensional tested subspace. An orthonormal sequence in \(\ker P\) is weakly null, so its images under \(K\) tend to zero in norm. Given \(\epsilon>0\), choose a unit vector \(e\) of this sequence with \(\langle Ke,e\rangle<\epsilon/4\). Then \(K'=K-(\epsilon/2)e\otimes e\) has \(PK'P=PKP\), \(\|K'-K\|<\epsilon\), and \(\langle K'e,e\rangle<0\). For a continuous kernel on a compact time interval, one can also choose \(e\) smooth by constructing the orthonormal sequence in the intersection of the smooth vectors with the finitely many orthogonality constraints. Its rank-one kernel is continuous. If a finite-data certificate uses only the compression and an arbitrarily small norm error, this perturbation gives identical compressed data with a negative unseen direction. A claim for a particular structured kernel would require checking that structure separately. In the arithmetic problem, a negative direction for the screw kernel \(G_g\) has different force from the unconditional positive Gram kernel built from the \(S_t\) path.
