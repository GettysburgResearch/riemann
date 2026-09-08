# Signed gluing of separated windows, including actual prime-shift cusps

Status: PROPOSED COMPLETE COMPONENT PROOFS; independent mathematical/code review
required. The original coefficient bound, full-source positivity, and RH remain
UNPROVED. No external priority claim.
Scope: the literal operator of PR #792; an explicit union of six intervals;
all complex L2 functions supported there; a general finite-window gluing lemma.
Exact parent: #792 at 2c3184545bafb4f5d873d2fa0ffc2c335a25d048,
local-window-positivity/PROOF.md, blob 8d7120ef2edc0ac033a4814eb61917652fc57ba8.
What was run: rational interval source evaluation, a six-dimensional signed
matrix certificate, and exact polynomial/jump integration controls. No zero
input, prime sweep, or sample of L2 functions is used to infer positivity.
Smallest unpaid step: a cofinal sign estimate for the complete center matrices,
or another estimate controlling all long-range interactions.
Local labels SW-1 through SW-3 have no canonical-registry status.

## 1. Same full source, not six independent local tests

Set a=3/4, b=3/2 and retain exactly the full arithmetic kernel

    T(t,u)=b exp(-a(t+u)) W(t-u),  t,u>=0.

For x>=0 the parent gives the exact local formula

    W(x)=exp(x/2)/2+C_b exp(-bx)+S_gamma(x)
          -(P2/b)cosh(bx)
          +(1/b)sum_(2<=n<=exp x) q_n sinh(b(x-log n)),      (1)
    C_b=(1-gamma_E-log(2pi))/3,
    P2=-zeta'(2)/zeta(2)=sum_(n>=2)Lambda(n)n^-2,
    q_n=Lambda(n)/sqrt(n),
    S_gamma(x)=sum_(j>=1) exp(-(2j+1/2)x)/((2j+1/2)^2-b^2).

W is extended evenly. The sinh term is zero at its endpoint. All prime
powers, including the unbounded tail, are retained: that tail is already
included in the safe scalar P2. This is not the raw arithmetic cutoff.

Our explicit support set is

    ell=1/1000,
    I_j=[log j, log j+ell],  j=1,...,6,
    U=union_(j=1)^6 I_j.                                   (2)

These intervals are disjoint. Their convex hull has length log(6)+ell;
the theorem does NOT assert positivity for all functions on that hull.

**SW-1 (six-window full-source positivity).** For every nonzero complex
f in L2(0,infinity) supported in U, let

    h_j(s)=exp(-a(log j+s)) f(log j+s),  0<=s<=ell,
    M_j=int_0^ell h_j(s) ds,
    G_j(s)=int_0^s h_j(t)dt-M_j/2.

Then

    <f,Tf> >= (81/6400)sum_j |M_j|^2
                +(69/40)sum_j int_0^ell |G_j(s)|^2 ds >0.  (3)

The same result holds for every simultaneous translation of the six
intervals into the positive half-line, using the translated damping in h_j.
This is a primitive-norm lower bound, NOT a uniform L2 spectral gap.
A compact positive operator can have eigenvalues tending to zero.

The interaction cells centered at log 2, log 3, log 4 and log 5 contain
actual prime-power derivative jumps. The proof keeps those jumps with their
exact signs and weights, rather than assuming all cross kernels are smooth.

## 2. The regular curvature and the prime atoms

On any compact subinterval of (0,infinity), W' is bounded between finitely
many jumps, and distributionally

    W'' = R(x) dx + sum_(n>=2) q_n delta_(log n),
    R(x)=b^2 W(x)-exp(x/2)
                    +exp(-5x/2)/(1-exp(-2x)).              (4)

To verify (4), apply D^2-b^2 to (1). The growing exponential contributes
-exp(x/2), each gamma summand contributes exp(-(2j+1/2)x), and the P2
cosh term contributes zero. At a prime-power knot, differentiating the
causal sinh gives the derivative jump q_n. The geometric sum of the gamma
contributions is the last term in R. All differentiations away from zero
are justified by normal convergence. W itself is continuous at each knot.

At negative knots the even extension has the same positive jump in W'.
The singularity at zero is not used in cross-window integration: all such
windows have positive separation. Within a single window we use the exact
positive local factorization from the parent, including its treatment of
W''(x)=O(1/x) as x decreases to zero.

## 3. SW-2: a general signed gluing theorem

Take distinct centers x_1,...,x_r with |x_i-x_j|>ell. Suppose
0<ell<=1/20. Put

    p=-W'(ell),
    A_ell=W(ell)+(ell/2)p.

The parent gives p>0, W(ell)>0 and positive curvature on (0,ell].
For h_j supported in [0,ell], define M_j,G_j as above without damping.
The parent triangle factorization gives the diagonal lower bound

    int int W(s-t) conjugate(h_j(s))h_j(t) ds dt
       >= A_ell |M_j|^2+2p ||G_j||_2^2.                   (5)

No lower bound of this form for off-diagonal blocks is being assumed.

For i!=j, put d_ij=x_i-x_j and J_ij=[|d_ij|-ell,|d_ij|+ell]. Define

    C_ii=A_ell,
    C_ij=[W(d_ij-ell)+2W(d_ij)+W(d_ij+ell)]/4,             (6)
    D_ij=ess sup_(x in J_ij) |W'(x)|,
    B_ij=ell sup_(x in J_ij)|R(x)|
                         +sum_(n: log n in J_ij) q_n.     (7)

Take D_ii=B_ii=0. Endpoints may be included in the jump sum to make a
conservative bound; an isolated endpoint on a corner changes no integral.
All three matrices are symmetric. Let

    d_*=max_i sum_(j!=i) D_ij,
    beta_*=max_i sum_(j!=i) B_ij,
    c=2p-beta_*.

**Gluing assertion.** If C>=lambda I with lambda>0, c>0, and

    lambda*c > ell*d_*^2,                                 (8)

then the W quadratic form is strictly positive on every nonzero L2 function
supported in the union of these intervals. More precisely, for any theta
with 0<theta<c,

    Q_W(h) >= (lambda-ell*d_*^2/theta)sum_i |M_i|^2
                   +(c-theta)sum_i ||G_i||_2^2.            (9)

Whenever the first displayed coefficient is positive, (9) is a quantitative
strict bound. Equation (8) guarantees a choice of theta with that property.
It is an inequality for the entire infinite-dimensional support class.

### 3.1 Exact endpoint/primitive decomposition

Extend G_j by zero outside (0,ell). As distributions on the real line,

    h_j(s)ds=(M_j/2)(delta_0+delta_ell)+D G_j.              (10)

Indeed G_j(0+)=-M_j/2 and G_j(ell-)=M_j/2, so both boundary jumps in its
zero extension are -M_j/2. Omitting either endpoint gives a wrong formula.

For the cross kernel W(d_ij+s-t), substitute (10) in both variables.
The mass term is exactly conjugate(M_i)M_j C_ij. If

    a_ij(t)=[W'(d_ij-t)+W'(d_ij+ell-t)]/2,

the mixed terms, summed over all ordered pairs, are

    2 Re sum_(i!=j) conjugate(M_i) int_0^ell a_ij(t)G_j(t)dt. (11)

The remaining terms are

    -sum_(i!=j) int int conjugate(G_i(s))G_j(t)
                                      W''(d_ij+s-t)dsdt.   (12)

The minus sign follows from partial_s partial_t W(d+s-t)=-W''(d+s-t).
The atom at d+s-t=log n in (12) is a signed overlap integral, not a
pointwise value to be discarded. Its absolute value is bounded by
q_n ||G_i||_2 ||G_j||_2 via Cauchy--Schwarz on the translated overlap.
The regular part has absolute value at most
ell sup|R| ||G_i||_2 ||G_j||_2. This proves the bound B_ij in (7).

For rigor, integration by parts can first be performed with piecewise
smooth functions and the finitely many knot cells separated. Continuity of
W, its bounded one-sided W' on the cross cell, and its finite curvature
measure there give precisely (10)--(12). Approximation in L2 then passes
to general h_j: primitives converge in H1, and every term is bounded by
these stated norms. No distribution at the zero singularity is introduced.

### 3.2 Operator bounds and completion of squares

Since ||a_ij||_2<=sqrt(ell)D_ij, (11) has absolute value at most

    2 sqrt(ell) d_* ||M||_(Euclidean) ||G||_(direct-sum L2).

For example, apply Cauchy--Schwarz to the matrix with nonnegative entries
D_ij; its l2 operator norm is at most its maximum row sum because it is
symmetric. The same argument with B bounds the absolute value of (12) by
beta_*||G||^2. There is no missing factor two: the matrices and the sums
already include both orientations of every cross pair.

Combining with (5) gives

    Q_W(h)>=lambda||M||^2-2sqrt(ell)d_*||M||||G||+c||G||^2. (13)

Young's inequality with parameter theta proves (9). If M=0 and G=0 then
h_j=G_j'=0 for every j. Thus a strictly positive lower bound on these two
norms is genuinely strict for every nonzero h. This proves SW-2.

## 4. Complete arithmetic certificate for the six intervals

At ell=1/1000 and x_j=log j, the checker proves the following strict bounds
by exact rational outward intervals:

    p>11/5,
    C-(1/100)I is positive definite,
    d_*<5/4,
    beta_*<9/4.                                            (14)

The six LDL pivots of C-(1/100)I have approximate values

    0.0344209892176422,
    0.0259225602083954,
    0.0210185712787491,
    0.0194084269894463,
    0.0140210208965130,
    0.0060156397998575.

These decimals are orientation only. Acceptance uses the rational endpoint
intervals in result.json, each recomputed from source. Other upper bounds
are approximately d_*<=1.244099 and beta_*<=2.200386, and p>=2.247981.

There is actual signed matrix cancellation: in the first row the sum of
the absolute off-diagonal entries is greater than 7/100, while its diagonal
is less than 9/200. Absolute diagonal dominance cannot prove its positivity.
The LDL calculation retains the signs of the complete matrix.

Now c>2(11/5)-9/4=43/20. Set theta=1 in (9). Since

    ell(5/4)^2=1/640,
    1/100-1/640=27/3200,
    43/20-1=23/20,

we obtain

    Q_W(h)>=(27/3200)sum_j |M_j|^2+(23/20)sum_j ||G_j||^2.

The original damped T form equals b Q_W(h). Multiplication by 3/2 proves
SW-1, including the constants 81/6400 and 69/40 in (3).

### 4.1 Which arithmetic enters the certificate

Every positive cross separation is below log 7 because 6exp(ell)<7.
Consequently (1) needs only n=2,3,4,5 in its finite sum; Lambda(6)=0.
The tail at n>=7 has NOT been discarded: it is part of P2. The weights are

    q_2=log2/sqrt2, q_3=log3/sqrt3,
    q_4=log2/2,     q_5=log5/sqrt5.

Each cross cell centered at log(i/j) is checked against every such knot.
It contains a knot precisely when i/j is one of these integer prime powers.
The ratio 6 is not a prime-power knot. The interval widths and this finite
coverage are certified rather than inferred from rounded logarithms.

For x>0, with v=exp(-x), the exact gamma formulas used are

    S_gamma(x)=[exp(-bx)log((1+v)/(1-v))
                  +exp(bx)log(1-v^2)+exp(-x/2)]/6,
    S_gamma'(x)=[-exp(-bx)log((1+v)/(1-v))
                  +exp(bx)log(1-v^2)+exp(-x/2)]/4.          (15)

They are the parent's normally convergent logarithm-series identities.
The source enclosure recomputes P2 and C_b with the parent's rational
Euler--Maclaurin/Cauchy/logarithm/arctangent contract. The imported code is
loaded only after its literal Git blob and the parent proof blob match.
No parent result file or saved decimal constant is trusted as source data.
The result file exports intervals rounded further OUTWARD to a 10^-12 grid
for readability; every mathematical threshold is checked before that export.

Every exponential and logarithm operation rounds outward to the parent's
rational grid 10^-40. Exponentials at interval arguments use monotonicity.
Square-root endpoints for q_n are obtained by integer square roots at that
grid, with explicit floor/ceiling inequalities.

At a knot-crossing interval, the causal sinh value is enclosed using its
positive part. Its derivative includes the whole interval from zero to the
positive cosh maximum; both one-sided limits are covered. Bounds for R use
(4), not an erroneously smooth second derivative across the knot. Every
q_n whose knot crosses the cell is added separately in beta_*.

## 5. SW-3: what finite positivity can and cannot propagate

For ANY fixed finite set of distinct centers, suppose the sample matrix

    K=[W(x_i-x_j)]_(i,j=1)^r

is strictly positive definite. Then SW-2 proves positivity for ALL L2 tests
on the union of sufficiently narrow equal intervals at those centers.
This statement allows prime-knot differences between centers.

Proof: as ell decreases to zero, C in (6) tends to K, since W is continuous
and ell*p tends to zero. From (15),

    W'(ell)=(1/2)log ell+O(1),
    p=(1/2)log(1/ell)+O(1) -> infinity.

At the fixed nonzero cross separations, D_ij and R stay bounded, and the
finitely many jump masses stay bounded. Thus d_* and beta_* stay bounded,
c->infinity, and ell*d_*^2->0. A fixed positive eigenvalue lower bound for
K then makes (8) hold for all sufficiently small ell. This proves the
assertion; it is not an effective uniform width over arbitrary center sets.

Conversely, if a finite sample matrix has a strictly negative quadratic
value at a vector v, take h_j=v_j/ell on each corresponding short interval.
Continuity and finite double integration give Q_W(h)->v*Kv<0 as ell->0.
Thus every sufficiently narrow version already has a negative L2 test.
The singular semidefinite boundary is not assigned either strict conclusion.

### The attempted global induction and its actual stopping point

One possible global center family is

    K_N=[W(log(i/j))]_(1<=i,j<=N).                           (16)

If every K_N is PSD, W is positive definite on all of R. Indeed, for any
finite set of real t_j, choose integers n_j(m) with n_j(m)/m->exp(t_j).
For all large m they are positive and distinct when the t_j are distinct.
The corresponding matrices are principal submatrices of K_(max n_j(m));
continuity makes them tend to [W(t_i-t_j)]. The closed PSD cone passes to
the limit. Repeated centers cause no extra difficulty by grouping weights.

Conversely global positive definiteness clearly gives every K_N PSD. By the
parent's source-exact operator/zero criterion this is equivalent to RH and
to the original subexponential coefficient target. This density argument
is a classical implication, NOT a newly proved arithmetic sign theorem.

The present six-center certificate supplies one instance of the finite
sample sign and, by SW-2, the entire neighboring function-space sign. It
does not provide an induction in N. In particular none of the following
would be valid: replacing the signed center matrix by its positive diagonal;
asserting a polynomial row-bound controls all Schur complements; or passing
from six intervals to their full convex hull. The tested mass matrix is not
even absolutely diagonally dominant. Its exact signs were used in (14).

A cofinal center-matrix lower bound, or a direct full-source sum of squares,
remains unpaid. This pass therefore proves genuine long-range interaction
control at one specified multi-window geometry, not global positivity.

## 6. Literature and verification boundaries

The general framework is classical Weil positivity and the resolvent/Hardy
construction already pinned in #792/#793. Triangle-mixture positivity,
primitive integration by parts, Schur-complement inequalities, and closedness
of the PSD cone are classical. No external novelty or record-window claim
is made. In particular a union of tiny separated intervals is not comparable
by its convex-hull length to a theorem for EVERY function on that hull.

For context, Suzuki, 'Aspects of the screw function corresponding to the
Riemann zeta-function', arXiv:2206.03682v4 (2023), and 'Weil's quadratic form
via the screw function', arXiv:2606.09096v2 (2026), study the surrounding
operator framework. Chuk, 'Weil positivity in compact windows',
arXiv:2608.24827v1 (2026), discusses full-window spectral certification.
These works were consulted for the boundary/overlap map, not used as proof
or numerical-certificate dependencies here. Their numerical claims were not
independently replayed. The branch #793 source compiler at 6d8a1d0c... was
also inspected for scope; no positivity is transferred from its eight-by-eight
matrix, whose metric and basis differ from this packet.

The finite checker authenticates the source arithmetic inequalities and
144 independent polynomial cross identities, including the minus sign and
overlap term of a derivative jump. It does not machine-prove integration
on arbitrary L2 functions, the parent's curvature theorem, or RH. The proof
and code require independent review before canonical integration.
