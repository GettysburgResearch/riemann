# A faithful cofinal cutoff, and the sharp universal tail exponent

Status: PROPOSED COMPLETE COMPONENT PROOFS; independent review required.
Scope: every coefficient sequence |b(k)|<=1, including the literal 67-free
Mobius source. No RH, zero table, prime number theorem, or numerical saddle
assumption. No new Mobius cancellation estimate or external priority claimed.
Local labels CT1--CT4 apply only to this packet.

## 1. The actual missing approximation theorem

Write

    a_n(b)=sum_(k>=1) b(k) k^(-3/2) L_n(2log k),
    a_n(b;X)=sum_(1<=k<=X) b(k) k^(-3/2) L_n(2log k).

L_n is ordinary Laguerre, with L_0=1. Every individual series converges
absolutely. The preceding raw-cutoff counterexample showed that log X_N=o(N)
can suppress the entire exponential signal. Fixed-degree convergence therefore
cannot justify the joint limit. The theorem below supplies a JOINT bound.

## 2. CT1: an explicit universal bound

For any integer X>=1, n>=0 and 0<r<1/3 set

    alpha(r)=(1-3r)/(2(1+r)).

Then

    |a_n(b)-a_n(b;X)|
      <= U_n(X):=sum_(k>X) k^(-3/2)|L_n(2log k)|
      <= r^(-n) X^(-alpha(r))/[(1-r)alpha(r)].             (CT1)

Proof. The classical generating identity is

    sum_n L_n(x) z^n=(1-z)^(-1)exp(-xz/(1-z)).

For real x>=0 and |z|=r, elementary algebra gives
Re(-z/(1-z))<=r/(1+r). Cauchy's coefficient inequality thus gives

    |L_n(x)| <= r^(-n)/(1-r) exp(xr/(1+r)).

Sum k^(-1-alpha(r)) over the tail. Since X is an integer and this power is
decreasing, its sum over k>X is at most its integral from X to infinity.
This proves CT1, including n=0. All signs and the term k=1 are retained in
the definitions; only the omitted tail is bounded absolutely.

For every N>=1 choose the explicit integer cutoff

    X_N=2^(11N),        r=1/16.

Then simultaneously for EVERY 0<=n<=N,

    |a_n(b)-a_n(b;X_N)| <= (544/195) 2^(-7N/34).           (CT2)

Here alpha=13/34 and 16^N X_N^(-13/34)=2^(-7N/34).
In particular the entire prefix vector has Euclidean error at most

    tau_N=(544/195)sqrt(N+1)2^(-7N/34) ->0.

The cutoff is large. This theorem is an error certificate, not a suggestion
to enumerate 2^(11N) integers. SOURCE_COMPILER.md gives a different, short
source evaluation that RETAINS an analytic tail rather than dropping it.

## 3. CT2: the cofinal energy test can no longer falsely pass by truncation

Let b(k)=mu(k)1_(67 does not divide k),
E_N=sum_(n=0)^N |a_n|^2 and E_N^cut=sum_(n=0)^N |a_n(X_N)|^2. Minkowski gives

    |sqrt(E_N)-sqrt(E_N^cut)|<=tau_N.                      (CT3)

Consequently both energies have the same exponential root limsup. In
particular

    RH <=> for every eps>0 there is C_eps with
             E_N^cut<=C_eps exp(eps N), every N>=1.        (CT4)

For the RH connection, the coefficient germ is

    A(z)=1/[(1-z)zeta(w(z))(1-67^(-w(z)))],
    w(z)=1/2+(1+z)/(1-z).

The generating identity starts on an absolute-convergence disk. The map w
sends the unit disk onto Re s>1/2. Any zeta zero there gives a nonremovable
interior pole; RH makes the germ holomorphic on the disk. Cauchy's radius
formula proves RH iff E_N has all-epsilon subexponential growth. This is
the PREDECESSOR endpoint, not an additional analytic claim in this pass.
Since a_0>0 and a_0(X_N)->a_0, both root limsups are at least one; CT3 then
preserves them even in the bounded-energy case.

CT4 has NOT been proved unconditionally. Its importance is that it is a
faithful finite-arithmetic version: unlike a subexponential size cutoff,
it cannot lose an exponential signal in an uncontrolled omitted tail.
The same implication holds for any rational coefficient enclosures with
uniform error <=2^(-N) through degree N, independently of how they were
computed. It does not follow that these enclosures obey CT4.

## 4. CT3: the optimal exponential tail cost

For C>0 define U_n(ceil(exp(Cn))) as above. Put

    rho(C)=C-1-sqrt(C(C-2))
          =1/[C-1+sqrt(C(C-2))],              C>2,
    Phi(C)=log3,                             0<C<=8/3,
    Phi(C)=-log rho(C)-C alpha(rho(C)),       C>8/3.

Then the exact exponential-rate theorem is

    lim_(n->infty) (1/n)log U_n(ceil(exp(Cn)))=Phi(C).      (CT5)

The same rate holds if the summand is multiplied by mu(k)^2 1_(67 does not
divide k). In the range C>8/3, L_n has constant sign throughout the tail;
therefore the SAME statement there holds for the modulus of the SIGNED tail
of the one fixed positive squarefree source b(k)=mu(k)^2 1_(67 does not divide k).
This source is not Mobius and is not a counterexample to RH.

### Upper bound and optimization

Apply CT1 and let n tend to infinity. Optimize

    -log r-C alpha(r),           0<r<1/3.

The derivative vanishes precisely at C=(1+r)^2/(2r). For C>8/3 the minimizer
is rho(C); for C<=8/3 the infimum is the boundary value log3. Integer rounding
of exp(Cn) does not affect the rate.

### Self-contained outer saddle estimate

For t in a compact subset of (2,infinity), put r=rho(t) in (0,1). On the
Cauchy circle z=-r exp(i theta),

    (-1)^n L_n(2tn)
      =r^(-n)/(2pi) int_(-pi)^pi
       exp(n[2tr exp(i theta)/(1+r exp(i theta))-i theta])
          /(1+r exp(i theta)) dtheta.

The real part of the exponent has its unique maximum at theta=0. Its first
derivative is zero there because 2tr/(1+r)^2=1, and the second derivative is
-(1-r)/(1+r)<0. The denominator is bounded away from zero. Split at a small
fixed |theta|: the outer portion has a uniform strictly negative exponent
gap, while theta=v/sqrt(n) in the inner portion converges to a Gaussian,
dominated by exp(-c v^2). Taylor's theorem on the compact t-range makes all
these statements uniform. It follows that

    (-1)^n L_n(2tn)
      = exp(n[-log r+2tr/(1+r)])
        /sqrt(2pi n(1-r^2)) * (1+o(1)).                   (CT6)

This is the ordinary nondegenerate outer Laguerre saddle, rederived here to
make the rate proof auditable. It is not an external novelty claim and is
not used at the turning point t=2.

### Lower bound from one actual integer interval

Fix t>max(C,2). Use only k in [exp(tn),exp(tn+1)]. For every such k,
log(k)/n=t+O(1/n); CT6 is uniform there. The interval contains exp(tn+O(1))
integers. Its contribution has exponential rate

    -t/2-log rho(t)+2t rho(t)/(1+rho(t)).

For C>8/3 let t decrease to C. For C<=8/3 use t=8/3 if permitted, or let t
decrease to 8/3 from above. The resulting lower bounds equal the upper
bounds. This proves CT5 without an interchange at the oscillatory turning
point or a claimed full asymptotic constant for U_n.

For the squarefree restriction, elementary inclusion-exclusion gives

    sum_(k<=x) mu(k)^2 1_(67 does not divide k)
      =delta_67 x+O(sqrt x),
    delta_67=1/[zeta(2)(1+1/67)]>0.

Indeed expand mu(k)^2=sum_(d^2|k)mu(d), retain 67-free d and k/d^2, and
estimate the floor errors and the convergent d^(-2) tail. A bound 5sqrt x
suffices for x>=1. The same interval therefore contains
(delta_67(e-1)+o(1))exp(tn) admissible integers, proving its lower bound.

Finally the n-by-n Laguerre Jacobi matrix has diagonal 2j+1 (0<=j<n) and
off-diagonal j+1. Its characteristic polynomial is (-1)^n n! L_n, by the
three-term recurrence. Its Gershgorin right endpoints are strictly below 4n,
so L_n(x) has sign (-1)^n for x>=4n. For C>8/3, all tail arguments exceed
4n. There is no cancellation in the positive squarefree tail, proving the
last assertion of CT5.

## 5. CT4: a sharp universal threshold, not a new RH exponent

There is a unique C_*>8/3 with Phi(C_*)=0. Numerically,

    C_*=7.1779883631304... .

An exact definition is C_*=(1+r_*)^2/(2r_*), where r_* in (0,1/3) solves

    -log r_* -1/(4r_*)+1/2+3r_*/4=0.

The left side has derivative (1-r)(1-3r)/(4r^2)>0; it tends to -infinity at
zero and equals log3 at 1/3. The checker encloses r_* between the rationals
0.08146966677 and 0.08146966679 using outward rational logarithms. The decimal
for C_* is descriptive; the defining equation and rational enclosure are
the certificate.

For C>=C_* the omitted tail at X_N=ceil(exp(CN)) is uniformly subexponential
through degree N; for C>C_* it decays exponentially. If C<C_* the worst-case
tail has positive exponential rate. Near the threshold this already occurs
for the SAME fixed positive squarefree source, not a degree-dependent choice
of signs. Thus C_* is the sharp threshold for this UNIVERSAL ABSOLUTE tail
problem. It is NOT asserted to be the minimum cutoff for actual Mobius, nor
the optimum cutoff for every possible finite-energy RH criterion.

The attempted last step is still a sign problem: CT1 controls the omitted
tail but does not bound the assembled finite Mobius energy in CT4. A generic
absolute estimate of that finite sum has exponential cost. The companion
source compiler avoids false arithmetic convergence; it does not turn a
coefficient evaluation into the missing all-degree signed estimate.
