# Level-2 audit F2-ng-eighth

```text
Status: AUDIT (Level 2; adjudicated where flagged)
Scope: the specific issue named below, not the whole paper
Exact sources or dependencies: see 'Sources checked'
What was actually run: independent reading and recomputation by an auditor agent; independent two-sided adjudication where the auditor flagged an issue
Smallest remaining gap: see adjudication
```

**Target.** F2-ng-eighth: Ng, Shen and Wong, "The eighth moment of the Riemann zeta function". arXiv:2204.13891, only version v1 (29 Apr 2022). Published in J. Eur. Math. Soc. 28 (2026), no. 10, 4175-4237, DOI 10.4171/JEMS/1568, CC BY 4.0. It imports Theorem 1.2 from the companion paper "Shifted moments of the Riemann zeta function": arXiv:2206.03350 v1, published in Canad. J. Math. 76 (2024) 1556-1586, DOI 10.4153/S0008414X23000548.

**Auditor classification.** `correct_but_misinterpreted`

**Final classification.** `correct_but_misinterpreted`

**Summary.** Our reader's "k>=12" comes from text extraction. The paper's LaTeX source has "Let $k\ge \frac{1}{2}$", and pdftotext prints \frac{1}{2} as "12" (it also prints ζ(1/2+it) as "ζ( 12 + it)"). In Theorem 1.2, k is the exponent on each factor, |ζ(1/2+it+it0)|^k |ζ(1/2+it−it0)|^k. Proposition 3.1 uses k=4 with symmetric shifts α1=t0, α2=−t0 and |t0|<=√T. Every hypothesis of the companion's theorem holds there: RH, real k>=1, |α_i|<=0.5T, |α1+α2| = 0 <= T^0.6, and T large. One minor citation mismatch: the eighth-moment paper quotes the range k>=1/2, but the companion proves only k>=1 (arXiv v1 and CJM alike). This does not matter at k=4, and Curran (arXiv:2303.10123, assuming RH, all exponents >=0) covers the wider range anyway. Theorem 1.1 is conditional on both RH and Conjecture 1, a smoothed quaternary additive divisor conjecture with error O(P^C X^{1/2+ε0}) uniformly for 1<=|r|<<X^{1-ε'}. It gives only I_4(T) ~ (24024 a_4/16!) T (log T)^16, with no power saving.

**Witness / evidence.** (1) LaTeX source of arXiv:2204.13891v1, line 318: "Let $k\ge \frac{1}{2}$ and assume the Riemann hypothesis." The pdftotext output of the same PDF reads "Let k ≥ 12", and the same extraction renders ζ(1/2+it) as "ζ( 12 + it)". The JEMS PDF reads "Let k [glyph] 1=2". (2) Companion arXiv:2206.03350v1, Theorem 1.2 (CJM Theorem 1.3) reads: "Let k ≥ 1 be real. Let α1 and α2 be real-valued functions αi = αi(T) of T which satisfy the bound (1.2) [|α1|,|α2| ≤ 0.5T] and (1.6) |α1 + α2| ≤ T^0.6. Then the Riemann hypothesis implies that for T sufficiently large, I_k(T,α1,α2) ≪_k T(log T)^{k²/2} F(T,α1,α2)^{k²/2}", where I_k = ∫_0^T |ζ(1/2+i(t+α1))|^k |ζ(1/2+i(t+α2))|^k dt. (3) Proposition 3.1 of 2204.13891 (lines 576-660 of the source; pp. 4184-4186 of the JEMS version) applies this with exponent 4 on each factor, α1+α2 = 0, and |t0| <= √T. (4) Exact check with sympy: 4/638512875 = 2^17/16!, 13381/2615348736000 = 107048/16!, and the difference is 24024/16! = g_4, the Keating-Snaith value (g_1..g_4 = 1, 2, 42, 24024). The k=4 exponent k²/2 is 8, and ∫_{1/L}^{1/200} t^-8 dt = L^7/7 + O(1), matching the (log T)^7 step. (5) Non-rigorous mpmath check (high precision, not certified): on Re(s)=0, |g(iu,t)| <= ~1.5(1+(u²+1)/t) on grids with t ∈ {200, 1000, 5000} and |u| <= 3t. This supports the way Lemma 2.2(i) is used in Proposition 3.1.

**Sources checked.**
- arXiv:2204.13891v1 PDF via fetch_arxiv_text.sh (sha256 842e142283d2f06562667a9221594fecaee524d68327aefed402594fd29d2153), full text
- arXiv:2204.13891 LaTeX e-print EighthmomentApril2022.tex (gzip sha256 4408a39e4eb231233235efa2e7923999f34b38a39a8e20776790204bb7e22685): Conjecture 1, Theorems 1.1-1.2, Section 3 (Prop 3.1, Props 3.2-3.3, proof of Thm 1.1), Section 6.1-6.3 (application of Conjecture 1, Lemma 6.3), bibliography
- JEMS published version, ems.press serial-article-files/53325 (sha256 f7c3978bb89fb2d0633473df5408f5388d6a389c976b4218583c928231130c14): Conjecture 1, Theorems 1.1-1.2, Remarks, Prop 3.1-3.3
- arXiv:2206.03350v1 (companion [26]) PDF (sha256 48e5bf264157b59816eff7c6c28b7f10c9f254fed0e6719d489bed33232de5d4): Theorem 1.2, Section 2 tools, Section 3 proof outline, uses of T^0.6
- Canad. J. Math. 76 (2024) 1556-1586 published companion PDF, open access (sha256 26dcfd65dd391386c6727f7302fa27b8400bcd783f3b62923205fa373185d85b): Theorem 1.3, remarks, the (3.17)-(3.18) dyadic step
- arXiv:2303.10123v2 Curran, Correlations of the Riemann zeta function (sha256 0d2cb91d167bf026ea1b3140e3a66c00d64671f3075930f8f1cd67674cc4ee2f): abstract and Theorem 1.1
- arXiv API metadata for 2204.13891 (v1 only) and the Quanli Shen author listing
- Crossref metadata for 10.4171/jems/1568 and 10.4153/S0008414X23000548
- Observatory ledger LED-MOM-13 (frontiers/ledger.jsonl, records_ledger.md) and methodology.md sections 5-6
- Scratch scripts (not project files): /tmp/claude-0/-home-user-riemann/e62aa4cb-6226-5e37-8f52-ea0fa055746f/scratchpad/l2/scripts/ngsw_consts.py and ngsw_gbound.py

## Auditor report

# L2 audit: F2-ng-eighth, Ng–Shen–Wong, "The eighth moment of the Riemann zeta function"

**Outcome: `correct_but_misinterpreted`.** The paper is fine on this point; our reader's note misread it.

**What I did:** read the full text (arXiv v1 PDF and its LaTeX source, plus the published JEMS PDF). I checked Proposition 3.1 line by line against the imported theorem, as published in the arXiv v1 and CJM versions of the companion paper.

## 0. Bibliographic identity (L0)
- **Authors:** Nathan Ng, Quanli Shen, Peng-Jie Wong. Dedicated "In memory of Aleksandar Ivić".
- **arXiv:** 2204.13891, **v1 only** (29 Apr 2022).
- **Published:** J. Eur. Math. Soc. 28 (2026), no. 10, 4175–4237, DOI 10.4171/JEMS/1568, CC BY 4.0.
  - Received 6 Oct 2022, revised 30 May 2024.
  - Crossref gives the publication date as 2025-01-09.
- **Companion paper** (cited as [26] in arXiv v1 and [27] in JEMS): Ng–Shen–Wong, "Shifted moments of the Riemann zeta function".
  - arXiv:2206.03350, v1 only.
  - Canad. J. Math. 76 (2024), no. 5, 1556–1586, DOI 10.4153/S0008414X23000548, open access.
- **Ng's sixth-moment paper** (cited as [25]): Discrete Analysis 2021:6, according to NSW's bibliography. This is secondary confirmation of the ledger's "memory, unverified" venue note.

## 1. Resolving the reader's note ("Theorem 1.2 requires k>=12")
The "k>=12" is a **pdftotext artifact**:
- LaTeX source line 318 reads `Let $k\ge \frac{1}{2}$ and assume the Riemann hypothesis.`
- pdftotext renders `\frac{1}{2}` as "12" throughout; for example ζ(1/2+it) appears as "ζ( 12 + it)".
- The JEMS PDF reads "Let k ≥ 1=2" (the ≥ glyph is lost in extraction).

In Theorem 1.2, k is the exponent on **each** factor:

∫_0^T |ζ(1/2+it+it0)|^k |ζ(1/2+it−it0)|^k dt ≪_k T (log T)^{k²/2} 𝒢(T,t0)^{k²/2}, for |t0| ≤ 0.5T and T large,

where:
- 𝒢 = min{1/|2t0|, log T} if |t0| ≤ 1/200;
- 𝒢 = log(2+|2t0|) if |t0| > 1/200.

Footnote: 𝒢(T,t0) = F(T,t0,−t0) in the companion's notation. The eighth-moment application uses **k = 4**: |ζ|^4·|ζ|^4 = |ζ|^8 at t0 = 0. So the "exponent 4 on each side" is exactly k = 4, which is inside the stated range.

## 2. The imported result, with its exact hypotheses
Companion arXiv v1 Theorem 1.2, which is CJM Theorem 1.3 with the same wording:
- the Riemann hypothesis;
- **k ≥ 1 real**;
- α1(T), α2(T) real with **|α1|, |α2| ≤ 0.5T**;
- **|α1 + α2| ≤ T^0.6**;
- "T sufficiently large", meaning T ≥ T0(k) (Remark (6) in CJM).

Conclusion: I_k(T,α1,α2) := ∫_0^T |ζ(1/2+i(t+α1))|^k |ζ(1/2+i(t+α2))|^k dt ≪_k T(log T)^{k²/2} F^{k²/2}, where:
- F = min{1/|α1−α2|, log T} if |α1−α2| ≤ 1/100;
- F = log(2+|α1−α2|) otherwise.

The implied constant and T0 depend only on k. The proof's estimates are uniform in the shift functions, so the bound holds uniformly in t0. Proposition 3.1 needs exactly that, since it integrates over t0.

## 3. Hypothesis check at the point of use (Proposition 3.1)
Proposition 3.1 (`replacing-I`) shows I_ω − Ĩ_ω = O(εT(log T)^16) under RH, with U = T^{1−ε}. The weight ω is supported in [c1T, c2T]. Theorem 1.2 is invoked three times, always with α1 = t0, α2 = −t0 and exponent 4.

| Hypothesis | At the point of use | Satisfied? |
|---|---|---|
| RH | assumed in Proposition 3.1 and Theorem 1.1 | yes |
| k ≥ 1 (companion), k ≥ 1/2 (as quoted) | k = 4 | yes |
| \|α_i\| ≤ 0.5T | \|t0\| ≤ √T; larger t0 handled by convexity plus decay of G(it0). Apply with T' = c2T, or with dyadic T' ≍ T | yes |
| \|α1+α2\| ≤ T^0.6 | α1+α2 = 0 | yes |
| T ≥ T0(4) | T → ∞ | yes |

The three ranges, each re-derived:
- **|t0| ≤ √T:** 𝒢 ≤ log T, so the integral is ≪ T(log T)^16. Combined with the factor (|t0|²+1)/t, this gives ≪ ε(log T)^17. The bound on (t^{4it0}−U^{4it0})/(it0) is 4 log(t/U) = 4ε log T + O(1).
- **1/200 < |t0| ≤ log T:** 𝒢 ≪ log log T, so the integral is ≪ T(log T)^8 (log log T)^8.
- **|t0| ≤ 1/200:** the integral is ≪ T(log T)^8 min{|2t0|^−8, (log T)^8}.
  - ∫_{|t0|≤1/log T} gives T(log T)^15.
  - ∫_{1/log T}^{1/200} |t0|^−8 dt0 ≍ (log T)^7.
  - Multiplying by ε log T gives εT(log T)^16.

All three ranges check out.

**The theorem's decay in t0 is load-bearing.** With only the uniform bound T(log T)^16, the t0-integral would give εT(log T)^17, which is too large. The smallest input whose failure would break Proposition 3.1 is Theorem 1.2 at k = 4 for |t0| ≤ 1/200. That is the decorrelation case of Chandee's conjecture.

## 4. Smaller observations (none affects the result)
1. **The quoted range (k ≥ 1/2) is wider than what the companion proves (k ≥ 1).**
   - The eighth-moment paper (arXiv v1 and JEMS) states k ≥ 1/2. The companion (arXiv v1 and CJM) proves k ≥ 1.
   - This is a citation-level `typo_or_presentation` issue and does not matter at k = 4.
   - The k ≥ 1/2 range is in any case covered on [T,2T] by Curran (arXiv:2303.10123, Theorem 1.1): assuming RH, for β_k ≥ 0 and |α_k| ≤ T/2, ∫_T^{2T} ∏|ζ(1/2+i(t+α_k))|^{2β_k} ≪ T(log T)^{Σβ²} ∏|ζ(1+i(α_j−α_k)+1/log T)|^{2β_jβ_k}. The CJM version acknowledges Curran in a remark added on 8 Sep 2023.
2. **The [0,T] form for large shifts rests on an under-justified step in the companion; it is repairable.**
   - The companion's core estimate is on [T,2T] (CJM (3.17)). The [0,T] statement is reached by summing dyadic blocks T/2,…,T/2^j down to about √T.
   - At the lower scales the hypotheses |α_i| ≤ 0.5T' and |α1+α2| ≤ T'^0.6 are not re-checked.
   - Repair for the symmetric case, sketched here (not formalised):
     - **|t0| ≤ T^{1/3}:** the dyadic step is valid for T' ≥ 2T^{1/3}. Under RH, |ζ| ≪ t^ε makes the remaining piece O(T^{1/3+ε}).
     - **|t0| > T^{1/3}:** then 𝒢 ≥ (1/3) log T, so the right-hand side is ≍ T(log T)^{k²}. Cauchy–Schwarz plus Harper gives the same bound.
   - Proposition 3.1 does not need the [0,T] form at all. It only needs scales T' ≍ T, where |t0| ≤ √T ≤ 0.5T'. Classification: a presentation-level point in [26]; nothing in the target is affected.
3. **Lemma 2.2(i) is stated with no limit on Im(s).** It is used on Re s = 0 for all t0. A non-rigorous mpmath check (high precision, not certified) gives |g(iu,t)| ≤ ~1.5(1+(u²+1)/t) on grids with t ∈ {200, 1000, 5000} and |u| ≤ 3t. The region |t0| > √T is in any case killed by the decay of G.
4. **Contour radii.** JEMS changes the radii of the contours B_i from (0, 1/10) to (1/100, 1/10). This matches the proof's need for radii bounded away from 0 in the bound for D̃_{f_r}(r).

## 5. Exact conditionality of the main theorem
**Theorem 1.1:** assume **RH and Conjecture 1**. Then I_4(T) ~ (24024 a_4/16!) T (log T)^16. This is an asymptotic only:
- the argument "wins by an ε" (Remark (1) in JEMS, (2) in v1);
- there is no power saving and no lower-order terms, unlike the sixth-moment result [25].

**Conjecture 1** (smoothed quaternary additive divisor conjecture) says: there is a C > 0 such that, for smooth f with support in [X,2X]×[Y,2Y], Y ≍ X, and x^m y^n f^{(m,n)} ≪ P^{m+n},

D_{f;4,4}(r) = (main term: a double contour integral of ζ^4(z1)ζ^4(z2) Σ_q c_q(r)G_4(z1,q)G_4(z2,q)q^{−z1−z2} ∫f(x,x−r)x^{z1−1}(x−r)^{z2−1}dx) + O(P^C X^{1/2+ε0}),

uniformly for 1 ≤ |r| ≪ X^{1−ε'}. This is a square-root-cancellation hypothesis with a polynomial dependence on P. It is open: no unconditional power-saving result is known for D_{4,4}.

**Where each hypothesis enters:**
- **RH:** only in Proposition 3.1, through Theorem 1.2, and in Harper's bound I_4(η0T) ≪ η0T(log T)^16 when the smoothing weight is removed.
- **Conjecture 1:** only in Proposition 3.3 (off-diagonal terms). Its hypotheses are checked in Section 6.2:
  - X = M ≍ N = Y;
  - P = T^{1+ε1}/T0;
  - f = T^{−4ε1} f_r, which satisfies (1.10) by Lemma 6.3;
  - |r| ≪ M^{1−ε1}, with ε' ≤ ε1 < 1/6.
- **Unconditional:** the diagonal term (Proposition 3.2).

The main-term constant checks out exactly: 2^17/16! − 107048/16! = 24024/16!, and 24024 = g_4.

**Author remarks that are claims, not proved here:**
- JEMS Remark (2) says the theorem can be obtained from an averaged version of the conjecture.
- Remark (4) (v1 Remark (3)) says Conjecture 1 alone should give the matching lower bound.

The JEMS version also replaces v1's "no numerical confirmations" with a reference to Nguyen [28]. Nguyen's work concerns d_3 correlations, so it is only indirect evidence for the quaternary conjecture.

## 6. Suggested updates to ledger record LED-MOM-13 (for the integrator)
- Raise the evidence level for the NSW component from abstract-only to full-text L2: Proposition 3.1 and the imported theorem checked.
- Add the venue: JEMS 28 (2026) 4175–4237, DOI 10.4171/JEMS/1568.
- State the conditionality explicitly as "RH + Conjecture 1 (smoothed, error P^C X^{1/2+ε})".
- Record "asymptotic only, no power saving".
- Note the companion: CJM 76 (2024).
- Note that "k≥12" in any extracted text should read k ≥ 1/2.

## Computations
- `/tmp/claude-0/-home-user-riemann/e62aa4cb-6226-5e37-8f52-ea0fa055746f/scratchpad/l2/scripts/ngsw_consts.py`
  - Exact sympy: g_k for k = 1..4, the diagonal and off-diagonal constants, the t^−8 integral.
  - Non-rigorous mpmath: a_4 ≈ 2.1468e−4 from an Euler product truncated at p < 2·10^5.
- `/tmp/claude-0/-home-user-riemann/e62aa4cb-6226-5e37-8f52-ea0fa055746f/scratchpad/l2/scripts/ngsw_gbound.py`
  - Non-rigorous high precision: the gamma-ratio bound from Section 4, item 3.

None of these computations is certified.


