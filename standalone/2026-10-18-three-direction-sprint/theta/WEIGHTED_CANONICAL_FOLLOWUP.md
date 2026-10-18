# Weighted canonical products: the surviving all-order gate

**Conditional consumer and research assessment. No all-order positivity,
RH, or improved zero-free region is proved.** This note credits repository
PR #1003, exact head `669b6a01f4d4858ae1ef806b07547be95c08c935`,
`standalone/2026-10-18-theta26-and-critical-family/theta/WEIGHTED_CANONICAL.md`
and its `extension/POWER_SUM_EXTENSION.md`. The weighted half-plane
construction genuinely escapes the positive-density transfer architectures
excluded in this sprint: its finite approximants need not be characteristic
functions, entire functions, or products with integer multiplicities.

## 1. The exact remaining target

In the source normalization, write

    H(z)=xi(1/2+i z/sqrt(v))/xi(1/2),
    log H(z)=-z^2/2-sum_(r>=2) Q_r z^(2r)/r.

The source proves that finite positive nodes and positive weights satisfying
`sum_j lambda_j b_j^r=Q_r` for `2<=r<=M`, at unbounded M, imply RH.
Its half-plane logarithm and global imaginary-axis remainder avoid the
need for a common Taylor disk of the finite approximants. The single
matched coefficient Q_2 controls their common quartic envelope.

The following simplification uses an extra property of the actual theta
target: `H(it)>0` for every real t, since it is the moment generating
function of its positive symmetric theta law. Thus only one family of
Hankel positivity tests is necessary in an all-order proof.

## 2. A single-Hankel-family consumer

**Theorem.** Let H be even, real entire, with H(0)=1, H''(0)=-1 and
`H(it)>0` for every real t. Define Q_r by the local logarithm above.
If

    [Q_(i+j+2)]_(i,j=0)^N is positive semidefinite for every N>=0,  (1)

then every zero of H is real. In particular, (1) for the actual theta
coefficients implies RH. No separately shifted Hankel assumption is needed.

**Proof.** Put `s_k=Q_(k+2)`. The classical Hamburger moment theorem gives
a positive finite measure nu on the real line with

    s_k=integral t^k dnu(t), k>=0.                              (2)

The exact imported theorem is Schmuedgen, *The Moment Problem* (2017),
Theorem 3.8, including positive semidefinite and degenerate cases; its
statement and proof were read in the [full primary monograph]
(https://www.imath.kiev.ua/~golub/ref2/The-Moment-Problem.pdf), printed
pages 64--65. The Hankel condition (1) is exactly its hypothesis.

Write `H(z)=F(z^2)` with F entire and F(0)=1. Cauchy's estimate on a
zero-free disk of F bounds `|s_k|<=C A^k`, after increasing positive
constants C,A if necessary. The measure in (2) has support in [-A,A]:
positive mass where `|t|>=A+epsilon` would make its even moments exceed
`C A^(2n)` as n tends to infinity. The zero-measure case is harmless.

For sufficiently small w, geometric expansion now gives

    -F'(w)/F(w)=1/2+w integral dnu(t)/(1-tw).                  (3)

The right side is holomorphic on

    Omega=C minus ((-infinity,-1/A] union [1/A,infinity)).

This connected domain contains a disk about zero and every nonreal
number. Meromorphic continuation of (3) by the identity theorem shows
that F has no zero in Omega: a zero would give its logarithmic derivative
a nonzero integer residue, whereas the right side is holomorphic there.
Consequently every zero of F is real. If w<0, however,
`F(w)=H(i sqrt(-w))>0`; also F(0)=1. Hence all zeros of F are positive,
and their square roots give only real zeros of H. QED.

The proof also shows why the extra imaginary-axis positivity matters.
Without it, the same Hamburger argument permits imaginary zeros of H;
the independently shifted Stieltjes positivity condition excludes those
in the more general source consumer.

For the actual theta function the converse is classical as well. Under
RH its paired order-one Hadamard product has positive real zeros a_j,
and `Q_r=sum_j a_j^(-2r)` for r>=2. Thus
`nu=sum_j a_j^(-4) delta_(a_j^(-2))` makes (1) positive semidefinite.
This is an exact reformulation, in the classical Grommer/moment-criterion
tradition, rather than a reduction of the known difficulty of RH.

## 3. What would count as a completion

A successful analytic argument must prove, for every real polynomial p,

    sum_(i,j) p_i p_j Q_(i+j+2) >= 0.                        (4)

A source-derived positive integral for this complete quadratic form, or a
positive Jacobi operator whose actual spectral moments equal these Q_r,
would satisfy the missing all-order gate. A finite list of positive
matrices, coefficient signs, or an extension trajectory without a
uniform continuation theorem does not establish (4).

The coefficients here are logarithmic coefficients (even cumulants),
not the raw moments of the positive theta density. Positivity of the
original density therefore supplies the usual raw-moment Hankel forms,
not (4). The known convexity or GHS information does not, by itself,
produce a positive representation of this new quadratic form. The
actual missing estimate has not been proved in this sprint.

This is nevertheless a useful surviving architecture: it removes several
unnecessary finite-model restrictions simultaneously and makes a single,
precise target for a possible all-order positivity proof. The classical
criterion is credited; no novelty or priority claim is made for it.
