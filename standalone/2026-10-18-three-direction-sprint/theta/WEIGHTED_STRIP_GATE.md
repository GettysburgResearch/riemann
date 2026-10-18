# A safe weighted complex-node gate, and an exact false-completion trap

**Proposed complete analytic consumer and counterexample construction.
The actual all-order cone membership is open. No new zero-free band is
proved.** This extends the positive-real-node half-plane idea in PR #1003,
head `669b6a01f4d4858ae1ef806b07547be95c08c935`. Complex nodes introduce
an identification issue absent from that source's real-node theorem.
The exact obstruction below shows why moment matching and a modulus bound
alone do not cure it.

## 1. Physical coordinates and admissible nodes

Use the actual physical Xi variable throughout this note:

    H(z)=xi(1/2+iz)/xi(1/2),
    log H(z)=-v z^2/2-sum_(r>=2) A_r z^(2r)/r.                (1)

Thus `A_r=v^r Q_r` in #1003's standardized coordinates and `v>0` is
the original theta variance. For positive B and R0 with

    R0>sqrt(8) B,  eta=1-8 B^2/R0^2>0,                       (2)

let K consist of0 and the complex nodes b such that every root of
`1-bz^2` has `|Im z|<=B` and `|z|>=R0`.

This is a compact conjugation-invariant semialgebraic set. In coordinates
`b=u+it`, `s=u^2+t^2`, an exact description is

    u>=0,  s<=R0^(-4),  s<=[u+2 B^2 s]^2.                  (3)

Indeed, for nonzero b, write r=|b|. Its root satisfies
`|Im z|^2=(r-u)/(2r^2)` and `|z|^2=1/r`. Under (2), (3) forces
`u>=r-2B^2r^2>0`, so squaring introduces no wrong-sign branch.

## 2. Cofinal positive-weight cone consumer

Suppose for unbounded M there are finitely many nonzero nodes
`b_(M,j) in K` and positive real weights lambda_(M,j), closed under
conjugation with equal conjugate weights, satisfying

    sum_j lambda_(M,j) b_(M,j)^r=A_r, 2<=r<=M.              (4)

Then all zeros of the actual H obey `|Im z|<=B`.

**Proof.** If z=a+ic is either root associated to b and
`theta=arg z`, then

    Re(b^2)/|b|^2=cos(4theta)
       =1-8 sin(theta)^2+8 sin(theta)^4 >=eta.

Consequently the already matched second node power pays the complete
weighted modulus resource:

    T_M=sum_j lambda_j |b_j|^2 <= A_2/eta.                  (5)

Choose once and for all `B<d<R0`, and let

    D_d={|z|<d} union {Im z>B}.

This is simply connected: the two component domains are simply connected
and their intersection is a nonempty connected circular cap. Each factor
`1-b_jz^2` is nonzero there, so it has an analytic logarithm L_j on D_d
uniquely normalized by L_j(0)=0. Define

    P_M(z)=exp[-v z^2/2+sum_j lambda_j(L_j(z)+b_j z^2)].     (6)

All P_M are holomorphic and nonvanishing on the SAME connected domain.
The elementary inequality

    |(1-w)exp(w)|<=exp(|w|^2/2)

therefore gives, independently of the chosen logarithm's imaginary part,

    |P_M(z)|<=exp[v|z|^2/2+A_2|z|^4/(2eta)], z in D_d.    (7)

They form a normal family. At zero, (4) makes their Taylor coefficients
agree with H through degree2M. Derivatives pass to every locally uniform
limit, so any limit equals H on the disk and hence on all D_d. The full
cofinal family thus converges to H there. Hurwitz excludes zeros in
`Im z>B`, and conjugation excludes those in `Im z<-B`. QED.

For `B=1/3`, the modest fixed choice `R0=4` gives `eta=17/18`, so
`T_M<=(18/17)A_2`. The native complete theta bound in THETA_GROWTH.md
also proves the actual target has no zero on `|z|<=4`: its bound
`E exp(tX)<=exp(5t^2/176)` gives

    |H(z)-1|<=E cosh(|z|X)-1<=exp(5|z|^2/176)-1<1

on that disk. Thus this fixed gap is compatible with actual theta, rather
than a new proposed low-height conclusion. The cofinal nodes (4), with
this gap and band, are the missing construction.

## 3. A concrete approximation gate

At every order M, (4) is positive measure membership in the cone generated
by the vectors

    (Re b^2,Re b^3,...,Re b^M), b in K.                     (8)

Conjugate pairing reconstructs the complex equalities. It does not require
the real Stieltjes Hankel matrices to be positive: admissible nonreal
nodes are expressly permitted. Thus this is a genuine weaker-band
construction target rather than the real-node RH gate in disguise.

The normalization (5) bounds the total masses after weighting them by
|b|^2. An atom at0 in an original finite lambda measure contributes no
matched power and may be discarded. In contrast, an atom at0 in a WEAK
LIMIT of the |b|^2-weighted measures can retain a fourth-degree canonical
exponential contribution; it must not be silently discarded. The direct
normal-family proof above already retains such limits. A constructive
all-order argument must place the ACTUAL
vectors (A_2,...,A_M) in these cones cofinally. Positive linear dual tests
are real parts of analytic polynomials nonnegative on K. The geometric
description (3) makes both a positive construction and an obstruction
precise, but neither is obtained by merely checking finitely many orders.

There is an important missing distinction from an unrestricted numerical
complex fit: positivity of weights, the common gap, and the common branch
domain must all be certified. The following exact construction makes
that necessity decisive.

## 4. Any jet can be faked if the gap is dropped

Let any even real entire target with H(0)=1 have a local expansion (1).
Choose fixed R large enough that

    sum_(r>=2) |A_r|R^(-r)<infinity,
    R^(-1/2)<B.

Choose a fixed C greater than twice that sum. For each M>=2 let N>2M,
`theta_j=2pi j/N`, and set

    b_j=R exp(i theta_j),
    lambda_j=[C+2sum_(r=2)^M A_r R^(-r)cos(r theta_j)]/N.   (9)

Every weight is strictly positive and conjugate weights agree. Discrete
Fourier orthogonality gives EXACTLY

    sum_j lambda_j b_j^r=A_r, 2<=r<=M,
    sum_j lambda_j |b_j|^2=C R^2.                          (10)

All roots lie on the fixed circle `|z|=R^(-1/2)<B`, hence in the desired
band. The same quartic modulus envelope is uniform in M. These are
therefore positive-weight, cofinal exact jets, with both a zero band and
a uniform canonical modulus resource, for EVERY such target.

They do not imply the target's zero band. For example the standardized
positive three-point law

    H(z)=(3+cos(2z))/4

has H''(0)=-1 and zeros on `|Im z|=arcosh(3)/2>1/3`.
Construction (9) still works with B=1/3.

The reason is analytic, not numerical. Fractional canonical factors have
branch points on the inner circle. As M grows those points can become
dense, and there need be no common zero-free connected domain joining
the local Taylor disk to the exterior half-plane. A normal limit on that
exterior domain is then not identified with H by the local moments.
In contrast, the gap in Sections1--2 makes D_d common and connected.
The real positive nodes in #1003 have their branch points on the real
axis, so its direct imaginary-axis argument avoids this trap altogether.

## 5. Actual remaining analytic task

For B=1/3 and R0=4 the entire completion question is now (4) in the small
explicit region (3). Existing theta positivity and convexity give raw
moment positivity, whereas (4) concerns logarithmic coefficients. No
native positive measure for these actual holomorphic moments is yet
constructed. The prime-Gaussian log-derivative calculation is being used
to identify the arithmetic form that such a measure would have to pay;
finite complex fitting alone is not accepted as a completion.
