# Version and scope check for Sklyar–Marchenko Proposition 6(4)

17 November 2026. Internal comparison of the archived preprints, the later resolvent paper, and the journal metadata. In this note the subsequence assertion refers to the exact text in arXiv:1405.2731v2 and v3. The latest arXiv version omits the assertion. The journal version of record was unavailable through the checked full-text routes.

## The statement and its scope

I visually checked §2.3 and Proposition 6 on pp. 8–9 of v2, including the statement and its whole proof. The starting \((e_n)\) is a Riesz basis of a Hilbert space \(H\), its associated right shift is \(Te_n=e_{n+1}\), and \(\phi_n^k=(I-T)^ke_n\), \(k\ge1\). Item (3) concerns the whole sequence in \(H\). Item (4) says “For each \(\mathcal G\subset\mathbb N\) the sequence \(\{\phi_n^k\}_{n\in\mathcal G}\) is not a basis sequence.” The lead-in spells out that the stated conclusion concerns a basis of “any subspace \(L\subseteq H\).” The proof of item (4) consists of “It follows from the structure of \(\{\phi_n^k\}_{n\in\mathcal G}\).” The quantifier includes infinite proper subsets and the lead-in expressly permits a proper closed span. [Pinned v2, pp. 8–9](https://arxiv.org/pdf/1405.2731v2) · [Archived v2](../../sources/finite_moment63_operator_antecedents/sklyar_marchenko_eigenvectors.pdf)

A narrower statement would be valid with “a basis of \(H\)” in place of “a basis sequence.” Indeed, the full biorthogonal sequence in item (2) supplies a nonzero continuous functional annihilating any subsequence that omits its own index. Item (3) addresses the full index set. The explicit lead-in and the separate statement of (3) rule out using that narrower reading as an explanation of item (4).

## Direct subsequence calculation

Take the allowed instance \(H=\ell^2(\mathbb N)\) with its standard orthonormal basis and \(k=1\). For \(\mathcal G=\{2,4,6,\ldots\}\), \(\phi_{2j}^1=e_{2j}-e_{2j+1}\) are mutually orthogonal and all have norm \(\sqrt 2\). Precisely,
\[
 \left\|\sum_j a_j\phi_{2j}^1\right\|^2=2\sum_j|a_j|^2
\]
for any finite list of coefficients. The map from \(\ell^2\) onto their closed span is a scaled isometry. Hence this infinite proper subsequence is a Riesz basis of that closed span.

The same structure gives such an example for every fixed \(k\). Take \(\mathcal G=\{(k+1)j:j\ge1\}\) and write
\[
 \phi_n^k=\sum_{r=0}^k(-1)^r\binom{k}{r}e_{n+r}.
\]
The coordinate blocks are disjoint. Their norm squared is \(\sum_{r=0}^k\binom{k}{r}^2=\binom{2k}{k}\). A bounded invertible map sending the canonical orthonormal basis to the chosen Riesz basis transfers the binomial blocks and preserves upper and lower Riesz bounds. Thus the calculation fits the stated hypotheses for arbitrary \(k\) and arbitrary starting Riesz basis.

In v3 the proof of item (4) is changed to a reference to the argument for item (3). The full-system biorthogonal vectors used in (3) need not be the representing vectors of the coefficient functionals in the smaller closed span. For \(k=1\), the full-system vectors are \(\psi_n=\sum_{r=1}^n e_r\), with norm \(\sqrt n\). On the even subsequence the relevant vectors are the orthogonal projections of \(\psi_{2j}\) onto \(L=\overline{\operatorname{span}}\{\phi_{2m}^1:m\ge1\}\), namely \(\phi_{2j}^1/2\), of constant norm \(1/\sqrt2\). A norm argument for the full biorthogonal system therefore does not apply to this subsequence. [Pinned v3, pp. 9–10](https://arxiv.org/pdf/1405.2731v3)

## Version comparison and access

| Edition | Exact comparison |
| --- | --- |
| arXiv v1, 12 May 2014 | Proposition 2.5(4), p. 7, expressly says no \(\mathcal G\) forms a basis of any subspace. |
| arXiv v2, 22 September 2014 | Proposition 6(4), p. 8, says no \(\mathcal G\) is a basis sequence. The surrounding prose states the intended any-subspace meaning. |
| arXiv v3, 3 November 2014 | Proposition 6(4), p. 9, adds \(|\mathcal G|=\infty\). The proof, p. 10, invokes similarity to item (3). The infinite even subsequence still meets the hypothesis. |
| arXiv v4, 24 August 2016 | The latest archived preprint ends §2 on p. 8 after Proposition 5, then opens §3 on p. 9. The earlier §2.3 and universal subsequence assertion are omitted. The log-frequency group appears as Theorem 6, with the whole-family basis property addressed separately in Proposition 3. |

The dates are arXiv version history dates and the watermarks identify the scanned versions. The v2 archive SHA-256 is \(\texttt{70d11b5f0b6b3407c11f4f83ddf3ab56dda7c9e565a8b84214fdd9c04fc537c4}\). The other full-text hashes are recorded in the [source manifest](../../sources/sklyar63_prop6_audit/SHA256SUMS). [ArXiv revision history](https://arxiv.org/abs/1405.2731) · [v1 PDF](https://arxiv.org/pdf/1405.2731v1) · [v3 PDF](https://arxiv.org/pdf/1405.2731v3) · [v4 PDF](https://arxiv.org/pdf/1405.2731v4)

Crossref identifies the journal article as *J. Funct. Anal.* **272**(3), 1017–1043, February 2017, DOI 10.1016/j.jfa.2016.11.001. The article, direct PDF, DOI redirect and Elsevier content API returned a gateway 403. The OpenAlex stored PDF and XML routes returned 401. The Karazin repository returned zero items for exact-title and DOI searches. The zbMATH entry supplies bibliographic metadata. The Crossmark record displays “Document is current” and lists no update. A targeted Crossref correction query returned the article and related results, with no matching formal correction. These are metadata checks. The wording of the journal version remains unverified, and omission in v4 is the directly observed revision result. [DOI](https://doi.org/10.1016/j.jfa.2016.11.001) · [Crossmark](https://crossmark.crossref.org/dialog/?doi=10.1016/j.jfa.2016.11.001&domain=www.sciencedirect.com&uri_scheme=https) · [Archived Crossref receipt](../../sources/sklyar63_prop6_audit/crossref.json) · [Archived zbMATH receipt](../../sources/sklyar63_prop6_audit/zbmath.json)

## Separation from the later spectral results

Sklyar–Marchenko's 2021 resolvent paper, Theorems 1.2 and 3.1, states the full-family minimality/non-basis property and the spectral and resolvent formulas. Its Theorem 2.1 concerns a Schauder decomposition made from a partition \(\bigcup_j E_j=\mathbb N\) of the whole family. A single even-indexed basis sequence of its proper closed span supplies no such decomposition. These 2021 statements and the log-group construction in v2 Theorem 8/v4 Theorem 6 remain separate from the superseded preprint subsequence wording. [2021 paper, §§1–3](https://doi.org/10.4171/JST/344) · [Archived 2021 PDF](../../sources/finite_moment63_operator_antecedents/sklyar_marchenko_resolvent.pdf)
