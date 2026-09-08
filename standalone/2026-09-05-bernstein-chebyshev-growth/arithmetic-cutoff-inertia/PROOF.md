# Finite arithmetic cutoffs have infinite negative index

Status: PROPOSED COMPLETE COMPONENT PROOFS; independent mathematical review required.
The original all-epsilon coefficient bound, positivity of the full operator, and RH are NOT proved.
Scope: every finite prime-power cutoff of the literal arithmetic operator in PR #792;
complete or finitely truncated gamma source; one separately defined continuum-tail repair.
Parent: PR #792 at 39c13367f4b3956631ea1e00fac6c3005fc32057,
cross-route-hardy-laguerre/BRIDGE.md, Git blob 81d7d5db7a25f5875a08c10235fdb514d67cc744.
Local labels AC-1 through AC-4 apply only to this packet. No priority claim.
What was run: exact rational identities and integrity/refusal controls, not an infinite prime evaluation.
Smallest remaining gap: a signed bound for the FULL arithmetic source, not positivity of its raw cutoffs.

## 1. Which object is being truncated

Keep a=3/4, b=3/2, c=1/2, c_j=2j+1/2, and

    C_b=(1-gamma_E-log(2pi))/3,   q_n=Lambda(n)/sqrt(n).

For every real X>=2 define

    W_X(x)= (1/2)e^(c|x|)+C_b e^(-b|x|)
            +sum_(j>=1) e^(-c_j|x|)/(c_j^2-b^2)
            -(1/3)sum_(2<=n<=X) q_n
                      [e^(-b|x-log n|)+e^(-b|x+log n|)],
    T_X(t,u)=b e^(-a(t+u)) W_X(t-u),            t,u>=0.       (1)

The cutoff includes ALL prime powers n<=X with their von Mangoldt weights.
W_X contains the ENTIRE gamma series. Define T_(X,J) by keeping only
j<=J in that series, with the SAME C_b and growing exponential. J=0 is
also allowed. T_(X,infinity)=T_X.

These are literal arithmetic-source cutoffs, not finite zero models and
not the matrix compressions P_M T P_M of the FULL operator T. The parent's
arithmetic decomposition proves that all these operators are self-adjoint
and trace-class and that T_(X,J)->T in trace norm as X,J->infinity.
No part of that theorem says that a cutoff is positive.

The new result is stronger than one counterexample:

**AC-1 (uniform explicit negative witness).** For EVERY finite X>=2 and
J in {0,1,2,...,infinity}, put

    L=30(1+log X),
    chi(s)=s^3(1-s)^3 for 0<=s<=1, zero otherwise,
    phi_L(t)=chi(t/L),
    h_L(t)=phi_L''(t)-(1/4)phi_L(t),
    f_X(t)=e^(at) h_L(t).                                   (2)

Then f_X is a nonzero real L2 function supported in [0,L] and

    <f_X,T_(X,J)f_X> <= -(4/3)||h_L||_2^2 <0,               (3)
    <f_X,T_(X,J)f_X>/||f_X||_2^2
                 <= -(4/3)e^(-45)X^(-45).                  (4)

The constants are conservative, not optimized. This is an all-X analytic
result. In particular no raw finite arithmetic cutoff can be factored B*B.

**AC-2 (inertia).** Every T_(X,J) has infinitely many negative eigenvalues,
counting multiplicity. T_X with the entire gamma series also has infinitely
many positive eigenvalues. The eigenvalues accumulate only at zero.

These statements do not assert negativity of T. The test f_X depends on X;
no fixed negative vector is transported to the limit by (3).

## 2. The exact multiplier on a moment-annihilating test space

Use Fourier convention hhat(omega)=int_R h(t)e^(-i omega t)dt. Let h be
compactly supported, belong to H1(R), and satisfy

    int e^(ct)h(t)dt=int e^(-ct)h(t)dt=0.                    (5)

A translate puts its support in [0,infinity). Set f=e^(at)h on that half-line.
Define

    Omega(omega)=Re psi_Gamma(1/4+i omega/2)-log pi,
    V_X(omega)=Omega(omega)
                 -2sum_(2<=n<=X)q_n cos(omega log n).

**Exact quadratic identity.**

    <f,T_X f> = (b/(2pi)) int_R
                  V_X(omega)/(b^2+omega^2) |hhat(omega)|^2 d omega.  (6)

This is NOT a claimed Fourier transform of the growing function e^(c|x|)
on all test functions. The constraints (5) are essential.

### 2.1 Why the growing exponential can be handled

Let v=e^(c|.|)*h. The two constraints make v identically zero outside the
convex hull of the support of h. Distributionally,

    (D^2-c^2)v=2c h,
    vhat(omega)=-2c hhat(omega)/(omega^2+c^2).

Consequently the (1/2)e^(c|x|) term contributes the multiplier
-c/(omega^2+c^2). This argument uses a compactly supported v, not a
Fourier transform of an exponentially growing kernel. For (2), (5) follows
immediately by two integrations by parts because phi_L and phi_L' vanish
at both endpoints. Alternatively v=2c phi_L in that case.

### 2.2 Gamma terms and the normalization of Omega

The other terms have ordinary integrable Fourier transforms. Their gamma
multiplier is

    G(omega)= -c/(omega^2+c^2)+2b C_b/(omega^2+b^2)
       +sum_(j>=1) 2c_j/[(c_j^2-b^2)(omega^2+c_j^2)].        (7)

It equals Omega(omega)/(omega^2+b^2). To check the constants, multiply (7)
by omega^2+b^2, use b^2-c^2=2, and write each gamma summand as

    2c_j/(c_j^2-b^2)-2c_j/(omega^2+c_j^2).

The first fraction equals 1/(2j-1)+1/(2j+2). The convergent scalar difference

    sum_(j>=1)[1/(2j-1)-1/(2j+2)]=log 2+1/2

then gives precisely the real part of the digamma partial-fraction formula

    psi(z)=-gamma_E+sum_(k>=0)[1/(k+1)-1/(k+z)].             (8)

The positive gamma kernels may be summed inside their quadratic forms by
Tonelli. Their coefficient series sum_j 1/(c_j^2-b^2) converges, so there
is also no operator convergence issue. One must not separate two divergent
harmonic sums when using (8).

The shifted n term has Fourier multiplier

    -2q_n cos(omega log n)/(b^2+omega^2),

because b=3/2. This proves (6), including both shift orientations.
The multiplier in (6) is bounded: it behaves as O(log(2+|omega|)/omega^2)
at infinity. Thus the identity also extends to the stated H1 tests by
ordinary L2 approximation, or directly by the convolution calculation.

## 3. An elementary global majorant

Reflection and duplication of digamma give

    Omega(0)=-gamma_E-pi/2-3log 2-log pi < -4.               (9)

For the displayed inequality it is enough that gamma_E>=0, pi>3,
log 2>1/2, and log pi>1. All are elementary; e<3<pi gives the last one.
Taking real parts in (8) gives the exact, nonnegative difference

    Omega(omega)-Omega(0)
      =sum_(k>=0) (omega/2)^2 /
          [(k+1/4)((k+1/4)^2+(omega/2)^2)]
      <=18 omega^2.                                        (10)

Indeed sum_(k>=0)(k+1/4)^(-3)<=64+8=72 by integral comparison.
Since cos v>=1-v^2/2 for ALL real v, define

    Q_X=sum_(2<=n<=X)q_n,
    alpha_X=4+2Q_X,
    beta_X=18+sum_(2<=n<=X)q_n(log n)^2.

Then, for every real omega,

    V_X(omega)<=-alpha_X+beta_X omega^2,
    beta_X/alpha_X <= max(9/2,(log X)^2/2),
    1/b^2+beta_X/alpha_X <= 5+(log X)^2/2.                  (11)

Only q_n>=0 and log n<=log X were used. No prime number theorem, zero
verification, or conjectural cancellation enters these bounds.

For every h satisfying (5), (6), (11), and Plancherel therefore imply

    <f,T_X f> <= -(alpha_X/b) ||h||_2^2
                    +(beta_X/b+alpha_X/b^3)||h'||_2^2.     (12)

For clarity, the scalar inequality used is

    (-alpha+beta v)/(b^2+v)
      =-alpha/b^2+(beta+alpha/b^2)v/(b^2+v)
      <=-alpha/b^2+(beta/b^2+alpha/b^4)v,   v>=0.

## 4. Proof of the explicit witness

The function chi in (2), extended by zero, has its first two derivatives
zero at the endpoints and belongs to H3(R). Thus h_L is in H1(R), is
compactly supported, and satisfies (5). Exact polynomial integration gives

    I0=int_0^1 chi^2=1/12012,
    I1=int_0^1 (chi')^2=1/770,
    I2=int_0^1 (chi'')^2=2/35,
    I3=int_0^1 (chi''')^2=36/7,
    I1/I0=78/5, I2/I1=44, I3/I2=90.                        (13)

The norm identities, retaining the derivative cross terms, are

    ||h_L||_2^2=L[I2/L^4+2c^2 I1/L^2+c^4 I0],
    ||h_L'||_2^2=L[I3/L^6+2c^2 I2/L^4+c^4 I1/L^2].          (14)

Integration by parts has no endpoint terms: chi, chi', and chi'' vanish
where needed. In particular h_L is not zero, and

    ||h_L'||_2^2/||h_L||_2^2 <=90/L^2.                     (15)

For ell=log X>=0 and L=30(1+ell),

    (90/L^2)(5+ell^2/2)<=1/2.                              (16)

After multiplication by (1+ell)^2, the difference of right minus left is
ell+(9/20)ell^2>=0. Substitution in (12) proves

    <f_X,T_X f_X><= -alpha_X/(2b)||h_L||_2^2
                    <=-(4/3)||h_L||_2^2.

Also ||f_X||_2^2<=e^(2aL)||h_L||_2^2, which proves (4).

Every discarded gamma summand is a POSITIVE operator. Consequently

    T_(X,J) <= T_X

in quadratic-form order. The same witness and both bounds apply to every
finite J. This completes AC-1. Smooth compactly supported witnesses can
also be obtained by approximation, preserving strict negativity; the
piecewise-polynomial witness above is already a valid L2 test.

A rational-length variant is available without evaluating log X: take
L=30(1+k) for any integer k>=log X, for example k=ceil(log_2 X). The
same proof gives (3) and its corresponding e^(-3L/2) Rayleigh bound.

## 5. Infinite negative index; both signs with the full gamma source

We give a constructive translation argument, rather than claiming that
one negative vector proves infinite index. Fix X,J and let h be the
negative witness in Section 4. Write its convolution-form value as -kappa,
kappa>0, before multiplying by the outer factor b.

For |x|>log X, the cutoff kernel has the exact shape

    W_(X,J)(x)=(1/2)e^(c|x|)+B_X e^(-b|x|)
                      +sum_(1<=j<=J) e^(-c_j|x|)/(c_j^2-b^2),
    B_X=C_b-(2/3)sum_(2<=n<=X)q_n cosh(b log n).             (17)

This also holds for J=infinity; the gamma coefficient sum is finite.
Take translates h_i(t)=h(t-iR), i=0,1,..., with R>L+log X. For i!=j the
growing-exponential cross term is EXACTLY ZERO by (5). All other cross
terms are bounded by

    C_(X,J,h) exp(-b R|i-j|),

where one may take

    C_(X,J,h)=||h||_1^2 exp(bL)
                  (|B_X|+sum_(1<=j<=J)1/(c_j^2-b^2)).

Choose R still larger so that

    2C_(X,J,h) exp(-bR)/(1-exp(-bR)) < kappa/2.

Each finite Gram matrix of the convolution form on the h_i has diagonal
-kappa and off-diagonal absolute row sum below kappa/2. It is strictly
negative definite. For the actual half-line operator use f_i=e^(at)h_i.
These are linearly independent L2 functions with compact support and have
the same quadratic matrix multiplied by b. Thus for every integer m there
is an m-dimensional negative subspace. The min-max principle for compact
self-adjoint operators gives infinitely many negative eigenvalues.

For T_X with the FULL gamma series there are also infinitely many positive
eigenvalues. Classical digamma asymptotics give

    Omega(omega)=log(|omega|/(2pi))+o(1), |omega|->infinity.

The finite trigonometric sum is bounded, so V_X is positive on some open
frequency interval. Choose a nonzero smooth compactly supported bump eta
and a frequency omega_0 in that interval. Long packets

    phi_H(t)=H^(-1/2)eta(t/H)e^(i omega_0 t),
    h_H=(D^2-c^2)phi_H

satisfy (5). Their value in (6) tends, as H->infinity, to

    b (omega_0^2+c^2)^2 V_X(omega_0)/(b^2+omega_0^2) ||eta||_2^2>0.

This follows by Fourier scaling and dominated convergence: eta's transform
is Schwartz, while the multiplier grows at most polynomially after the
differential factor. A translate gives positive half-line support.
The same separated-translate construction now gives arbitrarily large
positive subspaces. No positive-index claim for finite J is needed.
This proves AC-2.

## 6. AC-3: the first natural continuum-tail repair is not automatically positive

The raw cutoff leaves the growing exponential uncompensated. A natural
repair replaces only the MISSING prime measure by its continuous average:

    W_X^av(x)=W_X(x)-(1/3)int_X^infinity y^(-1/2)
                  [e^(-b|x-log y|)+e^(-b|x+log y|)]dy.       (18)

Unlike W_X, this repaired function is bounded and integrable. For x>=log X
the added continuum term is exactly

    -(1/2)e^(cx)+[X^2/6-1/(3X)]e^(-bx),

so the growing exponential cancels. Nevertheless positivity is not automatic:

**AC-3.** The operator with kernel b e^(-a(t+u)) W_2^av(t-u)
is NOT positive semidefinite. It has infinitely many negative eigenvalues.

Here is a proof not requiring numerical evaluation of any special function.
The ordinary Fourier transform of (18) is

    What_X^av(omega)=1/(b^2+omega^2) * [V_X(omega)
      +2sqrt(X){c cos(omega log X)+omega sin(omega log X)}
                             /(c^2+omega^2)].               (19)

One can obtain (19) by integrating (18) piecewise. Equivalently its safe
arithmetic logarithmic-derivative source is

    L_Gamma(r)-sum_(n<=X)q_n e^(-r log n)-X^(c-r)/(r-c).

The pole at r=c is removable after combination. Taking the sum at r=iomega
and r=-iomega in the parent's Laplace formula gives (19); integrability
justifies the ordinary Fourier boundary evaluation.

For X=2 the numerator of (19) at omega=0 is

    Omega(0)+sqrt(2)(4-log 2)<0.                             (20)

Indeed Omega(0)<-5: use gamma_E>1/2, pi/2>3/2, 3log2>2, and log pi>1.
For a fully elementary bound on gamma_E, the integral comparison gives
gamma_E>H_6-log 7, while H_6=49/20 and log7<39/20. The latter follows
already from sum_(k=0)^6 (39/20)^k/k!>7. Also log2>2/3 follows from strict
Jensen for 1/x on [1,2]. Finally sqrt2<3/2, so

    sqrt2(4-log2)<(3/2)(10/3)=5.

This proves (20). Continuity leaves a negative frequency interval. Long
low-frequency packets and then separated translates give infinitely many
negative directions, as in Section 5. In this integrable-kernel case no
exponential-moment constraints are required.

This refutes positivity of ALL such repaired cutoffs, not positivity on
some unproved cofinal subsequence, and not every possible completion of a
finite source. Both the discrete and continuous missing tails converge in
trace norm: the parent's atom estimate integrated against dy bounds the
continuous tail by O(X^(-1/4)). Thus norm convergence does not fix this sign
problem for the repaired family either.

## 7. AC-4: why trace-norm convergence has not supplied the missing sign

The parent proved (for finite J>=1)

    ||T-T_(X,J)||_1<=1/(4J)+(4/3)X^(-1/4)(4log X+19).        (21)

AC-1 and AC-2 are compatible with (21), including if T is positive. The
negative gap in (4) tends to zero and is much smaller than the available
error bound. The location/shape of the witness changes with X. One may not
pass a varying negative witness through a norm limit as though its gap
were fixed. Infinite negative index is not continuous in trace norm.

The exact full-source positivity endpoint remains the parent's assertion:

    T>=0 -> |d_n|<=d_0 -> original c_n(2) all-epsilon bound -> RH.

If T were positive, its omitted-prime tail would necessarily obey, on the
EXPLICIT witness in (2),

    <f_X,(T-T_X)f_X> >= alpha_X/(2b)||h_L||_2^2.             (22)

This is a conditional necessary tail-sign statement, not a proved bound.
Its left side retains all missing prime shifts and their interference.
Taking their absolute trace norms does not prove (22).

The proposed completion "prove every finite arithmetic cutoff positive,
then pass to the trace-norm limit" is now rigorously REFUTED for this exact
source. The distinct construction "prove every compression of the FULL
operator positive" is not refuted, and is still OPEN. Neither (3) nor (20)
is evidence that the full operator is negative or that RH is false.

This pass therefore completes the analysis of a specific attempted sign
mechanism, not the user's requested RH proof. No new signed full-prime
upper bound or full-source sum-of-squares factorization has been obtained.

## 8. Classical inputs and validation boundary

The only imported analytic facts needed beyond the parent's explicitly
constructed kernel are the digamma partial fractions, reflection/duplication
identities and high-frequency asymptotic, Fourier/Plancherel theory, and the
compact self-adjoint min-max principle. Source details are in SOURCES.md.
No PNT or zero-set theorem is used to prove AC-1 through AC-3.

The rational checker reconstructs the polynomial moments, endpoint
identities, norm algebra, scalar majorant and multiplier identities at its
stated finite controls. Those tests do not machine-prove Fourier analysis,
infinite inertia, or the global-in-X theorem. The complete arguments above
require independent mathematical review.
