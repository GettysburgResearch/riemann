# A reflected-ratio composition with boundary 19/21

**Status.** Proposed source-qualified composition; not an independently accepted theorem. The new ratio lemma and rational calculations have one author. The complete analytic inputs below are stated unconditionally in their sources, but in particular the short-support reconstruction in #965 and the correction reconstruction in #971 have not received a new independent proof audit here. An error in either invalidates this proposed global consequence, regardless of the checker. No RH/GRH, unknown native inverse moment, or unproved signed-energy estimate is assumed.

**Proposed conclusion.** For each number field K,

    zeta_K(s) != 0 when Re s > 19/21, s != 1,             (1)

with the analogous finite-order Hecke conclusion. There is no assertion on the boundary or of uniform constants over fields/conductors. Compared with #969's 49/54 this gains 1/378; compared with the 68/75 proposal archived in #970 it gains 1/525. Neither is independent certification of those proposals. This is not stronger than the reported 7/8 theorem in its different special setting, and it is not RH.

The new mechanism is to use the numerator/denominator conjugacy on each zero-free class, not another higher-numerator moment. Only the existing second mean is used on the full good class and the small-frequency range. None of #966's selected fourth density, #968's higher moments, or #969's fourth off-central moment is an input to (1).

## 1. Exact imported source and what is not independently checked

Start over F containing mu_12, with the fixed CT/DF finite S, permissible generators, balanced physical supports, finite S-unit sixth classes, and characters as used in #969. Actual Poisson indices are sixth-power-free exterior ideals ordered by FULL norm q_u, times that finite list. They are not merely squarefree or radical ordered. All nonunit zeros and fixed omitted Euler factors remain. The denominator character is the conjugate of the numerator character. Infinite-order angular characters are not substituted for these finite-order characters.

Adopt the following full analytic contracts, with the exact pins in SOURCES.md.

**R: short-support reflection.** The reconstruction in #965 yields

    sum_(physical support norm N) |B_m(Z)|^2
        << (NZ)^eta [N+N^2/Z],
    sum_physical |additive_weight|^2 << 1/X+1/Y,         (2)

including all auxiliary ideals and all subunit effective lengths. Physical sets are finite balanced supports, not infinite norm-only element balls. Both terms in the first bound remain. This is the adopted unrestricted-reflection reconstruction, not an extension by substitution into CT's simplified long-support corollary.

**P: exact Poisson identity.** Retain CT's entire identity with scale monomial

    X^(1/2-z) Z^(xi+z-1) Y^(w-1),                       (3)

and nonprincipal row factor

    q_u^(-z) zeta_F^S(6z) L_F^S(w,chi_u)
                   H_u(xi,w,z)/L_F^S(xi,bar chi_u).     (4)

All original archimedean/test factors and their joint height decay remain. The principal residues at w=1,z=1/6 give a nonzero constant times

    f_a(Z) = (1/(2pi i)) integral_(2)
       Z^(s-b) exp((s-5/6)^2) H(s)/zeta_F^S(s) ds,
    b=5/6-a/3, for X=Y=Z^a.                            (5)

The unchanged principal H is holomorphic and nonzero for Re s>2/3. The Gaussian in xi+z is used together with the independent profile decay in z,w; its nearly cancelling imaginary direction is not discarded.

**C: enlarged original-correction domain.** Adopt the explicit finite local sum and its proof in #971 RAMIFIED_FACTORS.md, Theorems R1-R2. The SAME correction H_u is holomorphic on

    x,y,z>0;
    6z+y>1, x+6z>1, x+y>1, x+y+6z>2, 6x+6z>5,          (6)

where x=Re xi, y=Re w and z denotes Re z. On every fixed compact real-part subset with x>=1/2 it satisfies |H_u|<<_lambda q_u^lambda for every lambda>0, uniformly in imaginary parts. This is only an upper bound, not a nonvanishing claim for H_u. The unramified local error and the five ramified factors are retained in that source. The old extra constraints 3x>2 and 3x+y>5/2 are NOT available on our new contours and are NOT imposed. In particular, adopting this enlarged domain is essential; omitting it would invalidate (1).

**M2 and density.** Use DF's full sixth-free large sieve

    K(U,V)=U+V+U^(5/6)V^(1/3)+U^(1/3)V^(5/6).            (7)

A complete Hecke AFE has conductor at most C U. For its second mean, the two pieces have length U^(1/2+small loss), up to a fixed height power. Mellin separation gives common coefficients. Write a full column n=c d^6, c sixth-free, with NO extra coprimality condition. The exact identity

    chi_u(c d^6)=chi_u(c) 1_((u,d)=1)

allows (7) on the restricted rows; Minkowski costs the convergent sum (Nd)^(-3+small loss). Evaluating K(U,U^(1/2)) gives O(U). Dual root numbers have modulus one and both AFE pieces and their rapid tails remain. Thus the second mean is O(U^(1+eta)(2+|t|)^C). This is the inherited second mean, not a new theorem attributed to this pass.

For each fixed sigma in (1/2,1), the original BGL/DF zero detector and this mean give the ten exponents

    1/2+(c+v d)/2+(1/2-sigma)e_d,
        (c,v)=(1,0),(0,1),(5/6,1/3),(1/3,5/6);
    (2-2sigma)e_d; 1+(1-2sigma)d;
    1/3+(11/6-2sigma)t, t=d,e_d;
    5/6+(4/3-2sigma)t, t=d,e_d,                         (8)

for mollifier A=U^d and smoothing length B=U^e_d. If d<=e_d and all ten are <=nu, the number of nonprincipal indices with a zero at Re s>=sigma, |Im s|<=4U^rho is O(U^(nu+eta)), for a sufficiently small fixed rho>0. Fixed twists and the character-generator interface remain as in #969. The count can equally be made for the conjugate family in a symmetric rectangle.

The formulas needed here occur in DF Section 9's proof of Corollary 1.5. With q=2sigma-1, use

  1/2<sigma<=2/3:
    d=1/2, e_d=2/(4-6q), nu=1-q/(4-6q);
  2/3<=sigma<=11/12, D=6q(10-6q)-10:
    d=(24q-5)/D, e_d=(42q-8)/D,
    nu=(9q(7-6q)-10)/D;
  11/12<=sigma<1, Delta=1-6(1-q)^2:
    d=(6q-4)/Delta, e_d=(8q-5)/Delta,
    nu=(1-q)(8q-5)/Delta.                               (9)

Every used instance of (9) is also checked against ALL ten inequalities (8). No optimizer is a premise. For the finite collection below choose one sufficiently small rho, after fixing the contour buffer. The later arbitrarily small reciprocal losses do not change the exceptional sets.

The primary de Faveri text was obtained during this pass through its arXiv record: definitions (1.2), the distinction between star/flat indices, Theorem 1.1's stated scope, family definitions and Section 9 parameter formulas were inspected. Some displayed equations were omitted by that text renderer. No claim is made to have freshly rendered the DF PDF or rebuilt its proof. The CT v2 body could not be freshly obtained; contracts R/P use the pinned repository reconstructions and C uses the separately read #971 proof. These are explicit review boundaries, not an independent certification of their foundations.

## 2. Scales, classes and the novel ratio estimate

For every fixed 0<e<=10^(-6), take

    a=3/7, h=4/7, X=Y=Z^a, N=Z^(6/7)<Z,
    theta=3/14, b=29/42,
    z0=1/2, small exponent=1/100,
    top intermediate U=Z^(h+e).                         (10)

Equation (2) and Cauchy give

    |I|^2 << Z^eta [Z^(6/7)+Z^(5/7)]Z^(-3/7),
    |I| << Z^(3/14+eta).                                (11)

The reflected diagonal term is kept, and dominates in this regime.

The complete increasing threshold list is the explicit UPPERS tuple in verify.py, starting at 16/25 and ending at 19/20. It has 36 thresholds. For each U dyad, let E_j be the actual rows whose conjugate L has a zero beyond threshold s_j in the fixed height rectangle. The 37 disjoint classes are

    E_0^c; E_0\E_1; ...; E_34\E_35; E_35.               (12)

There is one full M2 good class, 35 reflected-ratio classes and one terminal class. All frequencies, finite S-unit types and masks remain. A middle class is counted using (9) at its LOWER threshold s_{j-1}, and shifted using its UPPER threshold s_j. In particular its cardinality exponent is not silently evaluated at s_j.

For the good class take x=16/25+3e, y=1/2. Bound H and the reciprocal on the class, then use the full second numerator mean and Cauchy. Its U exponent before q_u^(-z) is mu=1.

For a middle class of size O(U^(nu+eta)), put

    x=s_j+3e, y=1-s_j-e.                                (13)

Apply RATIO_LEMMA Theorem 2. It bounds the quotient in (4) with U exponent

    mu=nu+s_j-1/2+e,                                    (14)

apart from arbitrary positive losses and polynomial heights. Notice that 1-y=s_j+e is inside the SAME zero-free rectangle as x; the two ordinates can vary independently. This is exactly why the numerator's conjugate character matters. No fourth or higher moment occurs.

For the terminal class there is no zero-free premise. Take x=1+e,y=e, use the Euler reciprocal and ordinary numerator convexity. Here nu=11/47 from the threshold 19/20 and mu=nu+1/2-e/2.

All central nonprincipal contours use z=z0. Start at (x,y,z)=(1+3e,1+3e,1/2), move xi on its truncated central rectangle and then move w. The domain (6) is convex, and every corner lies in it. In the new middle contours x+y=1+2e, so no mixed Euler pole is crossed. The numerator is nonprincipal and creates no pole at w=1. The reflected point 1-w lies right of the class's upper zero threshold, not to its left.

## 3. The exact physical bound

For an intermediate U dyad with U<=Z^(h+e), the complete exponent is

    p_j(e)=a/2+x-1+h z0+a(y-1)+(h+e)(mu-z0).             (15)

Every mu-z0 is positive. Thus the top dyad is legal; it has not been substituted into a decreasing U power. At e=0 the three powers are

    good: 16/25-a;
    middle: a-3/2+h(nu+2s_j);
    terminal: (1-2a)/2+h(11/47).                        (16)

For the middle classes the condition in (16) is especially simple:

    nu+2s_j < 9/4.                                     (17)

It is certified for EVERY transition in the finite list, not inferred from a plot of the density curve. The good slack is 1/350. The minimum middle slack is exactly

    115112128/90526848125 > 1/1000.                      (18)

All e-polynomials have degree at most two. Their Bernstein coefficients on [0,10^(-6)] prove

    p_j(e) <= theta+5e                                  (19)

for all 37 classes. The checker also proves every strict domain and nested-logarithm-disk inequality on (0,10^(-6)], including its right endpoint. No actual contour is taken at e=0.

Height powers from the functional equation, the L estimates and the correction are absorbed by the original joint profile decay. One may first truncate both numerator and denominator ordinates at the working height 2U^rho. In the complementary numerator-height tail no zero-free numerator claim is needed: ordinary polynomial L growth and the profile decay suffice. The denominator's shifted ordinate remains within the certified rectangle; outside it the xi line is retained on the original Euler half-plane. Thus (14) has not been applied to heights outside (2) of RATIO_LEMMA.

## 4. Principal, small, large and horizontal terms

**Principal terms.** Keep xi on x=1+e throughout. Start at w=1+e,z=1/6+e, move w to 1/2 taking its pole at one, then in that residue move z to e taking its pole at 1/6. Both remainder exponents are respectively

    h/6+(1+h)e, theta+(1+h)e,                           (20)

hence <=theta+2e. The full correction-domain corners are retained. No previously proposed zero-free bound is used on the principal xi contour. The double residue is exactly (5) with b=29/42.

**Small frequencies.** For U<=Z^(1/100), use x=1+e,y=1/2,z=1/4, separately from the central z0=1/2. The full second mean gives exponent

    h/4+3/400+e = 421/2800+e < theta+2e.                (21)

Keeping z=1/2 on the small range instead would be too expensive; this separate contour choice is part of the argument. It stays right of the zeta(6z) pole at 1/6 and within (6).

**Large frequencies.** For U>Z^(h+e), use the original absolute lines x=y=4 and z=L=10/e+2. The row exponent is 1-L, not a left-strip convexity bound. At the first dyad the physical exponent is

    a/2+3+hL+3a+(h+e)(1-L) = -69/14-e < -1.             (22)

Subsequent dyads decay geometrically. Dropping the positive gap e would invalidate this calculation.

**Horizontal and original-line tails.** Use the same height U^rho that defines the exceptional classes. On the shifted xi segments the zero-free logarithm lemma applies throughout. Elsewhere retain the original right xi line. The source has a Gaussian in xi+z and separate z,w decay, supplying any fixed inverse polynomial height power after all fixed growth factors. This also handles the nearly cancelling xi/z imaginary direction. Since U>Z^(1/100) in the intermediate range, a sufficiently large but fixed decay order makes every such tail O(Z^-1). No untruncated zero-free rectangle is assumed.

Choose every density, correction, reciprocal, numerator and dyadic loss sufficiently small after e, with total exponent <2e. The finite class decomposition, (19)--(22) and the source identity now yield

    I(Z^a,Z^a,Z)=c0 f_a(Z)+O_e(Z^(theta+7e)), c0!=0.

Together with (11) this is the proposed detector estimate f_a(Z)<<_e Z^(theta+7e).

## 5. Mellin conclusion and exact qualification

The right-line expression (5) is flat at zero by moving further right in absolute convergence. The preceding growth therefore makes its Mellin transform holomorphic for

    Re s>b+theta+7e = 19/21+7e.                         (23)

On the original half-plane that transform is exp((s-5/6)^2)H(s)/zeta_F^S(s). The unchanged numerator has no zeros here. Analytic uniqueness excludes target zeros in (23). Choose a sufficiently small fixed e>0 separately for each point with Re s>19/21. Uniform constants as e tends to zero are not needed, and no boundary-line conclusion follows.

For arbitrary K, apply the result over F=K(mu_12). The extension is abelian; classical Hecke factorization with holomorphic nonprincipal factors prevents a zeta_K zero away from one from disappearing in zeta_F. The corresponding class field for a finite-order Hecke character gives its analogous strict half-plane, with the usual classical nonvanishing at one for nonprincipal characters. There is no inference for infinite-order angular twists.

The proposed new fraction is a consequence of ALL adopted analytic interfaces plus the new ratio argument. The independent validity of those interfaces has not been established by this finite certificate. The ratio lemma does not prove a critical native moment, bound a class containing denominator poles, or justify taking the resonant residue in place of the complete Poisson integral.

The remaining global obstacle is not solved: with sharper density and this type of absolute row summation one can optimize further, but these estimates do not approach 1/2. Exploratory optimization performed in this pass is not a proved barrier for other methods and is not part of the theorem.
