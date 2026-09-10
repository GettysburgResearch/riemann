# Logarithmic cores and convergent residual certificates for the arithmetic Weil window

Status: PROPOSED COMPLETE COMPONENT PROOFS; independent review required.
RH IS NOT PROVED. No new actual-window sign is certified here.
Date: 2026-09-06. Local labels LC1--LC6 are not canonical claim identifiers.
Base: main@051808c1f8367b4320c52f94b40908eb2173d622.
Source: PR #792@465cb28ed8cbfa1bb071d9a85eeda9890decfe6b, especially
finite-window-coercivity/PROOF.md and energy-schur-reduction/PROOF.md.

The new step is NOT the existing Schur enclosure. It is an operator-core
and dense-range theorem for its **strong residual**, followed by a fixed,
regularized least-squares construction whose entire residual Gram tends to
zero. An essential ingredient is the Carleman bound for leakage of the
logarithmic Fourier multiplier across the interval endpoints.

The functional-analytic theorems below are general. Their application keeps
this exact arithmetic source. General logarithmic operators, Carleman's
inequality, Friedrichs extensions and least squares are classical tools;
no external priority claim is made.

## 1. Exact source, conventions and the inherited positive sector

Fix I=(0,L), L>0, a=3/4, b=3/2 and c=1/2. Inner products are antilinear
in the first argument. Fourier transform is fhat(w)=integral f(t)e^(-iwt)dt;
Plancherel therefore has factor 1/(2pi). Zero extension is denoted Z.
For x>=0 set

    W(x)= e^(x/2)/2 + C_b e^(-bx)
          + sum_(j>=1) e^(-(2j+1/2)x)/((2j+1/2)^2-b^2)
          - (P2/b)cosh(bx)
          + (1/b)sum_(2<=n<=e^x) Lambda(n)/sqrt(n)
                                  sinh(b(x-log n)),                  (1)
    C_b=(1-gamma_E-log(2pi))/3,  P2=-zeta'(2)/zeta(2).

Extend W evenly and define

    q(h,k)=b integral_I conjugate(h(t)) integral_I W(t-u)k(u)du dt.

This is the undamped form: if f=e^(at)h then q(h,h)=<f,T_L f> for the
parent's kernel T(t,u)=b e^(-a(t+u))W(t-u). Damping is a bounded invertible
map on each fixed interval; eigenvalues need not be preserved.

Choose an integer X>=max(2,e^L), put Q_X=sum_(n<=X) Lambda(n)/sqrt(n),
and tau_X=P2-sum_(n<=X) Lambda(n)/n^2. The number tau_X is nonnegative and
contains **all** omitted prime powers. Put

    Omega(w)=Re psi(1/4+iw/2)-log pi,
    V_X(w)=Omega(w)-2 sum_(n<=X) Lambda(n)/sqrt(n) cos(w log n).

Choose m,K with

    S_m=sum_(j=0)^m 4/(4j+1)>=7+2Q_X,
    C_m=(m+1)(2m+1),
    ((K+1)pi/L)^2>=2C_m+7/2.                               (2)

Such finite integers exist. Let E be spanned by e^(-ct), e^(ct), cosh(bt),
and sin(jpi t/L), 1<=j<=K, and V=E^perp in L2(I). The dimension of E is K+3:
independence follows by expressing these functions as exponentials with
distinct exponents. Let d_0=1, d_j=cos(jpi t/L), 1<=j<=K, and
d_(K+1)=sinh(bt). Define D=span{d_0,...,d_(K+1)}^perp and its projection Pi.

For v in V the clamped primitive

    phi_v(t)=c^(-1) integral_0^t sinh(c(t-u))v(u)du

satisfies phi_v=phi_v'=0 at both endpoints and v=phi_v''-c^2 phi_v.
Write y=phi_v'. Conversely, every y in H0^1(I) intersect D gives

    J y(t)=integral_0^t y(s)ds,  B y=y'-c^2 J y in V,        (3)

and is exactly the primitive derivative of B y. Here B is a differential
map, not the bounded perturbation B_L introduced below. To check all the
constraints, integrate against e^(+/-ct), sin(jpi t/L), and cosh(bt),
retaining y(0)=y(L)=J y(0)=J y(L)=0. In particular

    integral sinh(bt) B y(t)dt = -(b^2-c^2)/b
                                      integral cosh(bt)y(t)dt.       (4)

The exact cutoff identity and rank-two tail from the parent yield

    q(B y,B z)= b/(2pi) integral_R V_X(w) R(w)
                                      conjugate(yhat(w)) zhat(w)dw
                +(16/9)tau_X <y,cosh(bt)><cosh(bt),z>,       (5)
    R(w)=(w^2+1/4)^2/[w^2(w^2+9/4)].

The apparent w=0 singularity is harmless: integral y=0 and
J y has compactly supported zero extension. In particular
(2pi)^(-1) integral conjugate(yhat)zhat/w^2=<J y,J z>.

For clarity, the inherited positivity can be reconstructed without a prime
sign assumption. Digamma partial fractions give

    Omega(w)-Omega(0)=sum_(j>=0) [2/(2j+1/2)]
                                      w^2/[(2j+1/2)^2+w^2].

Using Omega(0)>-6, (2), and cos<=1 gives
V_X(w)>=1-C_m/(w^2+1/4). Polynomial division in the phi variable gives

    [(x+1/4)^2-C_m(x+1/4)]/(x+9/4)
       =x-(C_m+7/4)+(4+2C_m)/(x+9/4).

Removal of the first K Dirichlet sine modes of phi and (2) imply

    q(v,v)>=kappa ||phi_v'||_2^2,  kappa=3/4, v in V.       (6)

The exact tail is nonnegative on V because its cosh moment is zero.
For L=1,X=3,m=152,K=101 the source also proves kappa=6/5 for the SAME
space. That refinement, its exact scalar checks, and its limited scope are
retained; it is not positivity of the complete length-one window.

Finally W belongs to W^(1,1)(-L,L). For the gamma tail this follows from
monotone convergence of the integrals of its nonnegative negative
derivatives. The finitely many prime knots have continuous W and integrable
one-sided derivatives. Thus for z in L2(I), writing K_z=W*Zz on I,

    F_z=-K_z'+c^2 J K_z,       f_z=Pi F_z,
    q(v,z)=b <phi_v',f_z>,     f_z in D.                    (7)

Equation (7) needs only ONE kernel derivative. Hard-cutoff endpoint delta
terms are not substituted for the interior convolution derivative.

## 2. LC1: the positive sector is a logarithmic operator plus a bounded term

Put ell(w)=(1/2)log(1+w^2) and define the global self-adjoint multiplier
mathcal L=ell(D). The exact division

    R(w)=1+1/(36w^2)-16/[9(w^2+9/4)]                       (8)

is the useful change of viewpoint. V_X-ell is bounded: use the digamma
asymptotic on the vertical line and the FINITE prime sum. Also

    B0(w)=[V_X(w)-V_X(0)]/w^2,
    B1(w)=V_X(w)/(w^2+9/4)

are bounded real even functions, with B0 defined by continuity at zero.
Near zero V_X is smooth and even; at infinity it is O(log(2+|w|)).
Consequently (5) becomes

    a(y,z):=q(B y,B z)
       = b/(2pi) integral ell(w) conjugate(yhat(w))zhat(w)dw
           +<y,B_L z>,                                   (9)

where B_L is the bounded self-adjoint operator ON D represented by

    b Z* (V_X-ell)(D) Z
      +(b/36) Z* B0(D) Z
      -(16b/9) Z* B1(D) Z
      +(b V_X(0)/36) J*J
      +(16tau_X/9)|cosh(bt)><cosh(bt)|,                    (10)

compressed on both sides to D. Signs in (10) are not discarded.
All its constants may depend on L and X; there is no uniform bound in L.

Let

    Q={y in D : integral (1+ell(w))|yhat(w)|^2 dw<infinity}.

The form (9) is closed and semibounded on Q. Smooth interior functions
satisfying the D constraints are form-dense: the shrink/mollify/correct
construction in Section 3 proves this for both weights 1+ell and 1+ell^2.
It follows from (6) that a>=kappa on Q. In particular its form norm is
equivalent to the 1+ell Fourier norm. Let A_L be its associated Friedrichs
operator on D. Then

    A_L=A_L*, A_L>=kappa I, ||A_L^(-1)||<=1/kappa.           (11)

This bounded inverse is for the **unbounded logarithmic operator on
primitive derivatives**, not for the original positive compact L2 block.
That distinction is indispensable.

## 3. LC2: Carleman leakage identifies the entire operator domain and core

We prove the following statement with any b>0, finite linearly independent
smooth real constraints d_j on [0,L], and any bounded self-adjoint B_L on D.
Assume the closed form (9) is bounded below. Then

    Dom(A_L)={y in D : ell(w)yhat(w) belongs to L2(R)},      (12)
    A_L y=b Pi Z* mathcal L Z y+B_L y.

Moreover C_c^infinity(I) intersect D is an OPERATOR CORE, not just a form
core. Thus approximation can preserve both y and A_L y in L2.

### 3.1 The explicit endpoint leakage bound

The elementary integral identity

    ell(w)=integral_0^infinity (1-cos(wr))e^(-r)dr/r

follows by differentiating in w and fixing the value at zero. Hence, for
smooth g,

    mathcal L g(x)=integral_0^infinity e^(-r)/r
                      [g(x)-(g(x+r)+g(x-r))/2]dr.          (13)

If g=Zy and x=-s<0, its off-support value is

    -(1/2) integral_0^L e^(-(s+t))y(t)/(s+t)dt.             (14)

There is the reflected expression for x>L. The Carleman operator
Cf(s)=integral_0^infinity f(t)/(s+t)dt has norm at most pi on L2(0,infinity).
Indeed Schur's test with weight t^(-1/2) uses the exact identity

    integral_0^infinity t^(-1/2)/(s+t)dt=pi s^(-1/2),

obtained by t=s u^2. Dropping the positive exponential factor in (14)
and applying this bound to |y| gives

    ||1_(R\I) mathcal L Z y||_2 <= pi/sqrt(2) ||y||_2.     (15)

This is a bound on both exterior half-lines, not on the full multiplier.
The multiplier itself is unbounded. Formula (14) holds distributionally
and then in L2 for all y in L2(I), by approximation and the bound.

### 3.2 Domain identification, including boundary distributions

Let y belong to Dom(A_L), so a(z,y)=<z,A_L y> for all z in Q.
Testing on C_c^infinity(I) intersect D shows that the interior distribution
b mathcal L Z y-(A_L y-B_L y) annihilates every test orthogonal to the d_j.
The annihilator is precisely their finite span. To see this without a
quotient assumption, choose smooth interior tests eta_j with
<d_i,eta_j>=delta_ij and subtract their moment correction from an arbitrary
test. Thus the interior distribution mathcal L Z y is an L2 function.
By (15) its exterior distribution is L2 too.

There cannot be a missing delta distribution at 0 or L. For every y in L2,
mathcal L Z y belongs to H^(-1/4)(R), since
ell(w)/(1+w^2)^(1/8) is bounded. After subtracting the interior/exterior
L2 functions, any remaining distribution has support {0,L}. A nonzero
finite linear combination of derivatives of point masses is not in
H^(-1/4): its Fourier transform is an exponential polynomial with
nonnegative polynomial degree, whose squared weighted integral diverges.
Therefore this remainder is zero. This proves ell yhat in L2 globally.

Conversely, global L2 membership permits the Plancherel pairing in (9)
against every Q test and gives the stated A_L expression. This proves (12).
The proof does not infer endpoint values of y from logarithmic regularity.

### 3.3 An explicit graph-core approximation

The global norm is

    ||g||_log^2=(2pi)^(-1) integral (1+ell(w)^2)|ghat(w)|^2dw.

For y in (12), first contract Zy affinely toward L/2 by a factor theta<1,
with the usual theta^(-1/2) normalization. Its support is strictly inside I.
These contractions converge in this norm as theta increases to one.
One proof uses strong continuity on Schwartz functions, their density in
the global weighted Fourier space, and the uniform weight comparison
1+ell(w/theta)^2 <= C(1+ell(w)^2), theta in [1/2,1].

Mollify with a compactly supported smooth approximate identity narrower
than the support margin. Fourier dominated convergence gives convergence
in the same norm. This produces smooth interior y_n, initially without
the D constraints. Choose eta_j as above and replace y_n by

    y_n - sum_j eta_j <d_j,y_n>.

Because y lies in D, all correction coefficients tend to zero. Each eta_j
has finite global logarithmic norm. The corrected sequence therefore
converges in the logarithmic norm, lies in C_c^infinity(I) intersect D,
and, by (12) and boundedness of B_L, converges in the graph norm of A_L.
This proves the operator-core assertion, including finite constraints.

The form embedding Q into L2(I) is compact: bounded form norm controls
Fourier tails uniformly because ell tends to infinity, and bounded support
controls translation tightness. The L2 compactness criterion then applies.
Thus A_L has compact resolvent; if (11) holds, A_L^(-1) is compact as well.
Compact resolvent is an additional structural statement, not an RH sign.

## 4. LC3: a fixed family and a convergent strong-residual construction

For the actual space D, no adaptive zero-dependent choice is necessary.
Let omega(t)=t(L-t) and form the positive matrix

    M_ij=integral_I omega(t)d_i(t)d_j(t)dt.

It is strictly positive since the d_i are linearly independent and
omega>0 in I. Put eta_j=omega sum_k d_k(M^(-1))_kj and

    p_n(t)=omega(t)(t/L)^n,
    y_n=p_n-sum_j eta_j<d_j,p_n>,
    v_n=B y_n,                       n=0,1,2,... .          (16)

These eta_j vanish at the endpoints; they need not be compactly supported.
They and y_n have zero extensions in H1(R), hence in the domain (12).
They are exact continuum-constrained tests, not sampled constraints.

The span of y_n is graph-dense in Dom(A_L). Indeed each smooth interior
D test can first be approximated in H1 by omega times polynomials: divide
by omega, extend smoothly to the endpoints, approximate the derivative
uniformly by polynomials and integrate. The bounded finite moment
correction preserves this convergence. H1 convergence of zero extensions
implies logarithmic graph convergence. Combine this with Section 3.
Linear dependencies among the y_n do not affect this density statement.

For each elementary exceptional vector e_i in E put f_i=Pi F_(e_i).
Equation (7), the representation theorem, and (11) identify its positive
energy representative with

    y_i^*=b A_L^(-1) f_i.                                  (17)

The representing original vector need not be in L2. For every core y,
(7) and (12) give the STRONG identity

    Pi F_(B y)=A_L y/b.                                    (18)

Both sides are in D; equality against the dense primitive test space proves
the equality in L2, not just a form equality. By (12), (16), and the
surjectivity of A_L, the span of r_n=Pi F_(v_n) is dense in D.

Here is a rank-safe finite construction. For m>=1 let Z_m: C^m -> D
map the n-th coordinate to r_n, 0<=n<m. Use delta_m=1/m and define

    alpha_(i,m)=(Z_m* Z_m+delta_m I)^(-1)Z_m* f_i,
    v_(i,m)=sum_(n<m) alpha_(i,m),n v_n,
    r_(i,m)=f_i-Z_m alpha_(i,m).                            (19)

The matrix inverse is always legitimate, even with dependent columns:
its smallest eigenvalue is at least delta_m. All columns and targets are
source-defined; no off-line zero is supplied.

For every i, ||r_(i,m)||_2 ->0. Given epsilon>0, density supplies a fixed
finite coefficient vector alpha with residual norm below epsilon. Pad it
by zeros. The minimum of
||f_i-Z_m alpha||^2+delta_m||alpha||^2 is at most
 epsilon^2+delta_m||alpha||^2. Its minimizing residual therefore has
limsup at most epsilon^2. Let epsilon decrease to zero. For the entire
fixed d=dim E block this proves

    R_m=[<r_(i,m),r_(j,m)>] ->0 in matrix norm.              (20)

There is no assertion of a rate uniform in L, or a claimed sharp rate in m.
The construction differs from merely invoking energy convergence of the
old Galerkin approximants. That weaker argument was insufficient.

## 5. LC4: two-sided effective matrices with a vanishing certified width

For z_(i,m)=e_i-v_(i,m), define U_m=[q(z_(i,m),z_(j,m))].
Let S_L be the parent's exact energy-completed Schur matrix. With
C_kappa=b^2/kappa, equations (7) and (11) give

    U_m-C_kappa R_m <= S_L <= U_m,
    ||U_m-S_L|| <= C_kappa ||R_m|| ->0.                    (21)

Here C_kappa=3 in general and 15/8 for the specified length-one space.
Proof: U_m-S_L is the energy Gram of the representing errors. For a
coefficient vector u, this energy error equals

    b^2 <r_(u,m), A_L^(-1) r_(u,m)>
       <= (b^2/kappa)||r_(u,m)||^2.

This is a simultaneous Loewner bound for all complex u. In particular the
lower matrices ALSO converge to S_L. Neither sequence is asserted monotone
for the ridge choice (19); exact energy-Galerkin upper matrices do have the
parent's monotonicity, but that is a different construction.

Consequences at fixed L:

* If S_L is positive definite, some finite exact lower matrix in (21) is
  positive definite. With sufficiently accurate rigorous entry enclosures,
  a finite positive certificate will be found.
* If S_L has a negative eigenvalue, some finite upper matrix has a strictly
  negative quadratic value, again robust to certified entry errors.
* If S_L is positive semidefinite and singular, a strictly positive lower
  certificate need not exist. For every eta>0, however, eventually the
  lower matrix is greater than -eta I. No zero-margin decision is promised.

This closes the strong-residual convergence omission of ES-4. It does not
assert that the actual S_L is positive, or that the old unvalidated sampled
matrices are continuum certificates.

## 6. LC5: primitive truncation budgets and the finite-certificate contract

For effective certification in this section, L is a supplied positive rational
(or a computable real with specified effective input); the RH exhaustion below
uses integers. The analytic core theorems allow arbitrary real L>0.
The construction need not use an oracle with unspecified special-function
tails. Write alpha_j=2j+1/2 and retain j<=J, J>=1, in the gamma source.
Since alpha_j^2-b^2=4j^2+2j-2>=4j^2,

    ||S_tail||_(L1(-L,L)) <= L/(2J),
    ||S_tail'||_(L1(-L,L)) <= 1/(2J).                       (22)

For the second inequality, integrate each negative exponential derivative
first; no pointwise derivative bound at zero is used. If only this gamma
tail is omitted, for every z in L2(I),

    ||Pi(F_z-F_z^J)||_2
       <= (1+L^2/4)/(2J) ||z||_2,                         (23)
    |q(z,w)-q_J(z,w)| <= b L/(2J)||z||_2||w||_2.

The safe arithmetic constant P2 has the elementary approximation

    sum_(2<=n<=N) Lambda(n)/n^2 <= P2
       <= sum_(2<=n<=N) Lambda(n)/n^2+(log N+1)/N, N>=2.    (24)

Use Lambda(n)<=log n and decreasing integral comparison. An error epsilon
in P2 changes the two kernel norms by at most

    2 epsilon sinh(bL)/b^2,
    2 epsilon (cosh(bL)-1)/b,                              (25)

respectively. An error epsilon in C_b has bounds
2epsilon(1-e^(-bL))/b and 2epsilon(1-e^(-bL)).
Thus every omitted primitive is bounded with constants depending explicitly
on the fixed L. No numerical zeta-zero information is used.

Euler's constant can be enclosed by H_N-log N-1/N < gamma_E < H_N-log N.
The other constants use convergent rational series or standard elementary
interval algorithms for exp, log, sin, cos and pi. Thus computability of
C_b is not an unmentioned primitive assumption.

For fixed J,N and the finite tests (16), convolutions are finite integrals
of elementary smooth functions split at 0 and the finitely many prime-log
knots. Validated integration or their elementary antiderivatives suffice.
The finite constraint matrix M is positive definite; its inverse can be
enclosed to arbitrary precision by refinement. In (19), the independent
lower spectral bound delta_m prevents an undecidable rank test. Trial
coefficients may instead be replaced by close rational complex values,
while retaining the EXACT definition v=sum alpha_n B y_n. Approximating
the constraints themselves and declaring them exact is not permitted.

If matrix enclosures give ||U_tilde-U_m||<=eta_U and
||R_tilde-R_m||<=eta_R, an accepted LOWER matrix is

    U_tilde-C_kappa R_tilde-(eta_U+C_kappa eta_R)I.          (26)

For residual columns, individual L2 errors epsilon_i yield column-operator
error E=(sum epsilon_i^2)^(1/2). A bound M for the approximate column
operator norm gives Gram error at most 2ME+E^2. Per-entry errors may instead
be summed by the Frobenius norm. These budgets also include errors in trial
coefficients and the finite projections. Formula (26) is not a license to
use unvalidated quadrature.

Strict positivity/negativity is decidable from converging rational interval
enclosures when a nonzero margin is known to exist. A dovetailed search over
m,J,N and working precision therefore finds each strict certificate promised
in Section 5. This is an existence and correctness proof of such a primitive
algorithm. The delivered checker implements bounded exact controls and an
exact diagonal prototype, NOT an actual-W interval matrix engine. No cost
bound, large computation, or successful actual positive certificate is claimed.

## 7. LC6: an explicit end-to-end RH endpoint, and the unproved assertion

The all-window sign is still the missing arithmetic theorem. To display its
full endpoint without hiding a spectral adapter, let

    H(r)=xi'(1/2+r)/xi(1/2+r).

Direct integration of (1), first where Re r>1/2, gives

    integral_0^infinity e^(-rx)W(x)dx
        =[H(r)-(r/b)H(b)]/(b^2-r^2).                       (27)

The singularity at r=b is removable. Here are normalization checks. In the
original symmetric prime kernel, the two exponential integrals for log n=l
sum to 2[b e^(-rl)-r e^(-bl)]/(b^2-r^2). After multiplication by
-Lambda(n)/(2b sqrt(n)) this is exactly the zeta-log-derivative part of
(27). The gamma computation uses

    sum_(j>=1) 1/(alpha_j^2-b^2)=1/6+log(2)/3,
    sum_(j>=1) [alpha_j/(alpha_j^2-b^2)-1/(2j)]
                                                =log(2)/2-1/4.

Together with digamma partial fractions these give precisely C_b in (1).
All sums can be integrated absolutely in Re r>1/2, using Lambda(n)<=log n.
In particular W(x)=O((1+x)e^(x/2)); it is continuous and of exponential order.

If S_L>=0 for all L in an unbounded predetermined sequence, completion of
squares gives q>=0 on every compact interval. Approximate point masses by
L2 bumps, use continuity of W, and translate finite point sets into one
positive interval. Thus W is a positive-definite function on R. Its two-point
matrices give |W(x)|<=W(0), so its Laplace transform is holomorphic in Re r>0.
Equation (27) continues H holomorphically there. Any zero of xi in Re s>1/2
would give a nonremovable logarithmic-derivative pole, a contradiction.
Functional-equation reflection proves RH.

Conversely, under RH the genus-zero xi product gives the uniformly
convergent positive-weight representation

    W(x)=sum_(all signed ordinates gamma) m_gamma
                       e^(i gamma x)/(b^2+gamma^2).

It follows either from (27) and Laplace uniqueness or by the explicit
formula. The weights have finite total mass by the classical O(T log T)
zero count. Hence W is positive definite and every S_L is nonnegative.
These are classical analytic inputs, not a new verification of zeros.

### 7.1 Strictness of the effective matrix under RH

There is a stronger fixed-window conclusion that does NOT follow merely
from strict positivity on ordinary L2 tests:

    RH implies S_L is POSITIVE DEFINITE for every finite L>0.       (28s)

The missing ingredient is uniqueness for compactly supported distributions,
not an assumption that the energy minimizer belongs to L2.
We use the following classical conditional zero-count consequence, with its
import explicit: under RH, Littlewood's bound is
S_arg(T)=O(log T/log log T). The Riemann--von Mangoldt formula has a smooth
main term and jumps equal to the zero multiplicities. Taking left and right
limits therefore bounds every multiplicity in [T/2,T] by
O(log T/log log T). That interval contains asymptotically a positive constant
times T log T zeros with multiplicity, so the number of DISTINCT ordinates
in it is at least a positive constant times T log log T. Only its
superlinear growth is used. No simplicity, spacing, or finite zero table is
assumed. Source: Hall, J. London Math. Soc. 59 (1999), 65--75, opening
paragraphs, reporting Littlewood; see SOURCES.md. The classical bound itself
is imported, not proved by our finite checker.

Suppose RH, u!=0 and u* S_L u=0. Set e=sum u_i e_i, f=Pi F_e and
y*=b A_L^(-1)f. Approximate y* in the graph core by y_n and put
z_n=e-B y_n. Completion of squares gives q(z_n,z_n)->0. The positive
spectral representation above gives, for each individual real zero gamma,

    q(z_n,z_n)>= b m_gamma/(b^2+gamma^2) |zhat_n(gamma)|^2.

Hence zhat_n(gamma)->0. L2 convergence y_n->y* implies, for every complex z,
convergence to the entire function

    H_e(z)=integral_I e(t)e^(-izt)dt
             -iz integral_I y*(t)e^(-izt)dt
             +c^2 integral_I (J y*)(t)e^(-izt)dt.          (28t)

This is the Fourier transform of the compactly supported distribution
h=Ze-(Zy*)'+c^2 Z(Jy*). The mean-zero constraint gives Jy*(L)=0.
Cauchy--Schwarz yields |H_e(z)|<=C(1+|z|)exp(L|Im z|).
A nonzero entire function with this bound has O(T) zeros in |z|<=T:
apply Jensen at any fixed nonzero-value point with radii T and 2T.
But H_e vanishes at ALL the distinct zero ordinates, whose number is
superlinear. Therefore H_e is identically zero and h=0 as a distribution.

Now (Zy*)'=Ze+c^2 Z(Jy*) is in L2(R). Thus Zy* belongs to H1(R), and,
since it is supported in [0,L], y* belongs to H0^1(I). Formula (3) applies:
B y*=e belongs to V. It also belongs to E, so e=0. Independence of the
exceptional basis forces u=0, a contradiction. This proves (28s).
The argument explicitly allows non-L2 minimizers before the last step.
The synthetic zero-Schur example in Section 8 has no superlinear zero-set
uniqueness and hence does not contradict it.

Combining (21), (26), and (28s) gives the stronger source-defined criterion

    RH iff for every integer L>=1 there exists a finite, rigorously
            enclosed matrix (26) that is POSITIVE DEFINITE.         (28u)

Under RH, its strict finite-dimensional gap exists separately at each L;
no quantitative lower bound or uniform search cost is asserted. Conversely
one such lower certificate at each integer L proves the all-window sign
and then RH by (27). This is a universal family of finite certificates,
not one finite certificate for RH and not a proof that the family exists.

### 7.2 The remaining estimate

Using (21), one exact finite-certificate version is therefore

    RH iff for every integer L>=1 and every integer k>=1,
            there exists a rigorously enclosed finite lower matrix (26)
            which is >=-(1/k)I.                           (28)

For the forward implication, the converging exact lower matrices eventually
have a margin above -1/(2k); sufficiently precise primitives give (28).
The reverse implication sends k to infinity at each fixed L, then uses
(27). The identity matrix in (28) is in the fixed exceptional coordinate
basis; it is NOT a claimed L2 spectral error for the whole compact operator.

The attempted final bound was C - b^2 G* A_L^(-1) G>=0, where
C=[q(e_i,e_j)] and G has columns f_i. Sections 2--6 make this inverse,
its residual approximations and their primitive error budgets rigorous.
They do NOT prove that inequality. Applying Cauchy--Schwarz to the FULL
indefinite form to get it would assume the desired positivity. No argument
from A_L>=kappa I, trace positivity, or a finite positive upper section is
used to manufacture the missing Schur sign. No end-to-end RH proof is claimed.

## 8. Exact countercontrols for the reasoning boundary

Let h_j=sum_(r=1)^j 1/r and A=diag(h_j) on ell2. This is a rational
logarithmic-growth model with finite-support operator core and A>=I.
Take f_j=1/j and the original compact positive block diag(h_j/j^2),
with coupling 1/j^2. Its energy minimizer in original coordinates is
(1/h_j), which is not in ell2, whereas its primitive is 1/(j h_j).
The exact Schur scalar is

    S=C-sum_(j>=1) 1/(j^2 h_j).

Truncation at M has

    U_M=C-sum_(j<=M) 1/(j^2 h_j),
    R_M=sum_(j>M)1/j^2 <=1/M,
    U_M-1/M<=S<=U_M.                                      (29)

For C=2,M=2 the lower certificate is 1/3>0. For C=1,M=2 the
upper certificate is -1/6<0. At C equal to the infinite sum, S=0 while
the original L2 form has no nonzero null vector. This retains the nullity
warning even though the strong residuals now converge.

Energy convergence alone still does not suffice: y_j=e_j/h_j has energy
1/h_j ->0 but ||A y_j||=1. This is a counterexample to that inference,
not to the specifically constructed ridge sequence (19).

These are synthetic operator models. Their signs are not actual xi/Weil
signs, and the delivered finite checks are not proofs of the infinite
analytic steps above.
