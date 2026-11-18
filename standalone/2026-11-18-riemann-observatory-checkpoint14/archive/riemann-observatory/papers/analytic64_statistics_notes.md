# Zeta zero statistics, moments and critical-line history

The records identify the edition read and the exact theorem, section or equations consulted. Three full-edition readings are attached to new records. The Hardy facsimile reading supplements the existing record PAPER-S007. The other records describe targeted passages, including hypotheses and whether the source presents a theorem, a conjectural calculation or experimental evidence.

## Complete original readings

### G. H. Hardy, 1914, supplemental reading for PAPER-S007

Read the original French print pp. 1012–1014, complete §§1–3. The first section starts from Mellin inversion of the exponential, attributed there to Cahen. Summing over squares and shifting the contour to Re u=1/4 produces (1), an identity between a Gaussian theta sum and an integral of the real-valued Ξ on the critical line. Substituting y=πe^{iα} gives (2). Differentiating 2p times gives (3), with t^{2p} in the integrand as shown on the facsimile.

The second section uses Bohr–Riesz summability for the alternating square-index Dirichlet series and the trivial zeros to make the differentiated theta term vanish as α approaches π/2. Under the eventual-positive-sign assumption, the limiting integral in (4) is justified by passing to the limit on the compact initial part and using positivity on the tail. For odd p the right-hand side of (4) is negative, so (5) bounds the positive tail by K T^{2p}. The positive subinterval [2T,2T+1] gives the lower bound in (6) of order (2T)^{2p}, incompatible with (5) for large odd p. Even p treats an eventually negative sign. The argument proves infinitely many critical-line zeros. [Original three-page scan receipts](../sources/analytic64_statistics/hardy_receipts.json)

### Andriy Bondarenko and Winston Heap, half-sized gaps

Read all six pages of arXiv:2610.26038v1. Theorem 1 assumes RH and bounds the normalized liminf by 1/2. Suppose instead that it exceeds 1/2 and choose 1/2<c<min(1,μ). Equation (3) then bounds the count N_c(v) in a short centered window by one over the relevant heights. Lemma 1 uses the integrated real logarithmic derivative and its Poisson kernel, (19)–(21), to place Re z in a narrow enlargement of [0,1]. The tangent representation (4) bounds the symmetric quotient F of shifted zeta values and makes it holomorphic in the rectangle used for the contour shift.

The cosine and sine Möbius coefficients in (7)–(12) are chosen so that F times one Dirichlet series has the coefficients of the other. Lemma 2 shifts the Gaussian-weighted integral and extracts the diagonal by (22)–(24). The resonators have length T^{1/(2c)}. The strict inequality c>1/2 controls the off-diagonal terms, while c<μ excludes poles when shifting the contour. The Gaussian norm evaluations and (18) would keep the difference of coefficient energies bounded above. The sign of cos(πc) in (17) makes that difference grow like a positive multiple of log T. The source concerns spacings of ordinates with multiplicity. [Pinned original](../sources/analytic64_statistics/half_gaps.pdf)

### Daniel A. Goldston and Ade Irma Suriajaya, the prime number theorem and pair correlation

Read all nine pages of arXiv:2205.06503v2, including the revision's priority note. Theorem 1 assumes RH and the long-range bound in Conjecture 1 for the generalized weighted correlation F_β. Lemma 1 identifies F_β as an exponentially weighted squared sum over ordinates, then uses the Gallagher–Sobolev inequality and partial summation to bound an unweighted block sum of x^{iγ}. Section 4 applies this to dyadic blocks in the truncated explicit formula for ψ(x), bounding the normalized error by the sum in (2.3) plus a low-height term. Corollaries 1–3 insert specific β, L and W choices and require the stated uniformity in both variables.

Lemma 2 expresses the change from F to F_β through a log-scale integral of differences of F. The proof of Theorem 2 splits that integral at log(β log T)/β and uses Conjecture 2 for the short part. Corollary 4 describes how a uniform quantitative error in F would imply both conjectures. The added remarks credit the main results to the prior paper by Languasco, Perelli and Zaccagnini, with β=1/τ relating their parametrizations. [Pinned original](../sources/analytic64_statistics/goldston_pnt.pdf)

### H. M. Bui, M. B. Milinovich and N. Ng, consecutive gaps

Read all seven pages of arXiv:0910.2052v1. Under RH, Theorem 1.1 gives the normalized limsup λ>2.69 and liminf μ<0.5155. Section 2 recalls the Montgomery–Odlyzko h(c) criterion and relates it to a ratio of the Dirichlet polynomial's mean square weighted around zeros and its ordinary mean square. A test polynomial with divisor coefficients models a positive power of ζ and gives the large-gap method. Adding the Liouville factor reverses the prime contributions and gives the small-gap method.

Section 3 uses the asymptotic (3.1) for the divisor coefficient square sum, partial summation and the prime number theorem to obtain (3.2), a quadratic form with the sine factor sin(πcv)/v. Section 4 derives the plus-sign version (4.1) from λ(pk)=−λ(k), where λ(k) in that formula is the Liouville function. The authors substitute r=3.1 and f(x)=1+10x+39x² for the large gap, and r=1.23 and f(x)=1+0.99x−0.42x² for the small gap. Section 5 discusses limitations of h(c) and demonstrates that degree-two test polynomials reproduce the earlier r=1 benchmarks to the given precision. Numerical optimization is reported as in the source. [Pinned original](../sources/analytic64_statistics/bui_mil_ng_gaps.pdf)

## Source distinctions

- Bourgain and Watt's published perturbed-cones paper is DOI 10.1093/imrn/rnx009. Its pinned arXiv counterpart has the exact 1273/4053+ε bound in §13 Theorem 3 and is the source cited by Andersson. Its distinct sequel claimed a stronger exponent in v1. The v2 withdrawal names proof gaps and removes the sequel's Theorems 1–3 from theorem status. [Perturbed-cones paper](../sources/analytic64_statistics/bw_perturbed.pdf) · [Sequel withdrawal](../sources/analytic64_statistics/bourgain_watt_withdrawal.html)
- Hardy–Littlewood's 1921 Mathematische Zeitschrift article was extracted as PDF pages 294–328 of the GDZ journal volume. Those pages bear the printed numbers 283–317. A similarly titled Zenodo result links a different DOI and returned HTTP 403. The GDZ scan supplies the identified 1921 article. [GDZ volume](https://gdz.sub.uni-goettingen.de/id/PPN266833020_0010)
- The 1994 Rudnick–Sarnak announcement and their 1996 full journal article have distinct titles, scopes and publication records. The earlier announcement gives an outline and points ahead to the later comprehensive treatment. [Announcement](../sources/analytic64_statistics/rudnick_announce.pdf)
- The Goldston–Lee–Schettler–Suriajaya Part I and the separate Baluyot–Goldston–Suriajaya–Turnage-Butterbaugh Part I have distinct author lists, identifiers and hypotheses on their forms of pair correlation.
- The publication endpoint for Bagchi's 1982 article returned HTML. The record remains pending primary-text access. Ingham's 1928 mean-value article, Gonek's 1984 derivative paper and the 1916 Hardy–Littlewood paper already have records in the corpus.

## Reconciliation and source receipts

The shard adds 41 works, with three whole-edition Level 1 readings and 38 targeted Level 0 readings. Deduplication covered the canonical bibliography and every sibling paper-record shard using DOI, arXiv identifier and normalized title. The Hardy reading was retained under the existing work identity. The withdrawn Bourgain–Watt sequel is historical evidence, with the withdrawal reflected in its record status. The selection receipt documents rejected candidates, blocked endpoints and the alternatives that supplied the final source. [Selection receipt](../sources/analytic64_statistics/final_selection_receipt.json) · [Source hash manifest](../sources/analytic64_statistics/SHA256SUMS)
