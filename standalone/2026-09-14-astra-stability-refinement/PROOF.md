# SR26: tunable stability and a source-qualified simple-zero improvement

**Status: PROPOSED component proofs and a source-qualified quantitative corollary,
pending independent mathematical review. Not an RH proof or a claim of a world
record.** Date: 2026-09-14. Base: main
`f99d9e3908dde4865377c75d9ca051c1f545bf4f`.

This is a change of objective from the preceding Möbius/trace programme: improve
an actual quantitative conclusion using a proved finite inequality, rather than
produce another equivalent condition for RH. The numerical gain is small and is
stated as such. No new covariance, Mertens, zero-free, or all-zero theorem is
claimed. All older packets and their unresolved premises remain unchanged.

## 0. Dependencies and the quantitative claim

Let N(T) count nontrivial zeta zeros with multiplicity in 0<Im(rho)<=T and let
S(T) count simple zeros on the critical line there. The proposed corollary is

    liminf S(T)/N(T) >= B_new > 0.67300966525.                 (0.1)

B_new is the exact expression in Section 6. Its derivation uses exactly:

* **P7:** the already certified seven-point Montgomery--Taylor pressure
  inequality in main `reviews/A/supplement/REPORT.md`, S01, with constants
  1/3000 and 19/5000. Its original source is
  `ainta/zeta-simple-zeros@040c5e899e658aed7b56a2a87f501798fe10761d`.
  This pass does NOT rerun either seven-point exhaustion.
* **PC:** the unconditional BGST pair-correlation theorem in the smooth,
  compact-support formulation stated in Section 5. This is an external
  analytic input, not proved by the new finite checker.
* Classical Riemann--von Mangoldt and conjugation/functional-equation symmetry.

The named inputs are not new RH-strength conjectures. Nonetheless, this packet
is not an independent re-verification of their original proofs or certificates.
The corollary is explicitly source-qualified to those inputs. Its new arguments
are supplied below, including removal of the pair weight and the smoothing
limit. No finite-dimensional Weil-frame approximation is assumed.

Credit: the c=2 stability-enhanced rank inequality and the seven-point lifting
strategy already occur in ainta's source. Main's S02 already improves the
269-point result to a 280-point bound. Lamzouri's Hilbert-space finite-multiset
framework and direct BGST transfer are also prior work. The present changes
are a free clipping threshold, an all-energy sharp spectral envelope, their
complete finite-multiset transfer, and a slightly better explicit constant.
No comprehensive novelty claim is made for the elementary matrix lemmas.

## 1. SR26-1: a free-threshold stability-enhanced rank--inertia inequality

For c>=1 and t>=0 put

    h_c(t) = t^2                    for 0<=t<=c,
             2ct-c^2                for t>=c;
    Psi_c(t) = h_c(t)-2t+1
             = (t-1)^2-(t-c)_+^2.                          (1.1)

Psi_c is convex, nonnegative, and Psi_c(1)=0. At c=2 this is the existing
piecewise quadratic/linear defect, not a different normalization.

Let V have r columns of norm at most one, P=VV*, M=V*V, and let Q be Hermitian
with at most b positive eigenvalues. Every matrix is finite. Then

    ||P+Q||_F^2 >= 2c tr(P+Q) -(2c-1)r-c^2 b+tr Psi_c(M). (1.2)

Proof. Write Q=Q_+-Q_- with orthogonal positive/negative parts. Then

    ||P+Q||_F^2 = ||P-Q_-||_F^2+||Q_+||_F^2+2tr(PQ_+).

The last term is nonnegative. Also ||Q_+||_F^2>=2c tr Q_+-c^2b, by summing
(x-c)^2>=0 over its at most b positive eigenvalues. Von Neumann's trace
inequality applied to P and Q_- gives, with p_i the eigenvalues of P,

    ||P-Q_-||_F^2+2c tr Q_- >= sum_i h_c(p_i),              (1.3)

because min_{n>=0}[(p-n)^2+2cn]=h_c(p); the minimizer is (p-c)_+.
The nonzero spectra of P and M agree and h_c(0)=0. Thus

    sum_i h_c(p_i)=2tr P-r+tr Psi_c(M).

Combine this with (1.3) and tr P<=r. The coefficient 2-2c is nonpositive,
which explains the stated c>=1 restriction. This proves (1.2).
No positivity of Q or commutation with P is required.

## 2. SR26-2: a sharp defect bound at every admissible variance

For an m-by-m PSD matrix G of trace m, m>=2, write

    E=tr(G-I)^2,   0<=E<=m(m-1),
    Phi_(m,c)(E)=E-(sqrt((m-1)E/m)-(c-1))_+^2.              (2.1)

Then, for every c>=1,

    tr Psi_c(G) >= Phi_(m,c)(E).                           (2.2)

The bound is SHARP for every E in the stated range, including E>=2.
It is stronger in scope than the earlier low-energy envelope in main S02.

Proof. Let x_i=lambda_i(G)-1, so x_i>=-1, sum x_i=0 and sum x_i^2=E.
Put b=c-1>=0. If every x_i<=b, the defect is E and the assertion is immediate.
Otherwise let I={i:x_i>b}, k=|I|, and write x_i=b+u_i for i in I, with
u_i>0. Necessarily 1<=k<m. Set s=sum_I u_i and t^2=sum_I u_i^2. Then s>=t.
Cauchy on the complementary coordinates gives

    E >= kb^2+2bs+t^2+(kb+s)^2/(m-k)
      >= b^2+2bt+t^2+(b+t)^2/(m-1)
       = m(b+t)^2/(m-1).                                 (2.3)

Here each replacement uses b>=0, s>=t and k>=1. It follows that
sum_i(x_i-b)_+^2=t^2 <= (sqrt((m-1)E/m)-b)^2. Subtracting from E proves
(2.2). The case with no active coordinate obeys the positive-part version.

For sharpness, put u=sqrt((m-1)E/m) and take the eigenvalues

    1+u,  1-u/(m-1), ..., 1-u/(m-1).                       (2.4)

They are nonnegative exactly over the claimed E range, and attain (2.2).
They can even be realized by a UNIT-DIAGONAL Gram matrix:

    G=(1-u/(m-1))I+(u/(m-1)) 11*.

Thus a better universal estimate based only on m, trace, and E is impossible.
A better bound for the specific translation kernel would require further
geometric information, not another relaxation using only those same data.

Phi is increasing and 1-Lipschitz on [0,m(m-1)]. Below its clipping threshold
its derivative is one; above the threshold it is
1/m+(c-1)sqrt((m-1)/m)/sqrt(E), between 1/m and one. Hence if z>=0 and
E+z>=q with 0<=q<=m(m-1),

    tr Psi_c(G)+z >= Phi_(m,c)(q).                         (2.5)

This follows by monotonicity when E>=q, and by the 1-Lipschitz property when
E<q. It avoids any extrapolation of an E<2 formula to larger energies.

## 3. SR26-3: retain stability in Lamzouri's exact finite-multiset setting

Let g be a real, nonnegative, even, compactly supported L1/L2 density of mass
one on the real line, and k(z)=integral g(t)exp(-2pi i zt)dt. Let Z be a finite
conjugation-invariant set of complex points, with positive integer
multiplicities mu_z preserved by conjugation.

Write N=sum mu_z, S=number of real points of multiplicity one, and let b be
(number of distinct multiple real points)+(number of nonreal conjugate pairs).
Define J=N-S-2b>=0, and let M be the Gram matrix of the S unit vectors

    v_x(t)=sqrt(g(t)) exp(2pi i xt), x real and simple.

Thus M has diagonal one and entries k(x-y), up to harmless transpose. Set

    E_Z=sum_(z,w in Z) mu_z mu_w k(z-w)^2,
    a_c=2c-c^2/2.

Then E_Z is real and nonnegative, and

    E_Z >= a_c N-(a_c-1)S+tr Psi_c(M)+(c^2/2)J.            (3.1)

Proof. On the finite span of all v_z and v_conj(z) form the operator

    A=sum_z mu_z |v_z><v_conj(z)|.

Conjugation invariance makes A selfadjoint. Its trace is N because
<v_conj(z),v_z>=integral g=1. The rank-one product trace and evenness of g
give tr A^2=E_Z exactly. This is k(z-w)^2, not |k(z-w)|^2.

Separate the simple real vectors as P=VV*. A multiple real point contributes
one positive rank-one summand to Q=A-P. A nonreal pair contributes

    mu_z (|v_z><v_conj(z)|+|v_conj(z)><v_z|)
     =(mu_z/2)(|v_z+v_conj(z)><v_z+v_conj(z)|
                -|v_z-v_conj(z)><v_z-v_conj(z)|).

Its positive index is at most one, including degenerate cases. The positive
index of a sum is at most the sum of the positive indices; intersect the
nonpositive subspaces to see this directly. Thus n_+(Q)<=b. Apply (1.2)
with r=S and tr A=N. Substituting b=(N-S-J)/2 gives (3.1).

At c=2 and after dropping the nonnegative 2J, (3.1) is precisely the
stability improvement of the finite-multiset simple-real count:

    S >= 2N-E_Z+tr Psi_2(M).

This is a direct operator proof. It does not assume individual nonreal pair
terms are positive, nor does it identify a PSD model with the actual zeta
source. The multiplicity surplus J is retained in (3.1), but we do not assert
that it is positive for a positive proportion of actual zeros.

## 4. SR26-4: use the existing seven-point certificate without changing it

Put

    g_0(t)=cos(sqrt(2)t)/K_0 for |t|<=1/2, zero otherwise,
    K_0=sqrt(2)sin(1/sqrt(2)),
    k_0(x)=integral g_0(t)exp(-2pi i xt)dt,
    w_0(x)=k_0(x)^2.

The imported P7 theorem says for all six nonnegative gaps

    (sum_i gap_i)/3000
     +sum_(s=1)^6 [2/(7-s)] sum_(i=1)^(7-s)
           w_0(gap_i+...+gap_(i+s-1)) >= 19/5000.          (4.1)

For m>=7 ordered real points y_1,...,y_m, summing over all consecutive
seven-point windows gives

    E_m+(y_m-y_1)/500 >= q_m,
    E_m=2sum_(i<j)w_0(y_i-y_j), q_m=19(m-6)/5000.         (4.2)

Each pair of index separation s<=6 occurs at most 7-s times and each gap
at most six times; omitted pair terms are nonnegative. The Gram matrix has
trace m and E_m=tr(G-I)^2. Set d_(m,c)=Phi_(m,c)(q_m). Equation (2.5) yields

    tr Psi_c(G)+(y_m-y_1)/500 >= d_(m,c).                 (4.3)

For an arbitrary finite ordered real set of size S and span L, its full Gram
M therefore obeys

    tr Psi_c(M) >= d_(m,c) S/m
                    -(m-1)L/(500m)-(m-1)d_(m,c)/m.       (4.4)

Proof of the full block accounting. Partition consecutive points into
m-point blocks at each of the m possible index offsets. Convex trace
pinching bounds the full defect below by the sum of defects of those
principal blocks; leftover singleton defects are zero. Convex trace
pinching itself follows by diagonalizing the blocks and applying scalar
Jensen to the doubly stochastic squared-unitary matrix of eigenvectors.
Each possible complete m-point window occurs once over all offsets, so
there are S-m+1 such windows when S>=m. Each gap occurs in at most m-1 of
their spans. Divide the resulting sum by m. When S<m the right-hand side
of (4.4) is nonpositive and the inequality remains valid. This proves the
finite endpoint constant, not only an asymptotic version.

### A smooth window does not lose the pressure

Let g_e be even nonnegative smooth probability densities supported strictly
inside (-1/2,1/2), converging to g_0 in L1 and L2. Such a family follows by
cutoff and convolution followed by normalization. Write epsilon=||g_e-g_0||_1.
Their Fourier transforms satisfy |k_e-k_0|<=epsilon and |k_e|,|k_0|<=1 on
the real axis. Hence |k_e^2-k_0^2|<=2epsilon there. The total pair-coefficient
weight in (4.1) is 12, so all the preceding inequalities hold with

    q_(m,e)=(m-6)(19/5000-24epsilon),
    d_(m,c,e)=Phi_(m,c)(q_(m,e)),                           (4.5)

for epsilon sufficiently small. This is uniform on ALL real separations.
No uniform estimate of k_e at unbounded complex arguments is needed below.

## 5. SR26-5: complete pair-correlation transfer, with the rational weight removed

Here is the exact external PC input. For a fixed smooth even function f
supported inside (-1,1), put L_T=log T, R_T=T log T/(2pi),
xi_(rho,rho')=i(rho-rho')L_T/(2pi). Then

    (1/R_T) sum_(rho,rho') m_rho m_rho'
        fhat(xi_(rho,rho')) 4/[4-(rho-rho')^2]
      -> f(0)+2 integral_0^1 u f(u)du.                    (5.1)

The sum includes all nontrivial zeros with 0<Im rho<=T and their
multiplicities. This smooth special case of BGST is also the pair-correlation
input in the inspected AxiomMath/Lamzouri interface. The original analytic
proof is imported, not replaced by a finite code check. Its pair theorem is
unconditional; the thin-box assumption in BGST's separate simple-zero
application is NOT assumed here. Riemann--von Mangoldt gives N(T)/R_T->1.

Fix a smooth g_e from Section 4 and let f=g_e*g_e, so fhat=k_e^2.
Both f and f'' are fixed admissible smooth tests in (5.1). Integration by
parts gives

    Fourier(f'')(xi)=-4pi^2 xi^2 fhat(xi)
        =(rho-rho')^2 L_T^2 fhat(xi)

at the displayed scaled argument. Consequently the EXACT identity

    unweighted_sum(k_e^2)
      = weighted_sum(f)-weighted_sum(f'')/(4L_T^2)        (5.2)

holds. There is no pole in the rational pair weight for these zero
differences, since their real-part difference has magnitude less than one.
Apply (5.1) separately to the two fixed tests, rather than asserting a
uniform theorem for a T-dependent family. Equations (5.1)-(5.2) give

    E_e(T)/N(T) -> kappa_e
       := integral g_e^2 + double integral |x-y|g_e(x)g_e(y)dxdy. (5.3)

The first term is f(0); the second is integral |u|f(u)du by evenness.

Map each zero to z_rho=i(rho-1/2)L_T/(2pi). Functional-equation reflection
rho -> 1-conj(rho) makes this multiset conjugation-invariant and preserves
multiplicity. Real points are exactly critical-line zeros. Its simple real
points span an interval of length at most R_T. The diagonal of their Gram
matrix is EXACTLY one at every T; no grid normalization limit is used.

Apply (3.1), drop J>=0, and then apply (4.4)-(4.5). If

    a_c-1-d_(m,c,e)/m >0,

we obtain

    liminf S(T)/N(T)
      >= [a_c-kappa_e-(m-1)/(500m)]
                           /[a_c-1-d_(m,c,e)/m].           (5.4)

All finite endpoint costs in (4.4) vanish after division by N(T). The span
cost is bounded using R_T/N(T)->1. We first let T tend to infinity at FIXED
e, then let e decrease; no unproved interchange of varying test functions
and growing height occurs.

### Evaluation of the limiting pair energy

Let J(x)=integral |x-y|g_0(y)dy for |x|<1/2. Then J''=2g_0 and
 g_0''=-2g_0, so g_0+J is an even affine function and is constant.
At x=1/2, J(1/2)=1/2 because g_0 has mass one and mean zero. Therefore

    kappa_0 = 1/2+(1/sqrt(2))cot(1/sqrt(2)).               (5.5)

Indeed multiplying the constant identity by g_0 and integrating gives
exactly the two terms in (5.3). L2 convergence proves convergence of the
first term and L1 convergence on the fixed compact support proves that
of the double integral. Thus kappa_e->kappa_0.

Combining (5.4)-(5.5) proves a source-qualified bound for every admissible
m,c:

    B_(m,c) =
      [H_0-(c-2)^2/2-(m-1)/(500m)]
         /[1-(c-2)^2/2-Phi_(m,c)(q_m)/m],                 (5.6)
    H_0=3/2-(1/sqrt(2))cot(1/sqrt(2)),

provided the denominator is positive. This is an actual numerical density
conclusion from P7, PC and the classical symmetry/counting inputs, not a
conditional RH completion with another RH-equivalent upper estimate missing.

## 6. SR26-6: a strict, small quantitative gain

Choose ONCE, independently of zeros or height,

    m=281, c=400059/200000,
    q_m=209/200,
    d=209/200-(sqrt(1463/1405)-200059/200000)^2,
    e=3481/80000000000.

The clipping term is strictly active. The exact proposed constant is

    B_new = [H_0-e-14/7025]/[1-e-d/281].                  (6.1)

The Fraction-only interval calculation certifies

    0.673009665251783092 < B_new < 0.673009665251783093,
    B_new > 0.67300966525.                                (6.2)

The old m=280,c=2 constant from main S02 satisfies

    0.673009652279136912 < B_old < 0.673009652279136913.

The difference is rigorously between

    0.000000012972646180 and 0.000000012972646181.           (6.3)

It is approximately 1.30e-8 in proportion, or 1.30e-6 PERCENTAGE POINTS.
This is a tiny improvement, not an approach to 100 percent. The comparison
is with the repository's pinned source-qualified 280-block expression;
this packet does not establish a current world-record claim.

For reproducibility the new scalar enclosure uses no floating trigonometry:
with y=1/sqrt(2),

    H_0=3/2-cos(y)/(sin(y)/y).

Both series have rational alternating terms in y^2=1/2. Forty-eight terms
and the next-term remainder bound enclose them. Integer square roots give
a 220-bit outward enclosure of sqrt(1463/1405). The denominator is proved
positive before division. `results.json` retains outward rational endpoints.
A binary64 search suggested the rational c; its numerical optimizer and
optimality are NOT premises. We claim no global optimization over m,c.

## 7. What changed, what remains, and useful next work

This closes no RH route. The older polynomial/covariance, gamma, Ising,
branching and Hardy-domain obligations remain precisely where they were.
The user's critique correctly identifies a repeated failure to turn exact
reformulations into a new arithmetic upper bound. This packet deliberately
claims only a quantitative simple-zero refinement and its matrix tools.

At fixed m and E the new defect envelope is already sharp. Substantial further
gain therefore requires information about the actual translation Gram matrix
beyond trace and variance, or a stronger geometric pressure estimate. Useful
next targets include a certified joint bound involving a third spectral moment,
a sharper seven-point pressure, or a pressure assembled from longer distances.
None of those improvements is assumed here. Changing the test window requires
paying BOTH its pair-energy cost and its geometric pressure; the classical
scalar Montgomery--Taylor extremum is not contradicted by retaining this
additional stability information.

A positive density of simple central zeros does not exclude a finite or
zero-density exceptional set. Even an eventual density-one result alone would
not prove RH. No such conclusion, new numerical zero census, independent
referee acceptance or formal proof is claimed.
