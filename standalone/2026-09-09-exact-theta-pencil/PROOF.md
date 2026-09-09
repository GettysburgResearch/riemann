# The exact theta differential pencil: a direct whole-function attempt

Date: 2026-09-09.
Status: proposed component derivations and a failed spectral-reality argument.
**This is NOT a proof of RH, a self-adjoint Hilbert–Polya realization, or a new
unconditional zero-location theorem.** Independent mathematical review is needed.
The remaining global assertion is identified in Section 6, not assigned to a
reviewer as routine verification. No priority claim is made for Fourier/theta,
Wronskian, supersymmetric factorization, or differential-pencil methods.

## 0. What changed in this attempt

The existing residual, entropy, graph, and approximation results have not proved
an RH-strength upper bound. The finite gamma approximants in the preceding
packet cannot satisfy the proposed all-height zero-location lemma. This note
therefore works with the UNMODIFIED infinite theta source throughout Sections
1–6. There is no finite-height exhaustion, fitted spectrum, or zero-selected
potential in that construction.

The attempted completion was: construct a positive self-adjoint differential
operator from the source; identify its characteristic equation with xi; then
use spectral reality. The identification below is exact, but it produces a
NON-self-adjoint quadratic pencil, not a self-adjoint eigenvalue equation. Its
positive constant term does not prove reality of its characteristic parameters.
Section 7 tests the proposed generic inference using positive self-reciprocal
heat traces and supplies explicit nonreal characteristic parameters. Those are
changed sources, NOT zeros asserted for zeta.

## 1. The exact source and its normalization

Let

    xi(s) = entire continuation of s(s-1) pi^(-s/2) Gamma(s/2) zeta(s)/2,
    Xi(z) = xi(1/2+i z),
    theta(x) = sum_(n in Z) exp(-pi n^2 x), x>0,
    h(t) = exp(t/2) theta(exp(2t)), t real.

The classical Jacobi identity theta(x)=x^(-1/2)theta(1/x) implies h(-t)=h(t).
Set

    phi(t) = [h''(t)-h(t)/4]/2
           = sum_(n>=1) [4pi^2 n^4 exp(9t/2)-6pi n^2 exp(5t/2)]
                                      exp(-pi n^2 exp(2t)).                 (1)

The full-line Fourier convention is

    Xi(z) = integral_R phi(t) exp(i z t) dt.                               (2)

In particular, the coefficients 4 and 6 in (1) are necessary with (2).
The half-sized kernel would give Xi/2. The sum and its derivatives converge
locally uniformly for real t. On t>=0 every summand is strictly positive;
evenness, not termwise positivity on the negative half-line, proves phi>0
on all of R. Modular inversion also supplies smooth even matching at zero.

For completeness one can verify (2) without using any zeros. Write
psi(x)=(theta(x)-1)/2. Splitting the absolutely convergent theta Mellin integral
at x=1, and applying Jacobi inversion to (0,1), gives the entire continuation

    xi(s) = 1/2 + s(s-1)/2 integral_1^infinity
                       psi(x)[x^(s/2)+x^((1-s)/2)] dx/x.                  (3)

On t>=0 put g(t)=h(t)-exp(t/2)=2exp(t/2)psi(exp(2t)). Then g'(0)=-1/2,
phi=(g''-g/4)/2, and integration by parts twice gives

    2 integral_0^infinity phi(t)cos(z t)dt
      =1/2-(z^2+1/4) integral_0^infinity g(t)cos(z t)dt.

Changing x=exp(2t) in (3) with s=1/2+iz proves (2). All boundary terms at
infinity vanish faster than any exponential. The calculation first holds
on bounded complex z sets and the same domination proves it everywhere.

The n=1 term gives, as t tends to +infinity,

    phi(t)=4pi^2 exp(9t/2-pi exp(2t))
                    [1-3exp(-2t)/(2pi)+O(exp(-3pi exp(2t)))].             (4)

A fixed number of differentiated remainders has the corresponding bound with
an additional fixed polynomial in exp(2t). This follows by differentiating the
series, then bounding n>=2 by its exponentially decreasing tail; that error
is smaller than every power of exp(-t). In particular, for

    V(t)=-log phi(t),       C(t)=V'(t)/2,

V is real smooth and even, C is real smooth and odd, and

    V(t)=pi exp(2t)-9t/2-log(4pi^2)+O(exp(-2t)),
    C(t)=pi exp(2t)-9/4+O(exp(-2t)),
    C'(t)=2pi exp(2t)+O(exp(-2t)).                         (t->+infinity)  (5)

These statements hold after every fixed number of derivatives that is used
below. Reflection gives the negative tail. Consequently C^2 tends to infinity
at both ends and, for every epsilon>0,

    |C'(t)| <= epsilon C(t)^2 + K_epsilon, all real t.                     (6)

Neither global convexity of V nor RH is required in what follows.

## 2. A genuinely positive base, with its domain specified

All Hilbert norms in this section are in L2(R,dt). Start with

    A0 f = -f'+C f, f in C_c^infinity(R),
    q[f] = ||A0 f||^2.

Integration by parts gives

    q[f] = ||f'||^2 + ||C f||^2 + integral_R C'|f|^2.                     (7)

By (6), q[f]+K||f||^2 is equivalent to
||f'||^2+||C f||^2+||f||^2, for a sufficiently large fixed K. The closure
of the form therefore has domain

    Q = {f in H^1(R): C f in L2(R)}.                                     (8)

Cutoff and subsequent smoothing prove C_c^infinity is a form core: the
cutoff derivative error tends to zero in L2, the weighted tails tend to zero,
and C is bounded and smooth on each compact set. Thus the form is closed,
densely defined, and nonnegative. Let H be its associated self-adjoint operator:

    H = A0* A0 = -d^2/dt^2 + C^2 + C',                                 (9)
    Dom(H) = {f in Q: -f''+(C^2+C')f belongs to L2 in distributions}.

The embedding Q into L2 is compact. On a fixed compact interval use the
one-dimensional compact H^1 embedding; outside it use
integral_|t|>R |f|^2 <= [inf_|t|>R C^2]^-1 ||Cf||^2. A diagonal subsequence
then proves compactness. Hence H has compact resolvent.

Its kernel is zero. Equality q[f]=0 implies -f'+Cf=0 distributionally,
so f is a constant multiple of exp(V/2), which is not in L2. Compactness
and nonnegativity now imply

    H >= lambda0 I for some lambda0>0.                                  (10)

No numerical value of lambda0, relation of its eigenvalues to zeta ordinates,
or claim that (10) is itself RH-bearing is made.

Multiplication by C is bounded from Q with its form norm to L2. For f in
Dom(H), (7) and (6) give

    ||Cf||^2 <= K[ <f,Hf>+||f||^2 ].                                    (11)

Cauchy–Schwarz and the scalar Young inequality then make C infinitesimally
H-bounded: ||Cf||<=epsilon||Hf||+K_epsilon||f||. This specifies a common
operator domain for the entire family

    P(z)=H-i z C-z^2 I/4,       Dom(P(z))=Dom(H), z in C.                (12)

The family is closed on that domain. For clarity about the spectral boundary,
P(z)H^-1=I-iz CH^-1-z^2 H^-1/4 is identity plus a compact operator.
Indeed H^-1/2 is compact and CH^-1/2 is bounded by (11). Thus P(z), as a
map Dom(H) with its graph norm to L2, is Fredholm of index zero. We do not
assert a specific regularized Fredholm determinant or identify multiplicities
of such an unconstructed determinant. The characteristic Wronskian below is
explicit and suffices.

## 3. Exact characteristic equation at EVERY complex parameter

Define, for every complex z,

    Q_z(t)=exp(V(t)/2-i z t/2),
    I_-(t,z)=integral_-infinity^t phi(u)exp(izu)du,
    I_+(t,z)=integral_t^infinity phi(u)exp(izu)du,
    y_-(t,z)=Q_z(t)I_-(t,z),
    y_+(t,z)=Q_z(t)I_+(t,z).                                             (13)

There is no zero input in any of these definitions. Direct differentiation
of (12) gives the factorization of differential expressions

    P(z)=(d/dt+C-iz/2)(-d/dt+C-iz/2).                                  (14)

Since Q_z'/Q_z=C-iz/2 and I_-'=Q_z^-2=-I_+', both y_- and y_+ solve
P(z)y=0. Their Wronskian, in the convention W(f,g)=f g'-f' g, is EXACTLY

    W(y_-,y_+)=-Q_z^2 Q_z^-2 (I_-+I_+)=-Xi(z).                          (15)

This is the actual whole xi function, with the normalization of Section 1.
It is not an asymptotic identity or a finite approximation.

### 3.1 Boundary and operator-domain conditions

Here is the tail estimate needed to use (15). On the positive tail, uniformly
for z in a fixed compact set, integrate once using

    d[phi(t)e^{izt}]/dt=-(V'(t)-iz)phi(t)e^{izt}.

The derivative of 1/(V'-iz) is -V''/(V'-iz)^2=O(exp(-2t)). For sufficiently
large t the real part V'(t)+Im(z) is positive. Its exponential growth bounds
the absolute integral of the remainder. Equivalently change variables v=exp(2u)
inside the integral and use an endpoint Laplace estimate. This gives

    I_+(t,z)=phi(t)e^{izt}/[V'(t)-iz] [1+O_z(exp(-2t))].                 (16)

One explicit justification of the relative error is the following. With
w_z=phi e^{izt}, the remainder is an integral of w_z V''/(V'-iz)^2.
For u>=t the absolute derivative quotient is O(exp(-2t)); moreover
integral_t^infinity |w_z(u)|du <= K |w_z(t)|exp(-2t),
while |w_z(t)/(V'(t)-iz)| is comparable to |w_z(t)|exp(-2t).
These inequalities follow from (5) by the substitution v=exp(2u), uniformly
on the same compact parameter set. They bound the relative error as stated.
Reflection supplies the negative-tail estimate for I_-.

Thus y_+ decays faster than every exponential at +infinity, while Q_z grows
faster than every exponential there. The same holds for y_- at -infinity.
For the decaying solution, the derivative formula

    y_+'=(C-iz/2)y_+ - Q_z^-1

shows y_+' and Cy_+ lie in L2 on that tail. The ODE shows
H y_+=(izC+z^2/4)y_+ lies in L2 there. The negative endpoint is identical.
All integrations by parts below therefore have zero boundary terms when the
two decaying solutions join. In particular their derivatives, Cy, and t y
have the required integrability; no unweighted plane wave is put into L2.

Every local solution has form Q_z(t)[a+b I_-(t,z)]. The negative L2 condition
forces a=0. The positive L2 condition then forces b Xi(z)=0, since
I_-(t,z)=Xi(z)-I_+(t,z). At a zero the resulting solution is nonzero: I_-'
never vanishes. Hence

    ker P(z) != {0}  IFF  Xi(z)=0;                                     (17)
    dim ker P(z)=1 whenever Xi(z)=0.

The geometric dimension assertion is NOT simplicity of a zero of Xi.
Equation (15) retains every analytic multiplicity of Xi without assuming it
is one. The full characteristic set in (17) is discrete, since Xi is nonzero
entire. No numerical zero census has been imported.

## 4. The direct energy attempt, and the missing equality

Let z=a+ib be a characteristic parameter, with a nonzero state y in Dom(H).
Write N=||y||^2, c=<y,Cy> (real), and h=<y,Hy> (real). Equation (12) gives

    h-iz c-z^2 N/4=0.                                                  (18)

There are no imaginary-axis characteristic parameters, because
Xi(ib)=integral phi(t)cosh(bt)dt>0. Thus a is nonzero at every characteristic
parameter. Separating the imaginary and real parts of (18) proves

    c=-b N/2,            h=|z|^2 N/4,                                 (19)
    integral_R V'(t)|y(t)|^2 dt = -Im(z)||y||^2.                        (20)

This is a useful exact diagnostic, but not a reality proof. It allows b!=0.
Positivity of H bounds |z| from below; it does NOT set b to zero.

The sufficient missing statement is now completely explicit:

    For the UNMODIFIED phi of (1), every nonzero solution of (12)
    satisfying both L2 endpoint conditions has
                  integral V'(t)|y(t)|^2 dt=0.                        OPEN

If OPEN were proved, (20) would force all characteristic parameters real;
(17) would then prove RH. Conversely under RH all parameters in (17) are real
and (20) proves OPEN. This is an equivalence, NOT an independent hypothesis
that has been cheaply established. No proof of OPEN is supplied.

### 4.1 Why reflection does not establish OPEN

Let R be spatial parity, (Rf)(t)=f(-t). Since C is odd and H is even,

    R P(z) R = P(-z),          P(z)* = P(-conjugate(z)).                 (21)

For real z, R P(z) is self-adjoint, but R is an INDEFINITE unitary: it is +1
on even functions and -1 on odd ones, both infinite-dimensional subspaces.
This is not a positive-Hilbert-metric self-adjoint eigenvalue problem.

More concretely, at a characteristic parameter the normalized state (13)
satisfies

    y_-( -t,z) = -y_-(t,-z),
    conjugate(y_-(t,z)) = y_-(t,-conjugate(z)).                          (22)

The first equality uses Xi(z)=0; the second uses the real source. Together
these relate the state at z to the state at conjugate(z). They imply an even
modulus when z is REAL, but not when z is nonreal. Replacing the state at
conjugate(z) by the state at z would assume the reality one is trying to prove.

Likewise the two factors in (14) are NOT adjoints for nonzero real z:
(-d/dt+C-iz/2)*=d/dt+C+iz/2, with the opposite sign. Dropping that distinction
turns a valid characteristic realization into an invalid Hilbert–Polya proof.

### 4.2 A derivative identity does not prove simplicity either

With the normalization y=y_-(.,z) at a characteristic parameter, one also has

    Xi'(z)=integral_R (iC(t)+z/2) y(t)^2 dt.                            (23)

To verify it, y'=(C-iz/2)y+Q_z^-1 and y/Q_z=I_-. Therefore
(-iC-z/2)y^2=-(i/2)(y^2)'+i I_-. Integrating, using both endpoint estimates,
and integral I_-=-integral t phi(t)e^{izt}dt, proves (23). Every integral
converges. The square in (23) is BILINEAR, not |y|^2. No positivity or
nonvanishing of the right side is inferred. Multiple xi zeros are allowed.

## 5. The same unresolved sign in the direct Fourier calculation

There is also an entirely division-free route. Put U(x,y)=|Xi(x+iy)|^2. From
(2), Fubini and the change of variables (u,v) to (u+v,u-v), with Jacobian 2,

    partial_y U(x,y) = 4 integral_R K_y(v) cos(2xv)dv,
    K_y(v)=integral_R u sinh(2yu) phi(u+v)phi(u-v)du, y>0.               (24)

Every integral and each fixed derivative converges locally uniformly in x,y.
The kernel K_y is positive pointwise. That is NOT a proof that its Fourier
transform is nonnegative. The associated-kernel/Laguerre approach is classical;
this is not claimed as a new general RH criterion.

A proof of partial_y U>=0 for all real x and y>0 would prove RH directly. If
Xi(x0+iy0)=0, monotonicity and U>=0 would make U(x0,y)=0 on [0,y0], forcing
the nonzero entire Xi to vanish identically. Reflection handles y<0.
We did not establish this sign. Equations (20) and (24) are two descriptions
of the same unresolved source-specific reality problem, not two proved
estimates that can be combined to close it.

## 6. What was actually tried to finish the proof

The proposed closure was OPEN via parity of the potential and positivity of H.
Equations (18)–(22) show the exact failure of that inference. A second attempt
was positivity in (24) from the positive theta weights and Jacobi symmetry.
That drops the oscillatory cosine or implicitly assumes positive definiteness
of K_y. It too does not prove the source-specific inequality.

The next section strengthens the test: even positive SELF-RECIPROCAL theta-type
heat traces can satisfy these structural properties and have explicitly nonreal
characteristic parameters. Accordingly, the literal integer-square theta
spectrum, rather than just positivity and modular inversion, must enter any
successful proof in these coordinates. This is a statement about the failed
method's hypotheses, not a proof that every route needs the same intermediate
objects or a claim to have exhausted possible uses of modular symmetry.

## 7. An exact self-reciprocal heat-trace control

Fix d>0 and 0<eta<1/2, and set

    c=cosh(d eta),      D=c+cosh(d/2),
    theta_(d,eta)(x) = [c theta(x)
           +(e^(d/2)/2)theta(e^(2d)x)
           +(e^(-d/2)/2)theta(e^(-2d)x)]/D.                            (25)

This is a strictly positive Laplace sum with positive atomic weights. The
constant term is one. It is completely monotone in x>0, with the convention
that the constant term has zero higher derivatives. All its Laplace sums and
derivatives converge on compact subsets of x>0. Direct use of Jacobi's identity
exchanges the last two terms and proves EXACTLY

    theta_(d,eta)(x)=x^(-1/2)theta_(d,eta)(1/x).                         (26)

In logarithmic coordinates,

    h_(d,eta)(t)=[c h(t)+(h(t+d)+h(t-d))/2]/D,
    phi_(d,eta)(t)=[c phi(t)+(phi(t+d)+phi(t-d))/2]/D.                  (27)

Thus phi_(d,eta) is positive, even, smooth, and superexponentially decreasing.
Its completed Fourier transform is

    Xi_(d,eta)(z)=Xi(z)[cosh(d eta)+cos(dz)]/D.                          (28)

The entire completed function xi_(d,eta)(s)=Xi_(d,eta)(-i(s-1/2)) satisfies
xi_(d,eta)(s)=xi_(d,eta)(1-s) and xi_(d,eta)(0)=xi_(d,eta)(1)=1/2. It is
real under conjugation and positive on the real segment [0,1]. It is entire
of order one: its multiplier has exponential type and the real-axis growth
of xi retains order one. No zeros have been used to choose the source.

Nonetheless, for every integer k,

    z_k^+ = (2k+1)pi/d + i eta,
    z_k^- = (2k+1)pi/d - i eta                                  (29)

are nonreal zeros of Xi_(d,eta). They are simple zeros of the displayed
multiplier, since sin((2k+1)pi +/- i d eta) is nonzero; if Xi also vanishes
there the multiplicity increases, never cancels. Under the s coordinate,
these are at Re s=1/2 +/- eta inside the critical strip. No assertion that
they are zeros of the UNMODIFIED Xi is made.

There is an additional exact constraint on what a proposed reality proof can
use. For EVERY real x,

    [cosh(d eta)-1]/D <= Xi_(d,eta)(x)/Xi(x)
                                <= [cosh(d eta)+1]/D,                  (30)

where the quotient means the entire multiplier in (28), including removable
values at real zeros. Both bounds are strictly positive. Thus the changed
function has EXACTLY the same real zero divisor, with the same multiplicities
and real signs, as the original Xi. This is not a finite zero-table comparison.
It still has all the additional nonreal zeros (29). Therefore even complete
knowledge of the critical-line zero divisor together with these structural
properties would not establish the claimed all-zero conclusion for this
larger source class. No assertion that (30) is a uniformly vanishing relative
error as d->0 is made; its oscillations persist at heights of order 1/d.

The same differential construction applies to this changed positive source.
Its positive-tail leading term is the translate phi(t-d), so its log potential
has the form pi e^(-2d)e^(2t)-9t/2+O(1), with the differentiated bounds of
Section 2. It therefore also has a positive self-adjoint base H_(d,eta),
compact resolvent, and the symmetries (21), but has the nonreal parameters
(29). Equations (25)–(29) refute the GENERIC reality inference used in Section 6.

The control does NOT retain theta's literal spectrum {pi n^2:n in Z} or the
ordinary unit Euler factors. For any d>0, the extra atom pi e^(-2d), coming
from n=1, lies strictly between zero and pi and has positive weight; it cannot
be canceled. Thus the specific arithmetic source is genuinely changed.

### 7.1 Small source errors are also insufficient for a global inference

For fixed eta, as d decreases to zero the functions phi_(d,eta) approach phi
in each seminorm integral e^(B|t|)|partial_t^j(phi_(d,eta)-phi)|dt, with error
O_(B,j,eta)(d^2), for fixed finite B,j. Taylor's integral remainder proves
this: the symmetric translation difference is bounded in the weighted L1
norm by d^2 e^(B d)||phi^(j+2)||_(weighted L1); the denominator correction
D-(c+1)=cosh(d/2)-1 is O(d^2). All those weighted derivative norms are finite.
The same argument works in weighted L2.

Thus the entire transforms converge on every fixed compact with O_K(d^2)
error, while their extra zeros have real parts of size 1/d and do not survive
in any fixed compact as d->0. This is a concrete nonuniform-height warning,
NOT an off-line zero or an instability theorem for the unmodified xi.

This modest finite-shift construction is not claimed novel. Its purpose is
to test the actual assumptions of this direct theta/pencil attack, rather
than relying on a unrelated positive polynomial or a changed Hilbert metric.

## 8. Scope, literature, and honest stopping point

Sections 1–4 provide an exact all-parameter differential realization of the
whole Xi function and the correct energy identities. They do not provide a
fixed self-adjoint operator whose eigenvalues are all zeta ordinates. Section
7 proves that source positivity, Jacobi-type inversion, endpoint normalization,
entireness of order one, and positivity of the differential base are together
insufficient. The unmodified lattice coefficients might supply a further
identity, but none proving OPEN or the sign in (24) has been established here.

The primary classical inputs are the Jacobi transformation and split Mellin
formula (DLMF 20.7 and 25.4–25.5), and basic closed-form/compact-embedding
operator theory. The domain argument needed here is included. Csordas,
arXiv:1309.0055v2, Sections 3–4, is explicit prior art for associated Fourier
kernels, Laguerre tests, and the distinction between positive kernels and
positive-definite kernels. McGuigan, arXiv:2002.12825, is relevant prior work
on theta/xi-inspired supersymmetric potentials; its abstract was inspected,
not its full paper. No priority claim or theorem import from that paper is made.

Only bounded symbolic algebra is checked by the accompanying program. No
numerical xi zero, actual potential eigensolve, all-height inequality, complete
repository audit, formal proof, or new numerical positive range is claimed.
The manuscript is a record of a direct attempt at the FULL problem and its
precise failure, not a completed proof proposal awaiting cosmetic review.
