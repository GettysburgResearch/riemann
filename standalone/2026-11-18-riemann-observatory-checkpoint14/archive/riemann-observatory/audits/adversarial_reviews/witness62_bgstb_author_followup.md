# BGSTB author follow-up and versioned correction

Siegfred Alan C. Baluyot, Daniel Alan Goldston, Ade Irma Suriajaya, and Caroline L. Turnage-Butterbaugh, *Pair Correlation of Zeros of the Riemann Zeta Function I: Proportions of Simple Zeros and Critical Zeros*, arXiv:2501.14545, repository DOI 10.48550/arXiv.2501.14545. I read all 16 pages of v3 and compared the theorem statements and correction passages in v1 and v2. This is a whole-work Level 1 read of v3 and targeted checks of its predecessors. The external references' original proofs were outside this task. [ArXiv history](https://arxiv.org/abs/2501.14545) [v3 PDF](../../sources/witness62_bgstb_followup/2501.14545v3.pdf)

## Version and corpus identity

| Version | Submission in arXiv history, UTC | Date on PDF | Scope checked |
|---|---|---|---|
| v1 | 24 January 2025, 14:48:27 | 27 January 2025 | Theorems 1–2, §§2–3 correction, targeted use in §§4–7 |
| v2 | 21 November 2025, 03:36:05 | 24 November 2025 | Theorems 1–2, §§2–3 correction, targeted use in §§4–7 |
| v3 | 1 September 2026, 08:18:04 | 8 June 2026 | Whole work, pp. 1–16 |

The current arXiv comment says the updated version was submitted for publication on 10 June 2026 and is under review. No journal reference or journal DOI is given there. The raw corpus OpenAlex result W4406841235 already supplies candidate CAND-69503A8570C6, previously metadata-only and pending relevance review. Exact title and identifier searches of the curated bibliography and paper records found no duplicate selected entry. The primary relevance is its author correction of a theorem in PAPER-A006, with a distinct later horizontal-multiplicity result. [DataCite DOI](https://doi.org/10.48550/arXiv.2501.14545) [ArXiv metadata snapshot](../../sources/witness62_bgstb_followup/arxiv_history.html)

## Three formulas and the proof repair

Write \(L=\log T\) and \(F_I(x)=\sum_{\gamma,\gamma'\in I}x^{\rho-\rho'}4/(4-(\rho-\rho')^2)\), with zeros counted with multiplicity. The comparisons below hold over \(1\le x\le T\).

1. **Published 2024 formula, documented by the authors' follow-up.** The follow-up quotes the original theorem for \(I=(0,T]\) as
   $$
   \left(\frac{T L^2}{2\pi x^2}+\frac{T}{2\pi}\log x\right)(1+O(L^{-1/2})).
   $$
   This source claim appears in v1 and v2 §2 after (2.3), and in v3 §3 after (3.2). At \(x=cL\) with \(c>0\) fixed, the factorized bound would pin down the order-\(T\) coefficient as \((c^{-2}+\log c)/(2\pi)\), with an \(O(T\log L/\sqrt L)=o(T)\) ambiguity. The authors explain that this dependence on \(c\) is wrong and attribute the source of the issue to Goldston–Montgomery 1987, Lemma 8. The published 2024 formula is attributed here through the authors' account. The Acta Arithmetica PDF remains subscriber-restricted and was not inspected.
2. **Original 2023 preprint formula.** arXiv:2306.04799v1 (1.4) states with \(x=T^\alpha\)
   $$
     \frac{F_{(0,T]}(T^\alpha)}{T L/(2\pi)}
       =T^{-2\alpha}(L+O(1))+\alpha+O(L^{-1/2}),
       \qquad 0\le\alpha\le1.
   $$
   This already has an additive remainder in the \(\alpha\) term, unlike the multiplicative journal formula the authors quote.
3. **Author's corrected initial-segment formula.** The first line of v1/v2 (3.3) and v3 (3.5) gives
   $$
   F_{(0,T]}(x)=\frac{T}{2\pi x^2}(L^2+O(L))+\frac{T}{2\pi}\log x+O(T\sqrt L).
   $$
   This has exactly the remainder structure stated in the 2023 preprint when divided by \(T L/(2\pi)\). For the dyadic range \(I=(T,2T]\), v1/v2 (2.3) and v3 (3.2) state \(T L^2/(2\pi x^2)(1+O(L^{-1/2}))+T\log x/(2\pi)+O(T\sqrt L)\), with the peak remainder deliberately relaxed. This dyadic statement also carries reality, nonnegativity, and inversion symmetry.

The proof of v3 (3.5), pp. 7–8, starts from the original (2.17)–(2.18) and the three terms \(A_1,A_2,A_3\) of the explicit formula. It uses the prime-side square mean from Goldston–Montgomery Lemma 7 or Goldston's thesis Lemma B. Cauchy–Schwarz bounds the terms involving \(A_3\). The \(A_1 A_2\) term is treated directly by integrating \(n^{it}\log(t+2)\) by parts to obtain \(O(L/\log n)\), then summing against \(\Lambda(n)n^{-1/2}\min(n/x,x/n)/x\). This cross term is \(O(L)\), so the auxiliary estimate avoids the factorized error. For (3.2) the proof subtracts the initial-segment formulas at \(2T\) and \(T\) and bounds cross-window pairs using the local ordinate count and Vinogradov–Korobov. [Original preprint (1.4)](../../sources/analytic/2306.04799.pdf) [Follow-up v1 §§2–3](../../sources/witness62_bgstb_followup/2501.14545v1.pdf) [Follow-up v2 §§2–3](../../sources/witness62_bgstb_followup/2501.14545v2.pdf) [Follow-up v3 §3](../../sources/witness62_bgstb_followup/2501.14545v3.pdf)

## What survives and what the follow-up proves

The follow-up explicitly says that applications of the original Theorem 1 such as Lemmas 5 and 7 retain their conclusions. This can be checked at the point where the form factor enters. On integrating the normalized initial-segment formula against the even, supported test \(r\) of original Lemma 5, the additive \(O(L^{-1/2})\) contributes \(O(L^{-1/2}\|r\|_1)\). The term \(L e^{-2\alpha L}\) on \(0\le\alpha\le1\), doubled by evenness, has mass \(1+O(e^{-2L})\) and produces \(r(0)\) for a test Lipschitz near zero. The relaxed \(O(\sqrt L)e^{-2\alpha L}\) remainder of the dyadic result also integrates to \(O_r(L^{-1/2})\) using the same boundedness near zero. Lemma 7 uses \(r(\alpha)=j(\alpha)\operatorname{sech}\alpha\) in that integral. Bounding the weight-removal term then uses the separate unit-window count and \(w(u)-1=u^2w(u)/4\). Thus the statement of Lemma 7, with its far-pair term \(S(T)\) still present, survives the form-factor correction. [Original preprint §§3–5](../../sources/analytic/2306.04799.pdf) [Follow-up v3 footnote 2 and §4](../../sources/witness62_bgstb_followup/2501.14545v3.pdf)

In v3 §§4–5 the authors use \(j(\alpha)\operatorname{sech}(b\alpha)\) and obtain positivity of \(\Re K_b(x+iy)\) in \(|y|<b\). The full box hypothesis on \(T<\gamma\le2T\) ensures \(|\beta-\beta'|<b/L\) for every pair. Thus the proof of v3 Lemma 4 has no far horizontal pairs. Original §6, which handles far pairs allowed by the original hypotheses, is a different step. The follow-up v3 Remark 3 refers to a possible strong-density replacement, citing original BGSTB24 Theorem 3, but gives no fresh estimate for the omitted pairs. The follow-up's own Theorem 3 is an elementary horizontal-multiplicity principle. This does not establish how the published 2024 article handled (6.4), and the authors' footnote about the form-factor correction addresses a distinct issue. [Follow-up v3 Remark 3 and §§4–6](../../sources/witness62_bgstb_followup/2501.14545v3.pdf) [Independent original §6 audit](witness62_bgstb_section6.md)

## Full v3 reading map

- **§1, pp. 1–4.** Theorems 1–2 assert a lower bound on the intersection of simple and critical zeros in the dyadic box. Where v1/v2 gave separate \(2/3\) lower bounds and an intersection lower bound of \(1/3\) as \(b\to0\), v3 gives \(2/3\) for the intersection itself. At fixed \(b=0.3185\) and \(0.001\), the v3 intersection constants are \(0.66666908\) and \(0.67250064\) multiplying \(T L/(2\pi)\).
- **§2, pp. 4–6.** Each height \(g\) has horizontal multiplicity \(H(g)\), the count of zeros at that height with multiplicity. The ordered equal-height count is \(\sum_\rho H(\gamma)\). Reflection forces \(H=1\) to be simple and critical. For \(H=2\), a double critical zero or a pair of simple reflected zeros gives membership in exactly one of the simple and critical sets. For \(H=3\), every zero at that height lies in their union. These facts and truncation of \(2-H,3-H,4-H\) at zero give the three inequalities of Theorem 3.
- **§3, pp. 6–10.** Corrects the published error and proves the dyadic version as detailed above. Lemma 1 gives real nonnegative square formulas on the complex form factor and its purely ordinate counterpart. The application uses the uniform range \(1\le x\le T\).
- **§4, pp. 10–11.** The Fejér or Montgomery–Taylor function divided by \(\cosh(b\alpha)\) supplies the compactly supported test. Integration against (3.2) separates the peak at zero and the linear main term, producing (4.6).
- **§5, pp. 11–14.** The Fourier transform of the cosh ratio is positive on the real axis for \(|y|<b\). Convolution with the nonnegative transform of \(j\) gives strict positivity of the real part of the complex kernel. Integrating by parts twice supplies the decay bound. The identity \(W(u)-1=u^2W(u)/4\) removes the weight in the box at cost \(O(T)\) for bounded \(b\). Remark 6 documents the authors' harmless factor-of-two normalization correction to Tsang's transform.
- **§6 and references, pp. 14–16.** Equal-height pairs contribute at least \(K_b(0)\), so positivity of all pairs yields \(N^\circledast(T)\le(C_b(j)+o(1))T L/(2\pi)\). The Fejér ratio tends to \(4/3\) as \(b\to0\); numerical Montgomery–Taylor ratios supply the fixed-box bounds. Table 1 includes \(b=1\) giving \(0.61748\) with \(j_M\) under the follow-up's box. The result uses the dyadic box, distinct from original Theorem 2's height range and Theorem 3's density hypothesis. [Complete v3 PDF](../../sources/witness62_bgstb_followup/2501.14545v3.pdf)
