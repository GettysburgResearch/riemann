# BUB26: unbounded protected bands and joint height/depth zero comparison

Date: 2026-09-12.
Status: PROPOSED component proofs, pending independent mathematical review.
**The requested gap-free expanding-window theorem and RH are NOT proved.**

Parent: PR #870 at `ee7f76736c235714496526f999e028d181302b56`.
New path: `standalone/2026-09-12-branching-unbounded-bands/`.
This is an additive continuation, not a repair or promotion of the parent.

## 0. The outcome and the distinction that must remain visible

There are two positive results.

1. An explicit joint height/depth theorem excludes approximation-created zeros
   outside small neighbourhoods of the ACTUAL xi zero divisor, over growing
   rectangles. Its depth cost is linear in height, apart from logarithms and
   the requested resolution. It does not put the actual divisor on the line.
2. Combining the source error with Conrey's CLASSICAL unconditional simple-zero
   proportion gives infinitely many disjoint FULL-WIDTH critical-strip bands,
   at unbounded heights, permanently containing exactly one simple central zero
   of every sufficiently late prescribed iterate. At least
   `(1/10-o(1)) N(T)` distinct xi ordinates through T admit such bands, where
   N(T) counts all nontrivial zeros with positive ordinate through T, with
   multiplicity. This counts bands by their xi ordinates, not by total length.

These bands are NOT a cover of `[0,T]`. Neither theorem proves that a prescribed
sequence of complete rectangles has only central zeros. The proof attempt at
that stronger statement stops in Section 8. The count in result 2 is a corollary
of an imported zero theorem and elementary pairing, not a new zero-proportion
record. No new actual-zeta zero computation is performed here.

## 1. Literal source and the error available before any zero selection

Let

    X_0 ~ Gamma(5/2, RATE 5/2),
    X_(n+1) = (X_n+X_n')/U^2,   U ~ Uniform[1,2],
    M_n(s) = E[((pi/6)(X_n+X_n'))^(s/2)],
    H_n(s) = [M_n(s)+M_n(1-s)]/[2(1+M_n(1))].             (1)

The children are independent; one independent U scales their SUM. Positive
real variables are raised to complex powers with the real logarithm.
The target is the analytic completion

    xi(s) = (1/2)s(s-1) pi^(-s/2) Gamma(s/2) zeta(s),
    xi(0)=xi(1)=1/2.

Both xi and H_n are real under conjugation and invariant under s -> 1-s.
For n>=1 they are holomorphic on a neighbourhood of the closed critical strip.
Let Z_xi denote the complete nontrivial zero set, without assuming RH or
simplicity. Multiplicity is retained whenever zeros are counted.

The source estimate reconstructed in BPW26 is

 |H_n(s)-xi(s)| <= (6/175) (31/80)^n
   [|s(s-2)(s-4)|+|(1-s)(1+s)(3+s)|+3], 0<=Re s<=1.    (2)

For every real R>=1, therefore,

 sup_(0<=Re s<=1, |Im s|<=R) |H_n-xi| <= C_R rho^n,
 C_R=(6/175)[2(R+5)^3+3],   rho=31/80.                 (3)

The slightly loose R+5 makes every factor bound valid without a height
threshold. Unlike the parent's tight C_30, it is a general-purpose constant.
The changing normalization in H_n is included.

### Source reconstruction behind (2)

This paragraph is a reconstruction of the parent argument, not a new zero
input. The normalized Brownian fixed law is

 X_*=(6/pi^2) sum_(j>=1) E_j/j^2, E_j independent mean-one exponentials.

Its Laplace transform is sqrt(6t)/sinh(sqrt(6t)). Direct integration verifies
that it is fixed under (1). Equal-mean independent-copy coupling gives W2
contraction sqrt(7/12), so it is the unique mean-one finite-second-moment fixed
law. Its pair V_*=(pi/6)(X_*+X_*') has Laplace transform
pi t/sinh(sqrt(pi t))^2. Positive Tonelli and gamma duplication give
E[V_*^(-r)]=2xi(-2r) for r>0; all positive and negative moments exist, so
analytic continuation gives E[V_*^(s/2)]=2xi(s). This is the classical BPY
source identity [BPY], not a model for random prime signs.

For B~Beta(5/2,5/2) and W=U^-2, moments of degrees 0,1,2 agree. Their density
difference W-B has exactly three switches and signs -,+,-,+. On [1/4,1] the
ratio is (3pi/256)x^-3(1-x)^(-3/2), decreasing to 2/3 then increasing.
Quadratic interpolation at the switches proves B <=_3 W. Multiplying by an
independent Gamma(5, rate 5/2), followed by induction under positive scaling
and independent addition, gives nu_0 <=_3 ... <=_3 nu_*.

The exact third-moment gap is (24/175)rho^n. Hence the positive Peano kernel

 K_n(t)=[E(X_*-t)_+^2-E(X_n-t)_+^2]/2

has mass (4/175)rho^n. Taylor's integral remainder controls complex tests by
that mass times their supremum third derivative. Uniform fourth moments,
obtained from the triangular raw moment recurrence, justify passage to the
fixed law in cubic-growth tests.

The order gives L_n(t)<=L_1(t) for n>=1. Mellin integration of this positive
Laplace bound and Holder give E X_n^-b,E X_*^-b<=12 for 0<=b<=3; the endpoint
E X_1^-3 is 15875/1344<12. For p=s/2, smoothing (x+y)^p by the other child
bounds its third derivative by 12|p(p-1)(p-2)|. Replacing two children in turn
therefore bounds |M_n(s)-2xi(s)| by (12/175)|s(s-2)(s-4)|rho^n.
Finally |xi(s)|<=1/2 on the strip follows from the positive BPY representation
and E V_*^0=E V_*^(1/2)=1. Subtracting the two normalized ratios in (1)
gives (2), including the `+3` contribution of M_n(1)-1. No Xi zero is used.

## 2. Local lower modulus, with all possible zeros retained

Put Z(s)=(s-1)zeta(s), with its analytic value at one. For every real t,

 max_(|z|<=4) |Z(2+it+z)| <= (|t|+10)^6,
 |Z(2+it)| >= |1+it|/2 >=1/2.                          (4)

To verify the first bound, use the N=1, n=2 Euler--Maclaurin formula [EM]:

 zeta(s)=1/(s-1)+1/2+s/12-s(s+1)(s+2)/720
  -s(s+1)(s+2)(s+3)(s+4)/120
       * integral_1^infinity B5({x}) x^(-s-5) dx.

B5(x)=x^5-(5/2)x^4+(5/3)x^3-x/6 has absolute value <=16/3<6 on [0,1].
In the disk Re s>=-2. Each displayed linear factor is bounded by U=|t|+10,
and the integral is at most 3. Thus

 |Z(s)| <= 1+U/2+U^2/12+U^4/720+U^6/40 <= U^6.

The final inequality follows at U=10 and thereafter by dividing by U^6.
The second bound in (4) uses the absolutely convergent reciprocal Euler
series: |1/zeta(2+it)| <= zeta(2)<2. This is not a critical-half-plane estimate.

**Local lemma.** Suppose f is analytic near the closed disk |z|<=4, f(0)=1,
and |f|<=2^L there, where L>=1. If |z0|<=2 and z0 is at distance at least
0<delta<=1 from every zero in |z|<7/2, then

             |f(z0)| >= 2^(-4L)(delta/6)^(8L).           (5)

Proof. Jensen's formula bounds the number of zeros in |z|<7/2 by 8L, with
multiplicity: log(8/7)>1/8 and log2<1. Choose a radius r in [3,7/2) with no
zero on its boundary. Remove all zeros inside it by the finite disk-r Blaschke
product B. The analytic zero-free quotient g=f/B has |g|<=2^L on the disk
and |g(0)|>=1. Harnack's inequality applied to

             L log2 - log|g(z)| >=0

gives log|g(z0)|>=-4L log2, since (r+2)/(r-2)<=5. Each removed Blaschke factor
has modulus at least delta/(r+2)>delta/6 at z0. Multiply at most 8L factors.
Choosing zero-free radii and taking limits handles boundary zeros in Jensen's
count. No zero is discarded from the divisor or presumed to be central. QED.

The argument is the classical Jensen/Blaschke/Harnack minimum-modulus method.
It is rederived here at |z0|<=2; earlier source-stability work used a related
safe-centred disk at a single line. This is not a priority claim.

For an integer R>=1 set

       L_R = 1+6 ceil(log2(R+10)).                       (6)

Normalize Z(2+it+z) by Z(2+it), and set z0=s-(2+it)=Re(s)-2. Equation (4)
and (5) show, for 0<=Re s<=1, |Im s|<=R, and dist(s,Z_xi)>=delta,

       |Z(s)| >= (1/2)2^(-4L_R)(delta/6)^(8L_R).        (7)

The only other zeros of Z are the trivial zeros -2,-4,...; none is within
7/2 of 2+it. Thus the stated separation from Z_xi supplies every required
local separation. The safe point s=1 is an analytic removal throughout.

## 3. The gamma factor is bounded below, not replaced by an asymptotic

Use the cancellation-safe identity

 xi(s)=pi^(-s/2) Gamma(1+s/2) Z(s).                    (8)

For z=a+ib with 1<=a<=3/2, Binet's integral [BINET] is

 log Gamma(z)=(z-1/2)Log z-z+(1/2)log(2pi)+R(z),
 R(z)=integral_0^infinity exp(-zt)
             [(1/2)coth(t/2)-1/t] dt/t.

The bracket is between 0 and t/12; this follows by differentiating
x cosh x-sinh x and (1+x^2/3)sinh x-x cosh x. Hence |R(z)|<=1/(12a).
Since |z|>=1, a+1/(12a)<2, sqrt(2pi)>2, and e<3,

 |Gamma(a+ib)| > (2/9) exp(-pi|b|/2).                 (9)

Here b arg z<=pi|b|/2, with the principal logarithm in the right half-plane.
No asymptotic threshold or unevaluated constant enters (9).
Together with pi^(-Re(s)/2)>1/2 and (7),

 |xi(s)| > (1/18) exp(-pi R/4)
                    2^(-4L_R)(delta/6)^(8L_R).       (10)

For dyadic delta=2^-a with integer a>=0, define

 B(R,a)=ceil(8R/7)+5+(8a+28)L_R.                      (11)

Then every separated point in the rectangle satisfies

                         |xi(s)| > 2^(-B(R,a)).       (12)

Indeed pi<22/7 and log2>11/16 imply exp(-pi R/4)>2^(-8R/7);
log2>11/16 follows already from the first three positive atanh(1/3) terms.
Also 1/18>2^-5 and 6<8. These estimates explain every integer in (11).

## 4. An explicit joint depth/height theorem for the whole divisor

Let

 m_R=ceil(log2 C_R),
 D(R,a)=11 ceil([B(R,a)+m_R+1]/15).                    (13)

All ceilings in (6),(11),(13) are integer/rational operations. In particular
rho^11<2^-15 is the exact integer inequality

                  31^11 * 2^15 < 80^11.

**BUB1.** For EVERY integer R>=1, integer a>=0, and integer n>=D(R,a),

 H_n(s)=0, 0<=Re s<=1, |Im s|<=R
       ==> dist(s,Z_xi)<2^-a.                         (14)

At every point outside these neighbourhoods, the whole segment
`xi(s)+t(H_n(s)-xi(s)), 0<=t<=1`, is nonzero. The same statement holds for
any real convex combination of xi and iterates whose depths are >=D(R,a).

Proof. Write q=ceil([B+m_R+1]/15), so D=11q. Equation (3) gives

 C_R rho^n <= C_R rho^(11q)
          < 2^(m_R-15q) <= 2^(-B-1) < |xi(s)|/2.

Equation (12) supplies the last comparison. This proves (14) and the homotopy
claim. All hypothetical off-critical xi zeros remain in the excluded set.

**BUB2 (multiplicity-preserving contour form).** Let a bounded domain have
piecewise smooth boundary, with its closure inside the closed rectangle,
and suppose every boundary point is at distance >=2^-a from Z_xi. Then all
n>=D(R,a) have exactly the same zero count in that domain as xi, including
multiplicity. In particular, a reflection-invariant domain with xi count one
contains one simple central H_n zero at every such depth.

Proof. Equation (12) excludes boundary zeros, and the preceding strict error
bound gives Rouche. Domains touching Re s=0 or1 are legitimate because the
functions extend holomorphically to a neighbourhood. Reflection is
s -> 1-conjugate(s), which preserves an ordinary full-width horizontal band.
An off-central zero would bring a distinct reflected zero, so a count of one
forces centrality. Repeated xi zeros are NOT asserted to remain unsplit: only
cluster multiplicity is preserved in the general version. QED.

The schedule has the transparent asymptotic

 D(R,a) <= (88/105)R + O((a+1)log(R+10)),              (15)

with all constants explicitly given by (6),(11),(13). It is a depth cost for
comparison AWAY from the actual divisor, not for proving where that divisor
lies. It does not claim an efficient algorithm evaluating the branching tree.

Example analytic schedules (not zero computations):

| R | a | D(R,a) |
|---|---|---|
| 30 | 7 | 2321 |
| 100 | 7 | 2750 |
| 1000 | 10 | 5698 |
| 1000000 | 20 | 854832 |
| 1048576 | 20 | 896368 |

The parent's tailored height-30 numerical margins give the much better depth
32. There is no conflict: (13) works with no numerical contour margin.

For a particularly simple prescribed growing sequence, take j>=4,

 R_j=2^j,   delta_j=2^-j,
 n_j=2^(j+1)+64(j+4)^2.                               (16)

Then n_j>=D(R_j,j). Thus all n>=n_j have every zero up to height R_j within
1/R_j of some actual xi zero. To check the schedule directly one may use
rho<1/2, L_R=6j+7, C_R<R^3, and ceil(8R/7)<=2R; the excess polynomial is
16j^2+285j+822>0. This is an unconditional expanding-window SHADOWING theorem.
It is deliberately not called expanding-window CENTRAL confinement.

## 5. An unconditional supply of permanently protected full-strip bands

Here a protected band means an open height interval I=(a,b), 0<a<b rational,
with its FULL strip rectangle

                Q_I={s: 0<=Re s<=1, a<=Im s<=b}.       (17)

The conclusion is: there is a finite integer N_I such that every n>=N_I has
no boundary zero and exactly one simple central zero inside Q_I. Real convex
interpolations among these late iterates and xi have the same property.
This is stronger geometrically than a small disk around a known zero.

Let N(T) count all nontrivial zeta zeros with 0<Im rho<=T, with multiplicity.
Let S(T) count simple central zeros in that range. Call a simple central
ordinate clean when NO off-central zero has that same ordinate, and let G(T)
count clean ordinates. We do not assume all central ordinates are clean.

**Counting lemma.** Exactly, at every height cutoff,

                    2G(T) >= 3S(T)-N(T).             (18)

Proof. Every non-clean simple central zero requires at least one reflected
pair of off-central zeros at its ordinate. Those pairs use disjoint zero
multiplicities at different ordinates. If B=S-G is their number, then
N>=S+2B=3S-2G. Central multiple zeros and extra off-central pairs only increase
N, so they cannot invalidate the inequality. QED.

The imported theorem is Conrey (1989) [CONREY]:

                    S(T)>=(2/5-o(1))N(T).             (19)

Its simplicity assertion is essential. This paper DOES NOT reprove Conrey's
mollified mean-square/Kloosterman argument, nor use an RH-conditional statement
about simple zeros. The original published introduction explicitly states
simple zeros on the critical line. Equation (19), not a newer unreviewed
proportion, is the external arithmetic input here.

Therefore

                    G(T)>=(1/10-o(1))N(T).            (20)

**BUB3 (unbounded exact protected bands).** There is a locally finite family
of pairwise disjoint rational intervals I_l, at unbounded heights, such that
each rectangle Q_(I_l) is permanently protected as above. They can be selected
one for every clean simple central ordinate. Counting bands by that ordinate
through T gives at least `(1/10-o(1))N(T)` bands.

Proof. For a clean simple zero rho=1/2+i gamma, zeros in a bounded strip are
finite. Since none other has ordinate gamma, a sufficiently short rational
interval containing gamma has exactly that one zero anywhere in its full
strip rectangle and no boundary zeros. Choose its endpoints inside one third
of the gaps to the neighbouring DISTINCT zero ordinates, with width <1/4.
These intervals can be chosen pairwise disjoint and locally finite.

The boundary has positive distance from the complete zero set: compactness,
zero discreteness, and the classical absence of zeros on Re s=0,1 ensure this.
Choose integer R>b and a with 2^-a below that distance. BUB2, with
N_I=D(R,a), protects the entire band for all later depths. Equation (20)
supplies an unbounded supply. No numerical zero height or derivative is used.
QED.

The constants R and a for an individual band are not numerically instantiated
here. There is no uniform lower bound on band widths and no claimed positive
proportion of HEIGHT MEASURE. The fraction 1/10 concerns a count of zero
ordinates. There is also no single finite depth protecting all bands at once;
only every finite selection has a common depth, namely max N_I.

One can start with the parent's protected `[0,30]` rectangle and select this
family above 30. Removing its finitely many low ordinates changes no asymptotic.
Conrey's theorem is used to prove existence of infinitely many successes, not
to supply a table of new numerical zero certificates.

## 6. A source-defined search is guaranteed infinitely many successes

There is a terminating test for any given band whose boundary is zero-free:
refine complete theta-integral enclosures along its boundary until a zero-free
polygon homotopy certifies the winding. Arbitrary precision, truncation order,
time cutoff and theta-index cutoff are increased; all tails remain bounded.
For a genuinely zero-free compact contour its minimum modulus is positive,
so sufficiently fine enclosures eventually succeed. Count one certifies a
clean simple central zero by reflection. A positive retained boundary margin
then chooses N_I via (3), without an unknown-zero input to the algorithm.

A fair dovetail over rational bands and refinement levels therefore emits
infinitely many successful permanent bands. Requiring emitted bands to be
disjoint does not obstruct this: each emitted count-one band contains just
one zero, and a locally finite set of zero ordinates leaves neighbourhoods
around the remaining clean ones. Limiting width to <1/4 prevents a remote
accepted band from interfering with infinitely many candidates near one height.

This is a computability/existence algorithm, not an implementation or executed
unbounded search. No runtime or first-success-height bound is supplied.
The present executable checks finite algebra and analytic constants only.
The parent's contour evaluator has a fixed height-30 contract; its current
CLI is NOT silently advertised as this arbitrary-height program.

## 7. Why the counting input cannot fill all the gaps

The fraction in (20) is sharp using only the information in (19). At four
synthetic positive ordinates place: one clean simple central zero; and at
each of three other ordinates, a simple central zero plus a reflected simple
pair off the line. There are N=10 positive-height zeros, S=4 simple central
zeros and G=1 clean ordinate. Conjugate the configuration at negative heights.
A real polynomial invariant under s -> 1-s realizes this configuration exactly.
It is NOT a zeta or branching source, and is used solely to check the count
inference. It shows why replacing 1/10 by 1, on the basis of (19) alone, is false.

A hypothetical actual off-central xi zero is entirely consistent with BUB1--3.
Choose a small disk around it, lying strictly on one side of the critical line
and with a zero-free boundary. BUB2 then forces the same positive zero count
of H_n in that OFF-CENTRAL disk at every sufficiently large depth. Better
comparison protects that zero just as faithfully as it protects a real one.

Consequently the new unconditional guarantees cannot be read as a proof of RH:

 - expanding rectangles are controlled relative to the ACTUAL xi divisor;
 - exact central protected bands exist at unbounded heights but have gaps;
 - the fraction of guaranteed bands counts zeros, not coverage of every point;
 - the high-height theorem in #860 has the opposite fixed-depth quantifier;
 - isolated simple-zero information cannot replace all-cluster confinement.

## 8. The attempted gap-free completion and the precise stopping point

The user requested cofinal protected windows. A sufficient target remains:
there exist R_j -> infinity, epsilon_j ->0 and depths n_j ->infinity such that
ALL zeros of H_(n_j) in 0<=Re s<=1, |Im s|<=R_j lie within epsilon_j of the
central line. Multiplicities may be grouped; no simplicity assertion is needed.
Rouche on a small off-central limiting zero disk proves the RH implication.

BUB1 completes a quantitative comparison step but gives proximity to Z_xi,
not to the line. Substituting the line for Z_xi in (14) without an additional
arithmetic theorem would assume the needed conclusion. BUB3 supplies an
unbounded collection of successful bands but not a cover of the intervening
regions. Neither a count proportion nor a finite boundary-margin calculation
bridges those gaps.

I attempted this completion by combining the inherited geometric error with
an unconditional minimum-modulus estimate, rather than assuming a lower bound
on an unknown zero-free contour. The resulting theorem is (14). Its separation
hypothesis exposes exactly where the all-central conclusion is still missing.
I do not have a proof that the remaining off-central clusters are absent.

The proposed new component proofs thus extend protected windows to UNBOUNDED
HEIGHTS IN A DISJOINT FAMILY, and price complete divisor comparison on growing
rectangles. They do not deliver the requested gap-free all-height extension.
No independent reviewer is asked to supply that missing theorem as a finishing
check, and no RH status is promoted.

## References and input boundaries

[BPY] P. Biane, J. Pitman and M. Yor, Probability laws related to the Jacobi
 theta and Riemann zeta function and Brownian excursions, 2000/2001;
 https://arxiv.org/abs/math/9912170. Classical source representation, not new.
[CONREY] J. B. Conrey, More than two fifths of the zeros of the Riemann zeta
 function are on the critical line, J. reine angew. Math. 399 (1989), 1--26;
 https://doi.org/10.1515/crll.1989.399.1. Imported unconditional simple-zero
 proportion; the original publisher's introduction was checked, not its full
 proof re-audited. No claim of a new zero proportion.
[EM] NIST DLMF 25.2.10, https://dlmf.nist.gov/25.2.E10.
[BINET] NIST DLMF 5.9.10_2, https://dlmf.nist.gov/5.9.E10_2.
[ZERO] NIST DLMF 25.10, https://dlmf.nist.gov/25.10. Classical zero strip,
 symmetry and discreteness. No RH conclusion is imported.
[BPW26] PR #870 at ee7f76736c235714496526f999e028d181302b56,
 standalone/2026-09-12-branching-permanent-window/PROOF.md, especially Section 3.
 Parent tests and height-30 numerical certificate were NOT rerun in this pass.

Jensen, Harnack, finite Blaschke products, Rouche, and analytic zero isolation
are classical. Their quantitative application is proved at the stated scope.
No external originality priority is claimed. Bounded checks of integer
constants and synthetic configurations do not machine-prove analytic lemmas
or the imported Conrey theorem.
