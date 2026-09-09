# Literal prime-cutoff moments: a complete transition law and a forced negative square

Status: PROPOSED COMPLETE COMPONENT PROOFS; independent review required. RH is NOT proved.
Scope: the ordinary von Mangoldt source, including every prime power through X; the fixed s=2 invariant germ; every moment order. No numerical zero data or RH hypothesis.
Local labels PT-1 through PT-6 are not canonical claim IDs. Classical PNT, Cauchy estimates and characteristic-function convergence are credited; no external priority claim.

## 1. Exact source and the proposed completion attempt

Keep the center of PR #793/pass3:

    s(u)=(1+sqrt(9+4u))/2, d(u)=2s(u)-1,
    f(u)=xi(s(u))/xi(2), q(u)=f'(u)/f(u),
    q(u)=sum_(j>=0) (-1)^j m_j u^j, m_j=p_(j+1).

The square root is the branch positive at zero. Define

    P_X(s)=sum_(2<=k<=X) Lambda(k) k^(-s),
    L_X(s)=1/s+1/(s-1)-log(pi)/2+digamma(s/2)/2-P_X(s),
    q_X(u)=L_X(s(u))/d(u)=sum_(j>=0)(-1)^j m_j(X)u^j.

X is real and at least 2; using floor X makes the same prime-power cutoff. Define the real polynomial functional ell_X(t^j)=m_j(X), and ell(t^j)=m_j.

The attempted construction was to prove positivity of every unshifted Hankel matrix of the finite arithmetic source, then pass to the coefficient limit using the preceding moment-completion theorem. The next result proves that this particular construction is impossible. It does not refute the moment-completion theorem or positivity of the FULL xi source.

## 2. PT-1: every finite cutoff fails, with an explicit sparse witness

For n>=1 put B_n(t)=1-(2t)^n. For every finite X there is n=O(log(X+2)) such that

    ell_X(B_n^2)<-1/12.                                    (PT1)

An explicit admissible n is any positive integer satisfying

    36(9+8X)(16/17)^n < 1.                                 (PT2)

Thus the (n+1)-by-(n+1) unshifted Hankel matrix is not PSD. This is an all-cutoff analytic theorem, not extrapolation from finitely many cutoffs. The vector has only two nonzero entries, at degrees 0 and n; its Euclidean norm grows with n. The -1/12 is a quadratic value, NOT a uniform negative eigenvalue bound.

### Proof

Cancellation of the 1/s term gives the exact identity

    q_X(u)=1/(u+2)+h_X(u),
    h_X(u)=[digamma(s(u)/2)-log pi-2P_X(s(u))]/[2d(u)].      (PT3)

The pole at u=-2 has residue one for EVERY finite X. In the actual completed xi germ it is absent: the pole of zeta at s=1 cancels the completion zero. A finite prime sum cannot perform that cancellation.

h_X is analytic on |u|<=17/8. There Re d>=1/sqrt(2)>1/2, |d|<5, Re s>=3/4 and |s|<=3. With z=s/2, the convergent digamma expansion

    digamma(z)=-gamma_E-1/z+sum_(k>=1) z/[k(k+z)]

shows |digamma(z)|<7, using 0<gamma_E<1, Re z>=3/8, |z|<=3/2 and sum k^-2<2. Since log pi<2 and |d|>1/2, the gamma part of h_X has modulus at most 9. Also

    |P_X(s)|<=4 X^(1/4)log X<=4X,

by Lambda(k)<=log k, integral comparison and log X<=X^(3/4). Hence |h_X|<=M_X:=9+8X. Cauchy's estimate gives

    m_j(X)=2^(-j-1)+e_j, |e_j|<=M_X(8/17)^j.

At zero,

    m_0(X)-1/2=-(gamma_E+log pi+2P_X(2))/6<-1/6,           (PT4)

using gamma_E>0 and pi>e. Therefore

    ell_X(B_n^2)=m_0(X)-2^(n+1)m_n(X)+4^n m_(2n)(X)
       <=-1/6+3M_X(16/17)^n.

PT2 proves PT1. All moments required for this test are at most order 2n. QED.

## 3. A source-only bound for the ACTUAL moments

The positive theta formula makes every nonconstant Taylor coefficient of f positive. Its exact safe value is

    f(10)=xi(4)/xi(2)=2pi/5<4/3.

Positivity of coefficients gives f(4)-1 <=(2/5)(f(10)-1)<2/15 and f'(4)<(f(10)-f(4))/6<1/18. Hence, for |u|<=4,

    |f(u)|>13/15, |q(u)|<5/78,
    |m_j| <= 5/(78*4^j).                                  (PT5)

In particular this small disk is zero-free by a direct source bound, not a zero census or RH. The positivity-of-coefficients input is proved by expanding the cosh in the split theta integral at invariant coordinate 2; it also appears in the parent packet.

The authenticated interval computation in verify.py proves m_0>1/50 and ell(B_1^2)>0, ell(B_2^2)>0. PT5 then proves, for EVERY n>=3,

    ell(B_n^2) >=1/50-(5/78)(2*2^(-n)+4^(-n))>0.            (PT6)

Thus these same sparse squares are positive for the full source at EVERY order, although they eventually become negative for EACH finite prime cutoff. This does not establish positivity for arbitrary polynomials; their nonzero constant term dominates in the small source disk.

## 4. PT-2: a uniform-in-order arithmetic tail estimate

Set y=log X and

    eps_X=sup_(v>=X) |psi_C(v)-v|/v,
    psi_C(v)=sum_(k<=v) Lambda(k).

This eps_X tends to zero by PNT. The classical quantitative PNT gives eps_X=O(exp(-c sqrt(log X))) for some c>0 after reducing c to absorb polynomial factors. No new PNT estimate or explicit numerical value of c is claimed.

Put r(z)=sqrt(9-8z),

    g(z)=(3-r(z))/2, H(z)=(1+1/r(z))/2,
    F_y(z)=H(z)exp(y(g(z)-1)),
    C_n(y)=[z^n]F_y(z)/(1-z).

Then for EVERY X>=2 and EVERY n>=0,

    |2^(n+1)(m_n(X)-m_n)-C_n(log X)| <=5 eps_X.             (PT7)

The bound is uniform over the complete, unbounded degree range, not just fixed n.

### Positive decreasing coefficient kernel

For x>=1 let

    k_n(x)=2^(n+1)(-1)^n [u^n] x^(-s(u))/d(u)
          =2^n x^(-1/2)/(sqrt(pi)n!)
             * int_0^infty v^(n-1/2) exp(-9v/4-(log x)^2/(4v))dv. (PT8)

The elementary Gaussian Laplace integral proves the equality. The right side is positive and strictly decreasing in x: both x-dependent factors are decreasing. Differentiation and all fixed-degree integrals converge absolutely. Source expansion on a sufficiently small disk with Re s>1 gives

    2^(n+1)(m_n(X)-m_n)=sum_(k>X) Lambda(k) k_n(k).

The continuous tail is exactly

    int_X^infty k_n(x)dx
       =[z^n] 2X^(1-s(-2z))/[(s(-2z)-1)d(-2z)]
       =C_n(y).                                           (PT9)

The factor two and pole normalization are important. At n=0 both sides of PT9 are 2/(3X).

### A probability law bounds both the mass and boundary term

g and H have nonnegative Taylor coefficients, g(1)=H(1)=1, g(0)=0. Therefore g is the probability generating function of a positive integer jump J, H that of a nonnegative integer V, and F_y that of

    Z_y=V+sum_(i=1)^(N_y) J_i, N_y~Poisson(y),

with all variables independent. Consequently C_n(y)=Pr(Z_y<=n) lies in [0,1]. This is a representation of a deterministic CONTINUOUS prime-tail kernel, not a random model for actual primes.

Also

    -partial_y C_n(y)=[z^n] D(z)F_y(z),
    D(z)=(1-g(z))/(1-z)=1/(1-g(z)/2), D(1)=2.

The coefficients on the right are nonnegative and have total mass 2. From PT9,

    0<=X k_n(X)=-partial_y C_n(log X)<=2.                   (PT10)

### PNT transfer with no degree-dependent loss

Stieltjes integration by parts on (X,infinity), retaining its lower boundary, gives an error bounded by

    eps_X [X k_n(X)+int_X^infty x(-k_n'(x))dx]
       =eps_X[2X k_n(X)+int_X^infty k_n(x)dx]
       <=5 eps_X.

The upper boundary vanishes at every fixed degree. This proves PT7 simultaneously with the same constant for every degree. In particular no uniform coefficient error has been multiplied by an infinite prime mass. QED.

## 5. PT-3: Gaussian cutoff transition at n=2log X

The generating functions give

    E J=2, E J^2=10, E J^3=122,
    E V=2, Var V=22.

Hence E Z_y=2y+2 and Var Z_y=10y+22. More sharply,

    (Z_y-2y)/sqrt(10y) converges in law to a standard normal.

For completeness, its characteristic function is

    H(exp(it/sqrt(10y)))
    *exp(y(g(exp(it/sqrt(10y)))-1)-2y it/sqrt(10y)).

Taylor expansion about 1, justified because g and H are analytic in a neighborhood of 1, makes this tend to exp(-t^2/2). The characteristic-function continuity theorem proves the statement. No quantitative Berry--Esseen rate is asserted.

Let Phi denote the standard normal distribution function. Combining PT5 and PT7 proves the actual arithmetic limit, for each fixed real z,

    2^(n+1)m_n(X) -> Phi(z),
    n=floor(2log X+z sqrt(10log X)), X->infinity.            (PT11)

This is not a limit for the full xi moments: the full moments contribute O(2^-n) after this normalization. It is the crossover of the SPURIOUS finite-cutoff pole caused by the omitted prime tail.

## 6. PT-4: the sparse negative square has an exact transition

For n as in PT11, Chebyshev's inequality for Z_y also gives C_(2n)(y)->1. Since m_0(X)->m_0, PT7 proves

    ell_X(B_n^2) -> m_0+1/2-Phi(z).                        (PT12)

In particular choose any fixed z with Phi(z)>1/2+m_0; the square is negative for all sufficiently large X. The actual source certificate puts m_0 between 1/50 and 1/40. No numerical quantile is needed for the theorem.

Away from the transition, for fixed theta>0 different from 1 and 2 and n=floor(theta log X), the three limits are

    theta<1:       m_0;
    1<theta<2:     m_0+1/2;
    theta>2:       m_0-1/2<0.                              (PT13)

Thus for every eta>0 a negative sparse square occurs by degree at most (2+eta)log X+O(1), for all sufficiently large X. This is an upper bound on a detection degree, not a proof that no other polynomial detects failure earlier. The Gaussian transition is sharp for THIS specific test family.

## 7. PT-5: what this closes and what it does not

These theorems close the proposed 'truncate the prime source, prove all moment signs, then take a positive limit' construction negatively. The cutoff needed to avoid even this sparse obstruction at degree N must grow exponentially with N (up to the stated asymptotic qualifications). Keeping an analytically certified infinite tail, as in the parent's Euler--Maclaurin moment certificate, is NOT the refuted procedure.

PT7 is an unconditional all-degree arithmetic approximation. Its natural scale is 2^(-n), whereas actual xi moments are much smaller; it does not give the exponentially finer, sign-resolving error needed for arbitrary high-order Hankel minors. The proof does not show such sharper error is impossible, only that the displayed bound does not supply it.

The full-stream PSD theorem remains open. The artificial pole at u=-2 is a defect of q_X, not a zero of actual xi and not a counterexample to RH.

## 8. PT-6: subtract the artificial pole with its exact continuum tail

Rather than discard the obstruction, define the balanced germ

    qbal_X(u)=q_X(u)-X^(1-s(u))/[(s(u)-1)d(u)].

Its apparent pole at u=-2 cancels. With moments mbal_j(X), PT7 gives

    |2^(j+1)(mbal_j(X)-m_j)|<=5 eps_X, EVERY j>=0.         (PT14)

Thus the classical PNT supplies an all-order, absolute error certificate in this fixed rescaled moment coordinate. For Hbal_X=[mbal_(i+j)(X)] and H=[m_(i+j)] on l2, the matrix-unit expansion is absolutely trace-norm summable and gives

    ||Hbal_X-H||_1 <=10 eps_X.                             (PT15)

Indeed each entry error is at most (5eps_X/2)2^(-i-j), and summing these rank-one matrix-unit norms gives 10eps_X. H itself is trace class by PT5. This bound is not asserted optimal; even unbalanced cutoffs converge in weaker norms, and norm convergence by itself has never implied positivity.

There is NO claim that Hbal_X is PSD. In fact the new rational interval certificate proves mbal_0(2)<0. For a cofinal balanced construction, proving its negative part tends to zero would still require new arithmetic information, not merely PT14 or PT15.

The outcome is therefore an exact repair of the unmatched-pole approximation, with a proved all-degree error, but NOT a completion of its positivity step. The displayed rescaled error does not resolve arbitrarily small Hankel eigenvalues.
