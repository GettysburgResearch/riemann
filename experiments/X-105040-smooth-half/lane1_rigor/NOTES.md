# Lane 1 (RIGOR) working notes — T-105040

## Setup (from branch claude/riemann-proof-review-8nz34i)
- L-105031 dumped to ./L-105031.md. Definitions confirmed against
  experiments/X-105030-maximal-license-and-circ13/lane_repair/{core,fast,lattice,identity}.py:
  * T_x(d) = (4 sqrt(x/d) - 3)/sqrt(d); rho_j(d) = Q_{x/d}(j)/(4 sqrt(x/d)-3);
    s(d) = (5 sqrt(Y)-3)/(4 sqrt(Y)-3), Y = x/d.
  * Q_Y(j) = sum_{j<=m<=Y} gamma_j(m) m^{-1/2} log(Y/m); gamma_j(j)=A_j=(j+1)/(j-1),
    gamma_j(j+1)=-B_j=-(j+1)(j-2)/(j(j-1)), gamma_j(m)=C_j=2/(j(j-1)) for m>j+1.
    Knot form (valid Y>=j+1, and trivially for Y in [j,j+1)):
    Q_Y(j) = A_j log(Y/j)/sqrt(j) - B_j log(Y/(j+1))/sqrt(j+1)
             + C_j [H(Y) - sum_{m<=j+1} log(Y/m)/sqrt(m)],  H(Y)=sum_{m<=Y} m^{-1/2} log(Y/m).
  * Greedy: evens (mu=+1) sorted by d ascending, prefix fill to demand D = sum_odds T(o).
  * M_j = sum_e theta*(e) Q_{x/e}(j)/sqrt(e) - sum_o Q_{x/o}(j)/sqrt(o);
    M_sc = sum_o T(o)s(o) - sum_e theta*(e) T(e) s(e).

## DERIVATION 0 (edge audit item 2): M_sc identity from demand equality
T(d)s(d) = (5 sqrt(Y)-3)/sqrt(d) = 5 sqrt(x)/d - 3/sqrt(d).
Demand equality sum_e theta* T(e) = sum_o T(o) gives
  sqrt(x)(sum_e theta*/e - sum_o 1/o) = (3/4)(sum_e theta*/sqrt(e) - sum_o 1/sqrt(o)).
Hence M_sc = -(3/4)(sum_e theta*/sqrt(e) - sum_o 1/sqrt(o))
           = (3/4)[ sum_e (1-theta*)/sqrt(e) - B^s_x ],  B^s_x = sum_{d<=x} mu(d)/sqrt(d).
EXACT, purely algebraic. Matches Corollary R.1 of L-105031. (Numeric check planned.)

## LEMMA 1 (expansion of H) — proof chain
S(N)=sum_{m<=N} m^{-1/2}, L(N)=sum m^{-1/2} log m; H(Y)=S(N)logY - L(N), N=floor(Y).
Euler-Maclaurin (order 1, B1tilde(t)={t}-1/2, b(t)=int_N^t B1 = ({t}^2-{t})/2 in [-1/8,0]):
(A) S(N) = 2 sqrt(N) + zeta(1/2) + 1/(2 sqrt N) + R_S,  |R_S| <= N^{-3/2}/16  (all N>=1).
    Constant = zeta(1/2) via zeta(s) = s/(s-1) - s int_1^inf {t} t^{-s-1} dt (Re s>0):
    zeta(1/2) = -1 - (1/2)int_1^inf {t}t^{-3/2} dt; matches the EM constant -3/2 - (1/2)int({t}-1/2)t^{-3/2}.
(B) L(N) = 2 sqrt N log N - 4 sqrt N - zeta'(1/2) + log N/(2 sqrt N) + R_L,
    |R_L| <= (log N)/16 * N^{-3/2}   for N >= 15  (needs g'(t)=t^{-5/2}((3/4)log t - 2) >= 0,
    i.e. t >= e^{8/3} = 14.392; |int_N^inf B1 g| <= (1/8) int_N^inf |g'| = (1/8)((logN)/2 - 1)N^{-3/2}).
    Constant = -zeta'(1/2) by differentiating the continuation formula at s=1/2:
    zeta'(1/2) = -4 - I0 + I1/2, I0=int {t}t^{-3/2}, I1=int {t}t^{-3/2} log t; EM constant c1 = 4 + I0 - I1/2.
(C) Recombination with Y = N + delta, u = delta/N <= 1/N:
    phi = 2 sqrt N log(Y/N) + 4 sqrt N - 4 sqrt Y, |phi| <= sqrt(N) u^2 = delta^2/N^{3/2} <= N^{-3/2}
    (from u - u^2/2 <= log(1+u) <= u; 1 + u/2 - u^2/8 <= sqrt(1+u) <= 1 + u/2).
    log(Y/N)/(2 sqrt N) <= 1/(2 N^{3/2}).
==> LEMMA 1: for real Y >= 15,
    |E(Y)| <= (log Y + 11)/(8 floor(Y)^{3/2}) <= (log Y + 11)/(8 (Y-1)^{3/2}).
    (1 + 1/2 from phi+midterm, logY/16 + logN/16 <= logY/8 from tails; 11/8 >= 3/2 - 1/8.)
E is continuous, piecewise-smooth; on each cell E' = (S(N)-zeta(1/2))/Y - 2/sqrt(Y) has at most
one zero Y* = ((S(N)-zeta(1/2))/2)^2, E unimodal (up then down) => cell extrema at endpoints/Y*.
So checking all integers + all Y* gives the TRUE sup on [2, 1e5]. Verification: lemma1_verify.py.

## LEMMA 2 (saturated margins) — derivation
Lattice L = squarefree d | P61 (2^18 divisors). x >= x_sat := 5 P61 => all Y=x/d >= 5 >= j+2.
Expansion of Q: Q_Y(j) = 4 C_j sqrt(Y) + lam_j log Y + kap_j + C_j E(Y), with
  lam_j = A_j/sqrt(j) - B_j/sqrt(j+1) + C_j [zeta(1/2) - sum_{m<=j+1} m^{-1/2}],
  kap_j = -A_j log j/sqrt j + B_j log(j+1)/sqrt(j+1) + C_j [zeta'(1/2) + sum_{m<=j+1} log m/sqrt m].
Threshold lock: evens sorted ascending; A_O = sum_odds 1/o EXACT rational (denominator P61);
e* := first even with cumulative sum_{e<=e*} 1/e > A_O; U = {evens < e*};
g = A_O - A_U in (0, 1/e*) exact rational, g2 = A_{U+e*} - A_O > 0 exact rational,
h = B_O - B_U (B = sum 1/sqrt). Greedy threshold equals e* for ALL x with
sqrt(x) > 3h/(4g)  (theta*>0; theta*<1 automatic since h > 1/sqrt(e*)); x* := (3h/(4g))^2.
theta*(x) = (4 sqrt(x) g - 3h)/T_x(e*) = theta*_inf + 3(g sqrt(e*) - h)/T_x(e*),
theta*_inf = e* g (exact rational). KEY: Delta_B^inf := B_U + theta*_inf/sqrt(e*) - B_O = g sqrt(e*) - h,
so Delta_B(x) = Delta_B^inf (1 + 3/(sqrt(e*) T_x(e*))) and sqrt(e*)T_x(e*) = 4 sqrt(x/e*) - 3. Hence
  M_sc(x) = -(3/4) Delta_B(x) = M_sc^inf * 4 sqrt(x/e*) / (4 sqrt(x/e*) - 3),  EXACT (no E terms),
  M_sc^inf = -(3/4)(g sqrt(e*) - h) — decreasing in x, > M_sc^inf.
Rows: the 4 C_j sqrt(x) * (A_U + theta*/e* - A_O) leading term is KILLED EXACTLY by demand
equality: A_U + theta*/e* - A_O = (3/(4 sqrt x)) Delta_B(x). Result:
  M_j(x) = lam_j Delta_B(x) log x + (3 C_j + kap_j) Delta_B(x) - lam_j Delta_L(x) + C_j Etil_j(x),
  Delta_L(x) = L_U + theta*(x) log(e*)/sqrt(e*) - L_O  (L = sum log d/sqrt d),
  Etil_j(x) = sum_{e in U} E(x/e)/sqrt e + theta* E(x/e*)/sqrt(e*) - sum_o E(x/o)/sqrt o.
Line form: M_j(x) = alpha_j log x + beta_j + err_j(x),
  alpha_j = lam_j Delta_B^inf,  beta_j = (3C_j + kap_j) Delta_B^inf - lam_j Delta_L^inf,
  err_j(x) = (3 Delta_B^inf/(sqrt(e*)T_x(e*))) [lam_j log(x/e*) + 3C_j + kap_j] + C_j Etil_j(x),
  first piece > 0 for x >= x_sat (bracket < 0, Delta_B^inf < 0), |Etil_j| <= env(x) via Lemma 1.
Hand-check vs orchestrator: lam_2 = 3/sqrt2 + zeta(1/2) - (1+1/sqrt2+1/sqrt3) ~ -1.62349,
lam_3 ~ -0.59357; Delta_B^inf ~ -(4/3)(13.9039) ~ -18.5385 => alpha_2 ~ 30.098, alpha_3 ~ 11.004. MATCHES
orchestrator slopes 30.1 / 11.0 and increments (139/50.7 per 100x). To be machine-verified.

## Status log — ALL DONE
- [x] lemma1_verify.py: proved-bound worst ratio 0.0486 (Y=15, for Y>=15 form);
      (Y-1)^{3/2} form worst ratio 0.0441 over [2,1e5]; sup|E|[2,16]=0.0288203 (Y=2);
      sup|E|[5,16]=0.0074255 (Y=5); |E|sqrtY/(logY+2) worst 0.0151340 (Y=2)
      => clean weak pair K=1/50, c=2 valid (proved Y>=20 from strong bound, verified [2,20]).
      E(10^k) = -2.633e-3/-8.333e-5/-2.635e-6/-8.333e-8/-2.635e-9 (k=1..5) ~ -(1/12)Y^{-3/2}.
      Knot form == gamma-sum Q to 1e-28; Qdirect - Qexp == C_j E(Y) to 1e-27. dps=30.
- [x] lattice_sat.py (after fixing my own T_at bug: T=(4 sqrt(x/d)-3)/sqrt d — first run
      had 4 sqrt(x/d)-3/sqrt d, gave theta*(x)->0.0126 and M2(1e26)=1472.23, off by ~1.06;
      exact-rational threshold section was unaffected):
      P61=117288381359406970983270 (~1.1729e23), x_sat=5P61=5.8644e23.
      e*=1110, |U|=131, sliver above e* = 130940 (orchestrator's 130941 counts e* itself).
      g=3.782726150280e-4 EXACT rational >0; g2=5.226282858729e-4 EXACT >0; no ties (int compare).
      theta*_inf = 1110 g = 0.419882602681071 EXACT rational in (0,1).
      x* = (3h/4g)^2 = 1.3529e9 << x_sat. h=18.5511552769738, h2>0 => theta*<1 automatic.
      A^s=0.131587351850 exact; B^s=0.00221440063387 == prod(1-1/sqrt p) [orch: 0.002214 OK].
      Delta_B^inf = g sqrt(e*)-h = -18.538552495926711447 (two routes agree to 20 digits);
      M_sc^inf = 13.903914371945 [orch 13.9039 OK]; Delta_L^inf = -218.16354112404407.
      lam2=-1.62349121562612 kap2=-4.26862018208013 alpha2=30.0971771275607 beta2=-330.668210741888
      lam3=-0.593569981349335 kap3=-1.50816534292762 alpha3=11.0039282592509 beta3=-120.074679149629
      Predictions: 1e26: M2=1471.16588554 M3=538.699831379 Msc=13.903914372 [orch 1471.17/538.70/13.9039]
                   1e28: 1609.76850832/589.374793726; 1e30: 1748.37113111/640.049756074;
                   1e34: 2025.57637669/741.399680771 [orch rounded 1610/589,1748/640,2026/741 all OK]
      Positivity at x_sat: M2>=1316.5009511, M3>=482.152274, Msc>13.903914; drift brackets
      -78.7/-28.8 <0 => err drift term positive for all x>=x_sat.
- [x] greedy_sat.py: INDEPENDENT literal greedy (no reduction algebra), x=1e26 dps30:
      e*=1110, theta*=0.41988260113773608356 (matches closed form to all digits),
      M2=1471.16588553533, M3=538.69983137915, Msc=13.9039143719798;
      Msc identity R.1 agrees to 1.41e-15.
- [x] frozen_1e6.py: direct-Q frozen greedy at x=1e6 (6945 active divisors):
      m2=106.198616 m3=39.393326 m_sc=10.744251 [L-105031(f): 106.2/39.4/10.7 OK];
      e*=899 theta*=0.123455171; Msc identity diff 1.30e-12;
      expansion-vs-direct margin deltas 1.9e-4 / 1.7e-5 (E-neglect, small-Y regime);
      zero-row-mass odds: j=2: 903 odds (demand 1.9282, row mass 0); j=3: 1341 (4.1640).
- [x] envsup.py: ENVSUP = sup_{x>=x_sat} |Etil_j| bound = 1.0801e-12 (uniform in x;
      handles the BND jump at Y=15 by taking per-divisor sup over [x_sat/d, inf);
      only d = P61/2, P61/3 have x_sat/d < 15).

## Final error decomposition (exact)
M_j(x) = alpha_j log x + beta_j + err_j(x),
err_j(x) = 3 Delta_B^inf [lam_j log(x/e*) + 3C_j + kap_j] / (4 sqrt(x/e*) - 3)  +  C_j Etil_j(x);
first piece EXACT closed form, positive and decreasing on [x_sat, inf) (bracket<0 there,
checked at x_sat, monotone since lam_j<0); |Etil_j| <= 1.081e-12 uniformly.
At x_sat the drift is ~4.8e-8. Hence for all x >= x_sat:
  M_j(x) >= alpha_j log x + beta_j - C_j * 1.081e-12,
  M_2 >= 1316.5009511, M_3 >= 482.1522743, and
  M_sc(x) = M_sc^inf * 4 sqrt(x/e*) / (4 sqrt(x/e*) - 3) > M_sc^inf = 13.9039143719 (EXACT, no E).
