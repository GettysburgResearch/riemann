# Keep the selected family inside the norm

Status: PROPOSED complete deductions from the stated de Faveri sixth-order
large sieve and classical Hecke approximate functional equations. Independent
mathematical review is required. These are numerator L-value moments, NOT
inverse-L/Mobius moments. No RH, GRH or unproved cancellation hypothesis is used.
Classical truncation, large-values and Holder arguments are credited; worldwide
priority is not claimed for the framework or its specializations.

## 1. Exact arithmetic input

Fix F containing mu_6, the admissible fixed S and generator choices of de Faveri
(DF), arXiv:2610.04045v1. The rows a are SIXTH-POWER-FREE exterior ideals, ordered
by their full norms Na<=U. Keep the finite list of fixed S-supported twists psi,
all original nonunit zeros, and complete ideal coefficients. The imported sieve is

 sum_a |sum_c z_c chi_a(c)|^2
  << (UV)^eta K(U,V) sum_c |z_c|^2,
 K(U,V)=U+V+U^(5/6)V^(1/3)+U^(1/3)V^(5/6),                    (1)

with BOTH a and c sixth-free. A fixed psi multiplies common column coefficients.
It is not the infinite-order angular theta character. The CT-to-DF adapter is
in the pinned #965 proof and the recovered local-support packet; this document
also applies directly to DF's own family, without using CT at all.

Let E be ANY fixed subset of rows, R=|E|. E may be selected by denominator zeros.
For complete coefficients b_n supported in V<Nn<=2V and bounded by (Nn)^(-y+eta),
including fixed-order divisor coefficients, the following hereditary block bound
holds, up to (UV)^O(eta):

 sum_(a in E) |sum_n b_n chi_a(n)|^2
       << V^(1-2y) min(R V, K(U,V)),   0<=y<=1.             (2)

This is the new organizing step: the short blocks pay R, not U.

The first bound in (2) follows from the triangle inequality on each row and
ideal counting: sum |b_n| << V^(1-y+eta). For the second, write n=c d^6 uniquely.
Shared primes between c and d are ALLOWED. The exact identity is

 chi_a(c d^6)=chi_a(c) 1_((a,d)=1).                          (3)

Fix d, apply (1) to the retained positive row subset, then use Minkowski over d.
The coefficient square mass on c~V/(Nd)^6 is
V^(1-2y+O(eta))(Nd)^(-6); the resulting root sum sum_d(Nd)^(-3+eta) converges.
K is increasing in its second variable. This proves the complete-column bound
without deleting powerful columns or masks. Take the minimum of these TWO valid
bounds for the SAME entire dyad; no unsupported minimum inside an Euler product
is used. Fixed twists and conjugates obey the identical argument.

## 2. Exact selected moments, including the actual dual conductor

Put

 k(v)=max(1,v,5/6+v/3,1/3+5v/6),
 Phi(nu,y,L)=max_(0<=v<=L) min(nu+(2-2y)v, k(v)+(1-2y)v).    (4)

For every FIXED integer r>=1, 0<=nu<=1, fixed 1/2<=y<1 and every eta>0,

 R<<U^nu  =>  sum_(a in E) |L_F^S(y+it,psi chi_a)|^(2r)
       << U^(Phi(nu,y,r/2)+eta) (2+|t|)^C.                  (5)

Constants depend on the fixed field, data, order, strip and loss; they are not
uniform as r grows. For a fixed finite list of strips and orders, C can be chosen
independently of 0<eta<=1. For 0<y<1/2 the valid exponent is

 Phi(nu,1-y,r/2)+r(1-2y).                                 (6)

Principal inducing rows are handled separately (or omitted), since L(s)^r can
have a pole there. They are finite in the exterior family and do not enter the
exceptional-character count. No AFE polar term is silently discarded.

Proof of (5). Work with the AFE for L(s,chi)^r, whose coefficients are the
complete ideal divisor coefficients d_r(n). Partition by actual inducing
conductor Q<=C U and fixed S/gamma type. Its main and dual pieces have length
Q^(r/2), up to arbitrary small norm losses and fixed polynomial height factors.
The dual scalar in their squared row norm has modulus Q^(r(1-2y)), up to the
stated height factor. It is NOT replaced by U^(r(1-2y)) when this power is negative.

Mellin separation on fixed small positive lines leaves common coefficient arrays
at each Mellin parameter, with conductor phases outside the column sum. The unit coefficient is handled separately and contributes O(R), exactly the
v=0 value in (4). For each product-norm dyad apply (2), then Minkowski. Truncating first and taking limits
is justified by the rapid AFE/Mellin tails and the convergent d-sum in (3).
Every original and dual dyad remains. The estimates for ideal divisor functions
and gamma factors cost an arbitrarily small U power and a fixed height power.

For clarity suppress those already allotted height/loss factors and write
Q=U^q, 0<=q<=1, V=U^v. On the main side 0<=v<=rq/2, so (2) is bounded by (4).
On the dual side its exponent is

 rq(1-2y)+min(nu+2y v, k(v)+(2y-1)v).

Because rq>=2v and 1-2y<=0, this is at most

 min(nu+(2-2y)v, k(v)+(1-2y)v).                            (7)

Thus the same Phi bounds EVERY conductor dyad, including small Q. Bounded Q
is handled with q=0; the harmless fixed constant C in Q<=C U is absorbed before
this exponent argument. Lengths containing a polynomial height factor are
handled by bounding that factor in each of the four monomials and the trivial
bound in (2). A small norm enlargement changes (4) by O_r(eta). Taking the decay
order large first justifies summing the infinite tails. Dyadic conductor sums
cost logarithms. This proves (5). Applying the exact functional equation with
its positive Q power when y<1/2 gives (6). QED.

## 3. A finite formula, not a numerical optimization

The crossing k(v)-v=nu occurs at

 v0(nu)=1-nu                 if 1/2<=nu<=1;
       =5/4-3nu/2            if 1/6<=nu<=1/2;
       =2-6nu               if 0<=nu<=1/6.                  (8)

For 0<=y<=1,

 Phi(nu,y,L)=nu+(2-2y)L                              if L<=v0;
            max(nu+(2-2y)v0, k(L)+(1-2y)L)           if L>=v0. (9)

Indeed before v0 the smaller bound is the increasing trivial line. After v0
it is k(v)+(1-2y)v, a convex piecewise-affine function; its maximum on a compact
interval occurs at an endpoint. This proves (9) over the ENTIRE real interval.
The endpoint nu=0 causes no problem: the functions coincide for v>=2.

Holder now gives, with kappa_r(nu,y) denoting (5) or (6),

 sum_(a in E)|L(y+it,psi chi_a)|
       << U^(m_r(nu,y)+eta)(2+|t|)^C,
 m_r=(1-1/(2r))nu+kappa_r(nu,y)/(2r).                     (10)

At each fixed y, m_r is nondecreasing and 1-Lipschitz in nu. This follows
directly from (4): increasing nu by d>=0 changes each minimum, and hence Phi,
by a number in [0,d]. Consequently a count U^(nu+e) costs at most an additional
e in (10). This is used in the complete contour certificate; it avoids an
unjustified change of subset when a later analytic loss is made smaller.

For fixed nu, possible extrema in y occur at endpoints or intersections of the
two affine functions in (9), together with y=1/2. The published finite parameter
table does not need an optimizer: the verifier evaluates its chosen rational
lines with (9) and checks every complete class budget.

## 4. Two useful specializations

If |E|<<U^(2/3), (5) at r=3,y=3/4 gives

 sum_E |L(3/4+it)|^6 << U^(5/6+eta)(2+|t|)^C.              (11)

Both endpoints are active: v0=1/3 costs 5/6, while V=U^(3/2) costs
19/12-(3/2)/2=5/6. A full-family moment would have cost U, because it paid
for the unit/short-column mass on ALL rows rather than the selected family.
By (6) the corresponding sixth moment at y=1/4 costs U^(7/3+eta); by (10),

 sum_E |L(1/4+it)| << U^(17/18+eta)(2+|t|)^C.              (12)

The best previously displayed full-family moment envelope at this (nu,y)
was 23/24, so (12) saves U^(1/72). This comparison is about the sufficient
bounds in the named repository packets, not a lower bound or worldwide record.

A second specialization drives DENSITY.md. For R>=sqrt(U), 1/2<=theta<1,

 sum_E |L(theta+it)|^4
  << U^eta(2+|t|)^C [U^(2-2theta)R^(2theta-1)+U^(13/6-2theta)]. (13)

The same-line mollifier M_A has

 sum_E |M_A(theta+it)|^2 << (UA)^eta [
   U^(2-2theta)R^(2theta-1)+A^(2-2theta)
   +U^(5/6)A^(4/3-2theta)+U^(1/3)A^(11/6-2theta)].          (14)

For (13), use (9) with L=1 and v0=1-log_U R. For (14), use (2) on every
mollifier dyad, L=log_U A. If A<U/R the trivial line is bounded by its value
at U/R; otherwise convexity after that point bounds it by the two endpoints.
The U*A^(1-2theta) endpoint is no larger than the short-column term in the
latter case. Fixed constants in R<<U are harmless; R>U is already covered by
the full-family bound and the displayed short term. The estimates persist on
neighboring fixed strips with arbitrarily small power losses for height maxima.

## 5. What this does not establish

No moment of 1/L, reciprocal-Mobius polynomial, fixed physical sextic source,
or critical covariance is estimated here. The selected set can be correlated
with L-values and denominator zeros; this is why no independence premise is
needed. Norm counting is not conductor counting. The gamma/conductor adapter,
full-column masks and the imported sieve remain essential analytic review
obligations. The finite checker authenticates algebra, not those obligations.
