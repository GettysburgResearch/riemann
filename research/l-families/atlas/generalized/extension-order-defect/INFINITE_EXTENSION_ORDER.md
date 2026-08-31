# Infinite adjoining makes the extension order change the Taylor radius

Status: proposed continuation, separate from the first finite-generator
extension-order packet. The completion input is the independently reviewed
`graded-completion-lab/MATHEMATICS.md` at
`64075f1a3f81529f217dee1ae139656dfb9356f3`. This companion's own execution
and frozen-commit review are not yet claimed.
The finite extension comparison is frozen at
`0018b73f60e42bc793d172c381547de34322d8ca`.

Scope: the actual S3 coherent source over F7 with a=1,b=0, and its constant-
field extension to F49. All sheaves are ordinary and constructible in
each finite grading degree. No infinite-rank cohomology theorem is used.

## 1. Two actual degreewise limits with the same generic algebra

Let T_n=B_n sign direct-sum C_n Std be the nontrivial part of the actual
untwisted Lie grade M_n, for even n>=2. Define the weighted generic
generator space Z=direct-sum_(even n>=2) T_n< n >. For every total grade
m only finitely many generators and weighted partitions contribute.
Consequently both constructions

    B_infinity=(j_*A) tensor Sym(direct-sum_even (j_*T_n)<n>),
    C_infinity=j_*(A tensor Sym Z)

exist degree by degree and have the same generic graded algebra. The
finite-generator comparison gives an injective map B_infinity->C_infinity
and an actual graded boundary B_infinity-module cokernel. This is a
formal source statement, not a topology or a convergent infinite determinant.

The finite boundary support still does NOT imply a rational scalar
correction once infinitely many grading degrees are assembled. This
note gives an explicit failure: the after-source full Euler limit has
Taylor radius1/sqrt(2) over F7, while the before-source limit has radius1/2.

## 2. Exact local products from the actual inertia characters

Put a_n=B_n+C_n, the transposition anti-invariant dimension of M_n.
At an old C2 branch, T_n has C_n invariant and a_n anti-invariant
vectors. Let

    V(t)=product_even (1-t^n)^(-a_n),
    W(t)=product_even (1+t^n)^(-a_n).

The common product from invariant generators cancels in the ratio.
For actual residue-field sign epsilon, the before/after ratio is

    R_epsilon(t)=[F_e(epsilon t)V(t)+F_s(t)W(t)]
                                      /[F_e(epsilon t)+F_s(t)].      (2.1)

At the central quadratic zero, every T_n is untwisted and n is even.
Hence the two extension orders still agree in all grades there.

At split infinity the sign module is C3-invariant and the standard
module has no invariant vectors. Write E(t)=even(F_e(t)) and
C(t)=even(F_c(t)). After canceling the common sign-generator factors,

    X(t)=product_even (1-t^n)^(-2C_n),
    Y(t)=product_even (1+t^n+t^(2n))^(-C_n),
    R_inf+(t)=[E(t)X(t)+2C(t)Y(t)]/[E(t)+2C(t)].                    (2.2)

At nonsplit infinity the residual coset consists of transpositions,
and cancellation instead gives

    R_inf-(t)=product_even (1-t^(2n))^(-C_n).                       (2.3)

These formulas follow by applying Reynolds averaging to the FULL generic
algebra in each finite degree. They are first formal identities. They
are analytic local expressions for |t|<1/2 except at removable denominator
zeros after the full source factors are restored. In particular they
do not replace the additive boundary cokernel by its ordinary determinant.

Both full-place products have an initial absolute-convergence disk
|z|<1/Q. To check this directly, choose a fixed local radius r<1/2.
The positive dimension series of the generic algebra converges there,
so every source-character local factor differs from one by at most
M_r |t| for |t|<=r. Closed points of degree d number at most a constant
times Q^d/d. Thus the local-factor difference sum converges when
Q|z|<1. This also identifies the formal comparison with an analytic
identity before continuation is used.

## 3. Controlled first singularities of the local correction

Set x=t^2 and D=1-4x. The completion source proves

    a_(2j)=4^j/(4j)+e_j,
    sum_j e_j x^j is holomorphic for |x|<4^(-1/3).

The analogous estimate for the standard multiplicity is

    C_(2j)=4^j/(6j)+f_j,
    sum_j f_j x^j is holomorphic for |x|<1/2.                      (3.1)

For completeness, the frozen Adams formula gives
|dim M_n-2^n/n|<=2^(floor(n/2)+1)/n for even n. In the 3-cycle
character, divisors divisible by three contribute only powers at most
2^(n/3); the remaining terms have absolute value at most4 per divisor.
Thus

    |tr(c|M_n)|<=4+2^(floor(n/3)+1)/n.

Since C_n=(dim M_n-tr(c|M_n))/3, (3.1) follows. These estimates prove
convergence of the remainders and are not finite character extrapolations.

Using logarithms defined at zero, the linear terms and absolutely
convergent quadratic remainders now give

    V=D^(-1/4) A_V,       W=D^(1/4) A_W,
    X=D^(-1/3) A_X,       Y=D^(1/6) A_Y,                           (3.2)

where every A is holomorphic and nonzero on |x|<1/3 and positive at
x=1/4 along the real interval. Indeed the multiplicity errors converge
there, and all quadratic logarithm tails are bounded by constants times
sum_j 4^j |x|^(2j)/j. Individual factors have no zeros in this chosen
disk. In addition V W=product_even(1-t^(2n))^(-a_n) is holomorphic
and nonzero across x=1/4.

At t=1/2, F_e(t)>0 while

    F_e(-t)=D/[(1+2t)(1+t)^4].

Equations (2.1)--(3.2) therefore yield exact leading behaviours

    R_+(t) ~ positive_constant D^(-1/4),
    R_-(t) ~ positive_constant D^(1/4),
    R_inf+(t) ~ positive_constant D^(-1/3).                       (3.3)

These are full local asymptotics, not the order of a meromorphic function:
the fractional powers are essential. The product R_+R_- has the form
U_0(t)+D^(1/2)U_1(t), with U_0 holomorphic and U_0(1/2)>0.
To see this, expand the two numerators. Their mixed term contains
V W and is nonzero; the remaining terms contain either W^2 or
F_e(-t)V^2 and hence D^(1/2). Similarly R_inf+ is D^(-1/3)
times a function holomorphic in t and D^(1/2), with nonzero constant term.

Nonsplit infinity is different: (2.3) is holomorphic across t=1/2.
Its first potential multiplicity singularity is at |t|=1/sqrt(2).
No transfer of the split-infinity exponent to that Frobenius coset is made.

## 4. The actual old branch points over F7 and F49

For the fixed source the old discriminant over F7 is u^4+3.
Its roots satisfy u^4=4, with factorization

    u^4-4=(u^2-2)(u^2-5).

The first factor has roots u=3,4=-3, and their quadratic signs are
minus and plus. The second is irreducible over F7 and is one closed
point of degree two. Its residue-field quadratic sign is plus:
the norm of a root is -5=2, a square in F7. Infinity is split because
7=1 modulo3. Therefore the infinite full boundary ratio is

    Xi_7(z)=R_+(z)R_-(z) R_+(z^2) R_inf+(z).                     (4.1)

Upon extending constants to F49 all four roots are rational and all
their quadratic signs are plus. Elements of F7^* become squares in F49;
the other two roots retain the just computed norm sign. Hence

    Xi_49(z)=R_+(z)^4 R_inf+(z).                                  (4.2)

This is exact constant-field source data, not a new F49 point count.
The finite replay checks the seven residue classes and this factorization.
Equations (3.3)--(4.2) give, at the positive point z=1/2,

    Xi_7(z) ~ c_7 (1-4z^2)^(-1/3),
    Xi_49(z) ~ c_49 (1-4z^2)^(-4/3),       c_7,c_49>0.            (4.3)

The degree-two factor in (4.1) is evaluated at z^2=1/4, strictly within
the local convergence disk, and is positive and nonzero. Its inclusion
is necessary even though it does not change this leading exponent.

The leading constants can be recorded without any fitted normalization.
Evaluate the analytic units in (3.2) at x=1/4. Since F_e(1/2)=32,
F_s(1/2)=16/9, E(1/2)=16 and C(1/2)=64/63, they are

    c_7  =(18/19)(63/71) A_V A_W A_X R_+(1/4),
    c_49 =(18/19)^4(63/71) A_V^4 A_X.                            (4.4)

There is also a distinct, intrinsic finite-generator boundary limit.
Retain grades n<=N=2J in every product, and write H_J=sum_(j<=J)1/j.
At t=1/2 the finite V,W,X,Y respectively have leading sizes
exp(H_J/4)A_V, exp(-H_J/4)A_W, exp(H_J/3)A_X and
exp(-H_J/6)A_Y. Therefore

    exp(-H_J/3) Xi_(7,2J)(1/2)  -> c_7,
    exp(-4H_J/3) Xi_(49,2J)(1/2) -> c_49.                         (4.5)

This is convergence in the prescribed source-generator order. It is not
an ordinary Fredholm determinant at the boundary and is not a rearrangement
of closed places. Replacing H_J by log J+Euler's constant gives the
equivalent J^(1/3) and J^(4/3) growth, with the corresponding Euler-constant
factors. In particular the grade cutoff is J=N/2, not N.

## 5. From local branches to exact radii of the full before-source

Let H_after,Q denote the full formal Euler function of B_infinity and
H_before,Q that of C_infinity. Formal comparison and initial convergence
give

    H_before,Q = H_after,Q Xi_Q.                                  (5.1)

One must exclude an earlier pole coming from a denominator in (2.1) or
(2.2). In the finite after-source H_2, each factor F_(A^I,phi) is
literally present at the corresponding bad place. Removing these
factors leaves a meromorphic function whose only possible interior
poles come from the same arithmetic cohomological factors. At their
zeros these removed bad numerators do not vanish, by the frozen
prime-support argument. The factor P_E(z^2) already cancels the first
arithmetic poles. Consequently H_2 divided by the finite product of
these bad A factors is holomorphic on |z|<1/2 in both fields: over
F7 its first remaining poles are farther away; over F49 all arithmetic
poles have been cleared. The extra finite-generator local determinants
have only unit-circle roots.

The pure after-ladder K_Q is holomorphic on |z|<1/2, and all local
generator products in the numerators of (2.1)--(2.2) converge normally
there. Restore the actual bad numerator factors using (5.1). This
proves that H_before,Q is holomorphic on |z|<1/2. It also explains why
studying Xi alone and counting its displayed denominator zeros would
give a false list of new poles.

Over F7 the completion theorem makes H_after,7 holomorphic on the larger
disk |z|<1/sqrt(2). At z=1/2 it has some finite integer zero order m>=0.
The first line of (4.3), with a nonzero Puiseux leading coefficient,
gives exponent m-1/3 for H_before,7. No integer m removes this branch.
Therefore

    radius H_before,7 = 1/2,
    limsup |[z^r]H_before,7|^(1/r)=2,                              (5.2)

whereas the after-source has coefficient root-limsup sqrt(2).
The two actual degreewise algebras have identical generic fibres; their
order of extension changes the full Euler Taylor radius.

Over F49 the after completion has local form H_2 times
(1-4z^2)^(-7/2) times a nonzero holomorphic function. The second line
of (4.3) therefore gives leading exponent m-29/6, where m is the finite
integer zero order of H_2 at z=1/2. It is again nonintegral. Thus the
before-source also has exact radius1/2 over F49, but its local branch
is changed by ramification. No uncomputed claim that m=0 is needed.

## 6. A precise scalar base-change falsifier

Ordinary sheaf operations and their degreewise comparison commute with
constant-field extension. That classical fact does not impose the
naive scalar norm identity on these nonlinear boundary Hilbert ratios.
Indeed the finite low-grade sources already show

    Xi_7(z)=1+13z^4+O(z^5),
    Xi_49(z)=1+12z^3+13z^4+O(z^5).

The old rational plus/minus degree-three terms cancel over F7; the
quadratic branch starts only in degree six. Infinity supplies13z^4.
Over F49 the four positive rational old branches supply12z^3.
It follows that Xi_49(z^2) is not Xi_7(z)^2: their degree-four
coefficients are0 and26. This is compatible with the exact pure
cohomological-ladder identity K_49,N(z^2)=K_7,N(z)^2. The two scalar
operations are different even though each is induced by honest sources.

The result does not assert a universal failure of arithmetic base change,
does not replace an ordinary L-function by a Hilbert factor, and does
not claim any infinite continuation beyond the explicit domains proved
here. It isolates the effect of full boundary invariants on a specified
actual infinite graded source.

## 7. Explicit bounds for a small exact replay

The companion replay never expands a high-dimensional generator space.
It uses literal low-grade eigenmonomials for the source comparison and
integer character recursions for the subsequent finite products. At
x=1/4 it encloses the logarithms of the analytic units, rather than
trying to evaluate the divergent V or X infinite products.

The estimates above imply, for j>=1,

    |e_j| <= 2^j/(3j),
    |f_j| <= 2*2^j/(3j)+4/3,
    0<=a_(2j),C_(2j)<=4^j/j.

For 0<=y<=1/4, the logarithm remainders satisfy

    0<=-log(1-y)-y <= y^2/[2(1-y)],
    |log(1+y)-y| <= y^2/2,
    |log(1+y+y^2)-y| <= 2y^2.

Let q=2x and v=4x^2. Truncation after j=J bounds the linear error tails by

    E_b = q^(J+1)/[3(J+1)(1-q)],
    E_c = 2E_b + 4x^(J+1)/[3(1-x)],

and a common conservative quadratic tail by

    E_quad = 4v^(J+1)/[(J+1)(1-v)].

Thus the log A_V and log A_W error is at most E_b+E_quad;
for log A_X it is at most 2E_c+E_quad; and for log A_Y it is at most
E_c+E_quad. These estimates hold at x=1/4 and prove the enclosures
used in the finite-generator critical calibration. Ordinary rational
atanh-series remainders enclose each finite logarithm. No numerical fit
or finite table is used to infer a convergence radius or a branch exponent.
