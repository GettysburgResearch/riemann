# Keeping the selected count in BOTH the detector and the mollifier

Status: PROPOSED complete deductions from the unconditional fixed-order large sieve and the standard Hecke AFE. Independent review is required. This is an exceptional-family/zero-density theorem, not a zero-free theorem for every member and not RH. CT theta estimates and previous proposed Dedekind boundaries are NOT inputs.

## 1. A new general-order density bound

Use the fixed field, characters, twists, full power-free ideal ordering and zero conventions of SPARSE_MOMENTS.md. Fix n>=6. For each eta>0 there is a fixed rho>0 such that

    sum_(Na<=U)^flat N(3/4,4U^rho,psi chi_a)
        << U^(g_n+eta),
    g_n = 3(n^2-2n-4)/(n(5n-16)).                        (1)

Inducing-principal rows may be omitted, or their finitely many fixed functions added by the elementary zero-count estimate in Section 5. Multiplicity is retained in N. No optimized height exponent, uniformity in n, or uniformity over fields is claimed. In particular n->infinity changes the family data, so the limit of this numerical formula is not a theorem for a single fixed field.

At n=6, (1) gives 5/7. Its improvement over the displayed de Faveri exponent 8/11 at 3/4 is 1/77. It improves the proposed #971 shifted-detector exponent 395/552 by 5/3864, and #966's 43/60 by 1/420. For n=8,10,12 the formula gives 11/16,57/85,29/44 respectively, and g_n tends to 3/5. The methods are classical; no exhaustive literature-priority claim is made.

The new step is not merely another choice of detector line. The bound for the mollifier depends on R, the UNKNOWN number of selected rows, before that number is eliminated.

## 2. A cardinality-sensitive mollifier mean

Put

    lambda = 1/2+1/(2n),
    M_A(s,chi)=sum_(Nd<=A) mu_F(d)chi(d)(Nd)^(-s).

Let E be ANY row subset of cardinality R, and assume U^(1/2)<=A<=U. Uniformly in real t,

    sum_E |M_A(lambda+it,psi chi_a)|^2
      << U^eta [ U^(1-1/n) R^(1/n)
                          + U^(1-1/n) A^(1/n) ].         (2)

For R=0 it is zero. When R is a fixed constant times U, the usual full-family bound proves (2) after enlarging the field-dependent constant. It suffices to treat 1<=R<=U.

Proof. Split the mollifier at Y=min(A,U/R). The short part has squared mean at most

    C R Y^(2-2lambda)=C R Y^(1-1/n),                     (3)

by ordinary ideal counting. This is at most C U^(1-1/n) R^(1/n); when Y=A this uses RA<=U. For dyads Y<V<=A apply the power-free sieve directly to the squarefree mollifier coefficients. Their square mass is O(V^(-1/n+eta)). The four contributions, up to logarithms, are

    U Y^(-1/n), A^(1-1/n),
    U^(1-1/n) A^(1/n), U^(2/n) A^(1-2/n).               (4)

The first is the same bound as (3) whenever a tail is present, since then Y=U/R. The third dominates the second and fourth when U^(1/2)<=A<=U and n>=3. This can be checked by writing A=U^a: the exponent differences are (1-a)+(2a-1)/n and (1-3/n)(1-a), both nonnegative. Cauchy/Minkowski across dyads loses logarithms only. The unit column and all original masks remain. Equations (3)-(4) prove (2).

From SPARSE_MOMENTS.md at nu=1,r=2,sigma=lambda, or its direct AFE proof,

    sum_all |L_F^S(lambda+it,psi chi_a)|^4
        << U^(1+eta)(2+|t|)^C.                          (5)

Indeed K_n(U,V)V^(-1/n)<=4U for 1<=V<=U; the ACTUAL negative conductor factor in the dual AFE is handled before replacing a conductor by U. (5) is the general-order version of #969's off-central fourth moment. Its n=6 instance is credited, not claimed anew.

## 3. A rowwise shifted detector, with all maxima and tails

We reconstruct the shifted detector rather than quote the critical-line BGL (5.3) as if it already had the new line. Let E contain the nonprincipal rows having a zero beta+i gamma with beta>=sigma0=3/4, |gamma|<=T, and choose ONE such zero per row. Euler products imply beta<=1. Work first with 1<=T<=U.

For fixed A<=B, define b_A(h)=sum_(d|h,Nd<=A)mu_F(d). Exactly b_A(1)=1, b_A(h)=0 for 1<Nh<=A, and |b_A(h)| is bounded by a fixed-order divisor function. At a selected zero, Mellin inversion gives

    sum_h b_A(h)chi(h)(Nh)^(-beta-i gamma) exp(-Nh/B)
       = (1/(2pi i)) integral_(2)
          L(beta+i gamma+v,chi) M_A(beta+i gamma+v,chi)
                                      Gamma(v) B^v dv. (6)

Move to Re v=lambda-beta. The only crossed Gamma pole is v=0, whose residue is zero because L(beta+i gamma)=0. Nonprincipal L is entire; polynomial vertical growth and Gamma decay justify the horizontal limits. Thus the modulus of (6) is at most

    C B^(lambda-sigma0) integral_R
      |L(lambda+i(gamma+t),chi)M_A(lambda+i(gamma+t),chi)|
                              (1+|t|)^C exp(-pi|t|/2) dt. (7)

The unit term on the left is exp(-1/B), bounded below. The remaining terms below A vanish EXACTLY. Terms above B(log U)^2 have negligible total mass by exponential decay and the divisor bound, uniformly in beta,gamma. Enlarging the logarithmic cutoff by a fixed constant covers all bounded initial U. Consequently each selected row has either a definite contribution from (7) or a definite dyadic PREFIX polynomial on A<Nh<=B(log U)^2, evaluated at real part sigma0.

No per-row ordinate maximum is silently replaced by a common ordinate. For (7) change variable u=gamma+t. On |u|<=T+C(log U)^2 the translated weight is uniformly bounded, so the sum over E is bounded by the integral there of sum_E |L(lambda+iu)M_A(lambda+iu)|. Outside it Gamma decay pays all polynomial field/conductor/height costs. Holder is applied at each COMMON u, on the SAME subset E:

    sum_E |LM| <= R^(1/4) (sum_E |L|^4)^(1/4)
                                  (sum_E |M_A|^2)^(1/2). (8)

Use (5) for L and (2) for M. Integrating costs a fixed polynomial in T and arbitrary U losses, not an extra factor U or R. This avoids needing a claim that an unproved rowwise height maximum obeys a fixed-height theorem.

For the second type, partial summation of (Nh)^(sigma0-beta)exp(-Nh/B), a decreasing weight of variation at most one, reduces it to a dyadic prefix at sigma0. Order ideals by norm, with ties fixed. Each prefix is a union of at most O(log U) binary intervals. At each binary level the intervals are disjoint; sum their coefficient-square masses BEFORE applying the sieve. For complete columns h=c d^n, Minkowski in l2(rows,intervals) and the same convergent sum (Nd)^(-n/2+eta) preserve this disjointness, so no factor equal to the number of intervals is lost.

A height supremum over each unit interval is bounded by the integral of |P|^2+|P'|^2 over a larger interval. The derivative adds only log Nh. Summing the height intervals costs O(T+log^2 U). The full-column sieve lemma then bounds this second type by arbitrary U losses and polynomial height times

    B^(1/2) + U A^(-1/2)
       + U^(2/n) B^(1/2-1/n)
       + U^(1-1/n) A^(-1/2+2/n).                       (9)

All four monomials of K_n are present. Their signs in V permit the stated endpoints for n>=6. Any dyad crossing A, and the harmless logarithmic enlargement of B, is included. This is the standard Mellin zero-detector argument of BGL/DF with its changed line and selected mollifier norm explicitly supplied.

Combining (2),(5),(7)-(9), and sqrt(x+y)<=sqrt(x)+sqrt(y), gives

    R << U^eta (2+T)^C [
      B^(lambda-sigma0) U^(3/4-1/(2n)) R^(1/4+1/(2n))
      + B^(lambda-sigma0) U^(3/4-1/(2n)) A^(1/(2n)) R^(1/4)
      + terms (9) ].                                   (10)

The exterior implied constant and losses in (10) do not depend on how E or the selected zeros were chosen. No reciprocal-L moment, independence assumption or pointwise zero-free hypothesis occurs.

## 4. Exact elimination at every n>=6

Set

    A=U^a, B=U^b,
    a=(4n-14)/(5n-16), b=(6n-20)/(5n-16),
    g=3(n^2-2n-4)/(n(5n-16)),
    g0=1-(n-2)b/(3n-2).                                (11)

Here 1/2<a<1<b, and

    a-g=(n-6)(n-2)/(n(5n-16))>=0,
    g-g0=2(n-6)(n-2)/(n(3n-2)(5n-16))>=0.               (12)

Eliminating the R power in the FIRST term of (10) gives exponent g0. Eliminating the R^(1/4) in the SECOND term gives exactly g. The third and fourth terms of (9) also have exponent exactly g; the remaining gaps are

    g-b/2=4(n-3)/(n(5n-16))>0,
    g-(1-a/2)=3(n-4)/(n(5n-16))>0.                     (13)

For a nonnegative inequality R<=A0 R^d+B0 R^(1/4)+C0, with d<1, at least one term on the right is >=R/3. Thus R is bounded by the maximum of (3A0)^(1/(1-d)), (3B0)^(4/3), and 3C0. Applying this to (10), allocating arbitrary small initial losses, proves

    R << U^(g+eta)(2+T)^C1                              (14)

for a finite C1 depending on the fixed family. At n=6, a=g=5/7, b=8/7, and the decisive term simplifies to U^(10/21) R^(1/3). Every exponent identity (12)-(13) is a rational identity in n, not a numerical optimum claim.

## 5. Counting multiplicities at a small polynomial height

For each nonprincipal inducing L-function, the number of zeros in Re s>=3/4, |Im s|<=T is O((T+1)log(U(T+2))). One elementary proof uses Jensen on discs centered at 2+ij, j integral, of outer radius 7/4 and inner radius 3/2. The inner discs cover the stated half-strip up to Re s=1. The Euler product bounds |L(2+ij)| below by a fixed positive constant; polynomial conductor/height bounds on the outer discs bound Jensen's logarithm by O(log(U(T+2))). Multiplicities are included. Fixed omitted Euler factors have no zeros in these positive-real-part discs. There are O(T+1) centers.

Multiply this per-row count by (14). Choose one sufficiently small FIXED rho>0 for the requested final eta so that T=4U^rho, the factor (2+T)^(C1+1), and all logarithms fit inside that final loss. This proves (1). For the finitely many inducing-principal functions, apply the same Jensen argument to (s-1)L(s), an entire function on these discs, and remove its known extra factor when counting. They contribute only O((T+1)log(T+2)) and can be added. This is not an optimized T-aspect density theorem.

## 6. Scope and next mathematical question

This improves the family density at the same fixed zero threshold without relying on CT or any proposed quasi-RH composition. The improvement comes from retaining the selected cardinality inside the mollifier norm, not from a presupposed improvement of the native signed covariance. SPARSE_MOMENTS.md gives the complementary all-fixed-order selected-moment theorem.

A smaller family density does not exclude a single exceptional fixed L-function. No new individual Dedekind boundary is announced. Its possible use in a future Poisson stratification requires every changed contour, principal term, family normalization and tail to be paid separately. The critical inverse-Mobius moment and RH remain unproved.
