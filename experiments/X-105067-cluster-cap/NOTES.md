# Lane T PLAN (cluster tree / per-cluster count cap, residual R-C1)
1. Read FINAL_LEMMA.md (esp S3 Steps 2-4, S6 R-C1) + LEMMA_A.md; extract exact defs: h', B, phi_j, deep/shallow, R4, cluster.
2. Verify orchestrator claim: C-2 Step 2 budgets (shallow+non-ov) are pointwise & (Sep)-free => Q=B-Phi'_far has Q''>0, Q''''>0 on G.
3. Set F = Phi'_K - Q on K_span∩G; Phi'_K rational, denominator D = prod (t-x_j)^2+y_j^2)^... explicit degree.
4. Attempt rigorous closure: multiply by D>0: zeros of h' = zeros of (P - D*Q); use derivative chain w/ sign info on Q'',Q''''.
5. If general m fails, prove fixed-m cap: Z <= c*m via "rational of degree d minus 2-4-convex background has <= C(d) zeros" — verify or refute.
6. Numeric duty: exhaustive 2-pair cluster scans (same scale/nested/straddle), then 3-pair; test Z<=6m; hunt counterexamples.
7. Write deposit-grade L-105067 draft in this dir; record honest residuals (unbounded m, any gaps).
8. Keep every response <200 lines; final <1500 words leading STATEMENTS PROVED.

## D1. Core derivation (Theorem T-1 skeleton)
Setup: G=(a,b), h' = Phi - Q, where Phi := Sum_{ALL deep ov pairs j=1..m (distinct z_j, mult m_j)} m_j phi'_j
(rational: Phi = N0/Prod q_j^2, q_j=(t-x_j)^2+y_j^2>0, deg N0 <= 4m-2), and
Q := B - Sum_{shallow ov} m_i phi'_i - Sum_{non-ov} m_i phi'_i  (NO deep pairs in Q at all).
Sign facts (pointwise on G, (Sep)-FREE):
 (a) Q > 0 under (L2): B >= 8/g^2; shallow positive parts <= (8/g^2)W_sh [C-2 Step1]; non-ov <= 0.
 (b) Q'' > 0 under (L4): C-2 Step2 clauses (i)(iii)(iv) only — B.3/B.4 are pointwise on G (checked).
 (c) Q'''' > 0 under (L6): same.
Triple set: T := {t in G : Phi>0} ∩ {Phi''>0} ∩ {Phi''''>0}.
Hypothesis (T-EMPTY): T = emptyset.
Chain: zeros of h' need Phi=Q>0 => in Omega := {Phi>0}∩G, #comp <= 2m (deg N0<=4m-2)
 [also Omega ⊆ ∪ I_j since sum of nonpositives <= 0].
Zeros of (h')'' need Phi''=Q''>0 => in {Phi''>0}: Phi'' = N2/Prod q_j^4, deg N2<=8m-4, #comp <= 4m-1.
Pieces V := comps of Omega ∩ {Phi''>0}: #V <= 2m + (4m-1) = 6m-1.
On each V: Phi''''<=0 (else V∩{Phi''''>0} ⊆ T nonempty) => (h')'''' = Phi''''-Q'''' < 0:
 h'' strictly concave on V => Z_mult((h')'',V) <= 2 [LEMMA A Step 3 concavity argument].
On omega\∪V: (h')'' = Phi''-Q'' < 0. So Z_mult((h')'',omega) <= 2 #V(omega), finite =>
(Rolle contradiction) (h')' and h' have finitely many zeros on omega; Rolle-with-mult twice:
 Z_mult(h',omega) <= Z_mult((h')'',omega) + 2.
Total: Z_mult(h',G) <= Sum_omega [2#V(omega)+2] <= 2(6m-1) + 2(2m) = 16m - 2.
extra(G) <= Z_mult(h',G) <= 16m - 2 <= 16 W(G)  [each deep pair: weight m_j >= 1 => m <= W].
If m=0: h' = -Q < 0 under (L2) alone: extra = 0.
KEY PROP: (Sep) => (T-EMPTY). Pf: t outside all Itilde_j: all f_j<=0 => Phi<=0. t in Itilde_j:
 others R4-far => their f,f'',f'''' <= 0 => triple positivity forces f_j>0 & f_j''>0 & f_j''''>0
 => |s_j|<y_j & |s_j|>(sqrt2-1)y_j & (|s_j|<(2-sqrt3)y_j or |s_j|>y_j) = empty since 2-sqrt3<sqrt2-1. QED
=> T-1 strictly contains C-2's regime. Single pair m=1: T-EMPTY automatic (same table).
METHOD-NECESSITY: if T has interior [c,d] with margins m0,m2,m4 >0, then Q_N := Phi - eps sin(omega t),
 eps < min(m0, m2/omega^2, m4/omega^4): Q_N,Q_N'',Q_N''''>0 on [c,d], Phi-Q_N = eps sin has ~omega(d-c)/pi
 zeros: NO bound from (Q>0,Q''>0,Q''''>0) alone. So T-EMPTY is exactly the frontier of the 0-2-4 method.

## D2. Sharpened constant + numeric findings on T-EMPTY
Sharper comp counts: Phi ~ -2(Sum m_j)/t^2 <0 at +-inf => #comp{Phi>0} <= (4m-2)/2 = 2m-1.
Phi'' ~ -12(Sum m_j)/t^4 <0 at +-inf => #comp{Phi''>0} <= (8m-4)/2 = 4m-2.
Pieces (merge bound: comps of A∩B <= compA+compB-1): <= 6m-4.
TOTAL: Z_mult(h',G) <= 2(6m-4)+2(2m-1) = 16m-10.  m=1 => 6 = LEMMA A constant (consistency!).
extra(G) <= 16m-10 <= 16 W(G).
NUMERIC (t1_triple.py):
 - m=1: T empty (margin 0.0) as proved.
 - equal scales (rho=1): T empty up to mult ratio ~1.75; NONEMPTY at mu=1.75 (c=0.672).
   mu=3.4, c=0.7: margin 0.258 — nonempty (hand example confirmed).
 - UNEQUAL scales: T NONEMPTY at UNIT multiplicities for rho<=0.8 (e.g. pairs (0,.8,1),(0.05,1,1),
   t*=-0.849: L0=+0.031, L2=+10.0, L4=+4.1). MECHANISM: pair-small's OUTER band u in (1,sqrt2+1)
   has signature (f,f'',f'''')=(-,+,+) with |f| tiny; pair-big's inner band (sqrt2-1,1) has (+,+,-);
   small-scale supplies L4>0 (~1/y_small^6) and L2, big-scale supplies L0. Robust, not a grid artifact.
 => T-EMPTY strictly contains (Sep) but does NOT cover scale-separated 2-clusters even with m_j=1.
 Refined residual R-C1' := clusters with nonempty triple set (checkable finite criterion per cluster).

## D3. Final status (2026-08-23)
PROVED: Theorem T-1 (per-cluster cap 16 m_K - 10, hence extra <= 16 W, under
(L2)(L4)(L6) + T-EMPTY; NO (Sep)); Prop T-2 ((Sep) => T-EMPTY; m_K=1 => T-EMPTY;
so T-1 regime strictly contains C-2's; m=1 constant = 6 = LEMMA A, consistency);
Prop T-3(a) (eps*sin(omega t) local counterexample: the 0-2-4 pointwise-sign method
cannot go beyond T-EMPTY).
CERTIFIED EXAMPLES (T nonempty, 40-dps replays): equal-scale mu=3.4 (2.011,4.806,20.86);
unit-mult (0,.8,1),(0.05,1,1) t=-.849 (0.0301,10.02,4.162); 13 unit pairs, islands
+-(0.1046,0.2035), t=-.1540 (2.191,6.459,410.5).
SCANS: 600 budget-passing configs, 0 violations of cap/confinement/2M (bracket-overlap
attribution needed — midpoint attribution false-flags, same as capC incident).
Adversarial nonempty-T families (B tuned to graze Phi, gaps to 128): Z(h')=2 always.
Coverage of random genuine clusters by T-EMPTY: ~99% (k=2 near-equal unit) to ~25-60%
(k=5 spread). ORCHESTRATOR CLAIM REFUTED: "degree-d rational minus (0,2,4)-convex
background has <= c*d zeros" is FALSE whenever the rational's triple set has interior
(T-3(a)); the suggested fixed-m closure cannot work as stated; T-EMPTY is the exact
salvage. RESIDUAL R-C1' recorded: clusters with T_K nonempty.
Deliverable: L-105067_DRAFT.md (this dir).
