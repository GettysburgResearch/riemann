# PR 910 replay: exponent arithmetic of the conditional 139999/160000 refinement

```text
Status: partial independent review, exploration level. This is not an integration verdict.
Reviewed object: GettysburgResearch/riemann draft PR 910, local ref pr910,
  head SHA 670a76c1a3a8f325c43c1755b1cfc24d313a3e3c (`git rev-parse pr910`),
  directory standalone/2026-10-10-quasi-riemann-height-descent/
Scope: exponent arithmetic and the stated geometric adapters ONLY. This covers
  GEOMETRY_PERTURBATION.md (Theorem 1.1), GEOMETRY_ENVELOPE_LIMIT.md, and the exponent
  tables of TAIL_AND_EULER.md Lemma 2.1-2.2. Every imported lemma of the 30 Sep 2026 OpenAI
  manuscript is a black box. Its stated output exponent is transcribed, not re-proved.
Exact sources or dependencies: imported manuscript paper.tex as resident in the pr910 tree
  (standalone/2026-10-07-openai-quasi-riemann-import/upstream/.../build/paper.tex,
  SHA-256 42a5ee0f...a6a3, identical to the hash bound in the PR's REVIEW.md). Its pdftotext
  rendering is scratchpad ext/qrh/paper.txt. Our model is scripts/threshold_calculus.py
  (SHA-256 6a013d3f...5c5b) with results/A_paper_bp11_12.json and results/B_paper_bp7_8.json.
What was actually run: reviews/pr910_replay.py, written from scratch for this review. It ran
  66 checks: 65 pass, plus 1 documented finding and 0 unexpected failures. Ordinary and
  `python -O` runs agree. The PR's own two checkers were also replayed in a scratch copy.
  They pass, and their output is byte-identical to the recorded results.
Smallest remaining gap: the imported analytic machinery itself. Within this PR, the first
  load-bearing step not verified here is the claim that the source's shared contour lemmas,
  stated for sigma0 in [7/8,1), hold at sigma0 = 139999/160000
  (GEOMETRY_PERTURBATION.md line 264; see Section 5).
```

RH is unsolved. Nothing here bears on RH directly. Theorem 1.1 of the PR is an implication *from* an external, unreviewed manuscript. That manuscript claims a zero-free half-plane Re s > 7/8 for all Dirichlet L-functions. That claim is itself unverified, and this review does not examine it.

## 1. Bound objects

| Object at `pr910` | SHA-256 |
|---|---|
| `GEOMETRY_PERTURBATION.md` | `6e3befcc15b92536dd80f376a87384d5fa4688a938c11d949be7924d4a4c1e12` |
| `GEOMETRY_ENVELOPE_LIMIT.md` | `9118bde4dd41557cb155f15304cbd58dd0c0a0852a5ca551f6d59d72aeedde80` |
| `TAIL_AND_EULER.md` | `9bc21c039465f14c9125f97718c82b91f3a91be334ab9071ce74dd50a90a81a0` |
| `REVIEW.md` | `b7db37e34a856122de72c8d561816f2e99d6eb8c5a50e9781f71c475a0a5afa2` |
| `VALIDATION.md` | `2f7bcd39789a3e1f0181ba286809ff0d095a28cdb8c78978ab7b74d59aedf9d8` |
| `checks/check_research_algebra.py` | `532ae0038e015f1a4674683c299e783c6b50b3a0ff1bc23589a0161f1a222ef6` |
| `checks/check_tail_euler.py` | `355a05fd9ea92b7b497fe78e12972d498450e6a5104562a3f762e226c42696f3` |
| imported `paper.tex` | `42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3` |

The hashes of the PR files match those recorded in the PR's own `REVIEW.md` section 6.

## 2. Verdict in one paragraph

Every exponent identity and inequality in the 139999/160000 deduction replays exactly. I rebuilt them from the source's black-box outputs, not from the PR's checker. The low side gives L0 = 3/16 - 1/160000. The corrected row loss is real but is absorbed by the tuple rescaling. The high-side margin is correct: 1073/22032000 is certified directly at the perturbed geometry, without using the derivative argument or the source's SOS identity. The true margin is about 4 times larger. Every Lemma 7.1-type exponent stays convergent on the enlarged principal region Re s >= 437/500.

The exact envelope limit (1507 - 2 sqrt 921)/1653 is correct. Our numerical optimum 0.8749602 lands on it once the optimizer's 2e-5 slack is removed. One displayed decimal is wrong: the PR prints `0.874957067...`, but the value is 0.8749570698... This is cosmetic, and no inequality depends on it.

**Exponent-arithmetic verdict: PASS, conditional on the imported machinery.** This is not a verdict on the analytic adapters or on the manuscript.

## 3. Verdict table

| Claim (PR location) | Checked how | Result |
|---|---|---|
| Tuple: ell = 20003/120000, lx = 84997/240000, ly = 114997/240000, h = 65003/80000, M + ell = 1 (GP 2.1) | exact Fractions | PASS |
| C(s) = s - 11/16, independent of ell (GP 2.2-2.3, line 102) | exact. Symbolic: C(s) - s = -2/3 - b/6 whenever M + ell = 1 | PASS |
| L0 = lx/2 + b/12 = 3/16 - 1/160000 = 29999/160000 (GP 1.2, 2.2) | rebuilt from the black-box outputs: sup of Lemma 14.3 E_ref = max(M', (2M'+1+3ell')/4, 2M'+ell'-1), the Prop 15.2 Gram factor with P_a = Z^b, and the Prop 15.3 tuple count Z^d with coefficient Z^(-3d/2). I took the max over d in [0, ell] at all exact breakpoints | PASS. The max excess is exactly 0, attained only at d = 0 |
| beta0 = 139999/160000 = 7/8 - 1/160000 = 11/12 - ell/4 (GP 1.1, 2.3) | exact. Symbolic: beta0(ell, b) = 11/12 - ell/4 on M + ell = 1 (b cancels) | PASS |
| Row-norm bound sum \|B\|^2 << Z^(M' + (5ell-1+d)_+/4) (GP 4.1) | (i) The algebra 1 + 3ell' - 2M' = 5ell - 1 + d holds and the saving identity in the proof is correct. I compared it line by line with the TeX proof of `lem:probe-row-norm`, lines 8226-8330. The only ell = 1/6 specialisations there are the range in (15.1), the "d - 1/6" line and the d = 1/6 endpoint remark. (ii) It equals the closed-form sup of E_ref; the third branch never binds | PASS for the exponent algebra. The analytic transfer is not re-proved |
| Corrected row loss f_ell(d) = -d + (5ell-1+d)_+/8 <= 0 (GP 4.2) | identical to my rebuilt excess at all breakpoints and 98 rational d. Kink at d = 1/6 - 1/8000. Row-energy loss at d = ell is 3/80000 > 0 (genuine). f_ell(ell) = -80003/480000 | PASS. The maximum is 0, at d = 0 |
| Length gates: lx - ell = 44991/240000, M - 2ell = 19997/40000, ly - ell - 11b/6 = 19991/240000 (GP 4.3) | exact | PASS (see note N1) |
| E(d) formula (GP 3.6) | symbolic: the sum of outside Mellin powers X^(1/2-z) Z^(s+z-1) Y^(w-1), the source factor U^(delta/2) Z^(ell(z0-1/2)+q ell), U^R and q_u^(-z0), minus C(sigma0), for arbitrary (lx, ly, ell) | PASS |
| E(h) = -1/4 + 5ell/4 + b/6 + delta(1/2+ell) + x delta ell - h(1-R) (GP 6.1, GEL 1.3) | symbolic from (3.6) with sigma0 = beta0(ell, b). It reduces at (1/6, 1/8) to source (20.4) at d = h | PASS |
| R_* closed form at kappa = 3/4, no Delta/4 (GP 5.2, Lemma 5.1) | symbolic: balancing the source's Prop 19.2 R_short(t) = L(t) at Delta = 0. Plain capacity (1-2m)/(6 kappa) = 2(1-2m)/9 at kappa = 3/4. Lemma 18.1 needs beta* <= (1+kappa)/2 = 7/8, which the imported 7/8 theorem supplies. Bin ceiling delta <= 3/4 | PASS (formula level) |
| dE/d ell = 5/4 + delta(1+x) - (3/2)(1-R_*) <= 5/2 (GP Lemma 6.1) | symbolic derivative. E is exactly affine in ell (second derivative 0). Exact identity 1 - R_* = delta[(alpha-delta)(2D_x - P_x) + 2 delta P_x]/(2J) >= 0, so R_* <= 1 | PASS |
| Source Lemma 20.2: -E_old >= 49/440640 on [0,5/6] x [0,1/2] | **independent** exact rational branch-and-bound (mean-value interval form, 341 boxes). It does not use the source's identity (20.9). J >= 1/2 > 0 is certified the same way | PASS |
| Margin 49/440640 - 1/16000 = 1073/22032000 (GP 6.2) | exact arithmetic, and a **direct** branch-and-bound at the perturbed geometry: -E_new >= 1073/22032000 (327 boxes) | PASS |
| (stronger, not claimed by the PR) | branch-and-bound: -E_new >= 19/100000. Float minimum 1.9483e-4 at delta ~ 0.38664, x = 1/2; the old geometry gives 2.2815e-4 | the PR's margin is conservative by about 4x |
| Our model: sup F at the PR geometry (high_sup, nde=401, nx=51, nd=41) | `threshold_calculus.high_sup(lx, ly, ell, 0.87499375, beta_prev)` | -1.9491e-4 (beta_prev = 11/12); -1.9484e-4 (beta_prev = 7/8). Binding at delta ~ 0.386, x = 1/2, d = h = 0.81254, R ~ 0.669. Source geometry gives -2.2823e-4. The shift 3.331e-5 matches s0 * dE/d ell = 3.333e-5 |
| Our model: low threshold at the PR geometry | `low_threshold(..., nd=4001)` | 0.87499375 exactly (float) |
| Floor bin margin (GP 6.2 item 3) | exact direct value E(h) = -4351/750000 ~ -5.80e-3 | PASS |
| Intermediate rows (item 4) | exact: E(1/2) is affine in delta. Endpoint values -0.2152 and -3.3807e-3 match the PR bound -49/14400 + (177/200)s0. The d-slope is positive | PASS |
| Small rows (item 5) | exact: h(z0-1/6) - ly/2 + 2 d_min = -(63/800 - (51/100)s0) | PASS |
| Prime supply and frequency extension (item 1) | ell/h = 40006/195009 > 8/39 > 7/37. 5ell - h = 1/48 + (7/2)s0 | PASS |
| Principal margins ly/20, h/600, mu = (437/1000)ell/K < (437/500) min ell_i (GP 3.9-3.10, section 7) | exact | PASS |
| Good-prime Euler exponents at alpha0 = 437/500 (GP 3.2) | terms DV, DW, VW and the two E_p terms derived from source (7.11)/(7.17) at Re w >= 19/20, Re z >= 33/200: -233/125, -228/125, -97/50, -1117/500, -907/500 | PASS. Max is -907/500 < -1, so summable |
| Ramified Euler exponents (GP 3.2) | R, the strict second family, J_1..J_5 from the source table. Decays 1117/500, 103/125, 228/125, 561/500, 393/250, 187/125, 973/500, 561/250 | PASS. Min 103/125 > 0 |
| \|R\| < Q^-1; tail O(P0^(-407/500)); selected principal decay min(alpha0, 99/100, 34/25, 47/50) = 437/500 (GP 3.1-3.4) | exact | PASS |
| Reproduces the source at alpha = 7/8 (-363/200, 33/40) | exact | PASS |
| alpha0 < beta0; small-row lines in D1(1/3); small-row good exponents < 0; ramified <= 1/2 (GP 3.5) | exact. Gap beta0 - alpha0 = 159/160000 | PASS |
| Envelope: R_*(delta, 1/2) - 2/3 = (288 delta^2 - 588 delta + 185)/(3(185 - 138 delta)) (GEL 2.2) | sympy | PASS |
| delta0 = (49 - sqrt 921)/48 in (3/8, 19/48); other root 1.653 > 5/6 | sympy | PASS |
| b cancels at R_* = 2/3 (GEL 2.3) | symbolic: dE/db = (R_* - 2/3)/2 | PASS |
| ell* = (8 sqrt 921 + 33)/1653; limit (1507 - 2 sqrt 921)/1653 (GEL 2.4-2.5) | sympy in Q(sqrt 921), plus an exact integer-sqrt enclosure | PASS. Value 0.87495706979917 |
| Displayed decimal "0.874957067..." (GEL:110, README:90, REVIEW:101) | exact enclosure (0.8749570697, 0.8749570698) | **WRONG in the 9th decimal.** It should read 0.874957069... (rounded 0.8749570698). The PR checker's bracket (0.87495706, 0.87495708) is too coarse to detect this. Cosmetic |
| beta0 lies above the limit | exact | PASS. Gap 3.668e-5 |
| (beyond PR) x = 1/2 is the best point on the b-free curve R_* = 2/3 | exact roots for x = 0, 0.01, ..., 0.5 | ell-threshold is minimal at x = 1/2: 0.166838387 (0.178571 at x = 0) |
| (beyond PR) Tightness of the d = h envelope | float grid, delta <= 3/4 by 1/2000, x by 1/400, b by 5e-4 | at ell = ell*, min over b of sup E = 2.3e-9 (grid level), at b ~ 0.1235. At ell* - 1e-5 it is -1.33e-5. The limit appears to be the infimum, not just a necessary bound (numerical, not proved) |
| Comparison with our optimum (results A and B) | removed the optimizer slack using dE/d ell at the reported binding point | B: 0.87496023 -> 0.87495705. A: 0.87496099 -> 0.87495723. Exact: 0.87495707. Our 0.8749602 is explained entirely by the 2e-5 slack. Our optimizer also allowed M + ell != 1 and dynamic kappa (scenario A), and found nothing below the limit |
| PR checkers (supplementary replay, not independent) | ran both in a scratch copy | 83 + 148 predicates pass. Output is byte-identical to the recorded JSON (hashes `ad2c47b0...`, `fb51e01d...`) |

Abbreviations: GP = GEOMETRY_PERTURBATION.md, GEL = GEOMETRY_ENVELOPE_LIMIT.md.

## 4. Notes on specific steps

**N1 (not a gap).** The source justifies Q >= 1 at TeX line 8593 by "M' >= 1/2". At the new geometry the smallest row length is M - 2ell = 19997/40000, which is below 1/2. The PR, in its line 449, uses positivity instead. That suffices for the stated hypotheses of `prop:probe-gram` (TeX 8340-8346): Q, Y' >= 1 in fixed polynomial ranges, and P_a >= 1. Lemma 14.3 asks only for bounded log-lengths. The PR should say explicitly that the source's "M' >= 1/2" is replaced and not inherited.

**N2 (where the gain comes from).** The improvement has two parts:
- The perturbed low exponent L0 = lx/2 + b/12 falls by s0/4, while C(s) stays s - 11/16.
- The kappa = 3/4 bootstrap removes the source's h Delta/4 count penalty. This is legitimate because the imported 7/8 theorem gives beta* <= 7/8, which is Lemma 18.1's hypothesis at kappa = 3/4. It is a use of the import's own conclusion, so the result is doubly conditional on the import.

The available high slack is about 1.95e-4. That would allow ell up to about 1/6 + 1.46e-4 before this one binding point closes. It is consistent with the exact envelope limit: the corner (delta0, 1/2) binds at ell* = 0.1668384.

**N3 (corrected row loss).** The per-subset row energy has a real loss of up to 3/80000 near d = ell. After Cauchy-Schwarz this becomes 3/160000. The Z^d tuple count, the Z^(-3d/2) scalar and the Z^(-d/2) from (X')^(1/2) more than compensate. The source's zero-loss statement (15.2) is therefore not needed per subset, as the PR says.

**N4 (geometry-independence of the compensated identity, GP line 124).** I checked the local multiplier derivation at TeX 8667-8684. The marked factor is Q^(x+z-1); the rescaled factor is Q^(-3/2) Q^(-(1/2-z)) Q^(-(w-1)). Both depend only on Q, x, w, z, not on lx, ly or ell. This is a lexical and structural check, not a re-proof of `eq:compensated-poisson-identity`.

## 5. First step not verified, and first step that looks wrong

**Looks wrong (first found): `GEOMETRY_ENVELOPE_LIMIT.md` line 110**, repeated at `README.md` line 90 and `REVIEW.md` line 101. The decimal `0.874957067...` is not a truncation of (1507 - 2 sqrt 921)/1653 = 0.8749570697991687... The correct digits are 0.874957069... The exact expression, the checker's 8-digit bracket, and every inequality are unaffected. Fix: print 0.8749570698... and tighten the checker bracket to 10 digits.

**First load-bearing step I could not verify: `GEOMETRY_PERTURBATION.md` line 264**, the Lemma 3.3 proof adapter. Lemmas 3.4 (line 337) and 3.5 (line 361) rely on the same kind of claim. The source's four shared lemmas are stated only for sigma0 in [7/8, 1): TeX lines 5811 (`Contour transformation for a fixed bin`), 6024, 6178 (principal signal) and 6345 (outer row norms). The PR applies them at sigma0 = 139999/160000 < 7/8 and asserts "These arguments do not use sigma0 >= 7/8".

The exponent consequences check out. All Euler-region exponents pass, and the small rows sit in D1(1/3). Supporting evidence also comes from a lexical scan of source Section 10 (TeX 5460-6492). It finds "7/8" only in:
- the four statements;
- the D2 definition (5574) and the H_eta region (5525, 5530);
- the D1(3/8) placements (6418-6419; 6469 is Part I).

These are exactly the places the PR replaces. Still, I did not re-derive the contour moves, the horizontal-join and trace estimates, or the dynamic error lemma `prop:probe-errors` at the new sigma0. This is a statement-outside-hypotheses use of an imported lemma, and per AGENTS.md it needs its own reviewer to read those proofs. Its failure would invalidate Theorem 1.1 even if every exponent above is right.

In reading order there are two earlier steps outside pure exponent arithmetic: the geometry-independence of the compensated identity (line 124, see N4) and the holomorphy/nonvanishing arguments of Lemmas 3.1-3.2. They are standard or exponent-free, and I checked them only at that level.

## 6. Explicitly not checked

- Any imported analytic statement. This includes the reflected energy (Lemma 14.3), the additive Gram bound, the buffered detector and saturated witnesses, the inverse and plain fourth moments (Lemmas 17.1, 17.6, 18.1), the dynamic error allocation, the smooth/external-tail calculus, the late-height closure and the Hecke-to-Dirichlet transfer.
- The proofs of the analytic adapters in GP Lemmas 3.3-3.5, 4.1 (beyond its exponent algebra) and 5.1 (beyond its count formula).
- The order of choices and quantifiers in GP section 7. I checked only that the margins it names are positive.
- TAIL_AND_EULER.md beyond its Lemma 2.1-2.2 exponent tables: section 3 factorization, sections 5-8 tail criteria.
- NATIVE_HEIGHT.md, FOURTH_MOMENT_REDUCTION.md, UPSTREAM_HEIGHT_AND_MOMENTS.md, CAUSAL_AUXILIARY_FACTOR.md and the native checker.
- No Lean build, no zero computation and no manuscript audit.

The float items (our model, minimum location, tightness probe) are FLOATING_RECONNAISSANCE. They corroborate the exact checks and are not gates.

## 7. Reproduction

```text
cd research/exploratory/qrh-2026-10/reviews
python3 pr910_replay.py      # about 50 s; writes pr910_replay_output.json
python3 -O pr910_replay.py   # same result; acceptance gates do not use assert
```

Script SHA-256 is `489729b62ea59035fca922c59e4e726c372b40e702f9a796a7ab3d4c3776ccaa`. Output SHA-256 is `7bf62879f3a697762c2c64266e8d89283db3155a08e547efe45d4b5f0142c322`; that hash is from the `-O` run, and its verdicts are identical to the ordinary run. The script needs sympy, numpy and scipy. It imports `../scripts/threshold_calculus.py` and reads `../results/{A_paper_bp11_12,B_paper_bp7_8}.json`. Exit status 0 means no unexpected failure. The single `FINDING` line is the decimal error in Section 5.
