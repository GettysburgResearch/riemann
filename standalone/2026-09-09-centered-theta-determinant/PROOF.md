# A fixed trace-class characteristic operator for the whole xi function

Date: 2026-09-09. Continuation of PR #834.
Status: PROPOSED COMPONENT THEOREMS WITH PAPER PROOFS; independent review required.
RH and the required spectral-reality statement are NOT proved.

The previous exact-theta packet gives a positive differential base H and a
non-self-adjoint quadratic pencil. Here the whole characteristic function is
realized instead by ONE compact integration operator, and then by an ordinary
Fredholm determinant of ONE trace-class operator. No zeros define either
operator. The positive base H determines singular values, not eigenvalue angles.
An attempted bounded positive-metric completion is proved impossible for these
operators on their full stated spaces, and after any finite derivative cutoff.
This is not a no-go theorem for other Hilbert--Polya constructions.

General regularized determinants, Volterra/rank-one reductions, parity block
identities and closed-operator inverses are classical. No external novelty or
priority is claimed. All normalizations in the following derivation are explicit.

## 1. The literal source, Hilbert space and two operators

Use exactly the parent's full-line convention

    Xi(z)=xi(1/2+iz)=integral_R phi(t) exp(izt) dt,
    phi(t)=sum_(n>=1) [4pi^2 n^4 exp(9t/2)-6pi n^2 exp(5t/2)]
                                      exp(-pi n^2 exp(2t)).          (1)

The entire completion has xi(0)=xi(1)=1/2. Jacobi inversion makes phi even;
on t>=0 every summand is positive. Thus phi is positive and smooth everywhere.
Let

    Z=integral_R phi(t)dt=Xi(0)>0, w=phi/Z,
    F(t)=integral_-infinity^t w(x)dx, Q(t)=1-F(t),
    H_w=L2(R,w(t)dt), <f,g>=integral conjugate(f)g w.

In particular ||1||=1, mean_w(t)=0. The cumulative F is NOT the xi function.
The source has all exponential moments. Its positive tail, with differentiated
remainders at each fixed order, is

    phi(t)=4pi^2 exp(9t/2-pi exp(2t))(1+O(exp(-2t))).       (2)

This follows by isolating n=1 and bounding the differentiated n>=2 series;
reflection supplies the negative tail. In particular, with V=-log w and C=V'/2,

    V'=2pi exp(2t)-9/2+O(exp(-2t)),
    V''=4pi exp(2t)+O(exp(-2t)),                         t->+infinity. (3)

The scalar normalization of w does not change C or the parent's H.

Define the CENTERED ANTIDERIVATIVE K first on compactly supported functions:

    (Kf)(x)=integral_R [1_(t<x)-Q(t)] f(t)dt.             (4)

Lebesgue dt, not w(t)dt, occurs on the right. In the weighted Hilbert space
its kernel is [1_(t<x)-Q(t)]/w(t). Equivalently it is the antiderivative of f
whose w-mean is zero. The cancellation in (4) must be retained: the two full
half-line integrals are not claimed separately bounded on H_w.

Let H_o be the closed odd subspace of H_w and set

    T=-K^2 restricted to H_o.                            (5)

The theorems below prove that K is Hilbert--Schmidt and T is trace class, and
that for EVERY complex z,

    det_2(I-izK)=Xi(z)/Xi(0),
    det_(H_o)(I-z^2 T)=Xi(z)/Xi(0).                      (6)

Here det_2(I+A)=det((I+A)exp(-A)) in finite rank and is its Hilbert--Schmidt
continuous extension. The second determinant is an ORDINARY trace-class
Fredholm determinant. It has no unspecified exponential prefactor and is
not the square of the desired function.

## 2. Boundedness, the full tail and the derivative inverse

For each fixed t, direct averaging over x gives

    integral_R |1_(t<x)-Q(t)|^2 w(x)dx=F(t)Q(t).

Therefore

    ||K||_HS^2=I_w:=integral_R F(t)Q(t)/w(t)dt.           (7)

This is a complete integral, not a compact-window norm. It is finite for the
actual source. On the positive tail V' is increasing, and (3) gives V'>=c exp(2t).
For u>=t sufficiently large, V(u)-V(t)>=c exp(2t)(u-t); hence
Q(t)/w(t)<=c^(-1)exp(-2t). Reflection bounds F/w at the other end, while
w is bounded below on every fixed compact. This proves (7) without RH.
It also proves an O(exp(-2R)) tail for the INTEGRAL (7); no numerical value
for that O-constant is certified here.

The kernel consequently extends uniquely to a Hilbert--Schmidt map H_w->H_w.
On its initial dense domain,

    (Kf)'=f,            <1,Kf>=0.                       (8)

Both assertions extend to every f in H_w: convergence in H_w implies L2
convergence on compact intervals, so distributional differentiation passes
to the limit; the mean is a bounded functional. In particular K is injective.

Let D be maximal differentiation in H_w:

    Dom D={f in H_w: f is locally absolutely continuous, f' in H_w},
    Df=f'.

It is closed and densely defined. Equations (8) show that it is onto and that
ker D consists exactly of constants. For every f in Dom D,

    KDf=f-<1,f>1.                                      (9)

Indeed the difference has distributional derivative zero, and its mean is
known. Restrict D to the mean-zero space H_0=1^perp; the resulting closed
operator D_0:Dom D intersect H_0 -> H_w is bijective, with bounded inverse K,
viewed here as a map into H_0 rather than the inclusion into all of H_w.
This distinction between its two Hilbert spaces is essential.

## 3. What the parent's positive H actually controls

Put U:H_w->L2(R,dt), Uf=sqrt(w)f. Then

    U D U^(-1)=d/dt+C,
    U D* U^(-1)=-d/dt+C.                                (10)

These are closed operator statements, not just formal expressions. One way
to check the second domain is to start with its maximal distributional domain.
The inequality |C'|<=epsilon C^2+K_epsilon follows from (3). For cutoffs chi_R,
apply the identity

    ||-g'+Cg||^2=||g'||^2+||Cg||^2+integral C'|g|^2

to chi_R g. Absorb C' and keep the cutoff derivative term. Uniform bounds and
local passage to the limit give g' and Cg in L2. Conversely those conditions
imply membership in the maximal domain. Cutoff and smoothing give the same
closed domain as the C_c^infinity closure. This is the parent's form domain.
Consequently

    U D D* U^(-1)=H=-d^2/dt^2+C^2+C'.                   (11)

The operator on the right is the positive self-adjoint form realization,
NOT an unrelated differential extension. Since D_0 is onto,
D_0 D_0*=D D*. Taking inverses between the stated spaces gives

    U K* K U^(-1)=H^(-1).                              (12)

For example this inverse identity can be obtained first from the closed
bijection D_0 and its bounded inverse, using
(D_0 D_0*)^(-1)=(D_0^(-1))*D_0^(-1). No product involving an undeclared
unbounded trial map is being used.

In particular

    Tr H^(-1)=I_w,
    singular_values(K)_j=eigenvalues(H)_j^(-1/2).       (13)

Thus the positive operator already constructed in the parent supplies the
SINGULAR values of K. These do not specify the arguments of K's eigenvalues.
Equation (13) is not a Hilbert--Polya spectral identification.

## 4. Exact determinant: first on a bounded interval, then on the whole line

We use classical properties of det_2: continuity in Hilbert--Schmidt norm,
its eigenvalue product with algebraic multiplicity, and

    det_2((I+A)(I+B))=det_2(I+A)det_2(I+B)exp(-Tr AB)     (14)

for Hilbert--Schmidt A,B. Products AB are trace class. The finite-rank formula
proves (14) directly; approximation proves its extension. Relevant standard
formulas are recorded in Zumbrun, Appendix A, (A.1),(A.3)--(A.6). The printed
lower estimate in that preprint's (A.2), which cannot hold at zeros, is NOT
used. These general determinant facts are imported, not new theorems here.

### 4.1 Volterra plus one rank-one correction

For an arbitrary positive continuous probability density on [a,b], put

    (Jf)(x)=integral_a^x f(t)dt,
    ell(f)=integral_a^b Q(t)f(t)dt,     K=J-1 ell.

All operators in this subsection are on that bounded interval. J is
Hilbert--Schmidt and quasinilpotent. For example its m-th iterate has kernel
(x-t)^(m-1)/(m-1)! on t<x, giving a factorial bound for ||J^m||. Thus
I-uJ is invertible for every complex u and det_2(I-uJ)=1. Set
r_u=(I-uJ)^(-1)1=exp(u(x-a)). Then

    I-uK=(I-uJ)(I+u r_u ell).

The rank-one formula and (14), retaining BOTH exponent corrections, give

    det_2(I-uK)=[1+u ell(r_u)]exp(-u ell(1)).             (15)

Indeed Tr(u r_u ell)=u ell(r_u), while
Tr((-uJ)(u r_u ell))=-u ell(r_u-1). Their combination is -u ell(1).
Integration by parts with Q(a)=1 and Q(b)=0 gives

    1+u ell(r_u)=integral_a^b exp(u(x-a))w(x)dx,
    ell(1)=mean_w(x)-a.

Therefore, on a bounded interval, exactly

    det_2(I-uK)=E_w exp(u(X-E_w X)).                    (16)

This proof never assumes the characteristic function is zero-free; determinant
multiplicativity in (14) does not require the rank-one factor to be invertible.

### 4.2 Passage to the actual infinite theta source

Let P_R be multiplication by 1_[-R,R] in H_w, Z_R=||P_R1||^2, e_R=P_R1, and

    B_R=P_R-(e_R tensor e_R)/Z_R,
    K_R=B_R K P_R.                                     (17)

The tensor is the orthogonal rank-one expression in the inherited metric.
Restricted to P_R H_w, K_R is exactly the centered antiderivative for the
conditional probability w_R=w 1_[-R,R]/Z_R: its mean-subtraction uses Q_R,
not the original Q. It is zero on the complementary input space.

Now P_R->I strongly and B_R->I-(1 tensor 1) strongly, with operator norms at
most one. Since K is Hilbert--Schmidt and its range has mean zero, finite-rank
approximation proves

    ||K_R-K||_HS ->0.                                  (18)

This is an operator-norm-ideal limit, not an interchange of separately divergent
Volterra and rank-one tails. Each conditional source is even. Apply (16) and
use all exponential moments of w to pass its moment-generating function to
the limit, locally uniformly in complex u. Determinant continuity proves

    det_2(I-uK)=M(u):=integral_R exp(ut)w(t)dt.           (19)

Finally M(iz)=Xi(z)/Xi(0), proving the first identity in (6) at EVERY complex z.
For a noneven source the same method includes the centering exponential in
(16); suppressing it without the zero-mean assumption would be incorrect.

## 5. A trace-class operator: remove regularization by parity, not by omission

Spatial parity Rf(t)=f(-t) satisfies RKR=-K, directly from (8) and the zero
mean. With H_w=H_e direct_sum H_o, write

    K = [0 A; B 0],    A:H_o->H_e, B:H_e->H_o.

A and B are Hilbert--Schmidt, and AB,BA are trace class. Finite-dimensional
block determinants, followed by Hilbert--Schmidt approximation of A,B, give

    det_2(I-uK)=det_(H_o)(I-u^2 BA).                    (20)

There is no exponential correction: in every finite block approximation the
trace of K is zero. AB/BA convergence is in trace norm. The equivalent
identity using the even block is consistent, but is not multiplied in again.
Putting T=-BA=-K^2|H_o and u=iz gives the second identity in (6).

In half-line coordinates H_o is L2((0,infinity),2w(t)dt), with odd extension.
A direct real-space formula for this SAME operator is

    (Tf)(x)=2x integral_0^infinity Q(t)f(t)dt
                       -integral_0^x (x-t)f(t)dt, x>0. (21)

It is initially interpreted on compactly supported functions and extended by
T=-K^2. Its sign-changing kernel is NOT a positive Green kernel. In particular
some entries 2xQ(t)-(x-t)_+ are negative for sufficiently large x with t fixed.
This observation alone is not a spectral counterexample to RH.

Define the entire function F_xi(v)=Xi(sqrt(v))/Xi(0) through its even Taylor
series. No square-root branch occurs in that definition. Then

    F_xi(v)=det(I-vT).

The nonzero eigenvalues of T are precisely z^(-2) for pairs +/-z of Xi zeros,
with algebraic multiplicity equal to the order of the corresponding Xi zero.
To see the multiplicity assertion, use the classical Fredholm eigenvalue
product and note that z->z^2 is locally biholomorphic at every nonzero z.
Xi(0)>0 ensures no exceptional z=0 case. We do not assume simple zeros.

Similarly the nonzero eigenvalues of K are 1/(iz)=-i/z, with the full individual
Xi multiplicities. One may check the eigenvectors without determinants:

    K exp(ut)=[exp(ut)-M(u)]/u, u!=0.                  (22)

At a zero u_0, this is an eigenvector with eigenvalue 1/u_0. Conversely
Kf=lambda f, lambda!=0 implies f'=f/lambda, hence f is exponential and its
zero mean gives M(1/lambda)=0. If M has order m at u_0, differentiating
exp(t/lambda) at lambda=1/u_0 through order m-1 supplies an explicit Jordan
chain; the determinant proves that there are no additional algebraic vectors.
For T an eigenvector is sin(zt), in the weighted odd space, at any Xi zero z.

All these statements are unconditional spectral identifications. They yield

    RH <=> every nonzero eigenvalue of T is positive real.              (23)

They do NOT prove the right-hand side. T is not asserted self-adjoint or
similar to a self-adjoint operator. Its positive Fredholm coefficients
E_w[X^(2n)]/(2n)! do not imply positive real eigenvalues.

## 6. The whole moment hierarchy becomes exact operator traces

Let kappa_n be the ordinary cumulants of the probability w, defined near zero by

    log M(u)=sum_(n>=1) kappa_n u^n/n!.

Every moment exists, kappa_1=0, and all odd cumulants vanish. For n>=2 the
power K^n is trace class. Expanding the logarithm of the regularized determinant
near zero, and comparing (19), gives

    Tr K^n=-kappa_n/(n-1)!,                 n>=2,
    Tr T^m=(-1)^(m+1)kappa_(2m)/[2(2m-1)!], m>=1.       (24)

In particular Tr T=E_w[X^2]/2>0. No sign of every higher trace or Hankel
matrix is inferred. Such an assertion would need a new source-specific proof.
The logarithm in this argument is only the locally chosen logarithm at M(0)=1;
no global logarithm across unknown zeros is presumed.

As an independent check of the n=2 normalization, the product kernel gives

    Tr K^2=-2 integral_(s<t) F(s)Q(t) ds dt=-Var_w(X).    (25)

Finite second moment permits Tonelli on the nonnegative last integrand:
for independent X,Y of law w, the double integral equals
E[(Y-X)_+^2]/2=Var(X)/2. The diagonal has measure zero. This is not the
positive Hilbert--Schmidt trace Tr K*K=I_w in (7).

## 7. The attempted positive-metric completion has a proved obstruction

A natural next step would be to find a bounded, boundedly invertible positive
G making iK self-adjoint in the equivalent norm. That would require

    K*G+GK=0,             G=G*>=cI, c>0.                (26)

This is IMPOSSIBLE on H_w. K is injective by (8), but K*1=0. Equation (26)
would imply K*=-GKG^(-1), making K* injective too, a contradiction. This
holds independently of RH. Purely imaginary eigenvalues of a compact
nonnormal operator do not imply bounded similarity to a skew-adjoint one.

Nor is this only the constant direction. For the actual smooth source define

    q_j(t)=w^(j)(t)/w(t), j>=0.

All q_j lie in H_w by (2) and its differentiated versions. They are linearly
independent: at +infinity q_j(t)=(-2pi)^j exp(2jt)(1+O_j(exp(-2t))). For a
compactly supported f, integration by parts in (4), whose output has constant
tails, gives

    K*q_0=0,             K*q_(j+1)=-q_j.                (27)

The products w^(j)Kf vanish at both endpoints. Boundedness and density extend
the identities to all f in H_w.

For each FIXED integer m>=0 let

    W_m={q_0,...,q_(m-1)}^perp,           W_0=H_w.  (28)

At m=1 this is the mean-zero space of Section 2. Equation (27) proves
K W_m subset W_(m+1). The restriction K_m:W_m->W_m is injective but its
adjoint has a nonzero kernel, because W_(m+1) is a proper codimension-one
subspace of W_m.
Thus (26) is impossible on EVERY such finite-codimension restriction too.
No uniform claim about a growing-order estimate is required: each m is exact.

There is a corresponding obstruction for the trace-class T itself. The nonzero
odd vector q_1 belongs to ker T*, since (K*)^2 q_1=0. T is injective. Hence
there is no bounded G=G*>=cI on H_o satisfying T*G=GT. This rules out that
particular bounded-metric self-adjointization, NOT positivity of its possible
real eigenvalues, and not an unrelated Hilbert--Polya operator.

The closed intersection W_infinity=intersection_m W_m contains EVERY
nonzero generalized eigenspace of K. Indeed K is invertible on such a finite
root space and K^m H_w subset W_m. Restriction to W_infinity therefore
retains all nonzero eigenvalues and their multiplicities, hence (19). One
may restrict its odd part for T as well. No metric, spectral reality, Riesz
basis, or completeness of eigenvectors is proved on this infinite restriction.
Removing these adjoint chains is a legitimate reduction; it is not a proof of RH.

## 8. What would complete the attack, and what this pass actually obtains

This pass replaces the quadratic pencil by the fixed explicit trace-class T
with det(I-z^2 T)=Xi(z)/Xi(0), constructs the actual algebraic root spaces,
and identifies H^(-1) with the singular-value operator of K. It also tests and
rules out the most immediate bounded positive-metric completion on the full
spaces and all finite derivative cuts. None of those results assumes RH.

The missing assertion is the source-specific spectral statement in (23), or a
genuine alternative that proves it. The determinant identity does not supply
that sign. In particular a positive singular-value operator, positive even
moments, a convergent Galerkin determinant, or an invertible finite matrix
cannot be substituted for (23). The parent's changed-source examples have
the same general centered-integration construction and nonreal characteristic
values; they are not counterexamples to the actual xi function.

A further unbounded spectral-sign estimate is not supplied here. Review is
requested for the component proofs, not for an RH proof with a missing last
lemma. The current branch's earlier gamma and theta-pencil packets remain
unchanged and retain their original proposed-review qualifications.

## References and precise use

R1. GettysburgResearch/riemann, PR834, exact-theta-pencil/PROOF.md at
2787339f8f1feb619f1679afb96cb9995e440958, Git blob
648a8a867be1ce808a30364d0bb6d4ab7ab3b6f6. The entire theta representation,
its differentiated tails and the H form domain are used and reconstructed above.
The local uploaded copy was authenticated against that exact blob. No parent
numerical certificate or author checker is counted as independently replayed.

R2. NIST DLMF 25.4, https://dlmf.nist.gov/25.4 . Classical xi normalization
and functional equation only. No zero-location assertion is imported.

R3. K. Zumbrun, '2-modified characteristic Fredholm determinants, Hill's method,
and the periodic Evans function of Gardner', arXiv:1011.5695, Appendix A
(A.1),(A.3)--(A.6) and Section 5's Volterra/rank-one method;
https://arxiv.org/abs/1011.5695 . Journal version Z. Anal. Anwend. 31 (2012),
463--472, https://doi.org/10.4171/ZAA/1469 . Only the specified standard
identities, continuity and algebraic zero interpretation are imported. The
whole-line weighted construction and its cutoff limit are proved here.
The browser supplied parsed PDF text; its page-image calls failed. No visual
verification or full audit of this reference is claimed. The invalid lower
side printed in (A.2) is explicitly not an input.
