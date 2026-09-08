# Native theta marks, connected cumulants, and the exact remaining RH gate

Status: PROPOSED PROVED IDENTITIES, OBSTRUCTIONS, AND CONDITIONAL CLOSURE;
independent review required. The full RH-bearing inequality remains OPEN.
Scope: every fixed v>0; the literal positive theta density; all finite orders.
Dependencies: HEAT_BERNSTEIN.md; the elementary cosh product; the classical
Hausdorff moment theorem and Fredholm determinant facts as explicitly used.
What was run: exact rational controls in verify_exact.py, not a theta sweep.
Smallest remaining gap: all mixed Hausdorff differences H_(a,b) for b>=1.

## 1. A second, positive source decomposition of the same count

Keep exactly X and Phi from HEAT_BERNSTEIN.md. Fix v>0 and b=v+1/4. Define

    d mu_v(tau) = 2 Phi(tau) cosh(sqrt(b) tau) d tau / X(v),
    Y=tau^2,   c_j=pi^2(j+1/2)^2,
    p_j(Y)=vY/(c_j+bY),                     j=0,1,2,... .       (1)

mu_v is a probability measure with strictly positive density on (0,infinity)
and moments of every order in Y. Conditional on Y, let the B_j be independent
Bernoulli variables with probabilities p_j(Y). Then

    P_v(z)=X(vz)/X(v)
          = E_mu product_(j>=0) (1-p_j+p_j z).                 (2)

Indeed the genus-zero product for cosh(tau sqrt(u+1/4)) has zeros
u=-1/4-c_j/tau^2. Divide the product at u=vz by its value at u=v, then
integrate against mu_v. Since sum_j p_j<=vY sum_j c_j^(-1)=vY/2,
the conditional count N=sum_j B_j is finite almost surely. All exchanges
on bounded z sets follow from the superexponential theta tail; alternatively,
first prove (2) for 0<=z<=1 and use the locally uniform entire expansions.
The absolute product for bounded z is dominated by the positive product at
|z|, which is the same cosh ratio with a positive real parameter.

This is NOT the marking used in PR #785's integration-by-parts mixture.
That mixture has a separate vacuum and one forced occupation. The scalar
PGF is the same, but we do not identify the two marked probability spaces.
No unknown zero is used to define (1).

## 2. A native marked determinantal realization is impossible

**Theorem ASTRA-TC-05.** For every v>0 and every i!=j,

    Cov(B_i,B_j)=Cov(p_i(Y),p_j(Y))>0.                          (3)

Consequently the marked occupation process in (1) is not a determinantal
point process with a Hermitian positive-contraction kernel. It is not the
occupation marginal of such a process on an enlarged ground set either.

Proof. Conditional independence gives equality in (3). For an independent
copy Y',

    Cov(p_i(Y),p_j(Y))
       = (1/2) E[(p_i(Y)-p_i(Y'))(p_j(Y)-p_j(Y'))].             (4)

Each p_j is strictly increasing, and the Y law is nondegenerate, so the
integrand is positive on a set of positive measure and never negative.
For a Hermitian determinantal kernel K,

    Cov(1_(i occupied),1_(j occupied))=-|K_ij|^2<=0.

Restriction to a subset keeps this determinantal identity, proving the
assertion about enlarged ground sets. This only concerns Hermitian DPPs,
or gauge-invariant/number-preserving quasifree fermionic occupations. No
claim is made about arbitrary Gaussian states with anomalous pairings.

Quantitatively, if d is total variation distance between the native two-mode
law and any such determinantal two-mode law, (3) is at most 3d: the joint
probability changes by at most d and the product of the marginals by at most
2d. Thus d>=Cov(B_i,B_j)/3>0. Mark-preserving approximation is obstructed too.

The same argument applies to the PARENT marking without changing its source:
put Y=0 on its vacuum atom, and Y=tau^2 on its continuous theta component.
Conditional probabilities of its non-forced modes are again the increasing
p_j(Y), with p_j(0)=0. Its nontrivial continuous mass gives the same strict
positive covariance. A proposed dilation preserving these actual marks
therefore fails, not merely a synthetic substitute for them.

This does NOT refute the unmarked count determinant

    P_v(z)=det(I-K+zK).                                       (5)

Such a K, if it exists, need not realize the theta mode occupations B_j.
Under RH it does exist. Forgetting the marks is a substantial operation.

## 3. Even the high-mode tail count is overdispersed

Here use any nondegenerate Y>=0 with finite third moment. Set M_k=E Y^k,
V=Var(Y)>0, L=J+1/2, and

    s_J=sum_(j>=J) 1/c_j,     r_J=sum_(j>=J) 1/c_j^2,
    m_J(Y)=sum_(j>=J) p_j(Y), q_J(Y)=sum_(j>=J) p_j(Y)^2.

**Theorem ASTRA-TC-06.** If

    L >= max(1, 16 M_2/(3V), sqrt(32 b M_3/(3 pi^2 V))),       (6)

then the conditional Bernoulli tail N_J=sum_(j>=J) B_j satisfies

    Var(N_J)-E N_J >= (v^2 s_J^2 V)/2 > 0.                    (7)

Proof. Directly from (1),

    0<=v s_J Y-m_J(Y)<=v b r_J Y^2,
    E q_J <= v^2 r_J M_2.

Writing m_J=v s_JY-delta, expanding the variance, dropping Var(delta), and
using Cov(v s_JY,delta)<=E[v s_JY delta] gives

    Var(m_J) >= v^2 s_J^2 V - 2 v^2 b s_J r_J M_3.

Conditional variance gives the exact identity

    Var(N_J)-E N_J=Var(m_J)-E q_J.

For L>=1, integral comparison of the decreasing powers yields

    s_J >= 1/(pi^2 L),
    r_J <= pi^(-4) (L^(-4)+(1/3)L^(-3)),
    r_J/s_J^2 <= 4/(3L),
    r_J/s_J   <= 4/(3 pi^2 L^2).

The two error terms divided by v^2 s_J^2 are each <=V/4 under (6).
This proves (7). All conditions hold for the actual mu_v.

Every positive trace-class contraction count has
Var(N)-E N=-Tr(K^2)<=0. Therefore the high-mode tail count alone cannot have
such a determinant, even after changing basis or forgetting its individual
marks. It is not, however, the whole count. An unknown unmarked realization
of (5) need not restrict to this particular latent-source tail.

There is also a two-mode asymptotic obstruction. Let D_i be the discriminant
of the quadratic PGF of B_i+B_(i+1). It is exactly

    D_i=(E p_i-E p_(i+1))^2-4 Cov(p_i,p_(i+1)).                (8)

Since (c_i/v)p_i(Y)->Y and (c_i/v)p_(i+1)(Y)->Y in L2,

    (c_i^2/v^2) D_i -> -4V < 0.                              (9)

Dominated convergence follows from p_j<=vY/c_j and c_i/c_(i+1)->1.
Thus every sufficiently high adjacent pair has a PGF with nonreal zeros.

## 4. Keep all connected cumulants before taking a scalar sign

Let

    Q_m(Y)=sum_j p_j(Y)^m,       m>=1,
    p_n^*(v)=(-1)^(n-1) n [y^n] log P_v(1+y).

Q_m are conditional power traces; p_n^* are global logarithmic factorial
cumulants with a sign/factor convention, NOT occupation probabilities.
Write kappa(Z_1,...,Z_r) for the joint cumulant under mu_v, with
kappa(Z)=E Z. It can be defined without analytic moment-generating functions
by the finite partition formula

    kappa(Z_1,...,Z_r)
      =sum_partitions pi (|pi|-1)! (-1)^(|pi|-1)
                          product_(B in pi) E product_(i in B) Z_i.

**Theorem ASTRA-TC-07 (exact connected formula).** For every n>=1,

    p_n^* = sum_(r=1)^n (-1)^(r-1) n/r!
            sum_(m_1+...+m_r=n; m_i>=1)
              kappa(Q_(m_1),...,Q_(m_r))/(m_1...m_r).          (10)

Proof. Expand the conditional log PGF as
sum_(m>=1) (-1)^(m-1)Q_m y^m/m, then expand the logarithm of its exponential
average by the partition cumulant identity. Work to finite order n; every
necessary moment exists. The product sign is (-1)^(n-r), giving (10).
Equivalently truncate the modes, prove the polynomial-jet identity, and
pass in the finite required moments using Q_m<=Q_1<=vY/2.
No unjustified convergence of an infinite cumulant series is required.

The first four identities are

    p_1^*=E Q_1,
    p_2^*=E Q_2-Var(Q_1),
    p_3^*=E Q_3-(3/2)Cov(Q_1,Q_2)+(1/2)kappa(Q_1,Q_1,Q_1),
    p_4^*=E Q_4-(4/3)Cov(Q_1,Q_3)-(1/2)Var(Q_2)
              +kappa(Q_1,Q_1,Q_2)-(1/6)kappa(Q_1,Q_1,Q_1,Q_1).

By ASTRA-TC-04, the COMPLETE right side of (10) is strictly greater than

    (1-2^(-83)) (v/(v+226))^n,                all n>=1, v>0.    (11)

This is the positive all-order result of the pass. Individual connected
terms need not have the same sign. Equation (11) includes, for example,
Var(Q_1)<E Q_2, despite the positive pairwise occupation correlations.

## 5. A self-contained end-to-end conditional RH theorem

Define the mixed differences

    H_(a,b)(v)=sum_(j=0)^b (-1)^j binom(b,j) p_(a+j+1)^*(v),
                         a,b integers >=0.                    (12)

**Theorem ASTRA-TC-08.** At ANY ONE fixed v>0, the following are equivalent:

  (i) RH;
 (ii) H_(a,b)(v)>=0 for every a,b>=0;
(iii) P_v(z)=det(I-K+zK) for some positive trace-class contraction K.

Proof of (i)->(ii),(iii). The invariant product under RH has a_j>0 and
sum a_j^(-1)<infinity. Put k_j=v/(v+a_j) in (0,1). Then
P_v(1+y)=product_j(1+k_j y), p_n^*=sum_j k_j^n, and

    H_(a,b)=sum_j k_j^(a+1)(1-k_j)^b>=0.

The diagonal operator with eigenvalues k_j gives (iii).

Proof of (ii)->(i). By the Hausdorff moment theorem, s_n=p_(n+1)^* is the
moment sequence of a finite positive measure sigma on [0,1]. Its mass is
s_0=p_1^*. Write F(y)=P_v(1+y), so F(0)=1. On a disk about zero,

    F'(y)/F(y)=sum_(n>=0) (-1)^n s_n y^n
             =integral_[0,1] (1+t y)^(-1) d sigma(t).          (13)

The integral is analytic on D=C\(-infinity,-1]. It is locally uniformly
bounded there by compactness in t. The identity F'=gF, with g the integral,
continues throughout connected D. Uniqueness for the analytic differential
equation, or the local multiplicity comparison at a hypothetical zero,
shows F has no zero in D. Therefore all zeros of X are on the negative real
axis. For a zeta zero beta+i gamma with gamma!=0, the imaginary part of
rho(rho-1) is gamma(2 beta-1); real invariant zeros force beta=1/2. The
classical absence of real nontrivial zeta zeros handles gamma=0. This is RH.

Finally (iii)->(i) follows because every zero of its Fredholm product is
real and nonpositive in z. A k=1 eigenvalue is excluded by P_v(0)>0.
This proof uses no scalar-to-matrix positivity shortcut and no zero
simplicity assumption. The final implication is complete; (ii) is not proved.

## 6. Laguerre form of the still-open arithmetic inequality

Use the generalized Laguerre polynomial convention

    L_b^(a)(x)=sum_(j=0)^b (-1)^j binom(a+b,b-j) x^j/j!.

The heat formula for p_n^* gives the exact identity

    H_(a,b)(v) = b!/(a+b)! integral_0^infinity
                   x^a exp(-x) S(x/v) L_b^(a)(x) dx.           (14)

To verify it, substitute (11) of HEAT_BERNSTEIN.md in (12) and use
sum_j (-1)^j binom(b,j)x^j/(a+j)! = b! L_b^(a)(x)/(a+b)!.
This is a finite sum with convergent integrals. Rodrigues and integration
by parts equivalently give

    H_(a,b)(v) = (-1)^b / ((a+b)! v^b)
        integral_0^infinity exp(-x) x^(a+b) S^(b)(x/v) dx.     (15)

The zero-count bound gives S^(r)(t)=O_r(t^(-r-1/2)log(2/t)) near zero;
the boundary terms in these b integrations vanish like at least
x^(a+1/2)log(2/x). The infinite endpoint decays exponentially.

Positivity of S proves every H_(a,0)>0, uniformly in a and v. For b>=1,
Laguerre oscillation is real signed information. Bounding (14) by absolute
values or by the pointwise heat lower bound destroys it. Formula (15)
exhibits precisely the unpaid complete-monotonicity step.

## 7. The proof attempt and its current stopping point

Attempted chain:

    actual theta source -> positive Bernoulli fibers
      -> one marked quasifree dilation -> unmarked determinant -> RH.

The marked-dilation arrow is REFUTED by ASTRA-TC-05, with the high-mode tail
obstruction ASTRA-TC-06 showing that merely dropping the forced occupation
or retuning the high modes cannot repair it.

The repaired chain is

    actual theta source -> exact connected cumulants (10)
      -> ALL mixed differences (12) nonnegative -> determinant -> RH.

This pass proves the full b=0 face, not the b>=1 family. COUNTERFEITS.md
shows that even a positive smooth source, a critical strip, a correct low
zero prefix, and all b=0 signs do not force the missing inequalities.
A successful continuation must use the theta arithmetic beyond those data.
The source-cumulant expression is a concrete object for that attack, not
claimed weaker than RH. No end-to-end unconditional proof is deposited.
