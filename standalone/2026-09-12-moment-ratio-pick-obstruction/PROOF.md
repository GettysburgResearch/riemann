# MRP26 — a native, parameter-uniform obstruction to a moment-ratio Pick completion

Date: 2026-09-12. Status: **PROPOSED component theorem with a complete-source directed certificate; independent analytic and implementation review required.**

**RH is neither proved nor disproved. This is not an RH-necessary Pick inequality.** It excludes a specific, stronger coefficient-ratio construction for the literal theta source and for every sufficiently accurate approximant to that source. An explicit characteristic function with only simple real zeros fails the same test. No xi zero is an input or an output of the certificate.

## 1. Why this attempted end-to-end route, and its exact boundary

PR #851 constructs positive full-law errors and local complex-zero certificates for Gauss–Thorin approximants. The newer branching proofs #859/#860 give eventual high-height critical-line confinement at each fixed depth, but not a joint depth/height theorem. The centered gamma continuation #862 permits finite nonreal defects and reduces an RH conclusion to their weighted cost tending to zero; that vanishing is open. PR #856 separately refutes the earlier specific Brownian companion phase inequality on its actual source.

This pass tried a different global completion: recover a positive Lévy/Bernstein structure from the actual theta coefficient ratios, then apply a structural real-zero theorem rather than extend a finite zero census. Konstantopoulos–Patie–Sarkar [KPS], Section 4.1, already ask whether xi belongs to their generalized entire-function class. Their Theorem 23 supplies a sufficient real-zero result for a **one-separated Bernstein–Pick subclass** at root parameter zero. The general Bernstein class is larger and can have nonreal zeros. Neither the coefficient-ratio idea nor that sufficient theorem is claimed as new here.

The new proposed contribution is an exact squared-rational separation test, its directed evaluation on the full theta source, exclusion uniformly over the root parameter in [0,1/2], and an open-neighborhood/cofinal exclusion theorem. We rule out every complete Bernstein interpolant in this construction, not merely one guessed interpolation. The proof below does not assume the correctness of KPS's zero-location theorem or any proposed repository convergence theorem: those explain the attempted application. The explicit class being excluded is defined by (4).

This does **not** exclude ordinary non-complete Bernstein factors, arbitrary coupled Lee–Yang systems, products or other transforms of generalized entire functions, or the possibility that the approximants have only real zeros by another mechanism.

## 2. Literal source, normalization and forced coefficient ratios

Use the classical theta representation, in standard Xi coordinates,

    Xi(z) = xi(1/2+iz) = integral_R W(t) exp(izt) dt,
    W(t) = sum_(l>=1) [4 pi^2 l^4 exp(9t/2)
                       -6 pi l^2 exp(5t/2)] exp(-pi l^2 exp(2t)).       (1)

The completed xi is entire, with xi(0)=xi(1)=1/2. Equation (1) is classical [KPS, Section 2.1]; it is a source identification, not a zero assertion. Put

    M_n = integral_R t^(2n) W(t) dt,   mu_n=M_n/M_0,
    Phi(z)=Xi(z)/Xi(0)=sum_(n>=0)(-1)^n a_n z^(2n),
    a_n=mu_n/(2n)!,   mu_0=a_0=1.                                  (2)

All M_n are positive. W is even; for t>=0 each summand is positive because pi l^2 exp(2t)>3/2. The bounds in Section 7 justify all integrals and expansions.

Define J_Psi(z)=sum_(n>=0)(-1)^n z^(2n)/product_(j=1)^n Psi(j), with empty product 1. If J_Psi=Phi and Psi(u)=(u-theta)phi(u), then necessarily

    Psi(n)=a_(n-1)/a_n=2n(2n-1) M_(n-1)/M_n,
    phi(n)=v_theta(n):=[n/(n-theta)] v_0(n),
    v_0(n)=2(2n-1) M_(n-1)/M_n.                                  (3)

We use 0<=theta<=1/2, the root-parameter interval in the motivating KPS class. No interpolation off the integers is presumed. Our computation uses M_0,...,M_10: normalization and the ten even moments through order TWENTY, not ten arbitrary derivatives.

For this packet, a complete Bernstein function (equivalently the Bernstein–Pick class on the positive axis) means a function admitting the classical positive representation

    phi(u)=A+B u+integral_(0,infinity) u/(u+t) sigma(dt),
    A,B>=0, sigma>=0, integral (1+t)^-1 sigma(dt)<infinity.           (4)

This representation can also be taken as the exact hypothesis defining our exclusion theorem; no abstract class equivalence is needed for its proof. Ordinary Bernstein functions need not admit (4).

**MRP1.** There are no theta in [0,1/2] and phi of the form (4) satisfying (3) for all n=1,...,10. Consequently there is no such representation of Phi, even with a positive rescaling of its spectral argument.

The proof consists of the following finite functional and the full-source certificate in Sections 6–7.

## 3. A derivative-free positive-square functional on the complete class

Let

    p(t)=t^2-24t+90,   D(t)=product_(n=1)^10(t+n),
    c_n=(-1)^n (n^2+24n+90)^2 / [(n-1)!(10-n)!].                    (5)

The exact rational vector is

    (-2645/72576, 5041/10080, -3249/1120, 10201/1080, -11045/576,
      405/16, -94249/4320, 29929/2520, -16641/4480, 9245/18144).

Partial fractions give the polynomial identity

    sum_(n=1)^10 c_n n/(t+n) = t (t^2-24t+90)^2 / D(t).             (6)

Indeed the residue at t=-n on the right is n c_n. Both sides are proper rational functions with the same simple poles and residues, so their difference is zero. Evaluation at zero and comparison of the coefficient of 1/t at infinity give

    sum c_n=0,   sum n c_n=0.                                      (7)

The checker independently multiplies out (6) in Fraction arithmetic. Its numerator coefficients, in ascending order, are 0,8100,-4320,756,-48,1, followed by zeros.

Substituting (4) and using (6)–(7),

    Q(phi):=sum c_n phi(n)
           =integral [t (t^2-24t+90)^2 / D(t)] sigma(dt) >=0.       (8)

Every individual integral u/(u+t) is finite by (4), so the finite interchange is valid. The final integrand is nonnegative, bounded near zero and O(t^-5) at infinity. This is a condition on the TEN VALUES of any admissible phi. We do not choose values of phi' or assume that a particular analytic interpolation is canonical.

## 4. The full-source contradiction, uniformly in the parameter

For the values (3), write Q_theta=sum c_n v_theta(n). The directed calculation in Section 7 proves

    -0.000000146710376192 < Q_0 < -0.000000146710376191.            (9)

These are outward terminating-decimal bounds, not nearest-rounded values. Positivity (8) is therefore impossible at theta=0.

For uniformity, define the degree-at-most-nine polynomial

    P(theta)=product_(n=1)^10(n-theta) Q_theta
            =sum_(n=1)^10 c_n n v_0(n) product_(j!=n)(j-theta).     (10)

Write it in the Bernstein basis on [0,1/2],

    P(theta)=sum_(j=0)^9 b_j binom(9,j)(2theta)^j(1-2theta)^(9-j). (11)

The basis functions are nonnegative and sum to one. If P(theta)=sum A_k theta^k, then the exact conversion used by the checker is

    b_j=sum_(k=0)^j A_k binom(j,k)/[2^k binom(9,k)].                (12)

All ten computed intervals satisfy b_j < -1/2. The largest upper endpoint is

    max_j upper(b_j) = -0.532382613124399411... < -1/2.            (13)

The exact dyadic endpoint, rather than the displayed decimal, is retained in results.json. Therefore P(theta)<-1/2 throughout the entire interval, without parameter sampling. Since its positive denominator is at most 10!,

    Q_theta < -1/(2*10!) <0,     0<=theta<=1/2.                    (14)

This contradicts (8) for every possible interpolant and proves MRP1. A rescaling J_Psi(a z)=Phi(z), a>0, multiplies every forced Psi(n) and phi(n) by a^2. It cannot change the sign of the functional; thus rescaling does not evade the theorem.

## 5. Quantitative robustness and why a cofinal approximation cannot evade it

Exactly,

    sum |c_n|=270142/2835,
    10! sum |c_n|=345781760.                                      (15)

If ten values v_0(n) are perturbed by at most epsilon, their polynomial (10) changes, uniformly on [0,1/2], by at most

    epsilon sum |c_n| n product_(j!=n) j
      =345781760 epsilon.                                        (16)

For epsilon=10^-10 this is 0.034578176. Equations (13),(16) leave a strict negative margin greater than 0.46 in magnitude. This parameter-uniform perturbation argument does not require perturbations of the Bernstein coefficients to preserve their signs individually.

The native checker also proves 0<v_0(n)<66 for 1<=n<=10. Suppose normalized moments mu'_0=1, mu'_1,...,mu'_10 satisfy

    |mu'_n/mu_n-1|<=10^-13,   1<=n<=10.                          (17)

Then, including the exact zeroth moment,

    |v'_0(n)-v_0(n)| <= 66 * [2*10^-13/(1-10^-13)]
                     =132/(10^13-1) <10^-10.                   (18)

**MRP2 (open-neighborhood exclusion).** Every normalized even function with positive moment coefficients satisfying (17) also fails (8) for every theta in [0,1/2]. No factorization of the form (3)–(4) is possible for any of these functions.

**MRP3 (cofinal exclusion).** Let F_j be normalized even holomorphic functions on one fixed neighborhood of zero, converging there locally uniformly to Phi. If their first ten even moment coefficients are positive, then for every sufficiently large j, no representation J_Psi(a z)=F_j(z) with (4), 0<=theta<=1/2 and a>0 exists.

Proof. Cauchy's formula gives convergence of all derivatives through order20. Each limiting mu_n is strictly positive, so (17) holds eventually at the finite set of indices. Apply MRP2. The parameter and positive scale may depend on j. QED.

For the reflected #851/#857 approximants, center at s=1/2, put s=1/2+iz and divide by the value at the center. Their stated local-uniform convergence supplies this corollary; for #862 it applies directly to its normalized entire functions. These are applications conditional on those separately proposed convergence arguments. MRP1–MRP3 themselves require none of their numerical certificates or high-height asymptotics.

This excludes the attempted structural COMPLETION at arbitrarily late approximation stages, not those families themselves. It does not prove that a late approximant has a nonreal zero. It is compatible with every one of their zeros being real.

## 6. An all-real control and misleading scalar tests

Take the characteristic function

    F(z)=cos(z)cos(4z).                                           (19)

It is the characteristic function of the sum of independent symmetric signs of magnitudes 1 and4. Every zero is real and simple: the two cosine zero sets cannot intersect, since 4(2k+1)=2l+1 is impossible. Its even moments are exactly

    mu_n=(5^(2n)+3^(2n))/2.

Nevertheless the same functional on its v_0(n) is

    Q_0 = -4504004553882705024374946395491624470853276603218402439331840
          /14063065147598422504688464762393177846987067968161793249053906663
         <0.                                                     (20)

The checker computes (20) entirely in Fraction arithmetic. Thus our negative native value is NOT an RH-disproof witness, nor is (8) necessary for real-zero entire functions. In particular this is not the RH-necessary xi/Pick or trace-Hankel criterion elsewhere in the repository. It is a separate coefficient-ratio constraint.

Conversely, all scalar alternating differences available on the native ten-node vector pass:

    (-1)^(k+1) Delta^k v_0(n)>0,   1<=k<=9, n+k<=10.             (21)

The checker encloses all 45 values positively. Scalar increasing/concavity/higher-difference reconnaissance therefore missed the stronger obstruction. These finite scalar signs do not establish an ordinary Bernstein interpolation either.

The rounded quadratic in (5) was discovered through nondirected numerical reconnaissance. No scout value, optimization output, derivative value, zero table or fitted moment enters acceptance. The rational witness is fixed before native reconstruction. No claim is made that ten nodes are minimal or optimal.

## 7. Complete source-error proof for the directed computation

The full source is (1). We evaluate M_0,...,M_10 with mesh h=1/d, integer d>=64, retaining lattice nodes |jh|<=4 and theta terms l=1,...,6. Every retained elementary operation is outward-rounded on a 288-bit dyadic grid. Each resulting moment interval is widened by 2^-101. We now prove that this pays ALL analytic omissions.

### 7.1 Evenness and analyticity needed for the contour bound

Let T(u)=sum_(l in Z) exp(-pi l^2 u), D_u=u d/du. Classical Gaussian Poisson summation gives T(u)=u^-1/2 T(1/u). The polynomial operator E=2D_u^2+D_u is invariant under D_u -> -D_u-1/2. Thus

    E T(u)=u^-1/2 (E T)(1/u),
    W(t)=u^1/4 E T(u), u=exp(2t),

which proves W(t)=W(-t). The defining theta series and all its local derivatives converge normally where Re exp(2t)>0, in particular |Im t|<pi/4. The real identity therefore extends holomorphically throughout that strip. This use of Gaussian Poisson summation is classical and separate from RH.

### 7.2 Entire trapezoidal alias remainder

Put eta=1/4 and f_r(z)=z^(2r)W(z), 0<=r<=10. For x>=0, 3<pi<4 and cos(1/2)>7/8 give

    |W(x+i eta)| <=88 exp(9x/2) sum_(l>=1) l^4
                          exp[-(21/8) l^2 exp(2x)]
                 <=176 exp(9x/2) exp[-(21/8)exp(2x)].             (22)

For the last inequality, l^4<=16^(l-1), l^2>=1+3(l-1), and the geometric ratio 16 exp[-(63/8)exp(2x)] is less than1/2. Also |x+i eta|^(2r)<=(x+1)^20<=exp(20x). Evenness and y=exp(2x) now give

    integral_R |f_r(x+i eta)| dx
       <=176 integral_1^infinity y^(49/4-1) exp[-(21/8)y]dy
       <=176*12!/2^13 <2^24.                                   (23)

The same bound holds on the lower line. Bounds of this kind also supply the decay on the vertical ends needed for shifting a Fourier contour. Hence for the convention fhat(omega)=integral f(x)exp(-i omega x)dx,

    |fhat_r(omega)|<=2^24 exp(-eta |omega|).

Poisson summation for this smooth rapidly decaying function and a geometric sum give the complete infinite-lattice alias bound

    |M_r-h sum_(j in Z) f_r(jh)|
       <=2^25/[exp(2pi eta/h)-1] <2^-102.                       (24)

Indeed 2pi eta/h>=32pi>96 and log2<3/4, so the denominator exceeds2^127. This is a full Fourier-tail estimate, not a finite grid's observed agreement.

### 7.3 Omitted theta terms on the whole lattice

For real t>=0 the theta summands are positive. For l>=7, t^(2r)<=exp(20t) yields

    t^(2r)W_l(t)
      <=64 l^4 exp[(49/2)t] exp[-3l^2 exp(2t)]
      <=64 l^4 exp(-3l^2) exp(-4l^2 t).                         (25)

To see the second inequality, put y=exp(2t)>=1; y^(49/4) exp(-l^2 y)<=exp(-l^2) because l^2>=49>49/4, and use y>=1+2t for the remaining exp(-2l^2y).

The entire symmetric-lattice tail is at most

    128 sum_(l>=7) l^4 exp(-3l^2) h/[1-exp(-4l^2h)]
       <4 sum_(l>=7) l^4 exp(-3l^2)
       <19208 exp(-147) <2^-180.                               (26)

Here h/(1-exp(-4l^2h))<=h+1/(4l^2), h<=1/64. Write l=7+k; then l^4<=2401*16^k and l^2>=49+14k, so the remaining series is geometric with ratio at most16 exp(-42)<1/2. The factor2 at the origin is an overbound, not a missing endpoint weight.

### 7.4 Omitted spatial lattice and all infinite tails

For t>=4, (49/2)t<=exp(2t)/2. Using l^4<=exp(l^2) in the same real-source bound gives

    |f_r(t)| <=128 exp[-2exp(2t)].                               (27)

For detail, with y=exp(2t)>=2, each exponent is bounded by -2l^2y; sum exp(-2l^2y)<=2 exp(-2y). Further, exp(8)>2^10 and exp(2u)>=1+2u imply

    |f_r(4+u)|<=128 exp(-2048)exp(-4096u), u>=0.

Thus the entire symmetric omitted lattice contributes at most

    256 exp(-2048) h/[1-exp(-4096h)]
       <8 exp(-2048) <2^-1000.                                 (28)

Equations (24),(26),(28) sum to less than2^-101. The finite approximation subtracts a subset of each of the two positive omitted tails, so their sum remains a valid overbound without double-counting concerns. Arithmetic rounding is not included in this analytic number: it is separately retained by the interval operations.

### 7.5 Arithmetic and acceptance contract

numeric_core.py uses integer endpoints divided by2^288. Addition is exact on this grid; multiplication and inversion round outwards. pi is enclosed by Machin's formula using alternating rational arctangent sums. exp uses a64-term Taylor polynomial after dividing its input by powers of2 until its absolute value is at most1/8. Its omitted absolute series is bounded by twice the first missing term; successive interval squaring restores the original scale. A negative lower bound may be replaced by zero because exp is positive.

The finite summand is evaluated as (4x^2-6x)exp(-x+t/2), x=pi l^2 exp(2t). The weight is h at t=0 and2h for positive t; t^(2r) is an exact rational. These prescriptions reproduce (1) on the positive half-lattice and its exact even reflection. No special-function backend, floating value or numerical integration package enters acceptance.

The accepting program reconstructs all eleven moment intervals from this primitive source, forms the ten ratios, proves (9), all ten strict polynomial coefficient bounds b_j<-1/2, v_0(n)<66, and all45 scalar signs (21). It checks (6)–(7),(15) and the all-real control in exact rational arithmetic. With --check it compares the entire freshly reconstructed record to the supplied JSON; a self-consistent modified record does not bypass primitive replay. All strict tests use explicit exceptions, so Python -O does not remove them.

The error2^-101 and its coverage contract are analytically justified above, not derived by the checker itself. Independent review must examine (1), evenness, the contour hypotheses, every exponent and constant in (22)–(28), the coefficient indexing in (3), and the class hypothesis (4). A passing program is not an independent analytic proof review.

## 8. Consequences for the continuing research programme

The hoped-for completion was:

    native theta moments -> one-separated Bernstein–Pick factor
       -> a global real-zero class -> RH.

The first substantive structural membership fails, even without the one-separation requirement. Equations (16)–(18) show that increasing source fidelity, tuning theta, or rescaling cannot repair this route within the specified single-factor class. This is an all-interpolants and cofinal exclusion, rather than another finite-approximant zero failure.

What remains viable is strictly broader: ordinary Bernstein factors without the Pick property would require a genuinely new zero theorem; coupled Lee–Yang structures are not subject to (8); the source-specific weighted-defect problem of #862 is untouched. The exact moment obstruction itself gives no control of the sign of that weighted xi defect.

In particular, #859/#860's statements have quantifiers `for each n, for all |t|>=T_n`. Local convergence at fixed t does not replace these by a uniform-in-n tail. A counterexample to such a generic implication is obtained by multiplying any convergent real-zero sequence by a fixed nonreal quartet factor. Each finite member still has only finitely many off-axis exceptions, and the same quartet persists in the limit. This example is a logical test, not a changed-source assertion about the repository's actual orbit.

A meaningful next closing theorem must exploit source-specific information absent from that generic implication. For #862 it is the vanishing of its weighted defect, not merely convergence of that defect to an unknown xi quantity. This pass has not established vanishing, a replacement phase inequality, or global confinement. It has identified and excluded a precise overstrong structural substitute, with explicit reproducible bounds.

## 9. Sources, credit and review scope

[KPS] T. Konstantopoulos, P. Patie, R. Sarkar, *A new class of solutions to the van Dantzig problem, the Lee–Yang property, and the Riemann hypothesis*, arXiv:2211.16680v1 (2022). HTML sections2.1,4 and4.1 and Theorem23 were inspected. https://arxiv.org/html/2211.16680v1 . The generalized series, Bernstein/Pick route and xi membership question are prior work. Our ratios are independently derived from (2), not copied from another normalization's displayed algebra.

[851] PR #851 @57726ef9b3bf90561df5a361e3b01169c892a62a. Prior source/error and local-zero packets supplied context. numeric_core.py adapts its scalar interval arithmetic; original intervals.py blob032d3693cb5b7828a38d0620ed8d901b1cdaee56 was authenticated against the supplied local file. The new checker does not call that parent's zero checker.

[856] PR #856 @f21012f63adac789653e9bf6dbb8c309fa5fe7c5. Read the current proposal/certificate scope in its PR description. Its exact-source negative companion phase prevents treating the old OPEN target as established. The phase computation was not rerun here.

[859] PR #859 @cbf7d5f9a693fee17ee62dae4cfb1c2296499282 and [860] PR #860 @e1a782cffaafbc9cc228273ed94ce63ae0407632. Read relevant principal proof sections: analytic-singularity and BV alternatives for fixed-depth high-height confinement. These are separate proposals, not independently accepted theorems or a uniform limit.

[862] PR #862 @67d5d6a5f588642f4c451fe35d2369b5ddac9346, standalone/2026-09-10-gamma-finite-defect/PROOF.md. Read the relevant source, radial-repair, defect-limit and obstruction sections. Its separately proposed convergence supplies one application of MRP3; no parent numerical certificate was rerun.

Main @f99d9e3908dde4865377c75d9ca051c1f545bf4f: README, AGENTS and STATUS; issue#763 Riemann Structures programme and recent PR descriptions provided orientation. This is a scoped research pass, not an exhaustive repository audit, integration review, whole-checkout validation, or Lean build. Existing research statements are not edited or promoted. No external priority claim is made for elementary positive-functional, partial-fraction, Bernstein-polynomial or contour-quadrature mechanisms.
