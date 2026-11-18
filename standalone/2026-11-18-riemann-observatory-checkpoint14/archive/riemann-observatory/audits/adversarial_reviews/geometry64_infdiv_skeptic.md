# Independent audit of the Nakamura–Suzuki finite-test obstruction

The proposed remote quartet construction passes the stated tests. A strengthened version passes **every finite grid of any cardinality and diameter at most a prescribed \(H\)**, with one choice of the sinc spacing and every positive exponential power. Its off-axis quartet still makes \(g_T\) positive at arbitrarily late times. The same verification confirms the real-line versus compact-group distinction and the \(-1/2\) cusp coefficient for the actual zeta exponent. The calculations below make no novelty claim. [Bridge under review](positivity64_infdiv_bridge.md)

## Primary criterion and conventions

I checked the five-page Nakamura–Suzuki article *On infinitely divisible distributions related to the Riemann hypothesis*, arXiv:2306.08317v1, June 2023 (the PDF footer says version June 16). Theorems 1.1 and 1.2 state the real-line criterion and compound Poisson measure, respectively. Equation (1.7), Lemma 2.1, Lemma 2.2 and §3 provide the convergent zero sum and the transform identification with the arithmetic exponent in (1.5). The local source copy has SHA-256 \(\texttt{756288c39bfd743f08f24b1e5074bb8a4adbe8a959d42edd763af07678801830}\). [Primary PDF](../../sources/suzuki_model63_positivity/suzuki_2306_candidate.pdf)

With \(E(z)=\xi(1/2-iz)\), the \(i\) in \(iE'(z)/(z^2E(z))\) is correct. For each zero \(\gamma\ne0\),
\[
\int_0^\infty \frac{e^{-i\gamma t}-1}{\gamma^2} e^{izt}\,dt
=\frac{i}{z^2}\left(\frac1{z-\gamma}+\frac1\gamma\right)
\quad\bigl(\operatorname{Im}z>\max(0,\operatorname{Im}\gamma)\bigr).
\]
The strip bound and \(\sum m_\gamma/|\gamma|^2<\infty\) give an integrable majorant \(C(e^{ht}+1)e^{-t\operatorname{Im}z}\) if the strip has half-width \(h\) and \(\operatorname{Im}z>h\). This controls the unbounded integration interval directly. Evenness removes the linear Hadamard term, and conjugation symmetry together with evenness makes the zero sum real. Under RH the inverse-square weights give a finite positive symmetric Lévy measure. Conversely a characteristic function of the form \(e^{g_\zeta}\) gives \(g_\zeta\le0\), irrespective of whether infinite divisibility was assumed. A fixed-sign Laplace abscissa strictly inside the upper half-plane would give a singularity at a positive imaginary point where \(E'/E\) is regular. The identity theorem then excludes all upper-half-plane zeros, and evenness gives all lower-half-plane zeros the same exclusion.

The eventual fixed-sign argument also works for either sign: subtract the integral on a finite initial interval, which is entire, then use the fixed-sign theorem if the remaining abscissa is positive. An identically zero tail already gives an entire transform. The absolute subexponential bound is independently sufficient by absolute convergence throughout the upper half-plane. The pole at \(z=0\) of the prefactor does not affect either argument. [Primary text, Lemma 2.2 and proof of Theorem 1.1](https://arxiv.org/pdf/2306.08317v1)

## Remote quartet and the original finite test

Each sinc factor is an even real entire function of exponential type. On the imaginary axis the factors are positive hyperbolic sine quotients, and their product grows exponentially there, up to a power of the ordinate. The quartet factor contributes a positive absolute square on the same axis and only polynomial growth. Thus both entire functions have order exactly one. Normalization gives \(E_T(0)=1\), the nonzero real zero lattices have irrational ratio and no overlap, and the quartet consists of four distinct simple zeros when \(T>a>0\). Under \(z=i(s-1/2)\) the zero strip becomes \(|\operatorname{Re}s-1/2|\le a<1/2\), and the resulting \(\Xi_T\) is real on the real axis and symmetric about \(1/2\). This family has linear zero counting growth, so its preserved hypotheses do not include the Riemann–von Mangoldt counting asymptotic.

Write \(A+iB=(T+ia)^{-2}\) and \(q_T=g_T-g_0\). Pairing the four terms gives \(q_T=4\operatorname{Re}((\cos((T+ia)t)-1)(A+iB))\). In particular,
\[
q_T(t)/4=A(\cos(Tt)\cosh(at)-1)+B\sin(Tt)\sinh(at),
\]
where \(A=(T^2-a^2)/(T^2+a^2)^2>0\) and \(B=-2Ta/(T^2+a^2)^2\). Since \(|\sin(Tt)|\le T|t|\), the bound \(q_T(t)\le C_{a,H}T^{-2}t^2\) on \([-H,H]\) follows with the sign stated in the bridge. For \(g_0\), any single zero pair gives a strict quadratic bound near zero. At every other point at least one cosine from the two lattices differs from one. On the rest of the compact interval the negative ratio \(g_0(t)/t^2\) therefore has a strictly negative maximum. Taking \(C_{a,H}T^{-2}<c_H\) gives \(g_T(t)<0\) throughout \(0<|t|\le H\), and \(g_T(0)=0\). At \(t_n=2\pi n/T\) the quartet contributes \(4A(\cosh(at_n)-1)\), while \(g_0\) is globally bounded. Thus the positivity tests cannot extend to all real times.

On a prescribed grid of \(r\) distinct times, the phases \(e^{ib t_i}\) can be made distinct by excluding countably many \(b\). On zero-sum vectors the baseline quadratic form is a nonnegative sum of squared trigonometric sums. Using frequencies \(b,2b,\ldots,rb\) gives an invertible Vandermonde matrix, validating strictness. The vanishing entrywise perturbation preserves strictness on the unit sphere of each finite zero-sum subspace. No uniformity in \(c\) is needed for that step. If \(G\) is the resulting conditionally positive grid matrix, anchor with \(B_{ij}=G_{ij}-G_{i1}-G_{1j}+G_{11}\). The zero-sum test gives \(B\succeq0\). The entrywise exponential of \(cB\) is positive semidefinite by its power series and the Schur product theorem. Diagonal congruence recovers \([\exp(cG_{ij})]\) for every \(c>0\). The proof handles arbitrary real locations of the prescribed grids, including times far outside \([-H,H]\) when their differences are among the finitely many tested values.

## Strengthening to all grids of bounded diameter

Choose \(b>0\) so small that \(b\sqrt2 H<2\pi\) and
\[
C_b=\pi\left(\frac1b+\frac1{b\sqrt2}\right)>(1+2\cosh(aH))H.
\]
The cosine series \(\sum_{n\ge1}(\cos(nu)-1)/n^2=-\pi|u|/2+u^2/4\) for \(|u|\le2\pi\) follows by integrating the Fourier series of the periodic sawtooth, or by computing its coefficients by parts. Applying it to the two lattices, with both signs and their exact inverse-square weights, gives \(g_0(t)=-C_b|t|+t^2\) on \([-H,H]\).

For any finite distinct grid of diameter at most \(H\) and zero-sum vector \(u\), let \(F(x)=\sum_i u_i {\bf1}_{[t_i,\infty)}(x)\). It is supported on the interval spanned by the grid, and \(F'=\sum_i u_i\delta_{t_i}\) in distributions. Put \(Q_k(u)=\sum_{i,j}\bar u_i u_j k(t_i-t_j)\). Integration by parts in both variables gives
\[
Q_{-|t|}(u)=2\|F\|_2^2,\qquad
Q_{t^2}(u)=-2\left|\int F(x)\,dx\right|^2.
\]
For \(q_T\), cancellation of the squared frequency with the inverse-square denominator gives \(q_T''(t)=-4\operatorname{Re}\cos((T+ia)t)\). Thus \(\sup_{[-H,H]}|q_T''|\le4\cosh(aH)\), uniformly in \(T\). Integrating twice and applying Cauchy–Schwarz gives \(|Q_{q_T}(u)|\le4H\cosh(aH)\|F\|_2^2\). Hence
\[
Q_{g_T}(u)\ge \bigl(2C_b-2H-4H\cosh(aH)\bigr)\|F\|_2^2.
\]
For distinct locations \(F\ne0\) if \(u\ne0\). The inequality covers all such grids and all \(T>a\), and the preceding Schur proof gives positive definiteness in the kernel sense for every \(c>0\). In particular two-point grids give strict negativity at every nonzero time of magnitude at most \(H\). Taking \(T\) beyond any prescribed zero height retains the remote quartet. A much later two-point grid fails, as required by the transform proof.

## Cusp and the compact-group law

For \(0<t<\log 2\), (1.5) has no prime contribution. The exponential elementary term is \(O(t^2)\) and the digamma term is linear. With \(a_0=1/4\) the derivative of the Lerch term is
\[
-\tfrac12 e^{-2a_0t}\sum_{n\ge0}\frac{e^{-2nt}}{n+a_0}.
\]
Subtract the series with denominator \(n+1\) inside the sum. The difference tends by absolute summability to \(-\psi(a_0)-\gamma_{\mathrm E}\), and the comparison series is \(-e^{2t}\log(1-e^{-2t})\). Consequently the differentiated term equals
\[
-\tfrac12\log(1/t)+\tfrac12(\log2+\psi(a_0)+\gamma_{\mathrm E})+o(1).
\]
Integrate from zero and include the other terms in (1.5). In particular the digamma constant cancels, giving the slightly sharper even expansion
\[
g_\zeta(t)=-\tfrac12|t|\log(1/|t|)
+\tfrac12(\log(2\pi)+\gamma_{\mathrm E}-1)|t|+o(|t|).
\]
If \(e^{g_\zeta}\) is a characteristic function, \(1-\operatorname{Re}e^{g_\zeta(t)}\sim \tfrac12 |t|\log(1/|t|)\). The pointwise inequality \(1-\cos v\le |v|\) implies a finite absolute first moment would bound this by \(|t|\mathbb E|X|\). Thus \(\mathbb E|X|=\infty\), and the second moment is infinite as well. Symmetry leaves no finite ordinary mean even though a symmetric principal value could be zero. The conclusion also holds for every positive real power which is a characteristic function. [Primary text, (1.5), (3.2)](https://arxiv.org/pdf/2306.08317v1)

On the compact prime torus, the product Poisson law has Fourier coefficient \(f(k)=\prod_p p^{-|k_p|/2}\) for finitely supported integer vectors \(k\). For each \(c>0\), replacing each Poisson radius by \(p^{-c/2}\) gives \(f(k)^c\), hence convolution roots in the same compact group. Map \(k\) to the ordinary real frequency \(\sum k_p\log p\), injectively by unique prime factorization. For \(k\) representing \((n+1)/n\), the corresponding frequencies tend to \(0\), but \(f(k)^c=(n(n+1))^{-c/2}\to0\), whereas \(f(0)^c=1\). Ordinary real-line characteristic functions are continuous at zero. This group mismatch is independent of the separate mismatch between derivative-weighted high-tail laws and the full multiplicity-weighted zero measure. [Prime-torus calculation](director_hlz_prime_torus_round9.md)

The verified scope is an obstruction to inferences from finite-grid positivity, even full positivity across every grid of one bounded diameter, together with the stated analytic symmetries. A proposed arithmetic extension would need a mechanism that propagates bounded-time inequalities to all times or supplies direct eventual sign or subexponential control in (1.5).
