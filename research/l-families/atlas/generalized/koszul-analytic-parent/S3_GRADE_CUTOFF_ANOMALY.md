# A native S3 grade-cutoff anomaly

This is the same canonical (2,3) homotopy-Lie Hilbert parent restricted
to the actual S3 source of the preceding companion. No new diagonal
operator is fitted to a desired answer. Its Lie-grade dimensions still
grow as 2^n/n. Ordinary trace class still stops at |t|=1/2 for every
unitary source action. The results below concern its ordered finite
grade products beyond that disk, not an ordinary Fredholm determinant.

The internal grade variable is t; no arithmetic Euler product is used.
Let g be a transposition or a three-cycle, and put d=2 or 3 respectively.
The actual source shadows are

    F_e(t)=(1+2t)/(1-t)^4,
    F_g(t)=(1-t^2)^(-2) if d=2,
    F_g(t)=(1-t^3)^(-1) if d=3.                             (0.1)

Each nonidentity F_g is nonzero and holomorphic throughout |t|<1.
Nevertheless its native finite-grade products have a smaller maximal
disk of locally uniform convergence, and an anomalous value at certain
points of its boundary.

## 1. Source characters and their improved trace radii

Let M_n be the proved native Lie-dual module and set

    P_g(t)=sum_(n>=1) (-1)^(n+1) tr(g|M_n)t^n.

The equivariant PBW identity and Mobius inversion give

    P_g(t)=sum_(m>=1) mu(m)/m log F_(g^m)(t^m).              (1.1)

All logarithms initially denote the germ zero at t=0. Splitting m into
indices divisible and not divisible by the prime d gives the exact
source identities

    P_s(t)=-1/2 sum_(r odd) mu(r)/r log(1+2t^(2r)),
    P_c(t)=-1/3 sum_(3 does not divide r) mu(r)/r
                       log[(1+2t^(3r))/(1-t^(3r))].        (1.2)

For example m=2r with odd squarefree r has mu(2r)=-mu(r), and the
denominator terms of F_s(t^r) and F_e(t^(2r)) cancel exactly. For the
three-cycle they leave the displayed factor (1-t^(3r)). These formulas
come from the source Adams powers, not merely the ordinary character
of g.

Consequently, with sigma=2^(-1/d),

    P_g(t)=-1/d log(1+2t^d)+J_g(t),                        (1.3)

where J_g is holomorphic on a disk strictly larger than |t|<sigma.
In fact J_s is holomorphic for |t|<2^(-1/6), and J_c has that same
available radius. The r=1 numerator gives genuine logarithmic branch
points at the d roots tau^d=-1/2, so P_g has exact Taylor radius sigma.
Its coefficients are zero unless d divides the grade. These are trace
cancellations; the dimensions and Schatten thresholds have not improved.

Writing n=dm, the exact character formula is

    tr(g|M_n)=(-1)^n/n sum_(r|m, d does not divide r) mu(r)
                 [(-1)^(m/r+1)2^(m/r) + 1_(d=3)],        (1.4)

and it is zero when d does not divide n. Thus the actual eigenvalue
multiplicities are (epsilon_n +/- tr(s|M_n))/2 for the transposition;
for the three-cycle they are (epsilon_n+2tr(c|M_n))/3 at 1 and
(epsilon_n-tr(c|M_n))/3 at each of omega and omega^2. Integrality and
nonnegativity follow from the constructed source representation.

## 2. An exact finite-band normal form

Let D_(N,g)(t) be the product of the first N whole native grades,
with even grades in the numerator and odd grades in the denominator.
Every finite product is holomorphic and nonzero on |t|<1. Its uniquely
normalized logarithm is

    log D_(N,g)(t)=sum_(k>=1) P_(g^k),N(t^k)/k,             (2.1)

where P_(h),N keeps the source grades n<=N. Choose eta such that

    sigma < eta < 2^(-1/(d+1)).

There are holomorphic B_(N,g) converging locally uniformly, exponentially
in N on smaller closed disks, on |t|<eta, for which the exact identity is

    log D_(N,g)(t)
      = B_(N,g)(t)
        -1/d sum_(m=floor(N/d)+1)^N (-2t^d)^m/m,            (2.2)
    B_(N,g)(t) -> log F_g(t).                              (2.3)

Proof. The k=1 term in (2.1) uses (1.3), truncated in actual grade n.
Its singular logarithm is therefore cut at m=floor(N/d). The k=d
term uses

    P_e(u)=log(1+2u)+J_e(u),

where J_e is holomorphic for |u|<2^(-1/2), and is cut at grade N.
These two singular pieces have opposite signs and leave exactly the
finite band in (2.2). The remaining k=1 and k=d terms are the Taylor
truncations of J_g(t) and J_e(t^d)/d. If d=3, the only additional
k<d term is P_c,N(t^2)/2, strictly inside its improved radius.
Finally the terms k>d, including their tails in source grade, converge
absolutely on |t|<eta by epsilon_n<=3*2^n and 2 eta^(d+1)<1.
Thus all the remaining terms define the stated B_(N,g) and holomorphic
limit B_g. Inside |t|<sigma the finite band tends to zero; inside the
original trace-class disk the source theorem identifies the determinant
with F_g. Analytic uniqueness therefore gives B_g=log F_g on |t|<eta.
This also proves all convergence claims made in (2.2)--(2.3).

In particular D_(N,g) converges locally uniformly to F_g on |t|<sigma.
This is the exact maximal centered open disk of locally uniform
convergence of the products themselves, not just their logarithms:
the different boundary values proved next prevent any larger disk by
analytic uniqueness and continuity.

## 3. Boundary anomaly and transition profile

On |t|=sigma, put y=-2t^d. If y!=1, the finite band in (2.2) tends to
zero by Dirichlet convergence, uniformly on closed arcs away from y=1.
Hence D_(N,g)(t)->F_g(t) there. At any tau with tau^d=-1/2,

    D_(N,g)(tau) -> d^(-1/d) F_g(tau).                      (3.1)

Indeed the band equals [H_N-H_floor(N/d)]/d and tends to log(d)/d.
The explicit limits are

    4/(9 sqrt(2)) for a transposition,
    2/(3 cuberoot(3)) for a three-cycle.                    (3.2)

These are finite, nonzero, and different from the Abel continuation
F_g(tau). The discrepancy is forced by the same source-grade cutoff in
two different Adams powers. Using a different cutoff to remove it would
change the prescribed summation procedure.

There is a more precise transition law. Fix tau^d=-1/2 and let

    t_N(w)=tau exp(w/(dN)).

Uniformly for w in compact subsets of C,

    D_(N,g)(t_N(w))/F_g(tau)
       -> exp[-1/d integral_(1/d)^1 exp(wx) dx/x].           (3.3)

Here (-2t_N(w)^d)^m=exp(wm/N), so the finite band is a Riemann sum
for the displayed integral, and B_(N,g)(t_N(w)) converges uniformly
to log F_g(tau). The floor affects the Riemann sum by O(1/N) on each
compact w-set. At w=0 the profile gives exactly d^(-1/d).
No numerical limit fit is used to obtain this profile.

Two explicit exterior behaviors further delimit the result. Stay in
sigma<|t|<eta. If y=-2t^d is real and greater than one, then
D_(N,g)(t)->0, even though F_g(t)!=0. If y is real and less than -1,
the even-N subsequence has modulus tending to zero and the odd-N
subsequence has modulus tending to infinity. To see this, for real
|y|>1 the elementary end-dominated sum satisfies

    sum_(m=floor(N/d)+1)^N y^m/m
        ~ y^(N+1)/[N(y-1)].                               (3.4)

This follows by writing m=N-j: the fixed-j terms have relative weights
y^(-j), their tails are geometrically controlled, and N/(N-j)->1.
For y<-1 the leading sign is (-1)^N. Formula (2.2) proves the claims.
No assertion of the same pointwise behavior for every complex exterior
point is made.

## 4. An explicit bounded error at the anomalous points

The replay uses positive rational determinant blocks at tau^d=-1/2,
without adjoining a numerical d-th root. If d does not divide n, the
character is zero and all d-th root eigenspaces have equal dimensions;
the block determinant is

    (1-(-1/2)^n)^(epsilon_n/d).

If d divides n, put u=(-1/2)^(n/d). For d=2 the factors are
(1-u)^m_+ (1+u)^m_-; for d=3 they are
(1-u)^m_0 (1+u+u^2)^m_1. Each whole block then has the sign (-1)^n
in its logarithm. All factor arguments are positive rational numbers.

For a rational upper bound sigma<r<eta, define

    C_e(a)=4a/(1-a)+6a^2/[(1-a)(1-2a^2)],
    C_s(eta)=eta^6/[(1-eta^2)(1-2eta^6)],
    C_c(eta)=eta^3/[3(1-eta^3)]
               +eta^6/[(1-eta^3)(1-2eta^6)],
    C_P(b)=b^3/[(1-b^3)(1-2b^3)].

They bound respectively J_e, J_s, J_c, P_c on the relevant circles,
by |log(1+v)|<=|v|/(1-|v|) and geometric summation of (1.1)--(1.2).
Dropping Mobius signs and the factors 1/m only enlarges these bounds.
With C_g=C_s or C_c, an explicit error for

    log D_(N,g)(tau) + [H_N-H_floor(N/d)]/d - log F_g(tau)

is the sum

    C_g(eta) (r/eta)^(N+1)/(1-r/eta)
    + C_e(eta^d)/d * [(1/2)/eta^d]^(N+1)/[1-(1/2)/eta^d]
    + 1_(d=3) C_P(eta^2)/2
                         * (r/eta)^(2N+2)/[1-(r/eta)^2]
    + 3(2r^(d+1))^(N+1)/[(d+1)(1-r)(1-2r^(d+1))].        (4.1)

The first three terms are Cauchy bounds for the corresponding truncated
Taylor series. The last bounds the omitted n>N, k>d block-log terms.
The replay uses (r,eta)=(5/7,3/4) for d=2 and (4/5,5/6) for d=3.
All required inequalities follow by taking integer powers, so the
bound is evaluated entirely in Q.

The same estimate applies to a rational x=t^d on either displayed real
y ray: require |x|<=r^d, and replace 1/2 by |x| in the J_e-tail ratio
in (4.1). The other three bounds already use the upper radius r. The
replay also uses x=+/-9/16, (r,eta)=(3/4,7/9) for d=2, and
x=+/-64/125, (r,eta)=(4/5,5/6) for d=3. This controls the finite band
on both exterior ray types without using an approximate root of x.

Weighted logarithms use the rational atanh series with explicit tail;
the exact integer multiplicity is applied before directed rounding.
No expanded eigenvalue list or integer raised to an exponentially large
multiplicity is formed. The finite replay verifies source characters,
integral eigenspaces, the finite-band identity to bounded formal degree,
and (4.1) at actual whole-grade cutoffs. The general convergence,
transition profile, and exterior statements are proved above rather
than inferred from these finite controls.
