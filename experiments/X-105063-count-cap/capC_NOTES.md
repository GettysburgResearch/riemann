# CAP-C ASSEMBLY PLAN
1. Read LEMMA_A.md, LEMMA_B.md + their NOTES; record exact statements and constants.
2. Identify what LEMMA_B's induction counted: zeros of h' or of shallow-only equation? on whole gap?
3. Check tolerance of LEMMA_B induction to deep pairs; localization of deep bumps to I_j.
4. Split: zeros of h' in G <= [zeros of shallow eq in G] + [zeros of full h' inside U=union deep I_j].
5. Cluster deep intervals; per-cluster bound: C * (#pairs in cluster) via cluster-internal argument.
6. Handle the sign issue on G\U (deep phi'_j < 0 there) — verify support claim numerically.
7. Assemble FINAL THEOREM extra(G) <= A' W(G) with explicit A'; use safety net if additive const appears.
8. Numeric duty: adversarial mixed deep+shallow scans; confirm constants.
9. Write FINAL_LEMMA.md (statement, proof, table, residual).
10. Final message < 1200 words.

## STEP 1: audit of inputs
LEMMA A: PROVED. (H1) one pair R4-active (R4=2+sqrt3), others R4-far => Z_mult(h',G)<=6, extra<=6.
 Method: Q=B-sum_other m phi' has Q,Q'',Q''''>0; localization to I=(x-y,x+y); split I by x+-(2-sqrt3)y;
 center: f''<0; wings: f''''<0 (strict concavity of (h')''); Z_mult((h')'',I)<=4; Rolle x2 => 6.
LEMMA B: PROVED CONDITIONAL. (SC) all ov y>=g/2. Ladder h^(2k+1)=-(2k+1)! Re S_{2k+2};
 (B.8): kappa*V_1+G_4(M_L+M_R)<1 => h'''<0 => extra<=2. Constants kappa=(11+5sqrt5)/64, G_4=0.02255.
 Residuals: (R1) near-critical shallow concentration, (R2) band-adjacent non-ov mass.
CAVEAT found: B-I(iii) bounds distinct zeros by 1+2#comp(P), P={h'>0}; #comp(P) is NOT <= #comp(U)
 (P subset U but a U-component can hold many P-components). So no unconditional distinct cap. Skip.

## STEP 2: NEW THEOREM C-4 (mixed deep+shallow), derivation
Hypotheses (per gap G):
 (Sep) deep ov pairs (y_j<g/2, I_j meets G) have pairwise disjoint R4-fattened intervals
       Itilde_j=(x_j-R4 y_j, x_j+R4 y_j)  [gives |t-x_i|>=R4 y_i for t in I_j, i!=j deep ov].
 (L2) W_sh := Sum_{shallow ov} m_i w_i < 1,  w_i=(g/2y_i)^2<=1.
 (L4) kappa*V_1 + G_4 (M_L^(4)+M_R^(4)) < 1,   V_1=Sum_sh m_i w_i^2.
 (L6) kappa_6*V_2 + G_6 (M_L^(6)+M_R^(6)) < 1, V_2=Sum_sh m_i w_i^3, kappa_6<=1, G_6<=2e^{-pi/2}.
Chain:
 (a) LEVEL-2 CONFINEMENT: at any zero t of h' in G: B(t)=Phi'(t). Positive contributions to Phi':
     only ov pairs with t in int I_j (support). Shallow-ov positive parts <= sum 2m_i/y_i^2
     = (8/g^2) W_sh < 8/g^2 <= B(t). So some DEEP ov pair has t in I_j. Zeros of h' confined to
     U_deep = union I_j (deep ov). [uses (L2) only]
 (b) PER-PAIR COUNT on J_j=I_j cap G: h' = m_j f_j - Q_j, Q_j := B - Sum_{i != j} m_i phi'_i.
     Need Q_j''>0 (L4) and Q_j''''>0 (L6) on J_j:
     Q_j'' = B'' - Sum (phi'_i)'': B'' >= 6/d_a^4+6/d_b^4 >= 192/g^4.
       shallow-ov: ((phi'_i)'')_+ = 12(-Re(t-z_i)^{-4})_+ <= 12 kappa m_i / y_i^4
                  = kappa m_i w_i^2 * (192/g^4).
       non-ov (any y): <= 6 G_4 m_i / d_side^4 (Lemma B.4, n=4), band cot(pi/8)=1+sqrt2.
       other deep-ov: |t-x_i|>=R4 y_i > (sqrt2+1)y_i => (phi'_i)'' <= 0. Drop.
       => Q_j'' >= (6/d_a^4+6/d_b^4)[1 - kappa V_1 - G_4 max(M_L,M_R)] > 0 under (L4).
     Q_j'''' = B'''' - Sum (phi'_i)'''': B'''' >= 120/d_a^6+120/d_b^6 >= 15360/g^6.
       shallow-ov: ((phi'_i)'''')_+ = 240(-Re(t-z_i)^{-6})_+ <= 240 kappa_6 m_i / y_i^6
                  = kappa_6 m_i w_i^3 * (15360/g^6).
       non-ov: <= 120 G_6 m_i / d_side^6 (B.4, n=6), band cot(pi/12)=2+sqrt3.
       other deep-ov: |t-x_i| >= R4 y_i = (2+sqrt3) y_i => (phi'_i)'''' <= 0. Drop.
       => Q_j'''' > 0 under (L6).
     Then Lemma-A Step 3 verbatim on J_j (split by x_j +- (2-sqrt3)y_j):
     center |s|<(2-sqrt3)y_j: f_j''<0, Q_j''>0 => (h')''<0. wings: f_j''''<0, Q_j''''>0 =>
     (h')'' strictly concave => <=2 each. Z_mult((h')'', J_j) <= 4 => Z_mult(h', J_j) <= 6.
 (c) TOTAL: Z_mult(h',G) <= 6 D_ov (D_ov = #distinct deep ov pairs); extra <= Z_mult(h',G)
     <= 6 D_ov <= 6 Sum_deep m_j <= 6 W(G).  If D_ov=0: h'<0 on G by (a) => extra=0.
No threshold upgrade needed; no additive constant. A' = 6 in this regime.

## STEP 3: constants (constants.py, constants2.py; mpmath 30dps + sympy identities)
f=-2Re(u-i)^{-2}, f''=-12Re(u-i)^{-4}, f''''=-240Re(u-i)^{-6}: sympy-verified (0,0,0).
kappa_4=(11+5sqrt5)/64=0.34656781 (exact, re-confirmed); kappa_6 = 1 EXACT (max at u=0; r>=1 proof).
G_4=0.0225424859 (v*=1.96261); G_6=0.0463162726 (v*=2.85784); rigorous cap G_n<=2e^{-pi/2}=0.41576.
R4=2+sqrt3: at |s|=R4 y: f<0, f''<0, f''''=0 (boundary root), f''''<0 beyond. Confirmed.
SIMPLIFICATION: if M^(4)=M^(6)=0 (no band-adjacent non-ov pairs), then (L2) => (L4),(L6)
 [kappa V_1 <= kappa W_sh < 0.347; V_2 <= W_sh < 1]. Headline form: (Sep)+(L2)+no band mass => extra<=6 D_ov.

## STEP 4: numerics (scanC.py, scanD.py, probe2.py, replay.py)
scanC: 700 random mixed configs, 487 pass (Sep)+(L2)+(L4)+(L6): ZERO violations of
 extra<=6 D_ov, confinement, per-interval Z(h',I_j)<=6. Max extra=16 at D=8 (2 per pair);
 max per-interval Z(h')=2 (proved cap 6). Initial 66 "outside" flags were float64 midpoint
 misattribution: probe2 (mpmath 40dps, bisect) shows roots INSIDE I_j at dist 1.4e-4*y from
 edges; classifier fixed to bracket-overlap; zero violations after fix.
replay (mpmath 40dps): extremal config g=1, 4 real zeros, 8 deep pairs (mults sum 15):
 17 distinct zeros of h in G => extra=16 confirmed exactly. extra/W = 16/15 > 1 (so A'>=2 needed
 in any such theorem; empirical extra = 2*D_ov throughout).
scanD residuals: (i) deep clusters (Sep violated, k=2..4 pairs crammed): max extra per pair
 still 2.0; (ii) supercritical shallow Wsh up to 3.02 + deep: max extra 6 = 2*D, per=[2,2,2],
 shallow added nothing. No blow-up observed in either residual regime.

## STEP 5: deposit structure decided
Thm C-0 (no overhang: extra=0), C-1 (=Lemma A, (H1): extra<=6<=6W), C-2 (NEW mixed:
 (Sep)+(L2)+(L4)+(L6): extra<=6 D_ov<=6W), C-3 (=Lemma B B-II/B-III imported, mult form 2kW).
Headline A'=6 on C-0 u C-1 u C-2. Residual: (R-C1) deep R4-clusters; (R-C2) Wsh>=1 beyond
 Lemma B conditions (its R1/R2). Write FINAL_LEMMA.md.
