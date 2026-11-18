# Suzuki’s screw line and the signed time correction

I checked arXiv:2209.04658v3 (May 17, 2023, nine pages, SHA-256 022d42869c10420f81c0f09ccf49c5e0a037a2fd50c35392d4205db61683db42), particularly p. 2 (1.5)–(1.7), p. 4 (2.2), p. 7 (3.2)–(3.5), and pp. 8–9 (3.6) and (4.1)–(4.2). The two earlier arXiv versions also display an even extension in the corresponding definitions. Suzuki has already issued a signed-time correction for the later journal work that incorporates these results. This audit independently checks the old obstruction and maps it to that author correction. [Pinned preprint](https://arxiv.org/pdf/2209.04658v3) [Author’s publication list](https://sites.google.com/view/msuzuki/home/articles)

## Witness against the literal even extension

In v3, the prime-side formula (1.6) and the zero sum (2.2) are both defined for \(t\ge0\). The text extends \(S_t\) and the corresponding zero-side \(P_t\) evenly in \(t\). For an even \(S_t\) with \(S_0=0\), the claim (3.3) at basepoint \(u=0\), \(t=a>0\), \(s=-a\) requires
\[
 \|S_a\|_2^2=G_g(a,-a)=g(2a)-2g(a).
\]
But the time-\(a\) diagonal already requires \(\|S_a\|_2^2=-2g(a)\). These conflict whenever \(g(2a)\ne0\). Equivalently, evenness gives \(S_a-S_{-a}=0\), while the claimed increment norm is \(-2g(2a)\). Under the theorem's RH assumption, choose any nonzero real ordinate \(\gamma_0\) of a zeta zero and let \(a=\pi/(2|\gamma_0|)\). Equation (3.5) shows \(-g(2a)\ge2m_{\gamma_0}/|\gamma_0|^2>0\). Existence of a nontrivial zero suffices. This is a contradiction within the theorem's assumed setting and requires no numerical zero enclosure.

The same issue affects the forward direction of the printed bilateral equality in Theorem 1.2. Choose an even nonnegative compact smooth unit-mass bump \(h_\varepsilon\) supported in \([-\varepsilon,\varepsilon]\) and set \(\phi_\varepsilon(t)=h_\varepsilon(t-a)-h_\varepsilon(t+a)\). It is odd and has integral zero. For the printed even \(S_t\), the integral defining \(\widehat P_{\phi_\varepsilon}\) is zero. The continuous kernel gives
\[
 \lim_{\varepsilon\downarrow0}\langle\phi_\varepsilon,\phi_\varepsilon\rangle_{G_g}
  =G_g(a,a)+G_g(-a,-a)-2G_g(a,-a)=-2g(2a)>0.
\]
The zero-mean domain therefore includes a witness. The literal even extension cannot be justified by pairing ordinates. Restricting *times* to nonnegative values would avoid this witness but would change the stated bilateral theorem and test domain.

## Signed extension and its scope

In the preprint’s convention, use the formula
\[
 P_t(z)=\sum_{\gamma\in\Gamma}m_\gamma
        \frac{e^{i\gamma t}-1}{\gamma(z-\gamma)}
 \quad(t\in\mathbb R)
\]
for signed \(t\). Absolute local convergence off the poles follows from the strip bound \(|\Im\gamma|<1/2\) and \(\sum m_\gamma|\gamma|^{-2}<\infty\). The symmetries \(\Gamma=-\Gamma=\bar\Gamma\), including multiplicity, yield for \(a>0\)
\[
 P_{-a}(z)=P_a(-z)=\overline{P_a(\bar z)}.
\]
Thus the signed extension can be made entirely through the nonnegative-time prime-side formula by Schwarz reflection of \(P_a\). It leaves the written nonnegative-time formula intact. On the real axis the multiplier \(1+\Theta\) and its reflected counterpart have the same modulus because \(|\Theta|=1\) off a discrete set. Hence the unconditional \(L^2\) membership from Proposition 1.1 and the compact-time norm majorants also apply to the signed extension; no new prime-side formula for negative \(t\) is required.

Under RH the actual coefficients in the orthonormal expansion (3.2) are now signed. In \(S_{t+u}-S_u\) the coefficient at \(\gamma\) is \(\sqrt{m_\gamma}\,e^{i\gamma u}(e^{i\gamma t}-1)/\gamma\). Taking the inner product cancels the basepoint phase and gives (3.3). Integrating the signed expansion against \(\phi\) gives the Fourier transform difference \(\widehat\phi(\gamma)-\widehat\phi(0)\) in (3.6), so the forward equality in Theorem 1.2 is recovered. The converse uses nonnegativity of the norm and Weil's form on the full derivative test domain and is independent of the time-extension choice. The one-sided norm criterion in Corollary 1.1 uses only \(t\ge t_0\ge0\) and survives directly, since the norm calculation at positive times already follows from (2.2). At \(z=0\), (4.1) is unchanged because the corrected reflection and the even sum for \(g(t)\) agree there. I only use (4.2) for positive time, as in its proof from (1.6). With the literal even extension its left side would be even if read bilaterally, whereas \(-g'\) is odd wherever defined.

## Author erratum in the journal successor

The author's publication list explicitly says that this preprint's results were incorporated into arXiv:2301.00421, *On the Hilbert space derived from the Weil distribution*, published in the Canadian Journal of Mathematics, DOI 10.4153/S0008414X25101739. The inspected journal HTML still shows the even extension below (1.6) and (3.2), while Theorems 4.2 and 4.4 are bilateral. The one-page erratum authored by Suzuki, linked from his publication list, is preserved with SHA-256 9c28b278874eb8242165ac3f8b3ab9ae44365cfba6958a4869e462eb057a1382. The rendered page confirms the bars in item (2). It replaces the p. 4 even line extension by \(\mathfrak P_t(z)=\overline{\mathfrak P_{-t}(\bar z)}\) for negative time. Item (3) defines the journal's signed exponential sum (3.2) for all real \(t\) and deletes the even extension. These items agree with the independent repair, allowing for the journal’s opposite sign in its exponential. Item (1) also corrects a separate overall factor \(i\to-i\) in journal (1.5). The erratum is author-hosted evidence for corrected reading of the journal work. Its existence does not imply the original arXiv file was amended or that the erratum has a separate publisher DOI. [Journal text](https://doi.org/10.4153/S0008414X25101739) [Author’s erratum](https://drive.google.com/file/d/1Gi7cUoqA_izzdsH5lzEL48bl20Lf9c8_/view?usp=sharing)
