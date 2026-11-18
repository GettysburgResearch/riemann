# Whole-memoir skeptical audit of Riemann 1859

PAPER-S001 · 2026-11-18 · Independent source review before comparison with the assigned advocate. This is a whole-work reading with a reconstruction of the argument and its local gaps. The canonical record stays Level 1 pending separate adjudication.

## Manifestations and reading ledger

Bernhard Riemann, *Ueber die Anzahl der Primzahlen unter einer gegebenen Grösse*, November 1859 Academy proceedings, printed pp. 671–680. Page 671 identifies a letter dated 19 October and Kummer’s presentation on 3 November. I directly read all ten first-print page images, including the Academy framing and the last empirical paragraph, with the Wilkins German TeX as a cross-check. The first print is decisive where witnesses disagree. [First print](../../sources/history_round4/riemann1859_original.djvu) · [Page image manifest](../../sources/history_round4/source_manifest.json)

| Manifestation actually consulted | SHA-256 | Scope |
|---|---|---|
| First-print DjVu and its page images | `9e2b9cd404dd8d054689607ef4b7c49734fd0d6648a272244451f6ae9a5f9b4c` | Complete, first-print pp. 671–680. Per-image hashes are in the manifest. |
| Wilkins German TeX, 1998, based on the 1892 collected text | `3e6eb1e50624de1d916a0947a4cb5f99202cb047a1541486b2137c100312d3e6` | Parallel text witness. |
| Rendered Wilkins English p. 3, local PNG | `d6d981a120912805eacb480f17879d8bda7175ae50b8dabf624d5ddd02dd2a12` | Intermediate theta split only. |
| 1892 collected edition | `55f149d350e4541d0c536222b4a26d74ce5f751a2f0ef97c3b8d3559894de358` | Rendered pp. 147, 154–155. |
| Genocchi 1860, extracted first print | `60c40a680b855cf36b17a588b94e70692d019416ce05654d895a82f149b5a35c` | Rendered pp. 57–58, specifically normalization and (11). |

| First-print page | Material directly checked |
|---|---|
| 671 | Proceedings framing, Euler product as departure. |
| 672 | Absolute-convergence half-plane, ordinary Gamma integral, Hankel continuation, cut prescription, negative-half-plane deformation. |
| 673 | Residues at nonzero multiples of \(2\pi i\), functional symmetry, Jacobi theta relation and split. |
| 674 | Centered completed function, two cosine integrals, strip, count, probable reality of all roots and proof explicitly deferred. |
| 675 | Product argument, definition at a prime, prime-power weighted count and Mellin transform. |
| 676 | Fourier inversion and midpoint, substitution of the product inside the inverse. |
| 677 | Integration by parts, Gamma product, constant transform, parameter differentiation and simple-pole sign. |
| 678 | Parameter-dependent primitives and two branch prescriptions, explicit formula, ordered comparison. |
| 679 | Continuation of ordering claim, finite inversion, differentiated finite approximation, smooth prime-power subtraction. |
| 680 | Gauss/Goldschmidt comparison continued and empirical weighted-count observation. |

## Continuation, count and factorization

On p. 672, \(\Re s>1\) justifies integrating the geometric series against \(x^{s-1}\) by absolute convergence. The Hankel formula uses a cut on positive real \(x\), with \(\log(-x)\) real for negative \(x\). Shrinking the origin arc is initially justified in that same half-plane because its contribution is \(O(\varepsilon^{\Re s-1})\). Keeping positive radius gives the continued expression. Any apparent integer singularities from dividing by \(\sin(\pi s)\Gamma(s)\) require removability or residue checks. They are bypassed by the theta continuation below. For the p. 673 deformation, take squares with horizontal edges at imaginary parts \(\pm(2k+1)\pi\) and vertical edges at real parts \(\pm(2k+1)\pi\). The reciprocal denominator is bounded on these edges, including the horizontal ones where \(e^x\) is negative real. The cut boundary is handled by the Hankel slit. The outer pieces are \(O_s(R^{\Re s})\), and the residues are absolutely summable when \(\Re s<0\). An arbitrary sequence of expanding contours would lack this separation from poles. The resulting functional equation follows on the overlap by continuation.

The alternative is independent of that large-contour estimate. With \(\psi(x)=\sum_{n\ge1}e^{-\pi n^2x}\), the theta change of variable gives
\[
\pi^{-s/2}\Gamma(s/2)\zeta(s)
=\frac1{s(s-1)}+\int_1^\infty\psi(x)(x^{s/2-1}+x^{-(s+1)/2})\,dx.
\]
The integral is entire by exponential decay locally uniformly in \(s\). The *intermediate* \(\psi(1/x)\) term is integrated from \(0\) to \(1\) on first-print p. 673 and collected p. 147. Both Wilkins versions put \(1\) to \(\infty\) there. At \(s=2\) that integrand tends to \(1/2\), by the theta relation, so the printed intermediate integral diverges. The final symmetric formula agrees across witnesses. [Original p. 673](../../sources/history_round4/riemann_original_p673.jpg) · [Collected p. 147](../../sources/history_round4/riemann1892_p147-163.png) · [Wilkins English p. 3](../../sources/history_round4/riemann_english_p3-04.png)

Write \(\xi_*(s)=s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s)/2\) and \(\Xi(t)=\xi_*(1/2+it)\). The latter is Riemann’s \(\xi(t)\), since his \(\Pi(z)=\Gamma(1+z)\). The cosine representation proves reality for real \(t\), evenness and entirety. Euler nonvanishing and reflection confine the zeros to the closed strip. The zero-free vertical edges require another argument. On the real \(s\) segment \((0,1)\), the positive alternating eta series and the negative factor \(1-2^{1-s}\) imply \(\zeta(s)<0\), hence \(\xi_*(s)>0\). The endpoints have value \(1/2\). There are therefore no centered zeros with real part zero.

At p. 674 the argument principle counts with multiplicity provided the rectangle has no boundary zeros. Its claimed relative “Bruchtheil” of order \(1/T\) is given without control of the horizontal variation near zeros. A modern proof uses a right edge strictly to the right of 1 and its reflected left edge, avoids zero ordinates at the top, and controls \(\arg\zeta\) separately from the Gamma contribution. For example, on the horizontal segment from 2 to \(1/2\), the analytic real-part proxy \([\zeta(z+iT)+\zeta(z-iT)]/2\) is bounded below at 2 by \(2-\zeta(2)>0\), and has polynomial upper bounds on a larger fixed disk by standard strip estimates. Jensen bounds its zero crossings by \(O(\log T)\), controlling the argument changes between crossings. Stirling supplies the two printed main terms. This also yields the local \(O(\log T)\) count for bounded-width windows. At a zero ordinate the chosen one-sided or midpoint count must be stated. Historically von Mangoldt 1895 supplies the rigorous count with \(O(\log^2T)\), and the 1905 work gives \(O(\log T)\). These are total counts. The next sentences of first-print p. 674 separately assert approximately as many real roots, call universal reality very probable, and defer a rigorous proof. The draft letter quoted by the 1892 editors p. 154 additionally names both the real-root estimate and the ordered-series/contour comparison as coming from an unpublished expansion. [Original p. 674](../../sources/history_round4/riemann_original_p674.jpg) · [Collected editorial p. 154](../../sources/history_round4/riemann1892_p154-170.png) · [Von Mangoldt 1895](../../sources/history_round4/mangoldt1895_pp255-305.pdf)

The p. 675 factorization argument needs a complex-plane growth bound for the logarithm of the zero-free quotient, beyond convergence of a product and a real-direction heuristic. There is a short modern repair directly from the source. For \(|t|\le r\), the theta bound \(\psi(x)\ll e^{-\pi x}\) and \(|\cos(t\log x/2)|\le x^{r/2}\) give \(\log M_\Xi(r)=O(r\log(r+2))\) by the Gamma integral. In the entire variable \(w=t^2\), \(G(w)=\Xi(t)\) has order at most \(1/2\), and \(G(0)>0\). Hadamard factorization at order below 1 gives an absolutely locally convergent genus-zero product with constant \(G(0)\), counting multiplicities. This proves \(\Xi(t)=\Xi(0)\prod_{\Re\alpha>0}(1-t^2/\alpha^2)\), without using a zero asymptotic or RH. The \(\pm\alpha\) pairing corresponds to \(\rho,1-\rho\), with \(\rho=1/2+i\alpha\). Conjugation is a different symmetry and in the off-line case generally completes a quartet. The product is global, while its logarithm requires a branch and is only used on eligible domains. [Original p. 675](../../sources/history_round4/riemann_original_p675.jpg)

## Inversion, branches and the omitted normalization

First-print pp. 675–676 imply
\[
\pi_0(x)=\sum_{p<x}1+\tfrac12\mathbf1_{x\text{ prime}},
\quad J_0(x)=\sum_{m\ge1}\pi_0(x^{1/m})/m.
\]
At a prime power \(p^m\) the jump is \(1/m\) with half that increment at the point. For example \(J_0(4)=9/4\). The absolutely convergent Euler logarithm on \(c>1\) gives the displayed Mellin transform \(\log\zeta(s)/s\). Dirichlet–Jordan Fourier inversion in \(u=\log x\) supplies the symmetric-height inverse. Indeed the unweighted step count is \(O(e^u(1+u))\) and its exponentially weighted jump measure is finite for \(c>1\) by the Euler logarithm. Thus \(e^{-cu}J_0(e^u)\) is integrable and of bounded variation, with the prescribed midpoint. The generic Fourier argument on p. 676 suppresses the reflected term in each sine or cosine inverse. The two reflected terms cancel in the sum, as the 1892 note (2) explains. For the original integrated-by-parts inverse at \(x>1\) the boundary term is \(O_{x,c}(T^{-1})\) because the Euler logarithm is bounded on the line. These facts justify the inverse of the *combined* logarithm.

The single shifted quadratic log on first-print p. 676 is printed without the summation sign. Pp. 675 and 678 identify the intended sum. The contour on p. 677 with integrand \(x^s/((\beta-s)\beta)\), upward on a line right of \(\beta\ne0\), has value \(-x^\beta/\beta\) after division by \(2\pi i\), for \(x>1\). The original omits the compensating minus sign. The nearby derivative in \(\beta\) is correct. The Wilkins German TeX has the compensating minus and the sum, and introduces a separate \(ds\) in the p. 675 elementary integrals where the first print has \(dx\). [Original pp. 675](../../sources/history_round4/riemann_original_p675.jpg), [676](../../sources/history_round4/riemann_original_p676.jpg), [677](../../sources/history_round4/riemann_original_p677.jpg) · [Wilkins German TeX](../../sources/history_round4/riemann_german_transcription.tex)

For \(x>1\), put \(\ell=\log x\). The real prime-pole contribution uses \(\operatorname{li}(x)=\mathrm{PV}\int_0^x du/\log u\); the two detours around 1 differ by \(2\pi i\) since the residue is 1. For nonreal \(\rho\) the root primitive compatible with the vanishing prescription on p. 678 is
\[
E_\rho(x)=\int_{-\infty+i\Im\rho}^{\rho}\frac{e^{\ell w}}w\,dw
=\operatorname{Ei}(\rho\ell)-i\pi\operatorname{sgn}(\Im\rho).
\]
The equality uses the usual \(\operatorname{Ei}\) continued above/below the negative real axis. This is a continuation with \(\log(x^\rho)=\rho\ell\), so reducing the phase of the exponentiated number would give different terms. The imaginary offsets cancel in every reflected pair. The negative-real Gamma roots give integrals from infinity and sum to the printed correction since \(\sum_{n\ge1}u^{-2n}=1/(u^2-1)\) for \(u>1\).

A separate real constant is forced before any conditionally convergent ordering question. For each reflected pair,
\[
1+(s-\tfrac12)^2/\alpha^2
=(1+1/(4\alpha^2))(1-s/\rho)(1-s/(1-\rho)).
\]
Changing normalization from the center to \(s=0\) introduces the absolutely convergent constant series \(D=\log\xi_*(0)-\log\Xi(0)\). The two integrals on p. 674 show \(0<\Xi(0)<1/2\), since in the differentiated one each term of the theta kernel has positive factor \(\pi n^2x-3/2\). Thus \(D>0\). The inverse of a constant divided by \(s\) is that constant at \(x>1\), so the final constant must be \(\log\Xi(0)+D=-\log2\). Neither a branch choice nor switching between magnitude and height yields a real additive shift. The literal comparison of the centered-log derivative integral on p. 678 with the ordered zero terms also carries the shift \(-D\log x\): differentiating the extra \(D/s\) gives \(-D/s^2\). Genocchi pp. 57–58 already computed the missing contribution and printed \(-\log2\) in eq. (11). The 1892 p. 155 note confirms the replacement and merely speculates about its origin. [Original p. 678](../../sources/history_round4/riemann_original_p678.jpg) · [Genocchi primary text](../../sources/riemann_constant_skeptic_round4/genocchi1860_pp52-59.pdf) · [Collected editorial p. 155](../../sources/history_round4/riemann1892_p155-171.png)

## The ordered limit and the final claims

Local uniform convergence of log factors on compact pieces of the vertical line is insufficient for removing the height cutoff after interchanging the infinite sum and integral. The original p. 678–679 explicitly raises the cutoff question and claims agreement, but supplies no domination or grouped estimates. A modern sufficient route inverts the logarithmic derivative on carefully chosen horizontal edges staying \(\gg1/\log T\) from all nearby zero ordinates. Such heights exist by the bounded-window count. The partial-fraction expansion and the same count give \(O(\log^2T)\) for \(\zeta'/\zeta\) along fixed-width horizontal edges in the relevant strip. The remaining sides, pole and trivial zeros require their own estimates when deriving the ordinary \(\psi\) explicit formula. For passage to the \(J\) zero sum, integration by parts in the ray integral gives \(E_\rho(x)=x^\rho/(\rho\log x)+O_x(|\Im\rho|^{-2})\), locally uniformly for \(x>1\). This isolates the absolutely convergent correction and transfers convergence from the symmetric \(\psi_0\) zero sum. A derivation of the identity must additionally retain the normalization and the pointwise midpoint representative. The historical proof of that identity is von Mangoldt 1895, pp. 283–292 for the paired limit and grouped tails, pp. 294–295 for the jump definition, p. 299 eq. (64) and pp. 300–302 for the unweighted specialization and branch comparison. The resulting pointwise statement is
\[
J_0(x)=\operatorname{li}(x)-\lim_{T\to\infty}\sum_{|\Im\rho|\le T}E_\rho(x)
+\int_x^\infty\frac{du}{u(u^2-1)\log u}-\log2,\qquad x>1,
\]
with multiplicity. The passage to every height from admissible heights, and to the original ordering by \(|\alpha|\), follows from \(E_\rho(x)=O_x(1/T)\) and \(O(\log T)\) zeros in the bounded shell between the cutoffs. Indeed \(|\Im\alpha|\le1/2\) gives \(|\alpha|-\Re\alpha=O(1/T)\) there. This argument does not establish the source’s stronger remark about obtaining every real value by reordering, which would require separate sign/divergence analysis. [Von Mangoldt 1895 first print](../../sources/history_round4/mangoldt1895_pp255-305.pdf)

The p. 679 Möbius inversion is exact and finite: substitute \(J_0\), group by \(k=mn\) and use \(\sum_{m\mid k}\mu(m)=\mathbf1_{k=1}\). Midpoint values propagate through this identity because taking the two one-sided limits commutes with the locally finite sum. The differentiated finite zero sum describes oscillatory approximants. The full staircase’s derivative is a discrete measure, so no ordinary pointwise derivative or uncontrolled termwise differentiation of the infinite zero sum follows. For off-line \(\alpha\) the cosine formula is algebraically valid with complex frequency and a growing hyperbolic factor in \(\log x\), so its displayed \(x^{-1/2}\) prefactor alone cannot bound the contribution at that scale. The smooth first prime-power subtraction is \(-\tfrac12\operatorname{li}(x^{1/2})\), of order \(-\sqrt{x}/\log x\). The tabulation through three million and the last p. 680 claim of empirical agreement with \(\operatorname{li}(x)+\log\Xi(0)\) cannot establish a uniform sign, prime-counting error, or RH. The smooth subtraction and the ordered explicit formula both survive the repairs. None upgrades the memoir’s conjecture. [Original pp. 679](../../sources/history_round4/riemann_original_p679.jpg), [680](../../sources/history_round4/riemann_original_p680.jpg)
