# LANE CAP-B PLAN (shallow cooperation: all overhanging y_j >= g/2)
1. Read repo lemma L-105061 for context (sec 4 saturation).
2. sympy: exact constants c_m = max_u |d^m phi'(u;y)| * y^{m+2} for m=1,2,3 (scale-invariant).
3. Prove B^{(k)} in-gap lower bounds: B >= 8/g^2, B'' >= 192/g^4, B'''' >= ... general even k.
4. Key induction: zeros of h^{(k)} confined + counted via B^{(k)} floors vs |Phi^{(k+1)}| ceilings.
5. Careful: only pairs with I_j meeting G matter? No — Phi'' sums over ALL j; must bound far-pair tails. Handle: split near (|x_j - G| <= dist) vs far; far tail bounded by B-type comparison? Verify.
6. Derive extra(G) <= 2 + C*W for W < W0 (small-W regime) via h''' < 0 argument.
7. Large-W regime: iterate levels or crude count; get linear-in-W bound.
8. Numeric duty: adversarial scans m=2..30 pairs, y in [g/2,1/2], count real zeros of h in gap.
9. Fold multiplicity capping.
10. Write LEMMA_B.md deposit-grade.

## DERIVED (step 1) — exact backbone
- phi'_j(t) = -2Re(t-z_j)^{-2}; hence h^{(k)}(t) = -(k)!*? precisely:
  h'(t) = -Re Sum_rho m_rho (t-rho)^{-2} (rho over ALL zeros: real + both pair members),
  h^{(j+1)}(t) = -(j+1)!*(-1)^j ... clean: d^j/dt^j (t-rho)^{-2} = (-1)^j (j+1)!(t-rho)^{-(j+2)}.
  So h^{(2k+1)}(t) = -(2k+1)! Re Sum_rho m_rho (t-rho)^{-(2k+2)}.  [SIGN: even # of derivs on h', (-1)^{2k}=+1]
- Re(u+iy)^{-n} = cos(n*theta)/r^n, r^2=u^2+y^2, theta=-atan2(y,u)... |Re(t-z)^{-n}| <= r^{-n}.
- Real zero at distance d: contributes +m/d^{n} (n=2k+2, positive). Endpoint floor:
  Re-sum >= 1/d_a^n + 1/d_b^n - hurt, since ALL real-zero terms positive.
- Pair {z,zbar}: contributes 2 m_j Re(t-z)^{-n} >= -2 m_j / r_j^n, r_j^2=(t-x_j)^2+y_j^2 >= y_j^2.
- Shallow ov pair (y_j >= g/2): hurt_j <= 2 m_j / y_j^n. Floor unit (one endpoint at worst
  position d = g/2): 1/(g/2)^n. Ratio: 2 m_j (g/2y_j)^n = 2 m_j w_j^{n/2}, w_j=(g/2y_j)^2 <= 1.
  Using BOTH endpoint terms: floor >= 2*(2/g)^n. So h^{(2k+1)} < 0 on G whenever
    Sum_ov m_j w_j^{k+1} < 1   [n=2k+2; hurt Sum 2 m_j w^{k+1} (2/g)^n < 2 (2/g)^n]
  (plus non-ov load allowance; sharper with kappa-band constants at k=1: W4 < 1/kappa = 2.885
   when using per-t band restriction? NO - band restriction needs t in band; pointwise safe bound
   uses kappa only for pairs hurting at that t; conservative clean condition: Sum m_j w_j^{k+1} < 1.)
  CHECK the constant: hurt <= Sum 2 m_j/y_j^{2k+2} = Sum 2 m_j (2/g)^{2k+2} (g/2y_j)^{2k+2}
   = 2 (2/g)^n Sum m_j w_j^{k+1}. Floor >= 2 (2/g)^n. ==> condition Sum_ov m_j w_j^{k+1} < 1. YES.
  With kappa refinement (only banded pairs hurt, max band hurt 2*kappa m_j/y^4 at k=1):
   condition W4 := Sum m_j w_j^2 < 1/kappa = 2.8854 (k=1, no non-ov load).
- LADDER COUNT: h^{(2k+1)} < 0 on G ==> Z_mult(h^{(2k)},G) <= 1 ==> (Rolle w/ mult, j steps)
  Z_mult(h', G) <= 2k ==> Z_mult(h, G) <= 2k+1 ==> extra <= 2k.
- Choose k minimal with Sum m_j w_j^{k+1} < 1: since Sum m_j w_j^{k+1} <= w_max^{k-1} W2,
  k <= 1 + ceil( log(W2)/log(1/w_max) ) when w_max < 1. W2 := Sum m_j w_j^2 <= W.
  ==> extra <= 2 + 2*ceil(log_+ (W2) / log(1/w_max)). Blows up only as w_max -> 1 (critical pairs).
- Non-ov pairs: at level n, left non-ov pair has r^2 >= (y_j+d_a)^2: hurt <= 2m_j/(y_j+d_a)^n
  vs endpoint 1/d_a^n: ratio 2 m_j (d_a/(d_a+y_j))^n. Hypothesis (load): for all t in G, sides:
   L_n(t) := Sum_{nonov left} 2 m_j (d_a/(d_a+y_j))^n <= 1-theta (same right) and
   Sum_ov m_j w_j^{k+1} < theta ==> negativity. Note: only pairs in a cos(n theta)<0 band hurt at
  all; and hurting far stacks must be charged to THEIR OWN gaps by the assembly (interface note).

## FINAL STATE
- LEMMA_B.md deposited (234 lines): Thm B-I (anchored excitation, uncond.),
  Thm B-II (ladder cap, explicit conditions (B.7)/(B.8)), Cor B-III (explicit caps,
  log-in-W, linear via safety net), remainder (R1) near-critical concentration +
  (R2) band-adjacent non-ov mass, numerics, falsifiers.
- Exact constants: kappa=(11+5sqrt5)/64, 1/kappa=16(5sqrt5-11)=2.8854,
  G_4=0.022543, G_n <= 2e^{-pi/2} < 5/12 (proved).
- Numerics: 600-config scan max extra=2; 80 admissible configs h'''<0 all;
  slicing attacks fail (drown before slicing); mpmath 40dps replay: extra=2 at W=18.1.
- Suggested-angle correction recorded: the naive factorial ladder gains NOTHING
  (floor/ceiling ratio is exactly W at every level); the gain is w_j<1 geometric
  decay (V_k <= w_max^{k-1} V_1), plus kappa/G_n band constants.
