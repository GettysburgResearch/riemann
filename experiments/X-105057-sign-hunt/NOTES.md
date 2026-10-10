# Lane S PLAN (sub-diagonal reformulation + deep sign hunt)
1. Read L-105053, O-105054, T-105051, X-105053 ANALYSIS + hhfe_energy.py + results.json.
2. Re-derive Gram split H = D + O; state reformulation lemmas (i),(ii) precisely.
3. Write O-105057 claim draft (reformulation only, no overclaim).
4. Implement q-fiber form of O: O = sum_{(a,b)=1, a>b, a/b<4} 2 R(log a/b)(ab)^{-1/2} S_q(a,b), S_q = sum_q h(qa)h(qb)/q, qa<=N.
5. Validate fiber form vs deposited exact values at 1e4..1e6 (target 1e-10 rel).
6. Push X: 1e7, 1e8; sample beyond if feasible. Log O(X) on log-dense grid.
7. Sign-change census; [O]_+ octave integrals; drift constant fit.
8. Small-X scan X<1e4 all U regimes; U=X^theta robustness theta in {0.25,1/3,0.4}.
9. Late: read laneM NOTES for drift constants comparison.
10. Final: STATEMENTS PROVED + data summary; replay script deposited in laneS/.

## Band-separation identity (replaces q-fiber form; EXACT, O(N))
R piecewise linear in v=ln(m/n): on (0,h]: 3h-(3+s2)v; on (h,2h): -2*s2*h+s2*v (h=ln2,s2=sqrt2).
c_n=h_U(n)/sqrt n, d_n=c_n ln n, C(x)=sum_{j<=x}c_j, Dp(x)=sum_{j<=x}d_j. Then
O = 2 sum_n c_n [ (3h+(3+s2)ln n)(C(m2)-C(n)) - (3+s2)(Dp(m2)-Dp(n))
                 + (-2 s2 h - s2 ln n)(C(m4)-C(m2)) + s2 (Dp(m4)-Dp(m2)) ],
m2=min(2n,N), m4=min(4n-1,N)  [m=4n has R=0, excluded harmlessly; m=2n: R continuous at v=h].
Exact rearrangement of the deposited pair sum. Cost O(N) after h build (sieve O(N loglog)).
=> X=1e12 needs N=1e8: feasible. Validate vs deposited O_signed at 1e4..4e6 to <=1e-10.

## Reformulation lemmas to prove (O-105057 draft)
S1: H>=0, D>=0 pointwise => O = H-D >= -D >= -X^{o(1)} ALWAYS (unconditional lower bound on O!).
S2: [O]_+ <= |O| <= [O]_+ + D; [H-D]_+ <= H; H <= D + [O]_+.
    => octave gates equivalent: int[O]_+ ~ int H ~ int|O| up to int D = 2^{o(L)}.
S3: (sign conj) O(X)<=polylog for all X>=X0 => gate. a.e. version needs exceptional-set
    measure(dX/X) <= 2^{-(2/3)L}*2^{o(L)} vs trivial sup [O]_+ <= O_abs << X^{2/3+o(1)}.

## FINDINGS (running log, 2026-08-23)
F1. Band evaluator validated: <=2e-13 vs deposited pair sums (9 X values), Gram err <=2e-13.
F2. Dense grid 100 pts, 1e4..9.3e8, U=X^{1/3}: ALL O<0, O in [-3.43,-1.66], H in [0.52,2.33].
F3. Small-X COMPLETE census X in [8,10^4]: O(X)<=0 for EVERY X>=8 (O=0 iff pair set empty,
    X in {8,9}); strictly negative X>=10. NO positive O at small X in canonical regime.
F4. theta-robustness: theta=1/3, 0.4 all negative on 1e4..1e8. theta=0.25 POSITIVE windows
    (X~4e7..2e8, O up to +13.0, H up to 17.9) — verified vs exact sweep (err 1e-10).
    Negativity is a property of U >= X^{1/3}, NOT universal.
F5. BIG: canonical regime HAS SIGN CHANGES: O(4e10)=+0.604 (f128 + sweep verified),
    O(1e12)=+0.939 (f128 verified). Positive across entire U-cells (U=3418..3420 all >0,
    smooth in U, jump at U-increment). STRICT sign conjecture (O<=0 eventually) EMPIRICALLY
    FALSE; gate-compatible: positives are O(1) size.
F6. Oscillation fit vs gamma_1=14.1347 (ln U and ln N frequencies): R^2 <= 0.14, FAILS.
    Positives are +3.4..3.8 outliers vs any linear+single-zero model. Mechanism unresolved.
F7. laneM: signed low-torsion drift skeleton sum -> ~0, NOT -2.3; exact second moment
    (8-6 sqrt2) log 2. Consistent with F5: negativity not a convergent-drift constant,
    and indeed not even permanent (sign changes exist).

## FINAL LOG
F8. Onset located: first positive O in canonical regime at U=2782, X=2.154e10 (O=+0.018);
    U-scan 1000..2780 step 20 all negative (near-miss -0.437 at U=2780, -0.453 at U=1420).
F9. Top scan U=8400..10800 step 100: 13/25 positive; O in [-4.03,+9.54]; rapid multi-window
    oscillation; O(U=9900)=+9.538 (X=9.7e11).
F10. Octave stats (304 pts): E_+ estimate 0 for L<=33; 0.13 (L=34); 1.39 (L=39); 0.84 (L=40).
     mean H: 0.55 (L=13) -> 5.5 (L=39): growth polylog-vs-X^0.1 UNRESOLVED. Gate unfalsified.
F11. Signed octave mean O: -2.15 -> -3.1 (L=33) -> +0.70 (L=39). Drift -2.3 is transient.
Files: fast_O.py (evaluator+validation), deep_run.py, big_run.py, small_run.py, theta_run.py,
uscan*.py, verify_pos.py, out_*.json; claim draft O-105057-*.md. Largest exact point: X=1e12
(N=1e8, 30 s/eval, f128 check 72 s).
