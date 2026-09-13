# An exact centered-gamma shape flow and its complete nonreal-zero current

2026-09-12. **Proposed component proofs; independent analytic review required.
The actual signed-production inequality and RH remain open.**

PR #862 at `67d5d6a5f588642f4c451fe35d2369b5ddac9346` supplies the centered
family, eventual real tails at fixed stage, and convergence of its weighted
nonreal-zero defect to the Xi defect. PR #869 at
`6603f8b04f9a2d073123a328ac0298a498c93a96` has already constructed a different
positive convolution path from a known zero-defect Bessel anchor to compressed
native sources, with a signed Jensen balance. We do not claim the general
source-derivative or signed-balance idea as new.

Here the path joins consecutive ORIGINAL centered integer stages by increasing
one gamma SHAPE, while keeping its rate fixed and removing precisely the added
mean. The constructive addition is a positive coefficient expansion with an
explicit normalized score, followed by a finite-all-exceptions zero-current
identity at each fixed step. It is not #868's scale path, #869's anchor path,
or an assertion of globally nonpositive production.

## 1. A mean-preserving positive path between exact integer stages

Let G_n be independent Gamma(shape 2, rate 1), and

    X_N=sum_(n<=N)G_n/n^2, tau_N=2sum_(n>N)n^-2.

Fix N>=2, let B=(N+1)^2, and for 0<=u<=2 define

    Y_u=X_N+Gamma(shape u, rate B)+b_u,
    b_u=tau_N-u/B.                                         (1)

Shape zero means the deterministic zero variable. The endpoints are precisely
X_N+tau_N and X_(N+1)+tau_(N+1). The drift b_u is strictly positive. The mean is
constant, 2zeta(2)=pi^2/3. No spectral data define this interpolation.

For Re(s)>=0 the exact Laplace identity is

    L_u(s)=L_0(s) exp{u[s/B-log(1+s/B)]}.                    (2)

Extending the density g_u by zero below its support, its derivative is

    partial_u g_u(x)= B^-1 partial_x g_u(x)
       +integral_0^infinity [g_u(x-v)-g_u(x)]exp(-Bv)dv/v.   (3)

The subtraction in the small-jump integral is indispensable. One proof uses
Frullani's identity in (2); another truncates the Lévy measure below epsilon,
differentiates the finite compound-Poisson convolution, and passes to zero.
The translation difference is bounded by v times a weighted derivative norm.
The Gamma(2,rate1) factor and the other gamma factors give the needed smoothness
and exponential tails. Thus (3) is a convergent identity, not a formal
infinite-order differential operator with a guessed sign.

## 2. A positive density expansion for every parameter in the step

Write nu=2N+u and w=x-b_u>0. Form the 2N nonnegative numbers

    B-1,B-1,B-4,B-4,...,B-N^2,B-N^2.

Let h_k be their complete homogeneous symmetric polynomial of degree k,
h_0=1, and put

    S_nu(w)=sum_(k>=0) h_k w^k/(nu)_k.

Then the COMPLETE density is

    g_u(x)=[(N!)^4 B^u/Gamma(nu)]
                  w^(nu-1)exp(-Bw)S_nu(w).                (4)

Indeed expand the Laplace transform about s+B:

    product_(n<=N)(s+n^2)^-2 (s+B)^-u
                 =sum_(k>=0) h_k(s+B)^-(nu+k).

All coefficients are positive; Tonelli and the gamma Laplace integral justify
inversion and equality. The same formula holds at u=0. No additional h_k term
comes from the new gamma factor, because its rate difference B-B is zero.
Thus h_k does NOT depend on u.

Let D=B-1. Counting the 2N variables gives, for every u in [0,2],

    0<=h_k/(nu)_k <=D^k/k!.                                (5)

Consequently (4) and its necessary parameter/space derivatives converge
normally on compact positive w intervals.

### A complete and directly usable tail budget

For v=Dw, L=K+1 and r=v/(K+2)<1, set t=v^(K+1)/(K+1)!. The omitted positive
series is at most t/(1-r); its k-weighted version is at most

    t [L/(1-r)+r/(1-r)^2].                                (6)

The harmonic weight H_(nu,k)=sum_(j=0)^(k-1)1/(nu+j) is <=k/(2N), so (6)/(2N)
pays its complete omitted tail. These are full infinite series bounds, not
successive-truncation agreement. gamma_score.py implements the resulting
positive enclosures for rational inputs; evaluating an entire Fourier contour
would still require an additional whole-integral quadrature certificate.

## 3. An explicit normalized source score without a digamma evaluation

Under the discrete probability distribution

    P_w(K=k)=h_k w^k/[(nu)_k S_nu(w)],

differentiate (4) at fixed x, noting partial_u w=1/B:

    partial_u log g_u(x)
       =log B-psi(nu)-1+log w
        +[nu-1+E_w K]/(Bw)-E_w H_(nu,K).                   (7)

Every expectation in this expression is positive-series computable using
(5)–(6). There is no uncomputed signed gamma-mixture expansion.

Set x_+=pi exp(2t), x_-=pi exp(-2t), w_+=x_+-b_u, w_-=x_--b_u, and

    h_u(t)=sqrt(g_u(x_+)g_u(x_-)), Z_u=integral_R h_u(t)dt,
    p_u(t)=h_u(t)/Z_u, F_u(z)=integral_R exp(izt)p_u(t)dt.

Inside the support define

    S_u(t)=(1/2)sum_(sign=+,-)
       {log w_sign+[nu-1+E_(w_sign) K]/(B w_sign)
                          -E_(w_sign) H_(nu,K)}.           (8)

The constant log B-psi(nu)-1 disappears on normalization. Thus the exact update
is

    partial_u p_u(t)=p_u(t)[S_u(t)-E_p S_u],
    partial_u F_u(z)=Cov_p(exp(izt),S_u(t)).                (9)

These are complex-bilinear covariances, not nonnegative variances.

### Moving endpoints and the full source are accounted for

The support radius is T_u=log(pi/b_u)/2. From (4),

    h_u(t)=(T_u^2-t^2)^(N+(u-1)/2) A_u(t), |t|<T_u,       (10)

where A_u is positive and real analytic on the closed segment and nonvanishing
in a complex neighborhood. To obtain the neighborhood, factor the endpoint
zeros of x_sign-b_u explicitly, and use positivity of S_nu on the compact
real interval, including S_nu(0)=1. Compactness in u supplies common local
nonvanishing neighborhoods at fixed N. The positive square roots fix the
analytic branches; no unrestricted complex square root is presumed.

Here the endpoint exponent is at least 3/2. In (8) the only possible leading
singularities are inverse distance and logarithm, so p_u S_u is integrable.
Differentiating the moving support adds no boundary atom because h_u vanishes
there. With t=T_u v the domain is fixed to [-1,1]; the endpoint factor
(1-v^2)^(N+(u-1)/2) and all its local u derivatives are integrable. This proves
(9), including both endpoints u=0,2, and locally uniform entire z convergence
of the derivatives. It also gives local holomorphic dependence on a complex
u near the real parameter interval after choosing the fixed logarithm of
1-v^2 in the integral.

For a full step-wide envelope write Y_u=G_1+V_u. Jensen's inequality on the
omitted tail and the unused portion of Gamma(2,rate B) gives

    E exp(V_u)<=product_(n>=2)(1-n^-2)^-2=4.

Hence g_u(x)<=4x exp(-x) and h_u(t)<=4pi exp(-pi cosh(2t)). Also E V_u<1.3,
so P(V_u<=2.6)>1/2. On 3<=x<=4 the remaining G_1 argument is in [0.4,4], where
x exp(-x)>1/16. Since both pi exp(+-2t) lie in [3,4] for |t|<=1/100,
Z_u>1/1600. These estimates are uniform in N and u; they retain the whole law,
not a truncated density.

## 4. All nonreal zeros are in one finite disk for each FIXED step

**Proposed component theorem G1.** For every fixed N there is an R_N such that
for every u in [0,2], every zero of F_u outside |z|<=R_N is real and simple.
No N-uniform R_N or numerical value is asserted.

Here is why the compact-parameter strengthening of #862's endpoint argument
applies. The exponent in (10), the positive endpoint amplitudes, their analytic
neighborhoods and derivative majorants vary on compact parameter sets. Their
positive lower bounds do not vanish. The complete two-endpoint contour
expansion, in the near-horizontal sector, has the uniform form

    F_u(z)=c_u z^(-alpha_u-1)
       [cos(T_u z-pi(alpha_u+1)/2)
                       +O_N(exp(T_u |Im z|)/|z|)],        (11)

where alpha_u=N+(u-1)/2 and c_u is positive. Constants are uniform in u,
not in N. In the complementary near-vertical sectors one endpoint dominates
and the same remainder is smaller than it. No late nonreal zero can occur
there. In the horizontal sector the two-endpoint bound first confines zeros
to shrinking disks about the REAL cosine zeros in (11). Uniform Rouché
comparison on disks of radius K_N/|z| gives exactly one zero in each late disk
and none in the complement. Each disk is invariant under conjugation and F_u
is real entire, so that unique zero is exactly real and simple.

The contour justification is the endpoint proof of #862 with uniform compact
parameter majorants: retain both branch endpoints, indent locally along their
chosen cuts, and estimate the remaining displaced contour exponentially. On
the complementary vertical sector retain the single dominant endpoint. This
is not a fixed-frequency expansion extrapolated to all arguments. Replacing
its pointwise positive constants by their minima/maxima on [0,2] gives (11)
and a common R_N. Independent review of this uniformization is important.
The theorem allows nonreal zeros at arbitrarily many successive integer stages.

## 5. A current that includes every multiplicity and every collision

The inherited weighted defect is

    Delta(u)=(1/4)sum_(F_u(rho)=0) mult(rho)(Im rho)^2/|rho|^4.

Equivalently, sum once over each first-quadrant nonreal quartet with its
multiplicity. Imaginary-axis zeros are absent because F_u(iy)>0, and F_u(0)=1.
For fixed N, G1 places every nonzero contribution inside one finite disk.
Jensen and the uniform entire envelope bound the number of zeros there
uniformly, and compact convergence keeps them away from the origin.

Local Weierstrass preparation and Puiseux parametrization give finitely many
root branches on compact real parameter subintervals. Persistent multiplicity
is allowed; isolated splitting/collision parameters need not be simple. Their
coordinate derivatives have integrable power singularities. The function
(Im rho)^2/|rho|^4 is smooth away from zero, so its contribution is absolutely
continuous even when real roots split into a nonreal quartet or merge back.
Real zeros crossing an artificial disk boundary contribute zero. A finite
parameter cover proves absolute continuity of the WHOLE Delta(u), not merely
of a preselected list of tracked simple roots.

At a regular parameter, let rho be a root of persistent multiplicity m. Then

    rho'=- [partial_u partial_z^(m-1)F_u(rho)]/
                         [partial_z^m F_u(rho)]
         =- E[(it)^(m-1)exp(i rho t)S_u(t)]/
                         E[(it)^m exp(i rho t)].           (12)

The denominator is nonzero at exactly that multiplicity. The centering term
in (9) cancels because partial_z^(m-1)F_u(rho)=0. This is the appropriate
formula at a persistently multiple root, not an illegal division by F'_u.

For rho=x+iy, direct differentiation gives

    d/du [y^2/|rho|^4]
         = [2y/|rho|^2] Im(rho'/rho^2).

Consequently the COMPLETE integer-step balance is

    Delta_(N+1)-Delta_N
       =integral_0^2 sum_(first-quadrant rho)
            [2m_rho Im rho/|rho|^2] Im(rho'/rho^2) du.      (13)

At the finitely many branch events this is understood through the absolutely
continuous continuation just proved. There are no omitted collision atoms,
no discarded nonreal tail, and no simplicity assumption on Xi. The finite
checker verifies the current's sign/factors on Gaussian-rational derivatives;
it does not compute the actual zero branches or certify the integral's sign.

## 6. The unresolved end-to-end estimate

Equation (13) is NOT a dissipation theorem. The source score is not assigned
a sign, and an absolute density approximation does not bound the sign of
(12). #858's actual centered N=5 nonreal quartet already precludes pretending
that all finite stages have zero defect.

One sufficient target is a cofinal block sequence N_j and numbers
0<a_j<=1, b_j>=0 satisfying

    Delta_(N_(j+1)) <= (1-a_j)Delta_(N_j)+b_j,
    sum a_j=infinity,       b_j/a_j ->0.                   (OPEN-G)

The elementary scalar iteration then forces Delta_(N_j)->0: for any epsilon,
eventually b_j<=epsilon a_j, and the remaining excess contracts by the product
of 1-a_j. The inherited whole-source defect convergence gives Delta_Xi=0 and
hence RH, with all multiplicities retained. Neither OPEN-G nor an alternative
native signed-production bound is established here.

Starting (13) at a generic finite N also leaves an unknown initial defect.
#869's Bessel anchor addresses that baseline for its different path, and its
signed Jensen balance is complementary to this explicit consecutive-stage
score. Convergence of differences alone cannot determine the limiting defect.
The remaining inequality is substantive research, not a routine reviewer task.
