# BHH26 — eventual critical-line confinement at every finite branching depth

Date: 2026-09-10. **Proposed component theorem with a paper proof; independent
mathematical review required. RH is NOT proved.**

This is a direct continuation of #857 at
`3f1984867d23b588d09c88a892882411724b174b`. No predecessor is edited. The new
statement is `for every fixed depth n, there exists a finite height T_n`.
There is NO uniform-in-depth threshold, no certification of the remaining
bounded-height zeros, and no interchange of the two limits.

The new mechanism is analytic continuation in the **Laplace variable**, not a
small-moment or positivity-of-mixtures inference. All leading singularities
collapse into one degree-n polynomial. Its coefficient recursion confines its
zeros to a fixed disk. A contour estimate pays the complete analytic remainder,
so the polynomial controls actual Mellin transforms at sufficiently high height.
The result supplies a true infinite-height region for every member of the
prescribed orbit, but does not settle the growing region below that threshold.

## 1. Actual orbit and the precise theorem

Set k=5/2, c=pi/6, and use Gamma(shape, RATE). Let

    X_0 ~ Gamma(k,k),
    X_(n+1) = (X_n+X_n')/U^2 in distribution,
    U ~ Uniform[1,2].                                    (1)

The children are independent and one independent U scales their sum. Write

    L_n(z)=E exp(-z X_n),
    M_n(s)=E[c(X_n+X_n')]^(s/2),
    H_n(s)=[M_n(s)+M_n(1-s)]/[2(1+M_n(1))].               (2)

Positive powers use the real logarithm. In particular these definitions are
unchanged from #850/#853/#857. Define

    alpha_n=(3/2)2^n+1,    beta_n=2alpha_n=3*2^n+2,
    rho_j=k4^j,   0<=j<=n.                               (3)

Here beta_n is the leading singularity order of L_n^2. It is NOT the pair
shape A_n=5*2^n in #857's gamma–Dirichlet representation.

**BHH1 (eventual confinement).** For every integer n>=0 there exists a finite
T_n such that every zero of H_n in

    0<=Re s<=1,    |Im s|>=T_n

is simple and lies on Re s=1/2. There are infinitely many such zeros.
The same assertion holds for the entire E_n constructed in #857, since its
gamma multiplier is nonzero on this strip.

**BHH2 (actual high-height asymptotic).** The quantities below are explicit:

    b_(0,0)=1,
    b_(n+1,j)=b_(n,j)^2-2b_(n,j-1)^2,                     (4)

with missing indices equal to zero; and

    c_0=1,   c_(n+1)=c_n^2/beta_(n+1),
    P_n(v)=sum_(j=0)^n b_(n,j)^2 v^j.                    (5)

For fixed n, uniformly on -1/2<=Re s<=3/2 as |Im s| tends to infinity,

 M_n(s)=c_n^2 Gamma(beta_n+s/2)/Gamma(beta_n)
          * (pi/15)^(s/2) P_n(2^(-s)) [1+e_n(s)],        (6)

where e_n is holomorphic in the high parts of that wider strip. The value
has the bound below on the wider strip; the combined value-and-derivative
bound is asserted on the CLOSED CRITICAL SUBSTRIP 0<=Re s<=1:

    |e_n(s)|+|e_n'(s)|
       =O_n((1+log(2+|Im s|))^(2^(n+1))/|Im s|).          (7)

A fixed-radius Cauchy disk inside the wider strip supplies that derivative
bound. At n=0, e_0=0.
All constants and starting heights in this notation can depend on n. This
is not a uniform approximation as n and |Im s| increase together.

**BHH3 (counting at fixed depth).** Let N_n(T) count all zeros of H_n with
0<Re s<1 and 0<Im s<=T, with multiplicity. Then, for each fixed n,

 N_n(T)=T/(2pi) log(pi T/(30*4^n))-T/(2pi)+O_n(1).        (8)

Only finitely many counted zeros can be off the central line. This does not
identify which, or prove that their number is zero.

The paper proves these statements below. The thresholds T_n are not numerically
instantiated and the proof does not provide a useful uniform bound for them.

## 2. A differential–dilation identity and all finite singular points

Initially for positive real z, substitution v=z/u^2 in the branching law gives

 L_(n+1)(z)=(sqrt(z)/2) integral_(z/4)^z L_n(v)^2 v^(-3/2)dv,

and consequently

    2z L_(n+1)'(z)-L_(n+1)(z)
             =L_n(z)^2-2L_n(z/4)^2.                    (9)

This identity holds by analytic continuation on the slit plane
Omega=C\(-infinity,-k]. There is no assumed source symmetry in (9).
The coefficient 2 on the delayed term comes from both the integration
endpoint and its Jacobian. The analytic value L_(n+1)(0)=1 selects the
solution; an arbitrary homogeneous sqrt(z) term is not added.

For completeness, the gamma–Dirichlet representation needed here is elementary.
Write a_n=k2^n. The change from two equal-rate gamma variables to their sum
and beta ratio yields, inductively,

 X_n=G_n Z_n in law,  G_n~Gamma(a_n,k), G_n independent of Z_n,
                   4^(-n)<=Z_n<=1.                    (10)

Indeed Z_0=1 and Z_(n+1)=[B Z_n+(1-B)Z_n']/U^2 with independent
B~Beta(a_n,a_n). Thus

    L_n(z)=E(1+z Z_n/k)^(-a_n)                           (11)

on Omega. This also gives, uniformly there for |z|>=2k4^n,

    |L_n(z)|<=C_n |z|^(-a_n),
    |L_n'(z)|<=C_n |z|^(-a_n-1).                       (12)

Here and below C_n denotes a finite depth-dependent constant, not the compact
mixing variable used in #857. Bounds (12) follow from
|1+zZ_n/k|>=|z|Z_n/(2k); the powers a_n are real.

### Local structure, including the lower logarithmic terms

For n>=1, on either side of the slit, L_n continues locally across every
negative real point except the n+1 points -rho_j. Near each such point,
with d=1+z/rho_j,

 L_n(z)=c_n b_(n,j) d^(-alpha_n)
       +O_n(|d|^(-alpha_n+1)(1+|log|d||)^(2^n-1)).       (13)

The same expansion may be differentiated: the derivative of the error is
O_n(|d|^(-alpha_n)(1+|log|d||)^(2^n-1)). Both local sides are included.
The leading coefficient is real and the same on both sides. There can be
lower logarithmic terms: (13) does NOT assert that L_n is meromorphic.

Here is a local induction that also justifies the differentiability and
uniform sector bounds, rather than differentiating an unspecified O-term.
At n=0, L_0(z)^2=(1+z/k)^(-5) is rational. Solving (9) locally away from
zero is integration against an analytic nonvanishing factor. A meromorphic
forcing integrates to a meromorphic function plus analytic coefficients times
logarithms. Consequently L_1 has, at -k and -4k, finite Laurent-log expansions
of log degree at most one and pole degree four. Elsewhere away from zero it
continues analytically along either bank of the slit. At zero it is analytic
by (11).

Inductively the local representation is a finite sum h_l(d)(Log d)^l, with
meromorphic h_l and log degree at most 2^n-1. Squaring doubles the log degree;
integration raises it by at most one. To see the latter directly, expand the
analytic coefficients into convergent power series and integrate each
monomial d^m(Log d)^l: when m=-1 the log degree rises by one; otherwise
integration by parts gives a finite polynomial in Log d times d^(m+1).
The resulting analytic series converge on a smaller disk. Thus the maximum
log degree at depth n+1 is at most 2^(n+1)-1. This also provides derivative
bounds on the closed upper/lower local sectors. Integration can introduce no
finite singular point other than an existing point or four times one; zero
is already removable. The analytic homogeneous solution is harmless locally
at every nonzero point.

The largest forcing order at -rho_j is 2alpha_n. Since
alpha_(n+1)=2alpha_n-1, comparing its coefficient in (9) gives

 2alpha_(n+1) c_(n+1) b_(n+1,j)
           =c_n^2 [b_(n,j)^2-2b_(n,j-1)^2].             (14)

In fact 2z times the derivative of C d^(-alpha_(n+1)) contributes
2alpha_(n+1)C d^(-2alpha_n) at leading order. Equations (4)-(5) follow.
All other forcing terms are at least one power less singular, with the
stated finite log factors. Their integrated terms obey (13). The next
section proves that every leading coefficient is nonzero, completing the
induction and the claim that these are the actual singular points.

## 3. The polynomial invariant: all leading Mellin roots miss the strip

Put d_(n,j)=b_(n,j)^2. At every depth,

    d_(n,0)=1,
    d_(n,j)>=4d_(n,j-1)>0,  1<=j<=n.                    (15)

Proof. The update is d'_j=(d_j-2d_(j-1))^2. For an interior index,

d'_j >= d_j^2/4 >=4d_(j-1)^2 >=4d'_(j-1).

The last inequality uses 0<=d_(j-1)-2d_(j-2)<=d_(j-1).
At j=1 the same argument uses the missing coefficient zero, and at the new
last index d'_(n+1)=4d_n^2>=4d'_n. Start with the single entry 1.
In particular b_(n,0)=1, b_(n,j)>0 for 1<=j<n, and b_(n,n)<0 for n>=1.
No singularity was lost through an unproved leading-term cancellation.

The first rows are

 P_0(v)=1,
 P_1(v)=1+4v,
 P_2(v)=1+4v+64v^2,
 P_3(v)=1+4v+3136v^2+16384v^3.                          (16)

**All roots of P_n lie in |v|<=1/4.** This is the elementary
Enestrom–Kakeya mechanism, proved here rather than invoked as an oracle.
The coefficients of Q_n(w)=P_n(w/4) are positive and nondecreasing by (15).
If Q=sum_(j=0)^n q_j w^j, then

 (1-w)Q=q_0+sum_(j=1)^n(q_j-q_(j-1))w^j-q_n w^(n+1).

For |w|>1, the modulus of the first n+1 terms is at most q_n|w|^n,
strictly less than q_n|w|^(n+1). Hence Q(w) cannot vanish there.
This proves the disk assertion. It does not assert that the roots are real;
P_2 already has a nonreal conjugate pair.

For 0<=Re s<=1 one has |2^(-s)|>=1/2, so P_n(2^(-s)) is never zero.
On the wider strip -1/2<=Re s<=3/2 it is still uniformly separated from zero
at each fixed depth. Indeed, writing its roots r_l with multiplicity,

 |P_n(v)| >= d_(n,n)(|v|-1/4)^n,
 |v P_n'(v)/P_n(v)| <=2n,       |v|>=1/2.               (17)

No root data of xi or a finite numerical polynomial solve is used.

## 4. A complete contour remainder turns this into an actual-source theorem

Let F_n(z)=L_n(z)^2, and subtract the complete collection of leading terms:

 R_n(z)=F_n(z)-sum_(j=0)^n c_n^2 d_(n,j)(1+z/rho_j)^(-beta_n). (18)

These terms are a comparison function, NOT another probability law and NOT
an exact identity for the full F_n. For example at n=1 their total value at
zero is 5/64, whereas F_1(0)=1.

From (12)-(13), R_n is analytic on Omega, regular at zero, and has, along
both banks near each singular point,

 |R_n'(z)| <= C_n |z+rho_j|^(-beta_n)
                    (1+|log|z+rho_j||)^(2^(n+1)),      (19)

and R_n'(z)=O_n(|z|^(-beta_n-1)) at infinity. On the compact portions of
either bank away from the stated points, its continued derivative is bounded.
These estimates include all subleading polar, logarithmic and analytic terms.

For p=s/2 in -1/4<=Re p<=3/4, the Laplace/Mellin identity applied to the
actual pair and to each comparison gamma law gives exactly

 M_n(2p)-c_n^2 Gamma(beta_n+p)/Gamma(beta_n)
                 (c/k)^p P_n(4^(-p))
       =-c^p/Gamma(1-p) integral_0^infinity z^(-p)R_n'(z)dz. (20)

For positive real z this follows by Fubini from
integral_0^infinity z^(-p)x exp(-zx)dz=Gamma(1-p)x^p.
All needed negative moments exist by (10); the comparison gammas have shape
beta_n>=5. No subtraction at infinity is omitted.

Here is the explicit large-frequency contour argument. Put tau=Im p>2,
delta=1/tau and theta=pi-delta. Rotate the integration ray in (20) to
z=r exp(-i theta). The small arc vanishes since Re p<1 and R_n' is regular
at zero. The large arc vanishes by its complete decay above. The rotation
stays below the negative cut, crosses no singular point and contributes the
factor exp[-i theta(1-p)], of modulus exp(-theta*tau).

On that ray, in a fixed small neighborhood of -rho_j, the distance to the
singular point is comparable, with depth-dependent constants, to
|r-rho_j|+delta. From (19), direct integration yields

 integral_0^infinity r^(-Re p)|R_n'(r exp(-i theta))|dr
       <= C_n delta^(1-beta_n)(1+log(1/delta))^(2^(n+1)). (21)

To verify the power: substitute u=(r-rho_j)/delta in each local integral;
for beta_n>1 the integral of (1+|u|)^(-beta_n) times any fixed power of
1+|log(1+|u|)| is finite. The remaining compact part, zero endpoint and entire
infinite tail are bounded independently of delta. A finite sum covers all
n+1 singular points. This is an analytic full-ray bound, not a sampled contour.

There is a useful exact cancellation of gamma growth. Since beta_n is an
INTEGER, the gamma reflection and recurrence identities give

 1/|Gamma(1-p)Gamma(beta_n+p)|
              =|sin(pi p)|/[pi |(p)_(beta_n)|]
              <=exp(pi*tau)/(pi*tau^(beta_n)).          (22)

Combine (20)-(22), (17), and delta=1/tau. The factors exp(-pi*tau) and
exp(pi*tau) cancel, the remaining power is tau^-1, and exp(delta*tau)=e.
This proves (6)-(7) for the value. The proof for negative tau is its conjugate.
It is uniform on the stated wider vertical strip.

For derivatives, divide by the nonzero comparison factor to define e_n
holomorphically at large heights. Cauchy's estimate on a fixed-radius disk
inside the wider strip gives the same O_n bound for e_n' on 0<=Re s<=1.
The disk radius is independent of s and tau. It is not an unjustified
termwise derivative of a pointwise asymptotic. At n=0 the comparison is exact.

This is the load-bearing analytic transfer: positivity of P_n's coefficients
alone would not control M_n without the entire remainder argument (18)-(22).

## 5. Eventual critical-strip zeros are central and simple

At sufficiently large |t|, (6) and (17) make M_n nonzero on the whole closed
strip. Differentiate its logarithm locally. If v=2^(-s),

 M_n'/M_n(s)
  =(1/2)log(pi/15)+(1/2)psi(beta_n+s/2)
       -log2 * vP_n'(v)/P_n(v) + e_n'(s)/(1+e_n(s)).    (23)

The standard vertical gamma/digamma asymptotic, uniform for the fixed real
part range, gives Re psi(beta_n+s/2)=log(|t|/2)+o_n(1).
For s=sigma+it define the REAL derivative

 D_n(sigma,t)=d/dsigma log |M_n(s)/M_n(1-s)|.

The chain rule includes both reflected terms, and (17),(23) give

 D_n(sigma,t)
   >=log(pi |t|/30)-4n log2-o_n(1),                    (24)

uniformly for 0<=sigma<=1. Thus for each n it is positive, and for example
at least 1/2, beyond some finite T_n. The elementary logarithm alone becomes
large on a scale comparable to 16^n, but the unevaluated remainder threshold
must ALSO be passed. This is NOT a proved T_n=O(16^n) statement.

At sigma=1/2 the modulus ratio is one by conjugation. Strict increase in
sigma makes it greater than one on the right and less than one on the left.
A zero of M_n(s)+M_n(1-s) would require the ratio to be exactly -1. This proves
the zero confinement in BHH1.

On the central line write M_n(1/2+it)=r(t)exp(i phi(t)), r(t)>0. Then

 phi'(t)=Re[M_n'/M_n(1/2+it)]=(1/2)D_n(1/2,t)>0.

The reflected numerator is 2r cos(phi). At each of its zeros the t derivative
is -2r sin(phi)phi', which is nonzero. Thus every such high zero is simple.
The normalization denominator in (2) is positive, so this conclusion transfers
to H_n and, by the parent's nonvanishing multiplier, to E_n.

There is no conflict with #857's rigorous D_1(1/2,23)<0. The new theorem is
eventual, at fixed n; it does not validate the earlier all-height monotonicity
attempt or assign a value to T_1.

## 6. Complete fixed-depth zero count

At s=1/2+it, |v|=1/sqrt2. Factoring P_n and using |r_l/v|<=1/(2sqrt2)<1
provides a continuous logarithm

 log P_n(v)=log d_(n,n)+n log v+sum_l log(1-r_l/v),
 log v=-s log2.

The last sum has bounded imaginary part for each fixed n. Stirling's phase
formula therefore gives, with a continuous argument of M_n at high t,

 phi(t)= (t/2)log(pi t/(30*4^n))-t/2+O_n(1).             (25)

As phi is eventually strictly increasing and unbounded, it crosses every
sufficiently large half-integer multiple of pi exactly once. That proves
infinitely many high critical zeros and count (8). The bounded rectangle
below T_n contains only finitely many zeros: H_n extends holomorphically
across its closure and is not identically zero. Adding those zeros changes
only O_n(1). Multiplicities in that rectangle have not been restricted.

The fixed-depth counting law differs at linear order from the classical xi
count. That is compatible with E_n -> xi on fixed compact sets: n is FIXED in
(8), whereas it tends to infinity in the approximation theorem. No joint
height/depth limit has been controlled.

## 7. The attempted full ending and the exact remaining obligation

The new theorem proves high-height confinement for EVERY finite depth, not
confinement at every height and not confinement of the limiting xi.
It leaves the bounded-but-depth-dependent region |Im s|<T_n uncontrolled.

One sufficient completion would prove, for an unbounded sequence n_j, that
there are no off-central zeros in that remaining region. BHH1 would then give
whole-strip zero safety at those depths; #857's locally uniform E_n -> xi and
Hurwitz would prove RH. The weaker original criterion of confinement on
some expanding rectangles is also still valid.

Neither finite-region assertion is proved here. An off-central xi zero at a
fixed height, were it to exist, could be accompanied by off-central E_n zeros
inside the unresolved region for every large n. Finiteness of the exceptions
for each n does not exclude that possibility. The new high-height theorem
cannot be substituted for the missing unbounded-depth control.

No source moment, gamma polynomial or companion zero in this packet is a
newly asserted zeta zero. The exploratory numerical observations disclosed in
VALIDATION.md are not used in any theorem or certificate. The conclusions
are proposed paper proofs, not a completed RH proof awaiting routine review.

## References and dependency boundaries

* #857, exact head above: gamma–Dirichlet source coordinates, gamma-normalized
  entire E_n, and E_n -> xi. Its proposed proofs are imported only for the
  final approximation interface; (10)-(11) are reconstructed here. Parent
  quadrature/phase code is not executed or used as an oracle.
* Biane, Pitman and Yor, *Probability laws related to the Jacobi theta and
  Riemann zeta function and Brownian excursions*, arXiv:math/9912170: classical
  Brownian source and Mellin identification of the limit, inherited via #850.
* DLMF 5.5 and 5.11: gamma reflection/recurrence and vertical Stirling/digamma
  formulas. The contour comparison and its complete remainder are proved
  above, not imported from a numerical gamma routine.
* Enestrom–Kakeya's classical coefficient theorem; the complete special-case
  proof is Section 3. See also Annaby and Elsayed-Abdullah,
  arXiv:2406.17925, for its classical geometric background.

No exhaustive priority claim, independent mathematical acceptance, formal
proof build, or numerical value for T_n is made.
