# Hostile review: drift lanes (M/S/P) — incremental notes

## Hand-verified analytics (pre-numerics)
- laneM T-M2 Pochhammer identity: g_{j+a}g_j = g_a (a-1/2)_j(-1/2)_j/((a+1)_j j!) — CHECKS (shift identities exact).
- laneM T-M3 Euler-integral positivity: a=alpha-1/2>0, c-a=3/2>0, integrand (1-xt)^{1/2}>0 — CHECKS.
- laneM C-M4 SD exponent: sum c_q/q ~ (logQ)^{1/4} * G(1)/Gamma(5/4); Gamma(5/4)=(1/4)Gamma(1/4)
  matches partial-summation from SD count ~ Q(logQ)^{-3/4}/Gamma(1/4). EXPONENT AND GAMMA-FACTOR CORRECT.
- laneM L-M7: hatA_-(s)=(1-2^{-s})(1-sqrt2 2^{-s})/s verified; Phi'(1/2)=hatA'(1/2)hatA(-1/2)
  = 2(1-2^{-1/2})log2 * 2(1-sqrt2) = (8-6sqrt2)log2 — CHECKS exactly.
- laneM T-M5: R(log1.35)=3log2-(3+sqrt2)*0.3001=0.755>0; |varrho|>=r_2(1)^2>0.17; PNT block >>1/log p; divergence CHECKS.
- laneS .1/.2: trivial inequalities all check ([O]_+<=H, H<=D+[O]_+, |O|<=[O]_++D).
- laneS .3: sup_oct [O]_+ << 2^{(2/3)L}L^{O(1)} via |h|<=tau — plausible and stated as ledger cite; product with mu_L bound = 2^{o(L)} — CHECKS.
- laneP .1 Plancherel: support (U,4N), window (U,4X/U) contains it; N_X=floor(X/U) integrality — CHECKS.
- laneP .3: SD z=-1/2: Gamma(-1/2)=-2sqrt(pi) -> -x/(2sqrt(pi)log^{3/2}x) — CHECKS; (iii) partial-summation factor
  (1-ig)/(1/2-ig) converts 1/(1-ig) -> 2/(1-2ig) — CHECKS exactly.
- laneP .4 b_N: Hankel of (s-s0)^{-1/2}: 1/Gamma(1/2)=1/sqrt(pi); R_U(1)=-m(U); partial-summation factor -> -2m(U)N^{1/2-ig}/((1-2ig)sqrt(pi logN)) — SIGN AND CONSTANT CHECK.
- laneP .5 H^2 lemma quantifier logic: negation limsup<c_0 => exists A'<c_0, T_0: Q(T)<=A'logT for T>=T_0;
  J(h)=2h int Q T^{-2h-1}dT <= A'/(2h)+O_{A'}(1) — boundary terms vanish, T<=T_0 part O(1) unif in h. CORRECT.
  Analyticity: CS gives abs conv of Mellin integral for Re s>-1/2; continuation => no zeta zeros Re>1/2 UNDER HYPOTHESIS (contradiction logic OK).
  Plancherel J(h)=(1/2pi)int|F(-1/2+h+it)|^2dt: m(e^x)e^{(1/2-h)x} in L^2(0,inf) iff J(h)<inf — derived. CORRECT.
  Window: |F|>=1/(|s|C_1|h+i(t-g1)|); |s|^2->1/4+g1^2; int dt/(h^2+d^2)->pi/h; two windows: (1/h)/((1/4+g1^2)C_1^2). CORRECT.
  Combine: A'/2 >= 1/((1/4+g1^2)C_1^2), h->0 then r0->0 => A'>=c_0 contradiction. LOGIC SOUND.
- laneP .5 Cor 3 (smoothing robust): PROVED only for FIXED delta (clean Mellin multiplier); u-DEPENDENT delta(u)->0 breaks the multiplier structure — as stated overbroad. FLAG.
- laneP .2(c) "the gate is EXACTLY the statement..." — only gate=>segment proved; converse needs uniformity |gamma|<=N. "EXACTLY" overclaims. FLAG.
- laneP branch mass: |b_N|^2 = 4m(U)^2 N/((1+4g^2) pi logN); (1/2pi)int w|b|^2 = (2/pi^2) I_w m^2 N/logN — algebra CHECKS.

## To verify numerically
1. fast_O validate vs deposited; 2. X=4e10 sign reproduction (band + independent sweep); 3. laneM constants; 4. laneP replay; 5. c_0 via mpmath; 6. cross-lane branch-mass vs out_big signs.

## Numerical results (all run in review_drift/)
- fast_O validate: band vs deposited pair sums max diff 1.9e-13; gram <=2e-13. PASS.
- X=4e10: O=+0.6040725308167303 EXACT match; indep sympy-mu 300/300, indep divisor-sum h 150/150 exact;
  cancellation-free sweep H=5.14460959 > D=4.54054 (gram 4.6e-11). SIGN REAL.
- Onset: step-1 scan U=2776..2800: U<=2781 negative (near-miss -0.0064 at 2778!), U=2782 O=+0.0183 = claim.
  BUT no U=2782 row in any deposited out_*.json (step-20 stops at 2780, step-25 starts at 2800). Replay gap.
- laneM model.py: identity err 2.2e-23; G(1)=0.9184884, C_SD=1.0133339; factorization relerr <=2.6e-5 (s=1.5),
  <=5.3e-4 (s=1.25); A11/SD ratio ->1.0063; kernel int = (8-6sqrt2)log2 to 6e-16. ALL MATCH.
- laneM trunc: O^hi replays deposited O_hi_signed exactly; SIGN-LAW COUNT IS 38/40 NOT 39/40
  ((4,1) violates at X=1e4 AND 1e6). Deposit text error.
- laneM drift: S(P) values match deposit; Sabs*log^2P/P in [1.1,1.8] matches.
- laneP replay (independent spf-based g sieve): m, Q/logT, M_half, Sigma_g ALL match to full digits.
- c_0 first-principles: gamma_1=14.13472514, |zeta'(rho_1)|=0.79316043, c_0=0.015892422. MATCHES.
- I_w true value 0.4991459; lane's 0.4990635 misses [0,0.0005] segment (0.017% low). MINOR.
- sum over 30 zeros = 0.02719 (lane says "~0.023+"). MINOR.
- w_min[1,2]=0.3804161, min|zeta|=0.53963, 2pi/log2=9.06472: all match.
- CROSS-LANE: branch mass at out_big rows: {4e10: 2.09, 1e12: 2.38} = the ONLY two positive-O rows;
  all others mass <=0.35 and O<0. Mechanism-level coherence CONFIRMED.
- theta=0.25 positives at X~4e7..2e8 predicted by mass~5 at U~100 (sqrt(100)m(100)=0.311). COHERENT.
- Octave table L=39/40 stats reproduced exactly from scan jsons.
- Gram claim "<=5e-13" at big X NOT reproduced (4.6e-11 here). MINOR misreport.
