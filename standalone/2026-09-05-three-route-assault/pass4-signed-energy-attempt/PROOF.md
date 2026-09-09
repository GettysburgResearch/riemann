# A direct attack on the signed Laguerre energy

Status: PROPOSED COMPLETE COMPONENT PROOFS; independent review required.
RH completion: NOT OBTAINED. No all-radius signed-energy bound is proved.
Base: PR #793, bfb66e07f7e38306dbcb916911332a591efce917.
Cross-source: PR #790, bce97be9727dea9968db7517738edc966d2cc86b,
heat-hankel-pass5/PROOF.md, Sections 1--4.
Scope: literal 67-free Mobius source; infinite sums, all degrees, and fixed
real damping 0<r<1. Bounded code controls do not prove the analytic theorems.
No external novelty or priority claim is made.

## 1. Fixed source and the precise unfinished task

Write q=67, mu_q(k)=mu(k)1_(q does not divide k), and

    D(s)=1/[zeta(s)(1-q^(-s))],
    a_n=sum_(k>=1) mu_q(k) k^(-3/2) L_n(2log k),
    E(r)=sum_(n>=0) |a_n|^2 r^n in [0,infinity].

L_n is the ordinary Laguerre polynomial. Each a_n is an absolutely
convergent arithmetic sum. Initially near z=0, its generating germ is

    A(z)=sum a_n z^n=D(w(z))/(1-z),
    w(z)=1/2+(1+z)/(1-z).

This is the predecessor's normalization, with no coefficient or endpoint
changed. The Laguerre generating identity and termwise integration prove
it first in an absolute-convergence neighborhood. Meromorphic uniqueness
then applies; no global convergence of the Taylor series is assumed.

The target E(r)<infinity for every r<1 is equivalent to RH: its finiteness
makes the germ A holomorphic on the disk, while any zeta zero with real
part greater than 1/2 creates a nonremovable interior pole. Conversely RH
makes A holomorphic on the disk, and every smaller closed disk has finite
Taylor square norm. This imports only the ordinary analytic continuation,
functional equation and zero-free half-plane Re s>1, not RH in the forward
argument. Repeated critical-line zeros are allowed.

The attempt below gives an exact safe-source expression for E, completes
its diagonal asymptotic, and proves one unconditional convergence region.
It does not bound E on every smaller disk.

## 2. The exact derivative-norm identity, including divergence

For 0<r<1 put

    q_r=sqrt(r),
    s_r=(3+r)/[2(1-r)] > 3/2,
    b_r=2sqrt(r)/(1-r),
    J(r)=sum_(j>=0) b_r^(2j) |D^(j)(s_r)/j!|^2.

Every derivative defining J is at an absolutely convergent real source
point. The following identity holds in the extended nonnegative reals:

    (1-r) E(r) = J(r).                                  (1)

### Proof, with the holomorphic-domain issue retained

Let phi(zeta)=(zeta-q_r)/(1-q_r*zeta), an automorphism of the unit disk.
Direct algebra gives

    w(q_r*zeta)=s_r+b_r*phi(zeta).

On the unit circle its angular Jacobian is

    d arg(phi(zeta))/d arg(zeta)=(1-r)/|1-q_r*zeta|^2.

For holomorphic functions in H2 of the disk, the weighted composition

    U(g)(zeta)=sqrt(1-r)/(1-q_r*zeta)*g(phi(zeta))

is unitary. The displayed Jacobian proves this first for functions
holomorphic on a neighborhood of the closed disk, and density of
polynomials plus the inverse disk automorphism proves it on H2.

If E(r)<infinity, sqrt(1-r) A(q_r*zeta) is in H2. Apply U inverse.
Meromorphic uniqueness identifies the result with D(s_r+b_r*zeta): the
mapped disk contains the original point s=3/2, and the two germs agree
there. Thus this meromorphic function has no pole in that disk, its Taylor
square norm is J(r), and unitarity gives (1).

If J(r)<infinity, start instead with the H2 germ at s_r and apply U.
The same uniqueness argument gives A(q_r*zeta), so E(r)<infinity and (1).
If neither norm is finite, both sides of (1) are infinity. This proves the
extended identity without identifying a meromorphic boundary integral
with a Taylor norm across a pole. QED.

Equivalently, E(r) is finite exactly when D has no pole in the CLOSED disk
|s-s_r|<=b_r. This disk is compactly contained in Re s>1/2. In the absence
of a pole on the closed disk, D is analytic on a larger neighborhood.
An interior pole prevents H2 continuation; a boundary pole of positive
integer order has a non-square-integrable boundary singularity. The
finite Euler factor has no poles there. All remaining poles are precisely
those caused by zeta zeros.

This is a Hardy disk-change identity specialized to the source, not a
new general theorem about composition operators.

### Exactly why known individual derivatives do not finish the proof

A Taylor expansion at a safe real point may have a finite radius. In the
synthetic model D_*(s)=1/(s-rho), rho=3/4, let c=3/2-rho=3/4 and d=1/2+rho=5/4.
Then a_n=(-d/c)^n/c, and

    E_*(r)=1/(c^2-r*d^2)             when r<9/25;
    E_*(r)=infinity                 when r>=9/25.

Likewise J_*(r) has the same finiteness threshold because

    (s_r-rho)^2-b_r^2=(c^2-r*d^2)/(1-r).

Above the threshold the meromorphic circle integral is nevertheless
finite, with value 1/| (s_r-rho)^2-b_r^2 |. It is not J_*(r). The model is
not zeta; it refutes the proposed analytic inference only.

## 3. A genuine unconditional radius from the source constant

Retain the invariant coordinates used by #790:

    X(u)=xi(1/2+sqrt(u+1/4)),
    H=X'(0)/X(0)=1+gamma_E/2-log(4pi)/2,
    A_rho=rho(1-rho)=x+iy,

where the list uses upper-half-plane zeta zeros with multiplicities.
The classical invariant genus-zero product gives

    H=sum_A Re(1/A),       x>0, y^2<=x.

All terms are positive, and a nonreal A comes with its conjugate. Thus for
any hypothetical off-line quartet, even without simplicity,

    H>=2*x/(x^2+y^2)>=2/(x+1).

The independent elementary rational certificate in verify.py proves
0<H<1/40 without any zero data. Consequently every nonreal A has x>79.

For rho=1/2+delta+i gamma with 0<delta<1/2,

    x=gamma^2+1/4-delta^2,
    z_rho=(rho-3/2)/(rho+1/2),
    1-|z_rho|^2=4delta/[x+3/4+2delta+2delta^2].

For fixed x>79 the fraction on the right increases on 0<=delta<=1/2:
its derivative has the sign of x+3/4-2delta^2. Therefore

    |z_rho|^2 > 1-2/(79+9/4)=317/325.

Line zeros have |z_rho|=1. The meromorphic germ A therefore has no pole
on the closed disk |z|<=sqrt(317/325). The disk is strictly inside |z|<1,
so compactness gives an analytic neighborhood and hence

    E(r)<infinity, J(r)<infinity,     0<r<=317/325.          (2)

The factor two uses an entire off-line conjugate invariant pair; dropping
it gives a weaker radius. This is a coarse bounded-region consequence of
classical xi theory and a safe source constant, NOT a new zero-free-height
record, new asymptotic zero-free region, or all-radius estimate.
The radius is fixed and less than one. Changing it to one is not licensed.

## 4. Complete diagonal asymptotic with the atom at k=1 retained

Define

    Delta_n=sum_(k>=1) mu_q(k)^2 k^(-3) L_n(2log k)^2,
    D_N=sum_(n=0)^N Delta_n,
    d_q=1/[zeta(2)(1+1/q)]=201/(34pi^2),
    C_q=1+d_q/2=1+201/(68pi^2).

We prove the all-degree-averaged asymptotic

    D_N ~ C_q (N+1),                                    (3)

and the explicit Abel estimate

    |(1-r)sum_(n>=0)Delta_n r^n-C_q|
          <=10sqrt(1-r),      1/4<=r<1.                  (4)

No sign cancellation, zero information or PNT is used. The predecessor's
upper bound D_N=O(N^(3/2)) is sharpened to an exact linear leading term.
The isolated 1 in C_q comes from k=1. Omitting it gives a wrong constant.
No error rate for D_N is inferred from (4) alone.

### 4.1 Elementary squarefree counting with explicit constants

Let B(x)=sum_(k<=x)mu(k)^2. Expanding mu(k)^2=sum_(d^2|k)mu(d) and
bounding the floor error and the d>sqrt(x) tail gives

    |B(x)-x/zeta(2)|<=3sqrt(x), x>=1.

Indeed, with D=floor(sqrt x), the two errors are at most D and x/D;
D<=sqrt x and D>=sqrt x/2.
The exact local-factor inverse gives

    B_q(x):=sum_(k<=x)mu_q(k)^2
          =sum_(j<=log_q x)(-1)^j B(x/q^j).

The infinite density series has sum d_q. The geometric errors and its
truncated density tail are bounded by

    3sqrt(x)/(1-q^(-1/2))+1/(1-q^(-1)) <5sqrt(x), q=67.

Put E_q(x)=B_q(x)-1-d_q(x-1). Then E_q(1)=0,

    E_q(x)=-d_q(x-1),   1<=x<2;
    |E_q(x)|<=6sqrt(x), x>=1.                            (5)

### 4.2 Positive Poisson kernel and exact continuous mass

Use the classical Hille--Hardy formula at Laguerre parameter zero
(DLMF 18.18.27):

 sum_(n>=0)r^n L_n(t)L_n(u)
  =(1-r)^(-1) exp[-r(t+u)/(1-r)]
                  I_0(2sqrt(rtu)/(1-r)).                 (6)

At t=u=2log x, let

    alpha=4r/(1-r), beta=4sqrt(r)/(1-r),
    g_r(x)=x^(-3-alpha) I_0(beta log x).

Tonelli on the positive diagonal gives

    (1-r)sum Delta_n r^n=sum_k mu_q(k)^2 g_r(k).           (7)

The elementary integral representation of I_0 yields

    integral_1^infinity g_r(x)dx
      =[(2+alpha)^2-beta^2]^(-1/2)=1/2.                  (8)

For example, substitute u=log x and integrate its cosine integral;
(2+alpha)>beta and the discriminant is exactly 4. No limit in the
Laguerre degree is used here.

Set c=3+alpha-beta=(3-sqrt r)/(1+sqrt r)>1. The same Bessel integral gives
I_0'(v)<=I_0(v), so g_r is decreasing. Also, for v>0,

    I_0(v)<=e^v min(1,v^(-1/2)).                          (9)

To prove the second bound, use cos theta<=1-2theta^2/pi^2 on [0,pi],
extend the Gaussian integral to infinity, and note sqrt(pi)/(2sqrt2)<1.
Thus g_r(x)<=x^(-c)/(sqrt(beta)*sqrt(log x)) for x>1.

### 4.3 The atom and density error

Partial integration using (5) gives exactly

    sum_k mu_q(k)^2 g_r(k)=1+d_q/2-integral_1^infinity E_q(x)g_r'(x)dx.

On [1,2] its absolute error is at most

    d_q integral_1^2 g_r(x)dx <=2sqrt(log 2)/sqrt(beta).

On [2,infinity), using monotonicity and (5), it is at most

  6[sqrt2 g_r(2)+(1/2)integral_2^infinity x^(-1/2)g_r(x)dx]
       <=6sqrt2/[sqrt(beta)*sqrt(log 2)].

Here g_r(2)<=1/[2sqrt(beta log 2)] and the remaining integral is at most
sqrt2/[sqrt(beta log 2)]. For r>=1/4, beta>=2/(1-r); also 1/2<log2<1.
The total is less than (14/sqrt2)sqrt(1-r)<10sqrt(1-r). This proves (4),
including convergence of the infinite sum in (7).

### 4.4 Positive Tauberian passage, with a proof

For x tending to infinity put the finite measures on [0,1]

    nu_x=(1/x)sum_(n>=0) Delta_n exp(-n/x) delta_(exp(-n/x)).

By (4), their kth moments tend to C_q/(k+1) for every k>=0. Thus they
converge weakly to C_q times Lebesgue measure: polynomial approximation
of continuous functions suffices, with total masses controlled by k=0.
The limiting measure has no atom at e^(-1), and y^(-1) is bounded on
[e^(-1),1]. It follows that

    (1/x)sum_(n<=x)Delta_n
       =integral_[exp(-1),1] y^(-1)dnu_x(y) -> C_q.

Taking integer x proves (3). This is the elementary index-one instance
of the positive Tauberian theorem, not an unproved Tauberian step.

## 5. Why the completed diagonal does not complete the signed estimate

Changing mu_q(k) to mu_q(k)^2 leaves Delta_n EXACTLY unchanged, for every
n. Its generating function is instead

    A_+(z)=zeta(w(z))/[(1-z)zeta(2w(z))(1+q^(-w(z)))].

In Re w>1/2, zeta(2w) and the finite Euler factor have no zeros. The pole
at w=1, z=-1/3, is noncancelling; it is the only pole in the disk. Therefore

    limsup |a_(+,n)|^(1/n)=3,
    limsup [sum_(n<=N)|a_(+,n)|^2]^(1/(2N))=3,

despite the IDENTICAL sharp linear diagonal asymptotic (3). This exact
control is inherited from pass3, now with the sharper diagonal theorem.
It is not actual reciprocal zeta and does not refute RH.

Likewise (1) is not a convergence theorem at every r. It expresses the
needed infinite norm through individually safe derivatives. A uniform
bound on their entire weighted square sum has not been obtained. The
pole countercontrol in Section 2 is the precise reason that replacing
this sum by a finite meromorphic circle integral would be circular.

## 6. Disposition of the completion attempt

The actual signed source is proved convergent in the fixed region (2).
The diagonal is completely evaluated at leading order by (3)--(4).
The all-radius norm identity (1) is exact, with infinity allowed.

The missing statement is still

    for EVERY 0<r<1, J(r)<infinity.

No bound covering the remaining radii up to one is proved. Routes 1 and 3
also still lack their all-order arithmetic positivity. The new cross-
branch capture theorem was read, but its small negative-trace bound does
not imply zero negative index. This packet does not rename any of these
missing sign/convergence estimates as a completed lemma.
