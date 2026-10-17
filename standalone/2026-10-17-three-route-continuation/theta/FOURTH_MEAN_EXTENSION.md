# Fourth-mean interpolation reaches the proposed 49/54 boundary

Status: **PROPOSED complete composition from stated unconditional analytic inputs.**
This is a separate extension of THETA_COMPARISON.md. It adds the numerator
fourth-moment deduction in concurrent PR #966, then supplies a new interpolation
and complete comparison. It does not use #966's new selected-character density
theorem. No RH, unknown inverse-L moment, or signed physical projection estimate
is assumed. Independent mathematical review of the imported analytic foundations
remains necessary; exact rational bookkeeping does not provide that review.

Scope: for each fixed number field K, the proposed strict half-plane is

    zeta_K(s) != 0 for Re s>49/54, s!=1,

with the corresponding finite-order Hecke conclusion. Constants may depend on
the field, character and distance from the boundary. No boundary-line claim,
infinite-order character extension, or full RH proof is made.

Exact added source: PR #966, commit
`8d94494698ee447711a53dec922986586418e398`,
`standalone/2026-10-17-selected-fourth-density/PROOF.md`, Theorem A.
The original second-mean-only 9081/10000 argument remains independent of this
source. The other source interfaces are those frozen from #965 at
`d58e3282a9379b6ae165681bc2e21e4f9fd18c26` in THETA_COMPARISON.md.

## 1. The added fourth mean and its precise analytic dependencies

Let F contain mu_6. Use the full sixth-power-free ideal family of de Faveri,
arXiv:2610.04045v1, with the same fixed choices and local classes. Its indices
are ideals a with all valuations at most five, ordered by their FULL norm.
Keep the original zero extension at nonunits and any fixed finite-order
S-supported twist psi. The primitive conductor is O(Na), and the finite
archimedean and S-type lists are fixed.

The imported sieve, de Faveri Theorem 1.1 at n=6, has constant

    V_6(U,V)=U+V+U^(5/6)V^(1/3)+U^(1/3)V^(5/6)

for arbitrary common coefficient arrays on sixth-power-free columns. Its
norm bound includes the usual (UV)^eta loss. Together with the classical
approximate functional equation it gives the deduction from #966:

    sum_(Na<=U)^flat |L_F^S(1/2+it,psi chi_a)|^4
        <<_eta U^(7/6+eta)(2+|t|)^C.                      (1.1)

Here is the full reduction, to make the added dependency inspectable. Each
of the two approximate-functional-equation sums has effective length
L<=U^(1/2+delta)(2+|t|)^C, with rapidly decreasing tails. Mellin inversion
separates the conductor-dependent weights into common column coefficients
and row factors. On a small fixed positive Mellin line, the row factors
cost U^O(delta) and polynomial height factors. Their phases have modulus
one; the kernels have integrable norms after any needed polynomial height
weight. Split the finite gamma/S types. Bound the two AFE sums separately
using |P+Q|^4<=8(|P|^4+|Q|^4), so the dual root number costs no norm.

The square of a common polynomial is again a character polynomial, by
complete multiplicativity including the zero values. Its product column b
has norm at most V=L^2. Its coefficient has modulus at most
(Nb)^(-1/2+O(delta)); the divisor count is absorbed into the arbitrarily
small exponent. Distinct ideals with the same rational norm are still
distinct columns. The two factors of b need not be coprime.

Write every complete column uniquely as b=c d^6 with c sixth-power-free.
The factors c and d may share primes. The identity is

    (psi chi_a)(c d^6)
        =psi(c)psi(d)^6 chi_a(c) 1_((a,d)=1).             (1.2)

For each fixed d, the last factor is a positive restriction of the row set,
and it can be dropped when applying the sieve to that row norm. It cannot
be deleted from the character identity. The squared coefficient sum in c
costs V^O(delta), while the d factor is (Nd)^(-3+O(delta)) before squaring
the norm. Minkowski and the sieve therefore give

    || squared polynomial ||_(ell^2 in a)
        << (UV)^O(delta) sum_d (Nd)^(-3+O(delta))
                    V_6(U,V/(Nd)^6)^(1/2)
        << (UV)^O(delta) V_6(U,V)^(1/2).                 (1.3)

The full d sum converges. Columns with length below one are empty; AFE
dyadic tails beyond the effective length are paid by their original rapid
decay, with no truncation of the source. At V<=U^(1+O(delta))(2+|t|)^C,
the four U exponents in V_6 are at most 7/6+O(delta). Squaring (1.3),
integrating the separated kernels, and choosing delta after eta proves
(1.1) from the displayed sieve and AFE. The conjugate family has the same
argument. This reproduces the deduction credited to #966; it does not
claim a new sieve or a worldwide priority for this fourth-moment method.

The CT application still uses #965's choice-compatible identification with
these ideal families and finitely many twists. The fourth mean concerns
the numerator L-family. It is not a moment for the native reciprocal or
for the signed principal Poisson term.

## 2. New interpolation of the fourth mean

For a finite vector of the actual nonprincipal numerator functions, the
Euler product gives a uniform ell-infinity bound at Re s=1+delta, and
(1.1) gives its ell-four norm at Re s=1/2. All functions are holomorphic
in this strip and have polynomial vertical growth. Fixed omissions are
retained. Let 1/2<sigma<1 and put

    theta_delta=(sigma-1/2)/(1/2+delta),
    p_delta=4/(1-theta_delta), p_delta'=4/(3+theta_delta).

For any vector c of ell-p_delta'-norm one, choose analytic dual weights

    b_j(v)=phase(c_j) |c_j|^(p_delta' (3+v)/4),

with b_j=0 if c_j=0. Their ell-4/3 norm on Re v=0 is one, their ell-one
norm on Re v=1 is one, and b_j(theta_delta)=c_j. Apply three lines to
the scalar sum of b_j(v)L_j(1/2+(1/2+delta)v+it), multiplied by
exp(kappa(v-theta_delta)^2). This fixed Gaussian makes the polynomial
height bounds integrable and leaves the value at theta_delta unchanged.
Holder on the left and the Euler bound on the right yield, by duality,

    ||L_j(sigma+it)||_(p_delta)
        << U^((7/6+eta)/p_delta)(2+|t|)^C.               (2.1)

Take p=2/(1-sigma). Then p_delta<p, so ell-p norm is at most ell-p_delta
norm. Choose one fixed delta sufficiently small for each prescribed final
loss. The difference between 1/p_delta and (1-sigma)/2 tends to zero.
Consequently

    ||L_j(sigma+it)||_p
        << U^((7/12)(1-sigma)+eta)(2+|t|)^C.             (2.2)

This is exactly the finite-vector proof in the critical interpolation
component with the left norm changed to four and its exponent to 7/6.
No maximum or row-specific choice of coefficients is substituted for a
family norm.

Let E be ANY subset with at most U^nu members. Holder in (2.2), followed
by the primitive functional equation at 0<y<1/2, proves

    sum_(j in E) |L_j(y+it)|
       << U^(1/2+nu-y*(5/12+nu/2)+eta)(2+|t|)^C.        (2.3)

Indeed, the upper-line subset exponent at sigma=1-y is
nu(1-y/2)+(7/12)y. Reflection costs U^(1/2-y). The ratio of the literal
imprimitive Euler products costs only U^eta on each fixed positive line,
by the proof in ../critical/INTERPOLATED_NUMERATOR.md. The conductor cost
is essential. At y=1/2 formula (2.3) agrees with direct Holder on (1.1):

    sum_E |L_j(1/2+it)| << U^(3nu/4+7/24+eta)(2+|t|)^C.

The new reflected exponent improves the second-mean reflected exponent
by y(5/6-nu)/2 when nu<5/6. It improves individual convexity by
y(nu-1/6)/2 when nu>1/6. These statements hold even for subsets defined
by denominator zeros. They require no statistical independence.

## 3. Limiting scales and the unchanged physical theorem

Take the fixed scales

    a=4/9, h=5/9, X=Y=Z^a, M=8/9,
    theta=a/2=2/9, b=5/6-a/3=37/54,
    b+theta=49/54.                                      (3.1)

Use the complete #965 reflected bound Z^eta(T+T^2/Z), T=XY, and the
unchanged additive bound 1/X+1/Y. Since M<1, they give

    |I(X,Y,Z)| << Z^(theta+eta).                         (3.2)

The detector is the same actual residue with the correctly changed shift:

    f(Z)=(1/(2 pi i)) integral_(2) Z^(s-b)
             exp((s-5/6)^2) H(s)/zeta_F^S(s) ds.         (3.3)

Its principal correction H is the inherited one, nonzero on Re s>2/3.
There is no insertion of a previously proposed zero-free conclusion.

## 4. Complete fixed partition using the ORIGINAL density theorem

Fix 0<e<=10^(-6), z0=2/5, kappa=1/1000. Use the 1641 thresholds

    sigma_j=(4000+j)/6000, j=0,...,1640,

from 2/3 to 47/50. Let E_j(U) be the nested exceptional sets defined in
THETA_COMPARISON.md: denominator zeros with real part at least sigma_j
and height at most 4U^rho, for U<=Nu<2U. Choose rho and the density loss
after e and this finite grid, so that

    #E_j(U) <<_e U^(g(sigma_j)+e).                       (4.1)

Here g is precisely the ORIGINAL de Faveri Corollary 1.5 exponent, including
its endpoint value g(2/3)=5/6. No estimate from #966 Theorem B or its new
zero detector is used. The checker rederives all ten original norm/height
monomials at every threshold, including the endpoint 2/3.

For Z^kappa<U<=Z^(h+e), the 1642 disjoint classes have these lines:

| Class | Count nu | x=Re xi | y=Re w | Numerator |
|---|---|---|---|---|
| Outside E_0 | 1 | 2/3+e | 1/2 | Original second mean |
| E_j minus E_(j+1), sigma_j<3/4 | g(sigma_j)+e | sigma_(j+1)+e | 1/2 | Fourth mean |
| E_j minus E_(j+1), sigma_j>=3/4 | g(sigma_j)+e | sigma_(j+1)+e | 1-sigma_(j+1)+e | Interpolated fourth mean |
| E_1640 | g(47/50)+e | 1+e | e | Individual convexity |

The 500 first middle classes use the fourth mean; the other 1140 use (2.3).
Each middle class is counted at its lower threshold and moved only past
its upper threshold. The same analytic-logarithm and reciprocal argument
from the independent second-mean comparison applies. It requires a fixed
positive gap, not sigma_0 strictly greater than 2/3: the actual first
contour is 2/3+e. The final class stays on the reciprocal Euler line.

The real-domain inequalities for the original correction remain

    x,y,z>0; 6z+y>1; x+6z>1; x+y>1; x+y+6z>2;
    6x+6z>5; x>1/2; 3x>2; 3x+y>5/2.                    (4.2)

Start at (1+e,1+e,z0), move xi to the stated x on the zero-free rectangle,
then w to y. Every intermediate corner lies in (4.2), so all joining
segments do by convexity. Nonprincipal numerator L-functions are entire.
There is no pole at w=1 for these rows, and z0 stays right of 1/6.

Define E(x,y,z)=a/2+x-1+h z+a(y-1). The U exponents, after the reciprocal
and correction losses, are respectively

    (nu+1)/2-z0,
    3nu/4+7/24-z0,
    1/2+nu-y*(5/12+nu/2)-z0,
    nu+(1-y)/2-z0.                                     (4.3)

All are positive. Thus their worst dyad is U=Z^(h+e). The exact checker
proves, on the WHOLE e interval and for all 1642 classes,

    E(x,y,z0)+(h+e)R <= theta+4e.                       (4.4)

The good-class growth is theta+(8/5)e. It ties theta at e=0, which is
allowed because the actual contours have e>0 and the final half-plane is
obtained with arbitrarily small fixed losses. The smallest middle-class
constant margin is

    118384121/35223109200 > 0,

at lower threshold 4801/6000 and upper threshold 2401/3000. Its growth
polynomial, in increasing degree, has exact coefficients

    7708973479/35223109200,
    1837711531/863311500,
    -2243892001/19568394000,
    -1/2.

The checker uses nonnegative Bernstein coefficients to verify the full
interval inequalities, rather than sampling e. The density and domain
checks remain separate gates. Fixed polynomial height factors are absorbed
by the original joint Gaussian/Schwartz weights after their needed orders
are known. No unproved height independence is used.

## 5. Principal terms, the necessary small-norm change, and all tails

Keep principal xi on 1+e. Take the w=1 residue, then the z=1/6 residue in
that term, exactly as before. The double residue is c0 f with c0 nonzero.
The principal w remainder at (x,y,z)=(1+e,1/2,1/6+e) has exponent

    5/54+(14/9)e.

The principal z remainder at (1+e,1,e) has exponent

    2/9+(14/9)e.

All these contour paths satisfy (4.2). Principal xi never moves left of
one, so the comparison is not circular.

For small nonprincipal U<=Z^kappa, change z from z0 to z_small=1/3,
keeping x=1+e and y=1/2. This segment remains in (4.2), and crosses no
zeta(6z) pole. With the full row count and individual convexity, its power is

    E(1+e,1/2,1/3)+kappa*(5/4-1/3)
        =20099/108000+e < theta+4e.                    (5.1)

This is a substantive contour correction: keeping z=2/5 would give
theta+17/20000+e, which is too large as e tends to zero. Shrinking a fixed
positive small-norm cutoff alone would not cure that limiting tie.

For intermediate horizontal edges and original-line xi tails, the same
joint weight argument applies. Since U>Z^(1/1000) and U<Z^(14/25), the
coarse Z^2 U^2 cost is defeated by any sufficiently large fixed decay order,
for example net order greater than 6000/rho after all polynomial height
factors. The nearly cancelling direction Im z approximately -Im xi is
paid with z-Schwartz decay. These complete tails contribute O(Z^-1).

For U>Z^(h+e), use the initial x=y=4 lines and z=L=10/e+2. Absolute
convergence gives U^(1-L+eta). At the first dyad the exponent is exactly

    a/2+3+3a+hL+(h+e)(1-L)=-44/9-e.                   (5.2)

The remaining dyads decay geometrically. The positive e cutoff gap is
retained, L is fixed after e, and the rightward z shift crosses no pole.

Choose all remaining mean, correction, reciprocal, norm-conversion and
dyadic losses with combined Z cost less than e. Equations (3.2), (4.4),
and (5.1)--(5.2), with the principal terms, prove the proposed comparison

    I(X,Y,Z)=c0 f(Z)+O_e(Z^(2/9+5e)),
    f(Z) <<_e Z^(2/9+5e).                              (5.3)

This accounts for bounded norms, all intermediate classes, every principal
remainder, horizontal/original-line tails, and the entire large-norm range.

## 6. Mellin conclusion and the precise limit reached

The detector is flat at zero by shifting its original right line farther
right. Its Mellin integral is therefore holomorphic for

    Re s>b+2/9+5e=49/54+5e.

On an initial right half-plane it equals
exp((s-5/6)^2)H(s)/zeta_F^S(s). The inherited nonvanishing of H on
Re s>2/3 then rules out denominator zeros in this region. For each point
with Re s>49/54, choose one fixed e with 5e below its distance to the
boundary. No uniform constant as e tends to zero, or boundary-line claim,
is required. The abelian extension K(mu_12)/K and finite-order class-field
factorization give the same descent as in THETA_COMPARISON.md, including
the classical nonvanishing at one and the fixed Euler omissions.

The improvement over the independent 9081/10000 composition is
187/270000, and over #966's 109/120 composition is 1/1080. The new ingredient
in this extension is the interpolation of the fourth mean, with the small-
norm contour moved to retain a strict margin. It reaches the lower limit
49/54 of this balanced comparison's good-class budget. This is not a
universal obstruction to other theta arguments, nor a mechanism approaching
the critical line by scalar optimization.

The full native signed first-transverse estimate, Newton coarse-amplitude
saving, and cofinal Lee--Yang realization remain open. None follows from
the numerator means in this note.

## 7. Verification boundary

`verify_fourth.py` imports only exact rational bookkeeping utilities and
the original DF detector formulas from `verify_theta.py`. It reconstructs
all 1642 class powers and all 1641 threshold detector monomials. It checks
the entire e interval, all real-domain corners, principal remainders,
small/large ranges, the conductor identity and the limiting Mellin shift.
Explicit failing checks remain active under optimized Python.

Its corruptions test removal of the new fourth mean, omitted conductor
cost, upper-threshold counting, retention of the old small z line, the old
Mellin shift and deletion of the positive large-tail gap. The output is
finite bookkeeping. The analytic sieve, the AFE, the character adapter,
the theta/Poisson foundations and the reflection theorem must be assessed
from their stated sources and proofs.
