# Compensated Euler phases with a bounded critical transfer

Status: PROPOSED component proofs; no independent mathematical review.
Scope: exact coefficient identities, uniform same-height norm comparisons,
analytic multipliers, and finite computations. The full native moment and RH
are not proved, and no zero-free exponent is improved.

## 1. Native source and the change of coefficient class

Let K=Q(omega), omega^2+omega+1=0. Let S include the primes over 2 and 3
and any original fixed exclusions. All ideals below are prime to S. Every
remaining prime ideal has norm at least 7. Distinct conjugate prime ideals
remain distinct. Let xi_u be any completely multiplicative ideal function
with |xi_u(n)|<=1; in the application xi_u(n)=nu(n) chi_n(u), extending the
sextic symbol to all prime powers and retaining its literal nonunit zeros.
Let W be bounded and supported in [a,b] inside (0,infinity), and set

    A_u(X)=sum_n mu_K(n) xi_u(n) W(Nn/X).

The analytic arguments work for the smooth tests in the moment programme;
the finite census explicitly uses a hard window instead.

The naive deformation has local factor 1-z*x. It changes the prime coefficient
and generally creates a zeta-power singularity. Here we CHANGE THE FAMILY by
adding nonsquarefree coefficients, not by claiming that naive phase averaging
has become valid. For an integer r>=1 define

    F_{z,r}(x)=(1-z*x)(1-x)^(1-z)
               exp(sum_{m=2}^r (z^m-z)*x^m/m),                 (1)
    K_{z,r}(x)=F_{z,r}(x)/(1-x).

The empty sum for r=1 is zero. The power uses the Taylor logarithm at x=0.
Every assertion about finite coefficients is formal and has no branch choice.
Direct logarithmic expansion gives the decisive identity

    log K_{z,r}(x)=sum_{m>=r+1} (z-z^m)*x^m/m.               (2)

In particular F_{0,r}=F_{1,r}=1-x. For every z, its coefficients at x and
x^2,...,x^r are -1 and 0 respectively. At r=2,

    [x^3]F=(z-z^3)/3,
    [x^4]F=-z/12+z^3/3-z^4/4.                              (3)

Thus every squarefree coefficient is STILL exactly mu_K(n), and at r=2 the
whole cube-free coefficient set agrees with mu_K, including its zeros.
Randomness does not alter this difficult squarefree source.

For any profile |z_p|<=1 define f_z,r(n), h_z,r(n), g_z,r(n) multiplicatively
by the local factors F, K, K^(-1). Then

    f_z,r=mu_K*h_z,r,     mu_K=f_z,r*g_z,r.                  (4)

The two kernels h and g have support only on (r+1)-full ideals: each occurring
prime has exponent at least r+1. No coprimality between the two convolution
factors is imposed. Define the complete, norm-filtered polynomial

    C_u,z,r(X)=sum_n f_z,r(n) xi_u(n) W(Nn/X).

All sums at a fixed physical scale are finite.

## 2. A common absolute kernel bounded at the critical normalization

### Theorem 1
For every r>=2 there is ONE nonnegative multiplicative majorant v_r,
independent of the profile, such that

    |h_z,r(n)|<=v_r(n),  |g_z,r(n)|<=v_r(n),
    sum_n v_r(n)/sqrt(Nn) <= exp(50/27) < e^2.               (5)

This includes all profiles |z_p|<=1, and needs no additional small-prime gate
beyond the original exclusion of 2 and 3.

Proof. Since |z-z^m|<=2 on the closed unit disk, a coefficientwise majorant
for either sign of (2), after exponentiation, is

    V_r(t)=exp(2 sum_{m>=r+1} t^m/m).

Take its coefficients as the local coefficients of v_r. All are nonnegative.
For a prime norm q>=7 and r>=2,

    log V_r(q^(-1/2))
       <= (2/3) q^(-3/2)/(1-q^(-1/2)).

In this quadratic field at most two prime ideals have any one specified norm.
Consequently

    sum_p (Np)^(-3/2)
       <=2 sum_{n=7}^infinity n^(-3/2)
       <=4/sqrt(6)<5/3.

Also 1/(1-1/sqrt(7))<5/3. The logarithm of the full product is therefore
less than (2/3)(5/3)(5/3)=50/27. Monotone convergence proves (5), including
its coefficientwise uniformity. The latter is important: we did not merely
bound each profile's norm separately and then interchange an unjustified
supremum with a coefficient sum. QED.

The constants are deliberately not optimized. First-order compensation
alone has a degree-two logarithm and gives a logarithmic critical cost;
cancelling the degree-two logarithm is what makes (5) scale independent.
The absolute-convolution method overlaps the earlier #935/#939 completions;
this explicit disk-valued, two-term compensation and its stronger constant
critical bound are the component recorded here.

## 3. Two-way physical moment comparison at the SAME row height

Let w be any fixed finite nonnegative measure on nonzero rows and p>=1.
A probability measure pi on profiles may be arbitrary, with no independence
assumption for this theorem. The row measure is unchanged at every shorter
column scale. For D>0 define

    E_A,p(D)=sup_{0<X<=D} X^(-1/2) ||A(X)||_{Lp(w)},
    E_C,p(D)=sup_{0<X<=D} X^(-1/2) ||C(X)||_{Lp(w x pi)}.

Small X<1/b give zero sums. These are suprema of norms, NOT norms of a
rowwise or samplewise maximum.

### Theorem 2
For r>=2,

    E_C,p(D) <= e^2 E_A,p(D),
    E_A,p(D) <= e^2 E_C,p(D).                              (6)

Proof. Equation (4) gives the exact finite identities

    C_u,z,r(X)=sum_d h_z,r(d) xi_u(d) A_u(X/Nd),
    A_u(X)=sum_d g_z,r(d) xi_u(d) C_u,z,r(X/Nd).            (7)

The d sum is automatically cut off at Nd<=bX by the test. Shared primes
between d and the residual ideal are essential and remain in (7).
Multiplication by xi_u(d) is an Lp contraction even on nonunit rows. Apply
Minkowski, bound coefficients by the SAME v_r(d), divide by sqrt(X), and
use (5). In the inverse formula regard A as constant in the probability
variable. This proves both inequalities for arbitrary pi. QED.

For order p=2k the moment cost is at most e^(4k), not a power of D or even
a logarithmic power. The theorem is uniform in k at the root-norm level.
It does NOT turn a bound given only on H=X^h into a same-height envelope.
All original twist/test/shortened-scale obligations remain explicit.

## 4. Full-circle averaging is unbiased and has a positive excess

Two laws are especially useful: one common variable z uniform on the unit
circle, assigned to every active prime; or independent uniform circle
variables z_p. Inactive primes have z_p=0 (or 1), whose local factor is native.
At finite X the completed polynomial is a polynomial in finitely many phase
variables. Its holomorphic constant coefficient is exactly A_u(X), because
F_{0,r}=1-x. Thus

    E C_u,z,r(X)=A_u(X),   E C_u,z,r(X)^k=A_u(X)^k.         (8)

For the common-circle law write the exact polynomial

    C_u,z,r(X)^k=sum_{j>=0} B_j(u;X) z^j,   B_0=A_u(X)^k.

Circle orthogonality gives

    sum_u w(u) E|C_u,z,r(X)|^(2k)
      = M_{2k}(X;w)+sum_{j>=1} sum_u w(u)|B_j(u;X)|^2.    (9)

For independent phases replace j by a multi-index. In particular the average
is at least the native moment. Together with (6), the circle-averaged and
native SAME-HEIGHT scale envelopes are equivalent with constant cost.
No small angular window shrinking like a power of D is required.

This does not contradict #943's obstruction: (1) is not the uncompleted
squarefree source mu(n)z^omega(n). It has different nonsquarefree coefficients,
while its prime coefficients and all squarefree coefficients are unchanged.

For independent phases, revealing them one by one gives the usual conditional
expectation martingale, starting at the UNKNOWN native A and ending at C.
Its expected 2k-th moments increase, rather than making the spurious smooth
mean excursion from #938. This is not an inexpensive random starting theorem:
the initial moment is exactly the unproved native moment. Nor is deterministic
freezing of a realized phase to 1 a martingale assertion.

## 5. Direct fixed-scale stability when only large primes are active

This removes the shorter-scale envelope from a useful restricted variant.
Let Y>=2 and put z_p=0 whenever Np<=Y. At other primes allow arbitrary disk
values. For fixed r>=2 and the same fixed W,

    |C_u,z,r(D)-A_u(D)| <<_{K,W,r} D Y^(-r),              (10)

uniformly in ALL rows, all masks, every permitted profile, and D>=1.

Proof. In (7) remove the term d=1. Elementary ideal counting gives
|A_u(T)|<=C_W T whenever the sum is nonzero. Therefore the difference is
at most C_W D times the nonconstant kernel mass at weight (Nd)^(-1).
The active-prime majorant has logarithm

    2 sum_{Np>Y} sum_{m>=r+1} (Np)^(-m)/m <<_r Y^(-r),

using at most two prime ideals per integer norm and the convergent integer
tail; for bounded Y absorb a fixed constant. Exponentiating and subtracting
1 gives O_r(Y^(-r)). This proves (10), without a prime number theorem. QED.

Take r=2 and Y=max(2,ceil(D^(1/4))). For any probability law on these profiles,
Minkowski and the reverse triangle inequality give

    | ||C(D)||_{Lp(w x pi)}-||A(D)||_{Lp(w)} |
        <<_{K,W} (sum_u w(u))^(1/p) sqrt(D).              (11)

Hence the completed and native diagonal moment estimates are equivalent at
this SINGLE D,H, with no hidden smaller-scale input. For the circle laws (8),
the native moment is also a lower bound on the completed moment.
This is square-root stability for arbitrary angular width, after explicit
compensation, not a bound for either unknown moment.

## 6. Analytic continuation: artificial singularities disappear, genuine ones stay

For a fixed profile the Euler multiplier

    H_z,r(s)=product_p K_{z_p,r}(xi_u(p)(Np)^(-s))

is holomorphic and nonvanishing for Re(s)>1/(r+1). Its logarithm converges
normally on compact subsets there by (2), since the first term has degree
r+1. This statement is uniform over disk profiles on each such compact set.
On Re(s)>1 the exact Euler identity is

    sum_n f_z,r(n) xi_u(n)(Nn)^(-s)
        = H_z,r(s) sum_n mu_K(n)xi_u(n)(Nn)^(-s).          (12)

Where the native source is the specified inverse Hecke series, this is
H_z,r(s)/L_u^S(s), and (12) supplies the corresponding continuation.
The zeros and poles have EXACTLY the native orders in Re(s)>1/(r+1), because
H never vanishes there. At r=2 this includes the whole half-plane Re(s)>1/3.
No nonvanishing of L is assumed or concluded. A genuine off-critical zero
would survive this completion as a pole. The spurious phase-dependent pole
or branch at 1 is removed locally; the true zero-detection problem is not.

## 7. What this attack does and does not establish

The positive result is a canonical macroscopic deformation, a constant-cost
critical norm transfer, an exact nonnegative averaged excess, and the direct
large-prime square-root stability (11). All have full finite-horizon and
nonunit-mask semantics. These are proposed complete arguments, not accepted
integration, global novelty claims, or a solution of the native moment.

The explicit sufficient target at r=2, Y=max(2,ceil(D^(1/4))) is

    sum_{0<Nu<=D^h} E|C_u,Z,2(D)|^(2k) << D^(h+k+epsilon), (OPEN)

with the original test and twist coverage. By (8) and (11) this is equivalent
to the full native moment at the SAME scale. At fixed small-prime profiles,
(6) instead gives the same-height envelope equivalence. Neither version is
asserted easier merely because it is an average. In (9) the j=0 summand
already is the ENTIRE native moment, so bounds on nonconstant phase modes
alone cannot finish the proof. The outstanding arithmetic cancellation
across the original squarefree prime/composite degrees remains necessary.

The elementary extreme-point observation explains this limitation. If a
random coefficient c(p) obeys |c(p)|<=1 and E c(p)=-1, then Re c(p)>=-1
with expectation -1, hence c(p)=-1 almost surely. An unbiased unit-bounded
randomization cannot move the prime coefficient. Our completion respects
that restriction rather than hiding it in an independence argument.
