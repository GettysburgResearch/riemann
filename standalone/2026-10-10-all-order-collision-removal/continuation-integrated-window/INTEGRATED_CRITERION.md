# One fixed window and one signed scale integral suffice

**Status:** proposed complete component proofs and a conditional arithmetic criterion. The new signed arithmetic upper bound is NOT proved. No new fourth/sixth moment, 17/24 half-plane, or RH proof is claimed. This is an add-only continuation of PR #916 at `8d49acb264577f63374358c33636ebe8e05ccf70`, not an integrated theorem or an independently reviewed result.

## 1. The change in the analytic target

The preceding `continuation-balanced-closure/BALANCED_CLOSURE.md` requires a balanced mean-square bound separately at every smaller factor length, on one full fixed row range. Here the scale supremum is replaced by ONE weighted scale integral. The diagonal of that integral is bounded completely. A one-sided upper bound for the remaining signed off-diagonal is sufficient.

An explicit single nonnegative compactly supported C-infinity window has a Mellin transform nonzero on Re(s)>0. Therefore the zero-free implication needs this one window, not a theorem for every smooth window and not a window chosen after a hypothetical zero. The window is the classical dyadic uniform-convolution / Rvachev-up construction; it is not a new special function.

The proof has three independent pieces: an unconditional integrated norm comparison, an exact prime-replica extraction in weighted L^(2k), and Mellin continuation. None imports an OpenAI quasi-RH theorem. The prime ideal theorem in the fixed quadratic field is used only to count replica primes.

## 2. Fixed arithmetic, row conventions, and inverse kernel

Work over K=Q(sqrt(-3)). Ideal sums mean nonzero integral ideals. The fixed finite set S contains primes over 6 and the conductor of a fixed finite-order Hecke character nu. Use the primary-generator sextic symbol of the parent:

    theta_u(n) = nu(n) (u/n)_6,  (n,S)=1.

It is completely multiplicative in n, including its zero values, and has modulus at most one. For a real bounded compact window W supported in [a,b] subset (0,infinity), put

    A_u(X) = sum_(n,S)=1 mu_K(n) theta_u(n) W(Nn/X),

and, for fixed integer k>=2,

    B_u(X) = sum_(n_1,...,n_k squarefree and pairwise coprime)
             mu_K(n_1...n_k) theta_u(n_1...n_k)
             product_i W(Nn_i/X),

with every n_i prime to S. There are no moving excluded primes. Repeated copies of the unit ideal are permitted. Every sum vanishes for X<1/b.

Let sigma=1/2+delta, delta>0. The parent inverse kernel is defined primewise by

    Q_k(z_1,...,z_k) = (1-sum_i z_i)/product_i(1-z_i),
    b_k(0)=1,
    b_k(e)=1-|supp(e)|  for e != 0,
    D_k(d_1,...,d_k)=product_(p not in S) b_k(v_p(d_1),...,v_p(d_k)).

Its exact finite-horizon identity is

    B_u(X) = sum_d D_k(d) theta_u(product_i d_i)
                         product_i A_u(X/Nd_i).                 (2.1)

At each prime this is simply multiplication of Q_k by product_i(1-z_i). The identity remains true at theta_u(p)=0; it never divides by a character value.

Define the nonidentity absolute mass

    q = sum_(d != (1,...,1)) |D_k(d)| / (product_i Nd_i)^sigma.  (2.2)

The parent proves q<=1/3 after ONE fixed sufficiently large enlargement of S. For completeness, when 0<delta<=1/2, the explicit sufficient cutoff is

    P >= max((2k)^3, (24k^2/delta)^(1/(2delta))).                (2.3)

Indeed the one-prime absolute mass is

    F_k^-(t) = 2-(1-kt)/(1-t)^k,
    F_k^-(t)-1 <= k^2 t^2   when kt<=1/2.

The elementary ideal count # {n:Nn<=x} <=3x gives
sum_(Np>P) (Np)^(-1-2delta) <= (6/delta) P^(-2delta).
Thus the sum of local nonconstant masses is at most 1/4 and their Euler product is at most 4/3. These constants do not depend on the large horizon, the row, or the window. They need not be uniform in k or delta. We use only fixed positive delta.

## 3. Integrated balanced closure

Let U be ANY finite row set with ANY nonnegative row measure, unchanged throughout this section. For D>=max(2,1/b), define

    I_M(D;U) = integral_0^D sum_(u in U) |A_u(X)|^(2k)
                              X^(-2k sigma) dX/X,
    I_B(D;U) = integral_0^D sum_(u in U) |B_u(X)|^2
                              X^(-2k sigma) dX/X.              (3.1)

These are finite without any conjectural estimate: the coefficient sets below bD and U are finite, and the integrands vanish below 1/b.

### Theorem 3.1. Integrated norm equivalence

If q<1, then

    (1-q)^2 I_M(D;U) <= I_B(D;U) <= (1+q)^2 I_M(D;U).          (3.2)

In particular q<=1/3 gives I_M <=(9/4) I_B. No pointwise scale supremum, no derivative norm, and no independently assumed rectangular estimate occur.

**Proof.** Apply Holder to the k factors on the SAME product measure space U times (0,D), with measure du dX/X. For a fixed kernel tuple d,

    || X^(-k sigma) product_i A_u(X/Nd_i) ||_(L2(u,X))
    <= product_i [ integral_0^D sum_u |A_u(X/Nd_i)|^(2k)
                         X^(-2k sigma) dX/X ]^(1/(2k))
    <= (product_i Nd_i)^(-sigma) I_M(D;U)^(1/2).               (3.3)

For the last inequality, set Y=X/Nd_i. The new upper endpoint is D/Nd_i<=D, and the nonnegative row measure is still U. Multiplication by theta_u(product d_i) is a contraction. Minkowski applied to (2.1) gives the upper inequality in (3.2). The d=(1,...,1) term is A_u(X)^k, with coefficient exactly one. Isolating this term gives

    I_M^(1/2) <= I_B^(1/2) + q I_M^(1/2).

All quantities are finite, so absorption is legitimate. This proves the lower inequality. QED.

**Important boundary.** U may be chosen to be {u:0<Nu<=D^h} AFTER D is fixed, but it must not be changed to {u:0<Nu<=X^h} inside the integral or after the substitutions in (3.3). That different moving-row statement is not proved here. The new result weakens scale-by-scale control to integral control; it does not claim that a natural-curve estimate automatically covers the full row range.

## 4. Exact extraction directly in the weighted scale norm

Fix D large, h>0, H=D^h, Y=H^(1/6), and let P(D) consist of prime ideals outside S with Y/2<Np<=Y. Use their unique primary generators. Their sixth powers are distinct nonzero element rows of norm at most H. The fixed-field prime ideal theorem gives

    J(D)=#P(D) asymp Y/log Y.                                 (4.1)

Write C_p(X)=A_(p^6)(X). Exactly, including all nonunit zeros,

    A_1(X) = C_p(X) - nu(p) C_p(X/Np).                        (4.2)

This is separation of the terms divisible by p in a squarefree Mobius sum. Define the weighted norm

    ||f||_(p0,sigma;D)^p0 = integral_0^D |f(X)|^p0
                                       X^(-p0 sigma) dX/X,
    p0=2k.

The dilation estimate is exact:

    ||f(X/q0)||_(p0,sigma;D)
       = q0^(-sigma) ||f||_(p0,sigma;D/q0)
       <= q0^(-sigma) ||f||_(p0,sigma;D).                     (4.3)

Consequently ||A_1|| <= (1+(Np)^(-sigma)) ||C_p|| <= 2||C_p||.
Raise to 2k, sum over p, and retain these rows in the complete row moment:

    J(D) integral_0^D |A_1(X)|^(2k) X^(-2k sigma) dX/X
       <= 2^(2k) I_M(D; {0<Nu<=H}).                          (4.4)

This step has NO one-shot O(D/Y) error, NO scale supremum, NO small-scale induction, and NO constant allowed to depend on a moving prime. It uses the same prime set at every X below the chosen horizon D. The extraction is elementary because (4.2) is bounded directly in a scale norm stable under the smaller dilation.

For a nontrivial zero-free result h will be near one; h>0 is sufficient for this particular implication. Large h may simply give a boundary at least one.

## 5. A single compact window with no Mellin blind spots

Let V_j be independent uniform random variables on [-1,1], and set

    Z = sum_(j>=1) 2^(-j) V_j.

The sum is absolutely convergent, |Z|<=1. Its law has a nonnegative even C-infinity density f supported in [-1,1], with total mass one. Put

    W_*(y)=f(log y),  y>0.                                  (5.1)

Then W_* belongs to C_c^infinity((0,infinity)), is nonnegative, and is supported in [exp(-1),exp(1)]. Its Mellin transform is

    F_*(s)=integral_0^infinity W_*(y) y^s dy/y
          = product_(j>=1) sinh(2^(-j)s)/(2^(-j)s).           (5.2)

Each factor is interpreted as one at s=0. This is the classical dyadic uniform-convolution / Rvachev-up window, described for example by Arias de Reyna, arXiv:1702.05442 and 1702.06487. Its construction is credited, not claimed as new.

**Self-contained proof of the properties needed here.** On compact sets of s, each factor is 1+O(4^(-j)|s|^2); hence the product converges normally to an entire function. The Fourier transform of the probability law is its restriction to the imaginary axis. For each fixed integer m, bound the first m factors by C_m(1+|t|)^(-m), and every other factor by one. The Fourier transform therefore decays faster than any prescribed power. Fourier inversion gives a C-infinity density. Its probability interpretation gives nonnegativity, unit mass, evenness, and the stated support. The same proof on any fixed vertical strip follows by bounding the tail factors by exp(2^(-j)|Re s|). Composition with log preserves smooth compact support in (0,infinity).

Every zero of a factor in (5.2) is nonzero and purely imaginary. Away from the factor zeros, normal convergence with a summable deviation from one makes the infinite product nonzero. In particular,

    F_*(s) != 0 for Re(s)>0.                                 (5.3)

More precisely the zeros are s=2 pi i m, m a nonzero integer, of multiplicity 1+v_2(|m|). No uniform lower bound as |Im s| tends to infinity is asserted or needed. Holomorphic division is local.

The self-similarity Z=(V+Z')/2 gives an exact rational moment recurrence. If m_n=E[Z^n], then m_0=1, odd moments vanish, and

    (2^n-1)m_n = sum_(j=0)^(n-1) binom(n,j) m_j E[V^(n-j)].  (5.4)

In particular m_2=1/9 and m_4=19/675. This supplies finite exact checks of the specified window's normalization; those checks do not certify the infinite arithmetic criterion.

## 6. The single-window integrated implication

Use W=W_* henceforth. Let lambda>=0. Fix k>=2, h>0, delta>0 and the associated fixed S with q<1. Suppose, for every epsilon>0 and all sufficiently large D,

    I_B(D; {0<Nu<=D^h}) << D^(h+lambda+epsilon).              (6.1)

All constants may depend on k,h,delta,nu,S and epsilon, but not on D. This is a NEW UNPROVED ARITHMETIC PREMISE, not a consequence of Theorem 3.1.

### Theorem 6.1. Conditional zero-free boundary

Under (6.1), the fixed target L_K(s,nu) is zero-free for

    Re(s) > alpha,
    alpha = sigma + (lambda+5h/6)/(2k),
    sigma=1/2+delta.                                         (6.2)

Poles of principal functions at one are allowed. The boundary line is not included.

**Proof.** Combine (3.2), (4.1), and (4.4), absorbing the logarithm into an arbitrarily small power. This gives

    integral_0^D |A_1(X)|^(2k) X^(-2k sigma) dX/X
       << D^(lambda+5h/6+epsilon).                           (6.3)

For s with Re(s)>alpha, Holder on [2^j,2^(j+1)] bounds

    integral_(2^j)^(2^(j+1)) |A_1(X)| X^(-Re s) dX/X
       << 2^(j[ sigma + (lambda+5h/6+epsilon)/(2k) - Re s ]).

Choose epsilon small on each compact subset of Re(s)>alpha. The geometric series converges locally uniformly. Derivatives in s insert powers of log X, absorbed by a still smaller geometric margin. Thus

    G(s)=integral_0^infinity A_1(X) X^(-s) dX/X

is holomorphic on Re(s)>alpha. For Re(s)>1, absolute convergence and the change y=Nn/X give

    G(s)=F_*(s) / L_K^S(s,nu).                               (6.4)

By (5.3), division by F_* gives a holomorphic continuation of the reciprocal to Re(s)>alpha. Any zero there would instead give a pole. Deleted Euler factors are nonzero for Re(s)>0, so they create or remove no zero in the claimed region. QED.

This theorem needs only W_*. For all finite-order targets one must assume (6.1) for each such nu, with allowed target-dependent constants. For RH of zeta ALONE it suffices to use nu=1 over K at cofinal orders: away from s=1,

    zeta_K(s)=zeta(s)L(s,chi_(-3)),

and the second factor is entire, so a zeta zero cannot be canceled by a pole. The usual functional equation supplies reflection across 1/2. A proof of the moment premise might still need auxiliary character families; they have not been silently supplied by the logical implication.

If (6.1) is available for arbitrarily small fixed delta, its limiting boundary is

    1/2 + 5h/(12k) + lambda/(2k).                            (6.5)

At h tending to one, lambda=0 yields 17/24 for k=2 and 23/36 for k=3. At unbounded fixed orders k_j, it is enough that delta_j tends to zero and (lambda_j+h_j)/k_j tends to zero. Constants need not be uniform in j. These remain conditional consequences.

## 7. Completely bound the diagonal; retain only a signed scalar

Group the balanced polynomial by its squarefree product r:

    B_u(X)=sum_(r squarefree,(r,S)=1) c_X(r) chi_r(u),
    c_X(r)=mu_K(r)nu(r) w_X(r),
    w_X(r)=sum_(n_1...n_k=r) product_i W_*(Nn_i/X).           (7.1)

Since r is squarefree its factorizations automatically have pairwise-coprime factors. Keep every ordered divisor allocation. Define the literal row kernel

    K_H(r,s)=sum_(u in O,0<Nu<=H) chi_r(u) conjugate(chi_s(u)).

It retains row units and zeros. For each fixed D,H all sums below are finite. Exactly,

    I_B(D;H)=D_diag(D;H)+O_signed(D;H),                       (7.2)

where

    D_diag = integral_0^D X^(-2k sigma)
                  sum_r |c_X(r)|^2 K_H(r,r) dX/X,
    O_signed = 2 Re sum_(r<s) K_H(r,s)
                  integral_0^D c_X(r) conjugate(c_X(s))
                                      X^(-2k sigma) dX/X.   (7.3)

Any fixed ordering of ideals can be used in r<s. The real part and exact signs in O_signed are indispensable. This is not a positive decomposition into two energies.

### Proposition 7.1. The complete integrated diagonal is O(H)

For every fixed k,delta>0 and fixed data,

    0 <= D_diag(D;H) << H,    D,H>=2.                        (7.4)

**Proof.** K_H(r,r)<=C_K H by the lattice count. For each eta>0, the fixed-order ideal divisor bound gives

    sum_r |c_X(r)|^2 <<_(k,W,eta) X^(k+eta),  X>=1.           (7.5)

Indeed w_X(r) is at most a constant times d_(k,K)(r), its support has Nr<=b^k X^k, and its total absolute mass counts at most O(X^k) ordered tuples. Bound one copy of the divisor weight by O(X^eta) and sum the other copy. The interval 1/b<=X<=1 contributes O(H) separately. Choose eta<2k delta. The remaining integral is bounded by

    C H integral_1^D X^(eta-2k delta) dX/X <= C' H.

This proves (7.4). No off-diagonal cancellation was used. QED.

Because I_B is nonnegative, O_signed>=-D_diag>=-C H automatically. It follows that the single ONE-SIDED hypothesis

    O_signed(D;D^h) <= C_epsilon D^(h+lambda+epsilon)          (7.6)

implies (6.1), hence (6.2). No absolute-value estimate for O_signed is required. At lambda>=0 the converse follows from (7.2) and (7.4), up to changing the constant. Thus the remaining target is one signed cumulative statistic for one fixed smooth window.

**What remains open:** (7.6) with a useful lambda, in particular lambda=0 near h=1. The diagonal bound, inverse-kernel absorption, single-window construction, and exact extraction do not bound this signed remainder. Replacing it by an absolute sum discards precisely the unproved arithmetic cancellation.

## 8. Relationship to adjacent work

- PR #916's frozen predecessor proves the inverse kernel and pointwise finite-envelope absorption. Section 3 here moves that absorption to the joint row/scale measure, eliminating the pointwise smaller-scale hypothesis.
- PR #917 at `6b4723042b3d250024eef45cb1924f88f28e902c` and PR #919 at `9b04a887e171b3104a66cf57296ce5b0b2920d78` advertise averaged full-moment and signed-conductor criteria. Their metadata were inspected, but their complete proofs were not imported or re-audited here. The present extraction is proved independently from (4.2)-(4.4).
- The present signed scalar is the full balanced product-column covariance, not #919's further restricted conductor core. Their stronger sector removals must not be claimed here without an additional checked adapter.
- No conclusion about zeros at a height growing with k, and no quantitative effective cutoff in height, is asserted.
