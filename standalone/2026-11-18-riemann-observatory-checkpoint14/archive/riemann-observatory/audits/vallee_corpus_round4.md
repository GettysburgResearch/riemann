# Scoped original-source reconstruction: de la Vallée Poussin1896

Agent `/root/corpus`,2026-11-17. Canonical source identity and exact partial-reading scope: PAPER-H404. The actual manifestation is a1897 offprint explicitly extracted from the1896 Annales volume. No whole74-page technical audit is claimed. This note separates a derived elementary lemma from source theorem statements and historical allegations.

## 1. Coefficient extraction needs no frequency gap under ℓ1 summability

Let Λ be a countable subset of R\{0}. Suppose Σ_(λ∈Λ)|cλ|<∞ and ε:[0,∞)→C is locally integrable with ε(t)→0. Define

\[
 g(t)=A+\varepsilon(t)+\sum_{\lambda\in\Lambda}c_\lambda e^{i\lambda t}.
\]

For every real ω,

\[
 \lim_{T\to\infty}\frac1T\int_0^Tg(t)e^{-i\omega t}\,dt
 =\begin{cases}A,&\omega=0,\\c_\omega,&\omega\ne0,\end{cases}
 \tag{V1}
\]

where cω=0 for ω outside Λ. Like frequencies must first be collected; absolute summability justifies collecting them. No discreteness or positive distance of Λ from0 or ω is assumed.

**Proof.** The ε contribution has modulus bounded by its Cesàro mean, which tends to zero: split at a fixed R, divide the finite initial integral by T, and bound the tail by sup_(t≥R)|ε(t)|. The constant contribution is A for ω=0 and tends to zero otherwise. The averaged exponential at frequency λ−ω is1 when λ=ω and `(exp(i(λ−ω)T)−1)/(i(λ−ω)T)` otherwise; its modulus is at most1 and it tends to zero in the latter case. Dominated convergence on the counting measure weighted by |cλ| proves (V1). Uniform absolute convergence justifies termwise integration before that limit.

Consequently A and all collected coefficients are unique. Multiplication by e^(iβt) shifts frequencies, and any shifted zero frequency is absorbed into the constant term; absolute summability is preserved. Finite linear combinations give sine/cosine multiplication. If φ(y)=g(log y), this proves the source's logarithmic-average coefficient formulas on printed45–47 in the enlarged no-gap class.

Ordinary averaging also preserves this class. Integrate from1 to y and divide by y. Each exponential y^(iλ) becomes `(y^(iλ)−1/y)/(1+iλ)`; the new coefficient is cλ/(1+iλ), of modulus at most|cλ|. The sum of the discarded constants is O(1/y), and the average of ε(log y) tends to zero. The constant A is unchanged up to a term tending to zero. Thus no small denominator is introduced by ordinary averaging. In contrast, an indefinite logarithmic antiderivative introduces1/λ and need not have absolutely summable coefficients; the averaged limit (V1) does not require that antiderivative expansion.

**Scope and prior status.** This is an elementary modern reconstruction/generalization of PAPER-H404§§35–41, not a claim of a new harmonic-analysis theorem. No statement is made for a conditionally summable Fourier/zero series. Independent reviewer `/root/li_skeptic` read the actual source43 and §§35–41 OCR, and checked (V1) with the stated local-integrability and duplicate-frequency qualifications. This is an independently checked local lemma, not an independent audit of the whole PNT proof. Root review was requested.

## 2. A precise qualification to the stated class closure

Source printed43 says its nonzero frequencies do not approach zero, and then §36 claims closure under multiplication by an arbitrary fixed sine/cosine. If the frequency condition is interpreted only as a gap at0, with arbitrary finite accumulation elsewhere allowed, literal closure is false.

For β=1 put

\[
 P(t)=\sum_{n\ge2}2^{-n}\cos((1+1/n)t).
\]

This is an absolutely summable series whose frequencies are all at least1. Multiplication gives

\[
 P(t)\cos t=\frac12\sum_{n\ge2}2^{-n}
 [\cos((2+1/n)t)+\cos(t/n)].
\]

The frequencies1/n approach0 and have nonzero coefficients. Formula(V1), already proved without a gap, implies no alternative ℓ1 expansion with frequencies bounded away0 can represent the same function plus a term tending to a constant: the averages at frequency1/n would contradict coefficient uniqueness. Thus the class with only a gap at0 is not closed under all fixed modulations.

This is a **qualification of the auxiliary abstract class as literally phrased**, not an error finding about the zeta proof. The zeta-zero frequencies used there have no finite accumulation and tend to infinity; any fixed modulation preserves local finiteness after zero frequencies are collected. Alternatively, remove the gap condition entirely and use(V1). A different historical interpretation of 'ne tendent pas vers zéro' may impose stronger discreteness implicitly. Independent reviewer `/root/li_skeptic` agrees with the gap-only witness and emphasizes the historical wording may mean merely no full-sequence limit0, under which the interleaved new frequencies need not violate the literal condition. Classification: unresolved scope/proof-convention ambiguity, with an explicit witness for the gap-only interpretation. No author-error allegation is elevated.

## 3. Local canonical-product sign inconsistency

The scanned printed26 product is

\[
 F(s)=F(0)e^{\alpha s}\prod_\rho(1-s/\rho)e^{s/\rho}.
\]

Its logarithmic derivative is

\[
 F'(s)/F(s)=\alpha+\sum_\rho[1/(s-\rho)+1/\rho].
\]

The displays on26–27 instead print a minus before1/ρ. This disagrees with direct differentiation of the adjacent product. As a finite witness take F(s)=(1+s)e^(−s), α=0,ρ=−1. The true derivative at0 is0; the printed minus expression gives2. Correcting this sign restores the standard convergent genus-one derivative. The surrounding double-pole integral identity has the usual correct residue structure; no failure of that theorem or the PNT proof is inferred. Classification: localized printed-formula inconsistency, likely typographical, source manifestation specific until compared with the journal first printing. The exact26–27 images are retained. Root has been notified; independent classification review is pending.

## 4. Convergence and historical fairness

The source's double-pole zero sum is absolutely summable; its truncated-kernel proof on27–28 provides a majorant independent of the contour height. This is a valid kind of justification to seek. The normalized zero-tail decay on62 requires absolute summability and exclusion of each boundary zero, not a uniform zero-free strip. The author explicitly declines a convergence rate.

For θ monotone and A(y)=∫_1^y θ(x)dx/x, A(y)~y implies θ(y)~y by two fixed multiplicative increments. This is the same exact elementary unsmoothing mechanism independently reconstructed for Hadamard; the source's printed67–68 takes the large-y limit before the increment tends to zero. It does not justify a shrinking increment without a local quantitative modulus.

The appendix's allegations against von Mangoldt/Cahen are not accepted as verified findings. Conditional sums need a specified ordering; a growing sum of individually small terms may fail to vanish. Neither observation alone proves that a particular original proof made the alleged mistake. Required next evidence: original von Mangoldt1894printed892 and the1895 full version, exact uniform estimates and parameter dependencies, and a comparison with subsequent corrections. The appendix's broader pessimism about explicit formulas is a historical assessment, not a modern mathematical impossibility theorem.

No RH gain or novelty claim is made. The useful output is a precise reusable coefficient-extraction lemma, explicit hypothesis controls, and an executable source-audit continuation task.


## 5. Subsequent comparison with the criticized source

After this first reading, PAPER-H405 accessed/read the whole18-pageFrench1896translation of the1894extract, then originalGerman891–892. The original891exactly decomposes the growing sums;892explicitly invokes kernel14–16 and SectionItheorem2 local zero counting. PAPER-H406 then records the full1895German285–292 estimates, independently inspected after deriving the audit's modern O(log²h/h) reconstruction. These detailed estimates predate the1896criticism. Thus the archive does not confirm the allegation that the argument merely forgot H. This is scoped evidence about the grouped limit, not a whole-paper error/no-error judgment. Independent reconstruction review is underway in `audits/mangoldt_grouped_remainder_corpus_round4.md`.
