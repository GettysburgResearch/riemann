# A genuine real-zero Bessel construction and its cofinal obstruction

Status: **PROPOSED native component proofs and a failed all-order
completion attempt. No RH proof or new zeta zero-free region.**

After the Gaussian mediator failed, a natural replacement is a
double-exponential onsite density. It has the right leading scale for
the actual theta kernel. The simplest such base really does have only
real Fourier zeros. Nevertheless its positive Lee--Yang auxiliary
extensions cannot converge to the actual theta density, even weakly.
The obstruction is an analytic boundary of the density, rather than
finite moment infeasibility.

## 1. The base is an actual real-zero law

For a>0 let the unnormalized density be exp(-a cosh(2x)). Its Fourier
transform is

    F_a(z)=integral_R exp(-a cosh(2x)) exp(izx) dx
          =K_(iz/2)(a),
    K_(iv)(A)=integral_0^infinity exp(-A cosh t) cos(vt) dt.  (1)

The integrals converge locally uniformly in every complex parameter z.
The second equality follows by t=2x and evenness. These formulas can be
taken as the definition of K here; no assertion about its zeros is
imported.

Differentiation of (1), followed by integration by parts in t, gives
the modified Bessel equation. Consequently

    y(s)=K_(iz/2)(a exp(s)),  s>=0,
    -y''(s)+a^2 exp(2s)y(s)=(z^2/4)y(s).             (2)

All endpoint terms vanish by the exponential decay. The elementary
Laplace estimate at t=0 gives, for each fixed complex z,

    K_(iz/2)(A)=sqrt(pi/(2A)) exp(-A)(1+O_z(1/A)), A->infinity,

with the analogous differentiated bound. For example, split the
integral at a small fixed t, use cosh t=1+t^2/2+O(t^4) on the first
part and rescale t by A^(-1/2); the complementary part is exponentially
smaller. These estimates put y and y' in the energy space on the
half-line and show y is not the zero solution.

If F_a(z)=0, then y(0)=0. Multiply (2) by conjugate(y) and integrate
over the half-line. Integration by parts gives

    (z^2/4) integral |y|^2
      =integral [|y'|^2+a^2 exp(2s)|y|^2] >0.        (3)

Thus z^2 is a positive real number, so z is real. This proves the
whole-plane real-zero assertion. It does not identify these spectral
zeros with the zeta zeros.

The integral also gives log max_(|z|<=R)|F_a(z)|=O_a(R log(2+R)):
complete the elementary maximum of -a cosh(2x)+R|x| and integrate
its decreasing tails. Thus F_a is an even real entire function of
order at most one. Its paired Hadamard product has no quadratic
exponential and is a locally uniform limit of real-rooted polynomials.

There is an elementary legitimate augmentation. Multiplication of the
density by cosh(bx), b>=0, changes its transform to

    [F(z+ib)+F(z-ib)]/2.                            (4)

For a real-rooted polynomial P, if Im z>0 and b>0 then
`|P(z+ib)|>|P(z-ib)|`, by comparing each distance to each real root.
The sum in (4) therefore has no upper-half-plane zero; conjugation
gives the lower half-plane. Constant polynomials are harmless. Apply
this to the polynomial approximants of F_a and use locally uniform
convergence and Hurwitz. Repeating proves that every finite density

    exp(-a cosh(2x)) product_j cosh(b_j x)           (5)

has only real Fourier zeros. Integrability and convergence of the
transforms are paid by the double-exponential base. This is an actual
all-size construction class, not numerical zero location.

## 2. A broader cofinal class and its weak compactness

Allow any bounded symmetric auxiliary variable Y_N whose characteristic
function has only real zeros, and put

    p_N(x)=Z_N^(-1) exp(-a_N cosh(2x)) M_N(x),
    M_N(x)=E exp(xY_N),  a_N>0.                     (6)

This contains (5), with arbitrary growing numbers and weights of
independent spins. We need no additional claim that every auxiliary
in (6) preserves Fourier real zeros: the obstruction applies to the
entire broader class, so also to the verified subclass (5).

**Theorem.** The laws (6) cannot converge weakly to the actual theta law.
There is no assumed bound on a_N, on the auxiliary sizes, or on their
supports or moments.

For each N, bounded support and the real-zero hypothesis give the
even Hadamard product

    M_N(x)=product_j(1+t_(j,N)x^2),
    t_(j,N)>0,  sum_j t_(j,N)<infinity.             (7)

The product can have infinitely many factors even for finite spin
systems. The order-one bound excludes a Gaussian exponential factor;
evenness removes the linear factor. The variance also authenticates
the displayed summability.

Set V_N(x)=a_N cosh(2x)-log M_N(x). The function V_N(sqrt(u)) is
convex for u>0: cosh(2sqrt(u)) has a power series with nonnegative
coefficients and is convex, whereas log(1+tu) is concave.

If p_N converged weakly to the positive continuous theta density p,
the native compactness lemma in
`theta/RANK_ONE_HIERARCHY_OBSTRUCTION.md`, sections 2--3, would give

    V_N(x)-V_N(y) -> -log[p(x)/p(y)], x,y>0.        (8)

Its proof restricts the law of X_N^2 to a compact interval away from
zero, weights by sqrt(u), and normalizes. The new densities are
logconcave. Positive limiting masses at two exterior anchors bound
their logarithms above and below on interior compact intervals;
concavity bounds their slopes. Weak convergence then identifies the
only possible locally uniform log-density limit. This is a weak-to-local
ratio argument, not an assumption of tail convergence.

Define

    C=cosh(6)-(8/3)cosh(4)+(5/3)cosh(2)>0,
    G(t)=-log(1+9t)+(8/3)log(1+4t)-(5/3)log(1+t)>0, t>0.

Both inequalities follow by strict convexity, respectively strict
concavity, as functions of u at u=1,4,9. The coefficients cancel the
constant and linear terms. Hence

    V_N(3)-(8/3)V_N(2)+(5/3)V_N(1)
       =a_N C+sum_j G(t_(j,N)).                    (9)

The left side is bounded by (8). In particular a_N is uniformly
bounded. The additional finite difference from 1 to 2 gives

    sum_j log[(1+4t_j)/(1+t_j)]
       =a_N[cosh(4)-cosh(2)]-[V_N(2)-V_N(1)] <=C_1.

Every term is nonnegative. For t<=1 its logarithm is at least 3t/5;
for t>1 it is at least log(5/2). Consequently

    sum_(t_j<=1)t_j<=C_2,    #{j:t_j>1}<=C_3.       (10)

These uniform resources were deduced from weak convergence and fixed
local ratios. They were not imposed on the candidate models.

Normalize the auxiliary at x=1 rather than at zero:

    Q_N(z)=M_N(z)/M_N(1)=product_j (1+t_j z^2)/(1+t_j).

For |z|<=R the small factors have product bounded by exp(C_2 R^2),
and each large factor has modulus at most max(1,R^2). Thus (10)
gives a common entire bound for Q_N. After taking a subsequence,
a_N tends to a>=0 and Q_N tends locally uniformly to an entire Q
with Q(1)=1. Equations (6) and (8) imply, for every real x>0,

    p(x)/p(1)=exp[-a(cosh(2x)-cosh(2))] Q(x).       (11)

The right side is entire in x. Therefore the proposed weak limit
would force the actual theta density to extend to an entire function.

## 3. A native cusp proof that the actual density is not entire

Let

    Theta(v)=sum_(n in Z) exp(-pi n^2 v), Re v>0.

The actual original even theta kernel, on |Im z|<pi/4, is

    Phi(z)=2 v^(9/4)Theta''(v)+3 v^(5/4)Theta'(v),
    v=exp(2z),                                    (12)

with the analytic branches inherited from this strip. Expanding the
derivatives gives exactly
`sum_(n>=1)[4pi^2 n^4 exp(9z/2)-6pi n^2 exp(5z/2)]exp(-pi n^2 exp(2z))`.
The sum is normally convergent on each compact substrip. It is positive
and nonzero at real z>=0.

Take v=i+epsilon with epsilon>0. The elementary Gaussian Poisson
formula, with the half-character (-1)^n, gives the exact identity

    Theta(i+epsilon)=sum_n (-1)^n exp(-pi epsilon n^2)
       =epsilon^(-1/2) sum_(m in Z)
                         exp[-pi(m+1/2)^2/epsilon]. (13)

Differentiating in epsilon once and twice is legitimate by absolute
convergence. On the right each derivative is a finite sum of fixed
powers of epsilon^(-1) and (m+1/2), multiplied by the same exponential.
The Gaussian tail is summable uniformly after its first exponent is
extracted. Thus Theta and its first two derivatives at i+epsilon
are `O(epsilon^(-A)exp[-pi/(4epsilon)])` for fixed finite A.

Put z(epsilon)=(1/2)Log(i+epsilon), on the branch approaching
z_0=i pi/4. Equation (12) yields

    Phi(z(epsilon))=O_N(epsilon^N) for every integer N>=0. (14)

If Phi had a holomorphic extension to a neighborhood of z_0, its
composition with the analytic coordinate z(epsilon), whose derivative
at zero is 1/(2i), would be holomorphic near zero. Equation (14) forces
every Taylor coefficient to vanish. The identity theorem would then
make Phi identically zero on the connected original strip, contrary
to its positive real value. Hence Phi has no holomorphic extension
through this cusp and is certainly not entire.

The normalized actual density is a fixed positive multiple of Phi,
so (11) is impossible. This proves the cofinal obstruction in section2.

## 4. What this attempt established

The Bessel base and all its finite independent-cosh augmentations are
legitimate whole-plane real-zero models. Replacing a Gaussian onsite
term by a double-exponential one therefore gives a concrete alternative
construction to try. The full weak-closure argument shows why this
particular positive auxiliary completion still cannot reach actual
theta, even with unrestricted size and parameters.

This does not exclude arbitrary nonanalytic onsite terms, changing
onsite shapes without the stated compactness, signed auxiliaries,
or other observation maps. It is a proposed internal component proof;
its exact final bytes need independent source-specific review. The
argument proves no claim about the location of the actual zeta zeros.
