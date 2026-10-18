# Full-density Euler-mask capture with a uniform finite-horizon inverse

Status: PROPOSED component deductions, awaiting independent mathematical review.
No critical native upper estimate, zero-free improvement, or RH proof is claimed.
The new contribution is a quantitative, source-preserving averaging/inversion
result, not new cancellation of the original Mobius sum. All limits below are
proved uniformly in the observation horizon and in the norm order.

## 1. Objects and the precise advance

Work over K=Q(omega), omega^2+omega+1=0. S consists of the primes above 2 and 3;
a further fixed finite set may be removed, at the cost of changing constants.
Every ideal is a nonzero exterior integral ideal. Write q(d)=Nd and r(d)=N rad(d).
Distinct prime ideals of the same norm remain distinct. Let chi be completely
multiplicative, chi(1)=1, |chi(d)|<=1. In particular, a zero at a nonunit is
retained. Fix the original Gaussian W_(c,tau)(y)=y^(-c) exp(-log(y)^2/(4tau)) /
sqrt(4pi tau), with real c and tau>0, and define

    A(D)=sum_d mu_K(d) chi(d) W_(c,tau)(q(d)/D),
    A_b(D)=sum_d mu_K(d) chi(d) 1_((b,d)=1) W_(c,tau)(q(d)/D).     (1)

These are the original Euler-deleted native sums. For the fixed sextic core
chi=chi_a and the character convention of #983, A_b=A_(a b^6), including (a,b)>1.
The abstract theorem itself only needs (1); it assumes no theta/Poisson adapter.
The labels b are UNRESTRICTED ideals, not sixth-free cores or independent rows.

Put N_B=I_S(B)=#{b:q(b)<=B}, and for 1<=p<infinity set

    ||A||_(sigma,p,T)=(integral_0^T |A(D)|^p D^(-p sigma) dD/D)^(1/p).

For p=infinity use ess sup_(0<D<=T) D^(-sigma)|A(D)|. Here sigma>0, T>0.
All these finite-horizon norms exist for (1): absolute ideal counting gives
Gaussian flatness at D=0 and continuity elsewhere. No RH is needed for that fact.

### Theorem A: signed averages have a bounded inverse, simultaneously for all p

For fixed sigma>0 there are B0,C>=1 such that, for EVERY B>=B0, T>0 and
1<=p<=infinity,

    C^(-1)||A||_(sigma,p,T)
      <= ||N_B^(-1) sum_(q(b)<=B) A_b||_(sigma,p,T)
      <= C ||A||_(sigma,p,T).                              (2)

C and B0 are independent of chi, p, T and B. This includes the critical weight
sigma=1/2 and permits p and T to grow with B. It estimates an operator, not A.
The individual mask moment constants in #983 can grow rapidly with p; averaging
SIGNED SOURCES BEFORE the norm instead gives this p-independent root cost.

The signed average has a uniform limit. Define k(d)=chi(d)/r(d) and

    V A(D)=sum_d k(d) A(D/q(d)).                            (3)

For EVERY fixed 0<eta<min(sigma,1/2),

    ||N_B^(-1)sum_b A_b - V A||_(sigma,p,T)
        <= C_(sigma,eta) B^(-eta) ||A||_(sigma,p,T).         (4)

This is uniform in p,T and the complete source, not only a pointwise coefficient
limit. On the native coefficients it has the exact identity

    V A(D)=sum_d mu_K(d) chi(d)
                product_(p|d)(1-1/q(p)) W_(c,tau)(q(d)/D). (5)

Thus the limiting source remains signed. It is not the unsigned diagonal.

### Theorem B: any vanishing fraction of whole replica trajectories may be lost

Let E be any subset of {b:q(b)<=B}, delta=1-|E|/N_B. There exist delta0>0 and
B1 such that (2) holds, with a new fixed C, for the SURVIVOR average

    |E|^(-1) sum_(b in E) A_b,

whenever B>=B1 and delta<=delta0. Constants are again independent of p,T,chi,E.
In particular this holds after ANY o(B) deletions, chosen adaptively using the
source, zeros, or the final horizon. E must be frozen across the ENTIRE norm
interval (0,T]. This theorem does NOT permit a different E(D) inside the integral.
No independence of the deleted set is assumed.

### Theorem C: a complete second-energy asymptotic with all cross terms

Let f(D)=D^(-sigma) A(D), R_d f(D)=f(D/q(d)), and use the inner product over
(0,T] with measure dD/D, linear in its first argument. Then

    (1/N_B) sum_(q(b)<=B) ||A_b||_(sigma,2,T)^2
       = Q_(sigma,chi,T)(f) + O_(sigma,eta)(B^(-eta)||f||_2^2),       (6)

where the EXPLICIT convergent quadratic form is

    Q(f)=sum_(d,e) chi(d)conj(chi(e)) /
            [q(d)^sigma q(e)^sigma r(de)] * <R_d f,R_e f>.           (7)

There are constants 0<c_sigma<=C_sigma<infinity, independent of T and chi, with

    c_sigma ||f||_2^2 <= Q(f) <= C_sigma ||f||_2^2.                  (8)

Every off-diagonal d!=e, every shared prime, and the finite upper horizon remain
in (7). It is NOT legitimate to replace it by its diagonal or by an infinite-line
Fourier multiplier without paying the discarded horizon contribution.

## 2. Elementary arithmetic counting with a power error

We supply the field-specific count so the rate in (4) has no imported RH premise.
The Eisenstein lattice has fundamental area sqrt(3)/2. A centered fundamental
parallelogram has radius at most sqrt(3)/2<1. Comparing the union of its cells
centered in the radius-sqrt(t) disk with disks of radii sqrt(t)+1 and
max(0,sqrt(t)-1) proves, after removing zero and dividing by the six units,

    I_K(t)=pi t/(3sqrt(3))+E(t), |E(t)|<=2sqrt(t), t>=0.             (9)

For t>=1 the error follows from 3pi/(3sqrt(3))+1/6<2; for 0<=t<1 use I_K(t)=0.
Every ideal is principal: Euclidean division follows by rounding a complex
number to the lattice within distance <1, so the norm is Euclidean. An ideal
has exactly six generators of a given norm, differing by units. This justifies
the cell count as an IDEAL count, not an element count in an infinite-unit field.

The prime above 2 has norm 4, not 2; the prime above 3 has norm 3. Inclusion and
exclusion, including their intersection of norm 12, gives

    I_S(t)=I_K(t)-I_K(t/4)-I_K(t/3)+I_K(t/12)
          =kappa_S t+O(5sqrt(t)), kappa_S=pi/(6sqrt(3))>1/4.        (10)

The bound 5 is valid since 2(1+1/2+1/sqrt(3)+1/sqrt(12))=3+sqrt(3)<5.
Consequently I_S(t)<=6t for t>=1 and N_B>=B/8 for B>=1600.
A further fixed set of exclusions uses the same finite inclusion-exclusion.
It retains an O_S(sqrt(t)) error and a positive leading density.

For any exterior ideal of radical norm r>=1 and B>=1600, (10) implies

    |I_S(B/r)/I_S(B)-1/r|
        <=80 B^(-eta) r^(-(1-eta)), 0<eta<=1/2.                   (11)

For r<=B first take eta=1/2: the numerator is bounded by
5sqrt(B)(r^(-1/2)+r^(-1)), and the denominator is at least B/8.
For eta<1/2 use (r/B)^(1/2-eta)<=1. For r>B, I_S(B/r)=0, and
1/r<=B^(-eta)r^(-(1-eta)). Thus the omitted large-radical range is also covered.

## 3. Causal convolution and complete Euler-mask inversion

Let X_(p,T)=L^p((0,T],dD/D), including p=infinity. Each R_d is a contraction:
its p-th integral is the original integral only through T/q(d). The same
inequality holds for the supremum norm. The operators commute and R_d R_e=R_de.
No extension beyond T is necessary. This one-sided convention is essential.

For a coefficient sequence h put ||h||_(1,sigma)=sum_d |h(d)|q(d)^(-sigma).
Its weighted dilation operator is

    h[S]f=sum_d h(d)q(d)^(-sigma) R_d f.

Absolute convergence in this coefficient norm implies operator convergence on
EVERY X_(p,T), with norm at most ||h||_(1,sigma), uniformly in p and T. Dirichlet
convolution of kernels corresponds exactly to composition of these operators.

At a fixed mask b let t_b(d)=chi(d)1_(rad(d)|b). Euler multiplication gives

    A_b(D)=sum_d t_b(d)A(D/q(d)),
    A(D)=sum_(d|rad(b)) mu_K(d)chi(d) A_b(D/q(d)).                 (12)

Indeed the local factor (1-chi(p)z) is canceled by its geometric series exactly
at p|b. The inverse expansion is finite. If chi(p)=0, all positive powers stay
zero. No condition (a,b)=1 or (squarefree core,power part)=1 is introduced.
For each fixed b, ||t_b||_(1,sigma)<=P_sigma(b), where

    P_sigma(b)=product_(p|b)(1-q(p)^(-sigma))^(-1)<infinity.         (13)

This proves (12) on finite-horizon norms by convergent convolution. It also
follows coefficientwise before smoothing: for fixed D the rearrangement is
absolutely convergent by the Gaussian's two tails. These identities and their
individual-mask interpretation are inherited from #983, not claimed anew.

## 4. A signed average converges to an invertible kernel

Average (12) over ALL b through B. Divisibility counts give the exact kernel

    k_B(d)=chi(d) I_S(B/r(d))/I_S(B).                             (14)

This retains all prime powers of d, even when their norms greatly exceed B:
only their RADICAL has to divide a mask. Since the b sum is finite, (13) justifies
interchanging it with the convergent d sum on every X_(p,T).

Using (11),

    ||k_B-k||_(1,sigma) <=80 D_(sigma,eta) B^(-eta),
    D_(sigma,eta)=product_p[1+q(p)^(-(1-eta))
                                  q(p)^(-sigma)/(1-q(p)^(-sigma))].       (15)

The product converges for eta<sigma: its local increment is O(q^(-1-sigma+eta)),
and comparison with the ideal count bounds the prime sum. Thus (15) proves (4)
in operator norm, with both infinite dilation tails included.

The kernel k has local series, with z=chi(p)p_formal,

    1+(1/q)sum_(j>=1) z^j=(1-(1-1/q)z)/(1-z).                    (16)

Its Dirichlet inverse l has local coefficients

    l(1)=1, l(p^j)=-(1/q)(1-1/q)^(j-1)chi(p)^j, j>=1.            (17)

Both kernels belong to the weighted coefficient algebra for EVERY sigma>0:

    ||k||_(1,sigma)<=Cplus=product_p[1+q^(-1-sigma)/(1-q^(-sigma))],
    ||l||_(1,sigma)<=Cinv=product_p[1+q^(-1-sigma)/
                                     (1-(1-1/q)q^(-sigma))].             (18)

All product errors are O(q^(-1-sigma)); there is no inverse-zeta assertion here.
Finite Euler products multiply to the identity, and absolute convergence passes
that identity to l*k=epsilon. Hence k[S] is invertible on every X_(p,T), with
inverse l[S] and inverse norm at most Cinv, uniformly in p,T,chi.

Choose B0>=1600 so 80 D_(sigma,eta) Cinv B0^(-eta)<=1/2. The Neumann series in
the SAME coefficient algebra inverts k_B and gives ||k_B[S]^(-1)||<=2Cinv.
The direct norm is at most Cplus+1/(2Cinv). These prove (2), including its uniform
p=infinity case. This is a finite-B inverse, not only invertibility of a limit.

Finally convolve k with the native coefficient mu_K chi. At p its generating
series is (1-z)*(1-(1-1/q)z)/(1-z)=1-(1-1/q)z. This proves (5), retaining all
squarefree native columns and giving zero on every nonsquarefree column. No
arithmetic cancellation estimate for this weighted Mobius source has been proved.

## 5. Robustness against deleting whole trajectories

The elementary divisor identity for P_sigma(b)^2 gives

    sum_(q(b)<=B) P_sigma(b)^2 <=6B C2,
    C2=product_p[1+((1-q^(-sigma))^(-2)-1)/q]<infinity.            (19)

To prove it, define nonnegative g on squarefree ideals by
 g(p)=(1-q^(-sigma))^(-2)-1. Then P_sigma(b)^2=sum_(d|b)g(d), so the sum is
sum_d g(d) I_S(B/q(d))<=6B sum_d g(d)/q(d). The product converges by (10).
This is the inherited linear mean-mask mechanism of #983, explicitly credited.

Let E omit delta N_B masks and first normalize its sum by N_B, not |E|. The
operator norm of the missing sum, on EVERY X_(p,T), is at most

    N_B^(-1)sum_(b notin E)P_sigma(b) <= sqrt(48 C2 delta).        (20)

Cauchy and N_B>=B/8 prove (20). It bounds an arbitrary adaptively chosen missing
set, not a random one. Choose B1 with the (15) error <=1/(4Cinv), and choose

    delta0=min(1/2,1/(16 Cinv^2 *48 C2)).                        (21)

Then the total distance to k[S] is <=1/(2Cinv); another Neumann series gives a
uniform inverse. Renormalizing by |E|=(1-delta)N_B changes norms by a factor in
[1,2]. This proves Theorem B. It is a signed-average statement, stronger than
merely proving that the average of nonnegative energies cannot be small.
The deleted indices must describe whole functions A_b on (0,T]; scale-dependent
switching inside the integral is not licensed by this proof.

## 6. The full second-energy operator and its coercivity

Expand the squared norm in (12), first with finite dilation sums, then pass to
the limit. The average count for two dilations is the number of masks divisible
by rad(de), namely I_S(B/r(de)). It is NOT I_S(B/r(d)r(e)) when d,e share a prime.
The entire series is absolutely dominated using contractions by

    ||f||_2^2 sum_(d,e) [q(d)q(e)]^(-sigma)/r(de)
       =||f||_2^2 product_p[1+((1-q^(-sigma))^(-2)-1)/q].         (22)

For the finite-B difference, (11) gives the summable bound

    80 B^(-eta)||f||_2^2
      product_p[1+q^(-(1-eta))((1-q^(-sigma))^(-2)-1)].           (23)

This product converges when eta<sigma. Equations (22)-(23) prove (6)-(7).
It is legitimate to take limits for each f,T because the error bound is uniform;
no full infinite-horizon energy is assumed finite.

Jensen in the Hilbert space gives

    ||k_B[S]f||_2^2 <=(1/N_B)sum_b ||t_b[S]f||_2^2.

Let B tend to infinity using (15) and (23). Since k[S] has inverse norm Cinv,

    Q(f)>=||k[S]f||_2^2>=Cinv^(-2)||f||_2^2.

The upper bound is (22), proving (8). This also proves full-density capture

    c N_B ||A||_(sigma,2,T)^2
      <=sum_b ||A_b||_(sigma,2,T)^2
      <=C N_B ||A||_(sigma,2,T)^2                            (24)

for all sufficiently large B, uniformly in T and chi. For any fixed finite p,
the upper bound uses the convergent mean P_sigma(b)^p; the lower bound follows
from (2) and Jensen, or from Theorem B on a permitted survivor set. No claimed
constant uniform in p is attached to the UPPER average-of-powers bound.

## 7. What this does and does not buy for the critical native problem

At sigma=1/2, (2) gives a uniform bounded root cost at every even order, including
orders growing with T. Equation (6) has error O(B^(-1/2+epsilon)||A||^2) for any
fixed epsilon in (0,1/2). The exponent 1/2 here concerns MASK SAMPLE SIZE B, not
a zeta zero location or a bound for the native energy.

For chi=1, if one could prove, for ANY B(T)->infinity and the permitted whole-
trajectory survivors E_T,

    integral_0^T | |E_T|^(-1)sum_(b in E_T) A_b(D) |^2 dD/D^2
                        <<_epsilon T^epsilon for every epsilon>0,       (OPEN)

then (2) would give the same bound for A. Its Gaussian Mellin identity initially
on Re s>1 is exp(tau(s-c)^2)/zeta_K^S(s). On each dyadic interval, Cauchy applied
to the critical energy bounds the absolute Mellin integral by
O(X^(1/2-Re s+epsilon/2)). Choose epsilon<2Re s-1 and sum. The small-D tail is
flat. The transform would therefore be holomorphic on Re s>1/2; its numerator
never vanishes, so no zeta_K zero can lie there. Functional-equation reflection
gives field RH, which implies ordinary RH using zeta_K=zeta L(s,chi_-3).

OPEN IS NOT PROVED. In particular a full-family cap on reciprocal values in
#984/#989 is not a bound for this signed native average. Nor are ordinary
sixth-free character rows the mask population b of this theorem. The original
principal member may be omitted (b=1), yet the remaining full-density average
still cannot hide that member's entire critical energy.

Relative to #983's prime-replica argument, no B/log B population or source-
envelope bootstrap is used here: all ideals yield N_B asymptotic to kappa_S B,
and arbitrary o(B) WHOLE-TRAJECTORY deletions are allowed. The comparison is
for cumulative finite-horizon norms, not a claimed improvement of its pointwise
moving-row deletion theorem. Those two scopes must not be silently equated.

A concrete guard against false promotion: replace the arithmetic A by A(D)=D^z
with real z>sigma. Its norm grows as T^(z-sigma); all the convolution, finite-B
inversion and capture conclusions still hold. Thus these operator estimates
alone cannot supply a subpower upper bound for an arbitrary source. This is a
changed-source control, not a counterexample to RH or to native cancellation.

The failed selected-residual/zero-detector optimization explored before this
route gave no improvement over the tested 11/15 and 5/7 envelopes. That numerical
search is not an optimality proof and is not a premise of any result above.
