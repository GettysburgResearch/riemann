# A proposed 9081/10000 boundary from interpolated numerator means

Status: PROPOSED composition of stated unconditional analytic inputs. The new finite-family interpolation theorem has a complete proof in ../critical/INTERPOLATED_NUMERATOR.md. The global conclusion requires the CT/OpenAI theta and Poisson foundations, the actual-family BGL mean, the de Faveri density theorem, and the subcritical reconstruction in #965. Those are explicitly imported, not recertified by a rational checker. No RH, unknown native moment, or open signed estimate is an assumption.

Scope: each fixed number field and each fixed finite-order Hecke character, with field-, character-, and boundary-distance-dependent constants. No infinite-order angular extension, boundary-line assertion, or full RH proof is made.

Exact parent: PR #965, d58e3282a9379b6ae165681bc2e21e4f9fd18c26, standalone/2026-10-17-subcritical-dedekind/PROOF.md. The earlier proposed 91/100 conclusion is not used as an input.

## 1. Conclusion and the genuinely new estimate

The proposed conclusion is

    zeta_K(s) != 0 for Re(s)>9081/10000, s!=1,

for every fixed number field K, and the corresponding open half-plane for finite-order Hecke L-functions.

The difference from #965 is 91/100-9081/10000=19/10000. The new analytic ingredient is not a new zero-density theorem. For the actual nonprincipal Poisson family, ordered by full norm U<=Nu<2U, and ANY subset E with #E << U^nu, the new component proves

    sum_(u in E) |L_F^S(y+it,chi_u)|
        << U^(1/2+nu(1-y)+eta) (1+|t|)^C,   0<y<1/2,       (1.1)

for every later fixed eta>0. Its hypotheses include the actual central BGL mean, the literal Euler omissions, and conductors O(U). The subset may be selected by denominator zeros. There is no independence assumption.

The proof first interpolates the vector of numerator functions between its ell^2 bound at real part 1/2 and its Euler ell^infinity bound at 1+delta, and then uses the primitive functional equation. Every imprimitive Euler factor is restored through a U^eta ratio. The conductor factor U^(1/2-y) is essential. In contrast, the earlier individual-convexity numerator exponent was nu+(1-y)/2. The gain in (1.1) is y(nu-1/2), so we keep individual convexity where it is better.

The finite-family theorem is an unconditional implication from its displayed central-mean hypothesis. Its application to the CT family imports the choice-compatible family identification and central mean in #965 Section 3.2. No mean for reciprocal L-functions is asserted.

## 2. Source interfaces retained from #965

Fix F containing mu_12, its S, allowed generators, local classes, measures and smooth profiles as in CT version 2. Fix them before choosing any small loss. All norms in the Poisson family are full exterior ideal norms.

The source interfaces used below are:

1. The exact original average I(X,Y,Z) and the additive estimate
       sum_m |A_t(m;X,Y)|^2 << 1/X+1/Y.
2. The complete reflected physical second moment, reconstructed in #965 Section 2:
       sum_(Nm << T, balanced shape) |B_m(Z)|^2
           << Z^eta (T+T^2/Z),      T=Z^M, any fixed M>0.  (2.1)
3. The exact triple Poisson integral, with its weight monomial
       X^(1/2-z) Z^(xi+z-1) Y^(w-1) (Nu)^(-z),
   numerator zeta_F^S(6z)L_F^S(w,chi_u), denominator
   L_F^S(xi,bar chi_u), and correction H_u(xi,w,z).
4. The correction domain, writing x=Re xi, y=Re w, z=Re z:
       x,y,z>0; 6z+y>1; x+6z>1; x+y>1; x+y+6z>2;
       6x+6z>5; x>1/2; 3x>2; 3x+y>5/2.                  (2.2)
   On each fixed-margin subdomain, H_u costs (Nu)^eta and fixed polynomial height factors.
5. The joint smoothing bound
       exp[-(Im xi+Im z)^2](1+|Im z|)^(-A)(1+|Im w|)^(-A),
   with arbitrarily large fixed A. Gaussian decay in xi alone is not assumed.
6. The unique principal row u=1; the nonzero double-residue constant c0;
   and the unchanged principal correction H(s), holomorphic and nonzero
   on Re s>2/3.
7. The actual-family central numerator mean and the sixth-free zero-density
   theorem with exponent g(sigma)=1-delta_6(sigma), including the fixed
   S-unit twists and literal common-prime zeros.

The complete reflected estimate (2.1) is important here. It keeps the T term when T<Z. Its proof in #965 retains every squarefree c, cube variable n, local a_f and powerful h: the two n sums have exponents 1+3b/2 and 5/2+3b/2 for a fixed positive b. The dyadic profile summation is valid also at effective length below one. We use that proof at its stated general M, not the earlier simplified bound T^2/Z.

For provenance, CT Proposition 8.3, (8.15)--(8.16), (9.2)--(9.3), and Sections 10--11 were compared with these interfaces in the primary PDF. This does not rebuild the metaplectic foundation. The full character adapter and density detector remain the review obligations documented by #965.

## 3. Scales, principal normalization, and the physical bound

Choose

    a=2243/5000,  h=1-a=2757/5000,
    X=Y=Z^a,      M=2a=2243/2500<1,
    theta=a/2=2243/10000,
    b=5/6-a/3=3419/5000.                                  (3.1)

Combining (2.1) with the additive estimate gives

    |I(X,Y,Z)| << Z^eta [(XY+(XY)^2/Z)(1/X+1/Y)]^(1/2)
               << Z^(theta+eta).                          (3.2)

The literal principal detector at these scales is

    f(Z)=(1/(2 pi i)) integral_(2)
          Z^(s-b) exp((s-5/6)^2) H(s)/zeta_F^S(s) ds.       (3.3)

The shift b comes from the ORIGINAL factor X^(1/2-z) at z=1/6. It must change when a changes; retaining #965's 17/25 would be an error. The principal residue is c0 f(Z), with c0 nonzero and independent of Z.

Moving the defining line right shows that f is flat at zero. The objective is an upper bound of order Z^(theta+arbitrarily small loss) at infinity.

## 4. A finite, complete density partition

Let 0<e<=10^(-6) be fixed. Put

    z0=2/5,  kappa=1/1000,
    sigma_j=(6728+j)/10000,   j=0,...,2672.                (4.1)

Thus sigma_0=841/1250 and sigma_2672=47/50. The grid and its size are fixed independently of Z and e.

For a dyad U<=Nu<2U, let E_j(U) consist of rows whose primitive denominator has a zero with real part at least sigma_j and absolute imaginary part at most 4U^rho. Choose rho>0 small after e and the finitely many density-height powers have been fixed. Then choose the density loss. The imported detector gives

    #E_j(U) <<_e U^(g(sigma_j)+e).                         (4.2)

The E_j are nested and fixed before the later reciprocal and interpolation losses. The analytic logarithm, Borel--Caratheodory, and three-circles argument from #965 gives, on the complement of E_j,

    |1/L_F^S(x+it,bar chi_u)| <<_(e,eta) U^eta,
    sigma_j+e<=x<=1+e, |t|<=2U^rho,                       (4.3)

for every later eta>0. The disks have radii 2-sigma_j-e/4, 2-sigma_j-e/2, 2-sigma_j-e and 1-e/4 around 2+it. Their inclusions and strict gaps are retained. Omitted Euler factors have no zeros at positive real part. Any strict/non-strict convention for the density count can be reconciled by a prior infinitesimal threshold change inside the density-loss allowance.

For Z^kappa<U<=Z^(h+e), use all 2674 disjoint classes:

| Class | Count exponent nu | xi line x | w line y | Numerator estimate |
|---|---|---|---|---|
| Outside E_0 | 1 | sigma_0+e | 1/2 | Central mean and Cauchy |
| E_j minus E_(j+1), sigma_j<69/100 | g(sigma_j)+e | sigma_(j+1)+e | 1/2 | Central mean and Cauchy |
| E_j minus E_(j+1), 69/100<=sigma_j<86/100 | g(sigma_j)+e | sigma_(j+1)+e | max(1-sigma_(j+1),5/2-3sigma_(j+1))+e | Interpolated reflected mean (1.1) |
| E_j minus E_(j+1), sigma_j>=86/100 | g(sigma_j)+e | sigma_(j+1)+e | 1-sigma_(j+1)+e | Individual convexity |
| E_2672 | g(47/50)+e | 1+e | e | Individual convexity |

Every middle class is counted at its LOWER threshold and shifted only past its UPPER threshold. The grid is a simple way of making the comparison finite and auditable; it is not additional analytic cancellation. The new ingredient is (1.1).

Start at (1+e,1+e,z0), move xi to x using (4.3), and then w to y. Every vertex and segment is inside (2.2); the domain is convex. All nonprincipal numerator functions are entire. No denominator zero is crossed on the truncated rectangles. For the last class the reciprocal is controlled by its Euler product on x=1+e.

## 5. Central dyads and exact exponent bounds

For any fixed real lines, write

    E(x,y,z)=a/2+x-1+h z+a(y-1).                           (5.1)

After taking the reciprocal and correction bounds, the three numerator options give U exponents

    R_mean=(nu+1)/2-z0,
    R_interpolated=1/2+nu(1-y)-z0,
    R_convexity=nu+(1-y)/2-z0.                             (5.2)

All row exponents in the table are strictly positive. Their largest value in the allowed U range is therefore obtained at U=Z^(h+e). Each complete dyad is bounded, up to a later arbitrary loss, by Z raised to

    E(x,y,z0)+(h+e)R.                                     (5.3)

All fixed polynomial height powers from the interpolation theorem are absorbed by the original joint weight. The available arbitrary Schwartz orders are chosen after the necessary height powers are known. No U^rho bound is substituted for an integrable height factor.

The accompanying exact-rational checker evaluates (5.3) for every table row, with nu including its e loss, and proves on the WHOLE interval 0<e<=10^(-6) that

    E+(h+e)R <= theta+4e.                                (5.4)

Its proof uses the Bernstein coefficients of the finite polynomial in e, not a sample of e values. It also reconstructs the ten norm and height monomials in de Faveri's detector at every threshold and compares their maximum with the stated piecewise g.

Useful exact landmarks:

- The good-class exponent is 1121/5000+(8/5)e; its constant margin below theta is 1/10000.
- The smallest middle-class constant margin is
      20321474869/416197180000000 > 0,
  at lower threshold 4043/5000 and upper threshold 8087/10000.
- That row's complete polynomial in e has coefficients
      93332705999131/416197180000000,
      2242386652871381/1040492950000000,
      -76347867793/208098590000,
      -1,
  in increasing degree. Its positive constant margin is not the only gate;
  the full interval polynomial is checked.
- There are 173 mean classes, 1700 interpolated classes and 801 convexity classes, including the good and last classes.

The code has explicit rejection gates for replacing (1.1) by the old numerator bound, omitting the functional-equation conductor cost, counting a class at its upper threshold, keeping the old small-norm cutoff, retaining the old Mellin shift, or removing the large-tail gap. Finite bookkeeping cannot verify the analytic inputs.

## 6. Principal row and every remaining range

### Principal row

Keep xi at 1+e throughout; no previously proposed global zero-free conclusion is required. Move w to 1/2, taking its residue at one, and in the w-residue move z past 1/6 to e. For the w-remainder move z to 1/6+e, without crossing that pole. The double residue is c0 f.

The two principal remainders have exponents

    E(1+e,1/2,1/6+e)=h/6+(1+h)e,
    E(1+e,1,e)=theta+(1+h)e.                             (6.1)

The contour paths are inside (2.2). The second exponent ties theta only at e=0 and is covered by (5.4).

### Small Poisson norms

For U<=Z^kappa, keep x=1+e, use y=1/2,z=z0 and individual convexity with the full row count. The exponent is

    E(1+e,1/2,z0)+kappa(1+1/4-z0)
       =22141/100000+e < theta+4e.                        (6.2)

The smaller kappa=1/1000 is necessary for this chosen proof. Reusing #965's 1/100 cutoff fails this budget.

### Horizontal segments and original-line tails

For the intermediate dyads, truncate at U^rho. On the new horizontal segments use (4.3); on the original xi tails use Euler convergence. The joint weight is handled in both height regions: when Im z is near -Im xi use its arbitrary Schwartz decay; outside that region the Gaussian gives the decay. The w factor is treated at the same time.

As in #965, a coarse pre-decay bound is O(Z^2 U^2), and here U<Z^(14/25). Since U>Z^(1/1000), choosing a fixed decay order larger than 6000/rho makes these tails O(Z^(-1)), including all dyadic logarithms and the fixed height factors. This chooses an estimate for the fixed weights, not new smoothing profiles.

### Large Poisson norms

For U>Z^(h+e), return to the initial integral at x=y=4 and move z right to

    L=10/e+2.

The row exponent is 1-L+eta by absolute convergence; the convexity formula is not extrapolated to y=4. The geometric dyad sum is controlled by its lower endpoint, with exponent

    a/2+3+3a+hL+(h+e)(1-L)
       =-9757/2000-e.                                    (6.3)

The positive gap e between the cutoff exponent and h is retained. The large contour is fixed after e is fixed. No pole is crossed.

Choose all remaining losses in (2.1), the means, reciprocal, correction, convexity, norm conversions and dyadic sums with combined Z cost below e. Equations (3.2), (5.4), and (6.1)--(6.3) give

    I(X,Y,Z)=c0 f(Z)+O_e(Z^(theta+5e)),
    f(Z) <<_e Z^(theta+5e).                              (6.4)

## 7. Mellin continuation and descent

Flatness at zero and (6.4) make

    integral_0^infinity f(Z) Z^(b-s) dZ/Z

holomorphic for Re s>b+theta+5e=9081/10000+5e. On an initial right line it equals exp((s-5/6)^2)H(s)/zeta_F^S(s). Analytic continuation and the nonvanishing of H on Re s>2/3 exclude denominator zeros in that open half-plane. At s=1 the reciprocal has a zero, not a pole.

For each individual point with real part greater than 9081/10000 choose one fixed e in the stated range with 5e smaller than its distance to the boundary. No uniform e-to-zero constant or boundary-line estimate is needed.

For an arbitrary K, pass to F=K(mu_12), an abelian extension. Class-field factorization expresses zeta_F/zeta_K as a product of entire nonprincipal Hecke factors, so a zero of zeta_K away from one would persist. The same argument through a finite-order character's class field gives the finite-order Hecke statement. At one, nonzero residues exclude a zero of a nonprincipal factor. All finite Euler omissions have their zeros on real part zero.

This completes the proposed composition from the imported source interfaces. It does not promote those interfaces to an independently reviewed theorem.

## 8. Why this does not supply a full-proof mechanism

The argument still applies absolute-value numerator bounds after separating the reciprocal. It supplies a genuine new intermediate-line estimate and a better proposed boundary, but no native critical signed estimate.

At balanced subcritical scales the boundary is 5/6+a/6. In the zero-loss limit, the good-class correction domain x>2/3 and its budget x<=3a/2 require a>=4/9, so this particular comparison cannot reach below 49/54 merely by optimizing its scales. Equality a=4/9 may be reached with a contour x=2/3+e and an arbitrarily small final loss. Additional middle-class constraints are stronger with only the present second-mean interpolation and density input. An exploratory optimization puts their bottleneck near a=0.4485237; that decimal is not an asserted certified optimal theorem.

The free-z principal projection and the diagonal finite-part investigation in the critical component seek different information before this separation. The Newton and Lee--Yang components address other mechanisms. None of their missing all-scale estimates is inferred from (6.4).

