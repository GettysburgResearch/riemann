# MCB31: coherent microscopic covariance and the critical quadratic threshold

**Status:** proposed component proofs; independent mathematical review required.
**No native subquadratic recurrence, new zero-free region, or RH proof.**
Date: 20 September 2026. Reading parent: PR #904 at
`d0d7ad05f9d4504e9d752518b34a9fd0609a06f7`.

The new result bounds a complete, smoothly selected microscopic frequency
band at ALL available denominators. The band includes, at weight one, every
reduced fraction with distance from an integer at most H/X, on the physical
block [X,2X). It includes dense mixed-prime interactions, not just sparse
partner graphs, prime powers, or a covariance diagonal.

The bound is quadratic in a LOCALIZED input energy, without a power of X.
After assembling native blocks it is linear in total previous energy times
the largest recent input energy. A separate result shows that exponent two
is sharp for the bounded-source class. Thus this pass reaches the critical
exponent on a previously unpaid band; it does not establish the strictly
subquadratic native gain required for RH. An intermediate frequency band
still carries an uncontrolled cutoff loss in the complete two-parameter bound.

## 1. Exact source and the band being estimated

Let c be a finite real source supported on 1,...,L, satisfying

    sum_(n<=L) c(n)/n = 0.

Write

    x_r=sum_(n<=r)c(n)/n,  x_0=x_L=0,
    J(c)=sum_(r=1)^(L-1) x_r^2,
    z(d)=(c*c)(d),  B_q=sum_(q|d) z(d)/d.

Convolution is ordinary Dirichlet convolution. The identity
J(c)=integral_1^infinity (sum_(n<=t)c(n))^2 dt/t^2 follows by expanding
1/max(r,s)=min(r,s)/(rs). This is the existing innovation norm, not a new
normalization or the physical prefix energy E_Y.

For alpha in (0,1), let e(alpha)=exp(2*pi*i*alpha), and define

    Z_alpha(k)=sum_(n=1)^k e(n alpha)/n + log(1-e(alpha)).   (1.1)

The logarithm is the radial Abel limit from the unit disk. Dirichlet
summation gives Z_alpha(k)=-sum_(n>k)e(n alpha)/n: the ENTIRE centered tail,
not a truncation. Conjugate frequencies are paired below.

Fix integers H>=1, X>=8H, and L^2<=8X. Define the C^2 cutoff

    chi_H(t)=1,                                   0<=t<=H,
             1-10u^3+15u^4-6u^5, u=(t-H)/H,      H<t<2H,
             0,                                   t>=2H. (1.2)

It lies in [0,1]. Its first two derivatives match at both transition ends.
The microscopic function is

    U_(X,H)(k)=sum_(q=2)^(L^2) B_q
                sum_(1<=a<q,(a,q)=1)
                    chi_H(X ||a/q||) Z_(a/q)(k),         (1.3)

where ||alpha|| is distance to the nearest integer. This is real. All
fractions with ||a/q||<=H/X have weight ONE. The transition to zero on
H/X<||a/q||<2H/X is part of the definition and is NOT omitted error.
No assertion for a sharp indicator cutoff is obtained by differentiating it.

Masks and source are fixed before the tail transform. Specifically, with

    (TP)(k)=P(k)/(k+1)-sum_(j>k)P(j)/[j(j+1)],

finite Fourier inversion and summation by parts give
T[e(alpha k)/(1-e(-alpha))]=Z_alpha(k). Thus (1.3) includes all centering
constants. A selected band does not generally have zero logarithmic constant.

The Newton source v=2c-1*c*c has reciprocal output

    m_v(k)=2m_c(k)-sum_(q>=2)B_q sum_((a,q)=1)Z_(a/q)(k). (1.4)

The full constants cancel since sum_d z(d)log(d)/d=0. Partial constants do
not cancel separately. These are the inherited finite Newton/Fourier/tail
identities, rederived in the earlier packets and credited here.

## 2. Main microscopic covariance theorem

Define

    a=max(0, floor(X/(2HL))-1),
    E_local(c;X,H)=sum_(r=a+1)^(L-1) x_r^2.              (2.1)

Then for any integer M with X<=M<2X,

    sum_(k=X)^M |U_(X,H)(k)|^2
       <= 2^21 H^4 E_local(c;X,H)^2.                    (2.2)

There is NO coefficient-cap hypothesis in (2.2). Only finite support,
reciprocal balance, X>=8H, and L^2<=8X are needed. This is a bound on the
whole signed sum in (1.3), including every cross-frequency covariance.
Its norm is over the stated finite block. Its VALUES retain the complete
infinite harmonic tails. It is not an assertion of the same bound for
energy on the entire future of this fixed microscopic mask.

### 2.1 Exact real derivative of a centered mode

For X<=k<2X put

    z_(X,k)(t)=2 Re Z_(t/X)(k)
       =2 sum_(n<=k) cos(2*pi*n*t/X)/n
          +2 log(2 sin(pi*t/X)).                        (2.3)

We only need 0<t<=2H<=X/4. A finite sine-sum identity gives exactly

    z'(t)=(2*pi/X) cos((2k+1)*pi*t/X)/sin(pi*t/X).        (2.4)

Indeed 2sin(theta) sum_(n=1)^k sin(2n theta)
=cos(theta)-cos((2k+1)theta). The logarithmic constant is load-bearing in
(2.4); differentiating only the finite cosine sum would give a different answer.

Abel summation bounds the complete complex tail by
2/[(k+1)|1-e(t/X)|]. Hence, using sin(pi*t/X)>=2t/X,

    |z(t)|<=1/t,
    |t z'(t)|<=4,
    |t^2 z''(t)|<=64t+8.                                (2.5)

For the second derivative, differentiate (2.4). Before replacing pi<4,
its bound is pi^2(2k+1)t/X+pi^2/2. Since 2k+1<4X this proves (2.5).
No large-sieve inequality or native-coefficient heuristic enters these bounds.

The cutoff obeys |chi'_H|<=2/H and |chi''_H|<=6/H^2.
The first follows from 30u^2(1-u)^2<=15/8. For the second, set
v=|1-2u|: 60u(1-u)|1-2u|=15v(1-v^2)<=10/sqrt(3)<6.
For g(t)=chi_H(t)z_(X,k)(t), (2.5) therefore gives

    |t g'(t)|<=6,
    |t^2 g''(t)|<=180H,
    |t g'(t)+t^2 g''(t)|<=256H.                         (2.6)

Here g and its first two derivatives vanish at and above 2H. For example,
the second bound is at most
64t+8+16t/H+6t/H^2<=128H+52<=180H.

### 2.2 Unreduce the frequencies BEFORE taking absolute values

For real d>0 define

    f_(X,k)(d)=sum_(j>=1) chi_H(jX/d) z_(X,k)(jX/d).      (2.7)

Only j<2Hd/X contribute; set f(0)=0. On 0<d<=L^2, the nonzero terms
have jX/d<=2H and at least 1/8. Because the cutoff is C^2 and flat at its
upper endpoint, the finite sum is C^2 even as terms enter or leave.
It vanishes for d<=X/(2H).

Reducing each fraction j/(rs) gives the exact finite identity

    U_(X,H)(k)=sum_(r,s<=L) [c(r)/r][c(s)/s] f_(X,k)(rs). (2.8)

The pairing in (2.3) counts j/(rs) and 1-j/(rs) together. X>=8H makes every
active j/(rs) strictly less than 1/2, so no self-conjugate term is doubled.
All product coincidences and mixed-prime divisibility conditions remain.
There is no assumption that B_q is multiplicative or negative.

Differentiation of (2.7), followed by (2.6), gives

    |f'(d)+d f''(d)|
      <= (1/d) sum_(j<2Hd/X) |t g'(t)+t^2 g''(t)|
      <= 512 H^2/X.                                    (2.9)

This estimate is uniform in d, k and the number of available denominators.

### 2.3 Two source summations by parts

Since c(r)/r=x_r-x_(r-1), two FINITE summations by parts turn (2.8) into

    U_(X,H)(k)=sum_(r,s=1)^(L-1) x_r x_s D_k(r,s),
    D_k(r,s)=f(rs)-f((r+1)s)-f(r(s+1))+f((r+1)(s+1)).    (2.10)

The mixed derivative of f(rs) is f'(rs)+rs f''(rs). Integrating it over
the unit rectangle [r,r+1]x[s,s+1] and using (2.9) proves
|D_k(r,s)|<=512 H^2/X.
If r<=a, every product in that rectangle is at most
(r+1)L<=X/(2H), so D_k(r,s)=0. The same holds for s<=a.
Therefore

    |U_(X,H)(k)|
       <= (512 H^2/X) (sum_(r>a)|x_r|)^2
       <= (512 H^2 L/X) E_local.                        (2.11)

There are at most X observation indices. Squaring, summing and applying
L^2<=8X proves (2.2). The signed c(r)c(s) were recombined by exact summation
by parts before the energy inequality. Dropping their signs first would
not give this input-energy estimate.

## 3. Recent native energy, not the entire past twice

Let y>=2 and retain the actual Mobius prefix through y. Complete the
reciprocal residual with the existing cap-three greedy rule: at each later
index n add the opposite-sign coefficient min(3,n*|residual|), until zero.
It has L<=y+ceil(y/2)<=2y. This uses |m(y)|<=1, which follows from
sum_(n<=y)mu(n)floor(y/n)=1. No future Mobius signs are used for completion.

Its reciprocal tail also has the LOCAL price

    sum_(r=y+1)^(L-1) m_c(r)^2
       <= F_y-F_floor(y/2),
    F_y=sum_(r<=y)m(r)^2.                               (3.1)

To verify the stronger localization of the known completion estimate, after
j tail entries its residual is
(|m(y)|-3 sum_(i=1)^j 1/(y+i))_+.
For j<=ceil(y/2), 3/(y+i)>=1/(y-i+1), so this is at most |m(y-j)|.
Only j=1,...,L-y-1 occur in the nonzero tail. Their y-j indices are all
above floor(y/2), proving (3.1) with no new unknown future quantity.

On an assigned block X<=k<=M<2X use y=floor(sqrt(M)). Then
M<(y+1)^2, L<=2y<=X (for X>=8), and L^2<8X. The exact Newton identity

    mu-(2c-1*c*c)=mu*(delta-1*c)*(delta-1*c)

makes every coefficient through M native, since delta-1*c vanishes below
y+1. Thus m_c(k)=0 and m(k) is minus the full spectral sum on this block.
The strict square endpoint is not included accidentally.

Set

    a0=max(0,floor(y/(8H))-1),
    Delta_(y,H)=F_y-F_a0.                               (3.2)

Since X>y^2/2 and L<=2y, the index a in (2.1) is at least a0.
The prefix part of E_local is at most Delta, and (3.1) pays the tail by
another Delta. Consequently the whole microscopic native block has

    sum_(k=X)^M |U_(X,H)(k)|^2 <=2^23 H^4 Delta_(y,H)^2. (3.3)

### Complete square-step assembly and a bounded-overlap gain

Take Y>=7, Y+1>=8H, b=Y+1, B=b^2-1. Partition [b,B] into

    X_j=b*2^j,  M_j=min(2X_j-1,B),  y_j=floor(sqrt(M_j)).

Each block uses its own completed native source through y_j<=Y, and its own
mask chi_H(X_j ||alpha||), fixed before the full tail transform. Restriction
to that assigned block occurs LAST. This is not T applied to a stitched
physical source; that different operation would need activation corrections.

Let U be the resulting piecewise microscopic component and set

    Delta_j=F_(y_j)-F_max(0,floor(y_j/(8H))-1),
    Delta_max=max_j Delta_j,
    N_H=12+2 ceil(log_2 H).

Then

    ||U||_[b,B]^2 <=2^23 H^4 sum_j Delta_j^2
                   <=2^23 H^4 N_H F_Y Delta_max.         (3.4)

This is LINEAR in the total previous energy times its largest recent input
energy, with no power of Y and no extra log Y overlap penalty.

For completeness, an input index r contributes to Delta_j only if
r<=y_j<8H(r+1)<=16Hr. For a nonfinal full block this confines X_j to
[r^2/2,129H^2 r^2]. There are at most 10+2ceil(log_2 H) powers-of-two
steps in that range. A possible shortened final block adds at most one.
Thus each m(r)^2 is counted at most N_H times, proving
sum_j Delta_j<=N_H F_Y and then (3.4).

Since Delta_max<=F_Y, a fixed H gives O_H(F_Y^2). The local form is stronger
when input energy is spread across scales. We have NOT proved a universal
native upper bound Delta_max<=F_Y^(1-delta); no subquadratic recurrence is
inferred from (3.4).

## 4. Mixed-prime restriction and covariance with the already controlled part

The microscopic theorem includes every denominator, not just composites.
A subtraction of prime powers must itself be paid because partial-band
prime-power logarithms need not cancel.

Here is a useful extension of NCL29's prime-power bound. For ANY fixed
conjugation-symmetric weights 0<=w_(a/q)<=1 restricted to prime powers,
let P_pp be their physical Fourier sum and W_pp=T P_pp. If |c(n)|<=K,
reciprocal balance and L^2<=8X give

    sum_(k>=X)|W_pp(k)|^2 <=2^12 K^4 H_L^10.             (4.1)

Indeed sum_(1<=a<q)|1-e(-a/q)|^-1<=q H_q/2. For primes,
B_p=-U_p^2 and |U_p|<=K H_L/p, giving physical absolute size
at most K^2 H_L^4/2. For a>=2,
|B_(p^a)|<=K^2 H_L^2(2a+1)/p^a by the exact threshold identity.
There are at most L possible primes at each exponent, and if
A=floor(log_2(L^2)), then A+1<=4H_L. Their total physical size is at most
16K^2 L H_L^5. Together it is at most 17K^2 L H_L^5.
The entire physical tail has total weight 1/X. The exact contractive tail
map then gives (4.1), since 289 L^2/X<2^12.

This argument takes absolute values only inside a sector whose complete
cost is proved affordable. It does not drop logarithmic constants.

If U_mix is (1.3) restricted to denominators with at least two distinct
prime factors, (2.2) and (4.1) imply

    ||U_mix||_[X,M]^2
       <=2^22 H^4 E_local^2+2^13 K^4 H_L^10.             (4.2)

Thus the new control applies to the DENSE microscopic mixed-prime band.
It is not restricted to prime squares or to bounded-degree partner graphs.

For an exact three-part native partition, choose the NCL29 far-angle
threshold eta=1/[2 ceil(log_2 b)]. Put weights chi_H(X_j||alpha||) in U;
put the complementary weights 1-chi in G if the denominator is a prime
power or ||alpha||>=eta; put the remaining weights in R. Then

    m=-U-G-R on every new native integer,
    ||G||^2 <= C(1+log Y)^11.                            (4.3)

The weighted NCL29 far-sector proof is unchanged: squared coefficient
mass only decreases for weights in [0,1]. Use (4.1) for the masked prime
powers. This decomposition does not double-count the smooth transition.
For fixed H, Cauchy--Schwarz and (3.4) give in particular

    |2<U,G>| <= C_H(1+log Y)^(11/2) sqrt(F_Y Delta_max).  (4.4)

This is at most C_H(1+log Y)^(11/2)F_Y: a LINEAR previous-energy budget
for the complete microscopic/controlled-sector covariance. The R energy
and its mixed terms are not eliminated by (4.4).

## 5. A complete two-parameter bound, and exactly why it is not closure

For a single native block whose source ends by X, the complement of chi_H
is supported on ||alpha||>H/X. NCL29's all-denominator weighted far bound,
with eta=H/X, gives

    sum_(k=X)^M |m(k)|^2
      <=2^22 [H^4 E_local^2 + K^4 (X/H) H_L^9].          (5.1)

This is an upper bound for the COMPLETE native block, including every
frequency and every covariance. It leaves no discarded component. But its
second term has a cutoff power. Increasing H reduces that term and increases
the first. Taking H comparable to X, or calling the two components orthogonal,
would invalidate the advertised gain. Balancing H^4 and X/H, where the
optimizing H is admissible, still leaves a positive power X^(4/5).

Thus (5.1) is a real whole-covariance estimate, not a scale-to-scale RH gain.
The separate, cutoff-power-free result is the microscopic bound (3.4).
Neither should be confused with the older NCG28 4/3 estimate for a different
window and a different fixed-source decomposition.

## 6. Exponent two is sharp in the capped nonnative class

There exists a family of reciprocally balanced sources c_R with a FIXED
coefficient cap, L_R<2R, and J(c_R) asymptotic to a positive constant times R,
such that, for X=R^2 and H=1,

    sum_(k=X)^(2X-1)|U_(X,1)(k)|^2 >= c J(c_R)^2.        (6.1)

Consequently no replacement of the quadratic exponent by p<2, even with
fixed logarithmic losses in L, holds for all such bounded sources.
These are explicitly NONNATIVE sources. They do not refute a native gain.

Here is a proof without a finite extrapolation. For t in compact subsets
of (0,infinity), k=floor(uX), u in a compact subset of (1,2), (2.3) converges
in C^2 in t to

    z_inf(t,u)=2(log u+gamma+log(2*pi*t))
                 +2 integral_0^u [cos(2*pi*t*v)-1]dv/v.

The integrand is continuous at zero. The zero-order convergence follows
from harmonic-number asymptotics and Riemann sums; the derivative convergence
follows directly and uniformly from (2.4) and its derivative.
In particular

    t z_inf'(t,u)+t^2 z_inf''(t,u)
       =-4*pi*u*t*sin(2*pi*u*t).                        (6.2)

Put v=d/X. By (2.7)-(2.9), X[f'(d)+d f''(d)] has a continuous limit
K(u,v) near (u,v)=(5/4,1). At that point j=1 has chi=1 and zero cutoff
derivatives, j=2 is at the flat upper cutoff, and all later terms vanish.
Equation (6.2) gives

    K(5/4,1)=-5*pi<0.

Therefore choose fixed small delta,epsilon,c0>0 such that K<=-c0 on
|u-5/4|<=epsilon, 1<=v<=(1+delta)^2. The same strict sign, with half the
margin, holds for all sufficiently large X. No effective first X is claimed.

Choose a fixed nonnegative nonzero C^2 bump phi supported strictly inside
(1,1+delta), scaled so that 2||phi'||_infinity<=1. Set

    x_n=phi(n/R),    c_R(n)=n[x_n-x_(n-1)].              (6.3)

Then reciprocal balance is exact by telescoping, the support is below 2R,
and |c_R(n)|<=1 for all sufficiently large R. Also
J(c_R)=sum x_n^2 ~ R integral phi^2.
On the displayed u interval, the double-difference representation has
nonnegative x_r x_s and every relevant mixed derivative <=-c0/(2X).
It follows that

    U_(X,1)(k) <= -(c0/(2X))(sum_r x_r)^2,

whose magnitude is bounded below by a positive constant. There are a
positive constant times X such observation indices. This proves (6.1).

One can also impose c_R(1)=1 and agreement with mu through 5: add the fixed
source alpha with coefficients +1 at 1,10,15,30, -1 at 2,3,5,6, and zero
elsewhere. Its reciprocal sum is zero. Innovation supports are disjoint,
so it adds a fixed energy. All its products with (6.3) are O(R)<X/2 and
therefore have EXACTLY zero microscopic weight for large R. The microscopic
output is unchanged. The source fails native divisor inversion at n=6.
The large-index coefficients in (6.3) are real, not asserted to be ternary.

The significance is specific: the calculus and energy-only estimate cannot
by themselves beat two. Further improvement must exploit actual arithmetic
constraints not satisfied by this family, or a different source-faithful
mechanism. This does not assign a probability to future success.

## 7. Finite evidence and retained limitations

The checker reconstructs full native square-step panels through Y=15 and 31,
using the scale-local sources above. A further focused Y=31, H=2 panel shows
what changes when the microscopic band is widened. Every assigned observation
cell is evaluated. It directly sums the microscopic spectral function with
144-bit outward elementary arithmetic and complete log constants.

Its complement is evaluated by exact subtraction from the independently
checked native Newton output, not by an exhaustive second spectral sum.
The source is independently compared with a full finite Mobius sieve; all
B_q are checked by a second gcd-threshold formula. Exact reduced-frequency
and uncoalesced-product dictionaries agree. The summation-by-parts identity
is checked coefficientwise as a formal linear combination of f(d).

The entire micro/complement covariance and a native semiprime/other-micro
covariance are retained. Small native micro/complement covariances are
positive; a universal negative-sign shortcut fails. A partial prime-power
mask has a nonzero logarithmic centering constant even though the whole
prime-power sector's constants cancel.

The analytic estimates, the continuum sharpness family, and unbounded native
behavior are not proved by these finite checks. See VALIDATION.md for exact
executed commands, counts, and publication identity. Source attribution and
reading boundaries are in SOURCES.md.
