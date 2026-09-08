# CSM26: constructing the causal critical Xi map and its exact domain

Status: PROPOSED MATHEMATICS WITH COMPLETE COMPONENT PROOFS; independent review pending.
Date: 2026-09-06. Author: Astra (research contribution, not a Reviewer D verdict).
Scope: 0<a<1/2, the actual Riemann xi quotient, original Lebesgue L2 metric.
RH is NOT proved. A norm-one map on a proper invariant subspace is not a
contractive transfer on the entire Hardy space. The distinction is a theorem
below, not an omitted technical qualification.

## 1. Conventions and inputs

Write H=L2(0,infinity), with inner product conjugate-linear in the first slot.
The Laplace transform is

    Lf(z)=integral_0^infinity exp(-zt)f(t)dt, Re z>0,

with Hardy norm (1/(2pi)) integral_R |Lf(iy)|^2 dy. Paley--Wiener identifies
these norms. Fourier signs, the half-plane and the factor 2pi are fixed here.
Let

    b=1/2+a, c=1/2-a, 0<a<1/2,
    Theta_a(z)=xi(z+c)/xi(z+b),
    xi(w)=w(w-1)pi^(-w/2)Gamma(w/2)zeta(w)/2.

We import the classical meromorphic continuation, functional equation and
real symmetry of xi, and the standard Hardy inner--outer/cyclic-subspace
theorem. No innerness of Theta is imported. Complete explanations of the
specific applications are given below. See EXTERNAL_INPUTS.md.

## 2. A positive source built from factorials

For t>=0 define r(t)={exp(t)} and

    g(t)=1-r(t)+integral_0^t r(u)du,
    d_b(t)=exp(-bt)g(t).
                                                     (C1)

At integer activations use the right-continuous fractional part. For
N=floor(exp(t)), elementary integration of floor(exp(u)) gives exactly

    g(t)=N(1-t)+log(N!).                              (C2)

In particular g(0)=1; g has slope -N between consecutive logarithmic knots
and an upward jump of ONE at log n (n>=2). The positive integral expression,
not cancellation-prone numerical evaluation of log(N!), gives

    0<g(t)<=1+t,    t>=0.                            (C3)

For every b>0, d_b belongs to L1 intersection L2, with

    ||d_b||_2^2 <= U_b^2:=1/(2b)+1/(2b^2)+1/(4b^3).  (C4)

### Exact transform

For Re w>1, counting integers and integrating each step yields

    zeta(w)/w = 1/(w-1) - integral_0^infinity r(t)exp(-wt)dt.

The integral is analytic for Re w>0. Thus the identity extends meromorphically
there. Multiplying by (w-1)/w and using (C1) proves

    D_b(z):=Ld_b(z)=(z+b-1)zeta(z+b)/(z+b)^2.          (C5)

The apparent singularity at z+b=1 is removed; its value there is 1. There is
no real zero on z>0 because d_b is positive. Within Re z>0 the zeros of D_b
are EXACTLY the zeta zeros with real part greater than b, shifted by -b,
with their complete multiplicities. No zero ordinate defines d_b.

This is a regularized fractional-part source in the Nyman--Beurling family.
The factorial formula is a useful explicit coordinate, not a priority claim
for a new characterization of zeta zeros.

## 3. An explicit causal output with the critical quotient

Set

    j_a(t)=2pi^a/Gamma(a) * exp(-ct)(1-exp(-2t))^(a-1), t>0,
    h_b(t)=exp(-bt)1_(t>=0),
    r_a=delta_0-2a h_b(t)dt.

Euler's beta integral gives

    Lj_a(z)=pi^a Gamma((z+c)/2)/Gamma((z+b)/2).         (C6)

Here j_a is positive and integrable: it behaves like a constant times
 t^(a-1) at zero and decays exponentially at infinity. Define the output
by ordinary causal convolutions, with r_a a finite signed measure:

    n_a = r_a * r_a * r_a * j_a * d_c.               (C7)

Young's inequalities show n_a belongs to L1 intersection L2. Its transform is

    N_a(z)=pi^a ((z+c)/(z+b))^3
             Gamma((z+c)/2)/Gamma((z+b)/2) D_c(z).
                                                     (C8)

Every factor is analytic for Re z>0; the canceled zeta pole in D_c is retained
with its removable value. Direct substitution of xi gives

    N_a(z)=Theta_a(z)D_b(z)                          (C9)

as a MEROMORPHIC identity. N_a itself has no poles in this half-plane.
For w=b+iy, z+c=1-conj(w); reflection and real symmetry of xi imply

    |N_a(iy)|=|D_b(iy)|                              (C10)

for every real y, including zeros by continuity. Nothing in this step assumes
that the quotient is analytic at an interior zero of D_b.

## 4. The source-defined exact isometry

Fix eta>0 and let R_eta be the causal all-pass operator

    R_eta f=f-2eta exp(-eta t)*f,
    LR_eta f(z)=r_eta(z)Lf(z),
    r_eta(z)=(z-eta)/(z+eta).

It is an isometry on H because |r_eta(iy)|=1. Set

    M_b=closure span{R_eta^j d_b:j>=0},
    M_a^out=closure span{R_eta^j n_a:j>=0}.            (C11)

These spaces and the generating vectors are defined without zeta zeros.
For any finite coefficients q_j, (C10) and Plancherel prove the FULL identity

    ||sum_j q_j R_eta^j d_b||_2^2
       =||sum_j q_j R_eta^j n_a||_2^2.                (C12)

All complex cross terms are included. Thus

    V_a(R_eta^j d_b)=R_eta^j n_a                     (C13)

extends uniquely to a surjective isometry M_b -> M_a^out. In particular
||V_a||=1 in the inherited metric. We have neither chosen a new metric to
force this equality nor assumed a positive Xi Pick kernel.

The Beurling cyclic-subspace theorem identifies the inner factors:

    D_b=B_b O_b,    N_a=C_a O_b,
    L(M_b)=B_b H2,  L(M_a^out)=C_a H2.                (C14)

A constant phase can be placed in C_a; the outer factor is common because of
(C10). The spaces do not depend on the choice of eta. Their invariance under
all causal translations follows either from (C14) or its continuous version.
On Hardy space the zero extension of V_a is the partial isometry

    M_Ca M_Bb^*,                                     (C15)

whose initial projection is onto B_b H2. It need NOT be the Toeplitz
compression P_+ M_Theta, which has a different order of factors.

### Why B_b has no singular inner factor

D_b is bounded analytic on Re z>0 by (C3). It extends analytically across
every finite boundary interval: the only possible pole z=-b is outside it
and the zeta pole is canceled. Its boundary zeros are isolated, of finite
order. The singular measure of an inner factor must therefore be supported
on that discrete boundary-zero set. A finite-order analytic zero has local
logarithmic growth, not the 1/x decay of an atomic singular factor, so no such
atom is possible. A singular measure supported on a countable set and with
no atoms is zero. An exponential inner factor exp(-tau z), tau>0, would force
|D_b(x)|<=||D_b||_infinity exp(-tau x), whereas (C5) gives D_b(x)~1/x as
x->+infinity. Hence that factor is absent as well.

Consequently B_b is precisely a Blaschke product of the shifted zeta zeros
Re rho>b, with multiplicities. In particular

    M_b=H  iff  D_b is outer
           iff  zeta has no zero in Re w>b.          (C16)

The same argument applies to N_a (its real-axis decay is a nonzero constant
times x^(-1-a)); C_a also has no singular inner factor.

## 5. The actual causal convolution, not just a boundary multiplier

Let s=2a, beta_s and alpha_s be the densities from the parent gamma regrouping:

    beta_s(t)=2pi^a/Gamma(a) exp(-3t)(1-exp(-2t))^(a-1),
    alpha_s=exp(-st)*beta_s.

With F_s(n)=product_(p|n)(1-p^(-s)), define

    k_a^0(t)=exp(bt)[beta_s(t)-s alpha_s(t)],
    k_a(t)=sum_(n<=exp(t)) F_s(n)n^(b-1)k_a^0(t-log n).
                                                     (C17)

There are finitely many summands on every compact time interval. Each local
singularity is of integrable order (t-log n)^(a-1). Thus k_a is L1_loc.
In the absolutely convergent initial half-plane Re z>b,

    Lk_a(z)=Theta_a(z).                              (C18)

Proof: at q=z-b, the positive locally finite source has transform
Z_s(q)=zeta(1+q)/zeta(1+s+q). The transform of alpha_s is A_s(q).
Since alpha_s(0)=0, beta_s-s alpha_s=alpha_s' has transform q A_s(q).
Thus the right side of (C17) has transform q A_s(q)Z_s(q), which is exactly
xi(1+q)/xi(1+s+q). This is Theta_a(z).

Convolution with k_a is bounded on L2(0,T) for each finite T by Young's
inequality. It agrees with V_a on all M_b. First check finite rational-filter
combinations using (C9), (C18), and Laplace uniqueness in the initial
half-plane. Then take limits: V_a converges globally in L2 and convolution
converges on every finite horizon by its local operator bound. This proves

    V_a f = k_a*f   a.e. locally and globally, f in M_b. (C19)

Thus the isometry is an ACTUAL causal critical-source map on its stated
domain, not an inference from one meromorphic boundary integral.

### Maximal L2 domain and cancellation

Let G be the common inner divisor of B_b and C_a, and write B_0=B_b/G,
C_0=C_a/G. Then the maximal causal domain is exactly

    {f in H:k_a*f in H}=L^{-1}(B_0 H2).              (C20)

Indeed Laplace uniqueness implies B_0 L(k_a*f)=C_0 Lf. Coprime inner
factorization forces B_0 to divide Lf. Conversely Lf=B_0 H implies the
output C_0 H is in H2 and coincides with the causal convolution by initial
Laplace uniqueness. It has the same norm. This handles ALL net pole orders.

The source-generated M_b may be smaller than this maximal domain if actual
numerator/denominator zeros cancel. We do not silently equate the two.
Completeness of M_b is a cancellation-free sufficient condition, and its
all-dyadic-scale version is exactly RH by (C16).

## 6. Direct recovery from the parent's positive Jordan measure

This is a distributional bridge, NOT a bounded map from L2(mu_a).
Retain the exact parent mu_a and S_a=Lmu_a, and set

    Q_a(q)=q^2+kappa_* a q+4a^2,
    P_a(q)=(q+a)^2(q+2a)^2(q+4a)^2,
    T_a(q)=q^3 P_a(q)/Q_a(q), kappa_*=sqrt(275/14).

The parent's centered identity gives exactly

    q A_(2a)(q)Z_(2a)(q)=T_a(q)S_a(q)+c_(2a)A_(2a)(q).
                                                     (C21)

The rational T_a has a polynomial part of degree seven and a strictly proper
stable remainder: both roots of Q_a have negative real part. Apply that
causal differential/convolution operator to the density of mu_a and add
c_(2a)alpha_(2a). Multiplication by exp(bt) then yields k_a in (C17).
On each finite interval this is well defined in causal distributions and
indeed locally integrable. Near an activation knot the leading density has
order t^(a+6); seven derivatives have order t^(a-1), with all lower initial
jets zero. The proper remainder is an ordinary stable exponential kernel.

This supplies the missing exact desmoothing recipe without pretending that
positive exponential evaluation in L2(mu_a) is defined. Its global bound in
that old Hilbert metric is NOT established. The controlled map (C13) uses
the new factorial source in Lebesgue L2 and retains its explicit domain.

## 7. A uniform small-time contraction

For 0<a<1/2 and every T>0 define

    H_a(T)=[1+2a T exp((1/2-a)T)] (2pi T)^a/Gamma(1+a).

Then

    ||k_a||_(L1(0,T))
      <= H_a(T) sum_(n<=exp T)F_(2a)(n)n^(a-1/2),    (C22)

and this is an explicit finite-horizon operator bound on the ENTIRE
L2(0,T), not just M_b.

To prove it, use 1-exp(-2t)>=2t exp(-2t) and a<=1 to obtain

    exp(bt)beta_(2a)(t)
        <= (2pi)^a t^(a-1)exp(-(1/2+a)t)/Gamma(a).

Also exp(bt)alpha_(2a)=exp((1/2-a)t)*[exp(bt)beta_(2a)].
Integrating absolute values gives H_a(T) for the unit component; summing all
active arithmetic delays gives (C22).

For T<=1/32 only n=1 occurs. Log-convexity of Gamma and gamma_E<1 imply
Gamma(1+a)>=exp(-a). Further,

    exp(T/2)<=64/63,
    exp(2T exp(T/2))<=63/59,
    2pi eT <33/56,
    (33/56)(63/59)=2079/3304 <2/3.

Here exp(x)<=1/(1-x) for 0<=x<1, pi<22/7 and e<3 suffice.
Using 1+x<=exp(x) in H_a yields the strict all-hard-scale bound

    ||f -> k_a*f||_(L2(0,T)->L2(0,T)) <(2/3)^a<1,
    0<a<1/2, 0<T<=1/32.                            (C23)

This is a LOCAL contraction only. It does not provide a common bound at
arbitrarily large T. ATTEMPT.md records the unsuccessful extension.

## 8. Boundary

Constructed: explicit actual input/output sources, full polarized equal-norm
identity, causal isometry on its source-generated domain, exact maximal
domain description, direct Jordan desmoothing, and a finite-horizon bound
with strict uniform short-time contraction. NOT constructed: a full-domain
critical Schur multiplier for every a>0, an original-metric global map out
of L2(mu_a), or the required cyclicity theorem. No independent novelty claim.
