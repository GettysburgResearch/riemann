# Energy-completed Schur reduction of the full arithmetic window

Status: PROPOSED COMPLETE COMPONENT PROOFS; independent review required.
RH and the original all-degree coefficient inequality are NOT proved.
Scope: the literal full PR #792 operator on each fixed interval (0,L),
complex L2 tests, every omitted prime power, and the complete gamma source.
Publication parent: ddeca90f7aa6facd77841d38207aabe38d7a8f53.
Mathematical inputs: finite-window-coercivity/PROOF.md and the exact
local-window source; immutable Git identities are in SOURCE_LOCK.json.
What was run: exact finite algebra, polynomial/cusp integration, compact
operator countercontrols, and integrity tests. No actual Schur sign was certified.
Smallest remaining gap: nonnegativity of the finite EFFECTIVE matrices S_L,
not their uncorrected restrictions or a leading sample matrix.
Local labels ES-1--ES-5 are confined to this packet. No priority claim.

## 1. Preserve the arithmetic form, but remove the inessential damping

Fix a=3/4, b=3/2, c=1/2. For x>=0 use the exact parent formula

    W(x)=e^(x/2)/2+C_b e^(-bx)+S_Gamma(x)-(P2/b)cosh(bx)
         +(1/b)sum_(2<=n<=e^x) q_n sinh(b(x-log n)),             (1)
    q_n=Lambda(n)/sqrt(n), P2=-zeta'(2)/zeta(2),
    C_b=(1-gamma_E-log(2pi))/3,
    S_Gamma(x)=sum_(j>=1)e^(-(2j+1/2)x)/((2j+1/2)^2-b^2).

Extend W evenly. Equation (1) retains the entire prime tail in P2; it is
NOT the raw prime cutoff. A term at x=log n is zero, with its one-sided
derivative jump retained. Let H=L2(0,L) with inner products antilinear in
the first argument, and define

    K_h(t)=int_0^L W(t-u)h(u)du,
    q(h,k)=b int_0^L conjugate(h(t))K_k(t)dt.                  (2)

If the original test is f=e^(at)h, then q(h,h)=<f,T_L f>.
The multiplication h->e^(at)h is bounded and boundedly invertible on a
fixed finite interval. Thus positivity and negative index of (2) are
exactly those of the original damped operator. Eigenvalues themselves are
NOT claimed to be preserved. The form q is bounded on H and represented
by a compact self-adjoint operator, by the parent's trace-class theorem.

Choose X,m,K exactly as in FW-1/FW-2. In particular X>=max(2,e^L),
S_m=sum_(k=0)^m 4/(4k+1)>=7+2Q_X, C_m=(m+1)(2m+1), and

    pi^2(K+1)^2/L^2 >= 2C_m+7/2.                            (3)

Let E be the span of the following d=K+3 real functions on (0,L):

    chi_-=e^(-ct), chi_+=e^(ct), chi_b=cosh(bt),
    chi_j=sin(j pi t/L), 1<=j<=K,                            (4)

and put V=E^perp in the ordinary H norm. These functions are linearly
independent: write them as exponentials with distinct real or imaginary
exponents and use the Vandermonde derivative test on an interior point.
This also proves E has dimension EXACTLY d. One may work in this basis or
orthonormalize its positive ordinary Gram matrix; inertia is unchanged.

For v in V let

    phi_v(t)=(1/c)int_0^t sinh(c(t-u))v(u)du.                 (5)

The exponential constraints give phi_v=phi_v'=0 at both endpoints, so
phi_v is in H0^2(0,L) and v=phi_v''-c^2 phi_v. Twice integrating against
the sine in (4) gives

    <sin(j pi t/L),v>=-((j pi/L)^2+c^2)<sin(j pi t/L),phi_v>.

Thus V is exactly the parent's positive subspace in the undamped variable.
In particular, with kappa=b/2=3/4,

    q(v,v)>=kappa ||phi_v'||_2^2, v in V,                    (6)

with strict positivity for v!=0. The parent's additional positive tail term
is not needed in the lower estimate (6); it is still part of q everywhere.
For L=1, the parent's choice X=3,m=152,K=101 gives d=104.

## 2. ES-1: the coupling is continuous in the POSITIVE ENERGY norm

Finite codimension alone does not imply this assertion. It is the
source-dependent step that makes the Schur reduction legitimate.

### 2.1 The kernel has one integrable derivative on every finite window

W is in W^(1,1)(-L,L). The growing, cosh and constant-exponential terms
in (1) are locally smooth. There are only finitely many prime-power terms
on [0,L], each continuous and piecewise smooth. The gamma series is positive
and decreasing, with

    S_Gamma(0)=1/6+log(2)/3<2/5,
    int_0^L |S_Gamma'(x)|dx=S_Gamma(0)-S_Gamma(L)<2/5.

The last equality follows first for finite sums and then by monotone
convergence of their nonnegative negative derivatives. It proves absolute
continuity at zero, including the logarithmic divergence of the derivative.
No bounded W'' at zero is asserted. No prime jump is discarded.

Write w0=||W||_(L1(-L,L)), w1=||W'||_(L1(-L,L)). Both are finite and can
be bounded from finite arithmetic. For example, setting Q=Q_X, one may use

    w0 <= 2[(e^(cL)-1)/(2c)+|C_b|(1-e^(-bL))/b+(2/5)L
             +(P2/b^2)sinh(bL)+(Q/b^2)(cosh(bL)-1)],
    w1 <= 2[(e^(cL)-1)/2+|C_b|(1-e^(-bL))+2/5
             +(P2/b)(cosh(bL)-1)+(Q/b)sinh(bL)].             (7)

The prime bound includes even n in (e^L,X] on the harmless upper side.
These are absolute continuity/size bounds, not arithmetic positivity.

For every z in H, convolution on the window satisfies

    K_z in H1(0,L), ||K_z||_2<=w0||z||_2,
    K_z'(t)=int_0^L W'(t-u)z(u)du,
    ||K_z'||_2<=w1||z||_2.                                 (8)

Use the interior derivative on (-L,L), not the distributional derivative
of W times a hard cutoff; artificial endpoint delta terms do not arise in
(8). An absolutely continuous extension and Young's inequality justify
(8), or it follows directly by difference quotients inside the window.

### 2.2 The exact residual formula

Define

    F_z(t)=-K_z'(t)+c^2 int_0^t K_z(s)ds.                    (9)

For every v in V and every z in H, integrations by parts with the clamped
primitive in (5) give the EXACT identity

    q(v,z)=b int_0^L conjugate(phi_v'(t)) F_z(t)dt.           (10)

Indeed int conjugate(phi_v'')K_z=-int conjugate(phi_v')K_z';
the boundary term vanishes since phi_v'=0 at the endpoints. Also
int conjugate(phi_v)K_z=-int conjugate(phi_v')int_0^t K_z,
since phi_v=0 at the endpoints. This proves (10) at H2/H1 regularity.
Only one derivative of W is used, so the genuine prime cusps cause no
missing second-derivative distribution in this calculation.

There is a useful finite projection. Put

    D=(span{1, cos(j pi t/L) (1<=j<=K), sinh(bt)})^perp
            in L2(0,L),                                    (11)

and let Pi be its ordinary orthogonal projection. Then phi_v' belongs to D.
The constant condition is phi_v(L)-phi_v(0)=0. The cosines follow by one
integration by parts and the sine conditions on phi_v. Finally

    int cosh(bt)v(t)dt=(b^2-c^2)int cosh(bt)phi_v(t)dt=0,
    int sinh(bt)phi_v'(t)dt=-b int cosh(bt)phi_v(t)dt=0.

All boundary terms vanish. Thus F_z can be replaced by Pi F_z in (10).
Computing Pi requires only the finite ordinary Gram matrix of the elementary
functions in (11); no arithmetic spectrum or inverse of a compact operator
is involved. Taking Pi=I is also valid, but gives a weaker bound.

Combining (6) and (10) proves

    |q(v,z)| <= sqrt(2b)||Pi F_z||_2 sqrt(q(v,v)).            (12)

In particular every exceptional coupling z=e in E is continuous for the
energy norm sqrt(q(v,v)). This is the exact range condition that a formal
inverse of the positive compact block would otherwise hide.

### 2.3 A stronger constant on the SAME L=1 subspace

For L=1, X=3, K=101, the exact same V admits the improved bound

    q(v,v)>=(6/5)||phi_v'||_2^2.                            (12a)

Here is an elementary source check, not a new sign assumption. The bound
Euler_gamma<3/5 follows from Euler_gamma<H_32-log(32), the first three
positive terms of log(2)=2sum_(j>=0)(1/3)^(2j+1)/(2j+1), and an exact
rational comparison. With pi/2<11/7, log(2)<7/10 and log(pi)<6/5, this gives

    Omega(0)>-[3/5+11/7+21/10+6/5]=-383/70>-11/2.

The literal Q_3=log(2)/sqrt(2)+log(3)/sqrt(3)<9/8 is also reconstructed
by rational log series and rational lower square-root bounds in the checker.
The exact rational sum S_92 is greater than 35/4=1+11/2+2(9/8), so the
same proof as the parent's frequency barrier gives

    V_3(w)>=1-17205/(w^2+1/4), 17205=93*185.

The parent's polynomial division, now with C=17205, and its SAME removed
101 sine modes imply

    q(v,v)>=b[1-(17205+7/4)/93636]||phi_v'||_2^2
            >=(6/5)||phi_v'||_2^2.

We used pi^2*102^2>9*102^2=93636 and the exact rational last inequality.
The nonnegative actual tail is still included. No finite window PSD is
inferred: (12a) is only the stronger positive-sector coercivity. In all
residual formulas below, b^2/kappa=3 can therefore be replaced by 15/8 for
this fixed L=1 construction.

## 3. ES-2: a finite effective matrix with no unbounded inverse

Complete V in the inner product q and denote that Hilbert space by V_q.
This is a completion, not the assertion that V is complete in q. Inequality
(12) extends the anti-linear functional v->q(v,e) continuously to V_q.
By the Hilbert-space representation theorem there is a UNIQUE g_e in V_q
such that

    q(v,g_e)=q(v,e), every v in V.                           (13)

The map e->g_e is linear, and

    ||g_e||_q^2 <= 2b ||Pi F_e||_2^2.                       (14)

It is NOT assumed that g_e belongs to the original L2 subspace V. The
ordinary inverse of the V block is neither introduced nor needed.

Choose any fixed basis e_1,...,e_d of E and define the finite Hermitian matrix

    S_L,ij=q(e_i,e_j)-q(g_(e_i),g_(e_j)).                    (15)

For u in C^d write e_u=sum u_i e_i and g_u=sum u_i g_(e_i).
The exact completion of squares is

    q(v+e_u,v+e_u)=||v+g_u||_q^2+u^*S_L u, v in V.         (16)

Equivalently,

    u^* S_L u=inf_(v in V) q(v+e_u,v+e_u).                 (17)

The infimum is finite, by (12); it need not be attained by an L2 function.
Equation (16) proves the lower bound in (17), and approximation to -g_u in
the definition of V_q proves equality. All couplings to infinitely many
positive directions have been included, not suppressed.

**ES-2 conclusions.**

    T_L>=0  iff S_L>=0,
    n_-(T_L)=n_-(S_L).                                     (18)

Here n_- counts strictly negative directions/eigenvalues, not nullity.
For the first equivalence use (16) and then (17). For the index equality,
any negative subspace of H maps injectively to E because V is positive.
Its image must be S_L-negative by (16), giving n_-(T_L)<=n_-(S_L).
Conversely take the finite negative eigenspace of S_L. Approximate the
finitely many g_(e_i) needed on it by elements of V. Uniformity on its
unit sphere preserves its strictly negative gap in (16), producing an
L2 negative subspace of the same dimension. This proves the reverse bound.
Compactness identifies negative dimensions with negative eigenvalue counts.

A basis change gives a congruent S_L. The matrix is therefore an effective
form on the quotient H/V, not a list of arbitrarily selected sample values.
For L=1, (18) is a genuine 104-dimensional reduction in the parent's stated
coarse parameters. It is NOT the leading 104-by-104 compression. Its entries
contain the variational corrections (15), and their signs are not computed
or established in this packet.

One must not add a nullity equality to (18): an energy minimizer need not
be an L2 vector. Section 6 gives an explicit countercontrol.

## 4. ES-3: finite Galerkin matrices converge from ABOVE

Let V_m be nested finite-dimensional subspaces whose union is dense in V
in L2. This also gives density in V_q because q is bounded in L2 and V is
itself dense in its completion. A concrete predetermined family is obtained
by projecting ordinary polynomials onto V in L2, discarding any dependencies.
The projection uses only the positive ordinary Gram matrix of (4).

For each e_i let v_(i,m) in V_m solve

    q(w,v_(i,m))=q(w,e_i), w in V_m.                        (19)

The finite Gram matrix G_m=q(w_r,w_s) is strictly positive definite. Thus
(19) is an ordinary, well-defined finite system. Let

    C_ij=q(e_i,e_j), B_ri=q(w_r,e_i),
    S_(L,m)=C-B^* G_m^(-1) B.                              (20)

These finite entries are obtained from (1)--(2), not from unspecified zeros.
Orthogonal projection in V_q shows

    S_(L,m)-S_L
      =[q(g_(e_i)-v_(i,m),g_(e_j)-v_(j,m))]_(i,j)>=0,
    S_(L,m+1)<=S_(L,m),  S_(L,m)->S_L in matrix norm.        (21)

Thus a negative quadratic value in S_(L,m) already proves negativity of the
full window, but positivity of S_(L,m) alone gives NO lower bound for S_L.
This is an essential direction-of-inequality distinction.

Every strict negative direction of S_L eventually appears in these finite
systems. For positive semidefinite S_L, (21) alone supplies no finite-time
positive certificate, especially on a singular boundary.

## 5. ES-4: an explicit residual error that can certify a LOWER bound

The following works for ANY exact trial vectors v_i in V, not just the
Galerkin minimizers. Put z_i=e_i-v_i and define

    U_ij=q(z_i,z_j),
    R_ij=int_0^L conjugate(Pi F_(z_i)(t)) Pi F_(z_j)(t)dt.   (22)

Then the exact source-specific enclosure is

    U-2b R <= S_L <= U,      2b=3.                         (23)

At L=1 with (12a), the stronger certified enclosure is

    U-(15/8)R <= S_1 <= U.                                 (23a)

Proof. Equation (13) gives

    U-S_L=[q(g_(e_i)-v_i,g_(e_j)-v_j)]>=0.

For every vector u and every w in V,
q(w,sum u_i z_i)=q(w,sum u_i(g_(e_i)-v_i)).
By (12), the norm squared of that representing vector is at most
2b||Pi F_(sum u_i z_i)||_2^2=2b u^*R u. This proves the other
Loewner inequality in (23) for all complex u at once.
No independent-entry estimate or triangle inequality replaces this Gram.

In particular the finite, verified condition

    U-3R>=0                                                (24)

would certify the complete L2 window, with all prime tails and all positive
sector couplings retained. It does not assume a bound on the inverse of a
compact L2 block. It is a sufficient test, not a theorem that (24) holds.

If certified approximate matrices U_tilde,R_tilde satisfy operator-norm
errors at most eta_U,eta_R, a safe acceptance test is

    U_tilde-3R_tilde-(eta_U+3eta_R)I>=0.                     (25)

For uniform per-entry errors eps_U,eps_R, one may use eta_U=d eps_U and
eta_R=d eps_R. This does not account for numerical errors that have not
actually been enclosed. The present finite checker does NOT implement a
validated actual-W quadrature or produce a matrix satisfying (25).

### Analytic assembly and endpoints for a future interval evaluation

For fixed L, W and W' in (9) use finitely many prime knots log n<=L, the
single safe constant P2, and the explicit gamma series. Knot intervals can
be separated exactly. Near zero, S_Gamma'(x)=O(1+|log x|); integration
bounds such as int_0^epsilon |log x|dx=epsilon(1-log epsilon) pay that end.
The functions F_z are in L2 by (8) and the bounded Volterra integral, and
Pi is a finite elementary projection. Thus (22) is a legitimate ordinary
integral; it is not an omitted distribution or a meromorphic boundary norm.

A crude computable bound follows already from (7)--(9):

    ||Pi F_z||_2 <= (w1+c^2 L w0)||z||_2.                   (26)

Replacing R by this crude bound is valid but can destroy the desired sign.
Neither (26), convergence in (21), nor the positivity of a finite leading
matrix proves (24) or its improved L=1 version. In particular no rate of convergence of the residual
bound R is claimed merely from energy convergence of the Galerkin vectors.

## 6. ES-5: exact compact controls for the domain and sign boundaries

These are synthetic operator models, not xi or altered prime measures.
Let V=l2(N), A=diag(4^-j) for j>=1 and b_j=4^-j. Define on V direct-sum C

    Q(v,u)=sum_j 4^-j |v_j|^2
              +2Re(conjugate(u)sum_j 4^-j v_j)+C|u|^2.     (27)

The representing vector g=(1,1,...) has finite energy norm squared 1/3,
but is NOT in l2. A^-1 b does not exist as an l2 vector. Nevertheless

    S=C-1/3,
    S_M=C-(1-4^-M)/3,
    S_M-S=4^-M/3.                                         (28)

For C=1/2 the form is positive and S=1/6. For C=1/3, S=0 but the form
is strictly positive on every nonzero (v,u) in l2 direct-sum C: equality
would require v_j=-u for every j, which belongs to l2 only for u=0.
This disproves an unrestricted nullity equality for (18). For C=1/4,
S=-1/12 although S_1=0; S_2=-1/16 supplies a finite negative vector.
The positive or nonnegative initial section is not a lower sign certificate.

The energy-continuity condition itself is substantive. Replace b_j by 2^-j,
which is still in l2. Now the finite minimizers with u=1 have v_j=-2^j
for j<=M, zero otherwise, and Q(v,1)=C-M. The infimum is minus infinity.
There is still a positive codimension-one subspace, but no finite Schur
entry. This is why the actual-source proof of (12) cannot be replaced by
finite codimension, boundedness, or formal use of a pseudoinverse.

## 7. Actual completion attempt and remaining sign

The previous gap was TWO separate tasks: justify eliminating the infinite
positive sector, then prove the sign of the resulting effective form.
ES-1--ES-4 complete the first task at each finite L, including the exact
range condition, all complex cross terms, negative index, and a one-sided
computable residual budget. They do NOT complete the second task.

The attempted direct bound is (23), with trials from (19), or v_i=0 as a
starting comparison. Source regularity bounds R finitely, but does not by
itself show it is smaller than U in Loewner order. No certified actual
residual matrix or positive lower matrix has been obtained.

The separate sampled-source reconnaissance is retained in RECONNAISSANCE.json.
At L=1 its constant-three lower approximations remain negative. After the
proved improvement to 15/8 in (12a), its largest-grid trials of rank 384,
704 and 880 give positive sampled lower matrices, with smallest eigenvalues
about 4.3e-10 to 4.6e-10. This is a direction for a validated finite-window
experiment, NOT a theorem: sampled constraints are not exact continuum
constraints, and no analytic discretization/rounding enclosure was supplied.
Neither their positive signs nor their apparent stability certify (23a).
Even a future rigorous L=1 certificate would be only one finite window,
not the required unbounded family. Conversely the earlier negative lower
estimates never implied that S_L itself was negative.

The route would close if S_L>=0 for every L in any unbounded predetermined
sequence. Indeed positivity for all such windows gives positivity on every
compactly supported test, hence T>=0 by boundedness, and the earlier exact
A*TA=T, d_n=(9/8)Tr(TA^n) identity proves the original coefficient bound.
This all-L sign remains RH-strength and OPEN. A fixed 104-dimensional
reduction at L=1 does not reduce the whole RH problem to 104 numbers.

Generalized Schur complements/shorted forms, Riesz representation, Galerkin
projection and inertia arguments are classical. The proposed contribution
is the actual-kernel W^(1,1) range proof, the explicit residual (9)--(12),
the fixed arithmetic quotient (15), and the constant-three lower enclosure
(23). No new general RH criterion or external priority is claimed.
