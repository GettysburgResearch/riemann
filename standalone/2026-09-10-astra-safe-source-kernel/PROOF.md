# AC28: a direct safe-source kernel for the full prediction problem

**PROPOSED component proofs; independent mathematical review pending. RH is not
proved.** The all-order positivity assertion Q-AC28 below is OPEN. In particular,
no all-vector upper estimate is inferred from the finite matrices in this packet.

Parent: PR845 at `e6dbb8ef4e458ea4c8d1b17ced77ec28905a7472`.
The new implication below does not assume Q-AC26, RH, simplicity, or an
unproved continuum-to-lattice adapter. The local-Gram/contraction mechanism
is classical; PR398 already uses local exact Pick positivity for a different
completed-xi quotient. Our particular kernel, first-gap cancellation, and
source/continuum interface are derived here. See SOURCES.json.

## 0. Fixed source and normalization

All arithmetic sums are on positive odd integers. Put

    m(x)=sum_(n<=x, n odd) mu(n)/n,    m(x)=0 for x<1,
    h(t)=exp(t/2)m(exp(t)),            h(t)=0 for t<0,
    ell=log 3,
    Z(s)=(1-2^(-s))zeta(s),
    a(z)=(z-1/2)Z(z+1/2).

The letter a is a scalar analytic function, NOT the parent's matrix B_X or a
new arithmetic rank. The only pole of zeta is canceled, so a is entire and

    a(1/2)=1/2.                                             (0.1)

The classical pole residue and reflection formula are the only zeta
continuation facts needed for the forward RH implication. On Re z>1/2,

    H(z)=integral_0^infinity h(t)exp(-zt)dt=1/a(z).            (0.2)

For completeness |m(x)|<=2 follows without RH. The integer identity
sum_(n<=N)mu(n)floor(N/n)=1 gives |sum_(n<=N)mu(n)/n|<=1.
Writing this all-integer sum as m(x)-(1/2)m(x/2) and iterating proves the
odd bound. Equation (0.2) then follows by absolute integration and the
absolutely convergent inverse Euler series.

For compactly supported complex G in L2(0,infinity), define

    (P G)(u)=integral_u^infinity h(v-u)G(v)dv, u>=0,
    (F G)(r)=integral_0^infinity h(r+v)G(v)dv, 0<=r<=ell.
                                                               (0.3)

These are the ACTUAL old and new continuum responses of AC27. Their norms
are finite for compact G without assuming any asymptotic cancellation.
The discrete Q-AC26 implies

    ||F G||^2 <= eta ||P G||^2+4 C ||G||^2.                   (0.4)

AC27 proves that one direction by a quantitative finite-relative-range
lattice limit. We do not assume its converse. The point of this packet is
that (0.4) can itself feed an RH conclusion directly.

Inner products below are linear in their first argument. Kernel positivity
means positivity of every finite complex Gram matrix, not just its diagonal.

## 1. AC28-1: cancel the inverse before attempting positivity

There is no odd arithmetic activation between 1 and 3. Consequently

    h(t)=exp(t/2), 0<=t<ell.                                (1.1)

The endpoint t=ell has no effect on any Lebesgue integral below. Define

    d_r(z)=integral_0^r exp(z(r-t))exp(t/2)dt,
    b_r(z)=exp(zr)-a(z)d_r(z).                              (1.2)

Both are ENTIRE functions of z, with values in L2(0,ell) as r varies. The
removable formula is d_r(z)=(exp(zr)-exp(r/2))/(z-1/2), with
b_r(1/2)=exp(r/2)(1-r/2).

On the Euler-safe domain Re z>1/2 and for G_z(v)=exp(-zv), direct substitution
in (0.3) gives

    P G_z(u)=H(z)exp(-zu),
    F G_z(r)=H(z)b_r(z).                                   (1.3)

Indeed F G_z=exp(zr)[H(z)-integral_0^r h(t)exp(-zt)dt],
and (1.1) proves the identity. Thus no infinite future-source expression
remains in b: it uses only a and the explicit first interval.

For eta,C>=0 define on the ENTIRE right half-plane

    K_(eta,C)(z,w)
      =[eta+4C a(z)conj(a(w))]/[z+conj(w)]
          -integral_0^ell b_r(z)conj(b_r(w))dr.              (1.4)

There is no reciprocal zeta, unknown zero, or pole of 1/a in this definition.
On safe points put U=Z(z+1/2), W=conj(Z(w+1/2)) and
I(t)=(3^t-1)/t, I(0)=ell. The complete final integral is

    J(z,w)=(1-U)(1-W)I(z+conj(w))
            +(1-U)W I(z+1/2)+U(1-W)I(1/2+conj(w))+2UW.     (1.5)

This includes every mixed term. Formula (1.2), not separately singular
pieces of (1.5), defines the continuation through z=1/2 or w=1/2.

For any finite safe exponential input, (0.4) is EXACTLY positivity of the
Gram matrix (1.4), after multiplication by the nonzero H(z) factors. This
is a Hermitian pairing, unlike the bilinear square in PR837.

## 2. AC28-2: one fixed safe interval controls the whole analytic kernel

Fix ANY nonempty open real interval I contained in (1/2,infinity), for
example I=(1,2). For each fixed eta,C>=0 the following are equivalent:

(i) K_(eta,C) is positive on every finite tuple from I;
(ii) it is positive on every finite tuple from Re z>0;
(iii) (0.4) holds for every compact L2 input G.

The constants must be the SAME for every tuple and every input. Allowing C
to depend on tuple size would not satisfy any of these statements.

### Proof of (i) -> (ii): a bounded map, not positivity by continuation alone

In H0=L2(0,infinity) direct-sum L2(0,infinity), set

    phi_z=(sqrt(eta)exp(-z t), 2sqrt(C)a(z)exp(-z t)),
    psi_z=(b_r(z))_(0<=r<=ell) in H1=L2(0,ell).

Their two Gram matrices differ by K. Assumption (i) makes

    S(sum c_j phi_(z_j))=sum c_j psi_(z_j), z_j in I,

well-defined and contractive: a zero input combination has zero output.
Extend S to the closed span, and by zero on its orthogonal complement.
Then S:H0->H1 is a contraction. The vector-valued maps phi_z and psi_z are
holomorphic on Re z>0. Applying the ordinary identity theorem to every
scalar pairing of S phi_z-psi_z extends the equality from I to that whole
connected half-plane. Taking Gram matrices proves (ii).

This proves the precise local-to-global step. Pointwise real positivity,
separate positivity of source factors, and finite-order tests do not define S.

### (ii) -> (iii): the full compact-input domain, without RH

Equation (1.3) first proves (0.4) for finite sums of safe exponentials.
Fix a0>1/2. On the weighted norm ||exp(a0 v)G(v)||, the estimate |h(t)|<=2exp(t/2)
gives

    ||P G||^2 <= 2/[a0(2a0-1)] ||exp(a0 v)G||^2,
    ||F G||^2 <= 8/(2a0-1) ||exp(a0 v)G||^2.               (2.1)

Finite sums of exp(-(a0+k)v), k=1,2,..., are dense in this weighted space.
One elementary proof reduces to completeness of exp(-kv) in L2(0,infinity):
a function orthogonal to them gives the finite measure
f(-log x)dx on (0,1), with all polynomial moments zero, hence is zero.
This uses polynomial density in continuous functions on [0,1].
Every compact G can therefore be approximated in the weighted norm, and
(2.1) passes all three terms of (0.4) to the limit.

For (iii) -> (i), truncate each G_z and use (2.1) with 1/2<a0<Re z for
the finite tuple being tested. Their weighted tails tend to zero, proving
(0.4) for the exponentials and hence (i). QED.

Rational nodes from I suffice, by continuity and density. Alternatively
one can test every Taylor-jet Gram at ONE real z0>1/2. The jet feature maps
are phi_z^(j)/j! and psi_z^(j)/j!. Positivity of every finite jet Gram
defines the same contraction on their span; norm-convergent Taylor series
first give the equality in a disk, then the identity theorem gives it globally.
No assertion that a finite jet order suffices is made.

## 3. AC28-3: a direct, quantitative full-zero exclusion

Suppose (i) holds for fixed eta,C. If a(alpha)=0 and delta=Re alpha>0,
then b_r(alpha)=exp(alpha r). The global diagonal of (1.4) gives

    0<=K(alpha,alpha)
      =[eta-(exp(2delta ell)-1)]/(2delta).

Therefore EVERY zero of a in the right half-plane satisfies

    delta <= log(1+eta)/(2log 3).                           (3.1)

This is independent of C, imaginary height, and multiplicity. In particular:

**Q-AC28 (OPEN).** For every eta>0 there is a finite C_eta>=0 such that all
finite Gram matrices (1.4) on the SAME fixed I=(1,2) are positive.

**Conditional theorem.** Q-AC28 implies RH.

Proof: a hypothetical nontrivial zero rho of zeta with Re rho>1/2 gives
alpha=rho-1/2 with Re alpha>0. Choose eta<exp(2Re(alpha)ell)-1. Equation
(3.1) contradicts Q-AC28. Reflection about Re s=1/2 then proves RH.
Only a sequence of positive eta decreasing to zero is needed. No
RH-to-Mertens implication, infinite zero expansion, or converse lattice
adapter is used in this argument.

This is a sufficient criterion; necessity for RH is not asserted. It is
not an unconditional proof of its all-order positive premise.

### Direct boundary cost and why eta=0 is impossible

Let rho=1/2+i gamma be ANY critical-line zero of multiplicity m, and let
alpha=i gamma. Write a(alpha+sigma)=c sigma^m+O(sigma^(m+1)), c!=0.
Existence of a critical-line zero is classical; no ordinate is evaluated.
At alpha+sigma the diagonal inequality forces

    4C_eta |a(alpha+sigma)|^2
       >=2sigma integral_0^ell |b_r(alpha+sigma)|^2 dr-eta. (3.2)

Since b_r(alpha+sigma)->exp(i gamma r) uniformly on the finite interval,
the integral tends to ell. Setting sigma=k eta/(2ell), k>1, and then
optimizing k gives

    liminf_(eta down0) eta^(2m-1) C_eta
      >= (2ell)^(2m)(2m-1)^(2m-1)
            /[4|c|^2(2m)^(2m)] >0.                        (3.3)

This reproduces the parent's critical-cost scale, but now directly from a
holomorphic numerator kernel: there is no use of conditional Mertens decay
to extend inverse-Laplace probes toward the critical boundary.

With eta=0 and finite C, the first term of K(alpha+sigma,alpha+sigma) tends
to zero, while its subtracted term tends to ell. Hence NO finite C gives
local all-order positivity at eta=0. Critical resonances must be allowed;
the old-response term is not an optional nuisance.

## 4. AC28-4: actual scalar positivity is insufficient

For EVERY real z>1/2,

    K_(0,4)(z,z)>0.                                        (4.1)

This concerns the true zeta source, not a synthetic replacement.

Put s=z+1/2>1 and c0=exp(r) in [1,3]. Group the odd integers at least 3 into
[3^k,3^(k+1)), k>=1. Each block has 3^k odd integers, so

    0<Z(s)-1<sum_(k>=1)3^(-k(s-1))=1/(3^(s-1)-1).

Consequently

    b_r(z)=exp(r/2)[1-(c0^(s-1)-1)(Z(s)-1)]

lies strictly between zero and exp(r/2) for 0<r<=ell. Thus ||psi_z||^2<2.
The decreasing integral comparison also gives
Z(s)>=1/[2(s-1)], so a(z)>=max(1/2,z-1/2). It follows that
a(z)^2/z>=1/4 and ||phi_z||^2=8a(z)^2/z>=2 when eta=0,C=4.
This proves (4.1).

Section 3 nevertheless proves that for EVERY finite C there is a finite
real-node Gram failure on I at eta=0. In particular, globally positive
safe-real diagonals, and any finite collection of positive tests, do not
justify the infinite all-vector inequality. Our nonzero-eta target is NOT
refuted by this statement.

## 5. AC28-5: naive finite-prime positivity cannot seed a limit proof

For ANY finite set P of odd primes, replace Z by

    Z_P(s)=product_(p in P)(1-p^(-s))^(-1),
    a_P(z)=(z-1/2)Z_P(z+1/2),

and keep the first-gap formula (1.2). These replacements are holomorphic on
Re z>0, but a_P(1/2)=0, whereas the true a(1/2)=1/2. The local-to-global
argument applies verbatim to their kernels. At alpha=1/2, (3.1) would require

    eta>=2.                                                (5.1)

Therefore for EVERY finite P, EVERY eta<2 and EVERY finite C, some finite
Gram matrix on any fixed safe real interval is not positive. This includes
the empty Euler product. There is no all-prime positivity proof obtained by
showing these uncorrected finite products positive and passing to a limit.

This is a genuine source effect: inverse finite-Euler coefficients give a
harmonic sum eventually equal to product_(p in P)(1-1/p)>0, so their h grows
like exp(t/2). They do have the correct first interval (1.1). They do not
have the native infinite-source pole cancellation at s=1. Correcting that
pole alone is not asserted sufficient for positivity either.

Exact rational controls at eta=1/100,C=1 and safe points z_i=2i-1/2:
P empty has a negative 1x1 matrix; P={3} and P={3,5} each have a negative
2x2 determinant; P={3,5,7} has a negative 3x3 determinant. The checker
reconstructs their complete mixed terms. These controls are not the native
source, whose corresponding tested matrices are strictly positive.

## 6. AC28-6: the critical cost can be paid in an exact full-input model

This section is an explicitly NONNATIVE comparison. Use h_b(t)=exp(bt) for a
real parameter b; its initial kernel is also exp(bt), NOT the native exp(t/2)
unless b=1/2. Let c_b=integral_0^ell exp(2br)dr>0. The model has

    P_b G(u)=integral_u^infinity exp(b(v-u))G(v)dv,
    F_b G(r)=exp(br)P_bG(0).

For eta>=0 and C>=0 the sharp all-compact-input inequality

    ||F_bG||^2<=eta||P_bG||^2+4C||G||^2                  (6.1)

holds if and only if

    eta>exp(2b ell)-1,
    C>=c_b^2/[4(eta-(exp(2b ell)-1))].                    (6.2)

At eta=0,b<0 the displayed conditions are meaningful. No finite C works
when eta equals the threshold. To prove it put p=P_bG, so G=-p'-bp,
p vanishes beyond the compact input support, and

    RHS-LHS=4C||p'||^2+(eta+4Cb^2)||p||^2
                         -(4Cb+c_b)|p(0)|^2.             (6.3)

The sharp half-line trace inequality |p(0)|^2<=2||p||||p'||, with its
exponential equality profiles and compact approximations, makes (6.3)
nonnegative exactly when (6.2) holds. Necessity at or below threshold
also follows by exponential profiles approaching the unstable mode.

For the marginal case b=0, (6.2) is C>=ell^2/(4eta); at equality there is
the explicit sum of squares

    eta||p||^2+(ell^2/eta)||p'||^2-ell|p(0)|^2
      =||sqrt(eta)p+(ell/sqrt(eta))p'||^2.                 (6.4)

This proves the critical single-mode cost at EVERY input and horizon, not
only on probes. It does not decompose the actual h into this model or bound
its unmodeled remainder. That additional step would be a new theorem.

## 7. AC28-7: a fixed-interval polynomial inequality, with positive dilation data

There is an exact reformulation avoiding both growing arithmetic matrices and
reciprocal-zeta functions. For an arbitrary complex ODD polynomial

    p(t)=sum_(k=1)^N c_k t^(2k-1),
    Q_p(t)=sum_(n>=1, n odd) p(t/n)/n,
    E_p(t)=Q_p(1)-sum_(n>=3, n odd) p(t/n)/n, 1<=t<=3,

all series and their derivatives converge uniformly on compact t intervals.
The new full target is

    integral_1^3 |E_p(t)|^2 dt
       <=eta integral_0^1 |p(t)|^2 dt
             +4C_eta integral_0^1 t^2 |Q_p'(t)|^2 dt       (7.1)

for EVERY odd polynomial, with ONE C_eta independent of its degree and
coefficients. For each fixed eta,C this is EQUIVALENT to AC28-2(i)-(iii).
Thus (7.1) for eta decreasing to zero would prove RH. No such all-degree
bound has been established here.

### Exact arithmetic isometry

At z_k=2k-1/2, the coefficient multiplier of Q_p is Z(2k), and the
multiplier of t Q_p' is (2k-1)Z(2k)=a(z_k). Under t=exp(-v),

    sum c_k exp(-z_k v)=sqrt(t) p(t),
    sum c_k a(z_k)exp(-z_k v)=sqrt(t) t Q_p'(t).

Under t=exp(r), sum c_k b_r(z_k)=sqrt(t) E_p(t). The Jacobians convert
the feature-map Gram inequality exactly into (7.1), with all cross terms.
These are actual positive-integer dilation sums, not replacement Mobius data.

### Why these unbounded real nodes are enough

Positivity of (7.1) gives a contraction S taking phi_(z_k) to psi_(z_k).
Although the z_k have no finite accumulation point, no identity theorem
is applied without an extra growth argument. On Re z>1,

    |a(z)|<=C0(1+|z|),   ||psi_z||<=C1.

The second bound follows from
|Z(z+1/2)-1|<=C2*3^(-Re z) and r<=log3. Consequently every scalar pairing
of (S phi_z-psi_z)/(z+1) is bounded analytic on Re z>1. Its zeros z_k violate
the half-plane Blaschke condition, since

    sum_k (Re z_k-1)/(1+|z_k-1|^2)=infinity.

A nonzero bounded analytic function cannot do that: mapping this half-plane
to the disk and applying Jensen's formula bounds the sum of 1-|w_k|.
Therefore S phi_z=psi_z throughout Re z>1, hence by ordinary continuation
throughout Re z>0. AC28-2 completes the equivalence. This is a full all-degree
argument, NOT a consequence of any finite set of even-zeta samples.

### The positive measure behind the operator

Writing p(t)=t P(t^2), define the FINITE positive measure

    nu=sum_(n odd) n^(-2) delta_(1/n^2).

Then Q_p(t)=t integral P(t^2 u)dnu(u). Its moments are the explicit positive
numbers Z(2k), and its total mass is pi^2/8. This supplies a fixed-domain,
positive dilation representation of the actual arithmetic operator.

The measure also has the classical explicit generating function

    integral dnu(u)/(1-z u)
       =sum_(n odd) 1/(n^2-z)
       =pi tan(pi sqrt(z)/2)/(4 sqrt(z)), |z|<1.          (7.3)

The value at z=0 is removable. Differentiate the normally convergent product
cos(pi x/2)=product_(n odd)(1-x^2/n^2) logarithmically and put z=x^2.
This is the classical cosine product, not a new identity; see DLMF 4.22.2.
Thus the primitive moment data have a trigonometric generating function.
Its known real poles do NOT determine the zeros of the distinct Mellin
multiplier a. No zero-location conclusion is inferred from (7.3) alone.

One noncritical estimate can be proved globally. On L2(0,1),

    Q_p'=p'+sum_(n>=3 odd) n^(-2)p'(t/n),
    ||Q_p'-p'|| <= (4/5)||p'||,
    (1/5)||p'|| <= ||Q_p'|| <= (9/5)||p'||.                (7.2)

Indeed the n-th derivative dilation has norm at most n^(-3/2), and

    sum_(n>=3 odd)n^(-3/2)
      <=3^(-3/2)+(1/2)integral_3^infinity x^(-3/2)dx
      =4/(3sqrt3)<4/5.

This all-degree bound does NOT prove (7.1). Its norm is unweighted Q_p',
whereas the required norm is t Q_p'. For that weighted derivative the
corresponding dilation on g=t p' is g(t/n)/n, of norm n^(-1/2).
Their norm sum diverges. Finite total mass of nu does not restore the lost
critical weight. The missing result is precisely the compensated estimate
(7.1), retaining eta||p||^2 and the COMPLETE left-hand expression.

## 8. Full attempt, outcome, and exact next deliverable

The completed bridge is

    discrete Q-AC26
        -> full continuum prediction inequality
        <-> exact local safe-source kernel positivity
        -> quantitative global zero-free strip;
    positivity for eta decreasing to zero -> RH.

The new RH implication bypasses the previously missing all-column converse
adapter. It does NOT prove the middle positive statement. The elementary
source data are now Z(s) only in the absolutely convergent real domain s>1,
combined in the complete Hermitian kernel (1.4)-(1.5).

I attempted to prove positivity by a finite Euler-product factorization and
by scalar safe-side bounds. Sections 4-5 show why neither closes the proof.
The exact one-pole sum of squares (6.4) is a model mechanism, not permission
to assign a decomposition to the actual Mobius source.

The decisive OPEN task is to prove the fixed-interval inequality (7.1), or
to construct, for each eta>0, a finite C_eta and a
contractive source-faithful map S with S phi_z=psi_z on one fixed safe real
interval, or equivalently a sum-of-squares/positive Gram factorization for
(1.4) at every order. A positive diagonal, any prescribed finite number of
positive matrices, or a norm bound for the factors separately is insufficient.

No new upper bound on E(X), no proof of Q-AC26/Q-AC28, and no complete RH
proof was obtained. All prior source/status boundaries are unchanged.
