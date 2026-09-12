# BHT26 — permanent zero-cluster transfer on windows of unbounded height

Date: 2026-09-12.
Status: PROPOSED component proofs, requiring independent mathematical review.
**Critical-line confinement at unbounded heights and RH are NOT proved.**
Scope: the unchanged Gamma(5/2, RATE 5/2) shared-uniform branching orbit.
Source: PR #870 at ee7f76736c235714496526f999e028d181302b56; its finite
height-30 certificate is not rerun or enlarged by a new zero census here.
This is a new add-only packet, not an amendment of #859/#860 or #870.

## 1. Exact outcome and its limitation

Retain independent children and one independent shared U uniform on [1,2]:

    X_0 ~ Gamma(5/2, RATE 5/2),
    X_(m+1) = (X_m+X_m')/U^2,
    V_m=(pi/6)(X_m+X_m'),
    M_m(s)=E V_m^(s/2),
    H_m(s)=[M_m(s)+M_m(1-s)]/[2(1+M_m(1))].             (1)

Positive-variable complex powers use their real logarithm. Let Z be the set
of nontrivial zeros of xi, with multiplicities retained when counting, and
put r=31/80. No assumed zero list defines the orbit or the bounds below.

For an INTEGER N>=N0=2^18, define the entirely rational radius prescription

    B_N=N+12,
    ell_N=ceil(log_2 B_N),
    k_N=floor(N/(500 ell_N)),
    eps_N=2^(-k_N).                                      (2)

The two indices have different roles: N is the protected HEIGHT and onset
DEPTH, while m>=N is any subsequent branching depth.

**BHT1 (unbounded-height permanent tracking).** For every integer N>=2^18,
every integer m>=N, and every s with -1/2<=Re s<=3/2 and |Im s|<=N+2,

    dist(s,Z)>=eps_N  ==>  |H_m(s)-xi(s)|<|xi(s)|.         (3)

In particular every H_m zero in that rectangle lies within eps_N of an
ACTUAL xi zero. This locates it relative to Z, NOT relative to Re s=1/2.
Here eps_N=exp[-Theta(N/log N)] and tends to zero; N is unbounded.

**BHT2 (complete multiplicity-preserving clusters).** For each such N there
is a radius a_N in (eps_N,2eps_N) such that the components of

    U_N=union_(rho in Z, |Im rho|<=N+1) {s:|s-rho|<a_N}

that meet |Im s|<=N have diameter at most

    96 log(B_N) eps_N < 1/4.                             (4)

Every such component contains exactly the same number of zeros of xi and
of EVERY H_m, m>=N, counted with multiplicity. Its boundary has no zero of
either function. All H_m zeros in 0<=Re s<=1, |Im s|<=N lie in these components.
The same conclusion holds for any finite real convex combination of these
H_m and xi. All these statements also apply to the parent's entire E_m,
whose gamma multiplier is nonzero on this rectangle.

The components are described using the ACTUAL zero set only in a mathematical
localization theorem. We do NOT claim that their centers have been computed,
that they are rational certificate inputs, or that their centers are central.
An implementation must independently isolate the reference clusters.

There also exists a rational h_N in (N-1/2,N) for which the complete outer
rectangle [-1/4,5/4] + i[-h_N,h_N] has zero-free boundary and the same total
zero count for xi and all H_m, m>=N. This count is not evaluated here. The
slightly enlarged real-part interval is intentional: no uniform distance
from xi zeros to the lines Re s=0,1 is assumed.

**What is not obtained.** The theorem does not prove Z is central. A
hypothetical off-central xi zero is tracked with the same multiplicity and
accuracy as a central one. Under RH, (3) gives the explicit shrinking-strip
bound |Re s-1/2|<eps_N for H_m zeros up to height N. We do not use that
conditional statement as an unconditional conclusion. Multiple central
zeros can split into nearby noncentral zeros; exact line membership is
inferred only for a symmetry-invariant component of count ONE.

General Jensen/Harnack minimum-modulus and Rouche methods are classical.
No priority is claimed for quantitative analytic zero stability. The new
proposed contribution is this explicit source/depth/height composition and
its correct quantified boundary, not a new RH equivalence advertised as easier.

## 2. A complete source bound on a wider strip

We first establish, without RH, for m>=1,

    |H_m(s)-xi(s)| <= 2(T+5)^3 r^m
    if -1/2<=Re s<=3/2 and |Im s|<=T, T>=0.              (5)

The extra half-unit margins are used to surround clusters near the edges of
the original critical strip. No continuation of an estimate beyond its
proved domain is made.

### 2.1 Source order and its exact smooth error

Here are the parent ingredients and their proof, rather than an import of a
finite numerical receipt. Let W=U^-2 and A~Beta(5/2,5/2). Their moments of
orders 0,1,2 are respectively 1,1/2,7/24. On [1/4,1] the ratio of their
densities is (3pi/256)x^-3(1-x)^(-3/2). It decreases to x=2/3, then increases;
it is above one at 1/4, below one at 2/3, and diverges at 1. Below 1/4 only
the beta density is present. Thus W minus A has three crossings and sign
pattern -,+,-,+. For f with f''' >=0, quadratic interpolation at those
crossings makes the remainder have precisely that pattern. Its quadratic
part integrates to zero by the three matching moments. Hence A <=_3 W.
Multiplication by an independent Gamma(5,RATE5/2), followed by beta-gamma
factorization, gives nu_0 <=_3 nu_1.

Replacing the two children separately shows this order is preserved by T:
the third derivative of f((x+y)/u^2) is u^-6 f'''((x+y)/u^2). Therefore
nu_m <=_3 nu_(m+1). Equal-mean coupling gives W2 contraction sqrt(7/12).
The fixed law is X_*=(6/pi^2)sum E_j/j^2; its Laplace transform
sqrt(6t)/sinh(sqrt(6t)) verifies the fixed-point equation by integration of
csch^2. This is the classical BPY law, not a new fixed-point identity.

The exact recurrence is

    E X_m^2=7/5,
    E X_m^3=93/35-(24/175)r^m.                            (6)

Fourth moments are uniformly at most 8: in their recursion a_4=127/896<1/7,
E X_m^3<3, (E X_m^2)^2<2, and
 a_4(2*8+8*3+6*2)<8.
The initial gamma fourth moment is below 8. Uniform fourth moments permit
the limiting order nu_m <=_3 nu_* for cubic-growth tests.

The Peano kernel

    K_m(t)=[E(X_*-t)_+^2-E(X_m-t)_+^2]/2

is nonnegative (approximate the truncated-square test by smooth tests) and
has integral (4/175)r^m. Taylor's integral formula, with matching first two
moments, consequently gives for REAL OR COMPLEX f

    |E f(X_m)-E f(X_*)| <= (4/175)r^m sup_(x>=0)|f'''(x)|. (7)

The complex case follows by the same positive-kernel integral; no missing
factor from separate real and imaginary estimates is used.

### 2.2 Inverse moments and complete Mellin normalization

Applying the order to -exp(-tx) shows that the Laplace transforms decrease
with depth. Integrating their positive inverse-moment representation gives

    E X_m^-4, E X_*^-4 <= E X_1^-4
       =[(2^9-1)/9]*(5/2)^4/24
       =319375/3456 <100,                               (8)

and similarly E X_m^-1,E X_*^-1<=35/24. Holder gives a bound of 100 for every
inverse exponent in [0,4]. For p=s/2 with -1/4<=Re p<=3/4, let

    g(x)=E[((pi/6)(x+Y))^p],

where Y is an independent child from nu_m or nu_*. Since 3-Re p lies in
[9/4,13/4] and (pi/6)^(Re p)<2,

    sup |g'''| <=200 |p(p-1)(p-2)|.

Replace each child using (7). This proves

    |M_m(s)-2xi(s)| <= (8/7)|s(s-2)(s-4)| r^m.           (9)

The identity M_*(s)=2xi(s) is classical BPY. To check its normalization
without any zero input, V_*=(pi/6)(X_*+X_*') has Laplace transform
pi t/sinh(sqrt(pi t))^2. For a>0, Tonelli and
csch(x)^2=4sum_(j>=1)j exp(-2jx) give

 E V_*^-a=2^(1-2a)pi^-a Gamma(2a+2)zeta(2a+1)/Gamma(a)
          =2xi(2a+1)=2xi(-2a).

Gamma duplication and xi reflection give the last equalities. All positive
and negative moments exist, so analytic continuation proves the identity
everywhere. This uses classical reflection, not RH.

Moreover E V_*=pi/3<4/3 and E V_*^-1<3, by X_*+X_*'>=X_* and (8)'s
first-inverse-moment analogue. Holder therefore gives |xi(s)|<1 on the
wider strip in (5). Retaining the changing denominator in (1), (9) yields

 |H_m(s)-xi(s)| <= (4/7)r^m[|s(s-2)(s-4)|
                          +|(1-s)(1+s)(3+s)|+6].        (10)

Each factor has modulus at most T+5. Since T+5>=5, (10) implies (5).
Inverse moments also justify holomorphy on a neighbourhood of the closed
strip. No boundary-only expectation is used in a contour argument.

## 3. An explicit minimum-modulus estimate that does NOT assume RH

For s=sigma+it, -1/2<=sigma<=3/2, 0<delta<=1, define B=|t|+10. We prove

 dist(s,Z)>=delta  ==>
 |xi(s)| >= (1/256) exp(-pi|t|/4) B^-60
                              (delta/6)^(24 log B).     (11)

The zero exclusion in the hypothesis is a distance from ALL actual zeros,
not only zeros already verified on the line.

### 3.1 Euler-safe normalization and a local zero count

Set F(s)=(s-1)zeta(s), analytically continued at 1, and s0=2+it.
For |z|<=4 the real part of s0+z is at least -2. Repeated integration by
parts in Euler summation gives

 zeta(s)=1/(s-1)+1/2+s/12-(s)_3/720
          -(s)_4/24 integral_1^infinity Btilde_4(x)x^(-s-4)dx, Re s>-3.

Here (s)_j is a rising factorial and |Btilde_4|<=1/30. Multiplication by s-1
removes its pole. Every |s+j| needed is <=B, and the absolute remainder
integral is <=1/30 on this disk. Hence

 max_(|z|<=4)|F(s0+z)|
 <=1+B/2+B^2/12+B^4/720+B^5/720 <= B^5.                 (12)

At s0 the absolutely convergent reciprocal Euler series gives
|zeta(s0)|>=1/zeta(2)>1/2, so |F(s0)|>=1/2.
Normalize f(z)=F(s0+z)/F(s0). Then f(0)=1 and max_|z|<=4 |f|<=B^6.

Jensen's formula bounds the number K of zeros in |z|<=3, counting every
multiplicity, by

    K log(4/3)<=6 log B,  hence K<=24 log B,              (13)

because log(4/3)>1/4. Boundary zeros in Jensen can be handled by radial limits;
the logarithmic singularities on a circle are integrable.

### 3.2 Finite Blaschke removal, including all off-line zeros

Divide f by the disk-radius-four Blaschke factors for ALL zeros |a|<=3,
with their multiplicities. In modulus such a factor is

    |b_a(z)|=4|z-a|/|16-conjugate(a)z|.

The quotient g is analytic on |z|<=4, bounded by B^6 there, zero-free in
|z|<3, and |g(0)|>=1. Thus h=6logB-log|g| is nonnegative harmonic in that
disk with h(0)<=6logB. The Poisson/Harnack inequality at |z|<=5/2 gives

    h(z)<=11h(0), hence |g(z)|>=B^-60.

At z=s-s0=sigma-2 we have |z|<=5/2. If its distance from each zero is at
least delta, |16-conjugate(a)z|<=24 gives |b_a(z)|>=delta/6. Therefore

    |F(s)| >= (1/2)B^-60(delta/6)^(24 logB).              (14)

The only extra zeros of F are its trivial zeros at negative even integers;
these are at distance >=3/2 from our strip. Thus the hypothesis involving Z
alone suffices when delta<=1. No zero has been omitted from the factorization.

### 3.3 Gamma normalization, with an actual lower bound

Use the exact identity

    xi(s)=pi^(-s/2) Gamma(1+s/2) F(s).                  (15)

This is regular at s=0. For z=a+ib, a>0, Binet's integral gives

 logGamma(z)=(z-1/2)logz-z+(log(2pi))/2+R(z),
 |R(z)|<=1/(12a).

Indeed 0<1/(exp u-1)-1/u+1/2<u/12, and the remainder is its Laplace
integral divided by u. The elementary coth inequalities prove the bracket
bound; no large-|z| asymptotic without a remainder is used.

For z=1+s/2 we have 3/4<=a<=7/4. Since log|z|>=log(3/4)>-1/3,
(a-1/2)log|z|>=-5/12; also -b argz>=-pi|t|/4.
Dropping the positive log(2pi)/2 leaves a constant greater than -3. Thus

    |Gamma(1+s/2)|> exp(-3)exp(-pi|t|/4)
                    > (1/27)exp(-pi|t|/4).

Also |pi^(-s/2)|>1/4 on the stated strip. Combining with (14) gives the
stronger constant 1/216, and hence (11). These are deliberately loose constants.

## 4. Join the height and depth estimates

Let N>=2^18 and eps_N be (2). Put L=log(N+12). Uniformly on |t|<=N+2,
(5) bounds the error at every m>=N by

    E_N=2(N+12)^3 r^N.                                 (16)

Outside the eps_N-neighbourhood of Z, (11) bounds |xi| below by

    M_N=(1/256)exp[-pi(N+2)/4](N+12)^-60
                                  (eps_N/6)^(24L).     (17)

We check E_N<M_N explicitly. The elementary inequalities

 log(80/31)>log(5/2)>312/343>9/10,
 pi/4<11/14, log6<2, log2<1

and L<=ell_N log2 imply

    24L log(1/eps_N) <= (24/500)N.

Consequently

    log(E_N/M_N) <11+111L-(3/50)N <0.                   (18)

For the final inequality, at N0=2^18 use L<19. The function
(3/50)N-111log(N+12)-11 is increasing thereafter, since its derivative is
3/50-111/(N+12)>0. This proves (18) at every allowed N, not only tested values.
Notice that none of these estimates uses an unknown minimum modulus as an
uninstantiated constant. Its complete dependence on distance to the ACTUAL
zero set is in (11). Equations (16)--(18) prove BHT1.

For later use, k_N>=ell_N+8 for every N>=2^18. On an ell-block its smallest
possible N is at least 2^(ell-1)-12, and

    2^(ell-1)-12 >=500ell(ell+8), ell>=19.                (19)

The case ell=19 is exact integer arithmetic. Doubling the left-side main
power proves induction because 2ell(ell+8)-(ell+1)(ell+9)=ell^2+6ell-9>0.
Thus

    96L eps_N <=96ell_N/2^(ell_N+8)<1/4.                 (20)

No astronomically small floating-point number is needed to implement (2).

## 5. Full clusters, not an assumed simple-zero matching

Let Z_N contain all distinct xi zeros with |Im rho|<=N+1, and choose a common
radius a_N in (eps_N,2eps_N), avoiding the finitely many radii causing circle
tangencies or higher boundary coincidences. The components of U_N then have
piecewise smooth boundaries; holes, when present, are included with negative
orientation. All zero counts below include multiplicity, even though disks
are drawn only once around repeated centers.

Consider a component meeting |Im s|<=N. It has a center rho0 with
|Im rho0|<=N+2eps_N. A simple chain of overlapping disks has center steps
less than 4eps_N. If a chain first reached distance 1/2 from rho0, all centers
before that exit would have imaginary parts within 1/2+4eps_N of Im rho0.
Their real parts are in (0,1). They consequently lie in the radius-three disk
centered at 2+i Im rho0. By (13) there are at most 24L such centers. But the
chain length is at most 96L eps_N<1/4, a contradiction.

Thus every center of the component is within 1/2 of rho0, and (13) bounds
its total number (even with multiplicity) by 24L. Any two centers can be
joined by a simple chain, proving the diameter bound 4eps_N(24L) in (4).
The component lies inside -1/2<Re s<3/2, |Im s|<N+1/4.
Its boundary has distance >=a_N>eps_N from Z_N. Any zero not in Z_N has
|Im rho|>N+1, so its distance from that component is >3/4.
Hence BHT1 holds on the ENTIRE component boundary.

Rouche's theorem gives the same complete zero count for all m>=N and xi.
The same error bound holds for every finite convex combination. Conversely,
BHT1 forces any H_m zero in the original window into a disk of U_N, and
therefore into one of the counted components. This proves BHT2.

For the outer rectangle assertion, zeros with ordinates in [N-1,N+1] number
at most 24L by the same disk estimate. Their disks exclude total horizontal
cutoff length at most 96L eps_N<1/4 from the half-unit interval (N-1/2,N).
Choose a rational height outside those projected closed intervals. Conjugation
handles its negative. The vertical sides at -1/4 and 5/4 are distance at least
1/4 from Z. BHT1 and the argument principle prove the stated complete count.
We do not evaluate that count, nor silently replace the enlarged sides by 0,1.

## 6. A quantified unbounded-height attack, and the missing implication

The source-to-zero transfer is now uniform on genuinely growing windows.
If a complete independent reference census proves xi's zeros central and
simple up to a particular height R, the parent fixed-window method protects
sufficiently small individual disks for every sufficiently late depth. That
last statement needs that FINITE reference input. This packet does not extend
the existing reference census from 30 to a new numerical height.

The new theorem is more general: without any simplicity assumption or zero
list it gives clusters and an explicit depth N for height N. It proves that
RH would imply, for EVERY N>=2^18 and EVERY m>=N,

 H_m(s)=0, 0<=Re s<=1, |Im s|<=N
       ==> |Re s-1/2|<eps_N.                            (21)

Conversely (21), or its assertion at any cofinal sequence of N with m>=N,
would imply RH. A hypothetical fixed off-central xi zero lies in a cluster
of diameter tending to zero; Rouche supplies approximant zeros in that
cluster, which eventually contradict (21). The zeros of that cluster are
inside the original strip for all sufficiently large N, since the fixed
hypothetical zero lies strictly inside it. Thus the equivalence does not
rely on the slightly enlarged outer rectangle.

We HAVE NOT proved the right-hand side of (21) unconditionally. The
minimum-modulus argument removes disks about all zeros; there is no reason
within it that their centers must be central. This is the exact failed
step of the attempted completion. A sharper bound on its constants does
not change that issue.

### 6.1 The two previously protected regimes cannot simply be joined

The high-height theorem in #860 supplies the deliberately conservative
threshold T_m>=320*16^m. The present small-error argument treats heights
of order m, not that exponential threshold. In fact its absolute-error
ALLOWANCE imposes a sharp asymptotic speed limitation on this particular
comparison procedure.

Let lambda=log(80/31). On the fixed strip -1/2<=sigma<=3/2, Euler summation with the periodic
B_2 remainder gives F(s)=O((1+|t|)^3). Gamma Stirling bounds then give
|xi(sigma+it)|<=C(1+|t|)^6 exp(-pi|t|/4).
If height is v m with v>4lambda/pi, the error allowance
2(vm+5)^3 exp(-lambda m) divided by this upper envelope tends to infinity.
Thus even an exact numerical model of xi would not make a disc of this
ALLOWANCE around its top-edge value avoid zero. This does not prove the
actual branching error is that large. It proves that this fixed allowance
cannot certify the missing overlap. The transition speed is

    4log(80/31)/pi = 1.20708129248448... .                (22)

For every fixed v below this speed, the same proof with adjusted constants
yields a radius exp[-c_v m/log(m+12)] on windows of height v m. This is a
tracking theorem, not a zero-confinement theorem. The explicit choice v=1
was used in BHT1 to avoid unevaluated thresholds.

### 6.2 An exact control against the false bootstrap

This example is NOT a branching law, not the theta source, and not xi.
It only tests the claimed logical inference from convergence plus the two
protected regimes. Put q_m=1/16+r^m/100 and

 G_m(z)=[(z-40)^2+q_m][(z+40)^2+q_m] cos(pi z/10).

Each G_m is real even entire, positive on the imaginary axis, and has exactly
three simple real zeros in 0<=Re z<=30, |Im z|<=1/2, at 5,15,25. All its
critical-band zeros above real frequency 41 are real and simple. Nevertheless,
its four explicit nonreal zeros +/-40 +/- i sqrt(q_m) persist inside the band
and tend to +/-40 +/- i/4.

The limit G has the same properties. On the entire band, G_m-G is O((1+|z|^2)r^m):
expanding the polynomial difference gives precisely
 (r^m/100)[2z^2+3200+1/8]+r^(2m)/10000.
Thus even global geometric convergence, an all-future lower window, eventual
high real zeros, symmetry and imaginary-axis positivity do not join the gap.
Only a further property of the literal source can distinguish it. We do not
claim the modified functions satisfy the exact stochastic recursion or the
xi functional normalization.

## 7. Attribution, evidence and review obligations

Classical analytic inputs: Euler summation/Euler--Maclaurin and periodic
Bernoulli polynomials (DLMF25.2); Binet's convergent integral (5.9.10_2);
Jensen's formula, finite Blaschke products, Poisson/Harnack, and Rouche;
xi reflection and its classical zero strip (DLMF25.4/25.10); the BPY Brownian
source (math/9912170). All normalization-sensitive specializations are derived
above. No source-specific zero-free estimate to the right of 1/2 is imported.

The bounded checker authenticates this packet and reconstructs the rational
constants, dyadic radius prescriptions, model polynomial identities, and
bounds used in the all-N inductions. It does NOT evaluate xi, enumerate zero
clusters, execute a new contour census, or formally verify an infinite theorem.
It is not the parent's quadrature checker. Normal/optimized execution and
rejection tests are implementation evidence, not independent analytic review.

Review first: extended-strip inverse-moment use in (9)--(10); pole removal and
Bernoulli remainder in (12); complete local zero removal in (14); the uniform
N/m comparison in (18); and the cluster-size/boundary argument in Section5.
The principal failure of the desired full proof is stated in Section6, not
left as an accepted lemma or delegated to a reviewer.
