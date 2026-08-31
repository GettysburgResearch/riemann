# Local crowding, weighted Hardy sampling, and actual-Xi capture

Status: PROPOSED ANALYTIC BRIDGE AND EXACT FINITE CONTROLS; review pending.
Base: `a7479e85fdc2a464cdc753021435cfef7a1f3910` (LB).
Scope: the literal boundary-dx Hardy metric; fixed lambda>0; bounded-height
surviving denominator nodes. RH, innerness, and cofinal alignment are not proved.

The proposed bridge replaces LB3's unpaid uniform unweighted Bessel hypothesis
by an explicit per-unit-cell Carleson crowding cost. This is a weighting of
test vectors, NOT a change of physical Hilbert norm or source observation.

Preregistered exact controls:

1. For every N=1,...,16, test two declared rational cell families:
   dispersed x_j=1/4+j/[2(N+1)], y_j=1/(64N^2), and
   crowded x_j=1/4+j/[64N^2(N+1)], y_j=1/4, j=1,...,N.
   Predictions: exact cell Carleson costs respectively1 andN.
2. Compare the polynomial-size endpoint/height enumeration with an independent
   complete nonempty-subset formula on all declared families N<=8 and a fixed
   mixed-height four-node control. No random or additional fitted families.
3. Exhaust rational test intervals with left endpoint j/8, -8<=j<=16,
   and length m/8, 1<=m<=24, on a fixed three-cell union of the declared
   families. Verify the universal normalized box bound3|I|, retaining all rows.
4. Verify exact crowded-kernel Rayleigh bounds and dyadic sparse-survey
   summability controls. All numeric output is rational strings or integers.

The all-height Jensen bound and the infinite Carleson/capture implication are
written analytic arguments. The finite controls do not machine-certify them.
No actual-Xi zero is newly evaluated in this packet.

## 1. An exact local crowding quantity

For a finite set S of nodes b=x+iy with0<y<=1 in one half-open unit cell,
let mu_S=sum_(b in S)y delta_b. Repetitions may be counted, although the
capture application uses distinct surviving zeros. Define

    c(S)=sup_I mu_S({x in I, 0<y<=|I|})/|I|,       c(empty)=1.       (OC1)

Intervals in this supremum may be closed: for a finite atomic measure this
has the same supremum as open boxes, by arbitrarily small enlargement.
For nonempty S, 1<=c(S)<=#S. The first bound uses one atom and an interval
of length y through it; the second uses y<=|I| for every contributing atom.

There are two exact, finite formulas. For each nonempty subset A of S put

    r(A)=max(max_(b in A)y_b, max_(b in A)x_b-min_(b in A)x_b).

Then

    c(S)=max_(nonempty A subset S) (sum_(b in A)y_b)/r(A).           (OC2)

For any A an interval of length r(A) contains it and its box contains every
atom of A, possibly more. Conversely, for any interval I the atoms its box
actually contains form A with r(A)<=|I|. These two inequalities prove OC2;
neither assumes a separation or height lower bound.

A polynomial-size alternative enumerates

    r in {all y_b} union {all positive |x_b-x_d|},
    a in {all x_b},
    [sum_(a<=x_b<=a+r, y_b<=r)y_b]/r.                              (OC3)

Its maximum is c(S). To see completeness, take a maximizing A from OC2,
set a=min_A x and r=r(A). This is one of the candidates, and its numerator
includes A. Every candidate is itself a real Carleson box. The producer
uses OC3; a separate exhaustive-subset checker uses OC2 for N<=8.

## 2. Cell normalization supplies a uniform weighted Bessel bound

Let S be ANY node family in0<y<=1 with FINITELY MANY nodes in each unit
cell, and S_n its nodes with n<=x<n+1. Let c_n=c(S_n). This applies to an
entire denominator's zeros,
or to any declared subset, without needing the zeros to be separated.
Put

    mu=sum_n (1/c_n)sum_(b in S_n)y_b delta_b.

**Theorem OC1.** For EVERY interval I of length r>0,

    mu(Q_I)<=3r.                                                   (OC4)

If r<1, I meets at most two unit cells, and each cell contributes at most r
by its defining c_n. If r>=1, I meets at most r+2 cells; each complete cell
has normalized mass<=1, by testing its own interval of length1 and using
y<=1. Thus mu(Q_I)<=r+2<=3r. Endpoint conventions do not alter these bounds.

Invoke the classical half-plane Carleson embedding theorem, in the boundary-dx
normalization: there is an absolute finite C such that

    sum_(b in S) |<F,e_b>|^2/c_(floor x_b) <= C ||F||_H2^2,         (OC5)

where e_b is LB's unit kernel. Indeed its reproducing kernel has squared
norm1/(4pi y), so the left side is4pi integral|F|^2dmu. OC4 supplies a
uniform embedding bound. The imported result is
[Jacob--Partington--Pott, Theorem1.1, pp2--3](https://arxiv.org/pdf/1201.1021).
We do not claim that the numerical box constant3 is itself the Bessel
constant C; the classical embedding constant is included in C.

This weights test vectors e_b/sqrt(c_n); it does not replace the physical
metric, transform U, remove a source atom, or commute an inner multiplier
through a band projection. The full physical operator is unchanged.
Also c_n can be replaced by the coarser q_n=max(1,#S_n), or by any proved
upper bound for c_n. For one selected node per occupied cell, c_n=1.

## 3. Actual-Xi local zero counts, without RH

Let f(z)=xi_R(1/2+iz), R_lambda=f^(5)-i lambda f^(6), lambda>0 FIXED.
For every fixed H>0,

    # {R_lambda zeros: |Re z-T|<=1, 0<=Im z<=H}
         =O_(H,lambda)(log(2+|T|)),                                (OC6)

with multiplicity. Constants and onset here are not numerically certified.

Here is a local Jensen proof, including its noncancelling anchor. By the
functional equation, write w=1/2-iz and

    f(z)=P(w)zeta(w),
    P(w)=w(w-1) pi^(-w/2) Gamma(w/2)/2.

On any fixed bounded vertical strip in z, as Re z=T->+infinity,

    |exp(pi z/4)f^(j)(z)|<=T^A,  0<=j<=6,                          (OC7)

for a constant A depending on that strip. Stirling cancels the exponential
Gamma decay exactly. The remaining zeta factor has polynomial growth on
each fixed real strip: apply Euler--Maclaurin with cutoff ceil(T), and a
fixed number M of corrections large enough that sigma+2M>1 throughout
the strip. The bounded periodic-Bernoulli remainder is at most a constant
times (1+|w|)^(2M)T^(1-sigma-2M), and the finite sum and correction terms
are polynomially bounded as well. The pole w=1 is absent for these large
heights. Cauchy's inequality on radius1 disks in a slightly enlarged strip
gives the derivative bounds in OC7. These are classical inputs; see
[DLMF5.11](https://dlmf.nist.gov/5.11) and
[DLMF25.2(iii)](https://dlmf.nist.gov/25.2#iii).

Choose z_T=T+i(H+2), so w_T=H+5/2-iT has fixed real part sigma>1.
All fixed zeta derivatives there are bounded by their absolutely convergent
Dirichlet series, and |zeta(w_T)|>=1/zeta(sigma). Put
q(w)=log(w/(2pi))/2, using the principal log. Logarithmic differentiation of
Stirling, followed by the finite product rule, gives for fixed j>=1

    xi_R^(j)(w_T)=P(w_T)q(w_T)^j[zeta(w_T)+O_(H,j)(1/log T)].

Since D_z=-i D_w, the signs and orders at the anchor are

    R_lambda(z_T)=i[lambda xi_R^(6)(w_T)-xi_R^(5)(w_T)]
      =i lambda P(w_T)q(w_T)^6 zeta(w_T)[1+O_(H,lambda)(1/log T)].   (OC8)

This is bounded away from zero for large T. In particular, for the ENTIRE
function F_lambda(z)=exp(pi z/4)R_lambda(z), Stirling gives

    |F_lambda(z_T)| >= a T^(sigma/2+3/2)(log T)^6 >0                (OC9)

with a>0 depending on H,lambda. The rectangle in OC6 lies in the disk of
radius r=H+3 about z_T. On the concentric disk of radius2r, OC7 supplies
max|F_lambda|<=T^A after enlarging A and T. Jensen bounds its inner zero
count by [log max|F_lambda|-log|F_lambda(z_T)|]/log2=O(log T).
Multiplication by the exponential creates no zeros. Finally
R_lambda(-conjugate(z))=-conjugate(R_lambda(z)) gives negative T, and
the finitely many zeros in the remaining compact rectangle absorb small T.
This proves OC6. No assertion about simple zeros, their height, or survival
of common cancellation occurs in this argument.

In particular, for any selected distinct R_lambda zeros in0<y<=1,

    1<=c_n<=q_n<=A_lambda log(2+|n|),                              (OC10)

where empty cells use c_n=q_n=1 and A_lambda is enlarged if necessary.
The earlier disk count O(R log R) alone would NOT prove this local count.

## 4. A cofinal capture criterion with no unweighted Bessel premise

Assume LB's literal inner premise for ONE fixed lambda>0:
Theta0=Gamma U and Theta5=Gamma B, with all four factors inner in C+.
Let S consist of distinct zeros b=x+iy of the actual R_lambda with0<y<=1,
|x|>=2, and with C5(b)!=0 and Theta0(b)!=0, so that they are genuine,
surviving B zeros. Define c_n from this SAME declared family S. Then:

**Theorem OC2.** If

    sum_(b in S) |Theta0(b)|^2 y/[|x|c_(floor x)] = infinity,       (OC11)

then for every D>0,

    ||Pi_[0,D] P_U P_(K_B)||_HS^2=infinity.                        (OC12)

Proof. LB3's one-node argument, with h=|x| and the fixed-lambda axis
calibration Theta0(ih)->-1, gives for every sufficiently large |x|

    ||Pi_[0,D]P_U e_b||^2
       >= |Theta0(b)|^2 y/(10|x|)-exp(-2D|x|).                    (OC13)

Divide by c_(floor x) and sum. OC6, c_n>=1, and elementary exponential
summability ensure that the total negative term is finite. The positive
term diverges by OC11. For any finite subset, OC5 and the same synthesis/
Hilbert--Schmidt argument as LB5 give

    sum ||Pi_[0,D]P_U e_b||^2/c_(floor x)
        <= C ||Pi_[0,D]P_U P_(K_B)||_HS^2.

The constant C is independent of the prefix. All operators use the same
lambda, and the weights use the chosen full family, not a claimed trace
of its nonorthogonal diagonal. Letting finite subsets exhaust S proves OC12.

Two more conservative, sufficient criteria follow:

    sum |Theta0(b)|^2 y/[|x|q_(floor x)] = infinity;
    sum |Theta0(b)|^2 y/[|x|log(2+|x|)] = infinity.                 (OC14)

The inverse-count version has automatically summable weighted exponential
tails even for an arbitrary unit-cell-finite bounded-height family, since
each cell contributes at most exp[-2D(|n|-1)]. For the finer c_n version,
do NOT discard the tail-count requirement in general: OC6 pays it for Xi.

One may also select in each cell a node maximizing |Theta0(b)|^2 y/|x|;
if the sum of these cell maxima diverges, OC11 holds for that one-per-cell
subfamily with c_n=1. This is an available input-subspace lower bound, not
an identification of the native decoder or a completeness claim.

## 5. Why the refined cost matters, and what remains open

The dispersed preregistered family has c=1 even though N grows; replacing
c by N can lose a full logarithm at Xi's expected local density. For a
heuristic pattern N(T) of order log T and heights of order1/log(T)^2,
the unpenalized weighted alignment behaves like integral dT/(T log T),
whereas the extra inverse-count penalty would make that comparison finite.
This is a motivation, NOT a proved Xi height or alignment asymptotic.

The crowded family has c=N. Its normalized Gram matrix has real entries
at least16/17 after taking real parts (its height is1/4 and its horizontal
diameter<1/64), so the all-ones Rayleigh quotient is>=16N/17. Thus the
unweighted Bessel constant genuinely need not be uniform. An infinite
synthetic example with N_n=1+floor(log2 n) crowded nodes in each cell n>=2
satisfies the Blaschke condition, has unbounded unweighted Bessel constants,
yet its c_n-weighted alignment for U=1 has divergent harmonic mass. OC2's
weighted mechanism is therefore not merely the old Bessel assumption renamed.
Here use the general inverse-count version, not any claim that these synthetic
nodes are zeros of the actual Xi companion.

Conversely, even an infinite fixed-width survey centered at2^j with O(j)
bounded-height nodes per surveyed box has
sum y/|x|=O(sum j/2^j)<infinity when |Theta0|<=1. Such a survey cannot
witness OC11, regardless of perfect alignment. This is NOT a theorem that
the survey's actual band capture is finite: the criterion is sufficient,
not necessary. Nor does it turn sampled boxes into a cofinal census.

What is paid: a local actual-Xi count, a uniform weighted sampling theorem,
an exact finite crowding algorithm, and a physical conditional implication.
What is unpaid: innerness, source-owned survival and a divergent value of
OC11 on a cofinal actual family. No new positive lower bound on that infinite
alignment sum, native outer metric, decoder, RH, or GRH is asserted.

The classical Carleson embedding, Stirling, Euler--Maclaurin, and Jensen
tools are credited. This packet's contribution is their explicit source/
metric-compatible assembly and finite crowding controls, not a new claim
to those classical theorems or a priority assertion.

## 6. Finite outcomes and replay

Both preregistered cost laws hold at every declared N=1,...,16. All17
independent subset comparisons pass; the mixed-height control has exact
cost7/4, attained at left endpoint1/8 and width1/4. All600 normalized
interval boxes satisfy the bound, all16 crowded Rayleigh lower bounds pass,
and all32 sparse-prefix/tail identities are exact. These finite statements
do not establish an infinite Xi alignment lower bound.

    python -B research/exploratory/xi_occupancy_carleson_capture.py --check
    python -B -O research/exploratory/xi_occupancy_carleson_capture.py --check
    python -B -m unittest discover -s tests -p test_xi_occupancy_carleson_capture.py

Only the standard library is required. Four exact Git/blob/LF-SHA256 sources
and the four current artifacts (note, producer, manifest, tests) are bound.
The historical analytic source files are authenticated but not executed;
mutable current-parent paths are not substituted for their frozen bytes.
The checker rebuilds the rational families, exact box costs, and every
declared finite row before comparing a fully resealed report. It does not
evaluate Xi, certify the analytic constants in OC6, or formalize the
imported Carleson embedding theorem. Arithmetic class: MIXED exact rational
and certified finite integer coverage, with no floating-point acceptance.
