# A smaller complete norm price for annular height-adapted probes

**PROPOSED source-qualified comparison theorem.** This improves the
comparison error for the ACTUAL annular mixed source using the stated
working fixed-field reciprocal bound. The complementary modified norm
is OPEN. No new zero detector or zero-free region is claimed.

Use the exact common-profile Fourier representation and untwisted
positive tail in `NORM_MELLIN_PROBE_ADAPTER.md`. The response matrix,
its weighted inverse bound, and its full-range infinity-norm stability
are proved in `../eisenstein/GROWING_PROFILE_COMPARISON.md`. Every
original input power, shared prime and nonunit zero remains. The
analytic imports are the SAME unrestricted zero-slot TWO-PLAIN moment,
and the fixed-field reciprocal bound explicitly assumed in
`../eisenstein/GROWING_RESIDUE_DEBIAS.md`:

* for a fixed 1/2<beta<1, 1/zeta_E^S(s) is holomorphic on Re s>beta;
* on each closed half-plane Re s>=beta+epsilon it has polynomial
  vertical bounds.

The working input beta=7/8 is permitted by that source foundation.
This note does not prove that input. The arithmetic response below
contains no further moving finite character: the original common
character remains in psi_u, as in the cited norm adapter.

## 1. Annular responses at every real height

Let V_a be a fixed smooth compact annular function. The actual Fourier
mode head is

    b_kappa(a)=mu(a)V_a(Na/D)(Na/D)^(i*kappa),
    Z_g(kappa)=sum_(g|a) b_kappa(a)v(a)/Na,             (1)

for good squarefree Ng<=G. The support of V_a is bounded AWAY FROM
ZERO. For each fixed nonnegative derivative order j and every epsilon
there are finite A_j,C_j such that, uniformly for every real kappa,

    |partial_kappa^j Z_g(kappa)|
       <= C_j (1+|kappa|)^(A_j)
                   D^(beta-1+epsilon)(Ng)^(-beta+epsilon). (2)

Here and below all lengths are in the original fixed polynomial ranges.

To prove (2), write a=g*c, (c,g)=1. The relevant Dirichlet series is

    sum_((c,g)=1) mu(c)v(c)/(Nc)^s
       = zeta_E^S(s)^(-1) H(s)
                      product_(p|g)(1-v(p)(Np)^(-s))^(-1), (3)

where H has an absolutely convergent Euler product for Re s>0.
Indeed v(p)=1+O(1/Np), so the local correction to 1-(Np)^(-s)
is O((Np)^(-1-Re s)). On Re s>=beta+epsilon the last product in
(3) is O_epsilon((Ng)^epsilon), uniformly in Im s, by the usual
primewise subpower estimate.

Apply smooth Mellin inversion with the ANNULAR weight

    V_a(x)x^(i*kappa)(log x)^j

at length D/Ng. Its Mellin transform is entire. On any fixed vertical
strip it decays faster than any power of |Im s+kappa|, uniformly
after the indicated fixed j derivatives. Precisely, if L_g=D/Ng and
q is the Dirichlet-series variable in (3), the integral has factor
`L_g^(q-1)*hat W_kappa(q-1)` and Dirichlet series (3) at q.
Shift to Re q=beta+epsilon, equivalently to Re s=beta-1+epsilon
in the ordinary weight-Mellin variable s=q-1.
No pole of the weight is crossed, and (3) has no pole there. The
polynomial vertical bound for the reciprocal costs at most a fixed
power of 1+|kappa| after integrating the rapidly decreasing transform.
The outside factor 1/Ng and the length (D/Ng)^(beta-1+epsilon)
give (2). Choosing internal epsilons before the prescribed final one
pays every displayed subpower.

This argument fails for a MODULATED PREFIX which is one near zero:
its Mellin transform has a pole at the shifted height, with a generally
nonzero reciprocal-zeta value as residue. At zero height the reciprocal
zero at the zeta pole can remove that prefix residue. That distinction
does not apply to (1), whose annular Mellin transform is entire at
EVERY height. No claim about independently modulated prefixes is made.

## 2. Complete Gram solution and its improved coefficient resources

Let B be the SAME real positive tail-response matrix, independent of
kappa, and solve B*xi(kappa)=-Z(kappa). Assume the same fixed Gram
margin G<=D^(1/2-delta), delta>0. Since

    f(g)^(-1) <<_epsilon (Ng)^(1+epsilon),
    sum_(Ng<=G) (Ng)^(1-2*beta+epsilon)
                                 <<_epsilon G^(2-2*beta+epsilon),

equation (2) and the weighted inverse bound imply

    ||partial_kappa^j xi(kappa)||_f
       << (1+|kappa|)^A (G/D)^(1-beta)(DG)^epsilon,
    sum_(Ng<=G) |partial_kappa^j xi_g(kappa)|/sqrt(Ng)
       << (1+|kappa|)^A D^(beta-1)
                                  G^(3/2-beta)(DG)^epsilon. (4)

The second inequality is weighted Cauchy over the COMPLETE index set.
The matrix is independent of kappa, so differentiation introduces no
new matrix or conditioning assumption.

The exact main inverse bound |F^(-1)_(g,h)|<<N(g,h)G^epsilon also
gives a useful infinity resource. In fact

    sum_(Nh<=G) N(g,h)/(Nh)^beta
      =sum_(d|g)phi(d) sum_(d|h,Nh<=G)(Nh)^(-beta)
      <<_epsilon G^(1-beta)(Ng)^epsilon.

Its proof is the ideal integral through G/Nd and the divisor bound
sum_(d|g)phi(d)/Nd<<g^epsilon. The existing Neumann estimate
||B_0^(-1)(B-B_0)||_(infinity->infinity)
 <<D^(-1/2)G^(1+epsilon)=o(1) preserves the main estimate. Therefore

    max_g |partial_kappa^j xi_g(kappa)|
       << (1+|kappa|)^A (G/D)^(1-beta)(DG)^epsilon.    (5)

The complete tail t_kappa(a)=mu(a)^2 W(Na/D)/v(a)
times sum_(g|a)xi_g(kappa) retains the same literal zero extensions
in its eventual character polynomial. The same B-energy argument as
in the cited comparison gives the additional arithmetic resource

    sum_a |t_kappa(a)|^2
       << (1+|kappa|)^A
                    D^(2*beta-1)G^(2-2*beta)(DG)^epsilon. (6)

For (6), use |W|^2/v^2<<D^epsilon W on the fixed tail annulus, so
the left side is bounded by D^(1+epsilon)*xi^*B*xi. The exact identity
xi^*B*xi=Z^*B^(-1)Z and (2) give the asserted power. No family-row
orthogonality is inferred from this arithmetic coefficient estimate.

## 3. Reassemble the ENTIRE original Fourier profile

Keep the original Fourier density c(xi,eta), kappa=xi-eta, in the
exact representation from the norm adapter. Replace b_kappa by
b_kappa+t_kappa ONLY in the intermediate comparison vector. Every
specified modal polar functional still vanishes exactly for every
squarefree Ng<=G, because the SAME equation B*xi=-Z is solved.

For a fixed mode, separate its product profile again in the two plain
input norm coordinates, as in that adapter. Expand every squarefree
tail Euler factor, square index and moving input coprimality mask
BEFORE the zero-slot TWO-PLAIN theorem is used. That proof gives

    ||Delta_(kappa,eta)||_row
       << U^(1/2+epsilon)(1+|eta|)^C
                              sum_g |xi_g(kappa)|/sqrt(Ng).

Insert (4). The original density has finite weighted Fourier L1 norm
at every required FIXED order. Thus its integral against
(1+|xi-eta|)^A(1+|eta|)^C is bounded by a fixed seminorm of the
ORIGINAL profiles. Bochner Minkowski over this SAME original density
is legitimate and includes its full unbounded height tails. It yields

    ||f_original-f_new||_row^2
       <<_epsilon U^(1+epsilon)
                   D^(2*beta-2)G^(3-2*beta)(1+T)^C ||K||_J^2. (7)

For general common row/input profiles use the identical original
three-coordinate density in the Eisenstein comparison; its additional
row mode only adds its original fixed weighted L1 cost. All fixed
height derivatives are covered by (2)--(4). The permitted original
height bound U^tau is absorbed by choosing tau in terms of the final
epsilon, exactly as in the source's common-profile calculus.

Equation (7) compares the COMPLETE original and modified mixed
vectors. It is not a collection of pointwise-height tests or an
estimate for independently chosen row coefficients. The modified
vector need not retain any hypothetical zeta zero: the original
detector and its consumer have not been changed. Every shared input
prime, all original powers, every row zero and every Fourier tail
is included in the paid difference.

## 4. Explicit improved arithmetic-label budget

At the working beta=7/8, (7) becomes

    ||f_original-f_new||_row^2
          << U^(1+epsilon) D^(-1/4) G^(5/4)(1+T)^C.   (8)

In particular G=D^(1/5) pays the comparison at row size U, for the
whole annular profile at all heights. For the relaxed target U^(6/5),
the adaptive choice

    G=U^(4/25)D^(1/5)                                (9)

pays (8) EXACTLY at U^(6/5+epsilon). On the full robust witness
range D between U^(1-eta) and U^(3/2+eta), with any sufficiently small
fixed eta, (9) has a fixed margin below D^(1/2). It therefore satisfies
the complete growing-Gram hypothesis. For example eta<=1/10 permits
the Gram margin delta=1/10. At D=U its exponent is 9/25;
at D=U^(3/2) it is 23/50. Reducing G by U^delta gives a strict
comparison margin U^(6/5-5*delta/4+epsilon).

Alternatively a fixed cutoff G=U^(9/25) works for D>=U. To retain
a robust lower length D>=U^(1-eta), reduce that fixed exponent by
eta/5, or simply use the adaptive choice (9). The earlier uniform
absolute bound UG remains valid without the reciprocal input, but
is a strictly weaker price for these actual annular Mobius heads.

Thus more growing polar labels can be removed at the SAME complete
comparison budget. The full continuous/nonpolar norm of f_new, all
unrelated character interfaces, and the simultaneous signed large-core
remainder are STILL OPEN. Equations (7)--(9) do not establish the
full U^(6/5) mixed mean required by its conditional zero-free consumer.
