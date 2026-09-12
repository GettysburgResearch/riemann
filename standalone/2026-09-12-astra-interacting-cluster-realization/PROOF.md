# ICR26 — a genuinely interacting theta realization through degree fourteen

Date: 2026-09-12. Status: PROPOSED COMPONENT PROOFS, pending independent
mathematical and implementation review. **The all-order realization and RH
are NOT proved.** No new zero-free region or external priority is claimed.

This is an add-only successor to PR854, exact source
`f737983edb993ffc1142c37320eb3c9b304ab06a`. That source already supplies a
270-spin degree-twelve realization, an independent-spin obstruction, and a
local Gaussian replacement argument. Those are credited, not republished as
new results. Here a fixed non-negligible interaction realizes degree fourteen.
CLUSTER_LIMIT.md gives a separate all-order restriction on bounded lattice
components. Neither result supplies an arbitrary-order induction.

## 1. The unchanged full theta source

For t >= 0 let

    phi(t) = sum_(n>=1) [4 pi^2 n^4 exp(9t/2)
                        -6 pi n^2 exp(5t/2)] exp(-pi n^2 exp(2t)).   (1)

Use its even extension. The classical Jacobi identity makes this extension
smooth and identifies

    Xi(z) = xi(1/2+iz) = integral_R phi(t) exp(izt) dt.

The series and its fixed derivatives converge locally normally. Every summand
is positive on t >= 0 because pi n^2 exp(2t) > 3/2. Define

    Z = integral_R phi(t)dt = Xi(0),
    w(t) = phi(t)/Z,
    mu_(2r) = integral_R t^(2r) w(t)dt,
    v = mu_2 > 0.

All exponential moments exist. These are the ACTUAL theta moments; no finite
theta truncation, supplied moment table, or zero list defines the target.
The classical representation and weighted Lee--Yang input are referenced in
SOURCES.json. Their general theory is imported, not certified by the code.

Let kappa_(2r) denote cumulants of t/sqrt(v), and let c_(2r) be cumulants of
one symmetric unit sign. Set s_r = kappa_(2r)/c_(2r). Cumulants are taken from
the logarithm at the origin only. Through order sixteen the sign cumulants are

    1, -2, 16, -272, 7936, -353792, 22368256, -1903757312.

They are all nonzero. The checker reconstructs them from exact moments using

    kappa_n = m_n - sum_(j=1)^(n-1) binom(n-1,j-1) kappa_j m_(n-j). (2)

## 2. A finite interaction which is not an infinitesimal perturbation

Take a pair of signs sigma,tau with Gibbs probability proportional to
exp(J sigma tau), where

    J = (1/2) log(3/2) > 0,       q = exp(-2J) = 2/3.               (3)

For W=(sigma+tau)/2, its probabilities at -1,0,1 are respectively
3/10, 2/5, 3/10. In particular

    E W^(2r)=3/5 (r>=1), E W^(2r+1)=0,
    E sigma tau = 1/5.

Write d_(2r) for its cumulants and a_r=d_(2r)/c_(2r). These are exact rational
numbers obtained from (2). The dimer's characteristic function is

    chi_W(t) = [2/3+cos(t)]/(5/3).

For cos(theta)=-2/3, the triple-angle formula gives

    chi_W(theta)=0,                  chi_W(3theta)=8/9.             (4)

Thus this actual positive interaction escapes the independent-sign zero-
tripling mechanism. Formula (4) alone is not an assertion about the complete
model's zeros or a source approximation theorem.

## 3. Seven equations define a 272-spin model

Let nu=(256,10,1,1,1,1). Take 270 independent signs in these six groups,
independent also of the dimer (3). For positive x_0,...,x_5,y define

    X = sqrt(v)[sum_(i=0)^5 sqrt(x_i) sum_(l=1)^nu_i epsilon_(i,l)
                                      + sqrt(y) W].               (5)

There are 272 physical spins. Each dimer spin has observable weight
sqrt(v y)/2. Its single edge has coupling (3); all other edges have zero
coupling. This is a valid, disconnected zero-field ferromagnet with nonnegative
observable weights, not a freely chosen mixture of Lee--Yang laws.

The seven equations are

    F_r(x,y) = sum_(i=0)^5 nu_i x_i^r + a_r y^r - s_r = 0,
                          1 <= r <= 7.                           (6)

**Theorem ICR1.** There is a unique solution of (6) in the closed box of radius
10^-14 about the following EXACT rational centers (the same strings are in
parameters.json):

```
x0  0.0007245200147405687920449900136668893220948893935101377569526328007
x1  0.02138904741115748995700305656835575761296468174774786040127667402
x2  0.04024967722717895668919811124086873711500621794322577651905476226
x3  0.07927386407176476958006213948159821034845572628343339386451453155
x4  0.1211702179747692772100782609906329832631412083279717456684506535
x5  0.2672564559754763122830390874602982353275986555976687054922021828
y   0.1544703114427502898401239860738676522664328160527108477718952212
```

At these exactly defined parameters,

    E X^(2r)=mu_(2r),  1<=r<=7;     E X^(2r+1)=0 for all r>=0.      (7)

The model is NOT Xi. Its first unmatched standardized moment obeys

    0.20 < [E X^16-mu_16]/v^8 < 0.21.                             (8)

The sole interacting component carries between 0.09268 and 0.09269 of the
total variance. Indeed its standardized variance is exactly (3/5)y, and
(6) at r=1 fixes total standardized variance one. No enumeration of 2^272
states is used or claimed.

### 3.1 Whole-box existence rather than a rounded fit

Let c be the rational center and J0=F'(c), an entirely rational 7-by-7 matrix.
Its entries are

    (J0)_(r,i)=r nu_i c_i^(r-1),
    (J0)_(r,6)=r a_r c_y^(r-1).

Compute R=J0^(-1) by exact rational elimination. All 49 identities R J0=I
are checked independently by multiplication. With row-sum infinity norms,
the outward computation of the FULL theta integrals in Section 4 proves

    ||R||_infinity < 75,000,000,
    beta := ||R F(c)||_infinity < 6*10^-22,
    L := sup_box ||I-R F'(x)||_infinity < 1.01*10^-7.              (9)

The complete retained dyadic upper endpoints are in result.json; acceptance
also directly tests beta+L*10^-14 < 10^-14 and L<1. Thus the map
x -> x-RF(x) takes this closed box strictly into itself and is a contraction.
Banach's theorem gives exactly one root IN THIS BOX, not global uniqueness.
The numerical use of interval enclosures of s_r is valid because the actual
s_r lie in them; no rounded moments define a different equation.

Cumulants add for independent components, giving (6). The triangular relation
(2) then proves (7). Since all lower cumulants agree, the sixteenth raw-moment
difference is the sixteenth cumulant difference, namely

    c_16[sum_i nu_i x_i^8 + a_8 y^8 - s_8].                       (10)

Interval evaluation on the entire root box gives (8), more specifically an
enclosure inside (0.2020747403,0.2020747702). The actual root, not the displayed
center, defines X. All intervals in (9)--(10) are strict.

For orientation only, the physical weights are approximately

```
256 copies: 0.005786195633153807
 10 copies: 0.031438632068846881
  1 copy:   0.043126987263934992
  1 copy:   0.060524740125188217
  1 copy:   0.074828297482982468
  1 copy:   0.111130181097347749
  2 dimer spins, each: 0.042243552658490797.
```

These rounded numbers are not the exact model or the certificate input.

## 4. Complete primitive interval contract

The accepting program uses integers and fractions only, with 320-bit dyadic
outward endpoints. Its interval and Taylor recursion is adapted from IMR26
(PR847), so this is NOT an independent transcendental backend. The raw moments
are recomputed, not copied from that packet or from PR854.

### 4.1 Scalar primitives

Machin's identity pi=16 atan(1/5)-4 atan(1/239) is enclosed with 96 alternating
terms and the first omitted term. For exp(r), range reduction makes |r|<=1/8;
96 Taylor terms and a geometric bound for the remaining ratios enclose the
positive exponential. Negative exponents use interval reciprocals; repeated
squaring reverses range reduction. Rational conversion, multiplication,
reciprocals and integer square roots all round outward.

### 4.2 The 84 finite cells

For n=1,2,3,4 use cutoffs U=2,3/2,1,3/4 respectively, divided into cells of
width 1/16: 32+24+16+12=84 cells. At each rational center c, use the scaled
variable (t-c)/(1/32). The analytic theta summand is expanded through degree
120 by exponential-series recurrences. Its product with t^j, j=0,2,...,16,
is integrated exactly termwise; all even monomial cell moments are retained.
The full-line factor two is included.

On the complex circle |t-c|=1/8, Re(exp(2t))>0. The factor
exp(-pi n^2 exp(2t)) therefore has modulus at most one. Bounding the remaining
prefactor by pi<4 and e<3 shows it is less than 10^11 on every such circle.
For example n<=4 and Re t<=17/8 give the elementary upper bound
4*(4*16)^2*3^10+6*(4*16)*3^6 < 10^11.
The radius ratio is (1/32)/(1/8)=1/4. The degree-120 remainder is at most
10^11*4^-121/(1-1/4) per point. The summed full-line integration length is
less than 16 and 0<=t<=2, so the moment error is bounded by

    e_j=16*10^11*2^j*4^-121/(1-1/4).                              (11)

Multiplying the truncated density polynomial by the EXACT degree-j power
polynomial does not truncate their product; the remainder is bounded separately
by (11). This avoids a hidden omission of moment-weighted Taylor terms.

### 4.3 All four time tails and every omitted theta index

For q=pi n^2 and t>=0,

    0<phi_n(t)<=4q^2 exp(9t/2-q exp(2t)).

At a cutoff U put E=exp(2U), lambda=2qE-9/2>0. The inequality
exp(2r)>=1+2r gives the full-line moment-tail bound

  2 integral_U^infinity t^j phi_n(t)dt
    <=8q^2 exp(9U/2-qE)
        sum_(k=0)^j binom(j,k) U^(j-k) k!/lambda^(k+1).            (12)

The checker evaluates (12) for each n=1,...,4. For n>=5 the bound at U=0
is 8pi^2 n^4 exp(-pi n^2) j!/(2pi n^2-9/2)^(j+1). Consecutive terms have
ratio at most (6/5)^4 exp(-11pi)<1/2, uniformly in j>=0. Thus their ENTIRE sum
is bounded by

    16pi^2*625 exp(-25pi) j!/(50pi-9/2)^(j+1).                   (13)

These positive tails are added to the upper endpoint; (11) inflates both
endpoints. The lower endpoint of Z is positive, so division and standardized
moments/cumulants are legitimate. The actual variance is enclosed near
0.04620998623083794. (12)--(13), not a fitted convergence trend, cover the
infinite domain and omitted arithmetic source.

## 5. Why this is an interacting extension, and what it does not prove

The predecessor #854 matches degree twelve and has an explicitly positive
fourteenth-moment discrepancy. Its optional interactions can be as small as
10^-100. In contrast, (3) is fixed at approximately 0.2027 with exact pair
correlation 1/5. The new seventh moment equation is solved with that interaction
present; it is not inferred from continuity from an independent fit.

The exploratory numerical path from another dimer parameter to q=2/3 was NOT
interval-certified. Only the final root box is claimed. No claim is made that
this root connects to the old six-variable root without collisions. Floating
attempts to continue the same seven-equation family toward a sixteenth-moment
match did not produce a certified solution; that is not a no-go theorem.

The Jacobian in (9) is nonsingular, so the implicit function theorem supplies
a local exact seven-moment family as J varies near (3). No global continuation
interval or all-order extension follows. The positive sixteenth discrepancy
in (8) is retained rather than omitted after reaching the desired degree.

## 6. Full sufficient ending and the remaining constructive problem

Weighted Lee--Yang states that for ANY finite zero-field Ising ferromagnet,
J_ij>=0 and a_i>=0, the Fourier transform of X=sum a_i sigma_i has only real
zeros. For its even entire moment generating function, paired factorization
and exponential type give

    E exp(hX)=product_k (1+h^2/gamma_k^2),
    sum_k gamma_k^-2=Var(X)/2.

Consequently

    E X^(2r)/(2r)! <= (Var(X)/2)^r/r!,
    |E exp(izX)| <= exp(Var(X)|z|^2/2).                           (14)

The general theorem is classical; it is not proved by finite moment matching.
The product coefficients imply (14) by bounding an elementary symmetric sum
by the corresponding power divided by r!. Repeated zeros are counted with
multiplicity. No simplicity assumption is used.

Suppose for EVERY m there were finite such models X_m with

    |E X_m^(2r)-mu_(2r)|<=2^-m, 1<=r<=m.                        (15)

Their variances are bounded. On each complex disk, the finite Taylor parts
converge to those of Xi/Xi(0). Estimate (14) pays the entire model Taylor tail,
and the target's entire moment-generating series pays its own tail. Thus the
characteristic functions converge locally uniformly to Xi/Xi(0). Hurwitz
excludes nonreal zeros of the nonzero limit, giving RH.

**No construction for (15) at arbitrary m is supplied.** The present model
solves one seven-equation problem. CLUSTER_LIMIT.md shows why repeating fixed
small lattice components is not an all-order induction. A successful next step
must construct larger correlated components, or genuinely different internal
weight patterns, while preserving lower moments and controlling feasibility.
Neither the number of parameters nor local nonsingularity proves reachability.
