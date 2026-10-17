# Sources, imported interfaces and reading scope

This packet proposes a new composition of stated unconditional inputs. Source citations do not mean every upstream proof was rebuilt. None of the old proposed zero-free conclusions, #961's OPEN-L, or the native critical covariance estimate is an assumption.

## CT: Cureton--Thorner, version 2

Dean Cureton and Jesse Thorner, *A quasi-Riemann hypothesis for Dedekind zeta functions*, Hexagon 2610.00200v2, revision 14 October 2026.

- Landing: https://hexagonmath.org/2610.00200v2
- PDF: https://hexagonmath.org/pdf/2610.00200v2
- Source index: https://hexagonmath.org/src/2610.00200v2/files
- TeX: https://hexagonmath.org/api/v1/works/2610.00200v2/source?path=DedekindZeta.tex

The actual v2 TeX and PDF were read through the web reader. Initial direct openings failed; following the landing/source links succeeded. A direct container download failed DNS. No full local source-file hash, mirrored PDF, or successful container download is claimed. The source index displayed DedekindZeta.tex and hash prefix f54808ad0f967b54, not an independently computed complete hash.

Load-bearing locations inspected:

1. The original average is defined for positive X,Y,Z before the special scale substitution. Section 7 supplies the allowed generators, finite local classes, Kummer conductors and bounded balanced representatives.
2. Section 8: Proposition 8.3, exact reflection and uniform finite-profile derivative bounds; equation (8.15), the separated d,c interaction with the COMPLETE n and a_f variables; equation (8.16), the local beta majorants. The rendered PDF page containing these equations was inspected (zero-based page 24).
3. Section 9: the actual quadratic-family verification and sieve (9.2); localized Fourier L1 bound; the M>1 support discussion and the final simplification which absorbs Z^M into Z^(2M-1). Rendered pages 24--25 were inspected. The new proof does NOT use that simplification for M<1; it reconstructs its own bound from the preceding interfaces.
4. Section 10: additive normalization before its last scale substitution, including both 1/Y and 1/X. Section 11: the full triple Mellin expression, correction domain, common-prime factors and principal H. Rendered page 27 was inspected. Correct numbering: principal nonvanishing is Lemma 11.1 in Section 11.2.
5. The Mellin-continuation argument and the contour/height/descent interfaces were inspected. The joint height bound retains Im(xi)+Im(z), rather than asserting Gaussian decay in xi alone.

CT's stated 31/32 conclusion is not used to bound a reciprocal on a line left of one in this packet. The principal xi line stays at 1+e. The analytic theta foundation, Poisson identity and nonvanishing correction are used as stated theorems. The full Kazhdan--Patterson realization and transitive formal dependencies were not independently reconstructed or built.

## BGL: central family mean

Valentin Blomer, Leo Goldmakher and Benoit Louvel, *L-functions with n-th order twists*, arXiv:1112.1650; IMRN 2014(7), 1925--1955.

https://arxiv.org/pdf/1112.1650

The 21-page PDF was freshly opened, with screenshots of zero-based pages 16--18. Relevant material: Theorem 1.3 as used in Section 5; equation (5.1), its complete AFE and squarefree/powerful decomposition; the detector calculation (5.3)--(5.5). Equation (5.1) includes all sixth-free rows on setting the sixth-power part to one. The finite fixed-twist extension is explained in PROOF Section 3.2, following #959; it is not assumed to follow from dropping twists. Root-number phases and full AFE columns are retained.

No new large sieve or central-value mean is claimed. The new application uses that mean on several zero-selected middle classes as well as the good class.

## DF: sixth-free density

Alexandre de Faveri, *Optimal large sieve for fixed order characters*, arXiv:2610.04045v1.

https://arxiv.org/html/2610.04045v1

Freshly inspected: Theorem 1.1, Corollary 1.5, Section 2.3's choice-dependent ray-class generators and Section 2.5's conductor/multiplicativity conventions, and the full proof of Corollary 1.5 in Section 9. Both indices in the enlarged sieve are sixth-power-free, ordered by FULL norm. The detector coefficients remain complete. The cubic conductor-ordered second moment and multiple-Dirichlet-series applications are not used.

The rational substitutions emitted by `python verify.py --details` are calculated from the displayed Section 9 formula, not fitted to numerical data. Fixed S-ray twists are treated by the coefficient multiplication in the inherited adapter, recalled explicitly in PROOF Sections 3.2--3.3.

## Internal sources and exact status

- #959: 7b845294207d96b883c1fa95028663082267804f, standalone/2026-10-17-numerator-mean-refinement/PROOF.md. Its precise source-family adapter, subset Cauchy lemma, reciprocal disks and complete contour organization are credited. Its 11/12 conclusion is not a black box used in the new proof.
- #961: 7bd275b44261fff93bb565a9342c44b7c66526f6, standalone/2026-10-17-review-imports-theta-escape/. The delivered thirteen-file packet matches the live subtree 916580e58acc72b87df6931b4e688543501c95ab. Its full THETA_ESCAPE.md, GEOMETRIC_ROUTE.md, REVIEW_959.md and checker were read. Both complete verifier modes and its manifest were freshly replayed. Historical mutation records are not relabeled as rerun.
- #960's latest PR description was read. Its rational-integer MRT route is not an input and is not transferred to number-field theta coefficients. Its full packet was not audited here.

The elementary methods used in the new bound are Minkowski, Fourier separation, ideal counting, geometric summation and product majorants; these methods are classical. What is proposed here is the all-scale source-compatible bound and the resulting 91/100 composition. A mismatch in any imported source interface invalidates the global conclusion regardless of the exact checker.
