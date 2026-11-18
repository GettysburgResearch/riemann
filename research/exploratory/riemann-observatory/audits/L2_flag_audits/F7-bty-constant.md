# Level-2 audit F7-bty-constant

```text
Status: AUDIT (Level 2; adjudicated where flagged)
Scope: the specific issue named below, not the whole paper
Exact sources or dependencies: see 'Sources checked'
What was actually run: independent reading and recomputation by an auditor agent; independent two-sided adjudication where the auditor flagged an issue
Smallest remaining gap: see adjudication
```

**Target.** F7-bty-constant: Bellotti-Trudgian-Yang, "Zero-free regions inspired by work of Heath-Brown", arXiv:2603.21490v1 (23 Mar 2026; the only version on arXiv as of 2026-11-17). Claim: zeta(sigma+it) != 0 for sigma > 1 - 1/(4.896 log t), t >= 3.

**Auditor classification.** `verified_error`

**Final classification.** `verified_error`; public characterization allowed: **True**

**Summary.** I reproduced the numerical chain behind 4.896, as far as it can be checked, using exact rationals and python-flint (Arb) ball arithmetic. The degree-16 polynomial is correct: all a_k >= 0, a0=1, and a1 and a match the paper exactly. The other checks also pass: B(y)=p/q, Lemma 3, Lemma 11 on [0,59], c_n, the Lemma 12 constants, and the final inequality. My chain gives eta log t > 0.2042602, which is about 1/4.89572, so 4.896 is confirmed given the imported results. One finding is a verified error, but it does not carry the proof. Table 1 entry m_5 = 0.00735709 is not a lower bound for min_x G_5(1,x) with the paper's stated rational polynomial. The minimum is 0.0073564919, and there is a rigorous Arb witness. Every Table 1 entry equals the 8-decimal truncation of the minimum for Mossinghoff-Trudgian's original floating-point F16, not the stated polynomial. The other 24 entries are certified valid lower bounds. With m_5 corrected, the sum of (log p) m_p is 0.2354513 > 0.23545, so Lemma 10 and Theorem 1 still hold. Several typo- or presentation-level problems were also found, each with a corrected computation: (a) the Lemma 4 constant c0 is mis-transcribed from Ford, and the paper's later numbers use Ford's correct value; (b) inequality (32) is false as printed, but its conclusion holds; (c) the derivation of the cubic in C1 does not match the printed c*, though C1 itself is valid; (d) the paper uses f(0) to mean eta*w(0); (e) A0 for Lemma 1 is misprinted as (4.8596)^-1; (f) there are small arithmetic slips in the eta^3 error constants. None of these changes 4.896.

**Witness / evidence.** WITNESS for Table 1, p=5. G_5(1,x) = sum_{m=1}^{15} 5^{-m} P(mx), with P(x) = |sum c_k e^{ikx}|^2/14912370 as in Section 4. Arb (128-160 bits) gives:
- G_5(1, 1.6495243310928345) in [0.00735649189978251 +/- 2.1e-18]
- G_5(1, 1.65118408203125) in [0.00735705254735760 +/- 4.6e-19]
Both are below the claimed certified bound m_5 = 0.00735709. A direct |Q|^2 evaluation in mpmath gives the same minimum, 0.00735649189978 at x = 1.64952424.

ROOT CAUSE. For all 25 primes, floor(1e8 * min_x G_p) computed with the Mossinghoff-Trudgian Table 5 F16 coefficients equals the printed m_p exactly. Example: for p=5 the MT minimum is 0.007357092282.

NOT LOAD-BEARING. A branch-and-bound in Arb, with a quadratic Taylor model on 2048 dyadic subintervals of [0, 13/4], certifies min G_p(1,x) >= m_p for the other 24 primes; the smallest margin is 6.8e-9 (p=79). It also certifies min G_5 >= 0.00735649. The certifier is sharp: it certifies 0.2342015 for p=2 and finds a violation at 0.23420151. With the corrected entry, sum (log p) m_p = 0.235451285405 > 0.23545, and kappa times this sum is 0.11868499 > 0.1186.

SECONDARY WITNESS: Lemma 4 constant, a typo. At z = 1000i, Arb gives |W0(z)||z|^3 = 50.011848 +/- 1e-8. The constant as printed gives C(0,1000) = 21.29, so the printed bound fails. Ford (arXiv:1910.08205v5, eq. 7.3) has c0 = 1/(sin(theta) cos^3(theta)), not csc(theta) sec^2(theta). With Ford's c0, the paper's own numbers check: C(x0/eta0, x0/eta0) = 51.954 < 52; C(-1, 1e10) = 50.0697 < 51; C(sigma0/eta0, sigma0/eta0)/x0^3 = 423.93 < 424.

INEQUALITY (32), conclusion still holds. Arb shows the integral over R of U(y)/(x0^2+y^2)^{3/2} is > 34.559, so (32) (< 24) is false as printed. With the true |Re digamma(1/4+iy/2)| the integral is < 23.5908, giving T1(t=0) <= 195.24 eta^3 < 199 eta^3.

C1 IN (42), conclusion still holds. The printed derivation (c* with u^3, times mu^3) gives a cubic coefficient of -0.000985, which falls short of C1 by up to 2.34e-4. The correct Taylor remainder uses c** = integral of u^4 |a1 e^{-u} - a0| w(u) du = 0.0103661 and mu^4. With it, Arb shows the bound exceeds C1 by at least 2.17e-4 on [mu0, 1].

**Sources checked.**
- arXiv:2603.21490v1 full text (fetch_arxiv_text.sh) and LaTeX source Bellotti_Trudgian_Yang_v1.tex (e-print, extracted under scratchpad/l2/bty_src/x)
- arXiv API record for 2603.21490 (only v1, 2026-03-23); WebSearch found no journal version or erratum
- Mossinghoff-Trudgian arXiv:1410.3926v1, Table 5 (F16 coefficients c_k, a_k)
- Ford arXiv:1910.08205v5, Section 6-7, eqs. (6.5)-(7.4) (definition of w, W0 formula, c0 = 1/(sin theta cos^3 theta))
- Independent computations: python-flint 0.9.0 (arb, acb.integral, arb_series), sympy 1.14 (exact Sturm root counts), mpmath 1.3.0, numpy/scipy; scripts in /tmp/claude-0/-home-user-riemann/e62aa4cb-6226-5e37-8f52-ea0fa055746f/scratchpad/l2/bty_work/

## Auditor report

# L2 audit: Bellotti-Trudgian-Yang, arXiv:2603.21490v1, the "4.896" zero-free region

**Claim.** zeta(sigma+it) != 0 for sigma > 1 - 1/(4.896 log t), t >= 3.

**Status.** Preprint. arXiv v1 is the only version as of 2026-11-17; no erratum or journal version was found.

**Scope.** I checked the numerically checkable parts independently: the trigonometric polynomial, the m_p table (Table 1), and every explicit constant in Lemmas 3, 5, 8, 9 and 11-15, ending with the final constant. Exact arithmetic used Python fractions and sympy. Rigorous checks used python-flint/Arb. Values from mpmath are labelled *non-rigorous high precision*.

**Imported, not re-derived** (spot checks are noted where made):
- Ford's W0 bound (Lemma 4)
- Kadiri's explicit formula (Lemma 7) and digamma majorant (31)
- Heath-Brown's Re W >= 0 and his Lemma 4.1
- Lehman's sums over zeros
- Platt-Trudgian's RH verification to 3e12
- Yang's Littlewood-type region (3)
- the starting region with c > 1/6

## Outcome

**The headline constant reproduces.** The paper's chain gives eta log t > 0.2042602, which is about 1/4.89572 and exceeds A0 + eps = 1/4.896 + 1e-100. The margin is 1.18e-5 in eta log t, or 5.96e-5 in the main inequality at t = exp(76.47).

**The final inequality also holds on the whole range,** not only at the endpoint. An interval check over L in [log H, 76.47] gives a minimum of C1 + C2 - 1e-7 - (a kappa w0/2)(A0+eps) of at least 6.86e-5. This replaces the paper's monotonicity argument.

**It survives every correction listed below.** I re-assembled the chain with the paper's printed lemma constants, fixed its internal arithmetic, used log(kt) in place of log t in Lemma 8, and even routed T1(t=0) through the majorant U. The minimum margin over L stays at least 8.57e-5, and the implied constant is about 4.89559.

**One verified error, not load-bearing.** Table 1's m_5 is wrong for the polynomial the paper states.

**Several presentation or typo issues,** each with a corrected computation.

## 1. Trigonometric polynomial (Section 4), reproduced exactly

- The coefficients satisfy sum c_k^2 = 14912370, so a0 = 1.
- a_k = 2 sum_j c_j c_{j+k}/14912370 gives a1 = 865534/497079 and a = sum_{k>=1} a_k = 2919857/828465, exactly as printed.
- All a_k > 0, and a1 > a0. The smallest coefficient is a5 = 19/677835.
- P >= 0 holds automatically, because P is |Q|^2.
- P is a rounded rational version of Mossinghoff-Trudgian's F16. For example, c1/c0 = -2 here versus -2.091 in MT.

## 2. Table 1 (m_p) and Lemma 10

**Rigorous certification.** I ran an Arb branch-and-bound on x in [0, 13/4] (with pi < 13/4), using 2048 dyadic cells, a second-order Taylor model and an enclosure of G'' on each cell. It certifies min_x G_p(1,x) >= m_p for 24 of the 25 primes. The certified margins range from 3.8e-5 (p=2) down to 6.8e-9 (p=79).

**The exception is p = 5.**
- The true minimum is 0.0073564919 at x = 1.6495242.
- Rigorous witness: G_5(1, 1.6495243310928345) in [0.00735649189978251 +/- 2.1e-18], which is below m_5 = 0.00735709.
- The same minimum was found independently by direct |Q|^2 evaluation in mpmath.

**Explanation.** Every printed m_p equals floor(1e8 * min G_p) computed with MT's floating-point F16 (Table 5 of arXiv:1410.3926), for all 25 primes. With the stated rational P, the minima are generally slightly larger (e.g. p=2: 0.2342015 versus 0.2341633), but for p=5 the minimum is smaller. Section 4 defines P, a0, a1 and a from the rational polynomial, so Table 1 was computed from a different polynomial than the one used in the rest of the proof.

**Impact: none on the result.**
- Replace m_5 by the certified value 0.00735649.
- Then sum (log p) m_p = 0.235451285 > 0.23545, compared with 0.235452251 as printed.
- kappa times the corrected sum is 0.1186850 > 0.1186.
- Lemma 10, and hence Theorem 1, are unaffected.

**Other Lemma 10 notes.**
- (a) The Mathematica check that dG_p/dsigma < 0 is unnecessary. Each term p^{-m sigma} P(mx) is >= 0 and decreasing in sigma, so G_p(sigma,x) >= G_p(1,x) holds trivially for sigma <= 1.
- (b) The sum keeps m <= 15 for every p < 100. For p >= 53 this includes prime powers p^m > N = e^59, where Lemma 11's bound f >= kappa*eta*w(0) is not established. I found that Lemma 11's comparison function becomes negative at u ≈ 59.2. The fix is to drop those terms. Each dropped tail is at most 6.8e-26, far below the certified margins of at least 6.8e-9, so this is a presentation gap with no numerical effect.

## 3. Lemma 11 (f(u) >= kappa f(0) on [0,59]): verified rigorously

Write h(u) = -kappa w(0) + w(eta0 u) sum_m kappa_m e^{-d_m u}.
- An Arb series evaluation on 8192 cells shows h >= 0 on [0, 59].
- At u = 0, h(0) = 0 exactly and h'(0) = 1.2038 > 0.
- h(59) = 0.0139, and h becomes negative at u ≈ 59.2, so the cutoff 59 is essentially sharp.

**Notation issue.** The proof actually establishes f(u) >= kappa*eta*w(0), which under Definition 2 equals f(0), not kappa f(0). See section 7.

## 4. Lemma 5 (non-negativity)

- I recomputed B(y) = sum_m b_m B_m(y) from the b_m (8, -71, 255, -354, 199, -1, -29)/859 with eps0 = 1/2000 and c0 = 151/153. The identity B = p/q holds exactly against the printed p and q.
- An exact Sturm count shows p(y) has no real roots, and B(0) = 0.0012248 > 0.
- (2 sigma0 - 1)/eta0 = 138.836 > 138, and 2 sigma0 - 1 = 0.98703 > 151/153.
- With Ford's constant, eta0^2 C(138,138)/((2 sigma0 - 1)^2 w0) = 4.66e-4 < 1/2000.
- The 5.7 constant holds (value 5.6728), and 2 * 5.7 * sum |kappa_m| = 43.04 < 44.
- Lemma 3: p(x) = sum kappa_m x^m has no roots in [0,1] by exact Sturm count (its real roots are -3.372 and 1.910), and p(1) = 433/859.

## 5. Lemma 4 constant: mis-transcribed from Ford (typo)

**Printed** c0 = csc(theta) sec^2(theta). **Ford's** (7.3) has c0 = 1/(sin(theta) cos^3(theta)).

**The printed version is provably too small.**
- As |z| goes to infinity, |W0(z) z^3| tends to |w''(0)| = 50.0697.
- The printed C(nu, r) tends to c0 c3 = 21.19.
- Arb witness at z = 1000i: |W0||z|^3 = 50.0118, while the printed C = 21.29 and Ford's C = 50.31.
- Further spot checks at z = 3000i, -1+3000i, 138 and 138+500i all lie below Ford's C and above the printed C.

**The paper's own numbers match Ford's c0, not the printed one.**

| Claim in paper | Value with Ford's c0 |
|---|---|
| C(x0/eta0, x0/eta0) < 52 | 51.954 |
| C(-1, 1e10) < 51 | 50.0697 |
| C(sigma0/eta0, sigma0/eta0)/x0^3 < 424 | 423.93 |

The Lemma 14 error constants computed with Ford's C are 1016 (printed 1126), 1072 (printed 1188) and 402 (printed 708). These printed values are valid upper bounds.

## 6. Lemma 8 and Lemma 9

**(32) is false as printed.** Arb gives the integral over R of U(y)/(x0^2+y^2)^{3/2} as > 34.559, against the printed < 24.

**The conclusion still holds.** Integrating the true |Re psi(1/4+iy/2)| (Arb, split at its sign change near y* ≈ 2.03206, with an explicit tail bound) gives an integral < 23.5908. Then T1(t=0) <= (52/2pi) * 23.59 = 195.24 eta^3 < 199 eta^3. If the paper's route through U is kept instead, T1 grows to 286.2 eta^3, but the final constant still survives (see Outcome).

**Smaller points.**
- For t >= H, the bound uses eta <= A0/log t, but the s_k have imaginary part kt. The exact eta^2 coefficient in (48) is 52.40 (a + sum a_k log k / log t): this is 187.54 at t = H and 185.76 at log t = 76.47, versus the printed 187. The effect is immaterial.
- The step log(t+y) <= log t in the bound on I2 fails by about 1e-12; immaterial.
- Lemma 9 constants: sum |kappa| = 3243/859, so 623 * sum = 2352.02 < 2353, 14 * sum = 52.85 < 53, and 424 * sum = 1600.74 < 1601.
- (48): 2353 + 1601a = 7995.6 <= 8013, and 53a = 186.79 <= 187.

## 7. "f(0)" notation (presentation)

- Definition 2 gives f(0) = kappa * eta * w(0).
- The proof of Lemma 9 writes eta w(0) times sum kappa_m(...) and then renames it "f(0)".
- Lemma 15 uses "-0.1186 w(0) eta - 1.568 w(0) eta" and divides by a kappa w(0)/2.

All of this is consistent only if "f(0)" in Lemmas 9-11 and 15 means eta*w(0). Read literally, Lemma 9's Gamma-term is off by a factor kappa, and Lemmas 10-11 are weaker than what their proofs give. Under the consistent reading every step checks: Lemma 10 gives at least 0.23545 * kappa * eta * w(0) = 0.11868 eta w(0), which is exactly what Lemma 15 uses. No effect on 4.896.

## 8. Lemmas 12-14

**Lemma 12.** Using the digamma function in Arb, (38) evaluates to -0.0410505 <= -0.041. The total constant is -1.568882 <= -1.568, even after scaling the 1e-10 error by sum |kappa_m|/kappa. Also sum a_k log k = 1.5602480.

**Lemma 13.** With the correct C, C(-1, 1e10) = 50.07 < 51; the remaining estimates are trivial.

**Lemma 14.**
- S1 = -0.68973613 and S2 = -0.81877927 are exact rationals.
- The eta-coefficient is -2.938373 (claimed > -2.939); the eta^2 coefficient is 11.2275 (claimed > 11).
- Arb integration reproduces c0..c3 and c* to all printed digits: 0.8763706262, 0.1200272738, 0.0203537951, 0.0004382722 and 0.0190417514.
- The C1 cubic is inconsistent with its stated derivation. The printed c* (using u^3) together with mu^3 gives c3/6 - c*/18 = -0.000985, which falls short of C1 by up to 2.34e-4.
- The correct remainder from |e^x - cubic| < x^4/18 uses c** (with u^4) = 0.0103661 and mu^4. Then (42) holds with margin at least 2.17e-4 on [mu0, 1], verified in Arb. The exact m=0 term exceeds C1 by at least 4.9e-4. The bound sup (e^x - cubic)/x^4 on [0, d] is 0.05232 < 1/18.
- T1(sigma0) gives a1 w0 T1 = 6.848125 (> 6.848) and a1 w0 (1+mu0) T2 = 15.508 (> 15). T_k' > 0 was checked at three points of [sigma0, 1].
- The eta^3 arithmetic slips: (41) prints -3188 and then -3193, but its own pieces give a1*1188 + 1126 = 3194.6. Lemma 14 prints -3897 where 3193 + 708 = 3901. C2 prints -11896 where 3897 + 8013 = 11910. Each slip changes the final value by at most 1.5e-7 against a margin of 6e-5. The true error constants are far smaller.
- The E1 bound divides by m, which is undefined at m = 0.

## 9. Final constant (Lemma 15)

- C2's eta-coefficient is (0.1186 + 1.568) w0 + 3.909 - 1e-10 = 13.4767, printed as 13.47.
- The expansion coefficients reproduce: 1.0058299, 1.8608874, -4.4105496 and -55.05839, printed conservatively as 1.00582, 1.86088, -4.4106 and -55.0584.
- At L = 76.47 the four-term expression is 1.0292774, printed as "1.02928..."; the direct value of C1 + C2 - 1e-7 is 1.0292874.
- a kappa w0/2 = 5.0390501.
- The printed equality "1.02928/(a kappa w0/2) = 0.204248..." is a misprint: the quotient is 0.2042602, and 0.204248 is 1/4.896 itself. The inequality > A0 + eps holds.
- log(K + T0/H) = 2.77280 < 2.78.
- The parameter table prints A0 = (4.8596)^-1 for Lemma 1, but eta0 = 0.0071093 and sigma0 = 0.9935164 correspond to A0 = (4.896)^-1. With (4.8596)^-1 the final inequality would fail, so this must be a typo.
- Lemma 15 is stated for all t >= H, but its proof only covers t <= exp(76.47). The induction closes once region (3) is used for heights above exp(76.463). This is a presentation gap.
- The crossover with Yang's region is at exp(21.233/4.896) = exp(76.46289), matching the paper's exp(76.463).

## 10. Not reproduced or out of scope

- **Lemma 2 / Theorem 2** (conditional on the thesis constant 19.62). The thesis crossover is at exp(56.6865), and the paper's exp(56.691) is conservative. With Lemma 2's parameters, (2 sigma0 - 1)/eta0 = 137.78 < 138, which breaks a step in Lemma 5. Using Lemma 1's constants, the analogous margin is only 1.9e-6, so Lemma 2 is not verified here.
- **Imported analytic results** were not re-derived. Ford's lemma was only spot-checked numerically at five points.

## Minor typos

- (25): F(2 sigma - 1 + beta0) should read F(sigma - 1 + beta0).
- (47): the factor a1 is missing.
- The proof of Lemma 9 cites Lemma 9 itself instead of Lemma 7.
- Lemma 9 is stated for t >= H but used at t = 0.
- Lemma 1 is stated from t = 3, but one sentence says "2 <= t".

## Scripts

All in /tmp/claude-0/-home-user-riemann/e62aa4cb-6226-5e37-8f52-ea0fa055746f/scratchpad/l2/bty_work/:

| Script | What it checks |
|---|---|
| poly.py | polynomial coefficients |
| certify_mp.py | Arb certification of m_p and the p=5 witness |
| mt_compare.py | Table 1 against MT's F16 |
| lem5B.py | B(y) = p/q and its real roots |
| lem11.py | Lemma 11 |
| lem14_arb.py | c_n, c*, c** and (42) |
| lem8_arb.py | integral (32) and the true digamma integral |
| ford_arb.py | Lemma 4 spot checks |
| final_arb.py, final_B.py | final constant, as printed and with the corrections |
| lemmas.py, lem14.py, corrC.py | constants in mpmath (non-rigorous) |

## Classification rationale

The m_5 entry is an explicit false "certified" claim for the stated polynomial, with a rigorous witness, so it is classified verified_error. It is localized and does not affect Lemma 10 or Theorem 1. Everything else is typo_or_presentation, and each item comes with a corrected computation that preserves 4.896. Under methodology rule (iv), m_5 should go to adjudication before it is described publicly.


## Independent adjudication

**Rationale.** The error is in Table 1, entry m_5 = 0.00735709. The paper calls it a certified lower bound for min_x G_5(1,x), but it is not one for the polynomial P the paper actually states. I checked this by three methods different from the auditor's:
- Exact rational arithmetic gives P_5(-0.0787) = 0.0073564925 < m_5.
- Rigorous root isolation (Arb) of P_5(y) - m_5 finds two simple real roots in [-1,1], at y = -0.08036 and y = -0.07693. This is the very check the paper says it ran in Mathematica, and it fails.
- An Arb ball evaluation at x = 1.6495243310928345 gives G_5 = 0.0073564918997825 +/- 1.5e-23.

The certified true minimum lies in (0.0073564918, 0.0073564919).

Root cause (non-rigorous mpmath check): all 25 table entries equal the minima for Mossinghoff-Trudgian's floating-point F16 (Table 5 of arXiv:1410.3926), truncated down at the printed precision. They were not computed from the rational P. The other 24 entries are certified valid for the rational P by root isolation.

The error does not carry the main result. With m_5 replaced by 0.0073564918, sum (log p) m_p = 0.2354512854 > 0.23545, and kappa times that sum is 0.1186850 > 0.1186. So Lemma 10, Theorem 1 and the constant 4.896 are unaffected.

Public characterization is allowed only in this scoped form: a localized Table 1 entry that is not valid for the stated polynomial, with a corrected value that preserves the theorem. It must never be described as an error in the 4.896 zero-free region.

The auditor's secondary items stay typo_or_presentation:
- Lemma 4's c0 is mis-transcribed from Ford. I confirmed this independently: Ford's (7.3) has 1/(sin theta cos^3 theta), and the printed bound fails at z = 1000i, yet the paper's numbers use Ford's correct constant.
- The printed quotient "0.204248..." should be 0.2042607.
- The other secondary items were not re-verified by me.

# Adjudication: Bellotti-Trudgian-Yang, arXiv:2603.21490v1, the 4.896 zero-free region

**Version status.** The arXiv API lists only v1 (published and updated 2026-03-23, "26 pages", no journal-ref). I found no erratum or author correction.

**Sources checked.**
- The LaTeX source, downloaded into a fresh directory (`Bellotti_Trudgian_Yang_v1.tex`). This confirmed the c_k, the claims in (35), Table 1 and Lemma 4 as printed.
- The text of MT (arXiv:1410.3926), Table 5.
- The text of Ford (arXiv:1910.08205), (7.3).

## 1. Strongest defense of the original

1. **Table 1 is a correct lower bound for a nearby polynomial.** Every entry is the downward 8-decimal truncation, or truncation at the printed precision, of min_x G_p(1,x) computed with MT's floating-point F16 (Table 5 of 1410.3926). The paper explicitly calls its P "a rational version" of that polynomial. So Table 1 is not a careless value. It was computed with the polynomial that the rational P approximates.
2. **Could a different reading of G_p save m_5?** I checked the alternatives, and none does.
   - G_p(sigma,x) = sum_{m<=15} p^{-m sigma} P(mx), with every term >= 0 and non-increasing in sigma. The relevant minimum is therefore at sigma = 1, as the paper says.
   - For p = 5, every m <= 15 has 5^m < e^59, so no terms drop.
   - x = t log p ranges over all of R, so the minimum over x is the right quantity.
   - The proof of Lemma 10 explicitly uses "P(x) be defined as above", meaning the rational P with a0 = 1, a1 = 865534/497079 and a = 2919857/828465. The same a and a1 enter the final constant.

   So the table must be a valid bound for the rational P.
3. **Short repair, and it works.** Replace m_5 with the certified value 0.0073564918. The Lemma 10 total still exceeds 0.23545 (see Section 3), so the paper's Lemma 10 and Theorem 1 stand.

## 2. Independent test of the witness (my methods differ from the auditor's)

All scripts I wrote are in /tmp/claude-0/-home-user-riemann/e62aa4cb-6226-5e37-8f52-ea0fa055746f/scratchpad/l2/adj_bty_scripts/.

**Polynomial reproduced exactly** (`adj_poly.py`, exact rational arithmetic):
- sum c_k^2 = 14912370, so a0 = 1.
- a1 = 865534/497079 and a = 2919857/828465.
- All a_k >= 0, with min a_k = a5 = 19/677835, and a1 > a0.
- P >= 0 holds because P = |Q|^2.

**Witness A: exact rational evaluation in the paper's own variable y = cos x** (`adj_exact5.py`).
- P_5(y) is built exactly as sum_l b_l T_l(y), with degree 240 and rational coefficients.
- P_5(-787/10000) = 0.0073564924813, computed exactly as a rational, which is < 0.00735709.
- At y = -3145868087/40000000000, P_5 = 0.00735649189978251, also < m_5.
- No floating point is involved.

**Witness B: the paper's own certification method fails** (`adj_roots.py`).
- I ran rigorous complex-root isolation (python-flint `fmpz_poly.complex_roots`, Arb) on the integer polynomial with the same roots as P_5(y) - 0.00735709.
- It finds exactly two simple real roots in [-1,1]: y = -0.0803554635874732 +/- 1.2e-17 and y = -0.0769305498446767 +/- 1.4e-17.
- So the paper's stated check, "P_p(y) - m_p > 0 on [-1,1] by exact real-algebraic verification", is false for p = 5.

**Witness C: Arb ball evaluation in the x variable.**
- The trigonometric form and the |Q|^2 form agree.
- G_5(1, 1.6495243310928345) = [0.0073564918997825078941 +/- 1.5e-23].
- G_5(1, 1.6495) = [0.0073564920188629631649 +/- 2.9e-23].
- G_5(1, 1.65118408203125) = [0.0073570525473576 +/- 3.6e-23].
- All three values are < 0.00735709. This matches the auditor's numbers to every printed digit.

**Certified true minimum** (`adj_corr.py`, root isolation).
- P_5 - 0.0073564918 has no real roots in [-1,1], and P_5(0) > m_5, so P_5 > 0.0073564918 on [-1,1].
- P_5 - 0.0073564919 has two real roots near y = -0.07865.
- Hence min_x G_5(1,x) lies in (0.0073564918, 0.0073564919).
- The printed m_5 is too large by 6.0e-7.

**The other 24 entries are certified valid** (`adj_roots.py`, all 25 primes).
- For every p != 5, P_p(y) - m_p has no real roots in [-1,1], and P_p(0) - m_p > 0.
- This is a different method from the auditor's Taylor-model branch-and-bound, and it reaches the same conclusion.

**Root cause, non-rigorous mpmath with a dense grid plus Newton refinement** (`adj_mt.py`).
- With MT's Table 5 a_k, the downward truncation of min G_p at the printed precision equals Table 1 for all 25 primes. For p = 5, the MT minimum is 0.00735709228.
- With the rational a_k, the minima are generally larger, e.g. p = 2: 0.2342015 versus 0.2341633. p = 5 is the only prime where the minimum is smaller: 0.0073564919.
- The rational P's coefficients differ from MT's. For example, a5 = 2.8e-5 versus MT's 9.4e-13, and sum a_k = 3.52442 versus 3.52332.

## 3. Impact (non-load-bearing), verified

I used Arb with python-flint 0.9.0.
- The printed sum (log p) m_p = 0.235452251068.
- With m_5 = 0.00735649, the corrected sum = 0.235451285405 +/- 5e-16, which is > 0.23545 with a margin of 1.29e-6.
- kappa times the corrected sum = (433/859) x 0.2354512854 = 0.118684990 > 0.1186.
- So the conclusion of Lemma 10 (>= 0.1186 f(0), in the paper's normalization) is unchanged. Theorem 1, with the constant 4.896, is unaffected by this entry.

## 4. Secondary items (independently re-checked where noted)

- **Lemma 4 constant: typo, confirmed.**
  - Ford's (7.3) reads c0 = 1/(sin theta cos^3 theta). The paper prints csc theta sec^2 theta.
  - At theta = 1.1338 these are 14.56 and 6.16.
  - With the printed c0, C(-1, 1e10) = 21.19 and C(0, 1000) = 21.29.
  - Rigorous analytic Arb integration of the Laplace transform gives |W0(z)||z|^3 = 50.0118 at z = 1000i (also 50.031 at 3000i and 49.21 at z = 138). So Lemma 4 as printed is false.
  - With Ford's c0, C(-1, 1e10) = 50.0697 < 51, which is exactly the value the paper quotes. The downstream numbers therefore use the correct constant.
- **Lemma 15 misprint, confirmed.**
  - a kappa w0/2 = 5.03905.
  - 1.02928/5.03905 = 0.2042607, not the printed "0.204248...". The latter is 1/4.896 itself.
  - The inequality "> A0 + eps" holds, and the implied constant is about 4.89570.
- **Lemma 10 remarks, confirmed by inspection.**
  - The Mathematica derivative check in sigma is unnecessary.
  - For p >= 53 the m = 15 terms have p^15 > e^59 and should have been discarded. Their size is about 1e-25, which is negligible.
- **Not re-verified by the adjudicator:**
  - the auditor's statement that (32) is false as printed (integral > 34.559 versus < 24) while T1(t=0) < 199 eta^3 still holds;
  - the inconsistency in the C1 cubic derivation (c* versus c**);
  - the "f(0)" means "eta w(0)" notation reading;
  - the A0 = (4.8596)^-1 parameter-table misprint;
  - the eta^3 arithmetic slips;
  - Lemma 11 on [0,59];
  - the full final-chain margin of 6.86e-5.

  These are plausible presentation-level findings. They should stay as auditor findings, typo_or_presentation, and should not be characterized publicly unless they are separately re-verified.

## 5. Not reproduced or out of scope

- The imported analytic inputs: Ford's W0 bound (only spot-checked), Kadiri's explicit formula, Heath-Brown, Lehman, the Platt-Trudgian RH height, and Yang's region (3).
- Lemma 2 and Theorem 2 (the conditional thesis constant).

## 6. Decision

**Classification: verified_error.** The error is localized to a single sub-claim and does not carry the result. Table 1's m_5 is presented as a rigorously certified lower bound for min_x G_5(1,x) with the stated rational P, and it is not one. Three independent witnesses show this, including failure of the paper's own stated algebraic check. The headline result is intact.

**Public characterization: allowed, in scoped form only.** Suggested wording:

> "Table 1 entry m_5 = 0.00735709 in arXiv:2603.21490v1 appears to have been computed from Mossinghoff-Trudgian's floating-point F16 rather than the paper's stated rational polynomial. For the stated P, min_x G_5(1,x) = 0.00735649190 (for example, P_5(-0.0787) = 0.0073564925 exactly). With the corrected value, sum (log p) m_p = 0.2354513 > 0.23545, so Lemma 10 and the zero-free region constant 4.896 are unaffected."

It must not be described as an error in Theorem 1 or in the constant 4.896. The Lemma 4 c0 issue may be described as a transcription typo, because its witness is independently verified and the paper's numbers use Ford's correct constant.

