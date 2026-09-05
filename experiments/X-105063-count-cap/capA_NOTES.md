# LANE CAP-A PLAN (single overhanging pair)
1. Read repo lemma L-105061 files to confirm available facts (phi' shape, B convexity).
2. Step A: (phi')'' sign structure: negative outside two bands (sqrt2-1)y<|t-x|<(sqrt2+1)y, positive inside; so (m1*phi'-B)'' <0 outside bands => sign pattern -,+,-,+,- => <=4 sign changes.
3. Step B: g'':=(m1 phi'-B)'' has <=4 sign changes => g' has <=5 distinct zeros... use: f has <= (#sign changes of f'')+2 distinct zeros? No: use Rolle chain: Z_dist(g) <= Z_dist(g') + 1 <= (Z_dist(g'')+1)+1 <= (4+1)+2? Careful with unbounded ends. Do it via sign changes of g'' <=4 => g' piecewise monotone on 5 intervals => g' has <=5 zeros... need distinct-zero counting on open interval with g''!=0 a.e. Formalize.
4. Step C: multiplicity: Z_mult(h',G) <= Z_dist(g) + Z_mult(g') with g=h'; iterate to g'' level; cap mult at any point by 4 using band structure? Alternative: mu-fold zero of g means g,...,g^{(mu-1)} vanish; since g'' has <=4 sign changes and is nonzero except at band boundaries? g'' can vanish. Use: Z_mult(g) <= Z_dist(g'') + 2*(1+...)? Clean route: Z_mult(f) <= Z_mult(f') + Z_dist(f)?? Actually Z_mult(f) <= Z_dist(f) + Z_mult(f') restricted; iterate twice and bound Z_mult(g'') by sign-change count 4 + ... need Z_mult(g'')<=? g''' analysis. Fallback: argument principle disk bound.
5. Decide cleanest mult route; write proof.
6. Combine: Z_mult(h,G) <= 1 + Z_mult(h',G) => extra <= Z_mult(h',G) => C_A.
7. Numeric duty: build B from finite real-zero configs + tail bound; count zeros of m1*phi'-B via fine bisection; scan grids g, x, y, asymmetry, mults.
8. Record max extra observed (expect 2); confirm <= C_A.
9. Write LEMMA_A.md deposit-grade.
10. Final message < 1200 words.

## STEP 1 (verified symbolically, y=1, s=t-x, f:=phi')
f(s)=2(1-s^2)/(1+s^2)^2.
f''  = -12(s^4-6s^2+1)/(1+s^2)^4 : roots |s|=sqrt2 -+ 1; f''<0 on |s|<sqrt2-1 and |s|>sqrt2+1.
f''''= -240(s^2-1)(s^2-4s+1)(s^2+4s+1)/(1+s^2)^6 : roots |s| in {2-sqrt3, 1, 2+sqrt3};
  sign: + on |s|<2-sqrt3; - on (2-sqrt3,1); + on (1,2+sqrt3); - on |s|>2+sqrt3.
f' = 4s(s^2-3)/(1+s^2)^3 (f decreasing on 0<s<sqrt3). f>0 iff |s|<1. Homogeneous in y by scaling s->s/y, f->f/y^2 etc.

## STEP 2 (localization -- the key)
Set Q := B - Sum_{other j} m_j phi'_j, so h' = g := m1*f - Q on G.
Fattening radius R4 := 2+sqrt3 (> sqrt2+1). Hypothesis (H1): every OTHER pair j has
Itilde_j := (x_j - R4 y_j, x_j + R4 y_j) disjoint from G.  Then on G, |t-x_j| >= R4 y_j so:
phi'_j <= 0 (since R4>1), (phi'_j)'' <= 0 (R4>sqrt2+1), (phi'_j)'''' <= 0 (R4 >= 2+sqrt3).
Hence on G: Q>0 (Q>=B>0), Q''>0 (>=B''>0), Q''''>0 (>=B''''>0), using
d^4/dt^4 (t-c)^{-2} = 120(t-c)^{-6} > 0 and termwise differentiation (abs.-loc.-unif. conv., Weierstrass).
LOCALIZATION: any zero t* of g in G has m1 f(t*) = Q(t*) > 0, hence t* in int I, I=(x-y,x+y).
So Z_mult(h',G) = Z_mult(g, J), J := I cap G (an interval; possibly empty => 0).

## STEP 3 (zero count of g'' on J)
Partition J by the points x -+ (2-sqrt3)y into <=3 pieces: J_L, C, J_R.
- On C (|s|<(2-sqrt3)y < (sqrt2-1)y): f''<0, so g'' = m1 f'' - Q'' < 0: no zeros; and g''<0 at
  the partition points themselves (|s|=(2-sqrt3)y < (sqrt2-1)y).
- On J_L, J_R ((2-sqrt3)y<|s|<y): f''''<0, so g'''' = m1 f'''' - Q'''' < 0: g'' strictly concave
  => Z_mult(g'', piece) <= 2 (strict concavity: a double zero is a touching max, mult>=3 impossible).
Total: Z_mult(g'', J) <= 4.

## STEP 4 (Rolle with multiplicity, analytic functions)
Lemma R: psi analytic, not ==0, finitely many zeros on interval J: Z_mult(psi,J) <= Z_mult(psi',J)+1.
(distinct zeros u_1<...<u_r, mults mu_i: psi' has mult mu_i - 1 at u_i plus >=1 zero in each gap:
 Z_mult(psi') >= Sum(mu_i - 1) + (r-1) = Z_mult(psi) - 1.)
Finiteness of zeros of g on J: g analytic on G, g -> -infinity at G endpoints (double poles of -B),
so zero-free near dG; interior accumulation would force g==0, impossible. Apply twice:
Z_mult(g,J) <= Z_mult(g',J)+1 <= Z_mult(g'',J)+2 <= 6.

## STEP 5 (conclusion)
h = F'/F analytic on G, +inf -> -inf, finitely many zeros; Lemma R: Z_mult(h,G) <= Z_mult(h',G)+1.
extra(G) = Z_mult(h,G)-1 <= Z_mult(h',G) <= 6 =: C_A. (If main pair does not overhang or J empty:
g = m1 f - Q < 0 on G... f<=0 on G then, so g<0, Z_mult(h',G)=0, extra<=0.)
m1 >= 1 arbitrary (m1 copies): all sign arguments unchanged. C_A = 6, absolute.

## NUMERIC RESULTS
scan3.py: 18144 grid configs (g in {.1,.5,1,2}; 7 backgrounds incl. mults/asymmetry/far zeros;
far R4-distant pairs; y in {.01...5}; 12 x-positions incl. non-overhang; m1 in {1,2,5}):
max extra = 2, max Z(h',G) = 2, zero configs with extra>2 or Z(h')>6.
Best (extra=2) mpmath-verified (dps30): g=.1, reals={0,.1}, x=.01, y=.01, m1=5 -> extra 2, zhp 2.
scan4.py: 2496 adversarial (endpoint-hugging x, y down to .001, m1 to 50, stacked endpoint mults)
+ 3000 random configs: max extra = 2, max Z(h') = 2, zero flags.
Float64 flutter incident reproduced (13 fake zeros in symmetric config) and killed by
cancellation-aware filter (|v| > 1e-11 * sum|terms|) + mpmath verification -- replay discipline.
CONFIRMED: proved C_A = 6 never approached; empirical max extra = 2 (conjectured sharp).
