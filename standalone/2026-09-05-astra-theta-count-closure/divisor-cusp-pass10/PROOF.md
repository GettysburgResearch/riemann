# A divisor sum of squares controls all prime cusps in arbitrarily many windows

Status: PROPOSED COMPLETE COMPONENT PROOFS; independent mathematical review required.
RH, the unrestricted source sign, and the heat-Hankel lower bound remain OPEN.
Base: PR #790 at 8cc6fc78db37f42290c7372bc994b3bfa94898ef.
Cross-source: #792 at e5e3c2cb98c584af8edc06e148a92e52d91d1b4a,
separated-window-gluing/PROOF.md, blob d5dd18b62ef8fd9a19919914186e75e93146529f.
Local names DC-1 through DC-4 are not canonical claim identifiers.
No external novelty claim: the weighted graph sum of squares is elementary;
the use of its exact divisor diagonal in the full arithmetic cusp form is
what is being supplied here. There is no numerical zero or PNT input.

## 1. An exact arithmetic Laplacian, with all coefficient signs retained

Write Lambda for the ordinary von Mangoldt function, with Lambda(1)=0, and

    M(x)=sum_(2<=n<=x) Lambda(n)/n,       x>=1.

For N>=1 define the real symmetric matrix C_N by zero diagonal and

    (C_N)_(i,j)=Lambda(n)/sqrt(n) if i=n*j or j=n*i, n>=2,
                 0 otherwise.                            (1)

Only prime powers give edges. Put

    d_j=log j+M(N/j),     D_N=diag(d_j),     L_N=D_N-C_N.

**DC-1.** For vectors v_1,...,v_N in ANY complex Hilbert space,

    sum_j d_j ||v_j||^2 - <v,C_N v>
       =sum_(n>=2, nj<=N) Lambda(n)
                     ||v_(nj)-v_j/sqrt(n)||^2 >=0.         (2)

The quadratic form in (2) is real; both cross orientations are included.
In the scalar case ker L_N is exactly span{(1,1/sqrt(2),...,1/sqrt(N))}.
The same description holds with one arbitrary common Hilbert-space vector.

Proof. The squared first term contributes
sum_k ||v_k||^2 sum_(n|k) Lambda(n)=sum_k log k ||v_k||^2.
The squared second term contributes sum_j M(N/j)||v_j||^2. The cross term
is exactly minus the symmetric form in (1). Finally the identity
sum_(n|k) Lambda(n)=log k follows by prime factorization. Equality forces
v_(pj)=v_j/sqrt(p) on every prime edge. Repeated removal of prime factors
connects every vertex to 1 and proves the nullspace description. QED.

This is a positive graph Laplacian, NOT positivity of C_N itself and NOT
an identification of its determinant or spectrum with xi.

## 2. A logarithmic bound, without the prime number theorem

For all real x>=1,

    Psi(x):=sum_(n<=x) Lambda(n) <3x,
    log x-1<=M(x)<=log x+3.                               (3)

At x=1 these statements use the empty sum. To prove the first bound,
valuation of the central binomial coefficient gives, at integer k>=1,

    Psi(2k)-Psi(k)<=log binom(2k,k)<=2k log 2.

Every prime power in (k,2k] contributes one to the corresponding valuation,
and the other floor-difference contributions are nonnegative. Sum over
dyadic k. If 2^(a-1)<x<=2^a, then
Psi(x)<=Psi(2^a)<2^(a+1)log2<4x log2<3x, using log2<3/4.
At dyadic equality the same strict upper bound follows directly.

For the second assertion use the exact divisor identity

    sum_(n<=x) Lambda(n) floor(x/n)=log(floor(x)!).

Since floor(x/n)>=x/n-1,
x M(x)<=log(floor(x)!)+Psi(x)<=x log x+3x. For the lower bound,
at an integer k, k M(k)>=log(k!)>=k log k-k+1 by integral comparison.
For k<=x<k+1, log x<=log k+1/k, while M(x)=M(k). This proves (3).

**DC-2.** For every N and every Hilbert-valued vector v,

    <v,C_N v><=(log N+3)sum_j ||v_j||^2.                  (4)

Indeed d_j<=log j+log(N/j)+3=log N+3 and use (2).
For scalar vectors the spectral norm has the same bound, because C_N
has nonnegative entries and |v* C_N v|<=|v|^t C_N |v|.

The leading order is sharp. On v_j=j^(-1/2),

    (v* C_N v)/(v* v)
       =2 sum_(k<=N) (log k)/k / H_N,  H_N=sum_(k<=N)1/k. (5)

This follows by grouping k=nj and the same exact divisor identity.
Elementary sum-integral comparison gives
sum_(k<=N)log(k)/k=(log N)^2/2+O(1), H_N=log N+gamma_E+O(1/N).
Thus, as N tends to infinity,

    log N-gamma_E+O(1/log N)<=lambda_max(C_N)<=log N+3,
    lambda_max(C_N)=log N+O(1).                            (6)

The asymptotic statements are not numerical certificates. In contrast,
the first absolute row sum is sum_(n<=N)Lambda(n)/sqrt(n), which can be much
larger. Equations (2)--(4), not independent edgewise absolute row sums,
are the estimates used below.

## 3. The exact full source used for the application

This section uses the Hardy/Weil operator from PR #792, NOT an unannounced
identification with PR #790's heat-Hankel operator. Set a=3/4, b=3/2 and

    T(t,u)=b exp(-a(t+u)) W(t-u),      t,u>=0.              (7)

The complete arithmetic source, for x>=0, is

    W(x)=exp(x/2)/2+C_b exp(-b x)+S_gamma(x)
            -(P2/b)cosh(bx)
            +(1/b)sum_(2<=n<=exp x) Lambda(n)n^(-1/2)
                                             sinh(b(x-log n)),
    C_b=(1-gamma_E-log(2pi))/3,
    P2=-zeta'(2)/zeta(2)=sum_(n>=2)Lambda(n)n^-2,
    S_gamma(x)=sum_(j>=1)exp(-(2j+1/2)x)/((2j+1/2)^2-b^2). (8)

Extend W evenly. The full unbounded prime tail is retained in P2. It is
not replaced by a finite cutoff. The parent derives (8) from the safe
logarithmic derivative and proves the operator is self-adjoint trace class.
We import those source identities, not the parent's finite six-window sign.

On compact subintervals of (0,infinity), the exact distributional curvature is

    W''=R(x)dx+sum_n Lambda(n)n^(-1/2) delta_(log n),
    R(x)=(9/4)W(x)-exp(x/2)+exp(-5x/2)/(1-exp(-2x)).        (9)

Extend R evenly as well. At negative knots the jump weight is the same.
Away from zero, R is
continuous, including through prime knots. No delta mass is discarded.

For transparent global bounds we also use the unconditional representation

    W(x)=sum_z m_z exp(izx)/(b^2+z^2),                      (10)

over ALL distinct Xi zeros, with both signs, multiplicities m_z, and
|Im z|<1/2. There is no zero census in this input. With A=z^2+1/4 indexed
instead over upper ordinates, the source H=h(0) and the critical strip give

    Re A>1, (Im A)^2<=Re A, sum_A 1/Re A<1.

These source-only inequalities were proved in heat-hankel-pass5. In (10),
|b^2+z^2|=|A+2|>=Re A+2. Hence

    |W(x)|<2 exp(x/2),                 x>=0,
    |R(x)|<(11/2)exp(x/2)+1/(2x),      x>0.                (11)

The last gamma term in (9) is at most 1/(2x), since
exp(-5x/2)/(1-exp(-2x))=exp(-x/2)/(exp(2x)-1).
This use of unconditional xi theory does not assume line location,
simplicity, or the sign of T.

## 4. Complete local primitive coercivity

For 0<x<=1/64, no prime knot occurs. Equation (11) and

    exp(-5x/2)/(1-exp(-2x))>=1/(4x)

show R(x)>0: the positive term is at least 16 and the possible negative
part is less than 11. We used exp(-5x/2)>=1/2 and exp(x/2)<2.
Thus W is convex on (0,1/64].

Put p_ell=-W'(ell). For 0<ell<=1/64 we have the explicit bound

    p_ell>(1/2)log(1/ell)-3.                              (12)

Here are all constants. The exact logarithm-series derivative is

    S_gamma'(x)=[-exp(-3x/2)log((1+exp(-x))/(1-exp(-x)))
                 +exp(3x/2)log(1-exp(-2x))+exp(-x/2)]/4.

Use log((1+exp(-x))/(1-exp(-x)))>=log(1/x),
log(1-exp(-2x))<=log(2x)<0, and exp(-3x/2)>=1-3x/2.
Since x log(1/x)<=1/e<1/2 and log2<1,
S_gamma'(x)<(1/2)log x+11/16. The derivative of exp(x/2)/2 is less
than 1/2. Also |b C_b|<1, using 0<gamma_E<1 and log(2pi)<2.
The derivative of -(P2/b)cosh(bx) is nonpositive. Their sum is less
than (1/2)log x+3. This proves (12).

If h is a complex L2 function on [0,ell] with integral zero and
G(s)=int_0^s h(t)dt, then G has zero endpoints and

    int_0^ell int_0^ell W(s-t) conjugate(h(s))h(t) ds dt
                                      >=2p_ell ||G||_2^2. (13)

To justify even the singular endpoint at zero, the convex identity is

    W(v)=W(ell)+p_ell(ell-v)
                    +int_v^ell (u-v)W''(u)du, 0<=v<=ell.

Each kernel (u-|s-t|)_+ is positive definite, as the autocorrelation of
an interval indicator. Its contribution is nonnegative. The constant
term vanishes for zero mean; the triangle of width ell contributes
2||G||^2. The integral at v=0 converges because uW''(u) is bounded
near zero. For L2 tests the remaining triangle form is O(u^2)||h||^2,
so its product with W''(u)=O(1/u) is integrable. This proves the passage
to the full convex identity and (13), with no fictitious finite delta at 0.

## 5. Integer ratios identify the COMPLETE cusp graph

For N>=1 set

    ell_N=1/(2^20 N^2),
    I_j=[log j,log j+ell_N], 1<=j<=N,
    U_N=union_j I_j.                                      (14)

The intervals are disjoint, since adjacent centers differ by at least 1/N.
For i!=j, any prime-power knot in the cross cell
[|log(i/j)|-ell_N, |log(i/j)|+ell_N] must be at its center.

Proof. Assume i>j and |log(i/(nj))|<=ell_N for an integer n>=2.
Then |nj-i|<=i(exp(ell_N)-1)<2N ell_N<1. Since nj-i is an integer,
nj=i. Conversely nj=i puts the knot at the center. Thus the cusp matrix
is EXACTLY C_N, not a matrix that drops nearby nondivisibility knots. QED.

For h_j of zero integral, put G_j(s)=int_0^s h_j. Twice integrating by
parts on a cross cell gives the contribution

    -int int conjugate(G_i(s))G_j(t) R(log(i/j)+s-t) ds dt,

plus, when i=nj or j=ni,

    -Lambda(n)/sqrt(n) int_0^ell_N conjugate(G_i(s))G_j(s)ds.

The sign is minus because partial_s partial_t W(d+s-t)=-W''(d+s-t).
The sum of ALL cusp terms is therefore exactly

    -int_0^ell_N <G(s),C_N G(s)> ds.                       (15)

Endpoints of G vanish, and the kernel is continuous with bounded one-sided
first derivatives on every nonzero cross cell. Standard piecewise integration
by parts, then approximation of h_j in L2, proves these formulas. A knot
at the center is a translated-overlap integral, not a point to omit.

The regular cross terms have operator bound

    |Q_regular_cross|<=R_N sum_j ||G_j||_2^2,
    R_N=ell_N[6N^(3/2)+2N(1+log N)]<1/2.                 (16)

Indeed d=|log(i/j)|>=|i-j|/max(i,j)>=1/N and ell_N<d/2.
Equation (11) on the cell is at most
6sqrt(max(i,j)/min(i,j))+1/d. For the exponential constant use
exp(ell_N/2)<12/11; for the reciprocal term use x>=d/2.
The first row sum is at most 6N^(3/2). The second is at most
2N H_(N-1)<=2N(1+log N). The L2 norm of a bounded kernel on an ell-square
is at most ell times its supremum. A symmetric row-sum bound then gives
(16). Finally log N<=N-1 and N^(3/2)<=N^2 imply R_N<=8/2^20<1/2.
At N=1 there are no cross terms.

## 6. DC-3: full-source positivity, any number of windows, all mean-zero directions

Let f be ANY complex L2 function supported on U_N. Define the damped local
functions and their primitives by

    h_j(s)=exp(-a(log j+s)) f(log j+s),
    int_0^ell_N h_j(s)ds=0,
    G_j(s)=int_0^s h_j(t)dt.                               (17)

The equality in (17) is a HYPOTHESIS, one per window. It is not a conclusion
from f being supported on U_N.

**DC-3.** For every N>=1 and every such f,

    <f,T f> >=(3/2)(log N+1/2) sum_j ||G_j||_2^2.          (18)

In particular it is strictly positive for every nonzero f. A common
translation of all intervals into the positive half-line is allowed,
with the actual damping included in h_j as in (17).

Proof. Summing (13), using (4) on the Hilbert-valued G_j, and retaining
(16), the undamped W form is at least

    [2p_ell_N-log N-3-R_N] sum_j ||G_j||^2.

Now 2p_ell_N>log(1/ell_N)-6=20log2+2log N-6>2log N+4,
and R_N<1/2. The bracket exceeds log N+1/2. The operator in (7)
contributes the factor b=3/2. If all primitives vanish, h_j=G_j'=0
almost everywhere and f=0. This proves (18). QED.

No PNT, zero data, numerical matrix, or discarded prime tail occurs in
this proof. The exact safe source P2 and the full W are retained.
This is a primitive-norm bound, not a positive uniform L2 eigenvalue gap.
The source T differs from the heat-Hankel source Gamma; restricted positivity
for one is not automatically restricted positivity for the other.

## 7. DC-4: negative directions, if present, must survive the window means

On L2(U_N), the map f -> (int h_j)_j is continuous and surjective onto C^N.
Its kernel is the strictly positive space in DC-3. Any subspace on which
the full form is strictly negative must therefore map injectively to C^N.
Consequently the full restricted operator has at most N negative eigenvalues,
counted with multiplicity. More basically, a negative vector cannot have
all its damped window means zero.

This does NOT say a negative vector is piecewise constant or that its value
is determined by the means alone. Cross terms between means and primitives
still require a Schur-complement or a valid completed-square estimate.

## 8. The actual completion attempt, and where it stops

The attempted global proof was: replace the previous large absolute cusp
row bound by the exact arithmetic square (2), glue arbitrarily many windows,
and then recover the complete source sign. The first two steps are proved
on the stated mean-zero subspace. The third does not follow.

For general h_j put M_j=int h_j and G_j(s)=int_0^s h_j-M_j/2. The exact
endpoint/primitive decomposition of the parent contains the mass matrix

    Cmass_ii=W(ell)+ell*p_ell/2,
    Cmass_ij=[W(log(i/j)-ell)+2W(log(i/j))+W(log(i/j)+ell)]/4,

as well as signed mean/primitive cross terms. Equations (2)--(4) control
the entire prime-cusp portion of the primitive block. They do not control
Cmass or its full Schur complement. This is a specific remaining piece,
not an assertion that the cusp bound secretly proves the entire form.

In the zero-width limit Cmass approaches [W(log(i/j))]. An all-N sign
for that sample matrix would imply positive definiteness of W by continuity
and approximation of arbitrary positive ratios by integer ratios, and then
RH by the existing full-background endpoint. No such sign is proved here.

In particular, shrinking intervals cannot recover arbitrary fixed L2 tests:
|U_N|=N*ell_N=1/(2^20 N) ->0. Any bounded-norm sequence supported there is
weakly null, by absolute continuity of the integral of |g|^2 for a fixed
L2 test g. It cannot converge strongly to a fixed nonzero test. The cofinal
capture theorem from pass8 does not apply to this different support family.

Likewise the positive divisor Laplacian is not the full Weil form. It has
a known one-dimensional nullspace, while neither a determinant identity
with xi nor a positivity-preserving intertwiner to the full source is supplied.
Using either identification without proof would reinstate the missing sign.
There is a concrete divergence to pay: for any fixed nonzero finitely
supported v, (3) implies <v,L_N v>=log N ||v||^2+O_v(1). The positive
matrices L_N do not converge to a finite full-source form in these fixed
coordinates. Removing log N times the identity is not positivity preserving:
on their exact null vector it has eigenvalue -log N. The normalized null
vectors themselves lose every fixed finite set of coordinates, since its
squared mass there is H_K/H_N ->0. None of these elementary facts rules
out a different useful matching, but the matching is an actual obligation.

Thus this pass proves an all-N SIGNED arithmetic interaction bound and its
full-function application, but not RH or the square-width heat lower bound.
The result is intended as a reusable replacement for absolute cusp row sums,
not as a substitute for the remaining mass/cross-term estimate.
