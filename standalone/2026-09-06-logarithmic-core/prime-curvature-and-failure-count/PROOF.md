# Prime-power curvature, negative runs, and a failure-count route

Status: PROPOSED COMPONENT THEOREMS; independent mathematical/code review required.
RH and the new failure-count estimate are NOT proved.
Parent: PR #803 at 94ed8cd0395350b465165b424cc5c6366223d4ae.
Date: 2026-09-07. Labels PC1--PC6 are local, not canonical claim IDs.

This pass attacks the native signed estimate, not the Euler counterfamily.
It gives a complete distributional curvature formula with every prime-power
knot, an unconditional Green interpolation bound, and a quantitative theorem
on runs of negative values. A hypothetical zero of real part beta>1/2 forces
the counting function of failing INTEGER annular inequalities to have upper
power-growth exponent at least beta. Hence a square-root-scale upper bound
on the NUMBER of failures would suffice for RH. That counting estimate is
not supplied. An exact native divisor renewal is also derived and tested;
its absolute-value version is not a contraction.

The Green interpolation connection was prompted by reading #805's different
odd-Mobius scalar at ea66cd5b152e7960ad51ea51b154734eebc9b96a, PROOF.md
sections 5--6. Its function, normalization, and estimates are not substituted
for ours. No general Green identity or external priority is claimed.

## 1. Literal source and exact scope

Throughout Lambda(p^k)=log p for all primes p and integers k>=1, with
Lambda(n)=0 otherwise. Define, for u>0,

 w(u)=u/3-1/(192u^2),       1/4<u<=1,
      1/(3u^2)-u/192,       1<u<=4,
      0,                   otherwise.

The two outer endpoint values are zero and the center is continuous.
Set a0=45/128 and

 P(X)=X^(-1/2) sum_n Lambda(n)w(n/X),              X>0,
 D(m)=P(m^2)-a0*m+1/4,                           m>=2.       (1)

The sums are finite. All source coefficients and thresholds are literal;
prime-only replacements are not permitted. This is exactly the parent's
D(m), and B(m)=192m^3 P(m^2). A failure means D(j)<0 for an INTEGER j>=2:

 N_-(M)=#{j in Z: 2<=j<=M and D(j)<0}.                       (2)

This is a count, not negative mass or a mean square. Equality D(j)=0 is
not counted. No finite list of successes proves any all-M assertion.

The only inherited input needed for the reverse directions of PC4/PC5 is

 RH => D(m)>1/10 for every real m>=2.                       (3)

The complete proposed proof, including the gamma remainder and actual
spectral mass, is AS1--AS3 at the locked annular parent. It is not freshly
re-certified here. The new forward analytic implications are derived in
section 6 directly from (1), without using the parent operator, its positive
extension, or a finite verified zero height. No external zero census enters
the new curvature, interpolation, negative-run, or forward count theorem.

### 1.1 Elementary bounds used below

The classical divisor identity sum_(d|n)Lambda(d)=log n follows by prime
factorization. Prime valuations of binom(2r,r) also give

 psi(2r)-psi(r)<=2r log 2,   psi(x)=sum_(n<=x)Lambda(n).

Indeed floor(2r/p^k)-2floor(r/p^k) is 0 or 1 and equals 1 for r<p^k<=2r.
Dyadic summation gives psi(2^j)<2^(j+1)log2. Enclosing a real x by its next
power of two then gives psi(x)<4(log2)x<3x for x>=1. These inequalities
include every prime power. Also 0<=Lambda(n)<=log n for n>=2.

The exact weight bounds 0<=w<=21/64 imply D(m)>=-a0*m+1/4>-m.
Away from its knots,

 D'(m)=m^(-2) sum_n Lambda(n)v(n/m^2)-a0,
 v(u)=-w(u)-2u*w'(u)
     =-u-1/(64u^2)  on (1/4,1),
      u/64+1/u^2   on (1,4),
      0 elsewhere.                                        (4)

Both pieces have absolute value at most 65/64. Thus

 |D'(m)|<13 a.e.,   |D(m)-D(n)|<=13|m-n|.                   (5)

The parent has sharper constants; this deliberately coarser self-contained
bound is sufficient here. D is continuous and locally absolutely continuous,
since on each compact interval it is a finite sum of continuous piecewise
smooth functions. Its derivative is locally of bounded variation.

## 2. PC1: the complete distributional second derivative

For one coefficient put f_n(m)=m^(-1)w(n/m^2). Its entire support and pieces are

 f_n(m)=0,                                      m<=sqrt(n)/2,
        m^3/(3n^2)-n/(192m^3),                  sqrt(n)/2<m<sqrt(n),
        n/(3m^3)-m^3/(192n^2),                  sqrt(n)<m<2sqrt(n),
        0,                                      m>=2sqrt(n).           (6)

At the three knots, the RIGHT minus LEFT derivative jumps are respectively

 1/(2n),               -65/(32n),                1/(8n).    (7)

These signs matter: the central jump is negative. The regular second
 derivative is m^(-3)r(n/m^2), where

 r(u)=4u-1/(32u^2),       1/4<u<1,
      2/u^2-u/16,         1<u<4,
      0 elsewhere.                                        (8)

Consequently, as signed Radon measures on (2,infinity),

 D''=g(m)dm + sum_(n>=2) Lambda(n)[
       (1/(2n)) delta_(sqrt(n)/2)
      -(65/(32n)) delta_(sqrt(n))
       +(1/(8n)) delta_(2sqrt(n))],
 g(m)=m^(-3) sum_n Lambda(n)r(n/m^2).                       (9)

Atoms outside the domain are omitted and coincident atoms are ADDED before
an exact evaluation. The displayed sum is locally finite. Formula (9)
follows by integrating (6) twice against a smooth compactly supported test;
continuity eliminates delta-prime terms and (7) supplies every delta term.

The left r piece increases from 1/2 to 127/32; the right decreases from
31/16 to -1/8. Thus |r|<=4 and

 |g(m)|<=48/m.                                             (10)

There is no assertion D''>=0 as a measure: the negative central atoms forbid
that argument. The linear main term and constant in (1) have zero second
 derivative and do not alter (9).

### 2.1 A short-interval curvature budget, including endpoint atoms

For 2<=A<B<=2A put h=B-A and ell=log(4B^2). Then

 |D''|([A,B]) <= ell [32h/A+3/A^2].                        (11)

At A=B the same expression bounds the atom there by 3 log(4A^2)/A^2.
Here |D''| denotes total variation, not the absolute value of its signed mass.

Proof. The regular contribution is at most 48h/A. For the three families
of atoms, count ALL integer n in the relevant closed interval, which is a
safe upper bound for prime powers. The counts are at most

 entry: 12Ah+1,       center: 3Ah+1,       exit: (3/4)Ah+1.

Their maximum weights (without Lambda) are 1/(8A^2), 65/(32A^2),
and 1/(2A^2). Bound every Lambda by ell. The atomic total is therefore

 ell [(255/32)h/A+(85/32)/A^2].

Since ell>=log16>2, the regular term is at most 24ell*h/A. Now
24+255/32=1023/32<32 and 85/32<3, proving (11).
The +1 terms pay atoms at endpoints and noninteger range endpoints;
none is absorbed into an unrecorded big-O constant. This proof needs no
short-interval PNT, prime gap bound, or rounding of square-root knots.

## 3. PC2: an exact Green formula and fourth-power arithmetic sampling

For A<m<B define the nonnegative Dirichlet Green function

 G_(A,B)(m,t)=(min(m,t)-A)(B-max(m,t))/(B-A),  A<=t<=B.

Let l(m) be linear interpolation of D(A),D(B). The exact identity is

 D(m)-l(m)=-integral_(A,B) G_(A,B)(m,t) dD''(t).             (12)

Both sides vanish at the endpoints and have the same distributional second
 derivative. Alternatively apply the identity separately to each piece (6).
The sign is fixed by -partial_m^2 G=delta_t. In particular, with h=B-A and
2<=A<B<=2A, using G<=h/4 and (11),

 |D(m)-l(m)| <= log(4B^2)[8h^2/A+3h/(4A^2)].               (13)

This controls the full original scalar on every interval, not only a
sampled approximation. A finite list of endpoint values together with (13)
is a rigorous continuum certificate whenever its margins pay this budget.

Take A=k^2, B=(k+1)^2 with integer k>=3. Then B/A<2, h<=7k/3,
and the bracket in (13) is smaller than 45. Hence

 D(m)>=min(D(k^2),D((k+1)^2))-45log(4(k+1)^4),
                         k^2<=m<=(k+1)^2.                (14)

The constant follows from 8*49/9+(3/4)*7/81<45. No endpoint scan is needed
to establish the interpolation inequality. The original prime scale is
X=m^2, so these m-nodes correspond to X=k^4, rather than X=k^2.

**PC4 (sparse sign criterion).** The following are equivalent, with the
reverse implication importing exactly (3):

 RH;
 D(k^2)>=0 for every sufficiently large integer k;
 B(k^2)>=(135/2)k^8-48k^6 for every sufficiently large integer k.       (15)

Indeed (14) yields D(m)>=-C log m eventually on the whole real half-line.
Section 6 proves that such a one-sided subpower lower bound implies RH.
Conversely (3) gives the stronger strictly positive values under RH.
Only O(X^(1/4)) locations are required through prime scale X. This is a
count of sample locations, NOT the cost of evaluating their prime sums.

The parent's first-derivative-only discussion of denser square sampling is
not refuted: (9)--(13) supply new second-derivative information. For p>2,
the synthetic smooth function -m^(1-2/p)sin^2(pi*m^(1/p)) vanishes at all
m=k^p, has derivative tending to zero and second derivative O(1/m), yet
has power-sized negative valleys. It is NOT a native arithmetic source.
It shows why further sparsification is not automatic from these curvature
upper bounds alone. No universally optimal sampling claim is made.

## 4. PC3: a negative value forces a long run of negative values

Here is a local statement about the ACTUAL D, not an assumed sinusoidal zero
model. Let z>=16, let 1<=H<=z, and suppose D(z)<=-H. Put

 ell_z=log(16z^2),     r=sqrt(Hz/(256ell_z)).                (16)

There is a sign sigma in {-1,+1} such that

 D(z+sigma*t)<-H/2 for EVERY 0<=t<=r.                      (17)

No sign or monotonicity of the rest of D is assumed. This interval is not
necessarily centered at z. It has length r and remains inside [z/2,2z].

Proof. The left and right derivatives exist at z. If the right derivative
is nonpositive, move right; if the left derivative is nonnegative, move
left. The only remaining case is a positive upward jump across zero.
Then the right derivative is at most that jump. By (11) at a singleton,
choose a direction with the directed starting slope at most 3ell_z/z^2.

For 0<t<=z/2, apply (11) on the chosen interval between z and z+sigma*t.
Its smaller endpoint is at least z/2 and its endpoint ratio is at most two.
The one-sided Taylor formula for a function with BV derivative therefore gives

 D(z+sigma*t)<=D(z)+64ell_z*t^2/z+15ell_z*t/z^2.             (18)

This uses the total variation bound; keeping only the positive variation
could sharpen constants but is unnecessary. Initial jumps are paid by the
starting-slope term and interior jumps by the measure integral.

For z>=16 one has ell_z<=z: check at 16 using log2<3/4 and then
(d/dz)(z-log(16z^2))=1-2/z>0. Also r<z/2. At t=r the quadratic term in
(18) is H/4 and the linear term is

 (15/16)*sqrt(H ell_z)/z^(3/2) <=15H/(16z)<=15H/256.

Both bounds increase with t. Their sum is 79H/256<H/2, proving (17).
All constants and directions are explicit. If H=-D(z) for a native negative
value, the condition H<z follows already from P>=0; for the applications
below it suffices to choose H=z^(2a) with a<1/2.

An interval of length r contains at least r-1 integers. Thus, whenever r>=2,
(17) supplies at least r/2 consecutive INTEGER failures of D>=0. This counts
all integer points in the run, not just the prime-power activation points.

## 5. PC5: an off-line zero forces a quantitative failure-count exponent

Suppose a nontrivial zero rho has beta=Re rho>1/2, and write alpha=beta-1/2.
For every 0<a<alpha there are arbitrarily large integers z with

 D(z)<-z^(2a).                                             (19)

Section 6 rederives this fact directly from the finite prime-power source.
Since 2a<1, apply PC3 with H=z^(2a). We obtain a run of failures of length

 z^(1/2+a)/(16sqrt(log(16z^2))).                            (20)

In particular, along an unbounded sequence,

 N_-(2z) >= z^(1/2+a)/(32sqrt(log(16z^2))).                 (21)

Taking logarithms, limsup, and then a increasing to alpha proves

 **PC5a:** limsup_(M->infinity) log(1+N_-(M))/log M >= beta.  (22)

This is an unconditional implication from existence of the hypothetical
zero. It does not assert such a zero exists. It needs no rightmost zero,
zero simplicity, independence of ordinates, or positive-density hypothesis.
The long runs occur at arbitrarily large scales; they are not asserted in
every dyadic interval. The limsup in (22) must not be replaced by a liminf.

**PC5b (failure-count criterion).** With the inherited necessity (3),

 RH iff, for every epsilon>0, there is C_epsilon such that
        N_-(M)<=C_epsilon M^(1/2+epsilon) for every M>=2.    (23)

Under RH, (3) makes N_-=0. Conversely, if RH fails, functional-equation
reflection supplies a zero beta>1/2. Choose epsilon<beta-1/2. Equations
(22)--(23) contradict each other. A finite collection of exceptional
initial m does not affect the criterion.

More generally an upper bound N_-(M)=O(M^theta), with 1/2<=theta<1,
would exclude zeros with real part greater than theta. No such nontrivial
upper bound is proved here. The only bound supplied without an additional
arithmetic argument is the trivial N_-(M)<=M. A density-one success theorem
alone is insufficient: M/log M failures still have exponent one.

This changes the sufficient arithmetic task from banning every failure to
bounding how many failures occur. It is not advertised as a demonstrated
easier estimate. The exact signed count, or any estimate strong enough to
imply (23), remains an OPEN RH-strength task.

## 6. Direct one-sided pole proof from the finite arithmetic formula

This section supplies (19) and the forward implication used in PC4, without
a spectral-definition substitution. Put

 J(s)=integral_(1/4)^4 w(u)u^(s-1)du,
 A(s)=65/64-(4^s+4^(-s))/8.

Elementary integration of the two rational pieces gives the entire identity

 J(s)=A(s-1/2)/[9/4-(s-1/2)^2],                            (24)

with its removable limiting values at s=-1,2. In particular J(1)=45/128.
Every zero of A lies on Re s=3/2 or Re s=-3/2. Therefore J(rho) is nonzero
at every nontrivial zeta zero. This fixed kernel is chosen before rho.

For Re s>1/2, Fubini on the absolutely convergent Euler series gives

 integral_0^infinity P(X)X^(-s-1)dX
     =J(s+1/2)*[-zeta'/zeta](s+1/2).                       (25)

P(X)=0 for X<=1/2, so there is no origin-integrability issue. If
E(x)=D(exp(x/2)) on x>=log4, then exactly

 integral_(log4)^infinity E(x)e^(-s x)dx
  =J(s+1/2)*[-zeta'/zeta](s+1/2)-H_0(s)
      -a0*4^(1/2-s)/(s-1/2)+4^(-s)/(4s),                 (26)
 H_0(s)=integral_(1/2)^4 P(X)X^(-s-1)dX.

H_0 is entire and is retained, not discarded. The pole at s=1/2 cancels
because J(1)=a0. The continued expression is analytic at every positive
real s: zeta has no real zero on (1/2,1), by the alternating eta identity,
and none above 1, by its Euler product. At s0=rho-1/2 it has a pole with
residue -m_rho J(rho), nonzero for every analytic multiplicity m_rho.

If for some 0<=a<Re s0 we had D(m)>=-C m^(2a) eventually at integers,
the Lipschitz bound (5) would give the same type of lower bound at every
large real m (with a larger constant). Then E(x)+C'e^(ax) is nonnegative
on a tail. Its Laplace transform has the pole s0, so its convergence
abscissa is at least Re s0>a; the abscissa is finite since (1) and psi<3x
give E(x)=O(e^(x/2)). The meromorphic expression (26) plus the elementary
majorant transform is analytic at every real point greater than a.
Landau's theorem for a nonnegative Laplace density contradicts this.
The case of abscissa minus infinity would give an entire transform and
is likewise excluded by s0. Hence the integer liminf of D(m)/m^(2a) is
minus infinity, giving (19). The upper-excursion statement follows by the
same argument with -E, but is not needed for PC5.

For completeness, the Landau boundary step is the positive Taylor/Tonelli
argument. If the Laplace transform were analytic at its finite real
abscissa sigma_c, choose sigma_1>sigma_c sufficiently close so its Taylor
disk reaches a real sigma_2<sigma_c. The Taylor series evaluated to the
left is a sum of nonnegative integrals, hence by Tonelli equals the
integral at sigma_2. Its finite value contradicts the definition of
sigma_c. Such a Taylor disk exists from the union of the right half-
plane and a neighborhood of sigma_c. Compact initial terms are entire.

A lower bound D(m)>=-C log m also excludes every off-line zero by choosing
any positive a<Re s0. This proves the sufficiency in PC4. Reflection then
closes the usual RH statement. None of these implications supplies the
unproved arithmetic lower or counting bounds.

## 7. PC6: attack through the exact unit-Euler-factor divisor identity

The counterfamily in the parent lacked Lambda*1=log. Here it is imposed
exactly, including every prime power. Define the explicit lattice quantity

 G(X)=X^(-1/2) sum_(n<=4X) log(n)w(n/X),   X>0.

Finite rearrangement using that divisor identity gives

 sum_(d<=2X) d^(-1/2) P(X/d)=G(X),
 P(X)=sum_(d<=2X) mu(d)d^(-1/2)G(X/d).                     (27)

Endpoint conventions do not matter when a displayed endpoint is integral:
its weight is zero. P and G vanish at X<=1/2. To check the first formula,
d^(-1/2)P(X/d)=X^(-1/2)sum_n Lambda(n)w(nd/X); collecting nd=k yields
log k. The inverse is the ordinary Mobius divisor identity. These are
native exact identities, not formulas for an arbitrary positive Euler model.
They are instances of the classical inversion principles cited in SOURCES.json.

The attempted argument was to use the explicit lattice G to bound all
negative excursions of P-a0 sqrt(X). It does not close: isolating P(X)
subtracts a positive sum of earlier P values. A lower bound does not follow
from replacing those values by lower bounds. The formal power envelope
for the delayed positive operator at scale exponent epsilon carries weights

 sum_(2<=d<=2X) d^(-1/2-epsilon),

which diverge for 0<=epsilon<=1/2 (logarithmically at the endpoint). Thus
this direct absolute-value estimate is not a contraction at subpower scales.
No claim is made that every possible signed use of (27) must fail.

The packet stops at two concrete choices: exploit (27) without losing its
Mobius cancellation, or prove the sign-count bound (23) by a native prime-
distribution argument. The new curvature and run theorem prevent narrow
unobserved negative spikes from being the excuse for an invalid bound.
They do not bound the number of broad negative runs. RH remains unproved.

## 8. Evidence and exclusions

The finite checker independently reconstructs Laurent-polynomial derivatives,
all jumps, exact Green integrals for rationally scaled atoms, the curvature
constants, the fourth-power-grid budget, native divisor/Mobius identities,
and bounded actual rational-logarithmic values. It tests accepting data and
rejects altered results and source locks. The finite cases do not prove the
infinite analytic theorems; their arguments are the paper proofs above.

No new positive range, zero-free strip, zero census, full-window certificate,
Lean proof, predecessor-producer replay, or independent acceptance is claimed.
The branch preserves all preceding files. The new result is not a reviewer
acceptance of our own earlier work. The only inherited RH-to-positive-margin
premise in (3) retains its previous proposed-review status.
