# Selected fourth moments and exceptional-character density

Status: PROPOSED complete deductions from explicitly named unconditional
inputs. No independent mathematical review or formal build has been performed.
This file proves a family fourth-moment bound and an improved exceptional-
CHARACTER count. CONTOURS.md composes them with the separately recovered
short-support theta argument. Neither finite checking nor publication certifies
an imported analytic theorem. No RH, GRH, native critical moment, or unknown
signed-covariance estimate is assumed. Classical AFE, Holder and zero-detection
methods are credited; no exhaustive literature-priority claim is made.

## 1. Exact family and external inputs

Fix a number field F containing mu_6 and the fixed permissible data of de
Faveri (DF), arXiv:2610.04045v1, Sections 2.1--2.5. Let I(S) be the nonzero
integral ideals coprime to the fixed S. A flat sum means SIXTH-POWER-FREE
ideals, with every prime valuation in {0,...,5}. It does not mean squarefree,
radical ordered, or conductor ordered. The index is the FULL ideal norm.
The actual Hecke character is chi_a, extended by zero at its nonunits.
Allow one fixed finite-order Hecke twist psi of S-supported conductor.
All constants retain F,S,psi and generator-choice dependence.

For outside-S primes dividing a, the local order of chi_a is nontrivial;
hence its primitive conductor outside S is rad(a), and its total conductor
is O_(F,S,psi)(Na). The finite S-type list and archimedean types are fixed.
Consequently the classical approximate functional equation (AFE) has length
O(U^(1/2+eta)(2+|t|)^C_F) on Na<=U. The proof below allows all AFE columns
and both the original and dual sums. It does not discard ramified masks.

The load-bearing imported analytic estimates are:

(LS) DF Theorem 1.1, at n=6, for arbitrary coefficients on flat columns:

  sum_(Na<=U)^flat |sum_(Nb<=V)^flat lambda_b chi_a(b)|^2
    <= C_eta (UV)^eta V_6(U,V) sum_b |lambda_b|^2,
  V_6(U,V)=U+V+U^(5/6)V^(1/3)+U^(1/3)V^(5/6).             (1)

Fixed twists multiply column coefficients by psi(b). Positive restrictions
on rows are allowed. No distribution or independence of the coefficients
relative to the selected row set is assumed.

(M2) BGL, arXiv:1112.1650, Section 5 equation (5.1), retaining the flat part
and the fixed twist by the same AFE argument:

  sum_(Na<=U)^flat |L_F^S(1/2+it,psi chi_a)|^2
    <= C_eta U^(1+eta)(2+|t|)^C_F.                       (2)

(ZD) The analytic zero detector BEFORE its first Cauchy step is BGL (5.3).
DF Section 9, proof of Corollary 1.5, makes it valid on the full flat family
and substitutes (1) in its Dirichlet-polynomial means. Its rowwise proof
also permits retaining an arbitrary subset E of the rows. We explicitly
use that pre-Cauchy form, not DF's final exponent as a stronger black box.
Section 3 writes the exact inequality used. The elementary inequalities
below do not prove (LS), the AFE, or the analytic zero detector.

The incomplete L^S and the inducing primitive L have the same zeros at
positive real part except possible finite Euler zeros on Re s=0, outside
our domains. Fixed S Euler factors change constants and polynomial height
bounds. Whenever the inducing character is principal, omit that row in a
zero count; its central value causes no difficulty in (2) or Theorem A.

## 2. Fourth moment with the complete column support

**Theorem A.** For U>=2, t real and every eta>0,

  sum_(Na<=U)^flat |L_F^S(1/2+it,psi chi_a)|^4
    <= C_eta U^(7/6+eta)(2+|t|)^C_(F,eta).              (3)

The height exponent is not optimized. The power 7/6 concerns the numerator
L-family, not the native inverse-L/Mobius moment sought in the RH programme.

**Proof.** The AFE supplies two smooth Dirichlet polynomials of length at
most L=U^(1/2+delta)(2+|t|)^C with rapidly decreasing tails. Mellin inversion
of the smooth weights separates their row-dependent conductor arguments.
Move each Mellin line to a fixed small positive delta. The modulus of the
conductor factor costs U^O(delta)(2+|t|)^C. The Mellin kernels have integrable
polynomially weighted absolute norms; truncated dyadic tail intervals cost
arbitrarily high negative powers. This also separates varying endpoints.
One does not take a supremum of a polynomial with arbitrary coefficients
chosen separately for each row. After this separation the coefficient
arrays are common across the rows. The finite gamma/S types are subdivided.
The dual root number has modulus one and disappears on bounding the two
AFE summands separately via |x+y|^4<=8(|x|^4+|y|^4).

Square either separated polynomial. Complete multiplicativity, including
zeros, gives a single character chi_a(b) at the product ideal b. Its norm
is at most V=L^2 and its coefficient has absolute value
O_delta((Nb)^(-1/2+delta)); the divisor factor d_2(b) is absorbed by a smaller
positive delta. This is an identity of ideals, not a collapse of distinct
ideals having equal rational norm. There is NO coprimality requirement on
the two original factors of b.

The product column b need not be flat. Write uniquely b=c d^6 with c flat.
Here (c,d)=1 is NOT required: at a prime the exponents 7,13,... leave the
same prime in c and d. The character identity is exactly

  (psi chi_a)(c d^6)
    =psi(c)psi(d)^6 chi_a(c) 1_((a,d)=1),               (4)

with the original S exclusions retained. The last factor is a ROW mask;
it is never replaced by one or by a restriction (c,d)=1. Fix d and use
Minkowski in the row l^2 norm. From (1), the norm of its c-polynomial is
at most

  C_delta (UV)^O(delta) (Nd)^(-3+O(delta))
                         V_6(U,V/(Nd)^6)^(1/2).

The coefficient-square sum over c is at most V^O(delta), by fixed-field
ideal counting and partial summation. Dropping the positive row restriction
in (4) is legitimate for this norm estimate. Since V_6 is increasing in
its second argument and sum_d (Nd)^(-3+O(delta)) converges, summing d costs
a constant, even with its full tail. Therefore the squared row norm of the
squared original polynomial is

  <= C_delta (UV)^O(delta) V_6(U,V).                    (5)

At V<=U^(1+O(delta))(2+|t|)^C the four norm exponents in (5) are 1,1,7/6,7/6.
The Mellin integrals and dyadic tails only change U^O(delta) and the displayed
polynomial height factor. Choose delta sufficiently small for the prescribed
eta. This proves (3). The proof treats the original and conjugate families
identically. QED.

**Corollary A1 (any selected class).** If E is any set of at most U^nu rows,
0<=nu<=1, then, up to U^eta and polynomial height factors,

  sum_(a in E) |L(1/2+it,psi chi_a)|
    <= min(U^((nu+1)/2), U^(3nu/4+7/24), U^(nu+1/4)).  (6)

The three alternatives are respectively (2) and Cauchy, (3) and Holder,
and individual convexity. The fourth-moment bound improves the other two
when 1/6<nu<5/6. It applies to a set selected using zeros of the denominator:
there is no independence assertion. All three alternatives remain available.

## 3. Keep the unknown exceptional count inside the detector

Let E=E(U,sigma,T) consist of the nonprincipal flat indices Na<=U for which
the inducing L(s,psi chi_a) has a zero with Re s>=sigma, |Im s|<=T. Write
R=|E|. Fix 1/2<sigma<1 and 1<=A<=B; put

  M_A(s,chi)=sum_(Nb<=A) mu_F(b)chi(b)(Nb)^(-s).

This mollifier is squarefree, hence already flat. In BGL (5.3) retain only
the rows E before applying any norm estimate. Its left side is at least R.
The detector is obtained for the individual rows/zeros, then summed. Thus
inserting a row indicator does not require a uniformity assumption about
how E was chosen. Any negligible rowwise detection errors can be made
O(U^-2), and absorbed. The supremum over common ordinates and dyadic column
lengths remains OUTSIDE the positive row sums exactly as in (5.3).

The first mean in that detector is sum_E |L(1/2+it) M_A(1/2+it)|. Apply
Holder with exponents (4,2,4), retaining the counting factor:

  sum_E |L M_A|
    <= R^(1/4) (sum_all |L|^4)^(1/4)
                           (sum_all |M_A|^2)^(1/2)
    <= C_eta R^(1/4) U^(7/24+eta)
                          V_6(U,A)^(1/2)(2+|t|)^C.     (7)

The mollifier coefficient-square sum is logarithmic and is absorbed in
U^eta A^eta. Using R<=U too early would lose the improvement.

For the second detector mean, retain DF's complete-column estimate. One
may also verify it directly: decompose each complete column b=c d^6 as in
(4), use (1) for c, then Minkowski and sum_d (Nd)^(-3+eta). For coefficients
bounded by (Nb)^eta on Nb~V, this gives O((UV)^eta V V_6(U,V)). Thus every
remaining term in DF's detector calculation is retained. We obtain

  R <= C_eta (UABT)^eta T { B^(1/2-sigma) R^(1/4)
            U^(7/24) (2+T)^C V_6(U,A)^(1/2)
       + B^(2-2sigma)+U A^(1-2sigma)
       + sup_(A<=V<=B)[U^(1/3)V^(11/6-2sigma)
                         +U^(5/6)V^(4/3-2sigma)] }.    (8)

This is an improved EXCEPTIONAL-CHARACTER count. We do not claim here an
optimized height exponent or a stronger total-zero-count theorem. The
outside analytic detector, which underlies (8), is stated unconditionally
in BGL/DF; it is not a hypothesized reciprocal-L moment.

If r<=a r^(1/4)+b with a,b,r>=0, either r<=2b or r<=(2a)^(4/3).
Apply this elementary implication to (8), with A=U^a, B=U^b. Let g4 be the
maximum of the following TEN exact norm exponents:

  7/18+(2/3)c*a+(2/3)d+((2-4sigma)/3)b,
       for (c,d)=(1,0),(0,1),(1/3,5/6),(5/6,1/3);
  (2-2sigma)b; 1+(1-2sigma)a;
  1/3+(11/6-2sigma)v, for v=a,b;
  5/6+(4/3-2sigma)v, for v=a,b.                        (9)

Then (8) proves R<=C_eta U^(g4+eta)(2+T)^C for some fixed C. Renaming eta
absorbs all finite multiples of the initial loss. In particular for every
eta>0 there is a fixed rho>0 such that T=4U^rho gives R<<U^(g4+eta).
The field, sigma, a,b are fixed when rho is chosen. For finitely many such
choices one rho works for all; no uniformity near a moving sigma is needed.

**Theorem B (explicit improvement at three quarters).** Set

  sigma=3/4, A=U^(7/10), B=U^(23/20).

The largest term of V_6(U,A) is U^(16/15). Before solving for R, the exponent
of its coefficient in (8) is

  -23/80+7/24+8/15=43/80.

After the power 4/3 the exponent is 43/60. Both endpoints of both supremum
monomials, and the two other terms, are at most 43/60; the active supremum
terms equal it. Therefore

  #E(U,3/4,4U^rho) <<_eta U^(43/60+eta)                 (10)

for suitably fixed rho>0. DF's displayed bound at this sigma gives 8/11
(up to a height loss); 8/11-43/60=7/660>0. This comparison is of the norm
exponents at small polynomial height, not a claim about matching optimal
T dependence. The counting theorem is independent of the CT theta argument.

For the further finite sigma values in strata.json we use

  D_sigma=36sigma^2-75sigma+31,
  a=-(48sigma-29)/(2D_sigma),
  b=-(33sigma-19)/D_sigma,
  g4=(468sigma^2-741sigma+271)/(6D_sigma).              (11)

Every used instance satisfies 0<=a<=b, and all ten expressions (9) are <=g4.
The checker verifies these as exact rational inequalities for EACH named
threshold. No global validity range or optimality is inferred from an
optimizer. At the final threshold we instead use DF's original detector
and its explicit high-sigma substitution, recorded in the same table.

## 4. Scope and precise remaining work

The analytic addition is (3), (7)--(10), and their specified family adapter.
The four-moment inequality is a direct consequence of DF's sieve with full
columns, not claimed as a new general moment method. The retained unknown
count in (7) supplies the extra density improvement. The later all-field
consequence in CONTOURS.md additionally depends on the recovered Theorem R
and CT's analytic identities. This file alone proves no new Dedekind boundary.

No assertion here concerns the original fixed-principal-twist critical
Mobius covariance or the cofinal native moment hierarchy. Higher fixed
numerator moments could be considered, but no saving is obtained by calling
them native inverse-L moments or assuming growing-order constants. Neither
BGL, DF nor CT is asserted to have been independently rebuilt in this pass.
