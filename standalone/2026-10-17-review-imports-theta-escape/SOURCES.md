# Primary sources, exact versions, and audit scope

All sources below were accessed live through the web reader or connected GitHub reads in this pass. “Read” means the locations specified, not a complete reconstruction of every cited theorem. Direct container downloads failed; no complete local PDF/TeX archive or source-file hash is asserted.

## Reviewed internal source

GettysburgResearch/riemann PR #959, head
`7b845294207d96b883c1fa95028663082267804f`:
https://github.com/GettysburgResearch/riemann/pull/959

`standalone/2026-10-17-numerator-mean-refinement/PROOF.md` was freshly fetched from that commit. The live PR body pins its parent at `e6dfa07d07ed7a5d049039d7255919a992cadc77` and records its original validation boundaries. This pass writes a different checker; it does not claim to have rerun the original one.

## CT: Cureton--Thorner, v2

Dean Cureton and Jesse Thorner, *A quasi-Riemann hypothesis for Dedekind zeta functions*, Hexagon 2610.00200v2, revision 14 October 2026.

- https://hexagonmath.org/2610.00200v2
- https://hexagonmath.org/pdf/2610.00200v2
- https://hexagonmath.org/src/2610.00200v2/files
- https://hexagonmath.org/api/v1/works/2610.00200v2/source?path=DedekindZeta.tex
- Formal source identified in the existing imports: https://github.com/AxiomMath/DedekindZetaZeroFree/tree/09afbb4ce6570c1615d58509dc197fc9f0956b7d

The versioned landing links enabled access after some initial direct URL failures. Inspected the actual TeX sections on allowed generators/Kummer characters, separated quadratic reflection, reflected mean square and arbitrary fixed support exponent M>1, the original additive factor A_t, triple Mellin expression, local correction domain, principal H, density/reciprocal argument and final contours. Labels `eq:moment`, `eq:additive-square-bound`, `eq:euler-factorization`, `eq:correction-regions`, and `lem:principal-nonzero` are the stable identifiers.

The last lemma is Lemma 11.1 in Section 11.2; the domain computation is in Section 11.1. This corrects #959's lemma numbering. The unrestricted positive theta estimate and its refinements in this packet are source-composition deductions, not a rebuilding of CT's metaplectic construction. The reported Lean formalization was not built or transitively axiom-audited here.

## BGL: 2011 preprint / 2014 publication

Valentin Blomer, Leo Goldmakher and Benoit Louvel, *L-functions with n-th order twists*, arXiv:1112.1650; International Mathematics Research Notices 2014(7), 1925--1955.

https://arxiv.org/pdf/1112.1650

Inspected Theorem 1.3, family conventions, and Section 5, especially (5.1) and the complete squarefree/powerful decomposition in its proof and zero detector. Rendered PDF pages 17--19 were inspected as screenshots, not inferred solely from extracted mathematical text. The fixed finite ray twists are treated through the proof, with full columns and root-number phases retained. BGL's primitive-character convention must not be mistaken for a claim of extra zero extension on arbitrary sixth-power rows; the restricted sixth-free CT adapter is essential.

## DF: de Faveri, v1

Alexandre de Faveri, *Optimal large sieve for fixed order characters*, arXiv:2610.04045v1.

https://arxiv.org/html/2610.04045v1

Inspected Theorem 1.1, Corollary 1.5, Section 2.3's choice-dependent generators and deep ray modulus, the conductor/multiplicativity conventions, and Section 9's full proof of Corollary 1.5. Its displayed detector is specialized to n=6 in our checker. The new first threshold 187/250 uses the middle range of its q=2sigma-1 formula. Full sixth-free norm, not radical ordering, is maintained.

## FSW import, v2

Christopher Frei, Efthymios Sofos and Martin Widmer, *Some applications of the quasi-Riemann hypothesis to class groups and small generators of number fields*, arXiv:2610.18491v2, 14 October 2026.

- https://arxiv.org/abs/2610.18491
- https://arxiv.org/html/2610.18491v2

Inspected the introduction's explicit conditional qualification; Theorem 1.1, Corollaries 1.2--1.4, Theorem 1.5 and generator conclusion; the QRH modification of the explicit-formula argument at its stated application scope. No new proof of effective Chebotarev or the class-group theorems is claimed. The record states arXiv's perpetual non-exclusive license. This packet includes original annotations and substitutions, not full source redistribution.

## BV import, v1

Manjul Bhargava and Sameera Vemulapalli, *The existence of small defining polynomials for number fields*, arXiv:2610.20600v1, 14 October 2026.

- https://arxiv.org/abs/2610.20600
- https://arxiv.org/html/2610.20600v1

Inspected the main theorem and geometric reduction at their stated scope; Sections 5--7 in detail, especially Lemma 8's approximate-functional-equation floor, Proposition 9's exact class/scaling period and normalization, and the CM subconvexity/mean estimates. The HTML identifies CC BY 4.0. No fresh proof of the cited Michel--Venkatesh subconvexity theorem is claimed. Our new geometric identities need only the stated period, elementary theta convergence and Mobius inversion; the proportion's asymptotic application additionally imports the source's restricted mean decay.

## Attribution boundary

No exhaustive literature-priority search was performed. The contribution claimed here is the explicit audit, source-compatible restricted-row calculation, retuned conditional comparison and geometric-interface deductions. The source theorems, Cauchy, Hecke's period identity, Mobius inversion and elementary probability inequalities remain attributed classical inputs. Neither source reputation nor source checks establish an independent final proof.
