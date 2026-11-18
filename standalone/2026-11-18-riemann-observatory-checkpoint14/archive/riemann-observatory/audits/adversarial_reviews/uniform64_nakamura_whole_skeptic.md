# Whole-work independent audit of Nakamura–Suzuki, arXiv:2306.08317v1

18 November 2026. PAPER-SM63-POS-040. I read the five pages in full, including the introduction's probability and zeta context, both theorems, both lemmas, the proof of the converse, all three appendix transforms, acknowledgments, and references. I reconstructed the main mathematical implications independently. The two principal theorems hold at this checked scope. A printed half-plane condition on one individual-zero integral is missing the convergence condition for its constant term; the lemma and the appendix use a larger half-plane where both terms converge. No promotion is made here.

## Source and version

The current arXiv history lists only v1, submitted 14 June 2023, and the PDF footer says “Version of June 16, 2023.” The current downloaded PDF is byte-identical to the cached five-page source, SHA-256 756288c39bfd743f08f24b1e5074bb8a4adbe8a959d42edd763af07678801830. Crossref identifies the journal work as *Statistics & Probability Letters* 201, article 109889, DOI 10.1016/j.spl.2023.109889. The publisher VOR, accepted manuscript, and text-mining endpoints tried during this audit returned HTTP 403, so I did not compare the journal text. The exact DOI record carries no correction/update relation, and the title-plus-corrigendum Crossref query did not find one. These checks do not establish the absence of a later privately circulated correction. Suzuki's separately documented signed-time correction to the L²-valued screw line concerns different source statements. The present scalar exponent is explicitly extended by evenness and its proof needs only the positive \(t\) transforms. [Checked PDF](../../sources/suzuki_model63_positivity/suzuki_2306_candidate.pdf) · [arXiv history](https://arxiv.org/abs/2306.08317) · [Journal DOI](https://doi.org/10.1016/j.spl.2023.109889) · [Separate signed-time correction](director_suzuki_correction_round8.md)

## Section 1: input conventions, arithmetic exponent, and antecedents

The completion in (1.1) is \(\xi(s)=s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s)/2\). The factors cancel the simple zeta pole at 1 and the gamma pole at 0, and the trivial zeros cancel the remaining gamma poles. The functional equation and real coefficients give \(\xi(1-s)=\xi(s)\) and \(\xi(\bar s)=\overline{\xi(s)}\). The nontrivial-zero strip gives \(|\Im \gamma|\le1/2\) in \(E(z)=\xi(1/2-iz)\). The characterizations in the introduction therefore reduce to the same RH statement. The basic completion, functional equation and order-one facts are as in Titchmarsh (2.1.12)–(2.1.15) and Theorem 2.12. The alternating eta Dirichlet series is strictly positive at every real \(\sigma>0\) by pairing successive terms. Thus \(\zeta(\sigma)<0\) for \(0<\sigma<1\), and \(s(s-1)\) then gives positive \(\xi(\sigma)\). For \(\sigma>1\) all contributing real factors are positive, and \(\xi(1)=1/2\) by the limit. This proves the nonvanishing at \(1/2\) used in the zero sums and on the positive real axis used in the converse. [Titchmarsh, §2.1 and §2.12](../../sources/equivalence_round2/titchmarsh1986.pdf)

For the \(e^{itx}\) convention, convolution multiplies characteristic functions. The definition of infinite divisibility is consistent with the Lévy–Khintchine normalization (1.2)–(1.3), with the bounded truncation \(\lambda/(1+\lambda^2)\), nonnegative \(a\), and positive Lévy measure putting no mass at zero. To drop the compensation term in (1.4), the added hypothesis makes \(\int|\lambda/(1+\lambda^2)|\,\nu(d\lambda)\) finite: on \(|\lambda|\le1\) use the small-jump first absolute moment and on the complement \( \nu \) is finite by (1.3). The exact drift is \(b'=b-\int \lambda/(1+\lambda^2)\,\nu(d\lambda)\). For the symmetric measure of Theorem 1.2 this integral vanishes absolutely. The proof below does not infer a finite first moment of the full law from this truncation hypothesis.

On \(t\ge0\), the prime term of (1.5) is locally a finite sum of continuous positive-part functions \((t-\log n)_+\), with \(\Lambda(1)=0\). The Lerch series is uniformly convergent down to \(t=0\), with coefficients bounded by \((n+1/4)^{-2}\); the \(s=2\) value at \(z=1\) is therefore well defined. The exponential, prime, digamma and Lerch terms all give zero at \(t=0\). This establishes a real continuous even arithmetic exponent after reflection. The matching zero-side formula (1.7) is proved independently in the appendix check below, so the main proof does not need to import the antecedent equality. In reference [8] Suzuki uses \(\Psi=-g_\zeta\): its displayed constant \(C=\pi^2+8G\) is \(\Phi(1,2,1/4)\) by splitting the odd reciprocal-square sum modulo 4. Its Fourier transform has the opposite sign to (2.2), and Theorem 1.1(2) likewise has \(1-e^{i\gamma t}\) in place of \(e^{-i\gamma t}-1\). Reflecting the zero set accounts for the exponent sign inside the exponential. [Suzuki, arXiv:2206.03682v4, (1.1) and Theorem 1.1](../../sources/effective_cluster62_operator2/suzuki_aspects.pdf)

The introductory example \(\zeta(\sigma+it)/\zeta(\sigma)\), \(\sigma>1\), is a characteristic function by normalizing the masses \(n^{-\sigma}\) at \(-\log n\). Expanding the absolutely convergent Euler-product logarithm gives the finite positive measure \(\sum_{p,r\ge1}p^{-r\sigma}\delta_{-r\log p}/r\), exactly as printed. For nonnegative completely multiplicative \(c(n)\) at a real \(\sigma\) where \(\sum c(n)n^{-\sigma}\) converges, each \(c(p)p^{-\sigma}<1\), and normalization of the associated Euler product gives the same formula with weights \(c(p)^rp^{-r\sigma}/r\). The convergence of the product logarithm follows from convergence of the nonnegative Euler series. This verifies the mathematical content of the claimed generalization on its normalization domain. Reference [6], Nakamura’s Theorem 1.2, states the claimed RH equivalent for all \(1/2<\sigma<1\). Its signed quasi-Lévy representation is defined by allowing \(a\) real and a signed \(\nu\) with \(\nu(\{0\})=0\), without requiring the usual total-variation integrability condition. This is a separate signed-law criterion, not the main paper's finite positive Lévy measure. [Lin–Hu bibliographic record](https://doi.org/10.2307/3318543) · [Nakamura, Theorem 1.2](https://arxiv.org/pdf/1504.03438)

## Section 2: zero series and both implications

For a compact real time interval \(|t|\le K\), \(|e^{-i\gamma t}-1|\le e^{K/2}+1\) by the strip. Since \(E\) is order one, its zero set with multiplicities has \(\sum_\gamma m_\gamma|\gamma|^{-\alpha}<\infty\) for any \(\alpha>1\), for example by the order-one Jensen counting bound \(O_\epsilon(r^{1+\epsilon})\) and dyadic summation. There is no zero at \(\gamma=0\). This proves Lemma 2.1. Symmetry under \(\gamma\mapsto-\gamma\) gives evenness; reality then uses also \(\gamma\mapsto\bar\gamma\) (equivalently, \(\gamma\mapsto-\bar\gamma\)), following from the real functional equation data. These absolute convergences justify the index substitutions. The scalar evenness is distinct from any convention for an L²-valued signed-time path.

Assume RH. Every \(\gamma\) is real, so the masses \(m_\gamma/\gamma^2\) are positive and finite in total, at \(-\gamma\), with no atom at zero. This checks all Lévy hypotheses, including the small-jump moment bound, regardless of multiplicities. More directly, writing \(\lambda=\nu_\zeta(\mathbb R)\), the probability measure
\[
 e^{-\lambda}\sum_{r\ge0}\frac{\nu_\zeta^{*r}}{r!},\qquad
 \nu_\zeta^{*0}=\delta_0,
\]
is well defined by total mass and has characteristic function \(\exp \int(e^{itx}-1)\nu_\zeta(dx)\). Replacing \(\nu_\zeta\) by \(\nu_\zeta/n\) gives the \(n\)-fold convolution root. Equation (1.7) therefore proves both the forward implication and the precise compound Poisson assertion, with \(a=b'=0\) in (1.4). Finiteness of the intensity measure is the relevant assertion.

For Lemma 2.2, write the Hadamard product \(E(z)=e^{A+Bz}\prod [(1-z/\gamma)e^{z/\gamma}]^{m_\gamma}\). The logarithmic derivative series is normally convergent on compacta away from the zeros because \((z-\gamma)^{-1}+\gamma^{-1}=z/[\gamma(z-\gamma)]\). At \(z=0\) the series vanishes and the evenness of \(E\) gives \(B=0\). With \(s=1/2-iz\), the derivative is \((\xi'/\xi)(s)=iE'(z)/E(z)\), giving the sign of (2.3). Direct integration for one zero yields
\[
 \frac{1}{\gamma^2}\int_0^\infty (e^{-i\gamma t}-1)e^{izt}\,dt
 =\frac{i}{\gamma^2}\left(\frac1{z-\gamma}-\frac1z\right)
 =\frac{i}{z^2}\left(\frac1{z-\gamma}+\frac1\gamma\right).
\]
The literal condition on p. 4 for this individual integral is \(\Im z>\Im\gamma\). It needs \(\Im z>\max(0,\Im\gamma)\) because the second exponential is \(e^{izt}\). For any hypothetical zero with \(\Im\gamma<0\), taking \(\Im z=(\Im\gamma)/2\) makes the first exponential decay while the second grows. The stated Lemma 2.2 assumes \(\Im z>1/2\), which already excludes this case. On that half-plane the uniform majorant
\[
 \left(\sum_\gamma m_\gamma|\gamma|^{-2}\right)(e^{t/2}+1)e^{-t\Im z}
\]
is integrable for \(t\ge0\). This gives the needed interchange on the half-line explicitly; compact uniform convergence from Lemma 2.1 alone would not suffice. The summed identity is (2.2).

For the converse, any characteristic function equal to the positive real-valued \(e^{g_\zeta}\) has \(g_\zeta\le0\) because its modulus is at most 1. Infinite divisibility is unused in this direction. The cosine representation asserted in the paper follows by the evenness of the characteristic function, though the modulus bound suffices. Set \(h(t)=-g_\zeta(t)\ge0\) for \(t\ge0\). Its Laplace integral has abscissa of convergence \(b\le1/2\), allowing \(b=-\infty\). Absolute convergence and holomorphy on \(\Re p>b\) follow by domination with a smaller real exponent still above \(b\), including differentiation by powers of \(t\). The cited fixed-sign singularity theorem can be proved directly here. If \(b\) is finite and the transform continues holomorphically to a disk about \(b\), choose a real \(p_0>b\) sufficiently close to \(b\) and \(r>p_0-b\) so the Taylor series at \(p_0\) converges at \(p_0-r<b\). Its terms in that direction are
\[
 \frac{r^j}{j!}\int_0^\infty t^j h(t)e^{-p_0 t}\,dt\ge0.
\]
By monotone convergence the sum of this convergent series is \(\int h(t)e^{-(p_0-r)t}dt\), contradicting the definition of \(b\). This uses the fixed sign on the integration half-line. Mere continuity on the positive imaginary axis would not give the required holomorphic extension.

If \(b>0\), write \(F(z)=\int_0^\infty g_\zeta(t)e^{izt}dt\) for \(\Im z>b\). From (2.2) the analytic identity \(z^2E(z)F(z)=iE'(z)\) holds there by the identity theorem. Since \(E(ib)=\xi(1/2+b)\ne0\) and \(b>0\), \(iE'/(z^2E)\) is holomorphic near \(ib\), giving a continuation of \(F\) and contradicting the fixed-sign result. Hence \(b\le0\) or \(b=-\infty\), and \(F\) is holomorphic for \(\Im z>0\). The same product identity now holds throughout that half-plane. Any zero \(\gamma\) there of order \(m\ge1\) would make the right side vanish to order \(m-1\) and the left to order at least \(m\), impossible. Reflection by \(E(-z)=E(z)\) rules out the lower half-plane. This completes the converse, handles arbitrary zero multiplicity, and confirms the stronger implication from a characteristic function alone.

## Section 3: appendix reconstruction

Let \(p=-iz\), so \(s=1/2+p\) and \(z^2=-p^2\). The logarithmic derivative of (1.1) is
\[
 \frac{\xi'(s)}{\xi(s)}
 =\frac1{s-1}+\frac1s-\tfrac12\log\pi+\tfrac12\psi(s/2)
   -\sum_{n\ge2}\Lambda(n)n^{-s}.
\]
The Euler-product differentiation is absolutely convergent for \(\Re s>1\), since \(\Lambda(n)\le\log n\). Term by term the Laplace transforms of (1.5) are as follows.

- For \(\Re p>1/2\), the elementary exponential part gives \(-4[(p-1/2)^{-1}+(p+1/2)^{-1}-2p^{-1}]\). This equals \(z^{-2}[(s-1)^{-1}+s^{-1}]\) by combining denominators.
- The transform of \(t\) is \(p^{-2}=-z^{-2}\) for \(\Re p>0\). Thus the explicit linear digamma term contributes \((\psi(1/4)-\log\pi)/(2z^2)\).
- With \(u=t-\log n\), the transform of \((t-\log n)_+/\sqrt n\) is \(n^{-s}/p^2=-n^{-s}/z^2\) for \(\Re p>0\). Including \(\Lambda(n)\), the interchange for \(\Re p>1/2\) is bounded in absolute value by \((\Re p)^{-2}\sum_{n\ge2}\Lambda(n)n^{-(\Re p+1/2)}\). This proves the printed prime-term sign, domain and interchange.
- Put \(v=n+1/4\). The Lerch difference in (1.5) is \(\tfrac14\sum_{n\ge0}(e^{-2vt}-1)/v^2\). Its half-line transform and termwise summation are absolutely justified for \(\Re p>0\) by \(\sum v^{-2}/(4\Re p)\). One term transforms to
\[
 \frac{1}{4v^2}\left(\frac1{p+2v}-\frac1p\right)
 =-\frac{1}{2p\,v(p+2v)}
 =-\frac1{2z^2}\left(\frac1{s/2+n}-\frac1{1/4+n}\right).
\]
The digamma series follows by logarithmic differentiation of the Euler product for \(1/\Gamma\): \(\psi(w)=-\gamma_{\rm E}+\sum_{n\ge0}((n+1)^{-1}-(n+w)^{-1})\), with local normal convergence away from poles. Subtract at \(s/2\) and \(1/4\) to obtain \( [\psi(s/2)-\psi(1/4)]/(2z^2)\), proving (3.1). The real-part condition ensures both digamma arguments stay in their right half-plane. The subtraction removes \(\gamma_{\rm E}\).

Combining the four transforms leaves the stated \(z^{-2}(\xi'/\xi)(1/2-iz)\) for \(\Im z>1/2\). Fix any \(y>1/2\). Both candidates for \(g_\zeta\), multiplied by \(e^{-yt}\mathbf1_{t\ge0}\), belong to \(L^1(\mathbb R)\), by the zero-side majorant and the four arithmetic estimates. Their ordinary Fourier transforms agree at every real frequency by the line \(z=x+iy\). Fourier injectivity gives equality almost everywhere, and continuity upgrades it to pointwise equality for \(t\ge0\), including zero. Both sides are even, so this proves (1.7) on the stated full real line. It also explains why the appendix does not assume RH, zero simplicity, a bilateral integral, or any conditional evaluation of the signed series.

## Coverage ledger

| Source location | Mathematical assertions checked | Scope |
|---|---|---|
| p. 1, abstract, §1, (1.1)–(1.4) | Completion, RH coordinate change, convolution definition, Lévy truncation and drift sign | Read fully. General Lévy–Khintchine theorem is a standard cited input; its needed finite-measure direction is proved directly above. |
| p. 2, (1.5)–(1.7), Theorems 1.1–1.2, historical discussion | Well-defined exponent, real/even convention, exact jump measure, older zeta compound Poisson law and signed-law distinction | Read fully. Main assertions checked in §§2–3; antecedent statements sourced or derived as detailed below. |
| p. 3, start of §2, Lemma 2.1, (2.1), forward implication, start of Lemma 2.2, (2.2)–(2.3) | Order-one summability, zero exclusion at 0, two symmetries, positive Lévy measure and Hadamard factors | Read fully and reconstructed. |
| p. 4, remainder of Lemma 2.2, (2.4), converse, start of appendix | Individual integral and normal convergence, half-line domination, fixed-sign abscissa, positive-axis nonvanishing, identity theorem, elementary and prime transforms | Read fully and reconstructed, with the narrower individual-integral domain explicitly identified. |
| p. 5, appendix (3.1)–(3.2), end matter | Gamma/Lerch substitution and sign, convergence, Fourier uniqueness, acknowledgments, full reference list | Read fully and reconstructed. Acknowledgments carry no mathematical premise. |

Reference roles checked individually:

1. Biane–Pitman–Yor is a contextual reference on theta, zeta and probability examples. Its bibliographic identity is verified. No theorem from it is used here. [DOI](https://doi.org/10.1090/S0273-0979-01-00912-0)
2. Gnedenko–Kolmogorov, Example 17.6, is cited for the classical zeta law. The exact Euler-product calculation yields the cited result independently; the book example itself was not re-read.
3. Lagarias–Rains is contextual for the probabilistic zeta literature. Its identity is verified, with no proof dependency in the article. [DOI](https://doi.org/10.5802/aif.1939)
4. Lebedev (1.3.16) supplies the digamma expansion. The exact formula and its convergence were reconstructed from the gamma product; the original book page was not re-read.
5. Lin–Hu, Theorem 2, is cited for completely multiplicative coefficients. The exact Euler-product extension on the convergent domain was independently derived above. Bibliographic identity was verified; its original theorem page was not obtained in this audit. [DOI](https://doi.org/10.2307/3318543)
6. Nakamura's signed-law prior result was checked against the primary text, definition and Theorem 1.2. Its role is contextual. [Primary PDF](https://arxiv.org/pdf/1504.03438)
7. Sato, Theorem 8.1, Remark 8.4 and (8.7), is cited for Lévy–Khintchine with the stated normalization. The finite-intensity special case used here was independently constructed, and the truncation change checked algebraically. I did not re-audit Sato's whole general theorem.
8. Suzuki, Theorem 1.1(2), was checked against primary v4, including the opposite sign convention and equality \(\Phi(1,2,1/4)=C\). The current paper nonetheless reproves the equality in its appendix. [Primary PDF](../../sources/effective_cluster62_operator2/suzuki_aspects.pdf)
9. Titchmarsh (1.1.8), Theorems 2.1 and 2.12, and (2.1.13) were checked as standard inputs at their relevant passages. Eta positivity and the application to \(\xi\) were independently spelled out. [Primary reference](../../sources/equivalence_round2/titchmarsh1986.pdf)
10. Widder, Chapter II Theorem 5b, is used for a fixed-sign Laplace singularity. The required local statement was independently proved by the Taylor/monotone convergence argument above; the original Widder page was not re-read.

This is whole-work coverage of the checked arXiv article and an independent reconstruction of its mathematical argument. It is not whole-work coverage of the references or an assertion about unseen publisher text.
