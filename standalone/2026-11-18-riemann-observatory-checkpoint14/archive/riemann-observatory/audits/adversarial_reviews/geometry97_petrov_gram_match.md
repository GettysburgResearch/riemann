# Petrov's exact tilted Toeplitz factors for derivative-rooted CUE

The exact Gram in Petrov's formula is positive definite for every real Laplace parameter. It is already different in degree two from the normalized complementary compression that generates \(P_J^{\rm det}\). The extra tail determinant contributes within the valid moment window. The positive-real zero of the polynomial extrapolation is therefore not associated with a failure of Petrov's exact formula. [Petrov, arXiv:2605.24976v1](https://arxiv.org/pdf/2605.24976v1) · [Rooted CUE moment window](director_cue_windows_round13.md) · [Primary-source comparison](geometry95_palm_moment_priority.md)

## Exact finite formula and hypotheses

Fix removed rank \(J\ge1\), write \(m=N-1\), \(n=m+J\), and put
\[
 f_N(w)=-\sum_{aN<k\le bN}\frac{w^k+w^{-k}}{2k}
       =F_+(w)+F_-(w),\qquad \phi=e^{z f_N}.
\]
Here \(w\) is a circle variable and \(z\) is the scalar moment parameter. In Petrov §3.1, (3.3)–(3.7), choose \(\phi_\pm=e^{zF_\pm}\), \(G=1\), and \(Z=e^{H_N z^2/4}\), with \(H_N=\sum 1/k\) over the band. The symbol is smooth, nonvanishing, and of zero winding for all complex \(z\), with \(z f_N\) as the chosen logarithm. Both triangular factors and their inverses are bounded at each finite \(N,z\).

Let \(P=P_m\) be the projection onto the first \(m\) Hardy modes on \(\ell^2(\mathbb Z_{\ge0})\). Identify its range with \(\mathbb C^m\). Use identical row and column tilts \(\theta=(1-w^{-1})^J\), \(\xi=(1-w)^J\). In §4.1, (4.2)–(4.4), this gives
\[
 X=T(\xi)P,\quad \Theta=P T(\theta)=X^*,\quad
 R=X^*T(\phi_+),\quad C=T(\phi_-)X,\quad \Gamma=RC .
\]
The star on \(X\) is legitimate for all \(z\) because this map is independent of \(z\). The \(m\) columns of \(X\) are the free-span basis. Equation (4.6) identifies the tilted matrix with \(X^*T(\phi)X\). Normalize its determinant by \(\det\Gamma(0)=\det(X^*X)>0\). Theorem 4.4 then gives the exact marked statistic transform
\[
 \mathbb E e^{zC_N}
 =e^{-H_N z+H_Nz^2/4}\,
    \frac{\det\Gamma(z)}{\det\Gamma(0)}
    L_{\rm obl}(z),\qquad
 L_{\rm obl}=\det_{\ker R}\!\left(I-\Pi_V K|_{\ker R}\right),
\]
where \(K=H(\mathfrak b)H(\widetilde{\mathfrak c})\) from (3.4), \(\mathfrak b=\phi_-/\phi_+\), \(\mathfrak c=1/\mathfrak b\), \(\widetilde{\mathfrak c}(w)=\mathfrak c(w^{-1})\), and \(\Pi_V=I-C\Gamma^{-1}R\). The factor \(e^{-H_Nz}\) includes the root. The complex-analytic identity holds near \(z=0\) because \(\Gamma(0)\) is invertible. Its oblique determinant can also be taken on the fixed Hardy space as \(\det(I-K\Pi_V)\), by Petrov's block argument (2.6). This gives a fixed-space analytic expression for Taylor comparisons.

For all real \(z\), \(\phi_-=\overline{\phi_+}\) on the circle and \(C=R^*\). The analytic multiplication map \(X\) is injective on \(P\), and \(T(\phi_-)\) has its bounded triangular inverse, so \(C\) is injective. Thus \(\Gamma=C^*C>0\), and \(\Pi_V\) is the orthogonal projection onto \(\ker R=(\operatorname{Ran}C)^\perp\). Also \(\mathfrak c=\overline{\mathfrak b}\) and
\[
 I-K=T(\mathfrak b)T(\mathfrak c)
     =T(\mathfrak b)T(\mathfrak b)^*.
\]
The first equality is the Toeplitz product formula with \(\mathfrak b\mathfrak c=1\). The operator \(T(\mathfrak b)=T(\phi_-)T(\phi_+^{-1})\) is a product of invertible triangular factors. Consequently \(I-K\) is bounded below by a positive constant at each fixed real \(z,N\). Its compression has the same property, so \(L_{\rm obl}(z)>0\) as a trace-class Fredholm determinant. Neither exact factor develops a positive-real zero. The cosine characteristic function is the complex specialization \(z=it\) wherever the chart is defined. At a chart singularity the exact expectation still has its ordinary finite determinant expression.

## Which factor cancels in the coefficient window

Let \(A_n=P_nT(\phi)|_{P_n}\) and let \(U\) be the \(J\) orthonormal columns for its removed span. The ordinary Borodin–Okounkov determinant on the ambient \(n\) modes is
\[
 \det A_n=e^{H_Nz^2/4} L_n(z),\qquad
 L_n=\det_{Q_n H}(I-Q_nK|_{Q_nH}),\qquad Q_n=I-P_n.
\]
Jacobi's complementary-minor identity on \(P_n\) and Petrov's tilted identity on \(P_m\) therefore give the exact quotient near zero
\[
 \frac{\det\Gamma(z)}{\det\Gamma(0)}
 \frac{L_{\rm obl}(z)}{L_n(z)}
 =\det(U^*A_n^{-1}U).
\]
This identity also holds with independent tagged Fourier sources near zero. For a tagged monomial, write \(P_{\rm freq},Q_{\rm freq}\) for its positive and absolute negative frequency totals. In the ordinary tail \((Q_nKQ_n)_{ij}\), each term has the form \(\widehat{\mathfrak b}(i+\ell+1)\widehat{\mathfrak c}(-j-\ell-1)\), with \(i,j\ge n\), \(\ell\ge0\). The first factor requires \(P_{\rm freq}\ge i+\ell+1\), and the second requires \(Q_{\rm freq}\ge j+\ell+1\). Grouping tags cannot relax these inequalities. Thus the ordinary Fredholm tail has no nonconstant coefficient with either total at most \(n\). This remains true in each nonconstant product term of its determinant. In the separate signed-total range \(P_{\rm freq},Q_{\rm freq}\le n\) only \(L_n\) can be replaced by \(1\) in the quotient. The right side is then the exact oriented compression determinant from the two-boundary Neumann argument. After removing its mass \(e^{JH_Nz}\) and passing to the limit, it gives the stated \(P_J^{\rm det}\) through \(r b\le1\). [Borodin–Okounkov §2 Theorem 1](https://arxiv.org/pdf/math/9907165v1) · [Exact compression and continuum polynomial](geometry93_rank_three_barrier.md)

The tilted tail itself contributes already in degree two. Taking the cosine ray and expanding the two Hankel factors gives
\[
 K(z)=z^2\,H(F_+)H(F_+)^*+O(z^3)
\]
in trace norm at each finite \(N\). Only the positive Fourier coefficients of \(\mathfrak b\) and the reflected negative ones of \(\mathfrak c\) enter, and their respective first-order coefficients are \(-F_+\) and \(-\widetilde F_-\). Hence
\[
 [z^2]L_{\rm obl}(z)
 =-\operatorname{Tr}\big[\Pi_{V(0)}H(F_+)H(F_+)^*\big].
\]
When the band is nonempty and \(K_N\le n\), the Hankel operator \(H(F_+)\) is supported on the first \(n\) rows and columns. At zero, \(\Pi_{V(0)}\) restricted to these modes is \(UU^*\). The trace is
\[
 \kappa_{J,N}
 =\sum_{j=0}^{J-1}\|H(F_+)^*U_j\|^2>0.
\]
Indeed \(U_0\) is constant with positive entries, and the nonzero Hankel entries of the cosine ray all have the same negative sign. Its pairing with \(U_0\) gives a nonzero vector. If \(2K_N\le n\), the second Taylor coefficient is inside the moment window, yet the normalized Gram determinant differs from \(e^{-JH_Nz}\det(U^*A_n^{-1}U)\) in that coefficient, by \(+\kappa_{J,N}\). This follows directly from the exact quotient and \(L_{\rm obl}=1-\kappa_{J,N}z^2+O(z^3)\).

For a fixed band with \(0<a<b\le1/2\), this mismatch persists in the limit. The normalized removed columns converge by Riemann summation to the \(u_j\), and
\[
 \kappa_{J,N}\longrightarrow
 \frac14\sum_{j<J}\int_0^b
       \left(\int_0^1
          \frac{{\bf 1}_{a<s+t\le b}}{s+t}u_j(s)\,ds
       \right)^2dt>0 .
\]
The Fourier weights are bounded after scaling on \(a<s+t\le b\); the only integration discontinuities are at the two lines delimiting the band. The constant mode again gives strict positivity. Thus even the limiting quadratic coefficient is a mismatch with the Gram alone. Treating the tilted tail as an ordinary high-index tail would lose precisely this term.

## The optional fixed-tail chart can fail on the real axis

Proposition 4.6 adds the invertibility of \(B=RP|_{PH}\), and Proposition 4.7 uses this chart for a rank bound on the correction to the ordinary \(m\)-tail. Its bound is \(2J\) for the present degree-\(J\) tilts. At zero \(B=P T(\theta)|_{PH}\) is upper triangular with diagonal one, so both propositions apply locally. This chart hypothesis does not follow from positive definiteness of \(\Gamma\) for all real \(z\).

For example take \(N=4\), \(J=2\) and any band selecting only \(k=2\), such as \((a,b)=(0.3,0.6)\). Then \(m=3\), \(\phi_+=e^{-z w^2/4}\) and \(B=T_3((1-w^{-1})^2e^{-zw^2/4})\). Exact coefficient extraction gives
\[
 B=\begin{pmatrix}
 1-z/4&-2&1\\
 z/2&1-z/4&-2\\
 z^2/32-z/4&z/2&1-z/4
 \end{pmatrix},\quad
 \det B=-\frac{z^3+4z^2-64z-128}{128}.
\]
The determinant goes from \(1\) at \(0\) to \(-1\) at \(8\), so the fixed-tail chart is singular at some positive parameter, even though \(\Gamma\), \(L_{\rm obl}\), and the actual finite Laplace transform stay positive. This concerns only the optional chart, with no identification between its singularity and the positive-real zero of the formal extrapolation. At the latter zero the unsupported higher Taylor coefficients, rather than a positivity failure in the exact factorization, account for the difference. The arithmetic application stays within the separate RH-conditional window \(rb<1/2\). [Petrov §4.2, (4.8)–(4.11) and Propositions 4.6–4.7](https://arxiv.org/pdf/2605.24976v1) · [Arithmetic scope](prime79_hlz_formal_moment_obstruction.md)

Source checked: Petrov v1 dated 24 May 2026, retrieved SHA-256 f8b1c3386d49e61e767ae969a02131b509a42af276151ff04492b8be75a79214. The finite three-by-three determinant was checked with exact symbolic coefficients. No corpus promotion or publication-priority conclusion follows from this comparison.
