# C3-failure-anatomy: independent skeptic review

Status: skeptic review of the investigator's report `REPORT.md` (materialised from the structured return) and of the code in `experiments/code/C3-failure-anatomy/`. This review makes no claim about RH.

Scope: all 22 structured claims (C3-D1 ... C3-D14, C3-A1, C3-Q1, C3-M1, C3-CG1, C3-D1-scan, C3-TAX, C3-CHECKLIST).

Method:
- Every computation that could be redone was re-implemented with a different algorithm or library. The investigator's scripts were not simply re-run.
- Every quoted primary or secondary source that was reachable was re-opened, and the quotation was located in it.
- Every "THEOREM" proof was re-derived line by line.

Summary verdict: no claim is refuted. 13 claims are upheld as stated. 7 claims are upheld with minor corrections, listed below. In C3-D1-scan the interpretive part needs a substantive correction, while the counts stand. Two side remarks inside C3-D3 could not be checked: the zbMATH/Crossref absence of the fine-structure paper, and r/math and MathOverflow.

## 1. What the skeptic ran (all new code, under `experiments/code/C3-failure-anatomy/skeptic/`)

Outputs are under `experiments/results/C3-failure-anatomy/skeptic/`. Libraries: python 3.13, python-flint 0.9.0, mpmath 1.3.0, sympy 1.14.0, numpy 2.5.3. At most 2 cores were used, with nice 10.

| script | method (how it differs from the investigator's) | runtime | output sha256 |
|---|---|---|---|
| `sk_conrey_li_mpmath.py 2000` | mpmath at 40 digits. Uses the closed form xi'(rho) = rho(rho-1)pi^{-rho/2}Gamma(rho/2)zeta'(rho) instead of Arb power series. The 34th zero comes from mpmath.zetazero, and the chi_4 zero from findroot. Also redoes the t-grid. | 182 s | `a32e7311...9662` |
| `sk_debranges_scan_flint.py 20000` | Arb at 128 bits with the closed-form xi'(rho) and zeta' from the zeta series only. Zero balls come from the certified TSV, not from `acb.zeta_zeros`. Adds an mpmath cross-check on a random sample of 150 zeros. | 169 s | `1ed296ba...7892` |
| `sk_mechanism_check.py` | mpmath full derivative `mp.diff` at mpmath zeros, n <= 200. | ~60 s | `3064599b...adb` |
| `sk_debranges_gram_phase.py 2000` | Reduces the de Branges zero condition to a Riemann-Siegel theta phase (new; see C3-D1-scan). | ~150 s | `04a9ca54...e8f3` |
| `sk_liouville_mobius_prodsieve.py 1e9` | Exact segmented sieve by the integer product of small prime powers: the cofactor n // prod is 1 or a prime > sqrt N. No logarithms and no floats in any decision. Asserts n == cofactor*prod. T(x) lower bound: floor for lambda=+1 terms, ceil for lambda=-1 terms (scale 2^56). Self-test against sympy to 2e5. | 358 s | `bf602b62...8c6f` |
| `sk_witnesses.py` | See the list below. | ~10 s | `9a63fc8a...f1f5` |

The `sk_witnesses.py` sections:
- **zeta_19 zero.** Rouche on a disc with an explicit bound \|F''\| <= sum (log n)^2 n^{-sigma}, instead of Krawczyk.
- **Davenport-Heilbronn zero.** Rouche by Arb ball evaluation on 400 arcs, plus a numerical check of the functional equation.
- **Cheng-Graham sum.** Recomputed in mpmath.
- **Atiyah.** Exact integer matrix for degrees up to 60 (Bareiss determinant), instead of sympy solve.
- **BBM.** mpmath Hurwitz zeta, and an explicit Euler-Maclaurin sum for x >= 1e8.
- **Queme.** Taylor coefficients by a Cauchy-integral trapezoid rule instead of `mpmath.taylor`.
- **Micheas.** Partial products in mpmath.
- **Oliva.** h_n in `np.longdouble`, and an analytic f'(x) with root-finding instead of numerical differentiation and bisection.

Script hashes:
- conrey_li `cf8b1b37...6977`
- scan `e159dbef...c5b0`
- gram `e7387aae...1f70`
- sieve `34f8e0e4...6ebd3`
- witnesses `f74bc70b...1688`
- mechanism `d3185249...ea12`

The investigator's output hashes in `manifest_C3.json` were re-verified and all match.

Negative knowledge, from the skeptic's own runs:
- In `sk_conrey_li_K2000.json`, the field `mechanism_identity_failures: 2000` is an artefact of the skeptic's own tolerance. The closed form for xi' drops the term (prefactor)'·zeta(rho), and that term is about 1e-24 relative when the ordinates have 25 digits. The re-check in `sk_mechanism_check.json` uses exact mpmath zeros and the full derivative, and finds residual 0 with \|Im Xi'\|/\|Xi'\| <= 1.6e-56.
- The first `sk_witnesses` run crashed for two reasons: mpmath's Hurwitz zeta allocates a prime sieve of size a for a = 1e10 (MemoryError), and a symbolic sympy expansion at degree 40 used too much memory. Both were replaced.
- `chengraham` prints `theta<=f'<=1-theta: false`. This is rounding at 40 digits: the range endpoints round to exactly 0.02 and 0.98. Analytically f' = theta + (1-2theta)·sigmoid lies strictly inside (theta, 1-theta).

## 2. Per-claim verdicts

### C3-D1 (de Branges positivity, Conrey-Li): UPHELD WITH CORRECTIONS (minor)

The Conrey-Li text (arXiv math/9812166, sha256 `bdb68ede...`) was re-read.

What the text confirms:
- Theorems 1 and 2 are transcribed correctly, including the hypotheses no real zeros, \|E(z̄)\| < \|E(z)\|, Ē(z̄) = εE(z-i), and strict monotonicity in y.
- The normalisation xi = s(s-1)pi^{-s/2}Gamma(s/2)zeta(s) has no factor 1/2.
- The condition numbers (3.1), (3.3), (3.7) and (3.8) are right.
- Sarnak's numerics-free remark covers F(W) for zeta and for every Dirichlet character.
- The claim that E(z) = xi(1-iz) meets the hypotheses unconditionally is what C-L argue in Sec. 3.1, using only 0 < Re rho < 1. The skeptic re-derived it: in the paired product, each factor is (Re rho+y)^2 + (Im rho-x)^2, which increases in y > 0. E has no real zeros because zeta(1+it) ≠ 0.

All four witness values were reproduced independently in mpmath, to 20 digits:
- -5.3891005071829451814e-69
- -0.00013195729337208344071
- -2.3103490049934834562e-45
- -0.00042234060658023277028

Correction: "a sufficient condition strictly stronger than RH" should read "a sufficient condition for RH that is unconditionally false". The phrase "strictly stronger" only has content if RH is true.

### C3-D1-scan: UPHELD WITH CORRECTIONS (counts upheld; interpretation corrected)

The counts were reproduced independently:
- K=2000: 195 failures, same first indices 34, 71, 106, ... (mpmath).
- K=20000: 2724 failures, of which 195 are at n <= 2000, with 0 undetermined. This used Arb with a different formula and zero source. The mpmath spot check on 150 random zeros with 2000 < n <= 20000 found 0 mismatches.
- The Theorem-2 grid negatives {282, 527.25, 527.5, 527.75, 836.5, 898.75, 899} are identical.

The identity -Re{xi'(rho)xi(1+rho)} = -Xi'(gamma) Im xi(3/2+i gamma) and the alternation of sign Xi'(gamma_n) were verified, with residual 0 for n <= 200.

Dependency to state explicitly: the scan places the zeros on Re s = 1/2 and assumes they are simple. This is justified by the computational verification of RH far beyond gamma_20000 ≈ 18047, but it should be written down.

Correction to "phase-locking has no arithmetic reason to hold": this sentence is wrong as stated. By Stirling, arg xi(3/2+it) = theta(t) + 5pi/4 + arg zeta(3/2+it) + c(t), with \|c(t)\| <= 0.040 for n >= 10 (computed). Here theta is the Riemann-Siegel theta function. The condition is therefore a Gram-type phase condition on theta(gamma_n) + arg zeta(3/2+i gamma_n). Let u_n = theta(gamma_n)/pi - n be the offset of the zero from the Gram grid; in mpmath's indexing Gram's law is u_n in [-2,-1). The failure rate binned by u_n (`sk_debranges_gram_phase_K2000.json`) is:

| u_n bin | failures / zeros |
|---|---|
| u_n < -1.5 | 0/995 |
| [-1.5, -1.25) | 5/645 |
| [-1.25, -1) | 127/297 |
| >= -1 | 63/63 |

So the condition fails essentially when a zero sits in the last quarter of its Gram interval or beyond it. The threshold is u = -5/4 - arg zeta(3/2+i gamma)/pi, and \|arg zeta(3/2+it)\| < 1. The phase does lock, through theta(t), exactly as in Gram's law. The failures are Gram-law-type irregularities, and a slowly rising rate (9.75% to 13.6%) is what Gram-type statistics lead one to expect.

On prior art: no published count of these failures was found, so "possibly new as a statistic" can stand. The search covered the arXiv API, a web search, and the AIM "de Branges' positivity condition" page. However, the statistic should be presented as a shifted-Gram-law statistic and compared with the Gram's-law literature (Titchmarsh; Trudgian, "On the success and failure of Gram's law and the Rosser rule"). That literature also suggests a route to proving infinitely many failures, which the dossier does not currently claim.

### C3-D2 (X.-J. Li 2008): UPHELD WITH CORRECTIONS (minor)

Re-fetched:
- The arXiv history: v1 1 Jul 2008, v2 2 Jul, v3 3 Jul, v4 6 Jul withdrawn "due to mistake on page 29", v5 4 Oct 2024 to v10 12 Oct 2025.
- The v1 and v3 abstracts.
- Tao's comment page; same sha256 `b566f1f6...`.
- The Woit page, which now has a different hash because it is dynamic, but contains the same Connes quotation.

All the quotations were found: (6.9) and the dilation symmetry; Tao's 4 July agreement that the change of definition fixes the problem; the error "after (7.13)"; the 7 July revision on p.18 invertibility and "merely dense"; and Connes on page 29/31 and measure 0.

The status nuance for v5-v10 is correct and important.

Correction: the fetched page timestamps Tao's first comment "2 July, 2008 at 6:28 pm", not 8:28pm.

### C3-D3 (Atiyah 2018): UPHELD (with C3-A1)

Sections 2-3 of the preprint (sha256 `55c05e2f...`) were re-read:
- Property 2.6 and the remark that it is "just the linear approximation" are as quoted.
- So are 3.1-3.3, the step "F(s)=2F(s)", and "T is not the zero polynomial and so it is invertible".

Point (i) holds. Atiyah states that T is a polynomial on every compact convex K, so one can take K convex, containing a disc around 1 and a segment of the critical line. Constancy near 1 then forces T ≡ 1 on that segment, which contradicts the limit Ж ≈ 137 in 2.5.

Point (iii), "proves too much", holds: nothing in 3.1-3.3 uses Re b ≠ 1/2.

The Lipton-Regan blog quotation was found, but its referent is ambiguous because the formulas are rendered as images.

Could not check: the absence of the companion paper from zbMATH and Crossref. Zbl 1442.11090, "Arithmetic physics -- Abel lecture", ICM 2018 Vol. I, 111-118, was confirmed.

### C3-A1 (2.6 forces T constant): UPHELD

The proof was re-derived. The coefficient of s^m in h(2s+s^2)-h(2s) is sum_{m/2<=k<=m-1} c_k C(k,m-k) 2^{2k-m}, and its top term is (m-1)2^{m-2}c_{m-1}. Induction gives c_1 = c_2 = ... = 0. Composition is legitimate because 2s+s^2 has zero constant term.

The skeptic's independent exact check builds the triangular integer system for c_1..c_59 and finds a nonzero Bareiss determinant, so the only solution is c = 0.

### C3-D4 (Bender-Brody-Mueller): UPHELD WITH CORRECTIONS (minor)

The Bellissard comment, the BBM reply and the PRL preprint were re-read:
- Bellissard states that p has deficiency indices n+ = 1, n- = 0, so no self-adjoint extension exists.
- Bellissard states that psi_z is not in L^2 for Re z = 1/2. His "convergence near the origin" refers to the t-variable of the integral representation, which corresponds to x → infinity.
- The BBM reply says these points are "already" in the paper, quotes "We are not able to prove that the eigenvalues of Ĥ are real", and relies on biorthogonal and pseudo-Hermitian arguments.
- The PRL text says "If the analysis ... can be made rigorous to show that Ĥ is manifestly self-adjoint".

Liu 2607.19067 (abstract) and Mueller 1704.04705 (abstract) are as described.

The growth |zeta(rho_1,x+1)||rho_1-1|/sqrt x → 1 was reproduced: 1.00332, 1.000025, 1.00000025, 1.0000000025, 1.000000000025. This used mpmath for x <= 1e6 and an explicit Euler-Maclaurin sum beyond.

Correction: Bellissard's weighted generator is A_alpha = i x d/dx + i(alpha+1)/2. Its constant term is i(alpha+1)/2, which is a shift of i·alpha/2 relative to alpha = 0, not a shift "by i(alpha+1)/2".

The sentence "no Hilbert space has been exhibited" should be qualified "to our knowledge (literature searched: ...)".

### C3-D5 (Turan partial sums): UPHELD

Platt-Trudgian (arXiv 1507.01340) was re-read:
- Theorem 1.1 is exactly as stated.
- Montgomery's psi_N formula is as Platt-Trudgian state it.
- Spira's Duke 1968 result is that one zero in sigma > 1 implies infinitely many.

zbMATH 0176.13904 gives Spira II as Math. Comp. 22, 163-173, so the investigator's pages are right. Platt-Trudgian's own reference list misprints them as 168-173.

The zeta_19 zero was re-certified by a different method: Rouche on the disc of radius 1e-15 around 1.0010955115364762904215 + 600884.2034277757127423324i, with M2 <= 8.706 and \|F'(m)\| = 2.1212. Re > 1 is certified.

### C3-D6 (Mertens, Stieltjes): UPHELD

Literature checked:
- zbMATH 0544.10047: limsup > 1.06, liminf < -1.009, non-constructive.
- zbMATH 0623.10031: exp(3.21e64).
- zbMATH 0063.02974: Ingham, on linear dependence and unboundedness under linear independence.
- Kim-Nguyen text: exp(1.96e19), with Kotnik-te Riele exp(1.59e40) and Saouter-te Riele exp(1.004e33) restated there.
- Hurst text: -1.837625 and 1.826054, with M computed for all x <= 1e16.
- The Stieltjes correction ("not refuted, open") is right.

The independent integer sieve to 1e9 matches every figure exactly:
- M(10^k) for k = 1..9.
- max M = 10246 at 903,087,703, and min M = -8565 at 456,877,618.
- The ratio record 0.46416 at 179,919,749 (M = -6226) for x >= 1e4.
- 0.565685 at x = 200 for x >= 200.

Kim-Rozmarynowycz 2023 (exp(1.017e29)) is an intermediate bound that is omitted. This is not an error.

### C3-D7 (Polya, Turan T): UPHELD

zbMATH reviews were checked:
- 0085.27102 (Haselgrove).
- 1198.11090 (BFM): the first T(n) < 0 at 72,185,376,951,205; L(n) > 0.061867 sqrt n infinitely often; L(n) < 0 for 1e9 <= n <= 2e14.
- 0063.02974 (Ingham), which states the "RH and simple zeros" consequence.

The independent sieve matches exactly:
- First positive L at 906,150,257, where L = 1.
- L(906,180,359) = 1.
- 305,426 positive values, the last at 906,488,079.
- max L = 829 at 906,316,571, and L(1e9) = -25,216.

The skeptic's tighter rigorous bound gives T(x) >= 1.42367e-6 for x <= 1e9, with the minimum of the bound at 456,877,629. This is consistent with the investigator's T >= 1.4205e-6.

### C3-D8 (Cramer, Maier): UPHELD

The Chernoff and Borel-Cantelli sketch was re-derived. The tail sum over x of exp(-c(log x)^{lambda-1}) converges exactly when lambda > 2, so the restriction lambda > 2 is correct and sharp for this argument.

The zbMATH review of Maier (0569.10023) states the Omega_± form for Phi = (log x)^lambda.

The Banks-Ford-Tao text (Sec. 1.1-1.2) contains the k-tuple / mod-p bias explanation and xi = 2e^{-gamma} = 1.1229 for Granville's model.

### C3-D9 (mollifier ceilings): UPHELD WITH CORRECTIONS (minor)

Checked:
- PRZZ text: 0.4088 (Conrey), 0.4105 (BCY), 0.4107 and 0.4128 (Feng), "more than five-twelfths" (0.417293).
- zbMATH 0668.10044 (Conrey, theta = 4/7).
- arXiv metadata for Pearce-Crump: v1 "at least 7%", v2 "more than 6.78%", "Corrected proportion".
- Alpoge-Furman v2 ("Proof discovered autonomously by Claude ...", at least two thirds).
- Lamzouri (67.25%).
- B. Wang (delta_0 = 6.66624e-8, "New method is need to obtain good improvement").

Corrections:
- Ceiling item 3 ("counts zeros of an auxiliary combination via Littlewood's lemma") describes Levinson-Conrey. Hardy-Littlewood and Selberg instead count sign changes of Z(t). The conclusion is the same: neither ever excludes an off-line zero.
- The JFM/Zbl numbers for Selberg 1942 and Hardy-Littlewood 1921 were not re-checked.
- Ceiling item 1 ("kappa < 1 for proven theta") is a tautology, not a ceiling theorem.

### C3-D10 (Oliva 1807.06447): UPHELD

Metadata: v3 is "Withdrawn for expected critical errors in both versions"; the published date is 2018-07-14 and the update date 2018-09-05.

The v1 text was re-read. The skeptic re-derived that Oliva's (3), (1 - e^{-γ}/LL_{n+1} - 1/p)(1 - e^{-γ}/LL_n)^{-1} >= 1 - 1/p, is algebraically equivalent to (1-1/p) loglog N_{n+1} >= loglog N_n. The counterexample hypothesis on A_n drops out entirely.

The four parts of C3-O1 were checked:
- **(a)** h(L) is decreasing because d/dL = (1-1/p)/L - 1/(L - log p) < 0. Oliva's g in (4) substitutes Dusart's lower bound for log N_{n+1} and for log N_n alike, so (3) ⇒ (4), not (4) ⇒ (3). The paper's "(3) is weaker than (4)" is a direction error.
- **(b)** The first-order law was re-derived. Littlewood's Ω_+ for theta(x) - x transfers to primes, because theta(x) - x is locally maximal at primes.
- **(c)** Reproduced in long double: min h = 1.2508e-10 at p = 17,991,383, and all h > 0 for p <= 2e7. The turning points x/(b log b) = 1.12039, 1.08501, 1.0660, 1.04583 were found by analytic f' with root-finding, and f'(b) < 0.
- **(d)** Correct, given Nicolas' dichotomy.

### C3-D11 (Queme 2004.00460): UPHELD

The v2 comment "irrecoverable error paragraph 6 page 4" and the v1 footnote 1 were verified.

Item 6 is on page 4 and performs the termwise limit as described. Nothing in steps 4-6 uses u > 0, so the argument proves too much.

The coefficients |(-v)^k a_k(rho_1+v)| were reproduced by a Cauchy-integral method and agree with the investigator's values to about 16 digits, tending to 1/v = 0.6667.

### C3-Q1: UPHELD

Re-derived:
- The radius of convergence is exactly v. If it were larger, the identity theorem would remove the pole.
- Abel's theorem along the radius gives lim f(rho + v(1-r)) as a finite limit, which contradicts |f| → infinity at a pole.
- The model 1/(z-rho) has every term equal to 1/v, and the sum at rho+eps is 1/eps.

### C3-D12 (Micheas 2607.04338): UPHELD

Verified: the submission history (v1 5 Jul 2026; v2 8 Jul 2026, withdrawn, "Mistakes in main approach. Withdrawn"), and Theorem 1 (C1)-(C5) with S the open critical strip. The paper itself suggests b_n = 1/n.

### C3-M1: UPHELD

Each step was re-derived. tau_1 = t_1 - 1/2 > 0. Strict increase follows from 1/(2n) - 1/(2n+2) > 0. For n >= 2, tau_n >= t_2 - 1/4 = 20.77 > t_1, so the factors lie in (0,1). The factor at n = 1 is (1/4 - t_1)/(1/4 + tau_1^2) ≠ 0, and the product converges absolutely.

The proof does not use RH: if some zeros were off the line, their ordinates would only repeat, and t_n would still be nondecreasing.

An even shorter proof exists: tau_n = t_n and tau_n = t_n - 1/(2n) are both admissible (when the t_n are strictly increasing) but give different zero sets.

The partial products were reproduced in mpmath: -0.0745866117836282, -0.00263220277869048, -0.00163092460323726, -0.00145084405962443 for N = 1, 100, 1e3, 1e4.

### C3-D13 (published-constant corrections): UPHELD

Every quotation was found:
- **Trudgian** (0903.1885): "several errors, which are fortunately corrected by Lehman"; footnote 3 on the 168π misprint; footnote 6 on Rumely's 1.1242; Lehman's corrections to Titchmarsh's explicit Riemann-Siegel error.
- **HPY** (2207.02366): Cheng-Graham Lemma 2 is S <= 1/(πθ)+1, the correct constant is 2/π, the error was reported by K. Ford and J. Arias de Reyna, Hiary's 0.63 becomes 0.77, and HPY's Theorem 1.1 gives 0.618 t^{1/6} log t for t >= 3.
- **Ford** (1910.08205): the version comments for v2-v5 were fetched individually (v2 commentary on (1.6), v3 the Lemma 3.2 proof, v4 (7.3), v5 (8.8), (8.9) and the argument after Lemma 9.2). The footnote says "Lemma 3 is false". Theorem 4 is 1/(8.464 log|t|) in v5 against 8.463 in v1. The constant 57.54 is unchanged.
- **PRZZ** (Feng): the gap reduces θ_F to 3/7, θ_F = 6/11 "validat[es] Feng's claim", and the claim was "not substantiated".
- **Pearce-Crump**: v1 7%, v2 6.78%.

### C3-CG1: UPHELD

The sum was recomputed in mpmath: |S| = 31.59808527367395444157674, matching the Arb ball, against 1/(πθ)+1 = 16.9155 and cot(πθ/2) = 31.8205.

The hypotheses hold: f' = θ + (1-2θ)σ((x-1000)/w) is continuous, strictly increasing, and lies strictly inside (θ, 1-θ).

As the investigator says, this adds only an explicit smooth instance to Landau's 1928 extremal examples.

### C3-D14 (Davenport-Heilbronn): UPHELD

The zero was re-certified by Arb Rouche on a 1e-10 circle around 0.808517182456637385553352 + 85.69934848537759217192927i (worst arc ratio 0.176, and the linearisation's zero lies inside), giving Re - 1/2 >= 0.30851718.

The functional equation Λ(s) = Λ(1-s), with Λ(s) = (5/π)^{s/2}Γ((s+1)/2)f(s), was checked at three points with relative residual about 1e-40 (mpmath). This confirms the period-5 coefficients and κ.

### C3-TAX: UPHELD WITH CORRECTIONS (heuristic classification)

Every code is instantiated by a dossier that was verified above.

Correction on fairness: F15 lists arXiv:2209.01890v58 (Fayed, 58 versions, no comment) beside arXiv:2112.05521v81 (Oukil, whose own comment reads "All previous attempts have failed"). A version count is not a mathematical failure mode. Fayed's paper has no located published critique, so listing it under a failure taxonomy goes beyond what critiques establish (rule (iv) of methodology §6). Either drop it, or state explicitly "version count only; no error identified by us or in the literature".

Also: the codes F1-F15 are not mutually exclusive, and several dossiers carry three to five codes. State that the codes are tags, not a partition.

### C3-CHECKLIST: UPHELD WITH CORRECTIONS (heuristic)

Item 13 says "Mertens (|M|/sqrt x < 0.571 up to 1e16)". This is false without a lower limit: |M(5)|/sqrt 5 = 0.894 and |M(13)|/sqrt 13 = 0.832.

Hurst's 0.571 is the rounded attained extreme q(7766842813) = 50286/sqrt(7766842813) = 0.5706 over his tabulated range. From both sieves, the maximum over 200 <= x <= 1e9 is 0.5657. The item should read "for 200 <= x <= 1e16, |M(x)|/sqrt x <= 0.5706 (Hurst)".

The other items are sound methodological advice and are backed by the dossiers.

## 3. General issues

1. The K=20000 output of the investigator's scan was produced by an earlier code version, as noted in the manifest. The default branch of the current script (no TSV argument) is the same computation, and the skeptic's independent count agrees. No action is needed beyond the existing note.
2. The scans assume the zeros are on the critical line and simple. This is valid by the RH verification to 3e12, but the dependency should be stated in C3-D1-scan.
3. Several primary texts remain at L0/L0+: Turan 1948, Montgomery 1983, Maier 1985, Odlyzko-te Riele 1985, Haselgrove 1958, Turing 1953, Lehman 1970, Cheng-Graham 2004, Stieltjes 1885. The report already says so. The skeptic upgraded nothing to L1 here except via the same secondary sources, but did check the zbMATH reviews of Odlyzko-te Riele, Pintz, Ingham, Haselgrove, Maier, Conrey 1989 and BFM.
4. No claim of RH or of its negation is made anywhere. All finite computations are labelled as finite.

## 4. Sources consulted by the skeptic (beyond the investigator's cached texts)

- arXiv API and abs pages for: 0807.0090 (v1, v3, v4 and history), 1807.06447, 2004.00460, 2607.04338 (history), 2609.15329 (v1, v2), 2608.13637, 2609.02882, 2609.24167, 2607.19067, 1704.04705, 2209.01890, 2112.05521, 2008.07206, 2404.06306, and 1910.08205 (v2-v5 comments).
- Tao's blog comment page (sha256 `b566f1f6...`).
- Woit, Not Even Wrong ?p=707.
- zbMATH: 0544.10047, 0623.10031, 0063.02974, 0085.27102, 0103.03204, 0446.10004, 0668.10044, 0031.30204, 0518.10046, 0966.11039, 1062.11056, 1198.11090, 0569.10023, 1442.11090, 0176.13903, 0176.13904.
- Web search for prior counts of de Branges-condition failures. None was found; results seen included [arXiv math/9812166](https://arxiv.org/abs/math/9812166v1) and the [AIM de Branges positivity page](https://aimath.org/WWN/rh/articles/html/40a).
