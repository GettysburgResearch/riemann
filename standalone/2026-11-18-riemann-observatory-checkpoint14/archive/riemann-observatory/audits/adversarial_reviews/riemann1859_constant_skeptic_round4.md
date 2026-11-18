# Independent review of the constant in Riemann's explicit formula

2026-11-17. Reviewer: `/root/li_skeptic`. This is the specifically requested normalization/branch review of existing `PAPER-S001`; it is not a second paper record or a whole-memoir technical audit. The finding is a **known historical correction, independently reconstructed**, not a newly discovered error. Original Genocchi1860 was recovered and its central correction visually verified. No consequence concerning the truth of RH follows.

## Conclusion and exact source scope

Under the definitions and branch prescriptions actually printed in Riemann's memoir, the final additive constant `+log xi_R(0)` must be replaced by `-log2`. The missing real correction is

\[
 \Delta=\log\frac{1/2}{\xi_R(0)}>0.
\]

It arises on replacing a product normalized at the critical center by linear zero factors normalized at `s=0`. A change of a logarithm or exponential-integral branch does not supply this real number. This exact calculation was already made by Angelo Genocchi in1860, printedp58; it is not our discovery.

Actual inspected sources:

* Read the complete nine-numbered-page Wilkins German transcription through its local TeX source. Its header identifies the1892 collected edition,pp145–153, and a1998 transcription; it is not an1859 manuscript itself.
* Visually inspected the actual first-print imagespp674,675,677,678, where the centered definition, product, constant transform and final formula occur. Source files are `sources/history_round4/riemann_original_p674.jpg` and corresponding page names. Original publication: November1859 communication, printed in the1860 volume,pp671–680. Other original printed pages were not independently read by this reviewer for this task.
* Visually inspected CMI rough-draft image3, including the same final `+log xi(0)` term. Manuscript attribution is based on the source-specific Gabcke evidence below, not the generic word “manuscript”.
* Read Genocchi's complete eight-page1860 article,printedpp52–59, from the actual public-domain volume scan; visually checked the crucial algebra onpp57–58. Only the constant calculation is independently reconstructed here; every inversion and limit elsewhere in that article has not been technically audited. Corpus owns canonical `PAPER-H402`.
* Read Edwards's actual scanned-book OCR passage,Section1.16,p31 (1974 text in the2001 unabridged Dover reprint), and the surrounding zero-pair discussionpp29–33. No whole-book reading and no independent verification of Edwards's archival claims are asserted.
* Read Gabcke2015, Sections1–4pp1–5 and referencespp5–6, for manuscript identity; figures were not independently subjected to a handwriting audit. Also visually inspected the1892 editorial notep155 supplied by corpus.

## 1. Two functions denoted by xi must be kept distinct

Write the modern completed function as

\[
 \xi_M(s)=\tfrac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s).
\]

Riemann's printedp674 sets `s=1/2+it` and

\[
 \xi_R(t)=\Pi(s/2)(s-1)\pi^{-s/2}\zeta(s)
         =\xi_M(1/2+it),
\]

because his factorial notation satisfies `Pi(z)=Gamma(z+1)`. In particular

\[
 \xi_R(0)=\xi_M(1/2),\qquad
 \xi_R(i/2)=\xi_M(0)=1/2.
\]

There is no redefinition of `xi` between this displayed definition and the final formula onp678. The same centered notation persists in the Wilkins transcription.

The difference is provably nonzero without numerical computation. The first integral onp674 gives

\[
 \xi_R(0)=\tfrac12-\tfrac14\int_1^\infty\psi(x)x^{-3/4}dx<1/2,
\quad \psi(x)=\sum_{n\ge1}e^{-\pi n^2x}>0.
\]

Positivity follows from the second integral on that page: its differentiated theta summands are positive for `x>=1`, since they contain the factor `pi n²x-3/2>0`. Exponential convergence justifies differentiating there. Thus `0<xi_R(0)<1/2` and `Delta>0` unconditionally.

## 2. The exact finite-factor identity locates the lost constants

For one representative `alpha` of a `+/-alpha` zero pair, put
`rho=1/2+i alpha`, so its reflected zero is `1-rho=1/2-i alpha`. Then

\[
 P_\alpha(s)=1+\frac{(s-1/2)^2}{\alpha^2}
 =\left(1+\frac1{4\alpha^2}\right)
       \left(1-\frac{s}{\rho}\right)
       \left(1-\frac{s}{1-\rho}\right).
\]

Indeed `rho(1-rho)=alpha²+1/4`; multiplying out proves the identity exactly. Therefore the quadratic logarithm is the sum of two normalized linear logarithms **plus** `log(1+1/(4alpha²))`, up to a purely imaginary branch multiple. The added constants must be retained.

The paired product on originalp675 is normalized by `xi_R(0)`. Evaluating it at `t=i/2` gives

\[
 \sum_{\Re\alpha>0}\log\left(1+\frac1{4\alpha^2}\right)
 =\log\xi_R(i/2)-\log\xi_R(0)
 =\log(1/2)-\log\xi_R(0)=\Delta.
\]

The zero count gives `sum |alpha|^-2<infinity`, so this constant series converges absolutely after finitely many initial factors. Off-line zero representatives occur with their conjugates; their constant products are positive real. Along the imaginary segment from0 to`i/2`, the centered completed function is positive, so the summed real logarithm is unambiguous. No RH assumption is required.

For a constant `C`, the source's integrated-by-parts Perron functional contributes exactly `C` for `x>1`:

\[
 \frac{C}{2\pi i\log x}\int_{a-i\infty}^{a+i\infty}
          \frac{x^s}{s^2}\,ds=C.
\]

Originalp677 explicitly makes this calculation for `C=log xi_R(0)`. Its next assertion that all other terms have the normalized linear-log form overlooks the displayed quadratic constants. Adding their total changes

\[
 \log\xi_R(0)\quad\hbox{to}\quad
 \log\xi_R(0)+\Delta=\log(1/2)=-\log2.
\]

This identifies the normalization issue without depending on delicate termwise convergence of the full conditionally convergent zero sum: the constant series itself is absolutely convergent.

## 3. Why the original branch prescriptions do not remove Delta

Originalp678 explicitly specifies the two upper/lower complex integration paths and requires the associated root integral to tend to zero as the imaginary part of the root parameter tends to positive/negative infinity. These prescriptions fix the relevant `Li` branches; a free root-dependent real integration constant is not left available.

For a fixed real `x>1`, let `l=logx`. In modern notation the vanishing branch for an upper-half-plane root is `Ei(rho l)-i pi`, and for a lower-half-plane root it is `Ei(rho l)+i pi`. The imaginary constants cancel in a reflected upper/lower pair. Here `Li(x^rho)` is continued in `rho` with `log(x^rho)=rho logx`; one must not exponentiate first and then reduce its logarithm to a principal branch. Equivalently one may define these branches by an exponentially convergent ray integral rather than use a principal `Ei`; this gives the same zero-pair terms. Ordinary continuation around the logarithmic singularity changes them by multiples of `2pi i`, not by the nonzero real number `Delta`.

There is no hidden rescue through the source's ordering prescription. Riemann orders the `alpha` representatives by magnitude. Since `|Im alpha|<1/2`, the difference between `|alpha|` and its positive real part (the corresponding zero ordinate) is `O(1/|alpha|)`. The two cutoffs therefore differ only by zeros in a bounded interval near the height cutoff, numbering `O(logT)`. A vanishing-branch paired `Li` term is `O_x(1/T)`, so the difference tends to zero. For example the ray representation of `Ei(z)-i pi` in the upper half-plane bounds its modulus by `e^{Re z}/|Im z|`, uniformly for bounded real part; the lower branch is conjugate. Thus the standard magnitude and height orders cannot generate this finite real shift.

An arbitrary rearrangement of a conditionally convergent zero series could change its real value, as Riemann warns, but it is not the specified order. Redefining each `Li` term by unrelated real constants could force a rewritten formula, but would change the function convention and violate the stated vanishing prescription. Neither is a branch interpretation of the printed formula.

## 4. Primary historical correction: Genocchi1860

The recovered original article is Angelo Genocchi, *Formole per determinare quanti siano i numeri primi fino ad un dato limite*, Annali di Matematica Pura ed Applicata,firstseries3(1860),52–59, DOI10.1007/BF03198027. Its actualp57 splits the shifted quadratic logarithm into two unnormalized linear logarithms and a normalizing constant. Page58 then explicitly evaluates

\[
 \sum\log(1+1/(4\alpha^2))
   =\log\xi_R(i/2)-\log\xi_R(0)
   =\log(1/2)-\log\xi_R(0).
\]

Its equation(11) has the final constant `-log2`. The following paragraph explicitly compares it with Riemann's `+log xi(0)`, courteously leaving the difference to Riemann's judgment. This is the same correction as the independent reconstruction above, already in1860.

Access was recovered through a public-domain scan of the entire journal volume, after the directly linked article PDF and publisher DOI endpoint failed. The article was extracted without altering the original pages:

* Volume: https://archive.org/download/annalidimatemati3186unse/annalidimatemati3186unse.pdf ; local `sources/riemann_constant_skeptic_round4/annali1860.pdf`.
* Extract: `sources/riemann_constant_skeptic_round4/genocchi1860_pp52-59.pdf`; original PDFpages56–63,printedpp52–59.
* Crucial rendered original pages: `genocchi_p57.png`, `genocchi_p58.png` in that directory.
* Retrieval hashes and exact extraction map: `genocchi_retrieval.json`, `genocchi_article_extract.json`.

No source-access or full-reading credit is assigned to a search snippet or the initially inaccessible article endpoints.

## 5. Edwards, the1892 editorial note, and manuscript identity

Edwards, *Riemann's Zeta Function*, Section1.16,p31, explicitly discusses this constant mismatch, relates it to the two product normalizations, and credits Genocchi. His text rejects the collected editors' typographical-error explanation, citing a letter and an unpublished numerical calculation. Those latter archival details are attributed to Edwards; this reviewer has not independently examined all those documents.

The actual1892 editorial notep155, visually checked here, itself says that following the calculation gives `log(1/2)` rather than `log xi(0)`, then speculates about a symbol/printing error. Its Li discussion and normalization correction are relevant evidence; its speculation must not be substituted for the original definitions. In particular one must not silently identify `xi_R(0)` with `zeta(0)`: the latter is `-1/2` and has a branch-dependent complex logarithm.

Gabcke's *On a Fair Copy of Riemann's1859 Publication Created by Alfred Clebsch*,thirdrelease16December2015, distinguishes the six-page Clebsch fair copy `Cod.Ms.B.Riemann3(16–18)` from Riemann's four-page autograph draft `3(19–20)`; see Sections1–2 and references[10]–[11],pp1–3,6. The CMI image inspected for this review is from the rough-draft group identified as the latter, not the Clebsch copy. It also contains `+log xi(0)`. The original printedp678 contains the same term, so the discrepancy is not introduced solely by the1998 transcription. Gabcke's identity study does not itself analyze the explicit-formula constant.

## 6. Validated numerical size, not the proof

An Arb192-bit check gives

\[
 \xi_R(0)=0.4971207781883141099\ldots,
\quad\Delta=0.00577508738538610588\ldots.
\]

Original real constant: `-0.6989222679453314153...`; corrected constant: `-0.6931471805599453094...`. Rigorous intervals and the executable check are preserved in `experiments/code/riemann_constant_arb_round4.py` and matching JSONresults. The program requires python-flint0.9.0; it uses no numerical zeros and assumes no RH. The exact positivity/product argument above establishes the discrepancy independently of these numbers.

## Audit classification and limits

This is a known corrected historical additive normalization issue, supported by the literal first print, a direct algebraic reconstruction, and the actual1860 correction. It is not an alleged new flaw in a current proof, and does not diminish the memoir's principal conceptual achievements. A whole technical audit of the memoir, Genocchi's integral interchanges, the full later rigorous explicit formula, or all manuscript variants is not claimed. Corpus owns the canonical same-work source updates and Genocchi record; this file is an independent agent review only. Root adjudication may use it together with corpus's separate reconstruction.
