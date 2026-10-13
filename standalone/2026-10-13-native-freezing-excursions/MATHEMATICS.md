# Native prime-freezing: sharp envelopes and a forced two-block excursion

**Status: proposed component mathematics with complete written arguments at the stated scope.**
No bound for the full native fourth moment, generalized diagonal moment hierarchy,
new zero-free half-plane, or RH is established. No independent mathematical review
or formal verification has been performed. All orders and all field/test/exclusion
data are fixed before the column scale grows.

This note continues PR #937 at `9f3250198a9b0551f42eb73dfd74a265c2a66854`.
The partially frozen family and signed restoration identity come from that packet.
PR #936 already gives the logarithmic-cutoff upper tradeoff for its rough-phase
projection, and sharpness with retained phases realized at an uncontrolled-height
CRT row. We credit those overlaps. The lower statements here keep **the original
Mobius coefficients, the principal datum, and small physical sixth-power rows**.
They do not use specially selected local phases or a growing twist.

Friable Mobius asymptotics are classical, not claimed as a new general theory.
Section 4 reconstructs the particular fixed polynomial-cutoff window needed here,
then applies it to the random-sign moments and the exact signed flux of #937.
See SOURCES.md for classical credit and the explicit input boundary.

## 1. Definitions and classical inputs

Let K=Q(sqrt(-3))=Q(omega), omega^2+omega+1=0, and let S be a fixed finite
set of prime ideals containing the primes above 2 and 3. Integral ideals n are
restricted by (n,S)=1. N denotes absolute ideal norm; mu_K is the ideal Mobius
function; P^+(1)=1 and P^+(n) is the largest prime-ideal norm dividing n.
Fix a nonzero complex W in C_c^infinity((0,infinity)), supported in [a,b],
0<a<b<infinity. Put X=max(3,bD). The same arguments requiring only finitely
many derivatives apply to the explicitly specified diagnostic weights, but no
smoothness of those weights is silently upgraded.

For each good prime ideal p, let chi_p(u) be the native sextic residue character,
with **value zero when p divides the element u**. Products on squarefree ideals
retain these zeros. In this note nu=1: the lower theorems concern the principal
datum, not every fixed twist. The upper estimates remain uniform in bounded
fixed local phases and extra deterministic exclusions.

Independently over the finitely many relevant prime ideals, set

    e_p=-1 if Np<=Y;       e_p uniform in {-1,+1} if Np>Y.

Define, for nonzero element rows u,

    P_(u,Y)(D)=sum_n mu_K(n)^2 chi_n(u) W(Nn/D) product_(p|n)e_p,
    B_(u,Y)(D)=E P_(u,Y)(D),
    B_Y(D)=B_(1,Y)(D)
          =sum_(P^+(n)<=Y) mu_K(n) W(Nn/D).                       (1.1)

If Y>=X, P is exactly the original native polynomial A_u(D). For smaller Y,
B is a smooth-number truncation of the actual Mobius sum. No coefficients are
replaced by their absolute values in (1.1).

We use the following classical fixed-field estimates, with constants allowed
to depend on K,S and the fixed requested integer N:

    I_K(x)=#{n:Nn<=x}=O_K(x),
    pi_K^S(x)=Li(x)+O_(K,S,N)(x/(log x)^N),
    M_S(x)=sum_(Nn<=x,(n,S)=1) mu_K(n)
          =O_(K,S,N)(x/(log x)^N)              for every fixed N. (1.2)

The last two are classical consequences of the fixed Dedekind-zeta zero-free
region near Re(s)=1; no GRH or uniform moving-conductor estimate is used.
They can alternatively be obtained for this field from zeta(s)L(s,chi_-3)
and fixed-conductor zero-free estimates. Fixed excluded factors do not change
the conclusion. We state (1.2) as external classical inputs, not as a numerical
consequence or an imported quasi-Riemann theorem. Section 2's lower argument
only needs pi_K^S(x)~x/log x; its upper argument needs only ideal counting.

Write

    zeta_K^S(s)=zeta_K(s) product_(p in S)(1-(Np)^(-s)),
    kappa_S=Res_(s=1) zeta_K^S(s)>0,
    R_S(s)=1/zeta_K^S(s),
    W_hat(s)=integral_0^infinity W(t)t^(s-1)dt,
    G(s)=R_S(s) W_hat(s).                                       (1.3)

Thus R_S is analytic near 1, R_S(1)=0 and R_S'(1)=1/kappa_S.
W_hat is entire and is not identically zero (uniqueness of the Fourier
transform after t=exp(v)). Its zeros have finite order.

## 2. Sharp logarithmic-cutoff mean envelope at the principal row

Fix A>2, alpha_A=1-1/A, and define the cutoff ENVELOPE

    Bcal_A(D)=sup_(2<=Y<=(log D)^A) |B_Y(D)|.                    (2.1)

**Theorem 2.1.** With exactly the original principal-row coefficients,

    limsup_(D->infinity) log(1+Bcal_A(D))/log D = alpha_A.        (2.2)

This is a statement about the supremum over the permitted cutoffs at each D.
It does NOT assert the lower bound on the single curve Y=(log D)^A, nor at
every scale. The same mean theorem in fact holds for A>1 with a slightly
larger local-error estimate below; A>2 is all that the moment application needs.

### Upper bound

For any fixed alpha_A<sigma<1, Rankin's bound and positivity of a majorant give

    |B_Y(D)| <= ||W||_infinity (bD)^sigma
                     product_(Np<=Y,p not in S)(1+(Np)^(-sigma)). (2.3)

Even the bound by ordinary integers for prime-ideal norms yields
sum_(Np<=Y)(Np)^(-sigma)=O_sigma(1+Y^(1-sigma)). For Y<=(log D)^A,
this is o(log D), because A(1-sigma)<1. Equation (2.3) is at most
D^(sigma+o(1)), uniformly over the permitted cutoffs. Let sigma decrease
to alpha_A. This proves the upper bound in (2.2).

### Finite Euler resonance

For a fixed Y let

    E_Y(s)=product_(Np<=Y,p not in S)(1-(Np)^(-s)).               (2.4)

This is a FINITE Dirichlet polynomial. Termwise Mellin integration is valid
at every complex s and gives the exact identity

    W_hat(s) E_Y(s)=integral_0^infinity B_Y(D) D^(-s-1)dD.        (2.5)

For fixed Y the integrand has compact D-support bounded away from zero;
there is no analytic continuation or infinite Euler-product exchange here.
Fix 1/2<sigma<1 and put s_Y=sigma+i*pi/log Y. The prime ideal theorem gives

    log |E_Y(s_Y)|
        ~ Y^(1-sigma)/((1-sigma)log Y).                          (2.6)

Here is a direct justification. The expansion
log|1-z|=-Re z+O_sigma(|z|^2) has summable error over prime ideals when
|z|=(Np)^(-sigma), since 2sigma>1. Also
sum_(Np<=Y)(Np)^(-sigma) ~ Y^(1-sigma)/((1-sigma)log Y).
For any fixed delta in (0,1), primes below Y^(1-delta) contribute o of
this last quantity. On the complementary range the angles
pi log(Np)/log Y lie in [pi(1-delta),pi], where their cosines tend
uniformly to -1 as delta decreases to zero. Squeeze, then let delta
 decrease to zero. Removing finitely many primes changes only O(1).
This proves (2.6), including its sign.

### Lower bound

Suppose for contradiction that Bcal_A(D)=O(D^c), for some c<alpha_A.
Choose max(c,1/2)<sigma<alpha_A with W_hat(sigma)!=0; this is possible
because W_hat has isolated zeros. Put T_Y=exp(Y^(1/A)). For D>=T_Y,
Y<=(log D)^A, so the supposed estimate bounds |B_Y(D)| by C D^c.
For D<T_Y use instead |B_Y(D)|=O_W(D), which follows from I_K(x)=O(x)
and the compact support; the finite lower D endpoint is harmless.
Taking absolute values in (2.5) gives

    |W_hat(s_Y) E_Y(s_Y)|
       << 1+T_Y^(1-sigma)+T_Y^(c-sigma)
       << exp((1-sigma)Y^(1/A)).                               (2.7)

But W_hat(s_Y) tends to the nonzero number W_hat(sigma), while (2.6)
grows exponentially on the larger logarithmic scale
Y^(1-sigma)/log Y, since 1-sigma>1/A. Contradiction. If the limsup
in (2.2) were below alpha_A, such a c would bound the envelope eventually.
This proves (2.2). In particular there are actual scales and permitted
cutoffs, with no phase or coefficient changes, of size D^(alpha_A-o(1)).

## 3. Exact moment-envelope exponent and physical sixth-power amplification

Let

    Fcal_(k,A)^(1)(D)=sup_(2<=Y<=(log D)^A) E|P_(1,Y)(D)|^(2k),
    Fcal_(k,A)(D,D^h)=sup_(2<=Y<=(log D)^A)
                   sum_(0<Nu<=D^h) E|P_(u,Y)(D)|^(2k).         (3.1)

The superscript (1) refers to the single principal row, not the moment order.
The cutoff is common to all rows. Fix k>=1 and h>0.

**Theorem 3.1.** For A>2,

    limsup log(1+Fcal_(k,A)^(1)(D))/log D = 2k alpha_A.          (3.2)

If lambda_(k,A)(h) is the corresponding limsup exponent for the all-row
quantity in (3.1), then

    2k alpha_A+h/6 <= lambda_(k,A)(h) <= 2k alpha_A+h.           (3.3)

Consequently, for each fixed A>2 and h>0,

    lim_(k->infinity) lambda_(k,A)(h)/(2k)=alpha_A.              (3.4)

These exponents describe the INTERMEDIATE randomized family with a cutoff
envelope. They are not exponents of the undamped native endpoint and do not
give a new zero-free boundary.

### Upper bound and prior-work boundary

The Rankin proof here is the sign version of the upper tradeoff already
present in #936. Expand the 2k-th moment and majorize its surviving tuple
terms absolutely. At a rough prime its total incidence must be even. If
r=(Np)^(-sigma), the local majorant is

    L_(k,2)(r)=((1+r)^(2k)+(1-r)^(2k))/2
             =1+k(2k-1)r^2+O_k(r^4).                           (3.5)

At a frozen prime use (1+r)^(2k); a row nonunit has local factor one.
For every fixed sigma>1/2 the rough Euler product converges. Inserting the
2k support bounds before removing the norm restrictions gives

    E|P_(u,Y)|^(2k) <= C_(k,sigma,W) D^(2k sigma)
                             product_(Np<=Y)(1+(Np)^(-sigma))^(2k). (3.6)

This is uniform in all rows, phases and zero masks. Choosing
sigma>max(1/2,1-1/A) makes the finite product D^o(1). Sum O(D^h) rows
for the upper bound in (3.3). In the sixth-root version the quadratic
coefficient is k^2 rather than k(2k-1); we do not conflate the two models.
Theorem 2.1 and Jensen give the matching lower in (3.2).

### Actual-height replicas

Put Q=D^(h/6). For every prime ideal q outside S with Q/2<Nq<=Q,
choose a generator pi_q. The class number of K is one. The element
u_q=pi_q^6 does not depend on which of its six unit associates is chosen,
and distinct q yield distinct rows. They satisfy

    0<Nu_q=(Nq)^6<=D^h,
    chi_n(u_q)=1_(q,n)=1.                                      (3.7)

Let R_h(D) be this row set and R(D) its cardinality. The prime ideal theorem
gives R(D) asymp D^(h/6)/log D. Uniformly over all polylogarithmic cutoffs
in (3.1), Nq>Y at sufficiently large D. Therefore no ideal in the smooth
mean contains q, and EXACTLY

    E P_(u_q,Y)(D)=B_Y(D).                                     (3.8)

Jensen applied at all these actual rows gives

    Fcal_(k,A)(D,D^h) >= R(D) Bcal_A(D)^(2k).                   (3.9)

Use Theorem 2.1 along its subsequence; this proves the lower in (3.3).
Dividing (3.3) by 2k proves (3.4).

**Corollary 3.2 (native limitation of a uniform freezing extension).**
A uniform bound Fcal_(k,A)(D,D^h)<<D^(h+k+epsilon) for every epsilon>0
is impossible whenever

    h < (6k/5)(1-2/A).                                        (3.10)

For example A=4,k=2,h=1 gives a lower limsup exponent 19/6, larger
than the requested diagonal exponent 3. Unlike the older unrestricted
coefficient/CRT constructions, the coefficients and row-height constraint
are both native here. Again this disproves a UNIFORM CUTOFF-ENVELOPE
extension, not the original endpoint moment and not a lower bound along
one prescribed logarithmic cutoff curve.

## 4. The polynomial-cutoff excursion of the actual smooth Mobius mean

This section uses all of the classical estimates in (1.2).
Fix a compact interval [theta_0,theta_1] within (1/2,1) and let Y=D^theta.

**Theorem 4.1 (fixed-window friable expansion).** For every fixed J>=0,
uniformly in theta in this interval,

    B_(D^theta)(D)
      =D sum_(j=0)^J (-1)^j G^(j)(1)/(log D)^(j+1)
           +O_(J,W,K,S,theta_0,theta_1)(D/(log D)^(J+2)).        (4.1)

Let r be the order of vanishing of W_hat at 1 (r=0 when W_hat(1)!=0).
Then r is finite and

    B_(D^theta)(D) ~ c_(W,S) D/(log D)^(r+2),
    c_(W,S)=(-1)^(r+1)(r+1) W_hat^(r)(1)/kappa_S !=0.          (4.2)

For a nonnegative nonzero W this is

    B_(D^theta)(D) ~ -(integral W)/kappa_S * D/(log D)^2.        (4.3)

The meaning of ~ for complex W is a complex ratio tending to one.
Equation (4.1) is a specialized elementary reconstruction of classical
friable Mobius asymptotics, not a claim to originate that subject.

### Exact single-large-prime identity

For large D, Y^2>bD. Every squarefree ideal in the supported columns has
at most one prime factor with norm greater than Y. Writing it as pm,
we have Nm<=bD/Y<Y, so p does not divide m automatically. The signs give

    B_Y(D)=A_1(D)+sum_(Np>Y,p not in S)
                          sum_(m,S)=1 mu_K(m) W(Np Nm/D).       (4.4)

Here A_1(D) is the full native smooth Mobius sum. All sums are finite;
there is no lost coprimality condition. Partial summation with (1.2)
gives A_1(D)=O_N(D/(log D)^N) for every fixed N.

### Replace the prime sum at controlled accuracy

For t=Nm define

    f_D(t)=integral_Y^infinity W(tv/D) dv/log v
          =(D/t) integral_(z>tY/D) W(z)/(log D+log z-log t) dz.   (4.5)

Partial summation against pi_K^S(v)-Li(v), including the lower boundary
at Y, gives an error O_N(D/(t (log Y)^N)) when t<=bD/Y and zero otherwise.
Summing this error over ideals costs at most O(log D), by I_K(x)=O(x).
As log Y is comparable to log D, the total error is smaller than any
specified fixed logarithmic power after choosing N sufficiently large.
This argument bounds the errors absolutely; it does not require cancellation
in a prime number theorem whose conductor depends on the cofactor.

Uniformly on the support of f_D, with L=log D,

    |f_D(t)| << D/(tL),      |f_D'(t)| << D/(t^2 L).            (4.6)

The moving lower-limit term in the derivative is supported where tY/D
is in [a,b]; there Y/t is comparable to D/t^2 and its denominator is
log Y, so it satisfies the same bound. This verifies that boundary too.

### The cofactor tail and the expansion

Set eta=1/(2(J+3)) and Z=exp(L^eta). Partial summation with M_S(t),
(4.6), and arbitrarily large N shows that the contribution of Nm>Z is

    O_N((D/L)(log Z)^(1-N)),                                   (4.7)

hence O(D/L^(J+2)) or smaller after enlarging N. For Nm<=Z the cutoff
in (4.5) disappears for all large D, uniformly in theta<=theta_1<1.
In 1/(L+log z-log Nm), expand the geometric series through degree J+1.
The sum of the absolute remainders is at most

    O(D (log Z)^(J+3)/L^(J+3))=O(D/L^(J+5/2)).                 (4.8)

We used sum_(Nm<=Z)1/Nm=O(log Z), |log z-log Nm|=O(log Z),
and a denominator bounded below by L/2. The extra degree J+1 term will
be absorbed in the final O(D/L^(J+2)) error.

For every fixed ell, partial summation using (1.2) proves convergence and
arbitrarily strong logarithmic truncation errors in

    sum_m mu_K(m)(log Nm)^ell/Nm = (-1)^ell R_S^(ell)(1).        (4.9)

For rigor, initially differentiate the absolutely convergent series at
Re(s)>1, then use the uniform tail bound from (1.2) to pass to s=1.
Thus the polynomial coefficient of L^(-j-1) becomes

    sum_(ell=0)^j binom(j,ell)(-1)^ell R_S^(ell)(1)
                           (-1)^(j-ell) W_hat^(j-ell)(1)
       =(-1)^j G^(j)(1).                                     (4.10)

Truncation errors in (4.9) can be made smaller than (4.8), since the
number of derivatives is fixed. Combining (4.4)--(4.10) proves (4.1).
Finally G has a zero of order r+1, with
G^(r+1)(1)=(r+1)W_hat^(r)(1)/kappa_S. Choose J=r+1 to obtain (4.2).

**Consequence.** Balancing finitely many Mellin derivatives of a fixed test
only inserts more powers of log D in this intermediate excursion. It cannot
reduce its power exponent below one. Infinite-order vanishing at 1 would
force the entire W_hat, and hence W itself, to vanish identically.

## 5. Actual intermediate moments, and two necessary opposite signed fluxes

The polynomial-cutoff mean is not a negligible component of a broad random
fluctuation. It dominates at the principal row and at small sixth-power rows.

### Linear rough part

Because Y^2>bD, (1.1) has the exact form

    P_(u,Y)=B_(u,Y)+sum_(Np>Y) e_p C_(u,p),
    |C_(u,p)| <= C_W D/Np.                                    (5.1)

The coefficient C includes the literal zero chi_p(u), all the frozen cofactor
Mobius signs, and the original exclusions. Distinct summands use independent
mean-zero signs. The elementary fixed-order Khintchine inequality therefore
implies, uniformly in u,

    ||P_(u,Y)-B_(u,Y)||_(2k)
        <<_(k,W) D (sum_(Np>Y)(Np)^(-2))^(1/2)
        <<_(k,W) D/sqrt(Y log Y).                             (5.2)

For completeness, the first inequality follows by expanding an even moment:
only prime multiplicities at least two survive, and the multinomial sum is
bounded by a k-dependent constant times (sum |C_p|^2)^k. Real and imaginary
parts handle complex coefficients. The second follows from the elementary
prime-count upper bound; even the weaker D/sqrt(Y) would suffice below.
For Y=D^theta this is negligible compared to (4.2).

For the actual replica set R_h(D) of Section 3 define

    E_(k,Y)(D)=sum_(u in R_h(D)) E|P_(u,Y)(D)|^(2k),
    Q_k(D)=R(D)|c_(W,S)|^(2k) D^(2k)/(log D)^(2k(r+2)).         (5.3)

**Theorem 5.1 (a forced two-block excursion).** For every fixed h>0,k>=1
and theta in the compact subinterval specified above,

    E_(k,D^theta)(D) ~ Q_k(D).                                (5.4)

If Y_0=(log X)^2 and Y_end=X, then

    E_(k,Y_0)(D)=o(Q_k(D)),       E_(k,Y_end)(D)=o(Q_k(D)).      (5.5)

Thus the total signed restoration increments on the first and second prime
blocks satisfy respectively

    sum_(Y_0<Np<=D^theta) Delta_(k,p) ~ +Q_k(D),
    sum_(D^theta<Np<=X) Delta_(k,p) ~ -Q_k(D),                  (5.6)

where rows are the SAME set R_h(D) throughout both sums. No row-measure or
height is changed while the primes are restored.

Proof. At u_q=pi_q^6, the mean is the smooth Mobius sum with ideals divisible
by q deleted. If Nq>Y this is exactly B_Y. Otherwise ideal counting gives

    |B_(u_q,Y)-B_Y| <<_W D/Nq                                 (5.7)

when Nq<=bD, and zero when Nq>bD. Since Nq asymp D^(h/6), this is
negligible compared with D/(log D)^(r+2), uniformly in q. Equations (4.2),
(5.2), and the reverse and forward L^(2k) triangle inequalities imply

    E|P_(u_q,D^theta)|^(2k)
       =|c_(W,S)|^(2k)D^(2k)/(log D)^(2k(r+2)) * (1+o(1))

uniformly on R_h(D). Sum to obtain (5.4).

Theorem 2.1/Corollary 2.2 of #937 gives
E_(k,Y_0)<<R(D)D^(k+epsilon), which is o(Q_k) on taking epsilon<k.
Alternatively (3.6) with any fixed sigma just above 1/2 and below 1 gives
the weaker but still sufficient o(Q_k) starting bound directly. At the endpoint
A_(u_q) is the full A_1 with ideals divisible by q removed. The same estimate
(5.7), together with A_1(D)=O_N(D/(log D)^N) for every N, shows uniformly
A_(u_q)=o(D/(log D)^(r+2)). This proves the endpoint part of (5.5).
It is a sub-excursion estimate, NOT a diagonal endpoint moment bound.

Finally, the exact restoration identity from #937 is

    Delta_(k,p)=-sum_(u in R_h(D)) E_later
        sum_(ell<=k,ell odd) binom(k,ell)
           (|U|^2+|V|^2)^(k-ell) (2 Re(U conjugate(V)))^ell,    (5.8)

where P=U+e_p V and V retains the true prime cofactor and its exclusion.
After freezing e_p=-1, the conditional moment minus its preceding average
is (|U-V|^(2k)-|U+V|^(2k))/2. Binomial expansion proves (5.8) directly.
Telescope separately to Y=D^theta and to X. Equations (5.4)--(5.5) give
(5.6) without estimating any individual increment. Equal norm primes may
be ordered arbitrarily; both displayed blocks end after an entire norm cutoff.

### Fourth-moment sign and scale

At k=2 write J_early and J_late for the two block sums of

    sum_u E_later Re(U conjugate(V)) (|U|^2+|V|^2).

Since Delta=-4 times this expression,

    J_early ~ -Q_2(D)/4,       J_late ~ +Q_2(D)/4.              (5.9)

These are lower/upper asymptotic statements about literal signed native
correlations, not an arbitrary coefficient example. Their sum can be much
smaller; no sign is asserted for the combined sum.

For every fixed k the excursion has power exponent 2k+h/6. Hence bounding
each prime block, or the total variation of the restoration increments,
by the desired full-row diagonal scale D^(h+k+epsilon) is impossible when

    h<6k/5.                                                  (5.10)

The proof of this impossibility already uses the restricted actual replica
measure, of mass at most the full physical row count. It refutes a proposed
block estimate uniform over nonnegative physical row measures, or such an
estimate specifically for these replicas. It does NOT assert that the
signed block sum over ALL rows has this lower bound: other rows may cancel
it. Absolute-value-in-row variants are also refuted by this subset.

For k=2,h=1, Q_2 has power exponent 25/6 whereas the full-row diagonal
budget has exponent 3. That comparison concerns an INTERMEDIATE moment
and separated signed blocks, not the final original fourth moment.

### A positive centered hierarchy near the terminal cutoff

**Corollary 5.2.** For any nonnegative row weights of total mass H, and
Y^2>bD, (5.2) gives the unconditional bound

    sum_u w(u) E|P_(u,Y)-B_(u,Y)|^(2k)
        <<_(k,W) H (D^2/(Y log Y))^k.                          (5.11)

In particular, for any fixed C>=0 and Y=D/(log D)^C,

    sum_u w(u) E|P_(u,Y)-B_(u,Y)|^(2k)
        << H D^k (log D)^((C-1)k)                             (5.12)

at all sufficiently large D. This retains every physical row and zero mask.
It is a diagonal-size hierarchy for the CENTERED random fluctuations, not
for the deterministic conditional means. Khintchine's inequality is classical;
the deduction is included to separate the two sources of difficulty explicitly.
Jensen and the triangle inequality show that diagonal moment control of the
whole hybrid at these cutoffs is equivalent, up to logarithmic factors, to
such control of its conditional means B_(u,Y). Neither control of those means
nor a transfer from this near-terminal hybrid to the original endpoint is
proved here. The fixed-theta asymptotic (4.1) is not asserted uniformly in
this moving-theta near-terminal window.

## 6. What the next arithmetic estimate must preserve

The total endpoint identity of #937 remains valid and its missing lower
bound on the total fourth-moment J remains OPEN. The present results rule
out replacing it by diagonal control of every intermediate cutoff, by a
prime-block total-variation estimate uniform in the physical measure, or
by a finite Mellin balancing that ignores the large smooth Mobius mean.

There are two logically separate findings:

1. At polylogarithmic cutoffs, even the unchanged principal row has the
   sharp envelope exponent 1-1/A for A>2. Physical prime replicas turn
   this into a genuine native restriction on uniform freezing moments.
2. At a fixed polynomial cutoff, the explicit friable mean creates two
   large opposite fluxes. Their reunion is essential even on the actual
   principal replica rows; a termwise or blockwise absolute approach fails.

A possible revised attack is to subtract and reunite these explicit mean
excursions BEFORE estimating the remaining signed correlations, keeping
the source, masks, same-height cofactors, and terminal value synchronized.
This is a research direction, not a proved renormalized moment bound.
The nonprincipal short-row correlations and the terminal signed estimate
are still unresolved. No new zero-free exponent follows from this packet.
