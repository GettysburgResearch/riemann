# Attempt at full causal completion: source-specific stability and inverse cost

Status: proposed component theorems, with proofs for independent review.
**This is NOT a complete proposed proof of RH.** The target-dependent
approximation estimate in Section 8 is not proved. Do not label it a theorem
or ask a referee to supply it implicitly.

Source freeze: PR #812, `cc5277c34fdbc48787cf650b4627a44a77862f1d`.
This note does not modify or supersede the parent's fixed-horizon certificate.
The new work is analytic; bounded checks below test finite constants and
algebra, not the infinite analytic assertions. No external priority is claimed.

## 0. The literal source and the completion being attempted

On H=L2(0,infinity), with causal convolution, let

    d(t)=exp(-t/2)[floor(exp(t))(1-t)+log(floor(exp(t))!)],
    D(z)=(z-1/2)zeta(z+1/2)/(z+1/2)^2,
    r(z)=(z-1/2)/(z+1/2),   phi_j=R^j d.

D(1/2)=1 is the REMOVABLE ANALYTIC value. This is not a product of arbitrary
assigned values at a pole. The source gives ||d||_1<=6 and ||d||_2^2<=5.
R is the causal isometry with multiplier r. For K>=0 put n=K+1 and

    G_K=(<phi_i,phi_j>)_(0<=i,j<=K).

The unitary Cayley image is

    A(w)=D((1+w)/(2(1-w)))/(1-w)=w zeta(1/(1-w)),
    A(0)=1, ||A||_H2^2<=5.                             (0.1)

Consequently G_K is the Gram of A,wA,...,w^K A, on the circle with normalized
measure dtheta/(2pi). No outerness of A is assumed.

The parent proved a general floor exp(-8sqrt(K+4))/n^2. Here the arithmetic
analytic continuation of this SAME A gives the sharper asymptotic floor
exp(-O(log^2 n)). A second theorem quantifies why exact inversion in L2 is
impossible even if RH holds. These statements concern different issues:
finite stability and the cost of approximating an unattained range point.
Neither establishes density of the source range.

## 1. A completely explicit local analytic bound for zeta

Let F(s)=(s-1)zeta(s), with the analytic value at 1. For any real t,

    max_(|z|<=4) |F(2+it+z)| <= (|t|+10)^6,
    |F(2+it)| >= |1+it|/2.                            (1.1)

Proof. The n=2 Euler--Maclaurin identity is

 zeta(s)=1/(s-1)+1/2+s/12-s(s+1)(s+2)/720
       -[s(s+1)(s+2)(s+3)(s+4)/120]
          integral_1^infinity B5({x})x^(-s-5)dx,       (1.2)

valid for Re s>-4. Here B5(v)=v^5-(5/2)v^4+(5/3)v^3-v/6. Its absolute
value on [0,1] is at most 16/3<6, by summing the absolute coefficients.
Equation (1.2) follows from repeated integration by parts on integer cells;
DLMF 25.2.10 is the cited classical normalization.

On the specified disk Re s>=-2. Put U=|t|+10. Each of |s-1|,|s|,...,|s+4|
is at most U. The integral's absolute value is at most 6/(Re s+4)<=3.
Multiplying (1.2) by s-1 therefore bounds |F(s)| by

    1+U/2+U^2/12+U^4/720+U^6/40 <= U^6, U>=10.

The last inequality follows by dividing by U^6 and checking U=10; all
terms other than 1/40 then decrease. This proof includes s=1 by analytic
continuation. In the Euler half-plane the ordinary reciprocal series gives
|1/zeta(2+it)|<=sum |mu(k)|/k^2<=zeta(2)<2. This proves the second bound.
No zero-free information in Re s<=1 is used. End of proof.

In particular the normalized entire function

    f_t(z)=F(2+it+z)/F(2+it)

has f_t(0)=1 and maximum on |z|<=4 at most 2(|t|+10)^6.

## 2. Local minimum modulus without assuming any zeros absent

Suppose f is analytic in a neighborhood of |z|<=4, f(0)=1, and
max_(|z|<=4)|f(z)|<=2^L, for an integer L>=1. If 0<delta<=1 and the point
z0=-3/2 is at distance at least delta from every zero of f in |z|<3, then

    |f(z0)| >= 2^(-3L) (delta/8)^(4L).                (2.1)

Zeros are counted with multiplicity throughout.

Proof. Jensen's formula bounds the number of zeros in |z|<3 by
L log(2)/log(4/3)<4L. Choose R in [5/2,3) with no zero on |z|=R. Form the
finite disk-R Blaschke product

    B(z)=product_a [R(z-a)/(R^2-conj(a)z)] times unimodular constants

over the zeros inside R. The quotient g=f/B is zero-free in this disk, is
bounded by 2^L on its boundary, and |g(0)|>=1. Thus
u=L log(2)-log|g| is nonnegative harmonic and u(0)<=L log(2).
The Poisson kernel on the disk gives

    u(z0) <= (R+3/2)/(R-3/2) u(0) <=4 L log(2).

It follows that |g(z0)|>=2^(-3L). Each Blaschke factor at z0 has modulus
at least delta/(R+3/2)>delta/8. Multiply the factors and use their count.
This proves (2.1). Jensen and the harmonic Poisson formula are classical;
this paragraph supplies all constants needed in this application.

The same Jensen argument bounds the zero count in |z|<7/2 by 8L, since
log(8/7)>1/8 and log2<1. Boundary-zero circles can be obtained by limits
from larger radii below 4; no zero on a chosen circle is divided without
removal. End of proof.

Crucial distinction: zeros have NOT been ruled out. A small set near their
ordinates is removed only to estimate an integral over its complement.

## 3. QP26.1 -- a quasipolynomial finite-Gram floor for the actual source

For n=K+1 define integers

    ell=ceil(log2(n+1)),  L=23+6ell,  a=16+4ell,
    q_n=3+2L(4a+15)=3+2(23+6ell)(79+16ell).           (3.1)

Then, for EVERY K>=0,

    G_K >= 2^(-q_n) I,       G_K <= 5n I.             (3.2)

Equivalently ||G_K^-1||<=2^q_n=n^O(log n). In natural logarithms this is
lambda_min(G_K)>=exp(-O(log^2(n+1))). The constants in (3.1) are deliberately
conservative. For small and medium ranks the parent's general floor is
better; one should use the larger of the two valid lower bounds. No best-
known literature bound or practical large-rank complexity is claimed.

Proof. On w=e^(i theta), write

    1/(1-w)=1/2+it,   t=(1/2)cot(theta/2).

Apart from w=1, |A(w)|=|zeta(1/2+it)|, and

    |dtheta/dt|=1/(t^2+1/4) <=4.                     (3.3)

Let p have degree <=K and normalized coefficient norm ||p||_H2=1. Then
|p(w)|^2<=n on the unit circle by Cauchy--Schwarz.

First discard |t|>4n. Its normalized circle measure is
2 arctan(1/(8n))/pi <1/(4pi n); it carries less than 1/12 of |p|^2 mass.
This step controls the accumulation point w=1; it is not treated as a
regular boundary point of A.

For each integer j with |j|<=4n+4, collect ALL zeros, with multiplicities,
of F in |s-(2+ij)|<7/2. The union may count the same zero repeatedly,
which only enlarges the following bound. From Section 1, its normalized
function on the radius-4 disk is bounded by 2^L: indeed

    2(|j|+10)^6 <=2[12(n+1)]^6 <2^23(n+1)^6 <=2^L.

There are 8n+9 centers, each contributing at most 8L zeros. Thus the
number J in the union, including repetitions, satisfies

    J<=8(8n+9)L<=72(n+1)L.                            (3.4)

Put delta=2^-a. For each zero in this union remove the interval
|t-Im rho|<delta. Its circle measure is at most 4delta/pi, by (3.3).
The total removed |p|^2 mass is therefore at most

 n*(4/pi)*J*delta
 <96 n(n+1)L 2^-a
 <=96*2^(2ell)*2^(ell+4)*2^(-16-4ell)
 =1536*2^(-16-ell) <=3/256 <1/64.                     (3.5)

We used pi>3 and L=23+6ell<=2^(ell+4), valid for ell>=1: check ell=1
and induct, since increasing ell adds 6 on the left and doubles the right.

For every remaining t, |t|<=4n. All zeros of the local f_t within |z|<3
are in the collected union: choose the nearest integer j to t, so shifting
the center moves by at most 1/2. Thus |rho-(2+ij)|<7/2 and |j|<=4n+4.
The evaluation point s=1/2+it is at distance >=delta from those zeros,
because its imaginary coordinate is. The bound 2^L for f_t holds as well.
Section 2 therefore gives

 |zeta(1/2+it)|
  =|f_t(-3/2)| |(1+it)zeta(2+it)|/|-1/2+it|
  >=(1/2) 2^[-L(4a+15)].                             (3.6)

The ratio |1+it|/|-1/2+it| is at least one. This also handles small t;
there is no asymptotic-height threshold.

The retained set carries at least 1-1/12-1/64>1/2 of |p|^2 mass.
Integrating (3.6)^2 there yields

    ||Ap||_H2^2 >=2^[-3-2L(4a+15)]=2^-q_n.

This is exactly the quadratic form of G_K. The upper bound is its trace
n||d||^2<=5n. End of proof.

No list of zeros or root locations enters the algorithm or constant. Zeros
appear only as a set in the proof whose measure is bounded by Jensen.
Possible OFF-LINE zeros are included, not excluded by assumption.

## 4. Finite arithmetic source cutoff and coefficient consequences

Let d^S(t)=d(t)1_[0,S](t). The source bound 0<g(t)<=1+t gives

    ||d-d^S|| <=e_S=(S+3)exp(-S/2).                   (4.1)

For G_K^S, the Gram of R^j d^S with ALL future filter tails retained,

    ||G_K-G_K^S|| <=n(2sqrt5 e_S+e_S^2).              (4.2)

This follows by subtracting each pair of inner products, using that every
R^j is an isometry, and bounding the matrix norm by n times its largest
entry modulus. If e_S<=2^-q_n/(12n) and e_S<=1, then

    G_K^S >= (1/2)2^-q_n I.                          (4.3)

A completely explicit choice is

    H=q_n+ell+10,     S=4H.                          (4.4)

Indeed e^-S/2<=2^-2H and S+3=4H+3<=2^H for H>=5. Hence e_S<=2^-H,
which is less than 2^-q_n/(12n), since n<=2^ell and 12<2^10.
Thus S=O(log^2(n+1)); the largest factorial argument required by this
source truncation is exp(O(log^2(n+1))), rather than the parent's
exp(O(sqrt n)) prescription. These are conservative growth classes, not
an executed large-rank computation or a bit-operation bound.

If c is a finite least-squares correction to a tail q0, then

    ||c||_2 <=2^(q_n/2)||q0||,
    sum |c_j|<=sqrt(n)2^(q_n/2)||q0||.                (4.5)

The projection has norm at most ||q0|| and its squared norm is c*G_Kc.
Combining (4.5) with the parent's ordinary-box-input realization provides
finite tolerances with the same quasipolynomial coefficient allowance.
That realization is not rerun here. Its source and tail hypotheses must
remain attached when this inequality is used.

These results make every finite solve well-posed and quantitatively
approximable. They give NO lower bound on how much of q0 is captured.

## 5. QP26.2 -- critical zeros force quantitative input blow-up

The full proof attempt next tried to control a single stable inverse input.
This strategy has a direct quantitative obstruction on the ACTUAL source.

Here is the general statement. Let d be a bounded causal L2 convolution
operator with analytic Laplace transform D. Suppose D extends analytically
through z0=i gamma and has a zero of finite order m>=1 there. Let a target
h in H have transform H extending continuously there, with h0=|H(z0)|>0.
Choose r0>0 and C>0 such that for 0<=r<=r0,

    |H(r+i gamma)|>=h0/2,
    |D(r+i gamma)|<=C r^m.                           (5.1)

For any v in H, write epsilon=||h-d*v||. Whenever
0<epsilon<=h0 sqrt(r0/8), one has

    ||v|| >= [h0^(2m)/(8^m C)] epsilon^[-(2m-1)].     (5.2)

If epsilon=0 there is NO such v in H.

Proof. Laplace evaluation at z=r+i gamma has norm 1/sqrt(2r) by the
Cauchy--Schwarz inequality. Thus

    |H(z)-D(z)V(z)|<=epsilon/sqrt(2r),
    |V(z)|<=||v||/sqrt(2r).

Set r=8epsilon^2/h0^2. The first error is at most h0/4, so (5.1) gives
|D(z)V(z)|>=h0/4. Therefore

 ||v|| >=sqrt(2r)*h0/(4C r^m)
        =h0^(2m)/(8^m C) * epsilon^(1-2m).

For exact equality epsilon=0, let r tend to zero in
h0/2<=C||v|| r^m/sqrt(2r), impossible for m>=1. End of proof.

Apply this with the literal d in Section 0 and h(t)=t exp(-t/2), whose
transform is H(z)=1/(z+1/2)^2. Classical existence of a critical-line zeta
zero rho=1/2+i gamma supplies the boundary zero of D, of whatever its actual
multiplicity m is. No simplicity, height, or value of zeta'(rho) is assumed.
Here h0=|rho|^-2>0. Thus for some source-dependent c>0,

    ||v|| >= c epsilon^[-(2m-1)]                     (5.3)

for every sufficiently accurate approximate inverse. In particular a lower
bound of order 1/epsilon holds without knowing m. Its constants are not
numerically certified here.

This does NOT refute closure of the range. Under RH the target belongs to
the closure of the source range, but not to its actual L2-input range. The
approximating inputs must become unbounded. Compact inputs are allowed in
(5.3); causality or compactness does not evade the evaluation inequality.
For a fixed compact-input seed and a future-only input correction, apply
(5.3) to the sum of both inputs. The future input's norm must be at least
this lower bound minus the seed input norm. No fictitious L2 impulse is used.

### The input exponent is sharp in the general statement

For each m>=1, the rational stable source and target

    D_m(z)=z^m/(z+1)^(m+1), H_m(z)=1/(z+1)^(m+1)

have a boundary zero of order m at 0 and H_m(0)=1. Take the genuine input
V_eta(z)=1/(z+eta)^m, eta>0. Its squared norm is exactly

    ||v_eta||^2=(2m-2)!/[(m-1)!^2(2eta)^(2m-1)].

The error transform is H_m(z)[1-(z/(z+eta))^m]. After setting t=eta u in
boundary Plancherel, dominated convergence gives

    ||h_m-d_m*v_eta||^2 / eta ->
    c_m=(1/(2pi))integral_R |1-(iu/(1+iu))^m|^2 du in (0,infinity).

For domination use |H_m(i eta u)|<=1, |iu/(1+iu)|<=1, and
|1-w^m|<=m|1-w|, which bounds the integrand by m^2/(1+u^2).
Thus ||v_eta|| is comparable to error^[-(2m-1)]. This proves that the
exponent in (5.2) cannot be improved for this general class. These rational
models are not zeta; they test sharpness of the analytic inequality, not RH.

## 6. Test of the proposed closing inference

A tempting proposal is now: because source cutoff and finite inverses cost
only quasipolynomial factors, choose a polynomial rank in the horizon and
obtain subexponential corrected error. The last step does not follow.

For any source A=B O in disk H2 and any degree K, the finite Grams of the
orbits of A and O are IDENTICAL. Multiplication by inner B is an isometry.
Their closed source subspaces are, however, B H2 and H2. The Gram contains
boundary-modulus information, whereas target alignment additionally involves
B and the cross vector. A conditioning theorem cannot erase an inner factor.
This does not claim that their constant coefficients are equal.

An explicit finite-dimensional check is A(w)=1-2w. It has A(0)=1 and squared
norm 5, just as allowed in the parent's hypotheses. Its n by n Gram has
main diagonal 5, adjacent diagonals -2, and every finite Gram is at least I.
For target 1 the exact least-squares error is

    U_n=3*4^n/(4^(n+1)-1) >3/4,   U_n ->3/4.         (6.1)

Proof. Its determinant satisfies Delta_n=5Delta_(n-1)-4Delta_(n-2), with
Delta_0=1, Delta_1=5, so Delta_n=(4^(n+1)-1)/3. The target cross vector is
(1,0,...,0), hence U_n=1-Delta_(n-1)/Delta_n. On the circle |1-2w|>=1,
proving the uniform Gram floor. This is a synthetic control, NOT zeta.

For this polynomial source, even better conditioning than (3.2) coexists
with a positive limiting defect. The source-specific proof of (3.2) uses
zeta analyticity to improve stability; it does not prove source outerness.
The constructed bad sets explicitly allow zeros. Thus using (3.2) as a
zero-exclusion theorem would reverse its logical content.

## 7. End-to-end implication, with the unproved premise exposed

Let M be the actual closed causal source space, h(t)=t exp(-t/2), and T>0.
A legitimate compact-input seed f0 can be constructed with f0=h before T
by finite Mobius inversion. Its shifted error is q0(u)=(f0-h)(T+u).
Let P_K project onto span(d,Rd,...,R^K d), and P_M onto M. Optimizing a
future-only correction gives

    U_K(T)=||(I-P_K)q0||^2
           =||(I-P_M)q0||^2+||(I-P_K)P_M q0||^2.      (7.1)

The first term is the intrinsic domain obstruction; the second is removable
finite-synthesis error. A derivation is immediate by orthogonal projection
since range(P_K) is a subspace of M. The earlier optimal-tail note identifies
the first term with the joint zero-interpolation minimum, including
multiplicities; no part of that identification is needed for the next bound.

If rho=1/2+delta+i gamma is ANY zero with delta>0, each compact-input output
f matching h before T has Laplace transform zero at lambda=rho-1/2.
The delayed error satisfies

    integral_T^infinity e^(-lambda t)(f-h)(t)dt=-1/rho^2.

Cauchy--Schwarz on that tail gives the unconditional conditional-on-a-zero
inequality

    ||f-h||^2 >=2delta exp(2delta T)/|rho|^4.          (7.2)

Finite sums of future closed-domain corrections satisfy the same zero
condition, as does their H limit by continuous evaluation in Re z>0.
Therefore an unbounded sequence of source-admissible corrected outputs with

    T_j -> infinity,  log(1+||f_j-h||^2)/T_j ->0       (7.3)

would exclude every right-of-line zero; reflection would prove RH.
The same conclusion holds with a zero lower limit along an unbounded
sequence. Constants or ranks may be selected before any hypothetical zero
is considered.

## 8. What remains missing -- not a task left for the referee

No estimate proving (7.3) is established in this manuscript. In particular,
(3.2) and (4.5) control the norm and sensitivity of a coefficient solution,
not the target-dependent residual in (7.1). They also do not show that its
first term is zero. The earlier fixed-horizon numerical improvement remains
at its original T=log2 and is not extrapolated here.

The direct stable-inverse route is ruled out by Section 5 if it demands
bounded L2 inputs as error tends to zero. Unbounded-input approximation can
still succeed; (5.2) is not an obstruction to subexponential OUTPUT error on
growing horizons. It is a constraint on admissible proposed closing proofs.

A complete proof would have to construct specific corrections and establish
(7.3), or independently exclude the intrinsic source obstruction. Neither
has been supplied. The referee can assess the COMPLETE proofs of the local
minimum-modulus lemma, quasipolynomial finite-Gram bound, source-cutoff bound,
and quantitative input cost. These must not be advertised as a complete RH
proof, and the open premise must not be promoted by successful finite tests.
