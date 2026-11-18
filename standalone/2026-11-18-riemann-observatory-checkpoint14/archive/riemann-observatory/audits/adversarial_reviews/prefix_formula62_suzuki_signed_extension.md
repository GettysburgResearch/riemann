# Suzuki’s signed screw line and the author’s erratum

I compared arXiv:2209.04658v3, pp. 2, 4 and §§3.2–3.4, with arXiv:2301.00421v3 and the Cambridge publisher text of the merged article. I read the author-linked one-page erratum, including a visual check of the conjugation bar in item (2). The [author bibliography](https://sites.google.com/view/msuzuki/home/articles) identifies the results as incorporated into the merged article. The DOI printed in the erratum, [10.4153/S0008414X25101739](https://doi.org/10.4153/S0008414X25101739), identifies the **article** to be corrected. The publisher’s web text inspected for this audit still displays the original even definitions. Local copies are `sources/effective_cluster62_operator2/suzuki_screw_line.pdf`, `sources/effective_cluster62_operator2/suzuki_weil_merged.pdf`, and `sources/witness62_suzuki_signed/cjm_errata.pdf`. This is a scoped verification of an existing author correction.

## The sign check without RH

Write \(f^\#(z)=\overline{f(\bar z)}\). Let \(\Gamma\) be the distinct zeros of \(A(z)=\xi(1/2-iz)\) with multiplicities \(m_\gamma\). The symmetries \(\gamma\mapsto-\gamma,\bar\gamma\), the strip \(|\Im\gamma|<1/2\), and \(\sum m_\gamma/|\gamma|^2<\infty\) are unconditional. The zero \(\gamma=0\) is absent since the eta series gives \(\zeta(1/2)\ne0\). For either sign convention \(\sigma=\pm1\), define
\[
P_t^\sigma(z)=\sum_{\gamma\in\Gamma}m_\gamma
 \frac{e^{\sigma i\gamma t}-1}{\gamma\(z-\gamma\)},\qquad t\in\mathbb R.
\]
Convergence is absolute locally uniformly off \(\Gamma\), uniformly for \(t\) in compact intervals. Conjugate and relabel \(\gamma\mapsto\bar\gamma\), or evaluate at \(-z\) and relabel \(\gamma\mapsto-\gamma\), to obtain
\[
P_{-t}^\sigma=\(P_t^\sigma\)^\#=P_t^\sigma\(-\,\cdot\).
\]
The stand-alone preprint uses \(\sigma=+1\) in (2.2) and (S_t=B P_t^+), where \(B=i(1+\Theta)/(2\sqrt\pi)\). The merged article uses \(\sigma=-1\) in (3.2). The positive-time explicit-formula calculations, Proposition 2.1 and Proposition 3.1 respectively, identify the two representations there. Consequently the conjugate continuation supplies the negative-time prime-based branch directly from positive time. This avoids inserting negative time into the Hurwitz–Lerch expression.

In the merged article, author erratum items (1)–(3) give \(\mathfrak S_t=-i(1+\Theta^\#)\mathfrak P_t/2\) for all real \(t\), \(\mathfrak P_{-a}=\mathfrak P_a^\#\) for \(a>0\), and the same signed zero series (3.2) for all real (t). Item (4) changes an inequality constant on p. 14 from \(\pi\) to \(4\pi\). Independently, direct conjugation of (3.5) gives
\[
\sqrt{\pi m_\gamma}\,F_\gamma^\#(z)
=\frac{-i\(1+\Theta^\#(z)\)m_\gamma}{2\(z-\bar\gamma\)}.
\]
Relabeling by conjugation verifies the unconditional signed expansion (3.6) with both corrected signs, including when zeros are off the line.

In either normalization, the prefactor \(B_*\) satisfies \(B_*/B_*^\#=-\Theta\) in the stand-alone version and \(-\Theta^\#\) in the merged version. On the real axis these ratios are unimodular a.e. Thus positive-time (L^2) bounds transfer isometrically to negative time. The positive-time locally uniform bound and the compact-time continuity of the meromorphic series away from poles give strong (L^2) measurability by approximation on bounded real intervals avoiding the pole set. This suffices for the Bochner integrals against compact smooth tests. The zero-value identity at \(z=0\) is unaffected by the signed time extension. The large-imaginary-axis limit in §4 of the stand-alone version is proved there for positive time only.

## Under RH and the converse

Under RH, use the model-space orthonormal basis \(F_\gamma\) of Proposition 4.1 of the merged article. The corrected integrated operator uses \(F_\gamma\), whereas the corrected pointwise screw line uses \(F_\gamma^\#\). The latter basis is orthonormal in \(\mathcal K(\Theta)^\#\) by antiunitarity of conjugation. The pointwise line is asserted into \(L^2(\mathbb R)\), which suffices for Theorem 4.2. Its increment coefficients are
\[
\sqrt{\pi m_\gamma}\,e^{-i\gamma v}\(e^{-i\gamma t}-1\)/\gamma.
\]
Their squared absolute values sum by comparison with \(4\pi\sum m_\gamma/\gamma^2\), uniformly in real times. In the inner product the \(v\)-phases cancel. Pairing \(\pm\gamma\) turns the resulting sum divided by \(\pi\) into \(G_g(t,u)=g(t-u)-g(t)-g(u)\). The stand-alone normalization omits the factor \(\pi\). For the merged operator, separate from the pointwise line,
\[
\widehat P_\varphi=\int_{\mathbb R}\mathfrak S_t^\#\,\varphi(t)dt
 =\sum_\gamma \sqrt{\pi m_\gamma}
 \frac{\widehat\varphi(\gamma)-\widehat\varphi(0)}{\gamma}F_\gamma
\]
with \(\widehat\varphi(x)=\int\varphi(t)e^{ixt}dt\). The interchange follows from uniform square-summable domination. Parseval proves (4.8) under RH. Conversely equality on zero-mean tests forces positivity of the screw form there. Every such test is a derivative of a compact smooth primitive, and the derivative identity with the Weil form and Weil’s criterion give RH. Corollary 4.3 keeps its original nonnegative-time quantifier and follows from the diagonal identity and the source’s eventual nonnegativity criterion.

One direct density check for the corrected operator uses \(D=i\partial_t\), so \(\widehat{D\psi}(\gamma)=\gamma\widehat\psi(\gamma)\). If \(\sum c_\gamma F_\gamma\) is perpendicular to all images \(\widehat P_{D\psi}\), then the tempered distribution \(\sum_\gamma\sqrt{m_\gamma}\,\bar c_\gamma\delta_\gamma\) annihilates all Fourier transforms of compact smooth \(\psi\). Indeed the distribution is tempered because \(\sum \sqrt{m_\gamma}|c_\gamma|/(1+|\gamma|)<\infty\) by Cauchy–Schwarz. Fourier injectivity and discreteness imply \(c_\gamma=0\) for each \\(\gamma\\). Hence the corrected image is dense in the model space under RH. This argument uses the RH basis and says nothing about unconditional model-space density.

## Scope of the original even convention

The original even prescription agrees with the signed one for nonnegative time. If read literally on the full real line, it forces \(\langle S_t,S_{-t}\rangle=\langle S_t,S_t\rangle\). The screw kernel requires their difference to be \(g(2t)\), which is nonzero for some \(t\) under RH by the positive sum for \(-g(2t)\). Likewise an odd test \(\varphi=\psi'\), with even nonnegative nonzero \(\psi\) supported in \(|t|<\pi/(2|\gamma_0|)\) for a real nonzero zero ordinate, integrates the even family to zero. Its screw form is positive under RH since \(\widehat\varphi(\gamma_0)=-i\gamma_0\int\psi(t)\cos(\gamma_0 t)dt\ne0\). This localizes the mismatch to the obsolete bilateral convention.

A half-line formulation already suffices for the equivalence. Under RH the increment proof works whenever all evaluation times are nonnegative. For the converse every zero-mean compact smooth test can be translated into the positive half-line. Its screw form is translation invariant because the one-variable terms integrate to zero. Thus equality restricted to such half-line tests still yields Weil positivity, and the author’s signed correction restores the stated full-line formulation.
