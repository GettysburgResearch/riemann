# Inumaru–Sugiyama v1 whole-work advocate review

18 November 2026. I read all 30 pages of the pinned arXiv v1, including both moment regimes, both density arguments, Appendix A, footnotes and bibliography. The key fixed-conductor continuous density theorem has a reconstructible proof. Several local notational or endpoint issues can be repaired directly. The paper supplies a continuous comparison statistic and a fixed-twist formula. It gives no extension of the discrete derivative-root law or its long-prime estimate. This is a Level 1 candidate for director adjudication. The cited upstream works were used at their stated interfaces and were not separately whole-work audited here. [Pinned source PDF](../../sources/prime122_frontier_pending/2610.41394.pdf) · [arXiv version history](https://arxiv.org/abs/2610.41394)

## Coverage ledger

| PDF pages | Substantive coverage |
|---|---|
| 1–2 | Scope of prior zeta moments, fixed rational twist, two regimes of Theorem 1.1, coefficients and explicit conductor-dependent errors |
| 3–6 | Fourier convention and off-line zeros, conductors and continuous translated family, Theorems 1.2–1.4, pole at conductor 1, normalization of Gauss sums and gamma factors |
| 6–10 | Lemma 2.1 with principal-character count, AFE source, finite shifted-support estimates in Lemmas 2.3–2.5 |
| 10–17 | Two adaptive AFE cutoffs, nine products, two diagonals, cross-arm oscillation, mean-square estimates for remainder terms, Laurent cancellation at the center, Corollaries 2.6 and 2.12 |
| 17–20 | Normalization in Theorems 3.1 and 3.3 and conductor conditions for denominator estimates |
| 20–25 | Full explicit formula and both proofs, with the prime-square and prime error exponents, triangular correction, and different-character cancellation |
| 26–28 | Unconditional unweighted test support, distinct GRH-dependent support removal, negative-height counting and tail integrability, footnote on Conrey's pole |
| 28–30 | Acknowledgment, references [1]–[38], including method dependencies and distinguishable comparison families, final author affiliations |

The PDF header dates arXiv v1 to 30 October 2026, while the author date on p. 1 is 2 November. The source is 30 pages, SHA-256 70d2a3caf711fab1a5d7926ed099e098ab8e41c99bd3075dddf0a218b7d7e290. Provider-only candidate CAND-AC026DA96A1D / OpenAlex W7225102923.

## Fixed twists and the two diagonal terms

Let \(\chi\) be primitive modulo \(q\), \(m,n\) coprime positive integers at most \(T\), \(T\ge3\), and \(T^{1/2}\le H\le T\). Theorem 1.1 evaluates \(\int_T^{T+H}|L(\sigma+it,\chi)|^2(m/n)^{it}dt\) for one real \(1/2\le\sigma\le1\). For \(\sigma>1/2\) the integrand of the main term is
\[
 \chi(m)\overline{\chi(n)}
 \left[(mn)^{-\sigma}L(2\sigma,\chi_0)
 +(qt/(2\pi))^{1-2\sigma}(mn)^{\sigma-1}L(2-2\sigma,\chi_0)\right].
\]
Thus if either twist integer shares a prime with \(q\), both leading diagonals vanish. The error is
\[
 O\big((qT)^{1-\sigma}mn\log^2(qT)\big)
 +O\big(Hq^{1/2}(qT)^{-\sigma/2}
       ((m/n)^{\sigma/2}+(n/m)^{\sigma/2})\log^2(qT)\big).
\]
Constants are stated as absolute. This is a coefficient estimate with no independent complex shifts.

The proof uses the AFE at \((x_1,y_1)=(\sqrt{qtm/(2\pi n)},\sqrt{qtn/(2\pi m)})\), with the two cutoffs interchanged on the conjugate factor. The first-first product diagonal \(n\nu=m\mu\) reduces to \((\nu,\mu)=(mk,nk)\) and cutoff \(k\le\sqrt{qt/(2\pi mn)}\). The dual-dual diagonal instead gives \((\nu,\mu)=(nk,mk)\), with that same cutoff. Its phase and coefficient again give \(\chi(m)\bar\chi(n)\). Truncating \(L(2\sigma,\chi_0)\) and \(L(2-2\sigma,\chi_0)\) using the principal-character count produces the same cutoff-power term with opposite signs. The off-diagonals are estimated by integrating at frequency \(\log(\mu m/(\nu n))\) or its dual equivalent, with both moving cutoffs converted to a lower height. Passing to the two integer frequencies gives the harmonic gap sum and the stated factor \(mn\).

The first-dual phase after gamma Stirling is, up to a constant, \(t\log(qtr/(2\pi e\mu\nu))\), \(r=m/n\). Both cutoff conditions imply \(t\ge(2\pi/(qr))\max(\nu^2,\mu^2)\). For \(\mu\ne\nu\) the first derivative is therefore at least \(|\log(\mu/\nu)|\), so the gap sum applies. The \(\mu=\nu\) subsum uses the second derivative \(1/t\). These two pieces give Lemma 2.4. Lemma 2.5 squares the cutoff polynomial, integrates off-diagonal gaps on the moving intervals, and estimates the diagonal by the usual power sum up to \(\sqrt{qTr/(2\pi)}\). Cauchy–Schwarz then converts to the needed first absolute moment. Multiplying this mean by the pointwise AFE remainders bounds the four linear remainder products. The product of the two AFE remainders is bounded directly. For example the \(H^{1/2}q^{1/2}(qT)^{1/2-\sigma}(m/n)^{1/2}\) term is absorbed by \((qT)^{1-\sigma}mn\) since \(H\le T\) and \(\sqrt{m/n}\le mn\).

At the center, write \(\gamma_q=\gamma_E+\sum_{p\mid q}\log p/(p-1)\). The two simple poles cancel and the central main integrand is
\[
 \frac{\varphi(q)\chi(m)\overline{\chi(n)}}{q\sqrt{mn}}
 \left(\log\frac{qt}{2\pi mn}+2\gamma_q\right).
\]
This follows by expanding \(L(s,\chi_0)\) at 1, with residue \(\varphi(q)/q\), and combining the two poles before taking the limit. Integrating \(\log t\) gives the \(H\)-window primitive displayed in Theorem 1.1. Lagged imaginary shifts or unequal real parts are outside the assertion.

Two endpoint details are worth making explicit. Lemma 2.1 states its real-parameter estimates at cutoff \(x>1\), while the diagonal cutoff \(\sqrt{qt/(2\pi mn)}\) can fall below 1. For \(0<x\le1\), compare the real-\(s\) principal expression at 1 and at \(x\); the integral \(\int_x^1u^{-s}\,du\) is \(O(x^{-s})\) and the possible jump at 1 is \(O(1)\). This extends the needed statement uniformly through \(s=1\) when pole-opposite terms are combined, and to \(s=0\) by the printed endpoint argument. If an adaptive AFE cutoff is below its fixed lower admissibility constant, then \(q\) is bounded and \(mn\gg T\). The balanced AFE and the diagonal-plus-gap mean square give \(O_q(T\log T)\) for the whole twisted integral by absolute value. The combined main term is also absorbed by the permitted first error in that range: for \(u=qt/(2\pi mn)\) the pole-cancelled combination inside the brackets after factoring \((mn)^{-\sigma}\) is \(O((1+|\log u|)\max(1,u^{1-2\sigma}))\) by the Laurent expansion. Thus the claimed estimate can be recovered on the edge without applying an AFE outside its cutoff assumptions.

I also read the displayed summands in Lemmas 2.4–2.5 symmetrically where a literal transcription omits a sign or a square root. The usable lower bound in Lemma 2.4 is the absolute logarithm above. In the Lemma 2.5 mean-square diagonal the length is \(O(\sqrt{qTr})\), so the \(\sigma\le1/2\) bound is \(O(H(qTr)^{1/2-\sigma}\log(qT))\) before Cauchy, and \(O(H\log(qT))\) before Cauchy for \(\sigma\ge1/2\). These are the stated result's powers. [Moment proof, source pp. 6–17](../../sources/prime122_frontier_pending/2610.41394.pdf)

## Normalization and weighted zero statistics

Section 3 fixes the full dyadic window in the normalized twist \(I_m/I_1\). In Theorem 3.1 the conductor condition is \(q\ll T^{4\sigma-1}\) at fixed \(\sigma>1/2\). Its denominator follows from \(q^{1-\sigma}T^{-\sigma}\ll T^{-4(\sigma-1/2)^2}\). The leading coefficient is \(\chi(m)m^{-\sigma}\) and the dual term has power \((qT)^{1-2\sigma}m^{\sigma-1}\). The two remaining types come from Theorem 1.1 divided by \(T\). Theorem 3.3 instead uses \(q\ll T/\log^8T\), and its denominator is \(\gg T\log(qT)/\log\log(q+2)\) from the central main term and \(\varphi(q)/q\gg1/\log\log(q+2)\). Its main twist \(\chi(m)m^{-1/2}(1-\log m/\log T)\) is sufficient at fixed \(q\). The conductor-growth conditions in this section do not turn the weighted density theorem into a growing-conductor statement.

Section 4 fixes both primitive characters and uses the full strip-zero convention. The variable \(\gamma=(\rho-1/2)/i\) can be complex. A Schwartz test on \(\mathbb R\) with compactly supported Fourier transform has the required entire extension and horizontal-strip decay. Dilation by \(\log T/(2\pi)\) about the height \(t\) leads to the standard Weil formula. Its gamma factor gives \(\widehat\varphi(0)+O(1/\log T)\) on \(T\le t\le2T\), because \(\log(t/(2\pi))=\log T+O(1)\); the prime powers \(p^j\) for \(j\ge3\) have an absolutely bounded sum before \(1/\log T\). For \(q=1\) the two pole test values are negligible: at real argument of order \(T\log T\) and imaginary argument of order \(\log T\), compact Fourier support and repeated integration by parts give arbitrary fixed power decay despite finite exponential-type growth. No hypothesis about locating all zeros on the critical line is used in this argument.

For fixed \(\sigma>1/2\), the leading prime term is summable by \(\sigma+1/2>1\). Of the prime errors, the last two have powers \(3a/2-\sigma\) and \(a(\sigma+1)/2-\sigma/2\) up to logs, where the test support is in \([-a,a]\). Thus \(a<\sigma/(\sigma+1)\) suffices. The prime-square arm is also within the error budget. In the estimate before (4.9), the sum \(\sum p^{2\sigma-3}\log p\) is \(O_\sigma(1)\) for fixed \(\sigma<1\) and \(O(\log T)\) at \(\sigma=1\); its printed decaying replacement for \(\sigma<1\) misses the bottom primes. Its prefactor \(T^{1-2\sigma}\) still gives the required bound. The other prime-square errors have powers \(a-\sigma\) and \((a-1)\sigma/2\). All leading prime-square terms are summable, including on the center line.

At \(\sigma=1/2\) the same strict support argument uses \(a<1/3\). The normalized twist at \(p\) contains \(1-\log p/\log T\). When \(\chi_1=\chi_2\), its leading contribution combines with the unweighted term to give
\[
 \widehat\varphi(0)-\int_{\mathbb R}(1-|u|)_+\widehat\varphi(u)\,du
 =\int_{\mathbb R}\varphi(x)\left(1-(\sin(\pi x)/(\pi x))^2\right)dx .
\]
When \(\chi_1\ne\chi_2\), the product \(\chi_1\bar\chi_2\) is nonprincipal and the corresponding prime sum is \(O(1/\log T)\) by the fixed-character prime harmonic sum and partial summation. Lemma 4.2 is written for primitive nonprincipal characters. Use the primitive inducing character of the product, which need not itself be primitive, and remove the finitely many differing primes. Thus the \(1-\operatorname{sinc}^2\) correction is present for the equal-character central law, while the unequal-character law and any fixed \(\sigma>1/2\) produce density 1. Theorem 1.3 at \(q=1\) improves the test support of the prior Sugiyama–Suriajaya 2610.05227 in this same continuous statistic. [Normalized moments and density proof, source pp. 17–25](../../sources/prime122_frontier_pending/2610.41394.pdf) · [Earlier classical comparison](https://arxiv.org/pdf/2610.05227v1)

## Appendix and dependencies

Appendix A proves the **unweighted** theorem for Fourier support in \([-2,2]\). The height average of \(p^{-jit}\) has size \(O((jT\log p)^{-1})\), and the first-prime endpoint \(a=2\) retains \(O(1/\log T)\) by the prime count; higher powers are easier. Under GRH only, the appendix then removes this unweighted support constraint for a test bounded by \(O((1+|x|)^{-1-\epsilon})\). In this second route the ordinates become real and averaging against a height indicator yields a signed counting increment \(N(T+v,\chi)-N(v,\chi)\) against \(\varphi((v-T)\log T/(2\pi))\). For \(-T\le v\le2T\) the increment is \(T\log T/(2\pi)+O_q(T)\), uniformly by the signed Riemann–von Mangoldt formula and bounded endpoint entropy expressions. On the two outer intervals the unit-height count and the decay of the test give \(O_{q,\epsilon}(T^{-\epsilon/2})\). This proves the Appendix A scope without adding GRH to the weighted compact-support theorem. At q=1 GRH here is RH. The source notes the missing zeta pole in a prior support-removal argument. [Appendix A, source pp. 26–28](../../sources/prime122_frontier_pending/2610.41394.pdf)

The cited proof inputs are Selberg [31, Lemmas 1 and 6] for the gap estimate and AFE organization; Titchmarsh [35, Thm. 4.15] for the zeta AFE; Rane [29] for the positive-height \(q>1\) AFE; Montgomery–Vaughan [25] for the principal-character tail model, explicit formula, nonprincipal prime harmonic sum and signed zero count; Ivić [13–14] for derivative tests and Stirling; and the fixed-character PNT and partial summation in §4. Conrey [3] and Bettin–Fazzari [2] organize Appendix A, while earlier weighted comparison laws are [33–34]. References [1–38] are read for their roles and coverage. Their proof details and the paper's named classical inputs are not re-established in this review.

## Observatory interface

Even setting \(q=1\), \(\sigma=1/2\), \(H\asymp T\), the termwise \(m=h,n=1\) substitution against \(|a_h|/\sqrt h\) costs \(O((T^{1/2}y^{3/2}+T^{3/4}y^{3/4})\log^2 T)\). That gives a power saving only below exponent \(1/3\), and it supplies no uniformity in two independent microscopic shifts. Our asymmetric continuous \(J\) input is already stronger in both respects. The density statistic samples a continuous \(t\)-height law with weight \(|L(\sigma+it)|^2\). The Observatory law selects zeta zeros and weights them by \(|\zeta'(\rho)|^2\); the long-prime sum is a varying reciprocal-modulus additive phase. The paper does not estimate this phase. [Continuous \(J\) comparison](prime90_pure_fourth_bottleneck.md) · [Long-prime target](prime117_long_prime_obstacle.md)
