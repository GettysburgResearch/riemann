# Actual reciprocal moments: one good family, all fixed orders, and a full capped law

Status: PROPOSED complete source-qualified deduction, awaiting independent
mathematical review. These are moments of actual reciprocal L-values, not
positive numerator moments or moments of independent replacement rows.
The uncapped theorem has an explicit sparse exceptional set; the full-family
theorem has an explicit growing cap. Neither restriction may be erased.
No RH, quasi-RH, native inverse-moment hypothesis, or CT theta theorem is used.

## 1. Exact statement

Use the fixed family of MOLLIFIED_APPROXIMATION.md, with n>=3. Fix
s=sigma+it, 1/2<sigma<1, and a nonzero nonnegative W in C_c^infinity((1,2)).
Write d0=2sigma-1 and

 c_W = [Res_{z=1} zeta_F^S(z) / zeta_F^S(n)] * integral_0^infinity W(x)dx.

For a good prime ideal p put q=Np and

 w_p=(1-q^(-1))/(1-q^(-n)),
 C_k(s)=product_{p notin S} [1-w_p+(w_p/n)
              sum_{zeta^n=1} |1-psi(p) zeta q^(-s)|^(2k)].       (1)

For each FIXED integer k>=1, this product is finite and strictly positive.
The factor w_p is the probability that an n-free row is coprime to p. It is
NOT 1-1/q. Distinct prime ideals of the same rational norm remain distinct.

There is a set G_U, independent of k, whose complement in U<Na<2U has
cardinality O(U^(1-c)) for some fixed c>0, such that, for every fixed k,

 sum_{a in G_U}^{n-free} W(Na/U) |L_a(s)|^(-2k)
                = c_W C_k(s) U + O(U^(1-eta_k)),               (2)

where eta_k>0. The same G_U works for all FIXED k; this asserts no uniform
estimate when k grows with U.

Furthermore, put tau_k=c/(8k), and define min(|L_a(s)|^(-1),U^tau_k) to be
U^tau_k when L_a(s)=0. Then the FULL family, including every exceptional row,
satisfies

 sum_a^{n-free} W(Na/U) min(|L_a(s)|^(-1),U^tau_k)^(2k)
                = c_W C_k(s) U + O(U^(1-eta_k)).               (3)

One permissible choice is

 a_k=min(d0/8,1/(16k)),     eta_k=min(d0*a_k/4,c/4).             (4)

The constants depend on all fixed family data, s,W,k. The cap in (3) changes
the observable and is essential to the assertion made here.

### A concrete sextic specialization

For n=6, sigma=3/4 and any fixed t, choose G_U using denominator zero exclusion
at sigma0=5/8, with a sufficiently small fixed polynomial height. The original
DF density exponent there is 9/10, so c=1/20 is permissible after paying the
height and arbitrary losses. Thus for every fixed k>=1,

 sum_a^{6-free} W(Na/U) min(|L_a(3/4+it)|^(-2k),U^(1/80))
       = c_W C_k(3/4+it) U + O(U^(1-1/(128k))).                (5)

The same main term and error hold for the uncapped sum on G_U. This is an
asymptotic with a positive explicit leading constant, not just U^(1+epsilon).
At k=1,

                    C_1(3/4+it)=product_p(1+w_p q^(-3/2)).     (6)

For k<n the root average in (1) reduces to sum_{j=0}^k binom(k,j)^2 q^(-2j sigma).
At k>=n the additional congruence classes MUST be retained, including their
psi(p) and t phases. The proof does not replace congruence modulo n by equality.

## 2. One common exceptional set, chosen before any moment order

Fix sigma0=(sigma+1/2)/2. For psi=1 the imported DF Corollary 1.5 gives an
exponent 1-c0<1 at sigma0, with a fixed polynomial height exponent. For the
fixed S-supported psi allowed here, use the following scope adapter, not an
assertion that the printed corollary already mentions every twist. In DF's
Section 9 proof, replace each L(s,chi_a) by L(s,psi chi_a), and each mollifier
coefficient mu_F(b) by mu_F(b)psi(b). The coefficient identity for L M has the
same divisor sum, since psi is completely multiplicative including its zeros.
Every Dirichlet-polynomial second norm has common coefficients multiplied by
the unitary psi(b); (2) of the preceding file is unchanged. Both AFE pieces
retain their common fixed gamma types, and the dual uses the conjugate fixed
twist. Their conductors still satisfy Q<=C_(psi) Na. Finite S corrections are
fixed polynomials or absolutely summable S-supported tails as in the preceding
file. Thus the rowwise Mellin detector, its mean estimates and the ten norm
monomials of DF's Section 9 proof are unchanged; only constants and polynomial
height factors may change. The same positive norm saving c0 and the explicitly
used first-range exponent are therefore retained. This adapter covers one
fixed twist or a fixed finite list, not growing-conductor twists.

Choose once a
sufficiently small rho>0 so that the zeros in

       Re z>=sigma0,   |Im z|<=4U^rho

occur among O(U^(1-c)) row indices, where c=c0/2 is permissible by first
allotting small norm losses and then the height cost. Let G_U be the rows with Na<=2U
without such a zero, omitting any finitely many inducing-principal rows.
The count includes the full n-free ideal indexing. Multiplicity in the
imported density only strengthens the index-count bound. No memberwise
zero-free assertion is assumed: bad rows stay in the complement.

For every lambda>0, uniformly on G_U and at the fixed s,

                       |L_a(s)|+|1/L_a(s)| <<_lambda U^lambda. (7)

Here is the analytic-log argument used for (7). Take a disc centered at 2+it,
with outer radius strictly below 2-sigma0 but larger than 2-sigma. Its
fixed-margin enlargement lies in the zero-free rectangle for all sufficiently
large U. The Euler logarithm supplies an analytic logarithm on the disc,
normalized at the center, and is uniformly bounded on an inner disc lying
strictly to the right of one. Polynomial conductor/height bounds control
Re log L by O(log U) on the outer disc. Borel--Caratheodory gives a modulus
bound on a slightly smaller disc, still beyond the target. Hadamard's
three-circles theorem between that disc and the Euler disc yields
|log L_a(s)|<=C(log U)^theta, theta<1. This proves (7) for BOTH signs.
Fixed Euler omissions have no zeros at positive real part and are retained.
There is no claim at the edge sigma0 or at heights outside the rectangle.
G_U depends on sigma and the fixed family, but not on k.

For the example, DF's first-range formula is
 g_n(sigma0)=1-q0/(4-n q0), q0=2sigma0-1.
At n=6, sigma0=5/8 it gives g=9/10. Taking a fixed small rho and norm loss
leaves the announced bound U^(19/20). This is the ORIGINAL density input,
not a use of #979's stronger estimate at the different threshold 3/4.

## 3. A complete character mean with the masks retained

For an exterior ideal b define rad(b) to include ALL its prime divisors,
even those with exponent divisible by n. Reciprocity gives chi_a(b), on
each of finitely many ray classes of a, as chi_b(a) times a fixed class factor.
Expand that factor in characters xi of R_c. The group R_c has exponent n.
Consequently the Dirichlet series in the n-free row variable is a finite
linear combination of

             L^S(z,xi chi_b) / zeta_F^{S union supp(b)}(n z).  (8)

The numerator retains its imprimitive Euler omissions at neutral primes.
This follows prime by prime from the finite geometric series of valuations
0,...,n-1. It is an identity initially at Re z>1. Class factors have bounded
Fourier coefficients because the ray group is fixed.

If b is NOT an n-th power, the inducing character has nontrivial ramification
outside S, by DF Section 2.5.1. A fixed S-supported xi cannot remove it.
Thus every numerator in (8) is nonprincipal, and has no pole at one. Its
conductor is at most a fixed multiple of N rad(b). On Re z=1/2+epsilon,
the denominator is in absolute Euler convergence, since n>=3. Its inverse,
including the moving omissions, is uniformly bounded on a fixed line.
The extra numerator Euler factors cost (Nb)^epsilon. The classical convexity
bound for the inducing Hecke L-function is

  << (N rad(b))^(1/4+epsilon) (2+|Im z|)^C (Nb)^epsilon.

Shift the smooth W Mellin integral from Re z>1 to 1/2+epsilon. Rapid Mellin
decay pays the polynomial height factor and both horizontal limits. This gives

 sum_a^{n-free} W(Na/U) chi_a(b)
       << U^(1/2+epsilon)(N rad(b))^(1/4+epsilon)(Nb)^epsilon. (9)

If b is an n-th power, do NOT use an analytic cancellation estimate. Exactly
chi_a(b)=1_{(a,b)=1}. The same Mellin calculation with its pole at one gives

 sum_a^{n-free} W(Na/U) 1_{(a,b)=1}
  = c_W U product_{p|b}w_p + O(U^(1/2+epsilon)(Nb)^epsilon). (10)

This proves both the main density and the original local zero probability.
No GRH or inverse L-contour shift occurs: the ONLY reciprocal factor used
in this step is at n Re z>1. All norms in these identities are ideal norms.

## 4. Moments of the actual truncated Mobius polynomial

For a fixed j>=1, expand |M_A(s,a)|^(2j) before averaging. Let
b_+=d_1...d_j and b_-=e_1...e_j. The row factor is

     chi_a(b_+) conjugate(chi_a(b_-))=chi_a(b_+ b_-^(n-1)).   (11)

Its modulus is zero on EVERY common-prime mask. Its inducing conductor
outside S divides rad(b_+ b_-), of norm at most A^(2j); the formal label
has norm at most A^(nj), which contributes only the specified epsilon loss.
It is principal exactly when the prime-exponent differences between b_+
and b_- are divisible by n. Equality of rational norms is NOT this condition.

Apply (9) to the nonprincipal tuples and (10) to the principal ones. Summing
the error absolutely costs

 (sum_{Nd<=A}(Nd)^(1/4-sigma+epsilon))^(2j)
                   << A^(j(5/2-2sigma)+epsilon).

Therefore

 sum_a^{n-free} W(Na/U)|M_A(s,a)|^(2j)
  =c_W U D_{j,A}(s)+O(U^(1/2+epsilon) A^(j(5/2-2sigma)+epsilon)), (12)

where D_{j,A} is the complete signed principal-tuple sum with the masks
product_{p|b_+b_-}w_p. No principal tuple is dropped or declared positive.

The infinite version of this tuple sum is the Euler product C_j in (1).
Every nonconstant local principal term uses at least two column occurrences:
n>=3 and a-b=0 mod n exclude a single occurrence. Hence the absolute local
sum is 1+O_{j}(q^(-2sigma)), summable over prime ideals. For any one column
constrained to Nd>A, apply Rankin with exponent d0/2. The local absolute
sum then converges because 2sigma-d0/2>1. A union bound over the 2j columns
proves, without changing any signs,

                         D_{j,A}=C_j+O(A^(-d0/2)).          (13)

Each local factor in (1) is positive and is 1+O_j(q^(-2sigma)), proving the
finite, strictly positive product. Combining (12)--(13) yields

 sum W |M_A|^(2j)=c_W C_j U
    +O(U A^(-d0/2)+U^(1/2+epsilon)A^(j(5/2-2sigma)+epsilon)). (14)

This is an actual family average, not a replacement by independent rows.
The independent zero/root law is an equivalent interpretation of the proved
Euler constant, with unit probability w_p and n equally likely unit phases.

## 5. Transfer to actual inverse values, with a power error

Fix k and choose a0=a_k from (4). Then a0<=d0/2, so the preceding file gives

                    sum_{Na<=2U} |L_a M_A-1|^2 << U^(1-d0*a0+epsilon), (15)

with A=U^a0; replacing U by 2U only changes fixed constants. For j<=2k,
the second error exponent in (14) is at most

       1/2 + 3k a0 <= 11/16,

before an arbitrarily small loss. In particular all these mollifier moments
are O(U), and (14) has its stated power asymptotic. Constants may depend on j.

On G_U put I_a=1/L_a(s) and E_a=L_a(s)M_A(s,a)-1. Exactly M_A-I_a=I_a E_a.
The elementary inequality

 ||M_A|^(2k)-|I_a|^(2k)|
        <=2k |I_a E_a| (|M_A|+|I_a|)^(2k-1)

and weighted Cauchy, (7), (14) at j=2k-1, and (15), give

 sum_{a in G_U} W ||M_A|^(2k)-|I_a|^(2k)|
                           << U^(1-d0*a0/2+epsilon).       (16)

Choose the subpower losses in (7) after k is fixed; their finite multiples
are absorbed into the epsilon in (16). No inverse moment is used to prove
(16): the crude pointwise subpower bound supplies that factor.

On the omitted set, Cauchy and (14) at j=2k show

                  sum_{a notin G_U} W |M_A|^(2k) << U^(1-c/2). (17)

Combining (14), (16), and (17), and choosing initial losses sufficiently
small, proves (2) with eta_k in (4). The margin 1-11/16 in the first-mean
error is larger than the small chosen eta_k.

On G_U, (7) makes the cap U^tau_k inactive for large U. The bad rows in (3)
contribute at most O(U^(1-c+2k tau_k))=O(U^(1-3c/4)). This proves (3),
including the convention at an actual zero. For the numerical specialization,
a_k=1/(16k), d0=1/2 and c=1/20, hence eta_k=1/(128k) and 2k tau_k=1/80.

## 6. Exact boundary toward the original research target

This is an all-FIXED-order law for actual negative L-value moments at every
fixed sigma>1/2. Unlike #976's positive numerator hierarchy, its good-family
moment scale is U with an explicit Euler constant. Unlike #931's independent
comparison model, (9)--(17) actually transfer to the arithmetic family.

It is NOT the complete native 2k-th inverse-Mobius polynomial moment at a
fixed physical height. In (2), a specific problematic character may remain
exceptional at every U. In (3), large reciprocal values and zeros are capped.
Neither a sparse exceptional set nor a capped asymptotic excludes a single
zero. There is no growing-k uniformity, boundary-line sigma=1/2 estimate,
uncapped all-member moment, pointwise RH bound, or new zero-free fraction.
These missing steps are mathematical gaps, not pending finite validation.
