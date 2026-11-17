# Level-2 audit F4-andrade-keating

```text
Status: AUDIT (Level 2; adjudicated where flagged)
Scope: the specific issue named below, not the whole paper
Exact sources or dependencies: see 'Sources checked'
What was actually run: independent reading and recomputation by an auditor agent; independent two-sided adjudication where the auditor flagged an issue
Smallest remaining gap: see adjudication
```

**Target.** F4-andrade-keating: J. C. Andrade and J. P. Keating, "Conjectures for the integral moments and ratios of L-functions over function fields", arXiv:1407.3099v1 (11 Jul 2014), J. Number Theory 142 (2014) 102-148, DOI 10.1016/j.jnt.2014.02.019. Points checked: Theorem 1 (Sec. 5.4), Sec. 5.3, and how later papers cite it.

**Auditor classification.** `correct_but_misinterpreted`

**Final classification.** `correct_but_misinterpreted`

**Summary.** The paper states the conditionality itself. Theorem 1 opens with "Conditional on Conjecture 5". Its proof says it uses "(4.61), which is a conjectural formula". Sec. 5.3 never calls its result a theorem: it says "our conjecture states" and "we conjecture". So the reader's worry that a conditional result is passed off as a theorem does not hold. What remains is presentational: the lead-in to Theorem 1 calls it "the following conjecture", (5.37) has the typo 2^{k(k+1/2)}, and Lemma 5 assumes a pole of residue 1 while zeta_A(1+s) has residue 1/log q (the (log q) factors in (5.37) correct for this). I checked the content independently with sympy: Theorem 1's leading coefficient prod_{j<=k} j!/(2j)! for k=1..4, and the Euler factors (5.23) and (5.28) against (3.6). Both agree exactly. In about 15 citing papers read in full text and the Semantic Scholar citation snippets, every later paper treats the result as conjectural. None cites Theorem 1 or Sec. 5.3 as unconditional. Later work has since proved Conjecture 5 for each fixed k when q is large enough: Bergstrom-Diaconu-Petersen-Westerland (2302.07664) combined with Miller-Patzt-Petersen-Randal-Williams (2402.00354, Thm 1.6). Earlier results cover k<=3 (k=1 by Hoffstein-Rosen and Andrade-Keating 2012; k=2,3 by Florea, with q = 1 mod 4 in the Andrade-Keating and Florea results as cited). In those ranges Theorem 1 now holds without condition.

**Witness / evidence.** This finding is not an error claim, so no counterexample is needed. Evidence that the conditionality is stated, from arXiv:1407.3099v1 (text extract lines 1717-1832):
- Lead-in to Sec. 5.4: "The main result is the following conjecture:"
- Then: "Theorem 1. Conditional on Conjecture 5 we have that as g -> infinity ... sum_{D in H_{2g+1,q}} L(1/2,chi_D)^k ~ |D|/zeta_A(2) (log_q|D|)^{k(k+1)/2} A(1/2;0,...,0) prod_{j=1}^k j!/(2j)!"
- In the proof: "Using (4.61), which is a conjectural formula, with alpha_1..alpha_k = 0 and the lemma above".
- Sec. 5.3: "For the third moment, our conjecture states that ..." and "identifying the coefficient of x^6, we conjecture (5.27)".
- Other results are labelled the same way: Sec. 5 opens with "we use Conjecture 5 to obtain explicit conjectural formulae". Theorem 2 reads "Assuming Conjecture 8", and Theorem 3 reads "Assuming the Ratios Conjecture 8".

Independent sympy check (python3 -I, scripts in /tmp/claude-0/-home-user-riemann/e62aa4cb-6226-5e37-8f52-ea0fa055746f/scratchpad/l2/ak_scripts/):
- Leading coefficient of the k-fold residue Q_k(x) from (3.4), with A normalised to 1, compared with prod j!/(2j)!: k=1 gives 1/2 and 1/2; k=2 gives 1/24 and 1/24; k=3 gives 1/2880 and 1/2880; k=4 gives 1/4838400 and 1/4838400.
- The Euler-factor differences (local(k) minus the paper's formula) are 0 for k=1 (P(1)), k=2 (5.23) and k=3 (5.28).
- Each local factor is a product of positive terms, so A(1/2;0,...,0) > 0 and the "~" in Theorem 1 is non-degenerate.
- mpmath shows that Bui-Florea's "Conjecture 1.1" constant 2^{-k/2} G(k+1) sqrt(Gamma(k+1)) / sqrt(G(2k+1) Gamma(2k+1)) equals prod j!/(2j)! for k=1..6. Their conjecture therefore restates Theorem 1's leading term, and they label it a conjecture.

Citation evidence (verbatim fragments from full texts):
- Florea 1507.02640: "For the third moment, Andrade and Keating [3] conjecture that ... 1/(2880 zeta(2)) A_3 ..."
- Florea 1609.01262: "According to conjectures of Andrade and Keating, we expect ..."
- Bui-Florea 1609.05363: "Concerning the leading terms, their conjecture reads Conjecture 1.1"
- Rubinstein-Wu 1407.1018: "Conjecture 2.1 (Andrade-Keating)"
- 2010.07214: "Andrade and Keating [4] conjectured that I_k(g) ~ C_k |D|(log_q|D|)^{k(k+1)/2}"
- 2109.05708: "Andrade and Keating [3] conjectured that ..."
- BDPW 2302.07664: "obtained the corresponding conjectural asymptotics for all moments"; Sec. 12.1.4: "Andrade and Keating [AK14, Conjecture 5] made the weaker conjecture ..."
- MPPRW 2402.00354: "See [AK14, Conjecture 5] ... Theorem 1.6 shows that ... for all sufficiently large (but fixed) q."

**Sources checked.**
- arXiv:1407.3099v1 full text (only arXiv version; text extract /tmp/claude-0/-home-user-riemann/e62aa4cb-6226-5e37-8f52-ea0fa055746f/scratchpad/fulltext/arxiv/1407.3099/text.txt): Sec. 1.5, Sec. 3 (Conjectures 5-6, Remark 3), Sec. 5.1-5.4 (Theorem 1, Lemma 5, (5.37)), Sec. 6 opening, Sec. 7 Theorems 2-3
- Crossref record 10.1016/j.jnt.2014.02.019 (JNT 142, 102-148; no update-to/erratum relation listed)
- ScienceDirect landing page (blocked by captcha; published version NOT inspected)
- Semantic Scholar citations API for arXiv:1407.3099 (60 citing records, citation contexts)
- arXiv:2302.07664 Bergstrom-Diaconu-Petersen-Westerland (Sec. 1.1.11-1.1.14, 1.2.8, 12.1.4)
- arXiv:2402.00354 Miller-Patzt-Petersen-Randal-Williams (Theorem 1.6 and surrounding discussion)
- arXiv:1507.02640 Florea, second and third moment
- arXiv:1609.01262 Florea, fourth moment
- arXiv:1505.03094 Florea, first-moment error term
- arXiv:1609.05363 Bui-Florea, hybrid Euler-Hadamard (Conjecture 1.1)
- arXiv:1407.1018 Rubinstein-Wu (Conjecture 2.1 and statement of AK12 with q = 1 mod 4)
- arXiv:1810.01303 Sawin (no AK14 phrasing found in extract)
- arXiv:2010.07214
- arXiv:2409.02876
- arXiv:2109.05708
- arXiv:2110.00477 (even characteristic; same 'Theorem ... Conditional on Conjecture' template)
- arXiv:1807.06347 Andrade-Jung-Shamesaldeen (same template, Theorem 4.1 'Conditional on Conjecture 2.2')
- arXiv:1909.08953 Andrade-Shamesaldeen
- Semantic Scholar context snippets for 2202.08783, 2402.01214, 2511.14563, 2607.06022, 2609.12764, 1404.2435, 2109.10396, 1908.04078
- Independent sympy/mpmath checks: leading coefficient of Q_k (k=1..4), Euler factors (5.23)/(5.28) vs (3.6), Bui-Florea constant identity (k=1..6)

## Auditor report

# L2 audit: F4-andrade-keating

**Paper:** J. C. Andrade and J. P. Keating, *Conjectures for the integral moments and ratios of L-functions over function fields*.
- arXiv:1407.3099v1 (11 Jul 2014). This is the only arXiv version.
- Published in J. Number Theory 142 (2014) 102-148, DOI 10.1016/j.jnt.2014.02.019.
- Crossref lists no erratum or update. The publisher's page was blocked by a captcha, so **the published version was not inspected**. Everything below refers to arXiv v1.

**Reader's flag:** "Theorem 1 and Sec 5.3 are conditional on Conjecture 5 despite being labeled Theorem."

**Classification:** `correct_but_misinterpreted`, with minor `typo_or_presentation` notes. No adjudication is needed.

## 1. What Theorem 1 says and what it assumes

The statement in Sec. 5.4 (p. 27 of the arXiv PDF) reads:

> **Theorem 1.** *Conditional on Conjecture 5* we have that as g -> infinity
> sum_{D in H_{2g+1,q}} L(1/2, chi_D)^k ~ |D|/zeta_A(2) · (log_q|D|)^{k(k+1)/2} · A(1/2;0,...,0) · prod_{j=1}^k j!/(2j)!.

- **Hypotheses:**
  - q is odd and fixed;
  - k is a positive integer;
  - D runs over monic square-free polynomials of degree 2g+1;
  - Conjecture 5 holds for this k. Conjecture 5 says sum_D L(1/2,chi_D)^k = sum_D Q_k(log_q|D|)(1+o(1)), where Q_k is the k-fold residue (3.4) with the Euler product (3.6).
- **What is proved unconditionally:** the leading coefficient of the polynomial Q_k(x) equals A(1/2;0,...,0)·prod j!/(2j)!. The proof is Lemma 5, which adapts [KO]/[CFKRS], together with #H_{2g+1,q} = |D|/zeta_A(2).
- **What is conditional:** only the link to the actual moments, which is exactly Conjecture 5. The proof says so: "Using (4.61), *which is a conjectural formula*, ...".
- **Is the conditionality disclosed?** Yes, in the theorem statement itself and again in the proof. Sec. 5 opens with "we use Conjecture 5 to obtain explicit conjectural formulae". Section 7 uses the same convention: "Theorem 2. Assuming Conjecture 8", and "Theorem 3. Assuming the Ratios Conjecture 8". This is standard practice for conditional theorems (compare "Theorem (assuming GRH)"). Later papers by Andrade and co-authors use the same template: arXiv:1807.06347, Theorem 4.1, and arXiv:2110.00477, Theorem 6.2, both "Conditional on Conjecture ...".

**Sec. 5.3 (third moment)** is never called a theorem. The text reads "For the third moment, *our conjecture states* that ..." and "identifying the coefficient of x^6, *we conjecture*" (5.27). The flag misreads this section.

## 2. Presentation issues found (minor; none affects the mathematics)

1. **Lead-in wording.** The sentence before Theorem 1 says "The main result is the following *conjecture*:", and the next line is labelled "Theorem 1. Conditional on Conjecture 5 ...". Both labels are defensible: it is a theorem about Q_k and a conjecture about the moments. Still, the mixed wording is probably what prompted the reader's flag.
2. **Typo in (5.37).** The exponent reads 2^{k(k+1/2)}; it should be 2^{k(k+1)/2}. Elsewhere, (5.31) and the final formula are correct.
3. **Normalisation in Lemma 5.** Lemma 5 assumes f has a simple pole of residue 1 at s=0. But zeta_A(1+s) = 1/(1-q^{-s}) has residue 1/log q, and is periodic with further poles at 2 pi i n/log q. The (log q)^{-k(k+1)/2} factor in (5.37) corrects for the residue. Only the neighbourhood of 0 matters, so the extra poles do no harm. This is consistent but not spelled out.
4. **Scope of Remark 3 and Sec. 5.1.** These say the k=1 case of Conjecture 5 "coincides with a theorem in [AK]" (Andrade-Keating 2012). Three later papers state that [AK12] assumed q ≡ 1 (mod 4): Rubinstein-Wu 1407.1018 (line 573), Bui-Florea 1609.05363, and arXiv:2010.07214. Conjecture 5 is stated for all odd q. So the "proves our conjecture when k=1" sentence is, strictly, narrower in q. BDPW 12.1.4 credits k=1 for general odd q to Hoffstein-Rosen 1992. This rests on secondary sources; I did not read [AK12] for this point. It does not touch Theorem 1.

## 3. Independent checks (sympy/mpmath, `python3 -I`)

Scripts are in `/tmp/claude-0/-home-user-riemann/e62aa4cb-6226-5e37-8f52-ea0fa055746f/scratchpad/l2/ak_scripts/` (`lead.py`, `afac.py`).

- **Leading coefficient of Q_k.** In the integrand of (3.4), the factor Delta(z^2)^2 cancels every pole 1/(z_i+z_j) with i<j. What remains is a Laurent polynomial times exp((x/2)·sum z) after the (log q) factors are taken out. The residue is homogeneous, so the leading x-coefficient can be extracted exactly. Result: (-1)^{k(k-1)/2}·2^k/k! × the residue coefficient equals prod_{j<=k} j!/(2j)!:

  | k | computed | prod j!/(2j)! |
  |---|---|---|
  | 1 | 1/2 | 1/2 |
  | 2 | 1/24 | 1/24 |
  | 3 | 1/2880 | 1/2880 |
  | 4 | 1/4838400 | 1/4838400 |

  This confirms the constant in Theorem 1, and the constants 1/(24 zeta_A(2)) in (5.22) and 1/(2880 zeta_A(2)) in (5.27).
- **Euler factors.** Specialising (3.6) at z=0 reproduces each formula exactly (symbolic difference = 0):
  - k=1: prod(1 - 1/(|P|(|P|+1))) = P(1);
  - k=2: (5.23), 1 - (4p^2-3p+1)/(p^4+p^3);
  - k=3: (5.28), 1 - (12p^5-23p^4+23p^3-15p^2+6p-1)/(p^6(p+1)).
- **Positivity.** Each local factor of A(1/2;0,...,0) is a product of positive terms, so A > 0 and the "~" asymptotic is meaningful.
- **Bui-Florea's restatement.** Their "Conjecture 1.1" constant, 2^{-k/2} G(k+1) sqrt(Gamma(k+1)) / sqrt(G(2k+1) Gamma(2k+1)), equals prod j!/(2j)! for k=1..6 (mpmath, 30 digits). Their conjecture is exactly Theorem 1's leading term, and they label it a conjecture.

## 4. How later papers cite it

Sources:
- the Semantic Scholar citation API (60 citing records, with context snippets for about 35);
- full-text greps of 14 citing papers.

**No instance was found of Theorem 1 or Sec. 5.3 being cited as an unconditional result.** Every citation calls the material a conjecture or prediction:

- **Florea, 1507.02640 (Forum Math.):** "Andrade and Keating [3] conjectured formulas for integral moments"; "For the third moment, Andrade and Keating [3] conjecture that ... 1/(2880 zeta(2)) A_3(...)|D|(log_q|D|)^6". This is §5.3, quoted correctly as a conjecture. She then proves the second moment and says her answer "agrees with Andrade and Keating's conjectured formula".
- **Florea, 1609.01262 (fourth moment):** "According to conjectures of Andrade and Keating, we expect ..."; "Andrade and Keating [2] conjectured asymptotic formulas".
- **Bui-Florea, 1609.05363:** "Concerning the leading terms, their conjecture reads **Conjecture 1.1**", which is Theorem 1's leading term (identity verified above).
- **Rubinstein-Wu, 1407.1018:** "Conjecture 2.1 (Andrade-Keating)", followed by numerical evidence. They also note that [AK2] proved k=1 for q ≡ 1 mod 4.
- **2010.07214, 2109.05708, 1909.08953, 1807.06347, 2110.00477, 1908.04078:** all say "conjectured".
- **Bergstrom-Diaconu-Petersen-Westerland, 2302.07664:** "obtained the corresponding *conjectural* asymptotics for all moments"; §12.1.4: "[AK14, Conjecture 5] made the weaker conjecture ...".
- **Miller-Patzt-Petersen-Randal-Williams, 2402.00354:** "See [AK14, Conjecture 5] ...". Their Theorem 1.6 proves the asymptotic Q_r(2g+1) "for all sufficiently large (but fixed) q".
- **Others:**
  - 2409.02876: "the [CFKRS]-[AK14] prediction".
  - 2202.08783: "Shifted Moments Conjecture ... formulated by Andrade and Keating".
  - 1404.2435: "By making use of the ratios conjecture ... Andrade and Keating have derived the one-level density". This is a correctly conditional phrasing of Theorem 3.

## 5. Later status: Theorem 1 is now partly unconditional

- **Each fixed k with q large.** BDPW (stable homology computation) combined with MPPRW (uniform twisted homological stability, Thm 1.6) proves Conjecture 5 for each fixed k (r in their notation) once q is a large enough odd prime power. MPPRW Thm 1.6 has error term O(4^{g(r+1)} q^{-(2g-34)/68}). From that displayed bound, I estimate (my reading, not their statement) that q > 2^{68(k+1)} suffices. MPPRW state that their Q_r "agrees with the conjectured formula". In that range, Theorem 1's leading-order asymptotic holds unconditionally.
- **Small k.** k=1 is known from Hoffstein-Rosen and [AK12] (q ≡ 1 mod 4 as cited). k=2,3 are known from Florea (q ≡ 1 mod 4 as cited). For k=4, Florea proved the top three coefficients.
- **Not covered.** For general fixed q and k >= 4, Theorem 1 remains conditional.

This is later work by other authors, not a correction to AK14.

## 6. Limits of this audit

- Only arXiv v1 was read; the JNT version could not be accessed.
- The citation search is not exhaustive. Semantic Scholar has 60 records and Crossref counts 34. I did not check Google Scholar, MathSciNet, or books and theses.
- Lemma 5 was checked through an independent computation of its constant for k <= 4, not by re-deriving its limit interchange for general k. Since Q_k is exactly a polynomial and the leading part is homogeneous, that interchange is routine.
- The claim that [AK12] needs q ≡ 1 mod 4 comes from secondary sources only.

## Verdict

The paper is open about Theorem 1's conditionality ("Conditional on Conjecture 5" in the statement, and "a conjectural formula" in the proof). Sec. 5.3 is labelled as conjecture throughout. The reader's flag misreads the paper. The only real blemishes are the "following conjecture"/"Theorem 1" wording clash and the exponent typo in (5.37). Later literature cites the material consistently as conjectural, and has since made Theorem 1 unconditional for each fixed k once q is large enough (BDPW + MPPRW).


