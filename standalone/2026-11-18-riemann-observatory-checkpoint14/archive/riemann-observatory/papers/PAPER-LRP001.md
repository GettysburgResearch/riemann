# PAPER-LRP001 — Lee1996

Jungseob Lee, **Convergence and the Riemann hypothesis**, *Communications of the Korean Mathematical Society*11(1)(1996),57–62. Publisher printing date1March1996. Received13September1995; revised26September1995. No DOI is supplied in the inspected publisher metadata. Candidate identity: `CAND-41E4476772DA`; OpenAlex `W813808457`.

Canonical publisher landing: https://ckms.kms.or.kr/journal/view.html?uid=1217 . Primary PDF: https://ckms.kms.or.kr/journal/download_pdf.php?spage=57&volume=11&number=1 . Historical KoreaScience identifier `DBSHCJ_1996_v11n1_57` redirects to `JAKO199611919487598`.

Actual source: `sources/logarithmic_riesz_priority_skeptic_round4/lee1996.pdf`, SHA256 `debbc5132b4338e06b8f2d81cb20ab8c47051e1d4e0cda15af713077c9ef4099`. The six printed pages were substantively read in the complete extracted text; main theoremp59 and central proofpp60–61 were also visually inspected. There is scan streaking onp61, but its displayed norm inequalities remain readable. **Whole-work Level1; no whole-work Level2 or independent verification of every proof step.**

## Exact theorem and notation

Let `C` be the space of finite sums `sum c_j{theta_j/x}` on `(0,1)`, with `0<theta_j<=1` and `sum c_j theta_j=0`. Let `R` be the analogous subspace with all `theta_j` rational. The main unnumbered theorem, printedp59, states for **fixed `1<p<=2`** that the following are equivalent:

1. `zeta(s)!=0` for `Re(s)>1/p`.
2. `C` is dense in `L^(p-epsilon)(0,1)` for every sufficiently small `epsilon>0`.
3. `R` is dense in those same spaces.
4. The prescribed **unsmoothed** sequence `f_N(x)=sum_(n<=N)mu(n){1/(nx)}` converges to `-1` in those same spaces.

Equivalently the norm range in4 is every fixed `1<r<p`. The source does **not** include `r=p`. In particular, at `p=2`, its RH-conditional convergence is below `L²`, not in the endpoint norm.

Equation(2),p60, introduces the constrained correction

`g_N(x)=f_N(x)−(sum_(n<=N)mu(n)/n){1/x}`.

Then `g_N` belongs to `R`; the scalar correction tends to zero by the prime number theorem. Dilation of these corrected sums approximates rational interval indicators and hence gives density. The reverse zero-free implication is the usual bounded Mellin-functional obstruction; the precise Mellin identity is Eq(1),p60.

## Proof architecture and dependencies

Pages58–59 give a fixed-distance reciprocal-zeta/Perron lemma. Page60 reconstructs the easy Beurling converse by Hölder and the Mellin transform, and derives density of rational generators from the prescribed convergence. Page61 attempts the zero-free-to-convergence implication through a Mellin/Fourier transform, an asserted Hausdorff–Young inequality, and the fixed-distance Perron estimate. The proof uses the prime number theorem to remove the coefficient constraint term and standard subpower reciprocal-zeta estimates in a strictly zero-free interior half-plane.

The source's Perron proof onp59 bounds an infinite vertical integral by `integral_R |v|^epsilon/(delta+|v−t|) dv`; that positive integral diverges for `epsilon>0`. Accordingly this printed proof passage is not accepted here as an audited absolute estimate. A truncated contour or a different argument is required to justify the intended fixed-distance lemma. This observation does not disprove the lemma or the main theorem, which Balazard–Saias subsequently prove by an explicitly truncated Perron route. No mathematical-error finding about Lee's theorem is elevated from this partial technical observation.

## Historical and priority significance

The explicit acknowledgement in Balazard–Saias *Notes sur la fonction zeta de Riemann,1*,p320, credits Lee with the central arithmetic Beurling convergence result, despite their independent proof and additional equivalent formulations. This primary source therefore repairs an omission in a historical dependency graph that would attribute the whole result only to1998.

Lee's exact array is `mu(n)` in fractional-part sums. It has neither the shifted coefficients `mu(n)n^(-epsilon)` nor fixed or growing logarithmic Riesz powers. The main theorem explicitly leaves the endpoint norm out. It is consequently **not an exact earlier statement** of the archive's RH-conditional moving-array boundary convergence with `mu(n)(1−log n/log N)^(c log N/loglog N)`.

This distinguishes the actual theorems; it does not establish novelty of the moving-array proposition. General summability theory and other primary sources remain to be checked.
