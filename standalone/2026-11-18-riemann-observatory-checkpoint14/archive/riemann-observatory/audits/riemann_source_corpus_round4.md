# Local reconstructions accompanying the German Riemann source audit

Agent `/root/corpus`, 2026-11-17. Source/reading scopes and page locators are in `papers/PAPER-S001_german_source_overlay_corpus_round4.md`. This note supplies two reusable checks without claiming a complete modern proof of Riemann's explicit formula.

## Mellin inversion and endpoint values, without RH

Fix real `a>1`. On the logarithmic variable u define `H(u)=e^(-au)J_0(e^u)`, taking it zero for u<0 and using midpoint values at jumps. Its positive jump measure before weighting is `sum_(p,m) (1/m)delta_(m logp)`. Thus the weighted jump mass is

\[
 \sum_{p,m}\frac1{mp^{ma}}=\log\zeta(a)<\infty,
\]

and Tonelli gives `integral_R H(u)du=logζ(a)/a`. The continuous part of its distributional derivative has total variation `a integral H=logζ(a)`; the jumps have that same finite mass. Hence `H` is an integrable function of bounded variation, with total variation at most `2logζ(a)`.

Its Fourier transform in convention `exp(-ibu)` is exactly `logζ(a+ib)/(a+ib)`, by the absolutely convergent Euler expansion and the Mellin integral. The ordinary symmetric Fourier inversion theorem for integrable bounded-variation functions returns the average of the two one-sided values at every point. Changing variables back gives

\[
 J_0(x)=\lim_{T\to\infty}\frac1{2\pi i}
 \int_{a-iT}^{a+iT}\frac{\log\zeta(s)}s x^s\,ds,
 \qquad x>1.
\]

This proves the prime-power half-weight convention at every jump and explicitly supplies the functional hypotheses missing from a formal unrestricted Fourier interchange. It proves nothing by itself about deforming the contour through zeros, summing zero contributions, or changing their order. The input Fourier inversion theorem is a precisely named external theorem, not formalized here.

The two separate cosine/sine inversions for a general h have reflected-frequency terms; only their sum is the unrestricted inversion. The1892 editor's note(2), printed154, flags this historical shorthand. In the actual application H is supported on positive u, so the reflected term vanishes when `log x>0`.

## The theta limit discrepancy has an explicit witness

The original printed673 and collected1892p147 split the small-x interval correctly as `integral_0^1 psi(1/x)x^((s-3)/2)dx`. Wilkins1998 German and English numberedp3 instead print `integral_1^infinity` with the same integrand. Jacobi's identity gives

\[
 \psi(1/x)=\sqrt{x}\,\psi(x)+(\sqrt{x}-1)/2.
\]

At `s=2`, the latter integrand is
`psi(x)+(1-x^(-1/2))/2`, which tends to1/2. The incorrectly limited integral diverges. The original limited integral converges rapidly because `psi(1/x)` decays exponentially as x tends to zero. The final continued theta identity is nevertheless typeset correctly in the transcription, so this is a local manifestation correction. Exact page images and hashes are preserved; independent source comparison is requested before integrating an aggregate finding.

## Historical constant: verification boundary

The shift-factor identity, conditional on the correctly normalized paired canonical product, is

\[
 1+\frac{(s-1/2)^2}{\alpha^2}
 =\left(1+\frac1{4\alpha^2}\right)
 \left(1-\frac{s}{1/2+i\alpha}\right)
 \left(1-\frac{s}{1/2-i\alpha}\right).
\]

The real total of the omitted logarithmic constants is
`sum_alpha log(1+1/(4alpha²))=log xi_R(i/2)-log xi_R(0)=−log2−log xi_R(0)`. This is absolutely convergent at the product level and does not assume RH. Appropriate local logarithms must be chosen by continuation; blindly applying principal logarithms separately is not a valid proof of the logarithmic identity globally.

Most importantly, the correction is not inferred only from this reconstruction: Genocchi1860 original printed57–58 explicitly performs it, retaining the Li normalization, and gives `-log2` in equation(11). The1892 notes154–155 supply the branch prescription and known correction. Independent advocate/skeptic source evidence, not agreement between repeated algebra alone, supports the historical interpretation. The independent detailed branch review is owned by `/root/li_skeptic`; no new error-discovery count is claimed here.
