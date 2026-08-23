# laneE1 PLAN (E1: close/refute branch-mass energy lower bound under RH)
1. Read laneP L-105058 doc + laneP/NOTES.md + lanep_num.py + num_results.json.
2. Read repo claims: T-105051, L-105052/53, O-105054 (dial context).
3. Re-verify L-105058.5 proof (H^2/Paley-Wiener off rho_1); check constants/windows.
4. E1a: sharp-vs-smoothed matching; u-blocks -> X-octaves via log U=(1/3)log X; U-cell bookkeeping.
5. E1b: RH remainder bound via truncated Perron + Hankel cut; edge-Y mechanism; verify I_w=0.49906.
6. Numeric duty: laneS out_big.json/out_uscan*; u m(u)^2 to 1e6; predicted vs measured table.
7. E1c: assemble theorem T-105059 draft OR honest residual map; forensic bootstrap check.
8. Circularity + quantifier checks (GATE all-L vs inf-many-L negation).
9. Write deposit-grade T-105059-draft.md in laneE1.
10. Final message: what closed, what resisted, bootstrap verdict. RH never claimed.

## L-105058.5 RE-VERIFICATION (step 3) — VERDICT: PROOF SOUND
Checked line by line: (1) F(s)=1/(s zeta(s+1)) on Re s>0: Abel + m bounded, T^{-s}m(T)->0. OK.
(2) J(h) <= A'/(2h)+O(1): partial integration vs Q(T)<=A'logT (T>=T0), int logT T^{-2h-1}=1/(2h)^2. OK.
(3) CS: int |m| u^{-sigma-1} du < inf for sigma > h'-1/2, any h'>0 with J(h')<inf => abs conv,
    F analytic Re s > -1/2; identity thm => 1/zeta(s+1) zero-free there (RH-strength; used only en route).
    Plancherel: phi_h(x)=m(e^x)e^{(1/2-h)x} in L2(0,inf), Mellin integral abs-convergent ON the line
    Re s=-1/2+h (uses J(h/2)<inf via CS) => hat(phi)=F a.e.; J(h)=(1/2pi)int|F|^2. OK.
(4) Schwarz on D(rho_1,1/2): zeta analytic there (|rho_1-1|=14.14>1/2); C_1(r_0)->|zeta'(rho_1)|
    (simplicity: rigorously known numerically); |s|^2->1/4+gamma_1^2; int dt/(h^2+tau^2)->pi/h. OK.
(5) c_0=2/((1/4+gamma_1^2)|zeta'(rho_1)|^2)=0.0158924 (|zeta'(rho_1)|=0.79316 checked). OK.
Cor 1, Cor 2 (io-blocks; else Q(2^J)<=C+(c_0-eps)J log2 contradicts limsup). OK.
Cor 3 CAVEAT: proves robustness for u-side log-scale smoothing at scale delta(u)->0 ONLY.
  The Hankel average in (.4)/(P-i) is SIGMA-side smoothing at scale 1/log N = DUAL variable:
  u-side it is a MACROSCOPIC reweighting of the tail (weight (1-log d/log N)^{-1/2}, = sqrt2 at
  d~U, NOT an approximate identity). Cor 3 does NOT cover E1's actual need. KEY FINDING.

## Edge-mechanism rederivation (step 5, Y-side, independent of laneP)
Bulk Y in (4U,N]: with C(x)=kappa sqrt(x) model, G_-=kappa sqrt(Y)[(1-2^{-1/2})-sqrt2(2^{-1/2}-2^{-1})]=0
  EXACTLY (= hatA_-(1/2)=0). Edge: Y in (N,2N]: G_-=kappa(sqrtN-sqrtY); Y in (2N,4N]: kappa(sqrtY/sqrt2-sqrt2 sqrtN).
E_edge=kappa^2 N [int_1^2(1-sqrt y)^2 dy/y + int_2^4(sqrt(y/2)-sqrt2)^2 dy/y] = kappa^2 N (3 ln2 - 2).
kappa=-2K/sqrt(pi logN) => E_edge=(4(3ln2-2)/pi) K^2 N/logN. Match vs laneP (2/pi^2)I_w K^2 N/logN
REQUIRES I_w = 2pi(3 ln 2 - 2) = 0.499144... (laneP numeric 0.49906, coarse grid). VERIFY EXACTLY.

## E1 ANALYSIS RESULTS (steps 4-5, full derivations in session; deposit draft to follow)
R1 [E1b CLOSES, RH, PROOF-STANDARD]: truncated Perron at kappa=1/2+1/logN, T=N; shift to
  Re w=1/2+eps with cut-hugging Hankel at w=1 (cut (1/2,1], b=((w-1)zeta)^{1/2} single-valued
  on half-plane under RH). Ingredients: RH => 1/zeta<<|t|^eps on sigma>=1/2+eps; M_U(w)-1/zeta(w)
  << U^{1/2-sigma+eps}|t|^eps (RH-Perron, Titchmarsh 14.25-type); horizontals << N^{-1/2+2eps};
  Perron error << N^eps. RESULT: Sigma_N(gamma) = HankelLoop_N(gamma) + O(N^eps), gamma in [1,2].
R2 [FINDING - E1a matching FAILS as planned]: loop coefficient = K_N = (1/sqrt(pi)) int R_U(1-v/logN)
  b(.) e^{-v} v^{-1/2} dv, NOT m(U)(1+o(1)): sigma-side smoothing = u-side MACROSCOPIC reweighting
  (weight (1-logd/logN)^{-1/2} = sqrt2 at d~U). Cor 3 covers u-side smoothing only: DOES NOT APPLY.
  Pointwise matching unreachable (R_U cut-variation >> m(U) by exp((logU)^{1/2+o(1)})/logN under RH).
  NUMERIC CONFIRMATION: slope 2.02 = |sqrt2|^2 in O-vs-pred fit.
R3 [NEW REDUCTION - kills gap g2]: CS on the outer edge band: int_{2N}^{4N} G dY/Y =
  -sqrt2 ln2 [C(N) - (1/ln2)int_{N/2}^N C dx/x] => E(L) >= 2ln2 int_oct Lambda(X)^2 dX/X, EXACT,
  UNCONDITIONAL, where Lambda = sum_{N/2<n<=N} h_U(n) n^{-1/2} ln(2n/N)/ln2 (tent sum). No K, no
  window-variation error, no RH.
R4 [THE remaining gap g1']: W-PW-lemma: W_u := Lambda sqrt(log N)/u ~ u^{-1/2}-scale; prove
  limsup (1/logT) int u W^2 du/u >= c0' > 0 via L-105058.5 machinery. Mellin of tent field:
  two-variable pinch (1/2pi i)int dz/z 2^{-z} zeta(w-z)^{1/2}/zeta(w+z): branch point w-z=1 pinches
  zero w+z=rho at s=2w-1=rho: RAW singularity (s-rho)^{-1/2} (log(1/h) blowup: TOO WEAK - this is
  the eta-partner HALF-SINGULARITY WALL = T-105051's negative-moment obstruction, now precise);
  sqrt(log)-weight restores full pole (model: F=(s-a)^{-1/2} <-> u^a/sqrt(pi ln u); weight sqrt(ln u)
  => (1/sqrt(pi))/(s-a)). Pinch-coefficient computation = the single open analytic step.
R5 [BOOTSTRAP UPGRADE]: If R4 closes, chain is UNCONDITIONAL: E(L) >= c 2^{L/3}/L io (no RH!)
  => not GATE_theta for all theta<1/3 => not GATE_{o(1)}. RH bootstrap no longer needed for the
  negative gate verdict; RH enters only for Theta_gate = 1/3 exactly (upper via T-105051 III).

## FINAL STATUS
Deposit draft written: T-105059-branch-energy-e1-closure-report.md
CLOSED: L-105058.5 audit (sound); edge lemma + I_w=2pi(3ln2-2) exact; E1b remainder O(N^eps)
under RH (PROOF-STANDARD); CS tent reduction E(L) >= 2ln2 int Lambda^2 (exact, unconditional);
cell/octave bookkeeping; bootstrap logic audit. NUMERICS: 212-pt corr 0.9975, slope 2.02=|sqrt2|^2.
NOT CLOSED: E1a in original form REFUTED (K != m(U)(1+o(1)); Cor 3 inapplicable); replaced by
single open W-pinch lemma (w1)-(w4). E1 overall: OPEN, reduced to one unconditional analytic lemma.
