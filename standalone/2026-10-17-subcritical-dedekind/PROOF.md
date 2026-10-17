# Subcritical physical support and a proposed 91/100 Dedekind boundary

**Status: proposed unconditional composition of stated analytic theorems, with a complete written argument; independent mathematical review required.** This is not a Lean proof or an independently accepted theorem. The main new review obligation is Section 2, which reconstructs the reflected estimate below the previously used support range. No open signed estimate from #961, native higher-moment hypothesis, RH/GRH, or earlier proposed zero-free conclusion is assumed.

## 1. Statement and source boundary

The proposed conclusion is

    zeta_K(s) != 0 for every number field K, Re(s)>91/100, s!=1.       (1)

The same half-plane is proposed for finite-order Hecke L-functions. Nonprincipal characters are nonvanishing at one; principal functions have a pole there. Constants need not be uniform in the field, conductor, discriminant, or distance to the boundary. Infinite-order angular twists are not covered.

Fix F containing mu_12, and CT's finite S, allowed generators, quotient Gamma=(R*)^6, local vectors, measures and smoothing functions, with R=O_(F,S). Write q_a=N a for the full norm of an exterior ideal. All arithmetic and geometric constants may depend on these fixed data. CT means Cureton--Thorner, Hexagon 2610.00200v2; BGL means arXiv:1112.1650; DF means de Faveri, arXiv:2610.04045v1. Exact source locations are in SOURCES.md.

CT defines, for positive X,Y,Z, the literal average

    I(X,Y,Z)=integral_(F_S^1/Gamma) sum_(m!=0) A_t(m;X,Y) B_m(Z) dt.  (2)

Bounded representatives t give a compact balanced support for m of norm O(XY). No new coefficients, randomized phases, or altered nonunit values are introduced. CT's additive argument before its last scale substitution gives

    sum_m |A_t(m;X,Y)|^2 << 1/Y+1/X.                              (3)

Indeed the uncombined expression is (XY)^(-1)(XY+Y^2)Y^(-1). Its derivation uses the number-field additive sieve with N comparable to XY and denominator range comparable to Y, and does not require XY>Z.

CT's *stated summed* reflected estimate was used in the range M>1, for XY=Z^M. That restriction must not be silently dropped. We instead reconstruct a two-term estimate directly from its unrestricted reflection formula, keeping the diagonal term which dominates when M<1.

## 2. A reflected bound valid on both sides of XY=Z

### 2.1 The complete source expression

Factor each physical index as mR=h d, where h is powerful, d is squarefree, and (h,d)=1. Powerful means every positive prime-ideal valuation is at least two. These are PHYSICAL indices, not the Poisson rows u used later.

Use the exact reflection of CT Proposition 8.3 and its separated expression (8.15). After fixing h, f|rad(h), an ideal a_f supported on f, an arbitrary exterior ideal n, and finitely many local classes, the dependence on d and squarefree c is

    omega rho(d) lambda(c)/(q_c^(1/2) q_n) * chi_d(c)^3
      * Phi(Z q_af q_c q_n^3/(q_d^2 q_f^2)).                     (4)

The profiles are a fixed finite family, independent of the growing indices. They satisfy, for j=0,1,2 and every fixed Adec>0,

    |(x d/dx)^j Phi(x)| << min(x^(1/8),x^(-Adec)).               (5)

Here |rho|,|lambda|<=1, and |omega|<=beta_f(a_f). For Q=q_p, the local majorant is

    beta_p(0)=1;
    beta_p(1+3k)=Q^(-k)                  (k>=0);
    beta_p(3k)=Q^(1/2-k)                 (k>=1);
    beta_p(2+3k)=0.                                          (6)

All original restrictions remain: (d,h n)=1, (c n,f)=1, and chi_d(c)^3 is zero on common primes. In particular c and n are allowed to share primes. Different local choices representing the same frequency are still summed separately. The angular factor is already incorporated in (4), not treated as a finite-order Hecke twist.

CT's verified quadratic-family interface gives, for squarefree d,c,

    sum_(q_d<=D) |sum_(q_c<=C) z_c chi_d(c)^3|^2
       <<_b (CD)^b(C+D) sum_c |z_c|^2,   b>0.                 (7)

Finite class restrictions are imposed before the sieve. Outer restrictions can then be retained by positivity and column restrictions by zeroing the coefficients.

### 2.2 A uniform profile summation, including subunit effective length

For r>0 and Adec>r, define w(v)=min(v^(1/8),v^(-Adec)). For every T>0,

    sum_(C=1,2,4,...) C^r w(C/T) <<_(r,Adec) T^r.              (8)

If T>=1, split at C=T. Below T, sum C^(r+1/8)T^(-1/8); above T, sum C^(r-Adec)T^Adec. Both geometric sums are O(T^r). If 0<T<1, the WHOLE sum equals a convergent geometric majorant O(T^Adec), which is at most O(T^r). No dyad is deleted when T<1. The estimate does not require an effective length to exceed one.

Restrict d to D<=q_d<2D and c to C<=q_c<2C. Put

    L=D^2 q_f^2/(Z q_af),    v=C q_n^3/L.                     (9)

CT's localized Fourier separation of the profile in log q_c-2 log q_d has L1 Fourier norm O(w(v)). The separated factors (q_c/C)^(it) and (q_d/D)^(-2it) are unitary. Ideal counting gives sum_(c~C)1/q_c=O_F(1). Thus (7) and Minkowski give the following l2(d)-norm for this C block:

    << beta_f(af)/q_n * D^(b/2) C^(b/2)
            (sqrt D+sqrt C) w(C q_n^3/L).                    (10)

Choose any sufficiently small b>0, and Adec>(1+b)/2. Apply (8) with r=b/2 and r=(1+b)/2, and THEN sum the full n variable. Since every n has weight 1/q_n, the two sums are bounded by

    zeta_F(1+3b/2),       zeta_F(5/2+3b/2),                   (11)

respectively. Both converge. A positive b is essential to the first sum; no value at b=0 is used. The fixed-h, fixed-f, fixed-af root bound is therefore

    <<_b beta_f(af) D^(b/2)
        [sqrt D L^(b/2)+L^((1+b)/2)].                        (12)

This proof keeps the c sum inside its quadratic sieve norm. It takes absolute values only for the auxiliary choices, using summable majorants. The d restrictions depending on n are handled for each n before Minkowski. It does not replace the complete reflection by a truncated polynomial. Apply the inequalities first to finite partial sums; (8), (11) and (14) give summable majorants that justify passage to the complete sums.

### 2.3 Full local sums and powerful rows

The following two local sums follow exactly from (6):

    S0(Q)=sum_j beta_p(j)
         =1+(1+Q^(-1/2))/(1-Q^(-1)),
    S1(Q)=sum_j beta_p(j) Q^(-j/2)
         =1+(Q^(-1/2)+Q^(-2))/(1-Q^(-5/2)).                  (13)

For q_h comparable to P, one has q_f<=N rad(h)<=sqrt(q_h) and L<=D^2 q_h/Z. Factors D^(b/2)L^(b/2) in (12) can consequently be bounded by arbitrarily small powers of PD, by choosing b small enough. The first term then uses S0, while the second retains q_f q_af^(-1/2)D/sqrt Z and uses S1.

Summing even over all divisors f of rad(h), a harmless enlargement of the permitted choices, gives

    sum_f sum_af beta_f(af) = product_(p|h)(1+S0(q_p)) <<_eta q_h^eta,

    sum_f q_f sum_af beta_f(af)/sqrt(q_af)
       = product_(p|h)(1+q_p S1(q_p))
       = N rad(h) product_(p|h)(q_p^(-1)+S1(q_p))
       <<_eta q_h^(1/2+eta).                                (14)

For either product, absorb every sufficiently large prime factor into q_p^eta; the finitely many smaller prime ideals contribute a fixed constant. This is uniform in the valuations of h. It does not presume the literal product over all primes converges.

There are O_F(P^(1/2)) powerful ideals up to norm O(P). Indeed write h=r^2 s^3 canonically with s squarefree and sum O(P^(1/2)q_s^(-3/2)). Balanced allowed generators have bounded multiplicity on every fixed compact shape set, uniformly under the fixed compact t translations in (2).

Square the fixed-h root bound coming from (12)--(14), use (u+v)^2<=2u^2+2v^2, and sum the powerful h. After renaming the arbitrarily small exponent, this proves

    Q_Z(P,D) <<_eta (PD)^eta P^(1/2)(D+D^2 P/Z).              (15)

This applies on any fixed compact balanced shape support, uniformly for P,D>=1 and Z>=2. The constants depend on eta and that shape, not on a support exponent M. The imported ingredients are the unrestricted reflection (4)--(6), the actual quadratic-family sieve (7), and the fixed profile bounds. CT's supercritical summed proposition is NOT being extended by assertion.

If physical support has norm O(T), then PD<<T. In particular,

    P^(1/2)D <= O(T) P^(-1/2),
    P^(3/2)D^2/Z <= O(T^2/Z) P^(-1/2).

For T=Z^M, any fixed M>0, sum the dyads and absorb logarithms into eta:

    sum_(physical support) |B_m(Z)|^2 <<_eta Z^eta(T+T^2/Z).  (16)

For M<1 the first term is dominant. The false substitution T+T^2/Z << T^2/Z would destroy this argument; the negative-control suite explicitly rejects it.

### 2.4 The new scales

Combining (3) and (16), with the compact quotient volume absorbed, gives

    |I(X,Y,Z)| << Z^eta [(XY+(XY)^2/Z)(1/X+1/Y)]^(1/2)        (17)

when X,Y are fixed positive powers of Z. Choose

    a=23/50,   X=Y=Z^a,   M=2a=23/25<1.                    (18)

Both X,Y tend to infinity. No endpoint M=1 is used. Equations (17)--(18) give

    |I| <<_eta Z^(23/100+eta).                              (19)

This estimates the COMPLETE original physical sum, including the low-powerful sector left open in #961, but at DIFFERENT scales. It does not prove #961's OPEN-L at its old scales.

## 3. The actual Poisson family and available estimates

### 3.1 Exact factorization, correction domain and normalization

On its initial lines (x,y,z)=(4,4,2), CT's Poisson summand is a fixed weight times

    X^(1/2-z) Z^(xi+z-1) Y^(w-1) q_u^(-z)
      zeta_F^S(6z) L_F^S(w,chi_u) H_u(xi,w,z)
                   /L_F^S(xi,bar chi_u).                   (20)

u runs over the sixth-power-free exterior ideals, with the fixed finite S-unit classes, ordered by their FULL norms. CT's unique principal row is u=1. No radical-norm or conductor ordering is substituted.

For x=Re xi, y=Re w, z=Re z, the correction is holomorphic with H_u<<q_u^eta on every fixed-margin subdomain of

    x,y,z>0; 6z+y>1; x+6z>1; x+y>1; x+y+6z>2;
    6x+6z>5; x>1/2; 3x>2; 3x+y>5/2.                        (21)

The last two inequalities are both retained from CT's maximum condition. The weight has joint decay

    <<_A exp[-(Im xi+Im z)^2]
                  (1+|Im z|)^(-A)(1+|Im w|)^(-A).           (22)

It is not Gaussian decay in xi alone. All fixed polynomial height factors will be absorbed using (22).

The principal residues w=1 and z=1/6 have nonzero coefficient c0=R_S^2 M(1/6) W1hat(1)/6. Set

    C=a/2+(1-a)/6=8/25,       b0=1-C=17/25,
    f(Z)=(1/(2pi i)) integral_(2)
       Z^(s-b0) exp((s-5/6)^2) H(s)/zeta_F^S(s) ds.          (23)

H is CT's UNCHANGED principal numerator, holomorphic and nowhere zero for Re s>2/3, with its source vertical bounds (Lemma 11.1 in Section 11.2). Moving an initial line right proves flatness of f at zero. The old b=2/3 or b=2/3-e/3 must not be retained after changing a.

### 3.2 Family identification and means

Use the same choice-compatible adapter as #959, recalled here to specify the inputs. Write u=epsilon g(a) modulo Gamma, where g is CT's allowed generator and epsilon ranges over fixed S-unit sixth classes. In DF's construction choose its deep S-ray modulus so local elements congruent to one are sixth powers. Choose its generating representatives E0 with m_E0=g(E0), extending multiplicatively. If a=(x)E h0^6 in the construction, then x m_E g(h0)^6 is an allowed generator of a. It differs from g(a) by Gamma. Residue symbols therefore identify

    chi_u = psi_epsilon chi_a^DF,  psi_epsilon(l)=(epsilon/l)_6. (24)

The chosen h0 is coprime to the tested ideal; both sides have their original zeros at shared exterior primes. The finite list psi_epsilon has fixed S-supported conductor. It is not the angular theta character.

BGL (5.1), with the sixth-power part of its index equal to one, includes every sixth-free row. Its fixed-twist extension gives

    sum_(N a<=U)^flat |L_F^S(1/2+it,psi chi_a)|^2
           <<_eta U^(1+eta)(1+|t|)^C_eta.                   (25)

For completeness, this extension follows from BGL's proof, not from dropping psi. Use the complete approximate functional equation, split the row into coprime squarefree a0 and powerful sixth-free a1, and split every column into squarefree and powerful factors. The latter root-weight sum with a positive Mellin shift converges. For fixed powerful parts, psi and their characters multiply column coefficients by modulus-at-most-one factors; the remaining row factors and dual root numbers are phases or masks. Finite class separation is unchanged. BGL's squarefree sieve, followed by the powerful-row sum, gives U+L sqrt(U)+(UL)^(2/3), with L<=U^(1/2+eta) times a fixed height power. This proves (25). Complete AFE columns, tails and coprimality zeros are retained.

For ANY subset with cardinality O(U^nu), uniform reciprocal and correction bounds taken BEFORE Cauchy give at y=1/2

    sum_subset |L_F^S(1/2+it,chi_u)| << U^((nu+1)/2+eta)(1+|t|)^C. (26)

The subset may be selected by denominator zeros. No independence is used. At other y in (0,1], use ordinary convexity, giving the alternative exponent nu+(1-y)/2. No mean for reciprocal L-functions is claimed.

### 3.3 Density bounds and fixed zero-free rectangles

Let g(sigma)=1-delta_6(sigma) from DF Corollary 1.5. For the fixed twists (24), the full detector proof is preserved: multiply its column coefficients by psi, retaining BGL's powerful-column separation and all sixth-free rows. DF Theorem 1.1 replaces the sieve in the two detector means. For 1<=A0<=B0, this gives

    sum_(Na<=N)^flat N_psi(sigma,T,a) << (NTB0)^eta T {
      B0^(1/2-sigma)(N T^(d/2))^(1/2)
        [A0+N+A0^(1/3)N^(5/6)+A0^(5/6)N^(1/3)]^(1/2)
      + B0^(2-2sigma)+N A0^(1-2sigma)
      + sup_(A0<=V<=B0) V^(1-2sigma)
          [N^(1/3)V^(5/6)+N^(5/6)V^(1/3)] }.                 (27)

Use DF's displayed substitutions A0=N^aa, B0=N^bb T^(zd). The checker reproduces every one of the ten norm/height monomials for all thresholds below. It independently compares the resulting g with the piecewise Corollary 1.5 formula; `python verify.py --details` records aa,bb,z and g as exact fractions.

Fix 0<e<=10^(-6). Choose rho>0 sufficiently small in terms of e, d and these finitely many density-height powers, THEN choose the density loss. For each threshold sigma_j, let E_j(U) be the rows U<=q_u<2U whose primitive denominator has a zero with Re s>=sigma_j and |Im s|<=4U^rho. Then

    #E_j(U) <<_e U^(g(sigma_j)+e).                            (28)

The sets are nested and fixed before the later arbitrarily small reciprocal losses. Conjugating a character reflects zero heights and preserves this symmetric count. Omitted Euler factors have no zeros for positive real part.

For u outside E_j(U), use the analytic logarithm of L on disks centered at 2+it, for |t|<=2U^rho, with radii

    R=2-sigma_j-e/4, r_o=2-sigma_j-e/2,
    r_t=2-sigma_j-e, r_i=1-e/4.

For sufficiently large U these disks lie in the zero-free rectangle and R>r_o>r_t>r_i>0. Convexity and Borel--Caratheodory bound log L on r_o by O_e(log U); its Euler logarithm is O_e(1) on r_i. Three circles gives O_e((log U)^theta), theta<1, on r_t. Thus for every later eta>0,

    |1/L_F^S(x+it,bar chi_u)| <<_(e,eta) U^eta,
       sigma_j+e<=x<=1+e, |t|<=2U^rho.                       (29)

For x>1 Euler convergence suffices. Restoring omitted Euler factors costs U^eta by splitting off finitely many small prime ideals. If a convention counts zeros with a strict real inequality, move its threshold infinitesimally left within the density-loss budget, before fixing the sets. No constant uniform as e tends to zero is required.

## 4. Twenty-two classes and the full comparison

Put h=1-a=27/50, z0=2/5, and define

    E(x,y,z)=a/2+x-1+h z+a(y-1).                              (30)

A central dyad has bound Z^E U^R, where

    R=(nu+1)/2-z0                   for the mean at y=1/2;
    R=nu+(1-y)/2-z0                 for convexity.             (31)

Use the following increasing list of density thresholds, with g values shown to make the family counts unambiguous:

| j | sigma_j | g(sigma_j) |
|---|---|---|
|0|69/100|3839/4751|
|1|3709/5000|24493363/33114742|
|2|3801/5000|25503523/35858182|
|3|7679/10000|103162393/147663262|
|4|7713/10000|103567537/149463358|
|5|7729/10000|103736593/150296062|
|6|484/625|3246329/4720886|
|7|7761/10000|104033233/151933822|
|8|389/500|130229/191111|
|9|3901/5000|26083123/38494582|
|10|1957/2500|3264851/4851359|
|11|7859/10000|104597713/156720142|
|12|987/1250|1635562/2475583|
|13|7941/10000|104671513/160459342|
|14|1999/2500|3266174/5088491|
|15|4033/5000|26021347/41423398|
|16|8157/10000|103127977/169150318|
|17|8281/10000|101103553/173380702|
|18|4229/5000|24193843/44615062|
|19|873/1000|868267/1840678|
|20|23/25|172/529|

For Z^(1/100)<U<=Z^(h+e), partition every nonprincipal row into:

* Outside E_0: x=sigma_0+e, y=1/2, nu=1; use the mean.
* E_j minus E_(j+1), j=0,...,19: x=sigma_(j+1)+e and nu=g(sigma_j)+e. For j=0,...,4 use y=1/2 and the mean. For j=5,...,19 use y=1-sigma_(j+1)+e and convexity.
* E_20: x=1+e, y=e, nu=g(sigma_20)+e; use convexity and Euler convergence for the reciprocal.

Each middle class is counted at its LOWER threshold and shifted only past its UPPER threshold. This is why a finer classification is needed; treating a middle class as sparse according to its upper threshold is invalid.

Start at (1+e,1+e,z0). Truncate xi, move it to x using (29), and then move w to y. For the last class no leftward xi shift is needed. Every vertex satisfies (21), and that domain is convex, so every connecting real segment does too. The characters are nonprincipal and z0>1/6; there are no crossed numerator poles or denominator zeros on the actual truncated rectangles.

All row powers (31) are positive. Hence their maximum in U occurs at U=Z^(h+e). The good class has exact exponent

    23/100+8e/5.                                            (32)

Every middle class has exponent c_j+k_j e+e^2/2, with c_j<23/100 and k_j<5/2. The smallest constant margin is

    23/100-c_4 = 6796459/747316790000 > 0.                    (33)

The last class has exponent

    2851/13225 + (114007/52900)e + e^2/2.                     (34)

The complete rational values are emitted by `python verify.py --details`, computed directly from (27)--(31). These formulas show that all twenty-two central exponents are at most 23/100+3e on the whole specified e interval. No floating optimization is an analytic premise.

### Principal row

Keep xi at 1+e throughout. In particular, NO already-known global zero-free theorem is needed for the principal remainder. Move w from 1+e to 1/2, taking the residue at one. In that residue move z from 1/6+e to e, taking the residue at 1/6. The double residue is c0 f. The two remainder exponents are exactly

    E(1+e,1/2,1/6+e) = 9/100+(77/50)e,
    E(1+e,1,e)       = 23/100+(77/50)e.                       (35)

All vertices and paths lie in (21). The principal z remainder still ties the theta exponent at e=0, but both move DOWN under the new scales. Unlike #961's old-scale escape, it need not be moved farther left to obtain (1).

### Small Poisson norms

For U<=Z^(1/100), leave x=1+e, take y=1/2, z=z0, and use individual convexity with the full row count. This gives

    E(1+e,1/2,z0)+(1/100)(1+1/4-z0)=449/2000+e.               (36)

### Horizontal contours and original-line tails

For intermediate dyads, horizontal edges at height U^rho use (29); original xi tails on x=1+e use Euler convergence. The reciprocal, correction and numerator contribute at most fixed polynomial height factors. In (22), integrate the z height as well: when Im z is close to -Im xi, its arbitrary Schwartz decay controls that region; elsewhere the Gaussian controls it. Together with the w decay this gives an arbitrary U^(-rho Adec) factor after absorbing those fixed height polynomials.

A coarse bound before this decay is C Z^2 U^2 on all these fixed real strips. Here U<Z^(55/100), and U>Z^(1/100). Taking a fixed Adec>500/rho makes the total of horizontal edges and original tails O(Z^(-1)), including dyadic logarithms. These choices change the order of a valid decay estimate, not the defining smoothing profiles. No untruncated global zero-free assertion for an exceptional row is used.

### Large Poisson norms

For U>Z^(h+e), use the INITIAL integral with x=y=4 and move z right to L=10/e+2. No pole is crossed. Absolute convergence gives row exponent 1-L+eta. It would be incorrect to apply the convexity expression (1-y)/2 at y=4. The dyads sum geometrically, and their lower endpoint exponent, before arbitrarily small losses, is

    a/2+3+h L+3a+(h+e)(1-L) = -97/20-e.                     (37)

The gap between the cutoff exponent and h is e>0. The large line L is fixed after e is fixed. This tail argument is independent of M>1 and never uses a zero gap.

Choose the remaining arbitrary losses in the reflected estimate, means, correction, reciprocal, convexity, norm-to-Z conversions and dyadic logarithms with combined Z cost below e. The fixed density sets and rho were already chosen. Equations (32)--(37) give

    I(X,Y,Z)=c0 f(Z)+O_e(Z^(23/100+4e)).                      (38)

Together with (19), this proves the proposed bound for the ACTUAL detector:

    f(Z) <<_e Z^(23/100+4e).                                (39)

## 5. Mellin continuation and descent

Flatness at zero and (39) imply that

    integral_0^infinity f(Z) Z^(b0-s) dZ/Z

is holomorphic for Re s>b0+23/100+4e=91/100+4e. On an initial line with Re s>1, Mellin/Fourier inversion identifies it with exp((s-5/6)^2)H(s)/zeta_F^S(s). Meromorphic continuation and the nonvanishing of H for Re s>2/3 exclude zeros of the denominator in that half-plane. At one the reciprocal has a removable zero, not a pole.

For any individual point with Re s>91/100, choose one fixed e>0, e<=10^(-6), so that 4e<Re s-91/100. No uniform e->0 constant, boundary-line claim, or limit at M=1 is used. This gives (1) for F.

For arbitrary K, F=K(mu_12) is abelian over K. Classical factorization writes zeta_F as zeta_K times entire nonprincipal Hecke factors. A zero of zeta_K away from one would persist in zeta_F. For a finite-order Hecke character over K, use its cyclic class field and the analogous factorization. Away from one all nonprincipal factors are entire. At one, the quotient of the two nonzero residues excludes a zero of any nonprincipal factor. Finite missing Euler factors have zeros only on Re s=0. No general Artin holomorphy or growing-field uniformity is asserted.

## 6. What changes, and what does not

The improvement over #959 is 11/12-91/100=1/150. The excluded width becomes 9/100 instead of 1/12, an 8% increase. This remains numerically weaker than the previously reported 7/8 special-setting result, and is far from RH.

The old positive theta ceiling in #959/#961 explicitly concerned M>1. It is not contradicted inside that range. The new step reconstructs the full reflected bound from its source before the supercritical simplification and uses M=23/25. The middle-class numerator mean is needed alongside that reconstruction. Adding bins to the old M>1 formula alone would not achieve this.

The old fixed-scale OPEN-L and native critical covariance are not proved. Neither the geometric double-Mobius route nor #960's rational-integer logarithmic cancellation is a premise. No exhaustive priority claim is made for these summation methods or this composition.

Priority adversarial review: (10)--(15), including uniform finite profiles, all auxiliary ideals and small effective lengths; then the fixed-twist adapter (24)--(29); then the full twenty-two-class comparison, principal remainder and moving large-frequency cutoff. A defect in one of these analytic steps would invalidate (1), irrespective of the finite checker.
