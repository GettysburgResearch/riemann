# Resolvent selection for the actual semilocal Weil form

Date: 22 October 2026. **PROPOSED component theorem with a complete author-side proof.**
No new zero-free region, no RH proof, no independent review, and no priority claim.

This is a structural alternative to the conditional decimal consumer in PR #1014.
The real-zero reproducing-kernel mechanism is classical de Branges theory. The
contribution proposed here is its explicit use for the full semilocal Weil form,
with the actual domain, a legal spectral shift, a rank-one construction, and a
bottom-eigenspace selection which does not assume simple-even ground states.
It does not prove the simple-even assertion about the unperturbed Weil operator.

## 1. The unchanged arithmetic source

Let a>0, I_a=[-a,a], and use an inner product antilinear in its first argument.
For f in L2(I_a), extended by zero, put

    F(z) = integral_(I_a) f(x) exp(-izx) dx,
    C_f(t) = integral_R conjugate(f(x)) f(x+t) dx.

The full semilocal Weil form, in additive coordinates, is

    q_a[f] = (1/(2pi)) integral_R w(t)|F(t)|^2 dt
             + 2 Re(F(i/2) conjugate(F(-i/2)))
             - sum_(2<=n<=exp(2a)) Lambda(n)/sqrt(n)
                                     * (C_f(log n)+C_f(-log n)),       (1)

where w(t)=Re digamma(1/4+it/2)-log pi. The sum includes EVERY prime power.
At the endpoint log n=2a the autocorrelation is zero. Equation (1) is
Connes--Consani--Moscovici [CCM], equation (3.19), after x=log u;
[CCM] uses lambda=exp(a). It is not a truncated zero sum, a diagonal-only
model, or an assumed positive form.

Its form domain is

    D_a = { f in L2(I_a): integral log(2+|t|)|F(t)|^2 dt < infinity }.  (2)

Indeed w is bounded below and differs from log(2+|t|) by a bounded function.
The pole evaluations are bounded linear functionals on this fixed interval.
Each prime term is a bounded partial translation. Thus (1) is a bounded
selfadjoint perturbation of the closed logarithmic Fourier form on functions
supported in I_a. It is densely defined, closed, and lower bounded. Let A_a be
its associated selfadjoint operator; equality q_a(f,g)=<f,A_a g> is used only
when g belongs to the operator domain.

For completeness, the form embedding is compact: a bounded form-norm family
has Fourier mass outside [-T,T] bounded by C/log(2+T). The map from L2(I_a)
to its Fourier restriction on [-T,T] is Hilbert--Schmidt. Low-frequency
compactness and this uniform tail imply L2 compactness. Hence A_a has compact
resolvent, a finite lowest eigenvalue lambda_0(a), and a finite-dimensional
lowest eigenspace. These source facts also appear in [CCM], Proposition 3.3
and Theorem 3.6. No quasi-RH input is used.

An explicit, deliberately crude lower bound is

    b_a = -gamma-pi/2-3log2-log pi
          -2(sinh a-a)
          -2 sum_(2<=n<=exp(2a)) Lambda(n)/sqrt(n).                  (3)

To prove it, the digamma series gives Re psi(x+iy)>=psi(x) for x>0.
The reflection and duplication formulas give psi(1/4)=-gamma-pi/2-3log2.
The pole contribution is

    2|<cosh(x/2),f>|^2 - 2|<sinh(x/2),f>|^2,

and ||sinh(x/2)||_2^2=sinh a-a. Finally each paired translation is bounded
below by -2||f||_2^2. Therefore q_a[f]>=b_a||f||_2^2. Choosing kappa=b_a-1
is always legal; no unproved positivity or numerical eigenvalue is needed.

## 2. Domain-safe division at a nonreal zero

For F with a zero z0=c+id, d!=0, define

    G(z)=F(z)/(z-z0),       H(z)=(z-c)G(z),       F=H-idG.             (4)

G and H are entire, have exponential type at most a, and are L2 on the real
axis. They are the transforms of g,h in L2(I_a). This is the L2
Paley--Wiener theorem: division by a canceled factor preserves exponential
type, and the real-axis bounds below preserve square integrability. Moreover

    |G(t)|<=|F(t)|/|d|,       |H(t)|<=|F(t)|,    t real,             (5)

so g,h lie in the actual form domain (2), not just a formal test class.
For any real kappa put q_kappa=q_a-kappa<.,.>. One has

    q_kappa(h,g) is real,
    q_kappa[f]=q_kappa[h]+d^2 q_kappa[g].                            (6)

Here is a check retaining every source term. On the real axis,
conjugate(H(t))G(t)=(t-c)|G(t)|^2 is real. Thus both the archimedean
integral and the L2 pairing are real. The paired autocorrelation at t and -t
is real for the same reason, using inverse Fourier transformation; hence
EACH prime-power pair is real. For the polarized pole term, put
A=conjugate(G(-i/2))G(i/2). Its value on (h,g) is

    (i/2-c) A + (-i/2-c) conjugate(A),

also real. All integrals converge by (2) and Cauchy--Schwarz. Expanding (4)
therefore proves (6). This is the zero-division compatibility that an
arbitrary positive matrix lacks.

## 3. Main theorem: a resolvent column has only real zeros

**Theorem R.** Fix real kappa<lambda_0(a) and real tau. Set

    e_tau(x)=exp(i tau x),
    u=(A_a-kappa)^(-1)e_tau,
    F_(a,kappa,tau)(z) = u_hat(z)/u_hat(tau).                        (7)

Then u_hat(tau)>0, and every zero of F_(a,kappa,tau) is real. This is an
entire function of exponential type at most a. For tau=0 it is real and even
and equals one at zero. No assumption about simplicity or parity of the
unperturbed lowest eigenspace is required.

*Proof.* Coercivity and the form representation theorem give

    q_kappa(u,v)=<e_tau,v>=v_hat(tau),      v in D_a.                (8)

In particular u_hat(tau)=q_kappa[u]>0. If u_hat has a nonreal zero c+id,
apply (4)--(6) and put

    n=q_kappa[g]>0,  r=q_kappa(h,g) real,  s=q_kappa[h],  t=tau-c.

Equation (8), first with v=g and then v=h, gives

    G(tau)=r+idn,      H(tau)=s+idr=t(r+idn).

The imaginary and real parts yield r=tn and s=t^2 n. Consequently

    q_kappa[h-tg]=s-2tr+t^2n=0.

Coercivity forces h=tg, hence (z-tau)G(z) is identically zero. This is
impossible for the nonzero u. Thus no nonreal zero exists. Reflection
and conjugation preserve (1); uniqueness in (8) makes u real and even
when tau=0. QED.

Theorem R is a source-specific version of the real-axis reproducing-kernel
property of de Branges spaces, not a new general positivity principle.
The direct proof is included to authenticate (2), the pole contribution,
all prime powers, and the required spectral inequality on kappa.

## 4. Rank-one implementation and finite computations

Write M=<e_tau,(A_a-kappa)^(-1)e_tau>>0. On D_a define

    B=A_a-kappa-(1/M)|e_tau><e_tau|.                                (9)

Then B>=0 and its kernel is exactly span(u). This follows from
|<e_tau,v>|^2=|q_kappa(u,v)|^2<=M q_kappa[v], with equality exactly when
v is proportional to u. For tau=0, (9) is a SIMPLE EVEN ground state of
a rank-one-perturbed operator. The perturbation subtracts a constant
convolution kernel. It does not establish that A_a itself has a simple
even ground state, and its coefficient 1/M depends on a and kappa.

For tau=0 the same real-zero conclusion holds for exact finite trigonometric
compressions, provided kappa lies strictly below their exact smallest eigenvalue. The
constant-kernel and identity shifts preserve the distributional matrix class
of Connes--van Suijlekom [CvS], equation (11). Theorem 5.6 of [CvS] then
proves real-zero Fourier transforms of these rank-one-selected finite
vectors. This is a consequence of their theorem, not a new finite
real-rootedness theorem. A generic Galerkin subspace need not be closed under
(4); it cannot use the continuum proof by fiat.

For fixed a and a fixed kappa<lambda_0(a), dense form-Galerkin solutions
converge to u in the q_kappa norm, by the orthogonal-projection property of
the variational equation (8). Their normalized Fourier transforms converge
locally uniformly. A kappa chosen just below a NUMERICAL finite minimum is
not thereby known to lie below the INFINITE-DIMENSIONAL minimum. Formula
(3) is one unconditional way to avoid that distinction.

**A sharp warning against generic-matrix reasoning.** In the basis of
frequencies -1,0,1 on [-pi,pi], the reflection-invariant matrix

    T=[[1,-2,0],[-2,9,-2],[0,-2,1]]

is positive definite (its leading principal minors are 1,5,1), and
T^(-1)e_0=(2,1,2). The normalized Fourier transform of that vector is

    sinc(pi z) * (1+3z^2)/(1-z^2),

with removable singularities at +/-1 and nonreal zeros +/-i/sqrt(3).
This matrix is NOT in the required convolution-distribution class.
Positive definiteness and reflection symmetry alone do not prove Theorem R.

## 5. Degenerate bottom spaces: selection, not universal real-rootedness

Let V=ker(A_a-lambda_0), P its L2 projection, d=dim V. Equation (6) with
kappa=lambda_0 shows: if a vector in V has a nonreal Fourier zero, dividing
by that factor as in (4) produces two further vectors in V. Nonnegativity
and equality of the sum are enough; simplicity is unnecessary.

**Theorem B.** Whenever Pe_tau!=0 for real tau, the transform of Pe_tau
has only real zeros. Such tau exist; the bad set is contained in the
discrete real zero set of any one nonzero ground-vector transform.

*Proof.* If Pe_tau has a nonreal zero, its divided vectors g,h are in V.
On V, <Pe_tau,v>=v_hat(tau). Repeat the proof of Theorem R with the
ordinary L2 inner product, whose cross term is real by (5). It forces
h=(tau-c)g, the same contradiction. QED.

This is compatible with [CvS], Remark 2.3: a general vector in a degenerate
kernel may have nonreal zeros; the claim concerns the specifically selected
projection. In fact every nonzero v in V has at most d-1 nonreal zeros,
counting multiplicity. Otherwise successive divisions yield d+1 independent
vectors F/P_j, where P_j are the nested products of the divided factors.
Multiplying a linear relation by P_d gives polynomials of distinct degrees,
which are independent. This would contradict dim V=d.

For Pe_tau!=0, spectral decomposition also gives

    delta (A_a-lambda_0+delta)^(-1)e_tau -> Pe_tau   in L2,

as delta decreases to zero. The normalized version tends locally uniformly
to the normalized bottom projection. This is a FIXED-INTERVAL assertion,
not a cofinal assertion as a tends to infinity.

## 6. What has and has not been removed

[CCM], Section 8, explicitly leaves both the unperturbed simple-even
assertion and the comparison of its ground vector with the actual Xi
source open. Theorems R and B bypass simple-even for CONSTRUCTING particular
real-zero entire functions. They do not prove the authors' original
simple-even statement or their Xi comparison. This packet's own
convergence target is recorded separately in CONVERGENCE.md.

The original Weil form can still have negative spectrum: subtracting a
legal kappa and a rank-one term has not proved its unshifted positivity.
Any proposed limit argument which silently chooses kappa approaching zero
from below while assuming kappa<lambda_0(a) would already assume the
missing global lower bound. That circular shortcut is expressly excluded.

## Primary sources

[CCM] A. Connes, C. Consani, H. Moscovici, *Zeta Spectral Triples*,
arXiv:2511.22755v1, https://arxiv.org/html/2511.22755v1.
Equations (3.19)--(3.20), Propositions 3.3--3.4, Theorem 3.6,
and Sections 7--8. Imported source definition and operator facts;
not a citation to a completed RH proof.

[CvS] A. Connes, W. D. van Suijlekom, *Quadratic Forms, Real Zeros
and Echoes of the Spectral Action*, arXiv:2511.23257v1,
https://arxiv.org/pdf/2511.23257v1. Remark 2.3, Remark 4.3,
Theorem 5.6, Theorem 6.1. The domain discussion here does not assume
that an arbitrary even distribution defines the same closed form.
