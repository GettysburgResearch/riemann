# Horizon-faithful Dickman completion and two exact boundary profiles

**Status:** PROPOSED COMPLETE COMPONENT PROOFS; independent mathematical review required. The requested RH completion is NOT obtained.
**Scope:** ordinary primes, the actual 67-free Mobius coefficients, causal L2 norms, and an explicit continuum completion. The unconditional norm results below are on Re(s)=1, not throughout Re(s)>1/2.
**Parent:** PR #793 at `8eee76d79a5a608f5d6b89c9205cc7bba637f66a`, especially `pass6-euler-energy-attack/PROOF.md`. All parent files remain unchanged.
**Imports:** classical quantitative PNT and Mertens estimates, Fourier/Laplace Plancherel, and the classical Dickman and Buchstab functions. The transform and delay identities needed here are proved below. No external novelty or priority is claimed.

Local labels DC1--DC6 are confined to this packet. An asymptotic assertion is never inferred from the finite checker.

## 1. Exact source; regroup the whole missing-prime contribution

Fix q=67 and X>=q, and put L=log X. Let

    mu_q(n)=mu(n)1_(q does not divide n),
    D(s)=1/[zeta(s)(1-q^-s)],
    P_X(s)=product_(p<=X,p!=q)(1-p^-s),
    M(y)=sum_(n<=y) mu_q(n),
    M_X(y)=sum_(n<=y, P^+(n)<=X) mu_q(n).

The n=1 terms are included. Squarefreeness is already enforced by mu. Define

    F_a(x)=exp(-a x)M(exp x),
    F_(X,a)(x)=exp(-a x)M_X(exp x),     x>=0.

F_(X,a) is in L2 for every a>0. Its Laplace/Fourier transform on Re(s)=a is P_X(s)/s. No such membership of F_a is assumed below except where proved or explicitly stated.

Let r_X(n) be one when every prime divisor of n is greater than X, and zero otherwise; r_X(1)=1. Dirichlet convolution gives EXACTLY

    mu_q  * r_X = mu_q 1_(P^+<=X),
    M_X(Y)=sum_(r<=Y) r_X(r) M(Y/r).                       (DC1)

This follows prime by prime, or on Re(s)>1 from P_X(s)=D(s) product_(p>X)(1-p^-s)^-1 and then coefficient comparison. It retains all rough prime powers. In particular, for X<=Y<X^2, only primes can occur among the r>1 terms, so

    M_X(Y)-M(Y)=sum_(X<p<=Y) M(Y/p)
              =sum_(m<=Y/X) mu_q(m)[pi(Y/m)-pi(X)].        (1)

The second identity is an interchange of finite sums, not an average-prime model. It also follows directly because two primes greater than X cannot divide an integer below X^2.

## 2. DC2: the first omitted-prime profile, with all original signs

Set

    g_a(y)=exp(-a y) sum_(m<=exp y) mu_q(m)(exp(y)/m-1),
    g(y)=g_1(y)=sum_(m<=exp y)mu_q(m)/m-exp(-y)M(exp y).

For every fixed a>0 and V>1, uniformly for 0<=y<=log V,

    L X^(a-1)[F_(X,a)(L+y)-F_a(L+y)]
                      =g_a(y)+O_(a,V)(1/L).              (2)

Indeed, for X>max(q,V), insert (1) and the PNT expansion
pi(cX)-pi(X)=(c-1)X/L+O_V(X/L^2), uniformly for 1<=c<=V. At a moving endpoint exp(y)=m the new summand is zero, so the assertion is uniform across integer breakpoints too. Notice the factor X^(a-1); the unscaled boundary error grows when a<1.

Partial summation gives the exact identities

    g(y)=integral_0^y exp(-v)M(exp v)dv,
    g_a(y)=exp((1-a)y)g(y),
    g_a'(y)=(1-a)g_a(y)+F_a(y)  almost everywhere.          (3)

We use the classical unconditional estimates, for some c,C>0,

    |psi(x)-x|+|M(x)| <= C x exp(-c sqrt(log x)), x>=2,     (PNT)

with constants adjusted for the finite Euler factor. The estimate for mu_q follows from M_q(x)=sum_(j>=0) M_standard(x/q^j), splitting at q^j=sqrt x. No numerical value of c or C is certified here.

Since D has a simple zero at 1 and D'(1)=q/(q-1)=:c_q, (PNT) and Abel summation imply sum mu_q(n)/n=0. Thus g(y)=-integral_y^infinity F_1(v)dv and g is in L2. Its norm is nonzero, since g(y)=1-exp(-y) on 0<y<log2. In particular

    C_g:=||g||_2^2 >= log2-5/8 >1/16.                    (4)

With Fourier convention fhat(t)=integral_0^infinity f(x)exp(-itx)dx,

    ghat(t)=D(1+it)/[(1+it)it],                            (5)

where t=0 is the removable value c_q. This uses an actual causal L2 function; it does not infer causality from a finite meromorphic boundary integral.

## 3. A uniform prime-tail formula on the line Re(s)=1

For t!=0 let

    J(v)=integral_1^infinity exp(-ivu)du/u,  v!=0,

as the ordinary oscillatory improper integral. Quantitative PNT gives

    P_X(1+it)=D(1+it) exp(J(tL)+delta_X(t)),
    |delta_X(t)| <= C(1+|t|)exp(-c sqrt L),                (6)

The logarithms are specified by sums of local Euler logarithms and their convergent tails; (6) is an exponential identity and has no arbitrary logarithm-branch choice.

Here are the complete error terms. On Re(s)=1 and t!=0,

    log(P_X(s)/D(s))
      =sum_(n>X) Lambda(n)/(log n)n^-s
       -sum_(p<=X,k>=2,p^k>X) 1/(k p^(ks)).               (7)

The second sum is O(X^-1/2), uniformly in t. Split its primes at sqrt X: each small prime contributes at most 2/X, and the remaining geometric tails are bounded by 2 sum_(n>sqrt X)n^-2. All prime powers of q cancel correctly in (7), since q<=X.

Replacing dpsi by dx in the first sum gives J(tL). Stieltjes integration against psi(x)-x bounds the remainder by

    C exp(-c sqrt L)/L
    +C(1+|t|) integral_L^infinity exp(-c sqrt v)/v dv.

Absorb the polynomial factors by decreasing c. The lower Stieltjes endpoint is included. This proves (6), including the infinite prime tail rather than a fixed finite sum.

Two elementary consequences used in the global norm proof are

    |P_X(1+it)| <= C L,
    |D(1+it)| <= C log^2(3+|t|) for |t|>=1.              (8)

The first follows from sum_(p<=X)1/p=log log X+O(1). For the second, apply (6) with an auxiliary cutoff Y satisfying log Y=A log^2(3+|t|), with A a sufficiently large fixed constant. Its delta is bounded and |J(t log Y)|<=2/(|t|log Y); then solve (6) for D and use the first bound. Thus no unproved critical-strip estimate for reciprocal zeta is imported. Near zero D(1+it)=c_q it+O(t^2).

Integration by parts and splitting the integral at 1/|v| give absolute constants such that

    |exp(J(v))-1| <= C/|v|,                       v!=0,
    J(v)=exp(-iv)/(iv)+O(v^-2),                   |v|>=1.
                                                                  (9)

For 0<|v|<=1, Re J(v)=-log|v|+O(1), proving the first assertion there. For |v|>=1 integrate twice and use |J(v)|<=2/|v|. In particular

    L exp(itL)[exp(J(tL))-1] -> 1/(it)              (t!=0). (10)

## 4. DC3: a full L2 boundary profile and the exact leading norm error

**Theorem.** With a=1, define G_X(y)=L[F_(X,1)(L+y)-F_1(L+y)] for y>=0. Then

    G_X -> g in L2(0,infinity),
    ||F_(X,1)-F_1||_2 ~ sqrt(C_g)/log X,
    ||F_(X,1)||_2^2
       =||F_1||_2^2+C_g/(log X)^2+o((log X)^-2).          (DC3)

Thus the raw genuine Euler-product approximants DO converge strongly at a=1, with an identified leading error. This is an unconditional PNT-level theorem, not an RH-strength estimate at a>1/2.

### Proof, including all frequencies

The difference is supported in x>=L by exact coefficient agreement. Therefore

    Ghat_X(t)=L exp(itL)[P_X(1+it)-D(1+it)]/(1+it).

First replace the numerator by D(1+it)[exp(J(tL))-1]. Equations (9)--(10) bound the resulting expression by

    C |D(1+it)|/[|t|sqrt(1+t^2)],

an L2 majorant by (8) and the simple zero at t=0. Dominated convergence and Plancherel give limit (5).

To justify the replacement, choose T_L=exp(c sqrt L/4) using the constant c in (6). On |t|<=T_L, delta_X(t)=O(exp(-c sqrt L/2)), after enlarging X. Also D exp(J(tL))/(1+it) has uniformly bounded L2 norm, by (9). Multiplying this error by L still tends to zero. On |t|>T_L, the squared norm of the actual scaled expression is at most

    C L^2 [L^2+log^4(3+T_L)]/T_L ->0.

The ideal expression has a vanishing tail by its common L2 majorant. This pays the COMPLETE frequency integral. A pointwise Euler-product limit alone would not do so.

Consequently ||F_(X,1)-F_1||^2=C_g/L^2+o(L^-2). Finally (PNT) gives ||1_(x>=L)F_1||_2=O(exp(-c' sqrt L)). Since the difference is supported there, its cross term with F_1 is o(L^-2). Expanding the square proves the final assertion. QED.

## 5. DC4: the next, macroscopic error is the derivative of Buchstab's function

Define the classical Buchstab function by omega(u)=0 for u<1,

    omega(u)=1/u, 1<=u<=2,
    (u omega(u))'=omega(u-1), u>2,

with continuous matching at integers. Its regular derivative r(u)=omega'(u) for u>1 is extended by zero for u<1. The jump of omega at 1 is NOT included in r.

Elementary method-of-steps bounds give 0<=omega<=1, hence |r(u)|<=1/u for u>2. Therefore r belongs to L2 and

    7/24 <= C_r:=integral_1^infinity |r(u)|^2du <=19/24.    (11)

The lower contribution is the exact integral of u^-4 on (1,2).

For Re z>0, put E1(z)=integral_1^infinity exp(-zu)du/u. If Omega(z) is the Laplace transform of omega, distributional differentiation at the jump gives

    -z Omega'(z)=exp(-z)(1+Omega(z)),
    1+Omega(z)=exp(E1(z)),
    rhat(v)=iv[exp(J(v))-1]-exp(-iv)=:R(v).                (12)

The second identity follows by solving the first with Omega(+infinity)=0. The third is its L2 boundary identity; the subtraction exp(-iv) removes exactly the jump at 1. It is also justified directly from (9): R(v)=O(1/|v|) at infinity and is bounded near zero. There is no unremoved Dirac delta in this L2 formula.

Define the first-profile residual on x>=0 by

    H_X(x)=F_(X,1)(x)-F_1(x)-L^-1 1_(x>=L)g(x-L).

Then the stronger scaling theorem is

    L^2 H_X(L u) -> c_q r(u) in L2(0,infinity),
    ||H_X||_2 ~ c_q sqrt(C_r) L^-3/2.                     (DC4)

Proof. Discarding the same exponentially small all-frequency error as in DC3, its Fourier transform at v/L, multiplied by L, is exactly

    [D(1+iv/L)/((1+iv/L)(iv/L))] R(v).

The bracket is uniformly bounded on the real axis by (8), including its removable value at zero, and converges to c_q at each fixed v. Dominated convergence with |R|^2, followed by Plancherel, proves DC4. The discarded norm is exponentially small, so multiplying it by L^(3/2) is harmless. QED.

This describes the aggregate signed missing-prime contribution on TWO scales, without replacing it by a diagonal. It also explains why a formal second Taylor correction with factors 1/t^2 cannot simply be estimated term by term at t=0: the Buchstab profile supplies the complete regular combination.

## 6. DC5: an all-orders causal completion, rather than another raw truncation

Let rho denote the classical Dickman function, not a zeta zero in this section:

    rho(u)=1 for 0<=u<=1,
    u rho'(u)=-rho(u-1) for u>1.

It is positive and decreasing, with rho(u)<=1/floor(u)!. One elementary proof uses
u rho(u)=integral_(u-1)^u rho(v)dv. A first zero contradicts this identity; the delay equation then proves monotonicity and the factorial bound. Consequently

    nu(u)=-rho'(u)>=0, supported on [1,infinity),
    integral nu(u)du=1,

and every exponential moment of nu is finite.

Define Ein(z)=sum_(k>=1)(-1)^(k+1)z^k/(k k!), an entire function. Its relation to the principal E1 is E1(z)=Ein(z)-gamma-log z. The Dickman Laplace transform is

    integral_0^infinity exp(-zu)rho(u)du=exp(gamma-Ein(z)). (13)

To verify it, Laplace-transform the delay equation to get z Rho'(z)=(exp(-z)-1)Rho(z); its normalization at positive infinity is 1/z because rho=1 initially. This determines the constant exp(gamma). Analytic continuation is permitted by the factorial bound.

The SINGLE-VALUED ENTIRE correction is

    C_X(s)=exp(gamma)(s-1)L exp(-Ein((s-1)L))
          =1-integral_1^infinity nu(u)exp(-(s-1)L u)du.   (14)

On Re s>1 it equals exp(-E1((s-1)L)); formula (14), not an ambiguous logarithm across a cut, defines it everywhere. It has a simple zero at s=1. Set

    Pcheck_X(s)=P_X(s) C_X(s).

At damping a>0 define the causal convolution kernel

    k_(X,a)(x)=L^-1 exp((1-a)x)nu(x/L), x>=L,
    Fcheck_(X,a)=F_(X,a)-k_(X,a)*F_(X,a).                 (15)

The kernel is in L1, so Fcheck is in L2 for each fixed X,a. Its transform is Pcheck_X(a+it)/(a+it). Most importantly,

    Fcheck_(X,a)(x)=F_a(x), 0<=x<L.                       (16)

Thus the completion changes NOTHING on the horizon where the prime cutoff is an exact representation of the source. It corrects the missing continuum collectively after that boundary. It is not claimed to supply the missing actual primes exactly afterwards.

At a=1, k_(X,1) is a probability density, hence the correction operator I-k* has L2 norm at most 2 and has nonnegative real quadratic part. It is not self-adjoint and is NOT a contraction. Indeed

    |C_X(1+2i/L)|=exp(Ci(2))>1.

The cosine-integral series gives Ci(2)=gamma+log2-1+1/6-2/135+..., whose remaining alternating tail is positive. Also gamma+log2>1, by the increasing lower sequence H_n-log(n+1). Hence Ci(2)>41/270. Long causal wave packets concentrated near this frequency verify the strict operator-norm lower bound. A probability-density correction is not automatically energy-decreasing.

**Theorem.** For some c'>0,

    ||Fcheck_(X,1)-F_1||_2 << exp(-c' sqrt(log X)).         (DC5)

Proof. On |t|<=T_L, (6) and (14) cancel the entire factor exp(J(tL)) exactly. The difference is D(1+it)(exp(delta_X(t))-1)/(1+it), with exponentially small L2 norm. Outside T_L, use |C_X(1+it)|<=2 and (8); the squared tail is O((L^2+log^4(3+T_L))/T_L), again exponentially small after reducing c'. The t=0 value follows by the simple zeros in D and C_X, not by dividing by zero. Plancherel proves DC5. QED.

This removes both DC3 and DC4 error profiles, and all the other continuum rough-prime layers, in one explicit causal operation. The Dickman kernel and its transform are classical; the claim is the stated source/horizon and norm calculation, not a new special function or a proof of RH.

## 7. Exact connection to the moment and Hardy routes

The same correction differentiates to the continuum tail used by the other routes:

    d/ds log C_X(s)=X^(1-s)/(s-1).                        (17)

Reconstruct an approximation to ordinary zeta, including the missing q factor, by

    Zetacheck_X(s)=1/[(1-q^-s)Pcheck_X(s)].

Its logarithmic derivative is exactly

    Zetacheck_X'/Zetacheck_X
      =-sum_(p<=X) log p/(p^s-1)-X^(1-s)/(s-1).           (18)

Adding 1/s+1/(s-1)-log(pi)/2+digamma(s/2)/2 gives the corresponding completed-xi logarithmic derivative germ. Thus this product correction is the integrated, causal version of a balanced continuum-tail source in the moment and Hardy constructions.

The cutoff convention matters. Equation (18) retains ALL powers of primes p<=X. The parent's hard prime-power cutoff retains only p^k<=X. Their difference is the explicit absolutely convergent tail

    sum_(p<=X,k>=2,p^k>X) (log p)p^(-ks),

bounded by O_sigma(X^(1/2-sigma)log X) on every fixed Re s>=sigma>1/2. Split p at sqrt X as in (7), now retaining log p. No equality between the two cutoff conventions is silently asserted.

Neither the finite completed germ's Hankel matrices nor its Hardy operator is proved positive. A source correction is not a positive determinant realization, and rho>=0 does not turn I-k* into a positive operator.

## 8. DC6: why the completion proved above does not finish RH

The intended final step was to extend DC5 from a=1 to a sequence a decreasing to 1/2. Two precise costs remain.

First, below one the kernel in (15) is exponentially tilted. Put theta=(1-a)L>0. Integration by parts in (13) gives

    ||k_(X,a)||_1=1+theta exp(gamma-Ein(-theta)),
    |C_X(a)|=theta exp(gamma-Ein(-theta)).                 (19)

For fixed 1/2<a<1,

    log |C_X(a)| ~ X^(1-a)/[(1-a)log X].                  (20)

Indeed -Ein(-theta)=integral_0^theta (exp(v)-1)dv/v is asymptotic to exp(theta)/theta. The correction itself has a growing operator norm below one; Young's inequality and the probability-kernel argument on the line one do not extend uniformly. Cancellation between P_X and C_X must be proved BEFORE taking their norms separately.

Second, classical (PNT) bounds the needed discrepancy integral on Re(s)=1. At any fixed sigma<1 its absolute majorant contains

    integral_L^infinity exp((1-sigma)v-c sqrt v)dv/v,

which diverges. This is a failure of that bound, not proof that the actual signed integral diverges and not evidence against RH.

A precise remaining endpoint is local boundedness of Pcheck_X throughout Re(s)>1/2. If for every compact K there the family is bounded uniformly in X, Montel and the already proved agreement on Re(s)>1 give a holomorphic continuation of D to that half-plane. Hence zeta has no zero there, and reflection proves RH. Conversely RH, the classical bound psi(x)-x=O(sqrt x log^2 x), and the discrepancy formula give local uniform convergence Pcheck_X->D on Re(s)>1/2 (with the removable zero at 1 retained). The tail error is O_K(X^(1/2-sigma_K)log X), after including the prime-power correction in (7). This is a classical completed Euler-product criterion, not an assertion of the required bound.

Alternatively uniform causal L2 bounds for (15) at every a>1/2 would suffice directly by (16) and Fatou. Such bounds are NOT proved or claimed equivalent here.

All three original routes remain active. This pass constructs a horizon-faithful all-orders continuum completion and proves its strong norm convergence at the classical line, with two sharper raw-error profiles. It does NOT prove the all-half-plane bound, signed Mertens cancellation, all-order moment signs, Hardy positivity, or RH. Independent review remains required.
