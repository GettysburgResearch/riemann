# Direct closure attempt: the exact normalized phase and the spectral sign

Date: 2026-09-10.
Status: UNSUCCESSFUL RH PROOF ATTEMPT. The global inequalities labelled OPEN
below are not proved. The auxiliary deductions have written proofs but have
not received independent mathematical review or formal verification.

This is not a new graph refinement, not a new numerical RH claim, and not a
claim of progress measured by the number of files or tests. It records the
attempt to finish the exact-theta approach after PR #835, and a cross-check
against the full-source determinant of PR #834. No predecessor is revised.

## 1. Frozen source and the full desired conclusion

Use the original completed function, with analytic pole removal,

    F(z) = xi(1/2+iz) = 2 integral_0^infinity Phi(u) cos(zu) du,
    Phi(u) = sum_(n>=1) phi_n(u),
    phi_n(u) = [4pi^2 n^4 exp(9u/2)-6pi n^2 exp(5u/2)]
                    exp[-pi n^2 exp(2u)].

The complete Phi is even and smooth on the whole real line; all its
odd derivatives at zero vanish. F is nonzero, real even entire of order one.
Its nontrivial zeros lie in |Im z|<1/2. These are classical theta/xi facts,
not statements of RH. The existence of an unbounded sequence of real zeros
is the classical Hardy theorem; no simplicity or numerical zero is imported.

For fixed N>=1 set

    F_N = 2 integral_0^infinity (sum_(n<=N)phi_n(u)) cos(zu)du,
    T_N = F-F_N,              q_N = pi(N+1)^2.

The TPR26 parent at 4b8fa9abfa9aac5ed1feb7f30acaeeb418ed405c proves,
at its proposed-review status, that Re T_N>0 on |Im z|<=q_N and, on the
critical band,

    Re T_N(x+iy) >= q_N^3 exp(-q_N)/[18(4q_N^2+x^2)],
    |T_N'/T_N| <=4/q_N.

It also gives a relative approximation for the COMPLETE tail, not for F.
The local parent manuscript is authenticated in SOURCES.json; its numerical
backend is not executed in this continuation. The elementary polynomial and
integration-by-parts arguments were read, not silently declared accepted.

The task is to exclude ALL nonreal zeros of the unchanged F. Defining an
operator, an inverse, or a normalized function does not establish that exclusion.

## 2. A simpler sufficient ending: normalized vertical monotonicity

Define on the open critical strip

    Q_N(z)=F(z)/T_N(z).

It is holomorphic there, is real on the real axis, and has exactly the same
zeros and multiplicities as F in that strip. It is NOT assumed to be inner,
outer, Hermite--Biehler, or real-rooted.

The following would be sufficient for RH for even ONE fixed N:

    OPEN-PHASE(N):
    Im[Q_N'(x+iy) conjugate(Q_N(x+iy))] <=0
    for every real x and every 0<y<1/2.                 (P)

This is a sufficient target, not an established estimate or a newly claimed
RH equivalence. No assertion that RH implies this particular normalized
condition is needed or made.

Proof of the sufficient implication. Set U_x(y)=|Q_N(x+iy)|^2. Analytic
differentiation gives

    U_x'(y)=-2 Im[Q_N'(x+iy) conjugate(Q_N(x+iy))].       (1)

Thus (P) makes U_x nondecreasing on [0,1/2). If Q_N(x0+iy0)=0 with
0<y0<1/2, nonnegativity implies U_x0(y)=0 for EVERY 0<=y<=y0. The identity
theorem then makes Q_N, hence F, identically zero. Reality deals with the
lower half of the strip. This proves the implication including multiple zeros.

A stronger, also sufficient, target is

    OPEN-CONVEX(N): L_(Q_N)(x,y)>=0 on the critical strip,
    L_H=|H'|^2-Re[H'' conjugate(H)].                     (C)

Indeed U_x''=2L_(Q_N), and U_x'(0)=0 because Q_N is real on the real axis.
There is NO need to prove that the normalization corrections are smaller
than L_(Q_N) after (C) is established: convexity of Q_N itself excludes
zeros. This removes a redundant sufficient requirement from a possible
completion. It does not prove (C), or the weaker (P).

For clarity the original-function expression for (P) is

    Im[F'(z) conjugate(F(z))]
        - Im[T_N'(z)/T_N(z)] |F(z)|^2 <=0, Im z>0.      (2)

All terms in (2) belong to the exact original source. TPR26 bounds the
second term, not the sign or size of the first.

The covariant second-order identity is also exact. With a=T_N'/T_N and
b=T_N''/T_N,

    L_F/|T_N|^2 = L_Q + (|a|^2-Re b)|Q|^2
                         +4 Im(a) Im(Q' conjugate(Q)).  (3)

Equation (3) is an identity, not an implication from positive real part of T_N.
The classical complex Laguerre criterion and its associated kernels are
credited to the literature cited below and to the parent, not claimed new.

## 3. Why fixed relative tail accuracy cannot supply the missing global sign

The attempted shortcut was to use the positive-real tail together with its
uniform relative approximation, then promote the finite expression's sign to
all frequencies. The following deductions show why a fixed error tolerance
cannot do that on its own. They do NOT refute the sign of the exact Q_N.

### 3.1 Exact cancellation condition number for the literal F

Fix N. The usual gamma and zeta bounds give a constant C0 with

    |F(x+iy)| <= C0(1+|x|)^3 exp(-pi|x|/4), |y|<=1/2.  (4)

Only existence of C0 is used; no numerical C0 is claimed. TPR26 supplies
an elementary Euler--Maclaurin/Stirling derivation. At real x with F(x)!=0,
let

    cond_N(x)=(|F_N(x)|+T_N(x))/|F(x)|.

Since T_N(x)>0, the reverse triangle inequality gives

    cond_N(x) >= 2T_N(x)/|F(x)|-1.

For |x|>=max(1,2q_N), the complete parent lower bound and (4) imply

    cond_N(x) >= [q_N^3 exp(-q_N)/(144C0)]
                          exp(pi|x|/4)/|x|^5 -1.       (5)

At a zero of F the condition number is infinite. Thus fixed-N addition of
the retained terms to their exact remainder is exponentially ill-conditioned
at large real frequency, unconditionally. This is not an assertion that
correct evaluation or a source-specific analytic proof is impossible.

### 3.2 Arbitrarily small constant error in the normalized function destroys
### eventual real Laguerre positivity

The preceding estimates imply

    Q_N(x)->0 as x->+infinity.

Its real zeros include the unbounded real-zero sequence of F, since T_N>0
on the real axis. Q_N is not identically zero.

**Lemma.** Let q be real analytic on a neighborhood of [0,infinity),
q(x)->0, and suppose q has arbitrarily large real zeros but is not identically
zero. For EVERY real epsilon!=0 and EVERY X there exists x>X with

    (q'(x))^2-(q(x)+epsilon)q''(x)<0.                    (6)

Proof. Otherwise choose X sufficiently large that |q|<|epsilon|/2 and (6)
is never negative beyond X. Then ell(x)=log|q(x)+epsilon| is defined there
and

    ell''(x)=-[(q')^2-(q+epsilon)q'']/(q+epsilon)^2 <=0.

It is concave and tends to the finite limit log|epsilon|. Its derivative
cannot be negative at any point, as concavity would force ell to tend to
minus infinity. It is therefore nondecreasing. At arbitrarily large zeros
of q it equals its limiting value. Once it reaches that value it is constant
thereafter. The eventual fixed sign of q+epsilon now makes q zero on an
interval, contradicting real analyticity and nontriviality. This proves (6).

Apply the lemma to q=Q_N on the real line. Although

    sup_(|Im z|<1/2) |(Q_N(z)+epsilon)-Q_N(z)|=|epsilon|,

the perturbed normalized function violates (C) at arbitrarily large real
points. By (1) and its second derivative, it also violates (P) at sufficiently
small positive heights near those points. The perturbation is an exact
constant; it introduces NO derivative error in q' or q''.

This is exactly a possible uniform relative tail error when reconstructing
from F_N: replacing T_N by (1+epsilon)T_N changes the reconstructed numerator
to F+epsilon T_N, whose quotient by the exact T_N is Q_N+epsilon.
A proof using the literal modular identity can exclude that changed source.
A proof using only a nonzero uniform relative-error envelope cannot exclude it.
The statement does not forbid height-dependent enclosures with appropriate
vanishing margins, or another exact global sign argument.

### 3.3 The unnormalized entire perturbation has a strict global failure too

Let

    G_epsilon=F+epsilon T_N, epsilon real and nonzero.

Put a_N=Phi_N'(0)>0. This is the exact positive number computed by the
parent's derivative polynomial and full modular cancellation. Integration by
parts, applied separately to u^j times each half-line kernel, gives

    T_N(x)=2a_N/x^2+O_N(x^-4),
    T_N'(x)=-4a_N/x^3+O_N(x^-5),
    T_N''(x)=12a_N/x^4+O_N(x^-6).

All real derivatives of the complete F decay faster than every inverse
power: integrate the full smooth Schwartz kernel rather than differentiating
an unspecified asymptotic remainder. Therefore

    L_(G_epsilon)(x,0)
          =-8 epsilon^2 a_N^2/x^6+O_(N,epsilon)(x^-8)<0
                                                    eventually. (7)

G_epsilon is nonzero real even entire of order at most one. It has constant
nonzero sign on each sufficiently distant real ray, so only finitely many
real zeros. It has infinitely many total zeros: otherwise Hadamard
factorization gives exp(az+b) times a polynomial; evenness forces a=0, in
conflict with its nonzero x^-2 asymptotic. It thus has infinitely many
nonreal zeros. This last statement does NOT locate them inside the critical
band. For epsilon>-1 its half-line kernel remains positive; its even
extension has a nonzero derivative jump at zero and is not the exact modular
Phi. This is a changed-source result, not an RH counterexample.

Neither (5), (6), nor (7) is a theorem that the exact F or Q_N has a negative
Laguerre value. They invalidate the specific approximate-to-global inference.

## 4. Cross-check of the whole-function determinant completion

PR #834 at f0e34780f4fe91bd5d07e791e8855189838c3df5 gives the following
proposed exact characteristic construction, with a complete operator-domain
argument in its own manuscript. Let w=Phi/F(0), a positive even probability
density, W(x)=integral_-infinity^x w(t)dt, and Qw=1-W. On H_w=L2(R,w dt),

    (Kf)(x)=integral_R [1_(t<x)-Qw(t)] f(t)dt,
    T=-K^2 restricted to odd functions.

It proves K Hilbert--Schmidt and T trace class, with

    det(I-z^2 T)=F(z)/F(0).                              (8)

Every nonzero eigenvalue of T has the form 1/z^2 for a +/- pair of Xi zeros,
with algebraic multiplicities retained. It also constructs a positive
self-adjoint differential operator H satisfying K*K unitarily equivalent
to H^-1. That last statement controls SINGULAR values of K, not the arguments
of its eigenvalues.

A closing read found PR #834 advanced to 62bd9bbed134e20c1ee9cd92d008562079af9ceb.
The comparison and new theta-spectral-crowding README were inspected; that
continuation reports a stronger obstruction to bounded metrics. Its new proof
is not an input here, and the determinant read remains pinned to f0e3478 above.

The hoped-for ending would be:

    OPEN-SPECTRUM: every nonzero eigenvalue of this actual T is positive real.

It is not proved here. In particular (8), positivity of w, evenness of w,
all exponential moments and positivity of H do not by themselves prove it.

Here is a full-line countercheck, not a substitute for the actual w. Let

    Z4=integral_R exp(-t^4)dt,
    w_*(t)=[exp(-(t-1)^4)+3exp(-t^4)+exp(-(t+1)^4)]/(5Z4).

This is strictly positive, even, smooth and has all exponential moments.
For t->+infinity its first shifted term dominates and

    -[log w_*]'(t)=4(t-1)^3+o(1),
    -[log w_*]''(t)=12(t-1)^2+o(1).

Consequently its tail-to-density ratio is O(t^-3), by integrating the
increasing logarithmic slope; reflection deals with the other tail. Thus
integral W_*(t)(1-W_*(t))/w_*(t) dt is finite. Its centered K_* is genuinely
Hilbert--Schmidt, not a formal noncompact replacement.

Its exact characteristic function is

    chi_*(z)=[3+2cos z] integral_R exp(-t^4)exp(izt)dt/(5Z4).

Set r=(3+sqrt(5))/2>1 and alpha=log r. Because r+r^-1=3,

    3+2cos(pi+i alpha)=0.

Thus chi_* has a nonreal zero z_*=pi+i alpha, whether or not the other factor
vanishes there. An explicit ordinary eigenvector calculation suffices:
K_* exp(iz_*t)=exp(iz_*t)/(iz_*), since the weighted mean is zero. Applying
K_* twice and taking odd parts gives

    (-K_*^2) sin(z_*t)=z_*^-2 sin(z_*t).

The nonzero eigenvalue z_*^-2 is nonreal. The vector belongs to H_w* because
quartic decay dominates its exponential growth. All hypotheses relevant to
the generic positivity-to-spectral-reality step hold, but the step is false.
This example is NOT modular, is NOT the theta source, and says nothing about
where actual Xi zeros lie. A theta-specific spectral-reality argument could
still succeed; it is not supplied here.

## 5. Attempted conclusion and exact stopping point

There are two fully stated sufficient endpoints on the unchanged source:

1. Prove (P) or its stronger version (C) for one exact Q_N on the entire strip.
   Section 2 then gives RH directly. No extra gauge-error estimate is needed.
2. Prove OPEN-SPECTRUM for the exact T of PR #834. Its determinant identity
   then puts every Xi zero on the real line.

Neither endpoint is established. The TPR26 source positivity theorem supplies
neither (P) nor (C). Small tail error cannot be promoted to a uniform sign by
itself, as Section 3 proves. The determinant representation and positive
singular-value operator supply neither a positive spectrum nor an allowed
self-adjoint similarity, as Section 4 illustrates.

No full proof is being submitted. The change from the previous pass is the
explicit first-order sufficient ending and a careful test of the two proposed
closing inferences; no RH-strength inequality has been silently accepted.
These tests are not advertised as a new zero-free range or an RH breakthrough.

## 6. Sources and execution boundary

- PR #835, head 4b8fa9abfa9aac5ed1feb7f30acaeeb418ed405c:
  GLOBAL_ATTEMPT.md and tail-positive-real/PROOF.md in
  standalone/2026-09-09-astra-global-xi-attack/.
- PR #834, head f0e34780f4fe91bd5d07e791e8855189838c3df5:
  standalone/2026-09-09-centered-theta-determinant/PROOF.md.
  Sections 1--6 were read. No independent acceptance of its whole packet,
  original differential construction, or numerical code is asserted.
- G. Csordas, "Fourier transforms of positive definite kernels and the Riemann
  xi-function", arXiv:1309.0055v2. The complex/real Laguerre framework is
  classical. The kernel is not identified with a positive-definite kernel
  merely because it is pointwise positive. Relevant text and a rendered page
  were inspected; no new assertion that this paper proves the open sign.
- DLMF 25.10 for classical real-zero existence; the written arguments do not
  require any named zero height, zero simplicity, or a numerical zero table.
- Hadamard factorization and differentiation of holomorphic functions are
  used in their ordinary classical forms. No external novelty claim is made.

The small standard-library checker verifies the normalization algebra, the
power-law Laguerre coefficients, and the exact polynomial identity r^2-3r+1=0.
It does NOT verify the infinite analytic theorems, compute the actual Xi sign,
repeat the parent's 152-cell quadrature, evaluate the new determinant, or
prove any spectral assertion by finite examples.
