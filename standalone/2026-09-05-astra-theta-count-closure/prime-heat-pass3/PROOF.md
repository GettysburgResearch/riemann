# Prime-side continuation of the invariant heat inequalities

Status: PROPOSED COMPLETE PROOFS in the stated regions; independent review
required. The unrestricted mixed inequality and RH remain UNPROVED.
Scope: actual xi, every derivative order specified below, all zeros with
multiplicity. No external novelty claim. Local IDs: ASTRA-PH-01 through 05.
Scientific base: PR790 at 401196451ef1b51e5ff4d84dd23bd75bbf9215a1.

## 1. Exact source formula; the endpoint terms disappear

Use the unchanged parent normalization

    A_rho=rho(1-rho),  S(t)=sum_(Im rho>0) exp(-A_rho t),
    D_m(t)=(-1)^m S^(m)(t),  t>0.

For m>=1 set d=1/4 and introduce the entire even test function

    F_(m,t)(z)=(z^2+d)^m exp(-t(z^2+d)),
    I_(m,t)=integral_R F_(m,t)(x) dx > 0,
    Fhat_(m,t)(ell)=integral_R F_(m,t)(x) exp(-i ell x) dx,
    Omega(x)=Re psi(1/4+ix/2)-log pi.

Here psi=Gamma'/Gamma, not a prime-counting function. For
w_rho=(rho-1/2)/i we have A_rho=w_rho^2+d. Evenness pairs the negative and
positive ordinates, hence the full zero sum is 2D_m. The Guinand--Weil
explicit formula, valid without RH for complex w_rho, gives

    4 pi D_m(t) = integral_R F_(m,t)(x) Omega(x) dx
                    -2 sum_(n>=2) Lambda(n)/sqrt(n) Fhat_(m,t)(log n).
                                                                  (PH1)

There are NO endpoint terms for m>=1: F_(m,t)(i/2)=0 exactly. For m=0 the
endpoint is nonzero and (PH1) without its correction must not be used.
All test functions decay faster than every power on each fixed horizontal
strip. All zero sums and prime sums used here converge absolutely. The
factor 2 on the prime sum and the factor 4pi on D_m are load-bearing.

Imported theorem: Guinand--Weil, in the normalization of Chirre--Goncalves,
Mathematische Zeitschrift 300 (2022), Proposition 5. Only that unconditional
proposition is used, NOT their RH-conditional main theorems. Their transform
uses exp(-2pi i x y); our ell is 2pi y. See SOURCES_REVIEW.md.

## 2. A uniform contour bound, derived from finite Gamma algebra

Put

    delta=td,  I0=Gamma(m+1/2)t^(-m-1/2),
    R_(m,l)=product_(k=0)^(l-1) (m-k)/(m-k-1/2),
    W_m(q)=sum_(l=0)^m R_(m,l) q^l/l!.

The empty product is 1. Direct binomial expansion and Gaussian integration
prove

    I_(m,t)=exp(-delta) I0 W_m(delta).                         (PH2)

For 0<=l<=m, 1<=R_(m,l)<=2^l. If l<=m/2, then R_(m,l)<2:
log R_(m,l)<=l/m<=1/2, using log(1+x)<=x. Thus

    W_m(q)<=exp(2q),
    W_m(q)<=3 exp(q)                 when m>=16q.              (PH3)

For the second assertion, split at l=m/2. The first part is <=2exp(q).
The other part is at most

    sum_(l>m/2) (2q)^l/l! <= 2^(-m/2) exp(4q) <=1,

since log 2>1/2 and m>=16q. The inequalities are strict where needed.
Also the truncated exponential lower bound gives

    exp(-delta) W_m(delta) >= 1-delta/(m+1).                  (PH4)

Indeed sum_(l>m) delta^l/l! <= delta exp(delta)/(m+1).

For y>1/2, the elementary identity

    |(x-iy)^2+d|^2=(x^2+y^2+d)^2-4dy^2

and the binomial integral give

    integral_R |F_(m,t)(x-iy)| dx
       <=exp(t(y^2-d)) I0 W_m(t(d+y^2)).                      (PH5)

Dividing by (PH2) gives two distinct, valid bounds:

    integral |F(x-iy)| / I <=exp(t(2d+3y^2))                 (all m>=1),
    integral |F(x-iy)| / I <4exp(2ty^2)                     (m>=16t(d+y^2)).
                                                                  (PH6)

For the second one, (PH3) bounds the numerator by 3I0 exp(2ty^2), and
(PH4) bounds I below by (15/16)I0. No large-order Gamma asymptotic is
needed in (PH6). All its constants are independent of m.

Shift the Fourier contour down to Im z=-y when ell>=0. Vertical sides
vanish, and the exponential contributes exp(-y ell). Therefore

    |Fhat(ell)| / I <= C_(m,t,y) exp(-y ell),                 (PH7)

where C can be either applicable bound in (PH6).

Let A(y)=sum_(n>=2) Lambda(n)n^(-y-1/2). This is an ordinary absolutely
convergent Euler sum, with no zero-free assertion in the critical strip.
For a=y-1/2>0, Lambda(n)<=log n and integration on [n-1,n] imply

    A(y)<=1/a^2+(log 2)/a.                                   (PH8)

Indeed log n<=log x+log 2 and n^(-1-a)<=x^(-1-a) there.
At y=2, a=3/2 and log2<3/4 give A(2)<17/18<1.
For y=1/2+1/(t+1), (PH8) gives A(y)<2(t+1)^2.
The Fourier contour is legal for every such y, since F is entire.

## 3. The archimedean lower bound retains the whole real integral

Euler--Maclaurin for psi, with periodic B1 of magnitude at most 1/2, gives

    psi(z)=log z-1/(2z)+integral_0^infinity B1(x)/(x+z)^2 dx.

For Re z=c>0 this implies |psi(z)-log z|<=1/c. In particular,

    Omega(x)>log|x|-6              (x!=0),
    psi(m+1/2)>=log m-1            (m>=1).                    (PH9)

For the first inequality, c=1/4, |z|>=|x|/2 and log(2pi)<2 suffice.
The logarithmic singularity of this lower bound at x=0 is integrable.
It is not a claim that Omega itself is singular.

Under the probability density F_(m,t)(x)/I_(m,t), binomial expansion gives

    E log|x|=(1/2) sum_(l=0)^m w_l psi(m-l+1/2)-(1/2)log t,
    w_l=R_(m,l)delta^l/(l! W_m(delta)).                       (PH10)

Every w_l is nonnegative and their sum is one. The recurrence for psi gives

    0<=psi(m+1/2)-psi(m-l+1/2)<=2l.

Using R_(m,l)<=2^l and W_m(delta)>=1, the weighted difference is at most
4delta exp(2delta). Consequently, with r=sqrt(m/t),

    integral F Omega / I
        > log r-13/2-(t/2)exp(t/2).                          (PH11)

Unlike a core-only estimate, this bound pays every part of the real-line
archimedean integral. It is uniform in m and t.

## 4. New common time interval and seven more decades of mixed depth

**Theorem ASTRA-PH-01 (explicit early-time source bound).** For m>=1 and
0<t<=1/10,

    D_m(t) > I_(m,t)/(4pi) [ log sqrt(m/t)-15 ].              (PH12)

Proof. Use y=2 in (PH6)--(PH8). Then C<=exp(25t/2)<=exp(5/4)<4 and
A(2)<1, so the normalized prime contribution in (PH1) is less than 8.
The last term in (PH11) is <1/2 for t<=1/10, so the archimedean part is
>log r-7. Subtract. This proof uses no finite zero verification.

For reference, e^(5/4)<4 follows from e<11/4 and (11/4)^5<4^4.

**Corollary ASTRA-PH-02.** Subject to the explicitly imported finite
verification and the pass2 theorem it supports,

    D_m(t)>0             for EVERY m>=0 and 0<t<=1/10;        (PH13)
    H_(a,b)(v)>0         for EVERY a>=0, v>0, 0<=b<=10^22.    (PH14)

Proof. The preserved pass2/SMALL_TIME_ALL_ORDERS.md, ASTRA-TC2-07, proves
D_m>0 for all t>0 and 0<=m<=10^15. For m>=10^15 and t<=1/10,
r>=10^8 and log r>16, so (PH12) is positive. This proves (PH13), including
m=0 via the parent theorem. It is not an induction on derivative order.

For (PH14), use the pass2 late-time theorem with H=3*10^12, M=10^22 and
tau=1/10. Its two overlap inequalities hold because

    2(M+1)<tau H^2,
    M log((H^2+1)/196)+log(32H^2)<60M+100<tau(H^2-226).       (PH15)

The same rational logarithm certificates used in pass2 apply. Thus D_m>0
for every t>0 and m<=M. Finally use the exact parent identity

    H_(a,b)(v)=v^(a+1)/(a+b)! integral_0^infinity
                         t^(a+b)exp(-vt)D_b(t)dt.            (PH16)

An explicit positive lower bound is obtained by retaining t>=1/10 and
inserting (15/16)196^b exp(-226t), as in pass2 equation (25).

V_(3*10^12) is the published Platt--Trudgian theorem. The full verification
was NOT rerun. The dependency on the proposed pass2 analytic proof is
retained; this corollary is not an independent reproof of that packet.
No 10^22-element computation or unbounded-b conclusion is asserted.

## 5. Time itself can grow: the constant-two logarithmic-logarithmic region

**Theorem ASTRA-PH-03.** For m>=1, t>0 and m>=40t,

    D_m(t) > I_(m,t)/(4pi)
       [log sqrt(m/t)-7-130(t+1)^2 exp(t/2)].                 (PH17)

In particular, whenever the bracket is nonnegative, D_m is strictly positive.
This theorem is independent of every finite zero verification and of the
pass2 small-time proof.

Proof. Set y=1/2+1/(t+1). Since d+y^2<=5/2, m>=40t ensures the second
bound in (PH6). Also

    2ty^2=t/2+2-2/(t+1)^2<t/2+2,
    exp(2)<8,   A(y)<2(t+1)^2.

Thus the prime term divided by I is <128(t+1)^2 exp(t/2). Combine with
(PH11); 13/2<7 and t/2+128(t+1)^2<130(t+1)^2 prove (PH17).

**Corollary.** For each epsilon in (0,2), there is M_epsilon such that

    m>=M_epsilon, 0<t<=(2-epsilon)log log m  =>  D_m(t)>0.   (PH18)

This is a simultaneous growing-(m,t) theorem, not just fixed-t positivity.
Let T=(2-epsilon)log log m. Then m>=40T eventually, and
log sqrt(m/T)~(1/2)log m, whereas

    (T+1)^2 exp(T/2)=O_epsilon((log log m)^2(log m)^(1-epsilon/2))
                    =o(log m).

The bracket is therefore positive at t=T. It is decreasing in t, so all
smaller positive t are covered. Equivalently, for each fixed T>0 all
sufficiently high orders are positive simultaneously on (0,T].
A completely explicit, deliberately huge choice is any integer

    m > max(40T, T exp(2[7+130(T+1)^2 exp(T/2)])).

The coefficient 2 describes this proved region. It is NOT claimed to be a
sharp mathematical boundary, and does not rule out improvements using signs.

## 6. Exact Hermite prime kernel and a fixed-time asymptotic

Put J(t,ell)=sqrt(pi/t)exp(-t/4-ell^2/(4t)). Fourier differentiation gives

    Fhat_(m,t)(ell)=(-partial_t)^m J(t,ell)
      =J(t,ell) sum_(j=0)^m binom(m,j)4^(-(m-j))
                (-1)^j(4t)^(-j) H_(2j)(ell/(2sqrt(t))).       (PH19)

H_k is the physicists' Hermite polynomial. Formula (PH19) retains the
entire signed polynomial before evaluating the prime sum. For example,
Fhat_1/J=1/4+1/(2t)-ell^2/(4t^2), which has both signs.

**Theorem ASTRA-PH-04 (fixed-t source asymptotic).** For every FIXED t>0,
as m tends to infinity and r=sqrt(m/t),

    D_m(t)/I_(m,t) = (1/(4pi)) [log(r/(2pi))-2 C_t(r)+o_t(1)],
    C_t(r)=sum_(n>=2) Lambda(n)/sqrt(n)
                exp(-(log n)^2/(8t)) cos(r log n).           (PH20)

The series for C_t is absolutely convergent for each fixed t. There is no
claim of an o(1) error uniform for unbounded t.

Proof details. The two real peaks of F are at +/-sqrt(m/t-d). Translating
by +/-r instead changes the peak locations by o(1). For fixed s,t, expansion
of the exact logarithm gives

    F_(m,t)(r+s)/[(m/t)^m exp(-m)] -> exp(-2ts^2).

The same statement holds at -r. These local limits are dominated in the
integrals by Gaussian envelopes: apply (log[x^(2m)e^(-tx^2)])''<=-2t to
sqrt(x^2+d), split |x|>=r/2 from its complement, and bound the latter by
O(r exp(-m/16)) times the maximum. Hence convergence holds in L1 after
splitting into the two peaks, and

    I_(m,t) ~ sqrt(2pi/t)(m/t)^m exp(-m),
    Fhat_(m,t)(ell)/I_(m,t)
       -exp(-ell^2/(8t))cos(r ell) ->0                       (fixed ell).

For fixed y>1/2, (PH6)--(PH7) dominate these normalized transforms by
4exp(2ty^2)exp(-y ell) for all sufficiently large m. This is summable
against Lambda(n)/sqrt(n) at ell=log n. The proposed Gaussian approximation
is separately summable there; dominated convergence proves the full prime
sum convergence, not just termwise convergence at finitely many primes.

Finally Omega(x)=log(|x|/(2pi))+O(1/|x|) at infinity. The same two-peak
Gaussian domination, splitting off |x|<r/2, proves
integral F Omega/I=log(r/(2pi))+o_t(1). Insert these limits in (PH1).
The small-x logarithm is integrable and the real Omega is bounded there.
This proves (PH20) without RH or a zero-spacing hypothesis.

## 7. The full attempted closure and its remaining signed estimate

For all m>=1,t>0 define, from the literal prime and gamma sources,

    P_(m,t)=2/I_(m,t) sum_(n>=2) Lambda(n)/sqrt(n) Fhat_(m,t)(log n),
    G_(m,t)=1/I_(m,t) integral_R F_(m,t)(x) Omega(x) dx.

**ASTRA-PH-05 (exact endpoint, not a proved source inequality).**

    [P_(m,t)<=G_(m,t) for EVERY m>=1,t>0] <=> RH.             (PH21)

Forward: (PH1), the already established S>0 and the all-order inequalities
make S completely monotone on (0,infinity). The parent's Bernstein/Stieltjes
argument then gives RH. Reverse: under RH every term A^m exp(-At) is positive.
This uses the exact parent RH criterion; it does not assume the desired
inequality in any proof above.

The attempt was to prove (PH21) with the uniform contour bound. It succeeds
in (PH12) and (PH17), giving (PH13)--(PH18), but fails to control arbitrary
intermediate times and orders. Its prime-side majorant grows like
(t+1)^2 exp(t/2), whereas the archimedean reserve grows like log sqrt(m/t).
That comparison is not favorable throughout the remaining region.

In particular, a possible failure must have m>10^22 and t>1/10, must avoid
the positive bracket in (PH17), and must occur before the late-time threshold
T_m(3*10^12). An infinite intermediate region remains. For any epsilon>0,
(PH18) also forces t>(2-epsilon)log log m at any sufficiently large failing
order. This is NOT a reduction to finite computation.

Replacing Fhat by |Fhat| loses the arithmetic oscillation displayed by (PH19)
and (PH20). Using (PH20) at t growing with m without a uniform error theorem
would be another gap. Neither move is made here. The two publications in
this session do not establish the unrestricted mixed inequality or RH.
