# Positive-loop continuation of a theta moment realization

Status: PROPOSED finite and local theorems with directed computational evidence;
independent mathematical review required. Neither RH, exact degree-20 matching,
nor an unbounded-order extension is proved. The all-order result below is a
LOCAL continuation theorem at each fixed order, with explicit hypotheses.
Classical Gibbs differentiation, the implicit-function theorem and Lee--Yang
are credited. The contribution is their specific compensated-loop construction
and source-certified application to the actual #981 theta realization.

## 1. Why change the graph, not another exponent

The #981 tree realizes the original standardized theta law through degree 18.
The current residual-moment estimates on the analytic route still allow a fixed
exceptional member. Instead of further optimizing either bound, we remove the
unnecessary tree restriction in the finite realization problem. A positive edge
between two existing vertices is allowed by Lee--Yang; no new spin is necessary.

The existing #988 also realizes degree 18, using a different tree. Its recorded
next-moment discrepancy (0.450,0.451) is SMALLER than the discrepancy of either
#981 or the cyclic model here. This packet claims a new local operation, not the
best degree-20 discrepancy across different models. Only #981 is a mathematical
and computational input. #988 was inspected at PR-description scope.

## 2. Exact insertion identity for any finite graph

Let P_x be a zero-field Ising measure on a finite graph, with nonnegative finite
pair couplings, and Y_x a nonnegatively weighted spin sum. The parameter x may
change specified weights and existing couplings, and all quantities below are
real analytic near x0. Choose a missing edge e=(v,w), put B_e=sigma_v sigma_w,
and add coupling J=atanh(q), 0<=q<1. Since B_e is +/-1,

    exp(J B_e)=cosh(J)(1+q B_e).

Thus for EVERY observable A (including the complete generating function),

    E_(x,q)[A] = (E_x[A]+q E_x[A B_e])/(1+q E_x[B_e]).       (1)

The normalization is essential. For q=0 the entire original measure is
unchanged. At q=0, differentiation gives Cov_x(A,B_e). This is classical Gibbs
interpolation, not a new general correlation theorem. No sign is asserted for
an arbitrary compensated covariance.

## 3. Local continuation theorem at every fixed matching order

Let C(x,q) in R^n consist of the first n even cumulants, or any fixed invertible
triangular normalization of them. Let H(x,q)=E_(x,q)[Y_x^(2n+2)]. Assume that
C(x0,0)=c*, x0 is interior for every positivity constraint on the n active
parameters, and J0=D_x C(x0,0) is invertible. The implicit-function theorem gives
a unique real analytic x(q) near zero, x(0)=x0, with

    C(x(q),q)=c*.

Every old positive parameter remains positive on a sufficiently small interval.
For q>0 the inserted coupling is strictly positive, so every resulting model
retains the full Lee--Yang property. A zero-weight auxiliary hub is allowed by
the standard Hurwitz limiting argument, with the hub kept in the Gibbs law.

The exact tangent and next-moment response are

    x'(0) = -J0^(-1) C_q,
    Gamma_e = H_q - H_x J0^(-1) C_q.                       (2)

If Gamma_e is nonzero, the next moment moves strictly in that direction for all
sufficiently small positive q. If two missing edges have Gamma_-<0<Gamma_+,
the UNION of the two positive-edge families contains an OPEN interval of next
moments around H(x0,0), while every lower prescribed moment remains exact.
This is a genuine two-sided local reachability conclusion using only positive
couplings. It neither gives the size of that interval nor says that the next
THETA target lies in it.

In raw-moment coordinates define the compensation polynomial

    P_e(y)=y^(2n+2)-sum_(r=1)^n lambda_r y^(2r),
    lambda = H_x J0^(-1).

Equation (1) gives Gamma_e=Cov(P_e(Y),B_e). Thus the missing sign is a finite,
source-specific compensated covariance, rather than an inference from the
positivity of the uncompensated Ising interaction. This formula is valid at
EVERY fixed n. It does not show that suitable signs exist at unbounded n.

## 4. Exact edge subdivision and why variance positivity is not enough

For comparison, replace an existing edge with bias c=tanh(J) by two edges
through a new spin eta, with biases u,v in (0,1) and uv=c. Summing eta gives
2(1+c sigma_v sigma_w), so the full marginal on old spins is EXACTLY unchanged.
Set

    alpha=u(1-v^2)/(1-c^2), beta=v(1-u^2)/(1-c^2).

Conditional on the endpoints, E eta=alpha sigma_v+beta sigma_w. If both endpoint
observable weights are positive, then, for sufficiently small epsilon>0,

    Y_epsilon=Y+epsilon(eta-alpha sigma_v-beta sigma_w)

is still a nonnegatively weighted spin sum on a ferromagnet. For its moment
generating function M_epsilon(t),

    d_epsilon M_epsilon(t)|0 = 0,
    d_epsilon^2 log M_epsilon(t)|0
       = t^2 E_t[1-(alpha sigma_v+beta sigma_w)^2].         (3)

This follows by conditional centering before differentiation. The bracket is a
conditional variance and is nonnegative for real t. It does NOT force the sign
of a particular higher Taylor coefficient after lower moments are retuned.
Exploratory evaluations of all six internal-dimer subdivisions at #981 moved
the compensated twentieth moment in the wrong direction in the old nine-coordinate
chart. That observation is not a universal obstruction or a certified all-gadget
classification. The loop construction was pursued instead.

## 5. The actual theta source and complete cyclic law

Retain #981's original even density

    Phi(t)=sum_(m>=1)[4(pi m^2)^2 exp(9t/2)-6 pi m^2 exp(5t/2)]
                           exp(-pi m^2 exp(2t)), t>=0,

extended evenly, and T* standardized to variance one. The classical Fourier
identity identifies its transform with the rescaled normalized xi function.
Let mu_j=E[(T*)^j]. We use the exact #981 rational parameters and nine active
coordinates (0,1,2,3,4,5,6,8,17). Their byte identities are checked before use.

The eleven component multiplicities are (256,10,1,1,1,1,1,1,1,1,1).
Types 0--4 are single spins; types 5--10 are dimers. There are 282 spins,
including a zero-weight hub, and 281 original edges. Put b_i=eta K_i a_i,
where K_6=K_7=3 and the other K_i=1/100. Conditional on hub +1, write

    G_i(t)=1-p_i+p_i cosh(a_i t)+p_i b_i sinh(a_i t),
    H_i(t)=b_i(1-p_i+p_i cosh(a_i t))+p_i sinh(a_i t),

with p_i=1 for singles. H_i(t) is E[sigma_root exp(tY_i)|hub=+1], NOT G_i
with a phase removed. For two distinct component roots i,j, the complete
conditional generating function after adding their edge is

    [G_i G_j+q H_i H_j]/[1+q b_i b_j]
       * product_l G_l^(multiplicity_l-1_(l=i)-1_(l=j)).    (4)

Average the two hub signs, equivalently take the even part. The denominator
is the same for both hub signs. All 2^282 configurations are represented by
this exact factorization; no sampling or configuration deletion is used.
The roots 7 and 9 and the roots 2 and 7 are missing edges in the old tree.
Inserting either creates one triangle through the original hub.

## 6. Directed response theorem at the TRUE theta-matching point

The new source reconstruction extends the pinned #981 primitive through degree
20. The old first nine equations are re-certified in the smaller radius 10^-36
box, not merely assumed true at the decimal center. The full source/root check
gives center correction below 8.404e-41 and contraction below 7.131e-18.
These decimal summaries are not acceptance inputs; CHECKS.json records exact
rational bounds and verify.py tests rational strict inequalities.

For the exact solution x* in that box, the certificate proves

    0.474 < E[Y_(x*,0)^20]-mu_20 < 0.475,                  (5)
    -3.423 < Gamma_(7,9) < -3.421,
     0.107 < Gamma_(2,7) <  0.109.                        (6)

Both signs concern the COMPLETE lower-moment compensation (2). Omitting that
compensation gives another quantity. Since the first nine cumulants are fixed,
the derivative of the twentieth raw moment equals that of the twentieth
cumulant. The checker uses this triangular identity to avoid subtracting large
raw moments in the response calculation.

Therefore the actual #981 solution is not locally one-sided in the twentieth
moment when positive cycles are allowed. A positive (7,9) edge moves toward
the actual theta target; a positive (2,7) edge moves away. No arbitrary-spin
approximation or hypothetical zeta-zero information enters (5)--(6).

### How the exact tangent is enclosed

Let R be the old rational preconditioner, J the interval lower Jacobian, h the
interval q derivative and L=||I-RJ||_infinity<1. Set y0=-Rh. For the EXACT tangent
y=-J^(-1)h,

    ||y-y0||_infinity <= L/(1-L) ||y0||_infinity.           (7)

This follows from the Neumann series for (RJ)^(-1). Multiply (7) by the l1 norm
of the top Jacobian row and add the direct q derivative interval. This encloses
Gamma at every parameter in the certified root box, including the true solution.
A fitted inverse, a center-only derivative or an unproved small roundoff is not
an acceptance premise.

## 7. A separate exact finite positive-loop realization

POSITIVE_LOOP.json fixes q=1/10000 and all passive parameters, and supplies a new
nine-dimensional rational center/preconditioner. The complete directed check on
a radius 10^-34 box proves center correction below 1.419e-40 and contraction
below 1.203e-15. It reconstructs the actual infinite theta source afresh.
Banach's theorem therefore supplies an EXACT connected ferromagnet matching
mu_2,...,mu_18, with 282 spins and 282 edges, and

    0.4737 < E[Y^20]-mu_20 < 0.4738.                      (8)

The exact old/new interval difference is more than 0.0004. This comparison is
between two certified endpoints, NOT extrapolation from Gamma(0). We do not
claim a validated continuous path between the two parameter boxes. The new
model still does NOT match mu_20. It also does not outperform #988's different
model. Its purpose is to authenticate the positive-cycle operation on the
literal theta source while retaining all lower moments.

## 8. Source and arithmetic fidelity

The inherited integer fixed-point interval primitive uses denominator 2^320,
Machin's pi formula, 96-term exp evaluation and outward reciprocal/squaring.
It is checked against the exact pinned SHA-256, not described as a second
independent backend. theta20.py reuses those primitives and the 98 cells and six
explicit theta indices; all normalization and standardization are outward.

For every j<=20 the density Taylor error is bounded by

    16*10^11*2^j/[4^121*(3/4)].

Indeed the old analytic density bound on the radius-1/8 circles is unchanged,
the density polynomial remains degree 120, and the real t^j factor is at most
2^j. Every time tail is bounded by the full sum

    8q^2 exp(9U/2-q exp(2U))
       * sum_(k=0)^j binom(j,k) U^(j-k) k!/[2q exp(2U)-9/2]^(k+1).

All omitted theta indices m>=7 are bounded by

    16*pi^2*7^4 exp(-49pi) j!/(98pi-9/2)^(j+1).

The index ratio is at most (8/7)^4 exp(-15pi)<1/2 and its denominator improves.
Thus extension to degree 20 changes no tail premise. Taylor errors are added
two-sided; the positive omitted terms are added only upward. No stored source
moment is an input to an accepting run.

The complete seven-spin Gibbs enumeration in controls.py is an independent
finite assembly of (4), including its normalization, both hub signs and all
moments 0--20. It shares rational arithmetic and source conventions, so it is
not an independent infinite-source or mathematical review.

## 9. Exact boundary of the result

At each fixed order, (2) turns possible extension into explicit compensated
edge covariances. We certify both signs at n=9 and one improved finite endpoint.
To reach RH by the retained #981 compactness theorem, models whose moments
converge at EVERY fixed order are still needed. Nothing here proves that the
successive target values remain in these local reachable intervals, prevents
Jacobian degeneration, or supplies unbounded-order feasibility. The large
numerical gap to the degree-20 target is stated in (8), not hidden.

The pure-Gibbs formula is classical; the finite theta application and choice of
compensated positive loops are the claimed repository additions. No worldwide
priority claim or accepted RH theorem is made.
