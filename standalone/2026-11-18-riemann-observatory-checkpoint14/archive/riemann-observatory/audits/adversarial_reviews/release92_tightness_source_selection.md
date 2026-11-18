# Independent source selection for two-scale tightness

18 November 2026. Recommend both dependencies for selection at Level 0. I compared normalized titles and author names, both relevant DOI strings, the first-edition ISBN and Library of Congress number, and the Numdam item identifier against all 999 canonical records, including 998 selected records, 87 contributor JSONL shards, 14 top-level corpus and provider ledgers and the paper alias register. No duplicate work or provider row matched either source. Each carries a specific proof dependency with an exact source locator.

## Garsia and Rodemich

Adriano M. Garsia and Eugène Rodemich, *Monotonicity of certain functionals under rearrangement*, appeared in *Annales de l'Institut Fourier* 24(2), pp. 67–116 (1974), DOI 10.5802/aif.507. I checked the PDF's publisher cover, journal imprint, pp. 69–70 and reference [7] on p. 116. The local Numdam scan has 51 PDF pages including its cover and has SHA-256 `36a0909f6684535ed0170fb89bf964628d6710bfb1cb49cd0e74954d9cf40a93`. Theorem 1.2 and equations (1.2), (1.3), (1.7) and (1.8) provide the deterministic modulus inequality with finite double-integral energy, an admissible gauge and a convergent gauge integral. The proof transfer uses the continuous polygonal interpolation and a rescaled block before applying the theorem. For continuous paths the almost-everywhere bound extends to all pairs; admissibility and integrability are checked in the local construction.

The 1974 two-author article directly reproduces the inequality and credits the earlier three-author result as [7]. Its own arrangement theorem has a different role. Attribute the classical inequality to Garsia, Rodemich and Rumsey and cite the 1974 re-statement as the exact inspected source. The complete journal PDF was available and the reading was targeted.

[Numdam journal record](https://www.numdam.org/item/AIF_1974__24_2_67_0/) · [Journal scan, p. 70](https://www.numdam.org/item/10.5802/aif.507.pdf#page=5) · [Local proof comparison](uniform89_tightness_priority.md)

## Billingsley

Patrick Billingsley, *Convergence of Probability Measures*, John Wiley & Sons, New York (1968), first edition, ISBN 0-471-07242-7 and LCCN 68023922. I checked the title and copyright scans and the printed pp. 55, 95–96 and 103. Theorem 8.2 supplies the initial-value and asymptotic modulus criterion in the space of continuous paths. Theorem 12.3 uses a single continuous nondecreasing clock and exponent greater than one. Section 12, Problem 9 gives the equally likely placement of one triangle among the (n) subintervals and its use at the critical exponent. The two-scale proof adapts its pitch and height and retains a separate grid-to-path step. The Wiley DOI 10.1002/9780470316962 identifies the 1999 second edition; the 1968 edition record carries a null DOI. The private source manifest pins the scanned excerpts individually. Access was limited to the checked excerpts.

[1968 scan with source passages](https://djvu.online/file/vaaIHv9IWlVeK) · [1999 publisher edition record](https://onlinelibrary.wiley.com/doi/book/10.1002/9780470316962) · [Local proof comparison](uniform89_tightness_priority.md)

## Disposition

Both are recommended primary passage dependencies. The source checks support the classical inputs and their use here. Priority for the exact arbitrary-grid two-parameter equivalence remains unestablished. The recommendations, source pins and corrected rows are in the pending decision receipt and admission copy.

[Decision receipt](../../quality/pending_round13/release92_tightness_source_decision_receipt.json) · [Admission copy](../../quality/pending_round13/release92_tightness_source_admission_records.jsonl)
