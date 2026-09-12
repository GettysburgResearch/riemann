# BPW26: permanently certified bounded windows for the branching Xi orbit

Date: 2026-09-12. **Proposed component proofs and a complete finite source
certificate; independent mathematical and implementation review required.**
RH and a cofinal expanding-window confinement theorem remain UNPROVED.

This is an add-only continuation of the explicit-cutoff variant in PR #860,
`e1a782cffaafbc9cc228273ed94ce63ae0407632`, not a replacement of #859 or #860.
Those variants use the same historical directory/identifier; the present
packet has a new path and identifier and does not reconcile their histories.

## 1. Outcome, with both quantifiers visible

Keep the prescribed law, the shared multiplier, and the original scaling:

    X_0 ~ Gamma(5/2, RATE 5/2),
    X_(n+1) = (X_n+X_n')/U^2,  U uniform on [1,2],
    M_n(s) = E[(pi/6)(X_n+X_n')]^(s/2),
    H_n(s) = [M_n(s)+M_n(1-s)]/[2(1+M_n(1))].             (1)

The children are independent; the SAME independent U divides their sum.
All complex powers of positive variables use the real logarithm. H_n is real
under conjugation and invariant under s -> 1-s. Write

    F(z)=xi(1/2+iz),       f_n(z)=H_n(1/2+iz).             (2)

The theorem established by the written argument and the directed certificate is:

**BPW1. For EVERY integer n >= 32, f_n has exactly THREE zeros in**

    0 <= Re z <= 30,      |Im z| <= 1/2.                  (3)

They are simple and real. There is exactly one in each square

    |Re z - a_j| < 1/100,    |Im z| < 1/100,
    a_1=14.134725,  a_2=21.022040,  a_3=25.010858.         (4)

There are no zeros on any of these rectangle boundaries. The same complete
counts hold for F. By evenness, the negative-height reflected statement also
holds. The gamma-normalized entire E_n from #857 has the identical zeros
with multiplicity throughout this strip, so the conclusion applies to it too.

This is not a statement merely about three sampled values, three isolated
roots without a complement check, or the first 32 iterates. It holds for the
ENTIRE specified window and EVERY later iterate. The sample decimal centres
in (4) are exact rationals chosen to propose squares, not input assertions
that these are zeros.

**BPW2.** Let gamma_j and gamma_(j,n) be the real zeros of F and f_n in (4).
With rho=31/80 and C_30=71502/35, the certificate proves

    |gamma_(j,n)-gamma_j| <= (C_30/d_j) rho^n,
    (d_1,d_2,d_3)=(1/1000,1/100000,1/1000000), n>=32.    (5)

Every real convex interpolation between any f_m and f_n with m,n>=32
(and also between such a function and F) has the SAME three simple real
zeros in this window, one in each square. Thus there is no boundary entry,
pair collision, or departure from the line during these interpolations.
This concerns linear interpolation of analytic functions, not a claim that
interpolation is another stochastic branching operation.

The parent theorem controls heights ABOVE a depth-dependent T_n. BPW1 controls
heights BELOW the fixed value 30 at all sufficiently large depths. These do
not cover the interval 30 < |Im s| < T_n. No passage to increasing height is
inferred from the present fixed-height certificate.

## 2. The finite-to-all-future principle

Here is the general mechanism, separated from the numerical instance.
Let f_n and f be holomorphic on a neighbourhood of a compact rectangle D,
real under conjugation, with

    sup_(z in D) |f_n(z)-f(z)| <= C_D rho^n,  0<rho<1.    (6)

Let p be an independently constructed analytic model, with

    sup_(z in D) |p(z)-f(z)| <= eta.                       (7)

Choose finitely many disjoint conjugation-invariant subrectangles D_j inside
D. Subdivide each of their boundaries and the outer boundary into segments.
Suppose each segment's image under p is enclosed in a CONVEX set that still
avoids zero after inflation by eta+C_D rho^N. Choose polygon vertices inside
the relevant adjacent sets. The polygon winding is then the winding of every
f_n, n>=N, and of f, around that contour.

Proof: every point of each analytic image path is in its inflated set. The
linear polygon segment is also in that convex set, since both endpoint
representatives are there. Straight homotopy within that set avoids zero.
These homotopies agree at adjacent vertices. The argument principle therefore
identifies the complete zero counts. No lower bound for an unknown derivative
or an unobserved zero is assumed. This is an application of classical validated
argument-principle/Rouche methods, not a new general zero-counting principle.

If the outer count equals the sum of the inner counts, there are no other
zeros in D. If each inner count is one, reflection forces that zero onto the
real line: otherwise its conjugate would be a second zero. A count of one
includes multiplicity, so the zero is simple.

This holds uniformly for any convex interpolation of the f_n and f because
its error relative to p is bounded by the same envelope. The limiting function
is an allowable member, not an assumed real-rooted reference.

There is a useful multiple-zero version: do not require inner counts one;
require only that all inner rectangles lie in |Im z|<epsilon. Equality of
outer and summed inner counts then confines every zero to that epsilon-strip,
with all multiplicities retained. Thus a future expanding-window programme
need not assume simplicity of all Xi zeros. A sequence of successful such
certificates with heights tending to infinity and epsilon tending to zero
would imply RH. Existence of that sequence is not proved here.

The key change from a one-step induction is that ONE contour margin protects
ALL future depths. We do not need to pay the same geometric perturbation
repeatedly or assume that the branching map preserves a general zero-safe
class. That latter assertion is already false for other starting laws.

## 3. Reconstructing the exact orbital error used in the certificate

The fixed law is

    X_*=(6/pi^2) sum_(j>=1) E_j/j^2,
    E_j independent mean-one exponentials.                 (8)

Its Laplace transform sqrt(6t)/sinh(sqrt(6t)) verifies the distributional fixed
point directly. Equal-mean optimal coupling gives W2 contraction factor
sqrt(7/12); this identifies the unique fixed law. The complete identity

    E[(pi/6)(X_*+X_*')]^(s/2)=2xi(s)                        (9)

is the classical Biane--Pitman--Yor source identity. Here is a direct
normalization check, not a numerical special-function evaluation. For
V_*=(pi/6)(X_*+X_*'), the exponential product gives

    E exp(-t V_*)=pi t / sinh(sqrt(pi t))^2.

For every real r>0, positive Tonelli and the expansion
csch(x)^2=4 sum_(j>=1) j exp(-2jx) give

 E V_*^(-r)
  = [2 pi^(-r)/Gamma(r)] integral_0^infinity x^(2r+1)csch(x)^2 dx
  = 2^(1-2r) pi^(-r) Gamma(2r+2) zeta(2r+1)/Gamma(r)
  = 2xi(2r+1) = 2xi(-2r).

The penultimate equality uses gamma duplication, the last the classical xi
functional equation. Every positive moment exists from an exponential moment
of the convergent gamma sum; every inverse moment exists from the displayed
Laplace tail. Thus its complex Mellin transform is entire. The identity theorem
extends the equality from negative real s=-2r to every complex s. This
reconstructs the classical BPY binding rather than using any zero information.

For completeness the ingredients behind the sharper geometric error are
reconstructed here. Third-order order means equal moments through degree two
and E f(X)<=E f(Y) for f with bounded nonnegative third derivative.
Put W=U^-2 and B~Beta(5/2,5/2). Their zeroth, first and second moments are
1,1/2,7/24. On (0,1), the signed density W minus B has pattern -,+,-,+:
its first switch is 1/4; on [1/4,1] the ratio of the densities is

    (3pi/256) x^-3 (1-x)^(-3/2).

It decreases to x=2/3 and then increases, is >1 at 1/4, <1 at 2/3, and tends
to infinity at 1. These facts follow with 3<pi<22/7. Quadratic interpolation
at the three switches has a third-derivative remainder with the same signs.
Its quadratic part integrates to zero; its remainder integrates nonnegatively.
Thus B<=_3 W. Multiplication by an independent Gamma(5,rate5/2) gives
nu_0<=_3 nu_1 by the beta--gamma change of variables.

Positive scaling and independent summation preserve this order, proving
nu_0<=_3 ... <=_3 nu_*. Uniform fourth moments, supplied by the triangular
branching recurrence, justify passage to the limit for cubic-growth tests.
The third-moment recurrence is

    m_(3,n+1)=(31/80)m_(3,n)+651/400,
    m_(3,n)=93/35-(24/175)(31/80)^n.                       (10)

The nonnegative Peano kernel

    K_n(t)=[E(X_*-t)_+^2-E(X_n-t)_+^2]/2 >=0

has integral (4/175)rho^n. Taylor's integral remainder, with the matching
lower moments, gives for real OR complex smooth tests with bounded third
absolute derivative

    |E f(X_*)-E f(X_n)| <= (4/175)rho^n sup|f'''|.         (11)

This extension to complex tests uses the positive kernel, not an unjustified
identification of real and complex operator norms.

Ordering applied to -exp(-tx) shows L_n(t)<=L_1(t), n>=1. Integrating this
Laplace bound against t^(b-1)/Gamma(b) and using Holder gives

    E X_n^-b, E X_*^-b <=12,  0<=b<=3, n>=1.

Indeed X_1=G/U^2 with G~Gamma(5,rate5/2), and
E X_1^-3=15875/1344<12. This pays the possible small-variable singularity.
For p=s/2, smooth the complex power by an independent other child:

    g(x)=E[((pi/6)(x+Y))^p].

On 0<=Re s<=1, |g'''(x)|<=12|p(p-1)(p-2)|, including the endpoints.
Apply (11) to the two children in turn. This proves

    |M_n(s)-2xi(s)| <= (12/175)|s(s-2)(s-4)| rho^n.        (12)

For the normalizing denominator, M_n(1)>0 and |2xi(s)|<=1 on the closed strip
by (9) and Holder between the exponents zero and one. Subtracting the two
ratios, rather than dropping their denominator change, gives

 |H_n(s)-xi(s)| <= (6/175)rho^n [|s(s-2)(s-4)|
                           +|(1-s)(1+s)(3+s)|+3].         (13)

For the rectangle (3), every modulus in these products is <31. Thus

    |f_n-F| <= C_30 rho^n, C_30=(6/175)(2*31^3+3)=71502/35.
                                                               (14)

Holomorphy on a neighbourhood follows from the inverse-moment bounds and
positive moments; no boundary-only formal transform is being counted.

## 4. A complete theta polynomial model, with no zero oracle

The source used for F is exactly

 F(z)=2 integral_0^infinity phi(u)cos(zu)du,
 phi(u)=sum_(n>=1) [4pi^2 n^4 exp(9u/2)-6pi n^2 exp(5u/2)]
                                      exp[-pi n^2 exp(2u)].     (15)

Jacobi's transformation gives its usual entire Xi normalization. The code
never calls zeta, gamma, a supplied zero list, or a floating quadrature.

Let h=1/16384. Apply composite Simpson separately to the first three theta
terms on [0,2], [0,1], [0,1/2]. Each uses its WHOLE uniform grid with even
cell count. Combine coincident nodes only after retaining the correct endpoint
Simpson weights for each term. There are 57347 term/node evaluations and
57344 term/cells, not 57347 independent mathematical theorems.

The resulting positive finite cosine sum is

    F_d(z)=sum_l w_l cos(u_l z),    w_l>0, 0<=u_l<=2.

Its total mass is proved <1 by outward arithmetic. Define

    c_j=sum_l w_l (32u_l)^(2j)/(2j)!,
    p(z)=sum_(j=0)^120 c_j (-z^2/1024)^j.                   (16)

The coefficients in the receipt are intervals enclosing these discrete moments,
NOT claims that Simpson moments are exact continuous theta moments. The errors
below compare the COMPLETE Fourier transform, before estimating its oscillatory
terms separately. Scaling the polynomial variable prevents loss from evaluating
extremely tiny unscaled Taylor coefficients at large z.

### 4.1 The composite Simpson error is uniform on the full rectangle

For q=pi n^2 exp(2u), let

    P_0(q)=4q^2-6q,
    P_(r+1)=2q P_r'+(1/2-2q)P_r.

Then phi_n^(r)=exp(u/2-q)P_r(q). For the first four indices on [0,2],

    B_r=6 sum_(k>=1)|[q^k]P_r|(k-1)!

bounds the L1 derivative norm. Substitution q=pi n^2 exp(2u), exp(u/2)<3,
and extension of the positive gamma integral to zero prove this. The first
five bounds are

    60, 366, 3135, 71463/2, 2044911/4.

They also bound our smaller three-term, shorter-interval calculation.
For |z|<=31 and |Im z|<=1/2, complex cosine derivatives are bounded by
3*31^j on u<=2. The L1 fourth derivative bound is consequently

    L=3 sum_(r=0)^4 binom(4,r) B_r 31^(4-r).

On a two-cell Simpson block the Peano kernel has absolute maximum h^4/72.
The factor two in (15) is retained. The whole error is at most

    eta_S=h^4 L/36 <1.412*10^-10.                           (17)

The Peano bound is applied to the full complex integrand, so no exponentially
large absolute sum of separately estimated Taylor-moment errors is substituted.

### 4.2 Every omitted time and theta-index tail is paid

For the nth summand and |Im z|<=1/2,

 2 integral_U^infinity phi_n(u) exp(u/2)du
       <=4 exp(-A)(A^2+2A+2), A=pi n^2 exp(2U).           (18)

This follows by v=exp(2u) and t=pi n^2 v; t^(3/2)<=t^2 and q^-1/2<=1.
At the three chosen endpoints A>=72, using only pi>3 and e>8/3. Their ENTIRE
combined time tail is bounded by

    eta_T=12(72^2+144+2)(3/8)^72.

For all omitted indices n>=4, use v^(3/2)<=exp(3(v-1)/2) in the same integral.
The successive positive majorants have ratio <1/2, giving

    sum_(n>=4) 2 integral_0^infinity phi_n(u) exp(u/2)du
       <=8q^2 exp(-q)/(q-3/2)<9q exp(-q)
       <=432(3/8)^48=:eta_I,  q=16pi>48.                  (19)

The polynomial ratio is at most (5/4)^4, while the exponential ratio is
at most exp(-27); these elementary inequalities prove the ratio bound.
The code checks eta_T+eta_I<10^-15. It uses their actual rational sum, not zero.

### 4.3 The finite Taylor sum has its complete remainder

For |z|<=32, all |u_l z|<=64. The full omitted cosine series in (16) is bounded
by the first omitted term and a decreasing geometric ratio:

 eta_C=64^242/242! / [1-64^2/(243*244)].                    (20)

The total discrete mass is <1, so this is an error for F_d itself.
Thus throughout |z|<=31, |Im z|<=1/2,

    |p(z)-F(z)| <= eta=eta_S+eta_T+eta_I+eta_C
                       <1.412*10^-10.                    (21)

For later contour enclosure the code also bounds p''''. The complete discrete
cosine fourth derivative is <=3 sum_l w_l u_l^4. The tail after differentiation
is at most

    16*64^238/238! / [1-64^2/(239*240)].

Using c_2 in (16) proves sup|p''''|<1 on the same domain.

All exponential and pi values are outward integer intervals at 256 bits.
Exponentials are range-reduced to |x|<=1/8; a degree-48 Taylor polynomial is
inflated by 2/(8^49*49!), then squared back with outward rounding. Machin's
pi identity uses 64 and 20 alternating terms with their next-term remainders.
No binary64 value enters any accepting inequality.

## 5. The complete contour certificate

For n>=32, the common model error is at most

    E=eta+C_30(31/80)^32 <2.777*10^-10.                    (22)

The outer rectangle is subdivided into 3100 axis-parallel segments of length
at most 1/50. Each square in (4) has 40 segments of length at most 1/500.
Their full boundaries, rather than selected samples, are covered.

At each segment midpoint c, automatic interval Taylor shifting evaluates
p(c),p'(c),p''(c)/2,p'''(c)/6 from (16). For half-length r, the complete image
is enclosed by that cubic evaluated on the whole real/imaginary interval,
inflated in both coordinates by

    r^4/24 + E.                                           (23)

The fourth derivative bound above proves this remainder. The coefficient
interval widths are retained in every Taylor operation.

Every resulting rectangle avoids the origin. Both endpoint representatives
of the rational image polygon lie inside the same enclosure; the checker
verifies that fact as well. Exact integer ray crossings compute its winding.
The outer winding is THREE; each of the three inner windings is ONE.
By Section 2 these counts hold for F and simultaneously every f_n,n>=32.

The retained minimum coordinate-separation lower bounds exceed respectively

    outer:  1.169*10^-8,
    first:  1.366*10^-5,
    second: 1.745*10^-7,
    third:  1.222*10^-8.

They already INCLUDE the numerical model, cubic contour interpolation and
entire infinite-depth perturbation budget. They are not raw sampled moduli.
The full exact endpoints and polygon fingerprints are reconstructed in result.json.
This proves BPW1 and the uniform interpolation statement.

## 6. Geometric tracking of the protected roots

A separate interval calculation on each real interval in (4) uses the midpoint
Taylor polynomial for p'. Its remainder is bounded by r^3/6. Cauchy's estimate
on disks of radius 1/4 gives |p'-F'|<=4eta, since those disks remain in the
region where (21) holds. It certifies

    |F'|>d_j throughout the jth real interval,
    d_1=1/1000, d_2=1/100000, d_3=1/1000000.               (24)

In particular the derivative has a constant real sign there. At a zero of
f_n, (14) gives |F(gamma_(j,n))|<=C_30 rho^n. The real mean-value theorem,
using the genuine zero gamma_j in the same interval, proves (5).

Cauchy similarly gives |f_n'-F'|<=4C_30 rho^n there, which is <d_j/2 at n>=32.
Thus the zeros are uniformly transverse; smooth convex interpolation has
real simple root paths by the implicit-function theorem. This argument does
not assume a numerical zero ordinate is exact.

## 7. The attempted unconditional finish, and its precise failure

A future certificate may replace 30 by an arbitrarily large R, use a new finite
model p_R and cover all inner roots by thin rectangles. Its sufficient data are
explicit: complete outer winding; matching total inner winding; zero-free
boundary enclosures after adding eta_R+C_R rho^N. Once it succeeds, that entire
region is protected for every later depth and for xi itself.

No theorem here guarantees success on an unbounded sequence of R. A hypothetical
off-line zero of xi in a later window forces a positive winding in a rectangle
away from the line; sufficiently accurate approximants preserve rather than
remove it. Therefore choosing N ever larger cannot itself prove the desired
confinement. It improves accuracy, not the limiting zero geometry.

The high-height result in #860 is not used to turn the present certificate
into a whole-strip verdict. Its T_n increases with n and leaves a nonempty
uncontrolled intermediate region. The statements

    every n has a safe upper tail; and
    every n>=32 has a safe fixed lower window

have both now been established in proposed components, but their union need
not cover the whole strip. The next substantive result must establish expanding
protected windows (or a different global zero-exclusion argument), not merely
invoke local uniform convergence or a larger number of bounded samples.

These are classical contour/homotopy mechanisms composed with the prescribed
branching error theorem. The actual contribution is the all-future certificate,
the complete native first three-zero window, and explicit root tracking. No
external priority, new zeta-zero discovery, verification-height record, or
independent mathematical acceptance is asserted.


## 8. Classical references and attribution

The probability representation is due to Biane, Pitman and Yor,
*Probability laws related to the Jacobi theta and Riemann zeta function and
Brownian excursions*, arXiv:math/9912170. The fixed-law Mellin normalization
is explicitly reconstructed in Section 3; the external paper was not newly
audited in full. The gamma duplication identity is DLMF 5.5.5; xi symmetry
and normalization are DLMF 25.4.3--4. The argument principle, convex homotopy,
Peano kernel, Cauchy and Taylor techniques are classical. This packet claims
no priority for those mechanisms or for the first three Xi zeros.

The proposed source-specific contribution is the single complete certificate
covering every future branching depth, including the full window complement
and geometric root tracking. Its relation to #860 is complementary: it closes
one fixed lower window, not the depth-dependent intervening gap.
