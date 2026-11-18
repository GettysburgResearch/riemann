# PAPER-H402 — Genocchi1860: the original explicit-formula normalization correction

**Identity.** Angelo Genocchi, *Formole per determinare quanti siano i numeri primi fino ad un dato limite*, Annali di Matematica Pura ed Applicata, original series3(1860),52–59, under the heading *Rivista bibliografica*, reviewing Riemann's November1859 communication. DOI https://doi.org/10.1007/BF03198027 . Publisher landing metadata provides1December1860; the original page footer identifies volumeIII,no.1,1860, so the exact month is retained as publisher metadata rather than inferred from the scan. Do not misread `series3(1)` in noisy metadata as third-series volume3; this is the journal's1858–1865 original sequence.

**Primary access.** The eight original article pages are extracted without alteration from the public-domain Internet Archive volume: https://archive.org/download/annalidimatemati3186unse/annalidimatemati3186unse.pdf . Local article: `sources/riemann_constant_skeptic_round4/genocchi1860_pp52-59.pdf`, SHA-256 `60c40a680b855cf36b17a588b94e70692d019416ce05654d895a82f149b5a35c`; full-volume SHA-256 `0bf71cbefaca14ae58f4d1ae229ef222ade1b2a3472f0d35008e65ad7718c7ac`. PDF56–63 correspond to printed52–59. The publisher landing is accessible but the attempted publisher PDF returned HTML, not source PDF; that failed access was not counted as full text.

**Reading and audit scope.** `/root/li_skeptic` read all eight original pages and visually checked57–58, independently reconstructing the central constant/branch calculation. `/root/corpus` subsequently read the complete eight-page extracted text and independently inspected the original57–58 images. Whole-work substantive reading Level1; selected normalization algebra reconstructed, not a whole-paper Level2 or a modern rigorous audit of all contour/infinite-product exchanges. OCR is noisy; central formulas below were verified against images. The work is a historically significant exposition and correction, not a proof of RH or PNT.

## Mathematical content and dependencies

Printed52–53 define prime counting, the prime-power weighted function and the Fourier/Mellin inversion. Genocchi initially counts primes `<=x`, then explicitly reduces the value at a prime by1/2 so that inversion returns the midpoint. Thus his final F is the same half-weighted count as Riemann's; endpoints are not an arbitrary convention added by this archive.

Printed54–55 reproduce the theta continuation and the entire even xi function. His symbol `rho` here denotes a zero parameter of **Riemann's t-variable xi**, corresponding to Riemann's alpha; modern nontrivial zeta zeros are `1/2 +/- i rho`. The paper explicitly allows real or nonreal such parameters in the horizontal strip, rather than assuming RH. Its paired product uses preexisting entire-function theory, citing Briot–Bouquet pp135–140; this dependency is not re-proved by the present audit.

Printed56–58 compute the inverse transforms using Cauchy's definite-integral identities. Crucially, printed57 retains the constant in

\[
 \log\left(1+\frac{(s-1/2)^2}{\rho^2}\right)
 =\log(s-1/2-i\rho)+\log(s-1/2+i\rho)-\log\rho^2,
\]

with consistent continuation. Printed58 obtains the contribution involving the two zeta-zero locations, and then evaluates the total constant as

\[
 \sum_\rho\log(1+1/(4\rho^2))
 =\log\xi_R(i/2)-\log\xi_R(0)
 =\log(1/2)-\log\xi_R(0).
\]

His equation(11), printed58, therefore has the corrected final constant `-log2`:

\[
 f(x)=\operatorname{Li}(x)
 -\sum_\rho[\operatorname{Li}(x^{1/2+i\rho})+
            \operatorname{Li}(x^{1/2-i\rho})]
 +\int_x^\infty\frac{du}{u(u^2-1)\log u}-\log2.
\]

The following paragraph explicitly compares this with Riemann's `+log xi_R(0)` and deferentially submits the discrepancy to Riemann's judgment. This is direct primary evidence of the correction during Riemann's lifetime. It is not a newly discovered defect. The infinite zero sum and contours still require the historical ordering/branch qualifications; the audit does not silently supply modern convergence proofs.

Printed58–59 establish finite Möbius inversion by divisor cancellation, then discuss Legendre, Dirichlet, Drach and Chebyshev's alternative approximations. Those comparisons are historical reports and approximation proposals, not proofs of the prime number theorem. In particular the familiar constant in `x/(logx-c)` is not certified by the correction argument.

## Value for the archive

The paper makes a small normalization term fully traceable and explains how a shifted paired product differs from a product normalized at s=0. The reusable rule is to retain the product's constant factors **before** Fourier/Mellin inversion; changing the center of the product changes a contribution that survives as a constant in the counting formula. The theorem-level graph should link this work to the precise normalization of PAPER-S001, not merely cite it as another early zeta paper.

Next steps: audit the cited Briot–Bouquet product result and Cauchy transform hypotheses separately; reconstruct one common modern Ei/zero-height convention for the entire explicit formula; and preserve the distinction between Genocchi's zero parameter rho and modern zeta's rho. The central correction has independent source scrutiny; none of these facts justify an author-wide error label or a publication-priority claim for this archive.
