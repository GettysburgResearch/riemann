# Joint heat asymptotics, exact continuum subtraction, and fixed-ray detection

Status: PROPOSED COMPLETE PROOFS of the statements below; independent review
required. The unrestricted signed arithmetic bound and RH remain UNPROVED.
Source: PR #790 at 337c222a54a232b89b9f47827b2caeb754145efc.
Scope: actual Riemann xi, with all zero multiplicities retained. No external
novelty claim. Local statement names ASTRA-JR-01 through ASTRA-JR-05.

This continuation does not raise a finite verification height or infer a
sign from an asymptotic outside its uniform range. It closes the fixed-time
uniformity limitation of PH20 in a specified joint regime, removes the
continuous prime main term exactly, and isolates a different, fixed-center
ray on which every hypothetical nonreal zero is detectable.

## 1. Normalization and imported interfaces

Let A=rho(1-rho) for every nontrivial zero rho with Im rho>0, counted with
multiplicity. Functional-equation reflection closes this multiset under
conjugation. Put

    S(t)=sum_A exp(-At),             D_m(t)=sum_A A^m exp(-At),
    F(x)=(x^2+1/4)^m exp(-t(x^2+1/4)),
    I=I_(m,t)=integral_R F(x) dx,
    Fhat(ell)=integral_R F(x)exp(-i ell x) dx,
    Omega(x)=Re digamma(1/4+ix/2)-log pi,
    r=sqrt(m/t).

All heat sums converge absolutely and locally normally for t>0. We use the
classical critical strip, the functional equation and N(T)=O(T log(T+2));
no finite zero verification or simplicity hypothesis is needed below.
The parent PH1 is the unconditional Guinand--Weil identity, for m>=1,

    4pi D_m(t)=integral F Omega -2 sum_(n>=2) Lambda(n)/sqrt(n) Fhat(log n). (1)

It follows directly from Proposition 5 of Chirre--Goncalves (2022), with
Fourier variable ell=2pi y. F(i/2)=0 removes the endpoint contribution.
We also re-use the elementary contour inequality PH6--PH7 at y=1:

    |Fhat(ell)|/I <=4 exp(2t-ell), ell>=0, m>=20t.             (2)

Its proof is finite Gamma-ratio algebra and a horizontal contour shift;
it does not import the RH-conditional main theorems of that article.

## 2. A square-root Gamma density bound, with a proof

For integer k>=1, let V have density

    p_k(v)=2 v^(2k) exp(-v^2)/Gamma(k+1/2), v>0.

For Z=V-sqrt(k), compare its density with

    g(z)=sqrt(2/pi)exp(-2z^2), z in R.

We claim the L1 distance is at most 2/sqrt(k). This is L1, not the
half-sized total variation convention.

Here is an elementary Gaussian Stein argument. For measurable |h|<=1,
solve phi'-4z phi=h-E_g h by

    phi(z)=g(z)^(-1) integral_(-infinity)^z (h(s)-E_g h)g(s) ds.

Since the numerator is also the negative complementary integral,

    |phi(z)|<=2 min(G(z),1-G(z))/g(z)<=sqrt(pi/2)<2.

The last bound follows for z>=0 by writing the Gaussian tail ratio as
integral_0^infinity exp(-4zs-2s^2)ds, and by reflection for z<0.
The shifted p_k density vanishes at its finite left endpoint. Integration
by parts therefore bounds the expectation difference by

    2 E |(log p_k)'(V)+4(V-sqrt(k))|.

The score defect is exactly 2(V-sqrt(k))^2/V. Gamma recurrence gives

    E V = k E(1/V),
    E[2(V-sqrt(k))^2/V]=4(E V-sqrt(k))<=1/sqrt(k),

where E V<=sqrt(E V^2)=sqrt(k+1/2) was used. Taking the supremum over h
proves the L1 bound. There is no distributional tail or normal approximation
hypothesis in this argument. The normal translation bound

    ||g(. -a)-g(. -b)||_1 <=2|a-b|                            (3)

follows by integrating |g'|, whose integral is 2sqrt(2/pi)<2.

## 3. Uniform Fourier approximation at every real frequency

Set delta=t/4 and

    R_(m,l)=product_(j=0)^(l-1) (m-j)/(m-j-1/2),
    W_m(delta)=sum_(l=0)^m R_(m,l)delta^l/l!,
    w_l=R_(m,l)delta^l/[l! W_m(delta)].

The distribution with density F/I, under the scaling v=sqrt(t)x, is a
mixture of the symmetrizations of p_(m-l), with probabilities w_l. This is
an exact binomial/Gamma integral identity. The k=0 density is included.
Crucially, R_(m,l+1)<=2R_(m,l), so W_m'<=2W_m and

    E_w l <=2delta,            Pr(l>m/2)<=4delta/m.            (4)

For l<=m/2 and m>=2, Section 2 and (3) bound the symmetrized density error
against normals centered at +/-sqrt(m) by

    2sqrt(2)/sqrt(m)+2l/sqrt(m).

The remaining components have L1 error at most 2. Averaging, using (4),
gives an error at most

    (2sqrt(2)+4delta)/sqrt(m)+8delta/m
      <=4(1+t)/sqrt(m).

The m=1 case follows from the trivial L1 bound 2. Fourier transformation
is contractive from L1 to bounded functions. We have proved:

**ASTRA-JR-01.** For EVERY integer m>=1, t>0 and real ell,

    |Fhat(ell)/I -exp(-ell^2/(8t))cos(r ell)|
       <= min(2,4(1+t)/sqrt(m)).                              (5)

In particular this is uniform in ell, not a fixed-frequency expansion.
A weighted prime sum still needs a separate infinite-tail argument, which
is supplied next; multiplying a uniform error by an infinite prime mass
would be invalid.

## 4. Full prime-sum transfer in a joint regime

Define the absolutely convergent series

    C_t(r)=sum_(n>=2) Lambda(n)/sqrt(n)
                      exp(-(log n)^2/(8t))cos(r log n).

For m>=4, m>=20t, set L=(log m)/2+2t. We have L>=log 2. Below exp(L),
Lambda(n)<=log n and sum_(n<=X)n^(-1/2)<=2sqrt(X) give, using (5),

    error_low <=8L(1+t)m^(-1/2)exp(L/2).

Above exp(L), both Fourier terms are bounded exponentially: (2) handles
the exact kernel and completing the square gives

    exp(-ell^2/(8t))<=exp(2t-ell).

For N=floor(exp L)>=2, integral comparison gives

    sum_(n>N) log(n)n^(-3/2)
       <=(2log N+4)/sqrt(N)<=6(L+2)exp(-L/2).

Thus error_high<=30(L+2)exp(2t-L/2). Substitution of L proves

    |sum Lambda(n)/sqrt(n) Fhat(log n)/I-C_t(r)|
       <=40(L+2)(1+t)exp(t)m^(-1/4).                         (6)

This controls the COMPLETE prime sum, without using the prime number
theorem, a zero-free strip, or an unproved cancellation estimate.

## 5. Uniform archimedean comparison

For completeness we pay the gamma-factor error as well. Write G=integral
F Omega/I. We prove, for m>=2,t>0,

    |G-log(r/(2pi))| <= E_G(m,t),
    E_G=10sqrt(t/m)+[1+t(20+2log(m+2)+|log t|)]/m.            (7)

Euler--Maclaurin for digamma in Re z>0 gives

    |digamma(z)-log z|<=1/(2|z|)+(1/2)int_0^infinity |z+s|^(-2)ds.

Consequently, for x!=0,

    |Omega(x)-log(|x|/(2pi))|<=3/|x|+1/(8x^2).               (8)

For a component with k=m-l>=m/2>=1, Gamma recurrence and Jensen give

    E |x|^(-1)<=2sqrt(t/k),  E |x|^(-2)<=2t/k.

Its (8) expectation is at most 9sqrt(t/m)+t/(2m).
For every k>=0 a cruder integrable bound is

    E_k |Omega(x)-log(|x|/(2pi))|
       <=17+log(m+2)+|log t|, k<=m.                          (9)

Here |Omega(x)|<=8+log(1+|x|). Also, for V=sqrt(t)|x|,
E log_+ V <=(1/2)log(k+3/2) and E(-log V)_+<=2. The latter follows from
Gamma(k+1/2) stochastic domination of Gamma(1/2), obtainable by adding k
independent exponential variables; direct integration at k=0 bounds it
by 2/sqrt(pi)<2. Jensen bounds E log(1+|x|) by
1+(1/2)log(1+(k+1/2)/t). These bounds imply (9) in both t<=1 and t>=1.
Multiplying (9) by the tail probability in (4), at most t/m, pays the
otherwise problematic k=0 component.

The exact logarithmic moment is

    E log|x|=(1/2)sum_l w_l digamma(m-l+1/2)-(1/2)log t.

For l<=m/2, the digamma decrement is at most 2l/m. For every l it is at
most 3+log m, by the harmonic sum of reciprocals j+1/2. Hence its average
is at most 4delta(4+log m)/m. The real digamma remainder also gives
|digamma(m+1/2)-log m|<=2/m. Thus

    |E log|x|-log r|<=1/m+t(4+log m)/(2m).

Combining these estimates proves (7) with the displayed conservative constants.

**ASTRA-JR-02 (joint prime asymptotic).** For m>=max(4,20t),

    4pi D_m(t)/I = log(r/(2pi))-2 C_t(r)+E_(m,t),
    |E_(m,t)|<=80(L+2)(1+t)exp(t)m^(-1/4)+E_G(m,t).          (10)

For every fixed epsilon in (0,1/4), E_(m,t)=o(1) UNIFORMLY throughout

    0<t<=(1/4-epsilon)log m, m->infinity.                    (11)

The first error is O_epsilon((log m)^2 m^(-epsilon)); the other terms
also tend uniformly to zero, including t|log t|/m near t=0.
This closes the fixed-t limitation of the parent PH20 in this specified
joint range. It does NOT assert positivity throughout (11): the SIGNED
C_t(r) remains present and can be much larger than its fixed-t bound.

## 6. Exact removal of the continuous prime main term

Define the right-continuous Chebyshev function

    Psi(x)=sum_(n<=x) Lambda(n),  E(x)=Psi(x)-x+1, x>=1,
    f(x)=x^(-1/2) Fhat(log x),
    J_(m,t)=int_1^infinity E(x) f'(x) dx.

E(1)=0. Gaussian-polynomial decay in log x and Psi(x)<=x log(x+1)
justify all integrations and endpoints. Stieltjes integration by parts gives

    sum Lambda(n)/sqrt(n) Fhat(log n)
       =int_1^infinity f(x)dx - J_(m,t).                     (12)

The large continuous term cancels exactly, rather than being estimated.
Fourier inversion at i/2 gives

    int_0^infinity [exp(ell/2)+exp(-ell/2)]Fhat(ell)dell
       =2pi F(i/2)=0, m>=1.

On the other hand, Fubini and the elementary cosine Laplace transform give

    int_0^infinity exp(-ell/2)Fhat(ell)dell
       =(1/2)int_R F(x)/(x^2+1/4) dx = I_(m-1,t)/2.

Therefore the EXACT identity is

    int_1^infinity f(x)dx=-I_(m-1,t)/2,
    sum Lambda(n)/sqrt(n) Fhat(log n)=-I_(m-1,t)/2-J_(m,t).   (13)

**ASTRA-JR-03.** Substitution in (1) gives

    4pi D_m(t)=int_R F Omega + I_(m-1,t)+2J_(m,t), m>=1.     (14)

The +1 in E and the plus sign on J in (14) are essential. This statement
is an exact identity, not positivity of E or of J. It provides an actual
mean-subtracted arithmetic target instead of the unsigned prime envelope.
It needs no asymptotic PNT error estimate.

## 7. A ray that detects every hypothetical nonreal zero

The following result explains why success in (11), even with a signed
estimate there, would not finish the global problem.

Fix u>0 and define

    z_u(A)=(e A/u)exp(-A/u),
    B_m(u)=(e/u)^m D_m(m/u)=sum_A z_u(A)^m,
    R(u)=max_A |z_u(A)|.                                    (15)

Since Re A>=gamma^2 and |A|<=gamma^2+1, the transformed atoms tend to zero
and sum_A |z_u(A)|<infinity, locally uniformly in u. Thus the maximum is
attained and positive. Normal convergence gives the meromorphic identity

    sum_(m>=1) B_m(u)w^(m-1)=sum_A z_u(A)/(1-w z_u(A)).        (16)

Coincident transformed atoms ADD their positive integer multiplicities.
Every pole has residue minus that multiplicity, so none cancels. Cauchy's
radius formula gives

    limsup_(m->infinity) |B_m(u)|^(1/m)=R(u).                 (17)

No statement of a full limit is made: finite phase cancellation can occur.

We next control the NEGATIVE part, not just the absolute value. Suppose
R(u)>1 and no dominant transformed atom is positive real. Let the distinct
dominant atoms be R lambda_j, |lambda_j|=1, with multiplicities d_j>0. Put

    P=sum_j d_j, V=sum_j d_j^2, T_m=sum_j d_j lambda_j^m.

Conjugation makes T_m real. Since no lambda_j=1, elementary finite geometric
sums show Cesaro mean T_m->0 and Cesaro mean T_m^2->V. Also |T_m|<=P.
It follows that the lower Cesaro mean of (T_m)_- is at least V/(2P), and

    lower density {m:T_m<=-V/(4P)} >= V/(4P^2).               (18)

Indeed T_m^2<=P|T_m| and (T_m)_-<=V/(4P)+P 1_(T_m<=-V/(4P)).
All nondominant atoms contribute O(q^m), q<R, since the atoms accumulate
only at zero and are absolutely summable. Hence on a set of integers with
the positive lower density in (18), for all sufficiently large such m,

    B_m(u)<=-V R(u)^m/(8P).                                 (19)

In particular limsup (B_m(u)_-)^(1/m)=R(u)>1. No independence of zero
ordinates or of phases has been assumed.

**ASTRA-JR-04 (rational-ray detection).** If RH is false, there is a FIXED
positive rational u for which (19) holds. Conversely RH makes B_m(u)>0
for every u>0 and m>=1.

Proof. Take a nonreal A=x+iy. At u=x,

    |z_x(A)|=|A|/x>1.                                       (20)

By continuity this holds with a fixed strict margin on a small compact
interval of u's. Only finitely many atoms can have modulus greater than
one anywhere on that interval, by the uniform tail bound. For a nonreal
atom, positivity on the real axis requires

    arg A - Im A/u =2pi k, k an integer.

Each of the finitely many relevant atoms has only finitely many such u
in the interval. A REAL positive A has z_u(A)<=1 for every u, by
log(A/u)+1-A/u<=0. Exclude the finite exceptional set and choose a rational
u in the remaining open interval. Then R(u)>1 and no positive real atom
is dominant. Equation (19) applies. Under RH all A are positive real,
so every term in (15) is positive. This proves the theorem.

The finite-exception argument matters: deleting an arbitrary countable set
would NOT justify choosing a rational outside it.

A quantitative formulation is also exact. If b_- means max(0,-b), then

    max(1, sup_(u positive rational) limsup_m B_m(u)_-^(1/m))
       =sup_A |A|/Re A.                                    (21)

The upper bound follows by maximizing |z_u(A)| in u: its maximum is |A|/Re A
at u=Re A. For the reverse inequality use (20), continuity, and the same
finite-exception argument. The case where the right side is one is RH
and both sides equal one. Equation (21) is NOT a numerical estimate for
actual zeros; it is a conditional quantitative identification of the defect.

For one atom, let q=|y|/x<=1/10 and u=x+|y|/2. Elementary inequalities give

    log|z_u(A)|>=q^2/3,
    q^2/3<=|arg z_u(A)|<=q^2/2.                             (22)

For example use log(1+q^2)>=q^2-q^4/2,
-log(1+s)+s/(1+s)>=-s^2/2, and q-q^3/3<=arctan q<=q.
The lower phase inequality follows from 1/(2+q)-q/3>=1/3.
This identifies an atom-level amplification scale proportional to q^(-2).
It is NOT an effective first-negative-order bound for the complete zero sum;
other dominant atoms and their multiplicities must still be included.

## 8. ASTRA-JR-05: the revised conditional endpoint and attempted closure

By ASTRA-JR-04, each of the following would suffice to prove RH:

(a) For every positive rational u, D_m(m/u)>=0 for all sufficiently large m.
(b) For every positive rational u and epsilon>0, there is C_(u,epsilon) with

    B_m(u)>=-C_(u,epsilon)exp(epsilon m), for all m>=1.        (23)

RH implies both. Thus (23) is an exact, weaker-looking but still
RH-equivalent, ONE-SIDED exponential bound. Equations (14)--(15) give its
literal prime-discrepancy form without inserting zeros into the source:

    B_m(u)=(e/u)^m/(4pi)
      [int F_(m,m/u)Omega+I_(m-1,m/u)+2J_(m,m/u)].            (24)

The attempt was to prove (23) by first subtracting the complete continuous
prime main term in (13), then using the Gaussian approximation to estimate
the residual. The subtraction is exact. The next step does NOT close:

- (10) is controlled for t<=c log m, whereas each ray t=m/u eventually
  leaves that regime. Its peak r=sqrt(u) stays FIXED, and its real width is
  of order sqrt(u/m). The large-height saddle estimates are not estimates
  for this increasing-resolution regime.
- The real Fourier error (5) becomes vacuous at t=m/u: its displayed bound
  grows like sqrt(m)/u. This is an explicit uniformity failure, not hidden
  in an o(1).
- E(x)=Psi(x)-x+1 has no proved sign that orients its signed derivative
  integral J. Replacing J by an absolute bound reintroduces exponential
  loss. Neither E=o(x) nor positive S licenses (23).

No source-side proof of (23) is supplied. The new results do not establish
RH or all mixed inequalities. They replace a potentially misleading
'keep enlarging the early-time region' plan by an exact rational-ray target
and provide a uniform prime approximation for the separate high-center
regime. These are reviewable tools and limitations, not a completed proof.
