# The first-circle ramification exponent over a general finite field

Status: new source theorem with independent proof review. This note is
separate from finite comparison freeze `0018b73f60e42bc793d172c381547de34322d8ca`
and infinite companion freeze `b3fde737e790e38ae15c20ce0858e72104c55550`.
The general after-completion theorem and its 3,044-source replay are pinned
at `075f9b203aefefb4a29f3279b6de1c4127093af6`; root reports all 28 tests in
both interpreter modes and all producer checks passed. This note's own
BEFORE/base replay is separate and awaits its root-run validation.

Let Q be an odd prime power of characteristic greater than3. Fix A!=0 and
4A^3+27B^2!=0. Use the actual S3 cover from

    E: u^2=x^3+Ax+B,
    D: v^2=-4A^3-27(B-u^2)^2,

and its smooth proper genus-three Galois closure Z. The previously constructed
source gives H^1(Z)=H^1(D) plus two copies of H^1(E) as Frobenius spaces.
Put a_E=tr(Frob|H^1(E)), a_D=tr(Frob|H^1(D)), and t_Z=a_D+2a_E.

The generic coherent algebra is the actual
Sym^m(Std) tensor Sym^m(Perm) tensor chi_u^m in grade m. Adjoin the same
untwisted T_n=B_n sign plus C_n Std in every positive even grade n, either
before or after extension. Both sources exist in every finite degree; their
comparison has the boundary module of the finite-source construction.

## 1. Counts must keep the ramified quadratic point separate

Among rational points of the base P1, define:

- r_+,r_-: the old simple C2 branch points u, classified by chi_Q(u)=+1,-1;
- g_+,g_-: nonzero, unramified finite u where x^3+Ax+B-u^2 splits into
  three distinct roots, classified by chi_Q(u)=+1,-1;
- g_0=1 if x^3+Ax+B splits into three distinct roots, and0 otherwise;
- g=g_++g_-+g_0 and r=r_++r_-;
- delta=1 if Q=1 modulo3 and0 otherwise.

The point u=0 is unramified for the original S3 cover, since its discriminant
is nonzero. It is ramified for chi_u and must not be assigned a quadratic
sign. Infinity is split in the original C3 inertia quotient exactly when
delta=1. The original proper closure has

    #Z(F_Q)=6g+3r+2delta,
    t_Z=Q+1-6g-3r-2delta.                                      (1.1)

Indeed a rational unramified fibre of a constant Galois S3 cover contributes
six points exactly when Frobenius is the identity. At an old branch the
normalizer of C2 is C2 itself, giving three rational points. Infinity has
two rational points in the split case and none otherwise. These count the
normalized cover, not the singular affine fibre product.

The old branch set is stable under u->-u and contains no zero, so r is even.
Also Q+1-2delta is divisible by6. Equation (1.1) therefore proves the exact
source congruence t_Z=0 modulo6 for every field in scope. In particular the
after-multiplier exponent t_Z/12 is always integral or half-integral; this
is not a regularity guessed from the phase atlas.

## 2. The local correction has a positive square-root term

Set tau=1/2 and D(z)=1-4z^2. The source multiplicities and local products
V,W,X,Y are those of `INFINITE_EXTENSION_ORDER.md`. Their analytic units
are independent of Q. Near z=tau, on the branch D^(1/2)>0 for real z<tau,
the old local ratios have the exact form

    R_+(z)=D^(-1/4)[A_+(z)+D^(1/2)B_+(z)],
    R_-(z)=D^( 1/4)[A_-(z)+D^(1/2)B_-(z)],                      (2.1)

where all four functions are holomorphic near tau and all four values at
tau are strictly positive. To check the second line, use
F_e(-z)=D/[(1+2z)(1+z)^4]; its V term is one half-power above the W term.
The first line follows directly from the positive F_e and F_s terms.
Their denominators do not vanish at tau.

Split infinity similarly gives

    R_inf+(z)=D^(-1/3)[A_inf(z)+D^(1/2)B_inf(z)],                 (2.2)

with both values positive. Nonsplit infinity instead gives the analytic,
positive unit product_even(1-z^(2n))^(-C_n) at tau.

Every nonrational old place is evaluated at z^d, d>=2. At z=tau these
arguments lie in (0,1/4], strictly inside the local convergence domain.
Both possible residue-field quadratic signs give positive factors there.
These places therefore supply analytic positive units, and do not alter
the first exponent. The new quadratic point has no extension-order defect.

It follows that the full boundary ratio has the local form

    Xi_Q(z)=D(z)^sigma U(z,D(z)^(1/2)),
    sigma=-(r_+-r_-)/4-delta/3.                                (2.3)

Here U is holomorphic in its displayed variables, U(tau,0)>0, and

    partial_2 U(tau,0)>0  if r+delta>0.                          (2.4)

For (2.4), the coefficient of the single square root in a finite product
is a sum of positive terms from (2.1)--(2.2), multiplied by positive leading
terms from every other factor. Analytic factors in z contain no square-root
term. This positivity concerns the local correction, not coefficients of
the full global arithmetic function.

## 3. The finite source has an exact integer zero order at tau

Let H_2=P_E(z^2)E_chi(z) be the finite after-source with only T2 adjoined.
Then

    ord_(z=tau) H_2=g_-,
    ord_(z=-tau) H_2=g_+.                                      (3.1)

These are finite meromorphic orders, not inferred from a sign of an infinite
Euler product outside its absolute-convergence disk.

To prove (3.1), use finite Koszul extraction on the common good open set.
Choose N large enough that Qr^(N+1)<1 for some r>tau. The remaining good
local factors are the original F_h(epsilon z^d) multiplied by finitely many
finite-monodromy determinant powers. Their high-degree product converges
normally near tau, with a nonzero tail after finitely many places have been
separated. Those auxiliary local determinants have only unit-circle roots.
The only original good factor that vanishes at tau is F_e(-z) at a rational
completely split point with negative chi; each such zero is simple. For
d>=2 the arguments have modulus at most1/4 and cannot be a zero of F_e.
The s/c class factors have no numerator zeros.

The extracted finite proper/compact cohomological factors are units at both
tau and -tau. Their eigenvalues have absolute values1, sqrt(Q), or Q,
including the degree-zero boundary eigenvalues. A zero at z=+/-1/2 in a
grade-n determinant would require an eigenvalue of absolute value2^n.
For weight1 this forces Q=2^(2n); for weight2 it forces Q=2^n; weight0 is
already impossible for n>=1. Each contradicts the odd characteristic.
For a residual degree d, the corresponding equality in absolute values is
Q^(dw/2)=2^(nd), which reduces to Q^(w/2)=2^n. Thus residue-field Frobenius
powers do not remove the obstruction.

All genuine bad A factors are positive and nonzero at tau and -tau.
At an old branch, the possibly vanishing F_e(-tau) is averaged with
F_s(tau)>0. The central quadratic factor and infinity factors retain their
even parts, which are positive. The finite generator denominators are units
there. The extra P_E(z^2) is another weight1 determinant and is a unit by
the same argument. Thus the finite residual good product supplies exactly
the orders in (3.1).

## 4. Infinite arithmetic cancellation must precede a radius statement

Write H_after,Q=H_2 K_Q. The pure multiplier K_Q adjoins all remaining T_n
and has local leading form

    K_Q(z)=D(z)^alpha A_Q(z),     alpha=t_Z/12,                  (4.1)

where A_Q is analytic and nonzero near tau after the finite initial
Frobenius factors have been separated. Equation (4.1) is the parallel
general after-completion lemma. Its source proof uses
B_n~2^n/(6n), C_n~2^n/(3n) on even grades, exponential character errors,
and a normally convergent higher-power logarithm remainder. It is not
deduced from the finite phase-atlas table.

For every compact disk |z|<=r<1/2, only finitely many possible arithmetic
poles of H_2 occur. Its imported exact divisor says they come from even
nontrivial elliptic constituents. Each denominator factor at such a point
is explicitly included, with at least that multiplicity, in a finite
initial part of K_Q. The remaining infinite product converges normally
on the disk. Thus H_after,Q is holomorphic on |z|<1/2 even for Q large
enough that the original finite H_2 had arithmetic poles inside that disk.
One must not claim that H_2 alone was holomorphic there for every Q.

For H_before,Q=H_after,Q Xi_Q, the displayed Xi denominator factors could
appear to introduce nonarithmetic poles. Restore the genuine finite bad
A factors from H_2 before continuing. Removing those factors leaves the
common-good extraction with only arithmetic cohomological poles. At
arithmetic weight points the removed bad numerators are nonzero, by the
frozen prime-support lemma: all conjugates of the inverse point have modulus
greater than1, while the relevant reciprocal numerator constants involve
only primes2 and3 and the field characteristic is greater than3. The same
finite initial K factors therefore cancel all remaining poles. The restored
local numerators and generator products converge normally for |z|<1/2.
Consequently

    H_before,Q is holomorphic on |z|<1/2.                       (4.2)

This is a statement about the actual full source. It cannot be obtained by
declaring Xi_Q itself pole-free, or by replacing the additive boundary
cokernel with its ordinary L-function.

## 5. The exact leading exponent and a first-circle criterion

Combine (2.3), (3.1) and (4.1). Near the positive point tau the before-source
has a nonzero Puiseux leading coefficient and exact leading exponent

    rho_+=g_-+t_Z/12-(r_+-r_-)/4-delta/3
          =g_-+(Q+1)/12-(g+r_++delta)/2.                         (5.1)

This is an exact local leading exponent, whereas its class modulo integers
does not require knowing g_-. At the negative point, exchange the signs:

    rho_-=g_++(Q+1)/12-(g+r_-+delta)/2.                         (5.2)

If rho_+ is nonintegral, tau is a branch point and the Taylor radius is
exactly1/2 by (4.2). If rho_+ is integral but r+delta>0, the nonzero
square-root term (2.4) still gives a branch: multiplying by the analytic
unit from H_2 and K cannot cancel its first half-integral coefficient.
Hence the same exact radius follows in that case. A negative integral
leading exponent also prevents holomorphic extension; (5.1) has already
included the finite-source zero order exactly.

In particular, if Q=1 modulo3, then Q modulo12 is1 or7. The fraction
(Q+1)/12 is congruent to1/6 or2/3 modulo integers, and subtracting a
half-integer cannot make it integral. Thus every source in this split-
infinity class has a nontrivial cubic component in its first-circle
monodromy and exact before-source Taylor radius1/2. The order need not be
three: the F49 example has exponent -29/6.

When Q=2 modulo3, no rational old branches are present, and rho_+ is a
nonnegative integer, the criterion deliberately does not assert a
singularity at tau. The first circle can be removable for the full source.
For example the declared comparison A=1,B=0 over F5 has elementary
point counts g_0=1,
g_+=g_-=r_+=r_-=0, a_E=2, a_D=-4 and rho_+=0. That is a declared
exceptional panel in the separately frozen phase atlas. Its independent
literal Python reconstruction agrees with the initial JavaScript discovery
capture; the criterion is not altered to fit that observation.

One removable class can already be described without enumeration. Suppose
Q=11 modulo12, r=0 and g_0=0. Then chi_Q(-1)=-1, while splitting of the cubic
depends only on u^2, so g_+=g_-. Both exact exponents in (5.1)--(5.2) are
(Q+1)/12, a positive integer. With no rational old branch and nonsplit
infinity, Xi_Q is an analytic unit at both points. Hence both first-circle
points are removable, with that exact positive zero order. The next section
identifies the next singularity and the exact centered Taylor disk.

## 6. The exact before-source radius has only two possibilities

The parallel after-completion theorem sharpens (4.1). After separating
finitely many Frobenius factors, its logarithm near the first two circles is

    log K_Q(z) = alpha log(1-4z^2)
       + beta log(1+2z^2) + gamma log(1-4z^4) + analytic remainder,

    alpha=t_Z/12,
    beta=(a_D-a_E)/6,
    gamma=(a_D^2+2a_E^2-6Q)/24.                                (6.1)

The remainder continues locally beyond |z|=1/sqrt(2), with the finite
Frobenius factors retained exactly. One may choose an outer radius strictly
below 2^(-1/3). This is a continued scalar identity, not a statement that
the original infinite product converges normally on that larger disk.

For clarity, its character calculation uses, in even degree n,

    dim M_n = 2^n/n - (-2)^(n/2)/n + O(2^(n/3)),
    tr(s|M_n) = -(-2)^(n/2)/n + O(2^(n/6)),
    tr(c|M_n) = O(2^(n/3)).

Consequently the first logarithmic power gives the alpha/beta terms in
(6.1); the second gives gamma. Higher powers and the stated character
errors converge beyond the second circle after a finite initial part is
removed. This summary fixes the conventions; the independent after proof
supplies the all-grade error bounds and convergence argument. It does not
use the before-source radius result below.

Write t_Z=6k. Then

    beta=k-a_E/2,
    gamma=(6k^2-4ka_E+a_E^2-Q)/4.                               (6.2)

Thus gamma is a quarter-integer. At least one of gamma and gamma+beta is
nonintegral: if a_E is odd, beta is a half-integer; if a_E is even, the
numerator in gamma is odd. The after theorem, with the independently proved
finite zero orders (3.1), yields the exact criterion

    R_after=1/sqrt(2)  iff
       g_-+alpha and g_++alpha are both nonnegative integers;
    R_after=1/2 otherwise.                                     (6.3)

Here R denotes a centered Taylor radius of the actual full source, not of
the pure multiplier K_Q. Negative integral alpha can be canceled by genuine
finite-source zeros in (3.1), which is why a criterion using alpha alone
would be false.

**Before-source theorem.** With the same hypotheses and source,

    R_before=1/sqrt(2)  iff
       r=0, delta=0, and both g_-+alpha,g_++alpha are nonnegative integers;
    R_before=1/2 otherwise.                                    (6.4)

**Proof.** If r+delta>0, Section5 already forces a first-circle branch,
including the case of an integral leading exponent. If r=delta=0, Xi_Q
is an analytic positive unit at both first-circle points, so removability
there is exactly the condition in (6.3). If that condition fails, the
before radius is1/2 by Section4. It remains to treat the removable case.

There are then no rational old branch factors and infinity is nonsplit.
For |z|<1/sqrt(2), every remaining old factor is evaluated at z^d, d>=2,
and hence lies inside its original |t|<1/2 product domain. The nonsplit
infinity factor is the exact source product

    R_inf-(z)=product_(even n>=2)(1-z^(2n))^(-C_n).              (6.5)

Its product also converges normally on that disk. Displayed denominators
of the old ratios still must be canceled using the actual bad A factors.
Do so as in Section4. The after theorem gives the holomorphic full source
on this disk; the common-good finite extraction has only arithmetic poles,
and the finite initial K factors remove all of them. Away from the two
already removed first-circle points, the after analytic continuation has
no new singular divisor there. The bad A numerators are nonzero at those
two points and at arithmetic poles. Thus dividing out the true bad A
factors does not create a pole, and restoring the before numerators proves
H_before holomorphic on |z|<1/sqrt(2).

Now take the positive second-circle point s=1/sqrt(2) and put
D_2=1-4z^4. The standard multiplicity estimate gives

    R_inf-(z)=D_2^(-1/6) A_2(z),                              (6.6)

with A_2 analytic and nonzero near s and A_2(s)>0. Indeed the linear leading
series is sum_j (4^j/(6j))z^(4j)=-(1/6)log D_2. The character error and
all higher logarithmic powers converge on a larger disk. For instance a
radius strictly below 2^(-1/4) is allowed for these remainder terms.

Let r_(2,+),r_(2,-) count the old closed places of degree two by their
residue-field quadratic signs. Applying (2.1) at t=z^2 gives respective
leading exponents -1/4,+1/4 in D_2, with positive leading constants at s.
Old places of degree at least three have positive analytic unit values
there, since s^d<1/2. Consequently the boundary ratio's second leading
exponent is

    sigma_2=-(r_(2,+)-r_(2,-))/4-1/6.                           (6.7)

The after function has leading exponent gamma plus a finite integer order
at s, by (6.1); the beta factor is nonzero there. Therefore the before
function has leading exponent

    integer + gamma - (r_(2,+)-r_(2,-))/4 - 1/6.                (6.8)

The first three terms form a quarter-integer, which cannot cancel1/6.
All the displayed local leading constants are nonzero. Thus s is a branch
point. Combined with holomorphy inside, this proves the exact radius in
the remaining case and completes (6.4). QED.

The integer in (6.8) can also be read from the finite source: it counts
good degree-two closed places with identity S3 Frobenius and negative
residue-field chi. The same finite-extraction argument as Section3 proves
this. At s, a possible extracted cohomological zero in grade n and residual
degree d would require Q^(dw/2)=2^(nd/2), again impossible in odd
characteristic for positive weight. Genuine bad numerator zeros at these
points are excluded by their reciprocal constant norm support at primes2,3;
the inverse point here has norm a power of2 and all its conjugates have
modulus greater than1. In the concrete S3 bad numerators the only nonunit
reciprocal constants are powers of3, so this last exclusion is strict.

Equations (6.3)--(6.4) prove R_before<=R_after in this specified family.
Strict inequality occurs exactly when the after first circle is removable
but at least one rational old branch or split infinity is present. The F7
example realizes that case. This is a classification for two declared
extension functors on the same generic algebra, not a statement comparing
arbitrary arithmetic completions.

All conclusions distinguish the formal degreewise algebra, its finite
cohomological multipliers, the nonlinear boundary ratio, and the analytically
continued full Euler function. No universal source uniqueness or ordinary
trace-class determinant beyond its proved domain is inferred.
