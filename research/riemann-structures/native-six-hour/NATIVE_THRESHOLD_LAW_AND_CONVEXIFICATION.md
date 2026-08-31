# Threshold laws and the exact pair-source convexification defect

This note gives an exact parametrization of the pair occupation body
and a constructive correction from an average of pair profiles to one
legal pair profile. It concerns the literal finite-prime half-source,
with its original2ds current and physical observation. It does not
identify a full retained-gamma source or optimize its energy.

The predecessor NATIVE_OCCUPATION_MOMENTS.md at
a75f3bbef5f75bb6a4bd7f3c91d051cfb132f3dc already proves the exact(A,C)
projection, sharp bounds on B, and the limitation of the event-order
polytope. NATIVE_REYNOLDS_PATH_OBSTRUCTION.md at
5e312c7dc81926e637d2d7343f90eba4708587c0 supplies the complementary
upper variance bound. The statements below derive the full threshold-law
parametrization and its precise source-averaging defect; no broad
priority claim about these elementary probability identities is made.

## 1. Every pair profile is one threshold law

Let u,v be continuous nondecreasing coordinates from0 to1. Integration
against du gives a nondecreasing profile f:[0,1]->[0,1], defined almost
everywhere. Vertical segments have zero du mass. There is a unique
probability law mu on[0,1] such that

    f(s) = mu([0,s]) almost everywhere.                       (1)

The atom at0 records an initial vertical segment, and the atom at1
records any final vertical completion. Thus(1) includes constant
profiles and all endpoint cases.

Conversely, every probability law mu defines a legal completed monotone
graph through(1), with initial and final vertical segments where needed.
Parameterizing that graph by its sum coordinate u+v gives a continuous
Lipschitz monotone path from(0,0) to(1,1). Its Stieltjes integrals are
the original integrals along that path. A finite atomic law gives a
finite piecewise-linear path. For a path convention restricted to
finitely many smooth pieces, general laws describe its continuous
completion; finite atomic approximation recovers all moment limits.

Let T,S be independent with the same law mu, and define

    A = integral_0^1 f(s) ds,
    B = integral_0^1 s f(s) ds,
    C = integral_0^1 f(s)^2 ds.

Tonelli's theorem applied to the threshold indicators gives

    A = 1-E T,
    B = (1-E T^2)/2,
    C = 1-E max(T,S)
      = A-E|T-S|/2.                                         (2)

Therefore the completed pair occupation body is exactly

    {(1-E T, (1-E T^2)/2,
       1-E T-E|T-S|/2): law(T)=law(S)=mu, T independent S},    (3)

where mu ranges over probability laws on[0,1]. This is a parametrization
by one common law, not permission to choose its first two moments and
its Gini mean difference independently. The random variables here
represent a fixed deterministic profile and do not replace2ds or the
original Mellin measure.

The upper variance inequality also has a short proof in these variables.
Since |T-S|>=(T-S)^2 on the unit interval,

    E|T-S| >= 2 Var(T).

Substituting(2) gives exactly C-A^2<=2B-A. Equality holds precisely when
mu is a point law or is supported on{0,1}. To prove necessity, the
nonnegative difference |T-S|-(T-S)^2 must vanish almost surely. If the
support contained two points at distance strictly between0 and1, small
neighborhoods of those points would have positive product measure and
give a contradiction. Any two distinct support points must therefore
be0 and1, and then there can be no third support point. A singleton
support is the remaining case. Conversely, both listed types give
equality directly. The corresponding profiles are exactly a full
zero-to-one threshold or a constant almost everywhere, including the
constant endpoint cases. The existing lower Gram bound and other
occupation constraints remain separate necessary consequences of(3).

## 2. Averaging profiles and averaging sources are different

Let f_omega be a measurable family of legal pair profiles, with omega
distributed by a probability law. Finite mixtures are included. The
pointwise average

    f_bar(s) = E_omega f_omega(s)                              (4)

is nondecreasing and lies in[0,1], so it is itself a legal completed
profile. Equivalently its threshold law is mu_bar=E_omega mu_omega.
The first two occupation coordinates are linear:

    A(f_bar)=E A(f_omega),  B(f_bar)=E B(f_omega).

The third has the exact defect

    Delta = E C(f_omega)-C(f_bar)
          = integral_0^1 Var_omega(f_omega(s)) ds
          = E ||f_omega-f_bar||_(L2[0,1])^2 >= 0.             (5)

It vanishes precisely when the profiles coincide almost everywhere
for almost every omega. In threshold-law terms, writing
G(mu)=E_(mu times mu)|T-S|, the same identity is

    G(mu_bar)-E G(mu_omega)=2 Delta.                          (6)

Thus forming the one legal average profile has an exactly measured
correction to the average current. It is not an operation that preserves
all pair-source coordinates unless Delta is zero.

For the two equally likely sequential orders, the profiles are0 and1.
Their average profile is1/2, with moments(1/2,1/4,1/4), whereas the
average source has moments(1/2,1/4,1/2). Equation(5) gives Delta=1/4.
The constant-height profile is realized by activating v to1/2, then u
to1, then completing v. This is a constructive legal correction of the
Reynolds example, but it changes its source and depends on the chosen
u-time coordinate. No permutation-equivariant projection is asserted.

The equality classification also identifies the unique nearest pair
profile in the maximum-moment norm of the Reynolds obstruction. Put
epsilon_*=(sqrt(10)-3)/2. At a legal triple whose distance from
(1/2,1/4,1/2) is epsilon_*, equality in

    1/4 <= 2 deltaB-deltaC+deltaA^2
         <= 3 epsilon_*+epsilon_*^2

forces deltaB=epsilon_*, deltaC=-epsilon_* and
|deltaA|=epsilon_*, as well as equality in the variance inequality.
A constant profile has B=A/2, which is incompatible with those
deviations. A threshold has C=A, forcing A=1/2-epsilon_* and its
threshold location t=1/2+epsilon_*. Thus the nearest moment triple and
its completed planar graph are unique, up to pauses and weak monotone
reparametrization. This does not determine any additional coordinates
in a higher-arity path or a nearest path in the physical Hilbert norm.

## 3. The entire correction for a genuine two-prime source

For exactly two schedule coordinates, every local half-source coefficient
lambda_n is bilinear in u,v. If f,g are any two bilinear polynomials,
the uv term cancels in df wedge dg; its remaining coefficients are a
linear combination of1,u,v. Consequently, modulo endpoint-exact forms,
all currents2 integral g df depend affinely on precisely A,B,C.
The actual curvature dimension is three, also given by the general
source quotient in NATIVE_S3_CURVATURE_ISOTYPES.md at
cb9278bec3844cc3fd8072987a6890f1df32a368.

Write the complete source as

    J(f)=J_0+A R_A+B R_B+C R_C,                              (7)

where R_C is the coefficient vector for a unit change of C with A,B
fixed. These are source vectors, not orthogonal Hilbert directions.
Equations(4)--(5) imply the full all-record identity

    E J(f_omega)-J(f_bar)=Delta R_C.                         (8)

The vector R_C is nonzero in the literal native source. For distinct
primes p,q, the original half-source gives

    B_(p,q)=A/2,  B_(p,pq)=-B/4,  B_(q,pq)=(C-1)/8,

with B_(n,m)=2 integral d(lambda_n) lambda_m. In particular the
(q,pq) record of(8) equals Delta/8, with no omitted derivative weight
or endpoint constant. These readouts also show independence of the
three coordinates in(7).

For every finite horizon, applying the complete original physical
observation to(8) gives the same identity with R_C replaced by its
observed field. All1/sqrt(nm) factors and1/d aliases remain inside that
linear map. At infinity the identity holds in the original Hilbert
space by finite-prime absolute completion; the faithful observation
proved at822646ffea23d906c385f0273a8c45693e982c4d makes its right side
nonzero whenever Delta>0. A small finite horizon can forget this
direction, so no claim of physical visibility at every cutoff is made.

For three or more coordinates, equations(1)--(6) still describe each
pair projection, but they do not reconstruct all joint occupation
moments of the original paths. A common-time realization of several
averaged pair profiles needs additional compatibility. Equation(8) is
therefore asserted for the complete two-prime source only. No energy
decrease, orthogonal projection, higher-arity decoder or optimizer
persistence is inferred from the nonnegative scalar Delta.

This is a proof-only construction. It requires no new numerical
acquisition or scientific test job.
