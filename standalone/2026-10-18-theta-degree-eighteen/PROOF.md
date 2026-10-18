# A connected ferromagnetic realization through theta degree 18

Status: PROPOSED finite theorem with a complete directed-arithmetic existence certificate. Independent mathematical review is required. No RH theorem, degree-20 realization, cofinal construction, or new zero-free half-plane is claimed. The source is the original theta density, not fitted moments or a finite zero census. The classical Lee–Yang theorem and elementary complex analysis are imported explicitly.

## 1. Exact statement

Put q_n=pi*n^2 and, for t>=0,

    Phi(t)=sum_{n>=1}(4 q_n^2 exp(9t/2)-6 q_n exp(5t/2)) exp(-q_n exp(2t)).

Extend Phi evenly. Each summand is positive for t>=0 since 2q_n exp(2t)>3. Its decay gives every exponential moment. Let T have density Phi/integral(Phi), v=E T^2, and T*=T/sqrt(v). The classical theta Fourier identity identifies E exp(izT) with xi(1/2+iz)/xi(1/2). Normalization removes the irrelevant overall factor in the unnormalized integral.

**Theorem A (finite realization).** There is a zero-field Ising model on a connected tree with 282 vertices and 281 strictly ferromagnetic edges, and a real observable Y with positive weights on all vertices except one zero-weight hub, such that

    E Y^(2r) = E (T*)^(2r), 1<=r<=9.

Every edge coupling J satisfies 1/200000<J<2. All odd moments vanish. Its characteristic function has only real zeros. In particular its full entire function, not merely its Taylor polynomial, agrees with the standardized theta characteristic function through degree 18. It is not asserted to equal the theta function away from those coefficients.

The theorem is an existence statement for the unique solution in an explicitly specified nine-dimensional box. The finite decimal centers are NOT themselves represented as exact solutions. All parameters not varied in that box are fixed rational numbers from parameters.json.

**Relation to #974.** At frozen source 89c37b6707cb77fc5a86143ea98d8756759fdcbc, the connected 281-spin tree matches through degree 16 and has a strictly positive standardized raw degree-18 discrepancy in (0.034,0.035). The present model adds one spin by replacing its largest single-spin component by a dimer. Several other parameters are retuned. The coupling upper bound is relaxed from 1/4 to 2; positivity, finiteness and connectedness are preserved. No certified path between the old and new parameter boxes is claimed or needed for the new existence certificate.

## 2. The entire finite graph and its normalized law

The parameters are z=(a_0,...,a_10,eta,p_0,...,p_4,p_new). The multiplicities of the eleven component types are

    nu=(256,10,1,1,1,1,1,1,1,1,1).

Types 0 through 4 are single spins. Type 5, previously one single spin, is now a two-spin dimer with alignment probability p_new. Types 6 through 10 are dimers with alignment probabilities p_0 through p_4. Thus there are 269 single spins, twelve spins in six dimers, and one hub: 282 vertices in total.

Set k_i=1/100 except k_6=k_7=3 and m_i=eta*k_i*a_i. Join the hub to the root of each component with coupling atanh(m_i). In a dimer of alignment probability p, join its two spins with coupling atanh(2p-1). These are all the edges: 275 hub edges and six dimer edges. The Gibbs density is proportional to exp(sum_edges J_e sigma_v sigma_w), with NO external field. The hub marginal is fair by spin-flip symmetry.

Conditional on hub value h, the root spin sigma of component i has probability (1+h*m_i*sigma)/2. In a dimer, its child tau conditional on sigma has probability (1+(2p-1)*sigma*tau)/2. Summing over the child is independent of the root; hence the root probabilities and conditional independence of ALL components are exact. Multiplicities count distinct spins, not an approximation by a Gaussian block.

The observable of a single spin of type i is a_i sigma. The observable of a dimer is a_i(sigma+tau)/2. The hub observable weight is zero. Conditional on h=+1, the normalized component moment generating functions are

    single: cosh(a_i t)+m_i sinh(a_i t),
    dimer: 1-p+p cosh(a_i t)+p*m_i sinh(a_i t).

Thus for every positive integer j a component has conditional moment

    a_i^j q_i                 for j even,
    a_i^j q_i m_i             for j odd,

where q_i=1 for i<5, q_5=p_new, and q_i=p_(i-6) for i>=6. Multiply these eleven generating functions to their full multiplicities. Averaging hub signs discards odd coefficients and retains even coefficients. This proves the complete finite moment formula implemented by model.py, without enumerating 2^282 configurations or discarding any of them.

## 3. Nine polynomial equations and the certificate

Let c_(2r) be the cumulants of one fair +/-1 sign. These nonzero integers are reconstructed from its exact moments by

    kappa_n = mu_n - sum_{j=1}^{n-1} binom(n-1,j-1) kappa_j mu_(n-j).

Set s_r=kappa_(2r)(T*)/c_(2r). The polynomial map A_r(z)=kappa_(2r)(Y)/c_(2r) is computed by finite formal series through degree 18. All divisions are by fixed nonzero integers. In particular it is a genuine polynomial with rational coefficients, not a numerical evaluation of a partition function.

The active parameter indices are

    (0,1,2,3,4,5,6,8,17).

All remaining coordinates are fixed at their rational centers. Each active coordinate ranges over its center plus or minus rho=10^-30. Let z_0 denote these centers, let J be the 9-by-9 derivative of A in the active coordinates, and let R be the rational matrix in parameters.json. R was chosen by numerical exploration, but it is not assumed to be an exact inverse. Its efficacy is verified using only rational interval arithmetic.

certify.py reconstructs the full source intervals S_r, then checks on the COMPLETE active box:

    beta = ||R(A(z_0)-s)||_infinity < rho/1000,
    L    = sup_box ||I-R J||_infinity < 1/1000,
    rho-beta-L*rho > (99/100)rho.

Every exact source value s lies in the reconstructed S_r; the bounds cover the entire source intervals, not just their midpoints. The actual reported bounds are approximately beta<=8.404e-41 and L<=7.131e-12, but these decimal displays play no role in acceptance. CERTIFICATE.json records outward integer numerators and the common denominator 2^320.

For each fixed actual source s, the map x -> x-R(A(x)-s) is a strict contraction sending the closed active box to its interior. Banach's fixed-point theorem gives a unique fixed point there. The inequality ||I-RJ||<1 also makes RJ invertible at the center, hence the square matrix R is invertible. A fixed point therefore solves A(x)=s, not just R(A(x)-s)=0. This supplies all nine exact even cumulants. The triangular moment/cumulant identities supply the nine exact even moments. Symmetry supplies the odd moments.

The certificate additionally checks strict positivity of amplitudes and eta, 1/2<p_i<1, and 0<m_i<1 throughout the box. For every edge-bias h it verifies

    h>1/200000,       h/(1-h^2)<2.

Since h<=atanh(h)<=h/(1-h^2) for 0<h<1, the asserted edge bounds follow. The count of vertices and edges is checked exactly. No optimizer or floating-point computation is used by this existence test.

The active Jacobian is invertible, so the target vector is an interior point of the realizable nine-moment region for this architecture, rather than a singular boundary fit. This local statement does not provide a degree-20 extension or an unbounded sequence of realizations.

## 4. Directed reconstruction of the infinite theta source

The source calculation is adapted explicitly from #974 theta_source.py and the #886 primitive backend copied there. It is not a newly independent transcendental implementation. Its analytic bounds are repeated here so that a stored source receipt is not an assumption.

For n=1,...,6 integrate from zero to U_n=(2,3/2,1,3/4,1/2,3/8) on cells of width 1/16, for a total of 98 cells. Use midpoint Taylor polynomials of degree 120, with scaled cell coordinate h=1/32. The coefficient recurrence for exp(g) is

    e_0=exp(g_0),   e_j=(1/j)sum_(k=1)^j k*g_k*e_(j-k).

The two prefactor exponentials are expanded and multiplied before exact polynomial integration against t^j, j=0,2,...,18.

### Taylor error

On a complex circle of radius 1/8 around any such midpoint, Re t<=17/8, |Im t|<=1/8, and Re(exp(2t))>0. Hence |exp(-q_n exp(2t))|<=1. Using 3<pi<4, n<=6, and e<3 bounds the absolute density summand on the circle by 10^11. Cauchy's estimate, with half-cell/radius=1/4, bounds its Taylor tail on the real cell by 10^11*4^-121/(1-1/4). The sum of full-line integration lengths is less than 16 and t^j<=2^j. A valid total two-sided error is therefore

    E_j = 16*10^11*2^j / [4^121*(3/4)].

This is a bound for the analytic remainder, not the last numerically observed Taylor coefficient.

### All time and theta-index tails

For t=U+u, q=pi*n^2, E=exp(2U), and lambda=2qE-9/2>0, positivity and exp(2u)>=1+2u give the complete full-line upper tail

    8q^2 exp(9U/2-qE)
       * sum_(k=0)^j binom(j,k) U^(j-k) k!/lambda^(k+1).

All six time tails are included. For n>=7 the corresponding U=0 numerator ratio is at most (8/7)^4 exp(-15pi)<1/2 and its denominator increases. Thus ALL omitted indices have total upper bound

    16*pi^2*7^4*exp(-49pi)*j!/(98pi-9/2)^(j+1).

The Taylor error is added both ways; positive time/index tails are added to the upper endpoint only. Divide outward by the positive total mass, and then by the outward variance powers. Apply the exact cumulant recurrence and fair-sign divisors outward. This constructs enclosures for the actual standardized s_1,...,s_9.

### Arithmetic implementation

All endpoints are integers divided by 2^320. Rational inputs are rounded outward. Products and reciprocal products use integer floor/ceiling. Pi uses Machin's identity with 96 alternating arctangent terms and the first omitted term. For exp, a nonnegative argument is reduced to [0,1/8], 96 positive Taylor terms are summed, and the tail beginning at term 97 is bounded by its geometric majorant; repeated squaring is outward. Negative arguments use an outward reciprocal. These routines accept no floating-point inputs.

Automatic differentiation of the finite polynomial uses the same outward operations. The certificate reconstructs the source each time by default. The --source option is solely an explicitly trusted development shortcut; the recorded ordinary and optimized final runs do NOT use it.

## 5. Real zeros of the entire model

The finite ferromagnetic Lee–Yang theorem states that, at zero field and with nonnegative observable weights, the moment generating function has only purely imaginary zeros. Equivalently the characteristic function has only real zeros. Unequal irrational positive weights are allowed. This statement is explicit in Newman--Wu, *Lee--Yang Property and Gaussian Multiplicative Chaos*, CMP 369 (2019), Section 1; the underlying theorem is Lee--Yang (1952).

Even a strictly-positive-weight version suffices. Give the hub weight delta>0, apply the theorem, and let delta decrease to zero. The finite configuration sums converge uniformly on compact sets. Their limit has value one at zero and is not identically zero. Hurwitz applied on the two non-real half-planes preserves zero-freeness. The hub is retained in the graph and in the Gibbs law; it is not deleted as an independent spin.

Rescaling Y by sqrt(v)>0 preserves real zeros and matches the unstandardized theta moments through degree 18. This proves Theorem A.

## 6. Why this is not RH

A fixed finite number of Taylor coefficients cannot determine an entire function's global zeros. The actual result closes the particular degree-18 realization left open by #974; it does not establish an arbitrary-degree extension.

COFINAL_COMPACTNESS.md records a classical, quantitatively useful simplification: variance-normalized finite Lee--Yang laws automatically have a common Gaussian entire-function bound. Therefore a cofinal sequence of exact moment realizations would converge locally uniformly to the theta transform without a SEPARATE growing-graph/constant estimate. The cofinal existence premise is still unproved. Classical compactness is credited, not presented as a new RH proof.

## 7. Exploration and independent-check boundaries

The search first tried a direct Newton step from the degree-16 solution. It failed because lower-moment curvature made its residual merit test overly restrictive. Fixed-coordinate continuation reduced the raw degree-18 excess but approached a nearly singular parameterization. Allowing additional amplitudes/probabilities to move, then freezing nine active coordinates at the final solution, found an interior degree-18 root. Neither unsuccessful search is a mathematical obstruction; neither the search path nor its small floating residual is used by the certificate.

controls.py independently enumerates every state of a seven-spin restriction and compares all moments through degree 18 with the factorized law. It also checks outward arithmetic and rejects four altered parameter/preconditioner cases in both execution modes. This is an independent finite assembly, not an independent arithmetic backend or mathematical referee. The full 282-spin measure is handled by exact conditional factorization, not claimed to have been directly enumerated. No upstream theorem reconstruction, Lean build or whole-repository CI run is claimed.
