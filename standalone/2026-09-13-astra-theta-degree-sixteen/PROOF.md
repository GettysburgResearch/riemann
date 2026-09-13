# D16 — a target-containing degree-sixteen theta realization

Date: 2026-09-13. Status: **proposed computer-assisted component theorem;
independent mathematical and code review required. Not an RH proof.**

The main new statement is an exact realization of the original theta moments
through degree sixteen. It is not an additional generic completion theorem.
It also gives an explicit target interval on the fixed lower-fourteen-moment
fiber, and a uniformly certified connected ferromagnetic extension. The
sixteenth target is reached, whereas the eighteenth is provably not reached
by the constructed box. No unbounded-order extension is asserted.

The defining inequalities are reconstructed from the complete source by
`certify.py`; the specified rational center is not a substituted approximate
root. The inherited interval/Taylor implementation is credited to ICR26 #863
and IMR26 #847. This is not an independent second transcendental backend.

## 1. The unchanged source and normalization

For t >= 0 let

    phi(t) = sum_{n>=1} (4 q_n^2 exp(9t/2) - 6 q_n exp(5t/2))
                        exp(-q_n exp(2t)),   q_n = pi n^2.

The even extension is the standard theta Fourier source:

    Xi(z) = xi(1/2+iz) = integral_R phi(t) exp(izt) dt.

We import the classical theta representation, not RH. Its normalization can
also be fixed by Q(t)=exp(t/2)theta(exp(2t)): Jacobi inversion makes Q even,
and phi=(Q''-Q/4)/2. Each summand on t>=0 is positive since q_n>3/2.
The complete source is smooth, positive, and has every exponential moment.

Set

    Z = integral_R phi(t) dt = Xi(0),
    w = phi/Z, v = integral_R t^2 w(t)dt,
    mu_j = integral_R t^j w(t)dt.

The checker reconstructs Z, v and all even mu_j through j=18. In particular
1/25 < v < 1/20. Odd moments are zero by symmetry. We use standardized theta
cumulants K_{2r}=kappa_{2r}(T/sqrt(v)), T distributed with density w.
Cumulants are coefficients of the logarithm AT ZERO only; there is no global
logarithm across unknown zeros. The moment/cumulant recursion used is

    kappa_n = m_n - sum_{j=1}^{n-1} binom(n-1,j-1) kappa_j m_{n-j}.

Let c_{2r} be the cumulants of a fair unit sign and d_{2r} those of W with
probabilities 3/10, 2/5, 3/10 at -1,0,1. Define

    alpha_r = d_{2r}/c_{2r},    s_r = K_{2r}/c_{2r}.

The c_{2r} needed here are nonzero integers. All alpha_r are computed exactly
as rational numbers; no fitted cumulant coefficients enter the proof.

## 2. The model and its finite equations

Take six independent sign groups of multiplicities

    nu = (256, 10, 1, 1, 1, 1),

and five independent interacting pairs. Each pair has the SAME fixed coupling

    J_0 = (1/2) log(3/2) > 0.

If its two spins are sigma_j,tau_j, put W_j=(sigma_j+tau_j)/2. The ratio of
an aligned configuration weight to an unaligned one is exp(2J_0)=3/2. Thus
W_j has exactly the distribution used above, and E sigma_j tau_j=1/5.

For positive parameters x_0,...,x_5 and y_0,...,y_4, define

    Y = sum_{i=0}^5 sqrt(x_i) sum_{l=1}^{nu_i} epsilon_{il}
          + sum_{j=0}^4 sqrt(y_j) W_j,
    X = sqrt(v) Y.

There are 270+10=280 physical spins and five nonzero pair edges at this stage.
The graph is disconnected; every component is an admissible ferromagnet.
Independence is between components, not between the two spins in a pair.
Cumulant addition gives the exact polynomial equations

    F_r(x,y) = sum_i nu_i x_i^r + alpha_r sum_j y_j^r - s_r,
                                      1 <= r <= 8.                 (1)

The eleven coordinates in `parameters.json` are ordered as the six x_i,
then the five y_j. Three y-coordinates are fixed rational numbers:

    y_0 = 0.11029812891763344,
    y_2 = 0.03299608980500281,
    y_4 = 0.012258437870010524.

The eight active coordinates have indices 0,1,2,3,4,5,7,9. Each lies within
10^-14 of its EXACT terminating rational center in `parameters.json`.
For orientation only, the full parameter vector is approximately

    x = (0.00057729066470184445, 0.014074519042128239,
         0.046546432007496311,   0.085699805636415925,
         0.12080169707818310,    0.26725707167233590),
    y = (0.11029812891763344, 0.11195524351313646,
         0.03299608980500281,0.051097754928573752,
         0.012258437870010524).

The displayed approximations do not define the root. The fixed rationals,
the exact centers, the box, and (1) do. All coordinates throughout that box
lie in (1/2000,1). Multiplicities are integers, not positive quadrature masses.

**D16-1.** Equation (1) has exactly one solution in this prescribed active box.
For that solution,

    E X^{2r} = mu_{2r},  1 <= r <= 8,
    E X^{2r+1} = 0.

This is uniqueness only within the prescribed box, not uniqueness of all
Ising realizations or of all positive solutions of (1).

## 3. Complete native-source enclosure

Here we justify the analytic remainders used by the code. They are not
inferred from agreement with stored moments or a quadrature scout.

For theta indices n=1,2,3,4 the integration endpoints are respectively

    U = (2, 3/2, 1, 3/4).

Use cells of width 1/16, with midpoint c and half-width h=1/32. There are
32+24+16+12=84 cells. Each source summand is expanded in the scaled variable
z=(t-c)/h through degree 120. Exponential series multiplication is performed
with outward 320-bit integer intervals, not floating-point rounding.
The polynomial (c+hz)^j is multiplied in exactly and all even powers of z
are integrated exactly. The factor two for the even full-line source is
retained in every cell.

### 3.1 Taylor remainder

On the complex circle |t-c|=1/8 we have |Im t|<=1/8, so
Re exp(2t)>0 and |exp(-q_n exp(2t))|<=1. Here Re t<17/8 and q_n<64.
The complete prefactor is bounded by 10^11: for example use pi<4, e<3,
4*64^2*3^10 + 6*64*3^6 < 10^11. Thus Cauchy's estimate bounds the source
Taylor remainder on each real cell by

    10^11 (1/4)^121/(1-1/4).

On every actual cell 0<=t<=2, so t^j<=2^j. The summed full-line lengths
are below 16. A valid error for moment j is therefore

    e_j = 16*10^11*2^j / [4^121*(3/4)].                    (2)

This is checked and included for EVERY even j from zero through eighteen.

### 3.2 Every infinite time tail

For the summand at n and t=U+u, write E=exp(2U), q=q_n and
lambda=2qE-9/2>0. Since exp(2u)>=1+2u and the summand is at most its
positive first term, its omitted full-line moment is bounded by

    8q^2 exp(9U/2-qE)
       * sum_{k=0}^j binom(j,k) U^{j-k} k!/lambda^{k+1}.   (3)

All four bounds (3) are included. No integral to infinity is set to zero.

### 3.3 Every omitted theta index

For any n>=5, the same bound at U=0 gives

    8 pi^2 n^4 exp(-pi n^2) j! /(2pi n^2-9/2)^{j+1}.

The ratio at n+1 to that at n is below 1/2 for all n>=5 and all j>=0:
drop the improving denominator ratio and use
((n+1)/n)^4 exp[-pi(2n+1)] < (6/5)^4 exp(-33) < 1/2.
Hence the COMPLETE omitted-index tail is at most

    16 pi^2*625 exp(-25pi) j! /(50pi-9/2)^{j+1}.           (4)

The code subtracts (2) from the finite integral's lower endpoint and adds
(2), all of (3), and (4) to its upper endpoint. Division by the enclosed
positive Z gives the normalized moments. Division by v^r and the full
triangular cumulant recursion give the actual s_r through r=9.

The interval backend uses Machin's identity for pi and the 96-term alternating
atan series with its first omitted term. For exp, argument reduction puts the
argument in [0,1/8]; the next exponential term and a geometric ratio bound pay
the entire remainder before outward squaring. The source recurrence is copied
with attribution from ICR26; the moment list is extended to eighteen and
these complete remainders are verified for that scope. Different interpreter
modes are not independent arithmetic implementations.

## 4. The root certificate and a target-containing moment interval

Let c be the vector of exact centers, J_c the eight-by-eight active Jacobian
of (1), and R=J_c^{-1}. All its entries are rational, since the target is absent
from the derivative and every alpha_r is rational. Both products R J_c and
J_c R are reconstructed entry by entry (128 identities).

The formulas are simply

    (J_c)_{r,i} = r nu_i c_i^{r-1}              for active head i,
    (J_c)_{r,i} = r alpha_r c_i^{r-1}           for active pair i.

Using the complete native intervals in Section 3 and interval polynomial
evaluation on the ENTIRE box, the accepting computation proves

    ||R||_infinity < 3,200,000,000,
    beta = ||R F(c)||_infinity < 10^-19,
    L = sup_box ||I-R F'(x)||_infinity < 2*10^-6.           (5)

The infinity norm is maximum ROW SUM. It is not maximum entry, an eigenvalue
estimate, or a floating condition number. The retained sharper values are
beta<4.135*10^-20 and L<1.563*10^-6; (5) is the simpler proved interface.
For radius r0=10^-14,

    beta+L*r0 < r0.

Thus x -> x-RF(x) maps the closed box strictly into itself and is a contraction.
Banach gives the exact root and uniqueness in the box. Cumulant addition and
the triangular moment/cumulant identities prove D16-1.

**D16-2 (an actual target interval).** Keep all theta moments through fourteen
fixed and replace the standardized sixteenth moment by

    mu_16/v^8 + delta,       |delta| <= 10^-15.             (6)

For EVERY such real delta, an exact solution exists in the same box. In
particular, this family actually contains the theta target, not just a
nearby attainable point with a target-directed derivative.

Indeed lower cumulants are fixed, so (6) changes only K_16 among the eight
target cumulants, by delta. Its normalized equation changes by delta/c_16.
The exact rational inverse calculation proves

    max_i |R_{i,8}| * 10^-15/|c_16| < 10^-15.              (7)

(The exact c_16 is -1903757312.) Combine (5),(7) with the same L. The new
self-map still has ample strict margin. The dependence on delta is analytic,
since the Jacobian remains invertible. This yields a small target-crossing
curve with the first seven even moments fixed. No global continuation from
the earlier 272-spin root is claimed: this new root is independently enclosed.

## 5. A connected finite extension, uniformly certified

For all 280 physical spins add a common coupling j to EVERY unordered pair,
retaining the original J_0 on the five designated pairs. Thus those five
couplings become J_0+j and all others become j. For j>0 there are exactly
280*279/2=39060 strictly positive pair couplings, all observable weights positive.
The main variance-carrying correlations remain the five fixed J_0 edges;
the additional couplings here are a conservative connecting device.

**D16-3.** For EVERY j in [0,10^-150] and EVERY delta in (6), there is exactly
one matching active weight vector in the same box. All first fourteen moments
remain the exact theta moments. At delta=0 the sixteenth is exact too.

Here is a complete finite-state estimate, avoiding a 2^280-state enumeration.
Let H(sigma)=sum_{a<b}sigma_a sigma_b. Throughout the parameter box,

    |Y|<280, |H|<40000, |partial_{x_i}Y|<10000.

The derivative bound follows from x_i,y_j>1/2000 and the stated multiplicities.
The Gibbs law for any real j is a finite positive probability distribution.
Differentiation gives, without changing its normalization convention,

    partial_j E_j Y^n = Cov_j(Y^n,H),
    |partial_j E_j Y^n| <= 80000*280^n,
    |partial_{x_i}partial_j E_j Y^n|
                             <=80000*n*10000*280^{n-1}.    (8)

The sum of the absolute coefficients of the cumulant polynomial of degree n
is at most C_n=n!*2^{n-1}. This follows directly by expanding log(1+u) and
counting ordered compositions of n. Product differentiation of its monomials
then bounds the corresponding first and mixed derivatives by

    C_n*80000*n*280^n,
    C_n*80000*n^2*10000*280^{n-1}.                         (9)

For every even n<=18 these integers are <10^80; the checker verifies each.
After division by c_n, |c_n|>=1 preserves this bound. Therefore both the
moment equations and each entry of their Jacobian differ from j=0 by at most
10^80*j. For the same R,

    beta_all <= beta + (target cost in (7)) + ||R||*10^80*j,
    L_all <= L + 8||R||*10^80*j.

The accepting calculation proves, uniformly on the full (j,delta) rectangle,

    10^-14 - beta_all - 10^-14*L_all > 9*10^-15,
    L_all < 1/100.                                       (10)

Contraction proves D16-3. The small j interval is a sufficient allowance,
not the maximal admissible coupling range or a statement that large positive
bridges can be introduced without changing the moments. Couplings are not
optimized or allowed negative values.

## 6. Nonnegligible interaction, exact zero geometry, and the next mismatch

For j=0 the variance carried by the five interacting components is

    (3/5) sum_{k=0}^4 y_k.

The same box proves it is between 0.191 and 0.192; the retained enclosure is
near 0.1911633930206. The total standardized variance is one. Thus the five
pairs carry approximately 19.1163 percent of it. For j>0 variance is not a sum
of independent-component variances, so that statement is NOT copied verbatim
to the connected model.

For the disconnected model the full characteristic function is explicit:

    chi_X(z) = product_{i=0}^5 cos(sqrt(v x_i) z)^{nu_i}
            * product_{j=0}^4 [2/5+(3/5)cos(sqrt(v y_j)z)]. (11)

Every zero in (11) is real. For a dimer factor this follows directly from
cos z=-2/3: if Im z!=0 the imaginary part forces sin(Re z)=0, and then
|cos z|=cosh(Im z)>1, a contradiction. The independent factors are cosines.
For the connected j>0 models, real zeros follow from the classical weighted
Lee--Yang theorem. Newman--Wu (2019), equation (21) and the following paragraph,
states that theorem for Jij>=0 and nonnegative observable weights. This is an
explicit imported theorem, not a claim about generic positive mixtures.

The realization is NOT theta. Since all lower cumulants through sixteen
agree at (j,delta)=(0,0), the normalized eighteenth-moment discrepancy is

    c_18 [sum_i nu_i x_i^9 + alpha_9 sum_j y_j^9 - s_9].   (12)

Full-box evaluation, including the complete theta source through degree
18, gives a strict enclosure inside

    (0.1695776569, 0.1695786421),

and in particular between 0.169 and 0.170. No model-zero or zeta-zero list is
used. Over the robust rectangle, changing K16 by delta changes the raw moment
18 by an additional binom(18,16)*delta, since K2=1 and the other lower even
cumulants are unchanged. The j change in K18 is bounded by 10^80*j. These
complete allowances still keep the discrepancy strictly in (0.169,0.170).
This last claim, too, is checked. No eighteenth-moment equality is inferred.

## 7. Relation to the whole programme and the exact open theorem

The result closes the next finite target, through sixteen, rather than
proving an arbitrary-order extension. The five-pair architecture is not
claimed to be an all-order model: the earlier bounded-lattice-component
obstruction would apply if one tried to finish by simply adding ever more
independent bounded-size components. Making the present graph connected by
j=10^-150 does not provide an unbounded-order graph construction.

The precise sufficient global task remains to construct finite ferromagnets
X_m with nonnegative couplings and weights, satisfying

    |E X_m^{2r}-mu_{2r}| <= 2^-m,  1<=r<=m,

for an unbounded sequence of m. Such a sequence would prove RH. For clarity,
the consumer is not an additional unknown norm assertion: each finite
Lee--Yang characteristic function has the even paired canonical product;
its exponential type excludes a quadratic exponential factor. The positive
MGF coefficients obey

    E X_m^{2r}/(2r)! <= (Var X_m/2)^r/r!.

The second moments would be bounded by the matching condition. This pays
all remaining complex Taylor tails uniformly on every disk, while each fixed
coefficient converges to the actual theta coefficient. The entire normalized
Xi is therefore the locally uniform limit. Hurwitz excludes nonreal zeros
because every approximant has only real zeros and the limit equals one at
zero. No simplicity premise is used.

The present finite box supplies no construction for unbounded m. Neither
parameter counting nor the small interval (6) implies that the eighteenth
theta target is reachable, and the retained mismatch proves that this box
does not reach it. The completion theorem of #880 can be applied CONDITIONALLY
at its proposed scope to give an infinite connected growth-calibrated version
of the new finite root. That optional application is not needed for D16-1--3
and is not another independent acceptance of #880.

## 8. Evidence and review boundary

The paper proves the source remainders, contraction implication, uniform
Gibbs bounds and global conditional consumer. The code reconstructs the
explicit numerical inequalities and finite rational controls. They are not
machine proofs of the paper's analytic arguments or of Lee--Yang.

Review priorities: the complete normalization; all 84 cells and three types
of tail; the active/fixed coordinate distinction; maximum-row-sum norms;
exact rather than rounded roots; the binomial term when delta!=0; and the
fact that (10) is a uniform finite-coupling existence theorem, not an
all-order reachability estimate. External novelty is not asserted.
