# PAPER-H405 — von Mangoldt1894 extract, read in its1896 translation

**Identity.** Hans von Mangoldt, *Auszug aus einer Arbeit unter dem Titel: Zu Riemann's Abhandlung „Ueber die Anzahl der Primzahlen unter einer gegebenen Grösse“*, Sitzungsberichte der Königlich Preussischen Akademie der Wissenschaften zu Berlin(1894),883–896. Presented14June1894. The original issue/session header is19July1894, while the original printed896 footer explicitly says issued26July. The translation's first-page citation gives the issue date19July; preserve both dates rather than silently treating the issue/session date as the distribution date. The actual primary mathematical manifestation read is Léonce Laugel's French translation, *Extrait d'un travail intitulé « Sur le mémoire de Riemann relatif au nombre des nombres premiers inférieurs à une grandeur donnée »*, Annales scientifiques de l'École Normale Supérieure, série3,13(1896),61–78, DOI https://doi.org/10.24033/asens.422 . The translation adds no distinct mathematical work to the corpus. The longer1895 Crelle article is a separate expanded publication/version dependency, not silently substituted here.

Source: https://www.numdam.org/article/ASENS_1896_3_13__61_0.pdf . Private copy `sources/history_round4/mangoldt1894_laugel1896.pdf`,2,219,263bytes, SHA-256 `c81953b062c701d8aefe9aca2a996bac1c38a5c21a9ca0fc3abe7c71a1aeded1`, accessed2026-11-17. The19-page PDF includes a Numdam cover, then all18article pages. Printed page p is PDF page p−59. Original German1894pages883,891–892,896 were subsequently inspected and compared; central891–892 confirms the same grouped identity and citation of the local-zero-count theorem. The entire14-pageGermanmanifestation has not been fully read. Copyright notices in the digitized copy are preserved; final distribution should link to the source rather than include this private copy by default.

**Reading/audit scope.** All18French article pages61–78, including displayed formulas, substantively read from the original scans after OCR traversal. Whole-work Level1 for this translation manifestation. A local Level2 reconstruction checks the grouped-limit argument on72 from its stated local-zero-count and kernel inputs; see `audits/mangoldt_grouped_remainder_corpus_round4.md`. This does not audit every numerical constant in the zero-count estimate, every preliminary canonical-product/gamma estimate, or the full51-page1895 paper. No paper-wide Level3 or exhaustive erratum search is claimed. The local reconstruction has been submitted to root for independent review.

## Notation and exact results

The source uses Riemann's variable t and ξ_R(t)=ξ_mod(1/2+it). Its α_j are **zeros of ξ_R with positive real part**, not modern zeros ρ of ζ and not assumed real. Multiplicity is counted, and α_j are ordered by nondecreasing real part. Their imaginary parts lie in [−1/2,1/2]. Thus γ_j=Re α_j corresponds to the positive height Im ρ in modern notation. The paired product on63 is

\[
 \xi_R(t)=\xi_R(0)\prod_j(1-t^2/\alpha_j^2).
\]

The source credits Hadamard's1893 entire-function work for this input; it does not prove RH by treating α_j as real.

**SectionI,66–67:** the source proves quantitative bounds on the number of zeros, including no ξ_R zero with |Re t|≤12; a local bound

\[
 \#\{j:h-k\le\Re\alpha_j\le h+k\}<k\log h,
 \quad\tan1\le k\le h-4;
\]

and, for h>12, the printed bound

\[
 N(h)=\frac h{2\pi}\log\frac h{2\pi}-\frac h{2\pi}+\frac54
 +\eta\,[0.34(\log h)^2+1.34\log h+1.33],\quad |\eta|\le1,
\]

where N(h) counts0<Re α_j<h with multiplicity. These are the exact source statements, not numerical constants independently certified by this archive. In particular its stated remainder is O(log²h); do not silently replace it by the sharper later classical O(log h) theorem while describing what this extract proves. The local bound, by fixed k=2, supplies O(log h) zeros per bounded height interval, which is more useful for the disputed convergence estimate than the global O(log²h) remainder.

**SectionII,68–69:** define the von Mangoldt weight Λ(n)=log p for n=p^m,m≥1 and0 otherwise. For fixed x>1,r real, put

\[
 A_0(x,r)=\sum_{n<x}\frac{\Lambda(n)}{n^r}
 +\frac12\frac{\Lambda(x)}{x^r}
\]

with Λ(x)=0 when x is not an integer prime power. This is exactly the source's half-value convention. For a>0,a+r>1,

\[
 -\lim_{h\to\infty}\frac1{2\pi i}
 \int_{a-ih}^{a+ih}\frac{\zeta'(s+r)}{\zeta(s+r)}\frac{x^s}{s}\,ds
 =A_0(x,r).
\]

The truncation is symmetric in height and the limit is pointwise in x. The μ=1 integral is not declared absolutely convergent. Fixed a+r>1 puts the contour in the absolutely convergent logarithmic-derivative half-plane, but does not by itself make the oscillatory1/s integral absolutely integrable in height.

**SectionII,71–73:** after the paired partial-fraction expansion and explicit kernel estimates, the source proves convergence of its paired zero series in increasing Re α_j order. For β_j,±=1/2−r±iα_j its term can be written compactly as

\[
 W_j(x,r)=\sum_{\pm}\frac{x^{\beta_{j,\pm}}-1}{\beta_{j,\pm}}.
\]

The elementary terms plus this series give A_0(x,r). At r=1/2 it reduces to2sin(α_j log x)/α_j. The resulting series need not converge uniformly across arithmetic jumps. The source explicitly recognizes this on73–74; discontinuity is not evidence against pointwise convergence or Perron half-values.

**Equation28,74:** in modern notation its r=0 consequence is

\[
 \psi_0(x)=x-\log(2\pi)-\tfrac12\log(1-x^{-2})
 -\lim_{T\to\infty}\sum_{|\Im\rho|\le T}\frac{x^\rho}{\rho},
 \qquad x>1,
\]

with multiplicity and symmetric-height pairing; ψ_0(x)=Σ_(n<x)Λ(n)+Λ(x)/2. The source displays the equivalent α_j-paired trigonometric formula. An arbitrary permutation of a conditionally convergent sum is not licensed.

**Equations29–32,75–76:** integrate the parameter r to pass from prime-power logarithmic weights to the weighted prime-power count. At r=0 the source obtains Riemann's prime-counting explicit formula with **−log2** as constant, not log ξ_R(0). Its principal-value/complex-power conventions are stated before SectionII; a complete independent branch audit of every transformed Li integral is not claimed here. The correct constant agrees with Genocchi1860's known correction in PAPER-H402. These observations require no discovery claim about the original Riemann paper.

**77–78:** the author notes that RH, or even a fixed narrower strip for ξ_R zeros, would imply a prime asymptotic through the explicit formula, but does not claim to prove such a strip or the PNT. He criticizes Cahen's claimed prime asymptotic; the target source is not adjudicated here. The final note credits Piltz's habilitation pp42–43 for earlier related convergence principles, under Riemann-type assumptions, discovered by the author after finishing his work. This is a useful primary-source provenance lead, not evidence that the two arguments have already been compared by this archive.

## The growing-sum criticism, fairly scoped

De la Vallée Poussin1896 appendix70 alleges that the1894 extract, printed892, ignores that a sum has H→∞ terms. In the translation, the corresponding passage is72. It explicitly invokes the kernel estimates14–16 **and the local-zero-count theorem2 of SectionI** to show that its grouped remainders vanish. The local count controls the growing number of terms. The scoped audit supplies the complete modern estimate

\[
 \sum_{\gamma_j\le h}W_j-I_h=O_{x,a,r}(\log^2h/h),
\]

where I_h is the full paired partial-fraction integral at finite height. This reconstruction tracks all growing sums and remains bounded when h is close to a zero ordinate. It supports the compressed step from the source's stated inputs. **The historical accusation is not accepted as a verified error.** The subsequently inspected full1895German285–292 explicitly supplies grouped estimates and predates the criticism (see PAPER-H406); originalGerman1894 central891–892 now confirms that the cited local-zero-count input was already present in the announcement; whole-paper technical certification is still not claimed.

## Dependency graph and next steps

Hadamard1893 product + gamma/argument estimates → local zero count and global count → truncated Perron kernels and paired partial fractions → grouped remainder control → pointwise explicit formula with ordering/half-values → parameter integration → weighted prime-power count formula. RH remains unproved throughout.

Original1894German891–892 has now been compared with translation72; the full1895German285–292 grouped estimates are inspected in PAPER-H406 and explicitly control the growing sums. The next task is independent review of the local reconstruction and a deeper audit of its original analytic inputs. Independently audit the reconstructed O(log²h/h) lemma before upgrading its verification status. Keep fixed-x convergence distinct from uniformity across prime powers, and keep the1894 O(log²h) zero-count error distinct from its1905 improvement. No literature novelty is asserted for the reconstruction.


## Original German source overlay

Public-domain1894scan extracted from https://archive.org/download/sitzungsberichte1894deutsch/sitzungsberichte1894deutsch.pdf . Local14-page `sources/history_round4/mangoldt1894_german_pp883-896.pdf`,573,252bytes, SHA-256 `cc1890b563c0aea9e5f618ab5761ad72cf11d51aa4025b9a42b10bf4fdd5a05d`. Mapping and full-volume hash are in `mangoldt1894_german_extract_corpus.json`. Printed891–892 are articlePDF9–10. These actual pages were visually compared with translation71–72; the exact decomposition into grouped growing terms and the explicit invocation of local zero counting agree. This rules out attributing the caveat to a later translation intervention. Actual883/896 identities and dated footer were also checked. No additional work or full-reading count is added by this manifestation overlay. The original896 credit identifies Piltz's habilitation as Jena1884, strengthening that candidate-only provenance lead.
