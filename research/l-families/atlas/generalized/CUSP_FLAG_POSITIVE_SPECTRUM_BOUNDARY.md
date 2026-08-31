# Cusp-flag quotient: positive forms versus positive Laplace spectra

Status: PROPOSED SOURCE-STRUCTURAL THEOREM; independent frozen-SHA review required.
Scope: every fixed even level-one weight k with d=dim S_k>=2, the exact
first-coefficient flag of the frozen family, and the fixed uncompleted
normalizations below. No claim of a new Laplace-uniqueness principle.

Scientific dependency: 43ecb4ac3f2487ee944b6bb6bef72e1ad92f2678,
CUSP_FLAG_QUOTIENT_GLOBAL_FAMILY.md, especially CF1--CF12.
The manifest binds all five family files plus the earlier weight-24 audit
at 8e9f05211954e0a7aae5e63c9367f1d520d3671d. This packet does not edit either.
Classical modularity and the parent's analytic convergence proof are imported,
not machine-proved again. Remote reference bytes are not authenticated.

What was computed: exact rational first-atom/gap controls for all 138 parent
rows, exact finite Schur-envelope controls, and signed-exponential controls
with rational evaluation parameters. No actual period or high derivative of
a cusp quotient is numerically sampled or certified.

Smallest unpaid quantitative issue: a certified numerical absolute tail mass
at a specified right abscissa, needed for an explicit numerical derivative
order witnessing the actual cusp quotient. The qualitative theorem is complete
without such a certificate.

## 1. Fix the variable and preserve the source

Write k=12d+r, r in {0,4,6,8,10,14}, N=d+1. Use exactly the integral Miller
basis f_1,...,f_d of CF1, ell(f)=[q]f, W=ker ell, and coefficients
c_n=[q^n]f_1, b_j(n)=[q^n]f_j. Put

    w=s+k-1,
    mathcal F_k(w)=D_11(w)-D_1W(w)D_W(w)^(-1)D_W1(w),
    mathcal L_k(w)=zeta(2w-2k+2) mathcal F_k(w),
    Q_k(s)=A_k(s) mathcal L_k(s+k-1),                         (PS1)

where D_ij(w)=sum_n a_i(n)a_j(n)n^(-w), and

    A_k(s)=pi^(-s)Gamma(s)(4pi)^(-s-k+1)Gamma(s+k-1).

Every derivative below is with respect to the real variable w. These are
the parent's F and L, reparametrized explicitly, not changed by an arbitrary
factor. Their continuation is meromorphic; the half-line w>k corresponds
exactly to real s>1, where D is positive definite and has no denominator zero.
The completed Q retains its reflection but is NOT assigned the monotonicity
or Laplace claims below.

For real w>k the parent variational identity gives

    mathcal F_k(w)=min_(ell(f)=1) sum_n |a_n(f)|^2 n^(-w).    (PS2)

The minimizer f_w is unique and real in the real coefficient basis, although
the minimum may equivalently be taken over complex forms. The canonical flag
is unchanged by constant complex adapted basis changes.

## 2. Strict positivity and the exact envelope

All coefficient sums and any fixed number of their derivatives converge
locally uniformly on w>k. Indeed choose k<w_-<w in a compact neighborhood;
the parent gives absolute convergence at w_-, and each factor (log n)^h
is bounded after multiplication by n^(-(w-w_-)). Cauchy--Schwarz handles
cross sums. Thus the inverse D_W and the minimizer coordinates are smooth.

Set y=-D_W^(-1)D_W1, a=(1,y)^t, and H=D_W. A prime denotes a w derivative.
The stationarity equation (Da)_W=0 gives

    a'_1=0,   y'=-H^(-1)(D'a)_W.
    mathcal F'=a^*D'a
       =-sum_(n>=2) (log n)|a_n(f_w)|^2 n^(-w).              (PS3)

The terms arising from differentiating a vanish by stationarity, not by
assuming that the minimizer is constant. Its first coefficient contributes
exactly one, so

    mathcal F_k(w)>1,   mathcal F'_k(w)<0,   F_k(+infinity)=1. (PS4)

For strictness, equality in either of the first two assertions would force
f_w(z)=q. This is not a modular form: at z=iy the absolute-value transformation
under z -> -1/z would require exp(-2pi/y)=y^k exp(-2pi y), impossible as
y tends to infinity. The limit follows from 1<=mathcal F<=D_11 and dominated
convergence at a fixed w_->k. Since zeta(2w-2k+2)>1 is strictly decreasing
to one, mathcal L also is >1, strictly decreasing, and tends to one.

The exact curvature is

    mathcal F''=a^*D''a-2 g^*H^(-1)g,   g=(D'a)_W.          (PS5)

To prove this, differentiate PS3, use y'=-H^(-1)g and the Hermitian symmetry
of D' on the real line. In particular the factor is TWO. The second term
is nonnegative and measures the loss caused by optimizing the coefficients.

A geometric equivalent makes the sign issue transparent. In ordinary l^2
put v_n=n^(-w/2)a_n(f_w), let U have columns n^(-w/2)b_j(n), and let P be
orthogonal projection onto ran U. With X=diag(log n), stationarity gives
U^*v=0 and all displayed vectors belong to the required square-summable
domains. Then

    F''=||Xv||^2-2||PXv||^2
       =||(1-P)Xv||^2-||PXv||^2.                            (PS6)

Neither this formula nor positivity of the parent matrix proves convexity
of the scalar. No actual cusp-family claim F''<0 is made here.

### Exact finite calibration, not a cusp-form counterexample

Take positive Laplace atoms with rates 0,1,10 and vectors
(1,0),(0,1),(1,3), with positive prefactors 1,2,1024. Their sum is a
positive-definite matrix for every real w, and each alternating matrix
derivative is positive semidefinite. At w=log 2 the tilted weights all
equal one. Its scalar quotient is

    F_toy(w)=1+1/(2^(-10) exp(10w)+9*2^(-1) exp(w)).
    F_toy(log 2)=11/10,
    F_toy'(log 2)=-19/100,
    F_toy''(log 2)=-46/125.                                 (PS7)

Here a=(1,-3/10), a^*D''a=109/100, g=-27/10, H=10, so the curvature
correction is 729/500. This checks the mechanism and factor in PS5.
The rates are natural exponential rates, not log-frequency rates of an
actual cusp source; the finite calibration is not passed off as native.

## 3. The inherited negative atom

The parent's normally absolutely convergent generalized Dirichlet expansion
on a sufficiently right half-plane has locally finite rational frequencies
rho>=1. Combine all equal frequencies before calling a coefficient an atom.
Let rho_* be the first fractional frequency and a_* its coefficient:

    rho_* = N^2/d,          a_*=-c_N^2 b_d(N)^2<0,
                  except at k=124,248;
    rho_* = N^2/(d-1),      a_*=-c_N^2 b_(d-1)(N)^2<0
                  at k=124,248.                            (PS8)

The exceptional pivots are 169884 and 142884, respectively; the zero top
pivot is retained. The all-weight nonvanishing and the true least-frequency
proof are imported from CF5--CF12, not inferred from the 138 finite rows.
The same a_* occurs in mathcal L: multiplication by zeta only adds square
integer factors, so no smaller integer frequency can become rho_*.

Write either f=mathcal F_k or f=mathcal L_k as

    f(w)=sum_x a_x exp(-wx),    x=log rho>=0,
    A(w_0)=sum_x |a_x| exp(-w_0 x)<infinity.                 (PS9)

Choose one fixed w_0 sufficiently far right, in the absolute convergence
domain for the chosen f; x_*=log rho_*>0. Such a w_0 is available at every
fixed weight. No common w_0 for varying k is asserted.

## 4. A moving-order derivative extracts the negative atom

For m>=1 set w_m=w_0+m/x_*. Differentiate the function first, then evaluate
the m-th derivative at w_m; this is NOT a derivative of the sampled sequence.
Absolute convergence at w_0 justifies any fixed derivative at w_m>w_0,
because x^m exp(-(w_m-w_0)x) is bounded on x>=0. Exactly,

    R_m := (-1)^m f^(m)(w_m) /
                    (x_*^m exp(-w_m x_*))
         =sum_x a_x exp(-w_0(x-x_*)) psi(x/x_*)^m,
    psi(t)=t exp(1-t),   0<=psi(t)<=1.                      (PS10)

For t>0, log psi(t)=log t+1-t<=0, with equality only at t=1.
The constant atom x=0 contributes zero when m>=1. The summands in PS10
are dominated in absolute value by the summable mass
exp(w_0 x_*)|a_x|exp(-w_0 x). Dominated convergence therefore proves

    lim_(m->infinity) R_m=a_*<0.                            (PS11)

Only the negative atom and absolute tilted mass are needed for this limit.
Isolation is not needed for dominated convergence, but gives an exponential
error estimate. Local finiteness supplies an open gap around x_*. Since
psi is increasing below 1, decreasing above 1, and tends to zero at both
ends, there is

    q_*=sup_(x!=x_*, a_x!=0) psi(x/x_*)<1,
    |R_m-a_*| <= exp(w_0 x_*) A_rest(w_0) q_*^m,            (PS12)

where A_rest omits the target atom. An empty supremum can be set to zero.
Consequently every sufficiently large integer m has
(-1)^m f^(m)(w_m)<0, with w_m tending to infinity.

If a certified upper bound M>=A_rest(w_0) is supplied, the explicit sufficient
condition exp(w_0 x_*)M q_*^m<|a_*|/2 gives a negative derivative margin.
The packet does NOT supply a numerical actual-cusp M or a numerical onset.
An available analytic majorant for F is the parent's
B(w_0)+(d-1)||x_abs(w_0)||_infinity^2/(1-eta), eta<1; multiplying by
zeta(2w_0-2k+2) bounds L. Its existence is not a certified numerical evaluation.

### Optional explicit atom gap, without evaluating logarithms

Let p=floor rho_*. There is no other frequency in (p,p+1) for either f.
For a nonexceptional weight p=d+2. The smallest possible non-first correction
is bounded below by the minimum of

    N(N+1)/d, N^2/(d-1) (when d>=3), N^3/d^2,

each greater than d+3. These cover, respectively, another endpoint index,
another pivot, or inverse depth at least one. Integer frequencies in B cause
no difficulty. For the two exceptions p=d+3; the corresponding non-first
possibilities are bounded below by

    N(N+1)/(d-1), (N+1)^2/d, N^2/(d-2), rho_* N/d,

each greater than d+4. These cover the active pivot, the zero top pivot with
its next endpoint, a smaller pivot, and positive inverse depth. Multiplication
by a square >=4 cannot put any term between p and p+1: lower frequencies
were integers and the first fractional frequency is rho_*.

Thus PS12 may use the explicit upper bound

    q <= max{psi(log p/log rho_*),
             psi(log(p+1)/log rho_*)}<1.                   (PS13)

Zero coefficients or cancellations can only improve this support enclosure.
These rational frequency inequalities are the bounded gap controls;
the analytic logarithms/exponentials are not represented as exact rationals.

## 5. The quantifiers matter

The first nonconstant atom of F has frequency N, coefficient c_N^2>0.
Its first correction lies strictly after N. For L the first nonconstant
frequency and coefficient are

    N<4:  frequency N, coefficient c_N^2;
    N=4:  frequency 4, coefficient c_N^2+2^(2k-2);
    N>4:  frequency 4, coefficient 2^(2k-2).                (PS14)

Every later frequency is separated from this leading positive atom by local
finiteness. For each FIXED derivative order h>=1, termwise differentiation
followed by leading-atom domination gives

    (-1)^h f^(h)(w)
        ~ a_lead (log rho_lead)^h rho_lead^(-w)>0
                    as real w->infinity.                  (PS15)

For rigor, first shift from the absolute abscissa w_0 to w_1>w_0 so the
log^h-weighted absolute mass is finite; then dominated convergence after
division by the leading exponential proves the asymptotic. The case h=0
is f(w)->1>0. For any fixed finite H, taking the maximum of the finitely
many thresholds proves the correct signs for all 0<=h<=H on a common tail.

But PS11 says that for every right half-line (R,infinity), some derivative
order and some w>R have the wrong sign; indeed all sufficiently large m
work along w_m. Therefore neither F nor L is completely monotone on ANY
right half-line. One cannot interchange
"for every finite order, there exists a tail" with
"there exists a tail working for every order."

Any positive Borel Laplace representation on [0,infinity) in this fixed
variable, finite on a right half-line, would have alternating derivatives
of every order there (differentiate at an interior point using an earlier
convergence abscissa). Thus such a representation is excluded. This includes
positive self-adjoint semigroup scalar representations
<f,exp(-wH)f>, H>=0, when their spectral integral has that convergence domain.
It does NOT exclude signed spectra, different transforms or variables,
w-dependent vectors, renormalizations, or every possible spectral construction.

The parent's positive automorphic integral is untouched: PS2 minimizes a
different vector at different w. Positivity of that variational value does
not supply one fixed positive scalar Laplace measure. No statement about
Weil positivity, an RH/GRH criterion, or a Riemann zero distribution follows.

## 6. Bounded exact controls and classical boundary

The producer authenticates all six Git bindings before using the frozen
family fixture. It does not rerun the parent's q-basis producer. It verifies
the first negative coefficient/pivot, the positive leading coefficient,
and all rational gap inequalities for every one of its 138 rows. Those
rows are controls for, not proofs of, the all-weight statements.

Finite Schur controls use explicitly declared real rational Gram atoms,
not a fabricated cusp-source decoder. Exact matrix inversion and moments
check PS3/PS5 and a separately parameterized rational Schur differentiation
checks PS7 in the tests.

A second finite signed-exponential calibration is

    h(w)=1+2 exp(-w)-exp(-2w)+exp(-3w).

It is >1 and strictly decreasing for w>0: with t=exp(-w),
h-1=t[(t-1/2)^2+7/4] and -h'=t[3(t-1/3)^2+5/3].
At w_m=m log(5/3),

    (-1)^m h^(m)(w_m)/(18/25)^m
                  =2(5/6)^m-1+(9/10)^m -> -1.

The eighth-order value is already strictly negative, by rational arithmetic.
This is an independent algebra calibration, not the actual-cusp onset in PS11.

Public caps are dimension<=24, finite matrix dimension<=4, atoms<=8,
derivative order<=32, integer toy rates<=32, primitive rational bits<=32,
internal rational bits<=4096, and 200000 charged loop/arithmetic units.
Charges precede declared expansions; this is not an interpreter instruction
count, wall-clock bound, or a denial-of-service guarantee for arbitrary JSON.
Duplicate/nonfinite JSON, schema/type drift (bool is not int), source drift,
artifact drift and cap violations fail closed. Full typed canonical report
reconstruction is the acceptance rule. No floating arithmetic is used.

The envelope, Schur complement and positive-Laplace uniqueness principles
are classical. A directly relevant primary account is
[Salazar, Determinacy Witnesses in the Completely Monotone--Stieltjes--Bernstein
Hierarchy, Proposition 2.3 and its proof](https://arxiv.org/html/2607.09868v1#S2):
a signed tilted Laplace measure is unique, and a negative atom obstructs a
positive representation. That paper expressly identifies the abstract
implication as elementary/classical. This packet gives its own derivative
proof PS10--PS12 and imports no result unique to that preprint.
For the classical source context see
[Schilling--Song--Vondracek, Bernstein Functions, author's book page](https://www.motapa.de/bernstein_functions/)
and the references to Bernstein/Widder in the primary account.
No claim is made that atom extraction or Schur-envelope differentiation is new.

The additional content is the source-specific simultaneous theorem:
a canonical automorphic quotient is strictly positive and decreasing,
every fixed-order derivative test eventually passes, yet the explicit
negative fractional atom forces wrong signs at moving orders arbitrarily
far right, in every weight covered by the parent, including both exceptions.

Replay from the repository root:

    python -B -m unittest discover -s tests -p test_cusp_flag_positive_spectrum_boundary.py
    python -B -O -m unittest discover -s tests -p test_cusp_flag_positive_spectrum_boundary.py
    python -B research/l-families/atlas/generalized/cusp_flag_positive_spectrum_boundary.py --check
    python -B -O research/l-families/atlas/generalized/cusp_flag_positive_spectrum_boundary.py --check

Ruff and the complete authoring-base-to-head whitespace check are separate
nonmathematical gates. Finite replay does not certify the analytic proof,
actual tail masses, or an effective numerical onset.
