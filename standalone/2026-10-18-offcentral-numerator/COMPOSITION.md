# A proposed 49/54 Dedekind zero-free composition

Status: PROPOSED source-qualified mathematics, not independently reviewed or formally certified. The conclusion is a deduction from the explicit analytic contracts below. They are stated unconditionally in the cited sources/repository reconstructions; their complete foundations have not been independently rebuilt here. No RH, native inverse-Mobius moment or unproved signed-covariance estimate is an input.

## 1. Claim and the exact new ingredient

The proposed conclusion is

    zeta_K(s) != 0 for every number field K, Re(s)>49/54, s!=1,

with the corresponding finite-order Hecke conclusion. This improves #966's proposed 109/120 by 1/1080 and #968's proposed 10/11 by 1/594. It does NOT improve the numerically stronger reported 7/8 special-setting result, concern infinite-order angular twists, or prove RH.

The new ingredient is OFFCENTER_MOMENT.md: a fourth numerator moment of U^(1+eta) at 7/12, hence U^(4/3+eta) at 5/12. Using it at w=5/12, rather than w=1/2, gains (3a-1)/24 in the actual Poisson exponent. The full good class retains its second mean at 1/2. The original de Faveri/BGL second-moment density suffices; the fourth-moment density refinement from #966 is NOT needed for this composition.

## 2. Adopted analytic contracts and source boundary

Work first over F containing mu_12 and its fixed CT data. All element-row sets below are finite balanced supports: multiplication by a radial section of a fixed compact shape, with the original unit quotient. They are not infinite norm-only element balls. The ideal and character conventions, generator choices, finite S-unit twists and nonunit zeros are exactly those of #965/#968.

(R) Adopt #965 PROOF.md, Sections 2 onward, at d58e3282a9379b6ae165681bc2e21e4f9fd18c26: the reconstruction from CT's unrestricted reflection and the quadratic-family sieve gives

    sum_{physical rows of support norm N} |B_m(Z)|^2
        <<_eta (NZ)^eta [N+N^2/Z],

and the original additive square norm is O(1/X+1/Y). Both terms are essential. This is not an extrapolation of CT's simplified M>1 corollary. Its all-auxiliary-ideal proof, subunit effective lengths and fixed-shape uniformity remain priority independent-review obligations. The numerical consequence here is invalid if this adopted reconstruction fails.

(P) Adopt the exact CT Poisson identity and correction domain as transcribed and audited in #966 CONTOURS.md at 8d94494698ee447711a53dec922986586418e398. The scale monomial is

    X^(1/2-z) Z^(xi+z-1) Y^(w-1).

The nonprincipal summand has numerator L_F^S(w,chi_u), denominator L_F^S(xi,bar chi_u), and a correction controlled on

    x,y,z>0; 6z+y>1; x+6z>1; x+y>1; x+y+6z>2;
    6x+6z>5; x>1/2; 3x>2; 3x+y>5/2.                  (P1)

Here x,y,z are real parts. This domain is convex. All nonprincipal frequencies are the full sixth-free ideal family, with its fixed finite S-unit labels, not a radical-ordered or merely squarefree subfamily. Fixed-order Hecke twists are retained, and the angular theta character is not substituted for one of them.

In the principal term the poles at w=1 and z=1/6 produce the unchanged nonzero constant times

    f_a(Z) = (1/(2pi i)) integral_(2)
       Z^(s-b) exp((s-5/6)^2) H(s)/zeta_F^S(s) ds,
    b=5/6-a/3,                                        (P2)

when X=Y=Z^a. The unchanged H is holomorphic and nonzero on Re(s)>2/3. The source also supplies arbitrary joint vertical decay: the Gaussian in xi+z together with the z,w profile decay, including the direction Im(z) approximately -Im(xi). We do not use decay in xi alone.

(S6/AFE) The exact sieve and complete AFE contract are given in OFFCENTER_MOMENT.md. It proves the needed off-central fourth mean. The same central AFE argument at product length U^(1/2) yields the already-used second mean U^(1+eta). Individual convexity supplies |L(y+it)| << U^((1-y)/2+eta)(2+|t|)^C for 0<y<=1. Fixed removed Euler factors change constants, not the norm exponents.

(D) The rowwise BGL (5.3) zero detector is used on the complete sixth-free family by the S6 adapter in #966 PROOF.md, Section 3. BGL's actual AFE/detector pages 18-19 were freshly rendered and read in this pass. Fresh CT and de Faveri primary-body retrieval failed. Their contracts above were read at the stated pinned repository sources, not freshly checked against a newly downloaded manuscript. This access distinction is part of the theorem's review boundary.

For clarity, here is the exact density calculation required, rather than an unexplained final density exponent. Put

    K(U,V)=U+V+U^(5/6)V^(1/3)+U^(1/3)V^(5/6),
    A=U^d, B=U^e_d, 0<=d<=e_d.

For a fixed threshold s in (1/2,1), the detector, the full second numerator mean and the mollifier second mean give a counting exponent at most the maximum of these ten numbers:

    1/2+(c+d_v*d)/2+(1/2-s)e_d,
      for (c,d_v)=(1,0),(0,1),(5/6,1/3),(1/3,5/6);
    (2-2s)e_d; 1+(1-2s)d;
    1/3+(11/6-2s)v, v=d,e_d;
    5/6+(4/3-2s)v, v=d,e_d.                            (D1)

The mollifier is squarefree. For complete detector columns n=c d0^6, retain chi_a(n)=chi_a(c)1_{(a,d0)=1}; the dyadic root sum over d0 costs (Nd0)^(-3+eta), which converges. No coprimality between c and d0 is inserted. This justifies using the complete column mean V K(U,V), rather than deleting its nonflat columns. The detector is initially rowwise, so subsets defined using zeros can be kept before taking positive sums. Its errors are absorbed by choosing the fixed truncation orders sufficiently large.

If every number in (D1) is at most nu, then for every eta>0 there is a sufficiently small fixed rho>0 such that the number of nonprincipal rows with a zero Re(s)>=s, |Im(s)|<=4U^rho is O(U^(nu+eta)). All height costs have a fixed polynomial exponent. For the finite list below a common rho exists. It is selected before the later arbitrary reciprocal losses; no unproved uniformity for a moving threshold is used.

## 3. Scales and complete exceptional-class certificate

For each FIXED 0<epsilon<=10^(-7), use

    a=4/9+epsilon, h=1-a=5/9-epsilon, X=Y=Z^a,
    M=2a<1, theta=a/2=2/9+epsilon/2,
    b=37/54-epsilon/3, z0=1/3,
    small cutoff exponent=1/100,
    large cutoff exponent=h+epsilon=5/9.               (S)

All arbitrary losses are chosen after epsilon. The new z0=1/3 is important: keeping z0=2/5 would leave no fixed positive small-frequency margin at the limiting scales.

Contract (R), with N=XY, gives

    |I(Z^a,Z^a,Z)|^2
      << Z^eta [Z^(2a)+Z^(4a-1)] Z^(-a),
    |I(Z^a,Z^a,Z)| << Z^(theta+eta),                    (R1)

because 2a<1. The N term is not discarded or replaced by N^2/Z.

There are exactly 36 disjoint classes: one good class using M2; 29 middle classes using the new M4 line; five further middle classes and the last exceptional class using convexity. Their fixed upper thresholds are the literal ordered UPPERS array in verify.py, beginning

    2/3, 14527/20000, 2363/3125, 38727/50000, ...

and ending

    88359/100000, 9053/10000, 19/20, 1.

The script contains ALL 36 rational thresholds and emits every class, including its lower threshold, exact count exponent, and two detector parameters. It requires no numerical optimizer, external library or network. The following closed expressions fix the intermediate density data exactly:

    D_s=72s^2-132s+53,
    d_s=-(48s-29)/(2D_s), e_s=-(42s-25)/D_s,
    nu_s=(216s^2-342s+127)/(2D_s).                       (D2)

Use (D2) only at the named lower thresholds at most 9053/10000, including 2/3. At the last lower threshold 19/20 use (d,e_d,nu)=(70/47,110/47,11/47). Every named instance is checked against ALL TEN inequalities (D1), and 0<=d<=e_d. No validity on an unverified continuous s-range or numerical optimality is claimed.

Let E_j(U) be the set with a zero beyond the j-th threshold, in the fixed height rectangle. These are nested. The classes are E_0^c, E_0\E_1, ..., and the last E_j. A middle class is counted at its LOWER threshold and shifted only beyond its UPPER one. All full ideal norms and all finite S-unit labels remain. The last class uses only the Euler reciprocal to the right of one.

The good class has nu=1, x=2/3+epsilon and y=1/2. In each M4 middle class put x=s_upper+epsilon, y=5/12. Every such x is greater than 25/36, as required by 3x+y>5/2. In convex classes put x=s_upper+epsilon and y=1-s_upper+epsilon; the last class thus has x=1+epsilon,y=epsilon. All central nonprincipal contours use z=z0.

The three numerator first-mean exponents are, respectively,

    mu=(nu+1)/2; mu=3nu/4+1/3; mu=nu+(1-y)/2.

Take reciprocal and correction suprema on a class BEFORE the numerator mean. For U<=Z^(h+epsilon), the exact central exponent is

    p_j(epsilon)=a/2+x-1+h*z0+a*(y-1)
                         +(h+epsilon)(mu-z0).           (C1)

All the U exponents mu-z0 are positive. The top dyad is therefore legitimate. Start at (1+epsilon,1+epsilon,z0), move xi centrally, then w. Every corner, hence every intervening segment, satisfies (P1). Principal rows were separated and create no missing w=1 pole in these nonprincipal moves.

The rational certificate proves on the ENTIRE epsilon interval

    p_j(epsilon)<=theta+2epsilon for every class.       (C2)

At epsilon=0 the good class meets theta. All other classes lie below theta by at least

    141065591711/333955226556000 > 1/4000.

The good-class domain is strict for epsilon>0, not at zero. The certificate is not a sampled parameter scan: each difference in (C2) is a polynomial of degree at most two. Its Bernstein coefficients on [0,10^(-7)] are nonnegative. Domain inequalities are certified likewise, with strict positivity on (0,10^(-7)]. Each possible zero-location interval has exactly one class. The complete exact report is CHECKS.json.

For reciprocals, outside a threshold-s exceptional rectangle, use disks centered at 2+it with radii 2-s-epsilon/4, 2-s-epsilon/2, 2-s-epsilon and 1-epsilon/4. The last disk lies in absolute convergence. Euler logarithms there, polynomial L-growth on the outer disk, Borel--Caratheodory, and three circles give |log L|=O_epsilon((log U)^kappa), kappa<1, on the target disk. Thus every later positive reciprocal loss U^lambda is available for the SAME fixed exceptional set. The working segment |t|<=2U^rho is contained in its rectangle. This is the inherited disk argument, not an assertion about zeros outside the actually truncated heights.

## 4. Principal terms, all tails and the Mellin conclusion

Principal contours remain x=1+epsilon. Start w=1+epsilon,z=1/6+epsilon; move w to 1/2 and take its pole at one. In that residue move z to epsilon and take its pole at 1/6. The two remainder corners have exponents

    h/6+(1+h)epsilon,
    a/2+(1+h)epsilon,

both at most theta+2epsilon. All corners satisfy (P1). The double residue is exactly (P2), with b=37/54-epsilon/3, because at w=1,z=1/6 the scale monomial is X^(1/3)Z^(xi-5/6). No previously proposed improved zero-free theorem is used to move the principal xi contour.

Small norms U<=Z^(1/100) use x=1+epsilon,y=1/2,z=1/3 and the full second mean. Their exponent is

    5/27+1/150+(2/3)epsilon,

strictly below theta+2epsilon. This is why the z0 change is part of the proof, not just a cosmetic contour choice.

For large norms U>Z^(h+epsilon), use the original absolute lines x=y=4 and z=L=10/epsilon+2. The row factor is U^(1-L+eta); do not use a left-strip convexity factor on these right lines. At the first dyad the exponent is

    a/2+3+h*L+3a+(h+epsilon)(1-L)
       =-44/9+(3/2)epsilon < -1.

The remaining dyads decay geometrically. L is fixed after epsilon. Dropping the positive cutoff gap epsilon would destroy this bound.

For intermediate horizontal edges and original-xi-line tails, use the SAME fixed height U^rho and the inherited joint Gaussian/profile decay. It supplies U^(-rho A) for an arbitrarily large fixed A after every fixed polynomial cost. This includes the nearly cancelling xi,z direction. Since U>Z^(1/100), choose A large enough to make the total O(Z^-1). All original profiles, finite S-types and nonprincipal frequency ranges are retained.

Allocate the finitely many density, numerator, reciprocal, correction and dyadic losses so their combined exponent is less than 2epsilon. Each is available with arbitrarily small norm loss; the height exponent is fixed first. Equations (C2) and the tail calculations give

    I(Z^a,Z^a,Z)=c0 f_a(Z)+O_epsilon(Z^(theta+4epsilon)), c0!=0.

Together with (R1), this proves the proposed detector bound f_a(Z)<<_epsilon Z^(theta+4epsilon). The original right-line expression is flat at zero, by shifting farther right in absolute convergence. Its Mellin transform is therefore holomorphic for

    Re(s)>b+theta+4epsilon=49/54+(25/6)epsilon.

On the original convergence half-plane this transform is exp((s-5/6)^2)H(s)/zeta_F^S(s). The numerator is nonzero throughout this new region. Analytic uniqueness rules out target zeros there. Choose one sufficiently small FIXED epsilon separately for each point with Re(s)>49/54. No epsilon-uniform constants or boundary-line assertion are needed.

For arbitrary K apply the result to F=K(mu_12); F/K is abelian. The classical Artin/Hecke factorization, with nonprincipal factors holomorphic away from the principal pole, prevents a zero of zeta_K from disappearing in zeta_F away from one. The cyclic class field attached to a finite-order Hecke character gives its analogous conclusion; the nonprincipal value at one uses classical Hecke nonvanishing. This does not address infinite-order angular characters or uniform conductor/discriminant constants.

## 5. What is still open, and what was actually checked

This reaches the limiting 49/54 boundary of the unchanged SYMMETRIC short-support/good-second-mean calculation. Indeed the good class on y=1/2 has leading exponent x-a, whereas theta=a/2 and the correction domain requires x>2/3. Hence a>4/9 and b+theta=(5+a)/6>49/54 before taking the fixed-positive-buffer limit. This is a restriction of this particular estimate scheme, not a no-go theorem for RH or for asymmetric/signed source arguments.

The fixed-principal critical signed covariance and the generalized native inverse-Mobius moment remain open. More exceptional bins do not by themselves improve the binding full-good-class term. A subsequent attack must change that term, its correction domain, the physical estimate, or preserve cancellation before the absolute numerator mean.

The exact checker verifies the displayed finite algebra and complete rational contour budgets. It does not verify CT's theta construction, the adopted short-support reconstruction, the exact DF sieve scope, the AFE or the zero detector. Proof and code have one author. No independent referee, Lean build, repository-wide validator, actual L-value calculation or remote CI result is claimed. The complete-source verification obligations are not replaced by a count of rational predicates.
