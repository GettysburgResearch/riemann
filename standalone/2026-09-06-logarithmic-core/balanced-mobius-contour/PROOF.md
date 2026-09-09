# A bounded-coefficient, two-moment Möbius completion for the actual annular scalar

Date: 2026-09-07.
Status: PROPOSED COMPONENT PROOFS; independent mathematical and code review required.
RH, the sparse deep-failure estimate, and positivity at unbounded lengths are NOT proved.
Parent research: PR #803 at 47b8a507aea0ad6e1dd0ab23dfd2035a0eb03abb.
Local labels BMC1--BMC5 are not canonical claim IDs.

This is a direct attempt to estimate the arithmetic behind the sparse-sign
criterion. It gives an explicit short Dirichlet polynomial with the exact
Möbius prefix, two prescribed Taylor data, uniformly bounded coefficients,
and logarithmic coefficient mean-square. A finite convolution identity then
replaces the logarithmic derivative by expressions with zeta in the NUMERATOR.
The critical-line contour and its complete high-frequency tail are justified
without RH. The remaining low-frequency signed estimate is NOT proved.

The convolution identity is an application of the classical quadratic
Vaughan/Heath-Brown identity, not a new inversion principle. The critical-line
approach in the different odd-Möbius source of PR #805 prompted this attempt.
Neither its observable nor its estimates are imported as our source. Sources
and external analytic inputs are listed in SOURCES.json.

## 1. Freeze the native observable

For u>0 put

    w(u)=u/3-1/(192u^2),     1/4<u<=1,
         1/(3u^2)-u/192,     1<u<4,
         0,                 otherwise.

The endpoint values are zero and the center is continuous. Write

    a0=integral w(u)du=45/128,
    J(s)=integral_(1/4)^4 w(u)u^(s-1)du
        =[65/64-(4^(s-1/2)+4^(-s+1/2))/8]
          /[9/4-(s-1/2)^2].                               (1)

The two apparent singularities in the quotient are removable: the integral
is entire. On every fixed vertical strip J(s)=O((1+|Im s|)^-2). In particular

    j(t):=J(1/2+it)
         =[65/64-(1/4)cos(t log4)]/(9/4+t^2)>0,
    j(t)<=81/[64(9/4+t^2)].                               (2)

Throughout Lambda(p^k)=log p for ALL prime powers. The source remains

    D(m)=(1/m)sum_n Lambda(n)w(n/m^2)-a0*m+1/4,  m>=2.    (3)

No prime-only replacement, random coefficient model, or finite zero census
is used. Our construction covers every real m>=2. Set Y=ceil(2m), so Y>=4.
The coefficient lemmas below in fact hold for every integer Y>=2.

## 2. BMC1: two moment conditions with bounded coefficients

Let

    M_Y=sum_(1<=n<Y) mu(n)/n,
    L_Y=sum_(1<=n<Y) mu(n)log(n)/n,
    ell_Y=(1/Y)sum_(Y<=n<2Y)log n,
    q_Y(s)=(1/Y)sum_(Y<=n<2Y)n^(1-s),

    b_Y=(M_Y*ell_Y-L_Y-1)/log2,
    a_Y=-M_Y-b_Y.                                        (4)

Define the finite Dirichlet polynomial

    p_Y(s)=sum_(n<Y)mu(n)n^-s
             +q_Y(s)[a_Y+b_Y*2^(1-s)].                   (5)

Equivalently its real coefficients p_Y[n] are mu(n) for n<Y,
a_Y*n/Y at Y<=n<2Y, b_Y*2n/Y at indices 2n with Y<=n<2Y,
and zero elsewhere. Those three sets of indices are disjoint. In particular
its support is n<4Y. No factorization beyond the Möbius prefix is required to
specify the correction; logs of ordinary integers enter ell_Y.

**BMC1.** The construction satisfies, exactly,

    p_Y(1)=0,             p_Y'(1)=1,
    p_Y[n]=mu(n) for n<Y,
    |p_Y[n]|<20 for all n,
    S_Y:=sum_n |p_Y[n]|^2/n < 130+log Y.                  (6)

The all-Y inequalities require neither PNT nor RH. They are proved below,
not inferred from small numerical Möbius sums.

### 2.1 The moment equations

Since q_Y(1)=1 and q_Y'(1)=-ell_Y,

    p_Y(1)=M_Y+a_Y+b_Y=0,
    p_Y'(1)=-L_Y-(a_Y+b_Y)ell_Y-b_Y log2=1.               (7)

Both conditions are important. The second fixes the residue of the proxy in
section 3; a zero at one alone leaves a source-dependent main-term deficit.

### 2.2 An elementary bound for the logarithmic Möbius mean

For integer N>=1,

    sum_(n<=N)mu(n)floor(N/n)=1.

As {N/1}=0, this gives |N sum_(n<=N)mu(n)/n -1|<=N-1,
and hence |sum_(n<=x)mu(n)/n|<=1 for all real x>=1.

Put m(x)=sum_(n<=x)mu(n)/n and

    F(x)=sum_(n<=x)mu(n)log(x/n)/n.

Finite divisor rearrangement gives the EXACT identity

    sum_(n<=x)(mu(n)/n) H_floor(x/n)=1,                   (8)

where H_N=sum_(k<=N)1/k. We will use the elementary uniform remainder

    H_floor(y)=log y+gamma_E+epsilon(y),
    |epsilon(y)|<=1/y,                         y>=1.     (9)

Here is a proof including noninteger y. For N=floor y, the standard defining
limit of gamma and telescoping integrals give

    1/[2(N+1)] < H_N-log N-gamma_E < 1/(2N).

For example the difference equals sum_(k>=N)[log(1+1/k)-1/(k+1)].
Its kth summand is integral_0^1 (1-t)/[(k+t)(k+1)]dt. Bound from above by
1/[2k(k+1)] and from below by 1/[2(k+1)^2], then sum. Thus the upper side of
(9) follows from 1/(2N)<=1/y. For the lower side, when N>=2 use
log(1+1/N)<=1/N<=3/[2(N+1)]. For N=1 use log2<3/4. In either case
H_N-log y-gamma_E > -1/(N+1)>=-1/y. This proves (9).

Insert (9) in (8). Since |m(x)|<=1 and 0<gamma_E<1,

    |F(x)-1| <= gamma_E + floor(x)/x < 2.                (10)

All sums here include n=1. This elementary O(1) statement is much stronger
than integrating |m(t)|<=1 alone, which would lose a log x.

At x=Y the term n=Y in F vanishes. Therefore

    M_Y*ell_Y-L_Y-1
      =M_Y(ell_Y-log Y)+F(Y)-1.

Since 0<=ell_Y-log Y<log2, and log2>1/2, (10) proves

    |b_Y|<1+2/log2<5,       |a_Y|<6.                    (11)

### 2.3 The exact coefficient norm

The disjoint supports give

    S_Y=sum_(n<Y)mu(n)^2/n
          + [(3Y-1)/(2Y)](a_Y^2+2b_Y^2).               (12)

The two corrections cost less than (3/2)(36+50)=129. The prefix costs at
most H_(Y-1)<=1+log Y. This proves (6); their individual coefficients have
magnitudes below 12 and 20 respectively. Thus the completion has logarithmic,
not polynomially growing, diagonal energy. It is not a bound on p_Y at an
individual critical-line point or in an arbitrary low-frequency norm.

There is also an unconditional sharp leading order for this coefficient norm:

    S_Y = (1/zeta(2)) log Y + O(1).                       (12a)

Indeed mu(n)^2=sum_(d^2|n)mu(d). Summing and using the absolutely convergent
Euler product at two gives sum_(n<=x)mu(n)^2=x/zeta(2)+O(sqrt x).
Partial summation gives sum_(n<Y)mu(n)^2/n=(log Y)/zeta(2)+O(1).
The correction in (12) is uniformly less than 129. Every polynomial with
the same prefix has coefficient norm at least that prefix contribution,
so our construction costs less than 129 above this unavoidable lower bound.
No PNT or assumption about zeros enters this argument. This is near-minimal
DIAGONAL cost, not an assertion of near-minimal continuum energy.

## 3. BMC2: an exact finite logarithmic-derivative proxy

Use arithmetic Dirichlet convolution, let u(n)=1, e=delta_1, and let
logarithm denote the arithmetic function l(n)=log n, including l(1)=0.
For ANY finite p agreeing with mu at n<Y, put

    r=e-u*p,
    Lambda_p=2p*l-p*p*u*l.

As u*mu=e and mu*l=Lambda, direct convolution algebra gives

    Lambda-Lambda_p = Lambda*r*r.                        (13)

The residual r vanishes below Y. Lambda vanishes below 2. Consequently

    Lambda_p(n)=Lambda(n),                 n<2Y^2.       (14)

This includes prime powers; it is not restricted to squarefree indices.
When the first residual coefficient r(Y) is nonzero, the discrepancy at
2Y^2 is exactly log2*r(Y)^2. Hence an infinite equality is NOT asserted.

The Dirichlet series of Lambda_p is, initially on Re s>1,

    mathscr L_p(s)=-2 zeta'(s)p(s)+zeta(s)zeta'(s)p(s)^2. (15)

This function is NOT globally -zeta'/zeta. Its defining formula has no
reciprocal-zeta poles. It is meromorphic with a possible pole only at s=1.
Its equality with the native coefficients holds only in (14).

### 3.1 Why both moment constraints are needed

If p(1)=0 and p'(1)=d, write p(1+z)=dz+O(z^2) and
zeta(1+z)=z^-1+gamma_E+O(z). Inserting these expansions in (15) gives

    Res_(s=1) mathscr L_p(s)=2d-d^2=1-(d-1)^2.            (16)

There is no double or triple pole in this case. If p(1) is nonzero, a triple
pole is generally present. With p=p_Y from (5), d=1 and the residue is
exactly one. Thus the pole of the actual Mangoldt main term is retained,
not accidentally reduced by an unproved near-one derivative estimate.

At Y=ceil(2m), the support of w(n/m^2) is n<4m^2<=Y^2<2Y^2.
Equation (14) therefore gives an exact identity for the FULL native scalar:

    D(m)=(1/m)sum_n Lambda_(p_Y)(n) w(n/m^2)-a0*m+1/4.   (17)

There are no discarded source terms in (17). The polynomial depends on the
chosen m-window, so holomorphy of (15) does not continue the original global
logarithmic derivative across any zeros.

## 4. BMC3: an unconditional critical-line identity

For every real m>=2, take Y=ceil(2m). Then

    D(m)=1/4+(1/pi) Re integral_0^infinity
       j(t) mathscr L_(p_Y)(1/2+it) m^(2it) dt.           (18)

The integral is absolutely convergent. In particular it has no principal
value prescription at a critical-line zeta zero: zeta is in the numerator
and (15) is regular there. This is a finite-source identity, not a
zero-free assumption used to move the native logarithmic derivative.

Proof. Mellin inversion for the continuous compact weight gives

    (1/m)sum Lambda_(p_Y)(n) w(n/m^2)
      =(1/(2pi i)) integral_(c) J(s)mathscr L_(p_Y)(s)m^(2s-1)ds,

initially at any fixed c>1. Both the Dirichlet series and the integral are
absolutely convergent there. The zero-valued outside endpoints of w need no
half-weight convention. Use a fixed c between 1 and 2.

For each fixed Y the Dirichlet polynomial is bounded on this vertical strip.
The classical zeta convexity estimate and Cauchy's formula for its derivative
give, for any epsilon>0,

    |zeta(1/2+it)|+|zeta'(1/2+it)|
                      <<_epsilon (1+|t|)^(1/4+epsilon),   (19)

and a sufficient uniform version on 1/2<=Re s<=c for large |t|. These are
imported classical analytic bounds, NOT numerical certificates here. They
follow from the approximate functional equation, the functional equation
and Phragmen--Lindelof; taking a circle of radius O(1/log |t|) gives the
derivative bound after absorbing its log loss into epsilon. No derivative
of an uncontrolled pointwise remainder is taken.

With epsilon<1/4, (1), (15), (19) make the critical integral absolutely
convergent and the horizontal contour sides tend to zero. The only crossed
pole is s=1 with residue J(1)m=a0*m, by (16). Subtract it as in (3) and pair
conjugate t-values. This proves (18).

This does NOT turn its signed square p_Y(s)^2 into |p_Y(s)|^2. The real part
and every mixed term remain essential.

## 5. BMC4: the entire high-frequency tail tends to zero

This is a genuine uniform estimate, not just convergence at each fixed Y.
For 0<epsilon<1/2 and all real m>=2, with Y=ceil(2m),

    D(m)=1/4+I_Y(m)
                 +O_epsilon((1+log Y)^2 Y^(-1/2+epsilon)),

    I_Y(m)=(1/pi) Re integral_0^Y
            j(t) mathscr L_(p_Y)(1/2+it)m^(2it)dt.         (20)

The implied constant depends on epsilon and the classical bound (19), but
not on Y or m. No numerical value or finite certified threshold is asserted.
The complete omitted absolute integral, not just an oscillatory remainder,
is bounded by this estimate.

We include an elementary mean-value argument rather than assuming an
unverified numerical large-sieve constant. If

    p(1/2+it)=sum_(n<=N)b_n exp(-it log n),
    S=sum |b_n|^2,

then on any interval of length U>0,

    integral |p(1/2+it)|^2dt <= [U+4N(1+log N)]S.         (21)

Indeed the diagonal is US. For n<k the absolute integral of the paired
cross term is at most 4|b_n b_k|/log(k/n). Since
log(k/n)>=(k-n)/k>=(k-n)/N, apply 2|b_n b_k|<=|b_n|^2+|b_k|^2,
then sum the harmonic rows. This proves (21) for arbitrary complex b_n,
with no spacing or source-cancellation premise.

For our p_Y use N=4Y, S=S_Y<130+log Y, and L=4N(1+log N).
On [U,2U], combine j(t)<<U^-2, (19), (21), and Cauchy--Schwarz only for
the LINEAR p term. For any sufficiently small epsilon>0 the two contributions
are bounded by constants times

    sqrt(S)[U^(-3/4+epsilon/2)
                   +sqrt(L)U^(-5/4+epsilon/2)],
    S[U^(-1/2+epsilon)+L U^(-3/2+epsilon)].               (22)

Use (19) with exponent 1/4+epsilon/2; its product then costs U^(1/2+epsilon).
Summing the geometric dyadic tails U=2^jY proves (20), since
L=O(Y(1+log Y)). The linear contribution decays faster than the displayed
bound. Larger epsilon follows by weakening a smaller-epsilon bound.

Thus high frequencies t>=Y are fully paid. The remaining finite interval
0<=t<=Y is NOT estimated at a sufficient scale. Applying (21) indiscriminately
near bounded t loses a factor O(Y), rather than producing a power saving
in the count of negative values of I_Y.

## 6. BMC5: exact source-preserving directions that defeat a universal absolute majorant

We test the claim that the Möbius prefix, both jets and the logarithmic
coefficient norm automatically control a low-frequency absolute integral.
It is false EVEN WITH ALL THREE conditions retained.

Let

    e_Y(s)=q_Y(s)(1-2^(1-s))^2.                          (23)

This polynomial is supported on the three disjoint sets n,2n,4n for
Y<=n<2Y, with coefficients n/Y,-4n/Y,4n/Y respectively. It has

    e_Y(1)=e_Y'(1)=0,
    sum |e_Y[n]|^2/n=13(3Y-1)/(2Y)<39/2,
    |e_Y[n]|<8,          support n<8Y.                   (24)

Therefore both p_Y+e_Y and p_Y-e_Y still have the exact original Möbius
prefix and the two jets in (6), all coefficients below 28 in magnitude,
and coefficient mean-square <300+2log Y.

For EVERY such polynomial the signed integral (18) is exactly the SAME
native D(m). This is not a counterfeit prime measure: different finite
representations reproduce the same prescribed finite prime-power sum.

There is an exact explanation for the cancellations. With r=1-zeta*p_Y,

    mathscr L_(p_Y+v)-mathscr L_(p_Y)
        =-2 zeta' v r + zeta zeta' v^2.                  (25)

For v supported at n>=Y, both Dirichlet series on the right begin at
n>=2Y^2; hence the compact arithmetic weight in (17) annihilates both.
If v(1)=v'(1)=0, neither term introduces a residue at one. Applying the
same legal contour shift shows that EACH signed integral on the right of
(25) is zero. All this holds for v=+/-e_Y.

In contrast, let I be a closed interval of positive length contained in
(0,infinity), small enough that zeta(1/2+it)zeta'(1/2+it) is nonzero on I.
Such an interval exists by analytic nonidentity and isolated zeros; no
particular ordinate or certified interval is claimed. Define the nonnegative
norm used in the triangle-inequality majorant of the quadratic term:

    A_I(p)=integral_I j(t)|zeta(1/2+it)zeta'(1/2+it)|
                              |p(1/2+it)|^2dt.           (26)

Uniform Riemann sums on this FIXED interval give

    Y^(-1/2+it) e_Y(1/2+it)
       -> (1-2^(1/2-it))^2 integral_1^2 u^(1/2-it)du.     (27)

The limit is continuous and nowhere zero on I: |2^(1/2-it)|=sqrt2>1,
and the integral equals [2^(3/2-it)-1]/(3/2-it), also never zero.
It follows, with an explicit positive integral as constant, that

    A_I(e_Y) ~ c_I Y,         c_I>0.                     (28)

By the parallelogram identity,

    A_I(p_Y+e_Y)+A_I(p_Y-e_Y)
          =2A_I(p_Y)+2A_I(e_Y)>=2A_I(e_Y).               (29)

For every sufficiently large Y, at least one of the TWO displayed,
completely specified representations has absolute majorant >=c_I Y/2,
although its diagonal norm is O(log Y), both jets are exact, its Möbius
prefix is unchanged, and its signed answer is exactly the native D(m).
This rules out a source-prefix/jet/diagonal-only universal subpower
majorant. It does NOT show A_I(p_Y) itself is large, does not refute a
special estimate for the distinguished p_Y, and is not an RH counterexample.
The sign choice in (29) can depend on Y; no single sign is asserted to
work for every Y.

## 7. The end-to-end attempt and the precise unproved step

The source-construction and high-frequency problems in this formulation
are closed on paper. The conclusion-producing assertion is still missing.
For integer k>=2 set m=k^2, Y=2k^2 and I_k=I_(2k^2)(k^2) as in (20).
The proved error tends to zero. Hence for all sufficiently large k,

    D(k^2)<-1    =>    I_k<-1,

because D=1/4+I_k+error and eventually |error|<1/4.
Consequently the following would finish through the pinned sparse-sign theorem:

    exists delta>0,C>0, for all K>=2:
       #{2<=k<=K : I_k<-1} <= C K^(1-delta).             (30)

Finite initial nodes can be absorbed in C. The exponent saving in (30) is
NOT proved. No bound of this type follows from (6), (21), or the existence
of the contour in (18). Even a simple eventual lower bound I_k>=-1 would
suffice, but that too is unproved.

The fixed raw-moment obstruction remains relevant. The present integral is
signed, with a square rather than a modulus square. Equation (29) shows why
an indiscriminate positive majorant can discard arbitrarily large exact
cancellations while retaining all local source constraints. The distinguished
completion (5), or a new rigorously selected one, would need a literal
Möbius-dependent estimate on the low-frequency interval. No such estimate
was obtained. Thus this is NOT an end-to-end proof of RH.

BMC1--BMC5 do not depend on the parent's unproved count premise or on its
operator-core or length-one positivity claims. Only implication (30) -> RH
uses the proposed sparse-sign consumer at its frozen source-qualified scope.
No new zero-free region, larger positive range, proof of all-length positivity,
or formal verification is asserted. Finite tests accompanying this manuscript
check exact source algebra, not the infinite analytic arguments.
