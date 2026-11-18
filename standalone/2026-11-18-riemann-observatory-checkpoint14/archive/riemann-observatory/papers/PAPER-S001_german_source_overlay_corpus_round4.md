# PAPER-S001 — German source and edition overlay

This is an **augmentation of the existing Riemann1859 work**, not another paper. Agent `/root/corpus`, 2026-11-17. The existing Wilkins English-translation reading record remains intact. A second manifestation, a transcription, a translation, and a manuscript image must not be counted as four works.

## Sources actually inspected

1. **Original German journal print, all ten article pages671–680 read.** *Monatsberichte der Königlichen Preußischen Akademie der Wissenschaften zu Berlin, aus dem Jahre1859*. The page671 heading identifies the session of3November1859, Kummer's presentation, and Riemann's letter to Encke dated19October. The volume is bibliographically dated1860 in the scan-host metadata and Gabcke's source description; the mathematical work remains conventionally Riemann1859. The ten-page public-domain scan is `sources/history_round4/riemann1859_original.djvu`, SHA-256 `9e2b9cd404dd8d054689607ef4b7c49734fd0d6648a272244451f6ae9a5f9b4c`. Each printed page has a separately inspected1280px JPEG with its printed page number in the filename. Source: https://upload.wikimedia.org/wikipedia/commons/d/d2/RiemannPrim1859.djvu . Original scan typography has `über ... Größe`; the later title `Ueber ... Grösse` is an edition spelling, not a different work.
2. **Wilkins German transcription, all nine text pages read**, plus its complete LaTeX source. PDF has a title page followed by numbered1–9, preliminary versionDecember1998; its LaTeX comment is dated16June1998 and explicitly names the1892 collected editionpp145–153 as its source. PDF SHA-256 `ba7fd13614b373798f9d953cee4bb7b4aa7764067edddaa7561e835a6a3331a2`; LaTeX SHA-256 `3e6eb1e50624de1d916a0947a4cb5f99202cb047a1541486b2137c100312d3e6`. URLs: https://www.maths.tcd.ie/pub/HistMath/People/Riemann/Zeta/Zeta.pdf and corresponding `Zeta.tex`.
3. **1892 collected edition, targeted original-page checks:** printed147 and editorial notes154–155 (PDF163,170–171), not a full reading of the book. Local full-volume PDF SHA-256 `55f149d350e4541d0c536222b4a26d74ce5f751a2f0ef97c3b8d3559894de358`; source https://archive.org/download/gesammeltemathem00riemuoft/gesammeltemathem00riemuoft.pdf . The notes are mathematically consequential and are absent from the standalone Wilkins memoir files.
4. **CMI manuscript images:** all four PDF images visually inspected as source manifestations; the dense Kurrent draft is not claimed independently transcribed in full. `riemann_cmi_images.pdf`, SHA-256 `2dd0ea0dde9df70cf6ae441247b1a0716eeaa434a55f9f006d70b48ae10134c2`, from https://www.claymath.org/wp-content/uploads/2023/04/riemann1859.pdf . This file contains Riemann's rough draft, identified as Cod.Ms.B.Riemann3(19–20), not the six-page Clebsch fair copy3(16–18). The classification is supported by Wolfgang Gabcke's actual §§1–4 and references9–11, printedpp1–6, read in his16December2015 third release; its appendix images were not fully audited. His historical identification is attributed, not independently established by handwriting expertise here.

Full hashes, access attempts, byte counts and URLs are in `sources/history_round4/source_manifest.json`. Local source copies are private working evidence; redistribution follows the archive's source policy.

## Exact mathematics and historical proof status

**Continuation and branches, printed672–674 / transcription2–3.** Riemann starts on `Re s>1` with the convergent Euler product/Dirichlet series. The Hankel-type contour circles zero positively while excluding the other poles of `1/(e^x-1)`, and `log(-x)` is real when x is negative. His symbol `Π(z)` is `Γ(z+1)`, so `Π(s-1)=Γ(s)`. The contour relation must not be read as the divergent positive-real Mellin integral being valid for every s; the continued contour expression and gamma factors supply the continuation.

The theta route gives a directly checkable modern statement. With `psi(x)=sum_(n>=1)e^(-πn²x)`,

\[
 \pi^{-s/2}\Gamma(s/2)\zeta(s)
 =\frac1{s(s-1)}+
 \int_1^\infty\psi(x)
 [x^{s/2-1}+x^{-(s+1)/2}]\,dx. \tag{R1}
\]

Initially derive it for `Re s>1`; the right integral is entire in s by uniform exponential decay on compact parameter sets. Its symmetry proves the completed functional equation and its only poles are at0,1. Multiplication by `s(s-1)/2` produces the entire completed xi. This local reconstruction uses Jacobi's theta transformation as an explicit external input and checks the Mellin split/continuation, not a whole-paper Level2 audit.

**Riemann's variable, printed674.** He sets `s=1/2+it` and `xi_R(t)=Π(s/2)(s-1)π^(-s/2)ζ(s)=xi_mod(1/2+it)`, where `xi_mod(s)=s(s-1)π^(-s/2)Γ(s/2)ζ(s)/2`. This distinction is essential: `xi_R(0)=xi_mod(1/2)`, while `xi_R(i/2)=xi_mod(0)=1/2`. The entire theta expression is even in t.

**Strip, count and RH, printed674 / transcription4.** The Euler product and symmetry exclude nontrivial zeros outside the **closed** modern strip `0<=Re s<=1`. They do not establish nonvanishing on its boundary; that is precisely an1896 issue. The German `zwischen` must not silently credit Riemann with the later boundary theorem. Riemann states the smooth count main terms and supplies an argument-principle sketch with a fractional-order qualifier involving1/T; this review does not certify a modern uniform remainder from that sketch. He describes all xi_R zeros being real as very probable and explicitly says a strict proof is desired and was set aside. This is a conjecture, not a theorem. No RH assumption is required to write the subsequent formula with generally complex zero parameters.

**Canonical product, printed675.** The paired xi_R product is asserted with a growth argument. The memoir does not supply all modern entire-function estimates needed to audit that argument completely. The1892 editors' note154 quotes Riemann's draft letter saying the proof was not fully executed and that two asserted conclusions depended on an unpublished expansion; it explicitly identifies both the real-zero counting assertion and the zero-series/contour agreement. This is important contemporary evidence about the memoir's proof scope.

**Half-weighted primes and prime powers, printed675–676 / transcription4–6.** Define `pi_0(x)=# {p<x}+1/2*1_(x is prime)` and

\[
 J_0(x)=\sum_{m\ge1}\frac{\pi_0(x^{1/m})}{m}
 =\sum_{p^m<x}\frac1m+
 \frac12\sum_{p^m=x}\frac1m.
\]

For `Re s>1`, `logζ(s)/s=integral_1^infinity J_0(x)x^(-s-1)dx`, with the logarithm defined by its absolutely convergent Euler expansion. For `a>1` and `x>1`, symmetric-height Mellin inversion gives the half-values. A precise local proof is in the accompanying audit; arbitrary regrouping of unsmoothed contour/zero terms is not allowed.

**Explicit formula, printed676–679 / transcription6–8.** Riemann explicitly says individual terms after splitting `logζ(s)` do not converge when integrated separately over the entire vertical line, and first integrates by parts. Printed678 prescribes different continuation paths for the complex logarithmic-integral terms, differing by2πi, and printed678–679 specifies a zero order and warns that rearrangement changes the result. A notation such as `Li(x^rho)` must mean continuation in `rho log x`; taking the principal logarithm of the complex number `x^rho` would fold its argument and change the formula.

**Known historical constant correction.** The original printed678 and rough-draft image3 display `+log xi_R(0)`. Genocchi1860, original printed57–58, explicitly derives the paired normalization constants and replaces this with `-log2` in equation(11); the1892 editors' note155 likewise states `log(1/2)` rather than `log xi_R(0)`. This is a recovered historical correction, not a newly discovered error. Its branch/constant reconstruction has an independent source audit by `/root/li_skeptic`; the new canonical work record is PAPER-H402. The editors' subsequent speculative typo explanation is not adopted as established history; in particular the modern value of zeta at zero is `-1/2`, so one must not reproduce a misleading `logζ(0)` explanation without its branch/sign context.

**Möbius inversion and final numerics, printed679–680.** `pi_0(x)=sum_m μ(m)J_0(x^(1/m))/m`; for fixed x this is a finite sum because the counting functions vanish below2. Half-weights commute with the finite divisor cancellation. Riemann's final comparison of Li with computed primes and his discussion of oscillatory zero terms are historical numerical interpretation. They do not prove that Li exceeds the prime count for all x, nor a modern unconditional square-root error estimate.

## A verified manifestation discrepancy, not an error in Riemann's print

The intermediate theta split on original printed673 and1892 printed147 contains

\[
 \int_0^1\psi(1/x)x^{(s-3)/2}\,dx.
\]

Both Wilkins1998 standalone German and English PDFs, numberedp3, instead typeset the limits `1` to `infinity` while leaving this integrand unchanged. The source LaTeX confirms those limits. This is a substantive transcription discrepancy: at `s=2`, Jacobi's identity makes the incorrect integrand tend to1/2 as x tends to infinity, so that integral diverges. The subsequent final formula(R1) is correct in all inspected versions. Use the correct original intermediate limits in reconstructions; preserve the downloaded versions and report the discrepancy rather than silently editing source evidence. No global judgment about the translator or the memoir follows.

## Audit accounting and next work

The same work PAPER-S001 already had a complete English-translation substantive reading; it now also has a complete original-German print reading and source comparison. This adds **zero works**, not another Level1 paper. Scope remains Level1 for the entire work with selected Level2 reconstructions; no whole-paper Level2/3 claim. Separate the published historical constant correction from the current transcription discrepancy and from the still-sketch-level global zero/count/contour arguments.

Useful next steps: retain a single standard Ei/height-order convention across the historical and modern explicit formulas; trace the1892 letter excerpt to its autograph before upgrading its historical interpretation; and connect the boundary gap Riemann left open to the exact original1896 arguments. The last task continues with Hadamard, PAPER-H401.
