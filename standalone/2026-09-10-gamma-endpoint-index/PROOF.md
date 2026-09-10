# Endpoint spectra and a finite exceptional index for the centered gamma cascade

Date: 2026-09-10. Status: **PROPOSED COMPONENT PROOFS; independent review required.**
RH and cofinal confinement of the exceptional zeros remain OPEN. This is a
research continuation of #855 at `0e19b74fe6dfb39bef69a5edd3f0b3098b10a6ad`,
not a change to its statements, the integration candidate, or accepted status.
Local GE labels are not canonical claim identifiers.

The positive result is global zero geometry at each *fixed* integer stage:
there are only finitely many nonreal zeros, and every sufficiently large zero
is real and simple, with an explicit two-term location formula. A finite-index
power-sum form isolates exactly the distinct exceptional quartets. The numerical
result tests the stronger proposed shortcut: the centered integer N=5 has a
nonreal zero inside the xi critical band. Thus neither global real-rootedness
nor critical-band real-rootedness at *every* centered integer stage is available.
The source-specific problem is eventual escape or collapse of the finite
exceptional part, not its omission.

Endpoint Watson asymptotics, Hadamard factorization, polynomial interpolation,
and finite negative-index forms are classical mechanisms. The arguments needed
here are supplied, including the actual source's analytic endpoint factor and
both complex sectors. No external novelty or priority claim is made.

## 1. The unchanged source and the distinction between two limits

Let G_n be independent gamma variables of shape two and rate one. Write

    X_N = sum_(n=1)^N G_n/n^2,
    tau_N = 2 sum_(n>N) n^-2 = pi^2/3 - 2 sum_(n<=N) n^-2.

Let f_N be the density of X_N on (0,infinity). Put tau=tau_N,

    L = (1/2) log(pi/tau),
    x(t)=pi exp(2t), y(t)=pi exp(-2t),
    h_N(t) = sqrt(f_N(x(t)-tau) f_N(y(t)-tau)) for |t|<L,
             0 otherwise,
    Z_N=integral_-L^L h_N(t)dt >0,
    F_N(z)=Z_N^-1 integral_-L^L h_N(t)exp(izt)dt.       (1)

Throughout this manuscript F_N denotes the *mean-centered reciprocal family*,
called Fhat_N in #855, not its raw family. The positive square root is taken
on the real integration interval. We will justify, rather than presume, the
complex analytic continuation required for endpoint contours.

The elementary bounds 0<tau<=4/3<pi give L>0. The exact infinite gamma/xi
identification is the classical Biane--Pitman--Yor source, with the conventions
reconstructed in #849 and #855. The proposed #855 whole-source theorem gives

    F_N -> Phi=Xi/Xi(0) locally uniformly in C, and
    sup_(|Im z|<=R) |F_N^(j)(z)-Phi^(j)(z)|=O_(R,j)(N^-3). (2)

Only local uniform convergence is used in the final RH-facing implication.
Its proof is inherited at the exact parent source, not newly accepted by this
continuation. The fixed-N results below do not need (2), a zero table, or RH.

There are two different limits: |z|->infinity at FIXED N in GE2, and N->infinity
at fixed or growing z in (2). Their interchange is not asserted.

## 2. GE1: a positive simplex law exposes the endpoint factor exactly

Set m=2N, p=m-1, beta=p/2=N-1/2, alpha=beta+1=N+1/2, and

    c_N=(N!)^4/(2N-1)!.

Let U be uniform probability on the (m-1)-simplex, and let the list lambda
contain two copies of 1^2,...,N^2. Then

    R_N^simplex=sum lambda_j U_j in [1,N^2],
    ell_N(w)=E exp(-w R_N^simplex),
    f_N(w)=c_N w^p ell_N(w),                            (3)

the last equality being the entire extension of the finite density. The
superscript prevents confusion between this auxiliary simplex variable and
the omitted infinite gamma tail in the parent.

**Proof.** A shape-two gamma is the sum of two rate-one exponentials. The joint
density of the m scaled exponentials is product(lambda_j) exp(-sum lambda_j v_j).
Change variables to their sum w and their simplex proportions; the simplex
volume is 1/(m-1)!. This proves (3) for w>0, and both sides are entire. In
particular ell_N(0)=1 and

    ell_N'(0)=-barlambda_N,
    barlambda_N=(N+1)(2N+1)/6.                          (4)

For N>=2, ell_N is zero-free on |Im w|<pi/(N^2-1). Indeed, multiplying by
exp((N^2+1)w/2) expresses its real part as a positive integral times
cos((R_N^simplex-(N^2+1)/2)Im w), which is strictly positive on this strip.
This holds for every Re w, not just the density half-line. At N=1 ell_1=e^-w
is zero-free everywhere. QED.

Let S(w)=sinh(w)/w, with S(0)=1. Direct multiplication gives

    (x(t)-tau)(y(t)-tau)
      =4 pi tau sinh(L+t)sinh(L-t)
      =(L^2-t^2) 4 pi tau S(L+t)S(L-t).                (5)

Consequently there is an even, real, strictly positive analytic factor A_N
on a complex neighborhood of [-L,L], including both endpoints, such that

    h_N(t)=(L^2-t^2)^beta A_N(t),  |t|<L,              (6)

with the following source formula:

    A_N(t)=c_N (4pi tau)^beta [S(L+t)S(L-t)]^beta
             sqrt(ell_N(x(t)-tau) ell_N(y(t)-tau)).    (7)

### A declared complex domain for (7)

For example take

    d_N=min(1/16, 1/[16(N^2+1) exp(2(L+1))]).

On the open rectangle |Re t|<L+d_N, |Im t|<d_N, the two S factors have no
zeros, since the nonzero zeros of sinh lie at imaginary multiples of pi.
Furthermore

    (N^2-1)|Im(pi exp(+-2t)-tau)|
      <=2pi (N^2-1) exp(2(L+d_N))d_N < pi.

Thus both ell factors are nonzero by (3). The rectangle is simply connected.
Choose analytic logarithms agreeing with positive real values on the real
segment, and define the powers and square root in (7) through these logarithms.
Uniqueness makes A_N even and real under conjugation. This does NOT extend
the positive probability density itself beyond its support. It extends its
nonvanishing endpoint factor; the fractional endpoint powers remain explicit.

### The first two endpoint coefficients are computable from the same source

Put

    X_0=pi^2/tau, a=X_0-tau,
    a_N=sqrt(c_N (2tau)^p f_N(a)) >0,
    b_N=beta-tau barlambda_N-X_0 f_N'(a)/f_N(a).        (8)

Then, as r->0 from the right, and also in the local complex branches,

    h_N(L-r)=a_N r^beta [1+b_N r+O_N(r^2)].            (9)

To check the signs, x(L-r)-tau=a-2X_0r+O(r^2), whereas
 y(L-r)-tau=2tau r(1+r+O(r^2)). Use (3),(4) and take one half of the two
logarithmic derivatives. Evenness gives the identical coefficient at -L.

No numerical root defines A_N, a_N, b_N, or d_N. A lower bound for the leading
coefficient is also elementary. If V=sum_(n=2)^N G_n/n^2, then E V<4/3 and
 a>65/12>4E V. Convolving the first gamma gives

    f_N(a)=e^-a E[(a-V)e^V; V<a] >=(a/4)e^-a.         (10)

This includes N=1, where V=0. Thus all constants in the endpoint argument
can in principle be bounded by declared finite, positive quantities. This
packet does not instantiate a numerical exterior threshold for any N.

## 3. GE2: every sufficiently large zero is real and simple

**Theorem.** For EACH integer N>=1 there are finite K_N,C_N,R_N such that:

1. Every zero of F_N with |z|>R_N is real and simple.
2. On the positive real axis these zeros have exactly one member in each
   sufficiently late disk about

       zeta_(N,k)=pi(k+N/2+3/4)/L,  k>=K_N,

   and there are no other large zeros. More precisely,

       z_(N,k)=zeta_(N,k)
                 +alpha b_N/[L zeta_(N,k)] + O_N(zeta_(N,k)^-2). (11)

3. The number of positive real zeros up to T is LT/pi+O_N(1). The transform
   has order one and exponential type L, and its nonreal zero set is finite.

All constants, the first k, and the threshold R_N may depend on N. No
practical or N-uniform exterior radius is claimed. The disks used in the
proof shrink with k and contain one simple zero *in the complex plane*;
reality follows from this count and conjugation, not from sign sampling.

### 3.1 A general endpoint lemma, with both sectors retained

The following argument applies to h(t)=(L^2-t^2)^beta A(t), beta>-1, with
A even, real, analytic on a neighborhood of [-L,L], and A(L)>0. Write (9)
with constants a>0,b and alpha=beta+1. Let H(z)=integral_-L^L h(t)e^(izt)dt.
For x=Re z>0, |Im z|<=x, uniformly as |z|->infinity,

    H(z)=2a Gamma(alpha) z^-alpha
          { cos(theta)+alpha b z^-1 sin(theta)
                         +O(e^(L|Im z|)|z|^-2) },
    theta=Lz-pi alpha/2.                              (12)

The power z^-alpha uses its analytic principal branch in this sector. It is
not a new singularity of the entire H.

Here is a proof of the uniformity needed for zero counting. Move the segment
[-L,L] upward to height eta>0 inside the analytic neighborhood, using the
endpoint branches continuous from the interior. Tiny endpoint arcs vanish
because beta>-1. If Top is the shifted horizontal integral, Cauchy's theorem
with its actual orientations gives

    H(z)=Top
          +i e^(-iLz) integral_0^eta h(-L+is)e^(-zs)ds
          -i e^( iLz) integral_0^eta h( L+is)e^(-zs)ds. (13)

The top is bounded by a constant times exp(L|Im z|-eta Re z). Locally,
 h(-L+is)=a(is)^beta(1+ibs+O(s^2)) and
 h( L+is)=a(-is)^beta(1-ibs+O(s^2)).
Extend the first two monomial integrals to infinity. Their errors and the
remaining endpoint portions are exponentially small. The quadratic remainder
is bounded by a constant times

    integral_0^infinity s^(beta+2)e^(-x s)ds
        =Gamma(alpha+2)x^(-alpha-2).

Since x>=|z|/sqrt(2), this is the error in (12), uniformly throughout the
sector. Both endpoints contribute; dropping one would destroy the cosine.
The finite-height cutoff errors are absorbed into the same bound for large x.
This is the elementary contour proof of the applicable Watson expansion
(DLMF 2.4(i)); it does not assume zero confinement.

The remaining sector is different. For y=Im z>=x>=0 set w=-iz=y-ix. Then

    H(z)=e^(-iLz) integral_0^(2L) h(-L+r)e^(-wr)dr.

Now Re w>=|w|/sqrt(2). The *left* endpoint dominates, and the same integral
bounds give

    H(z)=e^(-iLz) a Gamma(alpha) (-iz)^-alpha
                  [1+alpha b/(-iz)+O(|z|^-2)].        (14)

The part r>=eta is exponentially small relative to the displayed leading
factor. Thus (14) is nonzero at all sufficiently large z in this sector.
Conjugation and evenness cover the other sectors. No unexamined nearly
vertical direction is hidden in a real-axis asymptotic.

### 3.2 Why the large zeros are real, not merely close to real

In the first sector,

    |cos(theta)|^2=cos^2(Re theta)+sinh^2(L Im z).

For |Im z|>=1 this has a positive lower bound proportional to e^(2L|Im z|).
The O(1/|z|) relative perturbation in (12) therefore excludes all sufficiently
large such zeros. In the remaining horizontal strip, an elementary bound for
sine near its separated simple zeros shows that any zero must lie within
C/|z| of a real cosine zero

    zeta_k=pi(k+alpha/2+1/2)/L.

Choose disks of radius D/zeta_k with D sufficiently large and then k
sufficiently large. On each boundary the leading cosine strictly dominates
the correction in (12); Rouché gives EXACTLY ONE zero, counted with
multiplicity, in that disk. The disk is fixed by conjugation, so its unique
zero is real and simple. Away from those disks the same lower bound excludes
other zeros. This proves the first two claims. Substituting
z=zeta_k+Delta into (12), with Delta=O(1/zeta_k), gives
 L Delta=alpha b/zeta_k+O(zeta_k^-2), proving (11).

Counting the late separated disks proves the real zero density. Directly,
|F_N(z)|<=exp(L|Im z|), while (14) on the imaginary axis gives
log F_N(iy)=Ly-alpha log y+O_N(1). Hence order and type are exactly as stated.
A compact disk contains finitely many zeros of a nonzero entire function.
This proves GE2. QED.

### 3.3 An explicit way to bound the omitted constants, not an executed threshold

Choose eta<d_N/4. On the fixed compact rectangle, (3),(7) give finite bounds
for A_N and its first two endpoint Taylor remainders. For example
|ell_N(w)|<=exp(N^2 max(0,-Re w)), and
|S(w)|<=exp(|Re w|) via its integral representation. Cauchy on a slightly
larger rectangle bounds the derivatives. Equation (10) bounds a_N away from
zero. The errors in (13),(14) then use only gamma integrals and exponential
bounds. These yield an explicit, possibly enormous radius by increasing an
integer until all stated strict inequalities hold.

This describes a constructive majorant procedure; no numerical R_N,
optimal threshold, or complete bounded-region zero census was executed here.
The finite region may be much larger than any feasible computation.

## 4. The high-frequency approximation is necessarily nonuniform in N

The leading correction coefficient in (11) itself grows. In the actual source,

    b_N = (pi^2/2+1/3)N+O(1),
    alpha b_N = (pi^2/2+1/3)N^2+O(N),                 (15)
    lim_(N->infinity) log(a_N)/N=log 2-1-pi^2/4 <0.   (16)

**Proof.** Integral comparison, or one elementary Euler summation step, gives
 tau=2/N+O(N^-2) and X_0=(pi^2/2)N+O(1). The partial fractions of the finite
gamma density are

    f_N(x)=sum_(n=1)^N (A_(n,N)x+B_(n,N))e^(-n^2x),
    A_(n,N)=n^4 [2(N!)^2/((N-n)!(N+n)!)]^2.

The polynomial constant of the first term is
c_(1,N)=-2 sum_(n=2)^N 1/(n^2-1)=-3/2+1/N+1/(N+1),
so its contribution is A_(1,N)(x+c_(1,N))e^-x.
The factorial ratio is at most one, so A_(n,N)<=4n^4. Also
|c_(n,N)|<=2 sum_(j!=n)1/|j^2-n^2|<=4: the j<n part is bounded by
H_(n-1)/n<=1 and the j>n part by H_(2n)/(2n)<=1. Hence
|B_(n,N)|<=16n^4. At x=a=X_0-tau, the sum of n>=2 terms and its derivative is
O((x+1)e^-4x), uniformly in N. Therefore

    f_N'(a)/f_N(a)=-1+1/(a+c_(1,N))+O(e^-3a),
    log f_N(a)=-a+O(log N).

Insert this and barlambda_N=(N+1)(2N+1)/6 in (8). It proves (15).
Finally log c_N=2N log N-2N log2-2N+O(log N) by Stirling, and
 (2N-1)log(2tau)=2N(log4-log N)+O(log N).
Together with log f_N(a)=-(pi^2/2)N+O(log N), (8) gives (16). QED.

In particular, the phase correction in (12) is not O(1/|z|) with an
N-independent coefficient. Statements such as "take the fixed-N real tail
and then let N grow" discard a coefficient of order N^2, as well as the
N-dependent analytic neighborhood. Neither (15) nor (16) is asserted to be
an optimal location for the transition from bulk zeros to endpoint zeros.

## 5. GE3: the unresolved part is a finite polynomial and a finite negative index

There are no pure imaginary zeros: F_N(iy) is an integral of a strictly
positive density times cosh(yt), divided by a positive normalizer. Also
F_N(0)=1. Every nonreal zero therefore belongs to a quartet
 {z,-z,conjugate(z),-conjugate(z)}, with Re z>0, Im z>0 representative.

By GE2 there are finitely many such quartets. Let them be z_j, with analytic
multiplicities m_j. Define the real even polynomial

    P_N(z)=product_j [(1-z^2/z_j^2)(1-z^2/conjugate(z_j)^2)]^m_j. (17)

It is positive on the real axis and equals one at zero. Then

    F_N(z)=P_N(z) G_N(z),                              (18)

where G_N is a real even entire function in the Laguerre--Pólya class, with
G_N(0)=1. All its zeros are real; sufficiently large ones are simple.

This is an EXACT EXISTENCE/CLASSIFICATION statement, not a new operator
constructed without zeros and not an algorithm already computing P_N.
Indeed after dividing out the finite polynomial, Hadamard factorization
applied in the squared variable (order 1/2) gives

    G_N(z)=product_(positive real zeros r) (1-z^2/r^2)^mult(r).

The product converges locally uniformly, since (11) gives sum mult(r)/r^2
finite. It is a limit of real-rooted polynomials, proving the asserted class.
There is no unspecified exponential factor; evenness and order exclude one.

### The exact index can also be read from the source moments

Let lambda_j=z_j^-2 now range over ALL distinct squared-zero nodes, taking
one representative of each +/- pair, and let m_j be its multiplicity. The
real nodes are positive, and sum m_j |lambda_j| is finite. Set

    s_(N,k)=sum_j m_j lambda_j^k,
    H_(N,d)=(s_(N,i+j+2))_(i,j=0)^d.                  (19)

These are real symmetric matrices. They can equivalently be defined from
the Taylor coefficients of -log F_N(sqrt(v)) at v=0, without locating zeros.

**Finite-index theorem.** If q_N is the number of DISTINCT nonreal quartets,
then

    ind_-(H_(N,d)) <= q_N for every d,
    ind_-(H_(N,d)) = q_N for every sufficiently large d. (20)

Multiplicity weights remain in the formula but do not each count as a
separate negative direction. This is not a statement that a fixed small
matrix already determines the index or that q_N is bounded uniformly in N.

**Proof, including the infinite positive tail.** For a real polynomial p,
its form is sum m_j (lambda_j p(lambda_j))^2. Real nodes contribute
nonnegative values. Each conjugate nonreal pair contributes
2m Re(u^2)=2m[(Re u)^2-(Im u)^2], with negative index one. This proves the
upper bound.

For the lower bound choose 0<r<min{|lambda|:lambda nonreal}. Include all
nonreal nodes and all real nodes >=r in a finite interpolation set. Let
L_j be the complex Lagrange polynomial which is one at a chosen upper
nonreal node lambda_j and zero at every other node in this set. For integer
k>=1 define the REAL polynomial

    u_(j,k)(t)=i(t/lambda_j)^k L_j(t)
                 -i(t/conjugate(lambda_j))^k conjugate(L_j(conjugate(t))).

It is divisible by t, so it equals t p_(j,k)(t). Its values at the selected
pair are i,-i; all other selected nodes vanish. For every real 0<=t<r,

    |u_(j,k)(t)| <= C_j t (r/|lambda_j|)^(k-1).

The omitted real contribution is bounded by a fixed multiple of
sum_(real nodes<r) m_j lambda_j^2, which is finite, times a decaying geometric
factor. Thus the Gram on the q_N polynomials p_(j,k) converges to the
negative diagonal diag(-2m_j). It is negative definite for sufficiently
large k, giving q_N independent negative directions at some finite degree.
Monotonicity of the negative index under extending a principal matrix then
proves (20). No finite zero truncation substitutes for the last tail estimate.
QED.

The determinant of an actual theta operator is not imported here. This is a
classical finite-defect power-sum argument for the exact centered transforms.
It is compatible with, but different from, the all-rank questions in #839/#841.
Their recent descriptions were read only for orientation in this pass.

## 6. GE4: the centered INTEGER N=5 already has a critical-band exception

The defining-integral certificate in CERTIFICATE.md establishes exactly one
simple zero in the disk of radius 10^-12 about the exact terminating point

    31.0835163803300613860836804713778137956057544691
       +0.2347791171837078741080118319340221394471947526 i. (21)

The disk lies in 0<Im z<1/2 and Re z>0. The law is precisely

    X_5 + tau_5, tau_5=pi^2/3-2 sum_(n=1)^5 n^-2,

followed by (1). It is not the previous raw N=4 or intermediate raw law.
Conjugation and evenness give its other three simple zeros. In particular,
q_5>=1, and a finite Hankel negative direction exists by (20). This pass does
not compute its first detecting degree, a complete q_5, or every zero in a box.

The certificate uses a dyadic interval partition approaching the compact
support edge, full Taylor remainders, both density factors and a bound for the
entire remaining endpoint interval. It does not approximate tau by a floating
number or integrate past the support using an arbitrary square-root branch.
Normal and optimized runs are the same directed arithmetic implementation.

**This is not a zero of xi or a counterexample to RH.** It rejects the stronger
attempt to close the parent by demanding real zeros at *every centered stage*.
The all-N exterior theorem and the N=5 local defect are consistent.

## 7. The remaining ambitious target is now a finite exceptional divisor

Define the critical-band exceptional measure from (17), retaining
multiplicities, but only for |Im z_j|<=1. A sufficient theorem is that, on one
cofinal sequence N_l, its support either goes to unbounded |Re z| or collapses
toward Im z=0. Precisely, for some T_l->infinity and epsilon_l->0 there are no
quartets with |Re z|<=T_l and epsilon_l<|Im z|<=1.

By (2), any fixed nonreal xi zero has an off-real disk on which Rouché forces
approximant zeros with the same multiplicity for all sufficiently large N.
The proposed exceptional-divisor escape/collapse would forbid them. Hence
that SOURCE-SPECIFIC statement would give RH. It is not established here.

What GE2 changes is that the source has no unknown *infinite nonreal tail*
at a fixed stage: its entire nonreal part is a polynomial. What it does not
change is the lack of uniform N control. A finite exceptional set can persist
in a convergent sequence. Exact convergence, small error, or finite negative
index alone cannot rule that out. Also, imposing q_N=0 along a subsequence
would be stronger than necessary and could mishandle splitting near multiple
real limiting zeros; escape/collapse retains that distinction.

The next concrete analytic task is an N-dependent bound on this exceptional
part derived from the ordered squared rates and exact gamma convolution,
not from generic analytic endpoints. Computationally, one can certify a
bounded region and an exterior majorant at the SAME stage, then follow only
its finite exceptional part. Neither a global census nor such a uniform
exceptional-divisor bound was performed in this pass. The N=5 counterexample
must remain a required regression for any proposed blanket preservation rule.

## 8. Sources and review priority

[P1] #855, `0e19b74fe6dfb39bef69a5edd3f0b3098b10a6ad`,
`standalone/2026-09-10-centered-gamma-continuation/PROOF.md`, blob
`48dae66b76c92dccdd7d18fae61c6a5e23802569`. The full manuscript was read.
The family and proposed full-source convergence are inherited; this paper
independently proves the fixed-N endpoint geometry. The interval module is
copied unchanged, blob `36d6341b574fe5a512196bfa0d66fbae897365a6`.

[P2] #849, `11a12b8ceb7db98c7961a5cebf3870b2f31dfa79`,
`standalone/2026-09-10-reciprocal-gamma-cascade/PROPOSAL.md`, blob
`c324ba15d3f7f3e073b902042ec61c685b555f53`. Finite-density source, BPY scaling
and coefficient bounds. Its optional scout was inspected, not treated as a
certificate. The new reconnaissance is also separate from acceptance.

[E1] Biane--Pitman--Yor, Probability laws related to the Jacobi theta and
Riemann zeta functions, and Brownian excursions, Bull. AMS 38 (2001), 435--465,
https://arxiv.org/abs/math/9912170 . The gamma/xi source is a classical import
through P1/P2. It is not required to prove GE1--GE4 about finite gamma laws.
No new review of the complete external article is claimed.

[E2] NIST DLMF 2.4(i), https://dlmf.nist.gov/2.4#i and 2.3,
https://dlmf.nist.gov/2.3 . Classical endpoint Watson expansion and sector
uniformity. Those pages were read. Section 3 gives the contours and error
bounds used here; citing real-axis asymptotics alone would be insufficient.
DLMF 10.21, https://dlmf.nist.gov/10.21, provides the familiar comparison with
Bessel zero phases; no Bessel zero location is a primitive of our certificate.

[E3] Classical Hadamard genus-zero factorization in the squared variable,
Rouché's theorem, Stirling asymptotics, and polynomial interpolation. The
finite negative-index/tail argument is provided in full; no priority claim.

Review: check the simplex zero-free strip and chosen complex rectangle;
endpoint powers and phases; both large-z sectors; uniqueness versus mere
proximity of zeros; fixed-N versus N-uniform quantifiers; multiplicity in
(17)--(20); and every compact-support endpoint and branch budget of (21).
No source/claim status is promoted by an accepting computation.
