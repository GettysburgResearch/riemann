# PAPER-L001 — Li coefficients for automorphic L-functions

Jeffrey C. Lagarias. *Annales de l’Institut Fourier* 57(5) (2007), 1689–1740. DOI [10.5802/aif.2311](https://doi.org/10.5802/aif.2311). [Published source](https://aif.centre-mersenne.org/item/10.5802/aif.2311.pdf); associated preprint math/0404394 (history uninspected).

**Status:** bibliography verified and full text obtained. **Initial inspection was introduction pp.1690–1692; a later independent partial inspection extends the scope as recorded below.** No whole-work Level1, no detailed technical audit, and no independent reconstruction of the automorphic results is claimed. Source SHA256: `844a21e7e397d90ce8a12b31768ac088c1187e3a1a12efe54114fb6e008f19df`.

The inspected passage fixes a consequential notation point. Equation(1.1) defines λ_n by a symmetrically truncated zero sum; equation(1.3)'s derivative definition at1 first corresponds to λ_(-n). Their equality uses zero symmetry, equation(1.2). Generating functions(1.4)–(1.5) exhibit the two expansion centers. A proof that computes an isolated zero contribution must respect this distinction; the generic construction in `proposals/independent_campaigns/li_advocate.md` does so before invoking reflection symmetry.

The p.1691 discussion of Bombieri–Lagarias states the general multiset setting and summability conditions, equations(1.6)–(1.8). This is contextual provenance, not a substitute for reading the original proof. Author-host BL PDF access failed locally and web extraction was unusable; no BL audit is claimed.

The paper's full automorphic theory, quadratic-functional identification, conditional asymptotic constants, interpolation construction, and proof dependencies remain tasks for a future full reading. No exact theorem statements from uninspected later sections are supplied. Correction and version searches are incomplete. This record must be counted as a partial-source inspection, separately from full substantive readings.


Supplementary independent reading (2026-11-17, li_skeptic): introductionpp.1689–1695, definitions/Theorem2.1pp.1696–1699, and completeSection6pp.1721–1726; page1694 visually checked. Still no whole-workLevel1 claim. Same publishedPDF/SHA256, so no newwork count. The original explicitly credits the exponential masking mechanism to Bombieri–Lagarias1999 and supplies a finite-heightLi window. A separate scoped alternate-contour proof preservesTheorem6.1's finalerror despite an insufficient printed geometric-majorant inference; independent review remains pending. See `audits/lagarias2007_contour_scope_round3.md`. No assertion the mainresult is false and no noveltyclaim.
