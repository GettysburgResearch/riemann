# Lane A2 — hostile re-verification notes (running)

## Sources read line-by-line (branch:path)
- f4016db5:claims/lemmas/L-102009-... (two-field factorization) — read in full
- f4016db5:claims/lemmas/L-102010-... (half-divisor, AUDITED, constant 3) — read in full
- 89f9954:claims/lemmas/L-102010-... — OLDER COPY, constant 5 via Young; diff confirms the only change 3<->5 + audit line
- f4016db5:claims/theorems/T-102001-... — read; T-102001.5 |B|<=3H, T-102001.6 gate, T-102001.7 HHFE=>RH
- 4f69b765 (= tip research/gpt56-pro/100300-two-route-endgame = PR #685 per coverage census):
  claims/lemmas/L-100310, L-100311, L-100312 — read in full
- 89f9954:claims/lemmas/L-103100, L-103101, L-103102 — read in full
- 0a46dba5:claims/theorems/T-102100, T-102110; claims/lemmas/L-102106 — read in full
- Review: 55fe0b6f CLAIMS.tsv + ROUTE_EDGES.tsv; a520556a coverage PR_CENSUS.tsv; e9c84904 (PR #687) R-100400, T-100400

## KEY REVIEW-COVERAGE FINDING (part b)
- Reviewer A CLAIMS.tsv @55fe0b6f has NO rows for PR #685 (source_pr column: 674,675 present; 685 ABSENT).
- `git grep 100310` over review/ trees of ALL FIVE review branches (55fe0b6f, eb198750, 945a6eec, e91d6aa2, a520556a): ZERO hits.
  => L-100310/L-100311/L-100312 have zero claim-level review coverage in the entire 2026-08-21/22 wave.
- EDGE.HHFE.RH in ROUTE_EDGES.tsv cites 696@f4016db only; the L-100310..312 imports are un-rowed.
- Coverage census (a520556a PR_CENSUS.tsv row 685@4f69b765): reviewer_a=REPRESENTED_BY_BOTH(?), controlling_later_pr=687,
  first_broken_arrow="certificate normalization is inconsistent with the claimed native quantity",
  lifecycle="archive wrapper; retain corrected finite data".
- PR #687 @ e9c84904 R-100400: the normalization defect is in PR #685's CATD100300 cell-coarea route
  ("the CATD100300 -> RH arrow in PR #685 is invalid as written") — NOT the L-100310..312 notch/Vaughan chain.
  BUT T-100400 (corrected endgame) lists only Routes A/B and does not re-affirm the BVD100310 route either.
  => The BVD trio survives only on my own line-level re-derivation below; no reviewer has signed it.

## Line-level re-derivations (part a,b,c) — my own checks
- eta*eta=1: coefficient of z^k in (1-z)^{-1}; binomial identity to be numerically confirmed.
- a_U=b_U*1: mu=mu_U+b_U, mu*1=eps. OK.
- L-100311.1: A_U=1-zeta M_U; 2M_U - zeta M_U^2 + A_U^2/zeta = 1/zeta expands identically. OK.
- L-102009.9: a_U*a_U*mu = b_U*1*b_U*1*mu = b_U*b_U*1 = b_U*a_U. OK.
- L-102010.4: h*h = b_U*b_U*(eta*eta) = b_U*b_U*1. OK.
- Hardy relation: A_-=(D-1/2)A => d/dt[e^{-t/2}A(u+t)] = e^{-t/2}A_-(u+t); integrate: A = -T A_-; A_+=A_-+2A=A_--2TA_-. OK.
- Multiplier of I-2T: 1 - 2/(1/2-i xi) = (-3/2-i xi)/(1/2-i xi); |.|^2=(9/4+xi^2)/(1/4+xi^2)<=9, sup at xi=0. SHARP 3 CONFIRMED (f4016db audited version correct; 5 of 89f9954 also valid via Young ||T||<=2).
- Constant 3 vs 5: IMMATERIAL for gate (any absolute constant absorbed by 2^{o(L)}); T-102001 correctly uses 3.
- TRUNCATION CAVEAT (L-102010.11-.13, T-102001.4): the Hardy step bounds ||H_+||_{I_X} by 3||H^trunc_-||_{I_X^+}
  where the minus field is TRUNCATED at n<=X/U. The definition (L-102010.12)/(T-102001.4) of H_U(X) is written with the
  UNTRUNCATED field H_{U,-}; on (X/U,4X/U] these differ (untruncated has extra n in (X/U,4X/U)). The proved inequality is
  |B_U(X)| <= 3 * [truncated energy]. Reviewer A's required_fix "Keep support truncation before full-line Hardy" = this point.
  The equivalence lane L-103100/L-103102 uses exactly the TRUNCATED field H_{U,N}, N_X=floor(X/U_X): consistent with the
  proved inequality. So the correct gate object = truncated energy; chain sound under that reading. Numeric: compare both.
- L-100310.4 trapezoid: |1/Y sum k(m/Y) - int k| <= Var(k')/12 Y^{-2} (Euler-Maclaurin with |B2~|<=1/6): standard, needs k
  continuous with k' BV. K_1=A_-*_M A_+ continuous, piecewise smooth, k(x)=x^{-1/2}K_1(1/x): OK. int k = hatK_1(1/2)=0 since
  factor (1-sqrt2 2^{-s}) vanishes at s=1/2. OK. Numeric decay check planned.
- L-100311.6: |T_U| <= (V1/12) X^{-3/2} (sum_{a<=U} a)^2 = O(X^{-1/6}) at U=X^{1/3}. OK.
- L-100312.2: BVD => neg mass of W_1 subpower ((a+b)_- <= a_- + |b|; int|T_U| dX/X < infty) => Mellin of (W_1)_- entire on
  Re s>0 + hatK_1/zeta(s+1/2) analytic on positive reals (needs L-99272-style positive-axis audit + specialized Landau,
  PR #653 dependency VERIFIED_WITH_FIXES) => no pole at rho-1/2 => no zeros Re>1/2 => RH. Mechanism sound; the Landau/
  positive-axis audit for THIS kernel (hatK_1(s)/zeta(s+1/2) real-axis analyticity incl. s in (0,1/2)) is asserted via the
  PR #653 API; zeta(s+1/2)<0 on s in (0,1/2) nonzero, s=1/2 pole of zeta kills 1/zeta and hatK_1(1/2)=0 — double zero OK.
- L-100312.3 converse: RH => M(x)=O(x^{1/2+eps}), partial summation vs compact BV kernel. OK.
- HHFE => BVD: |B|<=3H + dyadic HHFE, sum over L<=log2 Y of 2^{o(L)} = Y^{o(1)} (uniformity standard). OK.
- L-103100.2 R(v): overlap computation re-derived: 3h-(3+sqrt2)v on [0,h]; -sqrt2(2h-v) on [h,2h]. OK. R(0)=3log2=int|A_-|^2. OK.
- L-103101: |h_U(n)|<=tau(n) (0<eta<=1); D=3log2 sum h^2/n <= N^{o(1)} (log absorbed). OK.
- L-103102.1 Plancherel: hatH(gamma)=psihat(gamma) P(1/2+igamma). OK; numeric check planned.
- L-103102.2: sum h_U n^{-z} = (1/zeta - M_U) zeta^{1/2}, Re z>1 Euler products. OK.
- HCNC<=>HHFE: O_+<=H (D>=0), H<=D+O_+, D dyadic-subpower. OK — with H = TRUNCATED energy (see caveat).
- T-102100.2 CFBB=>RH: v<=Mv+eps(1,1), rho(M)<1, M>=0 => v <= (I-M)^{-1} eps (1,1) = Y^{o(1)}; 2x2 criterion a<1,d<1,
  bc<(1-a)(1-d) checks out. Downstream needs PR #697 Perron absorption + L-102103 no-pole-cancellation (ledger VERIFIED).
- T-102110: HCNC => H subpower => (L-102106.5) |B_A†|+|B_Q†| <= C H => N_A+N_Q=Y^{o(1)} => CFBB with M=0 => RH.
  CAVEAT: L-102106.5's Cauchy-Schwarz is stated "at every endpoint" WITHOUT the finite-window localization that L-102010
  performs (full-line L2 norms of untruncated fields are infinite). Same repair as L-102010 presumably works but is NOT
  written. Also "finite duplicate-67 difference changes only the absolute constant" is asserted, not proved.

## Numeric plan (d)
1. binomial/eta*eta identity; 2. g=a*a*mu=b*b*1=h*h; 3. mu=2mu_U-mu_U*mu_U*1+a*a*mu; 4. K_1 closed form + Mellin check
5. two-field identity B via (g,K_1) vs int F_-F_+; 6. |B|<=3H trunc/untrunc tables X=1e3..1e5; 7. Plancherel 1e-6;
8. H=D+O; R(v) overlap check; 9. Type-I decay |S(Y)|Y^{3/2} bounded; 10. W_1=T_U+B_U exact.

## NUMERIC RESULTS (results.json, results_fixed.json; script verify_a2.py + fix_checks.py + inline checks)
- binomial/eta*eta: exact (dev 0.0 up to n=20000; binomial k<=39 <1e-12)
- a_U=b_U*1, a*a*mu=b*b*1=h*h, mu=2muU-muU*muU*1+a*a*mu: dev 0.0 (U=5/12/21, N up to 8000)
- K1 closed form (from A_-*_M A_+) vs both Mellin formulas (L-102009.6 and L-100310's (1-sqrt2 2^-s)K0hat): dev ~2e-16 at s=2, .8, 1+3i, 1.5; the two formulas agree identically => PR#685/PR#696 kernel compatibility CONFIRMED. K1hat(1/2)=2e-16~0.
- Two-field identity L-102009.13: rel dev 6e-14 (X=600,U=8), 6e-15 (X=2000,U=12)
- Symmetric identity L-102010.7 (H-fields): rel dev 8e-15 (X=2000,U=12)
- Hardy relation A_+=A_- -2TA_-: pointwise dev 1e-15 off jump points
- Norm step ||H_+||_{I_X}/||H_-^tr||_{I_X^+}: 0.934 (X=3e3), 1.121 (X=3e4) — both <= 3 (and <5)
- |B|<=3H table (X=1e3..1e5, U=floor(X^{1/3})): max ratio |B|/H_trunc = 0.326, |B|/H_untrunc = 0.343; both inequalities hold with big margin. NOTE X=3e4: H_untrunc(0.786) < H_trunc(0.883) — truncated/untruncated energies NOT ordered; confirms the truncation caveat is a real (if benign) statement issue.
- Plancherel L-103102.1: rel dev 3.5e-11 (panel Gauss to G=2000 + exact trig tail via Si; U=5,N=60)
- Gram H=D+O: rel dev 1e-14 (two cases); R(v) vs overlap integral: 2e-15 (81 v-values)
- Type-I L-100310.4: |S(Y)|*Y^{3/2} for Y=10..1e4: max ~13.5, no growth — consistent with (V1/12)Y^{-3/2}
- Vaughan decomposition W1=T_U+B_U (L-100311.3): dev 6e-15, 3e-15

## FINAL VERDICTS
(a) L-102010: PASS-WITH-CAVEATS. All identities correct; sharp constant 3 proved at f4016db5 (audited), 5 via Young at
    89f9954 (older copy, also valid); constant immaterial for gate. CAVEAT: proved inequality is |B|<=3*H^trunc (field
    truncated at n<=X/U); boxed defs (L-102010.12/T-102001.4) write untruncated field; correct gate object = truncated
    energy = L-103100's H_{U,N_X}. Numerically benign; formally must be read as fixed by Reviewer A/B fix lines.
(b) L-100310/311/312 content: PASS on my line-level re-derivation + numerics. COVERAGE: FAIL-OF-COVERAGE (loud):
    zero CLAIMS.tsv rows, zero review/ mentions on all 5 review branches; PR#685 census row says controlled-by-#687/
    archive-wrapper (defect is in the CATD route per R-100400, not the BVD trio, but no reviewer has affirmed the trio).
    HHFE=>BVD=>RH chain: sound; imports L-99272-class specialized Landau (VERIFIED_WITH_FIXES) for the consumer step.
(c) L-103100/101/102: PASS (with same truncation-reading caveat on the equivalence's reference to "the field-energy
    condition of PR #696"). T-102110/L-102106: PASS-WITH-CAVEATS (unlocalized Cauchy-Schwarz "at every endpoint";
    67-duplicate handled by assertion; no ledger rows; depends on unaudited-by-me PR#697 Perron absorption) — redundant
    spur, not load-bearing.
(d) All numeric identities PASS after fixing my own quadrature (R-check kinks, Plancherel oscillatory panels).
