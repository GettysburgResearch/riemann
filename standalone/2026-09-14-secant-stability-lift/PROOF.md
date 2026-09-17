# SSL26: charge the spectral gain and span penalty at the same rate

Status: **PROPOSED finite theorems and an input-qualified simple-zero corollary; independent review required.**
Date: 2026-09-14. Source base: `f99d9e3908dde4865377c75d9ca051c1f545bf4f`.

This is not an RH proof, another RH-equivalent criterion, or a claimed world
record. It improves the numerical consequence of the repository's existing
seven-point pressure input. The improvement over its already-recorded
280-point bound is small and explicit. The new matrix argument has no zeta
hypothesis. The zeta corollary retains the named analytic and computer-assisted
inputs; neither their formalization nor the six-gap pressure search
was rerun here.

The finite spectral envelope, stability-enhanced rank inequality and seven-point
pressure are credited to the sources in SOURCES.md. The proposed additions are
the jointly scaled pressure inequality, its trace-defect adapter, the resulting
322-point deduction, and optimality within a precisely limited affine class.
No novelty is claimed for spectral convexity, pinching, Cauchy--Schwarz, or
finite rational certification.

## 1. The retained input and the numerical conclusion

Let

    K(x) = integral_[-1/2,1/2] cos(sqrt(2)t) cos(2*pi*x*t) dt,
    k(x) = K(x)/K(0), K(0)=sqrt(2)sin(1/sqrt(2)), w(x)=k(x)^2.

Because cos(sqrt(2)t)>0 on this interval, k is the characteristic function
of a probability density. Thus [k(y_i-y_j)] is positive semidefinite (PSD)
with unit diagonal for every finite real point configuration.

**Inherited pressure input P7.** For every six nonnegative gaps,

    (sum_i g_i)/3000
      + sum_(s=1)^6 [2/(7-s)] sum_(i=1)^(7-s)
                          w(g_i+...+g_(i+s-1)) >= 19/5000.       (1)

The original ainta certificate and Reviewer A's independent reconstruction
have different traversals and trust contracts. This packet imports the
statement as retained by the latter; it does not combine their run counts.
Put k0=19/5000, sigma=1/500 and q_m=k0(m-6). Summing (1) over all length-seven
windows in m points gives

    E_m + sigma*span >= q_m,
    E_m = 2 sum_(i<j) |k(y_i-y_j)|^2.                         (2)

A separation-s pair is counted at most 7-s times and a gap at most six times.
Every omitted pair contribution is nonnegative. These facts, including the
sixfold span charge, are inherited, not new estimates.

Let H0=3/2-cot(1/sqrt(2))/sqrt(2). For m=322 define

    q=1501/1250,
    c=2sqrt(481821/402500)-1+1501/402500,
    H322=[H0-(c/q)*321/(500*322)]/[1-c/322].                 (3)

The complete finite certificate encloses

    0.673012903898232480616262080101
          < H322 <
    0.673012903898232480616262080102.                       (4)

Under P7 and the analytic interfaces stated in Section 5,

    liminf_(T->infinity) N_0^s(T,2T)/N(T,2T) >= H322.        (5)

N counts all nontrivial zeros with multiplicity; N_0^s counts SIMPLE zeros
ON THE CRITICAL LINE. No RH hypothesis enters those imported analytic
interfaces. This paper does not itself freshly establish their entire
analytic proof or its formal verification.

The already-recorded 280-point consequence is
0.673009652279136912013711991616..., not merely the older 269-point value.
The difference in fractions is 0.00000325161909556860255008848...;
in percentage points it is 0.0003251619095568602550088485....
This is not a change of that many percentage units or a large movement
of the remaining 32.7 percent. Strictly weaker rounded claims such as
H322>0.6730129 are safe.

## 2. SSL26-1: a sharp secant pressure inequality

For t>=0 define the convex nonnegative function

    Psi(t)=(t-1)^2,             0<=t<=2,
           2t-3,              t>=2.

For PSD G of order m>=2 and trace m put

    Delta(G)=tr Psi(G), E(G)=tr(G-I)^2.

For 0<q<2 set

    c_m(q)=q,                                  q<=m/(m-1),
           2sqrt((m-1)q/m)-1+q/m,              q>m/(m-1).    (6)

**Theorem.** If z>=0 and E(G)+z>=q, then

    Delta(G) >= c_m(q)*(1-z/q)_+.                          (7)

In particular

    Delta(G)+(c_m(q)/q)z >= c_m(q).                        (8)

Here positive part is applied to the scalar 1-z/q, not to a signed
arithmetic quantity. The trace-m premise is essential and is repaired for
actual norm-bounded Gram matrices in Section 3.

### Proof of the spectral envelope, with its original scope retained

Write x_i=lambda_i(G)-1. Then x_i>=-1, sum x_i=0 and sum x_i^2=E.
For 0<=E<2, at most one x_i is greater than one. If no such x_i exists,
Delta=E. If a=x_i>1, Cauchy--Schwarz applied to the other m-1 coordinates gives

    a^2 <= (m-1)E/m,
    Delta=E-(a-1)^2 >= 2sqrt((m-1)E/m)-1+E/m.              (9)

For E<=m/(m-1), the same Cauchy bound prohibits a>1 and Delta=E.
This reproduces the envelope phi_m(E) already in Reviewer A, S02.
On its nontrivial branch,

    d/dE [phi_m(E)/E] = [1-sqrt((m-1)E/m)]/E^2 <=0.       (10)

Below that branch the ratio is one. Thus, whenever E<=q,

    Delta(G) >= [c_m(q)/q] E.                            (11)

There is no assumption E<2 on the theorem's input G. If E>=q, let
G'=I+sqrt(q/E)(G-I). This is a convex combination of I and G, hence PSD,
with trace m and E(G')=q. Scalar convexity about the minimum at one implies
Delta(G')<=sqrt(q/E)Delta(G), and the envelope at q gives
Delta(G)>=c_m(q). Combining this with (11), and with E>=q-z when z<q,
proves (7). For z>=q, nonnegativity suffices. QED.

### Why the secant, not a tangent

The branch phi_m is concave, so its tangent is an UPPER estimate and cannot
be used here as a lower supporting line. Its ratio to E decreases, which
justifies exactly the secant in (11). Retaining the old unit span charge
would give only Delta+z>=c_m(q). Formula (8) improves that charge to
c_m(q)/q<=1 at the same intercept.

### Sharpness within the trace/pressure relaxation

The matrix

    G_q=(1-t)I+t*11*, t=sqrt(q/[m(m-1)])

has eigenvalues 1+a,1-a/(m-1),...,1-a/(m-1), where
 a=sqrt((m-1)q/m). It has E=q and Delta=c_m(q) for 0<q<2.
Thus equality in (8) occurs at (G_q,z=0). At the other endpoint,
G=I,z=q also gives equality. Any affine inequality

    Delta(G)+eta*z >= u                                  (12)

valid under ONLY PSD, trace m, z>=0, E+z>=q must have

    eta>=0, u<=eta*q, u<=c_m(q).                          (13)

The first follows by sending z to infinity with G=I; the latter two follow
from the displayed endpoints. For the full intercept c_m(q), the span
coefficient in (8) cannot be reduced.

These extremizers are abstract correlation matrices. They are NOT asserted
to equal a Montgomery--Taylor kernel Gram at a configuration with the tested
span. Thus this is not a ceiling on all geometric improvements of (1).

## 3. SSL26-2: trace defects and finite kernel errors are paid explicitly

Let G be PSD of order m with G_ii<=1. Define

    d=m-tr G >=0, E_off=sum_(i!=j)|G_ij|^2.

If z>=0, epsilon>=0 and E_off+z+epsilon>=q with 0<q<2, then

    Delta(G) >= c_m(q)-[c_m(q)/q](z+epsilon)-2d.           (14)

Proof: add D=diag(1-G_ii). Then Gbar=G+D is PSD, has unit diagonal,
E(Gbar)=E_off, and tr D=d. Psi is globally 2-Lipschitz. Weyl monotonicity
for a PSD perturbation gives ordered eigenvalues lambda_i(Gbar)>=lambda_i(G);
therefore

    |Delta(Gbar)-Delta(G)| <=2 sum_i[lambda_i(Gbar)-lambda_i(G)]=2d.

Apply (8) to Gbar with z+epsilon. This proves (14).

In particular, if G comes from vectors of norm at most one and
|G_ij-k(y_i-y_j)|<=epsilon0, then both overlaps have absolute value <=1,
so their squared absolute values differ by at most 2epsilon0. The ordered
energy discrepancy is at most 2m(m-1)epsilon0. This is an admissible epsilon
in (14). Diagonal convergence also makes d=o(1) at every fixed block size.
An entrywise matrix inequality is not used to infer a Loewner inequality.

## 4. SSL26-3: finite offset averaging

Assume P7. Let G=[k(y_i-y_j)] for S>=m ordered points, total span L. With
q=q_m<2 and c=c_m(q),

    Delta(G) >= (c/m)(S-m+1)
                  -(c/q)*sigma*(m-1)L/m.                (15)

For each of the m offsets, take disjoint consecutive full m-point blocks,
leaving their endpoint remainders. Convexity and unitary invariance of
tr Psi imply trace pinching cannot increase it. Since Psi>=0, the full
defect is at least the sum of full-block defects for that offset.
Across ALL offsets every length-m consecutive window occurs once: there
are exactly S-m+1 such windows. Any individual gap occurs in at most m-1
window spans. Apply (8) and (2), sum over these windows and divide by m.
This proves (15). Empty/short configurations can be handled separately;
no fictitious full blocks are inserted.

For the actual finite Gabor Gram, use (14) at blocks of span <q/sigma.
This is ONE fixed separation interval since m is fixed. On blocks of larger
span, the right side of (8) after solving for Delta is nonpositive, so
Delta>=0 is enough and no far-separation approximation is requested.
A uniform o(1) error on every short-span block, summed over O(N) blocks,
is o(N). This is the bounded-separation repair required in the prior review.
No uniform approximation at unbounded separations is assumed.

## 5. SSL26-4: the input-qualified zeta deduction

The imported analytic interface consists of the following specific statements.
They are recorded in ainta's paper and Reviewer A's S02, with the original
trace estimates coming from Claude, communicated by Alpoge and Furman.

(A1) There is a PSD Gram M_T of retained central simple critical-line zeros,
with norm-bounded columns, whose count is S_T=N_0^s(T,2T)-o(N_T). Their
normalized total span is at most N_T+o(N_T), N_T=N(T,2T).

(A2) Diagonal entries converge uniformly to one and overlaps converge
uniformly to k of normalized separation on EVERY FIXED compact separation
interval. Deleting the end strips costs o(N_T) points.

(A3) The trace, mean-square and tail calculation together with the
stability-enhanced rank inequality gives

    N_0^s(T,2T) >= H0*N_T+Delta(M_T)-o(N_T).              (16)

For transparency, the relevant finite stability inequality is

    ||P+Q||_F^2 >=4tr(P+Q)-3r-4b+tr Psi(V*V),            (17)

where P=VV*, the r columns of V have norm<=1, Q is Hermitian and n_+(Q)<=b.
This inequality is already in ainta's source; it is NOT new in this pass.
Write Q=Q_+-Q_- with orthogonal positive and negative parts. Dropping the
nonnegative cross term tr(PQ_+), using q^2>=4q-4 on each positive eigenvalue
of Q, and using von Neumann's trace inequality on P,Q_-, reduces to

    min_(n>=0)[(p-n)^2+4n]=2p-1+Psi(p), p>=0.

Sum over the r Gram eigenvalues, pad zeros if required, and use tr P<=r.
This proves (17). The zeta decomposition has b<=s_2+p where s_2 counts distinct
multiple central zeros and p counts off-line pairs. Since N(I')>=r+2s_2+2p,
(17) gives S>=4tr Ahat-||Ahat||_F^2-2N(I')+Delta. The imported trace and
mean-square limits, and their tail comparison, give (16).

In the original setup L=log(T/(2pi)), spacing h=2pi/L and
x_rho=(gamma_rho-T)/h. The full-grid Poisson identity normalizes columns to
norm<=1. Its normalized overlap is Phi(hx)/(aL), tending to k(x) after
the taper rescaling. The finite grid loses O(L^-2) away from normalized
endpoint strips of width L^2. Unit-interval zero counts make those strips
contain O(L^2)=o(N_T) zeros. The source's Section 7.1 gives the optimized
trace and mean-square inputs with O(log L/L) relative error. These inputs
are not supplied by our scalar numerical checker.

Combining (14)--(16) gives

    Delta(M_T) >= (c/m)S_T
                   -(c/q)*sigma*(m-1)N_T/m-o(N_T),

and hence, provided 1-c/m>0,

    liminf S_T/N_T >=
         [H0-(c/q)*sigma*(m-1)/m]/[1-c/m].               (18)

At m=322, q,c give (3)--(5). The rounding certificate uses no zeta values.
RH is not an assumption in (A1)--(A3), but their imported-proof status is
part of this corollary's assurance. No full analytic or Lean replay is claimed.

## 6. SSL26-5: a stopping rule for the affine block-size search

Consider the precisely restricted class of deductions that, for each fixed
m>=7, use ONLY PSD/trace m and E+z>=q_m to assert an affine inequality (12),
then apply the same offset averaging and (16). Fixed finite convex mixtures of
those deductions are allowed. Improved P7, information about actual kernel
extremizers, non-affine aggregation and adaptive partitions are NOT in this
class. There is no assertion of a ceiling for all simple-zero methods.

For all m>=7, including q_m>=2, the same equicorrelation witness is feasible:
q_m<=m(m-1). Its actual cost is

    c_eq(m)=q_m                         q_m<=m/(m-1),
             2sqrt((m-1)q_m/m)-1+q_m/m otherwise.         (19)

For q_m>=2, (19) is an UPPER bound on any affine intercept u (a witness),
NOT a claimed lower spectral envelope. This distinction is used by the code.
The witnesses in Section 2 force eta>=u/q_m and u<=c_eq(m). Taking u>=0
loses no improvement, since u<0 and eta>=0 cannot beat H0.
The scalar conclusion of such a deduction is at most

    max(H0,H_m),
    H_m=[H0-(c_eq(m)/q_m)*sigma*(m-1)/m]/[1-c_eq(m)/m].   (20)

Indeed with eta=u/q_m the quotient is fractional-linear and its derivative
in u has a constant sign. If positive it is maximized at c_eq; if negative
the best is u=0. Increasing eta only worsens the quotient. All denominators
are positive: c_eq/m<=max(k0,2sqrt(k0/m))<1.

The exact checker compares (20) for EVERY integer m=7,...,1999. Its unique
largest value occurs at m=322. The next largest, at321, is smaller by more
than 5.68*10^-10 in fractional proportion. The winner has q_m<2, so the
upper bound is genuinely attained by the proved secant deduction.

The remaining infinite tail is analytic. For m>=2000,

    c_eq(m)/q_m <=2/sqrt(q_m)+1/m <=3/4.                 (21)

The second assertion follows at2000 by squaring positive rational sides,
and both terms decrease thereafter. Let t=c_eq(m)/q_m. An exact rearrangement is

    H_m-H0 =
      t*[(k0*H0-sigma)+(-6k0*H0+sigma)/m]
            /[1-t*k0*(1-6/m)].                         (22)

The term -6k0H0+sigma is negative. If the numerator is negative, H_m<H0.
Otherwise its numerator is at most t(k0H0-sigma) and its denominator is
at least 1-t*k0. This gives for every m>=2000

    H_m <= H0+[(3/4)(k0H0-sigma)]/[1-(3/4)k0]
             <0.672918521465589 <H322.                  (23)

Both sign tests and (23) are certified with rational enclosures of H0.
Fixed finite convex mixtures cannot improve the maximum: writing each conclusion
as S>=(H0-b_i)N+a_i S, an upper value H bounds each H0-b_i by H(1-a_i),
and multiplication by nonnegative weights summing to one preserves that
inequality. This proves the stated restricted global optimum.

Thus tuning the block size further, or mixing fixed sizes using only this
same relaxation, has no remaining numerical payoff. The next larger gain
must use actual kernel geometry, stronger local pressure, different trace
information, or a different deduction. This is a stopping rule, not another
open RH-equivalent condition.

## 7. Evidence and limitations

Theorems (7), (14), (15) have written all-matrix/configuration proofs. The
finite certificate checks their scalar specializations and complete search
for (20), not all PSD matrices by enumeration. The combinatorial all-size
and analytic tail arguments, not finite extrapolation, handle unbounded sizes.

The checker authenticates no external seven-point transcript, Gabor data,
actual zeros or analytic input. It evaluates H0 by alternating rational
cos/sinc series, radicals by squared 200-bit integer enclosures, the
finite spectral corpus by exact algebra, and the entire m>=2000 remainder
by (21)--(23). Same-author normal/optimized execution is not independent
mathematical acceptance. Complete review priorities are in README.md.
