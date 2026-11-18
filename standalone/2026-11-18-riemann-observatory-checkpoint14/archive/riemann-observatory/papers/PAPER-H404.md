# PAPER-H404 — de la Vallée Poussin1896, first PNT memoir

**Identity.** Charles-Jean de la Vallée Poussin, *Recherches analytiques sur la théorie des nombres premiers. Première partie: La fonction ζ(s) de Riemann et les nombres premiers en général*, Annales de la Société scientifique de Bruxelles20, deuxième partie (1896),183–256. The manifestation actually accessed is the Hayez, Bruxelles1897 offprint, first part separately paginated1–74, in a bound collection. The offprint title gives1897; the following imprint explicitly says it is extracted from Annales t.XX, deuxième partie,1896. The journal page range comes from bibliographic indexing, not a comparison with the original journal leaves. No DOI has been verified. Do not use the Internet Archive item's erroneous1879 catalog date as the work date.

Source: https://archive.org/download/recherchesanalyt00lava/recherchesanalyt00lava.pdf . Private local copy `sources/history_round4/vallee_bound_reprint.pdf`, SHA-256 `38b003593a007ea06f9865598d771cf44edecf708152818d173bf0e435126a28`, accessed2026-11-17. The bound PDF has336pages and includes other works; **only the first part is analyzed here**. Printed first-part page p is PDF page p+12. The1–74first-part text is not a distinct mathematical work merely because the scanned manifestation is dated1897.

**Scope.** Entire first-part OCR/narrative traversed, but OCR loses many formulas. Original displayed formulas and surrounding text independently inspected on printed26–28,43–47,60,62,66–74, plus the title. Targeted primary-source mathematical reading and local reconstruction; **not a complete74-page Level1 reading or paper-wide Level2 audit**. Bibliographic/access Level0 is complete. Locally reconstructed arguments are the absolutely summable logarithmic-frequency coefficient extraction and monotone unsmoothing. The long boundary-zero contradiction in §§43–50 and all preliminary contour estimates are not independently certified. No substantive reading or audit of parts2–3 is claimed.

## Exact source results and limits

**§2, printed2:** the Euler product gives nonvanishing in Re s>1 and does not by itself settle Re s=1. This boundary issue is the stated objective, rather than a proof of RH.

**§23,26–28:** an entire function of genus zero or one with its zeros to the left of a vertical line, and an absolutely convergent reciprocal3/2-power zero sum, admits a double-pole logarithmic-derivative inversion formula. In a safely explicit version, let F(0)≠0, let its zeros ρ (with multiplicity) have Re ρ<h, let Σ|ρ|^(-3/2)<∞, choose y>1 and a>h, and choose distinct u,v with Re u,Re v<a, neither a zero of F. The displayed source formula is

\[
 \frac1{2\pi i}\int_{a-i\infty}^{a+i\infty}
 \frac{F'(s)}{F(s)}\frac{y^s}{(s-u)(s-v)}\,ds
 =\frac{y^uF'(u)/F(u)-y^vF'(v)/F(v)}{u-v}
 +\sum_\rho\frac{y^\rho}{(u-\rho)(v-\rho)}.
\]

This is a source transcription with explicit sufficient parameter exclusions inherited from the preceding discussion, **not a complete new certification of the contour theorem**. The source first takes finite partial products and finite vertical height, passes to the partial-product limit, then takes the height to infinity using a uniform majorant of order |ρ|^(1/2)/|(u−ρ)(v−ρ)|. The latter is summable under its3/2-power hypothesis. Simply knowing each term has a limit would not suffice. The canonical-product derivative display on26–27 has a localized sign inconsistency, discussed in the scoped audit; the correct derivative has +1/ρ. No failure of the resulting contour identity is inferred.

**§§35–41,43–47:** put t=log y. The source works with a convergent part A+ε(y), ε→0, plus an absolutely summable trigonometric series in t, with nonzero frequencies stated not to approach zero. It proves stability under fixed trigonometric multiplication and ordinary averaging, logarithmic averaging to A, coefficient extraction, and uniqueness. For example, after like frequencies are collected,

\[
 a_\alpha=2\lim_{Y\to\infty}\frac1{\log Y}
 \int_1^Y\varphi(y)\cos(\alpha\log y)\,\frac{dy}{y},
\]

with the analogous sine formula (§39,46). The audit supplies an elementary proof in a larger class requiring only absolute summability, with no gap between frequencies. It also records a qualification to the literal closure claim if arbitrary positive finite accumulation points are allowed. Zeta-zero frequencies have no finite accumulation, so that class issue is not a counterexample to the source's zeta application.

**§51,60:** ζ has no zero of the form1+iβ, β real. Combining with Euler-product nonvanishing excludes all zeros with real part≥1; s=1 is a pole. This is the boundary theorem. The original proof uses the two incompatible logarithmic-frequency representations developed in §§43–50, not the later compact3+4cos argument. Its full coefficient algebra has not been independently audited here.

**§52,61–62:** the normalized absolutely summable zero tail tends to zero after boundary nonvanishing. The author explicitly says that its convergence rate is unknown and could be slower than any negative power of y if zeros approach Re s=1 at large height. **Do not attach the later1899 logarithmic zero-free region or exponential PNT error to this1896 first-part theorem.**

**§§55–56,66–69:** the source obtains

\[
 \frac1y\int_1^y\theta(x)\,\frac{dx}{x}\longrightarrow1,
 \qquad\theta(y)=\sum_{p<y}\log p,
\]

then uses monotonicity on fixed multiplicative intervals to conclude θ(y)~y. The theorem is printed on69; the same page deduces that for every fixed k>0 the number of primes in (y,(1+k)y) tends to infinity. Endpoints p=y do not affect these asymptotics. Taking y→∞ before k→0 is essential in the unsmoothing. Modern partial summation yields the equivalent usual PNT π(y)~y/log y.

**§57,69:** an additional exact limiting assertion is

\[
 \log y-\sum_{p<y}\frac{\log p}{p-1}\longrightarrow\gamma,
\]

where γ is Euler's constant. This is the displayed source theorem. Its full dependency chain is not independently checked here; it should not be presented as a consequence of monotonicity alone.

## Architecture and historical controversy

Continuation, canonical product and zero counting → uniformly controlled truncated inversion kernels → double-pole explicit formulas → absolutely summable logarithmic-frequency expansions → coefficient-extraction uniqueness plus prime-weight positivity → boundary nonvanishing → dominated decay of the normalized zero tail → integrated prime asymptotic → monotone unsmoothing → PNT.

The appendix70–74 criticizes attempts to obtain the unsmoothed explicit formula, including von Mangoldt's1894 note and Cahen's1894 thesis. Its printed70 footnote alleges that a growing finite sum of vanishing terms was mishandled at von Mangoldt's printed892. **This is an unadjudicated historical allegation by the author, not an archive finding of an error in von Mangoldt.** The Cahen target is not source-audited here. Subsequently PAPER-H405 read the actual1894extract through its French translation, and PAPER-H406 inspected the full1895grouped-limit proof; those records do not confirm the growing-sum allegation. PAPER-H405/H406 subsequently reconstruct and inspect the grouped estimates, which explicitly use local-zero-count bounds; no growing-sum error is confirmed. The distinction between pointwise convergence, uniform tails in a smoothing parameter, and uniformity in the arithmetic variable remains essential. Hadamard1896printed220 responds with his μ>1 absolute-convergence device; source-paper identities and exact smoothing weights must be kept separate.

## Concrete next research steps

1. Complete a formula-by-formula original-image reading of §§10–34 and43–50 before upgrading this work to whole-paper Level1 or an intensive proof audit.
2. Read von Mangoldt1894printed892 and the fuller1895 memoir, preserving version changes, before adjudicating the appendix's convergence criticism. Compare pointwise Perron inversion, symmetric height truncation, half-values, and uniform tails separately.
3. Put the double-pole and Hadamard μ>1 smoothing schemes into a single exact hypothesis table. Both remove a non-absolutely-summable endpoint; determine which growth and boundary inputs each really needs.
4. Use the no-gap ℓ1 coefficient-extraction lemma for proposed positivity/trace models only after proving absolute summability. The lemma supplies no control of a merely conditionally convergent zero series, no spectral realization, and no RH implication by itself.

No claim of new literature novelty, a new zero-free region, an independently verified error in the PNT proof, or progress toward RH follows from this record.
