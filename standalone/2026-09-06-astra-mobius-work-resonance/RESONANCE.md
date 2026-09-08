# MWR26: boundary zeros force quantitative inverse-energy growth

Status: PROPOSED COMPLETE COMPONENT PROOFS; independent review pending.
This is an unconditional lower-bound theorem, not a proof of RH. No
asymptotic expansion over ALL zeros, simplicity assertion, or linear
independence assumption about zero ordinates is used.

## 1. A general local convolution theorem

Let d and f be causal functions with exponential decay times a fixed
polynomial. Let their Laplace transforms be D and F. Suppose h is locally
square integrable and

    d*h=f

on every finite interval. h need not be globally L2, tempered, or free of
exponentially growing components. Suppose lambda_j=i gamma_j, 1<=j<=r,
are distinct imaginary-axis zeros of D, all of EXACT multiplicity m>=1,
and F(lambda_j)!=0.

**MWR26.T2 (finite-packet resonance lower bound).** Then

    liminf_(T->infinity) T^(-(2m-1)) integral_0^T |h(t)|^2dt
       >= (1/(2m-1)) sum_(j=1)^r
                 |m F(lambda_j)/D^(m)(lambda_j)|^2.       (R1)

The inequality holds for every fixed finite selection. No assertion of
uniform error in a growing zero packet is needed. For zeros with different
multiplicities, apply (R1) to any selected common-multiplicity subset; in
particular any higher-multiplicity zero supplies its stronger power.

### 1.1 Divide by a boundary zero without creating an unstable kernel

Let p=m-1 and e_lambda,p(t)=e^(lambda t)t^p/p!. Define

    w_j=d*e_lambda_j,p.

The zero conditions D^(k)(lambda_j)=0, k<m, give the EXACT tail identity

    w_j(t)= - e^(lambda_j t)/p! *
               integral_t^infinity d(u)e^(-lambda_j u)(t-u)^p du.
                                                               (R2)

Indeed expansion of (t-u)^p makes its integral on [0,infinity) zero by
the m moment conditions. Because Re(lambda_j)=0 and d decays exponentially,
(R2) shows w_j decays exponentially times a polynomial. All its absolute
moments are finite. Its transform satisfies

    W_j(z)=D(z)/(z-lambda_j)^m,
    W_j(lambda_j)=D^(m)(lambda_j)/m! !=0.              (R3)

Causal associativity on each compact interval proves

    w_j*h=e_lambda_j,p*f=:y_j.                        (R4)

No unjustified whole-line Fourier transform of h is used.

Since f decays exponentially, the polynomial convolution in (R4) gives

    y_j(t)=e^(lambda_j t)[F(lambda_j)t^p/p!+O(t^(p-1))]
                                                               (R5)

for p>=1. For p=0 the remainder is exponentially small times a polynomial.
In both cases the estimates are uniform in t for each fixed j and packet.

### 1.2 Apply the finite-interval adjoint, not a boundary-value heuristic

On L2(0,T) let C_(j,T) be causal convolution by w_j, and set

    q_(j,T)(t)=e^(i gamma_j t)t^p,
    v_(j,T)=C_(j,T)^* q_(j,T),
    S_T=T^(2p+1)/(2p+1).

Then, in the convention <u,v>=integral conjugate(u)v,

    <v_(j,T),h>=<q_(j,T),y_j>
       = S_T F(lambda_j)/p! + O(T^(2p)).             (R6)

For p=0 the remainder is O(1), as required by the same formula.
Directly,

    v_(j,T)(u)=e^(i gamma_j u)
       integral_0^(T-u) conjugate(w_j(v))e^(i gamma_j v)(u+v)^p dv.

Complete the integral to infinity. Exponential moment bounds for w_j and
binomial expansion give

    ||v_(j,T)-conjugate(W_j(lambda_j))q_(j,T)||_2
          =O((1+T)^p)=o(sqrt(S_T)).                  (R7)

Here is why the endpoint is controlled. The polynomial terms with a positive
power of v have degree at most p-1 in u, hence L2 norm O(T^(p-1/2)) for
p>=1. The omitted tail v>T-u is bounded by a polynomial in T times an
exponential in -(T-u); its L2 norm is O((1+T)^p). At p=0 only that tail
remains, of O(1) norm. All implied constants may depend on the fixed zeros.

For j!=k, one integration by parts gives

    integral_0^T t^(2p)e^(i(gamma_k-gamma_j)t)dt=O(T^(2p)),

with the bounded p=0 case understood. Thus the Gram matrix G_T of the v_j
has

    G_T/S_T -> diag(|W_j(lambda_j)|^2).              (R8)

The limit is positive definite. The finite Gram projection inequality,
valid without any a priori bound on ||h||, is

    ||h||_(L2(0,T))^2 >= a_T* G_T^(-1) a_T,
    (a_T)_j=<v_(j,T),h>.

Combine (R6)-(R8) and divide by T^(2p+1). Since
m!/(m-1)!=m, this proves (R1).

### 1.3 The general coefficient is sharp

For any beta>0, real gamma, and integer m>=1, take

    D(z)=(z-i gamma)^m/(z+beta)^(m+1),
    F(z)=(m-1)!/(z+beta)^(m+1),
    h(t)=t^(m-1)e^(i gamma t).

Both d and f have the required stable polynomial-exponential form, and
D Lh=F initially. Here m F(i gamma)/D^(m)(i gamma)=1 and

    integral_0^T |h|^2=T^(2m-1)/(2m-1).

So equality is attained in (R1) for a single target. This is a synthetic
sharpness test for the general theorem, NOT a zeta model.

## 2. Application to the actual pole-neutral Mobius input

Use the literal factorial source from DCP26:

    d(t)=e^(-t/2)g(t),  0<g(t)<=1+t,
    D(z)=D0(z)zeta(z+1/2),
    D0(z)=(z-1/2)/(z+1/2)^2.

The actual input h and target f of WORK_IDENTITY.md obey d*h=f locally and

    F(z)=D0(z)Phi(z),
    Phi(z)=(z-1/2)(z+1/2)^2/(z+1)^4.

For a critical-line zero rho_j=1/2+i gamma_j of exact multiplicity m,
D0(i gamma_j)!=0 and

    D^(m)(i gamma_j)=D0(i gamma_j)zeta^(m)(rho_j).

Therefore (R1) specializes to

    liminf H(T)/T^(2m-1)
       >= (1/(2m-1)) sum_j |m Phi(i gamma_j)/zeta^(m)(rho_j)|^2.
                                                               (R9)

Phi has no zero at a nonzero imaginary point. For a finite set of simple
critical zeros, this reads

    liminf H(T)/T >= sum_j |Phi(i gamma_j)/zeta'(rho_j)|^2.        (R10)

No absence of off-line zeros is assumed. Were they present, they could
make the left side infinite; the proof still works. Both members of a
conjugate pair may be selected, giving their two contributions.

By the classical existence of at least one critical-line zero, and its
finite multiplicity, H(T)>=c T for some c>0 and all sufficiently large T.
If that zero has multiplicity m>1, the stronger T^(2m-1) lower bound holds.
Hence J_N>=H(log N) implies

    J_N>=c log N for all sufficiently large N.                  (R11)

Uniform boundedness, or an unbounded bounded-norm subsequence of THESE
inverse-input J_N, is impossible. This does not rule out bounded factorial
OUTPUT approximants y_T: the stable convolution d suppresses precisely
these boundary resonances.

For all simple critical zeros one may take the supremum over finite sets
in (R10). This is a monotone supremum of lower bounds, not an assumed
convergent infinite explicit formula. If H(T)<=C T eventually, all
critical zeros must be simple and the full nonnegative residue-square sum
is at most C. Together with the parent's off-line detection, such a
linear bound would be stronger than RH alone. A subexponential bound need
not assert simplicity; it remains the correct endpoint for this attempt.

## 3. Application to the other agent's compact inverse

The parallel CD26 construction uses

    m(x)=sum_(n<=x) mu(n)/n,
    v(t)=e^(t/2)m(e^t),
    f0(t)=t e^(-t/2).

Locally, d*v=f0. One proof is the absolutely convergent initial transform
identity

    Lv(z)=1/[(z-1/2)zeta(z+1/2)],
    D(z)Lv(z)=1/(z+1/2)^2.

The apparent real pole cancels with the reciprocal zeta zero; local
uniqueness then proves the convolution identity. No global L2 inverse is
assumed. For integer N,

    integral_0^log(N+1) |v(t)|^2dt = sum_(k<=N)m(k)^2=:S_N.

Applying (R1) gives

    liminf S_N/[log(N+1)]^(2m-1)
       >= (1/(2m-1))sum_j
               |m/[(rho_j-1)zeta^(m)(rho_j)]|^2.               (R12)

Thus its earlier qualitative S_N->infinity conclusion strengthens to
S_N>=c log(N+1) eventually, without RH or a simple-zero hypothesis.
Again this is a cost of the INPUT, not an obstruction to bounded OUTPUT.
The proof is reconstructed here; no new acceptance of CD26's larger
numerical certificate is inferred.

## 4. An elementary finite-T variant

For any single critical-line zero i gamma, even of higher multiplicity,
use m=1 without dividing by W(i gamma). The first-order stable kernel is

    w(t)=-e^(i gamma t)integral_t^infinity e^(-i gamma u)d(u)du.

Its L1 norm obeys

    ||w||_1 <= integral_0^infinity u|d(u)|du <=20.

Let F_t(i gamma)=integral_0^t e^(-i gamma u)f(u)du. Then
w*h=e^(i gamma t)F_t(i gamma), and finite-time Young gives

    H(T) >= (1/400)integral_0^T |F_t(i gamma)|^2dt.              (R13)

For the DCP26 f, a fully explicit tail bound is

    |F(i gamma)-F_t(i gamma)|
       <=e^-t[(3/8)t^3+(21/8)t^2+(25/4)t+25/4].               (R14)

Hence for any t0 with that tail <=|F(i gamma)|/2,

    H(T)>=(T-t0)|F(i gamma)|^2/1600,       T>=t0.              (R15)

These constants require no zeta derivative. No numerical zero location is
used by this packet's certificates. Existence of a critical-line zero is
an imported classical theorem, separately listed in EXTERNAL_INPUTS.md.

## 5. What has not been proved

The lower bounds neither imply an upper bound for W_N nor fill the
critical source domain. They identify which overly strong energy targets
would accidentally demand zero simplicity and stronger derivative controls.
The all-orders finite-packet theorem is analytical; finite tests below do
not machine-prove it. It uses standard convolution/finite-Gram techniques,
not an external novelty or priority claim.
