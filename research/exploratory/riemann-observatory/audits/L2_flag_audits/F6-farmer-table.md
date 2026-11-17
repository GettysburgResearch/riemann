# Level-2 audit F6-farmer-table

```text
Status: AUDIT (Level 2; adjudicated where flagged)
Scope: the specific issue named below, not the whole paper
Exact sources or dependencies: see 'Sources checked'
What was actually run: independent reading and recomputation by an auditor agent; independent two-sided adjudication where the auditor flagged an issue
Smallest remaining gap: see adjudication
```

**Target.** F6-farmer-table: Farmer, "Jensen polynomials are not a plausible route to proving the Riemann Hypothesis" (arXiv 2008.07206 v1/v2; Adv. Math. 411 (2022) 108781), Section 4.2, Table 4.1 and the accompanying sentence on X_10

**Auditor classification.** `verified_error`

**Final classification.** `verified_error`; public characterization allowed: **True**

**Summary.** Two of the four classical Jensen thresholds in Table 4.1 are wrong for the function the paper defines. All four were recomputed with independent Arb-rigorous code. j=40 (1897) and j=60 (4242) are exactly right. j=10 is off by one: J^{119,0}_{X10,cl} is certified real-rooted, so the maximal d is 119, not 118. That makes the text's "for all larger d [than 118] it has non-real zeros" false at d=119. The j=20 column (749 and "4 first zeros real") is exact for a different function: the cos zeros 9pi/2 and 11pi/2 moved to 20+-i. For X_20 as the text defines it (the two zeros closest to 20, i.e. 11pi/2 and 13pi/2), the maximal d is 477 and the zero count would be 5. A commented-out even-Jensen row in the arXiv LaTeX source independently points to that same 9pi/2, 11pi/2 function for j=20. Both slips are minor and numerical. The paper's qualitative conclusion is unaffected; with the corrected values it reads even more uniformly (d_max ~ 1.19 j^2 for all four j).

**Witness / evidence.** Notation: S(s)=sum_n d!/((d-2n)! d^{2n}) x_n s^n, where x_n=[w^n]X_j(sqrt w). Then J^{d,0}_{X_j,cl}(z)=S((dz)^2). The coefficients are rigorous Arb balls (relative radius below 10^-500), and the code was checked against direct evaluation of X_j.
(1) j=10, X_10 exactly as printed (5pi/2 and 7pi/2 moved). At d=119, deg S=59 and there are 59 strict ball-certified sign changes of S on (0,inf). By the IVT that gives 59 distinct positive roots, so J^{119,0} (degree 118) has only real zeros. The near-colliding pair sits at dz=10.0012 and 10.0531. At d=120 there is a certified non-real root at s=100.5323+1.6006i (dz=10.0269+0.0798i); the root-distance bound is N|S/S'| < 4e-591 < |Im s|. Real-rootedness was also certified for every d=2..119 and non-real roots for every d=120..200. A non-rigorous mpmath cross-check (tail-sum coefficients plus polyroots) agrees: d=118 and 119 real, d=120 non-real at w=0.0069814+0.00011115i.
(2) j=20, literal X_20 (11pi/2 and 13pi/2 moved): J^{477,0} is real-rooted (238/238 sign changes). J^{478,0} has a certified non-real root at dz=19.8912+0.0311i. J^{749,0} has a certified non-real root at dz=19.9285+0.5643i, which directly contradicts "only real zeros for d<=749". Alternative X_20 (9pi/2 and 11pi/2 moved): J^{749,0} is real-rooted (374/374) and J^{750,0} has a certified non-real root at dz=19.5103+0.0115i. That is exactly the printed 749.
(3) j=40 (25pi/2 and 27pi/2): d=1897 real-rooted (948/948), d=1898 certified non-real at dz=40.1486+0.0124i. Matches the printed value.
(4) j=60 (37pi/2 and 39pi/2): d=4242 real-rooted (2121/2121), d=4243 certified non-real at dz=59.9748+0.0087i. Matches the printed value.
Monotonicity lemma: J^{d-1,0} = J^{d,0} - (z/d) J^{d,0}'. For a real-rooted p of degree <= d, d p - z p' = z^{d-1} Ptilde'(1/z) with Ptilde(u)=u^d p(1/u), which is real-rooted by Rolle. So each certified pair (D real-rooted, D+1 not) fixes the maximal d exactly and covers all d.
Provenance: the arXiv v2 LaTeX source has a commented-out row "% J_ev has only real zeros for d<= 59, 365, 951, 2119". My certified even-Jensen maxima are 29 (j=10), 182 (j=20, 9pi/2 and 11pi/2), 118 (j=20 literal) and 475 (j=40). Three of the four commented values fit 2*d_ev+1: 59=2*29+1, 365=2*182+1, 951=2*475+1. The literal j=20 would give 237. This is circumstantial evidence that Farmer's j=20 computations used the 9pi/2, 11pi/2 function.

**Sources checked.**
- arXiv:2008.07206v2 full text (PDF via fetch_arxiv_text.sh), Sections 2-4, Table 4.1
- arXiv:2008.07206v1 full text (17 Aug 2020): identical Table 4.1 values and identical X_j description
- arXiv:2008.07206v2 LaTeX source jensenrh2d.tex (e-print, untarred under scratchpad/l2/farmer_src_v2, not executed): table source plus commented-out J_ev row
- Crossref record 10.1016/j.aim.2022.108781 (Adv. Math. 411 (2022) 108781): no update-to or erratum relation
- Observatory C1 results (jensen_farmer_check.json, jensen_root_certify.json, farmer_j20_alt.json, tables_C1.md), read only for comparison after independent recomputation
- Independent code: /tmp/claude-0/-home-user-riemann/e62aa4cb-6226-5e37-8f52-ea0fa055746f/scratchpad/l2/f6code/farmer_jensen.py, farmer_grid.py, farmer_big.py, farmer_ev.py; outputs in /tmp/claude-0/-home-user-riemann/e62aa4cb-6226-5e37-8f52-ea0fa055746f/scratchpad/l2/f6code/out/

## Auditor report

# L2 audit F6: Farmer (2020/2022), Table 4.1 (classical Jensen thresholds for the model functions X_j)

**Target.** D. W. Farmer, *Jensen polynomials are not a plausible route to proving the Riemann Hypothesis*, arXiv:2008.07206 (v1 17 Aug 2020 "...not a viable route..."; v2 9 Nov 2022), Adv. Math. 411 (2022) 108781. The audit covers Section 4.2, the X_10 paragraph and Table 4.1.

**Outcome:** `verified_error`. Both errors are minor and numerical, and neither affects the paper's conclusion.
- **j=10:** the printed value is off by one. The certified maximal d is 119, not 118.
- **j=20:** the column belongs to a different function from the one described. It is exactly right for moving 9π/2 and 11π/2, but for the X_20 the text defines (moving 11π/2 and 13π/2) the maximal d is 477.
- **j=40 and j=60:** the printed values 1897 and 4242 are confirmed exactly.

## 1. What the paper says

- (2.2) defines J^{d,n}_{f,cl}(z) = Σ_{j≤d} C(d,j) α(j+n) z^j, where f(z) = Σ α(j) z^j / j!.
- The model function is X_10(z) = cos z · (z²-(10+i)²)(z²-(10-i)²) / ((z²-(5π/2)²)(z²-(7π/2)²)).
- "In words, X_j(z) is the function obtained when the pairs of zeros of cos(z) closest to ±j are moved to ±j ± i."
- "By a direct calculation (we used Mathematica), J^{d,0}_{X_10,cl} has only real zeros for d ≤ 118, and for all larger d it has non-real zeros."
- Table 4.1 gives "the maximal d such that J^{d,0}_{X_j,cl} has only real zeros":

| j | 10 | 20 | 40 | 60 |
|---|---|---|---|---|
| # first zeros real | 2 | 4 | 12 | 18 |
| J cl real for d ≤ | 118 | 749 | 1897 | 4242 |
| Taylor detects for d ≥ | 20 | 60 | 118 | 175 |

v1 and v2 print the same values and the same description. Crossref lists no erratum for the journal version. I did not open the paywalled journal PDF; arXiv v2, dated just before publication, is taken as final.

## 2. Independent recomputation (my own code)

**Coefficients.** X_j(√w) = cos√w · Q(w) / ((w−A)(w−B)), where Q(w) = w² − 2(j²−1)w + (j²+1)², and A, B are the squares of the moved zeros. The Taylor coefficients x_n come from *forward power-series division* in Arb ball arithmetic. This gives the exact series of the entire quotient, and the radii track the large cancellation rigorously. Working precision ran up to 23,500 bits (j=60). I checked the coefficients against direct evaluation of X_j at several points.

This method differs from C1's, which used partial fractions with tail sums.

**Polynomial.** J^{d,0}(z) = S((dz)²), with S(s) = Σ_n d!/((d−2n)! d^{2n}) x_n s^n and deg S = ⌊d/2⌋. J is real-rooted if and only if every root of S is real and ≥ 0.

**Certificates.** Both are rigorous for the true ball polynomial, not for a rounded one.
- *Real-rooted:* N = deg S strict ball-certified sign changes of S on [0, ∞). By the IVT this gives N distinct positive roots.
- *Non-real:* a point r with N·|S(r)/S′(r)| < |Im r|. Since S′/S = Σ 1/(r − r_i), some root lies within that distance of r, so it is non-real.

**Where sample points come from.**
- **j=10:** a non-rigorous root locator (flint acb_poly.roots) picks the points.
- **j=20:** the same locator for most runs. I also re-confirmed d=477/478 (literal function) and 749/750 (alternative function) with the locator-free grid below.
- **j=40 and j=60:** no root-finder at all. The points are guided by the explicit Jensen zeros of cos, t_k = d·tan((2k+1)π/(2d)), plus a fine scan near t ≈ j. This method reproduced every j=10 and j=20 result before I used it.

**Monotonicity lemma (proved here).** J^{d−1,0} = J^{d,0} − (z/d)·J^{d,0}′. For a real-rooted p of degree ≤ d, d·p − z·p′ = z^{d−1}·P̃′(1/z), where P̃(u) = u^d p(1/u). P̃′ is real-rooted by Rolle, so d·p − z·p′ is real-rooted too.

So real-rootedness at D implies real-rootedness for every d ≤ D. Certifying "D real-rooted, D+1 not" therefore fixes the maximal d exactly. I also checked this numerically on 2,906 random cases.

### Results (all certified)

| j | moved zeros | max real-rooted d | first non-real d (witness, dz = d·z) | Farmer |
|---|---|---|---|---|
| 10 | 5π/2, 7π/2 (as printed) | **119** (59/59 sign changes) | 120 (dz = 10.0269 + 0.0798i) | 118 |
| 20 | 11π/2, 13π/2 (**closest to 20**, as described) | **477** (238/238) | 478 (dz = 19.8912 + 0.0311i) | 749 |
| 20 | 9π/2, 11π/2 (alternative) | **749** (374/374) | 750 (dz = 19.5103 + 0.0115i) | 749 |
| 40 | 25π/2, 27π/2 (closest) | **1897** (948/948) | 1898 (dz = 40.1486 + 0.0124i) | 1897 |
| 60 | 37π/2, 39π/2 (closest) | **4242** (2121/2121) | 4243 (dz = 59.9748 + 0.0087i) | 4242 |

Additional checks:
- **j=10, dense sweeps:** real-rooted for every d = 2..119 and non-real for every d = 120..200. This is consistent with the lemma.
- **j=10, separate method:** a non-rigorous mpmath run (tail-sum coefficients plus polyroots) gives the same answer: d=118 and 119 real, d=120 non-real.
- **j=20, literal function:** J^{749,0} itself has a certified non-real root at dz = 19.9285 + 0.5643i, with distance bound 4e-740. So does J^{500,0} and J^{550,0}.
- **Agreement with C1:** the j=10 and j=20 numbers agree with C1's Arb results (C1 used fmpz_poly.complex_roots on a rounded integer polynomial). The j=40 and j=60 certifications are new; C1 had only heat-flow predictions there (1891.9 and 4245.1).

## 3. Findings

**F6a (j=10): verified error, off by one.**
- J^{119,0}_{X_10,cl}, which has degree 118 because α(119) = 0, has only real zeros.
- So the maximal d is 119, and the sentence "for all larger d [than 118] it has non-real zeros" is false at d = 119.
- At d = 119 the two colliding zeros are close but clearly separate: dz = 10.0012 and 10.0531.
- How the slip happened cannot be determined (one possibility is numerical root-finding near this near-double root). The odd/even parity of d does not explain it, because the j=60 transition happens at an odd d (4243).

**F6b (j=20): the table does not match the defined function.**
- Under the paper's stated rule, the two cos zeros closest to 20 are 13π/2 ≈ 20.42 (distance 0.42) and 11π/2 ≈ 17.28 (distance 2.72). For that function the maximal d is 477, and five real zeros would come first (π/2 through 9π/2), not four.
- The printed 749 and 4 both match exactly the function with 9π/2 ≈ 14.14 (distance 5.86) and 11π/2 moved. No reading of "closest to ±j" selects 9π/2.
- Independent corroboration comes from the arXiv LaTeX source. It contains a commented-out row: `% J_ev has only real zeros for d ≤ 59, 365, 951, 2119`.
  - My certified even-Jensen maxima are 29 (j=10), 182 (j=20 with 9π/2, 11π/2), 118 (literal j=20) and 475 (j=40).
  - For j=10, j=20 (9π/2, 11π/2) and j=40, the commented values equal 2·d_ev + 1 exactly: 59, 365, 951. The literal j=20 function would give 237.
  - This points to the j=20 computations, both the classical and the even ones, having been done on the 9π/2, 11π/2 function.
  - The row is unpublished, commented-out material. I use it only as provenance evidence, not as a finding.

**Charitable reading.** The j=20 column is internally consistent and correct for an explicit, legitimate example function. The slip is in the correspondence between the description and the computation, so it is a presentation-level mismatch. Taken literally, though, the printed value is false for the defined X_20, and the witness above is certified.

**Rows not affected.**
- The "# first zeros real" row is right for j = 10, 40 and 60.
- The Taylor row ("detects non-real zero for d ≥") was not audited because the paper does not say what "detects" means. Exploratory mpmath data show that a zero of T_d lies within 0.001 of 20 + i by d ≈ 56–58 under both j=20 functions, so that row does not separate them.

## 4. Impact on the paper's claims

None on the qualitative conclusion.
- With corrected values (119, 477, 1897, 4242) the Jensen thresholds are still 6–24 times the Taylor thresholds (20, 60, 118, 175).
- The corrected column is in fact more regular: d_max/j² = 1.19, 1.19, 1.19, 1.18. The printed 749 (1.87·j²) was the outlier, and it overstated the inefficiency for the function as described.
- The "dispersal of information" argument and the comparison with Chasse's d < T² remain intact.

## 5. Limits and independence

- I wrote and ran all of this code myself. It does share the python-flint 0.9.0 (Arb) library with C1.
- j=40 and j=60 were checked only at the transition (d = 1896–1899 and 4242–4245). The lemma above extends those results to all d.
- Farmer's Mathematica code was not available, so how either slip arose remains speculation.
- **Recommended correction:** either change the j=10 entry and sentence to 119 and the j=20 entries to 477 and 5, or keep the j=20 numbers and state that X_20 moves 9π/2 and 11π/2.

All code is in /tmp/claude-0/-home-user-riemann/e62aa4cb-6226-5e37-8f52-ea0fa055746f/scratchpad/l2/f6code/ (farmer_jensen.py, farmer_grid.py, farmer_big.py, farmer_ev.py; outputs in the out/ subfolder).



## Independent adjudication

**Rationale.** I recomputed every disputed threshold with my own Arb ball-arithmetic code. It derives the Taylor coefficients by a backward recurrence on partial-fraction tails, started from a rigorous alternating-series enclosure. That is a third method, different from the auditor's forward series division and from C1's tail-sum code with a rounded integer polynomial.

Real-rootedness is certified by deg S strict ball sign changes. Non-real roots are certified by a Newton root plus the bound N|S/S'| < |Im r|. I re-derived the hereditary lemma J^{d-1,0} = J^{d,0} - (z/d)J^{d,0}' myself, so a certified pair (D real-rooted, D+1 not) fixes the maximum for all d.

Results:
- **j=10, as printed (5pi/2, 7pi/2 moved):** d=119 is certified real-rooted (59/59 sign changes). d=120 has a certified non-real root at s = 100.5323 + 1.6006i (dz = 10.0269 + 0.0798i). The paper's sentence "only real zeros for d <= 118, and for all larger d it has non-real zeros" is therefore false at d=119.
- **j=20, as defined in words (the two zero pairs closest to 20, i.e. 11pi/2 and 13pi/2):** the maximal d is 477, with a certified non-real root at d=478 (dz = 19.8912 + 0.0311i). J^{749,0} itself has a certified non-real root at dz = 19.9285 + 0.5643i. The printed 749 and "4 first real zeros" are exact for a different function, the one with 9pi/2 and 11pi/2 moved (749 real-rooted, 750 non-real at dz = 19.5103 + 0.0115i).
- **j=40 (1897) and j=60 (4242):** both confirmed exactly.

Defence considered:
- **j=10 "degree" reading.** J^{119,0} has degree 118, so "degree <= 118" would be true. But the table prints odd d values elsewhere (749, 1897), which rules that reading out.
- **j=20 "closest" readings.** No reading of "closest to +-j" selects 9pi/2, which is 5.86 away from 20 when 13pi/2 is 0.42 away. No rule that fits j = 10, 40 and 60 selects it either.
- **Errata and versions.** v1 and v2 are identical on these points, and Crossref shows no erratum.

The strongest mitigation is that the j=20 column is internally coherent for a legitimate model function. The "# first zeros real" = 4 row and the commented-out J_ev value 365 (= 2*182+1; I certified even-Jensen maximum 182 for that function versus 118 for the literal one) both point to it. This is most likely a mismatch between description and computation.

Both slips are minor and numerical, and the paper's qualitative conclusion is unaffected. The corrected thresholds 119, 477, 1897 and 4242 are about 1.18-1.19 j^2 each and remain far above the Taylor thresholds. The witness was produced independently of C1 and of the L2 auditor and is certified, which meets methodology rule 6(i). Public characterization is allowed only in measured form: minor numerical errors in Table 4.1 that do not affect the conclusions.

# Adjudication F6: Farmer (2020/2022), Table 4.1 (classical Jensen thresholds of X_j)

**Target.** D. W. Farmer, *Jensen polynomials are not a plausible route to proving the Riemann Hypothesis*.
- arXiv:2008.07206: v1 dated 17 Aug 2020 ("...not a viable route..."), v2 dated 9 Nov 2022.
- Published in Adv. Math. 411 (2022) 108781. Crossref shows no erratum and no update relation.
- **Section audited:** Section 4.2, the X_10 paragraph and Table 4.1.

**Final classification: `verified_error` (minor, numerical; the paper's conclusions are unaffected).**
- **j=10:** the printed threshold is off by one (119, not 118).
- **j=20:** the column was computed for a different zero pair from the one the text defines.
- **j=40 and j=60:** exactly correct.

**Public characterization:** allowed, in measured wording only (Section 6).

## 1. Source (re-read in v2 PDF text and LaTeX source; v1 identical on these points)

- **(2.2):** J^{d,n}_{f,cl}(z) = Σ_{j≤d} C(d,j) α(j+n) z^j, where f(z) = Σ α(j) z^j / j!.
- **The X_10 formula:** cos z · (z²−(10+i)²)(z²−(10−i)²) / ((z²−(5π/2)²)(z²−(7π/2)²)).
- **The general definition:** "X_j(z) is the function obtained when the pairs of zeros of cos(z) closest to ±j are moved to ±j ± i".
- **The j=10 claim:** "By a direct calculation (we used Mathematica), J^{d,0}_{X_10,cl} has only real zeros for d ≤ 118, and for all larger d it has non-real zeros."
- **Table 4.1:**

| j | 10 | 20 | 40 | 60 |
|---|---|---|---|---|
| # first zeros real | 2 | 4 | 12 | 18 |
| J cl real for d ≤ | 118 | 749 | 1897 | 4242 |
| Taylor detects for d ≥ | 20 | 60 | 118 | 175 |

The LaTeX also contains a commented-out row: `% $J_{ev}$ has only real zeros for $d\le$ & 59 & 365 & 951 & 2119`.

## 2. Strongest defence of the original

1. **j=20.** The printed entries 749 and "4 first zeros real" are exactly right for a legitimate, explicit model function: cos with 9π/2 and 11π/2 moved to 20 ± i.
   - The two printed rows and the commented J_ev row (365) are mutually consistent with that function, so the computation itself was coherent.
   - The slip is in identifying X_20 with the verbal rule. A one-line repair fixes it.
   - Any zero pair near j would illustrate Farmer's point.
2. **j=10, possible degree reading.** J^{119,0} has degree 118 because α(119) = 0. A statement read as "the real-rooted Jensen polynomials have degree ≤ 118" would be true.
3. **j=10, possible numerical cause.** At d=119 the two colliding real roots are only about 4.4e-4 apart in z. That makes machine-precision root-finding fragile, which would explain how the slip arose.

**Assessment of the defence.**
- **Reading 2 fails.** The table prints the odd values d = 749 and 1897, so d is the superscript, not the degree. Under the degree reading those entries would be 748 and 1896.
- **No reading of "closest to ±j" selects 9π/2 for j=20.** 13π/2 lies 0.42 from 20, 11π/2 lies 2.72 away, and 9π/2 lies 5.86 away. Every rule that reproduces j = 10, 40 and 60 also selects 11π/2 and 13π/2 for j=20.
- **No later correction exists.** v1 = v2 on these points, and Crossref lists no corrigendum.
- **Conclusion.** The defence explains how the slips plausibly arose. It does not make the printed statements true for the functions as defined.

## 3. Independent recomputation (adjudicator's own code)

**Coefficients.**
- In w = z², X_j(√w) = cos√w · [1 + c_A/(w−A) + c_B/(w−B)], where c_A = Q(A)/(A−B), c_B = Q(B)/(B−A), and Q(w) = w² − 2(j²−1)w + (j²+1)².
- The coefficient [w^m] of cos√w/(w−A) is g_A(m) = Σ_{n>m} c_n A^{n−1−m}, with c_n = (−1)^n/(2n)!.
- I computed g_A(m) by the **backward** recurrence g(m−1) = c_m + A·g(m), in Arb.
- The recurrence starts from the rigorous enclosure g(M) ∈ c_{M+1}·[1−ε, 1], where ε = A/((2M+3)(2M+4)) < 1. The tail is alternating with decreasing terms, which justifies this enclosure.
- This is a third method. It differs from both the auditor's forward series division and C1's code.
- **Validation:** at five configurations, Σ x_n w^n agrees with direct mpmath evaluation of X_j, to within mpmath's working precision. As a hand check, X_10(0) = 101²/((5π/2)²(7π/2)²) = 1.3678.

**Polynomial.**
- J^{d,0}(z) = S((dz)²), where S(s) = Σ_n d!/((d−2n)! d^{2n}) x_n s^n and deg S = ⌊d/2⌋.
- The working precision was d + 600 bits.

**Certificates (rigorous for the true polynomial inside the coefficient balls).**
- *Real-rooted:* deg S strict ball sign changes of S on (0, ∞). Sample points come from the explicit cos-Jensen zeros d·tan((2k+1)π/(2d)), three per interval, plus a 1e-3 grid on t ∈ [j−4, j+4]. No root finder was used.
- *Non-real:* a Newton point r with N|S(r)/S′(r)| < |Im r|. Because S′/S = Σ 1/(r − r_i), some root of S lies within that distance of r, so that root is non-real.

**Hereditary lemma (re-derived).**
- J^{d−1,0} = J^{d,0} − (z/d) J^{d,0}′.
- For a real-rooted p of degree ≤ d, d·p − z·p′ = z^{d−1} P̃′(1/z), where P̃(u) = u^d p(1/u). P̃′ is real-rooted by Rolle, so d·p − z·p′ is too.
- Hence a certified pair (D real-rooted, D+1 not) fixes the maximal d for all d.

### Results (all certified)

| j | moved zeros | max real-rooted d (sign changes) | non-real witness at D+1 (dz) | root-distance bound | Farmer |
|---|---|---|---|---|---|
| 10 | 5π/2, 7π/2 (printed) | **119** (59/59) | d=120: 10.02690 + 0.07981i (s = 100.5323 + 1.6006i) | 9.8e-227 | 118 |
| 20 | 11π/2, 13π/2 (closest, as defined) | **477** (238/238) | d=478: 19.89116 + 0.03110i | 2.1e-309 | 749 |
| 20 | 9π/2, 11π/2 (alternative) | **749** (374/374) | d=750: 19.51035 + 0.01154i | 4.2e-390 | 749 |
| 40 | 25π/2, 27π/2 | **1897** (948/948) | d=1898: 40.14856 + 0.01239i | 3.6e-726 | 1897 |
| 60 | 37π/2, 39π/2 | **4242** (2121/2121) | d=4243: 59.97477 + 0.00872i | 6.6e-1423 | 4242 |

**Additional checks.**
- **j=10:** every d = 2..119 is certified real-rooted. At d=119 the colliding pair sits at dz ∈ (10.001, 10.002) and (10.053, 10.054). d=121 is also certified non-real.
- **j=20, literal function at d=749:** J^{749,0} has a certified non-real root at dz = 19.92855 + 0.56431i (bound 8e-392), with only 372/374 sign changes. This directly contradicts the printed claim for X_20 as defined.
- **Agreement with earlier work:** every witness agrees to the printed digits with the L2 auditor's and with C1's stored outputs (`jensen_root_certify.json`, `farmer_j20_alt.json`).

### Corroboration of provenance (commented J_ev row)

Even-Jensen polynomial (3.2), in the variable u = d·w. Real-rooted maxima are certified by sign changes; the first failing d is certified non-real by the Newton bound.

| function | max d_ev | 2·d_ev + 1 | commented value |
|---|---|---|---|
| j=10 | 29 (d=30 non-real at dz = 9.9711 + 0.1235i) | 59 | 59 ✓ |
| j=20 alternative | 182 (d=183 non-real) | 365 | 365 ✓ |
| j=20 literal | 118 (d=119 non-real) | 237 | 365 ✗ |

- I did not recompute j=40 even; the auditor reports 475 → 951 ✓.
- 2d_ev + 1 is natural: J_ev^{d} uses Taylor coefficients α(0..2d), so the comparable classical index is 2d+1.
- The commented row is also about half the printed classical row in every column (59/118, 365/749, 951/1897, 2119/4242).
- **Reading of this evidence:**
  - It is circumstantial, because the row is unpublished.
  - Three things point the same way: the printed "4 first zeros", the printed 749, and the commented 365. All fit the 9π/2, 11π/2 function.
  - So Farmer's j=20 computations were very probably done on that function.

### The "# first zeros real" row
- Literal X_20: the real zeros are π/2 through 9π/2, five in all, before the pair 20 ± i (|20 ± i| = 20.02). That gives **5**.
- Alternative function: π/2 through 7π/2, four in all, then 20 ± i (20.02 < 13π/2 = 20.42). That gives **4**, the printed value.
- The rows for j = 10, 40 and 60 (2, 12, 18) are correct.

## 4. Findings

- **F6a (j=10): verified_error, off by one.** The explicit sentence "only real zeros for d ≤ 118, and for all larger d it has non-real zeros" is false at d = 119. That case is certified real-rooted by 59 IVT sign changes for a degree-59 S. The correct maximum is 119, and every d ≥ 120 has non-real zeros.
- **F6b (j=20): verified_error under the stated definition; a description/computation mismatch in substance.** For X_20 as defined (11π/2 and 13π/2 moved):
  - the maximum real-rooted d is 477, not 749;
  - the number of first real zeros is 5, not 4;
  - J^{749,0} has a certified non-real root.

  The printed j=20 entries are exact for X_20 with 9π/2 and 11π/2 moved. **Repair:** either print 477 and 5, or state that X_20 moves 9π/2 and 11π/2.
- **j=40 and j=60:** no issue found. Both values are certified exact.
- **Taylor row:** not audited, because "detects" is undefined in the paper. The auditor's exploratory data suggest this row does not distinguish the two j=20 functions.

## 5. Impact

None on the paper's qualitative argument.
- With corrected values (119, 477, 1897, 4242) the Jensen thresholds are still 6–24 times the Taylor thresholds (20, 60, 118, 175).
- The corrected column is in fact more regular: d_max/j² = 1.19, 1.19, 1.19, 1.18. The printed 749 (1.87·j²) was the outlier, and for the function as described it overstated the inefficiency of Jensen polynomials.
- The "dispersal of information" thesis and the comparison with Chasse's d < T² bound are unaffected.

## 6. Adjudication on the auditor's report

- **Confirmed in full:** the auditor's witnesses and numbers for j = 10, 20 (both functions), 40 and 60, the hereditary lemma, and the even-Jensen provenance for j=10 and both j=20 functions. The j=40 even value was not re-checked.
- **Classification:** I agree with `verified_error`. Rule 6(i) is met: the witness is explicit and certified, and I produced it independently of both C1 and the L2 auditor.
- **Severity:** both errors are minor and numerical. For j=20 the substance is a mismatch between description and computation, so it should be presented as such rather than as a flawed computation.

**Recommended public wording:**
> "Table 4.1 of Farmer (2020/22) contains two minor numerical slips: the j=10 threshold is 119 rather than 118 (J^{119,0}_{X_10} is certified real-rooted), and the j=20 entries (749; 4 real zeros) correspond to moving the zeros 9π/2, 11π/2 rather than the two closest to 20 (for which the threshold is 477 and 5 real zeros come first). The j=40, 60 entries are exact. The paper's conclusions are unaffected."

The cause of either slip cannot be determined, because Farmer's Mathematica code is unavailable. Do not speculate about it publicly.

**Adjudicator's files.**
- Code: /tmp/claude-0/-home-user-riemann/e62aa4cb-6226-5e37-8f52-ea0fa055746f/scratchpad/l2/adj_f6_code/xj.py, /tmp/claude-0/-home-user-riemann/e62aa4cb-6226-5e37-8f52-ea0fa055746f/scratchpad/l2/adj_f6_code/cert.py and /tmp/claude-0/-home-user-riemann/e62aa4cb-6226-5e37-8f52-ea0fa055746f/scratchpad/l2/adj_f6_code/ev.py. Built on python-flint 0.9.0 and mpmath 1.3.0.
- arXiv LaTeX source: /tmp/claude-0/-home-user-riemann/e62aa4cb-6226-5e37-8f52-ea0fa055746f/scratchpad/l2/adj_f6_src/jensenrh2d.tex

